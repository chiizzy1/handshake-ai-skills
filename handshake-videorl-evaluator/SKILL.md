---
name: handshake-videorl-evaluator
description: Evaluate, answer, create, or audit Handshake VideoRL rows and onboarding assessments. Use when a task involves short, verifiable video-reasoning questions built from event anchors, evidence, distractors, and modality gates, including Long Context VideoRL and Cross-Modal Anchoring queues.
---

# Handshake VideoRL Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- No VideoRL guideline or assessment files exist under `HANDSHAKE-AI/` at time of writing. If source files are unavailable, the three reference files in this skill folder are operative: `references/queue-router.md`, `references/cross-modal-anchoring.md`, and `references/long-context-videorl.md`. Say that the source file was unavailable.

## Covered Queues

Audio Anchored Visual Retrieval, Visual Anchored Audio Retrieval, Tracked AV Counting, Audio-Visual Event Alignment, Audio-Visual Sound Source Identification, Paralinguistic Understanding, Exact Temporal Order - Consequence, Exact Temporal Order - Repeated Events, Sparse Long-Video Retrieval, Long Trace-Grounded Counting, OCR Extraction / Frame-Following Dynamic Text, Short Spatial State-Change / Physical Outcome, Science & Technical Visual Reasoning, Action Anticipation & Prediction, Temporal Order - Fine-Grained, Temporal Ordering - How-To.

## Core Rule

Use the relevant VideoRL guideline file as the source of truth when one is available. If this skill, the user, memory, or a previous answer conflicts with the guideline file, follow the guideline file. When no guideline file can be found, this skill's reference files are operative.

Do not force image-generation, T2V artifact, TELUS (a separate annotation platform with its own rubrics), or generic video QA rules onto VideoRL rows. VideoRL rows are about writing or judging short, verifiable video-reasoning questions with clean anchors, short answers, evidence, distractors, and modality gates.

## Required Source Pass

Before answering a live VideoRL task, read only the sources needed for that task:

1. Read `references/queue-router.md` to identify the queue and its rubric.
2. Read the matching reference file in this skill folder. If an external guideline file for that queue is available in the workspace, read it too and let it outrank this skill.
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

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Give your answers in the chat, using the Answering Assessments format above.

