# Constructing the evidence package

Use [operative rules](../../shared-references/canonical-rules.md) and
[data selection](../../mark-task-builder/references/data-selection.md).

## Build around real dependencies

Select files because their information is needed: assignment records,
measurements, outcomes, sampling/design documentation, release histories,
crosswalks or operational constraints. Inspect the actual file graph and
demonstrate joins at the right observation units.

A file's format, length or position is not evidence of difficulty. The accepted
example with SQLite and compressed data does not establish that those formats
caused its success. Our earlier policy requiring artificial mess and burying the
arbiter was an unsupported generalization and is retired.

Keep authentic complexity that changes analytical work. Do not hide essential
definitions or intentionally break parsers. If reformatting is useful for a real
workflow or size limit, preserve values and record the transformation.

## Package integrity

Preserve downloaded raw files and provenance. Derived subsets must keep the
comparison groups, history and design structure the analysis needs. Do not
duplicate records to meet row counts or split/convert one source merely to claim
more independently necessary evidence.

Missing values need interpretable semantics. Do not introduce ambiguous dates,
colliding identifiers, unknowable units or invented outcomes.

Use scenario documents only for legitimate business context and constraints.
Mark their provenance as authored; generate copied factual values from the
source rather than hand-typing them.

## Measure necessity and difficulty separately

Run the solver on reduced evidence where practical and inspect what becomes
unreachable. A missing-file exception alone does not prove analytical necessity.
Distinguish essential evidence from corroboration and contextual material.

Compute credible shortcut and defensible analyses, test reasonable alternatives,
and run fresh blind solvers. Internal screens can be smaller than a submission
package. Only build out the complete package after the concept warrants it.
