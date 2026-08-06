# Handshake H2H / T2I Image Rubric

Use this reference for Handshake text-to-image, H2H image comparison, and T2I Magnifier Pairwise tasks.

## Source PDFs

Primary:

- `HANDSHAKE-AI/pdfs/handshake-ai-Text-to-Image (T2I).pdf`
- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/guidelines.md`, section `Image Evaluation for Head-to-Head (H2H) Tasks`, which covers the T2I Magnifier Pairwise flow

Foundations:

- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`

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
4. Identify the details a real person would notice first if they cared about the prompt. Prioritize big visible anchors before tiny defects:
   - requested subject and setting
   - count of people, animals, or objects
   - obvious object placement and relationships
   - geography, route, layout, or spatial order when requested
   - readable required text, labels, numbers, or signs
   - main action or interaction
   If a response fails one of these obvious anchors, that should usually matter more than small polish differences.
5. Zoom in on likely failure points:
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
6. Score each axis independently.
7. Write a concise justification that cites visible evidence.

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

### Preference Severity

- Use "Strongly Prefer" only when the winning response actually succeeds at the core prompt requirements and the losing response clearly fails, or when the quality gap is so large that the loser is basically unusable.
- If both responses fail a core instruction (wrong count, missing subject, broken data accuracy, wrong layout), cap the overall preference at "Slightly Prefer." The winner is just less bad, not genuinely good.
- "Slightly Prefer" is the right call when both share the same fundamental failure but one handles the rest of the prompt better.

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
- Sounds like a quick human assessment, not a formal rubric explanation.
- Keeps the sentence flow simple: pick the winner, name the visible details it got right, then name the main thing the other response missed.
- Avoids colon-style phrasing in prose. Use a colon only for actual lists or UI field labels. Prefer flowing sentences like `Response B is slightly better because...`
- Does not use em dashes. Use commas, periods, or "and" instead.
- Does not sound overly polished or robotic. Write like a normal person would explain their reasoning.
- Uses casual connectors like "but," "so," "because," and "also."

Good:

`Response A is better because both animals are shown mid-fall onto the cushion, and the dog and cat anatomy is cleaner. Response B loses one dog leg and the cat's face is oversized.`

Good for T2I Magnifier Pairwise open feedback:

`Response A is much better because it includes nearly all the requested whiteboard details, like the weekly signup chart, the red "510!!" note, the KPI sticky notes, the pie chart, the erased flowchart, the coffee stain, the marker tray, the monitor, and the plant. Response B looks cleaner, but it leaves the board too empty and misses too many prompt details.`

Good for close-call prompt compliance:

`Response B is slightly better because the phone detail is much clearer. One person is actually raising a phone toward the sculpture behind the group, which Response A does not show as well. It is not perfect because the man does not clearly look at the guide's face, but B still handles the sculpture part better.`

Good for geography or map prompts:

`Response A is much better because the map actually follows the Spanish Mediterranean coast and places Barcelona, Valencia, and Malaga in the right general spots along the shoreline. The dotted route also connects them clearly. Response B has a nice parchment style, but Barcelona is pushed way inland and the coastline layout feels wrong.`

Bad:

`A looks more realistic and aesthetically pleasing overall.`

Also bad:

`Upon review of the prompt-alignment criteria, Response A demonstrates superior fulfillment of the requested semantic elements and contextual constraints.`

## Final Checklist

- Prompt read before image judgment.
- Each requirement checked.
- Small details inspected.
- Axis-specific rules applied.
- No unjustified tie.
- Comment sounds like a normal person and mentions concrete evidence.
