# New-task runbook

Read [operative rules](../../shared-references/canonical-rules.md) first.
The following is our local investment sequence; follow the actual task UI for
official steps. Source screening is allowed before claiming a task slot.

## 1. Establish scope

For an existing slot, record task ID, objective, start date and applicable spec.
For exploratory work, keep candidates separate from existing tasks. Do not
silently rename, skip or overwrite an existing slot.

## 2. Screen sources

Use [data selection](data-selection.md). Search primary repositories, inspect
actual files and design documentation, verify access/rights, and record what
is available. A catalog listing does not prove the necessary fields exist.

## 3. Fetch and preserve

Download raw data with version, URLs, retrieval time, terms evidence and hashes.
Keep transformation/analysis scripts in the project, not only a temporary folder.
Derived files should be reproducible from immutable raw evidence.

## 4. Test the analytical core

Write an internal decision sketch with the target, population, time cutoff,
constraints and uncertainty treatment. Compute a defensible result and credible
shortcuts. Check which requested conclusions differ and whether reasonable
alternatives preserve the decision.

If needed, reject or narrow a source whose public data cannot identify the
result. Do not invent missing observations, manipulate real outcomes or select
ambiguous definitions to force a winner.

## 5. Use blind screening

Give fresh solvers the task and inputs with normal tools, without the golden,
rubric or earlier conversation. Record exact prompt and input hashes, tool/model
configuration, artifacts and substantive errors. A diagnostic version with
organized evidence can help distinguish analysis from search burden.

Two clean solves are a useful local stop signal. Pilot outcomes are not the
official Handshake gate. If independent solvers are unavailable, mark screening
not run rather than treating the author's self-check as blind.

## 6. Complete the package and platform gate

Once a concept warrants investment, satisfy current or inherited input limits,
check evidence necessity, and write a natural request for 1–3 deliverables on
new tasks. Validate the correct solution and use the official initial
Responses 1–2 gate in the UI's sequence.

Keep the answer key isolated from solver context. Historical reports of a
platform leak do not justify resetting/deleting live state automatically.

## 7. Finalize and validate

Generate every factual field from the data. Review authored files for accuracy
and business realism; identify scenario provenance honestly. Reproduce from
frozen inputs, reconcile metrics, render final files, and inspect rubric
coverage and defensible alternatives. Match all saved artifacts to one version.

Record source status, analytical screen, blind screen, official rollout and
final deliverable validation separately. Carry authorized local work through
completion; external messaging or submission needs user authorization.
