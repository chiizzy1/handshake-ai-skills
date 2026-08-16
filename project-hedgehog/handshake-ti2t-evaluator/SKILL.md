---
name: handshake-ti2t-evaluator
description: Evaluate Handshake Text Image To Text ELO (TI2T) tasks. Use when a task shows an image or video, a current user prompt, conversation history if present, and two candidate text responses to compare for acceptability, factuality, instruction following, helpfulness, and style/format.
---

# Handshake TI2T Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use the visible TI2T task instructions as the current source of truth. If a fuller TI2T PDF or guideline appears later, it outranks this skill and this skill should be updated.

Current source instruction:

- Judge which candidate response is more acceptable for the prompt instructions and the displayed image or video.
- Review the prompt and media carefully, including all images or videos shown for the current item.
- Read both candidate responses and rate them on the configured dimensions.
- Choose the response that handles the prompt more effectively, or use `Tie` when appropriate.
- For multi-turn prompts, treat previous turns as shared context only. Rate the candidate responses against the current/final turn, not earlier turns.
- Prefer responses that accurately reference visible image/video details, provide clear/correct/complete information, follow the prompt and stay on topic, and avoid unnecessary verbosity, repetition, or speculation.

Before rating a live TI2T task, read `references/rubric.md`.

## Hard Gates

- Do not rate before inspecting the media and reading both candidate responses.
- Do not answer from general impression when the image/video contains checkable details.
- Do not reward a response for confident wording if it invents visual facts.
- Do not punish a response for being concise if it fully answers the prompt.
- Do not judge earlier conversation turns. Use them only as context for the current/final user prompt.
- **Verification rule:** if a fact is visible in the displayed media, verify it from the media only. If the prompt depends on outside real-world facts (current prices, specifications, dates, verifiable claims), verify them with your web-search tool before rating. Do not rely on internal knowledge alone for outside facts, and do not go looking online for what the media already shows.
- Do not force a winner when the responses are genuinely equivalent or impossible to judge; that is what `Tie` is for. Equally, do not tie-spam a close call.

## Interaction Protocol

Which protocol applies depends on what the user pasted.

**Candidate responses are present** — the task arrives with the prompt, the media, AND both candidate responses. Produce the ratings directly using the Output Format below. Do not stop and ask.

**Candidate responses are NOT present** — the task arrives with the prompt and media only. Use the two-step hard stop:

*Step 1: Understand First.* Your response must ONLY contain:

1. **The Context**: A summary of your understanding of the prompt and the images/media.
2. **The Breakdown**: What you will be checking once the responses arrive.

END that response with **"Awaiting your command to grade."** Do not generate the Ratings Table or the Open Feedback at this stage.

*Step 2: Grade It.* Once the responses arrive and the user gives the go-ahead, output the Ratings Table and the Open Feedback.

## Workflow

1. Identify the current/final user prompt.
2. Treat earlier turns as context only.
3. Inspect every displayed image or video carefully.
4. Note the visible facts needed to answer the prompt: objects, people, text, numbers, labels, actions, positions, and states.
5. Read Response A fully.
6. Read Response B fully.
7. Check each response against the prompt and media.
8. Rate every dimension independently, for Response A and for Response B.
9. Pick the overall preference from those ratings, using `Tie` only when justified.
10. Write the Open Feedback: a short reason tied to the image/video and the response text.

## Required Rating Panel

TI2T is an ELO comparison. The panel rates **both responses on every dimension**, then asks for one overall preference on a five-point scale.

1. Factuality: `Major Issue`, `Minor Issue`, or `No Issue` — **for Response A and again for Response B**.
2. Instruction Following: same three levels, for A and for B.
3. Helpfulness: same three levels, for A and for B.
4. Style and Format: same three levels, for A and for B.
5. Overall: `Strongly Prefer A`, `Slightly Prefer A`, `Tie`, `Slightly Prefer B`, or `Strongly Prefer B`.
6. Open Feedback: minimum 100 characters.

Rate each response on its own merits first, then pick the overall preference from that evidence. Do not rate only the response you preferred: every dimension needs a level for both A and B.

Use the exact labels shown by the task UI. If a UI variant offers different choices (for example an `I don't know` option), follow the UI.

## Dimension Meanings

- Overall: which response handles the current prompt more effectively, and by how much.
- Factuality: whether the rated response makes correct claims about the image/video or any needed outside facts.
- Instruction Following: whether the rated response answers the asked question, follows constraints, and stays on topic.
- Helpfulness: whether the rated response gives enough useful information without missing key parts of the prompt.
- Style and Format: whether the rated response is clear, readable, well organized, and not needlessly verbose.

Use the exact labels shown in the UI. If the UI uses different dimensions, follow the UI and apply the same source rule: prompt + media first.

## Choosing the Overall Label

The Overall control is a five-point preference scale, so the strength of the gap matters, not just the winner.

- **Strongly Prefer A / B** when one response has a fundamental defect (a Factuality issue, an Instruction Following failure, or a severe Helpfulness gap) and the other succeeds.
- **Slightly Prefer A / B** when both complete the core task without visible errors but one is better on polish: formatting, a clearer explanation, or a more helpful tone.
- **Tie** only when the responses are genuinely equivalent, the media is not readable enough to decide, or the prompt is ambiguous and both readings are reasonable.

Do not tie-spam. Picking `Tie`, or `Slightly Prefer` on every dimension, reads as low effort and lowers the quality score. Use `Tie` only when the responses are truly indistinguishable, not when the call is merely close.

Keep the overall preference consistent with the per-dimension ratings you assigned: if A carries a Major Issue and B carries none, the preference should not favor A.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../../shared-references/how-to-see.md`.

## Open Feedback Style

The field is **Open Feedback**, minimum 100 characters. Write 2 to 3 sentences.

**The Persona: someone who read both answers with the image still open.**

You are not grading an essay. You checked each answer against what is actually in the media and noticed where one of them went wrong.

1. **Lead with the factual difference.** If one response misreads the image, that is the comment. Everything else is secondary.
2. **Quote the detail.** Name the value, label, or object the response got wrong, not "an inaccuracy."
3. **Length is not helpfulness.** If the longer answer padded, say it padded. Do not praise thoroughness that did not answer the question.
4. **Short sentences. Periods.** No em dashes, no semicolons, no colons in prose.
5. **Use "while" instead of "whereas."**
6. **Avoid absolutes.** Not "answers perfectly." Use "gets it right," "reads it correctly."
7. **Neutral.** Describe the error, do not editorialize about it.

**Banned phrases:** "demonstrates," "holistic," "nuanced understanding," "multimodal context," "Upon review of," "comprehensively addresses," "it is evident that," "superior."

For worked examples and the four recurring comment patterns, read the Comment Style section in `references/rubric.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your answers and ratings in clean markdown directly in the chat using the template below.

```markdown
### Input Analysis
[The current/final prompt and the objective facts visible in the media.]

### Response Analysis
[Analyze Response A against the prompt and media.]
[Analyze Response B against the prompt and media.]

### Final Ratings

| Dimension | Response A | Response B |
|---|---|---|
| Factuality | No Issue | Minor Issue |
| Instruction Following | No Issue | No Issue |
| Helpfulness | No Issue | Major Issue |
| Style and Format | No Issue | No Issue |

**Overall: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]**

### Open Feedback
[2-3 concise sentences, minimum 100 characters, naming the main difference and sounding like a person wrote it.]
```

Every dimension needs a level for both responses. Use the exact labels shown by the task UI; if the UI shows different dimensions or choices, follow the UI.

## Final Checklist

- Current/final prompt identified.
- All media inspected.
- Both responses read fully.
- Visible details checked against each response.
- Earlier turns used only as context.
- Every dimension rated for BOTH Response A and Response B.
- Overall preference chosen on the five-point scale and consistent with those ratings.
- Speculation, repetition, and unsupported claims checked.
- `Tie` used only when genuinely indistinguishable, not for close calls.
- Open Feedback is 2-3 sentences and at least 100 characters.
