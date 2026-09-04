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

## Verify live — never from memory

**Search the real web before claiming or downloading anything. Training
knowledge is stale by construction here**, and this project has proven it
repeatedly:

- The task spec changed twice in nine days (8/18 → 8/27). Anything remembered
  about rules or bars may already be wrong.
- Licence and restriction status are live facts. THE-RCT looks usable from
  memory; the actual ICPSR page says restricted access.
- URLs rot. Guessed CDC documentation paths returned 404s; the working link was
  only findable from the live page.
- Datasets gain vintages, revisions and new terms after any training cutoff.

The protocol, before any dataset is committed to:

1. **Web-search for current candidates** matching the assigned objective and the
   trap machinery needed — do not shortlist purely from memory or from the table
   below.
2. **Fetch the licence page itself** and read the actual terms. A licence
   remembered or asserted by a search snippet is not verified.
3. **Fetch or download the actual data URL** and confirm it resolves and matches
   the description (rows, fields, vintages).
4. **Record what was verified and when** in the provenance sidecar at download
   time, not retroactively.

**The human-fetch fallback.** When a promising source is unreachable — bot
protection, JavaScript-rendered pages, logins, no web tools in the session —
never abandon it and never substitute from memory. Hand the user the exact URL
and precisely what to save (print-to-PDF for pages, Save As for files,
screenshots for app screens). The user has standing instructions to fetch on
request; this pattern recovered the project handbook and the decisive CDC
documentation.

## Vetted sources, by trap machinery

Researched 2026-08-31 — a snapshot, not a substitute for the protocol above.
Re-verify each row live before use; licences and availability change.
**Append every source you newly vet** — verified licence, machinery, fit — so
the map grows the way rollout-lessons does. Upworthy row updated 2026-09-01
after live verification and use in task 02.

| Source | Machinery | Licence | Fit |
|---|---|---|---|
| **Upworthy Research Archive** (osf.io/jd64p) | **USED, task 02.** Exploratory file open (22,666 arms / 4,873 tests); confirmatory needs approved plans — do not use. Documented not-fully-randomized period 2013-06-25..2014-01-10 (21.5% of tests; 69.9% fail allocation-balance vs 0.5% outside); real winner/significance label columns | **CC-BY 4.0**, verified live 2026-08-31 | Experiment & Causal (proven build); Descriptive, Anomaly, Root-cause. API: api.osf.io/v2/nodes/jd64p/files/osfstorage/ |
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
top-two response average under 70%. Both top responses must therefore get the
**main recommendation wrong**. Supplementary difficulty produces ~18 points of
implementation scatter at best. Design the trap to flip the main answer, or
pick different data.
