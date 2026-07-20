# Handshake R2I / I2I / Omni R2I ELO Rubric

Use this reference for Reference-to-Image, Image-to-Image, and Omni R2I ELO tasks.

## Source PDFs

Primary:

All paths are under `HANDSHAKE-AI/pdfs/`.

- `Handshake-ai-Omni-R2-ELO.pdf`
- `handshake-Image-to-Image (I2I).pdf`
- `handshake-Omni R2I Elo — Examples.pdf`

Foundations:

- `handshae-ai-Image Evaluation.pdf`
- `handshake-ai-HOW-TO-SEE.pdf`
- `handshake-ai-Realism & Artifacts.pdf`

## Task Shape

R2I:

- Reference photo(s).
- Text prompt.
- Two generated responses.
- Six dimensions.

I2I:

- Original image.
- Edit instruction.
- Two edited versions.
- Closely follows the Omni R2I six-axis rubric.

Pixel Aligned I2I:

- Original/input image.
- Single target/edited image.
- Q1 instructions aligned, Q2 pixel aligned, Q3 no AI slop.
- Use `handshake-i2i-pixel-aligned` (read `../../handshake-i2i-pixel-aligned/SKILL.md`) instead of this ELO rubric.

Main question:

- Which response made the requested change while preserving what should remain?

## Mandatory Workflow

1. Read the prompt before judging the outputs.
2. Identify the intended transformation:
   - style transfer
   - lighting edit
   - pose edit
   - canvas/outpainting/inpainting
   - text or graphics edit
   - restoration/upscale/deblur
   - local recolor/material swap
   - scene generation from a reference
3. Inspect the reference image(s). Ask what should carry over:
   - people and faces
   - body build
   - pose/composition when not targeted
   - object count and layout
   - background
   - accessories
   - logos/text
   - colors/materials
   - framing/camera angle
4. Inspect both responses with zoom.
5. Score all six axes independently.

## Hard Fail Checks

Check these before choosing any axis:

- Requested edit did not happen.
- Edit happened to the wrong subject or wrong region.
- Reference person became unrecognizable.
- Untargeted subject, object, text, logo, background, or layout changed.
- Output added or removed important people or objects without instruction.
- Edited region has seams, mismatched light, warped texture, or broken anatomy.

A hard fail should affect the exact axis it belongs to. Do not spread it across unrelated axes unless it truly affects them too.

## Dimension 1: Overall Preference

Choose the response that best captures what the user actually wanted.

Overall is holistic. It can consider all axes, but it is not a mechanical vote count. A response that follows the core prompt is usually better than one that is prettier but misses the requested transformation.

If both images fail Instruction Following equally, use Visual Quality and Absence of AI Artifacts as stronger tie-breakers.

**Overall Preference Eval Task Cues (Hard Rules):**
1. **Look it up if you don't know:** When a prompt involves specialized knowledge (technical, historical, scientific, cultural, anatomical alignment), check a reliable source instead of guessing. Do not assume visual plausibility equals correctness.
2. **Watch out for the overly-AI look in the edit:** Things like unnaturally crisp edges, flat lighting, plasticky textures, or over-saturated colors in the edited area are common giveaways. An edit can look impressive at first glance but feel artificial on a closer look — don't let that initial wow factor automatically win.
3. **Watch out for text issues:** AI edits often add text where it doesn't belong or keep it sharp when it should be soft (far away, off-angle, or out of focus). Cluttered or unnaturally crisp text shouldn't win on visual impact alone.

## Dimension 2: Instruction Following

Judge whether the response did what the prompt said.

Check:

- Requested change happened.
- All prompt requirements were addressed.
- Quantities and relationships match.
- Style or era is correct.
- Targeted objects/people changed as requested.
- Explicit constraints were obeyed.
- The output did not under-edit or over-edit.

Under-editing is a failure: if the prompt asked for a meaningful change and the image barely changed, it may be as bad as ignoring the instruction.

Explicit constraints are hard requirements. If the prompt says "without fabricating facial features," invented details are an instruction-following failure even if they look realistic.

## Dimension 3: Person ID Preservation

Judge whether reference people remain recognizable.

ID is mainly carried by:

- face structure
- eyes, nose, mouth, jawline
- hairline and identity-bearing hair cues
- distinctive marks
- body build when relevant

Do not treat clothing or pose as identity by default. Clothing and pose are separate axes unless the prompt specifically requires preserving them as identity-defining details.

If the person wears different clothing or strikes a new pose but the face clearly reads as the same person, ID is preserved.

For age transformations, judge whether signature facial structure survives while the requested age change happens.

## Dimension 4: Content / Reference Preservation

Judge whether untargeted content stayed faithful to the reference.

Check:

- background
- layout/composition
- camera/framing
- object count
- object placement
- accessories, earrings, glasses, logos
- text and labels
- non-target clothing
- colors and material texture
- fine surface details

Unrequested camera shifts, missing accessories, changed background objects, or altered layout can lower this score.

In I2I, everything the instruction did not mention should usually stay the same.

## Dimension 5: Visual Quality

Judge normal image craft:

- crisp detail
- balanced exposure
- natural or intentional lighting
- good framing
- controlled saturation
- clean focus behavior
- no washed-out look
- no crushed shadows unless stylistically justified
- no obvious seams or mismatched edit regions

Oversaturation is a Visual Quality loss. Balanced compositions win.

Blur is not automatically bad. It is bad when it affects the intended subject, appears patchy, or contradicts the source/reference expectations.

## Dimension 6: Absence of AI Artifacts

Judge generation tells:

- waxy skin
- overly smooth surfaces
- malformed hands/fingers
- wrong limb count
- broken anatomy
- distorted faces
- garbled text
- impossible light or shadows
- unnatural reflections
- mismatched material behavior
- floating/clipping objects
- hallucinated extra details
- inconsistent focus planes

Ambiguous extremity distortion is a known AI tell. If responses are otherwise similar and one has suspicious fingers/toes/hands/feet while the other is clean, pick the cleaner one rather than tying.

## Special Scene Types

### Sci-fi, fantasy, imaginary scenes

Do not penalize intentional unreality the prompt requested. A flying submarine or alien physics can be valid. Still penalize garbled text, malformed anatomy, inconsistent lighting, or objects that do not fit the chosen world.

### Comic, manga, stylized illustration

Style does not exempt the image from artifact checks. Look for broken anatomy within the style, inconsistent line weight, garbled speech bubbles, and objects that do not belong.

### Charts, diagrams, infographics

Evaluate:

- facts plotted or shown correctly
- scale and axes appropriate
- layout clear
- labels readable
- values possible

Garbled axis labels and impossible values are equivalent to garbled text in a photo.

## Tie Policy

Avoid ties. Use a tie only when responses are virtually indistinguishable on that specific dimension.

Do not tie because:

- both have flaws;
- the gap is small but visible;
- one wins on one axis and the other wins on another;
- you are unsure but can name a cleaner response.

## Common Mistakes

- Letting a beautiful image win Instruction Following after it misses the core request.
- Treating clothing changes as ID failure when the face is preserved.
- Ignoring missing accessories or logos under Reference Preservation.
- Putting all issues under Overall rather than scoring axes separately.
- Treating intentional fantasy as an AI artifact.
- Tying to avoid a hard decision.

## Comment Style

Use simple, visible evidence:

`Response B follows the prompt better because it keeps all six people and the lifted-body composition. Response A removes people and loses the group-lifting pose.`

`Response A preserves ID better because the man's comb-back hair and facial structure stay closer to the reference. B makes the hair cooler and changes the face more.`

Avoid formal filler and long explanations.

## Final Checklist

- Prompt and reference both reviewed.
- Targeted changes identified.
- Untargeted preservation checked.
- Six dimensions scored separately.
- Person ID judged from identity-bearing features.
- Ties avoided unless truly indistinguishable.
- Comment names concrete evidence.
