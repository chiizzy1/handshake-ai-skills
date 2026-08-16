---
name: handshake-find-boundary
description: Handle Handshake Find the Boundary image-grounding tasks. Use when asked to write or judge prompts for bounding box, point, or counting outputs; decide whether the model passed or failed; correct boxes, points, counts, traces, tags, or confidence; or identify hard image/prompt boundary cases.
---

# Handshake Find Boundary

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-Find the Boundary.pdf` as the source of truth.

Before doing a live task, read `references/rubric.md`.

## Goal

Find the model's capability boundary, not easy wins. A good submission tests an image/prompt pair the model has a real chance of getting right or wrong.

Images may be uploaded directly or supplied by URL. Judge only the visible image content, regardless of how the image entered the task.

Treat every round as one of three outcomes:

- pass / "AI wins": the model is correct as-is;
- break / "I win": the model is wrong and the answer is corrected;
- discard / rewrite: the prompt is ambiguous, ungroundable, or references non-visible content.

Do not score malformed prompts as model failures.

## Output Modes

- Bounding box: draw a tight box around described object(s).
- Point: place one point on the described object.
- Counting: count matching objects and return one point per instance.

Do not switch formats mid-task to force a pass or fail. Format switching after seeing the answer is noise, not boundary signal.

## Prompt Rules

Good prompts are specific, falsifiable, and grounded in visible content.

Use:

- specific references
- spatial relations
- negation
- ordinal references
- attributes such as color, material, orientation, state
- stacked constraints when visible

Avoid:

- open-ended prompts
- ambiguous targets
- objects not in the image
- NSFW, PII, copyrighted content
- identifiable people unless clearly public figures in public context

Aim for hard images plus sharp prompts. The best submissions often feel like the model has about a 50-70 percent chance of getting the image/prompt pair right.

## Verdict Rules

Pick fail / "I win" when the model has:

- wrong object
- missed object
- hallucinated object
- loose box
- wrong point
- wrong count
- malformed format

Pick pass / "AI wins" when:

- boxes are tight enough
- points are on the correct object
- count is right
- no missed or hallucinated items
- format is valid

If genuinely 50/50, treat it as a fail and correct what the model should have done.

On a correct answer, the trace may still be edited if it cites wrong landmarks or reasoning while landing on the right output.

On pass / "AI wins", answer confidence is N/A. Rate trace confidence only. On fail / "I win", rate answer confidence for the corrected answer or for the wrong-answer judgment if no canvas edit was needed.

## Hard Gates

- Do not score an ambiguous prompt. Rewrite it first.
- If the prompt asks for an absent target and the human answer would be "there is no such thing", discard or rewrite. Do not count an absent-object prompt as a model failure.
- Discard rounds where the prompt asks for something not visible or where the trace mostly asks "what does this mean?"
- Do not pass loose boxes. About 5 percent slack around the visible silhouette is the tolerance.
- Do not pass a counting answer with missing or extra instances.
- Do not change output mode after seeing the model response.
- Do not use prompts about things not visible in the image.
- Do not over-tag. Tags should describe the real failure and challenge pattern.
- Use the magnifier for tiny objects such as icons, badges, fine print, and small targets.
- Ignore badges, streaks, session stats, and unlock toasts when judging task quality. They are informational and should not drive prompt choice or verdicts.
- If the platform says to watch a full video, do so only when the task actually provides video media. For ordinary Find the Boundary image tasks, inspect the provided image carefully.

## Comment Style

The Model Output Review and Corrections fields are read by an auditor deciding whether your break is real, so they need to be specific.

**The Persona: someone pointing at the box and saying why it is wrong.**

1. **Name the landmark.** "The box cuts off at the handle instead of the spout," not "boundary imprecision."
2. **Say how far off.** "About a third of the lid sits outside the box" beats "the box is loose."
3. **For trace edits, quote what the model claimed.** Then say what is actually there.
4. **Short sentences. Periods.** No em dashes, no semicolons, no colons in prose.
5. **Avoid absolutes.** Not "perfectly tight." Use "tight," "flush," "within a few pixels."

**Banned phrases:** "boundary imprecision," "localization failure," "demonstrates," "exhibits," "Upon review of," "spatially inconsistent."

Good

`The box covers the mug but stops at the rim, so the handle on the right is left outside it. The trace says it found the handle first, which does not match where the box landed.`

Good

`There is no second bicycle in this image. The model counted a reflection in the shop window as a separate bike.`

Bad

`The model exhibits localization failure with respect to the target object's spatial boundaries.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answer in a clean markdown format directly in the chat using the exact template below.

```markdown
### Prompt Check
[Is the prompt specific, falsifiable, and grounded in visible content? If not, discard or rewrite instead of scoring it.]

### Model Output Review
[Check the model's boxes, points, or count against the image target by target. Note the thinking trace if it cites wrong landmarks.]

### Verdict
[pass / "AI wins" | break / "I win" | discard or rewrite]

### Corrections
[Corrected boxes, points, or counts. Include trace edits when the reasoning is wrong in a specific, citable way. Write "none needed" on a clean pass.]

### Tags
- Failure Type: [tag(s), or N/A on a pass]
- Challenge Strategy: [tag(s)]
- Image Type: [tag(s)]

### Confidence
- Trace confidence: [1-5]
- Answer confidence: [1-5 on a break, or N/A on pass / "AI wins"]
```

## Final Checklist

- Prompt is grounded and not ambiguous.
- Output mode matches the task.
- All boxes/points/counts checked carefully.
- Loose boxes over about 5 percent slack were treated as failures.
- Tags describe what happened, not every possible detail.
- Confidence is honest.
