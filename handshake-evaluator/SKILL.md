---
name: handshake-evaluator
description: Router and source-of-truth controller for Handshake AI task work. Use when asked to rate, audit, create, verify, or structure Handshake tasks; when task type is unclear; when working from HANDSHAKE-AI/guidelines.md or HANDSHAKE-AI/pdfs; or when deciding which Handshake task-specific skill/rubric should apply.
---

# Handshake Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `../project-hedgehog/handshake-*/...` are Project Hedgehog task skill folders.
- `../project-lizard/lizard-*/...` are Project Lizard task skill folders.
- `../project-gaffer/gaffer-*/...` are Project Gaffer task skill folders.
- `../shared-references/...` are cross-project shared references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/task-router.md` in this skill folder as the operative routing reference and state that the source file was unavailable.

## Core Rule

Use the Handshake PDF for the specific task type as the highest authority. Use `HANDSHAKE-AI/guidelines.md` as a broad working summary only. If the user, this skill, an old answer, or general instinct conflicts with the PDF, follow the PDF.

Do not be agreeable for its own sake. Be cooperative with the user, but be loyal to the Handshake rubric.

Before routing or rating a live task, read `references/task-router.md`.

## Hard Gates

- Do not rate before reading the task prompt, visible media, response text, and rating labels.
- Do not use TELUS (a separate annotation platform with its own rubrics) rules, labels, or scoring logic on Handshake tasks.
- Do not infer hidden intent when the UI or PDF gives the rule.
- Do not select a tie to avoid a hard call. Use a tie only when the relevant rubric allows it and there is no meaningful visible difference.
- Do not invent image details. If a detail cannot be seen, treat it as unknown.
- Do not let the user's suggested answer control the rating. Check it against the PDF and visible evidence.
- When factual knowledge outside the task is needed, verify it before using it.

## Source Hierarchy

1. The relevant PDF in `HANDSHAKE-AI/project-hedgehog-pdfs/`, when one exists.
2. `HANDSHAKE-AI/hedgehog-extracted/docs/` for task types that have no PDF. These are the extracted Handshake training pages and are the highest local authority for the IG Video Pairs family and IG Entity Tagging Videos. They are extracted training material, not an official PDF — say so when you cite them. `HANDSHAKE-AI/project-gaffer/extracted/` plays the same role for Project Gaffer, which has no PDF at all.
3. The task UI instructions and visible prompt/media for the current item.
4. Task-specific Handshake skill reference files.
5. `HANDSHAKE-AI/guidelines.md`.
6. User preference or prior chat memory.

If a task depends on current real-world facts outside the image or prompt, verify with reliable sources before rating. Do not use outside research to override what the task asks you to judge visually.

## Routing Workflow

1. Read the current task text, visible images/video, prompt, response options, and rating UI labels.
2. Identify the task type from the UI and inputs.
3. **Identify the project**: Determine whether the task belongs to **Project Hedgehog**, **Project Lizard**, or **Project Gaffer** (or another project). Use the task UI labels, queue name, and visible cues. Project Hedgehog tasks involve image/video/code comparison, grounding, annotation, and entity tagging. Project Lizard tasks involve BabyVision (BV) and VQA workflows. Project Gaffer tasks are video captioning production in SuperAnnotate: one video, four captions, two tracks, no rating.
4. Load the matching task-specific skill from the correct project folder and its reference file.
5. If the task type is not covered, use the visible task instructions and PDF if available. Do not force a near-matching skill.
6. Apply the task-specific workflow exactly.
7. Keep the final answer compact and natural unless the user asks for full reasoning.

## Task Type Map

### Project Hedgehog

- Text Image To Text ELO / TI2T: use `handshake-ti2t-evaluator` (read `../project-hedgehog/handshake-ti2t-evaluator/SKILL.md`).
- Text-to-Video / T2V / Less AI Generated video artifact benchmark: use `handshake-t2v-evaluator` (read `../project-hedgehog/handshake-t2v-evaluator/SKILL.md`).
- Text-to-Image / H2H image comparison: use `handshake-h2h-image-evaluator` (read `../project-hedgehog/handshake-h2h-image-evaluator/SKILL.md`).
- Image-to-Image, Reference-to-Image, Omni R2I ELO with A/B preference axes: use `handshake-r2i-i2i-evaluator` (read `../project-hedgehog/handshake-r2i-i2i-evaluator/SKILL.md`).
- i2i Pixel Aligned / Project Hedgehog Q1-Q2-Q3 Yes/No edit checks: use `handshake-i2i-pixel-aligned` (read `../project-hedgehog/handshake-i2i-pixel-aligned/SKILL.md`).
- Ads Creative visual appeal / Compare Two Ad Images (two finished ad images, one five-button appeal call, ignore overlaid text): use `handshake-ads-visual-appeal` (read `../project-hedgehog/handshake-ads-visual-appeal/SKILL.md`).
- UD Caption ELO: use `handshake-ud-caption-evaluator` (read `../project-hedgehog/handshake-ud-caption-evaluator/SKILL.md`).
- Annot Critic: use `handshake-annot-critic` (read `../project-hedgehog/handshake-annot-critic/SKILL.md`).
- Critique Rework: use `handshake-critique-rework` (read `../project-hedgehog/handshake-critique-rework/SKILL.md`).
- Ego Physical Understanding: use `handshake-ego-phys-understanding` (read `../project-hedgehog/handshake-ego-phys-understanding/SKILL.md`).
- Find the Boundary: use `handshake-find-boundary` (read `../project-hedgehog/handshake-find-boundary/SKILL.md`).
- IG Entity Tagging (creating annotations on IG media): use `handshake-ig-entity-tagging` (read `../project-hedgehog/handshake-ig-entity-tagging/SKILL.md`).
- IG Entity Verification (one yellow-box target vs one reference, same/different verdict): use `handshake-ig-entity-verification` (read `../project-hedgehog/handshake-ig-entity-verification/SKILL.md`).
- IG Entity Tagging Videos (QA pass on an already-tagged clip: video checks, duplicate references, per-reference identity, frame boxing): use `handshake-ig-entity-tagging-video` (read `../project-hedgehog/handshake-ig-entity-tagging-video/SKILL.md`).
- IG Editing Convo (source two Reels that form a conversation): use `handshake-ig-editing-convo` (read `../project-hedgehog/handshake-ig-editing-convo/SKILL.md`).
- IG Audio Recreation (source a pair where the output redoes the input's audio): use `handshake-ig-audio-recreation` (read `../project-hedgehog/handshake-ig-audio-recreation/SKILL.md`).
- IG BTS (pair a finished clip with the making-of that exact shot): use `handshake-ig-bts` (read `../project-hedgehog/handshake-ig-bts/SKILL.md`).
- Sync a Video Pair / IG Temporal Alignment (review a sourced pair, keep or reject, align the shared moment): use `handshake-ig-temporal-alignment` (read `../project-hedgehog/handshake-ig-temporal-alignment/SKILL.md`).
- IG Video Temporal Alignment V2 — Review (audit another Fellow's Sync a Video Pair submission, grade 1-5): use `handshake-ig-temporal-alignment-review` (read `../project-hedgehog/handshake-ig-temporal-alignment-review/SKILL.md`).
- Web Dev Agents / Static Webpage data collection briefs: use `handshake-static-webpage` (read `../project-hedgehog/handshake-static-webpage/SKILL.md`).
- Text-to-Code ELO / Code Render Comparison: use `handshake-text-to-code-elo-evaluator` (read `../project-hedgehog/handshake-text-to-code-elo-evaluator/SKILL.md`).
- Image2Code / Image-to-Code reference-image recreation comparison: use `handshake-image2code-evaluator` (read `../project-hedgehog/handshake-image2code-evaluator/SKILL.md`).
- Visual Coding / AI Website Generation side-by-side rendered website comparison: use `handshake-visual-coding-evaluator` (read `../project-hedgehog/handshake-visual-coding-evaluator/SKILL.md`).
- VideoRL / Long Context VideoRL / Cross-Modal Anchoring: use `handshake-videorl-evaluator` (read `../project-hedgehog/handshake-videorl-evaluator/SKILL.md`).
- Grounding Hard Rollout / rollout trace review with per-attempt ratings: use `handshake-grounding-hard-rollout` (read `../project-hedgehog/handshake-grounding-hard-rollout/SKILL.md`).
- Multimodal Agent Arena / two AI-generated artifacts side by side with task-specific rubrics: use `handshake-multimodal-agent-arena` (read `../project-hedgehog/handshake-multimodal-agent-arena/SKILL.md`).

### Project Lizard

- BabyVision (BV) tasks (image review, question writing, model response generation, evaluate & rewrite, prompt validation): use `lizard-babyvision-evaluator` (read `../project-lizard/lizard-babyvision-evaluator/SKILL.md`).
- VQA tasks (question writing, stumping strategies, model response generation, evaluate & rewrite, prompt validation): use `lizard-vqa-evaluator` (read `../project-lizard/lizard-vqa-evaluator/SKILL.md`).
- Reviewer / QC & Audit tasks (evaluating LLM Judge, handling skipped/unusable tasks, and verifying answers): use `lizard-reviewer-evaluator` (read `../project-lizard/lizard-reviewer-evaluator/SKILL.md`).

### Project Gaffer

- Video Omni Caption / Project Gaffer (correct four pre-generated captions across two tracks — Speech Transcription, Speech Characteristics, Visual, Audio — then pass the Autochecker and route in SuperAnnotate): use `gaffer-video-annotator` (read `../project-gaffer/gaffer-video-annotator/SKILL.md`).
- Project Gaffer **reviewing** (R1 layer: fix and approve someone else's task, thumbs up and save every annotation, grade on 10 criteria, route to Hold or QC_Return): same skill, read `../project-gaffer/gaffer-video-annotator/references/reviewer-workflow.md`.

Gaffer is production annotation, not rating. Do not apply Hedgehog or Lizard rating logic to it, and do not look for a Gaffer PDF — its source of truth is the extracted training site under `HANDSHAKE-AI/project-gaffer/extracted/`.

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
2. **Watch out for the overly-AI look in the edit:** Look for unnaturally crisp edges, flat lighting, plasticky textures, or over-saturated colors in the edited area. An edit can look impressive at first glance but feel artificial on closer look - do not let that initial wow factor automatically win.
3. **Watch out for text issues:** AI edits often add text where it doesn't belong or keep it sharp when it should be soft (far away, off-angle, or out of focus). Cluttered or unnaturally crisp text shouldn't win on visual impact alone.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your answers and ratings in clean markdown directly in the chat.

For pairwise A/B tasks use this shape:

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[2 to 3 sentences naming the one difference that decided it. Follow Comment Style in `references/task-router.md`, and the routed skill's own style section when one applies.]
```

For all other task types, use the output format defined in the routed task-specific skill.

## Final Checklist

Before answering:

- Confirm the task type.
- Confirm the relevant PDF/rubric.
- Confirm no TELUS-specific labels or rules leaked into Handshake work.
- Confirm all visible prompt/media/response content was read.
- Confirm every rating follows the task-specific scale.
- Confirm the final comment names concrete evidence and does not sound padded or overly formal.
