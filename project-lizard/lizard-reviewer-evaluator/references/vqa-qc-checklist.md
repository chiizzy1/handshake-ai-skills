# VQA QC & Audit Checklist

This checklist mirrors the official VQA audit spec. Every reviewer should be able to point to the exact item when flagging work. Use `sqs-scoring.md` when assigning SQS scores.

## Contents

- [1. Image](#1-image)
- [2. Model Response](#2-model-response)
- [3. Prompt — Scope & Clarity](#3-prompt-scope-clarity)
- [4. Prompt — Question Design](#4-prompt-question-design)
- [5. Answer Format](#5-answer-format)
- [6. Answer Content](#6-answer-content)
- [7. Task Metadata & Ontology](#7-task-metadata-ontology)
- [Minor — Pass with Note](#minor-pass-with-note)
- [Subtle Failures to Watch Closely](#subtle-failures-to-watch-closely)

---

## 1. Image

- [ ] Image is clearly visible — any text or numbers needed to solve the question are legible, with no blur, pixelation, or low resolution. Skip if a watermark covers the entire image or obscures a specific subject of the prompt.
- [ ] Image contains enough content for a meaningful annotation — generic portraits, movie posters, overly simple scenes, images containing text in a foreign (non-English) language, and unreadable or toxic images are NOT workable.

---

## 2. Model Response

- [ ] Model Rating is set to Thumbs Down (👎).
- [ ] Model-generated answer box is non-empty.
- [ ] Model response is incorrect — if the live model answered correctly, the annotation is invalid and must be replaced with a harder valid question.

---

## 3. Prompt — Scope & Clarity

- [ ] Prompt is clearly written with a single interpretation and one verifiable answer — if two people can disagree on what's being asked, it's too ambiguous.
- [ ] If the image has multiple panels, the prompt specifies which panel the question refers to.
- [ ] Prompt is tied to the visual content — it cannot be answered from the title/caption alone or without the image.
- [ ] Prompt is fully standalone — no reliance on a "previous question/answer" or other annotations on the task.
- [ ] Prompt does not state or point so directly at the answer that visual reasoning disappears — the example answer must NOT equal the correct/rewrite answer.
- [ ] Prompt is written without first-person phrasing (e.g., no "I want you to…").
- [ ] Prompt avoids unnecessary wording, procedural steps, or performative complexity — ≤5 steps, and no excessive enumeration (max count of 50).
- [ ] If the prompt involves multiple steps, they are structured as a clear sequence of commands (Command 1 → Command 2 → Final Question), not unrelated separate questions.
- [ ] Annotation contains exactly one Question and one Answer (multi-part questions are OK). A question mark is not required as long as the prompt is valid.
- [ ] If multiple prompts exist on a task, each is unique and not a near-duplicate of any other — each must use different skill combinations or focus on entirely different visual components.

### Subtle failure: Answerable from the title alone
**Bad**: "What does this chart show?" when the chart title says "Q3 2024 Revenue by Region" — the model can answer from the title without understanding the chart data.
**Good**: "Which region had the highest revenue growth between Q2 and Q3? Answer as one word (e.g., Europe)." — requires actually reading the chart bars.

### Subtle failure: Two stacked unrelated questions
**Bad**: "Calculate the difference between 'Work from home' and 'On site' for each industry, and which industry has the highest 'Work from home' percentage?"
**Good**: "Calculate the difference between 'Work from home' and 'On site / office' for each industry. Which industry shows the largest positive difference in favor of 'Work from home'? Answer as the name of the industry (e.g., Public administration)."

---

## 4. Prompt — Question Design

- [ ] Question requires multi-step reasoning or interpretation — not trivial surface-level extraction (e.g., simply reading numbers from a chart, or extraction + basic arithmetic).
- [ ] Question has ≥4 real or implied answer options — binary or true/false questions are not allowed.
- [ ] Question avoids "none of the above," "all of the above," and "cannot be determined" as answer choices.
- [ ] Spatial questions use approximation wording or MCQ with sufficiently distinct options — no demands for subjective/unmeasurable spatial precision.
- [ ] Color references are specific — for shades of blue or yellow, use "light blue"/"dark blue" etc. rather than subjective color naming.
- [ ] For line/time-series charts, the question asks about a specific value or comparison, not an overall trend where many answers could be defensible. **Prompts with more than one possible answer are a Major fail.**
- [ ] Label, category, or legend prompts and answers use the exact text shown in the chart — not a paraphrase or abbreviation.
- [ ] If an exact value cannot be determined from the chart, the prompt asks for an approximation and the answer reflects a reasonable level of precision.

### Subtle failure: Trend question with many defensible answers
**Bad**: "Which line shows the most growth over the period?" — on a chart with several similar-slope lines, multiple answers are defensible.
**Good**: "At the 200-epoch mark, which model achieves the highest Top-1 Accuracy? Answer using the exact legend label (e.g., ResNet-50)." — one specific value, one answer.

### Subtle failure: Paraphrased chart text
**Bad**: Answer is "Public Admin" when the chart says "Public administration" — use exact chart text.
**Good**: Answer matches exactly: "Public administration"

---

## 5. Answer Format

- [ ] Prompt specifies the exact answer format — string/percent/integer/MCQ, lowercase, comma separators on numbers, whether the percent sign or dollar sign is included, etc.
- [ ] When a prompt asks for a percentage, the format explicitly says "answer as a percentage" to avoid confusion between values like 99.3 and 0.9930.
- [ ] Prompt includes an example answer — and if it asks for multi-item answers, specifies the exact ordering within the example (e.g., alphabetical).
- [ ] When multiple values are expected, that's stated explicitly (commas are used only when multiple items are required).
- [ ] MCQ options use strict A./B./C./D. format (letter + period, each on its own line), with **at least 4 options** that are 1–7 words each. In the Answer field, the response is the **bare letter only** (no period, no text).
- [ ] If the answer is numeric and naturally requires rounding, the rounding rule is explicit in the prompt and the answer matches that precision. If multiple arithmetic steps are needed, intermediate rounding is specified.

### Subtle failure: Percentage vs. decimal ambiguity
**Bad**: "What total percentage of respondents selected the top two options?" → Is the answer "99.3" or "0.993"?
**Good**: "What total percentage of respondents selected the top two options? Answer as a percentage (e.g., 45%)." → Unambiguous: "99.3%"

### Subtle failure: Example format doesn't match the real scale
**Bad**: "Answer as a whole number (e.g., 350)" but the real answer is in the millions.
**Good**: "Answer as a whole number with comma separators (e.g., 8,000,000)."

---

## 6. Answer Content

- [ ] Rewritten answer is factually correct.
- [ ] Answer field contains ONLY the final answer — no reasoning, explanation, or commentary.
- [ ] Answer is 1–7 words — no paragraph answers. Comma- or hyphen-separated strings/numbers count as "words." Slight overages are fine with judgment; the goal is to keep answers reasonably short.
- [ ] Answer is derivable from the image (with or without world knowledge). If numeric, the value is directly readable from a label, tick, or gridline — not estimated, unless approximation language is used.

---

## 7. Task Metadata & Ontology

- [ ] Task has 1–3 annotations.
- [ ] Explanation field is left blank.
- [ ] Question Type is non-empty and accurately matches the annotation (MCQ or short answer).
- [ ] **Core Skills**: At least one of Logical Reasoning, Table/Chart/Graph Understanding, or World Knowledge is tagged.
- [ ] **Skill count**: At least 2 skills tagged in the Ontology section, or at least 3 if Enumeration is used.
- [ ] The tagged skills accurately reflect the type of reasoning the question requires.

---

## Minor — Pass with Note
Flag, but do not reject:
- **Unit Ambiguity**: Question or answer uses ambiguous units (e.g., M vs m, K for both magnitude and physical units).
- **Mechanical Writing**: Grammar mistakes, typos, or misspellings in the question or answer. If a grammar error alters the meaning of the overall prompt, escalate it to a Major.
- **Inaccurate Ontology**: Skills are tagged but don't accurately reflect the reasoning the question requires.

---

## Subtle Failures to Watch Closely

These are the common edge cases that trip up both annotators and reviewers:

1. **Chart questions where more than one value or trend could be defensibly correct** — if two bars are nearly the same height and the question asks "which is taller?", the answer is ambiguous. Fail it.
2. **Label/legend answers that paraphrase or abbreviate the chart text** instead of matching it exactly — "Pub. Admin" vs "Public administration". Use exact text.
3. **Numeric answers that were estimated** when the value is actually readable from a tick or gridline — don't estimate when precision is available.
4. **Percentage vs. decimal ambiguity** when the format doesn't say "answer as a percentage" — 99.3 and 0.993 are both defensible without explicit format.
5. **Multi-step prompts written as separate unrelated questions** rather than a chained sequence — "What is X? Also, what is Y?" is two questions, not a sequence.
6. **Prompts that are technically answerable from the title/caption** without needing the image — if the title contains the answer, the prompt doesn't test visual reasoning.
7. **Performative complexity** — prompts that are long and procedural but only require simple extraction when you strip away the wording.
