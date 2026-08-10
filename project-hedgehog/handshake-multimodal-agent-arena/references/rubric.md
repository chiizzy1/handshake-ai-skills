# Handshake Multimodal Agent Arena Rubric

Use this reference for Multimodal Agent Arena tasks.

## Contents

- [Source PDF](#source-pdf)
- [Task Goal](#task-goal)
- [What You See in a Task](#what-you-see-in-a-task)
- [What Are Rubrics?](#what-are-rubrics)
- [Evaluation Workflow](#evaluation-workflow)
- [When No Rubrics Are Present](#when-no-rubrics-are-present)
- [Key Rules](#key-rules)
- [Good vs Bad Examples](#good-vs-bad-examples)
- [QA Rubric (How Submissions Are Graded)](#qa-rubric-how-submissions-are-graded)
- [When to Skip](#when-to-skip)
- [Core Evaluation Tips & Principles](#core-evaluation-tips-principles)
- [Pre-Submission Checklist (5-Point Verification)](#pre-submission-checklist-5-point-verification)
- [Common Mistakes](#common-mistakes)
- [Final Checklist](#final-checklist)

## Source PDF

- `HANDSHAKE-AI/project-hedgehog-pdfs/Project Hedgehog - multimodal-agent-arena.pdf`

## Task Goal

Compare two AI-generated artifacts side by side and judge which one better fulfills the task. Each task comes with its own rubrics (when present) — use them as your scorecard. You rate each response independently on the criteria, then pick an overall winner: Response A, Response B, or Tie.

## What You See in a Task

1. **A task prompt** — describes what the AI was asked to do. Includes text instructions and may include images, PDFs, videos, 3D files, code, or other input materials.
2. **Two artifacts (A and B)** — the AI's outputs. Could be websites, games, images, data visualizations, slide decks, 3D models, code outputs, reports, or anything else the model produced.
3. **A checklist of rubrics (when present)** — success criteria written specifically for this task. They tell you exactly what to look for. Not every prompt has rubrics.

## What Are Rubrics?

Rubrics are a list of things the output should achieve. They are written specifically for each task, so they change every time. Think of them as a scorecard.

Rubrics can be objective or subjective:

- Objective: "The page includes all major sections from the reference: navigation bar, hero banner, product grid, and footer."
- Objective: "A PNG image is saved for each frame with the detected contour drawn as an overlay."
- Objective: "The output is a single index.html file with inline CSS and no external dependencies."
- Subjective: "Does the layout look clean?" "Is the visualization easy to read?"

Both are valid — use your best judgment on subjective ones.

## Evaluation Workflow

### 1. Read the Task Prompt

Understand what was being asked before you look at the outputs. Look at all the input materials — images, reference files, attached documents.

### 2. Review Both Artifacts

Open and interact with both outputs:

- Websites, games, or apps — **use them, do not just look at them**. Click around, try things.
- Slide decks — browse through **every slide** before deciding.
- Images, reports, data visualizations — examine them carefully.

### 3. Rate Each Rubric (When Present)

For each criterion, rate Response A and Response B independently:

- **Pass** or **Fail** for A
- **Pass** or **Fail** for B

You are not picking a winner per rubric. You are judging each response on its own merits. When no rubrics are shown, skip this step and evaluate on overall quality.

### 4. Pick Overall Quality

Response A or Response B — whichever better fulfills the task overall. Use Tie only when both are genuinely equal in quality. If one is even slightly better, pick that one.

## When No Rubrics Are Present

Evaluate based on:

- Instruction following
- Visual quality
- Content completeness
- Usability

## Key Rules

### Coherence

Your overall A/B/Tie selection **must match** your rubric ratings and written justification. If your rubrics and comment clearly favor B, your final selection should not be A.

### Interaction Required

A partially-loaded or index-only build should not receive credit for criteria such as "fulfills the requested experience," "interactive," or "responsive." You must actually try both builds.

### Functionality Over Polish

A visually polished build is not better if it is broken, incomplete, overflowing, or unusable. A simpler build that actually works and fulfills the task should be treated as stronger.

### Broken Outputs Lose

If one output completely fails to load or render, mark all its rubrics Fail and pick the other. A broken output should always lose to a working one.

### Equal Weight

Treat each rubric as roughly equal weight unless one is clearly more central to the task.

### Specific Comments

Avoid generic comments like "both are good." Point to actual issues or behaviors you observed — broken buttons, missing sections, incorrect answers, text overflow, failed images/icons, incomplete functionality, or anything else that supports your choice.

### Natural Human Tone & Style

- **Sound like a real person**: Write in simple, natural, conversational English. Speak like a human reviewer explaining their findings to a colleague.
- **Keep it to 1–2 concise sentences**: Focus strictly on observable evidence (working features, broken links, missing content).
- **No AI jargon or fluff**: Avoid robotic phrases like *"Upon meticulous evaluation," "demonstrates superior alignment,"* or *"it is evident that."*
- **Good Example**: *"Response A generated the requested 3D model file (`birthday_cake_character.scad`), while Response B completely failed to render. A broken output must lose to one that delivers the file."*
- **Bad Example**: *"Upon careful analysis, Response A exhibits optimal aesthetic polish, whereas Response B demonstrates non-trivial structural defects across multiple criteria."*

### Label Awareness

The A/B labels shown in the tool do not change after submission. Make sure your selected winner, rubric ratings, and justification all refer to the correct response.

## Good vs Bad Examples

### Example 1: Website Task

**Input**: Build a restaurant landing page with hero, menu grid, and contact form.
**Rubrics**: (1) Hero section with image, (2) Menu grid with at least 6 items, (3) Working contact form, (4) Responsive layout.

**Good evaluation**:

| Rubric | Response A | Response B |
|---|---|---|
| Hero section with image | Pass | Pass |
| Menu grid with 6+ items | Pass | Pass |
| Working contact form | Pass | Fail — missing |
| Responsive layout | Pass | Fail — not responsive |

Overall: Response A (4/4 Pass vs B's 2/4 Pass).

Why this is good: Clear rubric-driven comparison. A satisfies all criteria, B misses two. Response A is the clear winner.

**Bad evaluation**: "A looks nicer." → Slightly Prefer A.

Why this is bad: No rubric analysis. "Looks nicer" is not grounded in the specific criteria. Always reference which rubrics each output passes or fails.

### Example 2: One Output Fails to Load

**Input**: Create an interactive data dashboard.
Design A: Loads and shows charts. Design B: Blank white page, console errors.

**Good evaluation**: Design B completely fails to render — no output visible. All B rubrics marked Fail. Overall: Response A.

**Bad evaluation**: "Both seem okay." → Slightly Prefer A. (One output is broken — this is wrong.)

## QA Rubric (How Submissions Are Graded)

| Score | Meaning |
|---|---|
| 5 — Exceptional | Thorough rubric-by-rubric analysis, interacted with both artifacts, rating clearly justified by specific rubric outcomes. |
| 4 — Strong | Good rubric coverage, reasonable rating, minor gaps in interaction or justification. |
| 3 — Acceptable | Rating seems correct but rubric analysis is shallow or incomplete. |
| 2 — Weak | Rating not well justified, rubrics mostly ignored, or did not interact with artifacts. |
| 1 — Unacceptable | Wrong rating, completely ignored rubrics, or did not examine the artifacts. |

## When to Skip

Skip only when:

- The prompt is in a language you cannot read.
- The task is clearly broken or nonsensical.

Do not skip because the task is unfamiliar. You do not need to be a domain expert — rubrics tell you what to look for.

## Core Evaluation Tips & Principles

1. **Interact, don't just look**: Interact with anything interactive — games, websites, apps. Click around, try things.
2. **Browse every slide**: For slide decks, browse every slide before deciding — don't judge by the first slide alone.
3. **Unfamiliar tasks are fine**: Don't worry if the task is unfamiliar. You don't need to be a domain expert — rubrics tell you what to look for.
4. **Neither has to be perfect**: It's okay if neither output is perfect. Judge each one independently, then pick the better one overall.
5. **Rubrics carry equal weight**: Treat each rubric as roughly equal weight unless one is clearly more central to the task.
6. **Broken outputs lose**: If one output completely fails (doesn't load, produces nothing, or is clearly broken), mark all its rubrics Fail/Bad and pick the other.
7. **Use Tie sparingly**: Use Tie sparingly — only when both responses are genuinely equal. There is almost always a slight edge one way.

## Pre-Submission Checklist (5-Point Verification)

1. [ ] **Did I read the prompt and reference all provided materials from the prompt?**
2. [ ] **Did I actually try both builds?**
3. [ ] **Did I rate each rubric independently?**
4. [ ] **Does my final A/B/Tie choice match my ratings and comment?** *(Comment applies if justification box is present below overall rating)*
5. [ ] **Did I explain the specific issues that support my choice?** *(Applies if justification box is present below overall rating)*

## Common Mistakes

- Judging by first impressions instead of interacting with both artifacts.
- Writing "both are good" or "A looks nicer" without grounding in rubric criteria.
- Giving the same Pass/Fail across every dimension without actually checking each one.
- Preferring a polished but broken build over a simpler but functional one.
- Not browsing all slides in a deck, or not clicking through a website.
- Giving a broken output anything other than all-Fail.
- Overall selection that contradicts the rubric ratings.

## Final Checklist

- Prompt and all materials read first.
- Both artifacts interacted with, not just viewed.
- Each rubric rated independently for A and B.
- Overall selection coherent with ratings and comment.
- Comment references specific observed behavior.
- Broken outputs get all-Fail.
- Tie used only when genuinely indistinguishable.
- A/B labels verified before submission.
