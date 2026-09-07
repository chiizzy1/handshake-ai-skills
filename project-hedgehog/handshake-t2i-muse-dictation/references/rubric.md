# T2I Muse Dictation Rubric

Operative rubric for the Handshake T2I Image Comparison task with the **Voice input and translation**
(Muse dictation) explanation.
Source: `HANDSHAKE-AI/t2i/vs-1788333814-comment-muse-dictation.md`.

Third variant of a family of three. `handshake-t2i-dual-boxes` uses two evidence boxes,
`handshake-t2i-live-feedback` uses one box plus a justification checker, and this one requires a spoken
explanation that Muse transcribes and translates. The rating scale, evidence tests, skip rules, and
boundary cases are identical across all three. Only the interaction differs.

**The character floor differs, though.** Dual boxes wants 50 characters total, live feedback wants 50
minimum, and this task has **no minimum at all**: "there is no minimum character target beyond
providing the required response." Do not import a floor that does not exist here.

## Contents

- [What The Task Measures](#what-the-task-measures)
- [The Interface](#the-interface)
- [Not An Audio Task](#not-an-audio-task)
- [The Voice Interaction](#the-voice-interaction)
- [The Rating Scale](#the-rating-scale)
- [Submit Evidence, Not A Verdict](#submit-evidence-not-a-verdict)
- [Evidence](#evidence)
- [Skip](#skip)
- [Worked Examples](#worked-examples)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Voice](#voice)
- [Final Assessment Answers](#final-assessment-answers)
- [Common Failure Modes](#common-failure-modes)
- [Checklist](#checklist)

## What The Task Measures

Two things at once, and the second is where items are lost.

1. **Which response better satisfies the prompt.** Overall preference on a five-point scale.
2. **Whether you can prove it from what is visible.** A required explanation naming traceable evidence.

The guideline's framing: "Concise and specific is better than long and generic." Every one of its ten
bad examples is a plausible rating attached to a comment that names nothing. The rating alone is not
the deliverable.

Prompt adherence outranks polish. A more attractive image that misses the central requirement loses to
a rougher one that hits it.

## The Interface

- Overview heading: **Dictate and confirm your explanation**.
- A prompt, then **Response A** and **Response B** images.
- **Overall Preference** row: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- A **Voice input and translation** interaction below the rating.
- Guidelines nav: Overview, Task Details, Good and Bad Examples, Workflow Check, QA Rubric, Final Assessment. The Workflow Check page currently reads "No walkthrough video uploaded yet."

### No character floor

"Be concise: **there is no minimum character target** beyond providing the required response."

This is the one place the three sibling tasks genuinely disagree, and the looser rule here is easy to
get wrong in both directions. There is nothing to pad toward, and nothing to trim under.

## Not An Audio Task

The responses are images and the comparison is visual. **No audio is evaluated.** Voice is the input
method for the required explanation, nothing more; the task is identical to its siblings with a
microphone in place of a keyboard.

What it changes is the fidelity of the comment between your eye and the submitted text, which is the
subject of the next section.

## The Voice Interaction

Six steps, in a fixed order the UI enforces.

1. **Choose your rating.**
2. **Record a short explanation** of the visible evidence. **You may speak in your native language.** Voice input is required by default. **Recording stops after 45 seconds.**
3. **Muse transcribes the recording and automatically translates it into English.**
4. **The explanation field opens only after a transcript is ready.**
5. **Review the confirmed English text.** Correct object names, letters, counts, and translation errors.
6. **Submit.** "This task submits the reviewed English text as the comment. **Only that text is scored.**"

### The transcript normalises your evidence

The failure this whole variant is built around.

Speech-to-text corrects misspellings. That is usually helpful and here it is catastrophic, because **the
misspelling is frequently the evidence**. You observe a sign reading STOIP and say so; the transcript
writes "stop". You observe STOR; the transcript writes "store". The transcriber has quietly repaired the
exact defect you were reporting, and the resulting comment describes two images that do not exist.

The guideline's Think First case:

> The transcript says the sign reads STORE, but you clearly said and observed STOR. What should you
> submit?
>
> **Correct the confirmed text to STOR before submitting.** The reviewed text, not the raw transcript,
> is the final comment.

And its worked example:

✅ Confirmed text: "A reads STOIP because of an extra center stroke; B reads STOR because the last letter has a diagonal leg."
*The annotator corrected the transcript and preserved exact visual evidence.*

❌ Unreviewed transcript: "A reads stop and B reads store, both are fine."
*The unreviewed text changes the observed lettering and would submit inaccurate evidence.*

Note how much the bad version destroys: both misspellings are gone, and "both are fine" reverses the
finding entirely.

### What to check every time

| Category | What goes wrong |
|---|---|
| **Letters and misspellings** | Auto-corrected to the real word. The defect disappears. |
| **Object names** | A near-homophone substituted, or a translated name that does not match the image. |
| **Counts** | "Two" and "three" mishear easily, and the claim changes with them. |
| **Translation** | You dictated in another language; the English may not name what the image shows. |

Quoting a garbled string aloud is the hardest input a transcriber can get. **If your evidence is a
misspelling, expect to fix it by hand every time.**

### Dictating well

The field does not open until a transcript exists, so the sentence has to survive being spoken.

- **Spell quoted misspellings out letter by letter**: "S, T, O, I, P."
- **Say the sentence you intend to submit**, not a rambling description you plan to rewrite.
- **One property, both sides**, the same shape as every exemplar.
- Then read it back against the image and **assume something changed.**

### Microphone and fallback rules

- **Voice input is required by default.** If a microphone is detected, **typing is not available.**
- **"I don't have a microphone" appears only when the browser confirms there is no audio-input device.** Some browsers confirm only after you press **Start voice input**. Selecting it unlocks the typing fallback.
- **A permission error or a transcription error does not unlock typing.** Allow access, or retry voice input.
- **If recording cuts off**, record again, or complete the reviewed transcript once transcription succeeds.
- **None of these is a Skip condition.** A recording problem is a recording problem.

### Privacy

**Audio is sent to the transcription service.** The guideline is explicit: "Do not assume a retention
policy that is not stated by that service." Describe the images and nothing else.

## The Rating Scale## The Rating Scale

| What you found | Your rating |
|---|---|
| One response satisfies the central requirement, the other misses it or carries a major defect | Strongly prefer that one |
| Both satisfy the central requirement, one is marginally better | Slightly prefer that one |
| The responses trade strengths and one has a small overall edge | Slightly prefer that one |
| No relevant detail favors either response | Tie |
| Both share the same defect at the same severity | Tie |

**Tie is not the close-call button.** A close call is a slight preference plus the one detail that broke
it. Tie is for when you genuinely cannot name a relevant difference, including two responses that fail
identically.

## Submit Evidence, Not A Verdict

The cheat sheet leads with this, and it is stated more strongly here than in the sibling tasks:

> Your explanation is required, but there is no character target. Name something visible and state how
> it affected the comparison. **Do not spend words repeating which response won.**

The rating is already recorded. With no character floor to reach, there is nothing to gain from a
preamble and nothing to pad toward. Name the thing, say how it affected the comparison, stop.

A verdict clause at the *end* of named evidence still earns its place ("A is the less severe failure").
A comment that is mostly verdict does not.

## Evidence

Three tests, all required:

1. **Locate it.** Name or select an object, word, body part, region, count, framing choice, or other visible detail.
2. **Discriminate.** Explain how A and B differ, or why a shared defect makes them a tie.
3. **Stay accurate.** Describe only what is visible. Do not invent a reason to complete the task.

Generic phrases (*looks better*, *better quality*, *follows the prompt*) are not evidence on their own.
They are allowed only when the visible fact that makes them true is attached.

**Aesthetic evidence counts** when it is concrete and comparable. Name the property and which response
exhibits it more strongly. Softer fill light against harsh side light is aesthetic and specific.
"Looks nicer" is aesthetic and useless.

### The comment

One or two sentences covering both responses on one property. No minimum length, so say the evidence and
stop.

The comment that is scored is **the reviewed English text**, not the audio and not the raw transcript.

## Skip

**Skip overrides every rating and overrides Submit.** If a Skip condition applies, do not submit a
rating. Never submit a partial entry; partial entries are discarded when the next comparison loads.

Precedence order: restricted or uninspectable content means Skip. A loaded output means rate the
observed result. Partial success means prioritize the central requirement. A close call means name the
deciding detail.

### Skip

- The prompt fails to load, or either response fails to load, even when the other loaded fine.
- One response fails to load and the other loads blank.
- The prompt's primary requirement cannot be understood, even when both responses render.
- A safety notice in the interface, or task-owner guidance given before the session, says not to inspect or rate the content.

### Do not skip

- A response that loads and is blank. That is observable model output. Rate it as a failure.
- An unfamiliar secondary label, when the primary requirement is clear and both responses can be tested against it. Rate normally and mention the partial readability.
- A subject that is merely unfamiliar or difficult. Every assigned subject is in scope.

### Blank versus not loading

| What you see | What it is | What you do |
|---|---|---|
| An image renders | Model output | Rate it |
| Loads, genuinely blank | Model output, visible failure | Rate it, name the blankness |
| Never loads | Tooling failure | Skip |
| One blank, one will not load | Mixed | Skip |

Never score an infrastructure failure as model output, and never invent a tooling error for output that
loaded successfully.

## Worked Examples

Ten pairs from the guideline. The good column is the standard to copy.

### Specific evidence instead of a preference preamble

Rating: Slightly prefer Response A.

✅ "A reads STOIP with one extra stroke; B changes the final P into an R."
Identifies the exact lettering in both responses and explains the comparison.

❌ "I slightly prefer Response A because it follows the prompt better and has better visual quality."
Repeats the recorded preference and uses generic claims without naming visible evidence.

### A tie still needs a reason

Rating: Tie.

✅ "Both responses omit the requested third frame; each shows only two."
The shared, countable defect explains why neither is better.

❌ "They look similar and both follow the prompt."
Similarity alone does not identify what was inspected or why the tie is justified.

### Complete the Voice input and translation interaction

The road lettering is the decisive evidence.

✅ Confirmed text: "A reads STOIP because of an extra center stroke; B reads STOR because the last letter has a diagonal leg."
The annotator corrected the transcript and preserved exact visual evidence.

❌ Unreviewed transcript: "A reads stop and B reads store, both are fine."
The unreviewed text changes the observed lettering and would submit inaccurate evidence.

### Compare severity when both responses fail

Both road signs misspell the requested word. Rating: Slightly prefer Response A.

✅ "A adds one stray stroke to the word; B replaces the final letter and makes the word read STOR. A is the less severe failure."
Names the shared failure and the concrete degree difference supporting the slight preference.

❌ "Both responses have bad text."
Names a shared category but does not explain why A is less severe.

### One response fails

Response A loads as a genuinely blank image. Response B contains the requested scene.

✅ "Response A is blank, while B renders the requested street scene; this is why B is preferred."
A loaded blank output is a visible failure. The comment names it and contrasts it.

❌ "Tie; A might still be loading."
Do not invent a tooling error when the blank output loaded successfully. Rate the visible result.

### Prioritize the central requirement

A performs the requested camera move with rough lighting. B has polished lighting but keeps the
original framing.

✅ "A performs the requested closer camera move; B keeps the old framing. The camera change is the central requirement, so A wins despite B's smoother lighting."
Identifies the main requirement and explains why it outweighs a secondary quality difference.

❌ "A follows the prompt, but B looks better, so either one is fine."
Lists generic tradeoffs without deciding which prompt requirement matters most.

### A slight preference needs one deciding detail

Both responses satisfy the prompt, but A keeps the subject's face sharper.

✅ "A is slightly preferred because the left eye remains sharp; B blurs the iris into the eyelid."
Names the single marginal detail that breaks an otherwise close call.

❌ "A is slightly better overall."
The preference strength is stated, but the deciding evidence is missing.

### Concrete aesthetic evidence

Rating: Slightly prefer Response A for presentation quality.

✅ "A uses softer fill light on the face; B has a harsh side light that flattens the cheek and eye area."
The preference is subjective, but the supporting visual properties are concrete and comparable.

❌ "A looks nicer and has better quality."
Generic, and gives no visible property another reviewer could inspect.

### Partial readability can still be judgeable

You understand the prompt's primary action and can inspect both responses, but a secondary label is
unfamiliar.

✅ "A completes the requested camera move; B keeps the original framing. The secondary label is unfamiliar, but it does not prevent judging the main request."
The main requirement and both responses are judgeable, so rate normally and disclose the limitation.

❌ "Skip because one label is unfamiliar."
An unfamiliar secondary detail is not a reason to skip when the primary requirement is judgeable.

### Unreadable primary requirement means Skip

The prompt's primary requirement cannot be understood, even though both responses render.

✅ "Skip. The primary requirement is unreadable, so the responses cannot be evaluated against it."
Readable outputs do not make a comparison judgeable when the requirement itself is unknown.

❌ "Tie. Both images look equally polished."
Invents a rating without knowing the requested requirement. Use Skip instead.

## Knowledge Check Answers

Both training checks, with the reasoning the module gives.

**Workflow Check: "What is the correct order for a normal comparison?"**
Inspect both responses, choose a rating, complete the required explanation, then submit.
*Inspect both outputs before rating, then capture the evidence that caused the decision.*

The distractors: "write a generic comment, then inspect one response" and "choose a winner from the
prompt without opening the responses". Both invert the order, and in both the comment stops being
evidence of anything.

**Think First.** The transcript says the sign reads STORE, but you clearly said and observed STOR.
**Correct the confirmed text to STOR before submitting.** The reviewed text, not the raw transcript, is
the final comment.

**"Which statement best describes the comment requirement?"**
The comment must name concrete evidence; length alone does not make it useful.
*Every submitted rating needs evidence. The task evaluates content, not a character-count ritual.*

Note this matches the dual-boxes wording, with no number in the correct option. The live-feedback
variant is the odd one out there.

Assessment items and their answers:

1. One response loads successfully but is blank, the other loads normally. **Treat the blank output as a failure and rate normally.**
2. Can a concrete aesthetic difference support a preference? **Yes. Name the property and which response exhibits it more strongly.**
3. Primary requirement clear, some secondary text unfamiliar. **Rate normally and mention the partial readability.**
4. Your comment is accurate and already names the misspelled sign, but the checker suggests naming a visible object. **Keep the accurate comment.**
5. Tie because both responses omit the same requested object. **Name the missing object and state that both responses omit it.**

## Voice

The baseline persona across these skills: **a careful person saying what they saw, not an evaluator
filing a report.** Name the object rather than the axis, keep sentences short, use "while" instead of
"whereas", avoid absolutes, and give the losing response its due before saying why it lost.

Banned: "Upon review of", "demonstrates superior", "holistic", "semantic", "it is evident that",
"exhibits", "the aforementioned", "aligns with the prompt". No AI power words (delve, meticulous,
seamlessly, striking visual narrative).

### Where this task departs from the house style

**Semicolons are allowed here.** The house baseline bans them. This task's own exemplars use them to
join the A half and the B half of an observation, and the task guideline outranks the baseline:

> "A reads STOIP with one extra stroke; B changes the final P into an R."
> "A uses softer fill light on the face; B has a harsh side light that flattens the cheek and eye area."
> "Both responses omit the requested third frame; each shows only two."

A period does the same work if you prefer one. The point is that a semicolon here will not be marked
against you, because the official examples are written that way.

### The parallel pattern

Almost every good exemplar has one shape: **the same property, named on both sides.**

| Property tested | Response A | Response B |
|---|---|---|
| Road lettering | reads STOIP, extra center stroke | final letter has a diagonal leg, reads STOR |
| Face sharpness | left eye remains sharp | iris blurs into the eyelid |
| Face lighting | softer fill light | harsh side light flattening the cheek |
| Requested camera move | performs the closer move | keeps the old framing |

Descriptive writing says what one image looks like. Discriminating writing tests one property against
both. The second is what the task asks for, and the parallel construction is what makes it visible.

### Verdict placement

A bare preference preamble is the single most common failure. A verdict stated *after* evidence is
correct and appears throughout the exemplars: "this is why B is preferred", "A is the less severe
failure", "so A wins despite B's smoother lighting".

Evidence first, conclusion after. Never conclusion alone.

## Final Assessment Answers

1. Tie because both responses omit the same requested object. **Name the missing object and state that both responses omit it.**
2. Neither response loads. **Skip the comparison as unjudgeable.**
3. The browser detects a microphone. **No typing fallback: use voice input and review the transcript.**
4. The recording hits the 45-second limit before the final detail. **Type the missing detail into the confirmed-text field, review it, and submit.**
5. The useful sentence: **"Response B shows four frames; the prompt requested three."**

Question 4 settles something the Task Details only imply. **Once a transcript exists, the confirmed-text
field is editable**, so finishing a truncated recording by typing is legitimate, and so is re-recording.
The restriction is narrower than it first appears: what you cannot do is type *before any transcript
exists*, unless the browser has confirmed there is no microphone.

Submitting the truncated transcript is the wrong answer because the evidence is incomplete, and
abandoning the rating throws away work the interface lets you finish.

## Common Failure Modes

1. **Restating the button.** "I slightly prefer A because it follows the prompt better." The rating is already recorded. The box is for what you saw.
2. **Generic praise.** *Looks better*, *better quality*, *higher fidelity*, with no visible fact attached.
3. **Submitting the raw transcript.** The single most likely failure on this task. The transcript is a draft.
4. **Skipping a blank that loaded.** A blank render is model output and must be rated.
5. **Rating a response that never loaded.** That is a tooling failure and forces Skip.
6. **Skipping over an unfamiliar secondary detail** while the primary requirement is perfectly clear.
7. **Tie as an escape hatch** on a close call you could decide with one named detail.
8. **Letting polish outrank the central requirement.** Smoother lighting does not beat the requested camera move.
9. **Naming a shared failure without the degree difference.** "Both have bad text" when one is a stray stroke and the other changes the word.
10. **Comment and rating disagreeing.** Evidence pointing at B under a Slightly Prefer A rating. Fix one before submitting.
11. **Inventing evidence to finish the item.** Describe only what is visible.
12. **Writing a comment that would fit any pair.** If it could be pasted onto a different item, it is not evidence.
13. **Rubric voice.** "Demonstrates superior prompt adherence" instead of "keeps the requested red bus".
14. **Describing instead of discriminating.** A comment that describes one image without testing the property against both.
15. **Letting a normalised spelling stand.** "Stop" for STOIP, "store" for STOR. The correction erases the evidence.
16. **Skipping over a microphone or transcription problem.** That is a recording issue, not a Skip condition.
17. **Typing before a transcript exists** without the browser having confirmed there is no microphone.
18. **Dictating a rambling draft** and relying on rewriting it afterwards. Plan the sentence, then record.

## Checklist

- [ ] Prompt read first, central requirement named as a testable claim.
- [ ] Both responses inspected before choosing a rating.
- [ ] Skip precedence applied. Blank-that-loaded rated, failure-to-load skipped, unreadable prompt skipped.
- [ ] Rating matches the scale, with Strongly reserved for a missed central requirement or a major defect.
- [ ] Tie only when no relevant detail favors either side.
- [ ] Rating chosen before recording.
- [ ] Sentence planned before pressing record, and it fits inside 45 seconds.
- [ ] Confirmed English text read back against the images.
- [ ] Letters, object names, counts and translation errors corrected by hand.
- [ ] Any quoted misspelling still spelled the way the image spells it.
- [ ] Comment locates, discriminates, and stays accurate. No padding, and no floor to reach.
- [ ] No generic phrase standing without its visible fact.
- [ ] Comment and rating agree.
- [ ] Delivered in the chat. No task file modified.
