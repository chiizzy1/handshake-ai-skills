# The Ten Common Errors

Every one of these is a real Project Gaffer task that scored **0%** on audit.
Each section shows what the worker submitted, what the auditor wrote back, and
what should have been written instead.

Read these before your first task and again whenever an audit comes back.

## Contents

- [1. Visual Description — Not Enough Detail](#1-visual-description--not-enough-detail)
- [2. Speech Characteristics — Missed Paralinguistics](#2-speech-characteristics--missed-paralinguistics)
- [3. Transcription — Misheard Words](#3-transcription--misheard-words)
- [4. OCR — On-Screen Text Typed Wrong](#4-ocr--on-screen-text-typed-wrong)
- [5. Missing Audio — Environmental Sounds Left Out](#5-missing-audio--environmental-sounds-left-out)
- [6. Speaker Attribution — Two People Merged Into One](#6-speaker-attribution--two-people-merged-into-one)
- [7. Hallucination — Describing Something That Is Not There](#7-hallucination--describing-something-that-is-not-there)
- [8. Missing Speech — Part of the Window Not Transcribed](#8-missing-speech--part-of-the-window-not-transcribed)
- [9. Timestamps — Stamps That Do Not Match the Video](#9-timestamps--stamps-that-do-not-match-the-video)
- [10. Wrong Track — Content in the Wrong Caption](#10-wrong-track--content-in-the-wrong-caption)
- [The Pattern Behind All Ten](#the-pattern-behind-all-ten)

## 1. Visual Description — Not Enough Detail

Tennis broadcast, `BGGOv8IYsA0`, 355.9 seconds. Annotation #54, window
`[301.9 – 335.4]`.

**Submitted:**

```text
Caption 1 · Visual
[301.9 - 335.4] The wide court view shows another point. The player in the light blue
shirt moves near the far side while the dark-clothed player covers the near side. Near
the end, the camera cuts to a closer sideline view where the players approach near the
court edge and one player in red outerwear stands nearby. On screen text reads "Rune 3
15, Van De Zandschulp 4 15" followed by an updated score " "Rune 3 30, Van De Zandschulp
40 15"
```

**Auditor:**

> Please check annotations 1, 2, 3, 31, 4, 5, 6, 7, 32, 8, 35, 11, 36, 37, 56,
> 57, 58, 13, 14, 39, 16, 19, 21, 23, 24, 26, 28, 29, 44-55
>
> Please check the amount of detail used in descriptions and take special care to
> annotate scene transitions throughout a given timestamp

**Should have been:**

```text
Caption 1: [301.9-311.9] "The wide court view shows another point". [312-314.5] Cut to a
close up of the player in green walking away from the camera. [314.6-315.2] Cut to a
close up of the player in blue. [315.3-322.9] The camera cuts to a wider shot of the
player in blue walking towards the net as he meets the player in green and they shake
hands and turn away. [323.0-326.5] Cut to a close up of the player in blue picking up
their racket and a towel from a bench. [326.6-333.0] Cut to a close up shot of the player
in green walking across the court and putting his tennis racket down. [333.1-335.0] The
camera cuts to the player in blue with a black and yellow duffel bag they are wearing as a
backpack as they walk across the court away from the camera. [335.1-335.4] Cut to shot of
the crowd.
```

**The lesson.** Thirty-three seconds held eight separate shots. The worker wrote
one. A single sentence covering half a minute of video is almost always a fail.
Watch for the cuts first, then describe each one.

Note also that nearly forty annotations were listed. When detail is thin, it is
thin everywhere, and the whole task goes down together.

## 2. Speech Characteristics — Missed Paralinguistics

Physics lecture, `79GY-hI_emE`, 353.1 seconds. Annotation #1, window `[0.0 – 13.0]`.

**Submitted:**

```text
Caption 1 · Transcription
[0.0-13.0] [Speaker 1]: There's one more property, of this thing that is important, and
it's...uh something called the correspondence principle, which is another classical
intuition.

Caption 2 · Speech characteristics
[0.3-13.0] Speaker 1 speaks at a steady lecture pace in a clear Peruvian accent, with
moderate volume and an explanatory tone. He pauses briefly at [5.7-6.5]. He raises his
pitch slightly as he emphasizes "principle" at [9.4-9.6].
```

**Auditor:**

> there is a brief pause after "property." there is also a slight stutter during
> this section of the caption "it's...uh something". The rise in pitch toward the
> end of the word "principle" is not quite an "emphasis" but still great catching
> the change of pitch. There is emphasis on "another"

**The lesson.** That caption is not lazy. It has accent, pace, volume, tone, a
timed pause and a timed pitch change — and it still failed, because in thirteen
seconds it missed a second pause, a stutter, and a second emphasis.

Speech Caption 2 is not a summary of the voice. It is a list of everything the
voice did. Play the segment again with your eyes shut and mark every pause,
every filler, every stumble, every stressed word.

## 3. Transcription — Misheard Words

Press conference, `2CTWu-UkhtA`, 547.5 seconds. Annotation #63, window
`[246.3 – 253.8]`.

**Submitted:**

```text
[246.3-253.8] [Speaker 2]: I have to find that we're gonna be treated fairly because
everybody sees it now, and it is a pure wit gun.
```

**Auditor:**

> speaker says "witch hunt," not wit gun

and elsewhere in the same task:

> See feedback ID 150, 52 - label should mention speech as unintelligible, not
> "no speech," ID 65, 66 misquote - should be "witch hunt"

**The lesson.** "A pure wit gun" is not a phrase. When a transcription does not
work as English, you misheard it — go back and listen again at reduced speed.

The second half of that note is its own error: a segment was tagged
`((No speech present))` when someone was in fact speaking, just not clearly. That
is `((unintelligible))`. The three tags are not interchangeable.

## 4. OCR — On-Screen Text Typed Wrong

CNBC business report, `2P_ZNErFQF8`, 63.6 seconds. Annotation #7, window
`[6.9 – 12.7]`.

**Submitted:**

```text
Caption 1 · Visual
[6.91 - 12.69] A picture of a building with name "Survey Monkey" appears in the
background. On screen text changes to "THAT'S ACCORDING TO SURVVEY MONEY'S SMALL BUSINESS
CONFIDENCE INDEX". We see a watermark "CNBC" on the bottom right corner and "GETTY"
watermark on top right corner through the scene.
```

**Auditor:**

> Mispelled on screen text in ID 7 could confuse meaning - additional
> misspellings in ID 8
>
> text is misspelled and could misconstrue meaning "Survey Monkey"

**The lesson.** `SURVVEY MONEY'S` is a typo the worker introduced. The company is
Survey Monkey. Two characters wrong changed the meaning, and the task failed.

Type on-screen text slowly, then read it back against the frame character by
character. Pause the video on the frame — do not transcribe a banner from memory
after it has gone.

The mirror-image error is just as bad: if the screen itself contains a typo, you
copy the typo. `RYAN: IVE NOT SEEN FULL SENATE HEALTH BILL YET` stays without the
apostrophe. You are recording what is on screen, not writing correct English.

## 5. Missing Audio — Environmental Sounds Left Out

World Rugby Sevens, `7Wd9YV5Jnyk`, 113.2 seconds. Annotation #27, window
`[0.0 – 37.7]`.

**Submitted (Audio caption):**

```text
[0.00 - 37.68] Stadium ambience and crowd noise are audible throughout the segment. In the
background, there is music featuring drums and trumpets.
```

**Auditor:**

> Please include all environmental sounds in the audio portion of the annotations
> Great job otherwise!!
>
> Please include the referee whistle at 19.50 and at 32.80 in c2

**The lesson.** The visual caption on this one was long and good. The audio
caption named the ambience and the music correctly. It missed two whistle blasts,
and the task scored 0%.

"Great job otherwise" is the whole point. There is no partial credit for a nearly
complete audio caption. Listen to the segment on its own, with the picture
ignored, and mark every discrete sound.

## 6. Speaker Attribution — Two People Merged Into One

`1sozeCvZMSI`, 199.4 seconds. Annotation #9, window `[83.5 – 87.9]`.

**Submitted:**

```text
Caption 1 · Transcription
[83.5-87.9][Speaker 1]: Ohhh, that's naughty. But very nice.

Caption 2 · Speech characteristics
[83.5-87.9]: Speaker 1 uses a playful tone throughout, noticeably stretching out the
beginning of the phrase at [83.7]. Following a pause from [85.0-86.2], his tone shifts to
sounding impressed, emphasizing the word 'very' through elongation at [86.4].
```

**Auditor:**

> That was 2 diffrent speakers
> Speaker1 : Ohhh, that's naughty.
> Speaker 2: But very nice.

**The lesson.** Look at what the worker's own Caption 2 says: a pause from
`[85.0-86.2]`, and then "his tone shifts". That was not a tone shift. That was a
different person starting to talk.

When you find yourself writing that a speaker's voice "changes" across a pause,
check whether it is the same speaker at all. Two voices in a segment is the
default assumption in conversation, not the exception.

## 7. Hallucination — Describing Something That Is Not There

Cooking demonstration, `5aNa7J-23Kc`, 92.9 seconds. Annotation #19, window
`[0.0 – 22.3]`.

**Submitted (Audio caption):**

```text
[00.0-22.3] Soft piano music
```

**Auditor:**

> Caption 2:
> - There is no soft piano music playing in the segment.

**The lesson.** The visual caption for this segment was detailed and accurate —
the woman's blouse, the cabbage in the glass bowl, the spice jars, the knife
block, the `"HOW TO SHRED CABBAGE."` overlay, all correct. Then four words of
invented music sank it.

"Soft piano music" is what a cooking video usually sounds like. That is exactly
why it got written, and exactly why it is wrong. Never write what a video of this
kind would probably contain. Write what this video contains.

The same rule kills inferred identities and roles: "the network's chief anchor",
"a female news reporter" where nothing on screen says reporter, "the speaker is
German". If you cannot point at the frame or the audio and show it, do not write
it.

## 8. Missing Speech — Part of the Window Not Transcribed

Long-form interview, `8uvzimVM7n0`, 396.2 seconds. Annotation #7, window
`[65.0 – 140.0]`.

**Submitted:**

```text
Caption 1 · Transcription
[65.0 - 140.0][Speaker 1]: Now, in my opinion, seeing this man prove every single doubter
wrong one by one while building businesses that actually make a difference is slowly
turning him into the greatest entrepreneur of all time. And when I first met him, he left
me with some advice that left me scratching my head for a couple of years. Alright, so
when I was 18, I started my first company and I got into the pilot program of this new
school for entrepreneurs called Draper University. It was a crazy month-long bootcamp on
how to start your startup.
```

**Auditor:**

> - Segment from [91.0-140.0] is not captioned. Both captions should be revised
> to properly transcribe the dialogue in caption 1 and properly describe the
> paralinguistics of the dialogue in caption 2.

The overall feedback on this task is worth reading in full, because it lists four
different error classes at once:

> **Speech Transcription:** Some annotations misidentify the speakers through the
> speaker tags within the segments. Annotations fail to capture the entire
> transcript heard within the time segment. Ensure stutters are properly
> transcribed within the caption, as there are multiple moments in which a
> speaker, mainly Speaker 4, is heard stuttering throughout their speech.
>
> **Speech characteristics:** Some annotations are missing the paralinguistic
> qualities of all speakers heard within the segments
>
> **Audio:** There is some unnecessary information captioned within annotations
> about whether or not something is heard in the segment, which should not be
> included. Some non-speech audio events are not labeled when they are prominent
> in their respective segment.
>
> **Visual:** Timestamps in which a visual event is shown are off in some
> annotations. There are some missing visual events that are not captioned within
> annotations, such as OCR, scene changes, spatial locations, etc.

**The lesson.** A 75-second window was covered by 26 seconds of transcript. The
caption reads as complete — full sentences, ending on a full stop — which is what
makes it dangerous. Check coverage by the clock, not by whether the paragraph
looks finished.

Note the reviewer also had to hand the worker the whole speaker list: *"s1 main
host guy, s2 commercial guy, s3 interviewer, s4 Elon, s5 Female informer, s6 Elon
coworker, s7 Man asking question"*. Seven speakers, and the tags were wrong.

## 9. Timestamps — Stamps That Do Not Match the Video

Political programme, `EDuFccGdEQs`, 270.3 seconds. Annotation #68, window
`[145.3 – 175.5]`.

**Submitted (extract):**

```text
[145.3-175.5]
At [155.5] the advertisement returns to the "LIFE LIBERTY & LEVIN" graphic. At [171.5] the
advertisement changes to the "MY VIEW…" graphic. At [145.3] The man in the blue suit is
now in a smaller window on the left [...]
[152.2] The image on the right changes to another of the same man. He is now wearing a
black button-up shirt, untucked over light blue jeans [...]
[163.3] The image changes to another of the same man. He is smiling facing to the left [...]
[173.3] The image changes to that of the same man wearing a white button up shirt [...]
```

**Auditor:**

> Caption 1:
> - Timestamps in which the images on the right appear do not align with what is
> shown on the video. E.g., event noted at [152.2] occurs at [148.2], event at
> [163.3] occurs at [153.0], event at [173.3] occurs at [157.2]
> - The right image also changes around [161.6 - 175.5]

**The lesson.** The descriptions were excellent — clothing, sunglasses, the
tractor half-submerged in water, the slow zoom on each still. Every one of them
was attached to the wrong moment, drifting from four seconds to sixteen. And a
change in the `[161.6 - 175.5]` stretch was missed entirely.

Detail attached to the wrong timestamp is not partly right. It is wrong. Step
through frame by frame at each transition and read the number off the player
before you write it.

## 10. Wrong Track — Content in the Wrong Caption

The project site files this as its tenth error and illustrates it with the same
task and the same annotation as error 9 (`EDuFccGdEQs` #68, plus #71), so there
is no separate failed caption to study. The rule it is pointing at is the one
tested directly by the assessment:

**Anything with words a person can make out belongs to the Speech track. Anything
else belongs to the Audio track.**

The routing table is in `../references/visual-audio-track.md`. The four that get
misfiled most often:

| Often misfiled | Correct home |
|---|---|
| Laughter | Audio caption. Speech Caption 2 may say the tone brightened, but not "he laughs" |
| A crowd chanting words in unison | Speech track, with a speaker number |
| Sung lyrics | Speech track. The instruments stay in the Audio caption |
| A gesture — "as he raises his arm" | Visual caption. Never Speech Caption 2 |

Two more track boundaries worth holding on to:

- A cough, sneeze or breath is a **sound**, so it is Audio — even though it came
  out of a speaker's mouth.
- A stutter or filler is **speech**, so it is Caption 1 as text and Caption 2 as
  description — never Audio.

## The Pattern Behind All Ten

Look at what these tasks had in common. Almost none of them were careless. The
tennis worker described the players correctly. The rugby worker got the ambience
and the music. The political worker wrote beautiful descriptions of every still
image. The cooking worker nailed the kitchen.

They failed on one of three things:

1. **Something present was left out** — a cut, a whistle, a stutter, forty
   seconds of speech.
2. **Something absent was written in** — piano music, a merged speaker, a job
   title.
3. **Something real was attached to the wrong moment or the wrong track.**

So the three questions to ask before you submit are:

- Is everything that happened in here?
- Is everything in here something that actually happened?
- Is it in the right place, at the right second, in the right caption?

The full checklist is in `../references/self-audit.md`.
