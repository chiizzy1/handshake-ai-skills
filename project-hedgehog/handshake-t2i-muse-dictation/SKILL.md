---
name: handshake-t2i-muse-dictation
description: Evaluate Handshake T2I Image Comparison tasks that use the Voice input and translation (Muse dictation) interaction. Use when a task shows a text prompt with Response A and Response B images, an Overall Preference row reading Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B, and requires recording a spoken explanation that Muse transcribes and translates into English for review before submitting; when the task says Dictate and confirm your explanation, Voice input and translation, Start voice input, or muse dictation.
---

# Handshake T2I Muse Dictation

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/cheat-sheet.md` in this skill folder. The task's own cheat sheet, reproduced verbatim.
2. `references/rubric.md` in this skill folder.
3. `HANDSHAKE-AI/t2i/vs-1788333814-comment-muse-dictation.md`, the full guideline.

**The rating is the easy half. The written evidence is the deliverable.**

**The reviewed English text is the comment. Only that text is scored.** Not what you said, not what the
transcriber heard. What you approve.

## This Is Not An Audio Task

**Nothing audio is being evaluated.** The responses are images, the question is which image better
satisfies the prompt, and no sound is part of the comparison.

Voice is only the **input method for the comment**. Speaking it instead of typing it changes nothing
about what you judge or how you judge it. Do not route audio, speech, or music evaluation work here.

What the voice step does change is the accuracy risk on the way out, which is what the rest of this
skill is about.

## Sibling Tasks

Third variant of the same family. Identical rating scale, evidence tests, skip rules, and boundary
cases. Only the interaction differs.

| Interaction cue | Task | Skill |
|---|---|---|
| Two evidence boxes, "50+ characters total across A and B" | Dual boxes | `handshake-t2i-dual-boxes` |
| One box plus a "Check my justification" button | Live feedback | `handshake-t2i-live-feedback` |
| A record button, a 45-second timer, a transcript to confirm | Voice input and translation | this skill |

**Character floors differ across the three.** Dual boxes wants 50 total, live feedback wants 50 minimum,
and **this one has no minimum at all**: "there is no minimum character target beyond providing the
required response." Do not import a floor that does not exist here.

## Task Shape

- A prompt, then **Response A** and **Response B** images.
- **Overall Preference**, five buttons: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- A **Voice input and translation** interaction: record, transcribe, translate, review, submit.
- Skip is available and overrides everything.

## The Voice Interaction

The order is fixed and the UI enforces it.

1. **Choose your rating first.**
2. **Record a short spoken explanation** of the visible evidence. **You may speak in your native language.** Voice input is required by default. **Recording stops after 45 seconds.**
3. **Muse transcribes the recording and automatically translates it into English.**
4. **The explanation field opens only after a transcript is ready.** You cannot type your way past this step.
5. **Review the confirmed English text.** Correct object names, letters, counts, and translation errors.
6. **Submit.** The reviewed English text is what gets scored.

### The transcript is a draft, never the answer

This is the failure this task is built around. **Speech-to-text normalises exactly the evidence you are
reporting.** You say a sign reads "STOIP" and the transcript writes "stop". You say "STOR" and it writes
"store". The transcriber helpfully corrects the misspelling that *was the whole point of your
observation*.

The guideline's Think First case: the transcript says the sign reads STORE, but you said and observed
STOR. **Correct the confirmed text to STOR before submitting.** The reviewed text, not the raw
transcript, is the final comment.

**Always re-read the transcript against the image before submitting**, with particular attention to:

- **Letters and misspellings.** The defect you are describing is the thing most likely to be auto-corrected away.
- **Object names.** "Iris" becoming "irises", "palm rest" becoming "palm rest" or something else entirely.
- **Counts.** "Two frames" and "three frames" sound similar and change the claim.
- **Translation errors**, when you dictated in another language. A translated object name may not match what the image shows.

Quoting a garbled string out loud is the hardest thing for a transcriber to get right, so if your
evidence is a misspelling, **expect to fix it by hand every time.**

### The microphone rules

- **Voice input is required by default.** If a microphone is detected, **typing is not available.**
- **"I don't have a microphone" appears only when the browser confirms there is no audio-input device.** Some browsers can only confirm this after you press **Start voice input**. Selecting the option unlocks the typing fallback.
- **A permission error or a transcription error does not unlock typing.** Allow access, or retry voice input.
- **If recording cuts off**, record again, or complete the reviewed transcript once transcription succeeds. **The confirmed-text field is editable once a transcript exists**, so typing the missing detail into it is the intended fix for a truncated recording, not a workaround. What you cannot do is type before any transcript exists, unless the browser confirmed there is no microphone.
- **Never submit a truncated transcript**, and never abandon the rating over a cut-off recording. The interface lets you finish it.

### Privacy

**Audio is sent to the transcription service.** Do not assume a retention policy that the service has
not stated. Say what you saw in the images, and nothing else.

## The Scale

| What you found | Your rating |
|---|---|
| One response satisfies the central requirement, the other misses it or has a major defect | Strongly prefer that one |
| Both satisfy the central requirement, one is marginally better | Slightly prefer that one |
| Mixed strengths producing a small overall edge | Slightly prefer that one |
| You cannot name a relevant detail favoring either side | Tie |
| Both share the same defect at the same severity | Tie |

Tie is not for "close". Tie is for "no nameable relevant difference".

## Evidence Test

Every claim must pass all three:

1. **Locate it.** Name or select an object, word, body part, region, count, framing choice, or other visible detail.
2. **Discriminate.** Explain how A and B differ, or why a shared defect makes them a tie.
3. **Stay accurate.** Describe only what is visible. Never invent a reason to complete the task.

Generic phrases such as *looks better*, *better quality*, or *follows the prompt* are not enough by
themselves. Add the visible fact that makes the phrase true.

A concrete aesthetic difference is valid evidence. Name the property and say which response exhibits it
more strongly.

**There is no minimum character target.** Be concise. Say the evidence and stop.

## Mandatory Workflow

1. **Read the prompt.** Identify the central requirement before looking at either image.
2. **Skip check.** Skip overrides every rating and overrides Submit.
3. **Inspect Response A, then Response B.** Both, before you rate.
4. **Rank the requirements.** Which is central? Secondary quality differences lose to it.
5. **Choose the rating.**
6. **Plan the sentence before you press record.** You have 45 seconds and the field will not open until a transcript exists. Know the object, the difference, and the two sides you are naming.
7. **Record.**
8. **Review the confirmed English text against the images.** Fix letters, object names, counts, and translation errors.
9. **Agreement check.** Do the comment and the rating point at the same decision?
10. **Submit.**

## Skip Rules

Skip overrides every rating and Submit. Precedence: restricted or uninspectable content means Skip, a
loaded output means rate the observed result, partial success means prioritize the central requirement,
a close call means name the deciding detail.

**Skip when:**

- The prompt fails to load, or either response fails to load. Skip even if the other one loaded.
- One response fails to load and the other loads blank.
- The prompt's primary requirement cannot be understood, even when both responses render.
- A safety notice in the task interface, or task-owner guidance before the session, says not to inspect or rate the content.

**Do not skip when:**

- A response loads and is **blank**. That is observable output. Rate it as a failure.
- A secondary label is unfamiliar but the primary requirement is clear. Rate normally and mention the partial readability.
- The subject is merely unfamiliar or difficult.
- **A microphone or transcription problem occurs.** That is a recording issue, not a Skip condition. Retry, or declare no microphone.

**Never submit a partial entry.** Partial entries are discarded when the next comparison loads.

## Blank Versus Not Loading

| What you see | What it is | What you do |
|---|---|---|
| Response renders an image | Model output | Rate it |
| Response loads, shows a genuinely blank image | Model output, and a visible failure | Rate it, prefer the other one, name the blankness |
| Response never loads | Tooling failure | Skip |
| One blank, one will not load | Mixed | Skip |

## Boundary Cases

- **Both responses fail.** Name the shared failure, then say which is less severe. Tie only if genuinely equivalent.
- **One response visibly fails.** Prefer the one that succeeds and name the observed failure.
- **Both partly satisfy.** Rate on the requirement most central to the prompt.
- **Pure aesthetics.** A concrete aesthetic difference is valid. Name the property and which response has it more strongly.
- **Language barrier.** Rate normally only if you can identify the primary requirement and test both responses against it. Mention partial readability. Unreadable prompt means Skip.
- **Close call.** Choose the slight preference and explain the one detail that broke the tie.
- **Recording cut off.** Record again, or complete the reviewed transcript after transcription succeeds.

## How to Write the Comment

One or two sentences covering both responses on one property. No minimum length.

### Voice

**Persona: a careful person saying what they saw, not an evaluator filing a report.**

- **Name the thing.** The object, the word, the body part, the region. Not a category word.
- **Short sentences.** Plain words in plain order.
- **Use "while" instead of "whereas"** when contrasting.
- **Avoid absolutes.** "Perfectly rendered" becomes wrong the moment someone zooms in.
- **Give the loser its due.** "so A wins despite B's smoother lighting."
- **No AI power words.** Delve, meticulous, seamlessly, striking visual narrative.
- **Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "it is evident that," "exhibits," "the aforementioned."
- **Do not narrate your process.** Say what you saw, not what you checked.

**Semicolons are fine here.** The house style bans them, but this task's exemplars use them: "A reads
STOIP with one extra stroke; B changes the final P into an R."

### Dictating well

Because the field opens only after a transcript exists, the sentence has to survive being spoken.

- **Say the letters slowly and separately** when quoting a misspelling: "S, T, O, I, P."
- **Speak the sentence you intend to submit**, not a rambling description you will rewrite.
- **One property, both sides.** The same shape as every exemplar.
- Then fix the transcript. **Assume it changed something.**

### Submit evidence, not a verdict

The cheat sheet's own heading, and it goes further than the sibling tasks: **"Do not spend words
repeating which response won."** The rating is already recorded, so the comment is for what you saw.

A verdict clause is still allowed when it is doing work at the end of named evidence, as in the
exemplars: "this is why B is preferred", "A is the less severe failure", "so A wins despite B's smoother
lighting". What is banned is spending the comment on the verdict, and opening with a preference
preamble.

### Good

```markdown
A reads STOIP because of an extra center stroke; B reads STOR because the last letter has a diagonal leg.
```

```markdown
Response A is blank, while B renders the requested street scene; this is why B is preferred.
```

```markdown
Both responses omit the requested third frame; each shows only two.
```

```markdown
A adds one stray stroke to the word; B replaces the final letter and makes the word read STOR. A is the less severe failure.
```

```markdown
A uses softer fill light on the face; B has a harsh side light that flattens the cheek and eye area.
```

### Bad, and why

- "A reads stop and B reads store, both are fine." **An unreviewed transcript.** It has silently corrected both misspellings, which were the evidence.
- "I slightly prefer Response A because it follows the prompt better and has better visual quality." Restates the vote, names nothing.
- "A is slightly better overall." States the strength, omits the deciding detail.
- "A looks nicer and has better quality." No visible property another reviewer could inspect.
- "Both responses have bad text." Names a shared category, not the degree difference.
- "They look similar and both follow the prompt." Similarity alone does not justify a tie.

## Hard Gates

- Do not rate before inspecting both responses.
- **Do not submit a raw transcript.** Read it against the image first.
- **Do not let the transcriber's spelling stand when the spelling is the evidence.**
- Do not treat a microphone or transcription failure as a Skip condition.
- Do not type before a transcript exists unless the browser confirmed there is no microphone.
- Do not pad. There is no minimum here.
- Do not spend words repeating which response won.
- Do not skip a blank output that loaded.
- Do not treat a failure to load as model output.
- Do not let a secondary quality difference outrank the central requirement.
- Do not use Tie for a close call you can actually decide.
- Do not submit when the comment and the rating disagree.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Central requirement:** <the one thing the prompt is really asking for>

**Response A:** <what it does against that requirement>
**Response B:** <what it does against that requirement>

**Overall Preference:** <Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B>

**Say this** (then correct the transcript against it):
<the sentence to dictate>

**Watch the transcript for:** <the letters, names or counts most likely to be auto-corrected>
```

## Final Checklist

- [ ] Prompt read and central requirement named before inspecting the images.
- [ ] Both responses inspected before the rating was chosen.
- [ ] Skip rules checked. Blank-that-loaded rated, failure-to-load skipped, microphone trouble not skipped.
- [ ] Rating chosen before recording.
- [ ] Sentence planned before pressing record, and it fits in 45 seconds.
- [ ] **Confirmed English text read back against the images.**
- [ ] **Letters, object names, counts and translation errors corrected by hand.**
- [ ] Any quoted misspelling still spelled the way the image spells it.
- [ ] Comment names located, discriminating, accurate evidence. No padding.
- [ ] Comment and rating point at the same decision.
- [ ] Answer given in the chat. No workspace file was modified.
