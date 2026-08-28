#!/usr/bin/env python3
"""Lint a Project Mark prompt for contract shape and answer-path leakage.

Validates the 8/27 contract rules (3+ deliverables, 2+ format families, 3+ asks
per file, filenames carry extensions) and flags wording that may walk the model
toward the answer.

This is a linter, not a judge. Read the flags and decide. It cannot tell whether
a phrase leaks *your* trap, only that the phrase is the kind that usually does.

Usage:
    mark_leak_check.py prompt.md
"""

import argparse
import re
import sys
from collections import OrderedDict

DATA = {"csv", "tsv", "json", "xlsx", "xls", "parquet"}
VISUAL = {"pptx", "png", "svg", "html", "htm", "jpg", "jpeg"}
TEXT = {"pdf", "docx", "doc"}
CODE = {"py", "ipynb", "sql", "r"}
KNOWN = DATA | VISUAL | TEXT | CODE

FILENAME = re.compile(r"\b([A-Za-z0-9][\w\-]*\.(" + "|".join(sorted(KNOWN)) + r"))\b")

# (label, pattern, why it usually leaks)
LEAKS = [
    ("method named", r"\b(z-test|t-test|chi-squared|chi2|regression|chi square|"
                     r"difference-in-differences|diff-in-diff|chi-square|ANOVA|chi²|"
                     r"propensity score|bootstrap|chi-sq|log-rank|chi test)\b",
     "Naming a statistical method removes the method-selection difficulty."),
    ("cleaning instruction", r"\b(deduplicat\w+|de-duplicat\w+|drop duplicates|"
                            r"remove outliers|exclude nulls|filter out|normali[sz]e by)\b",
     "The prompt must be vague on cleaning. Every valid approach should converge."),
    ("trap narrated", r"\b(be careful|watch out|note that|beware|keep in mind that|"
                      r"bear in mind|may be misleading|can be misleading|is misleading|"
                      r"might be stale|may be stale|is stale|do not trust|don't trust)\b",
     "Narrating suspicion tells the model a trap exists."),
    ("decisive file pointed at", r"\b(the (data )?dictionary|the changelog|the errata|"
                                 r"the revision file|the methodology note) (defines|says|"
                                 r"governs|supersedes|explains|takes precedence)\b",
     "Naming the arbiter defuses the trap before the model reads the files."),
    ("window fixed", r"\b(over the (last|past|final) (full )?(quarter|month|year|week)|"
                     r"using only the (last|first) \d+)\b",
     "If the window is the trap, fixing it in the prompt rules the trap out."),
    ("answer-path verb", r"\b(first|then|next|finally),? (you should |you must |"
                         r"compute|calculate|join|aggregate|group by)\b",
     "Step ordering walks the model through the answer path."),
    ("hedge permitted", r"\b(if applicable|where appropriate|as you see fit|"
                        r"you may (also )?consider|feel free to|options include|"
                        r"one or more|a range of recommendations)\b",
     "The prompt must force one committed call with no hedge available."),
    ("outside knowledge", r"\b(as is well known|industry standard practice|"
                          r"commonly accepted benchmark|typical(ly)? in the industry)\b",
     "Everything load-bearing must be derivable from the shipped bundle."),
]


def family(ext):
    ext = ext.lower()
    for names, label in ((DATA, "Data"), (VISUAL, "Visual"), (TEXT, "Text"), (CODE, "Code")):
        if ext in names:
            return label
    return "Other"


def parse_deliverables(text):
    """Map each named file to the count of bullet asks that follow it."""
    lines = text.splitlines()
    files = OrderedDict()
    current = None
    for line in lines:
        stripped = line.strip()
        bullet = bool(re.match(r"^([-*+]|\d+[.)])\s+", stripped))
        found = FILENAME.findall(line)

        if found and not bullet:
            current = found[0][0].strip()
            files.setdefault(current, {"ext": found[0][1].lower(), "asks": 0})
            continue
        if found and bullet and current is None:
            current = found[0][0].strip()
            files.setdefault(current, {"ext": found[0][1].lower(), "asks": 0})
            continue
        if bullet and current:
            files[current]["asks"] += 1
        elif not stripped:
            continue
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt")
    args = ap.parse_args()

    try:
        with open(args.prompt, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        sys.exit(f"cannot read {args.prompt}: {exc}")

    files = parse_deliverables(text)
    families = {family(v["ext"]) for v in files.values()}

    print("# Prompt check\n")
    print("## Contract\n")
    print("| Deliverable | Family | Asks | |")
    print("|---|---|---|---|")
    for name, meta in files.items():
        ok = "OK" if meta["asks"] >= 3 else "TOO FEW"
        print(f"| {name} | {family(meta['ext'])} | {meta['asks']} | {ok} |")

    n = len(files)
    problems = []
    notes = []
    if n < 3:
        problems.append(f"{n} deliverable(s) — the 8/27 floor is 3, with no upper limit")
    if len(families) < 2:
        problems.append(
            f"{len(families)} format family ({', '.join(sorted(families)) or 'none'}) — needs at least 2"
        )
    else:
        notes.append(
            f"families present: {', '.join(sorted(families))}. This script cannot know "
            "which two were ASSIGNED to your task — check them yourself."
        )
    thin = [f for f, m in files.items() if m["asks"] < 3]
    if thin:
        problems.append(f"fewer than 3 asks: {', '.join(thin)}")
    total_asks = sum(m["asks"] for m in files.values())
    notes.append(
        f"{total_asks} asks across {n} deliverable(s). The rubric must reach 25+ "
        "criteria; thin or repetitive asks are the usual reason it stalls near 20."
    )

    print(f"\nDeliverables: {n} (floor is 3, no upper limit)")
    print(f"Families: {', '.join(sorted(families)) or 'none'} — {len(families)} distinct (need 2+)")

    print("\n## Leak flags\n")
    flags = []
    for label, pattern, why in LEAKS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            line_no = text[: m.start()].count("\n") + 1
            snippet = text.splitlines()[line_no - 1].strip()
            flags.append((line_no, label, m.group(0), snippet, why))

    if flags:
        for line_no, label, hit, snippet, why in sorted(flags):
            print(f"- **line {line_no} · {label}** — `{hit}`")
            print(f"  > {snippet[:140]}")
            print(f"  {why}\n")
    else:
        print("None. That is not proof the prompt is clean — reread it for trap-specific hints.\n")

    print("## Verdict\n")
    if problems:
        for p in problems:
            print(f"- CONTRACT: {p}")
    else:
        print("- CONTRACT: shape OK")
    for note in notes:
        print(f"- NOTE: {note}")
    print(f"- LEAK: {len(flags)} flag(s) to review by hand")

    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
