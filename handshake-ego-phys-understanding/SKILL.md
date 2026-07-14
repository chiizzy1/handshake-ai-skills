---
name: handshake-ego-phys-understanding
description: Create or evaluate Handshake Egocentric Physical Understanding tasks. Use when Codex must write image-dependent multiple-choice questions from first-person images, handle categories like Counting, Safety, Task Planning, Trajectory Reasoning, Grasp Affordance, Spatial Reasoning, State Estimation, Task Progress, or decide skip/change-category for Ego Phys tasks.
---

# Handshake Ego Phys Understanding

## Core Rule

Use `HANDSHAKE-AI/pdfs/handshake-Ego Phys Understanding.pdf` as the source of truth.

Before writing or evaluating a live Ego Phys task, read `references/rubric.md`.

## Golden Rule

If someone can answer the question without looking at the image, it fails.

Ask why, how much progress, what next, or what risk. Do not ask simple "what is this" recognition questions.

## Hard Gates

- Do not write a question that can be answered from common sense alone.
- Do not write object-recognition questions.
- Do not use throwaway distractors.
- Do not use "all of the above," "none of the above," or equivalent shortcuts.
- Do not skip because the category is hard. Change category only when another category clearly fits better.
- For multi-frame tasks, do not write a question answerable from one frame alone.

## Workflow

1. Identify whether the task is single-frame or multi-frame.
2. Read the assigned category.
3. Study the image(s) from the first-person perspective.
4. Decide proceed, change category, or skip.
5. Write one image-dependent question.
6. Write four answer choices: one clearly correct, three near-miss distractors.
7. Select the correct answer.

## Multi-Frame Rule

For multi-frame tasks, the question must require both images. If covering Image 1 still lets you answer from Image 2 alone, the question fails.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
```

## Final Checklist

- Question cannot be answered without the image.
- Question meets the assigned category standard.
- Wrong choices are scene-grounded near-misses.
- Correct answer is unambiguous from visible evidence.
- Multi-frame question requires both frames when applicable.
