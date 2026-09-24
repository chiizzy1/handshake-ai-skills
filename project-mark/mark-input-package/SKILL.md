---
name: mark-input-package
description: Source and inspect Project Mark empirical input packages, including actual tables, joins, documentation, access rights, provenance, analytical suitability and submission packaging.
---

# Project Mark — Input Package

Find the evidence a competent analyst would need for the actual decision.
Read [operative rules](../shared-references/canonical-rules.md) for current and
inherited requirements. File counts and formats are compliance checks, not
evidence that a task is difficult.

## Screen before assembling

Inspect the actual source files and documentation before selecting the topic:

- What is one observation? Which keys link assignment, measurements and outcomes?
- Which variables, dates, sampling details or constraints determine the answer?
- Are those fields public, or withheld/restricted in the downloadable version?
- Does the evidence support the requested causal claim, forecast or comparison?
- Can competing defensible methods produce incompatible answers?
- Are the source license and service terms compatible with distribution and
  use for this training project?

Use [data selection](../mark-task-builder/references/data-selection.md) for the
current source shortlist and
[licensing and provenance](references/licensing-provenance.md) before fetching.

Look for naturally connected evidence, such as multiple waves with assignment
records and documented follow-up, or release histories that reconstruct
decision-time information. Verify the proposed analytical difference from data.
An elaborate schema or unfamiliar dataset is only a prospect until tested.

## Preserve evidence

Keep downloaded raw files unchanged with URL, publisher, retrieval date,
dataset version, license/terms evidence, byte size and SHA-256. Record every
derived subset or transformation with its script, upstream hashes and rationale.
Represent scenario documents as authored; never fabricate empirical records or
misrepresent document origin.

Retain authentic missingness and structure. Artificial corruption, arbitrary
format conversion and hiding a rule are not requirements. Do not duplicate
records to satisfy a row-count rule. Any subset must preserve needed comparison
groups, time coverage and design structure.

## Establish necessity

For each proposed input, name the result that depends on it. Run reduced-input
analyses where practical and distinguish:

- result becomes unreachable because essential evidence is absent;
- result changes because a partial analysis incorrectly proceeds;
- result survives because the file is corroborating or unnecessary.

Do not infer analytical necessity from a parser rejecting a missing filename.
Do not count redundant formats of the same data as independent evidence.
An internal prototype is not the shipping ZIP and need not meet the input floor.

## Package and verify

Once the concept survives early analytical and blind screening, build the
complete package to the applicable input requirements. Verify joins, row counts,
file sizes, formats, provenance and substantive file roles with
`../tools/mark_manifest.py` plus human review. Its default counters are inherited
checks; it does not establish platform approval or analytical difficulty.

Read [corpus construction](references/corpus-construction.md) when selecting the
shipped files and [business realism](references/business-realism.md) when
authoring scenario materials. Report counts and gates actually verified, and
which source/access questions remain open.
