# Handshake UD Caption ELO Rubric

Use this reference for UD Caption ELO tasks.

## Source PDFs

- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-1.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-intermidiate.pdf`
- `HANDSHAKE-AI/guidelines.md` UD Caption ELO section

## Task Shape

The task shows:

- An original reference image.
- Response A generated image.
- Response A caption used to generate that image.
- Response B generated image.
- Response B caption used to generate that image.

You judge how faithfully each generated image and caption captured the original.

## Five Criteria

Choices usually are:

- Response A
- Response B
- Both Good
- Both Bad

Use ties only when genuinely justified.

## Strict Separation

Keep these judgments separate:

- Generated image vs original image.
- Caption vs original image.
- Missing detail vs invented detail.
- Overall match vs small-detail accuracy.

A response can have the better image and the worse caption. Score the criterion the UI asks for, not the response as a whole.

## Original Fact Ledger

Before comparing responses, create a compact fact ledger from the original image only. For diagrams and structured images, recount visible objects by type/color and note the layout, panel titles, grid size, axis labels, and repeated-panel relationships before reading response claims.

If a response caption or another agent claims a different object count, geometry, or layout, re-check the original and trust the original fact ledger.

## Criterion 1: Overall Match

Ask which generated image better matches the original in overall composition, subject, and visual intent.

Check:

- Same number of main objects.
- Same layout.
- Same style.
- Same overall visual structure.
- Same big-picture purpose.

Do not reward a more polished image if it diverges from the original.

## Criterion 2: Image Details

Ask which generated image captures fine details more accurately.

Check:

- object count
- object shapes
- object orientations
- colors
- positions
- labels/text
- background
- geometry
- shadows/style if relevant

Go element by element. A single important wrong shape, missing label, or wrong placement can decide the axis.

For diagrams, charts, schedules, and geometric objects, be strict about layout, labels, visible text, rows/columns, and spatial relationships.

## Criterion 3: Caption Details

Ask which caption more completely and accurately describes the original image.

A good caption:

- Covers all key elements.
- Describes layout and relationships.
- Mentions important visible text or labels when relevant.
- Avoids adding unverifiable claims.
- Does not omit major details.

A caption can be too specific. Exact pixel dimensions, exact hex codes, exact measurements, camera metadata, and similar claims are hallucinations if they cannot be verified from the image.

## Criterion 4: Image Hallucination

Ask which image avoids inventing visual elements not present in the original.

Image hallucinations include:

- extra objects
- missing or wrong geometry
- wrong internal grid lines
- wrong object arrangement
- invented labels/text
- added textures/colors not present
- wrong shading style
- fabricated schedule entries or diagram components

Pick the image that stays closer to the original without fabricating.

For diagrams, wrong object counts, invented extra objects, missing objects, changed arrangements, or incorrect internal grid geometry are hallucinations, not just detail misses.

## Criterion 5: Caption Hallucination

Ask which caption avoids making things up or describing things not visible.

Caption hallucinations include:

- invented exact measurements
- invented technical specs
- invented color codes
- wrong days/dates/names
- wrong object counts
- wrong geometry descriptions
- claims about metadata or resolution not visible

Specificity is not automatically accuracy. It can hide fabrication.

For diagrams, a caption that states the wrong object count, adds extra colored objects, invents coordinates, or describes a layout not supported by the original is hallucinating.

## Independence Rule

Rate image and caption independently.

Examples:

- A can win Overall Match and Image Details while B wins Caption Details.
- A can have a better image but a worse caption.
- A caption with many words can lose if it invents facts.

## Both Good / Both Bad

Both Good:

- Both are genuinely excellent on that criterion.

Both Bad:

- Both significantly fail the criterion and neither is meaningfully closer.

Do not use Both Bad merely because the task is hard.

## Common Mistakes

- Choosing the prettier image instead of the faithful one.
- Ignoring captions because the images are more visible.
- Treating caption detail volume as caption accuracy.
- Accepting another agent's count, coordinate map, or layout claim without re-checking the original image.
- Missing small text, labels, dates, or diagram geometry.
- Penalizing one response on all axes because it lost overall.

## Comment Style

Keep justifications concise, grounded, and natural, like an average careful reviewer wrote them. Do not over-polish or over-explain. Do not use colon characters or em dashes in the justification prose. Keep the writing simple and flowing. Name the decisive visual difference and move on.

Prefer short explanations. Two clear sentences are usually enough.

Good

`Response B is better for Image Details because it keeps the Workshop entries on the Sunday dates, while A moves one Workshop to Tuesday.`

Good

`Response A is better for Caption Hallucination because B adds exact color codes and pixel-level details that cannot be verified from the image.`

Good

`Response A is better because it is closer to the same cropped document page with Problems 113 and 111 in the right order. Response B looks cleaner, but it changes the formatting more and adds sidebar details that are not as faithful to the original.`

Bad

`Response A is better because it keeps the page layout closer to the original. The two problems stay in the same order, the answer choices are preserved, and the text block still feels like the same cropped document page. Response B looks cleaner, but it changes the formatting more by splitting the variables into neat separate lines and adding sidebar details that do not match the original crop as well. Its caption also describes those extra sidebar details too confidently, while A stays closer to what is actually visible.`

Bad

`B is more detailed and therefore more accurate.`

## Final Checklist

- Original image inspected carefully.
- A image, A caption, B image, B caption all read.
- Criteria rated independently.
- Small text/labels checked.
- Hallucinated precision checked.
- Final answer uses concrete evidence.
