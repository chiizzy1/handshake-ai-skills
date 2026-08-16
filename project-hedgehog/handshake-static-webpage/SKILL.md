---
name: handshake-static-webpage
description: Create, evaluate, and answer Handshake Web Dev Agents Static Webpage data-collection tasks. Use when a task asks about writing static webpage descriptions, choosing website reference images, distinguishing reference images from page assets, selecting desktop/tablet/mobile target resolution, or completing the Web Dev Agents Static Webpage Assessment.
---

# Handshake Static Webpage

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use the Static Webpage assessment instructions as the source of truth when they are present:

- `HANDSHAKE-AI/assessments/Web Dev Agents — Static Webpage Assessment.md` (no such file or folder was present at last check; if it is still missing, `references/rubric.md` is the operative rubric and you should say so in your output)

Before answering a live Static Webpage task or assessment, read `references/rubric.md`.

This is not a Text-to-Code ELO task. Do not rate rendered code outputs, compare Response A/B, or use Visual Design / Functionality / Instruction Following axes unless the UI explicitly changes task type.

## Task Shape

Static Webpage data collection teaches an AI how to build websites from a description and reference imagery.

A worker usually must:

1. Write a webpage description of at least 100 words.
2. Upload 1 to 5 reference images that capture the desired vibe, layout, colors, and mood.
3. Optionally upload page assets that should appear directly in the final site.
4. Select a target resolution: desktop, tablet, or mobile.

## Mandatory Workflow

1. Identify the assigned website category, such as Online Store, Blog, News, Services, or Healthcare Booking.
2. Check whether the description is specific enough and at least 100 words.
3. Check whether the description moves top to bottom through the page.
4. Verify that colors, layout structure, sections, and mood are named clearly.
5. Treat reference images as critical inspiration inputs, not optional decoration.
6. Distinguish reference images from page assets.
7. Pick target resolution from the design intent and layout.
8. For assessment questions, choose the exact option that matches these rules.

## Fast Decision Rules

- Vague phrases like "clean, modern, professional, visually appealing" are not enough by themselves.
- A strong description names specific colors, sections, layout structure, and mood.
- Descriptions must be at least 100 words.
- Reference images are the most critical part of the task.
- Use 1 to 5 reference images.
- Reference images can be website screenshots, mockups, or photos that capture the vibe.
- Reference images do not need to be from the exact same category if they clearly express the desired style.
- Page assets are files meant to appear directly in the output, such as logos or background photos.
- Upload logos or specific final-use photos as Page Assets, not Reference Images.
- Desktop is appropriate for multi-column layouts, centered large imagery, and full horizontal navigation.
- Mobile is appropriate when the intended design is a narrow single-column mobile layout.
- Tablet is appropriate only when the intended design is clearly tablet-sized or in-between.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers in a clean markdown format directly in the chat using the exact template below.

This is a brief-writing and question-answering task, so the output is answers, not ratings.

```markdown
### Task Read
[The assigned website category, and which submission step the task is about: description, reference images, page assets, or target resolution.]

### Answers
**Q1. [restate the question or the decision being made]**
Answer: [the exact option or value, such as Desktop, up to 5, or Page Assets]
Why: [one or two lines naming the rule that decides it]

**Q2. [next question]**
Answer: [...]
Why: [...]

[Continue for every question the assessment asks. The rubric's Assessment Answer Key Logic covers Q1 through Q8.]

### Checks Applied
[Name the rules you used, such as the 100-word minimum, the 1 to 5 reference image range, page assets versus reference images, or the layout-to-resolution mapping.]
```

When the task asks you to draft or validate a description rather than answer questions, put the draft or the verdict under Answers and keep the same structure.

## Answer Style

The `Why:` line is one or two lines naming the rule that decides it. Short and plain.

**The Persona: someone who knows the rule and just says it.**

1. **Name the rule, not the reasoning path.** "The range is 1 to 5, and six were attached" beats "the submission exceeds the permitted quantity of reference materials."
2. **Do not restate the question.** The answer already sits above it.
3. **Short sentences. Periods.** No em dashes, no semicolons.
4. **Avoid hedging.** If the rule decides it, say so.

**Banned phrases:** "demonstrates," "it is evident that," "Upon review of," "in accordance with," "the aforementioned."

Good

`Why: Page assets are files that belong on the page itself. A logo the site will display is an asset, not an inspiration reference.`

Good

`Why: The description is 74 words, which is under the 100-word minimum.`

Bad

`Why: Upon review of the submission criteria, the aforementioned materials do not satisfy the requisite classification standard.`

When drafting a description, write it the way a person describing a website would. Name the colors, sections, and layout plainly, and skip words like "seamless," "vibrant," "cutting-edge," and "immersive."

## Relationship To Other Handshake Skills

- Use this skill for Static Webpage data-collection briefs and qualification questions.
- Use `handshake-text-to-code-elo-evaluator` (read `../handshake-text-to-code-elo-evaluator/SKILL.md`) only when comparing rendered code outputs A and B.
- Use visual design foundations only as background when describing reference images, not as an ELO scoring rubric.

## Final Checklist

- Task is Static Webpage, not code-output comparison.
- Description is at least 100 words if writing or validating a submission.
- Description includes colors, layout, sections, and mood.
- Reference images are present and treated as critical.
- Reference image count is between 1 and 5.
- Page assets are separated from inspiration references.
- Target resolution matches the design intent.
- Final answer follows the assessment's requested format.
