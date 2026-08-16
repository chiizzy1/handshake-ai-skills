---
name: handshake-ig-audio-recreation
description: Build Handshake IG Audio Recreation pairs. Use when asked to source two real Instagram videos where the output genuinely redoes the input's audio — the same song or speech, same segment, performed again rather than reused — then align the segment, write the transformation description, and self-grade 1-5.
---

# Handshake IG Audio Recreation

This is about redoing what you **hear**, not what you see. You discover pairs of real, already-existing Instagram videos where the output is a genuine new performance of the input's specific audio.

You are a scout, not a creator. You never film, edit, or AI-generate anything.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. `HANDSHAKE-AI/hedgehog-extracted/docs/05_ig_audio_recreation.md` — the task guideline page.
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
before answering anything about the clip as a whole. Run it on both clips and compare the transcripts — this task is decided on audio, and the guideline is explicit that you cannot judge the match from a description.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Core Rule

The connection lives in the **sound**, not the picture. Ask one question: does the second clip genuinely redo the first clip's audio?

**You cannot judge this from text.** A written description of a pair can read like a legitimate cover and still be graded bad once you listen. Never grade a song or segment match from a description. Always play both clips.

Before building a live pair, read `references/rubric.md`.

## The Three Rules

### Rule 1 — A new performance, not the same recording

The output must be a genuinely new performance of the source audio: a cover, remix, or live take. It cannot be the identical recording reused.

Lip-syncing plays back the same recording. The audio was never performed again, so it fails — no matter how perfectly the sound matches.

### Rule 2 — This song, not a different one

The output must redo the specific source's song or speech, not a different one, even when the two clips look similar. Two tender acoustic covers with the same mood are not a pair if they are different songs. Shared genre is not enough.

### Rule 3 — Same segment, pacing can differ

The output must cover the same segment or lines as the source. Pacing and tempo can vary — a slower, stripped-back acoustic take of the same bridge is fine — but it cannot be a different part of the song.

## Hard Gates

- Do not accept a clip that reuses the exact same sound or recording as the original.
- Do not accept a clip that recreates the visuals or performance but not the audio. That is a visual recreation, not an audio match.
- Do not accept two clips that merely share a topic.
- Do not accept a clip carrying a third-party watermark or logo — TikTok, YouTube, Shutterstock, Getty, or CapCut. A creator's own @handle, or an in-scene brand naturally part of what was filmed, is fine.
- Do not judge the song or segment match from a text description. Play both clips.
- Do not source the output from a hashtag grab.
- Do not let a good-sounding prompt carry a submission whose audio was not genuinely redone.

## How To Find A Pair

Three methods reliably lead to a genuine redo. One only looks like it does.

- **Search the song or speech by title** — surfaces other genuine covers and live performances, which you confirm by listening.
- **Check the comments and stitches on the original** — creators often reply with their own redo, so the matching output is frequently sitting right under the source.
- **Tap the audio name on the original** — links straight to every clip built on that exact sound. The tightest way to confirm an audio match.
- **Grab any clip from the song's hashtag** — **fails.** A hashtag is only loosely topical and never guarantees the clip redoes this source's specific audio, even when the caption names the song title.

## The Build, In Four Steps

1. **Source the input.** Pick a real Instagram clip with recognisable audio.
2. **Find a genuine redo of that exact audio.** A cover, remix, or live take of the same song or speech.
3. **Align both clips to the same segment.** Sync timing so they match — roughly the same 8-second window.
4. **Write the transformation description.** Call out concrete visual details: where the performer sits, mic position, wardrobe, layout.

## Writing The Transformation Description

Every description must:

- be at least **20 words**;
- describe the output's layout, calling out split-screen or picture-in-picture if used;
- describe the output's timing and content;
- explain how the output relates to the input.

**Too vague — works, but scores no higher than 3:** "Generate a related video featuring another performer singing a transformed version of the same song with a similar melody and emotional tone but a different vocal performance."

**Strong — a graded 4-star example:** "Generate @ROBBYKEY playing this song. He should be wearing a white shirt and black trouser and sits on a brown stool playing a piano. There should be a ring on his right ring finger and a watch on his left hand. There should be a long table over a patterned rug surrounded with chairs at his left side."

Concrete, specific visual detail is what separates an acceptable prompt from a strong one. Name the performer, the wardrobe, the setting, the layout, and the timing.

## Rating Scale

Self-calibrate every pair before submitting. Full tier language is in `references/rubric.md`.

- **5 Exceptional** — clearly redoes this exact clip's audio, high quality, audio lines up, prompt fully describes the audio change.
- **4 Strong** — a genuine new version, good quality, audio lines up; prompt describes it but may be slightly vague.
- **3 Acceptable** — works, but the prompt needs more detail.
- **2 Weak** — same audio in both clips. Not a transformation, even when the written description sounds like one.
- **1 Invalid** — the same video submitted twice.

## Prompt Style

The transformation description is what separates a 3 from a 4 on an otherwise valid pair. Concrete visual detail is the whole difference.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Write as a user asking a model for a change, not as an annotator describing a pair. No "this pair shows", no "the reference video", no "the output clip".
- Name concrete visible detail. Wardrobe, position, setting, layout, timestamps, handles.
- Call out split-screen or picture-in-picture when the output uses it.
- At least 20 words, and every one of them doing work. Padding to reach the count is visible.

Banned: "a related video", "a transformed version", "similar content", "some changes", "in this video we can see".

- Describe the audio change explicitly. Who performs it and how the performance differs.

- Good: `Generate @ROBBYKEY playing this song. He should be wearing a white shirt and black trouser and sits on a brown stool playing a piano. There should be a ring on his right ring finger and a watch on his left hand.`
- Bad: `Generate a related video featuring another performer singing a transformed version of the same song with a similar melody and emotional tone but a different vocal performance.`

The bad example is not too short. It is 26 words and still scores 3, because none of them name anything you could point at.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the pair in the chat using this template.

```markdown
### Input
[Link or description. The song or speech, and the segment covered.]

### Output
[Link or description. Who performs it, and how the performance differs.]

### Rule 1 — New performance
[What makes this a genuine redo rather than the same recording. Say explicitly that you played both clips.]

### Rule 2 — Same song
[The song or speech, confirmed by listening, not by caption or hashtag.]

### Rule 3 — Same segment
[The lines or section both clips cover, and the ~8-second aligned window.]

### Watermark Check
[Clean, or the disqualifying mark and where it sits.]

### Transformation Description
[20+ words: layout, timing, content, and the relationship to the input.]

### Self-Grade
[1-5 with the tier language that drove it.]
```

## Final Checklist

- Input and output are both real, already-existing Instagram posts — discovery only, nothing filmed, edited, or AI-generated.
- The output is a genuinely new performance of the input's specific audio, not the same recording reused.
- Same song and same segment as the input — not a different part or a different song.
- No third-party watermarks in either clip (TikTok, YouTube, Shutterstock, Getty, CapCut).
- The transformation description is at least 20 words and names concrete visual, layout, and timing detail.
- The pair was self-graded against the QA rubric before submitting.
