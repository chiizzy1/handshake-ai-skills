---
name: mark-task-builder
description: Build a Project Mark analytical task for Handshake AI. Use for authoring a task that stumps frontier models — sourcing a 10+ file input package, writing a prompt that commits one deterministic recommendation with two or more named deliverables, producing the golden deliverable set, reviewing the generated rubric, and clearing Readiness. Routes to the input, prompt, trap, golden, and validation skills. Project Mark is a production project, not a rating project.
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
| Exactly one output file | **2 or more across at least two families** |
| 3 to 5 standalone supplementary questions | **At least two asks per named deliverable** |

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

## Workflow

Nine steps. The conceptual relationship between prompt, inputs and golden is not
the build order — build in this order.

### 1. Pick the domain and objective

One of six domains, one Axis 1 objective. Chosen before you write a word of the
prompt. See `references/domains-objectives.md`.

Forecasting & Predictive Modeling is an objective, not a seventh domain, and more
of those are wanted.

### 2. Draft the trap — before the prompt

This is out of intuitive order and it matters. A prompt written first signposts
the catch: it names the metric that matters, or fixes a window that quietly rules
the trap out. Write the trap, then write the message a stakeholder would send if
the trap were invisible to them.

→ **`mark-trap-designer`**

### 3. Assemble the input package

10+ files, 4+ independently necessary, 2+ substantial, 3+ formats, one table with
10,000+ rows, joins required, provenance recorded per file.

→ **`mark-input-package`**

### 4. Write the prompt

One deterministic recommendation, 2 or more named deliverables across at least two
format families, at least two asks each. Every numeric ask states its unit and
rounding.

→ **`mark-prompt-writer`**

### 5. Build the golden deliverable set

Every requested file, in the requested format, under the filename the prompt
names. One set of numbers across all of them.

→ **`mark-golden-builder`**

### 6. Review the generated rubric — one pass

It is generated internally from your prompt contract and golden set. Fix genuine
problems only: missing coverage, wrong weighting, contradictory criteria, a
criterion the golden would fail. Leave phrasing alone.

→ **`mark-validator`**

### 7. Run the five validation gates

Reproduce · Fork · Live trap · then the rollout and the scoring bar.

→ **`mark-validator`**

### 8. Run and evaluate the rollout

Eight responses. At least 2 of Responses 1–4 below 50%, at least 1 of Responses
5–8 below 30%.

→ **`mark-validator`**

### 9. Clear Readiness and submit

51 blocking checks across 6 stages. You submit on Handshake yourself.

→ **`mark-validator`**

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
files, never the rubric.**

| Symptom | Where to repair |
|---|---|
| Models keep getting the recommendation right | The trap is not consequential, or the prompt leaks the path. Re-run Gate 3. |
| Two experts could defensibly disagree | Determinism bug. An unpinned definition, threshold, scope, population, metric, or window. Pin it in the prompt or the files. |
| Right answer, wrong reasons, still scored high | The rubric grades disclosure, or a criterion is too loose. One review pass fixes it. |
| Only the strong model fails, or only the weak one | The count gate needs both. Usually the trap is too shallow or too obscure. |
| A response beats your golden on a better-supported path | **That is a golden defect, not a response error.** Repair the golden. |

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
