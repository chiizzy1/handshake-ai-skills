> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Traceability

Every claim and every number in every file must trace back to a shipped input
file.

The chain is broken when:

- a figure appears in one deliverable that no step of your analysis produced
- a claim rests on knowledge that is not in the workspace
- a number disagrees with the same number in another deliverable

The third is the most common defect on the project.

## The trace table

Build this as you go, not afterwards. It is also the fastest way to answer a
reviewer's question.

| Figure | Value | Unit | Precision | Appears in | Derived from | How |
|---|---|---|---|---|---|---|
| Continuing-portfolio margin change | -2.7 | pp | 1dp | decision.pdf, scan.csv | txns_2024.csv, categories.xlsx | Margin recomputed excluding cut category, joined on category_id |

The "How" column is what makes Gate 1 pass. A finding that only reproduces with
an assumption living in your head is not reproducible.

## What the reviewer does

The reviewer independently reproduces every load-bearing number from the
submitted files: joins, filters, denominators, cohort or population definitions,
cleaning, transformations, normalization, QC, statistical calculations,
predictive validation, thresholds, and decision rules.

Then compares the recommendation, every supplementary answer, and every figure
inside the golden **against each other**, flagging stale numbers, copied text, and
contradictions.

So the two questions to answer before uploading are exactly those:

1. Does every number come back out of the frozen archive?
2. Do all the deliverables say the same thing?

## Tooling

`../../tools/mark_reconcile.py <golden_dir>` answers question 2 mechanically. It
reads DOCX, XLSX, CSV, JSON and source files with no dependencies; PDF needs
`pdfplumber` or `pypdf`, and without one it reports the file as **unread** rather
than silently skipping it — check that line, because an unread deliverable means
its numbers were never diffed.

It reports three things:

- **Figures agreeing across files** — the reconciled set
- **Near misses** — two files carrying almost-but-not-quite the same figure.
  Either one file rounds what another states precisely, which is fine when the
  prompt asked for that precision, or they disagree, which is the defect
- **Figures in only one file** — normal for file-specific detail, a defect when
  the value is load-bearing and should have been echoed

It finds numeric disagreement. It cannot tell you whether a figure is *correct*.
That is Gate 1, and it is manual.
