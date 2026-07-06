---
name: handshake-h2h-image-evaluator
description: Evaluate Handshake H2H, Text-to-Image, and T2I Magnifier Pairwise image comparison tasks. Use when Codex must compare two AI-generated images from the same text prompt across Overall Preference, Instruction Following, Visual Quality, and Absence of AI Artifacts; when task UI says H2H, T2I, text-to-image-compare, t2i-magnifier-pairwise, magnifier pairwise, or asks which image better follows a prompt.
---

# Handshake H2H Image Evaluator

## Core Rule

Use the H2H/T2I Handshake PDFs and task-specific markdown guidelines as the source of truth:

- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Text-to-Image (T2I).pdf`
- `HANDSHAKE-AI/pdfs/t2i-magnifier-pairwise/guidelines.md`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Read the prompt before looking at the images.
2. List the prompt requirements: subject, count, attributes, style, lighting, composition, text, relationships, and constraints.
3. Inspect both images closely. Zoom into faces, hands, text, edges, shadows, and small objects.
   - For T2I Magnifier Pairwise tasks, use the magnifier/full-resolution viewer whenever available. The magnifier is not a separate rubric; it is the inspection method for finding small prompt misses, artifact tells, text errors, and quality problems.
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

## Preference Severity

- Use "Strongly Prefer" only when the winning response actually succeeds at the core prompt requirements and the losing response clearly fails, or when the quality gap is so large that the loser is basically unusable.
- If both responses fail a core instruction (wrong count, missing subject, broken data accuracy, wrong layout), cap the overall preference at "Slightly Prefer." The winner is just less bad, not genuinely good.
- "Slightly Prefer" is the right call when both share the same fundamental failure but one handles the rest of the prompt better.

## Presentation Template

Always present evaluations using this three-section structure:

### Section 1: Prompt Analysis
Break down the prompt into its core requirements. List the subject, setting, count, attributes, style, and any constraints. This goes under a `### Prompt Analysis` heading.

### Section 2: Image Analysis
Under a `### Image Analysis` heading, analyze each image separately with bold subheadings (`**Image A:**` and `**Image B:**`). For each image, cover:
- How well it follows the prompt instructions
- Whether the logic/rules of the depicted subject make sense
- Any visual quality issues or AI artifacts spotted

Be specific. Point to exact details, scores, text, positions, or objects you can see.

### Section 3: Final Ratings and Justification
List the ratings cleanly under a `### Final Ratings` heading:
```
- Instruction Following: Response A
- Visual Quality: Response A
- Absence of AI Artifacts: Response A
- Overall Preference: Strongly Prefer A
```

Then write a `### Justification` paragraph. Keep it concise and grounded in what you actually saw.

## Tone Rules

- Do not use em dashes. Use commas, periods, or "and" instead.
- Do not sound overly formal or polished. Write like a normal person would talk through their reasoning.
- Avoid phrases like "Upon review of," "demonstrates superior," "holistic assessment," or "semantic elements."
- Keep sentences short and direct. Say what you saw and why it matters.
- It is fine to use casual connectors like "but," "so," "because," and "also."

## Final Checklist

- Prompt requirements were listed mentally.
- Both images were zoomed/inspected.
- Counts, relationships, text, and style were checked.
- Visual Quality and AI Artifacts were not mixed up.
- Ties were avoided unless truly justified.
- Final wording is specific, plain, and image-grounded.
