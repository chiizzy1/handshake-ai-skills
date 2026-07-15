---
name: handshake-evaluator
description: Router and source-of-truth controller for Handshake AI task work. Use when Codex is asked to rate, audit, create, verify, or structure Handshake tasks; when task type is unclear; when working from HANDSHAKE-AI/guidelines.md or HANDSHAKE-AI/pdfs; or when deciding which Handshake task-specific skill/rubric should apply.
---

# Handshake Evaluator

## Core Rule

Use the Handshake PDF for the specific task type as the highest authority. Use `HANDSHAKE-AI/guidelines.md` as a broad working summary only. If the user, this skill, an old answer, or general instinct conflicts with the PDF, follow the PDF.

Do not be agreeable for its own sake. Be cooperative with the user, but be loyal to the Handshake rubric.

Before routing or rating a live task, read `references/task-router.md`.

## Hard Gates

- Do not rate before reading the task prompt, visible media, response text, and rating labels.
- Do not use TELUS rules, labels, or scoring logic on Handshake tasks.
- Do not infer hidden intent when the UI or PDF gives the rule.
- Do not select a tie to avoid a hard call. Use a tie only when the relevant rubric allows it and there is no meaningful visible difference.
- Do not invent image details. If a detail cannot be seen, treat it as unknown.
- Do not let the user's suggested answer control the rating. Check it against the PDF and visible evidence.
- When factual knowledge outside the task is needed, verify it before using it.

## Source Hierarchy

1. The relevant PDF in `HANDSHAKE-AI/pdfs/`, when one exists.
2. The task UI instructions and visible prompt/media for the current item.
3. Task-specific Handshake skill reference files.
4. `HANDSHAKE-AI/guidelines.md`.
5. User preference or prior chat memory.

If a task depends on current real-world facts outside the image or prompt, verify with reliable sources before rating. Do not use outside research to override what the task asks you to judge visually.

## Routing Workflow

1. Read the current task text, visible images/video, prompt, response options, and rating UI labels.
2. Identify the task type from the UI and inputs.
3. Load the matching task-specific Handshake skill and its reference file.
4. If the task type is not covered, use the visible task instructions and PDF if available. Do not force a near-matching skill.
5. Apply the task-specific workflow exactly.
6. Keep the final answer compact and natural unless the user asks for full reasoning.

## Task Type Map

- Text Image To Text ELO / TI2T: use `handshake-ti2t-evaluator`.
- Text-to-Video / T2V / Less AI Generated video artifact benchmark: use `handshake-t2v-evaluator`.
- Text-to-Image / H2H image comparison: use `handshake-h2h-image-evaluator`.
- Image-to-Image, Reference-to-Image, Omni R2I ELO with A/B preference axes: use `handshake-r2i-i2i-evaluator`.
- i2i Pixel Aligned / Project Hedgehog Q1-Q2-Q3 Yes/No edit checks: use `handshake-i2i-pixel-aligned`.
- UD Caption ELO: use `handshake-ud-caption-evaluator`.
- Annot Critic: use `handshake-annot-critic`.
- Critique Rework: use `handshake-critique-rework`.
- Ego Physical Understanding: use `handshake-ego-phys-understanding`.
- Find the Boundary: use `handshake-find-boundary`.
- IG Entity Tagging: use `handshake-ig-entity-tagging`.
- IG Entity Verification: use `handshake-ig-entity-verification`.
- Web Dev Agents / Static Webpage data collection briefs: use `handshake-static-webpage`.
- Text-to-Code ELO / Code Render Comparison: use `handshake-text-to-code-elo-evaluator`.
- Image2Code / Image-to-Code reference-image recreation comparison: use `handshake-image2code-evaluator`.
- Visual Coding / AI Website Generation side-by-side rendered website comparison: use `handshake-visual-coding-evaluator`.
- VideoRL / Long Context VideoRL / Cross-Modal Anchoring: use `handshake-videorl-evaluator`.

## Universal Rules

- Inspect images closely. Zoom into faces, hands, text, edges, labels, markers, and small objects.
- Ground every judgment in visible evidence or task-provided text.
- Score dimensions independently when the UI has multiple dimensions.
- Avoid ties unless the relevant PDF allows them and the compared outputs are genuinely indistinguishable on that axis.
- Do not let visual polish hide instruction failures.
- Do not let one axis bleed into another unless the PDF says the issue belongs on both axes.
- Use plain human comments: short, specific, and tied to image details.
- If the rating UI asks only for selections, provide selections. If it asks for justification, keep it short and evidence-based.

## Overall Preference Eval Task Cues

When evaluating for overall preference, you MUST strictly adhere to these three hard rules:

1. **Look it up if you don't know:** When a prompt involves specialized knowledge (technical, historical, scientific, cultural, anatomical alignment), check a reliable source instead of guessing. Do not make assumptions.
2. **Watch out for the overly-AI look in the edit:** Look for unnaturally crisp edges, flat lighting, plasticky textures, or over-saturated colors in the edited area. An edit can look impressive at first glance but feel artificial on closer look - do not let that initial wow factor automatically win.
3. **Watch out for text issues:** AI edits often add text where it doesn't belong or keep it sharp when it should be soft (far away, off-angle, or out of focus). Cluttered or unnaturally crisp text shouldn't win on visual impact alone.

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

## Final Checklist

Before answering:

- Confirm the task type.
- Confirm the relevant PDF/rubric.
- Confirm no TELUS-specific labels or rules leaked into Handshake work.
- Confirm all visible prompt/media/response content was read.
- Confirm every rating follows the task-specific scale.
- Confirm the final comment names concrete evidence and does not sound padded or overly formal.
