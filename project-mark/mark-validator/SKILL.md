---
name: mark-validator
description: Validate Project Mark correctness, reproducibility, robustness, evidence necessity and observed model difficulty; inspect generated rubric coverage and prepare the requested submission artifacts.
---

# Project Mark — Validator

Read [operative rules](../shared-references/canonical-rules.md).
For new tasks the initial **Responses 1 and 2 must average below 70%** and the
rubric must have **25+ criteria**. These are the first two responses, not a
selection of the highest scores across later rollouts.

The September 5 update permits 1–3 deliverables with no assigned families or
ask quota. Do not significantly edit the rubric; repair a defective prompt or
golden upstream where possible. The historical 30/5–10/60 weight split is not
a newly confirmed requirement. Follow the actual task UI for later rollouts.

## Local validation before platform evaluation

1. **Reproduce:** rerun from frozen inputs in a clean directory and compare
   material results, not just a file-presence heuristic.
2. **Robustness:** examine reasonable metrics, populations, inference conventions
   and decision rules; resolve legitimate forks.
3. **Consequence:** compute plausible shortcuts and show what material results
   they change.
4. **Evidence necessity:** remove inputs in a temporary reduced corpus and
   distinguish missing evidence from a program demanding an unnecessary file.
5. **Blind screening:** use a fresh context without golden/rubric/history and
   normal tools. Save prompt, input hashes, model/harness, output and errors.

These checks support task quality; internal screens do not substitute for the
official platform gate. Two clean blind solves are a local reason to reconsider
a concept, not a published approval rule.

## Score fairly

A material analytical error can occur despite a correct final choice.
There is no proof that both models must choose the wrong winner to meet 70%.
Formatting losses or last-decimal conventions do not establish a valid stump.

Inspect substantive outcomes, including whether an alternative analysis is
better supported than the golden. Do not penalize valid CI conventions,
equivalent units, or a response to an underspecified question.

Match every response with its exact prompt, input ZIP, golden and rubric
version. Task 01's saved ZIPs and evaluation screenshot concern different
versions; Task 02's saved ZIPs cover v1. Do not merge their evidence.

An old report describes solution leakage through later platform fields.
Verify solver-context isolation; do not assume the bug persists or reset/delete
task state automatically.

## Final checks

Confirm generated rubric coverage, criteria count, applicable weights and
legitimate tolerances. Reconcile the requested deliverables, render them and
verify business realism. See [readiness](references/readiness.md) and
[rollout scoring](references/rollout-scoring.md).

Report pass, fail, not run or blocked with actual evidence. A local PASS is not
platform approval. Prepare files within authorization; do not contact people
or submit externally without the user's authorization.
