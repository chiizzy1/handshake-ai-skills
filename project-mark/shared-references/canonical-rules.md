# Project Mark — operative rules

Updated 2026-09-07. Read this before quoting a requirement.

## Source and applicability

The user's instructions govern our actions and authorizations. For project
acceptance requirements, use the current task UI and the most recent applicable
staff update, then the handbook. Local strategies are recommendations, not
platform rules.

The governing supplied source is Vincent's Slack announcement in the user's
screenshot, reviewed 2026-09-07. It explicitly distinguishes tasks started before
September 5 from new tasks. The message's full-update and examples links were
not available in the screenshot; do not claim those pages were inspected.
The source summary is in
`HANDSHAKE-AI/Project-Mark/9-05-updates.md` in the workspace.

The user explicitly confirmed that Vincent is the project lead and instructed
us to follow his announcement over James's subsequently supplied reminder.
Do not reintroduce that reminder's conflicting restriction on LLM-assisted
goldens or treat it as an unresolved approval dependency. Vincent permits LLM
assistance with iteration and editing; empirical evidence remains traceable.

| Requirement | New tasks under the September 5 update | Tasks started before September 5 |
|---|---|---|
| Deliverables | **1–3**; choose what the business request needs | Preserve the applicable old specification |
| Output families | No assigned families | Older assignments may require two families |
| Asks per deliverable | No numeric quota; natural prose | Older 8/27 contract required 3+ asks each |
| Rubric | **25+ criteria**, supported by substantive analysis | Apply the task's recorded rubric requirements |
| Rubric editing | Do not significantly edit; prefer upstream fixes for defects | 8/27 guidance treated it as generated and fixed |
| Difficulty gate | The initial **Responses 1 and 2 average strictly below 70%** | Use the applicable task UI; the 9/01 announcement raised the bar to 70% |
| Visuals | Encouraged where useful, including embedded visuals; not mandatory | Apply the task contract |
| Craft | Business-realistic deliverables; LLM assistance is allowed with iteration and review | Apply the applicable old specification |

Do not confuse the first two responses at the top of the task with the two
highest scores selected from all later runs. The screenshot does not restate a
new rubric-weight split or the final-rollout count. Follow the live UI on these.
The older ~30% recommendation / 5–10% instructions / ~60% supporting asks split
is historical, not a new-task rule inferred from the screenshot.

The update also says pre-September-5 failures receive no send-back feedback
under that old-spec route; a rebuttal may be submitted. Approval pays $800.
An assessment is mentioned with four attempts. Do not infer its questions,
answers, or the current availability of task slots.

## Input requirements inherited from earlier captures

The September 5 screenshot changes outputs; it does not establish that input
requirements disappeared. Until a current task UI supersedes them, use the
following as inherited package requirements and record that provenance:

- 10+ files in a single ZIP, under 50 MB total and under 10 MB per file.
- At least 4 independently necessary files, 2 substantial files, a table with
  10,000+ observations, and a decision requiring a join between tables.
- The handbook said 3+ formats; onboarding asked for 5+ formats and at least
  half the files to carry analytical weight. Plan for the stricter package
  where feasible, but do not call a local manifest PASS platform approval.
- Public domain, CC0, CC-BY or CC-BY-SA were the listed license classes.
  Verify each file and service's actual terms, including AI/training,
  commercial-use and redistribution restrictions. An open download is not a
  reuse license.
- Earlier guidance excluded Markdown as a requested deliverable. The screenshot
  does not expressly resolve that exclusion; prefer an appropriate supported
  business format unless the current task UI permits otherwise.

An internal source screen or analytical prototype is not a submission package
and need not be padded to meet these counts.

## Correctness, fairness and evidence

The task must force a defensible decision or determinate analytical result from
the supplied evidence. State the objective, units, scope, decision date and
binding constraints where they matter. Do not hide a definition to make the
model fail. Avoid giving away the solution, while keeping the problem complete.

Empirical evidence must remain real and traceable. Scenario rules, prompts and
golden deliverables may be authored with LLM assistance and reviewed. Record
their authored status; do not fabricate empirical findings or disguise AI work
as documents issued by a real organization. Preserve downloaded raw files and
record transformations separately.

A valid model failure is material analytical or methodological error, including
incorrect supporting analysis even when the final choice happens to be right.
A wrong winner is not mathematically required by the 70% threshold.
Formatting losses, unsupported tolerances, an equally valid CI convention,
missing evidence or an erroneous golden do not prove analytical difficulty.

No universal amount of noise, number of formats, hidden metadata rows, or
particular statistical method guarantees a stump. Artificial corruption and
burying a rule are not mandatory. Use authentic structure that the decision
actually depends on.

## Local workflow recommendations

These are working practices, not additional Handshake gates:

1. Screen several sources by their actual tables, study design and access.
2. Compute the defensible analysis and plausible shortcuts before polishing.
   Show which material results differ and test reasonable alternatives.
3. Use fresh solvers without golden answers, rubric or conversation history.
   Record model/harness/version, input hashes, outputs and observed errors.
4. Two clean blind solves are a useful reason to drop or substantially rethink
   a concept. This is a local stop rule, not an official response requirement.
5. Use a diagnostic run with well-organized evidence to distinguish reasoning
   difficulty from lookup burden.
6. Complete the source package and run the official initial-response gate
   before investing in the final presentation. Follow the current UI sequence.
7. Reproduce, reconcile and inspect every requested final deliverable.

A reported 9/01 answer-key context leak is an historical platform observation.
Keep solution artifacts separate from solver inputs and verify context. Do not
assume the bug persists or automatically reset/delete task state.

## Status reporting

Distinguish source discovered, license checked, files downloaded, schema
inspected, analytical prototype tested, blind screen run and platform gate run.
A check not performed is **not run**. Preserve prompt/ZIP/golden/rubric versions
together; never grade one version's response against another version's rubric.
Local authorization to create files does not authorize contacting third parties
or submitting tasks on the user's behalf.
