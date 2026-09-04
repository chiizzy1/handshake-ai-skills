#!/usr/bin/env python3
"""Lint authored input files and golden deliverables for LLM-generated tells.

Since 9/01, files that read as LLM output are a rejection criterion rather than
something staff quietly fix. This catches the mechanical tells: empty document
metadata, LLM-register vocabulary, uniform structure, default spreadsheet
formatting. It cannot judge voice - that is still a read-through.

    mark_realism_check.py <package_dir> [--authored a.docx,b.xlsx]

Files pulled from a real public source are realistic already. Pass --authored to
limit the check to what you wrote, or let it scan everything and ignore the
findings on sourced files.
"""
import argparse
import os
import re
import sys
import zipfile

# Register words that mark generated prose. Weighted: some are damning on sight,
# others only matter in bulk.
HEAVY = ["delve", "seamless", "multifaceted", "it is worth noting",
         "it's worth noting", "in today's", "ever-evolving", "testament to",
         "navigate the complexities", "unlock the", "harness the power"]
LIGHT = ["furthermore", "moreover", "comprehensive", "robust", "leverage",
         "underscore", "pivotal", "crucial", "in conclusion", "additionally",
         "holistic", "streamline", "facilitate", "utilize", "myriad"]

CONTROL_HINTS = ["rev ", "revision", "version", "effective date", "doc id",
                 "document id", "owner", "approved by", "prepared by",
                 "distribution", "confidential", "page "]


def docx_text_and_meta(path):
    try:
        import docx
    except ImportError:
        return None, None
    d = docx.Document(path)
    text = "\n".join(p.text for p in d.paragraphs)
    for t in d.tables:
        for row in t.rows:
            text += "\n" + " ".join(c.text for c in row.cells)
    cp = d.core_properties
    meta = {"author": cp.author, "company": None, "title": cp.title,
            "created": cp.created, "modified": cp.modified}
    return text, meta


def xlsx_report(path):
    """Structural realism of a workbook: sheets, freeze panes, widths, notes."""
    try:
        import openpyxl
    except ImportError:
        return []
    wb = openpyxl.load_workbook(path)
    out = []
    if len(wb.sheetnames) == 1:
        out.append("single sheet - real workbooks usually carry a notes or "
                   "working tab")
    frozen = any(ws.freeze_panes for ws in wb)
    if not frozen:
        out.append("no frozen panes on any sheet - default openpyxl output")
    widths = []
    for ws in wb:
        widths += [d.width for d in ws.column_dimensions.values() if d.width]
    if not widths:
        out.append("no adjusted column widths - default openpyxl output")
    props = wb.properties
    if not (props.creator and props.creator != "openpyxl"):
        out.append(f"creator is {props.creator!r} - set a real author")
    return out


def prose_report(text):
    out = []
    low = text.lower()
    hits = [w for w in HEAVY if w in low]
    if hits:
        out.append(f"LLM register (heavy): {', '.join(sorted(set(hits)))}")
    light = [w for w in LIGHT if re.search(rf"\b{re.escape(w)}\b", low)]
    if len(light) >= 3:
        out.append(f"LLM register ({len(light)} light markers): "
                   f"{', '.join(sorted(set(light))[:6])}")

    paras = [p.strip() for p in text.split("\n") if len(p.strip()) > 60]
    if len(paras) >= 4:
        lens = sorted(len(p) for p in paras)
        spread = lens[-1] / max(lens[0], 1)
        if spread < 2.0:
            out.append(f"paragraphs suspiciously uniform (longest/shortest "
                       f"= {spread:.1f}x) - real documents are lopsided")

    bullets = [l.strip() for l in text.split("\n")
               if l.strip()[:2] in ("- ", "* ", "• ")]
    if len(bullets) >= 4:
        lens = sorted(len(b) for b in bullets)
        if lens[-1] / max(lens[0], 1) < 1.8:
            out.append("bullets all the same length - vary them")

    if not any(h in low for h in CONTROL_HINTS):
        out.append("no document-control apparatus (revision, owner, effective "
                   "date, footer, distribution)")

    # A standard or policy is impersonal by design; correspondence is not.
    is_policy = len(re.findall(r"^\s*\d+\.\d+\s", text, re.M)) >= 3
    if not is_policy and re.search(
            r"\b(i|we|our|us|someone should|nobody|worth not)\b",
            text, re.I) is None:
        out.append("no first-person or organisational voice - reads as "
                   "description rather than correspondence")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("package_dir")
    ap.add_argument("--authored", help="comma-separated filenames you wrote; "
                                       "others are assumed sourced")
    a = ap.parse_args()

    only = set(f.strip() for f in a.authored.split(",")) if a.authored else None
    findings = {}
    for dirpath, dirnames, filenames in os.walk(a.package_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if fn.startswith(".") or (only and fn not in only):
                continue
            full = os.path.join(dirpath, fn)
            ext = os.path.splitext(fn)[1].lower()
            issues = []
            if ext == ".docx":
                text, meta = docx_text_and_meta(full)
                if text is None:
                    issues.append("python-docx not installed - skipped")
                else:
                    if not meta.get("author"):
                        issues.append("no author in core properties")
                    if not meta.get("title"):
                        issues.append("no title in core properties")
                    issues += prose_report(text)
            elif ext == ".xlsx":
                issues += xlsx_report(full)
            elif ext in (".txt", ".md"):
                issues += prose_report(open(full, encoding="utf-8",
                                            errors="replace").read())
            if issues:
                findings[fn] = issues

    if not findings:
        print("No mechanical tells found.\n\nThat is the lint passing, not the "
              "file reading as real. Read each authored file end to end and ask "
              "whether a person would have written it, for a reason.")
        return 0

    print("# Realism check\n")
    for fn, issues in findings.items():
        print(f"## {fn}")
        for i in issues:
            print(f"  - {i}")
        print()
    print(f"{sum(len(v) for v in findings.values())} finding(s) across "
          f"{len(findings)} file(s).\n")
    print("These are mechanical tells only. Voice, apparatus and dead weight "
          "still need a read-through - see "
          "mark-input-package/references/business-realism.md")
    return 1


if __name__ == "__main__":
    sys.exit(main())
