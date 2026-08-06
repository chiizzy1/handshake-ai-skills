---
name: handshake-t2v-evaluator
description: Evaluate Handshake Text-to-Video and Less AI Generated Benchmark tasks. Use when asked to compare generated videos from a text prompt, decide which video looks less AI-generated, detect temporal AI artifacts, count artifact categories, check prompt/audio adherence, scrub frames, or write concise timestamped artifact rationales.
---

# Handshake T2V Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

There is no T2V PDF in `HANDSHAKE-AI/pdfs/`. Use the current task UI as the source of truth, with `references/rubric.md` as the operative rubric. If a T2V instruction file later appears in the workspace, it outranks this skill.

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

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your answers and ratings in clean markdown directly in the chat using the template below.

```markdown
### Input Analysis
[What the prompt asks for: subjects, actions, setting, style, audio, ending state.]

### Response Analysis
[Analyze Response A: prompt adherence, temporal realism, spatial artifacts, audio.]
[Analyze Response B: prompt adherence, temporal realism, spatial artifacts, audio.]

### Final Ratings
- Less AI-generated: [Strongly prefer A | Slightly prefer A | Tie | Slightly prefer B | Strongly prefer B]
- Artifact categories in the more AI-generated video: [count, from the options the UI offers]
- Artifact notes:
  - [Category: what happened and when, e.g. `Object persistence: around 0:02, the ball vanishes between paddle contacts and reappears with no visible trajectory.`]

### Justification
[Brief, natural-language reason for the preference, naming concrete timestamped evidence.]
```

Use the exact rating labels shown by the task UI.

## Final Checklist

Before submitting:

- Full prompt read, and every visible rating question identified.
- Both videos watched at normal speed with audio, then scrubbed at suspect moments.
- Judgment made across time, not from a single frame.
- Intended style features not penalized; compression artifacts not counted as AI artifacts.
- Audio checked separately, and not forced into a visual artifact category.
- Preference strength matches the gap: strong for a clear difference, slight when both are flawed.
- Artifact categories counted once each, only when clearly visible, with no padding.
- Notes name artifact type plus what happened and when, with no vague wording.

