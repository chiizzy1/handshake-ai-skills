---
name: handshake-ti2t-evaluator
description: Evaluate Handshake Text Image To Text ELO (TI2T) tasks. Use when a task shows an image or video, a current user prompt, conversation history if present, and two candidate text responses to compare for acceptability, factuality, instruction following, helpfulness, and style/format.
---

# Handshake TI2T Evaluator

## Core Rule

Use the visible TI2T task instructions as the current source of truth. If a fuller TI2T PDF or guideline appears later, it outranks this skill and this skill should be updated.

Current source instruction:

- Judge which candidate response is more acceptable for the prompt instructions and the displayed image or video.
- Review the prompt and media carefully, including all images or videos shown for the current item.
- Read both candidate responses and rate them on the configured dimensions.
- Choose the response that handles the prompt more effectively, or use tie / I don't know when appropriate.
- For multi-turn prompts, treat previous turns as shared context only. Rate the candidate responses against the current/final turn, not earlier turns.
- Prefer responses that accurately reference visible image/video details, provide clear/correct/complete information, follow the prompt and stay on topic, and avoid unnecessary verbosity, repetition, or speculation.

Before rating a live TI2T task, read `references/rubric.md`.

## Hard Gates

- Do not rate before inspecting the media and reading both candidate responses.
- Do not answer from general impression when the image/video contains checkable details.
- Do not reward a response for confident wording if it invents visual facts.
- Do not punish a response for being concise if it fully answers the prompt.
- Do not judge earlier conversation turns. Use them only as context for the current/final user prompt.
- Do not browse for what can be verified directly from the displayed image/video.
- **ALWAYS browse online and fact-check!** Never rely solely on your internal knowledge, as it may be outdated or incomplete. If the task involves real-world facts, current prices, specifications, or verifiable claims outside the visible media, you MUST browse the internet to confirm the ground truth before assuming the model is correct.
- Do not force a winner when the UI allows tie / I don't know and the responses are genuinely equivalent or impossible to judge.

## Interaction Protocol (The Hard Stop)

When interacting with the user on TI2T tasks, you MUST follow this strict two-step protocol to ensure deep context and accurate ratings:

**Step 1: Understand First (The Hard Stop)**
When the user provides a new task, your response must ONLY contain:
1. **The Context**: A summary of your understanding of the prompt and the images/media.
2. **The Breakdown**: A summary of your analysis of what the models did (e.g., identifying factual errors, formatting issues).

*CRITICAL*: You must END your response with **"Awaiting your command to grade."** You are explicitly forbidden from generating the Ratings Table or the Open Feedback at this stage. You must stop and wait for the user to confirm your understanding.

**Step 2: Grade It**
Only after the user explicitly gives the go-ahead (e.g., "Grade it"), you will output the Ratings Table and the Open Feedback.

## Workflow

1. Identify the current/final user prompt.
2. Treat earlier turns as context only.
3. Inspect every displayed image or video carefully.
4. Note the visible facts needed to answer the prompt: objects, people, text, numbers, labels, actions, positions, and states.
5. Read Response A fully.
6. Read Response B fully.
7. Check each response against the prompt and media.
8. Rate the configured dimensions independently.
9. Pick the better response overall, or tie / I don't know only when justified.
10. Give a short reason tied to the image/video and response text.

## Required Rating Panel

TI2T tasks usually require this fixed rating sequence:

1. Overall: `Response A`, `Response B`, `Both Good`, or `Both Bad`.
2. Factuality: `Major issue`, `Minor issue`, or `No issue`.
3. Instruction Following: `Major issue`, `Minor issue`, or `No issue`.
4. Helpfulness: `Major issue`, `Minor issue`, or `No issue`.
5. Style and Format: `Major issue`, `Minor issue`, or `No issue`.

Choose Overall by comparing both responses. Then assign the four issue ratings using the response/output the UI is asking you to rate. If the UI does not show separate per-response issue controls, apply the issue ratings to the response you selected overall. If Overall is `Both Good` or `Both Bad`, rate the pair according to the shared quality level and explain briefly.

## Dimension Meanings

- Overall: which response handles the current prompt more effectively.
- Factuality: whether the rated response makes correct claims about the image/video or any needed outside facts.
- Instruction Following: whether the rated response answers the asked question, follows constraints, and stays on topic.
- Helpfulness: whether the rated response gives enough useful information without missing key parts of the prompt.
- Style and Format: whether the rated response is clear, readable, well organized, and not needlessly verbose.

Use the exact labels shown in the UI. If the UI uses different dimensions, follow the UI and apply the same source rule: prompt + media first.

## Overall Preference Thresholds

- **Strongly Prefer**: Use when there is a fundamental defect in one response (e.g., a Factuality issue, an Instruction Following issue, or a severe Helpfulness failure) while the other response succeeds.
- **Slightly Prefer**: Use when **both** responses successfully complete the core task without any visible errors (i.e., both rate "No Issue" across Factuality, Instruction Following, and Helpfulness). The preference is based solely on "polish"—such as better formatting, clearer explanations, or a slightly more helpful tone.

## Output Format

When presenting the results to the user in chat, always use this specific structure:

1. **The Ratings Table**: Present the ratings in a 4-column markdown table, including a "Brief Reasoning" column for concise, dimension-specific explanations.
2. **Open Feedback**: Output the exact heading `# Open Feedback (minimum 100 characters):` followed by the explanation. **Writing Style Rule**: Ensure that all writing is in American English, not British English. Keep the feedback extremely concise, simple, and naturally sounding, like a real human worker quickly typing out their reasoning. Do not use overly formal, robotic, or professorial language. Point out exactly what is wrong without verbosity. Never use em dashes (`—`) or other overly literary punctuation.

Example:

```markdown
### The Ratings Table

| Dimension | Response A | Response B | Brief Reasoning |
| :--- | :--- | :--- | :--- |
| **Factuality** | Major Issue | No Issue | **A** hallucinated the face was obscured; **B** accurately described the visible face. |
| **Instruction Following** | Major Issue | No Issue | **A** failed the synthesis directive; **B** flawlessly merged details. |
| **Helpfulness** | No Issue | No Issue | **B** fully answered the prompt; **A** provided a good scene breakdown despite the factual failure. |
| **Style and Format** | No Issue | No Issue | Both models used the requested clear formatting. |
| **Overall Preference** | | **Strongly Prefer B** | **B** mastered a complex prompt; **A** failed basic observation. |

# Open Feedback (minimum 100 characters):
Response A wrongly claimed that the face is obscure in every image which is wrong because attachment 0 and attachment 3 clearly shows the face. Due to this, response A missed major prompt requirements like head shape and eye-width measurements. Response B is better because it actually followed the instruction and described the face based on what is visible from the images.
```

### Good vs. Bad Feedback Examples (Avoiding Contradictions)

**Never contradict your own ratings.** If you mark a model as having a "Minor Issue" in Factuality because it misread a number (e.g., reading 8.05 as 6.05), you cannot say it "extracted the right numbers" in the feedback.

**[BAD] - Contradicts Ratings (Blanket Praise):**
"Response B is much better because it provides step-by-step working and gets the math right, making it an excellent study guide, while Response A provides no working and gets several math questions completely wrong by falsely claiming the correct answers are not in the options."
*(Why it's bad: It uses a blanket phrase "gets the math right" that completely contradicts the fact that Response B was marked with a Minor Issue for getting the trivia date wrong on Q29. Never claim something is 100% correct if you logged an error for it).*

**[GOOD] - Factually Accurate & Matches Ratings:**
"Response B is much better because it provides step-by-step working and mostly gets the math right except for Q29 where it made a mistake with the date, making it an excellent study guide, while Response A provides no working and gets several math questions completely wrong by falsely claiming the correct answers are not in the options."
*(Why it's good: It flawlessly combines the 'Winner First' structure while cleanly acknowledging the Q29 error without breaking the natural, conversational flow).*

**[BAD] - Contradicts Ratings (Subtle Contradiction):**
"Response B is much better because it correctly processes the uploaded exam paper and provides a full answer key despite making a few minor transcription typos, while Response A completely ignores the image and just repeats an old answer."
*(Why it's bad: It claims the model "correctly processes" the paper, but then immediately admits it made "transcription typos". If it made typos, it didn't process it correctly. This creates a logical contradiction. How to catch it in the future: Always double-check if your positive praise ("correctly processes") directly conflicts with any errors you are listing in the same sentence. If there are errors, always use hedging words like "mostly".)*

**[GOOD] - Factually Accurate & Hedged:**
"Response B is much better because it mostly correctly processes the uploaded exam paper and provides a full answer key except for a few minor transcription typos, while Response A completely ignores the image and just repeats an old answer."
*(Why it's good: It uses "mostly" and "except for" to safely praise the model while accurately acknowledging the errors, perfectly aligning with a Minor Issue rating without creating a logical contradiction).*

### Good vs. Bad Feedback Examples (Natural Flow & Formatting Focus)

**Write clearly, concisely, and flow naturally like a human being.** Explain *why* a difference matters to the user experience without rigidly forcing templates when they don't fit.

**[BAD] - Forced/Clunky Flow:**
"Response A just listed raw answers without the questions which is bad because it makes it hard to match the answers to the worksheet. Due to this, response A failed to be a useful study guide. Response B is better because it actually included the original questions and explained the false answers based on what is visible from the images, even though it made a few errors like adding conversational filler."
*(Why it's bad: It rigidly forces the "due to this" and "a few errors like" templates where they aren't needed, making the sentence clunky, overly long, and unnatural).*

**[GOOD] - Natural Flow & Explains the 'Why':**
"Response A only listed the answers without the questions and this makes it harder for the user to match questions to their answers. Response B lists the questions and answers side-by-side making it easier for the user to understand at a glance without needing to go back and forth to match questions to their answers. This makes Response B more useful overall."
*(Why it's good: It flows perfectly like a real human review, directly addresses the UX impact of "going back and forth," and perfectly justifies a win based purely on Helpfulness and Formatting).*

### Good vs. Bad Feedback Examples (Conciseness & Directness)

**Cut repetitive fluff.** Be extremely direct. Use simple, everyday vocabulary instead of academic/repetitive phrasing.

**[BAD] - Wordy & Repetitive:**
"Response A wrongly claimed that the angles add up to 180 degrees in question 16A which is wrong because the exterior angles of a triangle actually add up to 360 degrees. Due to this, response A failed to provide the accurate mathematical answer. Response B is better because it actually did the math correctly and gave the right answer based on what is in the image."
*(Why it's bad: It's too long, repeats concepts ("wrongly claimed... which is wrong"), and uses unnecessarily wordy phrasing ("failed to provide the accurate mathematical answer")).*

**[GOOD] - Short, Punchy, & Simple:**
"Response A gave the wrong answer for question 16A by saying the angles add up to 180. They actually add up to 360. Response B is better because it did the math correctly and gave the right answer."
*(Why it's good: It is incredibly concise, uses basic everyday vocabulary, eliminates all repetitive fluff, and gets straight to the point).*

### Good vs. Bad Feedback Examples (Context Awareness & Ignoring Image)

**Reward models that process the actual image. Penalize models that hallucinate answers based on chat history.**

**[BAD] - Ignores the core failure:**
"Response A provided a correct list of contact and non-contact forces which is helpful. Response B gave the answer key for the test. Response B is better because it provides more answers."
*(Why it's bad: It completely misses the point that Response A ignored the image and just repeated a previous chat history answer).*

**[GOOD] - Crisp, Context-Aware:**
"Response A completely missed the point by ignoring the uploaded image and repeating a previous answer. Response B is the clear winner because it actually analyzed the exam paper and provided a full, accurate answer key."
*(Why it's good: It calls out the exact failure (ignoring the image) and the exact success (analyzing the exam paper) in a natural, conversational tone).*

### Good vs. Bad Feedback Examples (Stripping AI-Speak & Extreme Directness)

**Avoid overly dramatic AI-evaluator words like "hallucinated" or "bizarre." Stick to the absolute basic facts of what happened without any extra flair or robotic emotion.**

**[BAD] - Dramatic / AI-Speak:**
"Response B is bizarre because it pretends it can actually hear the audio from the screenshot. Response A is much better because it didn't make things up and just used common sense to provide a straightforward list of the answers."
*(Why it's bad: Words like 'bizarre', 'pretends', and 'common sense' make it sound like an AI trying too hard to mimic human emotion).*

**[GOOD] - Stripped-Down & Factual:**
"Response B falsely claims to have listened to the audio when the user only uploaded screenshots. Response A is much better because it just provides the answers and does not contain any false claims."
*(Why it's good: It is stripped down to the absolute basics. It states the facts directly and professionally without trying to sound artificially 'chatty').*

### Good vs. Bad Feedback Examples (Structural Pattern: Winner First)

**Always state the WINNING response first, explaining why it won, followed by the LOSING response and why it failed. This creates a more positive, direct, and easier-to-read flow.**

**[BAD] - Loser First:**
"Response A completely ignores the prompt and does not answer the question about the baby's gender. Response B is much better because it directly addresses the question and correctly explains that the gender cannot be determined from the provided images."
*(Why it's bad: It focuses on the failure before getting to the actual correct answer).*

**[GOOD] - Winner First:**
"Response B is much better because it directly addresses the question and correctly explains that the gender cannot be determined from the provided images, while Response A completely ignores the prompt and does not answer the question about the baby's gender."
*(Why it's good: It immediately highlights the correct response and uses "while" to smoothly transition into the losing model's failure).*

If the UI asks only for a winner:

```markdown
Response B

Reason: B answers the current prompt more directly and does not invent details beyond the image.
```

## Final Checklist

- Current/final prompt identified.
- All media inspected.
- Both responses read fully.
- Visible details checked against each response.
- Earlier turns used only as context.
- Overall selected before assigning issue ratings.
- Factuality, Instruction Following, Helpfulness, and Style/Format issue levels selected from the UI choices.
- Speculation, repetition, and unsupported claims checked.
- Tie / I don't know used only when genuinely appropriate.
