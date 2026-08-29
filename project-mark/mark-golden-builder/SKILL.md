---
name: mark-golden-builder
description: Build the Project Mark golden deliverable set. Use when producing the reference answers a fully correct analyst would hand back — every file the prompt named, in the named format, under the named filename, with one consistent set of numbers across all of them. Covers structure by output type, traceability, cross-file reconciliation, and the manual QC checklist.
---

# Project Mark — Golden Builder

The golden deliverables are the last step of the build. The prompt commits the
analyst to one recommendation and names three or more output files with their asks; the
input files carry the evidence; the golden set is the finished work a fully
correct analyst would hand back.

There are no separate Justification or Assumptions fields to fill in, and no
five-field form. **Everything a grader needs lives inside the deliverables
themselves.**

## Hard Gates

- **Types, filenames, and count match the prompt exactly.** If the prompt asks for
  a PDF, a CSV, and a Python file, the golden is those three files under those
  three names. A missing file or a mismatched format blocks confirmation.
- **One set of numbers across all files.** The recommendation, every answer, and
  every table and chart agree exactly, file to file. **A grader will diff them
  against each other. Numbers that disagree across files is the most common
  defect on the project.**
- **Nothing extra.** No answers to asks the prompt did not make, no AI
  disclaimers, no placeholders, no files the prompt did not request.
- **Every claim and number traces to a shipped input file.** If a figure appears
  that no step of your analysis produced, or a claim rests on knowledge not in the
  workspace, the chain is broken and the set is not ready.

## What Goes Inside

The recommendation is stated in whichever file most naturally carries it — usually
the text or code deliverable — **first, in one or two sentences, naming what it
rejects**. Every other ask is answered in the specific file the prompt attached it
to, labelled so a grader can find it without reading the whole set.

Across the whole set, all five must be covered somewhere:

- [ ] The committed recommendation, stated first in its file, in one or two sentences, naming what it rejects
- [ ] One clearly labelled answer per ask, placed in the file the prompt attached it to
- [ ] The load-bearing figures behind each answer, each traceable to a shipped input file
- [ ] The path from raw files to the decision, including at least one trap refused, stated as a decision
- [ ] A short closing passage on why no other conclusion survives the prompt, the files, and standard domain knowledge

Reasoning sits with the answer it supports, not in a separate essay.

## Critical Components

> **At least four. Generally no more than ten.** More does not mean stronger, and
> **if one component negates another you have called critical, the task works
> against itself.**

The recommendation statement itself is **plain, concise, a single unambiguous
decision, and must not include any rationales or justifications** — those live in
the critical components, the step-by-step, and the deliverables.

Full guidance on all three rubric-feeding sections is in
`references/critical-components.md`.


The discrete load-bearing findings the solution rests on. The accepted examples
carry them as their own `## Critical components` section, and the rubric is
generated against them, so a vague one produces a criterion that grades
impressions.

**Every critical component is specific, numeric where a number decides it, and
falsifiable against a shipped file.** It names the analytical move that produces
the figure, not just the figure.

| | |
|---|---|
| Strong | "Recurring revenue is $38M once related-party sales are removed." |
| Strong | "Its lower 95 percent attribution share is 21.68 percent, below the 25.00 percent lower-bound gate." |
| Strong | "OP-318 loses the governed robust-regret comparison: Q90 regret 0.0230 against OP-284's 0.0170." |
| Weak | "The financials look weak, growth is slowing, and customer concentration is a concern." |
| Weak | "There are several red flags in the fundamentals." |
| Weak | "Management's growth projections seem optimistic relative to the market." |

The weak ones share a shape: an impression with no figure, no threshold, and
nothing a grader can check. "Several", "seem", "a concern" are the tells.

The test: **could a reviewer confirm or refute this from the shipped files
alone?** If not, it is not a critical component — it is a summary sentence, and it
belongs in the closing passage if anywhere.

The two real examples above come from example 01 in
`HANDSHAKE-AI/Project-Mark/examples/`. Read that section of any accepted example
before writing your own.

## Structure By Output Type

### Text goldens — PDF, DOCX

Open with the recommendation. One or two sentences, naming the option it rejects
and why the runner-up loses. Then the asks the prompt attached to this file, each
under a heading or label a grader can find. Close with the passage on why no
other conclusion survives.

It must read like a normal professional memo or report — not like a chat reply, a
model answer, or a template with the headings left in.

### Data goldens — CSV, JSON, XLSX

One row per entity at the grain the prompt implies. Column headers that name the
metric and its unit. Values at the precision the prompt required — if it said one
decimal place, every value carries one decimal place.

In XLSX, use **formulas for derived results** rather than pasted values, so the
workbook is auditable and the reconciliation is visible. Do not hard-code a
winner flag; let it fall out of the computation.

Where the prompt asked for a column naming what would flip the recommendation,
that column carries a real, evidence-backed change, not a placeholder.

### Visual goldens — PPTX, PNG, HTML

The chart says what the prompt asked it to say: correct axis, correct unit,
correct precision in the labels, the highlighted series the prompt named. Chart
values must equal the values in the data deliverable exactly.

A chart that disagrees with the table it was built from is the same defect as two
disagreeing numbers, and it is the easiest one for a reviewer to spot.

### Code goldens — PY, IPYNB, SQL, R

It must **run**, from a clean directory, and reproduce the committed decision from
the shipped inputs. No hard-coded local paths. No hard-coded answers — if the
winner is a literal in the source, the deliverable fails.

Accept the input package through an argument where the prompt says so. Print the
figures the prompt asked to be printed, in the units and precision it named.

## Traceability

Run this before you consider the set finished.

| Check | How |
|---|---|
| Every number appears in at least two places consistently | `../tools/mark_reconcile.py` |
| Every number traces to an input file | Name the file and field for each load-bearing figure |
| No number appears that your analysis did not produce | Walk the golden backwards, figure by figure |
| Precision matches the prompt | Decimal places, units, rounding, whole numbers |

`../tools/mark_reconcile.py` extracts numbers from the whole golden set — PDF,
DOCX, XLSX, CSV, and the stdout of a PY deliverable — and reports disagreements
across files. Run it before every upload. It is the cheapest defect to fix and
the most expensive to have found for you.

## Manual QC Checklist

Four checks, and none of them is mechanical.

- [ ] Answers the recommendation question and every ask in the prompt
- [ ] Contains no placeholders, TODOs, or unfinished sections
- [ ] No chat-style introduction, AI disclaimer, invented citation, or generic filler
- [ ] Reads and looks like a normal professional deliverable in this format

## What Happens Next

The rubric is generated internally from the prompt contract and these
deliverables, then you review it once. If you later change the prompt or the
golden, the rubric returns to review — that is expected, it is downstream of both.

→ **`mark-validator`**

## Output Format

```
## Golden set

### <filename.ext> — <family>
Answers: <which asks>
Recommendation stated here: yes/no
<summary of contents>

### <filename.ext> — <family>
...

## Reconciled figures
| Figure | Value | Unit | Precision | Appears in | Traces to |
|---|---|---|---|---|---|

## Contract match
Prompt named: <files>
Golden delivers: <files>
Match: ✓/✗

## Reconciliation
mark_reconcile.py: <clean / disagreements listed>

## QC
Every ask answered ✓/✗   No placeholders ✓/✗   No AI tells ✓/✗
Reads professional ✓/✗
```

If the code deliverable was not actually executed from a clean directory, say
so — "not run" is an honest status, "reproduces" is a claim.
