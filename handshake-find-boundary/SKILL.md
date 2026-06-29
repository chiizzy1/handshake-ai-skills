---
name: handshake-find-boundary
description: Handle Handshake Find the Boundary image-grounding tasks. Use when Codex must write or judge prompts for bounding box, point, or counting outputs; decide whether the model passed or failed; correct boxes, points, counts, traces, tags, or confidence; or identify hard image/prompt boundary cases.
---

# Handshake Find Boundary

## Core Rule

Use `HANDSHAKE-AI/pdfs/handshake-Find the Boundary.pdf` as the source of truth.

Before doing a live task, read `references/rubric.md`.

## Goal

Find the model's capability boundary, not easy wins. A good submission tests an image/prompt pair the model has a real chance of getting right or wrong.

## Output Modes

- Bounding box: draw a tight box around described object(s).
- Point: place one point on the described object.
- Counting: count matching objects and return one point per instance.

Do not switch formats mid-task to force a pass or fail.

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

## Hard Gates

- Do not score an ambiguous prompt. Rewrite it first.
- Do not pass loose boxes. About 5 percent slack around the visible silhouette is the tolerance.
- Do not pass a counting answer with missing or extra instances.
- Do not change output mode after seeing the model response.
- Do not use prompts about things not visible in the image.
- Do not over-tag. Tags should describe the real failure and challenge pattern.

## Final Checklist

- Prompt is grounded and not ambiguous.
- Output mode matches the task.
- All boxes/points/counts checked carefully.
- Loose boxes over about 5 percent slack were treated as failures.
- Tags describe what happened, not every possible detail.
- Confidence is honest.
