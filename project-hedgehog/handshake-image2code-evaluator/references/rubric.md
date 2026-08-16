# Handshake Image2Code Rubric

Use this reference for Image2Code tasks.

## Contents

- [Source](#source)
- [Main Idea](#main-idea)
- [Rating Scales](#rating-scales)
- [Render Gate](#render-gate)
- [Multi-Frame Rule](#multi-frame-rule)
- [Dimension 1 - Structure & Instruction Following](#dimension-1---structure-instruction-following)
- [Dimension 2 - Visual Quality](#dimension-2---visual-quality)
- [Dimension 3 - Text & Data Accuracy](#dimension-3---text-data-accuracy)
- [Overall Preference](#overall-preference)
- [N/A Rules](#na-rules)
- [Skip Or Flag](#skip-or-flag)
- [Comment Style](#comment-style)
- [Final Checklist](#final-checklist)

## Source

- `HANDSHAKE-AI/project-hedgehog-pdfs/image2code.md` (no such file was present at last check; if it is still missing, this rubric is the operative source)

## Main Idea

You compare two rendered outputs against a reference image. The reference image is the ground truth and primary spec.

The best output is the one that reproduces the reference more faithfully, not the one that looks nicer in a generic way.

## Rating Scales

Live tasks usually use:

| Rating | Meaning |
|---|---|
| A much better | A is clearly and significantly stronger |
| A slightly better | A has a noticeable but small edge |
| Tie | Both are roughly equal |
| B slightly better | B has a noticeable but small edge |
| B much better | B is clearly and significantly stronger |

Use N/A only when the dimension truly does not apply.

Quiz tasks may use only:

- A is better
- Tie
- B is better

For quiz tasks, do not use N/A.

## Render Gate

Apply this first.

If a render is empty, broken, white, black, a tiny fragment, or failed-to-render, it loses Visual Quality outright and is much worse on every other applicable dimension.

A working render always beats a broken render.

## Multi-Frame Rule

For animations, compare each output frame to the reference frame at the same timestamp.

For scrolling websites, compare each output frame to the reference frame at the same scroll position.

Never compare a model frame against the wrong time or scroll position.

## Dimension 1 - Structure & Instruction Following

Ask whether the right elements are in the right places.

Use the overlay test:

- Do major blocks line up?
- Do regions and relationships match?
- Are proportions, grouping, and ordering correct?
- Are non-text elements present in the right structure?
- Did the output avoid hallucinated structure?
- Is the output internally coherent?
- Are visible task instructions obeyed?

Do not score missing or garbled labels here. Text presence and correctness are Dimension 3.

Category checks:

- Website/UI - section order, header, nav, content, footer, alignment, proportions, and scroll-frame matching.
- Chart/graph - title, axes, legend, series, data proportions, pie slice angles, bar order and heights, line paths, scatter clouds, histogram bins, box plots, heatmaps, radar spokes.
- STEM diagram - arrows, cycles, branches, circuit wiring, molecular geometry, geometric constructions, flowchart topology, engineering views, music notes on the correct staff lines.
- Infographic - panel layout, panel count, icon-stat pairings, and hierarchy.
- Art/illustration - same subjects and objects in the same foreground and background arrangement.
- Icon/drawing - silhouette, proportions, element positions, inner details, size, and centering.
- Table - row and column count, merged cells, header versus data cells, nested structure. This dimension dominates for tables.
- 3D scene - object counts, spatial arrangement, camera angle, perspective, and scale.
- Animation - per-frame state, motion fidelity, easing, sequencing, looping, and secondary motion.

Calibration:

- Much better - one side reproduces the structure while the other drops, reorders, invents, or violates major elements.
- Slightly better - minor misalignment or one out-of-place element.
- Tie - the skeletons match.

Do not over-penalize sub-pixel misalignment or decorative details the reference leaves open.

## Dimension 2 - Visual Quality

Ask whether the render is polished and visually faithful to the reference.

Check:

- color accuracy, palettes, gradients, and fills;
- typography style, strokes, shadows, borders, and rounded corners;
- spacing, polish, and visual fidelity;
- overlapping, clipping, overflow, unstyled fallback, garbled output, and content cut off;
- placeholder or broken images where the reference shows a real photo.

Category checks:

- Website/UI - colors, fonts, spacing, shadows, borders, rounded corners, and image handling.
- Chart/graph - clean rendering, gridlines, series colors, marker and line styles, no text or line overlaps.
- STEM diagram - color, patterns, geometric precision, hatching, line weights, and neat music staves or beams.
- Infographic - section backgrounds, color coding, typography hierarchy, and decorative shapes.
- Art/illustration - color, gradients, shading, line style, aesthetic match, and level of detail.
- Icon/drawing - stroke width, caps, crispness, fills, gradients, transparency, size, and centering.
- Table - borders, cell alignment, background colors, and bold headers.
- 3D scene - materials, colors, lighting, shadows, ambient feel, and atmosphere.
- Animation - shapes, colors, gradients, opacity fades, and style.

Rule of thumb:

- One critical rendering bug usually outweighs several minor aesthetic wins.

## Dimension 3 - Text & Data Accuracy

Ask whether every piece of text, number, label, and domain notation is exact and attached to the right element.

Use N/A when the reference has no meaningful text.

Check:

- missing, reworded, garbled, or fabricated text;
- wrong numbers, dates, prices, percentages, or tick values;
- labels attached to the wrong element;
- broken chemical, math, physical, engineering, music, or domain notation;
- wrong or transposed table cell values.

Rules:

- Any wrong number is severe.
- Text presence and correctness live here.
- Text color, font, and styling live in Visual Quality.
- Non-text element presence lives in Structure & Instruction Following.

Category checks:

- Website/UI - headings, paragraphs, brand names, prices, dates, buttons, and nav labels.
- Chart/graph - titles, axis titles, tick values, legend entries, data-point values, and labels.
- STEM diagram - formulas, symbols, units, equations, place names, dimensions, markings, tempo, lyrics.
- Infographic - headline numbers, percentages, section titles, and stat labels.
- Table - every cell exact and in the right cell.
- Art, icon, drawing, and 3D scene - usually N/A unless text is present.
- Animation - any text inside the animation.

Calibration:

- Much better - one side is faithful while the other has multiple wrong values, fabricated text, or large omissions.
- Slightly better - a single minor typo or one slightly-off value.
- N/A - no meaningful text.

Do not over-penalize line wrapping of correct text.

## Overall Preference

Overall is a holistic judgment based on which output better reproduces the reference.

Structure can dominate for tables and diagrams. Text/data can dominate for charts, STEM, infographics, and tables. Visual fidelity can dominate for art, illustration, icons, and heavily visual layouts.

The justification should:

- be 2 to 3 sentences;
- name the dominant dimension or plain reason;
- cite concrete evidence;
- mention the losing side's strongest point when useful.

## N/A Rules

Use N/A only on live tasks and only when the dimension truly does not apply.

Most common case:

- Text & Data Accuracy is N/A when the reference has no meaningful text.

Do not default to Tie when a dimension is irrelevant.

## Skip Or Flag

Skip or flag instead of forcing a rating when:

- the reference is corrupt or unreadable;
- the prompt is nonsensical;
- both renders are broken in a way that makes comparison impossible;
- the content is too ambiguous to judge.

## Comment Style

Write like an average careful reviewer. Keep it short, concrete, and tied to the reference.

Good:

`Response A is better because it keeps the table's row and column structure intact, while B merges cells that should be separate. B has slightly cleaner borders, but the structure error matters more.`

Good:

`Response B is better because the icon silhouette and teal fill are closer to the reference. A includes the small inner notch, but its stroke is too thin and the whole shape is off-center.`

Bad:

`Response A is preferred due to a superior reconstruction of multimodal layout semantics.`

### The Four Patterns

Most image2code comments are one of these. Match the shape to the situation.

#### 1. The Render Gate

One output did not render, or rendered blank. Nothing else matters. Say it plainly and stop.

`Response B is better because it actually renders the page with the header, table, and footer in place. Response A comes up as a blank white screen, so there is nothing to compare it against.`

#### 2. Structure Beats Polish

The nicer-looking render broke the layout. Admit it looks better first.

`Response A is better because it keeps the three column layout with the sidebar on the left like the reference. Response B has nicer typography and spacing, but it stacks everything into one column.`

#### 3. The Data Miss

Numbers, labels, or headers are wrong. Name the specific value.

`Response B is better because the table headers read Revenue, Cost, and Margin in the same order as the reference. Response A relabels the third column as Profit and changes two of the row totals.`

#### 4. Justifying a Tie

Ties need more evidence than picks. Name what both did.

`Both renders keep the card grid and the same four sections in order. Neither one picks up the reference's dark header bar, so they land in the same place on fidelity.`

### Common Comment Failures

- Talking about the code instead of what the render shows.
- Naming every dimension instead of the one that decided it.
- Calling a render "clean" without saying what it got right.
- Writing a tie comment shorter than a pick comment.

## Final Checklist

- Reference image or frames checked.
- User prompt checked.
- Assets checked if present.
- Both outputs compared side by side.
- Render gate applied.
- Correct frame or scroll position matched.
- Structure, visual quality, and text/data rated separately.
- N/A used only when allowed and truly applicable.
- Overall comment is short and evidence-based.
