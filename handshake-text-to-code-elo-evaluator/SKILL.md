---
name: handshake-text-to-code-elo-evaluator
description: Evaluate Handshake Text-to-Code ELO tasks. Use when comparing two rendered code outputs (A and B) generated from the same text prompt. Rate three dimensions (Visual Design, Functionality, Instruction Following), pick an overall winner, and write a short justification.
---

# Handshake Text-to-Code ELO Evaluator

## Core Rule

Use the Text-to-Code ELO guidelines as the source of truth:

- `HANDSHAKE-AI/Text-to-code-elo/guidelines.md`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Read the prompt. Keep it visible the entire time. It is the ground truth.
2. Open both renders. Interact with each one. Click buttons, scroll, try forms, test links.
3. Apply the Render Gate first (see Functionality below).
4. Rate three dimensions independently: Visual Design, Functionality, Instruction Following.
5. Pick the overall winner.
6. Write the justification (2-3 sentences, minimum 100 characters).

## Hard Gates

- Do not rate before interacting with both renders. Actually click things.
- Do not let visual polish override functional breaks. A gorgeous render with a broken Submit button loses to an ugly render that works.
- Do not default to Tie when unsure. Leave the dimension unrated, or use N/A if it truly does not apply.
- Do not collapse all dimensions to Tie to match the overall verdict. Rate each dimension on its own merits.
- Do not let the halo effect from pretty styling make you forget to check if the prompt was actually followed.
- Do not write generic justifications. Every justification must name a specific element, value, or bug.

## Rating Scale

Every dimension uses the same 5-point scale:

| Rating | Meaning |
|---|---|
| Strongly Prefer A | A is clearly and significantly stronger |
| Slightly Prefer A | A has a noticeable but small edge |
| Tie | Both are roughly equal |
| Slightly Prefer B | B has a noticeable but small edge |
| Strongly Prefer B | B is clearly and significantly stronger |

**N/A** is available when a dimension does not apply to the item (see Functionality).

## Three Dimensions

### Dimension 1 — Visual Design

Overall aesthetic quality of the design: layout, color palette, typography, imagery, variation, originality, consistency, and clarity.

**Ask yourself:**

- Is the design visually appealing, professional, and polished?
- Are colors, typography, and spacing harmonious? No clashing colors, off-theme fonts, awkward gaps, crowded areas?
- Are complex effects (gradients, shadows) used effectively without harming readability?
- Does the design feel original and varied, rather than generic?

**Exception:** If the prompt asks for a clone or a specific style, prompt adherence wins. That belongs to Instruction Following.

**Calibration:**
- "Strongly Prefer" = one side is clearly polished and harmonious, the other has clashing colors, off-theme fonts, or visually jarring layout.
- "Slightly Prefer" = small spacing, shade, or polish differences.
- "Tie" = both look equally polished.

### Dimension 2 — Functionality

Does the output work as intended, fulfill the prompt's requirements, and provide a smooth user experience?

**RENDER GATE (apply FIRST):**
If a render is EMPTY, BROKEN, WHITE, BLACK, a TINY fragment, or failed-to-render, it loses Functionality outright ("Strongly Prefer" the other) AND is "Strongly Prefer" the other on every other applicable dimension. A working render always beats a broken one.

**For websites / apps:**
- Does it perform all required functions described in the prompt?
- Are buttons, forms, links working correctly?
- Is the UX smooth and intuitive? Responsive?
- Are there bugs, errors, or broken features?

**For slides / PDF:**
- Any elements placed outside the document area?
- Any unintentionally overlapped, misplaced, or illegible elements?
- Are figures, tables, SVGs, charts rendered correctly?

**Use N/A** when the prompt describes a purely static output with no interactivity and no document layout that can break (e.g. "draw a sunset icon").

### Dimension 3 — Instruction Following

How accurately and completely does the response follow the specific instructions in the prompt: required steps, details, design elements, and constraints.

**Ask yourself:**

- Does the response follow all instructions given in the prompt?
- Are any steps, requirements, or constraints from the prompt missing or incorrectly implemented?
- Are the instructions interpreted correctly and applied as intended?
- Does the response adhere to style instructions and design elements mentioned in the prompt?

**Look for:** missing required sections, ignored color/typography directives, wrong layout structure, violated constraints (word counts, item counts, "no images", "dark mode", "single page"), wrong text/numbers/labels the prompt specified exactly.

**Calibration:**
- "Strongly Prefer" = one side faithfully follows the prompt, the other drops, reorders, hallucinates, or violates a major instruction.
- "Slightly Prefer" = one minor missed detail.
- "Tie" = both follow the prompt equally well.

## Overall Preference

After rating the 3 dimensions, pick the overall winner using the same 5-point scale.

The overall verdict is not just an average. It is your judgment of which output better serves the prompt as a whole. If two dimensions slightly favor A but the third has a critical break in A, the overall can still go to B. Use the justification to explain your reasoning when the dimensions split.

## Writing the Justification

2-3 sentences (minimum 100 characters) that:

1. Name the dominant dimension(s) driving your decision.
2. Cite concrete evidence: specific elements, values, or bugs ("the primary CTA in A is unclickable", "B's hero has overlapping nav and body", "A is missing the 'Pricing' section the prompt asked for").
3. Acknowledge counter-arguments from the losing side when applicable ("A has cleaner typography but the broken interaction dominates").

## Skip vs Flag

- **Skip** = you personally cannot judge this item (out of your area, genuinely unsure).
- **Flag for removal** = the item itself is broken: corrupt prompt, unintelligible text, off-topic, both renders failed for an obvious data reason. Bad for everyone, not just you.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
```

## Calibration Examples (Learn from Past Mistakes)

**Mistake 1: Voting on appearance without clicking anything.**
*Context: A calculator app. A looks gorgeous but the buttons do not respond when clicked. B is ugly but every button works.*
*Lesson:* Always interact with the renders. Functionality asks whether the output actually works. A calculator whose buttons do not respond fails, even if it looks better.

**Mistake 2: Letting the halo effect override instruction checking.**
*Context: A coffee shop landing page. A has gorgeous styling and custom illustrations but only has hero + menu. Missing location and contact sections. B has plain Bootstrap styling but all 4 required sections.*
*Lesson:* Check the prompt requirements against each render. A landing page missing half its required sections fails the prompt, regardless of how pretty it is.

**Mistake 3: Collapsing all dimensions to Tie because both have flaws.**
*Context: A dashboard with 4 KPI cards. A has all 4 cards but placeholder text. B has only 3 cards but with real data. Annotator marked every dimension as Tie.*
*Lesson:* Rate each dimension on its own. A clearly wins Visual Design. Both fail Instruction Following in different ways. The point of having 3 dimensions is to surface tradeoffs. Collapsing them all to Tie throws that signal away.

**Mistake 4: Writing generic justifications.**
*Context: Justification was "A looks better than B."*
*Lesson:* No dimension named, no concrete element cited, no acknowledgement of what was tied. A reviewer cannot tell if you actually looked at the renders or guessed. Always name the dimension and cite one specific element.

**Mistake 5: Rating a broken render higher because it looked prettier.**
*Context: A renders blank (white screen). B renders partially with a broken layout. Annotator rated Tie because "both are broken."*
*Lesson:* Render gate. Any working render beats an empty one. B wins Functionality outright, and wins every other dimension too.

## Final Checklist

Before submitting:

- Prompt read and kept visible.
- Both renders interacted with (buttons clicked, forms tested, links tried).
- Render gate checked first.
- All 3 dimensions rated independently.
- Overall verdict is a holistic judgment, not a mechanical average.
- Justification is 2-3 sentences, 100+ characters.
- Justification names the dominant dimension.
- Justification cites concrete evidence (specific element, value, or bug).
- Justification acknowledges the losing side's counter-argument when applicable.
- Per-dimension ratings are consistent with the overall (no "A wins all 3 dims but overall is Tie").
- No generic, evidence-free justification.
- Comment sounds like a normal person, not a rubric-reciting robot.

## Core Lessons

1. **Interact before you vote.** The most dangerous failure is interactive code that looks right but does not work.
2. **Check completeness before polish.** Missing required sections is worse than ugly styling.
3. **Rate dimensions independently.** Do not let the overall verdict pull all dimensions to match.
4. **Cite specific evidence.** "The Submit button does not fire" beats "A has functional issues."
5. **Acknowledge tradeoffs.** When the loser has a genuine strength, say so.
6. **Use the prompt's exact words.** If the prompt says "dark mode pricing page," use those exact words in your justification.
7. **Keep comments human.** If your justification sounds like an AI evaluator wrote it, rewrite it until it sounds like a normal person.
8. **Never rewrite the user's words.** If the user provides exact phrasing, use it word-for-word.
9. **Never Touch Workspace Files:** The AI evaluator must provide feedback text directly in the chat in a clearly formatted manner. Never directly edit `task.md` or the user's workspace files.
