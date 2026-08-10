---
name: handshake-ego-phys-understanding
description: Create or evaluate Handshake Egocentric Physical Understanding tasks. Use when asked to write image-dependent multiple-choice questions from first-person images, handle categories like Counting, Safety, Task Planning, Trajectory Reasoning, Grasp Affordance, Spatial Reasoning, State Estimation, Task Progress, or decide skip/change-category for Ego Phys tasks.
---

# Handshake Ego Phys Understanding

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-Ego Phys Understanding.pdf` as the source of truth.

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

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answer in a clean markdown format directly in the chat using the exact template below.

```markdown
### Scene Read
[Objects, object states (open/closed, on/off, in progress), the action underway, and any hazards or constraints visible in the image(s).]

### Decision
[Proceed, change category (name the new category and why), or skip (name the reason).]

### Question
[One image-dependent question that meets the assigned category standard.]

### Answer Choices
A. [choice]
B. [choice]
C. [choice]
D. [choice]

### Correct Answer
[Letter, plus one line naming the visible evidence that makes it unambiguous.]
```

## Final Checklist

- Question cannot be answered without the image.
- Question meets the assigned category standard.
- Wrong choices are scene-grounded near-misses.
- Correct answer is unambiguous from visible evidence.
- Multi-frame question requires both frames when applicable.
