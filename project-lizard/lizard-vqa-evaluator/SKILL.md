---
name: lizard-vqa-evaluator
description: Evaluate or create Project Lizard VQA tasks. Use when asked to write or validate VQA image-grounded prompts that test complex visual reasoning on charts, tables, infographics, and data-dense images. Follows the 5-step VQA workflow and stumping strategies.
---

# Project Lizard - VQA Evaluator Skill

This skill guides the creation and validation of Visual Question Answering (VQA) tasks for Project Lizard.
VQA requires reading, multi-step logical reasoning, math reasoning, or chart/table understanding, making it distinct from BabyVision.

## Core Directives

1. **Complex Reasoning**: Every question must challenge the model on at least **2 skills**. If using *Enumeration*, it must use **3+ skills**.
2. **Anchor Skill**: Every prompt MUST include at least one of: *Logical Reasoning*, *Table/Chart/Graph Understanding*, or *World Knowledge*.
3. **Single Verifiable Answer**: 1-7 words. Must be unambiguously formatted.
4. **No Explanations**: Do NOT write anything in the Answer Explanation tab. It should always be blank when annotators submit.
5. **Prompt Text Only**: The question field should contain the prompt text and nothing else. Do not include labels like "Annotator question:", wrapping quotation marks around the entire prompt, or any other surrounding formatting.
6. **Use Second/Third Person**: Avoid first-person singular. Use constructions like "we can observe that…" or direct address with "you." Never write "I want you to…".
7. **Avoid Color in Short Answer**: Do not ask about color in short answer prompts — color naming is too subjective. If your prompt involves color, write it as an MCQ. Avoid comparing similar shades (e.g., light blue vs. dark blue) entirely, in any format.

## The 5-Step VQA Workflow

### Step 1: Review the Image
Assess the pre-loaded image. Work the image first — skip only if truly unusable.
- **Eligible**: Charts, tables, infographics, data-dense documents.
- **Skip Criteria**:
  - Low quality (blurry, text too small).
  - Too simple (minimalist scenes, basic portraits, no data).
  - Flyers/posters with NO data/charts.
  - Toxic content or foreign languages.
  - Requires niche specialized knowledge you don't possess.

*Annotation Scoping*: 1 is minimum, 2 is strongly recommended (must be distinct skills/focus), 3 is the hard max. Each annotation should focus on different visual elements and use different skill combinations. If two annotations feel similar, cut to one.

### Step 2: Write a Question
Write a prompt to expose a model failure.

**Step 2a — Tag Skills**: Pick at least 2. (Enumeration requires 3+). One must be an anchor skill.
- *Enumeration* — Counting objects or listing them. Max count 50. Use filtering to restrict counted items.
- *Attribute Perception* — Color, shape, case sensitivity. Letters/numbers are NOT attribute perception, but recognizing case sensitivity is.
- *Spatial Reasoning* — Location, relative position, chart positions, 2D/3D geometry, depth.
- *Math Reasoning* — Calculations, greater/lower comparisons, min/max, sum, difference, average, median, variance.
- **Anchor**: *Logical Reasoning* — Drawing conclusions, recognizing patterns, testing assumptions.
- **Anchor**: *Table/Chart/Graph Understanding* — Interpreting visual representations of interconnected values. Note: chart attributes like x-axis or y-axis labels do NOT qualify on their own.
- **Anchor**: *World Knowledge* — Public information outside the image (e.g., sides on a stop sign, minutes in an hour, value of pi). Must be timeless, not reference changing facts, and must be relevant to the image.

**Step 2b — Apply the 5 Prompt Quality Rules**:
1. **Complex enough**: Don't just ask to read a label. Requires reasoning, not just recognition.
2. **Single verifiable answer**: Provide an example format that DOES NOT match the correct answer. The example answer's value must never equal the rewrite answer.
3. **Self-contained**: Answer must be derivable from image (plus basic world knowledge if tagged).
4. **Independence**: Don't reference other tasks or annotations.
5. **No giveaways**: Don't reveal the answer in the prompt or in the example answer.

**Step 2c — Lock the Answer Format**:

*Short Answer*:
- Include an example answer in the prompt (e.g., "Answer as a single number (e.g., 3)").
- 1-7 words max, strictly enforced.
- Formatting must be explicitly requested: thousands separators, dollar signs, percentage signs, units — all must appear in the example if you want them in the response.
- No True/False or Yes/No questions.
- No colors as short answers.

*MCQ*:
- Include an example answer (e.g., "Answer with a single letter (e.g., B)"). The example letter must NOT be the correct answer letter.
- Minimum 4 options. Each option 1-7 words, strictly enforced.
- No "All of the above" or "None of the above."
- Use strict format: `A. text` / `B. text` / `C. text` / `D. text` — one option per line. No "Option" prefix.
- Rewrite Answer = bare letter only (e.g., `C`). Not `C.`, not `C. text`, not `Option C`.

### Step 3: Generate Model Response
Click "Generate Model Response". Wait up to 20s. **Click only once** — do not click repeatedly.
- **If the model answers correctly**: Your prompt is invalid. Rewrite it harder (see [Stumping Strategies](references/stumping-strategies.md)) and regenerate.
- **If the model fails**: Proceed to Step 4.
- **If `FINISH_REASON_LENGTH` appears**: Treat it as a model failure — the model wasn't able to answer your question. Proceed to Step 4.
- **If the model response box is empty / no response after 20s**: Save your work in SuperAnnotate, then reload the page. If that doesn't work, report it in #lizard-v2-tasking on Slack. Do NOT skip or submit with a blank response.

### Step 4: Evaluate and Rewrite
- **Rate**: Thumbs Down the model's response. All annotations must result in Thumbs Down.
- **Rewrite**: Write the exact correct answer in the required format. **NO explanation text, just the final answer.**
- **Format match**: Compare your Rewrite Answer against the format of the example answer. Matching punctuation, casing, units, rounding, and structure is as important as getting the value right. A correct value in the wrong format will be penalized.
- **Example check**: Ensure the example answer value does NOT match the Rewrite Answer value.

**If the model keeps answering correctly** — work through this order:
1. **Rerun the model**: Go back to Step 3 and generate again — up to 3 runs. Never exceed 5 runs without changing something. If the model answers incorrectly at any point, proceed.
2. **Rewrite the question**: If correct every time, return to Step 2, change the text, then rerun.
3. **Start small, then overhaul**: Begin with smaller rewrites. If small changes aren't stumping the model, try a completely different ontology — overhaul the question entirely.

### Step 5: Validate Your Prompt
1. Run **Check My Work**. Mark flags as Agree or Disagree. If you agree, fix the issue, regenerate, and re-run Check My Work.
2. Run **Verify Submission**. This checks all items in work validation across all annotations have passed. You cannot submit to QC until all checks pass.
3. Use the **Quality Checker AI** feedback in the Shadow Task before final submission. It is advisory, not a grade. Read every flag seriously — most of the time it's pointing at something real. But if you have a concrete reason why your annotation is correct as written, you can disagree and move ahead.

## Stumping Strategies
To make questions harder, use techniques like Rank-n on limited ranges, Legend-binding, Close Comparisons, combined counting, Math with visual grounding, Trend/Density, Heatmap lookup, or Graph traversal. See [Stumping Strategies](references/stumping-strategies.md) for details and examples.

## Shared References
Review the common-error reference files for broader rules applicable across all Project Lizard tasks:
- `../../shared-references/common-errors/image-feasibility.md` — When to skip an image
- `../../shared-references/common-errors/trivial-questions.md` — What makes a question too easy
- `../../shared-references/common-errors/prompt-clarity.md` — How to avoid ambiguity
- `../../shared-references/common-errors/annotation-independence.md` — Making annotations distinct
- `../../shared-references/common-errors/answer-format-validity.md` — Format rules and MCQ formatting
- `../../shared-references/common-errors/answer-correctness.md` — Verifying rewrite answers
- `../../shared-references/common-errors/minimum-annotation-requirements.md` — Submission requirements
- `../../shared-references/updated-guidelines-and-reminders.md` — Latest best practices
