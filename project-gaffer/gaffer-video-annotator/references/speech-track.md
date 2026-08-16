# Speech Track — Transcription and Speech Characteristics

The Speech track holds two captions. Caption 1 is **what was said**. Caption 2 is
**how it sounded**. Both cover the same segment window.

## Contents

- [Format](#format)
- [Speaker Numbering](#speaker-numbering)
- [Caption 1 — Transcription](#caption-1--transcription)
- [The Three Tags](#the-three-tags)
- [Songs and Lyrics](#songs-and-lyrics)
- [Swearing and Slurs](#swearing-and-slurs)
- [Caption 2 — Speech Characteristics](#caption-2--speech-characteristics)
- [What Never Goes in Caption 2](#what-never-goes-in-caption-2)
- [Worked Segments](#worked-segments)
- [Failures to Avoid](#failures-to-avoid)

## Format

Every caption opens with its window in square brackets, and every speaker turn
carries a speaker tag:

```text
[0.0-8.5][Speaker 1]: So for me, a lot of people will look at these young men...
```

Rules:

- Timestamps use seconds with one decimal place. `[14.5-24.3]`, not `[0:14-0:24]`.
- The window at the start of the caption is the segment's own window.
- You may split the window into smaller stamped ranges inside the caption. Every
  one of them must sit **inside** the outer window.
- Both `[0.0-8.5][Speaker 1]:` and `[0.0 - 8.5] [Speaker 1]:` appear in
  pass-grade work. Pick one and stay consistent across the task.

## Speaker Numbering

Number speakers by the order they **first speak in the whole video**. Speaker 1
is whoever talks first. That number belongs to that person for the entire task,
even if they do not speak again for four minutes.

Anyone who produces intelligible words gets a number, including:

- a voiceover or narrator who is never on screen
- a loudspeaker or tannoy announcement
- a crowd chanting words in unison
- a singer
- a talking toy

Background chatter where you cannot make out words or separate people is **not**
a speaker. That is ambience, and it goes in the Audio caption.

When a returning speaker comes back later in the video, reuse their number. When
a new voice arrives, give them the next number up.

If two people speak at once, give each their own line, with overlapping stamps:

```text
[6.7 - 8.3] [Speaker 1]: Tan Tana Done!
[6.7 - 8.3] [Speaker 2]: Tan Tana Done!
```

Speaker numbering is a common failure. In the missing-speech audit the reviewer
had to write out the whole cast by hand for the worker — "s1 main host guy, s2
commercial guy, s3 interviewer, s4 Elon, s5 Female informer, s6 Elon coworker,
s7 Man asking question". Build that list yourself, on your first listen, before
you write anything.

## Caption 1 — Transcription

Verbatim means verbatim. Type what came out of the mouth, not what the sentence
was trying to be.

**Keep:**

- Filler words. `um`, `uh`, `you know`, `I mean` — all stay.
- Repeats and false starts. `I, I think`, `that- that weekend`, `or- or- or`.
- Cut-off words. Use a hyphen for a word that was never finished: `we shou-`,
  `th- the reports`. Do **not** use an ellipsis for a cut-off word.
- Ordinary swear words, spelled as spoken.

**Do not:**

- Tidy grammar, finish sentences, or fix a mistake the speaker made.
- Guess a word you did not catch. That is what `((unintelligible))` is for.
- Merge two speakers into one turn.

Real examples from pass-grade tasks:

```text
[0.0-8.5][Speaker 1]: So for me, a lot of people will look at these young men or- or- or
the West Indies that did it in 2016 and disparage their character.
```

```text
[00.0 - 06.3] [Speaker 1]: But I wonder what you make of um the White House sending
Mike Pompeo to meet with the North Korean leader himself.
```

```text
[35.4 - 42.2] [Speaker 2]: You know, th- the reports I saw, he did raise issues such as
there's three Americans, uh uh imprisoned uh unfairly in North Korea.
```

And the assessment's model answer for a false start with a filler:

```text
[1.0-5.0][Speaker 1]: I, I think we shou- um, we should wait. [5.0-6.0][Speaker 2]: Yeah.
```

Note what that one gets right: `shou-` with a hyphen because the word was never
completed, the `um` kept, and the second voice given its own stamp and number
even though it only says one word off screen.

### Several turns in one window

A segment often holds a back-and-forth. Stack the turns, each with its own stamp
and tag, and let them overlap where people talk over each other:

```text
[43.4 - 56.5] [Speaker 2]: But I think it's that slow, gradual process towards getting
the summit organized. You know, we need a date for it, we need a location for it, and
clearly you have to have meetings for it to move forward. So I don't think that- that
weekend, that Easter Sunday visit was necessarily about getting a concession right there.
[43.4 - 56.5] [Speaker 3]: Mhm. Right. Right.
[56.4 - 56.8] [Speaker 1]: But But.
```

### Silence inside a talking segment

If part of a speech segment has no talking, stamp it and tag it. Do not leave it
uncovered:

```text
[14.0-23.8][Speaker 1]: The emphasis of spirit of cricket should be one for the
non-striker, the batsman, to stay in his ground until the release of the ball, to be
watching.
[23.8-27.5]: ((No speech present))
```

## The Three Tags

These are the only tags for missing or unusable speech, and each means one exact
thing. Getting them mixed up is a graded error.

| Tag | Means | Use when |
|---|---|---|
| `((No speech present))` | Nobody is speaking | Silence, or only music and noise |
| `((unintelligible))` | Words are spoken, you cannot make them out | Mumbling, crosstalk, drowned out |
| `((Non-English speech))` | Words are spoken, in another language | A passage you can hear is not English |

Never guess between them. `((No speech present))` on a segment where someone is
mumbling is a failure — the transcription audit flagged exactly that: *"label
should mention speech as unintelligible, not 'no speech'"*.

Tag only the part that needs it. `((unintelligible))` can sit mid-sentence:

```text
[64.0-69.0][Speaker 2]: Zack, look. ((unintelligible)) tattoos on the tongue.
```

**Simple non-English gets transcribed, not tagged.** If a lay viewer would
understand it, or the context makes it plain, write the words. The assessment's
model answer for a cook naming a dish is:

```text
[0.0 – 2.7][Speaker 1]: Brinjal and potato rasa.
```

not `((Non-English language))`. A whole video that is mostly non-English is a
different matter — that is a skip. See `../references/skip-flag-routing.md`.

## Songs and Lyrics

A song splits across both tracks:

- **Audible lyrics → Speech Caption 1**, transcribed, with the singer given a
  speaker number.
- **How the singing sounds → Speech Caption 2** — tempo, tone, drawn-out words.
- **The instrumental music → Visual+Audio Caption 2** (the Audio caption).

The family-entertainment golden example transcribes 129 seconds of theme song as
one Speaker 1 turn:

```text
[11.0 - 140.0][Speaker 1]: We're a family just like you, and we know just what to do,
yeah. Have a good time, let's have a good time. [...] Water parks and Christmas trees as
we share each memory, oh.
```

with the matching characteristics caption:

```text
[11.0 - 140.0] Speaker 1 is a male with a standard US accent. He speaks in a melodic,
rhythmic, and energetic singing tone. His volume is high and constant. He maintains a
fast, upbeat pace consistent with pop music and emphasizes the words "time" and "family"
at the start of various lyrical lines. Throughout the song, briefly pauses at [59.7],
[88.7], and [94.0], and emphasizes "He" after "Auntie," "Bee" after "Michael's," and
"ice cream."
```

If the lyrics genuinely cannot be made out, that is `((unintelligible))` on the
Speech track, and the music still gets described on the Audio track.

## Swearing and Slurs

- **Ordinary swear words are transcribed exactly as spoken**, like any other
  word. They do not make a video a skip.
- Put the **Partially Un-annotatable** flag on the task when there is a stray
  swear word or an isolated explicit stretch. The flag applies to the whole
  task — you cannot flag one word.
- **Hateful slurs are the exception. Do not write them out.** The Autochecker
  runs a hateful/offensive language check on captions, and auditors mark such
  tasks "partially un-annotatable due to derogatory term".

## Caption 2 — Speech Characteristics

This caption describes the *sound* of the speech. Cover, for each speaker in the
window:

- **Voice and accent** — "a male voice with an American accent", "a feminine
  standard Indian English accent", "a Jamaican accent", "a New Zealand accent".
- **Tone** — firm, playful, informative, emphatic, hesitant, acknowledging.
- **Pace** — steady, rushed, deliberate, moderately fast, quick.
- **Volume** — moderate, low, loud, "lower than Speaker 1".
- **Emphasis**, with a timestamp and the actual word quoted.
- **Pauses, breaths, stutters and fillers**, with timestamps.
- **Pitch changes**, when they carry meaning.

Every speaker who talks in the window gets described. When several speak, give
each their own stamped line:

```text
[8.3-24.1] Speaker 1 has a male voice with an American accent. His voice starts off soft
before picking up volume, stretching out the words 'looky there' and 'hey' before
emphasizing big time. [26.6-37.2] Speaker 2 has a male voice with a Scottish accent. His
voice is soft and steady, emphasizing the word Finally. [37.2-38.2] Speaker 3 has a male
voice that is soft and calm and an Irish accent.
```

More pass-grade samples, to copy the shape of:

```text
[0.0-8.5] Speaker 1 is a male speaking with a Jamaican accent. His tone is firm, his pace
is steady, and his volume is moderate. At [1.3] he emphasizes the words "me" and
"disparage their character". At [2.9-3.3] he briefly stutters, repeating "or."
```

```text
[00.0 - 06.3] Speaker 1 has a female voice with a standard American accent with a
moderate-low volume. She speaks in a direct and concise tone. At [03.0 - 04.0] speaker 1
slows her pace as she says "Mike Pompeo". At [04.1] speaker 1 takes a breath. She uses a
filler word "um".
```

```text
[43.4 - 56.5] Speaker 3 has a male voice with an American accent, he uses an
acknowledging tone, and he interrupts 3 times in a low volume.
```

When tone changes the meaning of what was said — sarcasm, or heavy stress on one
word — capturing it here is **mandatory**, not optional.

When nobody speaks, Caption 2 carries the tag too:

```text
[49.4-54.6]: ((No speech present))
```

## What Never Goes in Caption 2

The assessment's Q14 lists these as graded errors. All four came from one short
caption.

| Wrong | Why | Right |
|---|---|---|
| "The speaker is German" | That is a nationality, and you cannot hear it | "has a German accent" |
| "as he raises his arm" | Visual reference — belongs in the Visual caption | Drop it |
| "he laughs at [25.0]" | A laugh is not speech — it belongs in the Audio caption | "his tone turns brighter" |
| "The speaker..." | Speakers are numbered | "Speaker 1..." |

Judge an accent from the speech only. Never from clothing, setting, a flag on a
wall, or the topic being discussed.

## Worked Segments

A complete pass-grade Speech segment, both captions, from the cricket example:

```text
Caption 1 · Transcription
[37.0-47.9][Speaker 1]: Look at this. Look at how this young man now, Harris, is staying
in his ground, and he could even extend a little bit more and be in a more- athletic
position.

Caption 2 · Speech characteristics
[37.0-47.9] Speaker 1 speaks in a firm, emphatic tone with a steady pace and moderate
volume. At [37.2] he emphasizes the word "this". At [43.3] he emphasizes the word "more."
At [40.2] and [44.5] he pauses briefly before continuing. He stutters briefly at [46.0].
```

Read across those two. The `more-` hyphen in Caption 1 is the same stutter that
Caption 2 stamps at `[46.0]`. The two captions agree with each other. That is
what an auditor checks.

Another, where two people say the same words at once:

```text
Caption 1 · Transcription
[0.0 - 6.7] [Speaker 1]: Hey everyone! We are the Tandon Sisters, and we're coming on
Sanjeev Kapoor Khazana with a brand new fun show called
[6.7 - 8.3] [Speaker 1]: Tan Tana Done!
[6.7 - 8.3] [Speaker 2]: Tan Tana Done!

Caption 2 · Speech characteristics
[0.0 - 8.3]: Speaker 1 and Speaker 2 speak with a feminine standard Indian English
accent. Speaker 1 and Speaker 2 speak in an enthusiastic, casual, and friendly manner.
Speaker 1 holds the word "called"
Speaker 1 speaks in a slightly rushed pace, a moderate volume, and an enthusiastic tone.
Speaker 2 speaks in a steady pace, a moderate volume, and an enthusiastic tone.
```

## Failures to Avoid

Each of these failed a real audit. Full write-ups are in
`../references/common-errors.md`.

- **Misheard words.** A worker wrote "and it is a pure wit gun." The speaker said
  "witch hunt". Listen again to anything that does not make sense as a sentence.
- **Two speakers merged into one.** A worker wrote
  `[83.5-87.9][Speaker 1]: Ohhh, that's naughty. But very nice.` It was two
  people: Speaker 1 says "Ohhh, that's naughty" and Speaker 2 says "But very
  nice". The auditor had to split it by hand.
- **Half the window left untranscribed.** A caption covered `[65.0 - 140.0]` but
  the transcript stopped at 91.0. The audit note: *"Segment from [91.0-140.0] is
  not captioned."*
- **Characteristics that miss what is audibly there.** One caption was failed for
  missing a pause after "property", missing the stutter in "it's...uh something",
  and missing the emphasis on "another" — in a single 13-second segment. Listen
  for pauses, stutters, fillers, and stress on individual words every time.
- **Claiming no non-verbals when there are some.** "No stutters, sighing,
  laughter, or other non-verbal sounds are present" is a claim, and auditors
  check it. Only write it when it is true.
