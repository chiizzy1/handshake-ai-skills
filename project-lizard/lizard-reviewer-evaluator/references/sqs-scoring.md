# SQS Scoring Reference

SQS (Submission Quality Score) is the score reviewers assign to rate the quality of an annotator's work. This score is logged in the Shadow Task on Handshake and directly affects annotator quality metrics.

## Important Changes

- **SQS 1 is retired** (July 13, 2026). Roll any score you would have given as SQS 1 into SQS 2. Unusable images are still routed to Unusable via the shortened shadow-task flow — the only change is the score label.
- **Follow the SQS Score Rubric exactly** — do not deviate. Everything is a pass except for unannotatable images, but certain error modes trigger different SQS scores.

## SQS Score Meanings

| Score | Meaning | When to Use |
|-------|---------|-------------|
| **SQS 5** | Excellent | Annotation is strong, accurate, well-formatted, and requires no edits. |
| **SQS 4** | Good | Minor issues only (inaccurate ontology, unit ambiguity, mechanical writing errors that don't change meaning). Pass with note. |
| **SQS 3** | Acceptable | Annotation needed meaningful edits but was salvageable in a single review session (prompt rewrite, answer correction, format fix). |
| **SQS 2** | Poor / Unusable | Annotation has major errors, OR the image is unusable. Use for tasks routed to Unusable. Also used for any score you would have previously assigned as SQS 1. |

## Scoring Guidelines

1. **Ground every review against the QC Checklists** — they are the rubric your SQS scores and edits should reference. See `babyvision-qc-checklist.md` or `vqa-qc-checklist.md`.
2. **Name the error mode** in your Shadow Task justification — don't just say "fixed." Say which checklist item failed and what you changed.
3. **Be consistent** — follow the rubric exactly so all reviewers produce comparable SQS distributions.
4. **Minor errors don't drop the score below 4** — inaccurate ontology, typos, and unit ambiguity are pass-with-note issues, not failures.
5. **Major errors drop to 3** — wrong answer, unclear prompt, giveaway in the example, missing format constraints.
6. **Unusable or unsalvageable drops to 2** — image is not workable, or the annotation is so far gone it needed a complete rewrite.

## SQS for Skipped/Unusable Tasks

- **Annotator-skipped images routed to Skipped**: Log 1 Shadow Task per image. Score based on whether the skip was justified.
- **Annotator-skipped images routed to Unusable**: Log 1 Shadow Task per image at SQS 2.
- **Standard QC reviews**: Log 1 Shadow Task per individual annotation (not per image).

## Recommended Reviewer Mindset

Focus on the actual goal of the project when reviewing and scoring. The purpose is to:
- **Improve model understanding** of charts, tables, and graphs.
- **Avoid pure data extraction** (e.g., "What is the title?" or "Count the number of categories") — these are too trivial.
- **Avoid confusing "puzzle-style" prompts** (artificial complexity) — the difficulty should come from the image, not from convoluted wording.

Anchor your reasoning in the rubric so the rubric — not personal judgment — backs each score.
