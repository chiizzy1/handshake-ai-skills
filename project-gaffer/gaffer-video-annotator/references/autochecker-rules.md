# The Autochecker — Mechanical Rules

Every rule here is checked by machine. **One flag sends the task back.** Fix
flags as they appear while you work rather than memorising this, then run the
full list before submitting.

> **When the Autochecker and the guidance disagree, the Autochecker wins.**
> The project states this outright: *"If the checker and this site ever disagree,
> trust the checker and flag it in Slack."* That puts it above the instruction
> site, above the golden examples, and above this skill.

## Contents

- [The Loop](#the-loop)
- [Structure and Coverage](#structure-and-coverage)
- [Timestamp Format](#timestamp-format)
- [Marker Spellings](#marker-spellings)
- [Speakers](#speakers)
- [Events Need Stamps](#events-need-stamps)
- [Detail Presence](#detail-presence)
- [Right Content, Right Track](#right-content-right-track)
- [The Two Keyword Traps](#the-two-keyword-traps)
- [What It Does Not Check](#what-it-does-not-check)
- [Getting Paid](#getting-paid)

## The Loop

1. **Save** in SuperAnnotate — top-right button. Nothing reaches the checker
   until you do.
2. Wait. Results update roughly **every 15 minutes**.
3. Enter the Task ID on the Autochecker page and read the verdict.
4. Fix every flag.
5. Repeat until the verdict is a pass with **zero** errors.
6. Only then submit.

> **Read the "Results as of" banner before you act on anything.** It shows the
> time of the run, and edits made after it are not reflected. A flag you have
> already fixed will keep appearing until the next refresh. Check the banner
> timestamp against when you saved before concluding a fix did not work — that
> mistake costs a whole cycle each time, and the holding window is finite.

Editing a value in a field is not always enough — press the **Set Start Time** /
**Set End Time** buttons, then Save. A typed value that was never committed is a
common reason a "fixed" boundary keeps flagging.

Submitting a task that has not passed with zero errors means being unable to
complete future tasks until it is resolved.

## Structure and Coverage

- **At least 3 annotations per track.** A two-annotation track fails.
- Every annotation has a start time, an end time, and a **non-blank caption in
  both Caption 1 and Caption 2**.
- Annotations are in **start-time order** — no row starts earlier than the one
  before it. Checked per track.
- **No gap longer than 0.1s. No overlap longer than 0.5s.** Checked per track.
  The rows should touch: 40.7 ending and 40.7 starting is ideal, 155.8 ending and
  155.9 starting still passes. Anything wider flags.
- The **first** annotation starts within **0.1s** of 0.0, and the **last** ends
  within **0.1s** of the window's end. Checked per track.
- **No row spans more than 40.0 seconds** (end − start), on either track. The fix
  is **splitting**, not writing more — added text does not move audit outcomes on
  long rows.
- **Both tracks cover the window independently.** On a Mini task the window is
  the **first 60 seconds**; the boundary row that starts before 60s counts in
  full, and coverage past it is not graded.

> **An empty row breaks three checks at once.** A row created but never filled
> has blank captions and defaults to a start time of 0, which puts it out of
> order too. If you see blank-caption and start-time-order flags on the same high
> row number, you have a stray annotation — delete it.

## Timestamp Format

- Seconds only. `[SS.S]` or `[SS.SS]` — **never more than two decimals.**
- Ranges are `[SS.S - SS.S]`.
- A single instant is allowed in Caption 2: `[SS.S]`.
- Every Caption 1 opens with its range.
- End ≥ start, and nothing may extend beyond the video's duration.
- The annotation's own start/end fields must match the caption's first and last
  timestamps. Auditors flag mismatches by hand — one wrote: *"Start time should
  be 2.6 so there is not overlap."*

## Marker Spellings

These four are spelling-checked by machine:

```text
((No speech present))
((No non-speech sounds present))
((No audio present))
((Non-English speech))
```

- Every `((` must be closed with `))`.
- **Never square brackets.** `[unintelligible]` fails.
- The words **unintelligible, muffled and garbled may only ever appear inside
  `(( ))`.** You cannot write "her speech is muffled here" as prose.

## Speakers

- Numbering starts at **1** and has **no skips**.
- With two or more speakers, **every** dialogue line carries
  `[SS.S-SS.S][Speaker N]:` — including `((Non-English speech))` lines.

### Paragraph heads

**Every paragraph of Caption 1 — every inline `[SS.S-SS.S]` range — must be
headed** by one of:

- `[Speaker N]:`
- a collective tag: `[Both speakers]`, `[All speakers]`, `[Speakers 1 and 2]`
- a sanctioned absence marker: `((No speech present))`, `((No speech))`,
  `((Non-English speech))`, `((non-English))`, `((unintelligible))`,
  `((inaudible))`
- a nested `[range]`

This holds **at every speaker count** — a solo narrator's paragraphs still need
`[Speaker 1]:`. A bare `[40.7 - 47.9]: text` paragraph flags. Brackets are the
format: `[Speaker 1):` and unbracketed `Speaker 1:` both flag. A single-stamp
sub-head like `[41.0] [Speaker 4]: …` is valid.

`[Crowd]` and `[Audience]` are **not** valid attribution. A group producing
intelligible words is a speaker and gets its own `[Speaker N]`; unresolvable
crowd noise belongs in the Audio track.

### Speaker references, both directions

- Every `[Speaker N]` tagged in Caption 1 must be described in Caption 2.
- **`Speaker N` may not appear in Caption 2 unless `[Speaker N]` appears in that
  same row's Caption 1.** This is row-level, not task-level.

### Category coverage

- Each Speech Characteristics caption containing speech covers **at least 3 of
  the 5 categories, with `[SS.S]` time marks**:

  **tone/emotion · volume · rhythm/pace · word emphasis · speech patterns**

- **All 5 must appear at least once per main speaker** across the task. A main
  speaker appears in **3 or more annotations**.
- No single category is individually required.
- Categories are counted **semantically, not grammatically** — a compound
  descriptor credits every category it names. "loud, professional tone at a
  steady pace" scores volume, tone and pace.
- **Accent is not one of the five.** It is checked separately, as a literal
  keyword — see below.

Two exemptions:

1. A speaker who says **two words or fewer** in the row needs no characteristics,
   and a row whose only speech is two words or fewer is exempt entirely.
2. `((unintelligible))` or `((inaudible))` speech needs none — what cannot be
   heard clearly has no describable delivery.

`((Non-English speech))` rows are **not** exempt. Paralinguistics are
language-independent: tone, volume and pace are audible without comprehension.

## Events Need Stamps

When an Audio or Visual caption names **more than one discrete event**, each
named event carries its own `[SS.S]` stamp.

**Discrete = momentary**: a camera cut, a laugh, a knock, a burst of applause, a
hand reaching into frame.

**No stamp needed** for:

- Continuous or background material — "throughout", "continues", `((persists))`,
  "background music plays", a constant hum.
- A caption naming only **one** event. The row's own window locates it.
- The internal cuts of a **montage** that the caption itself declares as one unit
  ("a montage of X, then Y, then Z") and locates with a single range. Discrete
  events *outside* the declared montage still need stamps, and a bare chain of
  "Cut to …" shot changes not declared as a montage is **not** exempt.

This is a full error, not a minor one. A caption that describes three things and
stamps two of them fails.

## Detail Presence

- Visual and audio captions each carry **both low-level detail and high-level
  context**. This one is a minor, note-level flag rather than a hard fail.
- **Spatial information must appear somewhere in the Visual captions**:
  locations in frame, relative positions, where things appear and disappear,
  direction of movement.

## Right Content, Right Track

- **No lyrics or speech content in Audio captions.**
- **No visual-only information and no non-human sounds in Speech
  Characteristics.**
- **No "Speaker N", no sounds, and no speech content in Visual captions.**
  Quoted on-screen text is always allowed.
- **No race or ethnicity mentions.** Ever.
- No hateful or offensive language.
- **No ambiguous wording.** "A good volume" is a flag. Say loud, soft, moderate.
- **Word caps: Transcription 200 words. Every other caption 1000 words.**

The 200-word transcription cap bites on long musical numbers and uninterrupted
monologues. Split the segment rather than trimming what was said.

## The Two Keyword Traps

Two checks are literal string tests. A flawless task fails without them.

1. **The word "accent" must appear in the speech captions.** Give each speaker's
   accent on their first appearance — which the guidance asks for anyway. When
   you can hear an accent but cannot place it, write "Speaker N has a
   non-American accent."
2. **One of "camera", "shot", "screen" or "frame" must appear somewhere in the
   task.** Ordinary visual writing produces these naturally — "the camera cuts
   to", "a wide shot", "the left of the frame" — but check before submitting.

## What It Does Not Check

It cannot tell whether anything you wrote is **true**.

It will pass an invented sound, a misheard word, a hallucinated job title, a
timestamp four seconds out, and a scene change you never mentioned. Every 0%
audit in `../references/common-errors.md` passed the Autochecker first.

Truth, completeness and clarity are checked afterwards by a human auditor who
re-watches the video against every caption and thumbs each annotation up or
down. That is what `../references/self-audit.md` is for.

The bar is **90% agreement between QC and Audit, measured per annotation, not
per task.**

## The Mini Task Has No Error Budget

> **MINI RULE: mark EVERY violation — even ONE error makes the verdict
> Incomplete and the task is SENT BACK. The main track's per-item threshold does
> not apply on the mini sheet.**

Some checks are **hard-limit (auto-pause)** rules: tripping one halts the task on
its own, regardless of how clean everything else is. The gap check is one of
them. On a Mini task, treat every flag as fatal.

## Getting Paid

- **A task that does not pass the Autochecker inside the task-holding window
  cannot be paid.** Claim a task only when you have time to finish it.
- If you cannot finish, request removal via the form in the latest Slack
  announcement.
- **You may not request removal of a task you already submitted that was sent
  back to you.** You fix it.
- A returned task gets no extra shadow task. The fix is part of the original.
