---
name: handshake-t2i-point-write
description: Evaluate Handshake T2I Image Comparison tasks that use the Point + write interaction. Use when a task shows a prompt with Response A and Response B, an Overall Preference row reading Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B, and requires clicking markers directly on the evidence with an explanation attached to each marker totalling 50+ characters; when the task says Explain with a marked detail, Point + write, place a marker, or pin explanations.
---

# Handshake T2I Point + Write

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/cheat-sheet.md` in this skill folder. The task's own cheat sheet, reproduced verbatim.
2. `references/rubric.md` in this skill folder.
3. `HANDSHAKE-AI/t2i/vs-1788333815-comment-point-write.md`, the full guideline.

**Submit evidence, not a verdict.** The rating is already recorded. Do not spend words repeating which
response won.

**A marker without an explanation is not evidence.** Every marker you place must carry its own concrete
reason, and a marker you cannot explain gets removed rather than left standing.

## Sibling Tasks

Fourth variant of the same family. Identical rating scale, evidence tests, and boundary cases. The
interaction and the character floor differ.

| Interaction cue | Task | Skill | Floor |
|---|---|---|---|
| Two evidence boxes | Dual boxes | `handshake-t2i-dual-boxes` | 50 total across A and B |
| One box plus a "Check my justification" button | Live feedback | `handshake-t2i-live-feedback` | 50 minimum |
| A record button and a 45-second timer | Voice input and translation | `handshake-t2i-muse-dictation` | none |
| Clickable markers placed on the evidence | Point + write | this skill | 50 total across all markers |

## The Skip Rule That Differs From Its Siblings

**If the marker control itself is unavailable, use Skip. Do not submit an unmarked explanation in this
arm.**

Compare with the dictation variant, where a broken microphone is explicitly *not* a Skip condition
because a fallback exists (retry, or declare no microphone). **Here there is no fallback.** The marker
is the interaction, so losing it makes the item unsubmittable.

Do not carry the "tool trouble is never a Skip" habit across from that task. Check which arm you are in.

## Task Shape

- A prompt, then **Response A** and **Response B**.
- **Overall Preference**, five buttons: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- A **Point + write** interaction: click the evidence to place a marker, then write a reason for it.
- Skip is available and overrides everything.

## The Point + Write Interaction

1. **Choose the rating.**
2. **Click the most important evidence in either response.** Markers may go on either side.
3. **Write a concrete reason for that marker**, describing exactly what is visible at that location and why it matters to the comparison.
4. **Add more markers only as the evidence requires.** There is no fixed pin limit, and **one strong marker is enough.**
5. **Check the total.** Explanations across all markers must total **at least 50 characters**.
6. **Remove any marker you cannot explain.** Do not leave one unexplained.

### The marker must sit on the thing you are describing

The guideline's worked pair makes the failure concrete:

✅ Marker on Response A's road text: "The painted word reads STOIP; the thin extra stroke between O and P creates the error."
*The marker locates the evidence and the text names the exact visible defect.*

❌ Marker on the sky: "Response A looks better overall."
*The marker is unrelated to the claim, and the sentence only repeats the preference.*

Two failures in that bad example, and they compound: the marker points at nothing relevant, and the
text is a verdict rather than an observation. **The marker and the sentence have to agree about what
the evidence is.**

### Markers you cannot explain

The Think First case: you placed two explained markers and a third you cannot explain.

**Remove the third marker.** Keep it only if you can add a specific explanation before submitting.

An unexplained marker is worse than no marker. It asserts that something at that location mattered,
without saying what, and a reviewer cannot check it.

### Text-only responses

When a response is text rather than an image, **select the whole response**, then **quote or paraphrase
the decisive word, phrase, or sentence** in the explanation.

✅ Whole Response A: "the phrase *renewable energy credit* is the requested term; B says only *certificate*."
*For text-only content, select the whole response and quote the decisive phrase.*

❌ Whole Response A: "it is more accurate."
*The response is selected, but the explanation does not quote or identify the decisive wording.*

Selecting the whole response is a coarse marker, so **the quote does the locating work instead.** Naming
the exact words is what makes it evidence.

### Keyboard placement

Focus the image and press **Enter** or **Space** to place a **center** marker.

If the center does not land on the evidence, **name its precise location in the explanation**: "the
lower left corner of the sign", "the subject's right hand". The written location compensates for the
marker you could not aim.

## The Scale

| What you found | Your rating |
|---|---|
| One response satisfies the central requirement, the other misses it or has a major defect | Strongly prefer that one |
| Both satisfy the central requirement, one is marginally better | Slightly prefer that one |
| Mixed strengths producing a small overall edge | Slightly prefer that one |
| You cannot name a relevant detail favoring either side | Tie |
| Both share the same defect at the same severity | Tie |

## Evidence Test

1. **Locate it.** Name or select an object, word, body part, region, count, framing choice, or other visible detail.
2. **Discriminate.** Explain how A and B differ, or why a shared defect makes them a tie.
3. **Stay accurate.** Describe only what is visible. Never invent a reason to complete the task.

Generic phrases such as *looks better*, *better quality*, or *follows the prompt* are not enough on
their own. Add the visible fact that makes the phrase true.

A concrete aesthetic difference is valid evidence. Name the property and say which response exhibits it
more strongly.

**Use the 50-character minimum for specific evidence, not filler.**

**The 50 characters are counted across all marker explanations together**, not per response and not per
marker. Placing a marker does not waive the text requirement. If you are a few characters short, name
something else you actually saw rather than padding what is there.

## Mandatory Workflow

1. **Read the prompt.** Identify the central requirement before looking at either response.
2. **Skip check**, including whether the marker control is working.
3. **Inspect Response A, then Response B.** Both, before you rate.
4. **Rank the requirements.** Which is central?
5. **Choose the rating.**
6. **Place a marker on the single most important piece of evidence.**
7. **Write its explanation**: what is visible there, and why it changes the comparison.
8. **Add further markers only if the evidence genuinely needs them**, each with its own reason.
9. **Remove any marker you did not explain.**
10. **Check the explanations total 50+ characters** on content, not padding.
11. **Agreement check.** Do the markers, the explanations and the rating point at the same decision?

## Skip Rules

Skip overrides every rating and Submit. Precedence: restricted or uninspectable content means Skip, a
loaded output means rate the observed result, partial success means prioritize the central requirement,
a close call means name the deciding detail.

**Skip when:**

- **The marker control is unavailable.** Unique to this arm. Never submit an unmarked explanation here.
- The prompt fails to load, or either response fails to load. Skip even if the other one loaded.
- One response fails to load and the other loads blank.
- The prompt's primary requirement cannot be understood, even when both responses render.
- A safety notice in the task interface, or task-owner guidance before the session, says not to inspect or rate the content.

**Do not skip when:**

- A response loads and is **blank**. That is observable output. Rate it as a failure.
- A secondary label is unfamiliar but the primary requirement is clear. Rate normally and mention the partial readability.
- The subject is merely unfamiliar or difficult.
- The comparison is close or hard.

**Never submit a partial entry.** Partial entries are discarded when the next comparison loads.

## Blank Versus Not Loading

| What you see | What it is | What you do |
|---|---|---|
| Response renders | Model output | Rate it |
| Loads, genuinely blank | Model output, a visible failure | Rate it, mark it, name the blankness |
| Never loads | Tooling failure | Skip |
| One blank, one will not load | Mixed | Skip |

## Boundary Cases

- **Both responses fail.** Name the shared failure, then say which is less severe. Tie only if genuinely equivalent.
- **One response visibly fails.** Prefer the one that succeeds and name the observed failure.
- **Both partly satisfy.** Rate on the requirement most central to the prompt.
- **Pure aesthetics.** Name the property and which response has it more strongly.
- **Language barrier.** Rate normally only if you can identify the primary requirement and test both responses against it. Mention partial readability. Unreadable prompt means Skip.
- **Close call.** Choose the slight preference and explain the one detail that broke the tie.

## How to Write the Explanation

Describe exactly what is visible **at that location** and why it matters to the comparison.

### Voice

**Persona: a careful person pointing at the screen, not an evaluator filing a report.**

- **Name the thing under the marker.** The painted word, the left eye, the third frame, the phrase.
- **Short sentences.** Plain words in plain order.
- **Use "while" instead of "whereas"** when contrasting.
- **Avoid absolutes.**
- **No AI power words.** Delve, meticulous, seamlessly, striking visual narrative.
- **Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "it is evident that," "exhibits," "the aforementioned."
- **Do not narrate your process.** Say what you saw, not what you checked.
- **Semicolons are fine here.** The task's exemplars use them.

### Good

```markdown
The painted word reads STOIP; the thin extra stroke between O and P creates the error.
```

```markdown
A reads STOIP with one extra stroke; B changes the final P into an R.
```

```markdown
Both responses omit the requested third frame; each shows only two.
```

```markdown
A is slightly preferred because the left eye remains sharp; B blurs the iris into the eyelid.
```

```markdown
The phrase renewable energy credit is the requested term; B says only certificate.
```

### Bad, and why

- Marker on the sky, "Response A looks better overall." The marker is unrelated and the sentence is a verdict.
- "Whole Response A: it is more accurate." The response is selected but no wording is quoted.
- "I slightly prefer Response A because it follows the prompt better." Restates the vote, names nothing.
- "A is slightly better overall." States the strength, omits the deciding detail.
- "Both responses have bad text." Names a shared category, not the degree difference.
- An unexplained marker. Remove it.

## Hard Gates

- Do not rate before inspecting both responses.
- **Do not leave a marker unexplained.** Remove it instead.
- **Do not place a marker away from the thing you are describing.**
- **Do not submit an unmarked explanation.** If the marker control is broken, Skip.
- Do not select a whole text response without quoting the decisive wording.
- Do not pad to reach 50 characters. Add evidence, not adjectives.
- Do not spend words repeating which response won.
- Do not skip a blank output that loaded.
- Do not treat a failure to load as model output.
- Do not use Tie for a close call you can actually decide.
- Do not submit when the markers and the rating disagree.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Central requirement:** <the one thing the prompt is really asking for>

**Response A:** <what it does against that requirement>
**Response B:** <what it does against that requirement>

**Overall Preference:** <Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B>

**Marker 1** — on <response and exact location>:
<explanation>

**Marker 2** (only if the evidence needs it) — on <response and exact location>:
<explanation>
```

State the combined character count so the user can see the 50-character floor is cleared.

## Final Checklist

- [ ] Prompt read and central requirement named before inspecting the responses.
- [ ] Both responses inspected before the rating was chosen.
- [ ] Marker control confirmed working. If not, Skip rather than submit unmarked.
- [ ] Skip rules checked. Blank-that-loaded rated, failure-to-load skipped.
- [ ] Every marker sits on the thing its explanation describes.
- [ ] Every marker has its own concrete reason.
- [ ] No unexplained marker left in place.
- [ ] Text responses: whole response selected and the decisive phrase quoted.
- [ ] Keyboard-placed center markers have their real location named in the text.
- [ ] Explanations total 50+ characters on evidence, not filler.
- [ ] Markers, explanations and rating point at the same decision.
- [ ] Answer given in the chat. No workspace file was modified.
