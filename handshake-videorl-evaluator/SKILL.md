---
name: handshake-videorl-evaluator
description: Evaluate, answer, create, or audit Handshake VideoRL tasks and onboarding assessments. Use for Long Context VideoRL, Cross-Modal Anchoring, Audio Anchored Visual Retrieval, Visual Anchored Audio Retrieval, Tracked AV Counting, Exact Temporal Order, Repeated Events, Sparse Long-Video Retrieval, Long Trace-Grounded Counting, OCR/frame-following text, Short Spatial State-Change, Science & Technical Visual Reasoning, Action Anticipation, Paralinguistic Understanding, Audio-Visual Event Alignment, or Sound Source Identification tasks from HANDSHAKE-AI/pdfs/VideoRL--Cross-Modal Anchoring Guidelines.md or HANDSHAKE-AI/pdfs/Video RL.
---

# Handshake VideoRL Evaluator

## Core Rule

Use the relevant VideoRL markdown/PDF as the source of truth. If this skill, the user, memory, or a previous answer conflicts with the VideoRL guideline file, follow the guideline file.

Do not force image-generation, T2V artifact, TELUS, or generic video QA rules onto VideoRL rows. VideoRL rows are about writing or judging short, verifiable video-reasoning questions with clean anchors, short answers, evidence, distractors, and modality gates.

## Required Source Pass

Before answering a live VideoRL task, read only the sources needed for that task:

1. Read `references/queue-router.md` to identify the queue and required guideline file.
2. Read the matching file under `HANDSHAKE-AI/pdfs/Video RL/`, or the relevant section of `HANDSHAKE-AI/pdfs/VideoRL--Cross-Modal Anchoring Guidelines.md`.
3. For onboarding assessments, read the assessment item and answer exactly in the requested format.
4. When the queue is unclear, inspect the task wording and answer format before choosing a rubric.

## Universal VideoRL Gates

Reject or flag a row when any of these fail:

- The answer is not short, atomic, objective, and verifiable.
- The prompt uses raw timestamps instead of event anchors.
- The anchor gives away the answer or asks for the anchor itself.
- A single frame, audio alone, or video alone can answer a row that is supposed to require more.
- The row has no plausible distractor where the queue requires one.
- The evidence only restates the answer instead of saying where the answer appears and why near-misses fail.
- The question is yes/no, true/false, or multiple choice, except Paralinguistic Understanding, which intentionally uses A-H multi-select.
- The media is too ambiguous, unreadable, inaudible, cropped, or unverifiable.

## Cross-Modal Anchoring Workflow

Use `references/cross-modal-anchoring.md` for the two common onboarding queues:

- Audio Anchored Visual Retrieval: spoken phrase anchors, visual answer.
- Visual Anchored Audio Retrieval: silent visible action anchors, spoken answer.

Apply the 3-second boundary, one-time/distinctive anchor rule, mute test, audio-only test, distractor rule, and verbatim quote rule.

## Long Context Workflow

Use `references/long-context-videorl.md` for long-context queues such as ordering, sparse retrieval, counting, OCR, state-change, science reasoning, and anticipation.

Check the queue-specific timing floor:

- Exact/Repeated Temporal Order: watch span at least 5:00.
- Sparse Long-Video Retrieval: earliest-answerable at least 60s, target at least 120s.
- Long Trace-Grounded Counting: span 180-600s preferred, over 90s normal, under 60s blocked.
- Action Anticipation: cutoff strictly before action start, anticipation window 0.1-5s.
- Short Spatial State-Change: outcome usually within 2-20s.

## Answering Assessments

When the user asks for assessment answers:

- Give the selected answer first.
- Add a short "Why" only when helpful or requested.
- For write-in items, sound natural and concise; do not over-polish.
- Do not invent hidden video facts. Use only the assessment text and the rubric.

Preferred format:

```text
**1. Answer:**
Invalid - ...

**Why:**
...
```

For write-in responses, use 2-3 plain sentences.

## Creating Or Auditing Rows

When creating or auditing a VideoRL row:

1. Identify the queue.
2. Confirm the answer format.
3. Check anchors and modality gates.
4. Check timing fields and queue-specific floors.
5. Identify real distractors.
6. Confirm the evidence is reviewable.
7. Output the shortest useful verdict, correction, or completed row.

If a row can be fixed, name the concrete fix: choose a unique anchor, move the answer within the boundary window, replace a static answer with a changing one, add a same-type distractor, tighten the count window, or switch to the correct queue.


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

