# Visual Tracking

Following paths, tracing lines through intersections, preserving identity across visual clutter, and filling symbols from visual continuity.

## Sub-types

### 1. Maze
Ask for the entrance, exit, or route determined by following a continuous path. Reject if paths are broken, hidden, cropped, or visually ambiguous. If the task asks for a route, define the route format.

**Example Q**: "The monkey enters the maze from the left side with the red arrow and has to reach the banana at the bottom right, marked by another red arrow. Along the one and only correct path through the maze, how many turns cause the monkey to travel in the upward direction relative to the viewer of the puzzle? Provide your answer as an integer (e.g., 5)."
**A**: 15 · Answer-Type: Integer

### 2. Metro Map
Ask for the station, path, or transfer relationship visible in the map. Keep the question visual — do NOT require real-world transit knowledge. Quote station names exactly as they appear on the map.

**Example Q**: "In this subway map, what is the minimum number of stations to pass through from 'Quis' station to 'Sit' station? (Transfers are allowed, excluding the origin and destination stations). Answer with an integer (e.g., 2)."
**A**: 6 · Answer-Type: Integer

### 3. Connect the Lines
Use when the main point of the question is tracking a single line along its path (which start point connects to which end point). The task should require tracking line identity through crossings or clutter. Reject if a line intersection is visually impossible to resolve. Use labels for starts and endpoints whenever possible.

**Example Q**: "There are three animal patterns at the top of the picture and three environment patterns below, which are connected by lines in order. What is the connection method? Assume the animal patterns above are A, B, C, and the environment patterns below are 1, 2, 3. Answer as the letter number pair, separated by a dash. Separate the pairs with a comma and sort in alphabetical order (e.g., A-1, B-2, C-3)."
**A**: A-2, B-3, C-1 · Answer-Type: Open-ended

### 4. Lines Observation
Use for questions about **traits of a line** rather than tracing it end-to-end (e.g., how many other lines it intersects, how many times it turns by 90 degrees, how many squares it passes through). Reject if a line intersection is visually impossible to resolve. Use labels for starts and endpoints whenever possible.

**Example Q**: "In the bottom left worksheet, there are four lines connecting two separate, fully visible columns of images. How many line intersections are there? Answer with an integer (e.g., 8)."
**A**: 5 · Answer-Type: Integer

### 5. Recognize Numbers and Letters
Use **only** when the answer follows from a visual pattern or missing-symbol task. Do NOT turn BabyVision into OCR-only reading. Quote image text exactly in the prompt (e.g., if the image says "exit labeled C", write "Which path leads to the exit labeled C?" — do NOT abbreviate to "exit C").

**Example Q**: "Which character is inside the yellow box? Answer with one letter (e.g., D). A. N  B. 2  C. Z  D. S"
**A**: B · Answer-Type: Multiple-Choice in-question

## Common Pitfalls

### ❌ Abbreviating image labels
**Bad**: "Which path leads to exit C?"
**Good**: "Which path leads to the exit labeled C?"
**Why**: Image text must be quoted exactly — shortening "exit labeled C" to "exit C" changes the reference.

### ❌ Requiring real-world transit knowledge
**Bad**: "How many stops between Shibuya and Shinjuku on the Yamanote Line?"
**Good**: "In this subway map, what is the minimum number of stations between 'Quis' and 'Sit'?"
**Why**: The question must be answerable purely from the visual map, not from real-world knowledge.

### ❌ Missing answer format
**Bad**: "In this subway map, what is the minimum number of stations to pass through from Quis station to Sit station?"
**Good**: "In this subway map, what is the minimum number of stations to pass through from 'Quis' station to 'Sit' station? (Transfers are allowed, excluding the origin and destination stations). Answer with an integer (e.g., 2)."
**Why**: The bad version lacks the answer format instruction and doesn't quote station names.
