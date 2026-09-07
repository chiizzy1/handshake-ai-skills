> Historical idea catalog. Apply [operative rules](canonical-rules.md) first.
> Named mechanisms and accepted examples do not establish current model failure
> rates, mandatory layering, or current task-format requirements.

# Trap Catalog

## Coverage

| Catalog | Entries | Bodies |
|---|---|---|
| By **family** (A–F) | 83 | **83 — complete** |
| By **objective** | 104 | 33 titles, 0 bodies |

The family catalog below is complete: every trap carries its failure mode, a
realistic example, its in-corpus antidote, its pairings, and the model failure
behaviours it targets.

The parallel objective-indexed catalog at `/trap-examples` is still uncaptured
below the titles. It covers the same material sliced differently, so the family
catalog is usually enough.

Deep link format: `/trap-design/catalog?family=A#trap-A1`.

## The four fit checks

Every trap carries these on the platform. **Confirm all four before using it**, and
note the handbook's own caveat: nothing checks your work, and confirming all four
does not guarantee the trap is valid.

1. **Changes or invalidates a material conclusion**
2. **Correcting evidence exists inside the workspace**
3. **Bait is a plausible expert mistake**
4. **Qualified analysts should converge after finding the antidote**

If a condition cannot be met, check `/invalid-stumps` before revising — the shape
may be one that gets rejected in review.

## Families at a glance

| Family | Name | The shape | Entries |
|---|---|---|---|
| A | Aggregation and statistics | The number is computed correctly and still means the wrong thing. | 17 |
| B | Experiment and causality | The comparison looks clean but the design underneath it is broken. | 17 |
| C | Time and comparability | Two periods placed side by side that were never comparable. | 13 |
| D | Plumbing and joins | The data loads fine and the grain, keys, or units are lying. | 18 |
| E | Documents and formats | The decisive fact is present, just not where a skim will find it. | 12 |
| F | Definitions and framing | The metric named in the prompt is not the metric the decision needs. | 6 |

Cross-cutting: **Forecasting & predictive modeling** 10 · **Proven in production** 14.

Forecasting traps are methodological — leakage, validation scheme, regime change —
never cosmetic.

**"Targets" numbers** refer to the model failure behaviours on the Fundamentals
page, which is not captured locally.

---

# The 83 family traps

## Family A: Aggregation and statistics

### A1 — Simpson's paradox and mix shift · **Proven in production**

*The blended number moves one way while every segment moves the other.*

- **Why models miss it:** Models compute the headline rate and stop before segmenting.
- **Realistic example:** Overall conversion is up 2 points, but every segment is down. Growth came from a mix shift toward a high-converting, low-LTV segment.
- **In-corpus antidote:** Segment volumes in a separate dimension file, so the weighted decomposition is fully derivable.
- **Seen in:** Acquisition channel allocation
- **Pairs well with:** D18 Missingness that is not random · C10 Retention triangle misread
- **Targets:** 02 Anchoring on the first plausible number, 08 Arithmetic shortcuts on Fundamentals.

### A2 — Weighted vs unweighted averages

*Segment rates get averaged as if the segments were the same size.*

- **Why models miss it:** Models take a simple mean of rates that are already ratios.
- **Realistic example:** A survey table of average scores by region invites a plain mean, while the regions differ 50x in population and carry survey weights.
- **In-corpus antidote:** Population counts and survey weights ship with the raw file, so the weighted figure is recoverable.
- **Pairs well with:** A5 Totals vs rates · F3 Wrong denominator population
- **Targets:** 08 Arithmetic shortcuts on Fundamentals.

### A3 — Ratio of averages vs average of ratios

*Two defensible-looking formulas rank the options differently.*

- **Why models miss it:** Models pick whichever formula is easier from the shape of the file.
- **Realistic example:** Total revenue divided by total users picks a different winner than the mean of per-user revenue once whale accounts exist.
- **In-corpus antidote:** The stakeholder question names the population, so only one denominator answers it.
- **Pairs well with:** A4 Mean vs median under heavy tails · F3 Wrong denominator population
- **Targets:** 08 Arithmetic shortcuts on Fundamentals.

### A4 — Mean vs median under heavy tails

*A handful of accounts carry the entire average.*

- **Why models miss it:** Models default to means and never inspect the distribution.
- **Realistic example:** Three enterprise accounts drive 40 percent of usage, and the plan that looks like it is growing is flat at the median.
- **In-corpus antidote:** Account-level rows are present, so the tail is visible to anyone who looks at the distribution.
- **Pairs well with:** A12 Outlier contamination · B12 Survivorship bias
- **Targets:** 02 Anchoring on the first plausible number, 08 Arithmetic shortcuts on Fundamentals.

### A5 — Totals vs rates · **Proven in production**

*A headline count moves because the denominator moved.*

- **Why models miss it:** Models report totals when the decision depends on a rate.
- **Realistic example:** Reported cases doubled while the covered population tripled, so the incidence rate actually fell.
- **In-corpus antidote:** The population denominator file covers the identical period and geography, so the rate is a one-step calculation.
- **Pairs well with:** A13 Base-rate neglect · C3 Unequal day and weekday mix
- **Targets:** 02 Anchoring on the first plausible number on Fundamentals.

### A6 — Percent vs percentage points

*A memo phrase is ambiguous until you check it against the raw series.*

- **Why models miss it:** Models take the memo's wording at face value.
- **Realistic example:** Churn increased 20 percent means 5 to 6 percent, not 5 to 25 percent.
- **In-corpus antidote:** The raw churn series settles the reading with no interpretation required.
- **Pairs well with:** E3 Authoritative but stale document · F1 Competing metric definitions
- **Targets:** 04 Authority over correctness, 08 Arithmetic shortcuts on Fundamentals.

### A7 — Noise mistaken for trend · **Proven in production**

*A short move sits comfortably inside normal variance.*

- **Why models miss it:** Models build a narrative out of three data points.
- **Realistic example:** A two-week decline is within the weekly variance visible in the 18-month history file.
- **In-corpus antidote:** The long history file makes the variance band obvious.
- **Seen in:** Acquisition channel allocation
- **Pairs well with:** A8 Seasonality read as effect · C11 One-off event contamination
- **Targets:** 01 Head-of-file sampling, 02 Anchoring on the first plausible number on Fundamentals.

### A8 — Seasonality read as effect · **Proven in production**

*The lift is the calendar, not the change.*

- **Why models miss it:** Models do not check the same window a year earlier.
- **Realistic example:** A feature launched in November shows a lift that matches last year's holiday bump exactly.
- **In-corpus antidote:** Prior-year data for the same weeks is in the corpus.
- **Seen in:** Online-store category cutQ4 checkout bundle
- **Pairs well with:** C11 One-off event contamination · B4 Novelty effect
- **Targets:** 02 Anchoring on the first plausible number, 10 Time laziness on Fundamentals.

### A9 — Regression to the mean

*The worst cohort improves whether or not you touch it.*

- **Why models miss it:** Models take extreme selected cohorts at face value.
- **Realistic example:** The worst-performing program sites improved 30 percent after the intervention, and so did the untreated worst sites.
- **In-corpus antidote:** Untreated comparison sites are included in the same export.
- **Pairs well with:** B2 Pre-existing difference between arms · B9 Hidden confounder
- **Targets:** 05 Plausibility bias on Fundamentals.

### A10 — Small-sample overgeneralization · **Proven in production**

*The winning cell is tiny.*

- **Why models miss it:** Models rarely compute or sanity-check n before ranking.
- **Realistic example:** The winning variant leads in a cell with n equal to 43, and a model chosen on overall accuracy is worst in the one subgroup the decision is about.
- **In-corpus antidote:** Counts sit next to the rates, and per-subgroup performance is in the shipped evaluation file.
- **Seen in:** Acquisition channel allocation
- **Pairs well with:** A11 Multiple comparisons · B6 Underpowered null
- **Targets:** 08 Arithmetic shortcuts, 12 Premature synthesis on Fundamentals.

### A11 — Multiple comparisons

*One significant cell out of 48 is exactly what noise predicts.*

- **Why models miss it:** Models accept any cell flagged significant.
- **Realistic example:** A screen reports the one association under p equal to 0.05 out of 48 tested variants, with no correction applied.
- **In-corpus antidote:** The full grid of tests is present, so the number of comparisons is visible and correctable.
- **Pairs well with:** A10 Small-sample overgeneralization · B5 Peeking and early stopping
- **Targets:** 02 Anchoring on the first plausible number, 08 Arithmetic shortcuts on Fundamentals.

### A12 — Outlier contamination

*One enormous row decides the comparison.*

- **Why models miss it:** Models aggregate without scanning value ranges.
- **Realistic example:** A single fat-finger 2.4M order, cancelled later in the shipments file, flips the regional comparison.
- **In-corpus antidote:** The cancellation file carries the reversal with a matching order ID.
- **Pairs well with:** C7 Refund and chargeback lag · D14 Sentinel values
- **Targets:** 02 Anchoring on the first plausible number, 03 No cross-file reconciliation on Fundamentals.

### A13 — Base-rate neglect

*A huge relative change over a trivial base.*

- **Why models miss it:** Models report relative change without locating the denominator.
- **Realistic example:** Fraud alerts up 300 percent means 10 to 40 out of 2M transactions, and the volume file is separate.
- **In-corpus antidote:** The transaction volume file covers the identical period.
- **Pairs well with:** A5 Totals vs rates · D5 Bot and fraud traffic
- **Targets:** 03 No cross-file reconciliation on Fundamentals.

### A14 — Compounding error

*Growth rates get averaged instead of compounded.*

- **Why models miss it:** A pre-built forecast tab makes the error for the model.
- **Realistic example:** The mean of daily growth rates is presented as weekly growth in a spreadsheet tab.
- **In-corpus antidote:** The underlying daily series lets the correct compounded figure be recomputed.
- **Pairs well with:** E2 Mis-named workbook sheet · A8 Seasonality read as effect
- **Targets:** 04 Authority over correctness, 08 Arithmetic shortcuts on Fundamentals.

### A15 — Percentile blindness

*The median is healthy and the tail is on fire.*

- **Why models miss it:** Models report central tendency for a tail-driven problem.
- **Realistic example:** p50 latency is fine while p95 is catastrophic, and the prompt only says performance.
- **In-corpus antidote:** Raw per-request timings are available, so percentiles are computable.
- **Pairs well with:** A4 Mean vs median under heavy tails · F1 Competing metric definitions
- **Targets:** 08 Arithmetic shortcuts, 09 Definition sloppiness on Fundamentals.

### A16 — Test applicability, not test recall

*Two tests both return a clean number and only one is licensed.*

- **Why models miss it:** The familiar test gets recalled before its assumptions are checked.
- **Realistic example:** Group variances are compared with a normality-sensitive test on a heavy-tailed sample.
- **In-corpus antidote:** A methodology file states the distributional assumption, so the valid test is nameable from the corpus.
- **Pairs well with:** A12 Outlier contamination · A4 Mean vs median under heavy tails
- **Targets:** 02 Anchoring on the first plausible number, 05 Plausibility bias on Fundamentals.

### A17 — Prospective question, retrospective file

*The decision needs a design, and a nearby history file makes an estimate look computable.*

- **Why models miss it:** An estimate gets returned instead of what would have to be measured; resampling the wrong population feels like rigour.
- **Realistic example:** The brief commits to a program that has not run yet, and the shipped history covers a different population and instrument.
- **In-corpus antidote:** The history file's documentation pins that mismatch, so the deliverable is a design and its assumptions, not a number.
- **Pairs well with:** B15 Non-identifiable effect · F3 Wrong denominator population
- **Targets:** 05 Plausibility bias, 12 Premature synthesis on Fundamentals.


## Family B: Experiment and causality

### B1 — Sample ratio mismatch

*Assignment counts are not what the design says they should be.*

- **Why models miss it:** Models never check the split before reading the result.
- **Realistic example:** Test and control land at 56 and 44 when the design says 50 and 50, which invalidates the readout.
- **In-corpus antidote:** The design doc states the intended split and the assignment table carries the actual counts.
- **Pairs well with:** B3 Non-random assignment leak · D4 Internal and test accounts
- **Targets:** 11 Join naivety, 06 Absence of data as signal on Fundamentals.

### B2 — Pre-existing difference between arms

*The winning arm was already ahead before the test started.*

- **Realistic example:** Pre-period data in a separate file shows the treated group already trending 8 percent higher, so the groups were never comparable.
- **In-corpus antidote:** The pre-period export covers both groups with the same assignment IDs.
- **Pairs well with:** B9 Hidden confounder · A9 Regression to the mean
- **Targets:** 03 No cross-file reconciliation, 12 Premature synthesis on Fundamentals.

### B3 — Non-random assignment leak

*The rollout order confounds the result.*

- **Why models miss it:** The detail sits in an engineering memo, not the data.
- **Realistic example:** We rolled the test to iOS first, so platform is entangled with the treatment.
- **In-corpus antidote:** The memo is in the corpus and the platform column confirms it.
- **Pairs well with:** E4 Correction buried in a comms export · B9 Hidden confounder
- **Targets:** 01 Head-of-file sampling, 07 Format blind spots on Fundamentals.

### B4 — Novelty effect

*The lift decays across the test window.*

- **Why models miss it:** Models report the full-window average.
- **Realistic example:** Week 1 lift is plus 12 percent and week 4 is plus 1 percent, so the plus 6 percent average misleads.
- **In-corpus antidote:** Daily or weekly cuts are present in the readout file.
- **Pairs well with:** C6 Cohort maturity mismatch · B8 Winner's curse
- **Targets:** 02 Anchoring on the first plausible number, 10 Time laziness on Fundamentals.

### B5 — Peeking and early stopping

*The test was stopped the day it crossed significance.*

- **Why models miss it:** The stopping decision is buried in an experiment log.
- **Realistic example:** The analytics changelog records the stop date matching the first significant day.
- **In-corpus antidote:** The changelog dates and the daily series together make the peeking visible.
- **Pairs well with:** A11 Multiple comparisons · E4 Correction buried in a comms export
- **Targets:** 01 Head-of-file sampling, 07 Format blind spots on Fundamentals.

### B6 — Underpowered null · **Proven in production**

*No significant effect is read as no effect.*

- **Why models miss it:** Models treat a wide confidence interval as evidence of equivalence.
- **Realistic example:** The interval spans minus 2 percent to plus 14 percent and the deck calls it flat.
- **In-corpus antidote:** Sample sizes and the interval are both printed in the readout.
- **Seen in:** Feedback widget design
- **Pairs well with:** A10 Small-sample overgeneralization · E3 Authoritative but stale document
- **Targets:** 08 Arithmetic shortcuts, 12 Premature synthesis on Fundamentals.

### B7 — Contamination between arms

*Control users are exposed to the treatment indirectly.*

- **Why models miss it:** Detecting it requires reading the feature design doc.
- **Realistic example:** In a referral test, control users receive referrals sent by test users.
- **In-corpus antidote:** The design doc describes the referral mechanic explicitly.
- **Pairs well with:** B11 Cannibalization · E7 Long-file burial
- **Targets:** 07 Format blind spots, 12 Premature synthesis on Fundamentals.

### B8 — Winner's curse

*Post-launch data shows half the experimental lift.*

- **Why models miss it:** Models stop at the experiment file and never open the holdout.
- **Realistic example:** The model chosen on its training fit comes in at half that accuracy on the shipped holdout period.
- **In-corpus antidote:** The holdout export is in the corpus and covers the same outcome definition.
- **Pairs well with:** B4 Novelty effect · C5 Late-arriving data
- **Targets:** 03 No cross-file reconciliation, 02 Anchoring on the first plausible number on Fundamentals.

### B9 — Hidden confounder · **Proven in production**

*The correlation is produced by an eligibility rule.*

- **Why models miss it:** The rule lives in an event schema doc, not the data.
- **Realistic example:** Participants who used the service retain better because the service is only offered after an eligibility step that already selects for retention.
- **In-corpus antidote:** The program methodology document states the eligibility rule, and the same rule is the leakage check for any model trained on that field.
- **Seen in:** Q3 growth package
- **Pairs well with:** F3 Wrong denominator population · B3 Non-random assignment leak
- **Targets:** 07 Format blind spots, 12 Premature synthesis on Fundamentals.

### B10 — Goodhart and proxy divergence

*The named metric improves while the metric that pays declines.*

- **Why models miss it:** Models optimize whatever the prompt names.
- **Realistic example:** The optimized metric improves while the outcome that actually pays, tracked in a separate ledger, declines for the same accounts.
- **In-corpus antidote:** The outcome ledger is joinable on the shared ID.
- **Pairs well with:** F1 Competing metric definitions · C7 Refund and chargeback lag
- **Targets:** 05 Plausibility bias, 03 No cross-file reconciliation on Fundamentals.

### B11 — Cannibalization

*The new surface wins by stealing from the old one.*

- **Why models miss it:** Models never take the portfolio view.
- **Realistic example:** The new checkout lifts its own conversion while total company conversion stays flat.
- **In-corpus antidote:** Both flows appear in the same event stream.
- **Pairs well with:** B7 Contamination between arms · A1 Simpson's paradox and mix shift
- **Targets:** 03 No cross-file reconciliation, 05 Plausibility bias on Fundamentals.

### B12 — Survivorship bias

*Retention improved because the weakest users left first.*

- **Why models miss it:** Missing users are invisible in a retention table.
- **Realistic example:** A policy change pushed the weakest participants out in month 1, so the surviving cohort looks healthier.
- **In-corpus antidote:** The cohort entry file records who entered each cohort and when they left.
- **Pairs well with:** D6 Deleted and anonymized users · C10 Retention triangle misread
- **Targets:** 06 Absence of data as signal on Fundamentals.

### B13 — Supply constraint read as demand

*The drop is a stockout, not a demand problem.*

- **Why models miss it:** Models default to demand-side stories in product analytics.
- **Realistic example:** Conversion dropped in the weeks the inventory file shows zero availability.
- **In-corpus antidote:** The inventory export aligns to the same dates and SKUs.
- **Pairs well with:** D16 Missing is not zero · C11 One-off event contamination
- **Targets:** 05 Plausibility bias, 03 No cross-file reconciliation on Fundamentals.

### B14 — Reactivations counted as new

*New user growth is partly returning accounts.*

- **Why models miss it:** Models never question the new user definition.
- **Realistic example:** Acquisition channel rankings flip once reactivated accounts are separated out.
- **In-corpus antidote:** Account creation dates are present, so first-seen versus returning is derivable.
- **Pairs well with:** F1 Competing metric definitions · C8 Definition change mid-series
- **Targets:** 09 Definition sloppiness on Fundamentals.

### B15 — Non-identifiable effect

*The adjustment the estimate needs is documented as never measured.*

- **Why models miss it:** An estimate that runs feels like an answer, and abstaining feels like failure.
- **Realistic example:** A regression on the available covariates returns a tidy coefficient while the dictionary records the deciding variable as never collected.
- **In-corpus antidote:** The dictionary states the variable was never collected, so the correct call is to name what would identify the effect.
- **Pairs well with:** B9 Hidden confounder · E6 Partially wrong data dictionary
- **Targets:** 06 Absence of data as signal, 12 Premature synthesis on Fundamentals.

### B16 — Confounder or collider

*Two near-identical scenarios need opposite adjustment sets.*

- **Why models miss it:** Adjustment gets chosen from wording and habit, controlling for everything available.
- **Realistic example:** In one workspace the third variable is recorded before assignment; in the other it is recorded after treatment and outcome, and controlling for it inverts the estimate.
- **In-corpus antidote:** Collection order and timing in the schema and methodology fix each structure.
- **Pairs well with:** B9 Hidden confounder · A1 Simpson's paradox and mix shift
- **Targets:** 05 Plausibility bias, 09 Definition sloppiness on Fundamentals.

### B17 — Preprocessing fitted before the split

*Scaling, encoding, or selection saw every row, and the score looks excellent.*

- **Why models miss it:** Pipelines get assembled in reading order and the split is treated as bookkeeping.
- **Realistic example:** A target-encoded categorical and a scaler fit on the full table lift validation accuracy while the held-out file disagrees.
- **In-corpus antidote:** The data dictionary marks prediction-time availability field by field, and a held-out file ships.
- **Pairs well with:** C13 Temporal leakage · E6 Partially wrong data dictionary
- **Targets:** 09 Definition sloppiness, 12 Premature synthesis on Fundamentals.


## Family C: Time and comparability

### C1 — Timezone drift

*Two files bucket the same day differently.*

- **Why models miss it:** Models join on a date string without checking the zone.
- **Realistic example:** Events are UTC and revenue is local time, so daily aggregates disagree by up to 8 percent.
- **In-corpus antidote:** Both files carry full timestamps and the pipeline README states each zone.
- **Pairs well with:** D10 Unit mismatch across files · C2 Partial final period
- **Targets:** 10 Time laziness on Fundamentals.

### C2 — Partial final period

*A complete month is compared to a 20-day month.*

- **Why models miss it:** Models never check the export date.
- **Realistic example:** Revenue declined in the latest month, except the month is not over per the export footer.
- **In-corpus antidote:** The export date appears in file metadata and a footer line.
- **Pairs well with:** C5 Late-arriving data · C3 Unequal day and weekday mix
- **Targets:** 10 Time laziness, 01 Head-of-file sampling on Fundamentals.

### C3 — Unequal day and weekday mix

*Calendar composition explains the whole move.*

- **Why models miss it:** Models compare months as if they were equal containers.
- **Realistic example:** A 3 percent decline disappears once you account for a month with five Saturdays in a weekend-heavy product.
- **In-corpus antidote:** The daily series makes the weekday mix computable.
- **Pairs well with:** A5 Totals vs rates · C11 One-off event contamination
- **Targets:** 10 Time laziness on Fundamentals.

### C4 — Fiscal vs calendar periods

*Two files label the same quarter differently.*

- **Why models miss it:** Models match on the label, not the date range.
- **Realistic example:** Finance uses fiscal quarters and the product export uses calendar quarters, putting Q3 off by a month.
- **In-corpus antidote:** The finance file prints its period start and end dates.
- **Pairs well with:** C1 Timezone drift · E6 Partially wrong data dictionary
- **Targets:** 10 Time laziness, 03 No cross-file reconciliation on Fundamentals.

### C5 — Late-arriving data

*Recent periods always look low because the data is immature.*

- **Why models miss it:** Models read the lag as a decline.
- **Realistic example:** Recent periods look weak because the statistics are first releases; the revision file restates them, and nominal figures still need the shipped deflator to compare across years.
- **In-corpus antidote:** The README states the revision schedule, and the revision and deflator files cover the same periods.
- **Pairs well with:** C2 Partial final period · E6 Partially wrong data dictionary
- **Targets:** 06 Absence of data as signal, 10 Time laziness on Fundamentals.

### C6 — Cohort maturity mismatch

*Young cohorts are judged on a window they have not lived through.*

- **Why models miss it:** Models compare 90-day LTV across cohorts of different ages.
- **Realistic example:** The newest cohort underperforms only because it has 30 days of follow-up against 12 months for the others.
- **In-corpus antidote:** Cohort start dates and observation windows are both in the table.
- **Pairs well with:** C10 Retention triangle misread · B4 Novelty effect
- **Targets:** 10 Time laziness, 06 Absence of data as signal on Fundamentals.

### C7 — Refund and chargeback lag

*Gross revenue flatters the newest channel.*

- **Why models miss it:** Models stop at gross because net requires a second file.
- **Realistic example:** The high-growth channel carries a 22 percent refund rate that arrives 30 to 60 days later.
- **In-corpus antidote:** The refunds file is joinable on transaction ID.
- **Pairs well with:** A12 Outlier contamination · B10 Goodhart and proxy divergence
- **Targets:** 03 No cross-file reconciliation on Fundamentals.

### C8 — Definition change mid-series

*The inflection is a redefinition.*

- **Why models miss it:** Models read a series as continuous by default.
- **Realistic example:** The administrative definition of an eligible case changed in April, per the methodology changelog, and the step in the series is that change.
- **In-corpus antidote:** The changelog names the date and both the old and new rules.
- **Pairs well with:** F1 Competing metric definitions · C12 Instrumentation change, not behavior change
- **Targets:** 09 Definition sloppiness, 01 Head-of-file sampling on Fundamentals.

### C9 — Packaging change breaks comparability

*ARPU jumped because the cheap tier was removed.*

- **Why models miss it:** Models compare plan-level metrics across a repackaging.
- **Realistic example:** The Basic tier was discontinued and its users were migrated, per the pricing memo.
- **Pairs well with:** A1 Simpson's paradox and mix shift · F4 Trial and paid mix
- **Targets:** 09 Definition sloppiness, 10 Time laziness on Fundamentals.

### C10 — Retention triangle misread

*Blended retention declines purely from cohort mix.*

- **Why models miss it:** Models read across a cohort table instead of down it.
- **Realistic example:** Recent young cohorts dominate the blend, so the average falls while every cohort holds.
- **In-corpus antidote:** The full cohort triangle is present with sizes per cohort.
- **Pairs well with:** A1 Simpson's paradox and mix shift · C6 Cohort maturity mismatch
- **Targets:** 02 Anchoring on the first plausible number, 08 Arithmetic shortcuts on Fundamentals.

### C11 — One-off event contamination

*A single promo day carries the base period.*

- **Realistic example:** The month-over-month decline disappears once the flash-sale day is excluded.
- **In-corpus antidote:** The marketing calendar file lists the promo dates.
- **Pairs well with:** A7 Noise mistaken for trend · A8 Seasonality read as effect
- **Targets:** 10 Time laziness, 02 Anchoring on the first plausible number on Fundamentals.

### C12 — Instrumentation change, not behavior change · **Proven in production**

*The event changed, the users did not.*

- **Why models miss it:** Models read event volume as user behavior.
- **Realistic example:** Signups dropped 40 percent because the event was renamed and split mid-period.
- **In-corpus antidote:** The engineering changelog records the rename and the new event names appear in the stream.
- **Seen in:** PDP cart collapseOnboarding v2 rollback
- **Pairs well with:** C8 Definition change mid-series · E6 Partially wrong data dictionary
- **Targets:** 09 Definition sloppiness, 06 Absence of data as signal on Fundamentals.

### C13 — Temporal leakagek-fold looks excellent and rolling-origin collapses.

- **Why models miss it:** Random splits are the default, and the information set at prediction time is rarely reconstructed.
- **Realistic example:** A status field sits in the training file but is only recorded weeks after the prediction date the brief fixes.
- **In-corpus antidote:** Field-level timestamps and the brief's stated decision date make the offending feature and split checkable.
- **Pairs well with:** B17 Preprocessing fitted before the split · C7 Refund and chargeback lag
- **Targets:** 10 Time laziness, 05 Plausibility bias on Fundamentals.


## Family D: Plumbing and joins

### D1 — Join fan-out

*A many-to-one join silently multiplies rows.*

- **Why models miss it:** Models never compare row counts before and after a join.
- **Realistic example:** Joining orders to a route table with multiple legs per shipment silently multiplies rows and inflates delivered volume by 30 percent.
- **In-corpus antidote:** Row counts and a documented grain per file make the inflation checkable.
- **Pairs well with:** D13 Event vs user vs session grain · D3 Partial duplicates
- **Targets:** 11 Join naivety on Fundamentals.

### D2 — Wrong key among lookalikes

*Four ID columns are available and only one is correct.*

- **Why models miss it:** Models join on the most obvious-sounding column.
- **Realistic example:** Joining on the legacy area code instead of the current geographic identifier mixes two incompatible population definitions.
- **In-corpus antidote:** The data dictionary defines each identifier's population, and a crosswalk file connects the two vintages.
- **Pairs well with:** D13 Event vs user vs session grain · F3 Wrong denominator population
- **Targets:** 11 Join naivety, 07 Format blind spots on Fundamentals.

### D3 — Partial duplicates · **Proven in production**

*Duplicates that carry distinct IDs, so they never look like duplicates.*

- **Why models miss it:** Models check for exact dupes only.
- **Realistic example:** Retried payment events share an idempotency key while having new event IDs.
- **In-corpus antidote:** The idempotency key is present and the payments README explains retries.
- **Pairs well with:** D1 Join fan-out · D15 Embedded total rows
- **Targets:** 11 Join naivety, 01 Head-of-file sampling on Fundamentals.

### D4 — Internal and test accounts

*QA accounts cluster in the winning segment.*

- **Why models miss it:** The flag lives in a different file than the metric.
- **Realistic example:** 6 percent of users are internal per the users dimension file and they concentrate in one arm.
- **In-corpus antidote:** The is_internal flag is present in the dimension export.
- **Pairs well with:** B1 Sample ratio mismatch · D5 Bot and fraud traffic
- **Targets:** 03 No cross-file reconciliation, 11 Join naivety on Fundamentals.

### D5 — Bot and fraud traffic

*The surge driving the recommendation is not human.*

- **Why models miss it:** Detecting it needs a security or user-agent file.
- **Realistic example:** 70 percent of the traffic spike comes from datacenter IPs per the security export.
- **In-corpus antidote:** The security export maps sessions to IP classification.
- **Pairs well with:** A13 Base-rate neglect · D4 Internal and test accounts
- **Targets:** 03 No cross-file reconciliation, 07 Format blind spots on Fundamentals.

### D6 — Deleted and anonymized users

*Null joins silently drop the population under study.*

- **Why models miss it:** Models let inner joins do the filtering.
- **Realistic example:** A churn analysis excludes deleted accounts, which are precisely the churned users.
- **In-corpus antidote:** The deletion log records how many accounts were removed and when.
- **Pairs well with:** B12 Survivorship bias · D18 Missingness that is not random
- **Targets:** 06 Absence of data as signal, 11 Join naivety on Fundamentals.

### D7 — Stale derived column

*A precomputed column disagrees with the raw rows it came from.*

- **Why models miss it:** Models trust the column the prompt implies is primary.
- **Realistic example:** ltv_bucket was computed before the refund backfill, so recomputing from transactions changes the segment ranks.
- **In-corpus antidote:** The raw transactions and the backfill date are both available.
- **Pairs well with:** C7 Refund and chargeback lag · E3 Authoritative but stale document
- **Targets:** 04 Authority over correctness, 03 No cross-file reconciliation on Fundamentals.

### D8 — Schema drift mid-file

*A column changes meaning at a row boundary.*

- **Why models miss it:** Models read the head of the file and generalize.
- **Realistic example:** amount is in cents before 2025-03-01 and dollars after, per a one-line migration note.
- **In-corpus antidote:** The migration note states the cutover date.
- **Pairs well with:** D10 Unit mismatch across files · E6 Partially wrong data dictionary
- **Targets:** 01 Head-of-file sampling on Fundamentals.

### D9 — Currency mix

*One revenue column holds three currencies.*

- **Why models miss it:** Models sum the column without converting.
- **Realistic example:** Unconverted totals make the EU region the false winner.
- **In-corpus antidote:** The FX reference file covers the same dates as the transactions.
- **Pairs well with:** D10 Unit mismatch across files · C4 Fiscal vs calendar periods
- **Targets:** 01 Head-of-file sampling, 11 Join naivety on Fundamentals.

### D10 — Unit mismatch across files

*Two files measure the same thing in different units.*

- **Why models miss it:** Models compare numbers, not units.
- **Realistic example:** One file reports raw instrument counts and the other reports normalized values, so comparing them directly names the wrong sample as the outlier.
- **In-corpus antidote:** Each file's dictionary states its unit and whether normalization has been applied.
- **Pairs well with:** A15 Percentile blindness · D9 Currency mix
- **Targets:** 07 Format blind spots on Fundamentals.

### D11 — Wide and long mismatch

*A wide file carries an All row that the long file excludes.*

- **Why models miss it:** Models sum every row in the wide table.
- **Realistic example:** Summing the wide export double counts because the All category is a row, not a header.
- **In-corpus antidote:** The long file provides the category list that reveals the extra row.
- **Pairs well with:** D15 Embedded total rows · F3 Wrong denominator population
- **Targets:** 11 Join naivety on Fundamentals.

### D12 — Dirty keys with meaning · **Proven in production**

*The dirt is a breadcrumb pointing at one broken source.*

- **Why models miss it:** Models normalize casing and move on without asking where the variants came from.
- **Realistic example:** US, us, and a space-padded US all come from one integration that also drops a required field.
- **In-corpus antidote:** The source system column identifies which integration produced each row.
- **Seen in:** Q1 2010 cohort NRR
- **Pairs well with:** D18 Missingness that is not random · D8 Schema drift mid-file
- **Targets:** 06 Absence of data as signal on Fundamentals.

### D13 — Event vs user vs session grain

*The answer needs users and the file is events.*

- **Why models miss it:** Models count whatever grain the rows are in.
- **Realistic example:** Adoption computed on shipment legs rather than orders triple counts multi-leg deliveries.
- **In-corpus antidote:** Order IDs are present on every leg, so deduplication is trivial once noticed.
- **Pairs well with:** D1 Join fan-out · F3 Wrong denominator population
- **Targets:** 11 Join naivety, 09 Definition sloppiness on Fundamentals.

### D14 — Sentinel values

*Placeholder values are averaged as if they were data.*

- **Why models miss it:** Models aggregate without scanning value ranges.
- **Realistic example:** Minus 999 and 1970-01-01 in a duration field tank one group's average.
- **In-corpus antidote:** The dictionary documents the sentinel convention.
- **Pairs well with:** D16 Missing is not zero · A12 Outlier contamination
- **Targets:** 06 Absence of data as signal, 08 Arithmetic shortcuts on Fundamentals.

### D15 — Embedded total rows

*A grand total sits inside the data region.*

- **Why models miss it:** Models sum columns blind.
- **Realistic example:** Subtotal rows mid-table double count every category above them.
- **In-corpus antidote:** The label column names the total rows plainly.
- **Pairs well with:** D11 Wide and long mismatch · E5 Header not on row 1
- **Targets:** 11 Join naivety on Fundamentals.

### D16 — Missing is not zero

*Zero-filling manufactures the dip the stakeholder is asking about.*

- **Why models miss it:** Models fill time series gaps with zeros.
- **Realistic example:** The gap is a logging outage recorded in the ops notes, not an absence of events.
- **In-corpus antidote:** The ops incident log covers the outage window.
- **Pairs well with:** D14 Sentinel values · C12 Instrumentation change, not behavior change
- **Targets:** 06 Absence of data as signal on Fundamentals.

### D17 — Slowly changing dimension

*Facts get joined to current attributes rather than the ones in force at the time.*

- **Why models miss it:** Models join to the dimension table as it stands today.
- **Realistic example:** Records attributed to entities' current attributes rather than the ones in force at the time misstate which category actually drove the change; boundary or classification vintages
- **In-corpus antidote:** Each record carries its own attribute snapshot, and the vintage crosswalk is shipped.
- **Pairs well with:** C9 Packaging change breaks comparability · D2 Wrong key among lookalikes
- **Targets:** 11 Join naivety, 10 Time laziness on Fundamentals.

### D18 — Missingness that is not random

*Dropping nulls flips the ranking because the nulls are the story.*

- **Why models miss it:** Models drop nulls silently.
- **Realistic example:** At-risk records disproportionately have a null status field, and samples flagged in the QC report are exactly the ones missing a value, so dropping nulls flips the ranking.
- **In-corpus antidote:** The null rate by segment is computable, and the QC report names the excluded records.
- **Pairs well with:** D6 Deleted and anonymized users · A1 Simpson's paradox and mix shift
- **Targets:** 06 Absence of data as signal on Fundamentals.


## Family E: Documents and formats

### E1 — Footnote overrides the table · **Proven in production**

*The qualifier lives pages away from the number.*

- **Why models miss it:** Models read the table and skip the appendix.
- **Realistic example:** Excludes marketplace transactions, see appendix C, and appendix C holds the reconciliation.
- **In-corpus antidote:** The appendix is in the same PDF and is explicit.
- **Seen in:** Category cross-sell rule
- **Pairs well with:** E7 Long-file burial · E3 Authoritative but stale document
- **Targets:** 07 Format blind spots, 04 Authority over correctness on Fundamentals.

### E2 — Mis-named workbook sheet

*The sheet name lies about which version is correct.*

- **Why models miss it:** Models open the first or the best-named sheet.
- **Realistic example:** A sheet named old_do_not_use is the corrected version per the email thread.
- **In-corpus antidote:** The email thread is the arbiter and names the sheet directly.
- **Pairs well with:** E4 Correction buried in a comms export · E3 Authoritative but stale document
- **Targets:** 07 Format blind spots, 04 Authority over correctness on Fundamentals.

### E3 — Authoritative but stale document · **Proven in production**

*A polished deck beats a raw file in a model's mind.*

- **Why models miss it:** Models rank formatting as authority.
- **Realistic example:** The carrier's polished summary was produced before the restatement, per the tiny footer date, and it disagrees with the raw records.
- **In-corpus antidote:** The export date and the restatement memo date can be ordered.
- **Seen in:** Product category discontinuation
- **Pairs well with:** D7 Stale derived column · E4 Correction buried in a comms export
- **Targets:** 04 Authority over correctness on Fundamentals.

### E4 — Correction buried in a comms export

*The decisive line is message 340 of 400.*

- **Why models miss it:** Models skim long, boring exports.
- **Realistic example:** Heads up, the March numbers in the deck are wrong, use the warehouse table.
- **In-corpus antidote:** The message is unambiguous and dated after the deck.
- **Pairs well with:** E3 Authoritative but stale document · E7 Long-file burial
- **Targets:** 01 Head-of-file sampling, 07 Format blind spots on Fundamentals.

### E5 — Header not on row 1

*Parsers grab a title row as the header.*

- **Why models miss it:** Models accept whatever the first row gives them.
- **Realistic example:** Merged double headers make Q1 ambiguous between two years.
- **In-corpus antidote:** The real header row is plainly readable a few rows down.
- **Pairs well with:** D15 Embedded total rows · E10 Delimiter and encoding mess with stakes
- **Targets:** 07 Format blind spots on Fundamentals.

### E6 — Partially wrong data dictionary

*Documentation describes a schema that no longer holds.*

- **Why models miss it:** Models over-trust documentation over the rows.
- **Realistic example:** The dictionary describes v1 while two columns were repurposed in v2, per the changelog.
- **In-corpus antidote:** The changelog is dated and names the repurposed columns.
- **Pairs well with:** C8 Definition change mid-series · D8 Schema drift mid-file
- **Targets:** 04 Authority over correctness on Fundamentals.

### E7 — Long-file burial · **Proven in production**

*The number that decides it is on page 14 of 18.*

- **Why models miss it:** Models skim long PDFs and quote the summary page.
- **Realistic example:** The study protocol defines the valid analysis population, and that definition sits on page 14 of 18.
- **In-corpus antidote:** The section is legible text, not an image, and it is indexed in the contents.
- **Seen in:** Referral reward-tier standardization
- **Pairs well with:** E1 Footnote overrides the table · E4 Correction buried in a comms export
- **Targets:** 01 Head-of-file sampling, 07 Format blind spots on Fundamentals.

### E8 — Detail in a chart annotation

*A visual artifact carries a decisive caveat.*

- **Why models miss it:** Models describe charts loosely rather than reading annotations.
- **Realistic example:** A chart footnote flags that one series excludes trials.
- **In-corpus antidote:** Mirror the annotation in text. Chart-only facts are fragile and drift toward gotcha.
- **Pairs well with:** E1 Footnote overrides the table · E3 Authoritative but stale document
- **Targets:** 07 Format blind spots on Fundamentals.

### E9 — Nested JSON fields

*An optional array holds the adjustments.*

- **Why models miss it:** Models flatten JSON naively and lose nested nodes.
- **Realistic example:** Revenue events carry an optional adjustments array holding refunds, and ignoring it inflates net revenue.
- **In-corpus antidote:** The schema doc documents the optional array.
- **Pairs well with:** C7 Refund and chargeback lag · D14 Sentinel values
- **Targets:** 07 Format blind spots, 11 Join naivety on Fundamentals.

### E10 — Delimiter and encoding mess with stakes

*Naive parsing should visibly produce garbage, never plausible numbers.*

- **Why models miss it:** Models accept a mis-parsed file if the output still looks numeric.
- **Realistic example:** A semicolon CSV with quoted commas and a BOM.
- **In-corpus antidote:** Keep it recoverable in one or two obvious attempts, or it becomes a parsing puzzle.
- **Pairs well with:** E5 Header not on row 1 · D12 Dirty keys with meaning
- **Targets:** 07 Format blind spots on Fundamentals.

### E11 — The chart renders and reads wrong

*The figure draws cleanly and the order, scale, or aggregation reverses the story.*

- **Why models miss it:** Rendering gets treated as validation.
- **Realistic example:** String dates sort lexically, nulls drop silently, and a mean of ratios reverses the trend a weighted total shows.
- **In-corpus antidote:** The dictionary gives the date format and the weighting rule, and the raw rows allow the trend to be recomputed.
- **Pairs well with:** A2 Weighted vs unweighted averages · D16 Missing is not zero
- **Targets:** 07 Format blind spots, 08 Arithmetic shortcuts on Fundamentals.

### E12 — Summary contradicts the run

*A polished write-up claims an improvement the log never produced.*

- **Why models miss it:** A confident summary outranks the artifact that produced it.
- **Realistic example:** The metrics table shows the new model scoring worse on a lower-is-better metric.
- **In-corpus antidote:** The run log and metrics table ship alongside the summary and are the authoritative record.
- **Pairs well with:** E3 Authoritative but stale document · B10 Goodhart and proxy divergence
- **Targets:** 04 Authority over correctness, 03 No cross-file reconciliation on Fundamentals.


## Family F: Definitions and framing

### F1 — Competing metric definitions · **Proven in production**

*Two teams define conversion differently and the decision hinges on which one applies.*

- **Why models miss it:** Models grab the nearest definition.
- **Realistic example:** Two teams define the outcome differently, and for a model the choice between an overall accuracy score and a decision-relevant, calibrated metric ranks the candidates in
- **In-corpus antidote:** The stakeholder's question implies one definition, and the definitions doc pins each candidate metric.
- **Seen in:** Onboarding v2 rollback
- **Pairs well with:** C8 Definition change mid-series · F3 Wrong denominator population
- **Targets:** 09 Definition sloppiness on Fundamentals.

### F2 — Derivable churn or activation window

*The correct window is stated in the corpus, not chosen by the analyst.*

- **Why models miss it:** Models pick a round number like 30 days.
- **Realistic example:** The program document defines the observation window as 60 days, and using 30 flips the comparison between two grantees.
- **In-corpus antidote:** The program document is explicit, which is what keeps the task deterministic.
- **Pairs well with:** F1 Competing metric definitions · C6 Cohort maturity mismatch
- **Targets:** 09 Definition sloppiness, 12 Premature synthesis on Fundamentals.

### F3 — Wrong denominator population

*Eligible, exposed, and all users are three different denominators.*

- **Why models miss it:** Models compute over all users because that is the easiest set.
- **Realistic example:** A benefit only available to one eligibility class looks 4x less used when measured over the whole population.
- **In-corpus antidote:** Eligibility is recorded in the roster file.
- **Pairs well with:** B9 Hidden confounder · D13 Event vs user vs session grain
- **Targets:** 09 Definition sloppiness on Fundamentals.

### F4 — Trial and paid mix

*Blended conversion hides a composition change at the top of the funnel.*

- **Why models miss it:** Models report the blended rate.
- **Realistic example:** An outreach campaign floods the intake, so the blended success rate drops while the comparable subgroup improves, and two grantees report on incompatible periods until they
- **In-corpus antidote:** Intake source and reporting period are recorded on every record.
- **Pairs well with:** A1 Simpson's paradox and mix shift · C9 Packaging change breaks comparability
- **Targets:** 02 Anchoring on the first plausible number, 09 Definition sloppiness on Fundamentals.

### F5 — Attribution window mismatch

*Channel ROI ranking inverts depending on the attribution model.*

- **Why models miss it:** Models use whichever attribution column is present.
- **Realistic example:** Last click and first touch rank the channels in opposite order.
- **In-corpus antidote:** The finance reconciliation pins which model the budget decision uses.
- **Pairs well with:** D5 Bot and fraud traffic · C5 Late-arriving data
- **Targets:** 09 Definition sloppiness, 03 No cross-file reconciliation on Fundamentals.

### F6 — Non-linear funnel paths

*Users skip and repeat steps, so step-over-step rates lie.*

- **Why models miss it:** Models assume strict step ordering.
- **Realistic example:** Naive step rates exceed 100 percent or hide the real bottleneck.
- **In-corpus antidote:** The raw event sequence per user makes the true paths reconstructible. Deterministic outcome
- **Pairs well with:** D13 Event vs user vs session grain · F3 Wrong denominator population
- **Targets:** 11 Join naivety, 09 Definition sloppiness on Fundamentals.


---

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
