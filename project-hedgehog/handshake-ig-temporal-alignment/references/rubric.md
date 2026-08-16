# Handshake Sync a Video Pair Rubric

The operative rubric for IG Temporal Alignment. Read this before working a live pair.

## Contents

- [Source](#source)
- [The Task In Four Steps](#the-task-in-four-steps)
- [The Four Review Checks](#the-four-review-checks)
- [Watermarks And Text](#watermarks-and-text)
- [The Four Categories](#the-four-categories)
- [Reaction vs Recreation](#reaction-vs-recreation)
- [Behind-The-Scenes And Audio Recreation](#behind-the-scenes-and-audio-recreation)
- [How To Align](#how-to-align)
- [Good vs Bad Alignments](#good-vs-bad-alignments)
- [Trimming And Cropping](#trimming-and-cropping)
- [Transformation Must Be Present](#transformation-must-be-present)
- [Hard Rules](#hard-rules)
- [Grading Rubric 1-5](#grading-rubric-1-5)
- [Common Errors](#common-errors)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Final Checklist](#final-checklist)

## Source

No official PDF exists for this task. The highest local authority is:

- `HANDSHAKE-AI/hedgehog-extracted/docs/03_ig_temporal_alignment.md`
- `HANDSHAKE-AI/hedgehog-extracted/docs/04_task_simulation.md`

The task simulation screen recording is at `HANDSHAKE-AI/hedgehog-extracted/videos/examples/04_task_simulation__task_simulation_play_both.mp4`. Worked reaction and recreation example clips are under `HANDSHAKE-AI/hedgehog-extracted/videos/ig_reels/`.

## The Task In Four Steps

1. **Review the pair.** Run the four checks: connection, matching segment, engagement, video check.
2. **Keep or reject.** Only move on to alignment if the pair genuinely passes.
3. **Align the segments.** Anchor both clips to the same starting moment, then trim each clip's end once it drifts past the shared moment.
4. **Score against the rubric.** Self-check the sync before submitting.

Review before you align. A bad pair does not get better with alignment.

## The Four Review Checks

**Connection and Matching segment are make-or-break.** If either fails, reject immediately. Engagement and Video check shape the quality rating for pairs you keep.

### 1. Connection

Does the response correspond to this specific original — not just the same person, style, or topic? It must clearly be about this exact clip: reacting to this moment, showing how it was made, recreating this performance, or performing its song or speech.

### 2. Matching segment

Is there a shared moment you can anchor both clips to? The anchor can be visual (an action or beat) or audio (a word or lyric). No shared moment means it cannot be aligned — reject.

### 3. Engagement

Is the response worth watching? Clever, funny, entertaining — any of these count.

### 4. Video check

Confirm neither clip is AI-generated. If either clip appears AI-generated, reject the pair regardless of how well it otherwise connects.

## Watermarks And Text

**Crop before you reject.** Most watermark and text problems are fixable with a crop. Only what you cannot crop away should pull the rating down.

- **Third-party logo or watermark that can be cropped out of frame entirely** — a moving TikTok logo with username, a tiled Shutterstock or Getty overlay. Crop it out and continue the task as usual.
- **A logo or watermark that cannot be cropped out** — rate the pair below 3.
- **Other text, captions, @handles** — crop out anything on the edges or in the background that does not affect the important part of the video, where possible. Captions or @handles that cannot be cropped out are fine as long as they do not cover the important part of the scene.
- **Text over the main action** — text covering the most important aspects of the video, which cannot be cropped without losing that content, is not usable data. Rate below 3.
- A creator's own @handle or an in-scene brand is always fine.

## The Four Categories

The category tells you what kind of connection the pair has, and each one changes what "aligned" means.

A pair only belongs in a category if it meets **all** of that category's requirements. If a pair does not fully satisfy any single category, is not a clean example of that relationship, or is just the same video twice, rate it Below expectations or Unacceptable rather than forcing it into a category.

Use **Other** only for a genuinely good pair whose relationship does not fit any of the four.

## Reaction vs Recreation

The key question: is the output doing the same thing, or responding to it?

### Reaction

The output responds to the original — someone watching, commenting on, or reacting to it.

**Valid:** commentary or react videos, duets or stitches reacting to the clip, watch-and-respond posts.

**Do not submit:** a reaction that is not tied to this exact video, or a generic reaction that could be to anything. A clip where the person barely reacts — passive watching, no real response. Two unrelated videos that just happen to share a topic.

**Alignment rule:** the reaction should be reacting to or watching the same exact content seen in the first video throughout. It must not drift to a different moment.

### Recreation

The output performs the same content — same dance, same words, same choreography. Both clips should cover the same content start to finish.

**Valid:** dance covers, performance recreations and scene reenactments, parodies that follow the original's structure, step-by-step copies of actions.

**Do not submit:** two videos that just happen to do the same common move, dance, or trend without one clearly recreating the other. A clip where only the audio is redone with no visual recreation — that is an audio match. A "recreation" that only lines up through post-production editing rather than matching actions.

**End-alignment rule:** if it is a dance, both should be attempting the same moves throughout. If it is a skit or parody, both should start and end with the exact same words.

### The distinction

A reaction is *about* the original — you watch someone respond to it. A recreation *is* the original done again — the same performance, start to finish. If the output is doing the thing, it is recreation. If it is responding to the thing, it is reaction.

## Behind-The-Scenes And Audio Recreation

### Behind-the-scenes

The output shows how the original was made. Align to the same scene from the production side.

- **Perspective 1 (input)** — the person(s) or setting in the scene from the camera's POV. The final product.
- **Perspective 2 (output)** — the same person(s) or setting *while actively making* that scene, from a different perspective, with cameras, lighting, crew, and props visible.

**Valid:** making-of footage of that shot being filmed, a behind-the-camera angle, the set or camera setup, a before/after of that exact shot.

**Do not submit:** behind-the-scenes of a different scene than the finished clip, even from the same creator or shoot. The same video twice with no real finished-versus-process difference. The input video visible within the output — crop so only the BTS is submitted. A prompt that does not simulate a user adding the input video to a model. Two clips that just share a topic or creator. A clip of the actor getting ready, even in the same look or outfit, that is not BTS of filming this exact clip. A transformation that is just editing on top of the same video.

For the full BTS standard, see `../../handshake-ig-bts/references/rubric.md`.

### Audio recreation

The output covers the same song or speech — a cover, remix, or duet. Both clips must show a person actually performing the audio, not just ambient sound. The result audio must be a **new version**, not the same recording reused. The audio must contain lyrics or spoken words, not just sounds.

**Do not submit:** a clip that reuses the exact same sound or recording. A clip that recreates the visuals but not the audio. Two clips that just share a topic. Clips without a person performing the spoken audio. Any clip with third-party watermarks or logos that cannot be cropped out. Clips with text over the performer's face or other important parts.

**End-alignment rule:** both clips should start and end at the exact same point in the audio — the same lyric, word, or point in the song.

For the full audio standard, see `../../handshake-ig-audio-recreation/references/rubric.md`.

## How To Align

1. **Anchor both clips to the same starting moment.** Set both segments to begin on the exact same beat of the shared action. This is the part that has to be tight.
2. **Do not worry if the clips drift apart after the start.** A person recreating a dance will not keep perfect pace. What matters is that both clips keep showing the same event all the way through.
3. **Trim each clip's end once it moves past the shared moment.** Pull the end in as soon as it stops showing the shared content. The two clips need not be the same length, but a tail that no longer matches should be cut.
4. **When the picture is loose, use the sound.** Sync using the audio blend slider on a clear shared sound — a beat, a word, a clap. No echo on Play both means you are aligned.

## Good vs Bad Alignments

### Are both videos playing in sync?

- **Good** — both segments start on the same moment of the shared action. The first frame of Clip A and Clip B show the same moment, so the shared event lands together on Play both.
- **Bad** — Clip A appears about a second early in Clip B, so the two play out of sync and are no longer about the same segment.

### Same event the whole time, no wandering

- **Good** — both clips keep showing the same action across the full segment. Timing drifts slightly after the start, but it is the same event start to finish. Drift is fine; wandering onto a different action is not.
- **Bad** — the shared segment shows multiple scenes, some of which are not the same one. Both clips may be from the same show and a similar sequence without representing the same segment at all.

### Audio sync when the picture is loose

- **Good** — a recreation with different people and framing, synced on the shared soundtrack. The beat lands together in both, no echo on Play both.
- **Bad** — the audio is doubled or echoing when both play. When the pair shares a soundtrack, the sound must match. Re-anchor on the beat using the audio blend.

## Trimming And Cropping

Only trim to capture one scene at a time. Only allow through videos that are not poorly cropped and do not contain the input within the output at all.

Good submissions do not contain more than one individual scene, and are not cropped in a way that shows the input within the output.

## Transformation Must Be Present

Never allow the same video submitted twice for input and output. These are an automatic **1**. Videos must show a transformation between input and output.

Each task simulates a user handing a model an input video and asking for a transformation. The model does not generate the second clip — the second video must be a genuinely different, provided clip. A submission whose input and output are frame-for-frame identical, with only a caption added over a copy, is Unacceptable no matter how well it lines up.

A prompt that is gibberish, missing, or does not describe the relationship also fails, however good the clips are.

## Hard Rules

- **Length limits.** Each clip at least 5 seconds — the tool will not accept less. Both clips combined at most 16 seconds. Both must stay on the same event for the whole kept segment.
- **When to skip.** Skip is not for bad pairs — reject those in Step 1. Skip only when a clip will not load, or when you kept the pair but genuinely cannot carve a clean 5-second window where both clips stay on the shared moment. Do not skip because it is rough: if you can sync it by audio, sync it and submit.

## Grading Rubric 1-5

For reviewers and auditors: grade accepted pairs on the final clips and prompt only. The annotator's own QA rating of the pair does not affect this score. A correct reject earns full marks, with no alignment expected.

- **5 Exceptional** — perfect sync, no perceptible offset at the start, holds across the whole segment, same event throughout, accurate and specific prompt. **Or:** correctly rejected a genuinely bad pair.
- **4 Strong** — one minor flaw. Start anchored well under ~0.25s, slight drift only. Prompt accurate and clear, if not fully detailed.
- **3 Acceptable** — about 0.25s of desync (a faint echo on shared-sound pairs) and/or an adequate but thin prompt. The pair is genuinely valid and the same event; still usable.
- **2 Weak** — send back. Alignment clearly off (0.5-0.75s, obvious echo or visible lag) and/or an inaccurate prompt. **Or:** rejected a pair that could have been aligned.
- **1 Unacceptable** — unusable. No real attempt, or kept and aligned an unrelated pair. Also covers a missing or false prompt, and wrongly skipping a clearly syncable pair.

## Common Errors

Frequent reasons submissions get flagged, across all pair types. Check every pair against all four.

1. **Horizontal video orientation** — either clip is shot or exported in landscape instead of vertical. Only source vertical (portrait) IG clips. Horizontal videos must be rejected.
2. **One clip shows more than the other** — one clip includes content, action, or context the other never shows, so the two are not scoped to the same shared moment. Confirm both clips show the same event before aligning; if one contains material the other does not, reject.
3. **Animated or non-real footage** — either clip is animated, CGI, or otherwise not real filmed footage. Only submit real live-action video.
4. **Clip starts or ends mid-lyric** — trimmed so it begins or cuts off in the middle of a lyric or spoken line. Trim so both clips start and end on a clean lyric or word boundary.

## Knowledge Check Answers

- **Input and output frame-for-frame identical, with a caption added over a copy** → 1 (Unacceptable). No real transformation between input and output.
- **Response clip looks AI-generated — warped hands, inconsistent background — but connection and matching segment are strong** → reject the pair. AI-generated clips are not allowed no matter how well it otherwise connects.
- **Small Shutterstock watermark in the corner that can easily be cropped out without losing the shared moment** → crop it out and continue the task as usual.
- **Actor putting on the same outfit and doing makeup before a scene, with no camera, crew, or set shown** → not a valid behind-the-scenes pair. It is not BTS of filming this exact clip.
- **A creator doing the exact same dance as a viral original, same moves start to finish** → recreation, not reaction.
- **A recreation with different dancers and framing so poses cannot match, but both clips play the same song** → sync using the shared soundtrack via audio blend or a shared beat.

## Final Checklist

- Connection and matching segment reviewed before aligning.
- The start of both clips is anchored to the same moment.
- Both clips show the same event across the full kept segment.
- Play both pressed — no echo or double-hit.
- Each clip is at least 5 seconds; combined at most 16 seconds.
- The prompt accurately describes the transformation.
