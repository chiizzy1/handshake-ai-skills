# Handshake TI2T ELO Rubric

Use this reference for Text Image To Text ELO tasks.

## Contents

- [Current Source](#current-source)
- [Task Shape](#task-shape)
- [Core Standard](#core-standard)
- [Multi-Turn Rule](#multi-turn-rule)
- [Review Workflow](#review-workflow)
- [Rating Panel Rules](#rating-panel-rules)
- [Overall](#overall)
- [Factuality](#factuality)
- [Instruction Following](#instruction-following)
- [Helpfulness](#helpfulness)
- [Style And Format](#style-and-format)
- [Image/Video Reading Rules](#imagevideo-reading-rules)
- [Common Mistakes](#common-mistakes)
- [Comment Style](#comment-style)
- [Final Checklist](#final-checklist)

## Current Source

The current source is the TI2T instruction panel supplied by the user. No full PDF has been provided yet.

If a fuller TI2T PDF or task guide appears later, use it as the higher authority and update this file.

## Task Shape

The task usually shows:

- an image or video;
- a current/final user prompt;
- optional conversation history;
- two candidate text responses;
- a fixed rating panel:
  - Factuality: Major Issue, Minor Issue, No Issue - rated for Response A and again for Response B;
  - Instruction Following: same three levels, for A and for B;
  - Helpfulness: same three levels, for A and for B;
  - Style and Format: same three levels, for A and for B;
  - Overall: Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B;
  - Open Feedback: minimum 100 characters.

Your job is to decide which response is more acceptable for the prompt instructions and displayed media.

## Core Standard

Prefer the response that:

- accurately references visible details in the image or video;
- provides clear, correct, and complete information;
- follows the prompt and stays on topic;
- avoids unnecessary verbosity, repetition, and speculation.

## Multi-Turn Rule

When history is shown:

- Treat previous turns as shared context only.
- Rate the candidate responses against the current/final turn.
- Do not rate whether either response would have been good for an earlier turn.
- If the final prompt depends on earlier context, use that context only to understand what the final prompt is asking.

## Review Workflow

1. Read the current/final prompt.
2. Inspect every image or video shown for the current item.
3. Read any earlier conversation only as context.
4. Identify the exact task the response must perform:
   - answer a question;
   - describe the image/video;
   - extract visible text;
   - solve a problem shown in the image;
   - compare items;
   - explain a visible process;
   - follow a formatting or brevity instruction.
5. Read Response A.
6. Read Response B.
7. Check each response against the media and prompt.
8. Assign issue ratings for Factuality, Instruction Following, Helpfulness, and Style/Format, separately for Response A and Response B.
9. Choose the Overall preference from those ratings.

## Rating Panel Rules

### Overall Choices

The Overall control is a five-point preference scale, so record the size of the gap, not just the winner.

Strongly Prefer A / Strongly Prefer B:

- One response has a fundamental defect (a Factuality issue, an Instruction Following failure, or a severe Helpfulness gap) and the other succeeds.

Slightly Prefer A / Slightly Prefer B:

- Both complete the core task without visible errors, but one is better on polish: formatting, clearer explanation, or a more helpful tone.

Tie:

- The responses are genuinely equivalent, the media is not readable enough to decide, or the prompt is ambiguous and both readings are reasonable.

Do not tie-spam. Selecting Tie, or Slightly Prefer across every dimension, reads as low effort and lowers the quality score. Use Tie only when the responses are truly indistinguishable, not when the call is merely close.

### Issue Ratings

Rate every dimension for both responses. The panel asks for Response A and Response B separately on each of Factuality, Instruction Following, Helpfulness, and Style and Format.

Keep the Overall preference consistent with those ratings: if A carries a Major Issue and B carries none, the preference should not favor A.

## Overall

Choose the response that handles the current prompt more effectively.

Prefer the response that:

- answers the actual question;
- uses the image/video accurately;
- gives enough useful detail;
- avoids unsupported claims;
- is clear and efficient.

Do not choose a response just because it is longer or sounds more confident.

Tie is appropriate only when:

- both responses are essentially equal;
- the media is not readable enough to decide;
- the prompt is ambiguous and both interpretations are reasonable.

## Factuality

Check whether the response makes correct claims.

For image/video facts, use visible evidence:

- objects and people present;
- counts;
- positions and relationships;
- text, labels, numbers, and symbols;
- colors, states, and actions;
- math or problem content shown in the image;
- events visible in the video.

Major issue:

- The response gives a wrong answer to the main question.
- It invents important image/video details.
- It misreads key text, numbers, labels, or math.
- It makes an outside factual claim that is materially wrong.

Minor issue:

- A small detail is wrong but the main answer is still usable.
- It overstates uncertainty or certainty in a low-impact way.
- It omits a caveat that would make the answer cleaner.

No issue:

- Claims are supported by the media, prompt, or verified facts.

If outside knowledge is needed and you are unsure, verify before rating. Do not browse when the answer is visible in the media.

## Instruction Following

Check whether the response follows the current/final prompt.

Major issue:

- It answers the wrong question.
- It ignores a required format.
- It refuses or avoids a safe answer without reason.
- It focuses on earlier conversation instead of the final turn.
- It omits a required part of a multi-part prompt.

Minor issue:

- It mostly answers but misses a small constraint.
- It gives the right answer in a slightly wrong format.
- It includes some off-topic detail but remains usable.

No issue:

- It follows the prompt, constraints, and current-turn context.

## Helpfulness

Check whether the answer is useful for the user.

Major issue:

- It is too incomplete to satisfy the prompt.
- It does not explain enough when explanation is needed.
- It gives vague advice instead of using the image/video.
- It leaves out the main visible evidence needed for the answer.

Minor issue:

- It is usable but could be clearer, more complete, or more direct.
- It misses a secondary detail.
- It includes extra information that mildly reduces usefulness.

No issue:

- It directly answers the prompt with enough relevant detail.

## Style And Format

Check whether the response is clear and readable.

Major issue:

- Formatting makes the answer hard to use.
- The response is rambling, repetitive, or confusing.
- The tone is inappropriate for the task.

Minor issue:

- Slightly wordy.
- Minor formatting mismatch.
- Awkward wording that does not block understanding.

No issue:

- Clear, concise, readable, and formatted as requested.

## Image/Video Reading Rules

- Zoom or inspect small text, equations, labels, and objects before rating.
- If the image is unclear, do not pretend to see details.
- If both responses make unsupported guesses, prefer the one that is more cautious and less wrong.
- If one response says it cannot determine something that is genuinely not visible, that can be correct.
- If the answer is visible and one response refuses to answer, mark that down.

## Common Mistakes

- Rating based on which response sounds more polished.
- Ignoring visible text or numbers in the image.
- Treating earlier turns as the rated prompt.
- Rewarding unnecessary long explanations.
- Penalizing a concise answer that fully satisfies the prompt.
- Accepting speculation because it sounds plausible.
- Using a Handshake image-generation rubric on a text-response task.

## Comment Style

Use short, plain reasons.

Good:

`Response A is better because it reads the equation correctly and answers the final prompt directly. Response B changes the sign of the second term.`

Good:

`B is stronger because it mentions the warning label visible on the bottle. A gives general safety advice but misses the image detail.`

Bad:

`Response B demonstrates a more holistic and nuanced understanding of the multimodal context.`

## Final Checklist

- Current/final turn rated.
- Image/video details checked.
- Both responses compared against the same prompt.
- Factuality, instruction following, helpfulness, and style kept separate.
- Outside facts verified when necessary.
- Every dimension rated for both Response A and Response B.
- Overall preference chosen on the five-point scale and consistent with those ratings.
- Tie used only when genuinely indistinguishable, not for close calls.
- Open Feedback is at least 100 characters.
