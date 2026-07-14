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

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input asks for. Establish the objective facts from the original prompt/image/code.]

### Response Analysis
[Analyze Response A, pointing out strengths and weaknesses compared to the objective facts.]
[Analyze Response B, pointing out strengths and weaknesses compared to the objective facts.]

### Final Ratings
[List the ratings for all required criteria for the specific task.]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
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
