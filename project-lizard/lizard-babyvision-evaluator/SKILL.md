---
name: lizard-babyvision-evaluator
description: Evaluate or create Project Lizard BabyVision tasks. Use when asked to write or validate BabyVision image-grounded prompts that test visual primitives (matching, tracking, spatial perception, pattern completion) without relying on text reading, arithmetic, or outside knowledge. Follows the 5-step BabyVision workflow.
---

# Project Lizard - BabyVision Evaluator Skill

This skill guides the creation and validation of BabyVision (BV) tasks for Project Lizard.
BabyVision tests whether an AI model can see and reason from visual structure, not whether it can recall facts or perform complex arithmetic. The challenge belongs in the image, not in the language — a prompt is strong when the visual reasoning is hard, not when the sentence is hard to parse.

## Core Directives

1. **Visual Primitive Only**: The challenge must come from the image, not the wording. If it needs reading dense text, arithmetic, multi-step reasoning, or outside expert/cultural knowledge, it is NOT BabyVision — it belongs in VQA.
2. **Simplified Language**: Keep prompts short — one instruction per prompt, in the simplest words that do the job. No advanced terminology unless it's printed in the image.
3. **Single Verifiable Answer**: The answer must be 100% objective, unambiguous, and format-locked.
4. **No "Clustered Color Dots"**: Images with random dots of various sizes and colors are completely unusable — auto-skip.
5. **No Explanations**: Leave the Answer Explanation tab in SuperAnnotate empty. It should always be blank when annotators submit.
6. **Prompt Text Only**: The question field should contain the prompt text and nothing else. Do not include labels like "Annotator question:", wrapping quotation marks, or surrounding formatting.
7. **Avoid Color as Short Answer**: Never use a color as a short-answer response — convert to MCQ so the answer is unambiguous. When referencing a color in the question text, be specific (e.g., "light blue" or "dark yellow"). Avoid comparing similar shades (e.g., light blue vs. dark blue) entirely, in any format.
8. **No Arithmetic or Multi-step Reasoning**: Those belong to VQA-style tasks, not BabyVision.

## The 5-Step BabyVision Workflow

### Step 1: Review the Image
Assess the pre-loaded image. Only skip if it is **truly unusable**.
- **Eligible**: Grids, shadows, mazes, pattern completion, 2D/3D spatial reasoning, structured puzzles.
- **Skip Criteria (SQS 2)**:
  - Low quality (blurry, cropped).
  - No puzzle structure (generic photos, simple scenes).
  - Text-heavy or chart-heavy (this is VQA, not BV).
  - Toxic content or foreign languages.
  - Clustered color dot images (auto-skip).
  - Requires specialized expertise you don't have.

*Annotation Scoping*: 1 is minimum, 2 is strongly recommended, 3 is the hard max. Each annotation should use different skill combinations or focus on different visual elements.

### Step 2: Write a Question
Write a prompt that exposes a visual reasoning failure.

**Step 2a — Tag Categories**: Must select at least 1 BabyVision taxonomy. Tag every category and subcategory that accurately describes what the question tests. See references for detailed guides with examples:
- [Fine-grained Visual Discrimination](references/fine-grained-discrimination.md) — Find the different, find the same, shadows, reconstruction, pattern completion, counting clusters, counting patterns
- [Spatial Perception](references/spatial-perception.md) — 3D views, cube unfold, paper folding, counting 3D blocks, 3D pattern completion
- [Visual Pattern Recognition](references/visual-pattern-recognition.md) — Logic patterns, rotation, mirroring, overlay
- [Visual Tracking](references/visual-tracking.md) — Mazes, metro maps, connect the lines, lines observation, recognize numbers/letters

**Step 2b — Apply the 5 Prompt Quality Rules**:
1. **Complex enough**: Needs visual reasoning, not just trivial counting or reading.
2. **Single verifiable answer**: Ask objectively. Include an example format that does NOT match the correct answer.
3. **Self-contained**: Must not rely on outside knowledge.
4. **Independence**: Don't reference other tasks or annotations.
5. **No giveaways**: The wording must not reveal the answer. Do NOT give away information in the prompt (e.g., "The top-left and bottom-right sections contain the most sticks" reveals where to look).

**Step 2c — Lock the Answer Format**:

*Short Answer*:
- 1-7 words max.
- Include an example answer that does NOT match the correct answer.
- **Never use colors as short answers** — convert to MCQ.
- If asking for grid coordinates, specify 1-based indexing (e.g., "(row, column) starting from 1").
- Allowed types: open-ended, integer, or MCQ.

*MCQ*:
- Max 4 options. If the image uses 1/2/3/4, relabel to A/B/C/D.
- No Yes/No or True/False questions.
- No "All/None of the above" or "cannot be determined."
- Use strict A./B./C./D. format. Rewrite Answer = bare letter only (e.g., `C`).
- Example letter must NOT match the correct answer letter.

### Step 3: Generate Model Response
Click "Generate Model Response" and wait (~20s). **Click only once.** Read the model's answer.
- **If the model is correct**: Your prompt is invalid. Return to Step 2 and write a harder question.
- **If the model fails**: Proceed to Step 4.
- **If `FINISH_REASON_LENGTH` appears**: Treat as model failure. Proceed to Step 4.
- **If the response box is empty**: Save, reload, or escalate in #lizard-v2-tasking. Do NOT submit.

### Step 4: Evaluate and Rewrite
- **Rate**: Thumbs Down the model's response. All annotations must result in 👎.
- **Rewrite**: Write the exact correct answer in the format you promised. **No explanation or reasoning in the answer field.**
- **Format match**: Compare against the example answer's format — punctuation, casing, structure.
- **Example Check**: Ensure your prompt's example does not match this correct answer.

### Step 5: Validate Your Prompt
1. Run **Check My Work**. Mark flags as Agree or Disagree. Resolve agreed flags.
2. Run **Verify Submission**. Cannot submit until all checks pass.
3. **Self-Check**:
   - Solvable from image alone?
   - Tests a BV primitive (not just observation)?
   - Unambiguous format with non-matching example?
   - Answer field contains only the final answer?
   - Grid coordinates explicitly use 1-based indexing?
   - No arithmetic or multi-step reasoning?
   - No first-person phrasing?

## Shared References
Review the common-error reference files for broader rules applicable across all Project Lizard tasks:
- `../../shared-references/common-errors/image-feasibility.md` — When to skip an image
- `../../shared-references/common-errors/trivial-questions.md` — BV triviality criteria
- `../../shared-references/common-errors/prompt-clarity.md` — How to avoid ambiguity (includes BV POV rules)
- `../../shared-references/common-errors/annotation-independence.md` — Making annotations distinct
- `../../shared-references/common-errors/answer-format-validity.md` — Format rules and MCQ formatting
- `../../shared-references/common-errors/answer-correctness.md` — Verifying rewrite answers
- `../../shared-references/common-errors/minimum-annotation-requirements.md` — Submission requirements
- `../../shared-references/updated-guidelines-and-reminders.md` — Latest best practices
