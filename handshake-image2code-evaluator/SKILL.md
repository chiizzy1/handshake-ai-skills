---
name: handshake-image2code-evaluator
description: Evaluate Handshake Image2Code side-by-side tasks. Use when comparing two rendered outputs against a reference image or reference frames across Structure & Instruction Following, Visual Quality, Text & Data Accuracy, and Overall Preference.
---

# Handshake Image2Code Evaluator

## Core Rule

Use the Image2Code guidelines as the source of truth:

- `HANDSHAKE-AI/pdfs/image2code.md`

Before rating a live task, read `references/rubric.md`.

## Task Shape

You compare two rendered outputs, usually Output A and Output B, against one reference image or a set of reference frames.

The task may include:

- `user_prompt_text`, which tells the target format;
- one or more reference images;
- animation keyframes or a short clip;
- scrolling website frames at 0, 25, 50, 75, and 100 percent;
- optional image assets;
- two static rendered outputs.

The reference image is the primary spec.

## Workflow

1. Read the user prompt.
2. Study the reference image or all reference frames first.
3. Open both rendered outputs side by side with the reference visible.
4. Apply the render gate before scoring.
5. For multi-frame tasks, compare each output frame against the matching reference frame at the same time or scroll position.
6. Rate each dimension independently:
   - Structure & Instruction Following
   - Visual Quality
   - Text & Data Accuracy
7. Pick Overall Preference.
8. Write a short 2 to 3 sentence justification with concrete evidence.

## Hard Gates

- Do not judge from memory. Keep the reference visible.
- Do not compare an animation or scrolling output to the wrong frame.
- Do not test live interactivity. Image2Code outputs are static rendered outputs unless the task UI explicitly says otherwise.
- Do not default to Tie when a dimension does not apply. Use N/A on live tasks.
- Do not use N/A on quiz tasks when the quiz only offers A is better, Tie, or B is better.
- Do not penalize missing assets when the asset list is empty.
- If one render is empty, broken, white, black, a tiny fragment, or fails to render, it loses every applicable dimension.
- If the reference is corrupt, unreadable, or nonsensical, flag or skip instead of forcing a rating.

## Dimensions

Live tasks use these three dimensions plus Overall Preference:

- Structure & Instruction Following
- Visual Quality
- Text & Data Accuracy

Quiz tasks may collapse the scale to:

- A is better
- Tie
- B is better

Use the exact labels shown by the task UI.

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

## Comment Style

Write like a normal person comparing the render to the reference. Keep it short and concrete.

Good:

`Response B is better because it keeps the chart bars in the right order and matches the axis labels more closely. Response A has cleaner colors, but it changes two values, so the data errors matter more.`

Bad:

`Response B demonstrates superior multimodal reconstruction fidelity.`

## Final Checklist

- Reference image or frames were inspected.
- Both outputs were compared side by side with the reference.
- Render gate was applied.
- Multi-frame outputs were matched to the correct reference frame.
- Structure, visual quality, and text/data were scored separately.
- N/A was used only when allowed and truly applicable.
- Final justification names concrete visual or text evidence.
