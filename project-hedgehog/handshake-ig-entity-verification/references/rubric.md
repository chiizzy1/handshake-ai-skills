# Handshake IG Entity Verification Rubric

Use this reference for IG Entity Verification tasks.

## Source PDF

- `HANDSHAKE-AI/pdfs/handshake-IG Entity Verification.pdf`

## Task Shape

You review another annotator's entity tag.

You see:

- Target image on the left with a yellow box around the entity being verified.
- Reference image on the right. If the reference has a green box, use only that sub-region; otherwise use the whole reference.
- Entity type and label above the images.

Your job is to decide whether the target and reference actually refer to the same entity.

## Minimum Workflow

1. Read the entity type and label first. They define what kind of match counts.
2. Look at the yellow box first. That is the only target content being verified.
3. Look at the green box on the reference, or whole reference if no green box.
4. Find 1-3 identifying features that matter for the entity type.
5. Pick a verdict.
6. Write a short reason naming the features used.

## Decision Gate

Use this gate before choosing a verdict:

- If an image is broken, the boxed target is wrong, or the reference is unrelated: Flag as bad data.
- If the item is valid but key features are not visible enough: Skip.
- If features clearly match: Definitely Same.
- If features clearly conflict: Definitely Different.
- If features mostly match but quality or angle leaves doubt: Likely Same.
- If features mostly conflict but are not decisive: Likely Different.

## Verdict Scale

The key axis is confidence, not match strength.

### Definitely Same

Use when identifying features are clearly visible in both images and clearly match.

### Definitely Different

Use when identifying features are clearly visible in both images and clearly do not match.

### Likely Same

Use when the answer is probably same, but image quality, angle, occlusion, or distance leaves room for doubt.

### Likely Different

Use when the answer is probably different, but evidence is not fully decisive.

### Skip

Use when the images load and the annotation looks legitimate, but you personally cannot make a confident call. This returns the item to the queue.

Do not use "likely" for coin flips. If you cannot tell this time, skip.

### Flag As Bad Data

Use when the source itself is broken and should not be verified by anyone.

Examples:

- either image fails to load or is heavily corrupted;
- yellow box does not contain the claimed entity type;
- reference image is unrelated content;
- label or entity type is obviously wrong;
- target and reference are the exact same image, so there is nothing meaningful to compare.

Do not flag because the item is hard. "I cannot tell" is a skip.

## Identifying Features By Entity Type

### Person

Use:

- face structure
- hairline
- jawline
- nose shape
- mouth/lip shape
- distinguishing marks

Do not rely on:

- hair color alone
- clothing alone
- pose alone

Use Likely Same instead of Definitely Same when occlusion, closed eyes, angle, or image quality prevents a clean feature match.

### Clothing

Use:

- logo placement
- strap width
- cut
- hardware
- stitching
- distinctive construction

Color and style alone are not enough.

### Product

Use exact product identity:

- variant
- size
- scent
- flavor
- packaging text
- SKU-level cues when visible

Same brand line is not enough. Lip balm and sunscreen from the same brand line are different products.

### Location

Use:

- signage
- distinctive architecture
- fixed landmarks
- unique layout

Do not call it same just because it is the same kind of place.

### Animal

For a specific animal, use:

- individual markings
- face stripe pattern
- chest patch
- eye color
- scars or distinctive features

Breed match is not identity match.

## Reason Style

Write short reasons naming the features used.

Good:

`Likely different - both are brown tabbies, but the target has a solid white chest patch and darker face mask; the reference has narrower face stripes and no white chest.`

Good:

`Definitely different - target reads "Lip Balm SPF 25 Shea Butter," while the reference reads "SPF 25 Sunscreen Natural Mint & Shea Butter." Same line, different product.`

Good:

`Likely same - jawline, nose shape, and lip shape align, but the target's eyes are closed and one side of the face is occluded.`

Bad:

`Definitely same - they look similar.`

Bad:

`Likely same - both are brown tabby cats.`

## Skip vs Flag

Skip:

- legitimate item
- images load
- not enough confidence due to distance, occlusion, quality, or angle

Flag:

- broken input
- wrong entity type
- unrelated reference
- image failure/corruption
- target and reference are same image

Do not flag because the comparison is difficult.

## Common Mistakes

- Using breed/color as animal identity.
- Using same brand line as product identity.
- Calling person match definite despite occlusion.
- Judging outside the yellow target box.
- Ignoring the green reference box.
- Flagging when the correct action is skip.

## Final Checklist

- Entity type and label read.
- Yellow box target only.
- Green box or full reference used correctly.
- Entity-specific features identified.
- Verdict confidence matches evidence.
- Reason names concrete features.
