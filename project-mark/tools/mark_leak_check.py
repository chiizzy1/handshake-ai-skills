#!/usr/bin/env python3
"""Advisory Project Mark prompt check.

New September 5 tasks: 1-3 deliverables, no assigned-family or per-file ask quota.
Use --spec legacy for an older 8/27 contract. Filename discovery can mistake
input references for outputs; repeat --deliverable to identify the actual outputs.
Wording flags never establish leakage, fairness, difficulty or rubric coverage.
"""
import argparse
import re
from collections import OrderedDict

DATA = {"csv", "tsv", "json", "xlsx", "xls", "parquet"}
VISUAL = {"pptx", "png", "svg", "html", "htm", "jpg", "jpeg"}
TEXT = {"pdf", "docx", "doc"}
CODE = {"py", "ipynb", "sql", "r"}
KNOWN = DATA | VISUAL | TEXT | CODE
FILENAME = re.compile(r"\b([A-Za-z0-9][\w\-]*\.(" + "|".join(sorted(KNOWN)) + r"))\b", re.I)
NUMBERED = re.compile(r"^\d+[.)]\s+")
DASHED = re.compile(r"^[-*+]\s+")

LEAKS = [
    ("solution narration", r"\b(the correct answer is|the trap is|the hidden trap|the intended winner)\b",
     "Check whether this exposes the solution rather than the business request."),
    ("suspicion cue", r"\b(beware|may be misleading|do not trust|don't trust)\b",
     "Review whether the warning unnecessarily announces the intended failure."),
    ("method named", r"\b(z-test|t-test|chi-squared|regression|difference-in-differences|bootstrap)\b",
     "A method can be a legitimate requirement; review its role in this task."),
    ("scope or cleaning", r"\b(deduplicat\w+|drop duplicates|over the last quarter)\b",
     "Required scope and definitions must stay explicit. This flag is advisory."),
]

def family(ext):
    for names, label in ((DATA, "Data"), (VISUAL, "Visual"), (TEXT, "Text"), (CODE, "Code")):
        if ext.lower() in names:
            return label
    return "Other"

def parse_deliverables(text):
    """Discover all distinct named files, including several in one prose sentence.

    Bullet counts are a legacy heuristic, not a measure of meaningful asks.
    Review input-file mentions or use the explicit --deliverable override.
    """
    files = OrderedDict()
    current = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        found = FILENAME.findall(line)
        new = []
        for name, ext in found:
            if name not in files:
                files[name] = {"ext": ext.lower(), "asks": 0}
                new.append(name)
        if new:
            current = new[-1]
        elif current and (NUMBERED.match(stripped) or DASHED.match(stripped)):
            files[current]["asks"] += 1
    return files

def check_contract(text, spec="current", deliverables=None):
    files = parse_deliverables(text)
    problems = []
    if deliverables is not None:
        selected = OrderedDict()
        for name in deliverables:
            match = FILENAME.fullmatch(name)
            if not match:
                problems.append(f"Unrecognized output filename: {name}")
                continue
            selected[name] = files.get(name, {"ext": match.group(2).lower(), "asks": 0})
            if name not in files:
                problems.append(f"Output {name} is not named in the prompt")
        files = selected
    n = len(files)
    if spec == "current":
        if not 1 <= n <= 3:
            problems.append(f"{n} output files detected; new tasks require 1-3")
    else:
        if n < 3:
            problems.append(f"{n} output files detected; legacy 8/27 minimum is 3")
        if len({family(m["ext"]) for m in files.values()}) < 2:
            problems.append("Legacy contract needs its two assigned output families")
        thin = [name for name, meta in files.items() if meta["asks"] < 3]
        if thin:
            problems.append("Legacy bullet heuristic found fewer than 3 asks: " + ", ".join(thin))
    return files, problems

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt")
    ap.add_argument("--spec", choices=("current", "legacy"), default="current")
    ap.add_argument("--deliverable", action="append", help="Actual output filename; repeat to exclude input references")
    args = ap.parse_args(argv)
    try:
        with open(args.prompt, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        ap.exit(2, f"cannot read {args.prompt}: {exc}\n")
    files, problems = check_contract(text, args.spec, args.deliverable)
    print(f"Specification: {args.spec}")
    print("Detected outputs: " + (", ".join(files) or "none"))
    for problem in problems:
        print("CONTRACT REVIEW: " + problem)
    if not problems:
        print("CONTRACT: detected file count/legacy shape OK")
    print("NOTE: review filename detection; --deliverable distinguishes inputs from outputs.")
    if args.spec == "current":
        print("NOTE: no family or per-file ask quota; 25+ substantive rubric criteria require human/platform review.")
    else:
        print("NOTE: legacy ask counts are heuristic; verify actual asks and assigned families.")
    flags = 0
    for label, pattern, why in LEAKS:
        for match in re.finditer(pattern, text, re.I):
            line = text.count("\n", 0, match.start()) + 1
            print(f"ADVISORY line {line}: {label} — {why}")
            flags += 1
    print(f"Advisory flags: {flags}. This is not a difficulty or approval check.")
    return int(bool(problems))

if __name__ == "__main__":
    raise SystemExit(main())
