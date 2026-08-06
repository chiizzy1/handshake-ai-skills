# Answer Correctness

**Definition**: The rewrite answer must be factually correct based strictly on the image and any constraints in the prompt.

## ✅ Pass
- Accurate, mathematically sound, and aligned with all constraints (rounding, format, spelling).

## ❌ Fail
- Calculation error, misidentification, or formatting violation.

## Use the Validation Tools, but Don't Trust Them Blindly

Both validation tools — the Handshake Shadow Task quality checker and the SuperAnnotate Check My Work (Verify Submission) feature — are useful for catching mistakes you'd otherwise miss. Run them.

**You own the answer, not the tool.** These tools get things wrong. They flag correct answers and miss incorrect ones. A flag is a prompt to look again, not proof of an error — and a clean pass is not proof your answer is right. Always verify the answer yourself against the image and the prompt's constraints.

- Before implementing a suggested change, confirm it's actually correct. If it isn't, ignore it and submit your own answer.
- If you override a tool, be able to state the concrete reason why.

## VQA Examples

### Example — Wrong Calculation and Wrong Format

**Prompt**: "Identify all years in the Historic — GDP Growth Brazil chart in which the value for GDP Growth strictly decreased from the previous year (ignore the first year). What is the result of adding together all percentage values of these years? Answer in a single percentage number (e.g., 25,4%)."

**Rewrite Answer (wrong)**: 7%

**Why it fails**: The rewrite fails the formatting constraint (should use comma as decimal separator per the example format "25,4%") and contains a calculation error. Correct answer: 2,9%.

## BabyVision Examples

### Example — Ambiguous Premise and Incorrect Answer

**Prompt**: "If the green rubber band were removed without changing the positions of the nails, how many nails lie strictly inside of the triangular region formed by the band? Answer as a single number (e.g., 2)."

**Rewrite Answer (given)**: 7

**Why it fails**: The prompt says "triangular region" but the band's pinch point makes the shape closer to a quadrilateral than a triangle. Additionally, 7 doesn't match a careful count of nails inside the enclosed region.

**How to correct**: Rewrite the prompt to reference the region as currently bounded by the band (no removal), and acknowledge that the pinch point makes the shape closer to a quadrilateral. Then recount the nails inside the enclosed region against the image before submitting.

## Key Principle

**Always triple-check the rewrite answer against the image before submitting.** Answer correctness is one of the top audit failure modes. Reviewers: always work through the prompt yourself *before* looking at the rewrite answer, so you can confirm the rewrite is actually correct rather than anchoring to it.
