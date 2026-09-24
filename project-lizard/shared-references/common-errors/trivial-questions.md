# Trivial Questions

## VQA Triviality

**Definition**: The question must require the model to demonstrate conceptual understanding of the visual data — beyond simple extraction or counting. The model should interpret the "why" or "how" of the visual.

### Rules
- **Layers of reasoning**: Each VQA annotation needs at least 2 layers of logical reasoning — that is the requirement. A fully multi-step prompt with separate commands (Command 1 → Command 2 → Final Question → Final Answer) is one way to get there, but it is not mandatory. A single, well-built question that forces two layers of reasoning (for example, comparing groups and then interpreting the result) satisfies the same bar.
- **Ontology requirements**: Every VQA annotation must meet the ontology minimums — at least 2 ontologies, 3 if one of them is Enumeration, and at least 1 anchor ontology.
- **Contextual questions**: VQA annotations should get at the underlying meaning of the image, not surface-level details or arbitrary math. Ask two questions before submitting: (1) Does this annotation help the model understand the image better? (2) Would a human ever actually ask this? If the answer to both is no, the question is too trivial or arbitrary — revise it.
- **Performative length**: Avoid wording, procedural steps, or constraints that increase instruction-parsing effort without increasing reasoning difficulty. If the complexity lives in the sentence — long setup, stacked instructions, or advanced terminology — rather than in the image, it's performative.

### ✅ Pass
1. Requires the model to synthesize multiple visual cues.
2. Asks for numeric answers not directly written on the chart.
3. At least two steps structured as a clear sequence leading to one final question.
4. Instructions are clear and proportionate.
5. Answer length is no more than 7 words.

### ❌ Fail
1. Overly simple, single-step retrieval.
2. Question states the answer directly (giveaway).
3. No multi-step structure, or multiple separate questions instead of a sequence.
4. Excessive indirection or inflated wording.
5. Answer length is more than 7 words.

### Good Question Characteristics
- Comparison of multiple items, finding second/third highest.
- Numeric answers not directly on the chart.
- Choosing the correct subplot.
- Matching to legend labels.
- Region-restricted reading.
- Counting items that satisfy a condition.
- Threshold comparisons and near-ties.
- Distinguishing plotted values from labels.
- Judging trend changes or symmetry.
- Using heatmaps/tables/boxplots when clearly readable.

### Avoid
- Giveaways (including in the format example — the example must NOT equal the correct answer).
- One-step questions.
- Questions answerable from the title alone.
- Questions requiring external paper knowledge.

### VQA Examples

**Example 1 — Trivial Even Though Multi-step**
**Prompt**: "Find the number of letters (case insensitive) in the title of the table. Take that number and multiply it by the sum of the numbers on the y-column corresponding to the seventh row and third row (not counting the blue row at the top). Multiply that by the total number of distinct numbers found to the left of the table. Provide your final answer as a whole number (e.g., 24)."
**Why it fails**: Multi-step but still pure extraction + arithmetic. No conceptual understanding required.
**How to correct**: Include annotations that conceptually ask about the information (average comparison of groups, type of relationship, difference between points, etc.).

**Example 3 — Two Stacked Questions**
**Prompt (wrong)**: "Calculate the difference between 'Work from home' and 'On site / office' for each industry, and which industry has the highest 'Work from home' percentage?"
**Why it fails**: Two separate questions, not a sequence leading to one answer.
**How to correct**: Restructure as a single sequence: "Calculate the difference between 'Work from home' and 'On site / office' for each industry. Use those results to determine which industry has the highest 'Work from home' percentage. What is the final answer as the name of that industry (e.g., Public administration)?"

**Example 5 — Performative Length Hiding Pure Extraction**
**Prompt (wrong)**: "Analyze the spectral chart and perform the following steps. Step 1: Extract the integer at the top of the 'Signal Strength (dBm)' Y-axis (ignore the minus sign) — call this A. Step 2: Decide whether the solid red heatmap pixels sit in the left half (B = 5), right half (B = 10), or both halves (B = 15). Step 3: From the floating grey data box in the top-right, extract the single digit immediately to the left of the space before 'MHz' — call this C. Step 4: Compute (A * B) − C. Answer with a number only (e.g., 500)."
**Why it fails**: Simple data extraction dressed up in procedural language. Cannot be fixed by rewording — rebuild the prompt around an actual conceptual question about the chart.

---

## BabyVision Triviality

**Definition**: BabyVision questions are simple by design — they don't need multi-step chains or conceptual depth. There is one requirement that keeps them from being trivial: at least 1 of the BV taxonomies must apply to the annotation.

### Rules
- **Taxonomy grounding**: The question must exercise a real BV reasoning primitive — matching/discrimination, spatial reasoning, pattern recognition, or tracking. If none of the taxonomies apply, the question is trivial.
- **Simplicity is fine**: Short, single-step BV questions are acceptable as long as the taxonomy requirement is met. Don't inflate a BV prompt to look harder than it is.

### ✅ Pass
1. At least one BV taxonomy clearly applies to the question.
2. The question exercises that taxonomy's reasoning primitive, not just observation.
3. The prompt stays simple and direct.

### ❌ Fail
1. No BV taxonomy applies to the question.
2. The question is pure observation or labeling with no reasoning primitive behind it.
3. A taxonomy is selected but the question doesn't actually test it.

### BV Example — Giveaway Prompt with Ambiguous Counting Rule
**Prompt**: "How many hearts are shown in the image? Count only whole hearts that are fully visible and not touching any other object in the image. Answer as an integer (e.g., 10)."
**Answer**: 10
**Why it fails**: The example answer (10) matches the correct answer — this is a giveaway. Also, the counting rule "not touching any other object" is ambiguous for overlapping shapes.
**How to correct**: Change the example answer to a different plausible integer so it no longer matches the correct answer. Tighten the counting rule so it applies cleanly to overlapping objects, and restructure the prompt into Command → Final Question → Example Answer order.
