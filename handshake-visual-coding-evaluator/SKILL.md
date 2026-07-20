---
name: handshake-visual-coding-evaluator
description: Evaluate Handshake Visual Coding and AI Website Generation side-by-side tasks. Use when comparing two rendered websites or web apps from the same prompt across Instruction & Reference Fidelity, Visual Quality, Surface Interactivity, Workflow Correctness, and Overall Preference.
---

# Handshake Visual Coding Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use the Visual Coding guidelines as the source of truth when they are present:

- `HANDSHAKE-AI/pdfs/visual-coding.md` (no such file was present at last check; if it is still missing, `references/rubric.md` is the operative rubric and you should say so in your output)

Before rating a live task, read `references/rubric.md`.

## Task Shape

You compare two rendered websites or web apps, usually Site A and Site B, generated from the same user prompt.

The task may include:

- user prompt text;
- reference images or mockups;
- image assets, logos, photos, or product files;
- two live rendered websites in iframes;
- a live-task 5 point scale, or a quiz 3 option scale.

## Workflow

1. Read the user prompt and keep it visible.
2. Inspect all reference images and provided assets.
3. Open both websites side by side.
4. Scroll both pages and compare matching sections.
5. Interact with both sites before rating. Click buttons, nav links, tabs, dropdowns, forms, carousels, galleries, media controls, and any element that looks interactive.
6. Test multi-step flows when the prompt implies forms, carts, wizards, navigation, submissions, or persistence.
7. Rate each dimension independently.
8. Write a short 2 to 3 sentence overall justification with concrete evidence.

## Hard Gates

- Do not rate from a screenshot or first glance when the site is interactive.
- Do not mark N/A when an interactive element exists. Surface Interactivity applies whenever anything looks clickable or accepts input.
- Do not default to Tie when a dimension does not apply. Use N/A on live tasks.
- Do not use N/A on quiz tasks when the quiz only offers A is better, Tie, or B is better.
- Do not penalize a site for not using assets when no assets were provided.
- Do not force every provided asset into the site. Some assets may be noise.
- Do not let visual polish hide missing required sections, wrong assets, or broken workflows.
- If one site completely fails to load, mark it much worse on every applicable live-task dimension.

## Dimensions

Live tasks use these four dimensions plus Overall Preference:

- Instruction & Reference Fidelity
- Visual Quality
- Surface Interactivity
- Workflow Correctness

Quiz tasks may collapse the scale to:

- A is better
- Tie
- B is better

Use the exact labels shown by the task UI.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Establish the objective facts from the user prompt, reference images, and provided assets. This is what both sites are measured against.]

### Response Analysis
**Response A:**
[What it built correctly, what it missed, and what happened when you interacted with it.]

**Response B:**
[What it built correctly, what it missed, and what happened when you interacted with it.]

### Final Ratings
- Instruction & Reference Fidelity: [A much better / A slightly better / Tie / B slightly better / B much better]
- Visual Quality: [A much better / A slightly better / Tie / B slightly better / B much better]
- Surface Interactivity: [A much better / A slightly better / Tie / B slightly better / B much better]
- Workflow Correctness: [A much better / A slightly better / Tie / B slightly better / B much better]
- Overall Preference: [A much better / A slightly better / Tie / B slightly better / B much better]

Use the exact labels shown by the task UI. On live tasks, N/A is available when a dimension truly does not apply. On quiz tasks the scale may collapse to A is better / Tie / B is better, and N/A is not offered.

### Justification
[2 to 3 sentences naming the deciding dimension and concrete evidence. Write like a normal person testing websites.]
```

## Comment Style

Write like a normal person testing websites, not like a code reviewer. Keep it short and concrete.

Good:

`Response B is better because its checkout flow works from cart to confirmation, while A's Place Order button does nothing. A looks a little cleaner, but the broken checkout matters more.`

Bad:

`Response B demonstrates superior architectural compliance and therefore wins the evaluation.`

## Final Checklist

- Prompt, references, and assets were checked.
- Both websites were opened and interacted with.
- Render failures were handled first.
- Each dimension was rated separately.
- N/A was used only when allowed and truly applicable.
- Overall justification names the main deciding dimension and concrete evidence.
