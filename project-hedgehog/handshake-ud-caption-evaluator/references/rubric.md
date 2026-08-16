# Handshake UD Caption ELO Rubric

Use this reference for UD Caption ELO tasks.

## Contents

- [Source PDFs](#source-pdfs)
- [Task Shape](#task-shape)
- [Five Criteria](#five-criteria)
- [Strict Separation](#strict-separation)
- [Original Fact Ledger](#original-fact-ledger)
- [Criterion 1: Overall Match](#criterion-1-overall-match)
- [Criterion 2: Image Details](#criterion-2-image-details)
- [Criterion 3: Caption Details](#criterion-3-caption-details)
- [Criterion 4: Image Hallucination](#criterion-4-image-hallucination)
- [Criterion 5: Caption Hallucination](#criterion-5-caption-hallucination)
- [Independence Rule](#independence-rule)
- [Both Good / Both Bad](#both-good-both-bad)
- [Common Mistakes](#common-mistakes)
- [Comment Style](#comment-style)
  - [Per-Axis Phrasing](#per-axis-phrasing)
  - [Open Feedback Shape](#open-feedback-shape)
  - [The Four Patterns](#the-four-patterns)
  - [Common Comment Failures](#common-comment-failures)
- [Final Checklist](#final-checklist)

## Source PDFs

- `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-ai-UD Caption Elo Task example-1.pdf`
- `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-ai-UD Caption Elo Task example-intermidiate.pdf`
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

Keep comments concise, grounded, and natural, like an average careful reviewer wrote them. Do not over-polish or over-explain. Do not use colon characters or em dashes in the prose. Name the decisive visual difference and move on.

The style rules, persona, and banned-phrase list live in `SKILL.md` under Open Feedback Style. This section carries the worked examples.

### Per-Axis Phrasing

Use this shape inside the Response Analysis section, where one axis is under discussion.

Good

`Response B is better for Image Details because it keeps the Workshop entries on the Sunday dates, while A moves one Workshop to Tuesday.`

Good

`Response A is better for Caption Hallucination because B adds exact color codes and pixel-level details that cannot be verified from the image.`

Bad

`B is more detailed and therefore more accurate.`

### Open Feedback Shape

This is the text that goes in the task's Open Feedback box. It covers the whole comparison in 2 to 3 sentences, not one axis at a time.

❌ Too long, recites every axis

`Response A is better because it keeps the page layout closer to the original. The two problems stay in the same order, the answer choices are preserved, and the text block still feels like the same cropped document page. Response B looks cleaner, but it changes the formatting more by splitting the variables into neat separate lines and adding sidebar details that do not match the original crop as well. Its caption also describes those extra sidebar details too confidently, while A stays closer to what is actually visible.`

✅ Two sentences, one decisive difference

`Response A is better because it keeps the same cropped document page with Problems 113 and 111 in the right order. Response B looks cleaner but changes the formatting and adds sidebar details that are not in the original.`

### The Four Patterns

Almost every UD Caption comment is one of these four. Match the shape to the situation.

#### 1. The Split Decision

One response wins the image and the other wins the caption. The Independence Rule allows this, so the comment has to carry both halves without reading as a contradiction. Say which side won the image, then start the second sentence on the caption.

`Response B is better on the image because it keeps all eleven points and the axis running to 16, while Response A stops the axis at 12 and drops two points. Response A's caption is the more accurate one though, since B's caption adds exact pixel positions and an aspect ratio that cannot be read off the original.`

#### 2. The Polish Trap

The prettier output is the less faithful one. Say plainly that it looks better, then say why that did not decide it. Do not pretend the cleaner image is ugly.

`Response A is better because the bars stay in the same order with the same three colors as the original. Response B has a cleaner style and smoother gradients, but it merges two categories and drops the axis labels.`

#### 3. Precision Masking Fabrication

A long, confident caption invents specifics. Name the invented type of detail rather than calling the caption wrong in general.

`Response A's caption is better because it sticks to what is visible in the diagram. Response B reads as more thorough, but it adds exact hex codes and a stated resolution that are not in the original image.`

#### 4. Justifying a Tie

Both Good and Both Bad need more evidence than a pick, not less. Excessive tie usage is grounds for removal, so name what both did rather than saying they are similar.

`Both images miss the original layout in the same way, since each one turns the two stacked panels into a single wide panel. Neither caption mentions the panel split either, so there is no meaningful gap between them on this one.`

### Common Comment Failures

- Naming every axis in one sentence instead of the one that decided it.
- Saying "more detailed" when the point is that the detail was invented.
- Calling a response "perfect" or "flawless," which a zoomed-in reviewer can disprove.
- Writing a tie comment shorter than a pick comment.
- Dropping the original's own label text in favor of vague references like "the top item."

## Final Checklist

- Original image inspected carefully.
- A image, A caption, B image, B caption all read.
- Criteria rated independently.
- Small text/labels checked.
- Hallucinated precision checked.
- Final answer uses concrete evidence.
- Open Feedback matches one of the four patterns and reads like a person wrote it.
