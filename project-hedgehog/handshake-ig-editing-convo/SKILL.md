---
name: handshake-ig-editing-convo
description: Build Handshake IG Editing Convo pairs. Use when asked to source two real Instagram Reels that form a conversation — an input Reel that asks something and a response Reel that directly replies — then trim both clips, write the user prompt, and run the submit checklist.
---

# Handshake IG Editing Convo

Find two real Instagram Reels that form a conversation: one video that "asks" something, and a second that directly replies to it. You present them as a user turn (the input video plus a written prompt) and an assistant turn (the response video).

You are a scout, not a creator. You do not film, edit, or generate anything.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. `HANDSHAKE-AI/hedgehog-extracted/docs/02_ig_editing_convo.md` — the task guideline page.
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
before answering anything about the clip as a whole. Run it on both clips: the transcripts confirm the response genuinely replies and locate the trim window around the line being reacted to.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Core Rule

**The connection between the two videos has to be unmistakable.** A viewer who watches the first and then the second should feel that the second is a direct reply.

Same genre is not enough. Two cooking Reels that both feature pasta do not form a pair. The second video must reply to the first.

Before building a live pair, read `references/rubric.md`.

## Hard Gates

- Do not use anything but Instagram Reels. No YouTube, TikTok, or Shorts.
- Do not create, edit, or AI-generate any content.
- Do not put more than one video on a side.
- Do not submit a clip under 5 seconds, or a pair whose two clips exceed 16 seconds combined.
- Do not crop or source the output from the input video. This is never allowed regardless of trim length.
- Do not trim just to satisfy the length minimum. The cut has to be anchored to what the response is actually replying to.
- Do not submit an audio-based pair where both sides use the same sound bite.
- Do not default to dance recreations. They are a last resort.
- Do not call unrelated prep footage behind-the-scenes.

## The Six Steps

1. **Find an input Reel.** Scout Instagram for a real Reel that "asks" something — a clip with a recognisable line, moment, or template another creator has responded to.
2. **Find a response Reel that replies to it.** The connection must be unmistakable: a reaction, continuation, cover or duet, parody, or behind-the-scenes of that exact scene.
3. **Trim both clips to the same window.** Cut each clip to the most relevant moment so the input covers the beat the response is reacting to. At least 5 seconds each, at most 16 combined.
4. **Write the user prompt.** At least 20 words. Describe the difference between input and output, not just what the output shows.
5. **Check audio conditioning.** If the pair is built around audio, the two sides must use different audio.
6. **Run the checklist and submit.**

## Relationship Types

These are **examples to guide you, not a checklist.** You are not limited to them. Anything where the second video is a real, intentional response to the first counts.

- **Reaction** — Creator B watches Creator A's video and posts their genuine reaction.
- **Continuation** — the same or a related creator posts a follow-up that directly builds on the input. A true Part 2.
- **Cover / Duet** — Creator B performs the same song, dance, or routine from the original.
- **Behind-the-Scenes** — the response shows the making-of or backstory for the input video.
- **Parody / Spoof** — Creator B directly parodies or spoofs the specific content of Creator A's video.

A pair that fits none of the five but is still a real, intentional reply is valid. A museum recreating a viral "day in my life" Reel's exact pacing and captions to advertise an exhibit counts, even though it is not cleanly a parody or a continuation.

**Behind-the-scenes means the same scene, behind the camera.** Makeup, set arrival, and unrelated prep clips do not qualify. The BTS clip has to be the production side of the exact scene in the output.

## Trimming

Trim each clip to the most relevant moment. Strip intros, outros, and anything off-topic. A 52-second travel vlog might trim down to a 7-second beat at 0:28-0:35 that contains the line being reacted to.

The input must cover the same moment the response is reacting to — not the full source clip, and not an arbitrary window that happens to clear 5 seconds. If a response reacts to a musician hitting a high note at 0:12 of a 30-second clip, trim the input to roughly 0:08-0:15, capturing the note with a little buffer on each side.

## Writing The User Prompt

The user-turn prompt is what makes the pair legible to the model. At least **20 words**. It should describe the response video, not just the input, and explain the connection between the two clips. Reference specific detail: a timestamp, an on-screen overlay, the creator's name, or a line of dialogue.

- **Good** — "Find a video reacting to Karl's flying house at 0:04, where another creator pretends they're about to be flown past."
- **Good** — "Find a home-cook attempt at the plating technique demonstrated in the input chef's video, same dish, lower-skill execution."
- **Bad** — "Find a reaction."
- **Bad** — "A kid tries to make a fancy plated dish in their home kitchen." This describes only the response, not the relationship.

## Audio Conditioning

When the pair is built around audio, the focus is **temporal timing and match** — not which clip has the better audio. Do not pick a pair because one side's singing is notably worse than the other; that is not what the task teaches.

The strongest pairs use different audio on each side. A reliable pick is the same song performed in two different audios — two distinct recordings or performances, each with its own video. Do not pick two Reels that share the same audio sound bite.

## Client Feedback

Five things the reviewer has flagged:

1. **Temporal alignment** — trim input and output to the same window. Do not crop or source the output from the input video.
2. **Minimum 5 seconds per video** — do not trim submissions below 5 seconds on either side.
3. **Try not to submit dance recreations** — dancing imitations are a last resort, not a default. Find recreations with more specific content.
4. **Behind-the-scenes means the same scene, behind the camera** — makeup, set arrival, and unrelated prep do not qualify.
5. **Prompts must describe the difference between input and output** — not just what happens in the output. The prompt is the bridge that explains why the pair is a conversation.

## Prompt Style

The user prompt is the bridge that explains why two clips are a conversation. It is graded on whether it names the relationship, not on length.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Write as a user asking a model for a change, not as an annotator describing a pair. No "this pair shows", no "the reference video", no "the output clip".
- Name concrete visible detail. Wardrobe, position, setting, layout, timestamps, handles.
- Call out split-screen or picture-in-picture when the output uses it.
- At least 20 words, and every one of them doing work. Padding to reach the count is visible.

Banned: "a related video", "a transformed version", "similar content", "some changes", "in this video we can see".

- Name the moment being replied to, with a timestamp where you can.

- Good: `Find a video reacting to Karl's flying house at 0:04, where another creator pretends they are about to be flown past.`
- Bad: `Find a reaction.`
- Bad: `A kid tries to make a fancy plated dish in their home kitchen.` This describes the response and never mentions the input.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the pair in the chat using this template.

```markdown
### Input Reel
[Link or description, the trimmed window, and what it "asks".]

### Response Reel
[Link or description, the trimmed window, and how it replies.]

### Relationship
[Reaction / Continuation / Cover-Duet / BTS / Parody / other real reply — and the specific thing that makes the connection unmistakable.]

### Trim Rationale
[Why each window was chosen. Name the beat the response is replying to and where it sits.]

### User Prompt
[20+ words describing the relationship, with a concrete anchor.]

### Audio
[Different audio on each side, or not audio-based. If audio-based, name both sources.]

### Checklist
- Both links are Instagram Reels: [yes/no]
- Each clip at least 5s, combined at most 16s: [actual lengths]
- The response actually replies rather than sharing a genre: [one line of evidence]
- Prompt is 20+ words and specific to the response: [word count]
- If audio-based, the two sides use different audio: [yes / not applicable]
```

## Final Checklist

- Both links are Instagram Reels — no YouTube, TikTok, or Shorts.
- Each clip is at least 5 seconds, and the two combined are at most 16 seconds.
- The response actually replies to the input — it does not just sit in the same genre.
- The prompt is at least 20 words and specific to the response video.
- If the pair is audio-based, the two sides use different audio — not the same sound bite.
