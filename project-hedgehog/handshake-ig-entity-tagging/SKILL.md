---
name: handshake-ig-entity-tagging
description: Perform Handshake IG Entity Tagging tasks. Use when asked to annotate Instagram video/image content by tagging all visible entities, choosing entity labels/types, finding one reference image per annotation, or applying rules for people, clothing, products, locations, style elements, animals, visible text, and signage.
---

# Handshake IG Entity Tagging

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-IG Entity Tagging Task.pdf` as the source of truth.

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

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your annotations in a clean markdown format directly in the chat using the exact template below.

```markdown
### Visible Entity Scan
[Walk the scan order: people, clothing and shoes, accessories and bags, products and packaging, animals, places and landmarks, visible text/logos/signage, style elements.]

### Annotations
1. **Entity:** [noun at the most specific level the image supports]
   **Type:** [person / clothing / product / location / style element / animal / text or signage]
   **Reference image:** [what the reference shows and where it came from, e.g. official product page]
   **Why this level:** [one line on why this is the right specificity for what is visible]

2. **Entity:** ...

[Aim for at least four complete annotations when enough entities are visible. One reference image per annotation.]

### Skipped Or Uncertain
[Any visible entity you could not annotate, and why. Write "none" if everything visible was tagged.]
```

## Final Checklist

- All visible entities considered.
- At least four complete annotations where possible.
- Each annotation has one reference image.
- Reference image isolates the entity.
- Generic references were not used when an exact match was visible.
