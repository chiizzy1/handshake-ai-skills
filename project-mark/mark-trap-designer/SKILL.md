---
name: mark-trap-designer
description: Design the trap that makes a Project Mark task hard. Use when choosing or layering the analytical traps a task is built on — the six trap families, the four fairness criteria, the honest-data doctrine that replaced planted defects, recipe composition across families, and the fit checks that prove a trap is discoverable, consequential, deterministic and fair.
---

# Project Mark — Trap Designer

**Design the trap first, before the prompt.** A prompt written first signposts
the catch. Write the trap, then write the message a stakeholder would send if the
trap were invisible to them.

Stumping means a strong model gets a genuine analytical or methodological
question wrong while a careful analyst gets it right using only what was shipped.
**A different final sentence is not a stump.** The failure has to trace to a real
mistake: the wrong denominator, an invalid join, a mishandled cohort, an
unjustified causal claim, an invalid validation scheme.

## Hard Gate — Honest Data

The "flip the wrong number" trap is **retired**. A task built on a planted defect
gets returned.

The shape to avoid: a number is stated or clearly implied to be true, turns out
to be false once you dig deep enough, and catching that lie is the whole
challenge. That is not realistic, and once a model expects "something here is
secretly wrong", you have stopped testing analysis and started testing plant
detection.

Two rules keep it honest:

- **Do not stake the whole task on a hidden defect.** A messy or misleading
  detail is fine as texture, but the task has to stay hard *after* the model
  notices it. If spotting the trick is the whole game, the task fails.
- **Let the numbers be right.** Make the challenge a tempting adjustment that
  would wrongly talk the model out of a correct figure, or move it off the numbers
  entirely — into forecasting, method selection, a binding constraint, or a
  decomposition — all on data that is not lying.

| Shape | Retired (planted defect) | Valid (honest data) |
|---|---|---|
| Mixed or hidden subgroups | The extra "sessions" are secretly background wakes; strip them and the lead reverses | The lead is real and correctly reported. The trap is a tempting adjustment that would wrongly flip it |
| Conceptual or definition swap | The stated metric is a mislabel you have to catch | Both metrics are measured correctly. The work is choosing the one the problem structure requires |
| Coverage gap | Half the period is hidden in a third extract; find it and the answer flips | Every extract is present. The top-ranked option breaks a capacity limit, so the answer is the next option that fits |
| Mislabeled or miscategorized | Two brokers stamp "launch" at different moments; realign and the leader changes | Label semantics are documented and consistent, just spread across feeds. The work is conforming them to one definition |
| Clock or timing artifact | Timestamps are secretly UTC, not the documented local zone | Timestamps are correct and consistent. A known schedule change makes the next period genuinely differ |
| Wrong denominator | Zones vary hugely in size, so the rate secretly uses the wrong denominator | The rate and denominator are both correct. A real capacity or clawback limit caps which option is feasible |

## Four Fairness Criteria

Always in force. Every trap answers to all four.

| Criterion | Meaning |
|---|---|
| **In-corpus antidote** | Every deception has a correcting fact inside the files. Supersession is reconstructible from dates and documents. |
| **Deterministic outcome** | Ten competent analysts reach the same recommendation. All defensible cleanings converge. |
| **No parsing puzzles** | Every file loads with standard tooling in one or two obvious attempts. Difficulty is spent on reasoning, not input and output. |
| **No fabricated source data** | No LLM-generated files, no augmentation, no model-written memos. A self-written memo is a scenario document, not source data, and is recorded as such. |

### Discoverable

The model must be able to find, inside the prompt, files, and standard domain
knowledge, everything it needs to reject the wrong path. A fair trap may ship
evidence that encourages the wrong reading — the material that overturns it must
be present.

**Not discoverable:** a required rule or definition is absent · a necessary file
was never shipped · the analyst has to guess an unstated threshold · the deciding
fact lives outside the provided materials.

The strongest traps live **between** files: reconciling a summary against raw
records, joining at the wrong grain, a definition buried in supporting
documentation, one file that silently supersedes another.

### Consequential

Catching the trap has to matter. If the recommendation, an interpretation, or a
decisive intermediate result would be identical whether or not the model corrects
course, the trap is decorative.

### Deterministic

If the final answer changes depending on a reasonable but unpinned choice of
metric, scope, population, threshold, time window, or definition, the task is
underspecified — not hard.

### Fair

Semantic ambiguity, missing information, and arbitrary gotchas are disqualifying
even when they make a task hard. The prompt and supporting documents must never
narrate the trap: never say which file is misleading, which metric is wrong,
which join to avoid, or which conclusion is expected.

**No complexity for its own sake.** A task is not harder because it has more
files, rows, or formats. Irrelevant files, duplicated information, arbitrary
noise, and volume that only creates search burden all count against fairness.

## Valid Failure Versus Invalid Difficulty

| Topic | Valid | Invalid |
|---|---|---|
| Source of the failure | A genuine analytical mistake: wrong cohort, invalid method, missed reconciliation | An undefined term, unstated threshold, or missing fact |
| What correcting it looks like | Recovering evidence already in the workspace and revising the recommendation | Guessing at a definition nobody pinned down |
| Whether experts agree on the fix | Every competent analyst converges on the same corrected answer | Equally reasonable experts could defensibly disagree |
| What ships in the prompt | Evidence that makes the correct path findable | A hint, or narration, of what the trap is |

If two strong analysts could reasonably choose different definitions, thresholds,
scopes, metrics, populations, or time windows, and nothing resolves the choice,
that is an **underspecified task**, not a stump.

## Preflight

Confirm all five before going looking for a trap.

- [ ] The failure is a genuine analytical or methodological mistake, not a different final sentence
- [ ] No reasonable expert could defensibly choose a different definition, threshold, or scope and still be right
- [ ] The evidence that corrects the wrong path is present in the workspace, not narrated in the prompt
- [ ] A careful analyst using the materials correctly always lands on the same recommendation
- [ ] Catching the trap changes the recommendation or a decisive intermediate result, not just wording

## The Six Families

| Family | Name | The shape | Entries |
|---|---|---|---|
| A | Aggregation and statistics | The number is computed correctly and still means the wrong thing | 17 |
| B | Experiment and causality | The comparison looks clean but the design underneath it is broken | 17 |
| C | Time and comparability | Two periods placed side by side that were never comparable | 13 |
| D | Plumbing and joins | The data loads fine and the grain, keys, or units are lying | 18 |
| E | Documents and formats | The decisive fact is present, just not where a skim will find it | 12 |
| F | Definitions and framing | The metric named in the prompt is not the metric the decision needs | 6 |

Named traps, the parallel objective-indexed catalog, and the 14 worked recipes
are in `../shared-references/trap-catalog.md`.

**That file is a partial capture.** 34 of 83 family traps and 33 of 104 objective
traps are named, and **none** carries its failure mode, example, or antidote. When
a trap is named but not described, say so — do not reconstruct a body from a
title. The 14 worked recipes and the 25 examples under
`HANDSHAKE-AI/Project-Mark/examples/` carry real traps end to end and are the
reliable substitute.

## Composition

**Single traps get caught by strong models about half the time.** Layer a gate, a
flip, and a confirmation from **different families**, then check that all three
push toward the same wrong answer, so a partial analysis plausibly lands there.

Every layer must materially change the answer on its own. A layer that only adds
reading time is decoration, and it makes the task longer without making it
harder.

The 14 worked recipes in the shared trap catalog are the pattern library. Take
one and build it out rather than starting from a blank page. Every pattern is
domain-transferable: the same shape works in an operational, economic, policy, or
demographic workspace once the subject matter is swapped.

## Fit Check Per Trap

For each trap in the recipe, state all five before committing:

| Field | What to write |
|---|---|
| Role | Gate, flip, or confirmation |
| Bait | The clean, polished file that supports the wrong answer. Genuinely stale, wrongly scoped, or computed on the wrong basis, and named to sound authoritative |
| Antidote | The row, footnote, changelog line, or raw export that shows why the bait is wrong. Reachable, but not readable in the same glance as the bait |
| Arbiter | The file that settles the conflict — data dictionary, pipeline changelog, the memo saying which definition took effect when |
| Decision impact | What the recommendation loses when this is missed: the decision itself, its scope, its justification, or its robustness |

Why a strong analyst would plausibly take the bait — state it. If you cannot,
the trap is not tempting and the models will not fall for it.

## Output Format

```
## Trap design

Objective: <Axis 1 objective>
Recipe: <n> layers across <n> families

### Layer 1 — <family/ID if known> <title>
Role: gate / flip / confirmation
Bait: <file> — <why it is genuinely misleading, not planted false>
Antidote: <file, location> — <the correcting fact>
Arbiter: <file>
Decision impact: <what the recommendation loses if missed>
Why a strong analyst takes the bait: <...>

### Layer 2 ...

## Fairness check
In-corpus antidote ✓/✗   Deterministic ✓/✗   No parsing puzzles ✓/✗
No fabricated source data ✓/✗
Discoverable ✓/✗   Consequential ✓/✗   Fair ✓/✗

## Honest-data check
Is the whole task staked on a hidden defect? yes/no
Does the task stay hard after the model notices the messy detail? yes/no
```
