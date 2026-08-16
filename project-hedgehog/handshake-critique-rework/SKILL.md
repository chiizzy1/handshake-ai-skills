---
name: handshake-critique-rework
description: Evaluate and rework Handshake Critique Rework tasks. Use when the agent must audit another reviewer's critique of an AI-generated image, score critique quality from 1 to 5, decide whether it is worth fixing, correct markers/dots/notes/missed instructions/overall feedback, or apply coverage and accuracy rules for critique markers.
---

# Handshake Critique Rework

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## What This Task Is

In Critique Rework you audit someone else's critique of an AI-generated image — the markers, notes, and feedback another reviewer left. You read the whole critique, rate its quality from 1 to 5, then decide whether it is worth fixing. If it has correctable problems, you edit it in the task platform's editor; if it is already good or too broken to salvage, you submit your grade and move on.

You are grading on two things at once:

- **Coverage** — how completely the reviewer caught the real AI tells. Marking 2 things on an image riddled with broken hands, garbled text, and impossible shadows is a coverage failure even if those 2 marks are perfect.
- **Accuracy** — whether each marker is a real defect, placed on the exact spot, and described specifically. Invented dots, near-miss dots, and vague notes ("looks weird") are accuracy failures.

> **You are auditing, not redoing.** You are NOT re-doing the critique from scratch. You are auditing someone else's work: confirming what is right, fixing what is wrong, and filling obvious gaps.

## Source of Truth

Use `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-Critique Rework.pdf` as the canonical reference.

Before working a live Critique Rework task, read `references/rubric.md` for the full rubric, all 7 worked examples with Good/Bad comparisons, quiz calibration, the marker placement table, the false-positive list, and the rework cheat sheet.

## The Three Steps

### Step 1 — Read & Grade

Read the existing critique top to bottom, then rate it 1–5. You cannot continue without a rating.

**Tip:** Read the entire critique before you touch the rating — a strong opening marker does not guarantee strong coverage.

### Step 2 — Worth Fixing?

**Yes — fix it** when a note is vague but describes a real defect, a dot sits near rather than on a defect, a dot is on normal content, an obvious real tell was missed, or missing prompt content was never flagged.

**No — submit grade & continue** when the critique is already a clean 4–5 (do not invent edits), or it is too broken to salvage (grade 1–2 and move on — a full redo is not your job).

Either way, your grade and feedback are still recorded.

### Step 3 — Rework

Only if you chose Yes. Fix notes, move/add/delete dots, flag missed prompt content, adjust overall feedback, then submit. See the Rework Checklist in `references/rubric.md` for the six editor actions.

**"Edit in place" means editing the critique inside the task platform's UI — not editing any local file.** See Output Format below.

## Rating Scale (1–5)

| Rating | Label | What It Means |
|--------|-------|---------------|
| 5 | Exceptional | Catches essentially all the tells with precise, well-placed marks. One tiny slip is acceptable. ~9/10 marks real & on-target. |
| 4 | Strong | ~8/10 marks genuine & on-target; obvious tells all caught; only minor slips. |
| 3 | Acceptable | Core defects mostly found, but several dots imprecise/under-described or some tells missed. ~7/10, real gap on one axis. |
| 2 | Weak | Notes not tied to visible defects, dots off-target, or obvious tells missed. Below ~7/10 and/or several false positives. |
| 1 | Unacceptable | Most marks invented or wrong, and/or nearly all obvious tells missed. |

Point count does not decide the grade — a 6-dot critique can be a 4 and a 16-dot one can be a 2. Start from precision (~9/10 → 5, ~8/10 → 4, ~7/10 → 3, below → 2), then dock for coverage, then floor at 1 if the marks are mostly invented or coverage collapses.

## What A Critique Is Made Of

1. **Point markers** — dots placed on specific visible defects, each with a note.
2. **Missed instructions** — prompt content that the generated image failed to depict.
3. **Overall image feedback** — whole-image notes (grain, palette, mood) with no single precise location.

## The 7 Marker Rules

These are the standards you enforce on each mark. `references/rubric.md` has the full image-by-image worked examples for every rule.

1. Name the exact defect, not a vague quality.
2. Put the dot on the defect it describes.
3. A point needs a defect to sit on — not empty space.
4. Mark real defects, not invented ones.
5. Normal, plausible things are not tells.
6. A critique is a statement, not a question.
7. One dot per garbled block — not one per letter or object.

## Skip, Flag, and Clean Images

- **Skip** — you genuinely cannot audit the item (image will not load, prompt unintelligible, data broken).
- **Flag** — bad data that should be pulled for everyone (corrupt image, not a real submission).
- **Clean-image critiques** — some source images are genuinely clean (including real-photo honeypots). If the original reviewer correctly found no tells, grade it well. The mistake to catch is a reviewer who invented tells on a clean image.

## Hard Gates (Don'ts)

- Do NOT rubber-stamp every critique a 5 without reading it.
- Do NOT delete a marker just because the note is vague — fix the note instead if the defect is real.
- Do NOT add padding dots to "improve" a critique that is already complete.
- Do NOT put point-specific critiques into Overall feedback.
- Do NOT keep a dot because it sounds plausible when the pixels contradict it.
- Do NOT mark normal plausible content as a defect.
- Do NOT grade before checking every existing marker against the image.
- Do NOT give a high grade when obvious defects or missed instructions were ignored.

## Note Style

Every note you rewrite gets read by whoever audits this task, so phrasing carries weight. The same rules apply to your grade line and fix reason.

**The Persona: someone pointing at the screen and saying what is wrong.**

1. **Name the object, then the defect.** "Left hand, the ring finger and pinky merge into one shape." Not "anatomical issue in the hand region."
2. **State it as a fact.** No "appears to be," "seems like," or "possibly."
3. **One defect per note.** If a note needs the word "and" twice, it is two markers.
4. **Quote text you can read.** If a sign is garbled, write what it actually says.
5. **Short. Periods.** No em dashes, no semicolons in the note text itself.
6. **Neutral.** Describe the defect, do not editorialize about it.
7. **Do not polish a note that already works.** If the original reviewer's wording is specific and correct, leave it alone and say "unchanged."

**Banned phrases:** "anatomical inconsistency," "structural defect," "exhibits," "demonstrates," "artifacting is present," "lacks coherence," "Upon review of."

Good rewrite

`Fix note - Dot 3 - "hand looks off" → "Right hand, the thumb bends backward at the base joint."`

Good grade line

`2 - Weak - the reviewer caught the garbled sign but missed the six fingers and the floating chair, and two dots sit on clean areas.`

Bad

`Fix note - Dot 3 - "hand looks off" → "The subject's manual anatomy demonstrates structural inconsistency."`

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your grade and rework in the chat using the template below; the user applies the edits in the task platform's UI.

```markdown
### Grade
[1-5] — [label] — [one line: what drove the number, coverage and/or accuracy]

### Fix or No Fix
[Fix | No fix] — [one line reason]

### Reworked Markers
(Only when fixing. Omit this section entirely on a no-fix.)
- Fix note — Dot N — [old text] → [rewritten text]
- Move dot — Dot N — [from where] → [onto which exact defect]
- Delete dot — Dot N — [why it is not a real defect]
- Add dot — [where on the image] — [what is wrong, stated as a fact]
- Missed instruction — [prompt words to drag] — [what the image failed to depict]
- Overall feedback — [add/edit whole-image note, or "unchanged"]
```
