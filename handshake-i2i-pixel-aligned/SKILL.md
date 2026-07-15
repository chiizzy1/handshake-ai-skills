---
name: handshake-i2i-pixel-aligned
description: Evaluate Handshake i2i Pixel Aligned image-edit tasks. Use when a task asks Yes/No questions for Q1 instructions aligned, Q2 pixel aligned, and Q3 no AI slop; when comparing an input/original image against a single edited/target image; when the task says Project Hedgehog, Pixel Aligned, all and only the instructed change, unchanged areas stayed put, or both images free of AI slop.
---

# Handshake I2I Pixel Aligned

## Core Rule

Use `HANDSHAKE-AI/assessments/i2i Pixel Aligned assessment.md` and the I2I PDF guidance as the task source of truth.

Before answering a live Pixel Aligned item, read `references/rubric.md`.

This is not the normal six-axis R2I/I2I ELO task. Do not answer with Overall Preference, Instruction Following, Person ID Preservation, Content Preservation, Visual Quality, or Absence of AI Artifacts unless the UI explicitly asks for those axes.

## Task Shape

Pixel Aligned items usually show:

- Image 1: input / original.
- Image 2: target / edited output.
- One instruction describing the requested edit.
- Three independent Yes/No checks:
  - Q1: instructions aligned.
  - Q2: pixel aligned.
  - Q3: no AI slop.

The main question is: did the edited image make all and only the requested change, keep the untouched parts in exactly the same position, and keep both images clean?

## Mandatory Workflow

1. Read the instruction before judging the images.
2. Identify exactly what was requested and what was not requested.
3. Compare input and target side by side.
4. Scan the whole frame, not only the edited region.
5. Judge Q1, Q2, and Q3 independently.
6. If the prompt asks for a written explanation, keep it brief, concrete, and human.

## The Three Checks

### Q1 - Instructions Aligned

Answer Yes only when the target made all of the requested change and nothing else changed.

Answer No when:

- the requested edit is missing;
- the requested edit is only partly done;
- the edit affects the wrong object, person, or region;
- extra unrequested content was added, removed, recolored, reshaped, or restyled;
- the target changes background, lighting, wall color, clothing, face, body, objects, text, framing, or other content that the instruction did not mention;
- an upscale/restoration invents specific face, hand, text, or object details that were not recoverable from the input, especially when the prompt says not to fabricate.

### Q2 - Pixel Aligned

Answer Yes only when the areas that should stay unchanged line up perfectly with the input.

Answer No when:

- the target is shifted;
- the target is zoomed in or out;
- the target is cropped differently;
- the target is resized, stretched, warped, or perspective-shifted;
- unchanged objects moved relative to the frame;
- the edit causes nearby untouched areas to drift, bend, smear, or change location.

Q2 is about position and alignment, not whether the requested edit happened.

When genuinely unsure on Q2, answer No.

### Q3 - No AI Slop

Answer Yes only when both the input and the target look clean and free of AI slop.

Answer No when either image has:

- extra, missing, fused, or malformed fingers;
- warped faces, eyes, mouths, ears, teeth, or bodies;
- melted or smeared objects;
- plastic skin or over-smoothed textures;
- broken object shapes;
- fake, random, or unreadable text;
- impossible shadows, reflections, or lighting;
- hallucinated details that do not fit the image;
- unnatural hands, utensils, handles, wheels, straps, legs, or small structures.

Q3 checks both images, not only the edited image.

When genuinely unsure on Q3, answer No.

## Hard Gates

- Do not let Q1 success imply Q2 or Q3 success.
- Do not let Q2 success imply Q1 or Q3 success.
- Do not ignore AI slop in the input image.
- Do not ignore unrequested changes because the requested edit looks good.
- Do not ignore shifts, zooms, crops, or resizes because the content looks realistic.
- Do not use normal ELO preference logic on Pixel Aligned Yes/No tasks.
- Do not treat "better looking" as correct if the task requires exact preservation.
- Do not answer Yes on Q2 or Q3 when uncertain.

## Upscale / Restoration / Deblur Rule

For upscale, restoration, deblur, denoise, or enhancement tasks, the target may improve clarity, but it must not invent specific details that the input did not support.

For faces in group photos:

- recovering general clarity is allowed;
- preserving hair shape, face placement, and general identity cues is expected;
- small background faces can remain less detailed if the input does not support more detail;
- inventing new facial features is a failure when the instruction asks for plausible enhancement or forbids fabrication;
- fabricated face details can hurt Q1 and Q3.

For hands and small objects:

- sharper hands must still have plausible finger structure;
- an upscale that creates odd finger counts, fused hands, or unnatural rendering is AI slop;
- making a detail crisper does not excuse hallucinating its structure.

## How to See (Comprehensive Photographic Analysis)

Good image evaluation starts with consistent observation, not personal taste. Replace vague statements like "looks good" or "feels off" with specific, observable photographic claims. Rely on the following three comprehensive pillars to evaluate visual quality and detect generation failures.

### 1. Composition & Framing
Composition is how the elements of an image are arranged. It doesn't have to follow textbook rules perfectly, but it must look purposeful, not accidental.
- **Subject Placement & Rule of Thirds:** Photographers use a 3x3 grid to compose images. Placing a subject on an intersection of these grid lines creates tension and directs the eye naturally. Conversely, if a subject sits dead center with large, empty negative space on both sides, the framing often reads as an accidental AI generation rather than a purposeful composition.
- **Framing Scale:** Does the shot distance (wide, medium, close-up) match what the prompt asked for?
- **Visual Hierarchy:** What draws your eye first? Does it match the intended focus of the prompt?
- **Negative Space:** Is the area around the subject providing intentional "breathing room," or is it unresolved and distractingly empty?

### 2. Focus, Detail & Clarity
Blur is NOT inherently a flaw. Shallow depth of field (a blurred background with a sharp subject) is a legitimate, highly common photographic choice used to isolate a subject.
- **Natural Fall-off vs. AI Artifacts:** The question is whether the blur is intentional and consistent. Does the blur fall off smoothly and logically from the focal plane? In many AI-generated photos, the background is unnaturally sharp when it should be blurred, or it dissolves into soft blur in random, impossible patches with no optical logic.
- **Sharpness:** Is the intended subject actually in focus? Check the edges and fine details (e.g., hair strands, eyelashes, text).
- **Compression & Detail Loss:** Is fine detail (fabric weave, skin pores, grass blades) present where the image resolution should support it? Or is the image "mushy" in ways that look like a generation failure rather than an artistic choice?

### 3. Light & Color Consistency
Light is the most common source of physical inconsistency in AI-generated images.
- **Light Source Direction:** Do all shadows fall consistently from one primary source? Is the light hitting faces, objects, and the background from the exact same angle? (e.g., In "Rembrandt lighting," one side of the face is lit, the other falls into shadow, and everything in the scene must be consistent with that single source).
- **Softness vs. Harshness:** Harsh light (like direct sun) produces sharp, defined shadows. Diffused light (like overcast skies or studio softboxes) produces soft, blended shadow edges. Does the shadow quality logically match the apparent light source?
- **Contrast Check:** Are the highlights "blown out" (pure white with zero detail) or are the shadows "crushed" (pure black, destroying visual information)?
- **Color Temperature:** Is the overall image consistently warm (golden, amber) or cool (blue, gray)? Mixed, clashing color temperatures across a single scene are a massive red flag unless the specific lighting scenario explains it.
- **Saturation Consistency:** Is the color intensity consistent across the image, or do some regions look heavily over-processed while others fall flat?

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
```

## Relationship To Other Handshake Skills

- Use `handshake-r2i-i2i-evaluator` for normal A/B R2I, I2I, or Omni R2I ELO comparison tasks with preference axes.
- Use this skill for Pixel Aligned tasks with Q1/Q2/Q3 Yes/No checks.
- Use shared image foundations from HOW TO SEE, Image Evaluation, and Realism & Artifacts for visual inspection and AI slop detection, but keep the Pixel Aligned scoring logic from this skill.

## Final Checklist

- Instruction read first.
- Requested change identified.
- Unrequested changes checked.
- Input and target compared across the full frame.
- Q1 judged as all and only the requested change.
- Q2 judged as exact unchanged-area alignment.
- Q3 judged on both input and target.
- Unsure Q2/Q3 answered No.
- Final answer matches the UI format.
