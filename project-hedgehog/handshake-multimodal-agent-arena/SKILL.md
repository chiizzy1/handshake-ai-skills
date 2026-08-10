---
name: handshake-multimodal-agent-arena
description: Evaluate Handshake Multimodal Agent Arena tasks. Use when comparing two AI-generated artifacts side by side (websites, games, images, data visualizations, slide decks, 3D models, code outputs, reports); when rating per-rubric Pass/Fail for Response A and Response B independently; when picking an overall A/B/Tie winner; or when the task says Multimodal Agent Arena, artifact comparison, or side-by-side build evaluation.
---

# Handshake Multimodal Agent Arena

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/project-hedgehog-pdfs/Project Hedgehog - multimodal-agent-arena.pdf` as the source of truth.

Before doing a live task, read `references/rubric.md`.

This is not a code-only or website-only comparison. Artifacts can be anything the model produced — websites, games, images, data visualizations, slide decks, 3D models, code outputs, reports, or anything else. Adapt your evaluation to the artifact type.

## Task Shape

Multimodal Agent Arena items show:

1. **A task prompt** — describes what the AI was asked to do. May include text instructions, images, PDFs, videos, 3D files, code, or other input materials.
2. **Two artifacts (A and B)** — the AI's outputs. Could be any type of generated content.
3. **A checklist of rubrics (when present)** — success criteria written specifically for this task. Not every prompt has rubrics.

## Mandatory Workflow

1. Read the task prompt and reference all provided materials before looking at the outputs.
2. Keep the prompt and all input materials visible the entire time you are annotating.
3. Open and interact with both outputs. If they are websites or games, click around and try things. If they are slide decks, browse through every slide. If they are images or reports, examine them carefully.
4. Rate each rubric independently (when rubrics are present).
5. Pick overall quality: Response A, Response B, or Tie.
6. Write specific, evidence-backed comments that point at real behavior.

## Rubric Evaluation

Rubrics are task-specific success criteria that change every time. They can be:

- **Objective**: "Did it produce the file?" "Does the page include a navigation bar?"
- **Subjective**: "Does the layout look clean?" "Is the visualization easy to read?"

Both are valid — use your best judgment on subjective ones.

For each rubric criterion, rate Response A and Response B **independently**:

- **Pass / Good** — the response satisfies this criterion.
- **Fail / Bad** — the response does not satisfy this criterion.

*(Note: Depending on the task UI version, buttons may be labeled **Pass/Fail** or **Good/Bad**.)*

You are not picking a winner per rubric. You are judging each response on its own merits.

### When No Rubrics Are Shown

Evaluate based on overall quality:

- Instruction following
- Visual quality
- Content completeness
- Usability

## Overall Selection

Pick Response A, Response B, or Tie. Your overall selection **must be coherent** with your rubric ratings and written justification.

- If B is marked Fail and A is marked Pass on all rubrics, A should be the preferred response overall.
- Use Tie **sparingly** — only when both responses are genuinely equal in quality. There is almost always a slight edge one way.

## Hard Gates

- Do not judge by first impressions. Interact with both artifacts before rating.
- Do not default to giving the same Pass/Fail pattern across every dimension. Rate each criterion independently.
- Do not give credit to a partially-loaded or index-only build for criteria like "fulfills the requested experience," "interactive," or "responsive."
- A broken output should always lose to a working one. If one output completely fails to load or render, mark all its rubrics Fail and pick the other.
- Functionality matters more than polish. A visually polished build is not better if it is broken, incomplete, overflowing, or unusable. A simpler build that actually works and fulfills the task should be treated as stronger.
- Do not write generic comments like "both are good." Point to actual issues or behaviors you observed.
- The A/B labels shown in the tool do not change after submission. Make sure your selected winner, rubric ratings, and justification all refer to the correct response.
- Treat each rubric as roughly equal weight unless one is clearly more central to the task.

## When to Skip

Skip only when:

- The prompt is in a language you cannot read.
- The task is clearly broken or nonsensical.

Do not skip because the task is unfamiliar. You do not need to be a domain expert — rubrics tell you what to look for.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Answer in the chat.

```markdown
### Prompt Analysis
[What was the AI asked to do? Summarize the key requirements from the prompt and input materials.]

### Artifact Interaction
[What did you observe when interacting with Response A? Response B? Note specific behaviors, broken elements, missing sections, or standout features.]

### Rubric Ratings (when rubrics are present)
| Rubric | Response A | Response B |
|---|---|---|
| [Criterion 1] | Pass/Fail | Pass/Fail |
| [Criterion 2] | Pass/Fail | Pass/Fail |
| ... | ... | ... |

### Overall Selection
[Response A | Response B | Tie]

### Justification
[Specific, evidence-backed comment pointing at real behavior. Name concrete issues or strengths.]
```

## Comment Style Guidelines

When writing justification comments or answering free-response assessment questions:

- **Sound like a natural human**: Write in clear, straightforward, conversational English. Speak like a real human reviewer explaining their findings to a teammate.
- **Keep it concise and evidence-grounded**: 1–2 sentences pointing out exact behavior (e.g., broken links, missing sections, failed renders, working features).
- **Avoid stiff AI fluff & academic jargon**: Do NOT write robotic phrases like *"Upon meticulous inspection of both candidates," "Response A demonstrates superior alignment,"* or *"it is evident that."*
- **Examples**:
  - *Good*: "Response A generated the requested 3D model file (`birthday_cake_character.scad`), while Response B completely failed to render. A broken output that produces nothing must lose to one that delivers the file."
  - *Good*: "Response B is fully functional with working links to all 4 executive profiles, whereas Response A has broken links that fail to open."
  - *Bad*: "Upon careful analysis, Response A exhibits optimal aesthetic polish, whereas Response B demonstrates non-trivial structural defects across multiple criteria."

## QA Rubric (How Submissions Are Graded)

| Score | Meaning |
|---|---|
| 5 — Exceptional | Thorough rubric-by-rubric analysis, interacted with both artifacts, rating clearly justified by specific rubric outcomes. |
| 4 — Strong | Good rubric coverage, reasonable rating, minor gaps in interaction or justification. |
| 3 — Acceptable | Rating seems correct but rubric analysis is shallow or incomplete. |
| 2 — Weak | Rating not well justified, rubrics mostly ignored, or did not interact with artifacts. |
| 1 — Unacceptable | Wrong rating, completely ignored rubrics, or did not examine the artifacts. |

## Relationship To Other Handshake Skills

- Use `handshake-visual-coding-evaluator` (read `../handshake-visual-coding-evaluator/SKILL.md`) for Visual Coding / AI Website Generation tasks that specifically compare rendered websites with the five-axis rubric (Instruction & Reference Fidelity, Visual Quality, Surface Interactivity, Workflow Correctness, Overall Preference).
- Use `handshake-text-to-code-elo-evaluator` (read `../handshake-text-to-code-elo-evaluator/SKILL.md`) for Text-to-Code ELO tasks with the three-dimension rubric (Visual Design, Functionality, Instruction Following).
- Use this skill for Multimodal Agent Arena tasks where artifacts can be any type of generated content (not just websites) and rubrics are task-specific and variable.

## Final Checklist

- Prompt and all input materials read before examining outputs.
- Both artifacts interacted with (not just looked at).
- Each rubric rated independently for A and B.
- Overall selection coherent with rubric ratings and comment.
- Comment points to specific, observed issues — not generic praise.
- Broken outputs marked Fail on all rubrics.
- Tie used only when genuinely equal.
- A/B labels verified before submission.
