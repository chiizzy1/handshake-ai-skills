# Visual+Audio Track — Visual and Audio

The Visual+Audio track holds two captions. Caption 1 is **everything you see**.
Caption 2 is **every sound that is not speech**.

## Contents

- [Format](#format)
- [Which Track Does This Belong To](#which-track-does-this-belong-to)
- [Caption 1 — Visual](#caption-1--visual)
- [The Detail Checklist](#the-detail-checklist)
- [On-Screen Text](#on-screen-text)
- [Scene Changes and Timestamps](#scene-changes-and-timestamps)
- [Persistent Elements](#persistent-elements)
- [Montages](#montages)
- [The Model Visual Caption](#the-model-visual-caption)
- [Caption 2 — Audio](#caption-2--audio)
- [Failures to Avoid](#failures-to-avoid)

## Format

Same shape as the Speech track. The segment window opens the caption, and events
inside it get their own stamps:

```text
[14.7-29.1] The camera returns to the same high, wide stadium shot. At [20.1], the
top-left tournament graphic changes to the text "ICC" beneath a blue symbol. At [22.2],
the camera cuts to a close-up of a player wearing a blue jersey with red and green trim,
a red cap, and sunglasses resting on the cap brim.
```

Two ways to stamp events inside a caption, both used in pass-grade work:

- Inline — `At [20.1], the graphic changes to...`
- As a sub-range on its own line — `[12.4-14.8] Text appears to the left that reads...`

Use sub-ranges when something is on screen for a stretch, and inline stamps for
instant events like a cut. Every stamp must sit inside the segment's own window.

Remember the Visual+Audio segments are **not** the Speech segments. They break on
picture changes, not on who is talking.

## Which Track Does This Belong To

The single most common structural error is putting a sound in the wrong caption.
This table is taken from the assessment.

| Sound | Goes to |
|---|---|
| A cough from someone off-screen | **Audio** |
| Rustling noises | **Audio** |
| Instrumental background music | **Audio** |
| A crowd cheering, general noise, no words | **Audio** |
| Laughter between a speaker's sentences | **Audio** |
| Background chatter with no words you can make out | **Audio** |
| Applause, whistles, impacts, engines, swooshes, footsteps | **Audio** |
| A speaker's stutter | **Speech** (word in C1, stutter noted in C2) |
| Sung lyrics you can clearly make out | **Speech** (with a Speaker #) |
| A crowd chanting "GO! GO! GO!" in unison | **Speech** (words are intelligible) |
| A voiceover, a loudspeaker announcement, a talking toy | **Speech** |

The test is simple: **can you make out words?** Words go to Speech, with a
speaker number. Noise goes to Audio.

Coughs, sneezes and laughs are not words, so the sounds themselves go to Audio.
Speech Caption 2 may describe what a laugh did to the delivery — "his tone turns
brighter" — but the word "laughter" itself stays out of Caption 2.

The instrumental part of a song goes to Audio even when the lyrics go to Speech.
The same song lives in both captions, split by that line.

## Caption 1 — Visual

You are writing for a reader who cannot see the video and has to picture it.
Everything on screen counts.

Structure each segment roughly like this:

1. **What kind of shot it is** and what changed to get here. "The frame is a
   medium shot containing two women." "The camera cuts to a low replay shot from
   ground level beside the pitch."
2. **The people** — clothing, hair, accessories, where they are, what they are
   doing.
3. **The setting** — background objects, walls, furniture, screens, weather.
4. **On-screen text**, quoted exactly.
5. **Anything that changes during the segment**, each with its own timestamp.

Here is a pass-grade opening segment. Notice how ordinary the sentences are and
how much is in them:

```text
[0.0 - 2.1] The frame is a medium shot containing two women. The camera slowly zooms in
on the frame

The woman on the left is wearing a black and white striped tank top, blue ripped jeans, a
black belt with a silver clip, a black watch on her left wrist, and a ring on her left
ring finger and right middle finger. The woman on the left has black hair that goes past
her shoulders, and she has silver hoop earrings. The woman on the left is standing.
Behind this woman is a vase, and to the left of the woman is a potted plant sitting on
the windowsill.

The woman on the right has black shoulder-length hair, stud earrings, a black hair tie on
her right wrist, and is wearing black pinstripe pants and a dark green blouse. She is
sitting on a wooden stool.

Behind both women is a window with predominantly white polka dotted curtains and a
purple-orange city skyline. The wall behind them is white, and to the right of the frame
has a red kitchen appliance with a yellow towel on top of a white counter that is pink on
top. Above the appliance is a kitchen cabinet that's white and pink at the bottom.
```

That is 2.1 seconds of video. Nothing in it is clever. It just does not miss
anything.

## The Detail Checklist

Walk this list on every segment. If a thing is in the frame and not in your
caption, the caption is incomplete.

**People**
- Approximate build and hair — length, colour, how it is worn
- Every item of clothing, with colour and pattern
- Jewellery, watches, glasses, hats, microphones, hair ties
- Where they are in the frame and whether they are sitting, standing, walking
- What their hands are doing, and gestures, with timestamps
- Facial expression and where they are looking

**Camera**
- Shot type — wide, medium, close-up, aerial, point-of-view, low-angle
- Movement — zoom in or out, pan, tilt, static, slow-motion, freeze frame
- Every cut, with a timestamp

**Setting**
- Room, field, studio, street
- Furniture, appliances, plants, signage, vehicles
- What is on any screen inside the frame
- Lighting and background colours

**Graphics**
- Lower thirds, banners, scoreboards, tickers, logos, watermarks
- Animations and transitions, and what they look like
- When each appears, changes, and disappears

**Numbers on screen**
- Scores, prices, stock tickers, meter readings, clocks — copied digit for digit,
  and re-stated every time they change

## On-Screen Text

This has its own audit category, and the rules are strict.

**Quote it exactly, character for character, including typos.** If a banner
reads `RYAN: IVE NOT SEEN FULL SENATE HEALTH BILL YET` with no apostrophe, you
write it with no apostrophe. Silently "correcting" it to `I'VE` is a graded
error.

**Write only what is legible.** If someone's arm covers part of the word
`TEXAS`, you write that the text `"TEX"` is legible and that the rest is not.
You do not write `TEXAS`, because you cannot see it, and you do not leave it out
because all on-screen text must be included.

The model example handles a partly hidden label like this:

```text
Above the meter screen, there's a red rectangular area with a white label on it. It's
partially cut off. But we can read "er Spring Networks" in the first row, and
"0013500101748728" in the second row, under which a wide and flat barcode, and under the
barcode the text "S-NIC514 IC: 5975A-N/C514".
```

**Text too small or blurred to read at all** is called out as illegible:

```text
In the top left box we can read the words "Mi 6", while below that there is very tiny
writing that is illegible.
```

**Every change gets captured.** A meter reading that goes from `"99172"` to
`"63622"` is two facts, not one. A banner that swaps to a new headline is a
stamped event.

**Names are allowed when they are on screen.** The model caption writes "Florida
Governor Ron DeSantis" because the quoted overlay says
`GOV. RON DESANTIS (R) - FL`. If a name is not shown, you do not use it, no
matter how recognisable the face is.

**Describe the styling too** when it is visible — colour, position, and what it
sits on: *"in blue text over a dark border"*, *"in white text over a blue
underline, in the center of the screen"*.

## Scene Changes and Timestamps

Every cut is an event and needs a timestamp. Missing a scene change is a graded
failure on its own — the assessment fails an annotation purely for not
mentioning the scene change at `[71.9]`, even though the description that
follows it is fine.

**Your timestamps must match the video.** In the worst timestamp failure in the
project, a worker's events were stamped `[152.2]`, `[163.3]` and `[173.3]` when
they actually happened at `[148.2]`, `[153.0]` and `[157.2]` — drift of four to
sixteen seconds. Scrub to the frame before you write a number down.

**Never describe anything outside the window.** A caption for `[43.0–54.6]` that
ends with "At [55.0 - 59.7] he turns his head" is wrong on that ground alone.
That content belongs to the next segment.

Compare these two treatments of the same 33 seconds of tennis. The first failed
its audit; the second is what the reviewer wanted:

*Failed — one flat block for 33 seconds, cuts unmarked:*

```text
[301.9 - 335.4] The wide court view shows another point. The player in the light blue
shirt moves near the far side while the dark-clothed player covers the near side. Near the
end, the camera cuts to a closer sideline view where the players approach near the court
edge and one player in red outerwear stands nearby.
```

*What it should have been — every cut found and stamped:*

```text
[301.9-311.9] "The wide court view shows another point". [312-314.5] Cut to a close up of
the player in green walking away from the camera. [314.6-315.2] Cut to a close up of the
player in blue. [315.3-322.9] The camera cuts to a wider shot of the player in blue
walking towards the net as he meets the player in green and they shake hands and turn
away. [323.0-326.5] Cut to a close up of the player in blue picking up their racket and a
towel from a bench. [326.6-333.0] Cut to a close up shot of the player in green walking
across the court and putting his tennis racket down. [333.1-335.0] The camera cuts to the
player in blue with a black and yellow duffel bag they are wearing as a backpack as they
walk across the court away from the camera. [335.1-335.4] Cut to shot of the crowd.
```

Same footage. Eight shots instead of one. The audit comment was: *"Please check
the amount of detail used in descriptions and take special care to annotate scene
transitions throughout a given timestamp."*

## Persistent Elements

Things that sit on screen for the whole video — watermarks, station IDs, bugs —
get described **in full the first time**, then referred back to briefly in every
later segment.

First time:

```text
The watermark "10TampaBay.com" is visible in the top left corner of the screen.
```

Every segment after:

```text
The "10TampaBay.com" watermark is unchanged.
```

Other pass-grade phrasings: *"The watermark in the top left remains"*, *"The
watermark in the top left and the scoreboard at the bottom remains."*, and for a
watermark that only shows in some clips of a montage: *"Throughout the track,
there is a watermark in the bottom left that reads 'Family Fun Pack' in most of
the clips."*

Do not drop it after the first mention, and do not re-describe it from scratch
every time.

## Montages

Fast-cut montages get one segment holding a long stamped run of events, one per
shot. Keep each entry short and factual:

```text
[11.0-50.4] The video cuts through a fast montage of family clips. At [11.7], a child in
orange holds a green float-like object. At [12.3], a baby in white eats cake with balloons
in the background. At [16.2], a girl and boy wearing blue and yellow ride on a
roller-coaster-like ride. At [18.0], the camera cuts to a close-up of a child in yellow
wearing red, white, and blue sunglasses. At [18.7], a woman and child ride in a raised
construction-style lift.
```

That one continues for another thirty entries. Every cut in the montage is
present. None of the entries is longer than a sentence.

## The Model Visual Caption

This is the project's own worked example, marked as the standard to copy. The
video is a news report about a solar bill veto.

```text
[0.0 - 9.0] The video shows a news reporter standing to the right side of a large screen
display in a news studio. She is wearing a dark blue sleeveless dress with a square
neckline. She has long straight hair separated in the middle. She is wearing long
stick-shaped metal earrings and a ring on her left ring finger. The screen displays the
text "VETOES & CHALLENGES" in white, alongside an image of a white voting booth with the
American flag and the word "VOTE." The reporter speaks while maintaining direct eye
contact with the camera. She holds her hands in front of her abdomen throughout, except
when she gestures both hands to her right at [6.0].

The watermark "10TampaBay.com" is visible in the top left corner of the screen.

[9.0 - 14.0] The video cuts to a vertically split screen. On the left side, a blue frame
features white and blue text. At the top of the frame, a title written on a white
horizontal strip reads "VETOED." Below the title, the blue background displays two bullet
points in white text. The first bullet point states: "Bill would have phased out current
solar net metering", while the second explains, "Metering is the rate people get paid for
using solar, sending leftovers to the grid." The right side of the screen displays a roof
with solar panels. There are a total of 8 rows of solar panels, most of them divided into
5 grids.

The "10TampaBay.com" watermark is unchanged.

[14.0 - 17.0] The right side of the screen displays a meter locked in a gray metal box,
with two red labels affixed to the front of the box. The red label at the top says "SOLAR
PHOTOVOLTAIC ARRAY AC COMBINER", while the bottom red label says "GRID INTERACTIVE ROOFTOP
SOLAR PHOTOVOLTAIC INVERTERS PRESENT".

The "10TampaBay.com" watermark is unchanged.

[17.0 - 20.0] The right side of the screen changes to display a meter reading of "99172".
Above the meter screen, there's a red rectangular area with a white label on it. It's
partially cut off. But we can read "er Spring Networks" in the first row, and
"0013500101748728" in the second row, under which a wide and flat barcode, and under the
barcode the text "S-NIC514 IC: 5975A-N/C514".

The "10TampaBay.com" watermark is unchanged.

[20.0 - 22.0] The meter reading changes to "63622".

The "10TampaBay.com" watermark is unchanged.
```

The project's own note on why this is the model:

> low-level details (clothing, positioning, gestures) + high-level context
> (news-studio setting, the display's purpose), every on-screen text quoted
> exactly, every screen change timed.

and:

> Partially visible text handled right ("er Spring Networks" — only what's
> readable), every meter change captured ("99172" → "63622"), and names allowed
> because they're on screen. The persistent watermark is introduced once in the
> first segment, then carried in every later one.

Note the two-second segment at `[20.0 - 22.0]`. The only thing that changed was
a number on a meter, and it still got its own segment.

## Caption 2 — Audio

Every non-speech sound, with a timestamp when it is a discrete event.

Cover:

- **Music** — describe it, do not just say "music". "Upbeat bass music is heard
  softly in the background." "Upbeat, fast-tempo acoustic guitar music begins and
  continues throughout the segment." "In the background, there is music featuring
  drums and trumpets."
- **Ambience** — crowd noise, stadium ambience, room tone, static, traffic.
- **Discrete effects**, stamped: impacts, whistles, footsteps, swooshes, bell
  dings, horns, doors, engines.
- **Non-verbal human sounds** — breaths, coughs, laughter, applause.

Samples from pass-grade work:

```text
[2.1 - 4.4] The upbeat bass background music continues throughout. At [3.27] a bell ding
and a swooshing sound is heard.
```

```text
[14.7-29.1] Background stadium ambience continues. Footsteps are heard at [25.3], followed
by the thud of a bat striking a ball at [25.6]. Audience cheering begins at [26.9]
followed by brief low-volume applause.
```

```text
[19.2-21.5] Cheering can be heard with a whistle blowing rapidly in the background.
[21.51-25.5] Cheering and whistling can continue to be heard along with music that starts
playing.
```

```text
[0.0-1.4] In the background, there is a low pitched, deep electronic noises that sound
like a laser powering on.
```

```text
[5.4-11.4] Calm instrumental music can be heard playing in the background
At [9.2] the speaker can be heard taking a breath.
```

### Sounds that continue across segments

Describe the sound in full the first time, then make clear it is the same sound
carrying on. Do not re-introduce it as if it were new. The assessment's model
answer uses the `((persists))` tag:

```text
[79.0-82.0]: Soft instrumental music plays in the background, and a loud noise from an
electric food processor motor whirs.
[82.0-85.0]: Background music ((persists)).
```

and when a continuing sound changes character:

```text
Background music ((persists)), but the bells become more noticeable
```

Plain continuation wording works too, and is more common in the golden examples:
*"The upbeat bass music continues in the background."*, *"Crowd ambience
continues."*, *"The soft instrumental music continues."*

### Keep it to what is there

Describe the sounds present. Do not pad the caption with commentary about your
own listening or about what is absent — one audit flagged *"unnecessary
information captioned within annotations about whether or not something is heard
in the segment, which should not be included."*

When a segment genuinely has no non-speech sound at all, say so once and move on:
*"No other distinct non-speech sounds are heard."* Do not use that line as a
substitute for listening properly.

## Failures to Avoid

Full write-ups are in `../references/common-errors.md`.

- **Inventing a sound.** A caption said "Soft piano music" over a segment with no
  music at all. The audit note: *"There is no soft piano music playing in the
  segment."* If you did not hear it, it is not there.
- **Missing environmental sounds.** A rugby segment described the crowd and music
  but missed the referee's whistle at `19.50` and again at `32.80`. The audit
  comment was *"Please include all environmental sounds in the audio portion of
  the annotations. Great job otherwise!!"* — everything else was fine, and it
  still failed.
- **Misspelling on-screen text.** A caption wrote `"SURVVEY MONEY'S"` where the
  screen said Survey Monkey. The note: *"text is misspelled and could misconstrue
  meaning"*.
- **Timestamps that do not match the picture.** See
  [Scene Changes and Timestamps](#scene-changes-and-timestamps).
- **Inferring a role or identity.** "the network's chief anchor" is a graded
  error when no on-screen text says so. Describe the man in the suit.
- **Not enough detail, and unmarked cuts.** The tennis example above.
