# Long Context VideoRL

Use this reference for Long Context VideoRL onboarding and row review. Read the matching source file for the queue before final judgment.

## Contents

- [Shared Requirements](#shared-requirements)
- [Exact Temporal Order - Consequence](#exact-temporal-order---consequence)
- [Exact Temporal Order - Repeated Events](#exact-temporal-order---repeated-events)
- [Sparse Long-Video Retrieval](#sparse-long-video-retrieval)
- [Long Trace-Grounded Counting](#long-trace-grounded-counting)
- [OCR / Frame-Following Dynamic Text](#ocr-frame-following-dynamic-text)
- [Short Spatial State-Change](#short-spatial-state-change)
- [Science & Technical Visual Reasoning](#science-technical-visual-reasoning)
- [Action Anticipation & Prediction](#action-anticipation-prediction)

## Shared Requirements

- The answer must be short, atomic, and objective.
- Use event anchors in questions, not raw timestamps.
- The anchor must not leak the answer.
- A single frame should not answer the row unless the queue is explicitly OCR at an event-selected frame.
- Evidence must name the target moment, the answer-bearing cue, and why distractors fail.
- Strong rows include real near-misses: repeated objects, similar events, same-type OCR text, wrong actor/object, off-window actions, delayed consequences, or competing outcomes.

## Exact Temporal Order - Consequence

Answer format: comma-separated numeric sequence.

Check:

- 6-10 concrete numbered candidate events.
- Candidate list is shuffled, not chronological.
- No order-leaking words inside candidates: after, then, before, first, later, finally.
- Watch span is at least 5:00.
- Per-candidate timestamps exist.
- Order cannot be inferred from common procedure logic.
- At least two plausible swaps or temporal distractors.

## Exact Temporal Order - Repeated Events

Answer format: comma-separated numeric sequence with at least one repeated number.

Check:

- One repeated event remains one candidate; do not split into first/second occurrence.
- Every event appears at least once.
- Repeated event occurrences are interleaved with other events when possible.
- Per-occurrence timestamps are recorded per answer position.
- Span is at least 5:00.

## Sparse Long-Video Retrieval

Answer format: 1-8 words.

Check:

- Earliest-answerable is at least 60s; 120s+ is better.
- The answer is absent from the title, thumbnail, opening, and final 5 seconds without the anchor.
- The anchor selects a unique late/middle segment.
- The row names a plausible distractor segment.
- The question asks one short fact, not a summary.

## Long Trace-Grounded Counting

Answer format: integer only, including 0.

Check:

- Count span is 180-600s preferred, over 90s normal, under 60s blocked.
- Start and end anchors are clear.
- The counted event is precisely defined.
- Evidence lists each counted occurrence and excluded near-misses.
- Zero counts require real distractors.
- Do not count OCR/text instances here unless the queue is OCR text-instance counting.

## OCR / Frame-Following Dynamic Text

Answer format: exact visible text or number.

Check:

- The question asks what text says, not what it means.
- The target text is readable and not given in the question.
- A same-type readable distractor is present and recorded.
- The anchor selects the right frame or navigation chain.
- Preserve punctuation, symbols, digits, prices, scores, and meaningful case.

## Short Spatial State-Change

Answer format: short outcome phrase.

Check:

- Clear setup -> action/contact -> outcome.
- The answer cannot be known before the action.
- Prefer at least three plausible outcomes; avoid binary left/right or yes/no.
- Outcome appears on camera within about 2-20s.
- Name a competing destination, path, object, or outcome.

## Science & Technical Visual Reasoning

Answer format: one atomic fact.

Check:

- Requires reading visible evidence and applying a domain rule.
- Not pure OCR and not textbook recall.
- Grounded in a chart, table, equation, diagram, animation, or experiment.

## Action Anticipation & Prediction

Answer format: short verb phrase.

Check:

- Cutoff is strictly before the predicted action begins.
- Anticipation window is 0.1-5s.
- The action is not already visible/complete at cutoff.
- The answer is the immediate next action or outcome, not long-horizon speculation.
- The row requires both audio and video when the queue requires it.
