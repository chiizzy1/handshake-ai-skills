# Prompt Clarity

**Definition**: Each question should be written clearly and lack ambiguity.
- **Question is clear**: Grammatically correct, free of typos, and not open to multiple valid interpretations.
- **Fine-grained precision**: If the question challenges spatial reasoning, frame it to avoid precision disputes — use approximation wording or MCQs with sufficiently distinct options.
- **What to avoid**: Ambiguous questions or ties; exact numeric questions where the value cannot be read from the chart; overly broad trend questions with many possible answers; questions where nearby annotations or formulas could be confused with plotted values.

## ✅ Pass
1. Clear, precise language with proper grammar; the intent is unmistakable.
2. Spatial reasoning with clear boundaries, distinct choices, or approximation wording.

## ❌ Fail
1. Spelling errors, poor grammar, or vague language.
2. Demands an overly precise spatial judgment that is subjective or unverifiable.

## VQA Examples

### Example 1A — Vague Spatial Reference
**Prompt (wrong)**: "What is the largest category in the upper left part of the image? Answer in a word response (e.g., Other)."
**Why it fails**: "The upper left part" could mean the index, the top of the pie chart, or the transport breakout.
**How to correct**: "Which category in the index represents the largest share of heat demand? Answer in a word response (e.g., Other)."

### Example 1B — Vague Reference to "The Purple Part"
**Prompt (wrong)**: "What is the absolute percentage difference between the purple part of the pie chart and the heat breakdown? Answer in a whole number percentage (e.g., 20%)."
**Why it fails**: "The purple part" could reference one purple category or the sum of all purple categories.
**How to correct**: "What is the absolute percentage difference between the Transport category of the pie chart and the heat breakdown? Answer in a percentage without decimals (e.g., 20%)."

### Example 2 — Fine-grained Precision
**Prompt (wrong)**: "Looking at the monthly data points in the chart, what is the numerical change of the middle black line between Oct and Nov 2018? Answer with a single-digit whole number (e.g., 3)."
**Why it fails**: The exact numerical change between two close points on a line chart is subjective — different readers will estimate different values.
**How to correct**: Use clearer boundaries: "Looking at the monthly data points in the chart, how many of the following month-to-month comparisons show the middle black line increasing while the teal line decreases: MAI to JUN, JUN to JUL, and JUL to AGO? Answer with a single-digit whole number (e.g., 3)."

## BabyVision Examples

### Example — Missing POV / Perspective (Maze)
**Prompt (wrong)**: "What is the sequence of the first 4 turns that must be taken to follow the most direct path from the entrance at the bottom of the maze to the exit at the top? Answer with one letter (e.g., B). A. left, right, left, right  B. left, left, left, right  C. right, left, right, left  D. right, right, right, left"

**Why it fails**: The prompt does not state the POV or perspective needed to answer (e.g., bird's-eye view vs. first-person POV of a traveler inside the maze). "Left" and "right" flip depending on which frame the solver adopts, so more than one option is defensible. It also does not state whether "up" or "down" moves should count as turns.

**How to correct**: Specify the frame and what counts as a turn: "From a bird's-eye view of the maze below, what is the sequence of the first 4 left/right turns (ignoring straight segments) along the most direct path from the entrance at the bottom to the exit at the top? Answer with one letter (e.g., B)."

## Key Rules
- **Specify POV (BabyVision)**: If spatial directions (left/right/up/down) depend on perspective (e.g., a maze), explicitly state the Point of View (e.g., "From a bird's-eye view", "first-person view of a traveler").
- **Avoid subjective comparisons**: "most bluish-purple", "2 pixels longer", "slightly higher" — these are unverifiable.
- **Avoid ambiguous references**: "the upper left part", "the purple part", "the third line" when there are multiple candidates.
