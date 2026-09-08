# Traceability and reconciliation

Every substantive factual claim and computed result must trace to the frozen
inputs and a reproducible calculation. Identify authored scenario assumptions
separately. LLM assistance is permitted; provenance claims must remain accurate.

Keep a trace table while building the reference analysis:

| Metric | Value | Unit | Population / horizon | Precision | Output location | Inputs and calculation |
|---|---:|---|---|---|---|---|
| Continuing-portfolio margin change | -2.7 | percentage points | Continuing categories, specified comparison years | 1 decimal | decision.xlsx, Summary!B4 | Transactions joined by category ID, excluded categories removed, margin recomputed |

Independently reproduce the decisive joins, filters, denominators, timing,
transformations, missingness treatment, uncertainty, constraints and decision
rule. Compare each deliverable against these computed results. Accept legitimate
rounding and equivalent methods; inspect charts, labels and prose as well as
tables. Shared numbers alone do not prove that two outputs describe the same
metric.

`../../tools/mark_reconcile.py <golden_dir>` is an advisory numeric-token scan.
It can surface nearby or repeated numbers and unread files. It cannot associate
every number with its metric, unit, population or time horizon, and it cannot
certify semantic agreement or correctness. Unrelated metrics can share a value;
legitimate rounded values can differ. Review its candidates against the trace
table, and resolve unread files before claiming complete coverage.

Store the build and verification scripts with the task. Generate factual fields
from the computed results rather than copying constants into separate files.
Keep source versions and hashes with the analysis so a later rebuild cannot
silently substitute new observations.
