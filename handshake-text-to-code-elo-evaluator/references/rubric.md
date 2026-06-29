# Text-to-Code ELO Rubric

Use this reference for Text-to-Code ELO tasks (comparing two rendered code outputs from the same prompt).

## Source

- `HANDSHAKE-AI/Text-to-code-elo/guidelines.md`

## Task Shape

- A text prompt describing what to build (website, app, dashboard, form, chart, slide, icon, etc.).
- Two rendered outputs: A and B.
- Three dimensions + overall preference.
- A written justification (2-3 sentences, 100+ characters).

Main question: Which rendered output better matches the prompt?

## Rating Scale

| Rating | Meaning |
|---|---|
| Strongly Prefer A | A is clearly and significantly stronger |
| Slightly Prefer A | A has a noticeable but small edge |
| Tie | Both are roughly equal |
| Slightly Prefer B | B has a noticeable but small edge |
| Strongly Prefer B | B is clearly and significantly stronger |

N/A = the dimension does not apply to this item.

Do NOT default to Tie when unsure. Leave the dimension unrated, or use N/A if it truly does not apply.

## Dimension 1 — Visual Design

Overall aesthetic quality: layout, color palette, typography, imagery, variation, originality, consistency, and clarity.

**Ask yourself:**

- Is the design visually appealing, professional, and polished?
- Are colors, typography, and spacing harmonious (no clashing colors, off-theme fonts, awkward gaps, crowded areas)?
- Are complex effects (e.g. gradients) used effectively without harming readability?
- Does the design feel original and varied, rather than generic?

**Exception:** if the prompt asks for a clone or a specific style, prompt adherence wins (that is Instruction Following).

**Calibration:**
- "much better" when one side is clearly polished and harmonious and the other has clashing colors, off-theme fonts, or visually jarring layout.
- "slightly better" for small spacing/shade/polish differences.
- "Tie" when both look equally polished.

### Visual Design Flashcards

**Q1:** A uses a calm, harmonious blue palette with balanced spacing. B uses harsh red-on-orange with crowded margins. What rating?
**A1:** A much better. The difference is not subtle. A is polished and pleasant, B is visually jarring.

**Q2:** Both look polished and professional. A has marginally tighter spacing. What rating?
**A2:** A slightly better.

**Q3:** Both renders feel equally polished and aesthetically appropriate for the prompt. What rating?
**A3:** Tie.

## Dimension 2 — Functionality

Does the output work as intended, fulfill the prompt's requirements, and provide a smooth user experience?

### Render Gate (Apply FIRST)

If a render is EMPTY / BROKEN / WHITE / BLACK / a TINY fragment / failed-to-render, it loses Functionality outright ("much worse") AND is "much worse" on every other applicable dimension. A working render always beats a broken one.

### For Websites / Apps

- Does it perform all required functions described in the prompt?
- Are buttons, forms, links working correctly?
- Is the UX smooth and intuitive? Responsive?
- Are there bugs, errors, or broken features?

### For Slides / PDF

- Any elements placed outside the document area?
- Any unintentionally overlapped, misplaced, or illegible elements?
- Are figures / tables / SVGs / charts rendered correctly?

### When to Use N/A

Use N/A when the prompt describes a purely static output with no interactivity and no document layout that can break (e.g. "draw a sunset icon").

### Functionality Flashcards

**Q1:** A renders completely blank (white screen). B renders correctly with a working layout. What rating?
**A1:** B much better. Render gate applies: A fails on functionality and loses outright.

**Q2 (slides):** A has one chart cropped off the slide edge. B is laid out cleanly throughout. What rating?
**A2:** B slightly better.

**Q3:** Both interactive demos work. Both forms submit and confirm correctly. What rating?
**A3:** Tie.

**Q4:** The prompt asks for a single static SVG icon. Nothing to click, no document layout. What rating?
**A4:** N/A. The prompt describes a static image. There is no "functionality" to evaluate.

### Think First: The Calculator Test

**Scenario:** The prompt says "build a calculator app." Render A looks gorgeous but the buttons do not visually respond when clicked. Render B has uglier styling but every button presses in and updates the display. Which wins Functionality?

**Answer:** B. Functionality asks whether the output actually works for the prompt's implied use case. A calculator whose buttons do not respond fails the "this is interactive software" contract, even if the prompt did not literally say "buttons must respond visually." Visual Design may go to A. Functionality goes to B.

## Dimension 3 — Instruction Following

How accurately and completely does the response follow the specific instructions in the prompt: required steps, details, design elements, and constraints.

**Ask yourself:**

- Does the response follow all instructions given in the prompt?
- Are any steps, requirements, or constraints from the prompt missing or incorrectly implemented?
- Are the instructions interpreted correctly and applied as intended?
- Does the response adhere to style instructions and design elements mentioned in the prompt?

**Look for:** missing required sections, ignored color/typography directives, wrong layout structure, constraints (word counts, item counts, "no images", "dark mode", "single page") that were violated, wrong text/numbers/labels the prompt specified exactly.

**Calibration:**
- "much better" when one side faithfully follows the prompt and the other drops, reorders, hallucinates, or violates a major instruction.
- "slightly better" for one minor missed detail.
- "Tie" when both follow the prompt equally well.

### Instruction Following Flashcards

**Q1:** Prompt asks for "hero, menu, location, contact form." A has all 4 sections. B only has hero and menu. What rating?
**A1:** A much better. A followed all instructions and included all required sections, while B missed two required sections.

**Q2:** Prompt asks for a dark-mode pricing page with 3 tiers. Both have 3 tiers. A is dark mode, B is light. What rating?
**A2:** A slightly better (or A much better, depending on how central dark mode was to the prompt).

**Q3:** Both renders include every section the prompt asked for, in the requested order, with the requested styling. What rating?
**A3:** Tie. Both followed the instructions equally well.

## Overall Preference

After rating the 3 dimensions, pick the overall winner using the same 5-point scale.

The overall verdict is NOT just an average. It is your judgment of which output better serves the prompt as a whole. If two dimensions slightly favor A but the third has a critical break in A, the overall can still go to B.

Use the justification to explain your reasoning when the dimensions split.

## Writing the Justification

2-3 sentences (minimum 100 characters) that:

1. Name the dominant dimension(s) driving your decision.
2. Cite concrete evidence: specific elements, values, or bugs ("the primary CTA in A is unclickable", "B's hero has overlapping nav and body", "A is missing the 'Pricing' section the prompt asked for").
3. Acknowledge counter-arguments from the losing side when applicable ("A has cleaner typography but the broken interaction dominates").

## Skip vs Flag

- **Skip** = you personally cannot judge this item (out of your area, genuinely unsure).
- **Flag for removal** = the item itself is broken: corrupt prompt, unintelligible text, off-topic, both renders failed for an obvious data reason. Bad for everyone, not just you.

## Knowledge Check

**Q1:** Render A is completely blank (white screen). Render B is partial. The header renders, but the body has broken layout. How do you score Functionality?

**Options:**
- Tie. Both are broken.
- Slightly Prefer B. At least the header renders.
- Strongly Prefer B. Render gate: any working render beats an empty one.
- Skip the item. Both renders failed.

**Answer:** Strongly Prefer B. Render gate: any working render beats an empty one.

**Explanation:** The render gate says any working render beats an empty/broken one. A blank screen is the worst possible Functionality outcome. The partial render wins outright on Functionality (and on every other applicable dimension).

## Good vs Bad Examples

### Good Justification Example (Sales Dashboard)

**Prompt:** "Build a sales dashboard showing Q1 revenue by region as a bar chart."

**A:** 4 bars labeled North/South/East/West, heights look right, y-axis 0-120, clean gridlines, harmonious blue palette.
**B:** 4 bars labeled North/South/East/West, heights look right, y-axis 0-120, no gridlines, slightly cramped spacing, harsher color contrast.

**Verdict:** Slightly Prefer A.
**Justification:** "Visual Design is the main difference. Same correct chart structure as B, but A has visible gridlines, more balanced spacing, and a calmer palette that makes values easier to read. Functionality and Instruction Following are tied. The win is purely on aesthetic polish."

**Why this is good:** Names the dominant dimension (Visual Design), cites concrete evidence (gridlines, spacing, palette), acknowledges the dims that tied. A reviewer can audit this in 5 seconds.

### Bad Justification Example (Same Dashboard)

**Verdict:** Slightly Prefer A.
**Justification:** "A looks cleaner than B, I prefer A overall."

**Why this is bad:** Generic. No dimension named, no concrete element cited, no acknowledgement of what was tied. A reviewer cannot tell if you actually looked at the renders or guessed. This is the #1 failure mode. Fix it by always naming the dimension and citing one specific element.

### Good Example: Catching Silent Functionality Breaks

**Prompt:** "Build a contact form with name, email, message fields, and a Submit button that validates and shows a thank-you message."

**A:** Form with all 3 fields, beautiful gradient styling, but the Submit button does nothing on click. No validation, no thank-you state.
**B:** Form with all 3 fields, plain styling, Submit validates inputs and shows a thank-you confirmation.

**Verdict:** Strongly Prefer B.
**Justification:** "Functionality is the decider here. A's Submit button is unresponsive, so the form is non-functional. B's submit validates and confirms as the prompt requires. A is more visually polished, but a contact form that cannot submit fails the prompt's core ask."

**Why this is good:** Caught the silent functional break. The annotator actually interacted with the form instead of just judging on appearance. A broken interactive flow is exactly the failure Functionality exists to catch.

### Bad Example: Missing Functionality Break (Same Form)

**Verdict:** Slightly Prefer A.
**Justification:** "A has a much nicer gradient design and looks more modern. Both have the same fields, slight edge to A on polish."

**Why this is bad:** Missed the broken Submit button entirely. The annotator looked at styling without clicking anything. This is the most dangerous Functionality failure mode: interactive code that looks right but does not work. Always exercise the interactions before voting.

## Boundary Case: Completeness vs Polish

### Good Example (Coffee Shop Landing Page)

**Prompt:** "Landing page for a coffee shop: hero, menu section, location/hours, contact form."

**A:** Gorgeous styling, custom illustrations, smooth animations. But only has hero + menu. Missing location and contact.
**B:** Plain Bootstrap-y styling, but has all 4 sections present and laid out correctly.

**Verdict:** Slightly Prefer B.
**Justification:** "B wins Instruction Following clearly. It includes all 4 sections the prompt asked for. A is missing 2 of 4 (location and contact). A wins Visual Design on the styling and illustrations. But a landing page missing half its required sections fails the prompt. Instruction Following outweighs aesthetic polish here."

**Why this is good:** Resists the halo effect from A's beautiful styling. Names the tradeoff explicitly (B wins Instruction Following, A wins Visual Design), and grounds the verdict in the prompt. A coffee shop landing page without location/contact is broken regardless of how pretty it is.

### Bad Example (Same Coffee Shop)

**Verdict:** Strongly Prefer A.
**Justification:** "A looks incredible. Custom illustrations, smooth animations. Way more professional than B. B is plain and boring."

**Why this is bad:** Halo effect. Visual polish drove the verdict and the annotator never checked whether A actually fulfilled the prompt. A is missing half the required sections. B fulfills all of them. Visual Design is not Instruction Following. Rate each on its own.

## Boundary Case: Genuine Split Across Dimensions

### Good Example (KPI Dashboard)

**Prompt:** "Dashboard with 4 KPI cards: Revenue, Active Users, Churn, NPS. Show this month's values from the provided data."

**A:** All 4 cards present and clickable, polished design, but every value shows "Lorem ipsum" placeholder text.
**B:** Only 3 cards (Revenue, Active Users, Churn), plain styling, but each shows a real value matching the provided data.

**Verdict:** Tie overall (genuine split across dimensions).

**Per-dim:**
- Visual Design: Slightly Prefer A (more polished cards).
- Functionality: Tie (both render, neither has interactive bugs).
- Instruction Following: split. A has the full 4-card structure but ignores the "use the provided data" instruction. B uses real data but misses one card.

**Justification:** "Real tradeoff. A nails the structural requirement (4 cards, polished) but ignores the prompt's 'use the provided data' instruction. Every value is Lorem ipsum. B is missing one card but actually uses the data. Both fail the prompt in different ways. Calling it Tie overall."

**Why this is good:** Boundary case with no clean winner. The good annotation: (1) rates each dimension on its own (does not let the verdict pull the dims), (2) names the specific tradeoff, (3) commits to a verdict but explains why it is borderline. Tie here is earned, not a cop-out.

### Bad Example (Same Dashboard)

**Verdict:** Tie. All dimensions: Tie.
**Justification:** "Both have problems. A has fake data, B is missing a card. Both are about equally bad so it is a tie."

**Why this is bad:** Rates every dimension Tie to match the verdict, even though A clearly wins Visual Design. The point of having 3 dimensions is to surface tradeoffs. Collapsing them all to Tie throws that signal away. Rate each dim on its own merits, then form the overall verdict.

## QA Rubric

Use this rubric to calibrate yourself and understand how submissions are graded.

### 5 Stars — Exceptional

**Exemplary.** The justification names the dominant dimension, points at specific elements ("Submit button does not fire", "missing the Pricing section the prompt asked for", "clashing red/orange palette"), and acknowledges the losing side's strongest counter-argument. Per-dimension ratings line up with the overall verdict.

**Hallmark:** Another person can audit the verdict in 5 seconds because the justification tells them exactly what to look for. Each dimension is rated on its own merits, not pulled to match the overall.

**Example:** "Functionality dominates. A's Submit button is unresponsive and the nav overlaps the hero. A wins Visual Design on the gradient palette, but the broken form makes A unusable."

### 4 Stars — Strong

**Good.** Names the dominant dimension and cites concrete evidence, but does not acknowledge the strongest counter-argument from the losing side. Per-dimension ratings are correct and consistent with the overall.

**Solid annotation, one polish point short of exemplary.** A reviewer can still audit it quickly.

**Example:** "A's Submit button does not fire and the nav overlaps the hero, while B's form works." (Missing: acknowledging that A had a stronger color palette.)

### 3 Stars — Acceptable

**Acceptable.** Identifies the main reason for the verdict but is vague on which dimension or what specific element. Per-dimension ratings are mostly correct.

**Adequate.** The verdict is defensible but a reviewer has to re-look at the renders to verify it.

**Example:** "Prefer B. A has a broken interaction and B's design works." (Vague: which interaction? Which design element? No dimension named explicitly.)

### 2 Stars — Weak

**Below expectations.** One of two failure modes:
- (a) Generic justification that could apply to almost any pair of renders ("A looks cleaner", "more readable").
- (b) Inconsistent ratings. Per-dim ratings clearly favor one side but the overall is Tie (or vice versa).

**Both failure shapes kill the downstream signal.**

**Generic example:** "A looks more polished, I prefer it."
**Inconsistent example:** Per-dim ratings show A winning all three dimensions, but overall is marked Tie. If A wins every dimension, the overall is not Tie.

### 1 Star — Unacceptable

**Unacceptable.** Justification is missing, empty, copy-pasted across items, or factually contradicts the renders. Per-dim ratings appear random or unrelated to what is on screen.

**Strong signal** that the annotator did not actually look at the renders, or did not understand the rubric. These submissions are usually pulled and the annotator re-trained or removed from the task.

## Final Checklist

- Prompt read and kept visible.
- Both renders interacted with (buttons clicked, forms tested, links tried).
- Render gate checked first.
- All 3 dimensions rated independently.
- Overall verdict is a holistic judgment, not a mechanical average.
- Justification is 2-3 sentences, 100+ characters.
- Justification names the dominant dimension.
- Justification cites concrete evidence.
- Justification acknowledges the losing side's counter-argument when applicable.
- Per-dimension ratings are consistent with the overall.
- No generic, evidence-free justification.
- Comment sounds like a normal person, not a rubric-reciting robot.
