# Fine-grained Visual Discrimination

Detecting subtle visual differences, matching exact shapes, comparing colors or patterns, and identifying missing pieces.

## Sub-types

### 1. Find the Different
Ask for the unique item, location, or option. Use grid coordinates when there are many items. When you do, explicitly define the indexing AND start it at (1, 1), not (0, 0) — both are required to keep the answer unambiguous. Reject if more than one item appears different.

**Example Q**: "The image shows a total of 49 tiger patterns arranged in 7 rows and 7 columns. One of them is different from the others. Which row and column is it in? Answer in the format (x, y) where x is the row and y is the column (e.g., (1, 1))."
**A**: (4, 7) · Answer-Type: Open-ended

### 2. Find the Same
Ask which option exactly matches a target. Match should depend on shape, orientation, internal pattern, color layout, or relative part placement. Reject if multiple options are effectively identical.

**Example Q**: "In the image, some shoe patterns are same in pairs. Find the index pairs of these identical shoes. Answer with the pair's numbers, separated by a dash, with the numbers ordered in increasing order and pairs separated by a comma (e.g., 1-2, 3-4)."
**A**: 1-7, 2-9, 3-10, 4-8, 6-11 · Answer-Type: Open-ended

### 3. Find the Shadow
Ask which silhouette exactly matches the object. The answer should not depend on subjective resemblance.

**Example Q**: "There are 12 patterns in 4 rows and 3 columns, each with a number from 1–12. Among them, 1, 3, 5, 7, 9, 11 are specific patterns, and 2, 4, 6, 8, 10, 12 are shaded patterns. If the specific patterns and shaded patterns can be matched in terms of shape, what is the result? Answer in the format X-Y, where X increases sequentially and each pair separated by a comma (e.g., 1-3, 2-4)."
**A**: 1-4, 3-12, 5-10, 7-2, 9-6, 11-8 · Answer-Type: Open-ended

### 4. Reconstruction
Ask which option fills the missing piece or completes the pattern. Make the direction/order of the pattern clear. Reject if the missing piece can be solved only by guessing.

**Example Q**: "In the image is an excavator, then which of the options can constitute all the parts of this excavator? Answer with a single letter (e.g., D)."
**A**: B · Answer-Type: Multiple-Choice in-image

### 5. 2D Pattern Completion
Ask which option fills the missing piece or completes the pattern. Make the direction/order clear.

**Example Q**: "Which of the following 3 images can fill the missing part at the top of the figure? The 3 patterns are numbered 1, 2, and 3 from left to right. Answer with a single letter (e.g., A). A. 1  B. 2  C. 3"
**A**: C · Answer-Type: Multiple-Choice in-question

### 6. Count Clusters
Use when the task is mostly object or group enumeration — counting objects based on location or grouping. Typical prompts: "How many objects are in each group?", "Compare the number of items on the left vs right." The units are usually irregular, object-like, or grouped/cluttered. Counting is valid only when the challenge is **structured visual discrimination**, not trivial object counting. Avoid excessive counts unless the structure is very clear.

**Example Q**: "A picture with several sticks is divided into 9 sections. How many sticks are there in total? Answer with a number (e.g., 10)."
**A**: 18 · Answer-Type: Integer

### 7. Count Same Patterns
Use when the task is mostly matching a repeated pattern type and counting its occurrences. Typical prompts: "How many blue stars?", "How many black squares?", "How many shapes match this reference?", "Fill counts for each legend shape." The units are usually repeated shapes/icons/cells/matchsticks/pattern elements.

**Heuristic**: Counting by location or group → Count Clusters. All other counting descriptions → Count Same Patterns. Use best judgment on borderline cases — annotators and auditors shouldn't be overly critical of the categorical difference between these two when the choice is reasonable.

**Example Q**: "In the pattern, how many points do the blue line segments pass through in total? Answer with an integer (e.g., 2)."
**A**: 14 · Answer-Type: Integer

### 8. Pattern and Color Completion
Ask which option fills the missing piece or completes the pattern.

**Example Q**: "The following 4 small figures are labeled A, B, C, D from left to right. Which of them is the label for the missing part in the large figure above? Answer with a single letter (e.g., D)."
**A**: A · Answer-Type: Multiple-Choice in-question

## Prompt Quality Reminders
- Do NOT use first-person phrasing (e.g., "I want you to carefully examine…"). Use direct instructions.
- Do NOT give away the answer in the prompt (e.g., "The top-left and bottom-right sections contain the most sticks" — this reveals where to look).
- Keep prompts short and direct. BabyVision difficulty must come from the image, not from long or hard-to-parse sentences.
