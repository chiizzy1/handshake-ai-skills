---
name: gaffer-video-annotator
description: Write and self-audit Project Gaffer video captions for Handshake AI. Use for Video Omni Caption tasks in SuperAnnotate that need four captions across two tracks — Speech Transcription, Speech Characteristics, Visual, and Audio — with timestamps, speaker tags, skip/flag decisions, and submit routing.
---

# Gaffer Video Annotator

## What This Task Is

You watch a short video and describe it so completely that someone who never saw
it could almost re-create it. You are not rating anything. You are writing the
captions yourself, and a human auditor grades them afterwards.

Every video gets **four captions** on **two separate tracks**:

| Track | Caption | What goes in it |
|---|---|---|
| Speech | Caption 1 · Transcription | Every spoken word, verbatim, with speaker tags |
| Speech | Caption 2 · Speech characteristics | How the speech *sounds* — tone, volume, pace, accent, emphasis |
| Visual+Audio | Caption 1 · Visual | Everything you see — people, actions, camera cuts, on-screen text |
| Visual+Audio | Caption 2 · Audio | Every sound that is **not** speech — ambience, music, effects |

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is the cross-project shared folder in this repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace
  root (for example `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use this skill's `references/`
  files as the operative guidance and say plainly that the source file was
  unavailable.

## Core Rule

The Project Gaffer training site is the source of truth. It is extracted to:

- `HANDSHAKE-AI/project-gaffer/extracted/PROJECT_GAFFER_MASTER_DOC.md` — the
  guides, all ten common-error audits, and all nine golden examples.
- `HANDSHAKE-AI/project-gaffer-assessment/questions.md` — the assessment, which
  is the rubric in question form.
- `HANDSHAKE-AI/project-gaffer/extracted/MASTER_VIDEO_SPEECH_INSPECTION_REPORT.md`
  — keyframes and rough Whisper transcripts for the eighteen example videos.

There is no Gaffer PDF. Do not go looking for one and do not invent one. If the
live task UI and this skill disagree, the task UI wins for that task, and you
say so in your answer.

Do not be agreeable for its own sake. Be cooperative with the user, but be loyal
to the Gaffer rubric.

## Hard Gates

- **Do not write anything you did not see or hear.** No inference, no
  background knowledge, no filling gaps with what "must" be there. A woman on
  screen is "a woman", not "the network's chief anchor". An accent is "a German
  accent", never "the speaker is German".
- **Do not skip a hard video.** Skipping for the wrong reason gets people
  offboarded. Read `references/skip-flag-routing.md` before any skip.
- **Do not submit with Autochecker errors.** Submitting a task that has not
  passed with zero errors means being unable to complete future tasks.
- **The Autochecker cannot tell whether what you wrote is true.** It only checks
  format and coverage. Passing it is not passing the audit.
- **Do not leave a gap.** Every second of the video must be covered on both
  tracks. Silence is covered by `((No speech present))`, not by nothing.
- **Do not describe events outside the segment's own window.** If the segment is
  `[43.0-54.6]`, nothing in it may be stamped `[55.0]`.
- **Do not put a track's content in the other track.** A laugh is audio. A
  stutter is speech. See the routing table in `references/visual-audio-track.md`.
- **Never edit the user's task files.** Task files are read-only input. Put your
  captions in the chat reply using the output format at the bottom of this file.

## Workflow

Work in this order. Do not start writing captions until step 4.

### 1. Identify what you are holding

Check the task tag:

- Tag has **`Mini`** in the name (`Mini_Annotator`) → this is the **1-minute
  qualifying task**. Annotate only the first 60 seconds, no matter how long the
  video is. The Autochecker will let you submit after that.
- Tag is **`Precheck`** → this is a **full annotator task**. Annotate the whole
  video.
- `Mini_Completed` on a full task means the first part is already partly done by
  someone else. Do the whole task anyway. It is yours now.

Everyone except reviewers must do a 1-minute qualifying task before their first
full task.

### 2. Decide skip / flag / annotate

Before watching properly, check the skip criteria in
`references/skip-flag-routing.md`. Four things make a video a real skip: toxic
content or visible blood, unintelligible or mostly non-English audio, tracks
that are not equally rich in data, and length over 10 minutes.

Anything that only affects *part* of the video is not a skip. It gets the
**Partially Un-annotatable** flag and you annotate normally.

### 3. Inspect the video before you write a word

Run the inspector. Do not skip this and do not caption from memory of a single
viewing — every timestamp you write has to come from something you looked at.

```bash
~/.venvs/gaffer-tools/bin/python scripts/gaffer_inspect.py \
    "https://www.youtube.com/watch?v=VIDEO_ID" --out /tmp/gaffer
```

Plain `python3` works too if `--check-deps` passes on it. Setup for the dedicated
environment is in `references/video-inspection.md`.

It takes a YouTube URL, a video ID, or a local path, and produces the cut times,
a frame for every shot, isolated audio, a draft transcript, the no-speech
windows, and the loud non-speech moments. Read `INSPECTION.md` before anything
else. Full details, including what the tool cannot do, are in
`references/video-inspection.md`.

Then go through the material yourself:

- **Pass 1 — listen** to `audio.wav` against the draft transcript. Who speaks, in
  what order, and when. Number the speakers by the order they first speak.
  Speaker 1 is whoever speaks first, and stays Speaker 1 for the entire video.
  The tool does not identify speakers; you do.
- **Pass 2 — look** at every frame in shot order, and at every frame in the
  possible-transitions table. Read the on-screen text off the frames yourself and
  note exactly when it appears and changes. The tool does not do OCR.

If the inspector cannot run at all, say so plainly in your answer, and fall back
to `ffprobe`/`ffmpeg` by hand:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4
ffmpeg -i video.mp4 -vf fps=1 frames/frame_%04d.jpg     # one frame per second
ffmpeg -i video.mp4 -vn -ar 16000 -ac 1 audio.wav       # audio track only
```

### 4. Segment each track separately

**The two tracks have their own independent segment boundaries.** They do not
line up, and they are not supposed to. In the cooking-show golden example the
Speech segments are `0.0-8.3`, `8.2-15.7`, `15.7-26.0`, `26.0-30.1` while the
Visual+Audio segments over the same 30 seconds are `0.0-2.1`, `2.1-4.4`,
`4.4-6.6`, `6.6-8.5`, `8.5-9.0`, `9.0-9.9`, and so on.

- **Speech segments** follow who is talking. A segment is normally one utterance
  or one continuous stretch by one speaker. Gaps where nobody talks get their own
  segment carrying `((No speech present))`.
- **Visual+Audio segments** follow the picture. A new shot, a new graphic, or a
  new scene is a new segment. In fast montages one segment can hold many stamped
  events instead.

Segments run edge to edge with no gaps and no overlaps.

### 5. Write the four captions

Read the track reference before writing, every time:

- `references/speech-track.md` — transcription and speech characteristics,
  with the tag rules and worked samples.
- `references/visual-audio-track.md` — visual and audio, with the detail
  checklist, the on-screen text rules, and the track routing table.

### 6. Self-audit before you submit

Run the whole checklist in `references/self-audit.md`. It is built from the ten
things auditors actually fail people for. Do not skip it and do not claim you
ran it if you did not.

### 7. Route the task

`references/skip-flag-routing.md` has the routing table. Short version: full
annotators send to **Submit_to_QC**; the 1-minute qualifying task always goes to
**Annotator_Skip**, which is how it is submitted, not a skip.

## How To Write

This is the part people get wrong in both directions.

**Write plainly.** Short, flat sentences. Ordinary words. Subject, verb, fact.
Write the way the golden examples write:

> The frame is a medium shot containing two women. The camera slowly zooms in on
> the frame.
>
> The camera cuts to a low replay shot from ground level beside the pitch.

Not this:

> The composition establishes a carefully balanced two-shot, wherein the
> subjects are situated within a domestically-coded interior that evokes warmth.

**But do not be brief.** Plain style is about word choice, not length. The
coverage has to be exhaustive. Common error #1 in this project is *insufficient
detail*, and the assessment explicitly marks a dense, 150-word caption full of
stock tickers as a **PASS** — with "the level of detail is more than is needed"
listed as a wrong answer.

So: simple words, simple sentences, and you list everything that is there. A
caption is long because the frame is busy, never because the writing is fancy.

**Do not editorialise.** No "beautifully lit", no "the tension builds", no
"clearly frustrated". Say what is on screen and let it speak.

## What the Inspector Will Not Do for You

It finds cuts, silence and loud moments. It does not caption anything, and four
jobs stay entirely yours:

- **Reading on-screen text.** There is no OCR. You read every banner, ticker and
  watermark yourself, exactly as shown, typos included. Read it in the task player
  when you have one — the extracted frames are for timing and for detail you
  cannot pause on. If a character is still unclear at full resolution, write that
  it is illegible. That is the correct answer, not a cop-out.
- **Identifying speakers.** Whisper returns text, not who said it. Merging two
  people into one turn is a graded error.
- **Hearing sounds underneath speech.** The loudness scan cannot separate a
  whistle from the commentator talking over it. That is precisely the failure in
  common error #5.
- **Finding boundaries with no visual change.** On continuous action the camera
  follows play with no discontinuity to detect. Measured on the rugby golden
  example, two real segment boundaries appear in no table at all. The interval
  frames exist for exactly this.

**Whisper output is a draft, never the transcript.** In the tennis example it
renders the same commentary line six times and turns a player's name into
"Boatek Van the San Shul". Use it to find where speech is, then listen and write
what you actually hear. A misheard word is a real audit failure: one worker
wrote "a pure wit gun" for "a pure witch hunt" and the whole task failed.

The eighteen training videos are already inspected, in
`HANDSHAKE-AI/project-gaffer/extracted/MASTER_VIDEO_SPEECH_INSPECTION_REPORT.md`.

## References

Read the one that matches what you are doing.

| When | Read |
|---|---|
| Before you write anything — inspecting the video | `references/video-inspection.md` |
| Writing transcription or speech characteristics | `references/speech-track.md` |
| Writing visual or audio | `references/visual-audio-track.md` |
| Before submitting anything | `references/self-audit.md` |
| Deciding skip, flag, or where to send | `references/skip-flag-routing.md` |
| You want to see a full pass-grade task | `references/golden-examples.md` |
| You want to see what failure looks like | `references/common-errors.md` |

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Put the
captions in the chat reply, in this shape, so they can be pasted into
SuperAnnotate one annotation at a time.

```markdown
### Task Type
[Mini qualifying task (first 60s only) | Full annotation]

### Flag Decision
[None | Partially Un-annotatable — reason | SKIP: Toxic Content / Un-annotatable — reason]

### Speech Track

**Segment 1 · [0.0 - 8.3]**
Caption 1 · Transcription:
[0.0 - 8.3] [Speaker 1]: ...

Caption 2 · Speech characteristics:
[0.0 - 8.3] Speaker 1 speaks ...

**Segment 2 · [8.3 - 15.7]**
...

### Visual+Audio Track

**Segment 1 · [0.0 - 2.1]**
Caption 1 · Visual:
[0.0 - 2.1] ...

Caption 2 · Audio:
[0.0 - 2.1] ...

**Segment 2 · [2.1 - 4.4]**
...

### Self-Audit
[One line per check in references/self-audit.md, each marked pass or fixed.
Name what you actually verified. If you could not verify something — no audio,
unreadable text, no local file — say so instead of claiming the check.]

### Routing
Send to: [Submit_to_QC | Annotator_Skip]
Flags: [None | ...]
```

## Final Checklist

- [ ] I identified Mini vs full before writing anything.
- [ ] I checked the skip criteria before annotating.
- [ ] I ran `scripts/gaffer_inspect.py` and read `INSPECTION.md`, including the
      skipped-stages section.
- [ ] I looked at every shot frame and every possible-transition frame.
- [ ] I listened to `audio.wav` myself rather than trusting the draft transcript.
- [ ] Speaker numbers follow first-speaking order and never change.
- [ ] Both tracks cover every second, with no gaps and no overlaps.
- [ ] Every timestamp inside a caption falls inside that caption's own window.
- [ ] Every piece of on-screen text is quoted exactly as shown, typos included.
- [ ] Nothing is inferred. Everything written is something I saw or heard.
- [ ] Non-speech sounds are in the Audio caption, not the Speech captions.
- [ ] I ran the full self-audit in `references/self-audit.md`.
