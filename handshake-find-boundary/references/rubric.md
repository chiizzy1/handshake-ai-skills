# Handshake Find the Boundary Rubric

Use this reference for Find the Boundary tasks.

## Source PDF

- `HANDSHAKE-AI/pdfs/handshake -- Find the Boundary.pdf`

## Task Goal

You are testing an image-grounding AI model. You provide or judge a prompt about something in an image, run the model, then decide whether its answer is correct.

Every round is one of:

- a break/fail / `I win`: the model is wrong and you correct it;
- a pass / `AI wins`: the model is right as-is;
- a discard/rewrite: the prompt is ambiguous, ungroundable, or asks about non-visible content.

The goal is not to win or lose. The goal is to find the capability boundary: where the model succeeds, fails, and what the edge looks like.

The best submissions usually sit near the boundary: roughly a 50-70 percent chance that the model gets the image/prompt pair right. A 99 percent easy win is not informative, and a 1 percent impossible case is likely out-of-distribution rather than boundary-probing.

## Task Workflow

1. Pick an image with enough going on to probe: multiple objects, occlusion, or similar items the model must tell apart.
2. Choose bounding box, point, or counting before running the model.
3. Write a short, grounded prompt that an attentive human can confirm.
4. Run the model and inspect both the output and the thinking trace against the image.
5. Judge pass, break, or discard. If it is a break, correct the output.

Do not switch formats after seeing the answer to force a pass or fail.

## Operational UI Notes

- Images may be uploaded directly or supplied by URL. The source method does not change the rubric: judge only what is visible in the provided media.
- If the platform says to watch the full video, follow that instruction only when the task actually includes video media. For standard Find the Boundary image rounds, the relevant evidence is the image.
- Session stats, streaks, exploration depth, badge unlocks, and toast messages are informational only. Do not chase badges or let them influence whether a prompt is high-signal.
- A useful shorter session with careful boundary examples is better than a long streak of hollow submissions.
- On pass / `AI wins`, answer confidence is N/A; the verdict itself is the answer judgment. Rate trace confidence only.
- On fail / `I win`, rate trace confidence and answer confidence. Answer confidence covers either the corrected canvas answer or, if no canvas edit was needed, your confidence that the model answer was wrong.
- If the prompt asks for an object or target that is not present and the correct human response would be "there is no such thing", the prompt is malformed. Discard or rewrite it; do not score it as a model failure.

## Output Formats

### Bounding Box

Model's job:

- Draw a tight box around the object(s) described.

Example:

- `the red mug to the left of the laptop`

### Point

Model's job:

- Place a single point on the object described.

Example:

- `the recycle button on the screen`

### Counting

Model's job:

- Count the objects matching the prompt and return one point per instance.

Example:

- `the orange fish swimming behind the rocks`

Do not switch formats mid-image to game the outcome. Pick the format that matches what you actually want the model to do.

## Writing Good Prompts

Good prompts are:

- specific
- falsifiable
- grounded in visible content
- answerable by an attentive human

Use:

- specific references: `the small red button next to the search bar`
- stacked constraints: `the second cat from the right that is NOT looking at the camera`
- spatial relations: left of, above, closest to, partially hidden by
- negation: `the dog that is NOT wearing a collar`
- attributes: color, size, orientation, material, state

Do not:

- reference things not in the image;
- write open-ended prompts like `describe the picture`;
- write ambiguous prompts where multiple objects equally satisfy the constraints;
- use NSFW, PII, or copyrighted content;
- probe identifiable people unless they are public figures in a clearly public context.

If a target is absent, that is not a clever hard prompt. It is an invalid prompt for this task type because the model is supposed to ground visible content, not prove nonexistence.

## Ambiguous Prompts

Do not score ambiguous prompts. If the model trace is mostly trying to understand what the prompt means, the prompt is the problem.

Discard or rewrite it to a specific, falsifiable target and rerun. Do not turn a broken prompt into a model failure.

Example:

- Bad: `How many seams does it take to make the top part?`
- Better: `the bodice of the dress above the waist seam`

The dress example in the PDF is a discard/rewrite case: the model trace spends its budget guessing whether the prompt means the top part, the seams, or zero visible seams. That is not grounding; it is prompt ambiguity.

## Pass/Fail Gate

Before passing a model answer, verify:

- the target exists in the image;
- the prompt identifies one clear target set;
- every returned box or point is on the correct target;
- every required instance is included;
- no extra instance is included;
- box tightness is within tolerance;
- output format matches the task mode.

If any item fails, mark fail and correct the answer.

For counting mode, the model must return one point per visible matching instance plus the correct final count. Finding only the obvious instance is still a fail if other matching objects are visible.

## Hard Images

Good boundary work pairs hard prompts with hard images.

Hard image types:

- dense clutter: crowds, supermarket shelves, toolboxes, fish tanks
- small targets: UI icons, fine print, small birds
- low contrast/camouflage
- heavy occlusion
- unusual viewpoint or framing
- visual interference: blur, glare, reflections, neon scenes
- repetitive patterns and identical objects
- text-heavy scenes
- out-of-domain images: medical, industrial, satellite, microscopy, diagrams, game screenshots
- multi-instance ambiguity

## Hard Prompt Patterns

Useful prompt stressors:

- multi-hop spatial reasoning
- negation and exclusion
- ordinal references
- counting under stress
- subtle attribute distinctions
- constraint stacking
- affordance or state references
- cross-reference between objects

Examples:

- `the cup to the left of the lamp that is closest to the window`
- `every bottle except the green one`
- `the third book from the right`
- `the fifth person in the second row from the back`
- `the matte cup, not the glossy cup`
- `the chair that is rotated`
- `the door that is ajar`
- `the button that is pressed`
- `the cable plugged into the monitor on the right`

Strong prompt/image pairings from the PDF:

- dense bottle shelf + `the third bottle from the left in the second row that is NOT green`
- busy UI screenshot + `the close button on the dialog box in the background, not the modal in front`
- flock of birds + `the bird in flight whose wings are pointed downward`

## Boundary-Pair / Tweak Flow

When available, use `Tweak This` to submit a deliberate variation on the same image. A useful pass/fail pair on one image is one of the most valuable submissions.

Good tweak:

- original: `the red mug`
- harder variant: `the red mug to the left of the laptop`

Do not force pairs just for badges. If the predicted verdict does not flip and the UI warns that the boundary did not move, submit anyway if the tweak was meaningful.

## Verdict: I Win / Model Failed

Pick fail when at least one of these is true:

- Wrong object: boxed/pointed at something that does not match the prompt.
- Missed object: under-counted or missed instances.
- Hallucinated object: returned more items than exist or invented something.
- Loose box: significant padding or cuts off the object.
- Wrong point: point lands off the object, on wrong instance, or on a non-salient part.
- Format violation: malformed JSON, wrong key, out-of-bounds coordinate, wrong number of items.

Tight means within about 5 percent of the visible silhouette on each side.

A box with about 15 percent padding on every side is a fail even when it encloses the right object. Tighten it instead of passing it.

When fail is chosen:

1. Fix boxes or points.
2. Edit answer text if structurally malformed or counting label is wrong.
3. Fix the thinking trace if wrong in a specific, citable way.
4. Add tags: failure type and challenge strategy.
5. Add a one-line failure description if needed.
6. Rate confidence.

## Verdict: AI Wins / Model Passed

Pick pass when:

- boxes are tight enough;
- points are on the correct object;
- count is right in counting mode;
- no missed items;
- no hallucinated items;
- format is valid.

You may still edit the trace if the answer is correct but the reasoning is wrong, such as citing the wrong landmarks while landing on the right object.

## When In Doubt

If genuinely 50/50, treat it as fail and correct what the model should have done.

A confident correction is more useful than a coin-flip pass.

If a box is loose enough to bother you on a pass, it is probably a fail.

## Editing Canvas Rules

- Add a box by dragging on empty canvas.
- Add a point by single-clicking.
- Move a box or point by dragging.
- Resize a box by dragging a corner handle.
- Delete selected items with Backspace/Delete.
- Use repeated clicks to cycle overlapping boxes/points.
- Use the 5x magnifier for tiny objects; it follows the cursor with a crosshair and live draft rectangle.
- Revert only when abandoning canvas edits.
- Undo/redo with standard Ctrl/Cmd-Z and Ctrl/Cmd-Shift-Z.

For tiny targets such as favicons, single icons, small badges, and fine print, use the magnifier workflow: turn it on, hover over the target, and drag the box at 5x zoom for pixel-accurate edges.

## Tags

Use core tags by default. Tags describe what happened so similar cases can be grouped.

Tag categories:

- Failure Type: SmallObjectMiss, RelationSwap, NegationBlindness, etc.
- Challenge Strategy: AmbiguousReference, SmallTargets, MultiHopRelation, DenseOverlap, etc.
- Image Type: IndoorScene, ClutteredScene, TextOnObjects, etc.

Do not over-tag with overly specific labels.

## Confidence

Use honest 1-5 confidence. After every submission, the UI may ask for trace confidence. On fail, it may also ask for answer confidence on the corrected answer.

On pass / `AI wins`, answer confidence is N/A. Do not invent an answer-confidence rating for a correct locked answer.

- 5: certain
- 4: pretty sure
- 3: lean this way but could see the other side
- 2: honestly guessing more than knowing
- 1: no idea

There is no penalty for low confidence when it is genuine. A confident wrong answer is worse.

## Common Mistakes

- Passing "roughly right" loose boxes.
- Counting-by-default in counting mode or failing to scan for all instances.
- Switching format to win.
- Scoring vague prompts instead of rewriting.
- Editing the answer on a pass when it should simply pass.
- Forgetting the magnifier for tiny objects.
- Chasing badges instead of careful boundary examples.

## Final Checklist

- Prompt is visible-grounded and specific.
- Output format is correct.
- Model answer checked against every target.
- Fail/pass verdict follows the rules.
- Corrections are precise.
- Tags are meaningful.
- Confidence is honest.
