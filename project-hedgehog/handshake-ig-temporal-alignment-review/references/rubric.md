# Handshake IG Temporal Alignment V2 Review Rubric

The operative rubric for auditing Sync a Video Pair submissions. Read this before auditing a live item.

## Contents

- [Source](#source)
- [What You Are Reviewing](#what-you-are-reviewing)
- [The Three Decisions](#the-three-decisions)
- [The Two Grading Axes](#the-two-grading-axes)
- [Grading Rubric 1-5](#grading-rubric-1-5)
- [Is It Worth Fixing](#is-it-worth-fixing)
- [Rework Action Table](#rework-action-table)
- [The Four Checks From An Auditors Seat](#the-four-checks-from-an-auditors-seat)
- [Skip, Flag, And Neither](#skip-flag-and-neither)
- [Review Simulations](#review-simulations)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Feedback Quality](#feedback-quality)
- [Final Checklist](#final-checklist)

## Source

No official PDF exists for this task. The highest local authority is:

- `HANDSHAKE-AI/hedgehog-extracted/docs/07_temporal_alignment_v2_review.md` — the reviewer page.
- `HANDSHAKE-AI/hedgehog-extracted/docs/03_ig_temporal_alignment.md` — the underlying task standard being graded.

Full reviewer guidelines, including scoring templates, are not published yet. Until they are, grade against this rubric and ask in the corresponding Slack channel when a call is unclear.

## What You Are Reviewing

You are auditing pairs other Fellows already reviewed and aligned on Sync a Video Pair — Temporal Alignment. You are not doing the task from scratch.

This training gates you: passing its knowledge checks is what lets you continue tasking as a reviewer.

**You are auditing, not redoing.** You are not re-sourcing or redoing the pair. Confirm what is right, fix what is wrong.

## The Three Decisions

1. **Read and review.** Watch both clips and the original Fellow's call. Check it against the four review checks and, if the pair was kept, press Play both. Rate the submission 1-5. Watch the whole submission before you rate it.
2. **Decide whether it is worth fixing.** Yes sends you to the editor; No records your grade and moves to the next item.
3. **Fix only if needed.** Re-anchor the start, trim a drifted tail, re-sync by audio, or correct a wrong keep/reject call, then submit.

## The Two Grading Axes

A submission can fail on either axis. Judge both.

### Decision accuracy — did they make the right keep/reject call?

Did the Fellow keep pairs that should have been kept and reject ones that should have been rejected? A wrongly-kept bad pair or a wrongly-rejected good pair is a decision-accuracy failure, **regardless of how tight the alignment is**.

### Alignment precision — for kept pairs, how tight is the sync?

How close is the start to the shared moment, does the segment stay on the same event, and does the audio line up without echo? Loose starts, wandering tails, and doubled audio are alignment-precision failures.

## Grading Rubric 1-5

The exact rubric Fellows self-check against, applied from the auditor's seat.

- **5 Exceptional** — perfect sync, no perceptible offset at the start, holds across the whole segment, same event throughout, accurate and specific prompt. **Or:** correctly rejected a genuinely bad pair. A correct reject earns full marks; no alignment needed.
- **4 Strong** — one minor flaw. Start anchored well under ~0.25s, slight drift only. Prompt accurate and clear, if not fully detailed.
- **3 Acceptable** — about 0.25s of desync (a faint echo on shared-sound pairs) and/or an adequate but thin prompt. The pair is genuinely valid and the same event; still usable.
- **2 Weak** — send back. Alignment clearly off (0.5-0.75s, obvious echo or visible lag) and/or an inaccurate prompt. **Or:** rejected a pair that could have been aligned.
- **1 Unacceptable** — unusable. No real attempt, or kept and aligned an unrelated pair. Also covers a missing or false prompt, and wrongly skipping a clearly syncable pair.

Grade accepted pairs on the final clips and prompt only. The annotator's own QA rating of the pair does not affect this score.

## Is It Worth Fixing

Make one decision: does the submission have problems you can correct in the editor?

**Yes, fix it when:**

- The alignment is off but fixable — re-anchor, re-trim, or re-sync by audio.
- A bad pair was wrongly kept — correct the call by rejecting it.
- The relationship-type label is wrong.
- The prompt is weak but the pairing and alignment are sound — rewrite the prompt.

**No, submit the grade and continue when:**

- It is already a clean 4-5 with nothing meaningful to improve.
- The pairing itself is wrong and would need a full re-source, which is not your job.
- There is a clean reject to confirm — grade it well and move on.

When you choose No, your grade is still recorded. The submission is just kept as-is.

## Rework Action Table

| What you find | Action |
|---|---|
| Start not anchored (offset > 0.25s) | **Re-anchor** the start on the shared moment |
| Tail wanders onto a different action | **Trim** the tail back to where the shared event ends |
| Visuals don't match closely | Switch to **audio blend** and sync on the shared sound |
| Wrong relationship-type label | **Correct** the label |
| Weak but salvageable prompt | **Rewrite** the prompt to name the transformation specifically |
| Genuinely bad pair kept | **Reject** the pair |

You use the identical alignment toolset as the original Fellow:

- **Drag the strip / edges** — slide a segment while keeping its length, or drag the edges to change its length.
- **‹ › nudge** — moves the start one frame at a time.
- **Play both / , / .** — play both clips together, or step one frame back and forward.
- **Overlay (o)** — stacks Clip B over Clip A with an opacity slider, best for matching motion frame by frame.
- **Audio blend (A↔B)** — mixes the two soundtracks so you can hear them sync.
- **Speed (0.25× / 0.5× / 1×)** — slow down to place the start precisely.
- **Skip (s) / Reset (r)** — skip when you genuinely cannot audit; reset to start the alignment over.

## The Four Checks From An Auditors Seat

**Connection and Matching segment are make-or-break** — they decide whether the keep/reject call was right. Engagement and Video check shape the quality rating for kept pairs.

1. **Connection** — does the response correspond to this specific original, not just the same person, style, or topic? A pair that does not correspond but was kept should be rejected. If a pair that does correspond was rejected, that is a decision-accuracy failure — grade it per the rubric.
2. **Matching segment** — is there a shared moment both clips can be anchored to, visual or audio? No shared moment means the Fellow was right to reject. A clear shared moment that was rejected means correcting the call.
3. **Engagement** — is the response worth watching? Use this to shape the quality rating on kept pairs, not to overturn a good keep/reject call.
4. **Video check / watermarks** — no third-party watermarks (a moving TikTok logo, a tiled Shutterstock/Getty overlay). Creator @handles and in-scene brands are fine. If the Fellow kept a pair with a disqualifying watermark, reject it.

## Skip, Flag, And Neither

- **Skip** — use when you genuinely cannot audit the item: a clip will not load, the data is broken. Skipping records nothing and moves on.
- **Flag** — use when the item is bad data that should be pulled for everyone: a corrupt file, not a real submission.
- **Neither** — if the original Fellow's call and alignment are already exactly right, grade it well. Do not invent problems to justify an edit.

## Review Simulations

**Submission A.** Both segments start on the same moment of the shared action; on Play both the shared event happens together. The first frame of Clip A and Clip B show the same moment.

→ **Grade 5 and submit as-is.** The start is anchored and the shared action holds across the whole segment. Re-anchoring "just to be safe" would be padding an already-correct submission.

**Submission B.** Clip A appears about one second early in Clip B, so the two play out of sync and are no longer about the same segment.

→ **Grade 2 (Weak) and re-anchor the start.** The pair itself is fine; the alignment is what failed. This is not a 1 and not bad data.

## Knowledge Check Answers

- **A ~0.6s start offset with an audible echo on Play both, on a real and valid recreation** → grade 2 (Weak) and send it back. The alignment is clearly off but the pair is salvageable. It is not a 4 (slight drift is not 0.6s) and not a 1 (an echo does not make the whole submission unusable).
- **A valid reaction, start anchored at ~0.1s, both clips on the shared event, prompt reads "girl reacts to video" — accurate but thin** → grade 4 (Strong) and submit as-is. Accurate-but-thin prompt is the definition of a 4. Do not rewrite it, and do not push it to 5 with extra nudges.
- **A pair the Fellow rejected, where the clips share no anchor moment at all** → grade 5. A correct reject earns full marks on the rubric, with no alignment needed. Do not try to align it first.

## Feedback Quality

Your score is only one part of the evaluation. The feedback you provide is assessed for accuracy, clarity, and usefulness to the annotator. A correct score paired with vague or generic feedback is still a weak review.

See `../../shared-references/reviewer-feedback.md` for the full standard: the three-part pattern, what to avoid, and the care required on 1s, 2s, and 5s.

Before submitting, ask: could the annotator read this and know exactly what to do differently next time?

## Final Checklist

1. Did I grade before editing?
2. Did I avoid redoing from scratch?
3. Did I re-anchor any start offset greater than 0.25s?
4. Did I trim tails that wandered onto a different event?
5. Did I correct a wrong keep/reject call if I disagreed with it?
6. Did I avoid padding an already-correct submission?
