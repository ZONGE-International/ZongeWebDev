"""Render legacy.csv for an actual HTTP edge provider.

Usage: python3 scripts/export_edge_redirects.py cloudflare > /tmp/zonge-cloudflare.csv
       python3 scripts/export_edge_redirects.py netlify > /tmp/zonge-_redirects
"""

import argparse
import csv
import sys
from pathlib import Path


MANIFEST = Path(__file__).resolve().parents[1] / "redirects/legacy.csv"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provider", choices=("cloudflare", "netlify"))
    args = parser.parse_args()
    with MANIFEST.open(newline="") as source:
        rows = list(csv.DictReader(source))
    if args.provider == "cloudflare":
        # Cloudflare Bulk Redirect import: headerless, no subpath matching.
        writer = csv.writer(sys.stdout, lineterminator="\n")
        for row in rows:
            writer.writerow(("www.zonge.com" + row["source_path"], row["destination"],
                             row["status"], "FALSE", "FALSE", "FALSE", "FALSE"))
    else:
        for row in rows:
            print(row["source_path"], row["destination"], row["status"])


if __name__ == "__main__":
    main()
