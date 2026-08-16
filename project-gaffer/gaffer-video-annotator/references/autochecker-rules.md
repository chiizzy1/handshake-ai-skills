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

Submitting a task that has not passed with zero errors means being unable to
complete future tasks until it is resolved.

## Structure and Coverage

- **At least 3 annotations per track.** A two-annotation track fails.
- Every annotation has a start time, an end time, and a non-blank caption.
- Annotations are in **start-time order**.
- **No gap longer than 1.0s. No overlap longer than 0.5s.** Small gaps are
  tolerated; meaningful content still must not be left uncovered.
- The **first** annotation starts within 0.5s of 0.0.
- The **last** annotation ends within 0.5s of the video's end.
- **Both tracks cover the whole video independently.**

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
- Speech Caption 2 must reference the speakers that Caption 1 tags.
- Each Speech Characteristics caption containing speech covers **at least 2 of
  the 5 categories, with time marks.**
  Exempt: speakers of two words or fewer, and unintelligible-only annotations.
- **All 5 categories must appear at least once per main speaker** across the
  task. A main speaker is one appearing in **3 or more annotations**.

> **Open question — do not guess.** The instruction page lists seven qualities
> (tone, volume, rhythm/pace, emphasis, speech patterns, accent, speaker
> characteristics) and asks for the three most important. The checker counts
> "5 categories" without naming them. Aim for three or more per annotation and
> make sure tone, volume, pace, emphasis and accent all appear for each main
> speaker — that is the safest reading. Ask in Slack rather than assuming.

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

## Getting Paid

- **A task that does not pass the Autochecker inside the task-holding window
  cannot be paid.** Claim a task only when you have time to finish it.
- If you cannot finish, request removal via the form in the latest Slack
  announcement.
- **You may not request removal of a task you already submitted that was sent
  back to you.** You fix it.
- A returned task gets no extra shadow task. The fix is part of the original.
