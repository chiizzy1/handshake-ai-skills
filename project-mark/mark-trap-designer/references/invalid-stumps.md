# Invalid Stumps

The canonical reference for the six patterns that make a task fail the bar. Every
other page links here rather than re-explaining them.

> A valid stump has **one answer a competent expert is forced to**, and models fail
> it **on the analysis, not on guessing what the question means**.

**A task matching any of the six patterns is an invalid stump and will be sent
back, even when models fail it.** Difficulty has to come from reasoning over the
evidence — never from an invented cutoff, an undefined term, a hidden assumption,
or a margin thin enough that reasonable estimation flips the call.

**Run this audit right after your first model rollout.** A task that stumps models
for the wrong reason looks identical to a good one on the scoreboard.

## Five required rules

1. **The deciding line is drawn by the data**, a rule in the files, or a value
   every analyst would pick the same way — never by your own taste.
2. **Every load-bearing term is defined** in the prompt or the files. The model
   never has to guess what you meant.
3. **No hidden assumption.** Anything the answer depends on must be discoverable
   in the bundle, not carried in your head.
4. **The margin survives reasonable estimation.** If a defensible alternative
   method flips the call, widen the margin or pin the method.
5. **Ten of ten experts agree.** If you cannot claim that without explaining a
   rule to them first, it is not a valid stump yet.

## At a glance

| Failure | Symptom | Typical fix location |
|---|---|---|
| 1. Arbitrary threshold | Nudging an invented cutoff reverses the call | Prompt or a shipped rule/policy document |
| 2. Undefined metric or definition | A different, equally valid definition crowns a different winner | Prompt or data dictionary |
| 3. Wrong golden | Recomputing from the shipped files contradicts the intended answer | Golden solution, rebuilt from raw files |
| 4. No live trap | The obvious path already wins, or the trap catches no one | Trap design, not the workspace |
| 5. Missing evidence | The golden refuses the answer or invents a fact | Input workspace, add missing file |
| 6. Knife-edge result | A defensible alternative method flips the winner | Margin or estimation method, pinned in files |

## 1 — The answer hinges on an arbitrary threshold

**Why it fails.** The recommendation flips on a cutoff **the task author invented**,
not one grounded in a file, a stated rule, or a standard experts apply
consistently. *(Thresholds grounded in the workspace or a well-established
standard are fine; the problem is one load-bearing, invented number.)*

**Diagnostic:** *Who chose this number, and would every expert choose it the same
way?*

**Example — Deploy the risk model? (Forecasting).** The intended call is HOLD,
under a self-set bar of "0.90 recall in every segment" and a probability cutoff of
0.5. No file, policy, or service standard sets either number. At a 0.85 bar, or at
the cutoff that minimizes the documented cost of a miss, the call flips to deploy.

**Fix.** Ground the deciding line in the files, a stated rule, or a standard every
expert applies the same way.

## 2 — A metric or definition that decides the answer is left undefined

**Why it fails.** The goal is clear, but the answer flips on which reasonable
operationalization the analyst picks: incidence versus prevalence, gross versus
net demand, shipment date versus delivery date, two defensible readings of
eligibility, two valid metrics, or two valid definitions of the analysis
population.

**Diagnostic:** *If I swap in a different defensible definition, does the winner
change?*

**Example — Which forecast model wins? (Forecasting).** The intended winner is
picked by mean absolute percentage error. Weighted absolute error, equally
appropriate for a demand plan and computable from the same files, crowns the other
model. The prompt never says which metric applies.

**Fix.** Pin the deciding definition: state the metric and its formula, or ship the
document (contract, protocol, eligibility rule, data dictionary) that fixes it for
every expert.

## 3 — The golden answer is wrong or does not reproduce

**Why it fails.** Recomputing from the **actual shipped files** contradicts the
intended answer, so the "stumped" responses are often the correct ones. **A model
response is not wrong simply because it disagrees with an incorrect golden.**

**Diagnostic:** *Does every load-bearing number reproduce end to end from the raw
files — joins, filters, cohort, revisions, and QC included?*

**Example — Which grantee cut cost per outcome? (Nonprofit).** The intended answer
comes from a year-end summary sheet. The raw award ledger includes a Q3 revision
the summary predates, and the summary joins spending at program level against
outcomes at site level, double-counting shared sites. Rebuilt at the correct
granularity, a different grantee wins.

**Fix.** Recompute the golden from the raw shipped files — never from labels,
dashboards, or an earlier draft — and correct or reverse it if it does not hold.

## 4 — There is no live trap, so nothing actually stumps

**Why it fails.** The obvious path is already the correct one, or a planted
complication changes nothing, so strong model responses pass for free.
**Complexity is not difficulty:** extra files, formats, and cleaning steps only
count if mishandling them produces a meaningfully wrong result.

**Diagnostic:** *If a solver mishandled the planted complication, would the
recommendation actually change?*

**Example — Decorative data-quality and formatting traps (Supply chain).** A
workspace mixes three date formats, mismatched unit scales, and one flagged bad
shipment batch across a dozen files, meant to trip up solvers. Responses handled
all of it cleanly, and the flagged batch is too small to move the estimate.
Nothing actually stumps.

**Fix.** Redesign the trap so the obvious path actually leads somewhere wrong, and
confirm each planted complication, if mishandled, flips the winner.

## 5 — The files cannot support the answer the prompt demands

**Why it fails.** A load-bearing piece of evidence is missing from the workspace,
so any answer rests on an invented fact. Commonly missing: policy or eligibility
rules, historical periods a forecast needs, target or outcome data, study
metadata, cohort definitions, effect sizes, model outputs, QC documentation, or
crosswalks and identifiers.

**Diagnostic:** *Can the required answer be produced entirely from what is in the
bundle, with nothing supplied from memory?*

**Example — How many churned accounts will the program save? (Policy).** The
prompt demands a single saved-accounts number, but no effect size exists in the
bundle: outcome data end before any site launched, only process metrics are
shipped, and the eligible-population definition is absent. The golden refused a
number while responses invented one.

**Fix.** Add the missing evidence — ship the rule, the effect size, the model
output, the QC document, or the crosswalk — and confirm every file refers to a
compatible population with an authoritative version.

## 6 — The winner clears only by a knife-edge

**Why it fails.** Every input is grounded and all but one option is eliminated, but
the lead is thin enough that a reasonable re-estimate flips it. A recommendation
is **fragile** if an alternative but defensible analysis, validation choice,
confidence interval, or estimate reverses the winner.

**Diagnostic:** *Does the plausible range of the deciding estimate cross the line
that separates the two answers?*

**Example — Did the wage increase hurt small restaurants? (Economics).** The
intended call rests on a harm effect significant under the golden's
difference-in-differences setup (p about 0.0015). Controlling for pre-existing
trends, a standard adjustment here, gives a null result (effect near 1.0, interval
0.67 to 1.52). Whether the deciding effect even exists depends on the modeling
choice.

**Fix.** Widen the margin so the answer survives reasonable methodological
variation, or pin the estimation and validation method in the files.
