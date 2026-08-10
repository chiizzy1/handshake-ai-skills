# Handshake Grounding Hard Rollout Rubric

Use this reference for Grounding Hard Rollout tasks.

## Contents

- [Source PDF](#source-pdf)
- [Task Goal](#task-goal)
- [Three-Step Workflow](#three-step-workflow)
- [Critical Principle: Judge the Step, Not the Outcome](#critical-principle-judge-the-step-not-the-outcome)
- [Worked Example — The Butterfly Row](#worked-example-the-butterfly-row)
- [Confidence](#confidence)
- [When to Skip](#when-to-skip)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Common Mistakes](#common-mistakes)
- [Foundational Training](#foundational-training)
- [Comment Style Guidelines](#comment-style-guidelines)
- [Final Checklist](#final-checklist)

## Source PDF

- `HANDSHAKE-AI/project-hedgehog-pdfs/Project Hedgehog - Grounding Hard Rollout — Fellow Qualification Assessment.pdf`

## Task Goal

You verify and correct a model's attempt to find something in an image. You answer blind, reconcile against the dataset target, then critique the model's rollout and commit a verdict. Your judgment is the product.

## Three-Step Workflow

### Step 1 — Create the Blind Answer

Answer from the image and prompt alone. Draw a tight box around every visible instance of the target — one box per instance, flush to all four edges.

If no matching object exists in the image:
- Do not box a similar-looking object just because it is the only candidate.
- Tick "No matching object in the image."
- Do not skip the row. Skip is reserved for genuine blockers (broken image, truncated rollout, out of expertise, unsafe content).

### Step 2 — Compare with the Dataset Target

Your blind boxes (lime) and the dataset target (fuchsia) appear together. Pick one:

- **My blind** — your boxes are better.
- **The dataset target** — the dataset boxes are better.
- **Mixed** — some of yours and some of theirs.
- **Neither** — both are wrong.

The result is your confirmed set — the ground truth everything downstream builds on.

### Step 3 — Build the Final Answer

**Part 1 — Finalize boxes**: Your boxes are seeded from the confirmed set, with the model's prediction shown as a cyan reference. Diverge only if the rollout reveals something you missed, then Confirm.

**Part 2 — Rate every attempt**: The rollout contains a sequence of entries. Each entry is one of:

- **Thinking** — the model's written reasoning (e.g. deciding where an object's edges sit).
- **Tool call** — an action to gather information (e.g. cropping or zooming).
- **Tool output** — what the action returned (e.g. the cropped image).
- **Final answer** — the boxes and text the model submits.

Rate each attempt independently:

| Rating | Meaning |
|---|---|
| Correct | The step was needed and executed properly. |
| Unnecessary | The step should not have happened at all. |
| Incorrect | The step was needed but executed wrong. |

**Part 3 — Write the verdict**: Commit one verdict that matches what you did:

| Verdict | When to use |
|---|---|
| As-is | Final boxes/text untouched AND all trace attempts rated Correct. |
| Refined trace | Final boxes/text untouched, but 1+ trace attempts rated Incorrect/Unnecessary. |
| Refined answer | Final boxes/text edited, but all trace attempts rated Correct. |
| Refined both | Final boxes/text edited AND 1+ trace attempts rated Incorrect/Unnecessary. |

## Critical Principle: Judge the Step, Not the Outcome

The process and the final answer are graded independently because one can be right while the other is wrong.

- A model can reason sloppily, crop the wrong region twice, and still land on a correct final box by luck — a good outcome sitting on top of a broken process.
- Clean, sensible reasoning can end in a loose or mislabeled box.

If you judged only the final answer, you would sign off on the first case and reject the second, and both calls would be wrong.

**A crop that landed on the wrong object is Incorrect even if the model self-corrects later and the final box is perfect.** Rating it Correct because "the answer worked out anyway" is the single most common mistake on this task.

## Worked Example — The Butterfly Row

Prompt: "Show bounding boxes for black and white long limbs sucking nectar yellow in far beautiful flower."

1. **Blind step**: The Fellow boxed the butterfly and flower based on the prompt description.
2. **Compare step**: The Fellow's lime blind boxes (B1 around the full butterfly, B2 around the flower) are compared against the model's fuchsia target box (T1 around just the limbs).
3. **Answer step**: The model reveals its attempts and full rollout trace:
   - **Attempt Thumbnails Tile View**: Up to N attempt tiles shown side by side (e.g., Tile 1: original `/mnt/chat_data/000000.jpg`, Tile 2: red box crop `/tmp/overlay1.jpg`, Tile 3: green box crop `/tmp/overlay2.jpg`). Click any tile to expand, rate, and explain.
   - **Trace Log Entry Types**:
     - `bash SHELL` (e.g. `ls -l /mnt/chat_data`)
     - `Think` (e.g. reasoning about coordinates: `leftmost wing tip ~50, top ~214...`)
     - `view` (e.g. inspecting an image or overlay image file)
     - `bash DRAW BOX` (e.g. executing python script to generate bounding box crop overlay)
     - `Output` (e.g. image output or directory listing)
     - `Final` (e.g. `[{"x_min": 43, "y_min": 205, "x_max": 663, "y_max": 920}]`)
   - Each individual entry features a "Flag this step" control and must be evaluated independently.
   - Label color coding: Lime green boxes (B1, B2) for human blind boxes vs Fuchsia box (T1) for model targets vs Cyan box for Step 3 reference.

## Confidence

Rate 1–5 after the verdict — how sure you are of the verdict, not how good the model was. Do not default to 3.

- 5: certain
- 4: pretty sure
- 3: lean this way but could see the other side
- 2: honestly guessing more than knowing
- 1: no idea

## When to Skip

Skip is only for genuine blockers:

- Broken image
- Truncated rollout
- Out of your expertise
- Unsafe content

Never skip for difficulty, ambiguity, or "no matching object."

## Knowledge Check Answers

These are from the qualification assessment:

1. **Prompt: "the red kettle on the counter." The only kettle is plain stainless steel — no red kettle exists. What should you do in the blind step?**
   → Leave the canvas empty and tick "No matching object in the image." (Do not box the stainless kettle. Do not skip.)

2. **The model's first crop lands on the wrong shopping cart. Several steps later it notices, re-crops the correct cart, and its final box is right. How should you rate that first crop?**
   → Incorrect, because the step was needed but executed on the wrong cart. (Not Correct because the final answer worked out. Not Unnecessary because the step itself — cropping to find the cart — was needed.)

3. **You left the model's final box and text untouched because the answer was already correct, but you marked two attempts Incorrect for cropping the wrong region before self-correcting. Which verdict fits?**
   → Refined trace; the final answer needed no edits, but you flagged the reasoning.

## Common Mistakes

- Rating a wrong crop as Correct because the model self-corrected later.
- Boxing the closest-looking object when no matching target exists.
- Skipping because the prompt is difficult or no object matches.
- Defaulting confidence to 3 instead of being honest.
- Grading the rollout as a single unit instead of rating each entry separately.
- Working backward from the final answer to decide attempt ratings.

## Foundational Training

This task assumes the observation and rubric fundamentals:

- How to See — reading an image carefully before committing to what is there.
- Visual Quality — judging what is actually in the frame vs. what you expect.
- The per-attempt rating and verdict system described above.

## Comment Style Guidelines

When writing justification comments or rationale explanations:
- **Write like a normal human reviewer**: Use plain, direct, conversational English.
- **Keep it to 1–2 sentences**: State what should be done or what happened, and why, grounded in concrete evidence.
- **Avoid robotic AI fluff**: Avoid phrases like *"Upon careful observation," "demonstrates superior alignment,"* or stiff academic jargon.
- **Good Example**: *"The Fellow should draw a second box around the limes and lemon in the glass holder, since they are also citrus fruits on the counter."*
- **Bad Example**: *"Upon rigorous examination of the visual workspace, the annotator's initial boundary declaration exhibits an omission error regarding ancillary citrus specimens."*

## Final Checklist

- Prompt read before looking at the image.
- Blind boxes drawn tight and flush, one per instance.
- No matching object handled correctly (empty canvas, not a forced box).
- Comparison step completed honestly.
- Full rollout trace read top to bottom before rating anything.
- Each attempt rated on its own merits — step, not outcome.
- Verdict matches what was actually done.
- Confidence is honest and not defaulted to 3.
- Skip used only for genuine blockers.
