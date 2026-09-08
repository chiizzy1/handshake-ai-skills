# T2I Point + Write Rubric

Operative rubric for the Handshake T2I Image Comparison task with the **Point + write** explanation
(markers clicked onto the evidence, each carrying its own reason).
Source: `HANDSHAKE-AI/t2i/vs-1788333815-comment-point-write.md`.

Fourth variant of a family of four. The rating scale, evidence tests, and boundary cases are identical
across all of them. The interaction, the character floor, and one Skip condition differ.

| Interaction | Skill | Floor |
|---|---|---|
| Two evidence boxes | `handshake-t2i-dual-boxes` | 50 total across A and B |
| One box plus a justification checker | `handshake-t2i-live-feedback` | 50 minimum |
| Dictate, transcribe, translate, confirm | `handshake-t2i-muse-dictation` | none |
| Markers on the evidence | this task | 50 total across all markers |

## Contents

- [What The Task Measures](#what-the-task-measures)
- [The Interface](#the-interface)
- [The Point + Write Interaction](#the-point--write-interaction)
- [The Skip Condition Unique To This Arm](#the-skip-condition-unique-to-this-arm)
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

### The character floor

**At least 50 characters total across all marker explanations.** The guideline frames it as a
constraint on content, not a target: "use the 50-character minimum for specific evidence, not filler."

If one marker's honest explanation clears 50 on its own, that is a complete answer. **One strong marker
is enough.** Do not place a second marker to reach a count.

## The Point + Write Interaction

1. **Choose the rating.**
2. **Click the most important evidence in either response.** Markers may sit on either side.
3. **Write a concrete reason for that marker**: what is visible at that location and why it matters.
4. **Add further markers only as the evidence requires.** No fixed pin limit, and **one strong marker is enough.**
5. **Explanations across all markers must total at least 50 characters.**
6. **Remove any marker you cannot explain.**

### The marker and the sentence must agree

✅ Marker on Response A's road text: "The painted word reads STOIP; the thin extra stroke between O and P creates the error."
*The marker locates the evidence and the text names the exact visible defect.*

❌ Marker on the sky: "Response A looks better overall."
*The marker is unrelated to the claim, and the sentence only repeats the preference.*

The bad example fails twice over, and the two failures reinforce each other: a marker pointing at
nothing relevant, and a sentence that is a verdict rather than an observation. **The location and the
words have to be about the same thing.**

### An unexplained marker is worse than no marker

The Think First case: two explained markers and a third you cannot explain.

> **Remove the third marker.** Keep it only if you can add a specific explanation before submitting.

An unexplained marker asserts that something at that spot mattered without saying what. A reviewer
cannot check it, and the guideline is explicit: "Remove unnecessary markers instead of leaving them
unexplained."

### Text-only responses

When the response is text rather than an image, **select the whole response** and **quote or paraphrase
the decisive word, phrase, or sentence.**

✅ Whole Response A: "the phrase *renewable energy credit* is the requested term; B says only *certificate*."
❌ Whole Response A: "it is more accurate."

Selecting the whole response is a deliberately coarse marker, so **the quote does the locating work.**
Naming the exact wording is what turns the selection into evidence.

### Keyboard placement

Focus the image and press **Enter** or **Space** to place a **center** marker. If the center does not
land on the evidence, **name its precise location in the explanation**. The written location
compensates for the aim you could not take.

## The Skip Condition Unique To This Arm

**"If the marker control itself is unavailable, use Skip. Do not submit an unmarked explanation in this
arm."**

This is worth holding against the dictation sibling, where a microphone or transcription failure is
explicitly **not** a Skip condition. The difference is whether a fallback exists:

| Arm | Tool fails | Result |
|---|---|---|
| Muse dictation | Microphone or transcription error | **Not a Skip.** Retry, or declare no microphone to unlock typing |
| Point + write | Marker control unavailable | **Skip.** There is no unmarked path |

Do not carry the habit across. Check which arm you are in before deciding whether broken tooling
justifies a Skip.

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

### Complete the Point + write interaction

The road lettering is the decisive evidence.

✅ Marker on Response A road text: "The painted word reads STOIP; the thin extra stroke between O and P creates the error."
The marker locates the evidence and the text names the exact visible defect.

❌ Marker on the sky: "Response A looks better overall."
The marker is unrelated to the claim, and the sentence only repeats the preference.

### Text-only evidence

Response A uses the correct technical term; Response B uses a broader term.

✅ Whole Response A: "the phrase renewable energy credit is the requested term; B says only certificate."
For text-only content, select the whole response and quote the decisive phrase.

❌ Whole Response A: "it is more accurate."
The response is selected, but the explanation does not quote or identify the decisive wording.

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

**Think First.** You placed two explained markers and a third marker that you cannot explain.
**Remove the third marker.** Keep it only if you can add a specific explanation before submitting.

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

1. The useful explanation: **"A reads STOIP with one extra stroke, while B changes the final letter to R."**
2. A matches the requested action but has weaker lighting; B is polished but misses it. **The main requested action drives the rating, with the tradeoff named in the explanation.**
3. Neither response loads. **Skip the comparison as unjudgeable.**
4. Explained pins total 44 characters. **No: add at least 6 characters of specific evidence across the pin explanations.**
5. One response loads blank, the other loads normally. **Treat the blank output as a failure and rate normally.**

Question 4 settles the scope of the floor, which the Task Details leave implicit. **The 50 characters
are counted across all marker explanations together, not per response and not per marker**, and placing
a marker does not waive the text requirement. Both wrong answers are ways of hoping the floor does not
apply.

Read the correct wording closely: *add at least 6 characters of specific evidence*. The fix for being
short is naming something else you actually saw, never six characters of filler.

Question 2 is the central-requirement rule with the loser's due attached, and it also rules out the
tempting Skip: **responses trading strengths is a rating situation, not an unjudgeable one.**

## Common Failure Modes

1. **Restating the button.** "I slightly prefer A because it follows the prompt better." The rating is already recorded. The box is for what you saw.
2. **Generic praise.** *Looks better*, *better quality*, *higher fidelity*, with no visible fact attached.
3. **Leaving a marker unexplained.** Remove it instead. The guideline says so directly.
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
15. **Placing a marker away from the evidence.** A marker on the sky under a claim about road text.
16. **Submitting an unmarked explanation** when the marker control is broken. Skip instead.
17. **Selecting a whole text response without quoting** the decisive wording.
18. **Adding a second marker to reach 50 characters.** One strong marker is enough; add evidence, not markers.
19. **Leaving a keyboard-placed center marker unlocated** in the text when it missed the evidence.

## Checklist

- [ ] Prompt read first, central requirement named as a testable claim.
- [ ] Both responses inspected before choosing a rating.
- [ ] Skip precedence applied. Blank-that-loaded rated, failure-to-load skipped, unreadable prompt skipped.
- [ ] Rating matches the scale, with Strongly reserved for a missed central requirement or a major defect.
- [ ] Tie only when no relevant detail favors either side.
- [ ] Marker control confirmed working, or Skip.
- [ ] Every marker sits on the thing its explanation describes.
- [ ] Every marker carries its own concrete reason.
- [ ] No unexplained marker left in place.
- [ ] Text responses: whole response selected and decisive phrase quoted.
- [ ] Keyboard-placed center markers have their real location named.
- [ ] Explanations total 50+ characters on evidence, not filler.
- [ ] No generic phrase standing without its visible fact.
- [ ] Comment and rating agree.
- [ ] Delivered in the chat. No task file modified.
