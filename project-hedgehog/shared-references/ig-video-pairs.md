# IG Video Pairs — Shared Rules

Common ground for the five Project Hedgehog IG Video Pairs tasks: IG Editing Convo, IG Audio Recreation, IG BTS, Sync a Video Pair (Temporal Alignment), and Temporal Alignment V2 Review.

Read this alongside the task-specific rubric. **Where a task's own rubric differs from this file, the task rubric wins** — the differences are real and deliberate, and the ones that matter are flagged below.

## Contents

- [Source Of Truth](#source-of-truth)
- [The Scout Rule](#the-scout-rule)
- [Hard Limits Every Task Shares](#hard-limits-every-task-shares)
- [Relationship Types](#relationship-types)
- [Reaction vs Recreation](#reaction-vs-recreation)
- [Watermarks And Text](#watermarks-and-text)
- [Same Video Twice](#same-video-twice)
- [Writing The Prompt](#writing-the-prompt)
- [Trimming And Cropping](#trimming-and-cropping)
- [Common Errors Across All Pair Types](#common-errors-across-all-pair-types)

## Source Of Truth

There is no official PDF for the IG Video Pairs family. The highest local authority is the extracted training material:

- `HANDSHAKE-AI/hedgehog-extracted/docs/` — the extracted guideline pages.
- `HANDSHAKE-AI/hedgehog - IG Videos/` — the saved source HTML those pages came from.

The live task UI outranks both when it contradicts them for the item in front of you.

## The Scout Rule

You are a scout, not a creator. Every clip is a real, already-existing Instagram post that you find. You never film, edit, or AI-generate content. Trimming and cropping inside the task UI are the only changes you make.

## Hard Limits Every Task Shares

- Both links must be Instagram Reels. No YouTube, TikTok, or Shorts.
- Exactly one video per side.
- Each clip is at least 5 seconds after trimming.
- Both clips combined are at most 16 seconds.
- Both clips are vertical (portrait). A horizontal clip is rejected outright — it cannot be cropped or padded into the vertical frame.
- Both clips are real live-action footage. Animated, CGI, and AI-generated clips are not accepted regardless of quality.
- Trim to a clean lyric or word boundary. Never start or end mid-word.

## Relationship Types

Four categories carry the sourcing and alignment work:

- **Reaction** — the output responds to the original. Commentary, react videos, duets, stitches, watch-and-respond posts.
- **Recreation** — the output performs the same content. Dance covers, scene reenactments, parodies that follow the original's structure, step-by-step copies.
- **Behind-the-scenes** — the output shows how the original was made. Making-of footage, a behind-the-camera angle, the set or camera setup, a before/after of that exact shot.
- **Audio recreation** — the output covers the same song or speech as a genuinely new performance. A person must be visibly performing, and the audio must carry lyrics or spoken words, not just sound.

A pair only belongs in a category if it meets **all** of that category's requirements. Do not force a near-miss into a category — rate it down instead. On Sync a Video Pair, "Other" exists only for a genuinely good pair whose relationship fits none of the four.

IG Editing Convo treats these types as examples rather than a closed list, and accepts continuation (a true Part 2) and parody as their own kinds. On that task a real, intentional reply that fits no listed type still counts.

## Reaction vs Recreation

This is the distinction that causes the most mislabelling.

A reaction is **about** the original — you watch someone respond to it. A recreation **is** the original done again — the same performance, start to finish.

If the output is doing the thing, it is recreation. If it is responding to the thing, it is reaction.

The category changes what "aligned" means:

- **Reaction** — the output should be reacting to or watching the same exact content throughout. It must not drift to a different moment.
- **Recreation** — both clips cover the same content start to finish. For a dance, both attempt the same moves throughout. For a skit or parody, both start and end on the exact same words.
- **Audio recreation** — both clips start and end at the exact same point in the audio: the same lyric, word, or point in the song.
- **Behind-the-scenes** — align to the same scene from the production side, finished shot against that shot being made.

Two clips that merely do the same common move, dance, or trend are not a recreation. Neither is a clip where only the audio was redone with no visual recreation, nor a "recreation" that only lines up through post-production editing.

## Watermarks And Text

**The policy is not the same across tasks. Check the task rubric before applying it.**

- **Sync a Video Pair / V2 Review** — crop before you reject. A third-party logo or watermark that can be cropped out of frame entirely gets cropped, and the task continues as usual. Only a watermark that cannot be cropped out pulls the rating below 3.
- **IG Audio Recreation** — reject any clip carrying a third-party watermark or logo (TikTok, YouTube, Shutterstock, Getty, CapCut). There is no crop-and-continue path.
- **IG BTS** — a moving TikTok or YouTube logo with username, a tiled Shutterstock/Getty/Alamy/iStock overlay, or another app's export mark is not acceptable. Crop caption or username text where you can without hurting quality.

Shared across all of them:

- A creator's own @handle or username is fine.
- A brand or logo that is naturally part of the filmed scene is fine.
- Text covering the most important part of the video, which cannot be cropped away without losing that content, is not usable data. Rate below 3.
- Captions and @handles that cannot be cropped out are acceptable as long as they do not cover the important part of the scene.

## Same Video Twice

Each task simulates a user handing a model an input video and asking for a transformation. The model does not generate the second clip — the second video must be a genuinely different, provided clip showing a real transformation.

A submission containing the same video twice as both input and output is an **automatic 1 (Unacceptable)**. This is not a low score, it is not accepted, and repeated instances put task access at risk. Adding a caption over a copy of the same video does not make it a transformation.

## Writing The Prompt

Every pair task requires a user-turn prompt of **at least 20 words** that simulates a real user handing the model the input video and describing the change they want.

- Describe the relationship between the two clips, not just what the output shows.
- Name concrete detail: a timestamp, an on-screen overlay, the creator's handle, a line of dialogue, wardrobe, layout, camera position.
- Call out split-screen or picture-in-picture layout when the output uses it.
- Describe audio sameness or difference. On IG BTS this is required for every submission, including cropped pairs where the audio is identical on both sides.

"Find a reaction" is too vague. "Find a video reacting to Karl's flying house at 0:04, where another creator pretends they're about to be flown past" gives the model something to ground in.

## Trimming And Cropping

- Trim each clip to the most relevant moment. Strip intros, outros, and anything off-topic.
- Trim to the moment the pair is actually about, not to satisfy the length minimum.
- One contained scene per submission. If the output cuts between several moments or locations, no single description can cover it.
- Never crop or source the output from the input video.
- When cropping a split-screen source, the output frame must contain only the response half. A sliver of the other clip left at the edge invalidates the crop.
- Resolution must be at least 720px after cropping.

## Common Errors Across All Pair Types

Check every pair against these before submitting or accepting:

1. **Horizontal orientation** — either clip is landscape. Reject and find another source.
2. **One clip shows more than the other** — one clip includes content, action, or context the other never shows. The two are not scoped to the same shared moment.
3. **Animated or non-real footage** — either clip is animation, CGI, or AI-generated.
4. **Clip starts or ends mid-lyric** — trimmed so it begins or cuts off in the middle of a spoken line.
5. **Same topic, no real relationship** — two clips that share a genre, creator, or subject without one genuinely responding to, recreating, or documenting the other.
6. **Scene hopping** — the output cuts between several scenes instead of staying on one.
