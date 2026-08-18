# Handshake Multimodal Agent Arena Rubric

Use this reference for Multimodal Agent Arena tasks.

## Contents

- [Source Materials](#source-materials)
- [Task Goal](#task-goal)
- [What You See in a Task](#what-you-see-in-a-task)
- [What Are Rubrics?](#what-are-rubrics)
- [Evaluation Workflow](#evaluation-workflow)
- [The 30-Second Check](#the-30-second-check)
- [Editable Rubrics](#editable-rubrics)
- [When No Rubrics Are Present](#when-no-rubrics-are-present)
- [Key Rules](#key-rules)
- [Good vs Bad Examples](#good-vs-bad-examples)
- [QA Rubric (How Submissions Are Graded)](#qa-rubric-how-submissions-are-graded)
- [When to Skip](#when-to-skip)
- [Core Evaluation Tips & Principles](#core-evaluation-tips-principles)
- [Pre-Submission Checklist (7-Point Verification)](#pre-submission-checklist-7-point-verification)
- [Common Mistakes](#common-mistakes)
- [Final Checklist](#final-checklist)

## Source Materials

- `HANDSHAKE-AI/multimodal-task/multimodal-guidelines.md` — current source of truth.
- `HANDSHAKE-AI/project-hedgehog-pdfs/Project Hedgehog - multimodal-agent-arena.pdf` — older; where the two disagree, the guidelines file wins.

## Task Goal

Compare two AI-generated artifacts in separate tabs and judge which one better fulfills the task. Each task comes with its own rubrics (when present) — use them as your scorecard. You rate each response independently on the criteria, then complete the overall preference ratings.

## What You See in a Task

1. **A task prompt and input materials** — describes what the AI was asked to do. Includes text instructions and may include images, videos, PDFs, code, 3D files, or other data.
2. **Response A and Response B tabs** — one generated artifact each: website, HTML page, app, game, PDF, report, image, data visualization, slide deck, 3D model, code output, or anything else. Each response begins loading when you open its tab.
3. **A checklist of rubrics (when present)** — success criteria written specifically for this task. They tell you exactly what to look for. Not every prompt has rubrics, and on some comparisons they are editable.
4. **Overall rating dimensions** — compare A and B and select the appropriate preference strength.

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

### 2. Open Both Tabs and Review Both Artifacts

Open Response A, let it load, and test it. Then do the same for Response B. Both tabs must be opened before Submit unlocks, and opening a tab is what starts that response loading — never call an unopened tab blank. Switch between tabs freely and test comparable features in each.

Do not judge any artifact from its first screen:

- **Websites, HTML pages, and apps** — **use them, do not just look at them**. Click the nav, buttons, forms, links, search and filters; scroll; check links go where they claim. Render raw HTML rather than reading the source.
- **Games** — click inside the output first to give it focus. Follow on-screen control hints, then try arrows, WASD, Space, Enter, mouse movement and clicks. Press Escape to release pointer lock.
- **PDFs and reports** — page through the whole document and check the content against the prompt. "It opened" is not a pass.
- **Slide decks** — browse through **every slide** before deciding.
- **Images, data visualizations, code outputs, 3D models** — examine them carefully; confirm files were actually produced and do what was asked.

### 3. Apply the 30-Second Check

If either output is completely blank or unusable after 30 seconds, reject the comparison (see below) instead of rating it.

### 4. Review the Rubrics

When editing controls are present, edit only where the rules in [Editable Rubrics](#editable-rubrics) allow. Otherwise leave them as written.

### 5. Rate Each Rubric (When Present)

For each criterion, rate Response A and Response B independently:

- **Good** or **Bad** for A
- **Good** or **Bad** for B

*(Some task UI versions label these Pass/Fail.)*

You are not picking a winner per rubric. You are judging each response on its own merits — both may be Good, both may be Bad, or they may differ. Complete every rubric before submitting. When no rubrics are shown, skip this step and evaluate on overall quality.

### 6. Complete the Overall Ratings

Fill in every required overall rating dimension. Where a preference strength is asked for, match it to the size of the gap you observed: a single missing section is a slight edge, a build that fails most of the rubrics against one that passes them is a strong one. Use Tie only when both are genuinely equal in quality — if one is even slightly better, pick that one.

## The 30-Second Check

Give each response up to 30 seconds after opening its tab.

**Still loading** — a spinner is moving, content is appearing, the page is visibly making progress, or part of a usable interface has rendered. Keep waiting and inspect it once loading finishes. Never reject something that is gradually rendering.

**Broken or blank** — after 30 seconds it is still a white or black screen, shows only an error, displays only a tiny unusable fragment, is permanently stuck on a loading screen, or otherwise gives you no interface to judge.

If either response is broken or blank after the wait, select **Reject Sample → One or both outputs have a broken/blank interface**. That rejects the comparison instead of recording a preference vote, and one completely broken output is enough.

Do **not** reject because an output is unattractive, incomplete, misses prompt requirements, has some broken interactions, or is simply lower quality. Rate those differences.

## Editable Rubrics

Rubrics are editable only on some comparisons. When the controls are present:

- **Remove** a criterion that is impossible to assess from the prompt and available materials, or that clearly does not apply.
- **Clarify** a genuinely unclear criterion when a small wording change makes its intended requirement judgeable.
- **Correct** a criterion that clearly contradicts the prompt or refers to unavailable material.
- Preserve the original intent whenever possible, and apply the edited criterion equally to Response A and Response B.

Never edit a rubric to favor an output or to turn a failure into a pass. Do not edit merely because one response fails the criterion, or because it is difficult to check. If the rubric is already clear and applicable, leave it unchanged.

## When No Rubrics Are Present

Evaluate based on:

- Instruction following
- Visual quality
- Content completeness
- Usability

## Key Rules

### Coherence

Your overall selection **must match** your rubric ratings and written justification. If your rubrics and comment clearly favor B, your final selection should not be A.

### Interaction Required

A partially-loaded or index-only build should not receive credit for criteria such as "fulfills the requested experience," "interactive," or "responsive." You must actually try both builds.

### Functionality Over Polish

A visually polished build is not better if it is broken, incomplete, overflowing, or unusable. A simpler build that actually works and fulfills the task should be treated as stronger.

### Blank Interfaces Are Rejected, Weak Ones Are Rated

If an output's interface is completely blank or unusable after the 30-second check, reject the comparison — do not rate it and do not record a preference vote.

If it renders but is weak, incomplete, or partly broken, rate it. Mark the criteria it fails as Bad and pick the other response. A rendered-but-failing deliverable (an empty spreadsheet, a model file that never got written) is also a rating case, not a rejection.

### Equal Weight

Treat each rubric as roughly equal weight unless one is clearly more central to the task.

### Specific Comments

Avoid generic comments like "both are good." Point to actual issues or behaviors you observed — broken buttons, missing sections, incorrect answers, text overflow, failed images/icons, incomplete functionality, or anything else that supports your choice.

### Natural Human Tone & Style

Full rules and worked examples live in the skill's "How to Write (Tone Rules)" section. The short version:

- **Length**: 1-3 sentences, always.
- **Style**: Write like an average person casually explaining something to a friend.
- **Focus**: Lead with the big obvious difference. Do not nitpick small things when something major is broken or missing.
- **Vocabulary**: Basic and direct. No academic words, no long chains of adjectives.
- **Punctuation**: No em dashes. No colons unless it is for a list.
- **Banned phrases**: "Upon review of", "Upon meticulous evaluation", "demonstrates superior", "optimal aesthetic polish", "holistic assessment", "it is evident that", "demonstrating a severe lack of".
- **Good Example**: *"Response A actually made the 3D model file. Response B gave back nothing, so there is nothing to compare."*
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
| Hero section with image | Good | Good |
| Menu grid with 6+ items | Good | Good |
| Working contact form | Good | Bad — missing |
| Responsive layout | Good | Bad — not responsive |

Overall: Response A (4/4 Good vs B's 2/4).

Why this is good: Clear rubric-driven comparison. A satisfies all criteria, B misses two. Response A is the clear winner.

**Bad evaluation**: "A looks nicer." → Slightly Prefer A.

Why this is bad: No rubric analysis. "Looks nicer" is not grounded in the specific criteria. Always reference which rubrics each output passes or fails.

### Example 2: One Output Stays Blank

**Input**: Create an interactive data dashboard.
Response A: Loads and shows charts. Response B: still a completely white screen more than 30 seconds after its tab was opened.

**Good evaluation**: Reject Sample → One or both outputs have a broken/blank interface. One completely broken output is enough to reject the comparison.

**Bad evaluation**: Mark all of B's rubrics Bad and pick A. (There is no interface to judge — this is a rejection, not a preference vote.)

### Example 3: One Output Is Rendered but Faulty

**Input**: Same dashboard task.
Response A works. Response B renders but has a broken filter button and a missing chart.

**Good evaluation**: Rate both. B is marked Bad on the criteria it misses, and A wins on the overall preference.

**Bad evaluation**: Reject the comparison. (A rendered but low-quality interface gets rated. Rejection is only for a blank or wholly unusable render after the waiting period.)

### Example 4: Editing a Rubric

**Input**: The prompt requests a website and provides no reference image. An editable rubric says "Matches the supplied reference image exactly."

**Good evaluation**: Remove the inapplicable criterion — the referenced material does not exist — then rate the remaining criteria for both A and B.

**Bad input**: The prompt requires a working search field. Response A's search is broken, Response B's works.

**Bad evaluation**: Remove the search rubric because A cannot pass it. (Never edit or remove a valid criterion to protect an output from a failure.)

### Example 5: Testing Game Controls

**Input**: Both tabs show a game title screen reading "WASD to move, mouse to aim."

**Good evaluation**: Click inside each game, use WASD and the mouse, test the core interaction, and press Escape if the pointer gets locked.

**Bad evaluation**: Compare only the title screens and visual styling. (This misses the requested interaction and hides major functional differences.)

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

Reject Sample is a separate action with one trigger: an output whose interface is still completely blank or unusable 30 seconds after its tab was opened.

Do not skip because the task is unfamiliar. You do not need to be a domain expert — rubrics tell you what to look for.

## Core Evaluation Tips & Principles

1. **Interact, don't just look**: Interact with anything interactive — games, websites, apps. Click inside first, then click around and try things.
2. **Read the whole thing**: Browse every slide in a deck, page through the whole PDF or report, and render HTML rather than reading its source.
3. **Unfamiliar tasks are fine**: Don't worry if the task is unfamiliar. You don't need to be a domain expert — rubrics tell you what to look for.
4. **Neither has to be perfect**: It's okay if neither output is perfect. Judge each one independently, then pick the better one overall.
5. **Rubrics carry equal weight**: Treat each rubric as roughly equal weight unless one is clearly more central to the task.
6. **Blank means reject, weak means rate**: A blank or unusable interface after 30 seconds rejects the comparison. Anything that renders gets rated, however poor.
7. **Use Tie sparingly**: Use Tie sparingly — only when both responses are genuinely equal. There is almost always a slight edge one way.

## Pre-Submission Checklist (7-Point Verification)

1. [ ] **Did I read the prompt and reference all provided materials from the prompt?**
2. [ ] **Did I open both tabs and give each up to 30 seconds to load?**
3. [ ] **Did I actually try both builds, testing comparable actions in each?**
4. [ ] **If I edited a rubric, was the edit allowed and applied equally to A and B?**
5. [ ] **Did I rate every rubric independently for both responses?**
6. [ ] **Does my overall selection and preference strength match my ratings and comment?** *(Comment applies if justification box is present below overall rating)*
7. [ ] **Did I explain the specific issues that support my choice?** *(Applies if justification box is present below overall rating)*

## Common Mistakes

- Judging by first impressions instead of interacting with both artifacts.
- Deciding an unopened tab is blank, or rejecting a response that is still visibly rendering.
- Rejecting the comparison for a rendered but low-quality output.
- Rating a completely blank interface instead of rejecting the comparison.
- Writing "both are good" or "A looks nicer" without grounding in rubric criteria.
- Giving the same Good/Bad across every dimension without actually checking each one.
- Editing or removing a rubric because one response fails it.
- Preferring a polished but broken build over a simpler but functional one.
- Not browsing all slides in a deck, not paging through a PDF, or not clicking through a website.
- Overall selection that contradicts the rubric ratings.

## Final Checklist

- Prompt and all materials read first.
- Both tabs opened, each given up to 30 seconds.
- Both artifacts interacted with, not just viewed.
- Blank or unusable interface after 30 seconds → Reject Sample.
- Rubric edits justified and applied equally to A and B.
- Each rubric rated independently for A and B.
- Every required overall rating dimension completed.
- Overall selection and preference strength coherent with ratings and comment.
- Comment references specific observed behavior.
- Tie used only when genuinely indistinguishable.
- A/B labels verified before submission.
