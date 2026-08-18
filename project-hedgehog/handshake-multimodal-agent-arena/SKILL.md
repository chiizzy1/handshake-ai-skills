---
name: handshake-multimodal-agent-arena
description: Evaluate Handshake Multimodal Agent Arena tasks. Use when comparing two AI-generated artifacts in separate tabs (websites, HTML pages, games, PDFs, reports, images, data visualizations, slide decks, 3D models, code outputs); when rating each rubric Good/Bad for Response A and Response B independently; when deciding whether to Reject Sample for a blank or broken output; when editing rubrics that are marked editable; or when the task says Multimodal Agent Arena, artifact comparison, or side-by-side build evaluation.
---

# Handshake Multimodal Agent Arena

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/multimodal-task/multimodal-guidelines.md` as the source of truth. Where it disagrees with the older `HANDSHAKE-AI/project-hedgehog-pdfs/Project Hedgehog - multimodal-agent-arena.pdf`, the guidelines file wins.

Before doing a live task, read `references/rubric.md`.

This is not a code-only or website-only comparison. Artifacts can be anything the model produced — websites, games, images, data visualizations, slide decks, 3D models, code outputs, reports, or anything else. Adapt your evaluation to the artifact type.

## Task Shape

Multimodal Agent Arena items show:

1. **A task prompt and input materials** — describes what the AI was asked to do. May include text instructions, images, videos, PDFs, code, 3D files, or other data.
2. **Response A and Response B tabs** — each tab holds one generated artifact: website, app, game, visualization, slide deck, report, PDF, or anything else. Each response begins loading when you open its tab.
3. **Rubric criteria** — task-specific requirements, rated Good or Bad for each response. Not every task has them, and on some comparisons they are editable.
4. **Overall rating dimensions** — compare A and B and select the appropriate preference strength.

## Mandatory Workflow

1. Read the task prompt and inspect every input file before looking at the outputs.
2. Keep the prompt and all input materials in mind the entire time you are annotating.
3. Open Response A. Let it load, then test it.
4. Open Response B. Let it load, then test it.
5. If either output is completely blank or unusable after 30 seconds, Reject Sample and stop (see below).
6. Review the rubrics and, when editing controls are present, edit them only where the rules below allow.
7. Rate every rubric Good or Bad for A and B independently.
8. Complete every required overall rating dimension.
9. Write specific, evidence-backed comments that point at real behavior, then submit.

## Tab Mechanics

Both tabs must be opened before the Submit button unlocks. Opening a tab is what starts or continues that response loading, so never decide an unopened tab is blank. Switch between the tabs as often as you need, and compare the same features and workflows in both.

## The 30-Second Check

Give each response up to 30 seconds after opening its tab.

**Still loading** — a spinner is moving, content is appearing, the page is visibly making progress, or part of a usable interface has rendered. Keep waiting, then inspect it once loading finishes. Never reject something that is gradually rendering.

**Broken or blank** — after 30 seconds it is still a white or black screen, shows only an error, displays only a tiny unusable fragment, is permanently stuck on a loading screen, or otherwise gives you no interface to judge.

If either response is broken or blank after the 30 seconds, select **Reject Sample → One or both outputs have a broken/blank interface**. This rejects the comparison instead of recording a preference vote. One completely broken output is enough to reject.

Do **not** reject for poor design, missing prompt requirements, minor visual bugs, some broken interactions, or generally low quality. Those are rating issues — rate them.

## Interacting With Each Artifact Type

Do not judge any artifact from its first screen.

- **Websites and apps** — click through the nav, test buttons, forms, links, scrolling, and any search or filter. Check whether links go where they claim.
- **Raw HTML files** — render them, do not read the source and assume. Judge what actually appears in the browser.
- **Games** — click inside the response first to give the embedded output focus. Follow any on-screen control instructions, then try common controls: arrow keys, WASD, Space, Enter, mouse movement, mouse clicks. Press Escape if the pointer gets locked. Test comparable actions in A and B. A game that renders but has poor controls or broken mechanics is a quality failure to rate, not a rejection.
- **PDFs and reports** — page through the whole document. Check the content against what the prompt asked for; "it opened" is not a pass.
- **Slide decks** — browse every slide before deciding.
- **Images, charts, and visualizations** — examine them closely for accuracy, labelling, and readability.
- **Code outputs and files** — check the file was actually produced and does what the prompt asked.
- **3D models** — rotate and inspect the geometry where the viewer allows it.

## Rubric Evaluation

Rubrics are task-specific success criteria that change every time. They can be:

- **Objective**: "Did it produce the file?" "Does the page include a navigation bar?"
- **Subjective**: "Does the layout look clean?" "Is the visualization easy to read?"

Both are valid — use your best judgment on subjective ones.

For each rubric criterion, rate Response A and Response B **independently**:

- **Good / Pass** — the response satisfies this criterion.
- **Bad / Fail** — the response does not satisfy this criterion.

*(Note: Depending on the task UI version, buttons may be labeled **Good/Bad** or **Pass/Fail**.)*

You are not picking a winner per rubric. You are judging each response on its own merits. Both may be Good, both may be Bad, or they may differ. Complete every rubric rating before submitting.

### Editable Rubrics

Only some comparisons allow rubric editing. When the editing controls are present:

- **Remove** a criterion that is impossible to assess from the prompt and available materials, or that clearly does not apply. Example: the rubric says "Matches the supplied reference image exactly" but the prompt supplied no reference image.
- **Clarify** a genuinely unclear criterion when a small wording change makes its intended requirement judgeable.
- **Correct** a criterion that clearly contradicts the prompt or refers to unavailable material.
- Preserve the original intent wherever possible, and apply the edited criterion equally to A and B.

Never edit a rubric to favor an output or to turn a failure into a pass. Do not remove a criterion merely because one response fails it, because it is hard to check, or to make your preferred response look better. If a criterion is already clear and applicable, leave it alone.

### When No Rubrics Are Shown

Evaluate based on overall quality:

- Instruction following
- Visual quality
- Content completeness
- Usability

## Overall Selection

Complete every required overall rating dimension. Where the UI asks for a preference strength (for example strongly prefer A / slightly prefer A / tie / slightly prefer B / strongly prefer B), pick the strength that matches the size of the gap you actually observed — a single missing section is a slight edge, a build that fails most of the rubrics against one that passes them is a strong one.

Your overall selection **must be coherent** with your rubric ratings and written justification.

- If B is marked Bad and A is marked Good on all rubrics, A should be the preferred response overall.
- Use Tie **sparingly** — only when both responses are genuinely equal in quality. There is almost always a slight edge one way.

## Hard Gates

- Do not judge by first impressions. Interact with both artifacts before rating.
- Do not default to giving the same Good/Bad pattern across every dimension. Rate each criterion independently.
- Do not give credit to a partially-loaded or index-only build for criteria like "fulfills the requested experience," "interactive," or "responsive."
- If an output is completely blank or unusable after the 30-second check, Reject Sample. Do not rate it and do not record a preference vote.
- An output that renders but is weak, incomplete, or partly broken gets rated, never rejected. Mark the criteria it fails as Bad and pick the other response.
- Functionality matters more than polish. A visually polished build is not better if it is broken, incomplete, overflowing, or unusable. A simpler build that actually works and fulfills the task should be treated as stronger.
- Do not write generic comments like "both are good." Point to actual issues or behaviors you observed.
- The A/B labels shown in the tool do not change after submission. Make sure your selected winner, rubric ratings, and justification all refer to the correct response.
- Treat each rubric as roughly equal weight unless one is clearly more central to the task.

## When to Skip vs When to Reject

**Skip** only when:

- The prompt is in a language you cannot read.
- The task is clearly broken or nonsensical.

**Reject Sample** is a different action, and it is for one thing: an output whose interface is still completely blank or unusable 30 seconds after its tab was opened. Choose the "One or both outputs have a broken/blank interface" reason.

Do not skip because the task is unfamiliar. You do not need to be a domain expert — rubrics tell you what to look for.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Answer in the chat.

```markdown
### Prompt Analysis
[What was the AI asked to do? Summarize the key requirements from the prompt and input materials.]

### Artifact Interaction
[What did you observe when interacting with Response A? Response B? Note what you clicked or paged through, plus specific behaviors, broken elements, missing sections, or standout features. Note the 30-second outcome if either output was slow or blank.]

### Rubric Edits (only when rubrics are editable and an edit was warranted)
[Which criterion was removed or reworded, and why. Omit this section if nothing was edited.]

### Rubric Ratings (when rubrics are present)
| Rubric | Response A | Response B |
|---|---|---|
| [Criterion 1] | Good/Bad | Good/Bad |
| [Criterion 2] | Good/Bad | Good/Bad |
| ... | ... | ... |

### Overall Selection
[Response A | Response B | Tie, with the preference strength the UI asks for. Or "Reject Sample → One or both outputs have a broken/blank interface"]

### Justification
[1-3 sentences. Write like you are explaining it to a friend. No big words, no em dashes. Just say what you saw.]
```

## How to Write (Tone Rules)

**This section is critical. Read these examples EVERY TIME before writing your justification or answering a free-response question.** Same rules as `../handshake-h2h-image-evaluator/SKILL.md`.

### Rules

- **Length:** Justifications must always be 1-3 sentences total.
- **Focus:** Talk about the big, obvious difference. Do not nitpick small details when something major is broken or missing.
- **Style:** Write like an average person casually explaining something to a friend. Keep it simple and natural.
- **Vocabulary:** Do NOT use big academic words or long chains of adjectives. Keep it basic and direct. Say "broken" not "non-functional", "missing" not "absent from the deliverable".
- **Punctuation:** No em dashes. No colons unless it is for a list. Use commas, periods, or "and" instead.
- **Banned Phrases:** Never use "Upon review of," "Upon meticulous inspection," "demonstrates superior," "optimal aesthetic polish," "holistic assessment," "it is evident that," "non-trivial structural defects," or "demonstrating a severe lack of."

### Bad vs. Good Examples (Study These)

Every "Bad" example sounds robotic or over-analytical. Every "Good" example says the same thing like a normal person would.

- *Bad (Academic/Stiff):* "Upon careful analysis, Response A exhibits optimal aesthetic polish, whereas Response B demonstrates non-trivial structural defects across multiple criteria."
- *Good (Average Human):* "Response A looks nicer but half its buttons do nothing. Response B is plainer and everything actually works."

- *Bad (Wordy/Over-explaining):* "Response B is much better because it provides clean, organized navigation elements that correctly route the user to the intended destination pages. Response A is a confusing mess where the links resolve to nonexistent endpoints."
- *Good (Punchy/Direct):* "Response B is better because every profile link opens the right page. In Response A the last two links go to a 404."

- *Bad (Robotic/Jargon):* "Response A successfully generated the requested three-dimensional asset file, while Response B failed to produce any renderable output whatsoever."
- *Good (Conversational):* "Response A actually made the 3D model file. Response B gave back nothing, so there is nothing to compare."

- *Bad (Too vague):* "Response A is more complete and better organized than Response B."
- *Good (Specific but casual):* "Response A is a real 22 page report with numbers and sources in every section. Response B repeats the same placeholder line about detailed analysis being included later."

### The Four Patterns

Most arena comments are one of these. Match the shape to the situation.

**1. One Delivered Nothing.** An empty or failed deliverable loses to anything that works. Say what came out. (If the *interface itself* is blank or unusable after 30 seconds, reject the comparison instead of writing this comment.)

`Response A produced the working spreadsheet with all three tabs filled in. Response B returned an empty file, so there is nothing to compare.`

**2. The Broken Interaction.** Something on the page does not work when you use it. Name what you clicked.

`Response B is better because every profile link opens the right page. In Response A the last two links go to a 404.`

**3. Missing What Was Asked.** The artifact works but skipped part of the request.

`Response A is better because it includes the summary section and the chart the prompt asked for. Response B looks tidier, but it never adds the chart.`

**4. Justifying a Tie.** Ties need more evidence than picks. Name what both did.

`Both agents built the same three pages and the nav works in each one. Neither one wires up the search box, so they land in the same place.`

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
- Both tabs opened, each given up to 30 seconds to load.
- Both artifacts interacted with (not just looked at), testing comparable actions in each.
- Blank/unusable interface after 30 seconds → Reject Sample, not a rating.
- Rubric edits, if any, were justified by the editing rules and applied equally to A and B.
- Every rubric rated Good/Bad independently for A and B.
- Every required overall rating dimension completed, with a preference strength matching the observed gap.
- Overall selection coherent with rubric ratings and comment.
- Comment points to specific, observed issues — not generic praise.
- Tie used only when genuinely equal.
- A/B labels verified before submission.
