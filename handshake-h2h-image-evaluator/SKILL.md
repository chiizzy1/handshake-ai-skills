---
name: handshake-h2h-image-evaluator
description: Evaluate Handshake H2H and Text-to-Image image comparison tasks. Use when Codex must compare two AI-generated images from the same text prompt across Overall Preference, Instruction Following, Visual Quality, and Absence of AI Artifacts; when task UI says H2H, T2I, text-to-image-compare, or asks which image better follows a prompt.
---

# Handshake H2H Image Evaluator

## Core Rule

Use the H2H/T2I Handshake PDFs as the source of truth:

- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Text-to-Image (T2I).pdf`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Read the prompt before looking at the images.
2. List the prompt requirements: subject, count, attributes, style, lighting, composition, text, relationships, and constraints.
3. Inspect both images closely. Zoom into faces, hands, text, edges, shadows, and small objects.
4. Rate each axis independently:
   - Overall Preference
   - Instruction Following
   - Visual Quality
   - Absence of AI Artifacts
5. Avoid ties unless both images are genuinely indistinguishable on that axis.
6. Write a short justification with concrete visual evidence.

## Hard Gates

- Do not rate from image appeal alone.
- Do not reward an image for adding dramatic elements that the prompt did not request.
- Do not ignore count, text, or relationship errors because the image looks realistic.
- Do not treat stylization as an artifact when the prompt asks for that style.
- Do not call an axis a tie when one image has a visible prompt, quality, or artifact advantage on that axis.

## Axis Separation

- Instruction Following: prompt compliance only.
- Visual Quality: craft, composition, detail, color, exposure, framing, and seamlessness.
- Absence of AI Artifacts: AI tells such as bad anatomy, waxy skin, garbled text, impossible lighting, distorted objects, and broken logic.
- Overall Preference: holistic, based on what the user wanted. Instruction following usually matters more than small visual polish gaps.

Do not double-penalize artifacts under Visual Quality unless the artifact also harms normal craft quality. Put AI tells in Absence of AI Artifacts.

## Output Format

For checkbox/radio tasks, answer with the selected choices only when the user wants speed:

```markdown
- Overall Preference: Response A
- Instruction Following: Response B
- Visual Quality: Response A
- Absence of AI Artifacts: Response A

Justification: Response A keeps both animals mid-fall and has cleaner anatomy. Response B loses a dog leg and the cat's face is distorted.
```

For explanation requests, add one short sentence per axis.

## Final Checklist

- Prompt requirements were listed mentally.
- Both images were zoomed/inspected.
- Counts, relationships, text, and style were checked.
- Visual Quality and AI Artifacts were not mixed up.
- Ties were avoided unless truly justified.
- Final wording is specific, plain, and image-grounded.
