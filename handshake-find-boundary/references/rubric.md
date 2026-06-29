# Handshake Find the Boundary Rubric

Use this reference for Find the Boundary tasks.

## Source PDF

- `handshake-Find the Boundary.pdf`

## Task Goal

You are testing an image-grounding AI model. You provide or judge a prompt about something in an image, run the model, then decide whether its answer is correct.

Every submission is either:

- a break/fail: the model is wrong and you correct it;
- a pass: the model is right.

The goal is not to win or lose. The goal is to find the capability boundary: where the model succeeds, fails, and what the edge looks like.

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

Do not switch formats mid-image to game the outcome.

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

## Ambiguous Prompts

Do not score ambiguous prompts. If the model trace is mostly trying to understand what the prompt means, the prompt is the problem.

Rewrite it to a specific, falsifiable target and rerun.

Example:

- Bad: `How many seams does it take to make the top part?`
- Better: `the bodice of the dress above the waist seam`

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
- `the matte cup, not the glossy cup`
- `the door that is ajar`
- `the cable plugged into the monitor on the right`

## Verdict: I Win / Model Failed

Pick fail when at least one of these is true:

- Wrong object: boxed/pointed at something that does not match the prompt.
- Missed object: under-counted or missed instances.
- Hallucinated object: returned more items than exist or invented something.
- Loose box: significant padding or cuts off the object.
- Wrong point: point lands off the object, on wrong instance, or on a non-salient part.
- Format violation: malformed JSON, wrong key, out-of-bounds coordinate, wrong number of items.

Tight means within about 5 percent of the visible silhouette on each side.

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

You may still edit the trace if the answer is correct but the reasoning is wrong.

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
- Use magnifier for tiny objects.
- Revert only when abandoning canvas edits.

## Tags

Use core tags by default. Tags describe what happened so similar cases can be grouped.

Tag categories:

- Failure Type: SmallObjectMiss, RelationSwap, NegationBlindness, etc.
- Challenge Strategy: AmbiguousReference, SmallTargets, MultiHopRelation, DenseOverlap, etc.
- Image Type: IndoorScene, ClutteredScene, TextOnObjects, etc.

Do not over-tag with overly specific labels.

## Confidence

Use honest 1-5 confidence:

- 5: certain
- 4: pretty sure
- 3: lean this way but could see the other side
- 2: honestly guessing more than knowing
- 1: no idea

There is no penalty for low confidence when it is genuine. A confident wrong answer is worse.

## Common Mistakes

- Passing "roughly right" loose boxes.
- Counting by default when the mode expects a point or box.
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
