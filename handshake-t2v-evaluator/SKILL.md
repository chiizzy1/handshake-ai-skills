---
name: handshake-t2v-evaluator
description: Evaluate Handshake Text-to-Video and Less AI Generated Benchmark tasks. Use when Codex must compare generated videos from a text prompt, decide which video looks less AI-generated, detect temporal AI artifacts, count artifact categories, check prompt/audio adherence, scrub frames, or write concise timestamped artifact rationales.
---

# Handshake T2V Evaluator

## Core Rule

Use the current task UI and `HANDSHAKE-AI/T2V/instructions.md` as the source of truth when no task-specific PDF exists.

Before grading, read `references/rubric.md`.

## Goal

Judge which generated video looks less AI-generated, then analyze the more AI-generated video for clear artifact categories.

Do not judge from a single frame. AI video artifacts often live between frames.

## Required Workflow

1. Read the full text prompt and every visible rating question.
2. Watch each response at normal speed with audio.
3. Note suspect moments where motion, identity, physics, contact, text, or detail stability feels wrong.
4. Scrub or sample frames around those moments.
5. Compare the two videos on prompt adherence, temporal realism, spatial artifacts, and audio.
6. Select the response that looks less AI-generated.
7. For the worse response, count only artifact categories that are clearly visible.
8. Write brief artifact notes with artifact type plus what happened and when.

## Seven Artifact Types

- Flicker and shimmer: surfaces, textures, hair, fabric, scan lines, lighting, or background details rewrite between frames without a physical cause.
- Morphing and deformation: shapes, faces, hands, limbs, props, table edges, gravestones, or architecture bend or change form over time.
- Object persistence failures: balls, paddles, limbs, props, crows, gravestones, gates, or other objects vanish, reappear, duplicate, or teleport without an exit path or occlusion.
- Physics violations: gravity, momentum, bounce paths, collisions, slips, falls, impacts, or flashlight movement violate real-world or prompt-style physics.
- Identity drift: a person, character, clothing, face, body shape, hood, or environment gradually changes identity or design across the clip.
- Interaction inconsistency: bodies or objects overlap without contact response; paddles miss balls but hits occur; hands pass through props; feet slide with no friction; flashlight beam does not interact with surfaces.
- Text and detail distortion: text, numbers, labels, signs, UI, scan-line details, repeated background patterns, or fine details garble or change across frames.

## Prompt And Style Rules

- A stylized prompt does not need photorealism. It still needs temporal consistency within that style.
- For retro/game/low-poly prompts, judge whether a skilled human could have made it in that style.
- Do not penalize intended style features, such as lo-res polygons or static scan lines, unless they become inconsistent or break the requested style.
- Do not confuse compression artifacts with AI artifacts. Blocky encoding or color banding alone is not an AI artifact.

## Audio Checks

If audio is part of the prompt, inspect it separately from visuals.

Check:

- whether expected sounds are present;
- whether hits, bounces, steps, crowd reactions, caws, ambience, or effects are synchronized;
- whether audio contradicts visible action;
- whether audio is generic, missing, or overlaid without matching events.

Audio can affect which response is less AI-generated, but artifact-category counts should follow the task wording. If the artifact list is visual-only, mention audio separately in the preference justification rather than forcing it into a visual artifact category.

## Rating Guidance

Prefer the video that:

- follows the prompt more completely;
- has fewer visible AI artifacts;
- preserves subject/object identity over time;
- has plausible physics and interactions;
- keeps relevant details stable;
- uses audio that matches the requested scene.

Use a strong preference when one video is clearly more coherent or the other has multiple obvious artifact classes. Use slight preference when both are flawed but one is modestly cleaner.

## Artifact Count Guidance

Count categories, not individual moments.

Example: if a ball vanishes three times, that is one category: Object persistence failure.

Only count a category when there is clear evidence. Do not pad the count to make the answer sound more complete.

If the options are limited to 3, 4, 5, or 6 and you detect more than 6 categories, choose 6.

## Output Style

Keep platform justifications brief and direct:

`Response A looks less AI-generated because the players, ball, and paddle contacts remain more coherent. In B, the ball disappears around 0:02, the black-shirt player slides unnaturally, and the paddle hits do not match the audio.`

Artifact notes should be concise:

`Object persistence: around 0:02, the ball vanishes between paddle contacts and reappears near the table with no visible trajectory.`

Avoid vague notes like `the motion is weird`.



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

