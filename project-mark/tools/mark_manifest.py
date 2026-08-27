#!/usr/bin/env python3
"""Manifest an input package and check it against the Project Mark bar.

Gate 1 requires a manifest listing every file with its SHA-256 hash, byte size,
and role. This produces that, and reports the Readiness stage 1 counters at the
same time.

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
import io
import json
import os
import shutil
import sys
import tempfile
import zipfile

DATA = {".csv", ".tsv", ".json", ".xlsx", ".xls", ".parquet"}
VISUAL = {".pptx", ".png", ".svg", ".html", ".htm", ".jpg", ".jpeg", ".gif"}
TEXT = {".pdf", ".docx", ".doc", ".txt", ".md", ".rtf"}
CODE = {".py", ".ipynb", ".sql", ".r"}

MIN_FILES = 10
MIN_NECESSARY = 4
MIN_SUBSTANTIAL = 2
MIN_FORMATS = 3
MIN_BIG_TABLE_ROWS = 10_000
SUBSTANTIAL_BYTES = 100 * 1024


def family(ext):
    ext = ext.lower()
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


def count_rows(path, ext):
    """Row count for tabular files. None when not applicable or unreadable."""
    ext = ext.lower()
    try:
        if ext in (".csv", ".tsv"):
            delim = "\t" if ext == ".tsv" else ","
            with open(path, newline="", encoding="utf-8", errors="replace") as fh:
                return max(sum(1 for _ in csv.reader(fh, delimiter=delim)) - 1, 0)
        if ext == ".xlsx":
            return _xlsx_rows(path)
        if ext == ".json":
            with open(path, encoding="utf-8", errors="replace") as fh:
                data = json.load(fh)
            return len(data) if isinstance(data, list) else None
    except Exception:
        return None
    return None


def _xlsx_rows(path):
    """Largest sheet row count, read straight from the zip. No dependencies.

    Prefers each sheet's declared dimension; falls back to counting <row> tags.
    """
    try:
        import re

        best = 0
        with zipfile.ZipFile(path) as zf:
            sheets = [n for n in zf.namelist() if n.startswith("xl/worksheets/sheet")]
            for name in sheets:
                with zf.open(name) as fh:
                    head = fh.read(2048).decode("utf-8", errors="replace")
                    m = re.search(r'<dimension ref="[A-Z]+\d+:[A-Z]+(\d+)"', head)
                    if m:
                        best = max(best, int(m.group(1)) - 1)
                        continue
                    fh.seek(0)
                    body = fh.read().decode("utf-8", errors="replace")
                    best = max(best, body.count("<row ") - 1)
        return max(best, 0)
    except Exception:
        return None


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
            digest, size = sha256_and_size(full)
            meta = roles.get(rel) or roles.get(fn) or {}
            rows.append(
                {
                    "file": rel,
                    "format": ext.lstrip(".").lower() or "none",
                    "family": family(ext),
                    "bytes": size,
                    "rows": count_rows(full, ext),
                    "sha256": digest,
                    "role": meta.get("role"),
                    "necessary": meta.get("necessary"),
                    "source": meta.get("source"),
                    "pulled": meta.get("pulled"),
                    "licence": meta.get("licence"),
                }
            )
    return rows


def check(rows):
    formats = {r["format"] for r in rows}
    necessary = [r for r in rows if r["necessary"] is True]
    substantial = [r for r in rows if r["bytes"] >= SUBSTANTIAL_BYTES]
    row_counts = [r["rows"] for r in rows if r["rows"] is not None]
    biggest = max(row_counts) if row_counts else 0
    documented = [
        r for r in rows if r["source"] and r["pulled"] and r["licence"]
    ]
    unrecorded = [r for r in rows if r["necessary"] is None]

    return [
        ("10+ files", len(rows), MIN_FILES, len(rows) >= MIN_FILES),
        (
            "4+ independently necessary",
            len(necessary),
            MIN_NECESSARY,
            len(necessary) >= MIN_NECESSARY,
        ),
        (
            f"2+ substantial (>={SUBSTANTIAL_BYTES // 1024}KB)",
            len(substantial),
            MIN_SUBSTANTIAL,
            len(substantial) >= MIN_SUBSTANTIAL,
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
    ], unrecorded


def render(rows, checks, unrecorded):
    out = io.StringIO()
    w = out.write
    w("# Input package manifest\n\n")
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

    w("\n## Bar check\n\n| Requirement | Actual | Needed | |\n|---|---|---|---|\n")
    for name, actual, needed, ok in checks:
        w(f"| {name} | {actual} | {needed} | {'PASS' if ok else 'FAIL'} |\n")

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

    failed = [c for c in checks if not c[3]]
    w(f"\n**{len(failed)} of {len(checks)} requirements failing.**\n")
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

    checks, unrecorded = check(rows)
    text = (
        json.dumps(
            {
                "files": rows,
                "checks": [
                    {"requirement": n, "actual": a, "needed": d, "pass": ok}
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

    sys.exit(0 if all(c[3] for c in checks) else 1)


if __name__ == "__main__":
    main()
