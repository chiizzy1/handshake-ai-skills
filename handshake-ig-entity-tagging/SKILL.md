---
name: handshake-ig-entity-tagging
description: Perform Handshake IG Entity Tagging tasks. Use when Codex must annotate Instagram video/image content by tagging all visible entities, choosing entity labels/types, finding one reference image per annotation, or applying rules for people, clothing, products, locations, style elements, animals, visible text, and signage.
---

# Handshake IG Entity Tagging

## Core Rule

Use `HANDSHAKE-AI/pdfs/handshake-IG Entity Tagging Task.pdf` as the source of truth.

Before doing a live tagging task, read `references/rubric.md`.

## Minimums

- Tag all visible entities, not just the main subject.
- Aim for at least four complete annotations per image when enough entities are visible.
- Provide one reference photo per annotation.
- The reference image should isolate the entity clearly.

## Entity vs Reference

An entity is the thing you recognize. A reference is a matching image that represents that same entity.

Simple memory rule:

- Entity = noun.
- Reference = representation of the same noun.

Actions are not entities.

## Hard Gates

- Do not stop at the main person or product.
- Do not skip visible clothing, accessories, signage, animals, products, or locations just because they are secondary.
- Do not invent exact brand/model identity when it is not visible.
- Do not use a generic reference when exact identity is visible.
- Do not use a cluttered reference if a clean isolated reference can be found.
- Do not treat an action as an entity. Tag the object or person involved.

## Workflow

1. Watch or inspect the whole Instagram content.
2. List visible entities:
   - people
   - clothing
   - products
   - locations
   - style elements
   - animals
   - visible text/signage
3. Create annotations for all visible entities.
4. Find a clear reference image for each annotation.
5. Prefer cropped or product-style reference images that isolate one entity.
6. Use exact matches when identifiable. Do not settle for generic matches when a specific brand/model/style is visible.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
```

## Final Checklist

- All visible entities considered.
- At least four complete annotations where possible.
- Each annotation has one reference image.
- Reference image isolates the entity.
- Generic references were not used when an exact match was visible.
