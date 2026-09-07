# T2I Live Feedback Rubric

Operative rubric for the Handshake T2I Image Comparison task with the **Live feedback** explanation
(one comment box plus a "Check my justification" button).
Source: `HANDSHAKE-AI/t2i/vs-1788333816-comment-live-feedback.md`.

Its twin is `handshake-t2i-dual-boxes`, the two-box variant. The rating scale, evidence tests, skip
rules, and boundary cases are identical between them. Only the interaction differs.

## Contents

- [What The Task Measures](#what-the-task-measures)
- [The Interface](#the-interface)
- [The Live Feedback Checker](#the-live-feedback-checker)
- [The Rating Scale](#the-rating-scale)
- [Evidence](#evidence)
- [Skip](#skip)
- [Worked Examples](#worked-examples)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Voice](#voice)
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

- Task title: **T2I Image Comparison 3**. Overview heading: **Improve your explanation**.
- **Prompt** block, then **Response A** and **Response B** images side by side.
- **Overall Preference** row: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B.
- **One required explanation box.** Headed "Explain the visible difference", placeholder "Name the visible difference that most affected your choice", counter reading `0 / 50 minimum`.
- A **Check my justification** button beneath it, **disabled until the box reaches 50 characters** ("Write N more characters to enable the check").
- Header badges: `Required explanation`, `Live feedback`. Corner note: "50 characters minimum. Specific evidence is still required."
- Section header: "Compare the two responses. Choose your preference first, then provide the evidence that decided it."
- UI text under the button: "The checks are advisory and never change your rating. You control when they run. Finish your thought, then tap the button.
- Guidelines nav: Overview, Task Details, Good and Bad Examples, Workflow Check, QA Rubric, Final Assessment. A "View Cheat Sheet" button sits at the bottom.

### The character floor

**At least 50 characters, and concrete evidence named.** The knowledge check makes both halves
explicit: "Every submitted rating needs at least 50 characters, but length alone is not enough: the
comment must name visible evidence."

"One evidence comment of at least 50 characters completes this interaction; do not add filler."
Reaching the count with padding fails exactly as a vague comment does.

## The Live Feedback Checker

The one mechanic the sibling task does not have.

- Write your comment first. The button checks what you wrote.
- Tap **Check my justification** to run an initial specificity check. It returns **one** concise suggestion.
- After a **meaningful revision** you may tap it once more for one final check. Two checks in total.
- **Both suggestions are optional.** The checks do not score your rating and do not infer missing intent.

### The suggestion never outranks your observation

The guideline's Think First card is the governing case:

> The suggestion asks you to name a visible object, but your comment already names the misspelled road
> sign precisely. What should you do?
>
> **Keep the accurate comment.** The suggestion is optional and never overrides your own observation.

Accept a suggestion when it points at something you genuinely left vague. Decline it when your comment
is already specific and accurate. Two failure directions:

1. **Obeying it.** Rewriting a precise, located observation into something weaker because the checker
   asked for a change.
2. **Inventing for it.** Adding a detail you did not actually see so the suggestion is satisfied. This
   breaks the accuracy test, which outranks the checker entirely.

The checker is a specificity assistant, not a grader and not an authority.

## The Rating Scale

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

### Using the one box

- One comment, at least 50 characters, covering both responses.
- Do not add filler. The floor is a floor, not a target.
- When both responses share a defect, the comment states how it appears across both and which is less severe.
- The comment holds visible evidence, never a restatement of the button you clicked.

The single-box exemplar merges both halves into one comparison:

> "A is closer to the requested word: it reads STOIP with one extra stroke, while B changes the final P into an R."

Name the property, give A's version, give B's version, in one breath.

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

### Complete the Live feedback interaction

The road lettering is the decisive evidence.

✅ "A is closer to the requested word: it reads STOIP with one extra stroke, while B changes the final P into an R."
Gives the checker and downstream readers exact, comparison-relevant evidence.

❌ "I slightly prefer A because it follows the prompt and has better quality."
Restates the vote and uses generic quality language without naming anything visible.

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

**Think First.** The suggestion asks you to name a visible object, but your comment already names the
misspelled road sign precisely. **Keep the accurate comment.** The suggestion is optional and never
overrides your own observation.

**"Which statement best describes the comment requirement?"**
The comment must contain at least 50 characters and name concrete evidence.
*Every submitted rating needs at least 50 characters, but length alone is not enough: the comment must name visible evidence.*

Note the wording differs from the sibling task, whose correct option omits the number. Here the count is
part of the correct answer.

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

## Common Failure Modes

1. **Restating the button.** "I slightly prefer A because it follows the prompt better." The rating is already recorded. The box is for what you saw.
2. **Generic praise.** *Looks better*, *better quality*, *higher fidelity*, with no visible fact attached.
3. **Padding to reach 50 characters.** Filler words to clear the counter. The count and the evidence are both required, and neither substitutes for the other.
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
15. **Obeying the checker.** Rewriting an accurate, specific comment because the suggestion asked for a change.
16. **Inventing detail for the checker.** Adding something you did not see so the suggestion is satisfied. Accuracy outranks the checker.

## Checklist

- [ ] Prompt read first, central requirement named as a testable claim.
- [ ] Both responses inspected before choosing a rating.
- [ ] Skip precedence applied. Blank-that-loaded rated, failure-to-load skipped, unreadable prompt skipped.
- [ ] Rating matches the scale, with Strongly reserved for a missed central requirement or a major defect.
- [ ] Tie only when no relevant detail favors either side.
- [ ] Comment locates, discriminates, and stays accurate, at 50+ characters.
- [ ] No filler used to reach the count.
- [ ] Any checker suggestion accepted on merit, not obeyed. An accurate comment kept as written.
- [ ] No generic phrase standing without its visible fact.
- [ ] Comment and rating agree.
- [ ] Delivered in the chat. No task file modified.
