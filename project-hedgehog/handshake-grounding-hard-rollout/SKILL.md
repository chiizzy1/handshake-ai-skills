---
name: handshake-grounding-hard-rollout
description: Evaluate Handshake Grounding Hard Rollout tasks. Use when verifying and correcting a model's grounding attempts on an image; when answering blind, comparing against the dataset target, reviewing a model's rollout trace of thinking/tool-calls/tool-outputs/final-answer, rating each attempt as Correct/Unnecessary/Incorrect, or committing a verdict of As-is/Refined trace/Refined answer/Refined both.
---

# Handshake Grounding Hard Rollout

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use `HANDSHAKE-AI/pdfs/Project Hedgehog - Grounding Hard Rollout — Fellow Qualification Assessment.pdf` as the source of truth.

Before doing a live task, read `references/rubric.md`.

This is not a simple pass/fail grounding task like Find the Boundary. Do not answer with pass/fail verdicts or challenge tags. This task has a three-step workflow with rollout trace review and per-attempt ratings.

## Task Shape

Grounding Hard Rollout items have three steps:

1. **Step 1 — Blind answer**: Draw tight bounding boxes from the image and prompt alone, before seeing the model's answer. One box per instance, flush to all four edges. If no matching object exists in the image, tick "No matching object in the image" — do not box something that does not match.

2. **Step 2 — Compare with dataset target**: Your blind boxes (lime) and the dataset target (fuchsia) appear together. Pick My blind, The dataset target, Mixed, or Neither. The result is your confirmed set — the ground truth everything downstream builds on.

3. **Step 3 — Build the final answer and rate the rollout**:
   - Part 1: Your boxes are seeded from the confirmed set, with the model's prediction as a cyan reference. Diverge only if the rollout reveals something you missed, then Confirm.
   - Part 2: Rate every attempt Correct, Unnecessary, or Incorrect, judging each on its own merits.
   - Part 3: Write a verdict that matches what you did.

## Mandatory Workflow

1. Read the prompt before looking at the image.
2. Create blind boxes from image and prompt alone (Step 1).
3. Compare your blind boxes against the dataset target (Step 2).
4. Review the model's full rollout trace top to bottom before rating anything (Step 3).
5. Rate each attempt independently.
6. Commit the verdict.
7. Rate confidence 1–5 in your verdict call.

## The Rollout

A rollout is a sequence of separate entries, not one thing to grade as a whole:

- **Thinking** — the model's written reasoning, like deciding where it believes an object's edges sit.
- **Tool call** — an action it takes to gather information, like cropping or zooming into part of the image.
- **Tool output** — what that action returns, like the cropped image itself.
- **Final answer** — the boxes and text it ultimately submits.

The process (thinking and tool calls) and the final answer are graded independently, because one can be right while the other is wrong.

## Per-Attempt Ratings

Rate each attempt on its own merits:

- **Correct** — the step was needed and executed properly.
- **Unnecessary** — the step should not have happened at all.
- **Incorrect** — the step was needed but executed wrong.

## Critical Rule: Judge the Step, Not the Outcome

A crop that landed on the wrong object is **Incorrect** even if the model self-corrects later and the final box is perfect. Rating it Correct because "the answer worked out anyway" is the single most common mistake on this task.

## Verdict Options

Commit one verdict that matches what you did:

- **As-is** — the model reached the right answer (final boxes untouched) AND all trace attempts were Correct.
- **Refined trace** — the final answer needed no edits, but you flagged the reasoning (marked 1+ attempts Incorrect or Unnecessary).
- **Refined answer** — the final boxes/text needed edits, but all trace attempts were Correct.
- **Refined both** — you edited the final boxes/text AND marked 1+ trace attempts Incorrect or Unnecessary.

## UI Color Coding Reference

- **Lime green**: Your blind boxes (Step 1 & 2).
- **Fuchsia (magenta/pink)**: Dataset target boxes (Step 2).
- **Cyan (light blue)**: Model's predicted reference boxes (Step 3).

## Confidence

After the verdict, rate your confidence 1–5 in that call — how sure you are of the verdict, not how good the model was. Do not default to 3.

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

## Hard Gates

- Do not box an object that does not match the prompt just because it is the only similar thing in the image.
- Do not rate a step Correct just because the final answer turned out right.
- Do not skip because the prompt is difficult or the target is absent — use "No matching object" instead.

## Comment Style

When free-response rationale comments are required, write like a normal human reviewer pointing out real evidence:

- **Keep it plain, short, and direct**: Write 1-2 sentences in natural, conversational English.
- **Tie to concrete evidence**: Name specific objects, visual locations, or step numbers.
- **Avoid AI fluff and stiff jargon**: Do NOT use phrases like *"Upon careful observation," "demonstrates superior alignment," "it is evident that,"* or overly formal academic language.
- **Examples**:
  - *Good*: "The Fellow should draw a second box around the limes and lemon in the glass holder, since they are also citrus fruits on the counter."
  - *Good*: "The second crop was unnecessary because the model already had the yellow mug located and boxed correctly after the first attempt."
  - *Bad*: "Upon rigorous examination of the visual workspace, the annotator's initial boundary declaration exhibits an omission error regarding ancillary citrus specimens."
- Do not grade the rollout as a whole. Rate each entry separately.
- Do not let the model's self-correction retroactively upgrade earlier wrong steps.
- Read the full rollout trace before rating any individual attempt.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Answer in the chat.

```markdown
### Step 1 — Blind Answer
[Describe what you would box from the image and prompt alone. If no matching object exists, state that.]

### Step 2 — Compare
[Which set do you pick: My blind, The dataset target, Mixed, or Neither? Why?]

### Step 3 — Rollout Review
[For each attempt in the rollout, state the attempt number, type (Thinking/Tool call/Tool output/Final answer), and your rating (Correct/Unnecessary/Incorrect) with a brief reason.]

### Verdict
[As-is | Refined trace | Refined answer | Refined both]

### Confidence
[1-5]
```

## Relationship To Other Handshake Skills

- Use `handshake-find-boundary` (read `../handshake-find-boundary/SKILL.md`) for Find the Boundary tasks where you write prompts and judge pass/fail with challenge tags.
- Use this skill for Grounding Hard Rollout tasks where you review the model's multi-step rollout trace and rate each attempt independently.
- Both share bounding-box mechanics and the same visual inspection fundamentals from HOW TO SEE.

## Final Checklist

- Prompt read before looking at the image.
- Blind boxes drawn tight and flush.
- Comparison step completed honestly.
- Full rollout trace read before rating.
- Each attempt rated on its own merits, not the outcome.
- Verdict matches what was actually done.
- Confidence is honest and not defaulted to 3.
- Skip used only for genuine blockers.
