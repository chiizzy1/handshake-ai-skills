---
name: handshake-annot-critic
description: Evaluate and create annotations for Handshake Annot Critic tasks. Use when the agent must act as an image critic, finding all AI tells/defects in an image based on a prompt, dropping dots exactly on defects, and writing specific notes for each.
---

# Handshake Annot Critic

## What This Task Is

In Annot Critic, you act as a sharp-eyed critic of an AI-generated image. You study the image alongside the prompt that created it and find every "tell" — small mistakes that a real photo or careful human would never make (e.g., garbled text, out-of-order clocks, 6 fingers, floating objects, missing requested items).

For each tell, you must do two things:
1. **Drop a dot** exactly on the defect.
2. **Write one short, specific sentence** saying what is wrong.

Your work is judged equally on **Recall** (catching every single defect, often 8+ in a careful image) and **Precision** (only marking what you are truly sure is wrong, placing dots exactly on the defect, and writing specific factual notes). False positives (marking normal things) hurt your score more than misses.

## Step-by-Step Flow

1. **Read the prompt, then study the image:** The prompt tells you what was requested (counts, named items, spelling). Many tells are only obvious when compared to the prompt.
2. **Scan methodically and zoom in:** Check text/signs, hands/faces/anatomy, counts (fingers/legs/wheels), physics (floating/fused/shadows), and overall quality.
3. **Drop a dot exactly on each defect:** Click the specific defect, not the center of the surrounding object.
4. **Write one specific sentence per dot:** State plainly what is wrong, as a fact. Use the format `[what is wrong] on [which thing]`.
5. **Use special tools when they fit:**
   - *Missing element:* Drag across the words in the prompt panel (no pixel to mark).
   - *Overall feedback:* Use for whole-image qualities (grain, palette) with no single location.
   - *Not AI-generated:* Only if the image genuinely has no tells.
6. **Review every mark:** Ensure each dot is on a real defect, notes are specific, and you haven't marked normal extra content.

## Marker Placement Standard

Always click the specific defect. Zoom in for precision.

- **Face uncanny:** On the face itself, not the center of the person.
- **Clock scrambled:** On the wrong numbers, not the clock center.
- **Sign misspelled:** On the misspelled word (if whole word, center of the word).
- **Fused objects:** On the center of the fused region.
- **Floating object:** On the gap beneath it, or the object itself.
- **Wrong count (e.g., 3-wheeled car):** On the missing/extra part.
- **Shadow/reflection wrong:** On the shadow/reflection, not the object casting it.

## Writing the Note

A useful note names what is wrong and which thing it is on.
- **Good:** "Six fingers — an extra finger between the ring and pinky"
- **Bad (too vague):** "Hand looks wrong"
- **Good:** "Sign reads OPENNING instead of OPENING — double N"
- **Bad:** "Weird text"

Write statements, not questions. Avoid vague words like "blurry", "weird", or "looks off", as these often describe normal camera effects.

## What is NOT a Tell (Do NOT Mark)

- **Unrequested extra content:** If the prompt didn't ask for it and didn't forbid it, the model is free to include it. A dog in a kitchen is fine if not forbidden. Only mark an extra element if that element *itself* has a tell (e.g., the extra dog has 5 legs).
- **Normal plausible objects:** An ordinary apple or loaf of bread is not a tell unless it is actually malformed.
- **Natural camera effects:** Depth of field (blurry background), lens flare, and motion blur are normal photographic effects, not AI tells.

## Common Mistakes to Avoid

- **Stopping too early:** Don't stop at 2 or 3 tells; keep scanning for more.
- **Clicking the object, not the defect:** Putting the dot on the center of a person instead of their broken hand.
- **Padding with guesses:** Adding unsure dots lowers precision.
- **Vague descriptions:** Using "looks weird" instead of naming the defect.
- **Marking extras:** Flagging objects that simply weren't in the prompt but are rendered correctly.
- **Using a dot for a missing item:** Always use the prompt text drag tool for missing requested elements, never a dot on empty space.

## QA Rubric (How You Are Graded)

Your submission will be audited and graded on a 1–5 scale based on coverage (recall) and accuracy (precision):

*   **5 — Exceptional:** Caught essentially all tells (obvious and subtle). ~9/10 marks are real and precisely on-target. No false positives on clean images.
*   **4 — Strong:** Caught all obvious tells, but missed a few subtle ones. ~8/10 marks are genuine and on-target. Minor slips in precision.
*   **3 — Acceptable:** Captured core defects, but has real gaps. ~7/10 marks are genuine. May have a meaningful minority of false positives or vague descriptions.
*   **2 — Weak:** Missed many obvious tells, and/or fewer than 7/10 marks are genuine. High rate of misplaced dots or generic notes.
*   **1 — Unacceptable:** Ignored nearly all real tells, or submitted random/padded dots on normal content. Descriptions provide no useful information.
