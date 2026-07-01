# Handshake H2H / T2I Image Rubric

Use this reference for Handshake text-to-image, H2H image comparison, and T2I Magnifier Pairwise tasks.

## Source PDFs

Primary:

- `handshake-ai-Text-to-Image (T2I).pdf`
- `handshae-ai-Image Evaluation.pdf`
- `t2i-magnifier-pairwise/guidelines.md`

Foundations:

- `handshake-ai-HOW-TO-SEE.pdf`
- `handshake-ai-Realism & Artifacts.pdf`

## Task Shape

The task shows:

- A written prompt.
- Response A image.
- Response B image.
- Four rating axes, usually with choices: Response A, Response B, Both Good, Both Bad.
- Sometimes a magnifier or full-resolution compare viewer for close inspection.

The main question is which image better delivers what the prompt asked for.

## Review Workflow

1. Read the prompt first.
2. Break it into requirements.
3. Inspect A and B at normal size for overall impression.
4. Zoom in on likely failure points:
   - faces
   - hands
   - feet
   - limbs
   - text/signage
   - small objects
   - shadows/reflections
   - repeated patterns
   - edges of inserted or edited-looking objects
   Use the magnifier/full-resolution viewer in T2I Magnifier Pairwise tasks. Treat it as mandatory inspection support, not a fifth rating axis.
5. Score each axis independently.
6. Write a concise justification that cites visible evidence.

## Hard Fail Checks

Check these before choosing a winner:

- Required subject missing.
- Wrong count.
- Wrong action or relationship.
- Requested style ignored.
- Required text unreadable or wrong.
- Major anatomy failure on a visible person or animal.
- Serious face, hand, limb, or object distortion.

Any hard fail can decide the relevant axis even if the image is otherwise attractive.

## Axis 1: Overall Preference

Choose the image that best satisfies the user intent overall.

Use a holistic judgment. There is no fixed formula, but prompt compliance usually matters more than small differences in polish.

Prefer the image that:

- Captures the main subject and action.
- Preserves the intended style and vibe.
- Has fewer serious failures.
- Would be more useful to the person who wrote the prompt.

Do not choose a visually beautiful image if it misses the core request.

## Axis 2: Instruction Following

Judge faithfulness to the written prompt, not beauty.

Check:

- Required subject(s) included.
- Correct number of people/animals/objects.
- Correct attributes: color, material, clothing, species, age, pose, expression.
- Correct style: photo, oil painting, manga, noir, product shot, etc.
- Correct spatial relationships: left/right, above/below, holding, looking at, inside, behind.
- Correct action: jumping, sitting, lifting, pouring, opening, etc.
- Correct text or labels if requested.
- Explicit constraints, such as "do not add text" or "keep background plain."

Common failures:

- Missing required element.
- Wrong count.
- Wrong action or interaction.
- Wrong style.
- Wrong placement or relationship.
- Output is nearly unchanged when change was required.
- Adds extra elements that violate the prompt.

If both fail but one satisfies more requirements, pick the less bad one. Both Bad is only for genuinely equal failure.

## Axis 3: Visual Quality

Judge craft and visual appeal.

Check:

- Resolution and sharpness.
- Fine detail where detail should exist.
- Natural or intentional focus.
- Balanced exposure.
- Highlights not blown out.
- Shadows not crushed without reason.
- Color saturation not overdone or washed out.
- Color temperature consistent with the lighting.
- Framing and composition.
- Visual hierarchy: attention goes to the intended subject.
- No distracting clutter unless requested.
- Seamless edits if the image appears edited.

Blur is not automatically a flaw. Shallow depth of field is valid when the subject is sharp and blur falls off naturally.

Oversaturation can be a Visual Quality loss. If the image looks filter-applied or too clean in a way real cameras do not produce, also consider Absence of AI Artifacts.

## Axis 4: Absence of AI Artifacts

Judge whether the image looks natural within its intended style and free of generation tells.

Check:

- Waxy or overly smooth skin.
- Distorted faces.
- Wrong finger count.
- Fused, missing, or extra fingers.
- Implausible limb length or joints.
- Broken hands, feet, paws, hooves, wings, or tails.
- Clothing that does not drape with the body.
- Garbled or unreadable text.
- Broken non-Latin scripts.
- Impossible lighting or shadows.
- Reflections that do not match the scene.
- Floating, clipping, or fused objects.
- Wrong perspective.
- Over-sharpened edges, plastic surfaces, tiled patterns.
- Object scale problems.
- Same-distance objects with inconsistent focus.

Imaginary scenes are not automatically artifacts. Do not penalize flying submarines, fantasy physics, or intense colors if the prompt asks for them. Still penalize garbled text, broken anatomy, and objects that do not fit the scene's internal logic.

Stylized images still have artifact standards. Comic, manga, and illustration outputs should have consistent line weight, readable text, and anatomy that works within the style.

## Tie Policy

Use Both Good or Both Bad only when the axis is genuinely indistinguishable.

Do not tie because:

- both have some problems;
- the difference is small but visible;
- one wins visually and the other wins prompt compliance;
- you are unsure but can identify a cleaner response.

When in doubt, pick a winner and explain the visible evidence.

## Justification Rules

A strong justification:

- Names the selected response.
- Names the axis when needed.
- Cites specific visual details.
- Compares against the other response.
- Uses plain wording.

Good:

`Response A is better because both animals are shown mid-fall onto the cushion, and the dog and cat anatomy is cleaner. Response B loses one dog leg and the cat's face is oversized.`

Bad:

`A looks more realistic and aesthetically pleasing overall.`

## Final Checklist

- Prompt read before image judgment.
- Each requirement checked.
- Small details inspected.
- Axis-specific rules applied.
- No unjustified tie.
- Comment sounds like a normal person and mentions concrete evidence.
