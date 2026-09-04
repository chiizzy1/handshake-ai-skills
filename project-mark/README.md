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
| `tools/mark_fetch.py URL --out F --licence L --role R` | Downloads a source with SHA-256 and provenance recorded at fetch time; on failure or an HTML bot-block it prints the hand-to-user fallback |

`mark_reconcile.py` reads DOCX, XLSX, CSV, JSON and source files with no
dependencies. PDF needs `pdfplumber` or `pypdf` — see `tools/requirements.txt`.
Without one it reports the file as **unread** rather than silently skipping it.

## Known gaps in the source material

| Missing | Extent |
|---|---|
| Trap bodies, objective catalog | 104 entries, 33 titles — but it slices the same material as the complete family catalog |
| Five-condition eligibility check | Behind "I already have source data"; only matters if you skip the starter kit |

**Retired, not missing:** the Fundamentals page was merged into Stumping
essentials on 8/27 and its numbered twelve model failure behaviours were condensed
to prose. The `Targets 02 … 08 …` fields on every trap and the FAQ's "Stumping
2–3" references are orphaned pointers. The prose behaviours and the design rule
are captured; the numbering is gone from the site.

**Recovered:** all 83 family traps with full bodies · the six invalid-stump
patterns · 41 of 51 Readiness checks · all five validation gates · the layering
model and composition rules · the rollout diagnosis playbook · the complete rubric
spec · the full FAQ including size and licence limits · 60 example prompts · the
12-step walkthrough.

The skills say so where it matters. When something is named but not described, say
that rather than reconstructing it.

## Sources newer than the handbook capture

The spec changed twice in nine days. **8/27 is current and superseded 8/18
wholesale.** Most handbook pages still carry pre-8/18 numbers.

| Source | What it fixes |
|---|---|
| **8/27 update** — `8-27-updates.md` | 3+ deliverables (no ceiling) · two **assigned** format families · 3+ asks per file · rubric **generated and uneditable**, 25+ criteria, weighted 30/5–10/60 · **top-two-of-12 average under 50%** replaces stumping *(bar raised to 70% on 9/01)* |
| **Task walkthrough** — `task-walkthrough.md` | The real authoring sequence: 12 steps, 3 phases, 4 hard gates |
| **Example prompts** — `example-prompts.md` | 60 prompts in the current format, 10 per objective |
| **Live project page** | $800/task. Describes the work as sourcing "real **occupational** materials" for tasks forcing models onto "occupation-specific tools and instructions" — a framing the six analytical domains do not use |

All folded into `shared-references/canonical-rules.md`, which carries a
stale-numbers table naming every page still carrying a wrong figure.

## Naming Convention

All Project Mark skill folders use the `mark-` prefix, to prevent clashes with
Project Hedgehog (`handshake-*`), Project Lizard (`lizard-*`) and Project Gaffer
(`gaffer-*`).

## Source Material

The read-only handbook capture lives outside this repo:

- `HANDSHAKE-AI/Project-Mark/` — the extracted handbook
- `HANDSHAKE-AI/Project-Mark/examples/` — 25 accepted tasks with golden deliverables
