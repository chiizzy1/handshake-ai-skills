---
name: handshake-evaluator
description: Router and source-of-truth controller for Handshake AI task work. Use when Codex is asked to rate, audit, create, verify, or structure Handshake tasks; when task type is unclear; when working from HANDSHAKE-AI/guidelines.md or HANDSHAKE-AI/pdfs; or when deciding which Handshake task-specific skill/rubric should apply.
---

# Handshake Evaluator

## Core Rule

Use the Handshake PDF for the specific task type as the highest authority. Use `HANDSHAKE-AI/guidelines.md` as a broad working summary only. If the user, this skill, an old answer, or general instinct conflicts with the PDF, follow the PDF.

Do not be agreeable for its own sake. Be cooperative with the user, but be loyal to the Handshake rubric.

Before routing or rating a live task, read `references/task-router.md`.

## Hard Gates

- Do not rate before reading the task prompt, visible media, response text, and rating labels.
- Do not use TELUS rules, labels, or scoring logic on Handshake tasks.
- Do not infer hidden intent when the UI or PDF gives the rule.
- Do not select a tie to avoid a hard call. Use a tie only when the relevant rubric allows it and there is no meaningful visible difference.
- Do not invent image details. If a detail cannot be seen, treat it as unknown.
- Do not let the user's suggested answer control the rating. Check it against the PDF and visible evidence.
- When factual knowledge outside the task is needed, verify it before using it.

## Source Hierarchy

1. The relevant PDF in `HANDSHAKE-AI/pdfs/`, when one exists.
2. The task UI instructions and visible prompt/media for the current item.
3. Task-specific Handshake skill reference files.
4. `HANDSHAKE-AI/guidelines.md`.
5. User preference or prior chat memory.

If a task depends on current real-world facts outside the image or prompt, verify with reliable sources before rating. Do not use outside research to override what the task asks you to judge visually.

## Routing Workflow

1. Read the current task text, visible images/video, prompt, response options, and rating UI labels.
2. Identify the task type from the UI and inputs.
3. Load the matching task-specific Handshake skill and its reference file.
4. If the task type is not covered, use the visible task instructions and PDF if available. Do not force a near-matching skill.
5. Apply the task-specific workflow exactly.
6. Keep the final answer compact and natural unless the user asks for full reasoning.

## Task Type Map

- Text Image To Text ELO / TI2T: use `handshake-ti2t-evaluator`.
- Text-to-Image / H2H image comparison: use `handshake-h2h-image-evaluator`.
- Image-to-Image, Reference-to-Image, Omni R2I ELO: use `handshake-r2i-i2i-evaluator`.
- UD Caption ELO: use `handshake-ud-caption-evaluator`.
- Annot Critic: use `handshake-annot-critic`.
- Critique Rework: use `handshake-critique-rework`.
- Ego Physical Understanding: use `handshake-ego-phys-understanding`.
- Find the Boundary: use `handshake-find-boundary`.
- IG Entity Tagging: use `handshake-ig-entity-tagging`.
- IG Entity Verification: use `handshake-ig-entity-verification`.
- Text-to-Code ELO / Code Render Comparison: use `handshake-text-to-code-elo-evaluator`.

## Universal Rules

- Inspect images closely. Zoom into faces, hands, text, edges, labels, markers, and small objects.
- Ground every judgment in visible evidence or task-provided text.
- Score dimensions independently when the UI has multiple dimensions.
- Avoid ties unless the relevant PDF allows them and the compared outputs are genuinely indistinguishable on that axis.
- Do not let visual polish hide instruction failures.
- Do not let one axis bleed into another unless the PDF says the issue belongs on both axes.
- Use plain human comments: short, specific, and tied to image details.
- If the rating UI asks only for selections, provide selections. If it asks for justification, keep it short and evidence-based.

## Overall Preference Eval Task Cues

When evaluating for overall preference, you MUST strictly adhere to these three hard rules:

1. **Look it up if you don't know:** When a prompt involves specialized knowledge (technical, historical, scientific, cultural, anatomical alignment), check a reliable source instead of guessing. Do not make assumptions.
2. **Watch out for the overly-AI look in the edit:** Look for unnaturally crisp edges, flat lighting, plasticky textures, or over-saturated colors in the edited area. An edit can look impressive at first glance but feel artificial on closer look — do not let that initial wow factor automatically win.
3. **Watch out for text issues:** AI edits often add text where it doesn't belong or keep it sharp when it should be soft (far away, off-angle, or out of focus). Cluttered or unnaturally crisp text shouldn't win on visual impact alone.

## Final Checklist

Before answering:

- Confirm the task type.
- Confirm the relevant PDF/rubric.
- Confirm no TELUS-specific labels or rules leaked into Handshake work.
- Confirm all visible prompt/media/response content was read.
- Confirm every rating follows the task-specific scale.
- Confirm the final comment names concrete evidence and does not sound padded or overly formal.
