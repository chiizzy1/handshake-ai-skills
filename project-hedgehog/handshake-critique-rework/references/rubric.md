# Handshake Critique Rework — Full Rubric & Worked Examples

Use this reference when working Critique Rework tasks. It covers the rating scale, all 7 worked Good-vs-Bad examples from the PDF, calibration quizzes, and the complete marker standard.

## Contents

- [Source](#source)
- [Rating Scale (1–5)](#rating-scale-15)
- [How to Apply the Scale](#how-to-apply-the-scale)
- [Calibration Quiz 1](#calibration-quiz-1)
- [Calibration Quiz 2](#calibration-quiz-2)
- [The 7 Marker Rules — Full Worked Examples](#the-7-marker-rules-full-worked-examples)
- [Marker Placement Standard](#marker-placement-standard)
- [Good Notes vs. Bad Notes](#good-notes-vs-bad-notes)
- [When to Fix vs. When to Skip Fixing](#when-to-fix-vs-when-to-skip-fixing)
- [Skip, Flag, and Clean Images](#skip-flag-and-clean-images)
- [False Positives — Delete These](#false-positives-delete-these)
- [Common Mistakes](#common-mistakes)
- [Rework Checklist (6 actions)](#rework-checklist-6-actions)
- [Final Checklist](#final-checklist)

## Source

`HANDSHAKE-AI/project-hedgehog-pdfs/handshake-Critique Rework.pdf` (Project Hedgehog — https://hedgehog-faq.learn.joinhandshake.com/critique-rework)

If that file cannot be found, this rubric is operative on its own; say that the source PDF was unavailable.

---

## Rating Scale (1–5)

### 5 — Exceptional
Catches essentially all the tells with precise, well-placed marks. One tiny slip is acceptable. About 9/10 marks are real and on-target.

### 4 — Strong
About 8/10 marks are genuine and on-target. Obvious tells are caught. Only minor slips.

### 3 — Acceptable
Core defects are mostly found, but several dots are imprecise, under-described, or some tells are missed. About 7/10 real. A real gap on one axis (coverage or accuracy).

### 2 — Weak
Notes are not tied to visible defects, dots are off-target, obvious tells are missed, or there are several false positives. Below ~7/10.

### 1 — Unacceptable
Most marks are invented or wrong, and/or nearly all obvious tells are missed.

---

## How to Apply the Scale

Point count does not decide the grade. A 6-dot critique can be a 4 and a 16-dot critique can be a 2.

**Step 1:** Start from precision — how many marks are real and on the exact defect?
- ~9/10 → start at 5
- ~8/10 → start at 4
- ~7/10 → start at 3
- below ~7/10 → start at 2

**Step 2:** Dock for coverage — were obvious tells missed?

**Step 3:** Floor at 1 if marks are mostly invented or coverage completely collapses.

---

## Calibration Quiz 1

> A critique has 9 markers. All 9 sit exactly on real defects with clear, specific notes — but the image also has three more obvious tells (a melted hand, a misspelled sign, a floating cup) that the reviewer never marked. How should you rate it?

**Answer:** Around a 3 — accuracy is excellent, but coverage is weak.

- NOT a 5 (every single marker placed is perfect) — that ignores the coverage failure.
- NOT a 1 (missing any tell collapses the grade) — that is too harsh; the placed marks are all correct.

---

## Calibration Quiz 2

> A critique has 4 marks on an underwater orca scene — "shape is blurry", "doesn't show detail", and one dot on empty water for "graininess." None tie to a visible defect. What rating fits?

**Answer:** A 2 — Weak; notes are not tied to visible defects and a dot is on empty water.

- NOT a 4 (it found several issues, so coverage is fine) — finding "issues" that are not real defects is not coverage.
- NOT a 1 (any vague note is automatically Unacceptable) — a 1 requires most marks to be invented or nearly all tells missed; a 2 is the right call here.

---

## The 7 Marker Rules — Full Worked Examples

Each rule below is illustrated with a specific image scenario from the PDF showing the Bad input, the Good fix, and the Bad mistake to avoid.

---

### Rule 1 — Name the exact defect, not a vague quality

**Image:** Underwater orca scene. The dot is placed on the orca's eye.

**Bad input:** Note reads "doesn't show detail of the eye and is blurry." Underwater, some softness is normal for the medium — this note names a quality, not a defect.

**✅ Good fix:** Rewrite the note to state the real defect: "the eye is missing" or "misshapen / doubled." State what is wrong, specifically.

**⚠ Bad mistake:** Leave the note as "blurry / no detail."

**Takeaway:** A description must name the defect. "Blurry" could be normal. Vague quality words do not identify what is actually broken.

---

### Rule 2 — Put the dot on the defect it describes

**Image:** Horse jumping scene at a "SPRING CLASSIC" equestrian event. A banner reads "QUALIFIER" with garbled text. The note says "two words blended into one" — but the dot is placed on the wooden post/flowers to the side, not on the actual garbled lettering.

**Bad input:** The note is about garbled text, but the dot coordinates point to a post, not the text.

**✅ Good fix:** Move the dot directly onto the garbled "QUALIFIER" lettering it describes.

**⚠ Bad mistake:** Leave it on the post, near but not on the text.

**Takeaway:** A point's coordinates must land on the defect it describes. A dot near but not on the text is an accuracy error. The coordinates carry information.

---

### Rule 3 — A point needs a defect to sit on — not empty space

**Image:** Underwater orca scene (same image as Rule 1). A separate dot floats in the middle of open blue water with the note "quality in the water is grainy."

**Bad input:** There is no specific defect at that location. The dot sits on empty water.

**✅ Good fix:** Remove it. Whole-image graininess belongs in overall feedback (or skip the item entirely) — not a point marker placed on empty water.

**⚠ Bad mistake:** Keep the dot floating on the empty water.

**Takeaway:** Point coordinates are meaningless on empty space. Image-wide qualities (grain, noise, palette) go in overall feedback, not a point.

---

### Rule 4 — Mark real defects, not invented ones

**Image:** A dramatic lightning storm with jagged, forked bolts over a rocky landscape. A dot is placed on a lightning bolt with the note "unnaturally smooth and straight."

**Bad input:** The claim says "smooth and straight" — but the bolt in the image is clearly jagged and forked. The claim is directly contradicted by what the pixels show.

**✅ Good fix:** Delete the dot. If a mark's claim is not actually true in the image, it is a false positive.

**⚠ Bad mistake:** Keep it because it sounds like a plausible AI tell.

**Takeaway:** Invented defects — claims the image disproves — are the signature of a 1-rated critique. Always check every claim against the actual pixels before accepting it.

---

### Rule 5 — Normal, plausible things are not tells

**Image:** A man with an umbrella walking past "SHADOW BAKERY." A dot marks a normal-looking loaf of bread in the bakery window as a defect with the note "weird-shaped bread."

**Bad input:** The bread is a normal loaf. It is plausible everyday bakery content, not a rendering flaw.

**✅ Good fix:** Delete it — unless the bread is actually malformed (melted, fused, or with a garbled label). Plausible everyday objects are not tells.

**⚠ Bad mistake:** Keep it because the bread "looks a bit odd."

**Takeaway:** Marking normal or plausible content is a precision error. Unless an object is genuinely malformed, it should not be flagged.

**Other examples of things that are NOT tells:**
- Normal water grain/noise with no specific defect at that spot.
- Extra objects the prompt did not mention, unless the extra itself has a tell.
- Plausible clothing folds.
- Natural camera effects (depth of field blur, lens flare, motion blur).

---

### Rule 6 — A critique is a statement, not a question

**Image:** A basketball player's hand gripping a hoop rim. The hand is clearly missing a thumb — only four fingers are visible. A dot is placed on the hand.

**Bad input:** Note reads "Where is his thumb? It should be visible here." It is phrased as a question, not a statement of the defect.

**✅ Good fix:** Rewrite as a defect statement: "The thumb is missing — only four fingers are visible."

**⚠ Bad mistake:** Leave the question as-is.

**Takeaway:** A critique must state the defect plainly to be a clean training signal. Question-form notes are not specific enough.

---

### Rule 7 — One dot per garbled block — not one per letter/object

**Image:** A cafe counter scene with a "BARISTA EDITION" oat milk carton. Four separate numbered dots (10, 11, 12, 13) are stacked on the same carton's malformed text — two on the side label, two on the top panel — each noted "malformed text."

**Bad input:** Four dots all marking the same single carton's garbled text.

**✅ Good fix:** Collapse to one dot at the center of the garbled text block. Genuinely separate signs (e.g. a menu board AND a product label) each still get their own single dot.

**⚠ Bad mistake:** Keep all four dots on the one carton.

**Takeaway:** Several dots on one object's text is double-marking. It inflates the count without adding signal. One defect = one dot.

---

## Marker Placement Standard

**Where the dot goes** — always on the specific defect, not the center of the surrounding object.

| If the defect is... | Click here |
|---|---|
| Six-fingered hand | On the extra finger, not the palm |
| Misspelled sign | On the misspelled word; if many letters garbled, one dot at center of the word |
| Missing month on chart axis | Where the month should appear |
| Whole AI-looking face, no single broken feature | Center of the face, explained in the note |
| Two objects fused into one shape | Center of the fused region |
| Floating object | On the gap or on the floating object itself |

**Distributed defect** (whole garbled word, merged blob) → one dot at its center. Do not mark every letter of the same garbled word or every part of the same merged blob.

---

## Good Notes vs. Bad Notes

Good notes name the defect specifically. Bad notes use vague quality words.

| ✗ Bad | ✓ Good |
|---|---|
| "Looks weird." | "The right hand has six fingers; the thumb and index finger are fused." |
| "Blurry / no detail." | "The eye is missing from the orca's face." |
| "Bad quality." | "The sign text is garbled; the letters do not form readable words." |
| "Where is his thumb?" | "The thumb is missing — only four fingers are visible." |
| "Hand looks wrong." | "Six fingers — an extra finger between the ring and pinky." |
| "The clock is strange." | "Clock numbers run 1, 2, 13, 4 — out of order and past 12." |

**Rule:** Critique notes should be statements, not questions.

---

## When to Fix vs. When to Skip Fixing

### Fix (Yes) when:
- A note is vague but describes a real defect → rewrite it.
- A dot is near a real defect but off target → move it.
- A dot is on normal content or harmless extra → delete it.
- An obvious real tell was missed → add it.
- Prompt content is clearly missing but was not flagged → add missed instruction.

### Do Not Fix (No) when:
- The critique is already clean and strong (4–5). Do not invent edits.
- The critique is too broken to salvage (1–2). Grade it low and move on.

Either way, your grade is still recorded.

---

## Skip, Flag, and Clean Images

**Skip** — image will not load, prompt is unintelligible, data is broken enough that auditing is impossible.

**Flag** — corrupt image, bad data that should be pulled for everyone.

**Clean images** — some source images are genuinely clean (including real-photo honeypots). If the original reviewer correctly found no tells, grade it well. The mistake to catch is the opposite: a reviewer who invented tells on a clean image.

---

## False Positives — Delete These

Delete marks on normal or plausible content:

- Normal loaf of bread in a bakery.
- Normal water grain/noise with no specific defect at that spot.
- An object the prompt did not mention, unless the extra object itself has a tell.
- Plausible clothing folds.
- Natural camera effects (depth of field blur, lens flare, motion blur).

---

## Common Mistakes

- Rubber-stamping every critique as 5 without reading.
- Deleting a marker because the note is vague when the defect is real. Fix the note instead.
- Adding unnecessary dots to improve a critique that is already complete.
- Moving point-specific critiques into overall feedback.
- Keeping a dot because it sounds plausible when the pixels contradict it.
- Treating normal content as an AI tell.
- Grading high when obvious tells were ignored.

---

## Rework Checklist (6 actions)

When you have chosen to fix a critique, work through each of these:

1. **Fix a note** — click a marker and rewrite its text to name what is wrong, specifically.
2. **Move a dot** — switch to Point mode and drag the dot onto the exact defect.
3. **Delete a dot** — select it and use the trash icon (or Delete key). Remove markers on non-defects.
4. **Add a dot** — in Point mode, click where a real tell was missed. Your added dots appear blue.
5. **Missed instructions** — in the prompt panel, drag across words the image does not depict and add a short note.
6. **Overall feedback** — add or edit whole-image notes. Keep these for things with no single location; do not duplicate point markers here.

---

## Final Checklist

Before submitting any Critique Rework:

- [ ] Existing critique read fully before grading.
- [ ] Each marker checked against pixels.
- [ ] Grade uses both coverage and accuracy.
- [ ] Real defects were not deleted just because notes were vague.
- [ ] Normal plausible content was not marked as a defect.
- [ ] One distributed defect was not over-marked with many dots.
- [ ] Notes name specific defects, not vague qualities.
- [ ] Critiques are statements, not questions.
- [ ] No invented tells remain.
- [ ] Overall feedback is only for image-wide issues.
- [ ] Point-specific critiques are not in overall feedback.
