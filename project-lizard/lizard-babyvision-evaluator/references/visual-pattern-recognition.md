# Visual Pattern Recognition

Inferring the visual rule and applying it to select or produce the next item.

## Sub-types

### 1. Logic Patterns
Ask for the next item or missing item in a visual sequence.

**Example Q**: "Please tell me, according to the pattern, which of the three figures below should be filled in the question mark? Answer with a single letter (e.g., B). A. Left  B. Middle  C. Right"
**A**: A · Answer-Type: Multiple-Choice in-question

### 2. Rotation Patterns
Ask which option follows a rotation rule. Specify the answer format and avoid vague "looks rotated" wording — be explicit about the rotation direction and amount (e.g., "rotate one quarter-turn clockwise", "rotation by one face in the clockwise direction per arc of the arrow").

**Example Q**: "Which shape belongs at the top question mark? You may assume that the arrows indicate a rotation by one face in the clockwise direction per arc of the arrow. Answer with one letter (e.g., B). A. Shape 2  B. Shape 4  C. Shape 6  D. Shape 8"
**A**: C · Answer-Type: Multiple-Choice in-image

### 3. Mirroring Patterns
Ask which option is the mirror result or completes a mirrored pair. Mention the mirror axis if the image does not make it obvious.

**Example Q**: "Look at the first three rows of letters of the alphabet on the right side of the image. How many of these letters have both a vertical and horizontal line of symmetry? Answer with a whole number (e.g., 1)."
**A**: 2 · Answer-Type: Open-ended

### 4. Overlay Patterns
Ask which result comes from combining visual layers. Explanation should state which parts remain visible or combine.

**Example Q**: "The image shows two rows of figures, each row containing 3 geometric figures. A part of each figure is white and a part is red. According to the pattern in the image, which of the options should be the 3rd figure in the second row? Answer with a single letter (e.g., B)."
**A**: A · Answer-Type: Multiple-Choice in-image

## Common Pitfalls

### ❌ Giving away the reasoning strategy
**Bad**: "Visual sequences typically follow rotation or reflection rules. Which option most likely completes this type of pattern?"
**Good**: "According to the pattern shown in the image, which of the three figures below should fill the question mark? Answer with a single letter (e.g., B)."
**Why**: The bad prompt tells the model the strategy ("rotation or reflection") — the model should figure that out from the image.

### ❌ Subjective color matching
**Bad**: "Which option is the most bluish-purple match for the right side of the symmetrical figure?"
**Good**: "The graphic has a vertical dashed line as the axis of symmetry. Which of the given options should be the right part? Answer with a single letter (e.g., B)."
**Why**: "Most bluish-purple" is subjective and unverifiable. The good version asks about symmetry — a clear visual primitive.
