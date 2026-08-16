---
name: handshake-ig-temporal-alignment
description: Work Handshake Sync a Video Pair (IG Temporal Alignment) items. Use when asked to quality-check an already-sourced pair of Instagram videos, keep or reject it, pick the relationship category, and align both clips so the shared moment lands at the same time. Covers the four review checks and the 1-5 alignment rubric.
---

# Handshake IG Temporal Alignment (Sync a Video Pair)

Someone has already found two related Instagram clips. Your job is to confirm the pair is genuinely good, then line the clips up so the shared moment happens at the same time in both.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. `HANDSHAKE-AI/hedgehog-extracted/docs/03_ig_temporal_alignment.md` — the task guideline page.
2. `HANDSHAKE-AI/hedgehog-extracted/docs/04_task_simulation.md` — the practice run of the real tasking UI.
3. The current task UI and the visible pair in front of you.
4. `references/rubric.md`, then `../shared-references/ig-video-pairs.md`.
5. `HANDSHAKE-AI/guidelines.md` as a broad summary only.
6. User memory or prior answers.

Say plainly when an expected source cannot be found. Do not import TELUS or Outlier rules into Handshake work.

## Inspecting The Media

Do not judge a Reel you have not actually looked at. Fetch and inspect it first:

```bash
python3 handshake-ai-skills/tools/inspect_media.py --url <reel-url> --out /tmp/insp
```

This finds every scene, saves a keyframe per scene, builds a contact sheet, and
transcribes the audio with timestamps. Read the scene list and the contact sheet
before answering anything about the clip as a whole. Run it on both clips: the transcript timestamps give you the shared anchor word and let you measure the offset rather than eyeball it.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Core Rule

**Order matters. Review before you align.** A bad pair does not get better with alignment. If you are not sure the pair is good, reject — do not align.

Before working a live pair, read `references/rubric.md`. For the rules this task shares with the other IG Video Pairs tasks, read `../shared-references/ig-video-pairs.md`.

## Hard Gates

- Do not align before running the four review checks.
- Do not keep a pair that fails Connection or Matching segment. Those two are make-or-break.
- Do not keep a pair where either clip appears AI-generated. Reject it however well it otherwise connects.
- Do not reject over a watermark you could have cropped out. Crop first.
- Do not pass the same video twice as a pair. That is an automatic 1.
- Do not force a pair into a category it does not fully satisfy.
- Do not use Skip in place of Reject. Skip is for a clip that will not load or a kept pair you genuinely cannot carve a clean window from.
- Do not keep a pair to be agreeable. Keeping a pair that should have been rejected counts against your score.

## Step 1 — Review

Work these four checks in order. **Connection and Matching segment are make-or-break — if either fails, reject immediately.** Engagement and Video check shape the quality rating for pairs you keep.

1. **Connection** — does the response correspond to this specific original, not just the same person, style, or topic? It must clearly be about this exact clip: reacting to this moment, showing how it was made, recreating this performance, or performing its song or speech.
2. **Matching segment** — is there a shared moment you can anchor both clips to? The anchor can be visual (an action or beat) or audio (a word or lyric). No shared moment means it cannot be aligned. Reject.
3. **Engagement** — is the response worth watching? Clever, funny, entertaining — any of these count.
4. **Video check** — confirm neither clip is AI-generated. Handle third-party logos and watermarks by cropping first: if the watermark can be cropped out of frame without hurting the video, crop it and continue. Only reject or rate below 3 when it cannot be cropped out. A creator's own @handle or an in-scene brand is always fine.

### Fix What You Can

If the category label is wrong or the prompt is weak, correct them. Do not reject a good pair over something fixable. You cannot change the clips themselves.

### Keep Or Reject

- **Keep** → move on to alignment.
- **Reject** → you are done with this pair.

## The Four Categories

Every pair falls into one of four relationship types, and each one changes what "aligned" means. A pair only belongs in a category if it meets **all** of that category's requirements.

- **Reaction** — the output responds to the original. Align so the output is reacting to the same moment visible in Clip A, and does not drift to a different one.
- **Recreation** — the output performs the same content. Both clips cover the same content start to finish. For a dance, both attempt the same moves throughout; for a skit or parody, both start and end on the exact same words.
- **Behind-the-scenes** — the output shows how the original was made. Align to the same scene from the production side.
- **Audio recreation** — the output covers the same song or speech as a new performance. Both clips start and end at the exact same point in the audio.

Use **Other** only for a genuinely good pair whose relationship fits none of the four. If a pair does not fully satisfy any category, is not a clean example, or is the same video twice, rate it Below expectations or Unacceptable rather than forcing a fit.

Reaction and recreation cause the most confusion. A reaction is *about* the original; a recreation *is* the original done again. If the output is doing the thing, it is recreation. If it is responding to the thing, it is reaction.

## Step 2 — Align

1. **Anchor both clips to the same starting moment.** Set both segments to begin on the exact same beat of the shared action. This is the part that has to be tight — take your time.
2. **Do not worry about drift after the start.** A person recreating a dance will not keep perfect pace, and that is expected. What matters is that both clips keep showing the same event throughout.
3. **Trim each clip's end once it moves past the shared moment.** Pull the end in as soon as it stops showing the shared content. The clips need not be the same length, but a tail that no longer matches should be cut.
4. **When the picture is loose, use the sound.** Different framing, different people, a recreation that does not go move-for-move — sync using the audio blend slider on a clear shared sound: a beat, a word, a clap. No echo on Play both means you are aligned.

### Length Limits

Each clip must be at least 5 seconds — the tool will not accept less. Both clips combined must be at most 16 seconds. Both must stay on the same event for the whole kept segment.

### When To Skip

Skip is not for bad pairs — reject those in Step 1. Skip only when a clip will not load, or when you kept the pair but genuinely cannot carve a clean 5-second window where both clips stay on the shared moment. Do not skip because it is rough: if you can sync it by audio, sync it and submit.

## Alignment Controls

- **Drag the strip / edges** — drag the strip to slide a segment while keeping its length; drag the edges to change its length.
- **‹ › nudge** — moves the start one frame at a time for fine alignment.
- **Play both / , / .** — play both clips together, or step one frame back and forward.
- **Overlay (o)** — stacks Clip B over Clip A with an opacity slider. Best for matching motion frame by frame.
- **Audio blend (A↔B)** — mixes the two soundtracks so you can hear them sync.
- **Speed (0.25× / 0.5× / 1×)** — slow down to place the start precisely.
- **Skip (s) / Reset (r)** — skip per the rules above; reset to start the alignment over.

## Rating Scale

Full tier language is in `references/rubric.md`.

- **5 Exceptional** — perfect sync, no perceptible offset at the start, holds across the segment, same event throughout, accurate and specific prompt. **Or** a correct reject of a genuinely bad pair, which earns full marks with no alignment expected.
- **4 Strong** — one minor flaw. Start anchored well under ~0.25s, slight drift only.
- **3 Acceptable** — about 0.25s of desync, a faint echo on shared-sound pairs, and/or a thin but adequate prompt.
- **2 Weak** — send back. Alignment clearly off at 0.5-0.75s with obvious echo or visible lag, and/or an inaccurate prompt. **Or** rejected a pair that could have been aligned.
- **1 Unacceptable** — no real attempt, or kept and aligned an unrelated pair. Also a missing or false prompt, and wrongly skipping a clearly syncable pair.

For reviewers and auditors: grade accepted pairs on the final clips and prompt only. The annotator's own QA rating of the pair does not affect the score.

## Feedback Quality

When this task asks for written feedback, read `../shared-references/reviewer-feedback.md`. A correct score with vague feedback is still a weak review.

## Comment Style

For written feedback on a pair, follow the three-part pattern in `../shared-references/reviewer-feedback.md`. This section covers wording.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Give the offset as a number and a direction. "About a second early in the response" beats "out of sync."
- Name the shared moment. The beat, the word, the clap, the action.
- On a reject, name which of the four checks failed. Connection and matching segment are the make-or-break two, so say which.
- Say what good would have looked like, in one concrete sentence.

Banned: "looks off", "good job", "bad pair", "needs work", "the alignment is incorrect", "poor quality submission".

- Good: `The shared beat lands at 0:04 in the response and 0:05 in the original, so they do not hit together on playback.`
- Good: `No shared moment to anchor. The two clips cover different parts of the routine, so this one could not be aligned.`
- Bad: `Alignment is off, score 2.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the review in the chat using this template.

```markdown
### Step 1 — Review
- Connection: [Pass / Fail — what makes it this exact clip, or what is missing]
- Matching segment: [Pass / Fail — the anchor, visual or audio, at ~M:SS]
- Engagement: [Pass / Weak — one line]
- Video check: [Clean / Cropped a watermark / AI-generated — what you saw]
- Category: [Reaction / Recreation / Behind-the-scenes / Audio recreation / Other — why it meets all of that category's requirements]

### Decision
[Keep / Reject, with the check that decided it.]

### Step 2 — Alignment
- Anchor: [the shared beat both clips start on]
- Clip A segment: [start-end, and why the end was trimmed there]
- Clip B segment: [start-end, and why the end was trimmed there]
- Sync method: [visual match / audio blend on a named shared sound]
- Play both: [no echo / residual offset and its size]

### Rating
[1-5 with the tier language that drove it.]

### Feedback
[Three-part pattern: what worked, what missed and where, what good would look like.]
```

## Final Checklist

- Connection and matching segment reviewed before any alignment.
- The start of both clips is anchored to the same moment.
- Both clips show the same event across the full kept segment.
- Play both pressed — no echo or double-hit.
- Each clip is at least 5 seconds; combined at most 16 seconds.
- The prompt accurately describes the transformation.
