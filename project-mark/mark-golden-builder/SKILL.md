---
name: mark-golden-builder
description: Produce Project Mark reference deliverables from reproducible analysis, matching requested filenames and formats, reconciling results, and reviewing business realism and valid analytical alternatives.
---

# Project Mark — Golden Builder

Read [operative rules](../shared-references/canonical-rules.md).
New tasks request 1–3 deliverables; older tasks keep their applicable contract.

Establish the correct analytical result independently during source screening.
Produce the polished final files after the concept has survived difficulty
screening, in the sequence required by the current platform. Keep all golden
artifacts out of blind solver inputs.

## Build from one reproducible result set

Match every requested filename, format and substantive result. Compute figures
from shipped inputs and retain input hashes, transformations and the parameters
needed to rerun. Avoid hard-coded winner IDs or unexplained empirical constants.

Reconcile the same metric across files, tables, charts and text. Distinct
metrics can share a number, and repeated digits alone do not establish
consistency. A result need not appear twice unless the request calls for it.

Document decision-relevant uncertainty and robustness. Another defensible
estimator or CI is not wrong merely because it differs from the golden.
If valid alternatives change the decision, repair the task's evidence or
legitimate contract before grading.

## Choose structure for the intended user

- Data: explicit grain, stable keys, useful units; formulas where an auditable
  workbook benefits from them.
- Text: decision and necessary evidence in a concise professional memo.
- Visual: accurate, readable comparisons, units and uncertainty as appropriate.
- Code: reproducible from the supplied inputs in a clean directory, with the
  interface the prompt requests.

LLM assistance is permitted. Review and iterate on content and appearance.
Do not add invented human authors, fake organizational provenance, filler,
unrequested files or placeholders to make the output appear authentic.

## Validate the finished set

Run the analysis from the frozen inputs, reconcile results, open/render each
requested file and check all substantive requirements. A number-extraction
linter cannot verify every equation or visual.

Use [traceability](references/traceability.md) and
[by-format guidance](references/by-format.md) selectively; historical platform
field descriptions do not override the current UI.

Where the platform requests a golden ZIP, include only the requested
deliverables. The input ZIP and internal solution evidence are separate.
Report actual execution and visual inspection, unresolved concerns and artifact
paths. Then use **mark-validator** for the official checks.
