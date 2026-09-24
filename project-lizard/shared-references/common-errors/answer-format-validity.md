# Answer Format Validity

**Definition**: Prompts must specify the exact answer format — including comma conventions, string requirements, MCQ structure (A./B./C./D.), and explicit rounding rules for numeric answers. The Answer field must contain only the final answer.

**Where to find the full answer-format guidelines**: Each workflow page carries the answer-format guidelines for its own question type:
- VQA 2: Write a Question — answer-format guidelines for VQA annotations
- BV 2: Write a Question — answer-format guidelines for BabyVision annotations
- The two sets overlap heavily but are NOT identical. Always check the rules for the task type you're working on.

## Answer Rules (Both VQA and BV)
- **Short and Deterministic**: Text answers must be ≤ 7 words.
- **Exact Quotes**: Use exact visible chart text for labels, methods, models, categories, panels, or legend entries.
- **Numeric Precision**: For numeric answers, use visible labels, ticks, gridlines, or clearly readable marks. If the value is not exact, ask for an approximate value with reasonable visible precision.
- **Multiple Outputs**: If multiple answers are required, separate them with commas and specify the ordering (e.g., alphabetical, left-to-right). Provide a combined example format.
- **Explicit Constraints**: Thousands separators, dollar signs, percentage signs, and units must be explicitly requested in the example answer.

## VQA-Specific Rules
- **Rounding**: VQA questions involving math MUST specify rounding rules wherever applicable. BV questions should avoid advanced math entirely, so there is no rounding requirement.
- **MCQ**: At least four options. Each option 1-7 words. No "All/None of the above."
- **Rewrite Answer for MCQ**: The bare letter only (e.g., `C`). Not `C.`, not `C. 4`, not `Option C`, not `4`. Just `C`.

## BV-Specific Rules
- **MCQ**: Max four options. Relabel 1/2/3/4 in the image to A/B/C/D.
- **Rewrite Answer for MCQ**: Same as VQA — bare letter only.

## ✅ Pass
1. The prompt dictates one required answer format with explicit rounding (VQA).
2. The answer contains only the final value, word, or phrase.
3. MCQs use clear A./B./C./D. labels with the required number of options and an explicit "Answer in…" instruction.

## ❌ Fail
1. Prompt lacks strict formatting constraints, or the rounding rule is missing (VQA).
2. Answer includes solving steps, justification, or filler.
3. MCQs use "Option C", missing periods, or sit on a single line; or the Rewrite Answer is more than the bare letter.

## VQA Worked Examples

### Example 1 — Explanation in the Answer Field
**Rewrite answer (wrong)**: "Begin by carefully examining each density curve… leading to the answer of 3, meaning C is the correct choice."
**How to correct**: The Rewrite Answer must be just: `C`

### Example 2 — "Option" Prefix and One-line MCQ
**Prompt (wrong)**: "…Answer with a single letter (e.g., A). Option A. 21 years sideways Option B. 11 years sideways Option C. 25 years to recover Option D. 13 years to recover"
**How to correct**: Use strict A./B./C./D. labels (no "Option" prefix), one option per line. Set Rewrite Answer to the bare letter: `C`

### Example 3 — Missing Rounding Rule
**Prompt (wrong)**: "…what's the mean number of letters per blue cell? (e.g., 5.0)"
**How to correct**: Add the rounding rule: "…Answer as a number rounded to 1 decimal point (e.g., 5.0)."

### Example 4 — Multiple Valid String Formats
**Prompt (wrong)**: "…In which month does this bar appear?"
**Why it fails**: "Sep" and "September" are both defensible.
**How to correct**: Constrain the format: "…Answer using the abbreviated three-letter month (e.g., 'Sep')."

### Example 5 — Missing Precision on a Percentage
**Prompt (wrong)**: "…what percent larger was Coffee than Tea in March?"
**How to correct**: "…Answer in a percentage without decimals (e.g., 20%)."

### Example 6 — Example Format Doesn't Match True Scale
**Prompt (wrong)**: "…Answer as a whole number (e.g., 350)."
**Why it fails**: The example was in hundreds but the real answer was in millions.
**How to correct**: Match the scale and the comma convention: "…Answer as a whole number with comma separators (e.g., 8,000,000)."

### Example 7 — Two Outputs Required Without a Combined Format
**Prompt (wrong)**: "…Answer both with text and a number."
**How to correct**: Specify a combined format: "…Answer in the format (Coffee-8,000,000)."

### Example 8 — MCQ Without an Answer-format Instruction
**Prompt (wrong)**: "…which of the following best estimates coffee's demand across the entire graph?"
**How to correct**: Add the MCQ format instruction: "…Answer with a single letter (e.g., C)."

### Example 9 — Percentage vs. Decimal
**Prompt (wrong)**: "What total percentage of respondents selected the top two options?"
**Why it fails**: Without explicit format, 99.3 vs 0.9930 are both defensible.
**How to correct**: "…Answer as a percentage (e.g., 45%)."

### Example 10 — Multi-item Answers Without a Specified Ordering
**Prompt (wrong)**: "Which three countries had the highest GDP growth? Answer with the country names separated by commas."
**How to correct**: Specify the ordering: "…Answer with the country names in alphabetical order, separated by commas (e.g., Brazil, Canada, Denmark)." (The example answer must not be the same as the correct answer — that would be a giveaway.)

## Comma Convention
When using commas, specify your format with a valid example in parentheses (e.g., 1,000 — comma functions as a digit group separator).
