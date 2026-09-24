#!/usr/bin/env python3
"""Diff the numbers across a Project Mark golden deliverable set.

The handbook is explicit that numbers disagreeing across deliverables is the most
common defect, and that a reviewer diffs them against each other. This does that
diff first.

Extracts numeric values from every deliverable, groups them, and reports:
  - figures that appear in only one file (unreconciled)
  - near-miss clusters, where two files carry values close but not equal
    (a rounding or staleness mismatch, the usual culprit)

DOCX, XLSX, CSV, JSON, and source files are read with no dependencies. PDF needs
pdfplumber or pypdf; without one it reports the file as unread rather than
silently skipping it.

Usage:
    mark_reconcile.py <golden_dir_or_files...> [--tolerance 0.01] [--min 2]
"""

import argparse
import csv
import os
import re
import sys
import zipfile
from collections import defaultdict

NUM = re.compile(r"-?\d[\d,]*\.?\d*")
# Values this common carry no signal - years, small counts, percentages of 100.
NOISE = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 100.0}


def norm(raw):
    """Parse to float, rounded so storage noise merges.

    XLSX stores 44267.2 as 44267.199999999997. Without this they land as two
    distinct keys and get reported as a near miss against themselves.
    """
    try:
        return round(float(raw.replace(",", "")), 6)
    except ValueError:
        return None


def from_text(text):
    out = []
    for m in NUM.finditer(text):
        v = norm(m.group(0))
        if v is not None:
            out.append((v, m.group(0)))
    return out


def read_docx(path):
    try:
        with zipfile.ZipFile(path) as zf:
            xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    except Exception as exc:
        raise RuntimeError(f"docx unreadable: {exc}")


def read_xlsx(path):
    try:
        with zipfile.ZipFile(path) as zf:
            shared = []
            if "xl/sharedStrings.xml" in zf.namelist():
                raw = zf.read("xl/sharedStrings.xml").decode("utf-8", errors="replace")
                shared = re.findall(r"<t[^>]*>([^<]*)</t>", raw)
            chunks = list(shared)
            for name in zf.namelist():
                if name.startswith("xl/worksheets/sheet"):
                    raw = zf.read(name).decode("utf-8", errors="replace")
                    chunks.extend(re.findall(r"<v>([^<]*)</v>", raw))
            return "\n".join(chunks)
    except Exception as exc:
        raise RuntimeError(f"xlsx unreadable: {exc}")


def _quiet_pdfminer():
    """pdfminer logs font and colour-space complaints that are not our problem."""
    import logging

    for name in ("pdfminer", "pdfminer.pdfinterp", "pdfminer.pdffont",
                 "pdfminer.pdfpage", "pdfminer.converter", "pdfminer.cmapdb"):
        logging.getLogger(name).setLevel(logging.ERROR)


def read_pdf(path):
    try:
        import pdfplumber

        _quiet_pdfminer()
        with pdfplumber.open(path) as pdf:
            return "\n".join(p.extract_text() or "" for p in pdf.pages)
    except ImportError:
        pass
    try:
        from pypdf import PdfReader

        return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
    except ImportError:
        raise RuntimeError("PDF needs pdfplumber or pypdf - pip install pdfplumber")
    except Exception as exc:
        raise RuntimeError(f"pdf unreadable: {exc}")


def read_csv(path):
    """Join cells with newlines, never commas.

    Joining with commas lets the number scanner run across a field boundary and
    fuse two cells: ",1,0.8912," reads as "10.8912" once thousands separators are
    stripped. That produced phantom near-misses on every CSV deliverable.
    """
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        return "\n".join("\n".join(r) for r in csv.reader(fh))


def read_plain(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


READERS = {
    ".docx": read_docx,
    ".xlsx": read_xlsx,
    ".pdf": read_pdf,
    ".csv": read_csv,
    ".tsv": read_csv,
    ".json": read_plain,
    ".py": read_plain,
    ".sql": read_plain,
    ".r": read_plain,
    ".md": read_plain,
    ".txt": read_plain,
    ".html": read_plain,
}


def collect(paths):
    """value -> {filename: [raw strings]}, plus a list of files that failed."""
    index = defaultdict(lambda: defaultdict(list))
    unread = []
    read = []
    for path in paths:
        ext = os.path.splitext(path)[1].lower()
        reader = READERS.get(ext)
        name = os.path.basename(path)
        if reader is None:
            unread.append((name, f"no reader for {ext or 'extensionless file'}"))
            continue
        try:
            text = reader(path)
        except RuntimeError as exc:
            unread.append((name, str(exc)))
            continue
        read.append(name)
        for value, raw in from_text(text):
            index[value][name].append(raw)
    return index, read, unread


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+", help="golden directory, or the deliverable files")
    ap.add_argument("--tolerance", type=float, default=0.01,
                    help="relative gap below which two values are a near miss (default 0.01)")
    ap.add_argument("--min", type=int, default=2,
                    help="ignore magnitudes below this (default 2)")
    args = ap.parse_args()

    paths = []
    for t in args.targets:
        if os.path.isdir(t):
            for dirpath, dirnames, filenames in os.walk(t):
                dirnames[:] = [d for d in dirnames if not d.startswith(".")]
                paths += [os.path.join(dirpath, f) for f in sorted(filenames) if not f.startswith(".")]
        else:
            paths.append(t)
    if not paths:
        sys.exit("no files found")

    index, read, unread = collect(paths)

    print("# Golden set reconciliation\n")
    print(f"Read {len(read)} file(s): {', '.join(read) or 'none'}\n")
    if unread:
        print(f"**{len(unread)} file(s) not read.** Their numbers are NOT in this diff.\n")
        for name, why in unread:
            print(f"- {name} - {why}")
        print()

    if len(read) < 2:
        print("Fewer than two readable deliverables - nothing to reconcile against.")
        sys.exit(1)

    significant = {
        v: files for v, files in index.items()
        if abs(v) >= args.min and v not in NOISE
    }

    shared = {v: f for v, f in significant.items() if len(f) > 1}
    lonely = {v: f for v, f in significant.items() if len(f) == 1}

    print("## Figures agreeing across files\n")
    if shared:
        print("| Value | Appears in |\n|---|---|")
        for v in sorted(shared, key=lambda x: -abs(x))[:40]:
            print(f"| {v:g} | {', '.join(sorted(shared[v]))} |")
        if len(shared) > 40:
            print(f"\n({len(shared) - 40} more)")
    else:
        print("**None.** No numeric value appears in more than one deliverable. "
              "Either the files carry genuinely separate figures, or they disagree everywhere.")
    print()

    print("## Near misses - likely rounding or staleness mismatches\n")
    values = sorted(significant)
    misses = []
    for i, a in enumerate(values):
        for b in values[i + 1:]:
            if a == 0:
                continue
            gap = abs(b - a) / abs(a)
            if gap > args.tolerance:
                break
            if gap < 1e-9:
                continue
            fa, fb = set(significant[a]), set(significant[b])
            if fa != fb and not (fa & fb):
                misses.append((a, b, gap, sorted(fa), sorted(fb)))

    if misses:
        print("| A | in | B | in | gap |\n|---|---|---|---|---|")
        for a, b, gap, fa, fb in sorted(misses, key=lambda m: -m[2])[:30]:
            print(f"| {a:.12g} | {', '.join(fa)} | {b:.12g} | {', '.join(fb)} | {gap:.3%} |")
        print("\nEach row is two files carrying almost-but-not-quite the same figure. Either "
              "one file rounds what another states precisely, which is fine when the prompt "
              "asked for that precision, or the two disagree, which is the defect a reviewer "
              "finds first. Confirm which, per row.")
    else:
        print("None found.")
    print()

    print("## Figures in only one file\n")
    print(f"{len(lonely)} value(s) appear in exactly one deliverable. That is normal for "
          "file-specific detail, and a defect when the value is load-bearing and should "
          "have been echoed. Check the load-bearing ones by hand.\n")

    print("## Verdict\n")
    print(f"- Reconciled across files: {len(shared)}")
    print(f"- Near misses to resolve: {len(misses)}")
    print(f"- Single-file values: {len(lonely)}")
    print(f"- Files not read: {len(unread)}")
    print("\nThis tool finds numeric disagreement. It cannot tell you whether a figure is "
          "*correct* - that is Gate 1.")

    sys.exit(1 if (misses or unread) else 0)


if __name__ == "__main__":
    main()
