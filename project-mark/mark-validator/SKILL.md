---
name: mark-validator
description: Validate and submit a Project Mark task. Use for the five validation gates (reproduce, fork, live trap, neutralize-one-trap, remove-one-file), the one-pass rubric review and its fixed weights, the eight-response rollout and its scoring bar, classifying rollout divergence, and clearing the 51 Readiness checks before submitting on Handshake.
---

# Project Mark — Validator

Everything between a finished golden set and a submitted task. Work the gates in
order. Nothing here grades your task — these are your own reads, and **the rollout
is the evidence.**

## Hard Gates

- **Never claim a gate you did not run.** "Not run" is an honest status. "Pass" is
  a claim, and a reviewer will find out.
- **Never edit the prompt or the package after the recorded rollout** without
  rerunning it. The graded evidence has to match what you ship.
- **A response that beats your golden on a better-supported path is a golden
  defect**, not a response error. Repair the task at the source.
- **The fix for a misbehaving task is almost always the prompt or the input
  files, not the rubric.**

## The Five Gates

### Gate 1 — Reproduce

Prove the golden comes back out of the frozen archive, so every later gate tests
the task you will actually ship.

Freeze the archive and ship a manifest listing every file with its **SHA-256
hash, byte size, and role** — `../tools/mark_manifest.py` produces it.

Re-run the golden against that frozen archive and reproduce every load-bearing
finding from the actual files: filters, joins, denominators, cohort and sample
inclusion rules, transformations and normalization, time windows, superseding
revisions, thresholds, QC and variant-filtering rules, exposure and outcome
definitions, comparison groups. For predictive work also: target definition,
leakage checks, training and evaluation periods, split design, metric, forecast
horizon.

**Pass:** the golden reproduces end to end, with no step depending on knowledge
outside the files.
**Revise:** a finding only reproduces with an assumption living in your head, or a
hash changed without a re-run.

### Gate 2 — Fork

Prove the task has one defensible recommendation, not two. A fork here is a
determinism bug, not difficulty.

Re-solve under **each** defensible expert choice: alternative dedup keys,
inclusive versus exclusive date bounds, null handling, outlier rules, population
or cohort definition, metric choice, time window, analytical method. For
statistical or predictive work: reasonable model specifications, validation
splits, normalization choices, multiple-testing handling.

The winner must also survive estimation variation — confidence intervals,
forecast uncertainty, reasonable metric choices. **A knife-edge winner that needs
one exact computation fails.**

**Pass:** every defensible analytical choice lands on the same recommendation.
**Revise:** any defensible choice changes it. Pin the open definition in the
prompt or the files.

### Gate 3 — Live trap

Prove each trap is load bearing, and that every counted file earns its place.

**Neutralize-one-trap test.** Repair one trap at a time, leaving the others in
place, and re-solve. The trap is live only when mishandling it moves something
that matters: a load-bearing intermediate value, the interpretation, the ranking
of options, the prediction, or the recommendation. A trap whose repair changes
nothing is decorative. A trap that only catches careless reading or an absurd
analytical choice is not a trap.

**Remove-one-file test.** Delete each counted input in turn and re-solve. Record
per file whether the answer becomes unreachable, changes, or survives untouched.
A counted file that survives removal is not load bearing.

State, per trap, **why a strong analyst would plausibly take the bait.**

**Measuring difficulty:** wall-clock solve time is not evidence. Use evidence
coverage — the inputs a correct answer must actually touch — and decision
materiality — what the recommendation loses when each trap is missed.

### Gate 4 — Rubric review

One pass. See below.

### Gate 5 — Rollout

Eight responses. See below.

## Rubric Review — One Pass

The rubric is generated internally from your prompt contract and golden set. You
do not write it from scratch and you do not need to rewrite it to make it yours.

**Fix:** an ask with no criterion · two criteria grading the same thing · a weight
that misreads what decides the task · a criterion the golden output would fail.
**Leave alone:** phrasing, ordering, style. Rebuilding wastes time and introduces
drift between the rubric and the golden.

### Fixed weights

| Component | Weight |
|---|---|
| The single main recommendation, one atomic criterion | **Exactly 50%** |
| Supplementary answers, qualitative conclusion, output-file compliance | The other 50% |
| Output-file compliance | 2 to 5 points, taken **out of** the supporting 50, never added on top |
| Any single supplementary question | No more than 25% |
| Total | Exactly 100% |

### What a good criterion evaluates

Criteria grade **observable outcomes in the answer** — the conclusion reached, the
values reported, the questions answered, the file delivered. They never grade how
the analyst thought.

| Topic | Good | Bad |
|---|---|---|
| Reaching the conclusion | States the regression and recommends reverting only that surface, with direction and magnitude consistent with the shipped data | Explains its full chain of thought before answering, showing every intermediate calculation |
| Method | Reaches a result the shipped files support, by any defensible route | Requires a two-proportion z-test on the deduplicated holdout specifically |
| Numbers | Reports the corrected lift with correct sign, unit and rounding, allowing equivalent representations and reasonable tolerance | Requires the exact string "+0.62pp, z = 2.45" |

**Never reward disclosure.** A criterion that awards points for showing work,
naming a method, or narrating steps rewards verbosity instead of correctness. If a
step genuinely matters, grade the result it produced.

Write numeric criteria so equivalent representations pass: "0.62 percentage
points", "+0.62pp", and "roughly six tenths of a point in favour of treatment" are
the same answer. Allow reasonable calculation tolerance rather than string
matching.

### One-pass checklist

- [ ] The main recommendation is one atomic criterion worth 50%
- [ ] Every requested supplementary answer is covered exactly once
- [ ] The qualitative "why" is covered without demanding an essay the prompt never asked for
- [ ] The prescribed file format is covered at 2 to 5%
- [ ] No two criteria overlap or contradict each other
- [ ] The golden output satisfies every positive criterion
- [ ] Nothing rewards methodology disclosure or chain-of-thought
- [ ] Weights sum to 100%

## The Rollout

Eight responses, scored against the confirmed rubric.

- **Responses 1 to 4 are strong-model.** A qualifying stump scores **below 50%**.
- **Responses 5 to 8 are weak-model.** A qualifying stump scores **below 30%**.
- **Count gate:** at least **2 of Responses 1–4** and at least **1 of Responses
  5–8** must qualify.

Aim the trap at the recommendation. It carries 50% on its own, so a response that
gets it fully correct cannot fall below the strong-model threshold on minor
supplementary details alone. Supplementary asks deepen the evaluation; they never
substitute for the recommendation and must not read as artificial gotcha items.

### Classify every divergence before writing anything down

| Classification | Meaning | Counts as difficulty? |
|---|---|---|
| **Valid analytical stump** | The response misses decisive evidence, uses a provably wrong method, mishandles data, stops at a misleading artifact, or applies invalid cleaning / filtering / QC / statistical logic | **Yes** |
| **Semantic fork** | The response analyzes correctly but resolves an unpinned objective or convention differently | No — a determinism defect in your task |
| **Golden wrong** | The response follows a reproducible path better supported by the files than your golden | No — a solution defect, repair the golden |

### Never counts as a qualifying failure

formatting-only failures · alternative wording · an invalid or underspecified
prompt · a broken or unsupported golden · a missing file · a grader or packaging
failure · a failure caused only by an arbitrary rubric interpretation

Judge the rollout as a whole: strong-model responses should be making real
analytical errors, not stylistic ones.

## Readiness

**51 blocking checks across 6 stages.** For each: review the requirement, verify
it against your task, add an evidence note naming the file or step that proves it,
then mark it complete.

| Stage | Checks | Covers |
|---|---|---|
| 1. Policy | 6 | File counts, necessity, substantiality, distractors, AI-use rules, provenance |
| 2. Task shape | 4 | *Not captured* |
| 3. Inputs | 7 | *Not captured* |
| 4. Prompt and solution | 10 | *Not captured* |
| 5. Trap validation | 24 | *Not captured* |
| 6. Submission | — | *Not captured* |

Only stage 1 survives in the local handbook capture. `references/readiness.md`
holds those six verbatim and reconstructs what the remaining stages test from the
reviewer reference and the gates above. **When a stage is not captured, say so** —
work the equivalent gate in this skill and tell the user the official check text
was unavailable.

Stage 1, all blocking:

1. A task ships with at least ten input files.
2. At least four of the shipped files are independently necessary: remove any one and the solution can no longer be reached.
3. At least two of the inputs are substantial rather than token.
4. Optional distractor files are allowed and encouraged, but never count toward the four independently necessary files.
5. AI may be used to locate data or write transformation scripts, but never to create the empirical source evidence itself.
6. Scenario documents and derived files carry explicit provenance stating what they are and how they were produced.

## Final Handoff

Three steps, in order, all done by you:

1. Export evidence.
2. Open Handshake.
3. Confirm submission requirements, and submit.

Before submitting, confirm the prompt, the package, and the golden still agree
with each other after your last edit, and that the workspace has no LLM-generated
files and stays within size limits.

A reviewer picks it up from there and may send notes back. Revisions are normal
and unlimited.

## Output Format

```
## Gate status
| Gate | Status | Evidence |
|---|---|---|
| 1 Reproduce | pass / fail / not run | manifest hash, re-run result |
| 2 Fork | pass / fail / not run | choices tested, all converged? |
| 3 Live trap | pass / fail / not run | per-trap neutralize result, per-file remove result |
| 4 Rubric | pass / fail / not run | weights, 8-point checklist |
| 5 Rollout | pass / fail / not run | scores, count gate |

## Rollout
| Response | Model tier | Score | Qualifies? | Divergence class |
|---|---|---|---|---|
Count gate: <n> of 1–4 below 50% (need 2) · <n> of 5–8 below 30% (need 1) — ✓/✗

## Readiness
Stage 1 Policy: <n> of 6
Stages 2–6: <n> of 45 — official check text not captured, worked via gates above

## Blockers remaining
<list, or none>
```

Report what was actually run. Every "pass" needs the evidence beside it.
