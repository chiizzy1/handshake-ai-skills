# Handshake I2I Pixel Aligned Rubric

Use this reference for Handshake / Project Hedgehog i2i Pixel Aligned tasks.

## Source Materials

Primary source:

- `HANDSHAKE-AI/assessments/i2i Pixel Aligned assessment.md`

Related visual foundations:

- `HANDSHAKE-AI/pdfs/handshake-Image-to-Image (I2I).pdf`
- `HANDSHAKE-AI/pdfs/Handshake-ai-Omni-R2-ELO.pdf`
- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`

The Pixel Aligned assessment is the most specific authority for Q1/Q2/Q3 Yes/No tasks.

## Core Concept

Pixel Aligned tasks review whether an AI photo edit was done correctly.

Each item gives:

- an input/original image;
- a target/edited image;
- an instruction describing the requested change.

The evaluator answers three independent questions:

1. Q1 - Instructions aligned: did the target make all and only the instructed change?
2. Q2 - Pixel aligned: did unchanged areas stay perfectly aligned with the input?
3. Q3 - No AI slop: are both the input and target free of AI slop?

These questions are independent. A target can pass Q1 but fail Q2. A target can pass Q1 and Q2 but fail Q3. A target can fail Q1 but still pass Q2 if nothing moved.

## Required Inspection Order

1. Read the instruction.
2. Convert the instruction into a precise list of allowed changes.
3. Identify everything that should remain unchanged.
4. Compare the input and target.
5. Inspect the entire frame:
   - main subject;
   - edited region;
   - nearby untouched region;
   - background;
   - frame edges;
   - faces;
   - bodies;
   - hands and fingers;
   - clothing;
   - objects;
   - shadows;
   - reflections;
   - text and signs;
   - small details.
6. Answer Q1, Q2, and Q3 independently.

Do not scan only the obvious edit spot. Many failures are in the background, edges, hands, faces, or unedited objects.

## Q1 - Instructions Aligned

Question: did the target make all and only the requested change?

Answer Yes only if both are true:

- every part of the requested change is fully done;
- nothing else was added, removed, altered, recolored, reshaped, restyled, shifted in content, or regenerated.

Answer No if the requested change is missing, partial, wrong, or accompanied by any unrequested content change.

### Q1 Yes Cases

Use Q1 Yes when:

- the instructed object changed exactly as requested;
- the target object is the right object;
- the full requested change happened, not just a hint of it;
- no unrelated object, person, background, color, text, or lighting changed;
- the edit does not sneak in a new style or scene change;
- the edit does not create additional unrequested objects;
- the edit does not remove unrelated objects;
- the edit does not change identity-bearing person details unless requested;
- the edit does not fabricate specific details in a restoration/upscale task when the instruction forbids fabrication.

### Q1 No Cases

Use Q1 No when:

- the requested edit did not happen at all;
- the edit is incomplete;
- the wrong object was edited;
- the wrong person was edited;
- the change happened in the wrong location;
- extra changes appeared outside the requested edit;
- an object was added when only recoloring was requested;
- an object was removed when only recoloring was requested;
- the background color changed without instruction;
- wall, floor, curtain, sky, furniture, road, or window content changed without instruction;
- a person's face, clothing, body, pose, or hair changed without instruction;
- the target reinterpreted the whole image instead of editing only the requested part;
- text changed when text was not part of the instruction;
- a logo or sign changed when not requested;
- the edit added a filter or style change that was not requested;
- the prompt asked for all of something but only some instances changed;
- the prompt asked for only one object but multiple objects changed.

### Q1 Examples

Instruction: replace the apple on the table with a dog.

- Target replaces the apple with a dog and also changes the wall color: Q1 No.
- The requested replacement happened, but the wall color was not supposed to change.

Instruction: turn the parked car red.

- Target leaves the parked car unchanged: Q1 No.
- The instructed change was not made.

Instruction: remove the coffee cup from the counter.

- Target removes the cup and leaves the counter naturally reconstructed, with no other changes: Q1 Yes.
- Target removes the cup but changes cabinets, countertop color, or nearby objects: Q1 No.
- Target leaves part of the cup, its handle, reflection, shadow, or a ghosted outline: Q1 No.

Instruction: change the bicycle to green.

- Target makes the bicycle green and nothing else changes: Q1 Yes.
- Target makes the bicycle green but zooms the frame: Q1 can still be Yes if content did not otherwise change. The zoom belongs to Q2.
- Target makes the bicycle green but also changes the street or background: Q1 No.

## Q2 - Pixel Aligned

Question: did the parts that should stay the same stay put?

Q2 is about position and geometry. It is not about whether the instruction was followed. It is not about whether the image looks nice.

Answer Yes only if the unchanged areas line up perfectly with the input.

Answer No if the target is shifted, zoomed, cropped, resized, stretched, warped, perspective-changed, or if unchanged objects move.

When unsure on Q2, answer No.

### What "Pixel Aligned" Means

Pixel aligned means unchanged content remains in the same place, same size, and same geometry as in the input.

Check:

- frame edges;
- object boundaries;
- background lines;
- windows and doors;
- table edges;
- floor lines;
- horizon lines;
- body outlines outside the edit;
- repeated textures;
- shadows that should not have changed;
- placement of untouched objects.

If the target and input were flipped back and forth, unchanged areas should not jump.

### Q2 Yes Cases

Use Q2 Yes when:

- the target has the same framing as the input;
- the same objects remain in the same positions;
- unchanged areas have the same scale;
- background lines and edges line up;
- the edit is local and does not move nearby unchanged content;
- the target is not zoomed, cropped, rotated, or perspective-shifted.

### Q2 No Cases

Use Q2 No when:

- the whole image shifted left, right, up, or down;
- the target is slightly zoomed in;
- the target is slightly zoomed out;
- the target is cropped differently;
- the target has a different aspect crop;
- the target is resized or stretched;
- the target is rotated;
- the target perspective changed;
- background elements moved;
- unchanged faces, bodies, or objects changed position;
- the edit region pushed or pulled nearby pixels;
- the output has local warping around the edited object;
- the target preserves content but in a different placement.

### Q2 Examples

Instruction: make the man appear slightly older.

- Target ages the man but the whole frame shifts: Q1 Yes, Q2 No.
- The edit can be correct while alignment fails.

Instruction: add sunglasses to the woman.

- Target adds sunglasses but the whole image is zoomed and cropped: Q2 No.
- The sunglasses being correct does not make the unchanged areas aligned.

Instruction: change the bicycle to green.

- Target changes the bicycle correctly and looks clean, but the frame is zoomed/shifted: Q1 Yes, Q2 No, Q3 Yes.

## Q3 - No AI Slop

Question: are both images free of AI slop?

Q3 is a cleanliness check for both the input and target.

Answer Yes only when both images look clean and real enough, with no visible AI slop.

Answer No if either image has AI slop.

When unsure on Q3, answer No.

### Q3 Checks Both Images

Do not check only the edited target.

If the input image already has obvious AI slop, Q3 is No even if the target looks clean.

If the target introduces AI slop, Q3 is No even if the input is clean.

If both images have no obvious slop, Q3 is Yes.

### AI Slop Patterns

Use Q3 No for:

- six-fingered hands;
- fused fingers;
- missing fingers;
- extra fingers;
- twisted hands;
- hands blending into objects;
- warped faces;
- distorted eyes;
- mismatched pupils;
- broken mouths or teeth;
- melted ears;
- warped bodies;
- strange limbs;
- extra limbs;
- impossible joints;
- plastic or waxy skin;
- over-smoothed faces;
- smeared textures;
- melted object boundaries;
- broken handles;
- distorted cups, plates, wheels, chairs, utensils, tools, phones, glasses, or jewelry;
- fake or unreadable text;
- random letters on signs, packaging, clothing, books, or screens;
- impossible reflections;
- impossible shadows;
- light direction that contradicts the scene;
- background objects blending into each other;
- hallucinated details in a restoration or upscale;
- unnatural small structures like rails, spokes, zippers, buttons, fingers, teeth, lashes, or hair strands.

### Q3 Yes Cases

Use Q3 Yes when:

- both input and target are free of obvious artifacts;
- the edit looks clean;
- hands and faces are plausible;
- text is either readable or naturally too small/blurred to read;
- objects keep believable shapes;
- materials and shadows are plausible;
- any blur or low resolution is normal for the image and not a generation defect.

### Q3 No Examples

Instruction: add a hat to the child.

- Target adds the hat cleanly, but the input has a fused six-finger hand: Q3 No.
- Q3 checks both images.

Instruction: add a bowl of fruit to the kitchen counter.

- Q1 and Q2 may be No for other reasons, but if the person's face is warped in either image, Q3 is No.
- Q3 is independent.

Instruction: brighten the photo.

- Target brightens the image but creates plastic skin and fake text: Q3 No.
- A correct brightness change does not excuse slop.

## Independence Rules

Always judge Q1, Q2, and Q3 separately.

### Q1 Does Not Control Q2

The requested edit can be correct while alignment fails.

Example:

- The target correctly makes the man older.
- The whole frame shifts.
- Q1 Yes, Q2 No.

### Q1 Does Not Control Q3

The requested edit can be correct while AI slop appears.

Example:

- A watch is correctly added.
- The other hand is melted with extra fingers.
- Q1 Yes, Q3 No.

### Q2 Does Not Control Q1

The target can be perfectly aligned while the edit is missing.

Example:

- The instruction says turn the umbrella blue.
- The umbrella stays the original color.
- Nothing moved.
- Q1 No, Q2 Yes.

### Q2 Does Not Control Q3

A target can be pixel aligned and still have slop.

Example:

- Nothing shifts.
- A face is warped.
- Q2 Yes, Q3 No.

### Q3 Does Not Control Q1 Or Q2

A clean-looking image can still fail the instruction or alignment.

Example:

- The target is visually clean.
- It changes the wrong object.
- Q1 No.

## Upscale, Restoration, Deblur, And Denoise

Upscale/restoration tasks deserve special care because models often look better at first glance while inventing details.

Allowed:

- increasing resolution;
- making existing edges clearer;
- reducing noise;
- sharpening existing textures;
- clarifying general face placement;
- making hair and clothing generally clearer;
- improving recoverable detail.

Not allowed unless the instruction explicitly permits it:

- inventing new face structure;
- inventing specific facial features;
- changing identity;
- changing age more than required;
- inventing new teeth, eyes, eyebrows, wrinkles, or hairline details;
- changing hand structure;
- inventing fingers;
- making text readable by hallucinating new words;
- adding new logos or labels;
- changing background objects;
- making small background figures into invented people.

### "Without Fabricating" Is A Hard Constraint

If the prompt says "enhance plausibly without fabricating specific facial features," then fabricated details are an instruction-following failure.

This can affect:

- Q1, because the target did more than the instruction allowed;
- Q3, because hallucinated face or hand structure is AI slop.

### Group Photo Upscale Example

Prompt: upscale a group party photo to 4x resolution. Each person's face should gain definition, but smaller back figures will have less recoverable detail. Enhance plausibly without fabricating specific facial features.

Better response:

- improves clarity;
- preserves the same people and layout;
- keeps smaller background faces plausible rather than over-defined;
- avoids inventing new face structure;
- avoids strange hands.

Worse response:

- fabricates sharper facial features on people whose faces were not recoverable;
- changes the older man's face instead of just clarifying it;
- creates unnatural hands or finger structure;
- looks impressive at a glance but invents details.

Do not reward fake sharpness. Realistic-looking hallucination is still a failure when the instruction forbids fabrication.

## All And Only The Instruction

Q1 is strict.

"All" means every requested part happened.

"Only" means nothing else changed.

Common "only" failures:

- changing wall color while replacing an object;
- altering lighting while recoloring a car;
- changing a person's face while adding sunglasses;
- changing background props while removing a cup;
- changing crop or zoom is usually Q2, but if the content itself is also regenerated or altered, it may also affect Q1;
- adding a new object while changing color;
- changing multiple instances when one object was requested;
- changing one instance when all instances were requested.

## Alignment Versus Content

Use this distinction:

- Q1 asks: did the correct content change and nothing else?
- Q2 asks: did unchanged content stay in the exact same place?

A frame shift, zoom, or crop can fail Q2 even if Q1 is Yes.

Do not mark Q1 No only because of a pure alignment shift unless the shift also causes a content change beyond alignment.

Example:

- Instruction: make the man older.
- Target only ages the man, but the whole image shifts.
- Q1 Yes.
- Q2 No.

Example:

- Instruction: add sunglasses.
- Target adds sunglasses, zooms in, and crops out part of the woman's shoulder.
- Q1 may be Yes if the only content change is the requested sunglasses and the crop is treated as alignment/framing.
- Q2 No because kept areas no longer line up.
- If the crop removes meaningful content that should remain, mention it under Q2 and consider Q1 only if the UI/task treats crop as unrequested content alteration. In Pixel Aligned assessments, pure zoom/crop examples usually teach Q2 failure.

## Clean Photo Versus Low Quality

Do not confuse low resolution with AI slop.

Q3 No requires visible slop or a strong artifact signal. Normal blur, compression, low light, motion blur, or shallow depth of field can be clean if they are natural.

However, when unsure on Q3, answer No.

Use Q3 No for blur when:

- blur is patchy and artificial;
- blur melts anatomy or object structure;
- blur hides deformed hands/faces;
- the target creates plastic or smeared textures;
- text turns into random marks.

Use Q3 Yes for blur when:

- both images are normal low-resolution photos;
- small text is naturally unreadable due to distance;
- background faces are naturally out of focus;
- no clear AI artifact is visible.

## Common Assessment Patterns

### Object Replacement With Extra Background Change

Instruction: replace apple with dog.

Correct answer:

- Q1 No if wall color also changed.
- The dog replacement does not excuse the unrequested wall change.

### Recolor Not Done

Instruction: turn parked car red.

Correct answer:

- Q1 No if the car did not become red.
- The rest of the image staying unchanged does not matter for Q1 if the requested edit is missing.

### Correct Edit With Frame Shift

Instruction: make the man slightly older.

Correct answer:

- Q1 Yes if only age changed.
- Q2 No if the whole frame shifted.

### Correct Edit With Zoom/Crop

Instruction: add sunglasses.

Correct answer:

- Q2 No if the target is zoomed and cropped.
- The sunglasses being correct does not make Q2 Yes.

### Removal Task

Instruction: remove the coffee cup from the counter.

Check:

- Is the cup fully gone?
- Is there any handle, rim, shadow, reflection, stain, ghosting, or cup-shaped blur left?
- Was the counter reconstructed naturally?
- Did cabinets, counter, nearby objects, shadows, or background change?

Q1 is Yes only if the cup is fully removed and no unrequested content changes.

### Input Slop Counts

Instruction: add a hat to the child.

Correct answer:

- Q3 No if the input already has a six-fingered fused hand.
- The target being clean is not enough.

### Warped Face In Either Image

Instruction: add bowl of fruit.

Correct answer:

- Q3 No if a person's face is warped.
- Q3 is independent from Q1 and Q2.

### Brightening With Plastic Skin Or Fake Text

Instruction: brighten the photo.

Correct answer:

- Q3 No if target has plastic skin or fake text.
- A correct global brightness change does not excuse artifacts.

### Correct Edit But Zoomed/Shifted

Instruction: change bicycle to green.

Correct answer:

- Q1 Yes if the bicycle changed to green and no other content changed.
- Q2 No if the frame is zoomed or shifted.
- Q3 Yes if both images are otherwise clean.

## Answer Style

When the UI asks for a multiple-choice answer, give the exact option or mark it.

When the UI asks for a short explanation:

- start with Yes or No;
- name the visible reason;
- keep it brief;
- sound like a normal person, not a rubric;
- do not over-explain every axis if only one axis is asked.

Good:

`No - the cup is gone, but the counter and nearby objects changed too, so it was not only the requested edit.`

Good:

`Q1: Yes. Q2: No - the edited image is shifted, so the unchanged parts do not line up. Q3: Yes.`

Avoid:

`The target fails the image alignment preservation criterion due to geometric displacement of non-targeted regions.`

Use:

`No - the whole target is shifted, so the parts that should stay the same do not line up.`

## Decision Checklist

Before finalizing:

- Did I read the instruction first?
- Did I identify the exact allowed change?
- Did I check whether the edit made all of that change?
- Did I check whether it made only that change?
- Did I compare unchanged areas for movement, zoom, crop, resize, or warp?
- Did I scan both input and target for AI slop?
- Did I check hands, faces, text, edges, and small objects?
- Did I answer Q1, Q2, and Q3 independently?
- Did I default to No if genuinely unsure on Q2 or Q3?
- Did I keep the final answer in the requested format?
