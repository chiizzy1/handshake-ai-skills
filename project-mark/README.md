# Project Mark

Project Mark skills for the Handshake AI platform.

Mark is a **task authoring project**, not a rating project. You build a
reinforcement learning environment: a package of real sourced files, a prompt
committing an analyst to one deterministic recommendation, and the golden
deliverable set a fully correct analyst would hand back. Then you prove frontier
models get it wrong.

$800 per approved task, flat. Roughly seven hours for a first task, around five
after.

## Skills

| Skill | Covers |
|---|---|
| `mark-task-builder` | The router. The nine-step pipeline, hard gates, domain and objective selection, debugging |
| `mark-input-package` | Sourcing, licensing, provenance, the 10/4/2/3 bar, the remove-one-file test, the manifest |
| `mark-prompt-writer` | The task contract, prompt anatomy, the ask taxonomy, the no-leak rules |
| `mark-trap-designer` | Six trap families, four fairness criteria, honest-data doctrine, recipe composition |
| `mark-golden-builder` | The deliverable set, structure by format, traceability, cross-file reconciliation |
| `mark-validator` | The five gates, one-pass rubric review, rollout scoring, the 51 Readiness checks |

Start at `mark-task-builder`. It routes to the rest.

## Shared references

- `shared-references/canonical-rules.md` — **the operative rule table.** The
  handbook contradicts itself in six places because the 8/18 update changed the
  task shape and the older pages were not updated behind it. This resolves every
  conflict. Read it before quoting any number.
- `shared-references/trap-catalog.md` — the trap families and objectives, the
  named traps, and the 14 worked recipes.

## Tools

Run from this folder. Python 3.9+, no required dependencies.

| Tool | What it does |
|---|---|
| `tools/mark_manifest.py <package>` | Takes a directory **or a .zip**. SHA-256, byte size, format family and row count per file, plus the Readiness stage 1 counters. `--init-roles FILE` writes a fill-in-the-blanks template. **Gate 1 requires this manifest.** |
| `tools/mark_leak_check.py <prompt.md>` | Validates contract shape and flags answer-path leakage |
| `tools/mark_reconcile.py <golden_dir>` | Diffs numbers across the golden set. The most common defect on the project |

`mark_reconcile.py` reads DOCX, XLSX, CSV, JSON and source files with no
dependencies. PDF needs `pdfplumber` or `pypdf` — see `tools/requirements.txt`.
Without one it reports the file as **unread** rather than silently skipping it.

## Known gaps in the source material

The local handbook capture at `HANDSHAKE-AI/Project-Mark/` is a set of
folded-state DOM snapshots, so anything behind an expander was never captured.

| Missing | Extent |
|---|---|
| Trap bodies, family catalog | 83 entries, 34 named, **0 bodies** |
| Trap bodies, objective catalog | 104 entries, 33 named, **0 bodies** |
| Readiness checks | 45 of 51 (stages 2–6) |
| Example prompts | 94 of 96 |
| FAQ answers | 14 of 16 |
| `/trap-design/fundamentals`, `/invalid-stumps` | Not captured at all |

**Fully captured:** all 25 worked examples with their prompts, step-by-step
solutions, justifications and rubrics; the input bar; the prompt contract; the
golden rules; the five gates; rubric weights; the scoring bar; the reviewer flow;
the 14 recipes.

The skills say so where it matters. When a trap is named but not described, say
that rather than reconstructing a body from its title.

To fill the gaps, capture the pages with every expander open and append to
`shared-references/trap-catalog.md` and `mark-validator/references/readiness.md`.
Both use a stable schema, so new entries are appends.

## Sources newer than the handbook capture

Two surfaces post-date the local capture and win over it:

- **The 8/18 spec card**, reachable from the assessment and at
  `/818-updates`. Confirms 10+ files in a **single ZIP**, **two or more**
  deliverables with no stated ceiling, 2+ families, 2+ asks each with **unit and
  rounding** on every numeric ask, and that **only the main recommendation must
  stump**.
- **The live project page.** Confirms **$800/task**, and describes the work as
  sourcing "real **occupational** materials" for tasks that force models to draw
  on "**occupation-specific tools and instructions**" — a framing the handbook's
  six analytical domains do not use. Watch the first live task to see which
  framing governs.

Both are folded into `shared-references/canonical-rules.md`.

## Naming Convention

All Project Mark skill folders use the `mark-` prefix, to prevent clashes with
Project Hedgehog (`handshake-*`), Project Lizard (`lizard-*`) and Project Gaffer
(`gaffer-*`).

## Source Material

The read-only handbook capture lives outside this repo:

- `HANDSHAKE-AI/Project-Mark/` — the extracted handbook
- `HANDSHAKE-AI/Project-Mark/examples/` — 25 accepted tasks with golden deliverables
