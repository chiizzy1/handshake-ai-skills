---
name: handshake-critique-rework
description: Evaluate and rework Handshake Critique Rework tasks. Use when the agent must audit another reviewer's critique of an AI-generated image, score critique quality from 1 to 5, decide whether it is worth fixing, correct markers/dots/notes/missed instructions/overall feedback, or apply coverage and accuracy rules for critique markers.
---

# Handshake Critique Rework

## What This Task Is

In Critique Rework you audit someone else's critique of an AI-generated image — the markers, notes, and feedback another reviewer left. You read the whole critique, rate its quality from 1 to 5, then decide whether it is worth fixing. If it has correctable problems, you edit it in place; if it is already good or too broken to salvage, you submit your grade and move on.

You are grading on two things at once: how completely the reviewer caught the real AI tells (**coverage**), and how accurate their markers are — right spot, real defect, specific description (**accuracy**).

> **You are auditing, not redoing.** You are NOT re-doing the critique from scratch. You are auditing someone else's work: confirming what is right, fixing what is wrong, and filling obvious gaps.

## Source of Truth

Use `HANDSHAKE-AI/pdfs/handshake -- Critique Rework.pdf` as the canonical reference.

Before working a live Critique Rework task, read `references/rubric.md` for the full rubric, all 7 worked examples with Good/Bad comparisons, quiz calibration, and the rework cheat sheet.

## The Three Steps

Every item moves through the same flow.

### Step 1 — Read & Grade

Read the existing critique top to bottom, then rate it 1–5. You cannot continue without a rating.

**Tip:** Read the entire critique before you touch the rating — a strong opening marker does not guarantee strong coverage.

### Step 2 — Worth Fixing?

Decide whether the critique has problems worth correcting.

**Yes — fix it.** Open the editor and rework when any of these apply:
- Notes are vague but describe a real defect ("hand looks wrong") → rewrite them.
- A dot is placed near a defect instead of on it → move it.
- A dot is on normal content or a harmless extra → delete it.
- An obvious real tell the reviewer missed → add it.
- Prompt content is clearly missing from the image but was not flagged → drag it.

**No — submit grade & continue.** Record your grade as-is when either of these is true:
- The critique is already good (a clean 4–5) — nothing meaningful to improve. Do not invent edits.
- The critique is too broken to salvage (almost every dot is invented). Grade it low (1–2) and move on — a full redo is not your job.

Either way, your grade and feedback are still recorded — the critique is just kept as-is.

### Step 3 — Rework

Only if you chose Yes — edit the critique in place. Fix notes, move/add/delete dots, flag missed prompt content, adjust overall feedback, then submit.

## What A Critique Is Made Of

The original reviewer was marking everything that gives an image away as AI-generated. Their critique has three parts — and you will see all three.

1. **Point markers** — dots placed on specific visible defects, each with a note.
2. **Missed instructions** — prompt content that the generated image failed to depict.
3. **Overall image feedback** — whole-image notes (grain, palette, mood) that have no single precise location.

## Two Grading Dimensions

A critique can fail in two opposite ways. Judge both.

### Coverage — Did They Catch the Real Tells?

Most AI images have many tells — obvious and subtle. A strong critique finds them. If a critique marks 2 things on an image riddled with broken hands, garbled text, and impossible shadows, that is a **coverage failure** even if those 2 marks are perfect.

### Accuracy — Are the Marks Any Good?

Each marker should be:
1. A real defect.
2. Placed on the exact spot.
3. Described specifically.

Invented dots, dots near-but-not-on the defect, and vague notes ("looks weird") are all **accuracy failures**.

## Point Count Does Not Decide the Grade

A 6-dot critique can be a 4, and a 16-dot one can be a 2. Use this approach:

1. Start from precision (how many marks are real and on the exact defect): ~9/10 → 5, ~8/10 → 4, ~7/10 → 3, below → 2
2. Then dock for coverage (obvious tells missed).
3. Floor at 1 if the marks are mostly invented or coverage collapses.

## Rating Scale (1–5)

| Rating | Label | What It Means |
|--------|-------|---------------|
| 5 | Exceptional | Catches essentially all the tells with precise, well-placed marks. One tiny slip is acceptable. ~9/10 marks real & on-target. |
| 4 | Strong | ~8/10 marks genuine & on-target; obvious tells all caught; only minor slips. |
| 3 | Acceptable | Core defects mostly found, but several dots imprecise/under-described or some tells missed. ~7/10, real gap on one axis. |
| 2 | Weak | Notes not tied to visible defects, dots off-target, or obvious tells missed. Below ~7/10 and/or several false positives. |
| 1 | Unacceptable | Most marks invented or wrong, and/or nearly all obvious tells missed. |

## The 7 Marker Rules (Good vs. Bad)

These are the core standards you enforce when auditing each mark. Each rule has a Good fix and a Bad (mistake) outcome. See `references/rubric.md` for the full image-by-image breakdown.

### Rule 1 — Name the exact defect, not a vague quality
- **Input:** A dot on the orca's eye, noted only "doesn't show detail of the eye and is blurry." Underwater, some softness is normal — this does not say what is actually wrong.
- **Good fix:** Rewrite to the real defect: "the eye is missing" (or "misshapen / doubled"). State what is wrong, specifically.
- **Bad:** Leave "blurry / no detail."
- **Why:** A description must name the defect; "blurry" could be normal. The reviewer docked this submission for vague notes like this one.

### Rule 2 — Put the dot on the defect it describes
- **Input:** The note describes a text defect ("two words blended into one"), but the dot sits on the flowers/post — the garbled sign text is off to the side.
- **Good fix:** Move the dot directly onto the garbled lettering it describes.
- **Bad:** Leave it on the post, near but not on the text.
- **Why:** A point's coordinates must land on the defect it describes — a dot near but not on the text is an accuracy error.

### Rule 3 — A point needs a defect to sit on — not empty space
- **Input:** A dot floats on open water with the note "quality in the water is grainy." There is no specific defect at that spot.
- **Good fix:** Remove it. Whole-image graininess belongs in overall feedback (or skip the item) — not a point on empty water.
- **Bad:** Keep the dot floating on the empty water.
- **Why:** Point coordinates are meaningless on empty space; image-wide qualities go in overall feedback, not a point.

### Rule 4 — Mark real defects, not invented ones
- **Input:** The note claims the lightning is "unnaturally smooth and straight" — but the bolt in the image is clearly jagged and forked. The claim is contradicted by the image.
- **Good fix:** Delete the dot. If a mark's claim is not actually true in the image, it is a false positive.
- **Bad:** Keep it because it sounds like a plausible AI tell.
- **Why:** Invented defects — claims the image disproves — are the signature of a 1-rated critique. Check every claim against the pixels.

### Rule 5 — Normal, plausible things are not tells
- **Input:** A dot marks a loaf of bread as a defect ("weird-shaped bread"). A normal loaf on a counter is not a rendering flaw.
- **Good fix:** Delete it — unless the bread is actually malformed (melted, fused, or with a garbled label). Plausible everyday objects are not tells.
- **Bad:** Keep it because the bread "looks a bit odd."
- **Why:** Marking normal or plausible content is a precision error. The reviewer ruled this point invalid for exactly that reason.

### Rule 6 — A critique is a statement, not a question
- **Input:** Point note: "Where is his thumb? It should be visible here." It is written as a question rather than a statement of the defect.
- **Good fix:** Rewrite as a defect statement: "The thumb is missing — only four fingers are visible."
- **Bad:** Leave the question as-is.
- **Why:** A critique must state the defect plainly to be a clean training signal. The reviewer flagged question-form notes like this.

### Rule 7 — One dot per garbled block — not one per letter/object
- **Input:** Four separate dots sit on the same milk carton's malformed text — two on the side label, two on the top panel — each noted "malformed text."
- **Good fix:** Collapse to one dot at the center of the garbled text block. Genuinely separate signs each still get their own single dot.
- **Bad:** Keep all four dots on the one carton.
- **Why:** Several dots on one object's text is double-marking — it inflates the count without adding signal.

## Marker Placement Standard

**Where the dot goes** — on the specific defect, not the center of the surrounding object:

- Six-fingered hand → on the extra finger, not the palm.
- Misspelled sign → on the misspelled word; if many letters are garbled, one dot at the center of the word (not one per letter).
- Missing month on a chart axis → where the month should appear.
- A whole face that reads as AI with no single broken feature → center of the face, explained in the note.

## Rework Checklist (6 Items)

When reworking, work through each of these actions:

1. **Fix a note** — click a marker (list or image) and rewrite its text to name what is wrong, specifically.
2. **Move a dot** — switch to Point mode and drag the dot onto the exact defect.
3. **Delete a dot** — select it and use the trash icon (or Delete key). Remove markers on non-defects.
4. **Add a dot** — in Point mode, click where a real tell was missed. Your added dots appear blue.
5. **Missed instructions** — in the prompt panel, drag across words the image does not depict and add a short note.
6. **Overall feedback** — add or edit whole-image notes. Keep these for things with no single location; do not duplicate point markers here.

## Cheat Sheet — Marker Rules When Reworking

Use this as a quick checklist for every marker:

- [ ] Dot goes on the specific defect — not the center of the surrounding object.
- [ ] Distributed defect (whole garbled word, merged blob) → one dot at its center.
- [ ] Description names what is wrong, specifically — "6 fingers, extra pinky" not "hand looks wrong."
- [ ] No invented tells. A made-up dot on normal content is a precision error — delete it.
- [ ] Extras the prompt was silent about are not defects — unless the extra itself has a tell.

## Skip, Flag, and Clean Images

Three special cases sit outside the normal flow.

- **Skip** — use when you genuinely cannot audit the item (image will not load, prompt is unintelligible, data is broken). Skipping records nothing and moves on.
- **Flag** — use when the item is bad data that should be pulled for everyone (corrupt image, not a real submission).
- **Clean-image critiques** — some source images are genuinely clean (including real-photo honeypots). If the original reviewer correctly found no tells, grade it well. The mistake to catch is the opposite: a reviewer who invented tells on a clean image.

## Hard Gates (Don'ts)

Avoid these common mistakes:

- Do NOT rubber-stamp every critique a 5 without reading it.
- Do NOT delete a marker just because the note is vague — fix the note instead if the defect is real.
- Do NOT add padding dots to "improve" a critique that is already complete.
- Do NOT put point-specific critiques into Overall feedback.
- Do NOT keep a dot because it sounds plausible when the pixels contradict it.
- Do NOT mark normal plausible content as a defect.
- Do NOT grade before checking every existing marker against the image.
- Do NOT give a high grade when obvious defects or missed instructions were ignored.

## Final Checklist

Before submitting, confirm:

- [ ] Existing critique read fully before grading.
- [ ] Each marker checked against pixels.
- [ ] Grade uses both coverage and accuracy.
- [ ] Real defects were not deleted just because notes were vague.
- [ ] Normal plausible content was not marked as a defect.
- [ ] One distributed defect was not over-marked with many dots.
- [ ] Notes name specific defects, not vague qualities.
- [ ] No invented tells remain.
- [ ] Overall feedback is only for image-wide issues.
- [ ] Critiques are statements, not questions.
