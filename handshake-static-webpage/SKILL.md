---
name: handshake-static-webpage
description: Create, evaluate, and answer Handshake Web Dev Agents Static Webpage data-collection tasks. Use when a task asks about writing static webpage descriptions, choosing website reference images, distinguishing reference images from page assets, selecting desktop/tablet/mobile target resolution, or completing the Web Dev Agents Static Webpage Assessment.
---

# Handshake Static Webpage

## Core Rule

Use the Static Webpage assessment instructions as the source of truth:

- `HANDSHAKE-AI/assessments/Web Dev Agents — Static Webpage Assessment.md`

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

For multiple-choice assessment questions, give the selected answer exactly or mark it with `[x]`.

For free-response quality checks, keep the answer brief and concrete:

```markdown
No - the description is too vague because it does not name colors, page sections, layout structure, or mood.
```

For writing a description, produce at least 100 words and describe the page from top to bottom.

## Relationship To Other Handshake Skills

- Use this skill for Static Webpage data-collection briefs and qualification questions.
- Use `handshake-text-to-code-elo-evaluator` only when comparing rendered code outputs A and B.
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
