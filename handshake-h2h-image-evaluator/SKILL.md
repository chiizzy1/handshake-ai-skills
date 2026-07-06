---
name: handshake-h2h-image-evaluator
description: Evaluate Handshake H2H, Text-to-Image, and T2I Magnifier Pairwise image comparison tasks. Use when Codex must compare two AI-generated images from the same text prompt across Overall Preference, Instruction Following, Visual Quality, and Absence of AI Artifacts; when task UI says H2H, T2I, text-to-image-compare, t2i-magnifier-pairwise, magnifier pairwise, or asks which image better follows a prompt.
---

# Handshake H2H Image Evaluator

## Core Rule

Use the H2H/T2I Handshake PDFs and task-specific markdown guidelines as the source of truth:

- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Text-to-Image (T2I).pdf`
- `HANDSHAKE-AI/pdfs/t2i-magnifier-pairwise/guidelines.md`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Read the prompt before looking at the images.
2. List the prompt requirements: subject, count, attributes, style, lighting, composition, text, relationships, and constraints.
3. Inspect both images closely. Zoom into faces, hands, text, edges, shadows, and small objects.
   - For T2I Magnifier Pairwise tasks, use the magnifier/full-resolution viewer whenever available. The magnifier is not a separate rubric; it is the inspection method for finding small prompt misses, artifact tells, text errors, and quality problems.
4. Rate each axis independently:
   - Overall Preference
   - Instruction Following
   - Visual Quality
   - Absence of AI Artifacts
5. Avoid ties unless both images are genuinely indistinguishable on that axis.
6. Write a short justification with concrete visual evidence.

## Hard Gates

- Do not rate from image appeal alone.
- Do not reward an image for adding dramatic elements that the prompt did not request.
- Do not ignore count, text, or relationship errors because the image looks realistic.
- Do not treat stylization as an artifact when the prompt asks for that style.
- Do not call an axis a tie when one image has a visible prompt, quality, or artifact advantage on that axis.

## Macro Before Micro (The Reality Check)

Before zooming in to grade fine details like text, dates, or textures, you must first perform a macro-level reality check on the scene's composition and physics.

Do not let impressive text generation or highly detailed rendering blind you to fundamentally broken logic. Make specific, observable claims about the spatial relationships:

1. **Physical Relationships:** Does the interaction between subjects make sense? (e.g., Is the mechanic actually close enough to the car to reach it? Are objects floating instead of resting on surfaces?)
2. **Structural Logic:** Does the environment obey physics? (e.g., If a car is raised 6 feet in the air, a mechanic would stand, not lie on a creeper. Are the lift posts actually supporting the car?)
3. **Anatomical Plausibility:** Look at the entire body before the face. Are torsos impossibly long? Do necks bend at broken angles? Are there extra or phantom limbs hidden in the background?

If an image fails the Macro Reality Check (e.g., severe anatomical failure or broken spatial logic), it must be heavily penalized on the Absence of AI Artifacts axis, even if its micro-details (like text or lighting) are flawless.

## Axis Separation

- Instruction Following: prompt compliance only.
- Visual Quality: craft, composition, detail, color, exposure, framing, and seamlessness.
- Absence of AI Artifacts: AI tells such as bad anatomy, waxy skin, garbled text, impossible lighting, distorted objects, and broken logic.
- Overall Preference: holistic, based on what the user wanted. Instruction following usually matters more than small visual polish gaps.

Do not double-penalize artifacts under Visual Quality unless the artifact also harms normal craft quality. Put AI tells in Absence of AI Artifacts.

## Preference Severity

- Use "Strongly Prefer" only when the winning response actually succeeds at the core prompt requirements and the losing response clearly fails, or when the quality gap is so large that the loser is basically unusable.
- If both responses fail a core instruction (wrong count, missing subject, broken data accuracy, wrong layout), cap the overall preference at "Slightly Prefer." The winner is just less bad, not genuinely good.
- "Slightly Prefer" is the right call when both share the same fundamental failure but one handles the rest of the prompt better.

## Presentation Template

Always present evaluations using this three-section structure:

### Section 1: Prompt Analysis
Break down the prompt into its core requirements. List the subject, setting, count, attributes, style, and any constraints. This goes under a `### Prompt Analysis` heading.

### Section 2: Image Analysis
Under a `### Image Analysis` heading, analyze each image separately with bold subheadings (`**Image A:**` and `**Image B:**`). For each image, cover:
- How well it follows the prompt instructions
- Whether the logic/rules of the depicted subject make sense
- Any visual quality issues or AI artifacts spotted

Be specific. Point to exact details, scores, text, positions, or objects you can see.

### Section 3: Final Ratings and Justification
List the ratings cleanly under a `### Final Ratings` heading:
```
- Instruction Following: Response A
- Visual Quality: Response A
- Absence of AI Artifacts: Response A
- Overall Preference: Strongly Prefer A
```

Then write a `### Justification` paragraph. Keep it concise and grounded in what you actually saw.

## Tone Rules

- **Length:** Justifications must always be 1-3 sentences total.
- **Style:** Keep it concise, naturally flowing, and simple. Do not use overly polished English. Write like an average human being stating a reasonable conclusion.
- **Punctuation:** Do not use em dashes. Do not use colons (`:`) unless it's for an actual list. Use commas, periods, or "and" instead.
- **Phrasing:** Avoid phrases like "Upon review of," "demonstrates superior," "holistic assessment," or "semantic elements." It is fine to use casual connectors like "but," "so," "because," and "also."
- **Structure:** Use punchy, single-sentence comparisons when possible (e.g., "Response A is much better because it successfully generated a massive block of text without a single error, while Response B garbled several of the words.").

## Final Checklist

- Prompt requirements were listed mentally.
- Both images were zoomed/inspected.
- Counts, relationships, text, and style were checked.
- Visual Quality and AI Artifacts were not mixed up.
- Ties were avoided unless truly justified.
- Macro-level spatial logic and anatomy were verified before grading fine details.
- Final wording is specific, plain, and image-grounded.
