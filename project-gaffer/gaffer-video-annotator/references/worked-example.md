# Worked Example — A Mini Task That Passed

A complete 1-minute qualifying task that reached **zero Autochecker errors**,
with the eleven flags it collected on the way and what fixed each one.

Source video: `8t4TCfIFNAs`, "Why We've Skipped Some Uploads", 94.34s. Mini task,
so the graded window is the **first 60 seconds**.

## Contents

- [The Shape of the Answer](#the-shape-of-the-answer)
- [Speech Track](#speech-track)
- [Visual+Audio Track](#visualaudio-track)
- [Every Flag It Collected](#every-flag-it-collected)
- [What This Teaches](#what-this-teaches)

## The Shape of the Answer

Eight rows total. Both tracks touch end to end, both stop at 60.0, nothing over
40s.

| Id | Track | Start | End | Span |
|---|---|---|---|---|
| 1 | Speech | 0 | 4.56 | 4.56s |
| 2 | Speech | 4.56 | 40.7 | 36.14s |
| 3 | Speech | 40.7 | 60.0 | 19.3s |
| 4 | A+V | 0 | 4.67 | 4.67s |
| 5 | A+V | 4.67 | 38.95 | 34.28s |
| 6 | A+V | 38.95 | 48.22 | 9.27s |
| 7 | A+V | 48.22 | 54.5 | 6.28s |
| 8 | A+V | 54.5 | 60.0 | 5.5s |

Note the two tracks break at different times — 40.7 against 38.95 — because
speech breaks on utterances and Visual+Audio breaks on the picture.

## Speech Track

**Row 1 · 0 – 4.56**

```text
C1: [0.0 - 4.56]: ((No speech present))
C2: [0.0 - 4.56]: ((No speech present))
```

**Row 2 · 4.56 – 40.7**

```text
C1: [4.56 - 40.7] [Speaker 1]: Hey everybody, I just wanted to give you guys all a quick
update of why we didn't post a video yesterday or today, and um Owen's been really sick. He's
been in the hospital a little bit, he was in the ER. We'll have some more information about it
coming out in Mommy Monday, but I wanted to let you guys know that's why we haven't been
uploading, because we've just been in the doctor with him. I'm starting to get sick just from
no sleep, because we were up until 7 in the morning with him at the emergency room, and then
the next day we had to get up again and take him again at 9. And so he's doing okay, he's not
better, but you guys can hear in the background he's here getting a breathing treatment.

C2: [4.56 - 40.7] Speaker 1 has a female voice, and speaks in a clear American accent at a
moderate, conversational pace, and moderate volume. She sounds tired and worried but still
explains things calmly. At [12.6], she places emphasis on the words "really sick." At [26.0],
she sounds more worn out when saying "no sleep."
```

Caption 2 scores four of the five categories: tone ("tired and worried… calmly"),
volume ("moderate volume"), pace ("moderate, conversational pace"), and word
emphasis at two stamped moments. "accent" appears here, satisfying the keyword
check for the whole task.

**Row 3 · 40.7 – 60.0**

```text
C1: [40.7 - 47.9] [Speaker 1]: He's drinking some pumped out milk that I pumped out for him,
and he's been taking everything like a champ.
    [47.9 - 57.9]: ((No speech present))
    [57.9 - 60.0] [Speaker 1]: I love you.

C2: [40.7 - 60.0] Speaker 1 continues at the same moderate, conversational pace and moderate
volume. At [47.5], her voice becomes softer and more affectionate when she says "champ."
```

**This row is the one worth studying.** Three paragraphs — speech, silence,
speech — inside one annotation, each with its own head. Keeping them together
rather than splitting into three rows means the single Caption 2 does the
category work for the whole window, and no ten-second hole opens up in coverage.

## Visual+Audio Track

Abbreviated to the structure; the full captions are long.

**Row 4 · 0 – 4.67** — logo build, with every stage stamped at `[0.1]`, `[0.8]`,
`[1.8]`, `[2.6]`, `[3.6]`. On-screen text quoted in the logo's own mixed case:
`"FuN"`, `"FAMiLy"`, `"FAMiLy FuN"`, `"FAMiLy FuN PacK"` — while the corner
watermark, genuinely all-caps, is `"FAMILY FUN PACK"`. Same brand, two
renderings, both copied exactly.
C2: *"A cheerful, upbeat acoustic guitar jingle plays throughout the segment."*

**Row 5 · 4.67 – 38.95** — the woman filming herself. Clothing, jewellery, hair,
eyes, the lanyard with only the readable part quoted, the room behind her, the
watermark. She "moves her mouth" — never "speaks" or "talks", which is
speech-track content.
C2: *"Faint room noise can be heard along with a steady, low hum from a medical
device off-camera."*

**Row 6 · 38.95 – 48.22** — cut to the baby with a bottle, stamped events at
`[44.8]` and `[47.0]`.
C2: *"Faint room noise and the steady, low hum noise continues in the
background."* — carrying the cue forward rather than re-introducing it.

**Row 7 · 48.22 – 54.5** — the nebuliser mask.
C2: *"The same low hum continues, now louder and joined by a constant hissing
sound from the nebulizer."*

**Row 8 · 54.5 – 60.0** — camera pans to an older boy, with stamps at `[55.0]`,
`[56.0]` and `[58.2]`.
C2: *"The loud humming and hissing noise from the nebulizer continues in the
background."*

## Every Flag It Collected

Eleven flags across four rounds, every one structural rather than content.

| Round | Flag | Cause | Fix |
|---|---|---|---|
| 1 | ≥3 of 5 speech categories | Last row had only pace and volume | Merge it into the row carrying the "champ" observation |
| 1 | Row spans ≤40s | One speech row ran 53.3s | Split at 40.7, a real 1.6s pause |
| 1 | No blank captions | A caption left empty | Fill both captions on every row |
| 1 | Cover first 60 seconds | A+V stopped at 54.5 | Add the final row |
| 1 | First/last row at bounds | Same cause | Same fix |
| 1 | No gap >0.1s | A+V row ended 4.49, next began 4.67 | Set End Time to 4.67 |
| 1 | Speaker refs exist in C1 | C2 named Speaker 1, C1 had no tag | Add `[Speaker 1]:` |
| 1 | Paragraph heads | `[57.9 - 60.0]: I love you.` bare | Add `[Speaker 1]:` |
| 2 | Start-time order | Stray empty row defaulting to 0 | Delete it |
| 2 | No blank captions | Same stray row | Same |
| 3 | Events need stamps | A hand entering frame, unstamped | Add `At [58.2],` |

Rounds 3 and 4 also each burned a cycle on a **stale result** — the gap flag kept
appearing after it had been fixed, because the run predated the edit. Check the
"Results as of" banner before treating a flag as real.

## What This Teaches

**Content was never the problem.** Not one flag was about a wrong word, a missed
sound, or an invented detail. Every single one was structure: boundaries,
heads, stamps, coverage. Get the mechanics right and the Autochecker goes quiet.

**Merging beats splitting when a short utterance is involved.** A standalone
`[57.9 - 60.0]` row would need its own three categories for a three-word line.
Folded into the row above, the existing Caption 2 covers it.

**Split on real pauses.** 40.7 was chosen because there is a 1.6-second gap in
the speech there — not because 53.3 ÷ 2 ≈ 27. Boundaries at natural breaks
survive audit; arbitrary ones invite comment.

**Fix one thing at a time and read the banner.** Eleven flags took four rounds,
and two of those rounds were spent on errors that no longer existed.
