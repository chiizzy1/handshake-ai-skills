# Handshake Task Router

Use this reference before routing a Handshake task or building new Handshake task rules.

Skill paths below are relative to the skills repo root (the folder containing `handshake-evaluator/`). `HANDSHAKE-AI/...` is a sibling folder of that repo in the workspace root.

## Non-Negotiables

- The relevant Handshake PDF is the single source of truth when one exists. If no PDF exists for a task type, use the visible task instruction panel as the current source of truth.
- Do not apply TELUS (a separate annotation platform with its own rubrics) rules to Handshake. TELUS is only a structural model for skills.
- Do not agree with the user when the PDF points elsewhere.
- Do not rate from a first impression. Read the prompt, inspect the media, then apply the exact task rubric.
- If a task type is unclear, do not guess from the file name alone. Use the UI labels, inputs, and response format.
- If no matching Handshake skill exists, follow the visible task instructions and say that no task-specific skill is available yet.
- Do not mark a response better because it sounds polished. Handshake tasks are about the configured rubric.
- Do not use outside knowledge to override visible evidence. Use it only to verify facts the task actually depends on.

## Strict Rating Protocol

Before any selection, complete these steps:

1. Identify the task type from the UI.
2. Identify every rating axis shown by the UI.
3. Read the prompt or annotation instruction.
4. Inspect all media, including small text, boxes, captions, and reference regions.
5. Decide each axis separately.
6. Write the shortest useful reason, naming concrete visible evidence.

If any step cannot be completed because the media is missing, unreadable, or cropped, state that limitation instead of guessing.

## Shared Handshake Image Foundations

Several image tasks depend on the foundation PDFs:

- Image Evaluation: image evaluation is about whether generated images answer the request, look visually appealing, and avoid telltale AI artifacts.
- How to See: evaluate composition, framing, focus, depth of field, lighting, contrast, color temperature, and saturation using visible evidence.
- Realism & Artifacts: check faces, hands, limbs, materials, text rendering, and scene logic. Use precise visual notes, not vague phrases.

Foundation rules transfer into image comparison tasks only when they support the task-specific rubric. The task-specific PDF still controls the final scale and axis labels.

## Task Families

Quick index. The detailed sections below carry the inputs, axes, and special rules for each family — read the matching one before rating.

| Task cues | Skill | Path |
|---|---|---|
| Prompt + two images, pairwise axes | `handshake-h2h-image-evaluator` | `project-hedgehog/handshake-h2h-image-evaluator/SKILL.md` |
| Prompt + two videos, "less AI-generated" | `handshake-t2v-evaluator` | `project-hedgehog/handshake-t2v-evaluator/SKILL.md` |
| Video-reasoning row audit, queue names, `X out of Y` | `handshake-videorl-evaluator` | `project-hedgehog/handshake-videorl-evaluator/SKILL.md` |
| Media + prompt + two text responses | `handshake-ti2t-evaluator` | `project-hedgehog/handshake-ti2t-evaluator/SKILL.md` |
| Reference image(s) + edit prompt + two outputs | `handshake-r2i-i2i-evaluator` | `project-hedgehog/handshake-r2i-i2i-evaluator/SKILL.md` |
| Input + single edited image, Q1/Q2/Q3 Yes/No | `handshake-i2i-pixel-aligned` | `project-hedgehog/handshake-i2i-pixel-aligned/SKILL.md` |
| Reference image + two image/caption pairs | `handshake-ud-caption-evaluator` | `project-hedgehog/handshake-ud-caption-evaluator/SKILL.md` |
| Two rendered websites side by side | `handshake-visual-coding-evaluator` | `project-hedgehog/handshake-visual-coding-evaluator/SKILL.md` |
| Reference image + two static rendered outputs | `handshake-image2code-evaluator` | `project-hedgehog/handshake-image2code-evaluator/SKILL.md` |
| Single image + dots/notes to place | `handshake-annot-critic` | `project-hedgehog/handshake-annot-critic/SKILL.md` |
| Existing critique to grade 1-5 and rework | `handshake-critique-rework` | `project-hedgehog/handshake-critique-rework/SKILL.md` |
| First-person frames, write a physical-reasoning MCQ | `handshake-ego-phys-understanding` | `project-hedgehog/handshake-ego-phys-understanding/SKILL.md` |
| Grounding prompt + boxes/points/counts | `handshake-find-boundary` | `project-hedgehog/handshake-find-boundary/SKILL.md` |
| Instagram media, annotate visible entities | `handshake-ig-entity-tagging` | `project-hedgehog/handshake-ig-entity-tagging/SKILL.md` |
| Yellow-box target vs reference, same entity? | `handshake-ig-entity-verification` | `project-hedgehog/handshake-ig-entity-verification/SKILL.md` |
| Code render comparison from a text prompt | `handshake-text-to-code-elo-evaluator` | `project-hedgehog/handshake-text-to-code-elo-evaluator/SKILL.md` |
| Web Dev Agents / static webpage data brief | `handshake-static-webpage` | `project-hedgehog/handshake-static-webpage/SKILL.md` |
| Grounding rollout trace, per-attempt Correct/Unnecessary/Incorrect | `handshake-grounding-hard-rollout` | `project-hedgehog/handshake-grounding-hard-rollout/SKILL.md` |
| Two AI artifacts side by side, task-specific rubrics, Pass/Fail | `handshake-multimodal-agent-arena` | `project-hedgehog/handshake-multimodal-agent-arena/SKILL.md` |

### H2H / T2I / T2I Magnifier Pairwise Image Comparison

Inputs:

- One text prompt.
- Two generated images, usually Response A and Response B.
- Optional magnifier or full-resolution compare viewer for close inspection.

Main question:

- Which image better satisfies the prompt on each pairwise image axis?

Skill:

- `handshake-h2h-image-evaluator` (read `project-hedgehog/handshake-h2h-image-evaluator/SKILL.md`)

Axes:

- Overall Preference
- Instruction Following
- Visual Quality
- Absence of AI Artifacts

### T2V / Less AI Generated Video Benchmark

Inputs:

- One text prompt.
- Two generated videos, usually Response A and Response B.
- Sometimes audio requirements.

Main question:

- Which video looks less AI-generated, and which artifact categories are visible in the more AI-generated video?

Skill:

- `handshake-t2v-evaluator` (read `project-hedgehog/handshake-t2v-evaluator/SKILL.md`)

Criteria:

- Prompt adherence.
- Temporal consistency.
- Flicker/shimmer.
- Morphing/deformation.
- Object persistence.
- Physics realism.
- Identity drift.
- Interaction consistency.
- Text/detail stability.
- Audio presence and synchronization when requested.

### VideoRL / Long Context / Cross-Modal Anchoring

Inputs:

- VideoRL guideline or onboarding assessment.
- A proposed video-reasoning row, assessment question, or row audit.
- Usually one short answer, numeric sequence, exact text, quote, or `X out of Y` count.

Main question:

- Is the VideoRL row valid for its queue, or what answer/correction follows from the VideoRL rubric?

Skill:

- `handshake-videorl-evaluator` (read `project-hedgehog/handshake-videorl-evaluator/SKILL.md`)

Queues:

- Audio Anchored Visual Retrieval.
- Visual Anchored Audio Retrieval.
- Tracked AV Counting.
- Exact Temporal Order - Consequence.
- Exact Temporal Order - Repeated Events.
- Sparse Long-Video Retrieval.
- Long Trace-Grounded Counting.
- OCR / Frame-Following Dynamic Text.
- Short Spatial State-Change / Physical Outcome.
- Science & Technical Visual Reasoning.
- Action Anticipation & Prediction.
- Paralinguistic Understanding.
- Audio-Visual Event Alignment.
- Audio-Visual Sound Source Identification.
- Temporal Order - Fine-Grained.
- Temporal Ordering - How-To.

### TI2T / Text Image To Text ELO

Inputs:

- Image or video.
- Current/final user prompt.
- Optional conversation history.
- Two candidate text responses.

Main question:

- Which text response is more acceptable for the current prompt and displayed media?

Skill:

- `handshake-ti2t-evaluator` (read `project-hedgehog/handshake-ti2t-evaluator/SKILL.md`)

Common dimensions:

- Overall
- Factuality
- Instruction Following
- Helpfulness
- Style and Format

Special rule:

- In multi-turn prompts, earlier turns are context only. Rate the current/final turn.

### I2I / R2I / Omni R2I ELO

Inputs:

- One or more reference/input images.
- A text prompt asking for an edit, transformation, or generated image based on the reference.
- Two output images.

Main question:

- Which output made the requested change while preserving what should carry over?

Skill:

- `handshake-r2i-i2i-evaluator` (read `project-hedgehog/handshake-r2i-i2i-evaluator/SKILL.md`)

Axes:

- Overall Preference
- Instruction Following
- Person ID Preservation
- Content / Reference Preservation
- Visual Quality
- Absence of AI Artifacts

### UD Caption ELO

Inputs:

- Original reference image.
- Response A generated image and caption.
- Response B generated image and caption.

Main question:

- Which response better captures the original image and which caption is more accurate?

Skill:

- `handshake-ud-caption-evaluator` (read `project-hedgehog/handshake-ud-caption-evaluator/SKILL.md`)

Criteria:

- Overall Match
- Image Details
- Caption Details
- Image Hallucination
- Caption Hallucination

### Visual Coding / AI Website Generation Evaluation

Inputs:

- One user prompt for a website or web app.
- Optional reference images.
- Optional image assets such as logos or photos.
- Two rendered websites, usually Site A and Site B, loaded side by side.

Main question:

- Which site better follows the prompt, references, assets, visual quality expectations, interactions, and workflows?

Skill:

- `handshake-visual-coding-evaluator` (read `project-hedgehog/handshake-visual-coding-evaluator/SKILL.md`)

Axes:

- Instruction & Reference Fidelity.
- Visual Quality.
- Surface Interactivity.
- Workflow Correctness.
- Overall Preference.

Special rules:

- Interact with both sites before rating.
- Use N/A on live tasks only when a dimension truly does not apply.
- Quiz tasks may use only A is better, Tie, or B is better.

### Image2Code / Image-to-Code Evaluation

Inputs:

- One user prompt that tells the target format.
- One reference image, reference frame set, animation clip, or scrolling website frame set.
- Optional image assets.
- Two static rendered outputs, usually Output A and Output B.

Main question:

- Which output reproduces the reference image or reference frames more faithfully?

Skill:

- `handshake-image2code-evaluator` (read `project-hedgehog/handshake-image2code-evaluator/SKILL.md`)

Axes:

- Structure & Instruction Following.
- Visual Quality.
- Text & Data Accuracy.
- Overall Preference.

Special rules:

- The reference image is the primary spec.
- Apply the render gate first.
- For animation or scrolling tasks, compare each output frame to the matching reference frame.
- Use N/A for Text & Data Accuracy only when allowed and when the reference has no meaningful text.
- Do not test live interactivity unless the task explicitly changes the task type.

### Critique Rework

Inputs:

- An AI-generated image.
- Another reviewer critique with point markers, notes, missed instruction notes, and/or overall feedback.

Main question:

- How good is the critique, and is it worth fixing?

Skill:

- `handshake-critique-rework` (read `project-hedgehog/handshake-critique-rework/SKILL.md`)

Outputs:

- 1-5 critique grade.
- Fix/no-fix decision.
- Reworked markers/notes when fixing.

### Ego Physical Understanding

Inputs:

- First-person image or two related frames.
- Assigned physical reasoning category.

Main question:

- Write an image-dependent multiple-choice question that tests physical reasoning, not object recognition.

Skill:

- `handshake-ego-phys-understanding` (read `project-hedgehog/handshake-ego-phys-understanding/SKILL.md`)

Outputs:

- Question.
- Four answer choices.
- One clearly correct answer.

### Find the Boundary

Inputs:

- Image URL/content.
- A grounding prompt.
- Model answer in bounding box, point, or counting mode.

Main question:

- Did the model ground the prompt correctly, and if not, how should it be corrected?

Skill:

- `handshake-find-boundary` (read `project-hedgehog/handshake-find-boundary/SKILL.md`)

Outputs:

- Pass/fail style verdict.
- Corrected boxes/points/counts when failing.
- Failure tags and confidence where required.

### IG Entity Tagging

Inputs:

- Instagram video/image content.

Main question:

- Which visible entities should be annotated, and what reference images should support them?

Skill:

- `handshake-ig-entity-tagging` (read `project-hedgehog/handshake-ig-entity-tagging/SKILL.md`)

Outputs:

- All visible entity annotations.
- At least four complete annotations per image where possible.
- One isolated reference image per annotation.

### IG Entity Verification

Inputs:

- Target image with a yellow box.
- Reference image or green boxed sub-region.
- Entity type and label.

Main question:

- Do the target and reference refer to the same entity?

Skill:

- `handshake-ig-entity-verification` (read `project-hedgehog/handshake-ig-entity-verification/SKILL.md`)

Verdicts:

- Definitely same
- Likely same
- Likely different
- Definitely different
- Skip
- Flag as bad data

### Grounding Hard Rollout

Inputs:

- An image.
- A grounding prompt.
- Model rollout with thinking, tool calls, tool outputs, and final answer.

Main question:

- Did the model ground the prompt correctly, and was its reasoning process sound?

Skill:

- `handshake-grounding-hard-rollout` (read `project-hedgehog/handshake-grounding-hard-rollout/SKILL.md`)

Workflow:

- Step 1: Blind answer — box targets from image and prompt alone.
- Step 2: Compare blind boxes against dataset target.
- Step 3: Review rollout trace, rate each attempt (Correct/Unnecessary/Incorrect), commit verdict (As-is/Refined trace/Refined answer/Refined both).

Special rule:

- Judge the step, not the outcome. A wrong crop is Incorrect even if the model self-corrects later.

### Multimodal Agent Arena

Inputs:

- A task prompt with optional input materials (images, PDFs, videos, 3D files, code).
- Two AI-generated artifacts (A and B) — can be any type (websites, games, images, data visualizations, slide decks, 3D models, code outputs, reports).
- Task-specific rubric checklist (when present).

Main question:

- Which artifact better fulfills the task?

Skill:

- `handshake-multimodal-agent-arena` (read `project-hedgehog/handshake-multimodal-agent-arena/SKILL.md`)

Criteria:

- Per-rubric Pass/Fail for A and B independently (when rubrics present).
- Overall: Response A / Response B / Tie.
- When no rubrics: instruction following, visual quality, content completeness, usability.

Special rules:

- Interact with both artifacts before rating.
- Overall selection must be coherent with rubric ratings.
- Broken outputs get all-Fail and always lose.
- Functionality matters more than polish.

## Unknown Or New Task Types

When a Handshake task does not match any known type:

1. Read the visible task instructions as the controlling rubric.
2. Inspect the PDF folder for a matching source PDF.
3. If a PDF exists, use it as source of truth and create/adapt a new skill only if the user asks.
4. If no PDF exists, do not invent platform rules. Use the UI instructions and make uncertainty explicit.

## Comment Style

Use short, direct comments:

- Good: `Response B is better because it keeps the lifted group pose and has cleaner faces and hands.`
- Good: `A follows the color instruction, but B changes the product shape, so A is stronger on instruction following.`
- Bad: `Upon careful analysis, the second response demonstrates a superior alignment to the rubric.`

Avoid filler, hedging, and professor-style wording unless the platform requires it.
