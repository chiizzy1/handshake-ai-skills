---
name: handshake-ti2t-evaluator
description: Evaluate Handshake Text Image To Text ELO (TI2T) tasks. Use when a task shows an image or video, a current user prompt, conversation history if present, and two candidate text responses to compare for acceptability, factuality, instruction following, helpfulness, and style/format.
---

# Handshake TI2T Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

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
- **Verification rule:** if a fact is visible in the displayed media, verify it from the media only. If the prompt depends on outside real-world facts (current prices, specifications, dates, verifiable claims), verify them with your web-search tool before rating. Do not rely on internal knowledge alone for outside facts, and do not go looking online for what the media already shows.
- Do not force a winner when the UI allows tie / I don't know and the responses are genuinely equivalent or impossible to judge.

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

## Choosing the Overall Label

The Overall control offers `Response A`, `Response B`, `Both Good`, and `Both Bad`. There is no strong/slight gradient — pick one of those four.

- **Pick `Response A` or `Response B`** when one response has a fundamental defect (a Factuality issue, an Instruction Following issue, or a severe Helpfulness failure) and the other succeeds. Also pick a side when both complete the core task without visible errors but one is clearly better on polish — formatting, clearer explanation, or a more helpful tone.
- **Pick `Both Good`** when both responses genuinely succeed and no defensible difference separates them.
- **Pick `Both Bad`** when both responses genuinely fail.

Do not use `Both Good` or `Both Bad` just because the choice is close. Use them only when both responses genuinely belong in the same bucket.

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../shared-references/how-to-see.md`.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your answers and ratings in clean markdown directly in the chat using the template below.

```markdown
### Input Analysis
[The current/final prompt and the objective facts visible in the media.]

### Response Analysis
[Analyze Response A against the prompt and media.]
[Analyze Response B against the prompt and media.]

### Final Ratings
- Overall: [Response A | Response B | Both Good | Both Bad]
- Factuality: [Major issue | Minor issue | No issue]
- Instruction Following: [Major issue | Minor issue | No issue]
- Helpfulness: [Major issue | Minor issue | No issue]
- Style and Format: [Major issue | Minor issue | No issue]

### Justification
[Brief, natural-language reason tied to the media and the response text.]
```

Use the exact labels shown by the task UI. If the UI shows different dimensions or choices, follow the UI.

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
