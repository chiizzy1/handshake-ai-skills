# Rollout scoring and evidence

The September 5 announcement requires the initial **Responses 1 and 2 at the
top of the task to average strictly below 70%**. It does not mean selecting the
two highest scores from later runs. Use current UI instructions for later
rollout counts and submission. See [operative rules](../../shared-references/canonical-rules.md).

The threshold is a gate, not proof that a task is fair. Classify actual failures:

| Outcome | Interpretation |
|---|---|
| Material analytical or methodological error | Candidate valid failure; identify its empirical consequence |
| Different defensible estimator, CI, units or wording | Accept where supported; do not turn conventions into a stump |
| Missing definition or two legitimate decisions | Task ambiguity; repair the contract or evidence |
| Better-supported result than the golden | Golden defect; repair it |
| Formatting, loading or packaging failure only | Does not establish analytical difficulty |

A wrong main recommendation is not mathematically necessary for a score below
70%; materially wrong supporting analysis can matter. Evaluate the actual
rubric and avoid unsupported claims that a fixed number of points must be lost.

## Preserve matched evidence

Store task/version, prompt, source ZIP hash, golden, rubric, model/harness,
tool access and response outputs together. Do not score responses from another
version against the current rubric. Distinguish official scores from inferred
scores and local blind screens.

Keep the answer key out of the solver context. A September 1 report described
later form fields leaking solution material; its current status is unverified.
Do not automatically reset or delete a task to address an assumed bug.

## Iterate on demonstrated errors

If blind solvers repeatedly solve the analysis correctly, materially redesign
or retire the concept before polishing. Hiding evidence is not a proven fix.
If a low score comes from an unfair requirement, repair the requirement even
when doing so makes the task easier.

Do not significantly edit the rubric. Prefer upstream correction of the prompt
or golden for genuine defects and follow the current UI process.
