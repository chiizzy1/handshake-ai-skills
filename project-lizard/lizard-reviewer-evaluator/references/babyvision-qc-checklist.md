# BabyVision QC & Audit Checklist

This checklist mirrors the official BabyVision audit spec. Every reviewer should be able to point to the exact item when flagging work. Use `sqs-scoring.md` when assigning SQS scores.

## Contents

- [1. Image](#1-image)
- [2. Model Response](#2-model-response)
- [3. Prompt — Scope & Clarity](#3-prompt-scope-clarity)
- [4. Prompt — Question Design](#4-prompt-question-design)
- [5. Answer Format](#5-answer-format)
- [6. Answer Content](#6-answer-content)
- [7. Task Metadata](#7-task-metadata)
- [Minor — Pass with Note](#minor-pass-with-note)
- [Subtle Failures to Watch Closely](#subtle-failures-to-watch-closely)

---

## 1. Image

- [ ] Image is clearly visible — no blur, pixelation, or low resolution, and no watermark that covers the entire image.
- [ ] Image is eligible for BabyVision — has visual-reasoning structure (grid, maze, pattern, shadow, transformation, path). Skip generic photos with no puzzle structure, no visible pattern, chart-heavy or text-heavy images, images containing text in a foreign (non-English) language, and anything toxic.

### Subtle failure: Image looks "workable" but isn't
An image of a candid party photo has no reasoning primitive (no grid, no maze, no pattern, no shadow). Even if you could write a counting question about it ("how many fingers are visible?"), that's trivial extraction, not visual reasoning. Skip it.

---

## 2. Model Response

- [ ] Model Rating is set to Thumbs Down (👎).
- [ ] Model-generated answer box is non-empty.
- [ ] Model response is incorrect — if the live model answered correctly, the annotation is invalid and must be replaced with a harder valid question.

### Subtle failure: Model gave a partially correct answer
If the model's answer is close but wrong on a technicality (e.g., said "(4, 6)" when the correct answer is "(4, 7)"), that still counts as incorrect. The annotation is valid. But if the model's reasoning is correct and it got the final value right, the annotation is invalid regardless of how the prompt was worded.

---

## 3. Prompt — Scope & Clarity

- [ ] Prompt fits one of the BV subcategories — if it doesn't fall within a subcategory, it probably isn't a suitable question for BabyVision.
- [ ] Prompt is clearly written with a single interpretation and one verifiable answer — if two people can disagree on what's being asked, it's too ambiguous.
- [ ] If the image has multiple panels, the prompt specifies which panel the question refers to.
- [ ] If the prompt refers to an image or shape that is partially missing or cut off, it gives explicit instructions on how to count or identify it — otherwise it's ambiguous.
- [ ] Prompt is tied to the visual content — it cannot be answered without the image, and the answer is not readable from any answer key visible in the image.
- [ ] Prompt is fully standalone — no reliance on a "previous question/answer" or other annotations on the task.
- [ ] Prompt does not state or point so directly at the answer that visual reasoning disappears — the example answer must NOT equal the correct/rewrite answer.
- [ ] Prompt is written without first-person phrasing (e.g., no "I want you to…").
- [ ] Prompt does not require text-heavy reading, cultural knowledge, current events, or expert/domain-specific knowledge — it must be solvable by looking at the image alone, plus very basic knowledge such as common shapes and everyday objects. (Animal questions must be visual: "the animal with wings" is fine; "the animal that can fly" is not.)
- [ ] Prompt is short and carries a single instruction — BabyVision difficulty must come from the image, not from long or hard-to-parse sentences. **Fail prompts that stack multiple commands or bury the question in setup.**
- [ ] Prompt requires NO arithmetic and NO multi-step reasoning — calculating, comparing computed values, or chaining "first do X, then do Y" belongs to VQA, not BabyVision.
- [ ] Terminology stays simple — no school-level math and no complex terms. Advanced terms (e.g., "concave polygon," "line of symmetry," "z-value plane") are only allowed if the term is explicitly printed in the image.
- [ ] Annotation contains exactly one Question and one Answer (multi-part questions are OK).

### Subtle failure: Difficulty lives in the sentence, not the image
**Bad prompt**: "I want you to carefully examine the grid of tiger patterns and, using your visual reasoning skills, identify which specific tiger is the odd one out that does not match the others. Tell me the row and column in (row, column) format (e.g., (1,1))."

**Good prompt**: "One tiger pattern is different from the others. Which row and column is it in? Answer in the format (row, column) (e.g., (1, 1))."

Both ask the same thing — but the bad version stacks instructions, uses first-person, and inflates wording. The difficulty should come from the *image* being hard to parse, not the *sentence*.

### Subtle failure: Prompt quietly requires arithmetic
"Count the red shapes in the top half and the blue shapes in the bottom half. What is the difference?" — This chains two counting steps with a subtraction step. That's multi-step reasoning. Move it to VQA or simplify to a single visual primitive.

---

## 4. Prompt — Question Design

- [ ] Question tests a real BabyVision visual primitive (exact matching, path tracking, spatial transformation, pattern completion, structured counting) — not trivial object counting or simple label extraction.
- [ ] For counting questions, the challenge is structured visual discrimination, not just counting visible objects.
- [ ] Question has ≥2 real or implied answer options.
- [ ] Question avoids "none of the above," "all of the above," and "cannot be determined" as answer choices.
- [ ] Spatial questions use approximation wording or MCQ with sufficiently distinct options — no demands for subjective/unmeasurable spatial precision.
- [ ] **A color is never the short answer** — if the answer would be a color, the question must be converted to MCQ so the response is unambiguous. Where colors are referenced in the prompt, they are specific ("light blue"/"dark blue") rather than subjectively named.
- [ ] For matching/identification questions (e.g., Find the Same, Find the Shadow), all options/items are meaningfully distinct — no two effectively equivalent or duplicated.
- [ ] For path-tracking questions where the path crosses itself or another path, the prompt makes clear which route to follow (only needed when ambiguous).
- [ ] Grid-coordinate prompts state the row/column indexing rule explicitly AND start indexing at 1, not 0 (e.g., "rows top→bottom, columns left→right, starting at 1"). **Both are required** to remove ambiguity.
- [ ] Spatial transformation prompts explicitly define the transformation rules — axis of reflection, degrees and direction of rotation, etc.
- [ ] For pattern completion questions, only one rule explains the pattern — if multiple rules fit, fail it.
- [ ] If multiple prompts exist on a task, each is unique and not a near-duplicate of any other.

### Subtle failure: Color as short answer
**Bad**: "What color is the missing square?" → Answer: "blue"
**Good**: "What color is the missing square? Answer with a single letter (e.g., B). A. Red  B. Blue  C. Green  D. Yellow" → Answer: B

### Subtle failure: Grid coordinates without 1-based indexing
**Bad**: "Which cell is different? Answer in (row, column) format (e.g., (0, 0))."
**Good**: "Which cell is different? Answer in (row, column) format, rows numbered top to bottom and columns left to right, starting at 1 (e.g., (1, 1))."

---

## 5. Answer Format

- [ ] Prompt specifies the exact answer format (string, percent, integer, MCQ, (row, column), etc.).
- [ ] Prompt includes an example answer — and if it asks for multi-item answers, specifies the exact ordering within the example (e.g., alphabetical).
- [ ] When multiple answers are expected, that's stated explicitly (commas are used only when multiple items are required).
- [ ] Annotation uses an allowed answer type — open-ended, integer, or MCQ (in-image or in-question).
- [ ] MCQ options use strict A./B./C./D. format (letter + period, each on its own line), with **4 or fewer options** — relabel to A/B/C/D even when the options shown in the image are labeled with numbers. In the Answer field, the response is the **bare letter only** (no period, no text).
- [ ] If the answer is numeric and naturally requires rounding, the rounding rule is explicit in the prompt and the answer matches that precision.

---

## 6. Answer Content

- [ ] Rewritten answer is factually correct.
- [ ] Answer field contains ONLY the final answer — no reasoning, explanation, or commentary.
- [ ] Answer is 1–7 words — no paragraph answers. Comma- or hyphen-separated strings/numbers count as "words." Slight overages are fine with judgment; the goal is to keep answers reasonably short.
- [ ] Answer is derivable from the image without world knowledge.

---

## 7. Task Metadata

- [ ] Task has 1–3 annotations.
- [ ] Explanation field is left blank.
- [ ] Question Type is non-empty and accurately matches the annotation — MCQ is selected for both MCQ in-image and MCQ in-question answer types; short answer otherwise.
- [ ] BabyVision Type and Subtype are both non-empty and accurately reflect the visual primitive being tested (multiple categories/subcategories are allowed).

---

## Minor — Pass with Note
Flag, but do not reject:
- **Inaccurate Category**: Type/Subtype are filled in but don't accurately reflect the visual primitive being tested.
- **Unit Ambiguity**: Question or answer uses ambiguous units (e.g., M vs m, K for both magnitude and physical units).
- **Mechanical Writing**: Grammar mistakes, typos, or misspellings in the question or answer. If a grammar error alters the meaning of the overall prompt, escalate it to a Major.

---

## Subtle Failures to Watch Closely

These are the common edge cases that trip up both annotators and reviewers:

1. **Path-tracking prompts where crossings cannot be visually disambiguated** — if two lines cross and you genuinely can't tell which continues where, the prompt is invalid.
2. **Matching prompts where two options are effectively equivalent** — if options B and D are visually indistinguishable, the question has two correct answers. Fail it.
3. **Spatial prompts where orientation, hidden blocks, or fold direction is not defined** — "How many cubes?" is ambiguous if you can't tell whether hidden supporting blocks should count.
4. **Pattern prompts where the underlying rule is underdetermined** — if two different rules both explain the sequence, the "next" item is ambiguous.
5. **Counting prompts that are only trivial object counting** rather than structured visual discrimination — counting clearly visible apples on a table is not BV; counting overlapping shapes in a cluttered grid is.
6. **Prompts whose difficulty lives in the sentence** — long setup, stacked instructions, or advanced terminology — rather than in the image.
7. **Prompts that quietly require arithmetic** or a two-step chain of reasoning to reach the answer.
8. **Questions whose answer is a color but were left as short answer** instead of being converted to MCQ.
