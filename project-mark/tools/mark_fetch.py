#!/usr/bin/env python3
"""Fetch a source file with provenance recorded at download time.

Downloads URL to --out, computes SHA-256, and appends an entry to the roles
sidecar (source, pulled, licence, role, bytes, sha256) so provenance never has
to be reconstructed later.

    mark_fetch.py URL --out FILE --licence "CC-BY 4.0" --role "what it is" \
                  [--roles roles.json] [--timeout 120]

If a fetch fails or returns HTML instead of data, inspect the actual error,
check the official download route and retry ordinary technical failures. Follow
environment escalation rules for sandbox failures. Request a manual transfer
only when access genuinely requires the user. Never substitute from memory.
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) project-mark-sourcing/1.0"}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--out", required=True)
    ap.add_argument("--licence", required=True,
                    help="verified licence, from the source's live licence page")
    ap.add_argument("--role", required=True, help="analytical role of the file")
    ap.add_argument("--roles", default="roles.json")
    ap.add_argument("--timeout", type=int, default=120)
    a = ap.parse_args()

    try:
        req = urllib.request.Request(a.url, headers=UA)
        with urllib.request.urlopen(req, timeout=a.timeout) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
    except Exception as exc:
        print(f"FETCH FAILED: {exc}\n")
        print("Inspect the error and official download route; retry transient failures.")
        print("For sandbox/network restrictions, follow the environment's escalation procedure.")
        print("Ask for a manual transfer only if access requires the user's credentials or action.")
        print(f"  URL: {a.url}")
        print(f"  Save as: {os.path.basename(a.out)}")
        sys.exit(1)

    ext = os.path.splitext(a.out)[1].lower()
    if "text/html" in ctype and ext not in (".html", ".htm"):
        print(f"WARNING: server returned HTML ({len(data):,} bytes) but the target is "
              f"'{ext}'. This is usually a redirect or bot-block page, not the file.")
        print("Do not record this as the source file. Inspect the response and official download route.")
        print("A manual transfer is a last resort when access requires the user's action.")
        print(f"  URL: {a.url}\n  Save as: {os.path.basename(a.out)}")
        sys.exit(1)

    with open(a.out, "wb") as fh:
        fh.write(data)
    sha = hashlib.sha256(data).hexdigest()

    prov = {}
    if os.path.exists(a.roles):
        with open(a.roles, encoding="utf-8") as fh:
            prov = json.load(fh)
    prov[os.path.basename(a.out)] = dict(
        role=a.role, necessary=None, source=a.url,
        pulled=datetime.date.today().isoformat(),
        licence=a.licence, sha256=sha, bytes=len(data))
    with open(a.roles, "w", encoding="utf-8") as fh:
        json.dump(prov, fh, indent=2)

    print(f"fetched  {a.out}  {len(data):,} bytes  sha256 {sha[:16]}…")
    print(f"provenance recorded in {a.roles}")


if __name__ == "__main__":
    main()
