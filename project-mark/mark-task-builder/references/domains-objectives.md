# Domains And Objectives

Every task carries **one domain** and **one Axis 1 analytical objective**, chosen
before you write a word of the prompt.

## Six accepted domains

Pick the one whose decision-maker would actually own the call.

| Domain | Owns decisions about |
|---|---|
| Product Analytics | Feature launches, funnels, retention, experiment readouts, release dispositions |
| Supply Chain & Logistics | Capacity, terminal and depot allocation, routing, conversion awards |
| Economics | Rates, cost assumptions, labour market allocation, forecast revisions |
| Policy & Education | Programme scale-ups, funding rates, nominations, rebate schemes |
| Demographic & Social Science | Population composition, cohort outcomes, statewide programme targeting |
| Nonprofit & Grant-making | Grant awards, subaward certification, member ranking, drive allocation |

Program details still says "seven in-scope domains". That is stale — six is
canonical, confirmed by the Task types page and the examples index.

The published library skews hard to Product Analytics: 18 of the 25 accepted
examples. Supply Chain 2 · Policy & Education 2 · Nonprofit 2 · Economics 1. The
thinner domains are not disfavoured — they are underrepresented.

## Six Axis 1 objectives

Forecasting is an **objective**, not a seventh domain. Any domain can carry it
where the evidence pins the answer down, and more of those are wanted.

| Objective | The decision turns on | Trap count |
|---|---|---|
| Descriptive & Distribution Analysis | How a population is composed or how a metric is distributed, not why it moved | 15 |
| Anomaly Detection & Diagnostics | Separating a real event from an artifact | 18 |
| Root-Cause Analysis | Naming the driver, with rival explanations ruled out on evidence | 16 |
| Experiment & Causal Analysis | A causal claim, from a designed test or observational data with confounders | 19 |
| Forecasting & Predictive Modeling | A future value or predicted outcome the supplied history can pin down | 18 |
| Data Extraction & Conformation (ETL / Pipeline Build) | Reconciling messy multi-source inputs into one contract-conforming dataset | 18 |

## Choosing

Two questions settle it:

1. **Who would actually own this call?** That names the domain. If the answer is
   "it depends who you ask", the scenario is not concrete enough yet.
2. **What kind of mistake is the model going to make?** That names the objective,
   because the objective determines which trap families are in play.

The objective is what the trap catalog indexes on, so picking it early narrows
the trap search from 104 entries to 15–19.

## Forecasting notes

Its traps are **methodological** — leakage, validation scheme, regime change —
never cosmetic. When building a forecasting task, the fork gate gets harder: the
winner must survive reasonable model specifications, validation splits,
normalization choices, and multiple-testing handling, not just one fitted model.

Reviewers additionally test target definition, absence of leakage,
train/validation/test design, time-aware validation, forecast horizon, model
comparison fairness, metric choice, and calibration where decision-relevant.
