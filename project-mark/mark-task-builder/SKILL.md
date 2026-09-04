---
name: mark-task-builder
description: Build a Project Mark analytical task for Handshake AI. Use for authoring a task that stumps frontier models — sourcing a 10+ file input package, writing a prompt that commits one deterministic recommendation with three or more named deliverables, producing the golden deliverable set, reviewing the generated rubric, and clearing Readiness. Routes to the input, prompt, trap, golden, and validation skills. Project Mark is a production project, not a rating project.
---

# Project Mark — Task Builder

## What This Task Is

You **author** a task. You are not rating anything, and there is no task file to
mark up. You build a reinforcement learning environment: a package of real files,
a prompt that commits an analyst to one defensible call, and the golden set a
fully correct analyst would hand back. Then you prove frontier models get it
wrong.

$800 per approved task, flat, paid the Wednesday after approval. Revisions are
normal and unlimited.

Roughly seven hours for a first task, around five after. Those are estimates, not
deadlines and not performance thresholds.

## File Locations

- `references/...` is inside this skill's folder.
- `../shared-references/...` is the Project Mark shared folder.
- `HANDSHAKE-AI/Project-Mark/...` is the read-only handbook capture, a sibling of
  this repo in the workspace root.
- If a referenced file cannot be found, use this skill's `references/` as the
  operative guidance and say plainly that the source was unavailable.

## Core Rule — Source Hierarchy

1. **The live Handshake platform** for the task in front of you.
2. **Readiness and the reviewer reference.** These are the blocking gates.
3. **The 8/18 update.** It changed the task shape and the older handbook pages
   were not all updated behind it.
4. The individual handbook pages.
5. This skill, then user preference.

Several handbook pages carry stale pre-8/18 numbers. `../shared-references/canonical-rules.md`
resolves every conflict and is the operative rule table. Read it before quoting
any number to the user.

The three that catch people out:

| Stale | Canonical |
|---|---|
| 6 or more input files | **10 or more, in a single ZIP** |
| Exactly one output file, or 2 to 5 | **3 or more, no upper limit, across the two assigned families** |
| 3 to 5 standalone supplementary questions, or two asks each | **At least three asks per named deliverable** |

## Hard Gates

Three questions decide whether a task gets approved:

> **1. Is there exactly one defensible answer?** Ten competent analysts,
> independently, land on the same recommendation.
> **2. Does every number come back out of the shipped files?** With no step that
> depends on knowledge living in your head.
> **3. Do the models actually fail on the analysis?** Not on wording, not on
> formatting, not on a trick definition.

- **Never fabricate source evidence.** AI may locate data and write
  transformation scripts. AI may never create the empirical evidence. An
  LLM-generated PDF, DOCX, or PPTX gets the task rejected, and they are spotted in
  seconds: a few words per page, oceans of white space, tables that are too clean.
- **Never build a planted lie.** The "flip the wrong number" trap is retired. Let
  the numbers be honest and put the difficulty in method, constraint,
  decomposition, or forecast.
- **Never leak the answer path.** The prompt is silent on scope, cleaning,
  window, and method. It never names the trap, the decisive file, or hints that a
  metric is misleading.
- **Never let numbers disagree across deliverables.** A reviewer diffs them
  against each other. This is the single most common defect.
- **Never claim a check you did not run.** If a gate was skipped or blocked, say
  so plainly. The tools in `../tools/` exist so the checks are real.
- **File count is not difficulty.** A decorative file counts against fairness, not
  for it.
- **Verify sourcing facts on the live web, never from memory.** Specs, licences,
  restriction status and URLs all changed under this project mid-flight. Search,
  fetch the licence page, confirm the download URL — or say you cannot and ask
  the user to. `references/data-selection.md` has the protocol.
- **The dataset sets the difficulty ceiling.** If the correct solution requires
  nothing beyond careful reading and careful coding, current models solve it —
  verified across three live stump checks (`../shared-references/rollout-lessons.md`).
  Pick data with statistical machinery, or do not claim it.
- **Build a thicket, not a gotcha.** The accepted example's answer took eight
  interlocking steps across 28 files in 6 formats. Both of our three-step tasks
  on clean corpora were solved. Governed rules should carry several conditions
  each requiring correct computation, and the corpus should distribute the
  evidence. See `../mark-input-package/references/corpus-construction.md`.
- **The trap must flip the main recommendation.** The recommendation cluster is
  ~30–37 rubric points, so both top responses must get it wrong for the top-two
  average to fall under 70%. Supplementary-only difficulty cannot pass the gate.

## Workflow

Twelve steps, three phases, four hard gates. This is the 8/27 sequence and it
replaces the old nine-step walkthrough.

### Phase A — Set up the task

**1. Task type, domain, and data families.** **Claim the task slot BEFORE
designing anything or claiming a data kit.** One primary analytical objective and
two output format families are assigned per task, and unclaiming/re-claiming
re-rolls them. Read the assignment, then pick the domain and the data.
*Gate: deterministic decision.*
→ **`references/new-task-runbook.md` — the end-to-end sequence for a new task**,
with the mandatory research pass (model-failure literature + candidate data)
and the human-fetch fallback for blocked sources.
→ `references/data-selection.md` — the ceiling test and screening checklist. The
dataset decides the difficulty ceiling; a pre-computed index cannot stump.

**2. Prompt and input files.** Write the ambiguous, stakeholder-style prompt and
upload one ZIP of real, license-clean inputs.
*Gate: 10+ files, 3+ formats, one 10,000+ row table.*
→ `mark-input-package`, `mark-prompt-writer`, and `mark-trap-designer` first

### Phase B — Solve and specify

**3. Model responses.** Generate the model rollout on your prompt and inputs.
Note this happens **before** you commit your own answer.

**4. Final recommendation.** Commit the single deterministic recommendation the
task resolves to.

**5. Supplementary answers.** Answer each per-deliverable ask. **These carry ~60%
of the rubric**, so they must be hard and discriminating.

**6. Critical components.** Record the load-bearing intermediates the
recommendation rests on. Part of the ~30% recommendation block.
→ `mark-golden-builder`

### Phase C — Validate and deliver

**7. Rubric.** Generated for you and **fixed — you do not edit it.**
*Gate: 25+ criteria, weighted 30 / 5–10 / 60.*

**8. Step-by-step solution.** Lay out the path from the inputs to the committed
answer.

**9. Justification.** State why the answer is forced and the difficulty is
honest-data, not a planted lie.

**10. Determinism QC check.** A rollout check that the committed answers are
uniquely forced by the shipped files.

**11. Golden solution.** Ship the finished golden version of every requested
deliverable.

**12. Final model rollouts.** Run the responses against the fixed rubric. Only the
**top two are graded**; the rest are submitted unchecked, and the task passes when
those two **average under 70%**. **Non-blocking** if the top two already hit the
bar on the step 3 rollout.
*The source disagrees with itself on the count — 10 or 12. See canonical-rules.*
→ `mark-validator`

### Where the trap work goes

The twelve steps do not name trap design as its own step, but it still governs
steps 1 and 2. **Design the trap before writing the prompt** — a prompt written
first signposts the catch.

## The four hard gates

| # | Gate |
|---|---|
| 01 | Rubric reaches **25+ criteria**, weighted 30 / 5–10 / 60 |
| 02 | **Top 2 responses average under 70%** (9/01; was 50%) |
| 03 | A deterministic, fair stump on honest data |
| 04 | **3+ deliverables with 3+ asks each**, across the two assigned families |

## What Good Looks Like

| Standard | What it means |
|---|---|
| Deterministic | Competent domain experts converge on the same recommendation. |
| Reproducible | Every number and step in the golden comes back from the shipped files. |
| Analytically difficult | The difficulty lives in reasoning and method, not ambiguous wording. |
| Self-contained | Every load-bearing fact sits in the prompt, the files, or standard domain knowledge. |
| Supported by necessary files | Each shipped file does work; nothing load-bearing is missing. |

## Debugging

When a task misbehaves, the fix is almost always in **the prompt or the input
files** — and since 8/27 you cannot edit the rubric at all, so upstream is the
only repair available.

Full guidance, the file-size and licence limits, and the rules on malformed and
self-made files are in `references/debugging.md`.

| Symptom | Where to repair |
|---|---|
| Models keep getting the recommendation right | **The most common failure.** Task too easy: the obvious first analysis is also correct, the decisive number sits in a summary tab, or the data is clean and pre-joined |
| Two experts could defensibly disagree | Objective not bound to one recommendation. Re-read the prompt as an adversary optimizing a different legitimate goal |
| Right answer, wrong reasons, still scored high | The asks are not discriminating enough. A shortcut satisfies them |
| Top two responses clear 70% | Not hard enough. Deepen the trap or the computation |
| A response beats your golden on a better-supported path | **That is a golden defect, not a response error.** Repair the golden |

## Output Format

Never edit the user's files. Present the task artifacts in the chat reply.

```
## Task
Domain · Objective · The decision in one sentence

## Trap
<family/ID if known> — bait, antidote, what the recommendation loses if missed

## Input package
<n> files · <n> necessary · <n> formats · largest table <n> rows
| File | Role | Format | Source | Pulled | Licence | Necessary? |

## Prompt
<stakeholder context, the committed ask, the named deliverables with their asks>

## Golden set
<file> — <what it answers>
Reconciled figures: <the one set of numbers>

## Gate status
Reproduce · Fork · Live trap · Rubric · Rollout · Readiness
<pass / not run / blocked — with evidence named, never assumed>
```

State plainly which gates were actually run. A gate you did not run is "not run",
never "pass".
