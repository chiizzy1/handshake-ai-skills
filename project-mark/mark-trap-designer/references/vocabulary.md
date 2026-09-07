> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Trap Vocabulary

Working definitions. Where a term is used loosely elsewhere, this wins.

## Bait

The clean, polished file that directly supports the wrong answer. It is genuinely
stale, wrongly scoped, or computed on the wrong basis, and it is **named to sound
authoritative** — `exec_summary`, `APPROVED_final`.

A model that trusts the tidiest summary lands on the bait's conclusion and stops.

**Why it matters:** without a bait there is nothing for the model to fall for, so
the task tests patience rather than reasoning.

Note the word *genuinely*. Post-8/18, the bait is wrong for an honest reason —
stale, wrongly scoped, wrong basis — never because a number in it was planted
false.

## Antidote

The correcting fact that makes the trap fair. The row, footnote, changelog line,
or raw export that shows why the bait is wrong.

The antidote must be **reachable but not readable in the same glance as the
bait**, otherwise the trap is trivial.

**Why it matters:** bait without an antidote is an unsolvable task, not a stump.

## Arbiter

The file that settles a conflict between two sources: the data dictionary, the
pipeline changelog, the memo that says which definition took effect when.

When two files disagree, the arbiter decides which one governs.

**Why it matters:** the arbiter is what makes a contradiction deterministic
instead of ambiguous. A contradiction with no arbiter is a determinism bug.

## Deterministic

One defensible conclusion follows from the shipped files. Ten competent analysts
working independently land on the same recommendation, **even if they take
different routes to get there.**

Determinism is about the conclusion, not about the method.

## Reinforcement learning environment (RLE)

The harness that hands a model your prompt and your input files, collects its
responses, and scores them. Your task becomes an RLE once accepted: the prompt is
the instruction, the files are the environment, the solution defines correctness.

**Why it matters:** you are not writing a quiz, you are building an environment a
model gets trained and evaluated against.

## Reward

The score a model run earns, 0 to 1, for how well its response matches the
solution. Reported as the mean across runs for that model. **Lower reward means
the task stumped the model harder.**

## Strong model / weak model

Pre-8/27 terms. The old rollout split 8 responses into strong-model (1–4) and
weak-model (5–8) tiers with separate thresholds.

**8/27 retired the split.** Only the **top two** responses are graded now; the
rest are submitted unchecked, and the task passes when those two **average under
70%** (9/01; was 50%). There is no tier distinction and no per-tier threshold.

The terms still appear on stale handbook pages. Read them as historical.

## Role, in a recipe

Each layer of a composed trap plays one of three roles:

| Role | What it does |
|---|---|
| **Gate** | A constraint that rules out the apparent winner — a capacity limit, an eligibility rule, a threshold |
| **Flip** | A correction that changes the ranking once applied |
| **Confirmation** | Evidence that appears to corroborate the wrong answer, so a partial analysis feels finished |

The three should push toward the **same** wrong answer, so a partial analysis
plausibly lands there rather than stalling.
