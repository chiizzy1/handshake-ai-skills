# Project Mark skills

Start with [mark-task-builder](mark-task-builder/SKILL.md) and the
[operative rules](shared-references/canonical-rules.md). This package supports
analytical task authoring, source screening, reference deliverables and model
evaluation.

## Current specification

The user-supplied September 5 update allows 1–3 deliverables for new tasks,
removes assigned families and per-file ask quotas, retains 25+ rubric criteria,
and requires the initial Responses 1 and 2 to average below 70%.
Older tasks preserve their applicable old rules. Source detail and inherited
input requirements are in the operative table.

## Skills

| Skill | Purpose |
|---|---|
| mark-task-builder | Source/concept screening through complete task preparation |
| mark-input-package | Actual data, documentation, rights, provenance and packaging |
| mark-trap-designer | Consequential analytical differences and blind screening |
| mark-prompt-writer | Natural, determinate business requests |
| mark-golden-builder | Reproducible, consistent, reviewed reference files |
| mark-validator | Correctness, robustness and version-matched evaluations |

## Tools and references

- `tools/mark_manifest.py`: inventory, hashes, size and row counts; inherited
  input checks, not platform approval.
- `tools/mark_leak_check.py prompt.md --spec current`: advisory current prompt
  check; use `--spec legacy` for older 8/27 contracts.
- `tools/mark_fetch.py`: download with provenance after rights verification.
- `tools/mark_reconcile.py`: numerical comparison aid; review false matches.
- `tools/mark_realism_check.py`: presentation review aid; never fabricate
  authorship or provenance to satisfy it.

[Data selection](mark-task-builder/references/data-selection.md) and
[runbook](mark-task-builder/references/new-task-runbook.md) describe the current
workflow. [Rollout lessons](shared-references/rollout-lessons.md) retains dated
observations with current corrections. Historical examples and old reference
text are idea sources, not universal requirements.

The maintained handbook entry point is
`HANDSHAKE-AI/Project-Mark/guidelines.md` in the workspace. Original captures
remain historical evidence; do not silently rewrite them as new staff policy.
