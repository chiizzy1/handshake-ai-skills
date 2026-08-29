# The Analytical Trap Taxonomy

From the FAQ's answer on designing sophisticated traps. **This is the deepest
trap-design material on the project** and it is organised very differently from
the 83-trap catalog — by *where in the analytical pipeline* the trap sits.

> Think of the prompt as **a sequence of interacting analytical traps** rather
> than relying on a single data defect or statistical trick. The goal is to move
> beyond obvious errors in messy data and create situations where the model must
> reason correctly across **multiple layers of analysis**.

> The strongest prompts contain multiple interacting traps, **including some
> deliberately presented as plausible or apparently correct**. This forces the
> model to determine not merely whether an analysis is statistically valid, but
> whether its assumptions, interpretation, causal claims, predictions, and
> resulting decisions are actually defensible.

## The pipeline

```
Data → Measurement → Model → Inference → Causality → Prediction → Decision
```

**The decision process involves feedback from each step, so the prompt becomes
substantially harder when an apparently correct conclusion at one level is
undermined by a problem at another.**

The data may be accurately measured, the statistical model may fit well, and the
prediction may be calibrated — but the groups may not be comparable, the
relationship may not be causal, or the resulting decision may not be actionable.

> **Do not design the trap as "find the statistical mistake." Have the model
> determine whether each analytical step actually supports the next one.**

A worked combination: a hidden subpopulation in the data, a proxy variable for an
important construct, then asking the model to interpret a statistical comparison
as though the groups were directly comparable. **Each individual step looks
reasonable while the combined analysis leads to an incorrect conclusion.**

## Trap domains, and the question each asks

| Domain | Major trap question |
|---|---|
| Descriptive / Distributional | What does the data actually look like? |
| Sampling / Design | Where did the data come from? |
| Measurement | What do the variables actually measure? |
| Comparative | Are these groups legitimately comparable? |
| Model Specification | Is the mathematical model appropriate? |
| Inference | What does the statistical evidence establish? |
| Causal / Counterfactual | What caused the observed difference? |
| Explanation | What mechanisms or alternative explanations could account for it? |
| Prediction | Will the relationship generalize? |
| Decision / Materiality | Does the result matter enough to act on? |
| Communication | Does the interpretation accurately represent the evidence? |

## Causal and root-cause traps

**Especially useful, because they force the model to distinguish what is
*associated* with an outcome from what actually *generates* it.**

Construct a complex sequence of events in which **multiple explanations are
defensible depending on the level at which an intervention occurs**.

> A model may correctly estimate a statistical association while having no
> defensible evidence about the root cause. **Deliberately make the statistical
> fit look compelling while withholding the information needed to justify a causal
> interpretation.** The stump occurs when the model treats predictive or
> correlational evidence as proof of causation.

The model must distinguish among:

| Level | Question |
|---|---|
| **Association** | What variables are related? |
| **Causal identification** | What evidence supports a causal effect? |
| **Root cause** | What mechanism best explains the relationship? |
| **Intervention** | If X is manipulated, how will Y change? |
| **Action** | At what point in the causal chain should an intervention occur? |

## Predictive and forecasting traps

> A statistical model can be sophisticated and tempting to choose but still produce
> a misleading probability, poorly calibrated prediction, or invalid forecast
> because of how the data, the uncertainty, or the temporal structure is meant to
> be interpreted.

| Group | Traps |
|---|---|
| **Prediction** | Prediction vs explanation · prediction vs causation · feature importance vs causal importance · generalization failure · data leakage · overfitting · extrapolation |
| **Probability** | Base-rate neglect · conditional-probability reversal · odds vs probability confusion · rare-event problems · prior vs posterior confusion |
| **Calibration** | Discrimination vs calibration · overconfidence · underconfidence · subgroup miscalibration · temporal calibration drift |
| **Forecasting** | Trend vs seasonality confusion · autocorrelation · nonstationarity · structural breaks · regime changes · horizon dependence · recursive error accumulation |
| **Uncertainty** | Point vs probabilistic forecasts · confidence vs prediction intervals · coverage vs sharpness · parameter vs process uncertainty · tail risk · asymmetric uncertainty |
| **Validation** | Temporal leakage · inappropriate cross-validation · failure to use rolling-origin evaluation when appropriate · test-set contamination · distribution shift · concept drift |
| **Decision** | Predictive accuracy vs utility · threshold selection · asymmetric costs · actionability · resource constraints · intervention effects |

## Make the model explain the prediction, not merely produce it

**The most sophisticated predictive traps move beyond asking the model to produce
a number or select an option.** Require it to establish *why* the prediction
should be true and *what would happen under an intervention* — which separates
predictive validity, explanatory validity, causal validity, and intervention
validity.

Construct the prompt so that:

1. The available data supports a **seemingly strong prediction**
2. The predictive relationship is **statistically valid**
3. The relationship **does not establish causation**
4. The model is nevertheless asked **what mechanism explains** the prediction
5. The model is then asked **what would happen if one of the predictors were
   manipulated**

## The standard a strong stump meets

> A strong stump should leave the model with **a tempting, internally plausible
> path toward an incorrect answer**, while providing **enough information for a
> careful analyst to identify the hidden assumptions, alternative explanations,
> and limits of the evidence.**

That single sentence is the best statement of the bar anywhere in the material.

## Prompt-level stumping methods

Ways to edit a prompt toward a stump:

- employing **decoys and distractors**
- **hiding the shift in your determinator**
- **hiding the scope of the answer within binary phrasing**

## Invalid reasons a "stump" does not count

- a conclusion that **cannot be reproduced**
- a decision based on **arbitrary thresholds or undefined metrics**
- a **false stump** — no real traps in the logic
- **choosing the winner by a knife-edge**
