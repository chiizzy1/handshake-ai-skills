# Handshake IG Editing Convo Rubric

The operative rubric for IG Editing Convo. Read this before building a live pair.

## Contents

- [Source](#source)
- [Task Shape](#task-shape)
- [Hard Rules](#hard-rules)
- [Relationship Types](#relationship-types)
- [Trimming Calibration](#trimming-calibration)
- [Writing The User Prompt](#writing-the-user-prompt)
- [Audio Conditioning](#audio-conditioning)
- [Client Feedback](#client-feedback)
- [Worked Examples](#worked-examples)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Submit Checklist](#submit-checklist)

## Source

No official PDF exists for this task. The highest local authority is `HANDSHAKE-AI/hedgehog-extracted/docs/02_ig_editing_convo.md`.

Worked example Reels are under `HANDSHAKE-AI/hedgehog-extracted/videos/ig_reels/`, prefixed `02_ig_editing_convo__`. Cropping-failure screenshots are in `HANDSHAKE-AI/hedgehog-extracted/images/`.

## Task Shape

You find two real Instagram Reels that form a conversation and present them as:

- a **user turn** — the input video plus a written prompt;
- an **assistant turn** — the response video.

You are a scout, not a creator. Nothing is filmed, edited, or AI-generated. The only changes you make are trimming inside the task UI.

## Hard Rules

- Both URLs must be Instagram Reels — no YouTube, TikTok, or Shorts.
- No creating, editing, or AI-generating any content.
- Exactly one video per side.
- Each clip at least **5 seconds**; the two clips combined at most **16 seconds**.
- Trim each clip to the most relevant moment — strip intros, outros, and anything off-topic.
- Never crop or source the output from the input.

## Relationship Types

The five types below are **examples to guide you, not an exhaustive checklist.** Anything where the second video is a real, intentional response to the first counts.

| Type | What it is | Example |
|---|---|---|
| Reaction | Creator B watches Creator A's video and posts their genuine reaction | Chef reacts to a viral cooking hack |
| Continuation | Same or related creator posts a follow-up that directly builds on the input | Part 1 of an experiment, then a Part 2 update |
| Cover / Duet | Creator B performs the same song, dance, or routine from the original | Dance cover using the same audio |
| Behind-the-Scenes | Response shows the making-of or backstory for the input | BTS of a viral stunt or challenge |
| Parody / Spoof | Creator B directly parodies or spoofs the specific content | Parody of a viral dance or life hack |

**Good:** a viewer who watches the first and then the second feels the second is a direct reply — a reaction, a continuation (a true Part 2), a cover or duet, a parody or spoof, or a behind-the-scenes reveal.

**Bad:** same genre is not enough. Two cooking Reels that both feature pasta do not form a pair.

### Type calibration

- A cooking creator reacting in real time to a viral kitchen-fire-fail video, gasping and narrating what went wrong → **Reaction**.
- A fitness creator posting a "Day 30 update" following up on their own viral "Day 1" transformation → **Continuation**.
- A guitarist posting an acoustic cover of a song that went viral in someone else's dance Reel, using the same track → **Cover / Duet**.
- A stunt team posting footage of the rigging and camera setup for the exact car-flip stunt in a blockbuster trailer Reel → **Behind-the-Scenes**.
- A comedian exaggerating a viral "quiet luxury" fashion-haul Reel with thrifted rags and the same dramatic narration → **Parody / Spoof**.
- A museum recreating a viral "day in my life" Reel's exact pacing and captions to advertise a new exhibit → **fits none of the five cleanly, and still counts.** It is a real, intentional reply.

### Behind-the-scenes, specifically

BTS means the same scene from behind the camera. A separate Reel of the lead actor in a makeup chair before filming does not qualify as BTS of a car-flip stunt scene, even though both are from the same production and the makeup clip comes first chronologically. You need footage of the stunt being filmed — camera setup, crew, rigging.

There is no separate "production BTS" category that relaxes this.

## Trimming Calibration

The input must cover the same moment the response is reacting to.

| Situation | Call |
|---|---|
| Input is a full 45-second cooking demo submitted whole, paired with a 6-second reaction to the finished dish | **Not trimmed correctly** — cut the input to the moment being reacted to, not the full source clip |
| A 20-second stunt Reel trimmed to the exact 6-second jump the response reacts to | **Trimmed correctly** — the input covers the same window the response replies to |
| Fellow cannot pin down the reacted-to moment, so trims the input to the first 5 seconds to satisfy the minimum | **Not trimmed correctly** — trimming to hit a length minimum is not trimming to the reacted-to moment |
| Response reacts to a high note at 0:12 of a 30-second clip; input trimmed to 0:08-0:15 | **Trimmed correctly** — it isolates the beat being reacted to, with a little buffer |
| Fellow cannot find a real second Reel, so cuts a separate 6-second clip from later in the same source video and submits it as the "response" | **Not valid** — this is not a trimming issue. Cropping the output from the input is never allowed regardless of trim length |

A 52-second travel vlog might trim down to a 7-second beat at 0:28-0:35 that contains the line being reacted to.

## Writing The User Prompt

At least **20 words**. It should describe the response video — not just the input — and explain the connection between the two clips. Reference specific details: a timestamp, an on-screen overlay, the creator's name, or a line of dialogue.

**Good**

- "Find a video reacting to Karl's flying house at 0:04, where another creator pretends they're about to be flown past."
- "Find a home-cook attempt at the plating technique demonstrated in the input chef's video, same dish, lower-skill execution."

**Bad**

- "Find a reaction." — too vague, gives the model nothing to ground in.
- "A kid tries to make a fancy plated dish in their home kitchen." — describes only the response, not the relationship between the two clips.

The second bad example fails on relationship, not word count. Padding it to 20 words without naming what the response is replying to does not fix it.

## Audio Conditioning

When the pair is built around audio, the focus is on **temporal timing and match** — not on which clip has the better audio. Do not pick a pair just because one side's singing or sound is notably worse than the other; that judgment is not what the task is teaching the model.

- The strongest pairs use **different audio** on each side.
- An easy, reliable pick is the same song performed in two different audios — two distinct recordings or performances, each with its own video.
- Do not pick two Reels that share the same audio sound bite.
- What matters is that the two clips line up in time and the response clearly tracks the input.

## Client Feedback

Five things the reviewer flagged, verbatim in substance:

1. **Temporal alignment — trim input and output to the same window.** The input video must cover the same moment the response is reacting to, not just be the source clip cropped to length. Do not crop or source the output from the input video.
2. **Minimum 5 seconds per video.** Do not trim submissions below 5 seconds — input or output.
3. **Try not to submit dance recreations.** Dancing imitations are a last resort, not a default. Find recreations with more specific content.
4. **Behind-the-scenes means the same scene, behind the camera.** Makeup, set arrival, or unrelated prep clips do not qualify.
5. **Prompts must describe the difference between input and output** — not just describe what happens in the output. The prompt is the bridge that explains why the pair is a conversation.

## Worked Examples

**Example 1 — Reaction pair.** Aaron Rodgers' retirement announcement paired with a tribute edit that commentates on the moment. The second Reel replies directly to the first: same moment.

**Example 2 — Recreation of a viral template.** The "very demure, very mindful" original paired with Swinburne University of Technology's recreation as an introductory video. The response borrows the exact format and phrasing but redirects it to a brand intro — a clear, deliberate reply to a viral template. It does not fit any single listed type cleanly, and it still counts.

**A complete example.** A job-search influencer explains salary advice and lists what not to say during recruiting. DanFromHR, an HR professional, stitches his reply directly onto her clip and walks through why the advice is wrong. The reply is unmistakable: same claims, same on-screen text cues, rebutted point by point. That is the bar — not "two videos about recruiting," but one creator responding to another.

## Knowledge Check Answers

- **A full 30-second chef Reel submitted as input with an 8-second reaction to the plating moment** → the input must be trimmed to the same window the response is reacting to, roughly the plate-finish moment. The combined-runtime rule is not what fails here.
- **Swinburne recreating "very demure" as a brand intro** → it does not cleanly fit any single listed type, but it still counts because it is a real, intentional reply.
- **A movie's car-flip stunt scene paired with the lead actor in a makeup chair, tagged behind-the-scenes** → not valid. BTS means the same scene from behind the camera; the Fellow needs footage of the stunt being filmed, not unrelated makeup prep.
- **"A kid tries to make a fancy plated dish in their home kitchen"** → it only describes the response, not the relationship. A correct prompt names what the response is reacting to.
- **Two street performers singing the same song, different recordings, one more polished** → valid, and judged on how well the two clips line up in time, not on whose performance sounds better.

## Submit Checklist

All five must be true:

1. Both links are Instagram Reels — no YouTube, TikTok, or Shorts.
2. Each clip is at least 5 seconds, and the two clips combined are at most 16 seconds.
3. The response actually replies to the input — it does not just sit in the same genre.
4. The prompt is at least 20 words and specific to the response video.
5. If the pair is audio-based, the two sides use different audio — not the same sound bite.
