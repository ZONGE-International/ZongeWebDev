"""Check manifest destinations, and optionally deployed source 301s.

Run: python3 scripts/verify_redirects_live.py [--sources]
"""

import argparse
import csv
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen
from urllib.parse import urlsplit
from xml.etree import ElementTree


BASE = "https://www.zonge.com"
MANIFEST = Path(__file__).resolve().parents[1] / "redirects/legacy.csv"


class TracingRedirects(HTTPRedirectHandler):
    def __init__(self):
        self.hops = []

    def redirect_request(self, request, fp, code, msg, headers, newurl):
        self.hops.append((code, newurl))
        if newurl in (request.full_url, *(url for _, url in self.hops[:-1])):
            raise RuntimeError(f"redirect loop at {newurl}")
        if len(self.hops) > 10:
            raise RuntimeError("more than 10 redirects")
        return super().redirect_request(request, fp, code, msg, headers, newurl)


def inspect(url):
    tracer = TracingRedirects()
    opener = build_opener(tracer)
    request = Request(url, headers={"User-Agent": "Zonge-redirect-check/1.0"})
    with opener.open(request, timeout=20) as response:
        response.read(1)
        return response.status, response.url, tracer.hops


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", action="store_true", help="also require live source URLs to return a direct HTTP 301")
    args = parser.parse_args()
    failures = []
    with MANIFEST.open(newline="") as source:
        rows = list(csv.DictReader(source))
    with urlopen("https://legacy.zonge.com/page-sitemap.xml", timeout=20) as response:
        sitemap = ElementTree.fromstring(response.read())
    inventory = {
        urlsplit(node.text).path
        for node in sitemap.iter()
        if node.tag.endswith("}loc") and (node.text or "").startswith(
            ("https://legacy.zonge.com/geophysical-methods/",
             "https://legacy.zonge.com/instruments-home/")
        )
    }
    mapped = {row["source_path"] for row in rows}
    for path in sorted(inventory - mapped):
        failures.append(f"missing legacy sitemap URL: {path}")
    for row in rows:
        source_url = BASE + row["source_path"]
        destination = row["destination"]
        try:
            status, final, hops = inspect(destination)
            if status != 200 or hops:
                failures.append(f"{destination}: expected direct 200, got {status} via {hops}, final {final}")
            if args.sources:
                status, final, hops = inspect(source_url)
                if status != 200 or hops != [(301, destination)] or final != destination:
                    failures.append(f"{source_url}: expected one 301 to {destination}, got {status} via {hops}, final {final}")
        except (HTTPError, URLError, RuntimeError) as error:
            failures.append(f"{source_url}: {error}")
    if failures:
        for failure in failures:
            print("FAIL", failure)
        raise SystemExit(1)
    print(f"PASS: {len(rows)} direct destinations; {len(inventory)} sitemap URLs covered" +
          (" and source 301s" if args.sources else ""))


if __name__ == "__main__":
    main()
