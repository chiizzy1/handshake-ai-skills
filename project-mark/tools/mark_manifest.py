#!/usr/bin/env python3
"""Manifest an input package and report partial inherited Project Mark counters.

This records hashes, sizes, declared roles and supported row counts. It cannot
certify substantial content, analytical necessity, valid reuse or platform
approval. Current task UI requirements take precedence over inherited counters.

Roles and necessity cannot be inferred from a file, so they come from an optional
sidecar (--roles roles.json) mapping filename to
{"role": ..., "necessary": true, "source": ..., "pulled": ..., "licence": ...}.
Anything missing is reported as unrecorded rather than guessed.

Usage:
    mark_manifest.py <package_dir> [--roles roles.json] [--json] [--out FILE]
"""

import argparse
import csv
import hashlib
import bz2
import gzip
import io
import json
import lzma
import os
import shutil
import sqlite3
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

DATA = {".csv", ".tsv", ".tab", ".dta", ".json", ".jsonl", ".ndjson", ".xlsx", ".xls", ".parquet",
        ".sqlite", ".sqlite3", ".db"}
VISUAL = {".pptx", ".png", ".svg", ".html", ".htm", ".jpg", ".jpeg", ".gif"}
TEXT = {".pdf", ".docx", ".doc", ".txt", ".md", ".rtf"}
CODE = {".py", ".ipynb", ".sql", ".r"}
COMPRESSED = {".gz", ".bz2", ".xz"}

MIN_FILES = 10
MIN_NECESSARY = 4
MIN_SUBSTANTIAL = 2
MIN_FORMATS = 3
MIN_BIG_TABLE_ROWS = 10_000
SUBSTANTIAL_BYTES = 100 * 1024
MAX_FILE_BYTES = 10_000_000
MAX_ZIP_BYTES = 50_000_000
REPORT_NOTES = [
    "Partial inherited counters only; this is not platform approval.",
    "Substantial content and analytical necessity require review; 100 KiB is only a local size proxy.",
    "Row counts are candidates for review, not certified observations; CSV/TSV/TAB and XLSX assume one header row.",
    "XLSX counts nonempty rows rather than worksheet extent; notes and separate tables still need review.",
    "Unsupported or unreadable table formats, including DTA, have unmeasured row counts.",
    "Byte checks conservatively interpret MB as 1,000,000 bytes; limits are strict.",
    "A directory does not establish the final ZIP size. Supply the actual shipping ZIP to measure it.",
    "Joins, substantive file roles, reuse rights and any stricter current UI/onboarding rules are not certified here.",
]


def inner_ext(name):
    """Extension a file carries under any compression suffix.

    A gzipped table is still a table; ``package_records_2014.jsonl.gz`` counts
    as Data with countable rows, not as an unclassified blob.
    """
    stem, ext = os.path.splitext(name)
    if ext.lower() in COMPRESSED:
        ext = os.path.splitext(stem)[1]
    return ext.lower()


def family(ext):
    ext = ext.lower()
    if ext in COMPRESSED:
        return "Data"
    if ext in DATA:
        return "Data"
    if ext in VISUAL:
        return "Visual"
    if ext in TEXT:
        return "Text"
    if ext in CODE:
        return "Code"
    return "Other"


def sha256_and_size(path):
    h = hashlib.sha256()
    size = 0
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
            size += len(chunk)
    return h.hexdigest(), size


def _opener(path):
    """Text-mode opener that transparently handles a compression suffix."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".gz":
        return lambda: gzip.open(path, "rt", encoding="utf-8", errors="replace")
    if ext == ".bz2":
        return lambda: bz2.open(path, "rt", encoding="utf-8", errors="replace")
    if ext == ".xz":
        return lambda: lzma.open(path, "rt", encoding="utf-8", errors="replace")
    return lambda: open(path, newline="", encoding="utf-8", errors="replace")


def count_rows(path, ext):
    """Row count for tabular files. None when not applicable or unreadable.

    ``ext`` is the extension under any compression suffix, so a gzipped CSV or
    JSONL is counted the same as a plain one.
    """
    ext = ext.lower()
    compressed = os.path.splitext(path)[1].lower() in COMPRESSED
    try:
        if ext in (".csv", ".tsv", ".tab"):
            delim = "," if ext == ".csv" else "\t"
            with _opener(path)() as fh:
                return max(sum(1 for row in csv.reader(fh, delimiter=delim)
                               if any(value.strip() for value in row)) - 1, 0)
        if ext in (".jsonl", ".ndjson"):
            with _opener(path)() as fh:
                return sum(1 for line in fh if line.strip())
        if ext == ".xlsx":
            return None if compressed else _xlsx_rows(path)
        if ext in (".sqlite", ".sqlite3", ".db"):
            return None if compressed else _sqlite_rows(path)
        if ext == ".json":
            with _opener(path)() as fh:
                data = json.load(fh)
            return len(data) if isinstance(data, list) else None
    except Exception:
        return None
    return None


def _sqlite_rows(path):
    """Row count of the largest table in a SQLite database."""
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        names = [r[0] for r in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name NOT LIKE 'sqlite_%'")]
        best = 0
        for n in names:
            best = max(best, con.execute(
                f'SELECT COUNT(*) FROM "{n}"').fetchone()[0])
        return best if names else None
    finally:
        con.close()


def _xlsx_rows(path):
    """Largest nonempty sheet row count, less one assumed header row.

    A far-away styled cell changes a sheet's extent without adding observations.
    Inspect actual cell content instead. This still cannot identify notes or
    multiple tables within a sheet and does not evaluate formulas.
    """
    try:
        best = 0
        with zipfile.ZipFile(path) as zf:
            shared_strings = []
            if "xl/sharedStrings.xml" in zf.namelist():
                with zf.open("xl/sharedStrings.xml") as fh:
                    for _, elem in ET.iterparse(fh, events=("end",)):
                        if elem.tag.rsplit("}", 1)[-1] == "si":
                            shared_strings.append(any(
                                (node.text or "").strip() for node in elem.iter()
                                if node.tag.rsplit("}", 1)[-1] == "t"))
                            elem.clear()
            sheets = [n for n in zf.namelist()
                      if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")]
            for name in sheets:
                nonempty = 0
                with zf.open(name) as fh:
                    for _, elem in ET.iterparse(fh, events=("end",)):
                        if elem.tag.rsplit("}", 1)[-1] == "row":
                            if any(_xlsx_cell_has_content(cell, shared_strings)
                                   for cell in elem
                                   if cell.tag.rsplit("}", 1)[-1] == "c"):
                                nonempty += 1
                            elem.clear()
                best = max(best, nonempty - 1)
        return max(best, 0)
    except Exception:
        return None


def _xlsx_cell_has_content(cell, shared_strings):
    for node in cell.iter():
        tag = node.tag.rsplit("}", 1)[-1]
        content = (node.text or "").strip()
        if tag == "v" and content:
            if cell.get("t") == "s":
                if shared_strings[int(content)]:
                    return True
            else:
                return True
        if tag in ("t", "f") and content:
            return True
    return False


def build(package_dir, roles):
    rows = []
    for dirpath, dirnames, filenames in os.walk(package_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.startswith(".") or fn == "Thumbs.db":
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, package_dir)
            ext = os.path.splitext(fn)[1]
            under = inner_ext(fn)
            digest, size = sha256_and_size(full)
            meta = roles.get(rel) or roles.get(fn) or {}
            rows.append(
                {
                    "file": rel,
                    "format": ext.lstrip(".").lower() or "none",
                    "family": family(under) if under else family(ext),
                    "bytes": size,
                    "rows": count_rows(full, under),
                    "sha256": digest,
                    "role": meta.get("role"),
                    "necessary": meta.get("necessary"),
                    "source": meta.get("source"),
                    "pulled": meta.get("pulled"),
                    "licence": meta.get("licence"),
                }
            )
    return rows


def check(rows, zip_bytes=None):
    formats = {r["format"] for r in rows}
    necessary = [r for r in rows if r["necessary"] is True]
    row_counts = [r["rows"] for r in rows if r["rows"] is not None]
    biggest = max(row_counts) if row_counts else 0
    documented = [
        r for r in rows if r["source"] and r["pulled"] and r["licence"]
    ]
    unrecorded = [r for r in rows if r["necessary"] is None]

    return [
        ("10+ files", len(rows), MIN_FILES, len(rows) >= MIN_FILES),
        (
            "4+ declared independently necessary (review required)",
            len(necessary),
            MIN_NECESSARY,
            len(necessary) >= MIN_NECESSARY,
        ),
        (
            "2+ substantial files (content review)",
            None,
            MIN_SUBSTANTIAL,
            None,
        ),
        ("3+ distinct formats", len(formats), MIN_FORMATS, len(formats) >= MIN_FORMATS),
        (
            "10,000+ row table",
            biggest,
            MIN_BIG_TABLE_ROWS,
            biggest >= MIN_BIG_TABLE_ROWS,
        ),
        (
            "provenance recorded",
            len(documented),
            len(rows),
            len(documented) == len(rows),
        ),
        (
            "Each file strictly under 10 MB (largest bytes)",
            max((r["bytes"] for r in rows), default=0),
            f"< {MAX_FILE_BYTES}",
            all(r["bytes"] < MAX_FILE_BYTES for r in rows),
        ),
        (
            "Shipping ZIP strictly under 50 MB (bytes)",
            zip_bytes,
            f"< {MAX_ZIP_BYTES}",
            None if zip_bytes is None else zip_bytes < MAX_ZIP_BYTES,
        ),
    ], unrecorded


def render(rows, checks, unrecorded):
    out = io.StringIO()
    w = out.write
    w("# Input package manifest\n\n")
    for note in REPORT_NOTES:
        w(f"- {note}\n")
    w("\n")
    w("| File | Format | Family | Bytes | Rows | Role | Necessary | Source | Pulled | Licence | SHA-256 |\n")
    w("|---|---|---|---|---|---|---|---|---|---|---|\n")
    for r in rows:
        nec = {True: "yes", False: "no", None: "—"}[r["necessary"]]
        w(
            f"| {r['file']} | {r['format']} | {r['family']} | {r['bytes']:,} | "
            f"{r['rows'] if r['rows'] is not None else '—'} | {r['role'] or '—'} | {nec} | "
            f"{r['source'] or '—'} | {r['pulled'] or '—'} | {r['licence'] or '—'} | "
            f"{r['sha256'][:16]}… |\n"
        )

    w("\n## Partial inherited checks\n\n| Counter | Actual | Reference | Status |\n|---|---|---|---|\n")
    for name, actual, needed, ok in checks:
        status = "NOT MEASURED" if ok is None else ("PASS" if ok else "FAIL")
        w(f"| {name} | {actual if actual is not None else '—'} | {needed} | {status} |\n")

    proxy_count = sum(r["bytes"] >= SUBSTANTIAL_BYTES for r in rows)
    w(f"\nLocal size proxy: {proxy_count} files are at least 100 KiB. "
      "This does not establish that two files are substantial.\n")

    families = sorted({r["family"] for r in rows})
    w(f"\nFamilies present: {', '.join(families)}\n")

    if unrecorded:
        w(
            f"\n**{len(unrecorded)} file(s) have no necessity recorded.** "
            "Necessity comes from the remove-one-file test, not from this script. "
            "Run that test and supply --roles.\n\n"
        )
        for r in unrecorded:
            w(f"- {r['file']}\n")

    failed = [c for c in checks if c[3] is False]
    unmeasured = [c for c in checks if c[3] is None]
    w(f"\n**{len(failed)} measured checks failing; {len(unmeasured)} checks not measured.** "
      "Passing measured counters is not platform approval.\n")
    return out.getvalue()


def init_roles(package_dir, out_path):
    """Write a roles.json template pre-filled with every filename in the package."""
    stub = {}
    for dirpath, dirnames, filenames in os.walk(package_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.startswith(".") or fn == "Thumbs.db":
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), package_dir)
            stub[rel] = {
                "role": "",
                "necessary": None,
                "source": "",
                "pulled": "",
                "licence": "",
            }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(stub, fh, indent=2)
    print(f"wrote {out_path} with {len(stub)} file(s)\n")
    print("Fill in each entry, then re-run with --roles:")
    print('  role       what analytical work the file does')
    print('  necessary  true only after the remove-one-file test says the answer')
    print('             becomes unreachable without it. Distractors are false.')
    print('  source     the URL it came from')
    print('  pulled     YYYY-MM-DD')
    print('  licence    the licence name')


def resolve_target(target):
    """Return (dir_to_scan, tempdir_to_clean). Accepts a directory or a .zip."""
    if os.path.isdir(target):
        return target, None
    if zipfile.is_zipfile(target):
        tmp = tempfile.mkdtemp(prefix="mark_manifest_")
        with zipfile.ZipFile(target) as zf:
            zf.extractall(tmp)
        entries = [e for e in os.listdir(tmp) if not e.startswith((".", "__MACOSX"))]
        # a zip wrapping one folder should be scanned at that folder
        if len(entries) == 1 and os.path.isdir(os.path.join(tmp, entries[0])):
            return os.path.join(tmp, entries[0]), tmp
        return tmp, tmp
    sys.exit(f"not a directory or zip file: {target}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package", help="the input package: a directory or a .zip")
    ap.add_argument("--roles", help="JSON sidecar: filename -> role/necessary/source/pulled/licence")
    ap.add_argument("--init-roles", metavar="FILE",
                    help="write a roles.json template pre-filled with every filename, then exit")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of markdown")
    ap.add_argument("--out", help="write to FILE instead of stdout")
    args = ap.parse_args()

    scan_dir, tmp = resolve_target(args.package)
    try:
        if args.init_roles:
            init_roles(scan_dir, args.init_roles)
            return

        roles = {}
        if args.roles:
            with open(args.roles, encoding="utf-8") as fh:
                roles = json.load(fh)

        rows = build(scan_dir, roles)
        if not rows:
            sys.exit(f"no files found in {args.package}")
        run(rows, args)
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


def run(rows, args):

    zip_bytes = (os.path.getsize(args.package)
                 if os.path.isfile(args.package) and zipfile.is_zipfile(args.package)
                 else None)
    checks, unrecorded = check(rows, zip_bytes=zip_bytes)
    text = (
        json.dumps(
            {
                "files": rows,
                "scope": "partial inherited counters; not platform approval",
                "notes": REPORT_NOTES,
                "heuristics": {
                    "files_at_least_100_kib": sum(r["bytes"] >= SUBSTANTIAL_BYTES for r in rows),
                    "substantial_content_verified": False,
                },
                "checks": [
                    {"requirement": n, "actual": a, "needed": d, "pass": ok,
                     "status": "not measured" if ok is None else ("pass" if ok else "fail")}
                    for n, a, d, ok in checks
                ],
            },
            indent=2,
        )
        if args.json
        else render(rows, checks, unrecorded)
    )

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out}")
    else:
        print(text)

    # Preserve success/failure CLI behavior for measured counters. Unmeasured
    # checks remain explicit in the report and cannot establish acceptance.
    sys.exit(0 if all(c[3] is not False for c in checks) else 1)


if __name__ == "__main__":
    main()
