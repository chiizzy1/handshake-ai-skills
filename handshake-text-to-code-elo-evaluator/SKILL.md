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

```markdown
Visual Design: [rating]
Functionality: [rating]
Instruction Following: [rating]
Overall: [rating]

Justification: "Response [A/B] is better because [explain why]. [Explanation of why the other is bad.]"
```

Example of a good output:

```markdown
Visual Design: Strongly Prefer A
Functionality: Tie
Instruction Following: Strongly Prefer A
Overall: Strongly Prefer A

Justification: "Response A is better because it delivers exactly what the prompt asked for, a simple hacker-themed login screen with green buttons and the correct password behavior. Response B ignores the green button requirement, misses the hacker aesthetic, and over-builds a generic landing page template that was never requested. The prompt specifically asked for a 'simple and professional design' and Response A nails that."
```

Example of an evaluation where one response is broken:

```markdown
Visual Design: Strongly Prefer A
Functionality: Strongly Prefer A
Instruction Following: Strongly Prefer A
Overall: Strongly Prefer A

Justification: "Response A is better than Response B because it followed the prompt's instruction and actually built a beautiful and interactive 3D credit score guage, while Response B appears broken as it fails to output any designs and shows just a blank empty screen."
```

### Hard Comment Rules

**The Persona: The Average Everyday Person**
You are NOT a professional code reviewer, a prompt engineer, or a UX expert. You are an average person testing two websites side by side.

- **Do NOT talk about:** "executing constraints," "architectural patterns," "semantic HTML," "render pipeline," or "instruction following" as a named concept.
- **DO talk about:** What works, what is broken, what is missing, what looks better.

1. **Strict Pattern Requirement:** ALWAYS start your justification with "Response [A/B] is better because [explain why]". Then, explain why the other response is bad.
2. **Strict Length Limit:** Each justification comment MUST be at most 3 sentences. Two to three sentences is the perfect length.
3. **American English Punctuation:** Always use American English style for quotes. Periods and commas must go *inside* the quotation marks (e.g., write `"Ok."` instead of `"Ok".`).
4. **Natural Human Flow (Good vs. Bad Example):**
   - ❌ **BAD (Robotic AI-Speak):** "Response A is the clear winner because of its stunning, premium aesthetic. It completely nailed the high-end agency vibe with incredible, confident typography, clean monochrome spacing, and a truly cinematic layout. Since both responses successfully included all the requested sections, they tie on following the prompt, but Response A's visual polish puts it far ahead."
   - ✅ **GOOD (Natural Everyday Human):** "Response A is better because it nails the premium agency look with clean typography and dark spacing, while Response B feels like a cheap startup template. Response A does have a broken portfolio image which gives B the edge on functionality, but A's design still wins overall."
5. **ZERO TOLERANCE: No em dashes (—) anywhere. Ever.** Em dashes are the single biggest AI writing tell. Replace every em dash with a period or comma. If you catch yourself writing one, stop and rewrite the sentence. Average people do not use em dashes. No semicolons either.
6. **Avoid absolute words.** Never say a render did something "perfectly" or "flawlessly." Use safer words like "cleanly," "nicely," or "does a good job."
7. **Use "while" instead of "whereas".** "Whereas" sounds formal and academic.
8. **Never rewrite the user's words.** If the user gives you the exact phrasing for the justification, use it VERBATIM. Only fix obvious typos.
9. **Banned phrases:** "; note that", "suffers from", "fails the constraint", "render pipeline", "semantic structure", "garbled", "gibberish", "hallucinated".
10. **Good casual alternatives:** "does not work", "nothing happens when you click it", "is missing", "looks broken", "the layout is messed up", "looks better", "is way more polished".

### Anchoring to the Prompt

**Rule:** Always extract the exact specific requirement from the prompt and base your justification entirely around whether that specific requirement was met. Do not overcomplicate or invent generic reasons if the prompt gives you the exact vocabulary to use.

**Bad (robotic, overcomplicating):**
```
"A is better because it perfectly implements the responsive grid layout with optimal typography hierarchy and harmonious color theming as specified in the prompt requirements."
```

**Good (natural, anchored to the prompt's words):**
```
"A is slightly better on Visual Design. Same correct chart structure as B, but A has visible gridlines, more balanced spacing, and a calmer palette that makes values easier to read. Functionality and Instruction Following are tied. The win is purely on aesthetic polish."
```

### The "Interact Before You Vote" Rule

**Rule:** For any render that includes interactive elements (buttons, forms, links, dropdowns, sliders), you MUST actually interact with them before voting. The most dangerous failure mode is interactive code that looks right but does not work. Never vote based on appearance alone when interactivity is involved.

### Completeness vs Polish

**Rule:** A render that includes all required sections from the prompt but looks plain usually beats a gorgeous render that is missing half the required sections. Visual Design is not Instruction Following. Rate each on its own.

### Genuine Dimension Splits

**Rule:** When dimensions genuinely split (A wins Visual Design, B wins Instruction Following, Functionality is tied), do NOT collapse all dimensions to Tie to match the overall. Rate each dimension on its own merits, then form the overall verdict and explain the tradeoff in the justification.

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
