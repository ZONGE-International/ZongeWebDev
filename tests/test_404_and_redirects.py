"""Production build checks. Run with: python3 -m unittest discover -s tests -v"""

import csv
import http.server
from html.parser import HTMLParser
from pathlib import Path
import socketserver
import subprocess
import tempfile
import threading
import unittest
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://www.zonge.com/"
MAIN_GA_ID = "G-B7SVCQZ8GK"
OLD_PREFIXES = ("/geophysical-methods/", "/instruments-home/")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []
        self.robots = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("a", "link", "img", "script"):
            value = attrs.get("href") or attrs.get("src")
            if value:
                self.links.append(value)
        if tag == "script":
            self.scripts.append(attrs.get("src", ""))
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots.append(attrs.get("content"))


class PagesHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def do_GET(self):
        path = urlsplit(self.path).path
        candidate = (Path(self.directory) / path.lstrip("/")).resolve()
        if not candidate.is_relative_to(Path(self.directory).resolve()):
            self.send_error(404)
            return
        if not candidate.exists():
            body = (Path(self.directory) / "404.html").read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


class SiteChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.site = Path(cls.tmp.name) / "public"
        subprocess.run(
            ["hugo", "--environment", "production", "--minify",
             "--baseURL", BASE, "--destination", str(cls.site)],
            cwd=ROOT, check=True, capture_output=True, text=True,
        )
        handler = lambda *args, **kwargs: PagesHandler(*args, directory=str(cls.site), **kwargs)
        cls.server = socketserver.TCPServer(("127.0.0.1", 0), handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.local = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.tmp.cleanup()

    def fetch(self, path):
        from urllib.error import HTTPError
        try:
            with urlopen(self.local + path) as response:
                return response.status, response.read().decode("utf-8", errors="replace")
        except HTTPError as error:
            with error:
                return error.code, error.read().decode("utf-8", errors="replace")

    def test_http_status_and_analytics(self):
        status, home = self.fetch("/")
        self.assertEqual(status, 200)
        self.assertIn(MAIN_GA_ID, home)
        status, missing = self.fetch("/missing/a/b/random-no-such-page/")
        self.assertEqual(status, 404)
        self.assertNotIn(MAIN_GA_ID, missing)
        self.assertNotIn("googletagmanager.com/gtag/js", missing)
        self.assertNotIn("conversion-tracking.js", missing)
        parsed = Links()
        parsed.feed(missing)
        self.assertIn("noindex,follow", parsed.robots)

    def test_dedicated_404_analytics_is_opt_in(self):
        original = (ROOT / "hugo.toml").read_text()
        for measurement_id, expected in (("G-ONLY404TEST", True), (MAIN_GA_ID, False)):
            with self.subTest(measurement_id=measurement_id), tempfile.TemporaryDirectory() as folder:
                config = Path(folder) / "hugo.toml"
                config.write_text(original.replace(
                    '# analytics404ID = "G-EXAMPLE404"',
                    f'analytics404ID = "{measurement_id}"',
                ))
                output = Path(folder) / "public"
                subprocess.run(
                    ["hugo", "--config", str(config), "--environment", "production",
                     "--baseURL", BASE, "--destination", str(output)],
                    cwd=ROOT, check=True, capture_output=True, text=True,
                )
                html = (output / "404.html").read_text()
                self.assertEqual("googletagmanager.com/gtag/js" in html, expected)
                self.assertEqual("404_view" in html, expected)
                if expected:
                    self.assertNotIn(MAIN_GA_ID, html)

    def test_deep_404_links(self):
        status, html = self.fetch("/missing/a/b/random-no-such-page/")
        self.assertEqual(status, 404)
        parsed = Links()
        parsed.feed(html)
        local_paths = []
        for link in parsed.links:
            self.assertFalse(link.startswith(("./", "../")), link)
            if link.startswith("#"):
                continue
            resolved = urlsplit(urljoin("https://www.zonge.com/missing/a/b/", link))
            if resolved.netloc != "www.zonge.com":
                continue
            local_paths.append(resolved.path)
            self.assertEqual(self.fetch(resolved.path)[0], 200, link)
        self.assertIn("/", local_paths)
        self.assertIn("/contact/", local_paths)
        self.assertEqual(self.fetch("/contact/")[0], 200)

    def test_redirect_manifest(self):
        with (ROOT / "redirects/legacy.csv").open(newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertTrue(rows)
        sources = {row["source_path"] for row in rows}
        self.assertEqual(len(rows), len(sources))
        for row in rows:
            source = row["source_path"]
            target = urlsplit(row["destination"])
            self.assertTrue(source.startswith(OLD_PREFIXES), source)
            self.assertEqual(row["status"], "301")
            self.assertEqual(target.scheme, "https")
            self.assertIn(target.netloc, ("www.zonge.com", "legacy.zonge.com"))
            self.assertNotEqual(source, target.path if target.netloc == "www.zonge.com" else "")
            self.assertFalse(target.query or target.fragment)
            if target.netloc == "www.zonge.com":
                self.assertEqual(self.fetch(target.path)[0], 200, row["destination"])
                self.assertNotIn(target.path, sources, "redirect chain")
            else:
                # The original legacy path is the destination, avoiding invented slugs.
                self.assertEqual(target.path, source)

    def test_edge_exports(self):
        cloudflare = subprocess.run(
            ["python3", "scripts/export_edge_redirects.py", "cloudflare"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        entries = list(csv.reader(cloudflare.splitlines()))
        with (ROOT / "redirects/legacy.csv").open(newline="") as source:
            count = sum(1 for _ in csv.DictReader(source))
        self.assertEqual(len(entries), count)
        self.assertTrue(all(len(entry) == 7 and entry[2:] ==
                            ["301", "FALSE", "FALSE", "FALSE", "FALSE"] for entry in entries))
        netlify = subprocess.run(
            ["python3", "scripts/export_edge_redirects.py", "netlify"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        self.assertEqual(len(netlify.splitlines()), count)

    def test_robots_and_sitemap(self):
        status, robots = self.fetch("/robots.txt")
        self.assertEqual(status, 200)
        self.assertIn("Sitemap: https://www.zonge.com/sitemap.xml", robots)
        status, sitemap = self.fetch("/sitemap.xml")
        self.assertEqual(status, 200)
        root = ET.fromstring(sitemap)
        urls = [node.text for node in root.iter() if node.tag.endswith("}loc")]
        self.assertTrue(urls)
        self.assertTrue(all(url.startswith(BASE) for url in urls))
        self.assertFalse(any(any(prefix in url for prefix in OLD_PREFIXES) for url in urls))


if __name__ == "__main__":
    unittest.main()
