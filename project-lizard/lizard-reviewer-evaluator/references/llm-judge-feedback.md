# How to Handle LLM Judge Feedback

The LLM Judge acts as a QC layer that validates each annotation against the common error categories. It passes or fails the annotation on each category, and provides reasoning whenever it fails one. Your responsibility is to verify that the Judge's pass/fail determinations are accurate and that its justifications for any failures are sound.

## How the Judge Refers to Annotations
The Judge calls the first annotation on a task "Annotation 0", the second "Annotation 1", and so on.

## When to Agree vs. Disagree

For each LLM Judge category decision, select Agree (👍) or Disagree (👎). **All Judge decisions must be annotated before submitting to the next status.**

| Your Response | Guidance |
|---|---|
| 👍 **Agree** | The Judge correctly passes or fails the question in accordance with the error's guidelines, with correct reasoning. Also agree when the Judge correctly fails a question but with flawed reasoning — agree with the verdict, and explain in the notes how the reasoning fails. **Note**: When the Judge passes a question, no reasoning is provided. This is expected behavior — don't disagree just because a pass has no explanation. |
| 👎 **Disagree** | The Judge incorrectly passes or fails the question in accordance with the error's guidelines. **(Required)** In the notes section, state why and how the Judge is wrong. See the feedback scenarios below. |

**Two different judgments — don't mix them up:**
- **Judge Verdict** = whether the annotation passes/fails according to the LLM Judge.
- **Agree with Judge** = whether YOU agree or disagree with the Judge's decision.

## Providing Specific Feedback to the Judge

Feedback should be clear and explicit about how the Judge's reasoning is flawed and how it should be corrected, relative to the question and image.

### Feedback Scenarios

These are a blueprint, not an exhaustive list:

1. **Judge incorrectly evaluates the question as trivial**: The Judge says the question is trivial, but it actually requires multi-step reasoning or conceptual understanding. Disagree and explain what reasoning the question requires.

2. **Judge cannot apply the guidelines correctly (hallucinated rubric)**: The Judge cites a rule that doesn't exist in the guidelines. Disagree and note that the Judge is hallucinating the rubric.

3. **Judge correctly fails Answer Incorrect, but the annotator's rewrite is wrong**: The Judge catches a real error. Agree with the fail.

4. **Judge interprets the rubric differently**: The Judge applies a reasonable but incorrect interpretation of a guideline. Disagree and state the correct interpretation.

5. **Judge interprets the guideline correctly, but the guideline is flawed**: The Judge is technically correct per the rubric, but the rubric itself has a gap. Agree with the verdict, note the guideline issue in your feedback.

6. **Judge is vague in its feedback**: The Judge fails the annotation but doesn't give actionable feedback. If the fail is correct, agree and provide the specific missing feedback yourself.

7. **Judge lacks necessary context**: The Judge misses something visible in the image that changes the verdict. Disagree and describe what the Judge missed.

8. **Judge fails beyond the scope of the common error categories**: The Judge flags something that isn't covered by any error category. Disagree and note the scope issue.

9. **Image is not clear/workable, but the Judge passes it**: The Judge should have failed the image feasibility check. Disagree with each incorrect pass and note that the image is not clear.

10. **Judge lacks required capability**: The Judge cannot perform the visual reasoning needed (e.g., precise chart reading). Note this limitation.

## Critiquing the Judge's Overall Feedback

If you notice anything wrong with the LLM Judge's Overall Feedback (e.g., the Judge corrects itself in its own overall summary — this is unwanted behavior), use the standard Overall Feedback box for these comments, alongside your final verdict.

## Worked Examples

### Example 1 — Judge misses the image/question relationship
**Question**: "After feedback and peer review, what is the following step? A. Actual results B. Hypotheses C. Solve everyday problems D. Exploring the literature"
**Model Answer**: D — **Rewrite Answer**: B
**Judge verdict**: Incorrectly passes "Question Unclear" and "Answer Incorrect."
**Correct action**: Disagree with both. Notes:
- Question Unclear: "The LLM Judge fails to see that there are multiple outputs originating from 'feedback and peer review.'"
- Answer Incorrect: "The LLM Judge fails to see that there are multiple correct answers present in the MCQ due to 'feedback and peer review' having multiple outputs."

### Example 2 — Judge hallucinates a rubric rule
**Question**: "What is the average percentage of men's share of employment in STEM in countries that are above the 84-country average? Answer in a percentage (e.g., 54.5%)."
**Judge feedback**: "The prompt asks for an 'average' without specifying whether it refers to the mean, median, or mode, which is explicitly listed as a failure case in the rubric."
**Correct action**: Disagree. Notes: "The LLM Judge hallucinates what type of average must be specified." (The rubric does not require distinguishing mean/median/mode.)

### Example 3 — Correct fail, vague/incorrect reasoning
**Judge verdict**: Correctly fails "Skills don't match."
**Judge reasoning**: "Because the ontology field is null, it fails to accurately reflect the cognitive and visual tasks required to answer the question."
**Correct action**: Agree (the fail is correct), but note the flawed reasoning: "The Judge fails to give actionable feedback. The question misses the attribute perception, logical understanding, and spatial reasoning skills."

### Example 5 — Judge correctly catches an incorrect rewrite
**Question**: "What is the estimated allocated percentage of the Alternate Fixed Income? A. about 10% B. 15% C. strictly less than 5% D. strictly greater than 15%"
**Model Answer**: C — **Annotator Answer**: A
**Judge feedback**: "The annotator's rewrite answer 'A' (about 10%) is incorrect; visual estimation of the 'Alternatives' slice shows it occupies less than 5% of the chart."
**Correct action**: 👍 Agree. Notes: "The LLM is correct — the annotator is incorrect. The correct percentage is based on half of the yellow alternative fixed income allocation area."

### Example 6 — Judge correctly catches a penalized-but-correct model response
**Question**: Ordering four annotated levels on a candlestick chart from lowest to highest.
**Model Answer and Annotator Answer give the same ordering.**
**Judge feedback**: "The AI accurately ordered the levels using the exact phrasing provided in the prompt, meaning the annotator improperly marked a correct model response as failed."
**Correct action**: 👍 Agree. The model answered correctly — the annotation is invalid because the prompt didn't stump the model.

### Example 7 — Judge mislabels a multi-step question as trivial
**Question**: "On this image, group the bracket comparisons by their significance symbol. For each comparison, sum the sample size of the two groups connected by the bracket. If a symbol connects more than one pair, add their sums all together. What is the absolute difference between the highest and lowest of these symbol group totals? Answer as a single number (e.g., 8)."
**Judge feedback (Trivial Question)**: "The prompt asks for meaningless counting and arithmetic, failing to require any conceptual understanding."
**Correct action**: Disagree. Notes: "The question requires multiple steps of thinking including conceptual understanding, such as table/chart/graph understanding of relationships across the graph."

## Error Handling

**LLM Judge is not populated**: If the LLM Judge Feedback table is blank or not populated with data, flag the issue in the appropriate Slack thread before proceeding with the task. Do not submit without Judge feedback.
