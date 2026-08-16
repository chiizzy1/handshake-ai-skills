---
name: handshake-ig-bts
description: Build Handshake IG BTS pairs. Use when asked to pair a finished Instagram clip with real behind-the-scenes footage of that exact shot being filmed, crop a split-screen source down to the BTS half, write the transformation prompt, and self-score against the 1-5 BTS rubric.
---

# Handshake IG BTS

Pair a finished clip with the making-of **that exact shot**. The second clip shows how the first was made: the same shot or scene, a behind-the-camera angle, or the set and camera setup.

For each pair you pick a source video (the finished clip), find a result video showing how it was made, and write a short prompt describing the behind-the-scenes view.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. `HANDSHAKE-AI/hedgehog-extracted/docs/06_ig_bts.md` — the task guideline page.
2. The current task UI and the visible item in front of you.
3. `references/rubric.md`, then `../shared-references/ig-video-pairs.md`.
4. `HANDSHAKE-AI/guidelines.md` as a broad summary only.
5. User memory or prior answers.

Say plainly when an expected source cannot be found. Do not import TELUS or Outlier rules into Handshake work.

## Inspecting The Media

Do not judge a Reel you have not actually looked at. Fetch and inspect it first:

```bash
python3 handshake-ai-skills/tools/inspect_media.py --url <reel-url> --out /tmp/insp
```

This finds every scene, saves a keyframe per scene, builds a contact sheet, and
transcribes the audio with timestamps. Read the scene list and the contact sheet
before answering anything about the clip as a whole. Run it on both clips: the scene list proves the output stays on one scene, and the audio track is what the prompt's sameness-or-difference note has to describe.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Core Rule

**The result must show the making of this exact finished video.** You should recognise the same shot or scene twice: once finished, once being made.

Behind-the-scenes of a different clip from the same creator or shoot does not count. If it is not clearly the making of this clip, it is not a valid pair.

This task measures scene matching, not video quality. If the output is only *related* to the input, the model learns the wrong lesson.

Before building a live pair, read `references/rubric.md`.

## The Quick Test

Before you submit, ask two questions:

1. Can you point at something in the output that proves the input shot was being filmed?
2. Is everything in the output part of that one shot?

If either answer is no, the pair is **not valid**.

## Perspective Framing

The link is not the audio. Both videos should focus on the same person or content of the scene, from different perspectives.

- **Perspective 1 — input.** The person(s) or setting in the scene, from the POV of a camera. This is the final product.
- **Perspective 2 — output.** The same person(s) or setting *while actively making that scene*. We want to see cameras, lighting, or crew moving objects and props.

Usable output types: making-of footage of that shot being filmed, a behind-the-camera angle of that shot, the set or camera setup for that shot, a before/after of that exact shot.

## "Related" Is Not "The Exact Same Moment"

This is the single biggest reason pairs get rejected. The BTS clip shows the same subject, same set, or a similar action — but not the literal moment captured in the finished clip.

None of these qualify:

- Same dancer, different take.
- Same kitchen, different dish.
- Same movie, different scene.

The BTS footage must show the crew, camera, or rig actively capturing **this** exact shot, not a nearby one.

## Hard Gates

- Do not submit the same video for both sides. A BTS clip with no camera, crew, or rig visible and no real finished-versus-process difference is an **automatic 1**, not a low score. Repeated instances put your task access at risk.
- Do not leave the finished shot visible in the output. When cropping a split screen, remove it completely — even a brief replay before cutting to the crew invalidates the pair.
- Do not put multiple scenes in one submission. Every camera cut counts as a new scene.
- Do not submit a horizontal clip on either side. It cannot be cropped or padded into a vertical frame.
- Do not submit animated, CGI, or AI-generated footage.
- Do not submit actor prep footage — getting ready, makeup, arriving on set — even in the same look or outfit.
- Do not submit generic set footage. Real crew and cameras are not enough if none of it shows the exact scene being made. That is a missing transformation and should be rejected, not down-rated.
- Do not pull more than 3 pairs from the same source video.

## The Six Common Errors

Check every pair against all six before submitting.

1. **Same video for both input and output** — no real finished-versus-being-made difference. The output must show visible BTS evidence: a camera, crew, lighting, rig, or set.
2. **Split-screen source, cropped badly** — the crop leaves both halves visible, so the finished shot is still showing. Use Add Crop to isolate only the BTS half.
3. **Multiple scenes in one submission** — the output cuts between several moments. Keep each submission to one scene; split multiple BTS moments into up to 3 separate pairs.
4. **Horizontal video orientation** — source or result exported in landscape. Only source vertical (portrait) IG clips.
5. **Output shows more or less than the input** — extra takes, unrelated cutaways, or action the input never shows. Trim to only the BTS of the exact shot.
6. **Animated or non-real footage** — either clip is animated, CGI, or otherwise not real filmed footage.

## Cropping A Single Source Into A Pair

You may crop one Instagram video to extract both input and output. If you do, you must:

- **Keep the output pure BTS.** Remove the finished shot from the output completely.
- **Capture the exact actions.** A camera crew, a director, or the same actors in a different movie is not enough. The same scene must be visible occurring in both.
- **Include only the BTS scene in the output.** Do not include the final product.
- **Describe audio in the prompt.** Always describe audio differences or sameness, for every task in this project, even when not cropping. With cropped videos the audio is identical on both sides — you must still say so.
- **Check resolution.** At least 720px after cropping.
- **Submit at most 3 pairs from the same video.** Choose the best 3 scenes and use 3 separate submissions. Never combine scenes into one.

## Hard Requirements

- **Length** — at least 5 seconds per clip after trimming, at most 16 seconds total.
- **One video** — the final assistant turn contains exactly one video.
- **Same shot** — the result shows the making of this source, not a generic or different-scene clip.
- **Clarity** — both clips clear enough to recognise the shared shot. No unusable, fully obscured clips.
- **No third-party watermarks** — a creator's @handle or a brand shown in the scene is fine. A moving TikTok or YouTube logo with username, a tiled Shutterstock/Getty/Alamy/iStock overlay, another app's export mark, or text over an important part such as actors' faces is not. Crop caption or username text where you can without hurting quality; if you cannot, usernames are acceptable.
- **Prompt** — at least 20 words describing the behind-the-scenes relationship, simulating a user asking a model to produce the output from the input, covering what changed and what stayed the same.

## Building A Pair

1. **Add the source.** Add the finished clip on the user bubble. Paste the link or search Instagram, pick the carousel slide if needed, trim, and optionally crop.
2. **Write the prompt.** At least 20 words, describing the behind-the-scenes view and how it relates to the finished video: what is being filmed, the angle or setup shown, and audio sameness or difference.
3. **Add the result.** Add the BTS clip on the final assistant bubble. Paste, trim, crop, confirm.
4. **Line them up.** Trim both clips with the frame-by-frame nudge arrows and the draggable trim range. Use Add Crop for spatial cropping. Use Play Both from Start to preview that the same shot lines up, finished versus being made. Resolve flags and submit.

One pair that genuinely shows how the source was made is worth ten generic pairs.

## Rating Scale

Full tier language is in `references/rubric.md`.

- **5 Exceptional** — clearly shows how this exact finished video was made; same shot or scene, recognisable finished versus being made. High quality and informative. Shots line up temporally. Prompt fully describes the relationship.
- **4 Strong** — a genuine BTS of this finished clip, good quality, shots line up. Prompt describes it but may be slightly vague.
- **3 Acceptable** — a valid BTS of the source, but unremarkable or only loosely informative. The prompt connects them but is vague.
- **2 Weak** — quality problems, a different scene from the same creator or shoot, no real finished-versus-process difference, a prompt that misses it, or under 5s of lined-up overlap.
- **1 Unacceptable** — unrelated or disjointed, not actually BTS of this clip, a standalone clip or duplicate, or a missing/illogical prompt.

## Feedback Quality

When reviewing another Fellow's pair, read `../shared-references/reviewer-feedback.md`.

## Prompt Style

The prompt has to describe the behind-the-scenes relationship, covering what changed and what stayed the same.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Write as a user asking a model for a change, not as an annotator describing a pair. No "this pair shows", no "the reference video", no "the output clip".
- Name concrete visible detail. Wardrobe, position, setting, layout, timestamps, handles.
- Call out split-screen or picture-in-picture when the output uses it.
- At least 20 words, and every one of them doing work. Padding to reach the count is visible.

Banned: "a related video", "a transformed version", "similar content", "some changes", "in this video we can see".

- Describe audio sameness or difference. This is required on every submission, including cropped pairs where the audio is identical on both sides. Say that it is identical.
- Name the filming evidence. The tripod, the lighting stand, the crew member, the green screen.

- Good: `Create behind-the-scenes footage showing how this dance reel was filmed. Use a wider view of the room with all four women in matching black outfits practicing the routine. A phone mounted on a tripod is clearly visible at the front, recording the dance. The audio is the same track in both clips.`
- Bad: `Generate a behind the scenes video of this clip.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the pair in the chat using this template.

```markdown
### Source (input — finished clip)
[Link or description, trimmed window, the specific action or beat it shows.]

### Result (output — behind the scenes)
[Link or description, trimmed window, and the visible BTS evidence: camera, crew, lighting, rig, or set.]

### The Exact-Scene Test
[Point at the specific action, line, or beat in the finished clip and name where the output shows that same action being captured.]

### Crop
[Whether a split-screen source was cropped, and confirmation that no part of the finished shot remains in the output. Resolution after crop.]

### Prompt
[20+ words describing the BTS relationship, what changed, what stayed the same, and audio sameness or difference.]

### Six-Error Check
- Same video twice: [pass/fail]
- Split-screen crop clean: [pass/fail/not applicable]
- One scene only: [pass/fail]
- Both clips vertical: [pass/fail]
- Output scoped to the input's shot: [pass/fail]
- Real filmed footage: [pass/fail]

### Self-Score
[1-5 with the tier language that drove it.]
```

## Final Checklist

- Matched the exact scene — not just a similar setup, movie, or creator.
- Input video is not included inside the output.
- Audio sameness or difference is described in the prompt.
- Resolution checked — at least 720px after any crop.
- Prompt is 20+ words and simulates a real model request.
- Watermark check done — no third-party logos or overlays.
- Length limits respected — 5s+ per clip, 16s total max, exactly one video in the final turn.
- No more than 3 submissions pulled from the same source video.
