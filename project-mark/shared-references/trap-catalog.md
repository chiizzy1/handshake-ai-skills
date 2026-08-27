# Trap Catalog — partial capture

## Coverage warning — read this first

The handbook ships **two** trap catalogs over the same material, indexed
differently. Neither is fully captured here.

| Catalog | Where | Entries | Titles held | Bodies held |
|---|---|---|---|---|
| By **family** (A–F) | `/trap-design/catalog` | 83 | 34 | 0 |
| By **objective** | `/trap-examples` | 104 | 33 | 0 |

A "body" is the failure mode, worked example, in-corpus antidote, and
cross-family pairings. **No bodies are captured.**

**When a trap below is named but not described, say so.** Do not reconstruct a
body from the title. Titles are precise enough to pick a direction and to
recognise a shape, and not precise enough to reproduce the handbook's guidance.
The reliable substitute is the 14 worked recipes at the bottom of this file and
the 25 worked examples in `HANDSHAKE-AI/Project-Mark/examples/`, which carry real
traps end to end with their antidotes.

To extend this file, capture the two catalog pages and append. The schema below
is stable, so new entries are appends and nothing above them changes.

```
### <ID> <Title>
- **Family / objective:**
- **Failure mode:**
- **Example:**
- **In-corpus antidote:**
- **Pairs with:**
```

## The six families

| Family | Name | The shape | Entries |
|---|---|---|---|
| A | Aggregation and statistics | The number is computed correctly and still means the wrong thing. | 17 |
| B | Experiment and causality | The comparison looks clean but the design underneath it is broken. | 17 |
| C | Time and comparability | Two periods are placed side by side that were never comparable. | 13 |
| D | Plumbing and joins | The data loads fine and the grain, keys, or units are lying. | 18 |
| E | Documents and formats | The decisive fact is present, just not where a skim will find it. | 12 |
| F | Definitions and framing | The metric named in the prompt is not the metric the decision needs. | 6 |

Cross-cutting views: **Forecasting & predictive modeling** 10 · **Proven in
production** 14.

Deep link format: `/trap-design/catalog?family=A#trap-A1`.

## Named family traps

34 of 83, recovered from the recipe builder's worked pairings. ID and title only.

### Family A — Aggregation and statistics
- **A1** Simpson's paradox and mix shift
- **A4** Mean vs median under heavy tails
- **A8** Seasonality read as effect
- **A10** Small-sample overgeneralization
- **A14** Compounding error
- **A15** Percentile blindness

### Family B — Experiment and causality
- **B1** Sample ratio mismatch
- **B2** Pre-existing difference between arms
- **B4** Novelty effect
- **B7** Contamination between arms
- **B9** Hidden confounder
- **B12** Survivorship bias
- **B14** Reactivations counted as new

### Family C — Time and comparability
- **C2** Partial final period
- **C6** Cohort maturity mismatch
- **C7** Refund and chargeback lag
- **C8** Definition change mid-series
- **C9** Packaging change breaks comparability
- **C10** Retention triangle misread
- **C11** One-off event contamination
- **C12** Instrumentation change, not behavior change

### Family D — Plumbing and joins
- **D2** Wrong key among lookalikes
- **D3** Partial duplicates
- **D5** Bot and fraud traffic
- **D7** Stale derived column
- **D13** Event vs user vs session grain
- **D17** Slowly changing dimension
- **D18** Missingness that is not random

### Family E — Documents and formats
- **E1** Footnote overrides the table
- **E3** Authoritative but stale document
- **E7** Long-file burial
- **E8** Detail in a chart annotation

### Family F — Definitions and framing
- **F3** Wrong denominator population
- **F5** Attribution window mismatch
- **F6** Non-linear funnel paths

## The six objectives

| Objective | The shape | Entries |
|---|---|---|
| Descriptive & Distribution Analysis | The decision turns on how a population is composed or how a metric is distributed, not on why it moved. | 15 |
| Anomaly Detection & Diagnostics | Something in the data looks wrong and the analyst must separate a real event from an artifact. | 18 |
| Root-Cause Analysis | A metric moved and the task is to name the driver, with rival explanations ruled out on evidence. | 16 |
| Experiment & Causal Analysis | The conclusion depends on a causal claim, from a designed test or from observational data with confounders. | 19 |
| Forecasting & Predictive Modeling | The decision depends on a future value or a predicted outcome that the supplied history can pin down. | 18 |
| Data Extraction & Conformation (ETL / Pipeline Build) | The work is to reconcile messy multi-source inputs into one analysis-ready, contract-conforming dataset. | 18 |

## Named objective traps

33 of 104. Title only. The other four objectives are entirely uncaptured.

### Descriptive & Distribution Analysis — 15 of 15
- Mean/median summary hides the shape
- Hidden sub-population (mixture masquerading as one group)
- Heavy tail drives the aggregate but not the count
- Cutoff instability (the boundary is not robust)
- Materiality vs distinctness trade-off
- Wrong unit of analysis / grain
- Number-of-groups is a real choice, not a given
- Percentile tiers on a lumpy distribution
- Concentration metric misread
- Zeros and non-participants folded into the shape
- Distribution vs its driver (composition confound)
- Outliers vs the genuine tail
- Smooth distribution with no natural break
- Log-scale phenomenon read on a linear axis
- Coherence of the recommended segment is asserted, not shown

### Anomaly Detection & Diagnostics — 18 of 18
- No governance document to anchor on
- Insufficient evidence: the right call is HOLD
- Expected seasonal / calendar variation misread as an event
- Multiple comparisons / look-elsewhere effect
- Base-rate neglect
- Statistical significance vs. operational severity
- Single-point spike vs. sustained level shift
- Autocorrelation inflates apparent runs
- Wrong baseline window
- Regression to the mean after an extreme period
- Denominator/exposure-driven rate change (non-defect)
- Competing anomalies: pick the actionable one
- Threshold gaming at the boundary
- Leading indicator vs. lagging confirmation
- Simpson's reversal across segments
- Reporting/collection cadence artifacts (non-defect)
- Cost-asymmetry of the decision
- Short-window overreaction / not enough data yet

### Root-Cause Analysis — 0 of 16
Not captured.

### Experiment & Causal Analysis — 0 of 19
Not captured.

### Forecasting & Predictive Modeling — 0 of 18
Not captured. The handbook notes these traps are methodological — leakage,
validation scheme, regime change — never cosmetic.

### Data Extraction & Conformation — 0 of 18
Not captured.

## The 14 worked recipes

Fully captured, and the most usable trap material in this file. Single traps get
caught by strong models about half the time; layer a gate, a flip, and a
confirmation from **different families**, then confirm all three push toward the
same wrong answer so a partial analysis plausibly lands there.

A layer that only adds reading time is decoration. Every layer must change the
answer on its own.

| Scenario | The decision | Traps | How it works |
|---|---|---|---|
| Program funding reallocation | Which single program or channel gets the incremental budget? | F5 · D5 | A crediting-rule bait document plus an exclusion list that lives in a separate export. |
| Why did the measured rate drop | Reverse last period's change or not? | C12 · C2 | The stakeholder's wrong causal theory is stated in the prompt; a methodology note explains the measurement break. |
| Kill or keep the initiative | Retire or invest? | B12 · C6 · A4 | Three heavy participants carry the headline number; a second table at a different grain exposes it. |
| Intervention targeting | Which group receives the intervention? | A1 · D18 · A10 | A small-sample subgroup looks like the obvious winner until the eligible population is pinned. |
| Did the new terms work | Extend the terms to everyone? | A1 · C9 · C7 | Nominal versus adjusted values, and a discontinued category, separate the apparent winner from the real one. |
| Forecast next period | Commit to the target or re-plan? | A8 · C11 · A14 | A prebuilt forecast makes the compounding error, and a structural break invalidates the fitted trend. |
| Which variant won | Adopt A or B? | B7 · B4 · B2 | An early-read summary deck serves as the bait; the arms were never comparable. |
| Where is the process leak | Which stage gets the fix? | D3 · F3 · F6 | Denominator drift across stages hides the true bottleneck. |
| Is the increase real | Is there actually a problem? | C8 · C10 · B14 | Three separate comparability breaks, all pointing the same way. |
| Program redesign readout | Roll the redesign out to everyone? | B9 · B1 · E1 | Eligibility rules in a definitions document confound the cohort comparison. |
| Which sector gets the retention program | Point the budget at one sector, which? | D13 · B14 · E3 | A rollup, a one-pager, and a leadership email crown the same wrong sector; the raw records refute all three. |
| Which configuration ships | Which single configuration ships for peak season? | E3 · A15 · E7 | The winner on the stale revision fails a fine-grained capacity gate, and the fallback dies on a buried clause. |
| Is the spike real | Act on the drop or wait? | C6 · C2 · A1 | The alarming spike is made entirely of cases too recent to have reached the outcome yet. |
| Approve the plan or not | Does the plan clear the investment hurdle? | E1 · E3 · D7 | Subtracting the large headline cost flips the decision; three chained documents prove it is fully reimbursed. |

Read every pattern as domain-neutral. The same shapes appear in operational,
economic, policy, demographic, nonprofit, and predictive workspaces. Many of the
strongest entries are reconciliation problems across artifacts: a summary against
authoritative raw records, two tables at different grains, a dictionary that
redefines a field, a revision file that supersedes an older dataset. The
analytical dependency is the trap, not the file count.
