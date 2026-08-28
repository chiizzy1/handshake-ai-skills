# Composition & Recipes

Single traps get caught by strong models about half the time. Layer a **gate**, a
**flip**, and a **confirmation** from different families, then check all three push
toward the **same wrong answer** so a partial analysis plausibly lands there.

## The consequence rule

The single statement that governs every layer.

> **Every layer must be consequential.** At least one missed trap must change or
> invalidate the recommendation, and every remaining layer must independently
> affect its scope, justification, or robustness. **No layer may be decorative.**

## The layering model

Each layer targets a different failure population — this is how you hit both
calibration targets rather than one.

| | Layer 1 · **Gate** | Layer 2 · **Flip** | Layer 3 · **Confirmation** |
|---|---|---|---|
| Type | Exploration trap | Reasoning trap | Synthesis trap |
| Targets | **Weak models** | **Strong models** | **Write-up quality** |
| What it does | Punishes shallow reading: partial duplicates, internal accounts, unit mix, join fan-out | The statistical or causal trap that **reverses the headline recommendation**. The heart of the task | A second independent source that confirms the flipped answer when reconciled, but is itself guarded by a footnote, a stale column, or a definition |
| Drives | **The weak model under 30%** | **The strong model under 50%** | — |
| Example traps | D3 Partial duplicates · D4 Internal and test accounts · D1 Join fan-out · D10 Unit mismatch across files | A1 Simpson's paradox and mix shift · B1 Sample ratio mismatch · C6 Cohort maturity mismatch · C7 Refund and chargeback lag | E1 Footnote overrides the table · D7 Stale derived column · F2 Derivable churn or activation window |

**Layer 2 is the one that matters most.** It is what drives the strong model under
50%, and the strong model is the gate.

## Separating trap and antidote

Separate them at the **visual and analytical level**. The antidote must not be
readable in the same glance or resolvable in the same analytical step as the bait.

A footnote that overrides a table qualifies **when the reader has to leave the
summary read to use it**. A different file is one way to achieve separation, not a
requirement in every case.

## Composition rules

The traps you combine should feel like **one analytical story**: each one gates or
feeds into the next. A response that clears the first trap but misses the second
should still land on a wrong, *plausible* answer, not an obviously broken one.

- **Independent, not stacked on one number.** Spread traps across files and across
  the explore, analyze and synthesize phases, but keep them in one analytical
  chain: identify the right population, reconcile the right files, compute the
  right metric, then decide. **Unrelated gotchas are not composition.**
- **Compounding direction.** Every trap, handled correctly, pushes toward the same
  non-obvious recommendation. **Opposing traps create a knife edge.**
- **Deterministic after correction.** If a layer rests on an unstated threshold,
  missing evidence, or an unresolved conflict between files, it is not a trap.
- **Live, not cosmetic.** Mishandling a layer must produce a meaningfully wrong
  intermediate result, ranking, prediction, or recommendation. **If the same final
  answer survives the mistake, drop the layer.**
- **Margin after correction.** The winning option should survive a **10 to 15
  percent perturbation** of any judgment call.
- **Bait the anchor.** A clean summary that directly answers the prompt is the best
  delivery vehicle for a trap.
- **Decoy trap.** Include one shallow, obvious mess. Models catch it, feel
  diligent, and stop looking for the quiet one.
- **Interaction trap.** Two issues that roughly cancel in the aggregate but not in
  the deciding cut.
- **Trap reserve.** Build three, ship two, and keep the third file version ready
  **if the rollout comes back easy**.

## Tuning a rollout

**Depth is fair only while the trap stays findable.**

To make a task harder:

- Move the correcting fact deeper: later in a file, further from the headline, one
  more join away. **A normal analytical route must still reach it.**
- Downgrade the antidote's salience from a dedicated file → a section of a long
  file → a changelog line. **Stop at the point where a cold solve stops
  succeeding.**
- Add a second plausible destination: a distractor analysis that produces a
  specific, confident, wrong number.
- **Make the trap quiet rather than invisible.** Data that looks healthy is fair
  only when an observable reconciliation signal — a count, a total, a date, or a
  definition — exposes it during ordinary checks.
- Increase reconciliation distance. The two numbers that must disagree live three
  files apart, as long as the disagreement is still visible to someone who
  reconciles the metric once.

Three conditions must survive every tightening:

- A normal analytical route still reaches the correcting fact.
- An observable reconciliation signal exposes the problem during ordinary checks.
- **A cold solve, run from the files alone, still succeeds.**

## Failures you must not celebrate

| Failure | What it means | Fix |
|---|---|---|
| **Semantic** | They misread the ask | Fix the prompt |
| **Parsing** | They never loaded a file | Fix the file |
| **Threshold** | Their answer is arguably right | Fix determinism |

**All three are invalid-stump territory. Do not celebrate a failure you cannot
defend.** See `invalid-stumps.md`.
