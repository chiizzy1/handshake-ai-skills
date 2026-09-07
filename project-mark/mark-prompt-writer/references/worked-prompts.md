> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Worked Prompts

## The 60-prompt library — read this first

`HANDSHAKE-AI/Project-Mark/example-prompts.md` holds **60 example prompts in the
current 8/27 format**, ten per objective across all six, each labelled with its
domain. That is the best source for prompt shape, and it supersedes everything
below.

| Objective | Prompts |
|---|---|
| Descriptive & Distribution Analysis | 10 |
| Anomaly Detection & Diagnostics | 10 |
| Root-Cause Analysis | 10 |
| Experiment & Causal Analysis | 10 |
| Forecasting & Predictive Modeling | 10 |
| Data Extraction & Conformation (ETL) | 10 |

Find the closest match to your objective and domain and adapt it. Every one is a
stakeholder context, one committed recommendation, then 3+ named deliverables with
3+ asks each.

> ⚠️ The examples below, and the 25 accepted tasks under
> `HANDSHAKE-AI/Project-Mark/examples/`, predate 8/27. Their *reasoning* and trap
> design still hold. Their **deliverable and ask counts do not** — most ship 2 to 3
> deliverables with 2 asks each, where the floor is now 3 and 3.


Drawn from the 25 accepted examples in
`HANDSHAKE-AI/Project-Mark/examples/`. Every one is a real approved task. **Study
the shape; never reuse a prompt, dataset, or answer path.**

## Example 01 — Enterprise search incident diagnosis

Product Analytics · Root-cause · DOCX + PY + XLSX · rated "hardest"

> Cedar Code's four-hour Enterprise Search Answers pilot showed fewer successful
> searches, faster reformulations, and pressure on serving envelopes. Product
> leadership needs one committed root-cause decision before approving another
> Enterprise pilot.
>
> Using the shipped files, name one primary root cause, select one approved
> corrective action, and state whether the next pilot may proceed. **Do not hedge
> or provide a menu.**
>
> Return these three deliverables.
>
> Write a concise decision memo I can send to Product and Reliability leadership:
> `enterprise_search_launch_recommendation.docx`
> - Open with the committed cause, action, and pilot disposition, then explain why
>   the strongest competing cause and action were not selected.
> - Support the recommendation with the most decision-relevant evidence from the
>   package and identify the source records used.
>
> Hand me a runnable reproduction script: `enterprise_search_rca.py`
> - Accept the participant ZIP through `--input`, run from a clean directory, and
>   reproduce the same committed decision without hard-coded local paths or answers.
> - Separately quantify the governed margin between the committed cause and its
>   nearest competing cause, and between the selected action and its nearest
>   qualifying alternative.
>
> Include a decision-audit workbook backing the memo and script:
> `enterprise_search_decision_audit.xlsx`
> - Present the evidence and alternatives needed to audit the committed decision,
>   using clear labels and source references.
> - Use formulas for derived results and reconcile the workbook's conclusion to the
>   memo and script without hard-coding a winner flag.
>
> Across all three deliverables, report percentages to two decimal places, counts
> as whole numbers, whole-dollar amounts in USD, and unitless regret values to four
> decimal places.

**What to steal from it:**

- "Do not hedge or provide a menu" — forces the committed call explicitly.
- Every deliverable is a natural request naming its file, with exactly the asks
  that file must satisfy.
- The cross-deliverable precision paragraph at the end. Precision is
  load-bearing, so it is stated once, for the whole set.
- The script asks are demands about *behaviour* — accepts `--input`, runs clean,
  no hard-coded answers — never about method.
- Not one word about how to do the analysis. The trap (pooling the rollout hours
  breaks the registered randomization) is never hinted at.

**What made it hard**, from its own strength notes: a two-gate evidence rule
decides the root cause rather than the largest effect, and the corrective action
is selected on a governed robust-regret rule rather than on cost, speed, or mean
loss reduction. Both are honest-data traps — nothing is planted false, and a
solver who picks the biggest number or the cheapest action lands wrong.

## The two canonical shapes

### Comparative decision

> Q3 profitability fell below plan. Management must cut exactly one product
> category from the next buying cycle.
>
> Recommend the single category whose removal gives the strongest defensible
> improvement in continuing-portfolio economics.
>
> `category_decision.pdf` — a board-ready business report that makes the cut and defends it
> - Name the category to remove and the continuing-portfolio margin change the
>   removal produces, in percentage points to one decimal place.
> - Include a bar chart of continuing-portfolio margin by category (y-axis in
>   percent, one decimal), before and after the cut, with the runner-up highlighted.
>
> `category_scan.csv` — the working numbers so Finance can audit them
> - One row per category with revenue in whole USD, and direct margin and
>   continuing-portfolio margin as percentages to one decimal place.
> - A final column naming the single evidence-backed change that would make the
>   runner-up the better cut.

Note "exactly one" — the constraint a stakeholder would genuinely state, which
removes the hedge without leaking anything.

### Forecasting

> A subscription app owes Finance one committed Q3 renewal-revenue number by
> Thursday, from three years of billing history.
>
> Give a single committed Q3 renewal-revenue figure and say whether the current
> trend supports the board's growth target.
>
> `forecast.py` — a runnable script that reproduces the number from the shipped files
> - Print the committed Q3 renewal-revenue figure in USD rounded to the nearest
>   thousand, with its 80% interval in the same unit.
> - Print the holdout error for each of the last four quarters as MAPE in percent
>   to one decimal place.
>
> `finance_note.docx` — the one-page note to forward to the board
> - State the Q3 figure in USD to the nearest thousand and whether it clears the
>   board's growth target.
> - Name the single assumption that would move the number most, and by how much,
>   in USD to the nearest thousand.
>
> `monthly_actuals.csv` — backing the estimate
> - One row per month with actual and fitted renewal revenue in whole USD.
> - Flag the months excluded from training and give the reason.

Three deliverables across three families. "Flag the months excluded from training
and give the reason" asks for a *decision the analyst made*, without ever naming
which months or why — the trap stays intact.

## The tells of a returned prompt

Every one of these appears in real rejections:

| Tell | Why it fails |
|---|---|
| "Use a two-proportion z-test on the deduplicated holdout" | Names the method. Removes the method-selection difficulty |
| "Note that the summary deck may be out of date" | Narrates the trap |
| "Recommend one or more categories, if applicable" | Permits a hedge |
| "Give me a report" | No filename, no extension |
| "decision.pdf and summary.docx" | One family. Needs at least two |
| A file with a single ask | Needs at least two per file |
| "Compare against industry benchmarks" | Requires outside knowledge |
| "Also forecast next year's headcount" | A second decision, on a separate dataset |

## Reading the rest

The other 24 examples sit under
`HANDSHAKE-AI/Project-Mark/examples/<n>-<name>/example_task.md`, each with a
`## Prompt` section plus `## Why this example is strong`, `## Critical
components`, `## Step-by-step solution`, `## Justification`, and `## Rubric`.

The strength notes are the most useful part — they state exactly what made each
task hard and which competing path a model takes instead.
