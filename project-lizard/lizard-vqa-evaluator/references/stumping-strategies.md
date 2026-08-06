# VQA Stumping Strategies

Use at least one of these strategies per image to make questions more likely to stump the model. Do not force a strategy if the image cannot support it cleanly — a clean, high-quality annotation beats a contrived one.

**About the examples below**: The example prompts are illustrative, not golden. They're meant to convey the *shape* of each strategy, and may not fully comply with every other guideline in the playbook (phrasing, answer format, etc.). Treat them as directional, not as templates to copy verbatim.

---

## 1. Rank-n Questions (On a Limited Range)
When the question targets a limited range, the answer should differ from what you'd get if the whole image were considered. This tricks models that scan the entire chart instead of constraining to the specified range.

**Example 1**: "What algorithm shows the highest average caching reward at epoch 0?"
**Example 2**: "Which n_e value results in lowest loss in Frappe and the second-lowest AUC in MovieLens?"

---

## 2. Legend-binding on Close Colors, Marks, or Line Styles
Force the model to resolve a legend whose entries are visually similar. Works especially well on line charts with many overlapping series or bar charts with similar-shade categories.

**Example**: "What is the highest accuracy obtained on the Fashion-MNIST dataset across all plots?"

---

## 3. Close / Near-tie Comparisons
Ask the model to pick a winner when several values are nearly identical. This exploits the model's tendency to approximate rather than precisely read close values.

**Example 1**: "At 44 MB model size, which operation in the emlSGX-PM – Mirroring Step: Restore plot shows the least latency?"
**Example 2**: "What is the name of the model that has a low Intersection over Union, F1-score and Sensitivity with the smallest P.S.N.R but improves the most rapidly when P.S.N.R is increased?"

---

## 4. Counting Questions
Counting combined with one of the previous strategies (comparison, limited range, rank-N) raises difficulty significantly. Pure counting alone is often too easy.

**Example 1**: "Across both experiments, in how many groups of bars does LXMERT score higher than the proposed model?"
**Example 2**: "On the left chart, how many models have ever reached a Top-1 Accuracy over 80% on the K400 dataset?"
**Example 3**: "How many datapoints lie outside the bounds of the colored contour areas?"

---

## 5. Math Operations with Visual Grounding
Combine a simple arithmetic step with a visual extraction the model has to perform first. The math should depend on reading the image, not just generic computation.

**Example**: "What's the sum of all yellow squares?"

---

## 6. Trend or Density Questions
Ask about visual trends, clustering, or curves. Can be combined with other question types for extra difficulty.

**Example 1**: "In which subplot can the data be seen to form the clearest clusters?"
**Example 2**: "Which curve is the second to reach the steady Bprop. FLOPs per iter. value after 150?"
**Example 3**: "What is the number of clusters which monotonically decrease from x?"
**Example 4**: "Between x-axis value 0 and 5, what is the title of the subplot where its curves have the most negative relations with their respective curves in the inflation subplot?"

---

## 7. Heatmap / Cell Lookup
Force the model to scan a heatmap and combine information across rows and columns. Works well when cells are color-coded and labels are small.

**Example 1**: "Which is the country that is the least affected by all the products listed in this chart?"
**Example 2**: "What is the name of the subplot where its correlation matrix shows the strongest negative correlation between 'c4 restrictions on gatherings' and 'Positive rate' among all subplots?"

---

## 8. Flowchart / Graph Traversal
Ask the model to traverse a graph, map, or flowchart and find a path or intersection.

**Example**: "My friend is at Austin Station, and I am at Tsuen Wan Station. Which station would be the most convenient meeting point where our two lines intersect or connect?"

---

## Combining Strategies
The most effective prompts combine two or more strategies. For example:
- **Rank-n + Counting**: "Among the top-3 algorithms by reward at epoch 0, how many also appear in the top-3 at epoch 100?"
- **Legend-binding + Close comparison**: "Which of the two closest-performing models on Fashion-MNIST corresponds to the dashed line in the legend?"
- **Heatmap + Math**: "What is the sum of the three highest correlation values in the bottom-right subplot?"
