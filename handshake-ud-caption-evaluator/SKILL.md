---
name: handshake-ud-caption-evaluator
description: Evaluate Handshake UD Caption ELO tasks. Use when an original reference image is compared against two response pairs where each pair includes a generated image and the caption used to generate it, and the task asks for Overall Match, Image Details, Caption Details, Image Hallucination, or Caption Hallucination.
---

# Handshake UD Caption Evaluator

## Core Rule

Use the UD Caption ELO PDFs as the source of truth:

- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-1.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-intermidiate.pdf`
- `HANDSHAKE-AI/guidelines.md` section `UD Caption Elo Task`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Study the original image first.
2. Identify the key visual facts: object count, layout, labels/text, colors, geometry, style, background, and important small details.
3. Read Response A caption and inspect Response A image.
4. Read Response B caption and inspect Response B image.
5. Rate the five criteria independently:
   - Overall Match
   - Image Details
   - Caption Details
   - Image Hallucination
   - Caption Hallucination
6. Do not let a good image rescue a bad caption, or a good caption rescue a bad image.

## Hard Gates

- Do not judge the generated images before studying the original.
- Do not reward a caption for being long if it adds unverifiable details.
- Do not reward a generated image for polish when it changes the original layout or content.
- Do not merge image and caption scores. The task asks for both.
- Do not tie hallucination axes when one side invents a visible object, label, date, measurement, or technical detail.

## Key Principle

This is a fidelity task. Polished, photorealistic, or detailed output is not automatically better. The winner is the response that more faithfully captures the original.

## Output Format

```markdown
- Overall Match: Response A
- Image Details: Response A
- Caption Details: Response B
- Image Hallucination: Response A
- Caption Hallucination: Response A

Justification: A's image is closer to the original layout and geometry. B's caption is more complete, but it invents some technical precision that cannot be verified.
```

## Final Checklist

- Original image was studied before responses.
- Image and caption were judged separately.
- Fine details and labels were checked.
- Hallucination was checked for both image and caption.
- Ties were avoided unless genuinely indistinguishable.
