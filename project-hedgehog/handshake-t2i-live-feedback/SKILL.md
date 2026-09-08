---
name: handshake-t2i-live-feedback
description: Evaluate Handshake T2I Image Comparison tasks that use the Live feedback interaction. Use when a task shows a text prompt with Response A and Response B images, an Overall Preference row reading Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B, and a single required explanation box of 50+ characters with a "Check my justification" button that returns one optional suggestion; when the task header says T2I Image Comparison 3, Improve your explanation, or Live feedback.
---

# Handshake T2I Live Feedback

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/rubric.md` in this skill folder.
2. `HANDSHAKE-AI/t2i/vs-1788333816-comment-live-feedback.md`, the full guideline with its worked examples.

**The rating is the easy half. The written evidence is the deliverable.** Every bad example in the
guideline is a defensible rating ruined by a comment that names nothing. A correct verdict with a
generic comment fails.

Concise and specific beats long and generic. The overview names the goal directly: improve your
explanation.

## Sibling Task

This is the **one-box** variant. Its twin, `handshake-t2i-dual-boxes`
(`project-hedgehog/handshake-t2i-dual-boxes/SKILL.md`), is the **two-box** variant of the same family:
identical rating scale, evidence tests, skip rules, and boundary cases.

Tell them apart by the interaction under the rating:

| Cue | Task | Skill |
|---|---|---|
| Two boxes, "What specific evidence did you notice in Response A / B?", "One box required, 50+ characters total" | T2I Image Comparison 2, Dual boxes | `handshake-t2i-dual-boxes` |
| One box plus a "Check my justification" button | T2I Image Comparison 3, Live feedback | this skill |

| A record button, a 45-second timer, and a transcript to confirm | T2I Voice input and translation | `handshake-t2i-muse-dictation` |
| Clickable markers placed on the evidence | T2I Point + write | `handshake-t2i-point-write` |

If the UI shows two evidence boxes, you are in the wrong skill.

## Task Shape

- A **Prompt** block, then **Response A** and **Response B** images side by side.
- **Overall Preference**, five buttons: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- **One required explanation box** headed "Explain the visible difference", placeholder "Name the visible difference that most affected your choice", with a `0 / 50 minimum` counter.
- A **Check my justification** button that runs a specificity check and returns one concise suggestion.
- Header badges: `Required explanation`, `Live feedback`. Corner note: "50 characters minimum. Specific evidence is still required."
- Skip is available and overrides everything. The footer reads "Skip only if the comparison cannot be judged".

**The checker button is disabled until the box reaches 50 characters.** Until then it reads "Write N
more characters to enable the check". You cannot use the checker to help you get started, which is the
point: write your own observation first.

## The Live Feedback Checker

This is the only mechanic that does not exist in the sibling task, and the guideline is emphatic about
its status.

- Write the comment first. The button checks what you wrote; it does not write it for you. It stays locked below 50 characters, so there is no way to lean on it for a first draft.
- The UI states it plainly: "The checks are advisory and never change your rating. You control when they run.
- Tap **Check my justification** when ready. It returns **one** concise suggestion.
- If you make a **meaningful revision**, you may tap it once more for one final check. Two checks total.
- **Both suggestions are optional.** The checks do not score your rating and do not infer missing intent.

**The suggestion never overrides your own observation.** The guideline's Think First card puts it
plainly: when the suggestion asks you to name a visible object but your comment already names the
misspelled road sign precisely, **keep the accurate comment**.

Take a suggestion when it points at something you genuinely left vague. Ignore it when your comment is
already specific and accurate. Never edit a true, located observation into something weaker because the
checker asked. Never invent detail to satisfy it.

## The Character Rule

At least 50 characters of specific evidence. The knowledge check is explicit that both halves are
required: **at least 50 characters, and concrete evidence named.** Length alone is not enough, and
length is not optional either.

"One evidence comment of at least 50 characters completes this interaction; do not add filler." Hitting
the count with padding fails the same way a 20-character sharp observation would.

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
it more strongly.

## Mandatory Workflow

1. **Read the prompt first.** Identify the central requirement before looking at either image.
2. **Skip check.** Run the boundary rules below. Skip overrides every rating and overrides Submit.
3. **Inspect Response A against the prompt.** Then Response B. Both, before you rate.
4. **Rank the requirements.** Which one is central? Secondary quality differences lose to it.
5. **Choose the rating** from the scale.
6. **Write the comment.** One box, 50+ characters, covering both responses on one property.
7. **Optionally run the checker.** Accept a suggestion only when it makes the comment more accurate or more specific. Keep your own wording when it is already both.
8. **Agreement check.** Do the comment and the rating point at the same decision? If they disagree, fix one before submitting.

## Skip Rules

Skip overrides every rating and Submit. Precedence: restricted or uninspectable content means Skip, a
loaded output means rate the observed result, partial success means prioritize the central requirement,
a close call means name the deciding detail.

**Skip when:**

- The prompt fails to load, or either response fails to load. Skip even if the other one loaded.
- One response fails to load and the other loads blank.
- The prompt's primary requirement cannot be understood, even when both responses render perfectly.
- A safety notice in the task interface, or task-owner guidance given before the session, says not to inspect or rate the content.

**Do not skip when:**

- A response loads and is **blank**. That is observable output. Treat it as a failure and rate it.
- A secondary label is unfamiliar but the primary requirement is clear. Rate normally and mention the partial readability.
- The subject is merely unfamiliar or difficult. Every assigned subject is in scope.

**Never submit a partial entry.** Partial entries are discarded when the next comparison loads.

## Blank Versus Not Loading

| What you see | What it is | What you do |
|---|---|---|
| Response renders an image | Model output | Rate it |
| Response loads, shows a genuinely blank image | Model output, and a visible failure | Rate it, prefer the other one, name the blankness |
| Response never loads | Tooling failure | Skip |
| One blank, one will not load | Mixed | Skip |

Never score an infrastructure failure as model output. Never invent a tooling error for output that
loaded.

## Boundary Cases

- **Both responses fail.** Name the shared failure, then say which version is less severe. Tie only if the failures are genuinely equivalent.
- **One response visibly fails the requirement.** Prefer the one that succeeds and name the observed failure as the discriminating evidence.
- **Both partly satisfy.** Rate on the requirement most central to the prompt. Name that requirement and why it outweighs the other differences.
- **Pure aesthetics.** A concrete aesthetic difference is valid. Name the property and which response has it more strongly.
- **Language barrier.** Rate normally only if you can identify the primary requirement and test both responses against it. Mention partial readability. Unreadable prompt means Skip.
- **Close call.** Choose the slight preference that matches your judgment and explain the one detail that broke the tie.

## How to Write the Comment

One box means **one sentence, or two, covering both responses.** The single-box exemplar merges the two
halves into one comparison:

> "A is closer to the requested word: it reads STOIP with one extra stroke, while B changes the final P into an R."

That is the shape to copy. Name the property, give A's version, give B's version, in one breath.

### Voice

**Persona: a careful person saying what they saw, not an evaluator filing a report.**

- **Name the thing.** The object, the word, the body part, the region. Not a category word like "composition" or "quality."
- **Short sentences. Periods.** Plain words in plain order.
- **Use "while" instead of "whereas"** when contrasting. The exemplars use "while" repeatedly.
- **Avoid absolutes.** "Perfectly rendered" becomes a factual error the moment someone zooms in.
- **Give the loser its due.** "so A wins despite B's smoother lighting."
- **No AI power words.** Delve, tapestry, meticulous, striking visual narrative, seamlessly.
- **Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "semantic," "it is evident that," "exhibits," "the aforementioned," "aligns with the prompt."

**Semicolons are allowed here.** The house style across these skills bans them, but this task's own
exemplars use them to join the A half and the B half. The task guideline outranks the baseline.

### Stating the verdict

Do not open with a bare preference preamble. **You may close with the verdict once evidence has been
named.** The exemplars do this: "this is why B is preferred", "A is the less severe failure", "so A
wins despite B's smoother lighting".

"I slightly prefer A because it follows the prompt and has better quality" is the banned shape. The
verdict arrives with nothing behind it.

### Good

```markdown
A is closer to the requested word: it reads STOIP with one extra stroke, while B changes the final P into an R.
```

```markdown
Response A is blank, while B renders the requested street scene; this is why B is preferred.
```

```markdown
A performs the requested closer camera move; B keeps the old framing. The camera change is the central requirement, so A wins despite B's smoother lighting.
```

```markdown
Both responses omit the requested third frame; each shows only two.
```

```markdown
A uses softer fill light on the face; B has a harsh side light that flattens the cheek and eye area.
```

```markdown
A adds one stray stroke to the word; B replaces the final letter and makes the word read STOR. A is the less severe failure.
```

### Bad, and why

- "I slightly prefer A because it follows the prompt and has better quality." Restates the vote, generic quality language, nothing visible.
- "A is slightly better overall." States the strength, omits the deciding detail.
- "A looks nicer and has better quality." No visible property another reviewer could inspect.
- "Both responses have bad text." Names a shared category, not the degree difference.
- "They look similar and both follow the prompt." Similarity alone does not justify a tie.
- "A follows the prompt, but B looks better, so either one is fine." Lists tradeoffs without deciding.

**Self-check:** read it back and ask whether it could be pasted onto a different pair. If it could, it
names nothing.

## Hard Gates

- Do not rate before inspecting both responses.
- Do not let the checker's suggestion override an accurate, specific comment.
- Do not tap the checker more than twice, and not a second time without a meaningful revision.
- Do not invent detail to satisfy a suggestion.
- Do not pad to reach 50 characters.
- Do not skip because a secondary detail is unfamiliar.
- Do not skip a blank output that loaded.
- Do not treat a failure to load as model output.
- Do not let a secondary quality difference outrank the central requirement.
- Do not use Tie for a close call you can actually decide.
- Do not write in rubric voice. Name the object, not the axis.
- Do not open with a preference preamble. Evidence first, verdict after.
- Do not submit when the comment and the rating disagree.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Central requirement:** <the one thing the prompt is really asking for>

**Response A:** <what it does against that requirement>
**Response B:** <what it does against that requirement>

**Overall Preference:** <Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B>

**Comment:**
<the evidence comment, one or two sentences covering both responses>
```

State the character count so the user can see the 50-character floor is cleared.

## Final Checklist

- [ ] Prompt read and central requirement named before inspecting the images.
- [ ] Both responses inspected before the rating was chosen.
- [ ] Skip rules checked. Blank-that-loaded rated, failure-to-load skipped.
- [ ] Rating matches the scale. Strongly only when one side misses the central requirement or has a major defect.
- [ ] Tie used only when no relevant detail favors either side.
- [ ] Comment is 50+ characters and names located, discriminating, accurate evidence.
- [ ] Comment covers both responses on the same property.
- [ ] No filler used to reach the character count.
- [ ] Any checker suggestion was accepted on merit, not obeyed. An accurate comment was kept as written.
- [ ] Comment reads like a person pointing at the screen. No rubric voice, no AI power words, no absolutes.
- [ ] Comment and rating point at the same decision.
- [ ] Answer given in the chat. No workspace file was modified.
