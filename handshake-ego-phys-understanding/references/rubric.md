# Handshake Ego Physical Understanding Rubric

Use this reference for Egocentric Physical Understanding tasks.

## Source PDF

- `handshake-Ego Phys Understanding.pdf`

## Task Shape

You annotate first-person images by writing challenging multiple-choice questions that test physical reasoning.

Inputs:

- Category, pre-assigned per image.
- Question field.
- Four answer choices A-D.
- Task type: single-frame or multi-frame.

The question must be answerable only by carefully inspecting the image, not from general knowledge.

## Golden Rule

If someone can answer your question without ever looking at the image, it fails.

Ask:

- why
- how much progress
- what next
- what risk

Avoid:

- what is this
- where is this
- simple visible description
- general physics with no scene-specific constraint

## Automatic Rewrites

Rewrite the question if it:

- asks only what an object is;
- asks only where an object is;
- can be answered by knowing how the object usually works;
- has more than one reasonable correct answer;
- uses generic wrong answers;
- ignores the assigned category without changing category;
- uses only one frame in a multi-frame task.

## Egocentric Perspective

The camera is worn or held by the person doing the task. You see the world through their eyes.

You may see:

- the person's hands
- objects they are holding
- the immediate workspace
- reachable objects

You usually will not see:

- their face
- their full body

Use this to ask about:

- reachability
- grip constraints
- hand-object interactions
- what is behind vs in front
- what the user can or cannot do next

## Task Flow

1. Receive the task: single-frame or multi-frame, with assigned category.
2. Study the image:
   - objects
   - object state: open/closed, on/off, in progress
   - action underway
   - hazards and constraints
3. Decide:
   - proceed
   - change category
   - skip
4. Write the question using the category hardness standard.
5. Write four answers:
   - one clearly correct
   - three plausible near-miss distractors
6. Select the correct answer.
7. Submit. One attempt per task.

## Core Reasoning Principles

### Image dependency

The answer must depend on visible details.

### Reasoning over description

Avoid what/where questions. Ask why, how much progress, or what next.

### Egocentric leverage

Use the user's viewpoint: reachability, hand-object interactions, and what the user can or cannot see.

### Chained reasoning

Require multiple steps:

1. identify object
2. evaluate state
3. predict outcome

## Category Standards

### Counting

Use scenes where objects overlap, are occluded, or are partially visible at frame edges. The answer should require reasoning about hidden or partial objects.

### Grasp Affordance

Ask about the only viable grip given orientation, clutter, or what the hand already holds. Do not ask a generic "how would you pick this up?"

### Object Relationship

Use relative positioning between two or more specific objects to test 3D layout. The relationship should be functional or structural, not just direct adjacency.

### Pointing

Target an object whose identity depends on context, such as "the cup the user just set down." It should test state, not just shape.

### Process Verification

Pick mid-action scenes where correctness hinges on a subtle detail, such as a strap not buckled or a lid placed but not screwed on.

### Safety

Focus on non-obvious hazards from the combination of objects:

- knife near counter edge with child reach
- pot handle over burner
- unstable stack near hand path

Do not ask generic "is this dangerous?"

### Spatial Reasoning

Focus on 3D volume, height, and fit. Example: whether a foreground object would fit in a background container.

### State Estimation

Choose ambiguous states that require inspection:

- drawer slightly ajar
- faucet at low flow
- dim but on screen
- partially folded garment

### Task Affordance

Ask what action is blocked or enabled by the current configuration, not what an object can do abstractly.

### Task Planning

Require ordering of sub-steps with a non-obvious dependency. Example: move A before reaching B, even though B is the goal.

### Task Progress

Identify subtle work-in-progress states and ask about the next logical sub-task.

### Trajectory Reasoning

Include obstacles. A hard question requires a curved or non-linear path to avoid collisions, not a straight line.

### Other

Use only when no standard category fits. It must still demand image inspection and physical reasoning.

## Good Question Patterns

Trajectory:

- `Which path to the sink avoids knocking over the drying rack?`
- `How should the chair be rotated to fit through the doorway without hitting the frame?`
- `Which direction should the drawer be pulled to avoid hitting the person nearby?`

Object Relationship:

- `Which objects would fall if the large cookbook was pulled out from the shelf?`
- `What would happen to items on the tablecloth if it was suddenly pulled?`
- `Which items are being kept cold by their proximity to the ice in the cooler?`

Task Planning:

- `What should the user move first to reach the jar without knocking over the glass?`

## Bad Question Patterns

Bad because answerable without real scene reasoning:

- `Can a ball roll from the table to the floor?`
- `Which direction does the door swing to open?`
- `Would a straight line from the fridge to the stove be possible?`
- `If you push the toy car, which direction would it go?`
- `What objects are on top of the table?`
- `Which items are next to the lamp?`
- `Which objects are inside the cabinet?`

## Distractor Quality

Wrong answers must work as wrong answers.

Good distractors:

- are semantically similar in color, shape, or function;
- reference objects, positions, or states visible in the scene;
- are spatially close when the category is Pointing;
- require careful inspection to rule out.

Bad distractors:

- generic throwaways: `it does not matter`, `any approach works`
- unrelated to the scene
- obviously impossible
- skippable by logic alone

## Skip vs Change Category

Change category:

- Assigned category does not fit, but another standard category clearly produces a stronger image-dependent question.
- Do not overuse. It shifts dataset distribution.

Skip:

- Image is physically unusable: too dark, overexposed, corrupted, uninterpretable.
- Never skip because the category feels hard. Change category instead.

## Scoring Standard

### 5 - Exceptional

Every question requires the image. Strict category adherence. High-quality near-miss distractors. Flawless skip/category judgment.

### 4 - Strong

Avoids obvious questions. Has inferential depth. Multi-frame tasks require both images. No throwaway distractors.

### 3 - Acceptable

Image-dependent single-step reasoning. Generally follows category guidelines. Distractors are distinct and incorrect.

### 2 - Weak

Obvious or descriptive questions. Multi-frame tasks solvable from one frame. Throwaway distractors.

### 1 - Unacceptable

Answerable from general knowledge. High error rate. Misuse of Skip or Other.

## Pre-Submit Checklist

- Can this be answered without looking at the image? If yes, rewrite.
- Does it meet the category hardness standard?
- Are all three wrong answers scene-grounded near-misses?
- Is exactly one answer clearly correct and supported by visible evidence?
- For multi-frame: is the question impossible to answer from either frame alone?
