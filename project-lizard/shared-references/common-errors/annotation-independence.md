# Annotation Independence

**Definition**: Annotations must be standalone and truly distinct. The prompt cannot reference a "previous question/answer" or rely on context from other annotations on the same image. Each prompt must use different skill combinations or focus on different visual components — not minor template variations. The prompt must also depend on the image and not be answerable from general knowledge alone.

## ✅ Pass
1. Each annotation explores a unique data point or visual element with different cognitive steps, fully understandable in isolation.
2. The prompt relies entirely on visual evidence within the image and cannot be answered without it.

## ❌ Fail
1. References to "the other one," "it," or a prior question; repetitive structures or the same formula with only minor swaps.
2. Asks about items not pictured, or is a general-knowledge question solvable without the image.

## VQA Examples

### Example 1 — Two Prompts on the Same Image with the Same Formula

**Prompt 1**: "Locate the graph in the top-left section. Extract the single numerical value on its x-axis enclosed within a hand-drawn yellow circle. Next, locate the hand-written equation starting with 'pH =' in that same top-left section and extract the value written immediately after the equals sign. Multiply the circled value by the 'pH =' value. Answer as a single integer (e.g., 50)."

**Prompt 2**: "Locate the x-axis of the graph in the bottom-right corner and identify its highest explicitly printed numerical value. Then, locate the same 'pH =' equation in the top-left section and extract the value after the equals sign. Multiply these two values. Answer as a single integer (e.g., 50)."

**Why it fails**: Prompts 1 and 2 reuse the same "pH =" value and the same operation (multiply). They are template variations, not distinct annotations.

**How to correct**: Make Prompt 2 use different skills and different data: "Locate the x-axis of the graph in the bottom-right corner and extract its highest explicitly printed numerical value. Locate the pH range given for 'Phenolphthalein' (top-right section) and extract the highest numerical value from that range. Divide your extracted bottom-right x-axis value by your extracted Phenolphthalein maximum. Answer as a single integer (e.g., 5)."

### Example 2 — References a Previous Question

**Prompt**: "Using the count of 'Lows' found in the previous question, count each standalone appearance of the word 'Highs' (including within phrases like 'Higher Highs'), then add it to that previous count and compute the factorial of the total. Answer as a single number (e.g., 26)."

**Why it fails**: The prompt explicitly references "the previous question" — it is not standalone.

**How to correct**: Restate every needed value inside the prompt: "Count each standalone appearance of the word 'Highs' (including within phrases like 'Higher Highs'), then compute the factorial of this count. Answer as a single number (e.g., 26)."

### Example 3 — Answerable Without the Image

**Prompt**: "Queen Elizabeth II died on one of the months used to label the x-axis on the top right chart. What month did she die? Answer as one word (e.g., September)."

**Why it fails**: The answer (September) is common knowledge and does not require the chart. The chart is decorative, not functional.

**How to correct**: Make the prompt actually require the chart: "Looking at the bottom left chart, which month recorded the highest number of impressions? Answer as one word (e.g., September)."

## BabyVision Examples

### Example — Three Annotations That All Target the Same Visual Element

**Prompt 1**: "Which shadow matches the original image? Answer in the format Column:row (e.g., 2:1)." → Answer: 2:2

**Prompt 2**: "Looking only at the shape of the tree, including trunk, how many of the shadow options have the correct tree silhouette? Answer in a single number (e.g., 2)." → Answer: 4

**Prompt 3**: "Find which shadow on the right matches the original image on the left. What is the reason that the top-left shadow does not match the original image? Answer with a single letter (e.g., A). A. The hair is incorrect  B. The basket is incorrect  C. The person's body is incorrect  D. The tree is incorrect" → Answer: D

**Why this fails**: All three prompts are anchored to the same task — comparing the reference figure to the six shadows — so the surface rewording (pick the match, count matching trees, diagnose the mismatch) is exactly the "minor template variation" this criterion catches.

**How to correct**: Vary the visual element, the cognitive step (matching vs. counting vs. spatial transform vs. pattern completion), or the skill combination tagged. When a second prompt feels like a rewording of the first, cut to one strong annotation instead.

## Key Principle

**Vary the primitive**: If prompt 1 counts something, prompt 2 should find a match or track a path. Do not just swap one item for another while keeping the exact same formula. If there is any doubt that two annotations on the same image may be similar — in skills, visual element, or question shape — cut it down to one.
