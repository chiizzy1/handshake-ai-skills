---
name: mark-validator
description: Validate and submit a Project Mark task. Use for the five validation gates (reproduce, fork, live trap, neutralize-one-trap, remove-one-file), the generated 25+ criteria rubric and its 30/5-10/60 weights, the 12-response rollout and the top-two-average-under-50% pass bar, classifying rollout divergence, and clearing Readiness before submitting on Handshake.
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

The five gates are **Reproduce · Fork · Live trap · Robustness · Rollout**. They
sit between a drafted trap and a first rollout, and each names what to test, what
passing looks like, and the signal that sends you back to revise.

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

### Gate 4 — Robustness

**Purpose: prove the winning recommendation survives ordinary expert variation,
not just the one computation you ran.**

**What to test**

- **Vary the estimation:** confidence intervals, forecast uncertainty,
  alternative model specifications, and reasonable metric choices.
- **Run the knife-edge check:** a winner that needs one exact computation to stay
  ahead **is not validated**.

There is a specialised lens for *predictive or statistical work* that turns on only
when it applies to your task. Its contents were collapsed in every capture.

**Pass:** the same option wins across reasonable estimation variation.
**Revise:** the recommendation flips under normal estimation noise.
**Next:** move to Rollout and hand the archive to someone who did not build it.

### Gate 5 — Rollout

**Purpose: prove the task is solvable cold, clean to ship, and reported honestly.**

**Archive-only blind solve.** Hand the archive and the prompt to someone who did
not build the task and have them solve it cold. Confirm the workspace is coherent:
necessary files can be connected, identifiers and joins are recoverable, versions
and revisions reconcile, the valid population or period is identifiable from the
supplied documentation, **definitions are pinned by a document rather than by
intent**, and any conflict between sources is resolvable from the materials alone.

> Any step that needed outside context, a guessed definition, an unstated
> threshold, or evidence not in the archive is **unfair ambiguity, not analytical
> difficulty**. Any step that needed builder memory is an **undiscoverable
> convention**.

**Compliance pass.** Check the prompt for leaks, the corpus for personal data, and
every artifact for provenance and licensing **before the archive is frozen**.

> A named file, a method verb, a real person's data, or an unlicensed source is a
> **submission blocker regardless of how good the trap is**.

## The Rubric — You Do Not Edit It

**Generated internally from three things you already produced: the prompt
contract, the golden solution, and the requested output files. You do not write it
and you do not edit it. It arrives fixed.**

There is no review pass anymore. If the rubric looks wrong, **the fix is
upstream** — correct the prompt contract or the golden output, and the rubric is
regenerated from the corrected pieces.

Your job is to build a prompt, a golden, and an evidence package strong enough
that the generated rubric is hard for a model to satisfy.

### The 25-criteria floor

**A task cannot move on under 25 criteria.** Breadth is what forces a model to be
right across the whole task, not just on the headline call, so the surface has to
be wide.

### Weighting — three blocks totalling 100%

- [ ] About **30%** sits on the deterministic recommendation and its critical components, **split across 3 or more criteria**
- [ ] **No single criterion carries more than 20%** of the total score
- [ ] **5 to 10%** covers instruction-following: the requested files and the output-shape asks
- [ ] About **60%** covers the supplementary questions and asks, which must be **hard and discriminating, never trivial lookups**
- [ ] **Unit and rounding fold into the value criterion they belong to**, never their own criteria
- [ ] All criteria total 100%

**What instruction-following covers:** the file is present and named as asked, one
row per period, a required total row, a named column set, a specified ordering, a
page length, or printing the required figures.

Because supplementary is the largest block, **the supplementary questions carry
most of the difficulty. A wrong analytical path should get them wrong. A question
a model can answer with a surface lookup does not belong in this block.**

### What a good criterion evaluates

Criteria grade **observable outcomes in the answer** — the conclusion reached, the
values reported, the questions answered, the file delivered. They never grade how
the analyst thought.

| Topic | Good | Neutral | Bad |
|---|---|---|---|
| Reaching the conclusion | States that mobile web regressed and recommends reverting only that surface, with direction and magnitude consistent with the shipped data | Names the regression but leaves the recommended action implicit | Explains its full chain of thought before answering, showing every intermediate calculation |
| Method | Reaches a result the shipped files support, by any defensible route | Mentions a method without tying it to a result | Requires a two-proportion z-test on the deduplicated holdout specifically |
| Numbers | Reports the corrected lift with correct sign, unit and rounding, allowing equivalent representations and reasonable tolerance | Reports the right value with a missing unit | Requires the exact string "+0.62pp, z = 2.45" |

Numeric criteria are written so equivalent representations pass: "0.62 percentage
points", "+0.62pp", and "roughly six tenths of a point in favour of treatment" are
the same answer. Reasonable calculation tolerance is allowed rather than string
matching.

**Never reward disclosure.** A criterion that awards points for showing work,
naming a method, or narrating steps rewards verbosity instead of correctness. If a
step genuinely matters, the result it produced is graded, not the fact that it was
mentioned.

### What the generated rubric guarantees

You do not tune these by hand; you make them true **upstream, in the prompt and
the golden**.

- [ ] The rubric holds **25 or more criteria**
- [ ] The deterministic recommendation and its critical components carry about **30%**, spread across **3 or more criteria**
- [ ] **No single criterion is worth more than 20%**
- [ ] Instruction-following covers the requested files and output-shape asks at **5 to 10%**
- [ ] The supplementary block is about **60%** and every question in it is **hard and discriminating**
- [ ] Every requested ask is covered **exactly once**, with no two criteria overlapping or contradicting
- [ ] The golden output satisfies **every positive criterion**
- [ ] Nothing rewards methodology disclosure or chain-of-thought
- [ ] Weights sum to **100%**

### If the rubric lands under 25

The repair is in the prompt, using the five levers:

1. Three different findings, not one restated
2. One criteria-dense visual with its parts named
3. A second decision axis
4. A breakdown with an explicit grain
5. A robustness or validity check

Every criterion is a distinct, determinate answer a wrong analytical path would
get wrong. **Do not pad with rounding or units, and do not count one fact twice
because two files display it.**

## The Pass Bar

**"Stump the model" is retired as a phrase, but the operational reality is
narrower than the handbook implies.**

### How the 12 responses actually split

| Stage | Responses | Gate |
|---|---|---|
| **Step 3 — stump check** | **2** initial responses | **This is the gate.** These are the two that must average under 50% |
| **Step 12 — final rollouts** | **10** more | **No stumping bar.** They must simply not crash |

The task UI says it outright: *"You can submit after the models finish running. No
stumping bar."*

Confirmed by Handshake staff in Slack:

> **Vincent (Handshake AI):** "don't worry about the last 10 rollouts, no stump
> requirement there for now. as long as they don't crash"

> **James Cl. (Specialist):** "The model runs in the final 10 rollouts should
> mirror what has been seen in the earlier models. If you were able to get rubric
> scores to be less than 50% from the models at the start of the task, you should
> see models continue to not provide your golden solution at the bottom."

This resolves every apparent contradiction. "Twelve responses", "the top 2 are the
gate", "submit the bottom 10 unchecked", and step 12 being "non-blocking" are all
describing the same thing: **2 graded + 10 ungraded = 12.**

**Practical consequence:** you find out whether the task works at **step 3**, long
before the golden and deliverables are finished. If the two initial responses do
not come in under 50%, strengthen the task then — not after building everything.

> Vincent's "for now" is doing work. This is an operational relaxation, not a
> published rule. Re-check in Slack before relying on it for a task you have
> already built.

### What counts as stumped

A response counts as meaningfully stumped if it **gives the wrong recommendation**
*or* reaches the correct decision **through materially incorrect analysis**. Read
the actual recommendations, not the formatting.

**Aim the trap at the main recommendation.** It anchors the deterministic answer,
so a response that gets it fully correct should not fall below the threshold merely
by missing minor supplementary details.

### If the model is not stumped — open the environment view

The hidden **environment** view contains the model's full reasoning artifacts.
Check `analysis_report.md` and `analysis.py` from each model. **These show the path
the model took to reach its answer** — use them to identify weak spots in its
approach and design a better trap.

That is the single most direct debugging tool on the project, and it is not
mentioned anywhere in the handbook.

### Never counts as a qualifying failure

formatting-only failures · alternative wording · an invalid or underspecified
prompt · a broken or unsupported golden · a missing file · a grader or packaging
failure · a failure caused only by an arbitrary rubric interpretation

**The consequence of the reweighting:** the recommendation and its critical
components carry ~30% of the rubric and the supplementary questions ~60%, so **a
response cannot stay above 50% on the recommendation alone**. The supplementary
asks have to be hard and discriminating, or the top two will clear the bar too
easily.

## Diagnosing A Rollout

Captured from Validation & Iteration. This is what to do when the responses come
back, and it is the most actionable material on the project.

### Calibration targets

**Heuristic targets, not tests.** They tell you which gate to strengthen when a
rollout comes back off-target.

| | Weak model under 30% | Strong model under 50% |
|---|---|---|
| **Fails at** | Breadth of file coverage, long-file reading, any join beyond one key, row-count anomalies, multi-step arithmetic, resisting the bait | Silent statistical traps, chronology and supersession reasoning, identifying the valid population, overturning the stakeholder's frame, combining several correct sub-analyses into a counterintuitive conclusion |
| **Lever** | Layer 1 gate plus the bait file | **Layers 2 and 3, drawn from different families** |

**If a weak model is scoring 25 to 35 percent, the usual culprit is a rubric with
too many easy positive criteria, not insufficiently hard data.**

### Failure-texture diagnosis

Where the wrong answers landed tells you what the task actually tested.

| Texture | Reading | Verdict |
|---|---|---|
| **Consensus on your designed decoy** | Every wrong response lands on the bait's answer and you can name the analytical step it skipped. The trap is working exactly as built | **Healthy** |
| **Consensus on an answer you did not design** | There is a second self-consistent reading of your materials. That is a determinism bug on your side. **Fix the files, do not submit** | **Red flag** |
| **Scatter across different wrong answers** | Responses dying at different layers is a good sign, but scatter plus low-effort responses suggests unfair ambiguity rather than difficulty | Usually healthy |
| **Zero partial progress anywhere** | All near-zero reads as impossible to reviewers. The sweet spot is one or two attempts making real partial progress while the recommendation is still missed on average | **Watch it** |

### Required rollout reporting

**Any threshold you cite is meaningless without its denominator.**

- The model and version string for every model in the rollout
- Run count per model, and the exact pass denominator used
- Rubric version the responses were graded against
- Where transcripts are retained, and for how long
- Which thresholds are hard gates and which are soft
- For each failed response, **the substantive analytical mistake behind the wrong
  result, not just the wrong answer**

### The iteration loop

1. Read the passing response and find the **defusal moment** — the exact step where
   it caught the trap.
2. Trace every failure back to the analytical mistake that caused it. **If you
   cannot name the mistake, you cannot defend the stump.**
3. **Fix the leak, not the difficulty.** Most passing responses were tipped off
   rather than brilliant.
4. **Repair at the source rather than through the rubric:** correct the golden, add
   the missing evidence, pin the definition, strengthen the trap, widen the
   decision margin, or remove complexity that does no analytical work.
5. If the response legitimately reasoned through it, add a layer **from a different
   family than the one it beat**.
6. If responses fail but the stumps are invalid, **determinism is the problem**.
   Tighten the files until competing approaches converge.
7. **Re-run the golden after every change. A 100 percent self-score is your
   regression test.**

**Pass condition:** a cold solver reaches your recommendation from the archive
alone, the compliance pass is clean, and the rollout report carries its
denominator.

**Revise signal:** a step needed outside context or builder memory, a name, method
or personal record leaked, or the number was cited without its denominator.

**When responses keep passing:** find the defusal moment and pull a new layer from
a different family.

## Quality Checks And Review

The platform runs **Quality Check scripts** the handbook never mentions. They
scour the task for weakness and suggest edits — run them when models keep solving
your task.

**Only one thing blocks submission: a Quality Check saying there is no stump.**
Every other check can be disagreed with, in writing, with a rationale.

**The Quality Check is not the reviewer.** It is preliminary, and it cannot see
the model responses or the analysis report. A task can pass every check, get a
stump, and still come back for edits.

Verdicts, tracking, payment and throttling: `references/quality-check-and-review.md`.

| Verdict | Meaning |
|---|---|
| `prelim_verdict` | Deterministic, correct solution, passed preliminary difficulty and duplicate checks. **"98% there"** |
| `final_verdict` | Comprehensive review for difficulty and duplication. **98% of prelim passes also pass final** |

An approved status **changing** is the process working — prelim can precede a
different final.

## Readiness

**51 blocking checks.** All 41 substantive ones are captured verbatim in
`references/readiness.md`, grouped by the page you fix each on.

| Group | Checks | Fix on |
|---|---|---|
| Policy and input package | 6 | 02 Input Files |
| Task shape | 4 | Task types |
| Prompt | 4 | 03 Prompt |
| Rubric and rollout | 3 | Writing the prompt |
| Golden deliverable | 3 | 04 Golden Deliverable |
| Trap design | 14 | Fundamentals |
| Trap composition | 5 | Composition & Recipes |
| Trap validation | 5 | Validation & Iteration |

**Trap design is the largest group by far** — 14 of 41. That is where a task most
often fails, and it is why the trap gets designed before the prompt.

One check on the page is stale: it still asks for "three to five related
supplementary questions drawn from the defined buckets", which is pre-8/27. Build
to 3+ deliverables with 3+ asks each.

The **trap trace table** sits inside the Trap validation stage on its own tab —
one row per trap: a purpose, a location, a correction path, and an observable
effect.

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
| 4 Rubric | pass / fail / not run | criteria count vs 25 |
| 5 Rollout | pass / fail / not run | top-two average vs 50% |

## Rollout
| Response | Score | Rank | Divergence class |
|---|---|---|---|
Top two: <score> and <score> — average <n>% (must be under 50%) — ✓/✗
Bottom 10 submitted unchecked.

## Readiness
Stage 1 Policy: <n> of 6
Stages 2–6: <n> of 45 — official check text not captured, worked via gates above

## Blockers remaining
<list, or none>
```

Report what was actually run. Every "pass" needs the evidence beside it.
