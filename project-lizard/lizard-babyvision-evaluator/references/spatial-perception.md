# Spatial Perception

Understanding spatial relationships, hidden or visible blocks, folds, rotations, and 2D-to-3D transformations.

## Sub-types

### 1. 3D Views
Ask which view or option matches the object after mental rotation. Reject if perspective conventions are inconsistent or impossible to infer. **No Yes/No questions** (e.g., "Is option A the front view?" is invalid — rewrite as a letter-based MCQ asking which option shows the front view).

**Example Q**: "Assuming that all cubes in the shape have a visible face, which of the 4 options is the front view of this 3D figure? Answer with one letter (e.g., B)."
**A**: A · Answer-Type: Multiple-Choice in-image

### 2. 3D Cube Unfold
Ask which folded or unfolded option matches. Explanation should reference adjacency, opposite faces, orientation, or visible marks. Note: the shape doesn't have to be a cube — any polyhedron net qualifies.

**Example Q**: "Which cube can be folded from the unfolded shape in figure 1? Answer with one letter (e.g., B). A. Cube 6  B. Cube 7  C. Cube 3  D. Cube 8"
**A**: A · Answer-Type: Multiple-Choice in-image

### 3. Paper Folding
Ask which folded or unfolded option matches. Explanation should reference adjacency, opposite faces, orientation, or visible marks.

**Example Q**: "The figure shows a square folded three times along its axis of symmetry, and then a small triangle is cut off. Choose the correct unfolded option. Answer with a single letter (e.g., F)."
**A**: D · Answer-Type: Multiple-Choice in-image

### 4. Count 3D Blocks
Ask for the total number of blocks when the structure is clear. **Critically important**: Make clear whether hidden/supporting blocks should be counted if they are implied by the shape. Specify how any obscured faces should be handled.

**Example Q**: "The image shows a 3D shape made of stacked cubes. Assume all cubes in the 3D shape have at least one face visible. What is the minimum number of cubes? Answer with a number (e.g., 5)."
**A**: 7 · Answer-Type: Integer

### 5. 3D Pattern Completion
Ask which 3D piece completes the arrangement. Reject if the missing piece depends on subjective perspective rather than a clear spatial rule.

**Example Q**: "Select the appropriate option to complete the cube. Return the correct option. Answer with a single letter (e.g., B). A. The first one below  B. The second one below  C. The third one below"
**A**: A · Answer-Type: Multiple-Choice in-question

## Common Pitfalls
- **Yes/No questions**: Never ask "Is option A the correct front view?" — convert to an MCQ: "Which option is the correct front view? Answer with a single letter (e.g., B)."
- **Ambiguous hidden blocks**: If the structure has supporting blocks that aren't visible, the prompt MUST say whether to count them. Without this, the answer is ambiguous.
- **Perspective consistency**: If the 3D view's perspective conventions (e.g., which direction is "front") are inconsistent or impossible to infer from the image, reject the image.
