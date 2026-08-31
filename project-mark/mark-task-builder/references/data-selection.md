# Picking a Task and a Dataset

The dataset decides the difficulty ceiling before any trap is designed. This is
the most consequential choice in the whole build, and the field evidence in
`../../shared-references/rollout-lessons.md` is its justification.

## Order of operations — hard rule

1. **Claim the task slot first.** The platform assigns the analytical objective
   and the two required format families per task. Unclaiming and re-claiming
   re-rolls them.
2. **Read the assignment**, then choose data that fits the objective AND can
   host a main-recommendation stump.
3. Design the trap. Then build.

Designing before claiming means fitting a finished task to a random assignment.
It failed once already; do not repeat it.

## The ceiling test — apply before claiming any kit

Ask one question of the candidate dataset:

> **What does the correct solution require beyond careful reading and careful
> coding?**

If the answer is "nothing", the dataset cannot stump, whatever the trap.
Current frontier models (verified in live stump checks) correctly perform, by
default: missing-data sentinels, join/key/grain hygiene, leading-zero
identifiers, unit multipliers, cross-universe re-ranking, rule-document
compliance with section citations, denominator selection from documentation,
clean-directory reproduction, and unprompted robustness checks.

## What CAN carry a stump

Statistical machinery the tempting standard method mishandles:

| Data property | Trap it enables |
|---|---|
| Experiment / rollout data with a registered design | The registered estimator vs the tempting pooled comparison (the accepted-example pattern) |
| Survey microdata with weights and margins of error | Design-based inference; unweighted means that look adequate |
| Time series with revisions or vintages | Leakage, wrong-vintage evidence, supersession by date |
| Train/holdout or prediction context | Validation-scheme and leakage traps |
| Cohorts that mature at different rates | Maturity mismatch, denominator drift |

## Vetted sources, by trap machinery

Researched 2026-08-31. Verify the licence page directly before downloading.

| Source | Machinery | Licence | Fit |
|---|---|---|---|
| **Upworthy Research Archive** (osf.io/jd64p) | 32,487 real headline A/B tests, 150,817 arms, 538M assignments; registered exploratory/confirmatory/holdout split | **CC-BY 4.0** — on the acceptable list | Experiment & Causal (near-perfect); also Descriptive, Anomaly, Root-cause. Traps: B1 sample-ratio mismatch, B2, B4 novelty, B7, CTR denominators, ignoring the registered split |
| **ACS PUMS** (census.gov microdata FTP) | Person/household microdata with **80 replicate weights**; successive-differences variance | Public domain | Descriptive & Distribution. Unweighted means are wrong by construction |
| **NHANES** (CDC) | Survey microdata, BRR weights, documented oversampling of subgroups | Public domain | Descriptive, Anomaly. Naive means are biased in a documented direction |
| **ALFRED** (alfred.stlouisfed.org) | Every FRED series with real-time vintages (realtime_start/end) | Attribution terms — check | Forecasting, Economics. Leakage: an "as-of" decision must use the vintage available then |
| ~~THE-RCT (ICPSR 37932)~~ | Higher-ed RCT microdata | **RESTRICTED — unusable** | Reminder: check restriction status on every research archive |

## Red flags — walk away

- **Pre-computed composite indices or scores** (SVI-like). The analysis is
  already done; only arithmetic remains.
- Single vintage, no time dimension, no uncertainty measures, no design
  metadata — nowhere for statistical judgment to live.
- A decision reachable by one groupby.

## Gate arithmetic — why the main recommendation is everything

The recommendation cluster carries ~30–37 rubric points; the pass bar is the
top-two response average under 50%. Both top responses must therefore get the
**main recommendation wrong**. Supplementary difficulty produces ~18 points of
implementation scatter at best. Design the trap to flip the main answer, or
pick different data.
