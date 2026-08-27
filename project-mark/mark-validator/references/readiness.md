# Readiness — 51 checks across 6 stages

For each check: review the requirement, verify it against your task, add an
evidence note naming the file or step that proves it, then mark it complete.
Nothing is scored and nothing leaves the browser.

When a rule changes, the checks depending on it are cleared and flagged, so you
re-read the rule instead of shipping against a stale version.

## Capture status

| Stage | Checks | Captured |
|---|---|---|
| 1. Policy | 6 | **Yes, verbatim** |
| 2. Task shape | 4 | No |
| 3. Inputs | 7 | No |
| 4. Prompt and solution | 10 | No |
| 5. Trap validation | 24 | No |
| 6. Submission | — | No |

Stages 2 to 6 are rendered client-side and were not in the local handbook
capture. **Say so when it matters.** Work the equivalent gate below and tell the
user the official check text was unavailable — do not present a reconstruction as
the official wording.

To fill this in, open `/readiness`, click through each stage selector, and append.

## Stage 1 — Policy (verbatim, all blocking)

1. **A task ships with at least ten input files.** — requires at least 10 files
2. **At least four of the shipped files are independently necessary: remove any
   one of them and the solution can no longer be reached.** — requires at least 4
3. **At least two of the inputs are substantial rather than token: long, dense
   files that take real work to read and reconcile.** — requires at least 2
4. **Optional distractor files are allowed and encouraged, but they never count
   toward the four independently necessary files.**
5. **AI may be used to locate data or to write transformation scripts, but it may
   never create the empirical source evidence itself.**
6. **Scenario documents and derived files carry explicit provenance stating what
   they are and how they were produced.**

Rows 1 to 3 want your real count, not an estimate. `../../tools/mark_manifest.py`
produces all three, plus the evidence note.

The reviewer reference confirms these six are exactly what Review 1 checks, which
is why stage 1 is worth clearing before anything else.

## Stages 2 to 6 — the equivalent gates

Not the official text. These are the requirements the same ground is covered by
elsewhere in the handbook, so a task that clears them is unlikely to fail the
official checks.

### Stage 2 — Task shape (4 checks)
- One domain from the accepted six, one Axis 1 objective, both matching the actual task rather than just the populated fields
- One deterministic recommendation, no hedge available
- Two or more deliverables across at least two format families
- At least two asks per named deliverable

### Stage 3 — Inputs (7 checks)
The package checklist from the Input files page:
- Necessary files: ten or more counted, and removing any counted file breaks the answer
- Recoverable joins: files connect through keys or references an analyst can recover
- Sufficient signal: the data supports the analysis the prompt requests
- Definitions and governing rules supplied inside the package, not assumed
- Reproducibility: every figure in the golden comes back out of the shipped workspace
- No padding: no decorative or deletable file is counted
- No fabricated or corrupted complexity

### Stage 4 — Prompt and solution (10 checks)
- Prompt is silent on scope, cleaning, window, and method
- The trap is never named or hinted
- Every load-bearing fact is derivable from the bundle
- The losing option is refuted on the data
- Golden types, filenames, and count match the prompt
- One set of numbers across all deliverables
- Nothing extra in the golden
- Every number traces to a shipped input file
- The recommendation is stated first in its file, naming what it rejects
- No placeholders, AI disclaimers, or chat-style framing

### Stage 5 — Trap validation (24 checks)
The largest stage, and the five gates plus the four fairness criteria are what it
tests:
- Gate 1 Reproduce — frozen archive, manifest with SHA-256, deterministic rerun
- Gate 2 Fork — every defensible expert choice converges; the winner survives estimation variation
- Gate 3 Live trap — neutralize-one-trap and remove-one-file, per trap and per file
- In-corpus antidote, deterministic outcome, no parsing puzzles, no fabricated source data
- Discoverable, consequential, deterministic, fair
- Honest data: the task stays hard after the model notices the messy detail

### Stage 6 — Submission
- Prompt, package, and golden still agree after the last edit
- No LLM-generated files, within size limits
- The recorded rollout matches what is being shipped
- Evidence exported

## Final handoff

Three steps, in order, all done by you:

1. **Export evidence** — Export JSON keeps progress and evidence for re-import;
   Export Markdown gives a readable copy.
2. **Open Handshake.**
3. **Confirm submission requirements**, and submit.

Handbook Readiness state is **not** a Handshake status and **not** an approval.

A reviewer picks it up from there and may send notes back. Revisions are normal
and unlimited; only approval before the end of the project matters for payment.
