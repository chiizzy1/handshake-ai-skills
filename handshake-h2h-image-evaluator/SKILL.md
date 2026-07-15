---
name: handshake-h2h-image-evaluator
description: Evaluate Handshake H2H, Text-to-Image, and T2I Magnifier Pairwise image comparison tasks. Use when Codex must compare two AI-generated images from the same text prompt across Overall Preference, Instruction Following, Visual Quality, and Absence of AI Artifacts; when task UI says H2H, T2I, text-to-image-compare, t2i-magnifier-pairwise, magnifier pairwise, or asks which image better follows a prompt.
---

# Handshake H2H Image Evaluator

## Core Rule

**NEVER BE AGREEABLE FOR ITS OWN SAKE.** Always verify things independently. Do not rely blindly on user claims or assumptions, as the user might be wrong or missing information. If a task requires factual knowledge (like physics, anatomy, or astronomy), browse the web or use external tools to verify the ground truth before evaluating.

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
- **Focus on the Big Picture:** Focus on overarching structural/physical flaws (like inconsistent physics, broken spatial logic, or impossible lighting) rather than nitpicking generic "AI textures" or plastic artifacts.
- **Style:** Keep it concise, naturally flowing, and simple. Do not use overly polished English. Write like an average human being casually explaining something to a friend.
- **Vocabulary:** Do NOT use big academic words or long chains of adjectives (e.g., "mushy, abstract, distorted blob"). Keep the vocabulary basic and direct.
- **Punctuation:** Do not use em dashes. Do not use colons (`:`) unless it's for an actual list. Use commas, periods, or "and" instead.
- **Phrasing:** Avoid phrases like "Upon review of," "demonstrates superior," "holistic assessment," "semantic elements," "rendering the central face," or "demonstrating a severe lack of."
- **Examples of Good vs. Bad Tone:**
  - *Bad (Too detailed/AI-obsessed):* "Response B is the clear winner because it maintains physically consistent weather logic. Response A hallucinates impossible horizontal rain streaks..."
  - *Good (Punchy and focused):* "Response B is much better because it shows a physically consistent weather logic. Response A weather looks more like a painting."
  - *Bad (Academic/Adjective Chains):* "Response A fails the prompt entirely by rendering the central face as a mushy, abstract, distorted blob, demonstrating a severe lack of detail and clarity."
  - *Good (Average Human):* "Response B is much better because it actually made a realistic face that blends well with the shapes. Response A just turned the face into a blurry mess."
  - *Bad (Robotic/Stiff):* "Response A is much better because it shows a realistic, physically accurate wall sit with normal human proportions. Response B totally failed on the body structure, generating a terrifying mess of extra hands and melted fingers."
  - *Good (Casual/Natural):* "Response A is much better because she actually looks like a normal person doing a wall sit. Response B gave the girl a bunch of extra hands and totally messed up her arms."
  - *Bad (Too simple, misses key visual observations):* "Response B is much better because it looks like a real photograph with natural water reflections. Response A totally messed up the physics by copy-pasting the exact same cloud reflection onto multiple different levels of water."
  - *Good (Descriptive but conversational):* "Response B is much better because it looks like a real photograph with natural water reflections. Response A has clearly visible AI artifacts like perfectly even sized terraces with the exact same cloud reflections, and a filter effect that makes it look more like a painting than a real image."
  - *Bad (Overly Analytical):* "Response A is much better because it provides a sharp, high-resolution image with crisp text. Response B has the exact same layout but is blurry, pixelated, and looks heavily compressed."
  - *Good (User Example):* "Both responses correctly show the Venn relationship between Physics, Chemistry, and Biology and also correctly label their overlaps, but Response A is slightly better because it's much clearer and easier to read than Response B which is a little blurry."
  - *Bad (Wordy/Over-explaining):* "Response B is much better because it provides clean, organized labels that actually point to the correct parts of the train. Response A is a confusing mess where the lines cross over each other and point to the completely wrong objects."
  - *Good (Punchy/Direct):* "Response B is much better because its labels actually point to the correct parts of the train. Response A labels point to completely wrong objects."
  - *Bad (Robotic/Academic Text Analysis):* "Response B is much better because it generated the complex text and table structure flawlessly. Response A failed because it has obvious AI text hallucinations, completely jumbling the KEYBOARD NAME header and messing up several letters in the table cells."
  - *Good (Conversational Text Analysis):* "Response B is much better because it's writings are clear and easy to read and words spelled corectly. Response A has garbled spellings like in the first column header and in the sections of the the table."

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

### 4. Cross-Panel & Asset Consistency (Comics/Multi-Shot)
When analyzing a comic page or an image with multiple views of the same subject, consistency is the highest priority. 
- **Character Traits:** Does the character retain the exact same skin tone, hair style, and facial structure across every single panel? (e.g., A tan character suddenly having a pale white hand in one panel is a massive consistency failure).
- **Clothing & Props:** Do the clothes, weapons, or surrounding props maintain their structural logic, colors, and textures across different shots?

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

## Final Checklist

- Prompt requirements were listed mentally.
- Both images were zoomed/inspected.
- Counts, relationships, text, and style were checked.
- Visual Quality and AI Artifacts were not mixed up.
- Ties were avoided unless truly justified.
- Macro-level spatial logic and anatomy were verified before grading fine details.
- Final wording is specific, plain, and image-grounded.
