---
name: mark-prompt-writer
description: Write natural stakeholder prompts for Project Mark with a determinate decision and appropriate named deliverables, substantive evaluation coverage, clear scope and no answer-path narration.
---

# Project Mark — Prompt Writer

Read [operative rules](../shared-references/canonical-rules.md) before drafting.
For new tasks under September 5, request **1–3 deliverables**, choose relevant
formats, and use natural prose. There is no assigned-family requirement or
per-file ask quota. Preserve older task contracts under their applicable rules.

## Write the actual business request

Establish who owns the decision, its trigger, objective and consequences. Name
the required files and describe what the user needs to learn from them.
A workbook may contain the decision, supporting comparisons and a visual; a
standalone PDF is not automatically appropriate.

State the population, units, decision date, constraints and evaluation target
when they determine the answer. Required scope is not a forbidden hint.
Allow analytical judgment where defensible alternatives agree. Do not name the
trap, announce an expected failure, or dictate the full solution sequence.

Build the request around an empirically screened analytical concept. Avoid
spending effort on a long contract before checking the core difficulty.

## Evaluation coverage

The rubric still needs **25+ substantive criteria**. Breadth should arise from
distinct business-relevant results: material comparisons, decompositions,
uncertainty, feasibility, sensitivity and a useful visual where appropriate.
Do not multiply the same fact across files or pad with typography and decimal
places. The new announcement supplies no replacement weight split.

Specify useful units and precision without making arbitrary last-decimal
differences the challenge. If alternative valid confidence intervals or
estimators could affect grading, resolve legitimate requirements or permit
reasonable alternatives in the evaluation.

## Review

- One determinate decision or analytical objective, with sufficient evidence.
- Between one and three named outputs for a new task.
- Appropriate formats and business-realistic prose.
- Distinct substantive outcomes support the generated rubric.
- No hidden definitions, missing constraints or solution narration.
- Scope and requirements match the golden and input version.

`../tools/mark_leak_check.py prompt.md --spec current` is an advisory linter.
Its file detection and wording flags need review; it cannot verify 25 meaningful
criteria or determine whether a method or scope statement is appropriate.
For pre-September-5 contracts use `--spec legacy`.

[Supplementary questions](references/supplementary-questions.md) discusses
evaluation coverage. Worked prompts are historical examples, not templates or
authority for current counts. Make authorized edits in the user's requested
location; present the final prompt and its relevant verification.
