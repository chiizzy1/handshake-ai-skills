---
name: handshake-t2i-dual-boxes
description: Evaluate Handshake T2I Image Comparison tasks that use the Dual boxes explanation. Use when a task shows a text prompt with Response A and Response B images, an Overall Preference row reading Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B, and an Explain Response A and/or B section with two evidence boxes where one box is required and 50+ characters total; when the task header says T2I Image Comparison, Required explanation, or Dual boxes.
---

# Handshake T2I Dual Boxes

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/rubric.md` in this skill folder.
2. `HANDSHAKE-AI/t2i/vs-1788333814-comment-dual-boxes.md`, the full guideline with its worked examples.

**The rating is the easy half. The written evidence is the deliverable.** Every bad example in the
guideline is a defensible rating ruined by a comment that names nothing. A correct verdict with a
generic comment fails.

Concise and specific beats long and generic. The task evaluates content, not a character count.

This is not the visual-appeal task. There is a prompt here, and prompt adherence outranks beauty.
A prettier image that misses the central requirement loses.

## Sibling Task

This is the **two-box** variant. Its twin, `handshake-t2i-live-feedback`
(`project-hedgehog/handshake-t2i-live-feedback/SKILL.md`), is the **one-box** variant of the same
family: identical rating scale, evidence tests, skip rules, and boundary cases.

| Cue | Task | Skill |
|---|---|---|
| Two boxes, "What specific evidence did you notice in Response A / B?", "One box required, 50+ characters total" | T2I Image Comparison 2, Dual boxes | this skill |
| One box plus a "Check my justification" button | T2I Image Comparison 3, Live feedback | `handshake-t2i-live-feedback` |

| A record button, a 45-second timer, and a transcript to confirm | T2I Voice input and translation | `handshake-t2i-muse-dictation` |
| Clickable markers placed on the evidence | T2I Point + write | `handshake-t2i-point-write` |

If the UI shows one evidence box with a checker button, you are in the wrong skill.

## Task Shape

- A **Prompt** block at the top, then **Response A** and **Response B** images side by side.
- **Overall Preference**, five buttons: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- **Explain Response A and/or B**, two boxes: "What specific evidence did you notice in Response A?" and the same for B.
- Header badges: `Required explanation`, `Dual boxes`. Corner note: "One box required, 50+ characters total across A and B".
- Submit button reads "Submit rating and explanation". Below it: "Skip only if the comparison cannot be judged".

The UI enforces order. Choose Overall Preference first, then the boxes unlock.

## The Character Rule

The UI counter reads **50 characters total across A and B**. The guideline text asks that **each box
you complete carry at least 50 characters of specific evidence**.

Write to the stricter standard. Any box you open gets a full, specific observation. Never treat the
counter hitting 50 as the finish line.

## Dual Boxes

- At least one box is required. **The second box is genuinely optional.**
- Leave the other box empty when it adds no useful evidence. **Do not pad an unused box.** "Add filler so both boxes are populated" is an explicit wrong answer.
- If both responses share a defect, one box may state how that defect appears across both.
- Use the boxes for visible evidence, not for restating the verdict you already clicked.

Two boxes is the normal case for a real difference, because a comparison needs both sides. One box is
correct when the evidence lives entirely on one side, such as one response being blank.

## The Scale

| What you found | Your rating |
|---|---|
| One response satisfies the central requirement, the other misses it or has a major defect | Strongly prefer that one |
| Both satisfy the central requirement, one is marginally better | Slightly prefer that one |
| Mixed strengths producing a small overall edge | Slightly prefer that one |
| You cannot name a relevant detail favoring either side | Tie |
| Both share the same defect at the same severity | Tie |

Tie is not for "close". Tie is for "no nameable relevant difference". If you can name the deciding
detail, pick the side and name it.

## Evidence Test

Every claim must pass all three:

1. **Locate it.** Name or select an object, word, body part, region, count, framing choice, or other visible detail.
2. **Discriminate.** Explain how A and B differ, or why a shared defect makes them a tie.
3. **Stay accurate.** Describe only what is visible. Never invent a reason to complete the task.

Generic phrases such as *looks better*, *better quality*, or *follows the prompt* are not enough by
themselves. Add the visible fact that makes the phrase true.

A concrete aesthetic difference is valid evidence. Name the property and say which response exhibits
it more strongly. "A uses softer fill light on the face; B has a harsh side light that flattens the
cheek and eye area" is aesthetic and still concrete.

## Mandatory Workflow

1. **Read the prompt first.** Identify the central requirement before looking at either image. Write it down in your head as a testable claim.
2. **Skip check.** Run the boundary rules below. Skip overrides every rating and overrides Submit.
3. **Inspect Response A against the prompt.** Then Response B. Both, before you rate.
4. **Rank the requirements.** Which one is central? Secondary quality differences lose to it.
5. **Choose the rating** from the scale.
6. **Write the evidence.** One box or both. Each opened box carries a located, discriminating, accurate observation.
7. **Agreement check.** Do the comment and the rating point at the same decision? If they disagree, fix one of them before submitting.

## Skip Rules

Skip overrides every rating and Submit. Apply in this order: restricted or uninspectable content
means Skip, a loaded output means rate the observed result, partial success means prioritize the
central requirement, a close call means name the deciding detail.

**Skip when:**

- The prompt fails to load, or either response fails to load. Skip even if the other one loaded.
- One response fails to load and the other loads blank. The uninspectable side prevents a valid comparison.
- The prompt's primary requirement cannot be understood, even when both responses render perfectly.
- A safety notice in the task interface, or guidance from the task owner before the session, says not to inspect or rate the content.

**Do not skip when:**

- A response loads and is **blank**. That is observable output. Treat it as a failure and rate it.
- A secondary label or some secondary text is unfamiliar, but you can identify the primary requirement and evaluate both responses against it. Rate normally and mention the partial readability.
- The subject is merely unfamiliar or difficult. Every assigned subject is in scope.

**Never submit a partial entry.** Partial entries are discarded when the next comparison loads.

## Blank Versus Not Loading

This is the distinction the task tests most.

| What you see | What it is | What you do |
|---|---|---|
| Response renders an image | Model output | Rate it |
| Response loads, shows a genuinely blank image | Model output, and a visible failure | Rate it, prefer the other one, name the blankness |
| Response never loads | Tooling failure | Skip |
| One blank, one will not load | Mixed | Skip |

Never score an infrastructure failure as model output. Never invent a tooling error for output that
loaded. "Tie, A might still be loading" is an explicit wrong answer.

## Boundary Cases

- **Both responses fail.** Name the shared failure, then say which version is less severe. Tie only if the failures are genuinely equivalent.
- **One response visibly fails the requirement.** Prefer the one that succeeds and name the observed failure as the discriminating evidence.
- **Both partly satisfy.** Rate on the requirement most central to the prompt. Name that requirement and why it outweighs the other differences.
- **Pure aesthetics.** A concrete aesthetic difference is valid. Name the property and which response has it more strongly.
- **Language barrier.** Rate normally only if you can identify the primary requirement and test both responses against it. Mention partial readability. Unreadable prompt means Skip.
- **Close call.** Choose the slight preference that matches your judgment and explain the one detail that broke the tie.

## How to Write the Boxes

Each box answers "what specific evidence did you notice in this response?" Write what is visible,
in plain language, as if pointing at the screen for another reviewer.

### Voice

**Persona: a careful person saying what they saw, not an evaluator filing a report.**

- **Name the thing.** The object, the word, the body part, the region. Not a category word like "composition" or "quality."
- **Short sentences. Periods.** Plain words in plain order.
- **Use "while" instead of "whereas"** when contrasting.
- **Avoid absolutes.** "Perfectly rendered" becomes a factual error the moment someone zooms in. "Sharper" and "cleaner" survive.
- **Give the loser its due.** If the losing response looks better in some way, say so, then say why it still lost. The camera-move exemplar does exactly this: "so A wins despite B's smoother lighting."
- **No AI power words.** Delve, tapestry, meticulous, striking visual narrative, seamlessly.
- **Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "semantic," "it is evident that," "exhibits," "the aforementioned," "aligns with the prompt."

### The semicolon exception

The house style across these skills bans semicolons. **This task is the exception.** Its own exemplars
use them to join the A half and the B half:

> "A reads STOIP with one extra stroke; B changes the final P into an R."

The task's own guideline outranks the house baseline, so a semicolon joining two parallel observations
is correct here. A period is always safe if you prefer one.

### The pattern to copy

Nearly every good exemplar is the same shape: **same property, named on both sides.**

> A does X. B does Y.

"A reads STOIP with one extra stroke" against "B changes the final P into an R" is one property, the
lettering, tested on both responses. That parallel is what makes the evidence discriminating rather
than descriptive. When you write into both boxes, keep the property the same across them.

### Stating the verdict

Do not open with a bare preference preamble. **You may close with the verdict once evidence has been
named.** The exemplars do this constantly:

- "this is why B is preferred"
- "A is the less severe failure"
- "so A wins despite B's smoother lighting"

The banned move is "I slightly prefer Response A because it follows the prompt better," where the
verdict arrives with nothing behind it. Evidence first, conclusion after.

Good:

```markdown
Response A: the road text reads STOIP because of an extra center stroke.
```

```markdown
Response B: the final letter has a diagonal leg and reads STOR.
```

```markdown
Response A is blank, while B renders the requested street scene; this is why B is preferred.
```

```markdown
Both responses omit the requested third frame; each shows only two.
```

```markdown
A performs the requested closer camera move; B keeps the old framing. The camera change is the central requirement, so A wins despite B's smoother lighting.
```

Bad, and why:

- "I slightly prefer Response A because it follows the prompt better and has better visual quality." Repeats the recorded preference and names no visible evidence.
- "Response A: looks good. Response B: also looks good." Both boxes filled, neither says what is visible.
- "A is slightly better overall." States the strength, omits the deciding detail.
- "A looks nicer and has better quality." No visible property another reviewer could inspect.
- "Both responses have bad text." Names a shared category, not the degree difference.
- "They look similar and both follow the prompt." Similarity alone does not justify a tie.
- "A follows the prompt, but B looks better, so either one is fine." Lists tradeoffs without deciding.

Do not restate the button you clicked. The box is for what you saw.

**Self-check on voice:** read the box back and ask whether it could be pasted onto a different pair. If
it could, it names nothing. Then ask whether it sounds like a person pointing at a screen or a rubric
being recited. If it is the second one, cut the category words and name the object.

## Hard Gates

- Do not rate before inspecting both responses.
- Do not submit a comment that would fit any other item. If it could be pasted onto a different pair, it is not evidence.
- Do not pad the second box to fill it.
- Do not skip because a secondary detail is unfamiliar.
- Do not skip a blank output that loaded.
- Do not treat a failure to load as model output.
- Do not let a secondary quality difference outrank the central requirement.
- Do not use Tie for a close call you can actually decide.
- Do not submit when the comment and the rating disagree.
- Do not write in rubric voice. Name the object, not the axis.
- Do not open a box with a preference preamble. Evidence first, verdict after.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Central requirement:** <the one thing the prompt is really asking for>

**Response A:** <what it does against that requirement>
**Response B:** <what it does against that requirement>

**Overall Preference:** <Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B>

**Response A box:**
<evidence, or "leave empty" with the reason>

**Response B box:**
<evidence, or "leave empty" with the reason>
```

State the character count of each box you fill so the user can see the floor is cleared.

## Final Checklist

- [ ] Prompt read and central requirement named before inspecting the images.
- [ ] Both responses inspected before the rating was chosen.
- [ ] Skip rules checked. Blank-that-loaded rated, failure-to-load skipped.
- [ ] Rating matches the scale. Strongly only when one side misses the central requirement or has a major defect.
- [ ] Tie used only when no relevant detail favors either side.
- [ ] Every box that is open contains located, discriminating, accurate evidence of at least 50 characters.
- [ ] No box padded with filler. An empty second box is a valid answer.
- [ ] No generic phrase left standing without the visible fact behind it.
- [ ] Comment and rating point at the same decision.
- [ ] Boxes read like a person pointing at the screen. No rubric voice, no AI power words, no absolutes.
- [ ] Where both boxes are used, the same property is named on both sides.
- [ ] Answer given in the chat. No workspace file was modified.
