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



## How to See (Comprehensive Photographic Analysis)

Good image evaluation starts with consistent observation, not personal taste. Replace vague statements like "looks good" or "feels off" with specific, observable photographic claims. Rely on the following three comprehensive pillars to evaluate visual quality and detect generation failures.

### 1. Composition & Framing
Composition is how the elements of an image are arranged. It doesn't have to follow textbook rules perfectly, but it must look purposeful, not accidental.
- **Subject Placement & Rule of Thirds:** Photographers use a 3x3 grid to compose images. Placing a subject on an intersection of these grid lines creates tension and directs the eye naturally. Conversely, if a subject sits dead center with large, empty negative space on both sides, the framing often reads as an accidental AI generation rather than a purposeful composition.
- **Framing Scale:** Does the shot distance (wide, medium, close-up) match what the prompt asked for?
- **Visual Hierarchy:** What draws your eye first? Does it match the intended focus of the prompt?
- **Negative Space:** Is the area around the subject providing intentional "breathing room," or is it unresolved and distractingly empty?

### 2. Focus, Detail & Clarity
Blur is NOT inherently a flaw. Shallow depth of field (a blurred background with a sharp subject) is a legitimate, highly common photographic choice used to isolate a subject.
- **Natural Fall-off vs. AI Artifacts:** The question is whether the blur is intentional and consistent. Does the blur fall off smoothly and logically from the focal plane? In many AI-generated photos, the background is unnaturally sharp when it should be blurred, or it dissolves into soft blur in random, impossible patches with no optical logic.
- **Sharpness:** Is the intended subject actually in focus? Check the edges and fine details (e.g., hair strands, eyelashes, text).
- **Compression & Detail Loss:** Is fine detail (fabric weave, skin pores, grass blades) present where the image resolution should support it? Or is the image "mushy" in ways that look like a generation failure rather than an artistic choice?

### 3. Light & Color Consistency
Light is the most common source of physical inconsistency in AI-generated images.
- **Light Source Direction:** Do all shadows fall consistently from one primary source? Is the light hitting faces, objects, and the background from the exact same angle? (e.g., In "Rembrandt lighting," one side of the face is lit, the other falls into shadow, and everything in the scene must be consistent with that single source).
- **Softness vs. Harshness:** Harsh light (like direct sun) produces sharp, defined shadows. Diffused light (like overcast skies or studio softboxes) produces soft, blended shadow edges. Does the shadow quality logically match the apparent light source?
- **Contrast Check:** Are the highlights "blown out" (pure white with zero detail) or are the shadows "crushed" (pure black, destroying visual information)?
- **Color Temperature:** Is the overall image consistently warm (golden, amber) or cool (blue, gray)? Mixed, clashing color temperatures across a single scene are a massive red flag unless the specific lighting scenario explains it.
- **Saturation Consistency:** Is the color intensity consistent across the image, or do some regions look heavily over-processed while others fall flat?

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

