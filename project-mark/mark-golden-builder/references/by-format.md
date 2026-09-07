> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Golden Structure By Output Type

The prompt names the files. This is what each family has to look like once
written. Across the whole set, one rule dominates: **the numbers agree, file to
file, exactly.**

## Text — PDF, DOCX

Order matters. The recommendation goes **first**.

1. **The committed call**, one or two sentences, naming the option it rejects and
   why the runner-up loses.
2. **Each ask the prompt attached to this file**, under a heading or label a
   grader can find without reading the whole document.
3. **The load-bearing figures**, each cited to the file and field it came from
   where the prompt asked for that.
4. **The closing passage** on why no other conclusion survives the prompt, the
   files, and standard domain knowledge.

It has to read like a normal professional memo. Not a chat reply, not a model
answer, not a template with the headings left in. No "Here is the analysis you
requested", no AI disclaimer, no invented citation.

Length follows the prompt. "A one-page decision memo" means one page.

## Data — CSV, JSON, XLSX

- One row per entity at the grain the prompt implies.
- Column headers naming the metric **and its unit**.
- Values at the precision the prompt demanded. One decimal place means every
  value carries one decimal place, including the ones that land on a round number.
- Where the prompt asked for a rank, it is a whole number.
- Where the prompt asked for a column naming what would flip the recommendation,
  that column holds a real evidence-backed change, never a placeholder.

**In XLSX, use formulas for derived results.** A workbook of pasted values cannot
be audited, and the handbook's own accepted example is explicit that the workbook
must reconcile to the memo and script "without hard-coding a winner flag". Let the
conclusion fall out of the computation.

## Visual — PPTX, PNG, SVG, HTML

The chart says what the prompt asked it to say:

- correct axis and correct unit
- correct precision in the labels
- the highlighted series the prompt named
- values **identical** to the data deliverable

A chart that disagrees with the table it was built from is the same defect as two
disagreeing numbers, and it is the easiest one for a reviewer to spot.

Where the prompt asked for a before-and-after view, both states are present and
both are labelled.

## Code — PY, IPYNB, SQL, R

The hard requirements, from the accepted examples:

- **It runs**, from a clean directory, with no hard-coded local paths.
- **It accepts the input package** through the argument the prompt names, usually
  `--input`.
- **No hard-coded answers.** If the winner is a literal in the source, the
  deliverable fails. The committed decision must be derived from the inputs.
- It **prints** the figures the prompt asked to be printed, in the units and
  precision named.
- Where the prompt asked for a margin between the winner and its nearest
  alternative, the script quantifies that separately rather than asserting it.

Run it before you ship it. "Not run" is an honest status; "reproduces" is a claim.

## Cross-deliverable precision

Where the prompt states precision requirements across the whole set — "report
percentages to two decimal places, counts as whole numbers, whole-dollar amounts
in USD, and unitless regret values to four decimal places" — that precision is
**load-bearing** and a grader checks it in every file.

Run `../../tools/mark_reconcile.py` over the finished set before every upload.
