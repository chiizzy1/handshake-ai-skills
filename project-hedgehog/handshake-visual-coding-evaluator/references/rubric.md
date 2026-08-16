# Handshake Visual Coding Rubric

Use this reference for Visual Coding and AI Website Generation side-by-side tasks.

## Contents

- [Source](#source)
- [Main Idea](#main-idea)
- [Rating Scales](#rating-scales)
- [Dimension 1 - Instruction & Reference Fidelity](#dimension-1---instruction-reference-fidelity)
- [Dimension 2 - Visual Quality](#dimension-2---visual-quality)
- [Dimension 3 - Surface Interactivity](#dimension-3---surface-interactivity)
- [Dimension 4 - Workflow Correctness](#dimension-4---workflow-correctness)
- [Overall Preference](#overall-preference)
- [Render Failure Rule](#render-failure-rule)
- [N/A Rules](#na-rules)
- [Comment Style](#comment-style)
- [Final Checklist](#final-checklist)

## Source

- `HANDSHAKE-AI/project-hedgehog-pdfs/visual-coding.md` (no such file was present at last check; if it is still missing, this rubric is the operative source)

## Main Idea

You compare two rendered websites from the same prompt. The winner is the site that better serves the prompt, references, assets, and expected user behavior.

Do not judge by appearance alone. Actually use the websites.

## Rating Scales

Live tasks usually use:

| Rating | Meaning |
|---|---|
| A much better | A is clearly and significantly stronger |
| A slightly better | A has a noticeable but small edge |
| Tie | Both are roughly equal |
| B slightly better | B has a noticeable but small edge |
| B much better | B is clearly and significantly stronger |

Use N/A only when the dimension truly does not apply.

Quiz tasks may use only:

- A is better
- Tie
- B is better

For quiz tasks, do not use N/A.

## Dimension 1 - Instruction & Reference Fidelity

Ask whether the site built what was requested.

Check:

- required sections, components, text, ordering, theme, and workflow;
- provided assets in the correct roles, such as logo in header or product photo in product card;
- reference image layout, structure, palette, typography, and distinctive motifs.

Rules:

- The prompt is the authority.
- Not every asset must be used.
- Penalize missing relevant assets, wrong asset placement, forced irrelevant assets, and ignored reference motifs.
- If no assets were provided, skip the asset check.
- If no references were provided, skip the reference check.
- On live tasks, if there are no assets or references and the prompt is open-ended, this dimension may be N/A.

## Dimension 2 - Visual Quality

Ask whether the site looks polished and structurally clean.

Check:

- typography sizes, hierarchy, spacing, and readability;
- color, contrast, alignment, and visual balance;
- modern production-web feel, not raw unstyled HTML;
- animation easing, typography sophistication, and premium asset treatment for visually demanding prompts;
- broken images, missing icons, clipping, overflow, unintended horizontal scroll, and distorted assets.

Rule of thumb:

- One critical rendering bug, such as a broken hero image or overlapping nav, usually outweighs small aesthetic advantages.

## Dimension 3 - Surface Interactivity

Ask whether clickable things feel alive.

Check:

- hover, active, and focus states;
- buttons, links, and nav items;
- dropdowns, modals, tabs, accordions, and carousels;
- form fields accepting input;
- galleries, lightboxes, video controls, and media interactions;
- smooth transitions, tasteful motion, and sensible easing.

Penalize:

- UI elements that look clickable but do nothing;
- fields that cannot accept input;
- menus or tabs that do not open;
- rough or broken animations.

Use N/A only when the site is purely static and no interactive element is expected or visible.

## Dimension 4 - Workflow Correctness

Ask whether multi-step flows work end to end.

Applies to:

- forms;
- wizards;
- shopping carts;
- multi-page navigation;
- login, signup, booking, filtering, saving, or submission flows;
- data that should persist after refresh.

Classify each flow:

- Pass - all actions complete and expected outcomes hold.
- Fail - the flow completes but something is wrong.
- Blocked - the flow cannot be completed because a button is missing, the page crashes, a loader hangs, or a critical step is unreachable.

Rules:

- More passes is better.
- Blocked is worse than Fail.
- If one site passes a flow and the other is blocked, that is usually a much better signal.
- Use N/A when the task has no multi-step behavior, navigation, or persistence.

## Overall Preference

Pick the side that better serves the prompt as a whole.

Overall is not a simple average. Broken workflows can outweigh visual polish. Missing core prompt requirements can outweigh a nicer layout.

The justification should:

- be 2 to 3 sentences;
- name the dominant dimension or plain reason;
- cite concrete evidence;
- briefly acknowledge the losing side's strongest point when useful.

## Render Failure Rule

If one site completely fails to load, mark it much worse on every applicable live-task dimension.

If both fail badly, compare what is visible and flag the item if the task itself is broken or impossible to judge.

## N/A Rules

Use N/A on live tasks only when the dimension genuinely does not apply.

Do not use Tie just because a dimension is irrelevant.

Common N/A cases:

- Surface Interactivity when the site is purely static and nothing looks clickable.
- Workflow Correctness when there is no multi-step behavior, navigation, submission, cart, or persistence.
- Instruction & Reference Fidelity only when no assets or references exist and the prompt is so open-ended that there is no meaningful fidelity target for that subpart.

## Comment Style

Write like an average person who actually tested both websites.

Good:

`Response A is better because it follows the reference layout more closely and keeps the logo in the header. Response B has nicer card spacing, but it misses the product gallery the prompt asked for.`

Good:

`Response B is better because the booking form works all the way to the confirmation screen, while A gets stuck after selecting a date. A looks a little more polished, but the broken flow matters more.`

Bad:

`Response A is preferred due to superior semantic execution and elevated design language.`

### The Four Patterns

Most visual coding comments are one of these. Match the shape to the situation.

#### 1. The Broken Flow

One site's multi-step flow dies partway. Say where it stopped.

`Response A is better because the booking flow goes from date picker to confirmation without a problem. Response B looks more polished, but it freezes after you pick a date and the Next button stops responding.`

#### 2. The Missing Section

The prompt asked for something that is not on the page. Name it.

`Response B is better because it includes the pricing table and the FAQ the prompt asked for. Response A has a nicer hero section, but it skips pricing entirely.`

#### 3. Looks Better, Does Less

The prettier build is the emptier one. Give it credit, then say what it is missing.

`Response A is better because the filters actually narrow the product list when you click them. Response B has cleaner cards and better spacing, but the filters are decorative and nothing changes.`

#### 4. Justifying a Tie

Ties need more evidence than picks. Name what both did.

`Both sites build the same four sections and the nav links jump to the right anchors. Neither one makes the contact form submit, so they fail in the same place.`

### Common Comment Failures

- Reviewing the code instead of the page you clicked.
- Naming every dimension instead of the one that decided it.
- Saying "it works" without naming what you tested.
- Writing a tie comment shorter than a pick comment.

## Final Checklist

- Prompt read.
- References checked.
- Assets checked.
- Both sites scrolled.
- Interactive elements tested.
- Multi-step flows tested if present.
- Four dimensions rated independently.
- N/A used correctly.
- Overall justification is short, concrete, and natural.
