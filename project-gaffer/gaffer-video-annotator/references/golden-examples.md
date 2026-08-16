# Golden Examples

Nine tasks that passed audit with 100%, plus the project's worked example. Each
one teaches something different. When you are unsure how to handle a situation,
find the example that had the same problem and copy its shape.

All of them are reproduced in full in
`HANDSHAKE-AI/project-gaffer/extracted/PROJECT_GAFFER_MASTER_DOC.md`, with the
videos, keyframes and audio in
`HANDSHAKE-AI/project-gaffer/extracted/MASTER_VIDEO_SPEECH_INSPECTION_REPORT.md`.

## Contents

- [What They All Have in Common](#what-they-all-have-in-common)
- [The Model Visual Caption](#the-model-visual-caption)
- [Cooking Show Promo — Dense Detail on Short Shots](#cooking-show-promo--dense-detail-on-short-shots)
- [Cricket — One Utterance per Segment](#cricket--one-utterance-per-segment)
- [Live Cricket — Layered Audio](#live-cricket--layered-audio)
- [News Report — Conversation and Interruptions](#news-report--conversation-and-interruptions)
- [On-Screen Text — Overlay Timing](#on-screen-text--overlay-timing)
- [Family Entertainment — Montage and Song](#family-entertainment--montage-and-song)
- [Politics — One Long Speaker](#politics--one-long-speaker)
- [Rugby — Tracking People Without Names](#rugby--tracking-people-without-names)

## What They All Have in Common

Before the individual lessons, notice what is true of every one of them:

- **Plain sentences.** Nothing in any of these captions is written to impress.
  "The frame is a medium shot containing two women." "A player in a yellow shirt
  and green pants strikes the ball with her bat."
- **Nothing inferred.** Nobody is called a reporter, an anchor, a mother or a
  professional. People are "a woman in a blue-green dress", "the man in the blue
  suit", "Player 6".
- **Every cut timestamped.**
- **All on-screen text quoted exactly**, in double quotes.
- **Both tracks cover every second**, silence included.
- **The two tracks have different segment boundaries**, always.

## The Model Visual Caption

`-AJsQbl7t80` · 33.5 seconds · the project's designated worked example.

The full caption and the project's own commentary are quoted in
`../references/visual-audio-track.md`. The four things it is held up for:

1. Low-level detail and high-level context in the same caption — the earrings and
   the ring, plus what the studio display is for.
2. Every on-screen text quoted exactly.
3. Every screen change timed, including a two-second segment whose only event is
   a meter reading changing from `"99172"` to `"63622"`.
4. Partially visible text written only as far as it is readable —
   `"er Spring Networks"`.

## Cooking Show Promo — Dense Detail on Short Shots

`HnPifsJ-DrE` · 30 seconds · 26 of 26 annotations passed.

Thirty seconds split into 26 annotations — 4 Speech segments and 22 Visual+Audio
segments, several of the latter under a second long. That ratio is the clearest
demonstration in the set that the two tracks are segmented independently.

**What it teaches:** short shots still get full descriptions. The `[8.5 - 9.0]`
segment is half a second long and reads:

```text
[8.5- 9.0] There is a close-up, gently counter-clockwise rotating shot of food on a plate.
The plate is glossy, yellow-green ceramic. The food on the plate includes a fried egg with
black pepper sprinkled on top and a slice of toast with what appears to be a avocado mash
on top. The plate rests on a dark brown wooden surface.
```

Note "what appears to be a avocado mash" — hedged, because it is not certain. That
is the correct way to handle something you cannot positively identify. Do not
name it flatly, and do not leave it out.

**Also here:** two speakers saying the same words at once, each with their own
stamp; a freeze-frame-and-motion-trail effect described plainly; the trailing
`[26.0 - 30.0]: ((No speech present))` segment that covers the music-only outro.

## Cricket — One Utterance per Segment

`Gq_uMW2971c` · 54.6 seconds · 14 of 14 passed.

**What it teaches:** how short Speech segments can be. This task breaks a
punchy piece of commentary into segments of 1.3 and 2.2 seconds:

```text
[8.6-10.1][Speaker 1]: To me, that is wrong!
[10.2-11.5][Speaker 1]: It is erroneous!
[11.6-13.8][Speaker 1]: This is the law. It's in the law.
```

Each gets its own characteristics caption naming the emphasised word and when:

```text
[10.2-11.5] Speaker 1 speaks in a firm, emphatic tone with moderate volume. At [10.8] he
strongly emphasizes the word "erroneous."
```

**Also here:** a full-screen rules graphic transcribed word for word — six lines
of legal text in capitals, plus the header, the footer, and the moving background
graphics. When a screen is nothing but text, all of it goes in the caption.

## Live Cricket — Layered Audio

`AtzLa7hJ1JI` · 27.1 seconds · 12 of 12 passed.

**What it teaches:** how to write an Audio caption when several sounds overlap on
different timings. Split it into stamped lines rather than one sentence:

```text
[0.00–3.9] Repeated impact sounds are heard. At [3.9], the sound of a bat striking a ball
is heard.

[0.00-8.7] Crowd ambiance can be heard.
```

```text
[13.2-14.5] Crowd noise can be heard.
[13.2] A horn can be heard.
At [14.4], an impact sound can be heard.
```

The continuous bed of sound gets the full window; the discrete hits get their own
instants. Both are in the same caption.

**Also here:** a scoreboard graphic read out completely — `"SA 60-3 9.3 (13)
Target 98"` and `"TO WIN SOUTH AFRICA NEED 38 RUNS FROM 21 BALLS"` — and an
advertising board in the background quoted as `"Emirates FLY BETTER"`.

## News Report — Conversation and Interruptions

`9uwQXG11agU` · 185.3 seconds · 25 of 25 passed.

**What it teaches:** three people talking over each other, handled cleanly.

```text
[43.4 - 56.5] [Speaker 2]: But I think it's that slow, gradual process towards getting the
summit organized. You know, we need a date for it, we need a location for it, and clearly
you have to have meetings for it to move forward. So I don't think that- that weekend,
that Easter Sunday visit was necessarily about getting a concession right there.
[43.4 - 56.5] [Speaker 3]: Mhm. Right. Right.
[56.4 - 56.8] [Speaker 1]: But But.
```

Speaker 3 exists only to say "Mhm. Right. Right." and still gets a number and a
characteristics line:

```text
[43.4 - 56.5] Speaker 3 has a male voice with an American accent, he uses an acknowledging
tone, and he interrupts 3 times in a low volume.
```

**Also here:** fillers kept everywhere (`um`, `uh uh`, `you know`), a false start
written as `th- the reports`, and volume described relative to another speaker —
"His volume is lower than Speaker 1."

## On-Screen Text — Overlay Timing

`8ia7GY3BWR4` · 52.4 seconds · 11 of 11 passed.

**What it teaches:** text overlays that come and go on their own schedule, tracked
as sub-ranges inside one segment:

```text
At [5.4- 7.0] There is text overlay on the right side of the screen reading "THE MI 6
COMES WITH A DUAL LENS CAMERA" in blue text over a dark border..

At [7.3-9.2] A new text overlay enters on the left side of the screen reading "AND THE
LATEST PROCESSING TECHNOLOGY" in white text over a dark border.

At [9.5-11.4] Text to the right appears that reads "XIAOMI HAS BECOME ONE OF THE MOST
VALUABLE PRIVATE COMPANIES" in blue text over a dark border.
```

Each overlay gets its exact on and off times, its position, its colour, and what
it sits on.

**Also here:** a social media post read out in full including emoji — *"An emoji
with a yellow face and black sunglasses on, smiles following the word 'here'"* —
and text too small to read handled honestly: *"there is very tiny writing that is
illegible."*

## Family Entertainment — Montage and Song

`EpO06JNxJTQ` · 226.1 seconds · 11 of 11 passed.

**What it teaches:** two things at once.

**Montage.** A 39-second segment holds about thirty stamped shot descriptions,
one sentence each. See the excerpt in `../references/visual-audio-track.md`.

**Song.** The theme song runs 129 seconds and goes in the Speech track as a
single Speaker 1 turn with the lyrics transcribed, while the instrumental stays in
the Audio caption. The characteristics caption treats singing exactly like speech
— accent, tone, volume, pace, pauses at `[59.7]`, `[88.7]` and `[94.0]`, and which
words are emphasised.

**Also here:** the watermark rule for montages, where a bug is not present in
every clip: *"Throughout the track, there is a watermark in the bottom left that
reads 'Family Fun Pack' in most of the clips."* Accurate rather than tidy.

## Politics — One Long Speaker

`APWV7nQzioA` · 248.5 seconds · 10 of 10 passed.

**What it teaches:** how to segment a single continuous speech, and how many
emphasis marks a long segment needs.

Segments break mid-sentence when they need to, and the next caption simply picks
up where the last one stopped:

```text
[0.0-20.2] [Speaker 1]: ... And Nigerian forces are currently leading
[20.2-41.7][Speaker 1]: regional efforts against ISIS in West Africa and doing very well
as we have.
```

A 66-second segment carries eight separately timed emphasis notes:

```text
At [83.1], "trafficking" is emphasized. At [103.3], "human trafficking" is emphasized. At
[104.8], "slavery" is emphasized. At [118.7], "terrorists" is emphasized. At [127.6],
"obsolete" is emphasized and spoken slower and louder. At [129.3], "weak" is emphasized,
spoken slower and louder. At [131.0], "pathetic" is emphasized and also spoken slower and
louder.
```

**Also here:** a stutter written as `another ruth-ruthless jihadist terrorist
group`, and a misspoken year transcribed as the speaker said it — `April of
20,014` — not corrected to 2014. Verbatim means verbatim.

## Rugby — Tracking People Without Names

`CuFvCGSXOa8` · 43.6 seconds · 13 of 13 passed.

**What it teaches:** how to describe a crowd of near-identical people. Nobody has
a name, so the caption identifies everyone by shirt and number and stays
consistent for the whole task:

```text
The blue and white player with the number 6 on his back in dark blue is wearing neon
yellow cleats and is on the ground with both knees bent, passing a white rugby ball to
another teammate with the number 1 on his back in dark blue.
```

After that first full introduction they become "player 6", "player 1", "player 4
from the dark blue shirt team" — short, and never ambiguous, because both the
team and the number are always attached.

**Also here:** the best logo description in the set, worth reading before any task
with a broadcast ident:

```text
Centered on the screen is a logo of a shield whose top is slanted up to the right, with a
U-shape cut out of it that divides it into 3 parts. Inside the pieces of the shield is a
silver number 7 against a red background. Underneath the logo are the words 'WORLD RUGBY
TM' in black.
```

And three speakers distinguished purely by accent — American, Scottish, Irish —
each with their own stamped range inside one characteristics caption.
