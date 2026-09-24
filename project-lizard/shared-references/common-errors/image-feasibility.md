# Image Feasibility

**Definition**: The image must be both clear and usable.

- **Clear**: Legible enough to support the question. Text, numbers, and visual features required to answer must be readable without ambiguity from poor resolution, pixelation, or blurriness.
- **Usable**: Workable enough to support high-quality annotation. Only skip an image if it is truly unusable — force nothing.

## ✅ Pass
1. All details needed to answer are sharp and clearly legible.
2. The annotator correctly skips an unworkable image, or validly creates an annotation because the image is complex and workable.

## ❌ Fail
1. The image is too blurry, pixelated, or distorted to confidently read the text, numbers, or visual features required.
2. The annotator forces an annotation on an image that should have been skipped.

## Skip Criteria (Shared)
- Generic portraits, movie posters.
- Overly simple scenes with no puzzle/reasoning structure.
- Images with extremely disruptive watermarking (covering the entire image or obscuring the prompt's subject).
- Unreadable images.
- Toxic/inappropriate content.
- Foreign languages (text in a non-English language — skip even if the rest of the image looks fine).
- Images that require specialized expertise you don't have.

## VQA-Specific Skip Criteria
- Flyers, posters, and anything without a table, chart, or graph will rarely support a strong VQA prompt. Skip if there is genuinely no data to reason over.

## BabyVision-Specific Skip Criteria
- Clustered color dot images (auto-skip).
- Chart-heavy or text-heavy images (this is VQA, not BV).
- Generic photos with no puzzle structure (no grid, maze, pattern, shadow, transformation, or path).

## Where to Find the Full Unusable Image Lists
The full lists of skip/unusable image categories live on the review-an-image pages:
- VQA 1: Review an Image — unusable image categories for VQA tasks.
- BV 1: Review an Image — unusable image categories for BabyVision tasks.

## VQA Examples

### Example 1 — Unclear Image
**Prompt**: "What is the cost to acquire a customer for Channel 1 in February? Give the answer rounded to 1 decimal place (e.g., 1.5)."
**How to correct**: Skip this image — the chart is too blurry to read the February value with any confidence.

### Example 2 — Unusable Image (No Structure)
**Prompt**: "What quadrant of the picture has the most dense hot pink coloring? Answer with a single letter (e.g., C). A. Top left  B. Bottom left  C. Top right  D. Bottom right"
**How to correct**: Skip this image — it has no meaningful structure to reason about and the judgment is subjective.

## BabyVision Examples

### Example — Unusable Image with a Trivial Question
**Prompt**: "Look at the top left towards the man's hand. How many fingers are visible? Curled fingers are okay as long as they are visible. Answer with a single integer (e.g., 5)." → Answer: 4
**How to correct**: Skip this image — it's a candid party photo with no reasoning primitive (matching, path tracking, spatial transform, pattern completion), and counting fingers in the corner is trivial extraction rather than reasoning.

## Key Principle
Do not force an annotation on an unworkable image. Skip only when the image is truly unusable — but do not hesitate to skip when it is. Skipping is a last resort, not a shortcut.
