---
name: handshake-ig-temporal-alignment-review
description: Audit Handshake IG Video Temporal Alignment V2 submissions. Use when asked to review another Fellow's Sync a Video Pair keep-or-reject call and alignment, grade it 1-5 on decision accuracy and alignment precision, decide whether it is worth fixing, and rework it in place.
---

# Handshake IG Temporal Alignment V2 — Review

You audit another Fellow's Sync a Video Pair submission: their keep-or-reject call and, if they kept it, their alignment. Review the whole submission, rate it 1-5, then decide whether it is worth fixing.

**You are auditing, not redoing.** You are not re-sourcing or redoing the pair from scratch. Confirm what is right, fix what is wrong. A full redo is not your job.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. `HANDSHAKE-AI/hedgehog-extracted/docs/07_temporal_alignment_v2_review.md` — the reviewer guideline page.
2. `HANDSHAKE-AI/hedgehog-extracted/docs/03_ig_temporal_alignment.md` — the underlying task standard you are grading against.
3. The current task UI and the visible submission in front of you.
4. `references/rubric.md`, then `../shared-references/ig-video-pairs.md`.
5. `HANDSHAKE-AI/guidelines.md` as a broad summary only.
6. User memory or prior answers.

Full reviewer guidelines, including scoring templates, are not published yet. Until they are, grade against this rubric and raise unclear calls in the corresponding Slack channel.

Say plainly when an expected source cannot be found. Do not import TELUS or Outlier rules into Handshake work.

## Inspecting The Media

Do not judge a Reel you have not actually looked at. Fetch and inspect it first:

```bash
python3 handshake-ai-skills/tools/inspect_media.py --url <reel-url> --out /tmp/insp
```

This finds every scene, saves a keyframe per scene, builds a contact sheet, and
transcribes the audio with timestamps. Read the scene list and the contact sheet
before answering anything about the clip as a whole. Run it on both clips. Grading alignment precision means measuring the offset, and the rubric's 0.25s and 0.5-0.75s boundaries are numbers.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Prerequisite

You are applying the exact rubric Fellows self-check against on Sync a Video Pair. Read `../handshake-ig-temporal-alignment/SKILL.md` for the underlying task standard before auditing.

Before auditing a live submission, read `references/rubric.md`.

## The Three Decisions

Every item moves through the same flow.

1. **Read and review.** Watch both clips and the original Fellow's call. Check it against the four review checks — Connection, Matching segment, Engagement, Video check — and, if the pair was kept, press Play both. Rate the submission 1-5. Watch the whole submission before you rate it.
2. **Decide whether it is worth fixing.** Yes sends you to the editor. No records your grade and moves to the next item.
3. **Fix only if needed.** Re-anchor the start, trim a drifted tail, re-sync by audio, or correct a wrong keep/reject call, then submit.

**Grade before you edit.** Your grade reflects the submission as it arrived, not as you left it.

## Grade On Two Axes

A submission can fail on either axis. Judge both.

- **Decision accuracy — did they make the right keep/reject call?** Did the Fellow keep pairs that should have been kept and reject ones that should have been rejected? A wrongly-kept bad pair or a wrongly-rejected good pair is a decision-accuracy failure, regardless of how tight the alignment is.
- **Alignment precision — for kept pairs, how tight is the sync?** How close is the start to the shared moment, does the segment stay on the same event, and does the audio line up without echo? Loose starts, wandering tails, and doubled audio are alignment-precision failures.

## Hard Gates

- Do not redo the pair from scratch or re-source clips.
- Do not edit before grading.
- Do not invent problems to justify an edit. If the call and alignment are already right, grade it well and move on.
- Do not rewrite a prompt that is accurate but thin on an otherwise clean submission. Accurate-but-thin is the definition of a 4.
- Do not fix a pairing that would need a full re-source. That is not your job — grade it and continue.
- Do not use Skip for a bad submission. Skip is for items you genuinely cannot audit.
- Do not use Flag for a hard call. Flag is for broken data.

## Rating Scale

The same rubric Fellows self-check against, from the auditor's seat.

- **5 Exceptional** — perfect sync, no perceptible offset at the start, holds across the whole segment, same event throughout, accurate and specific prompt. **Or:** correctly rejected a genuinely bad pair. A correct reject earns full marks; no alignment needed.
- **4 Strong** — one minor flaw. Start anchored well under ~0.25s, slight drift only. Prompt accurate and clear, if not fully detailed.
- **3 Acceptable** — about 0.25s of desync (a faint echo on shared-sound pairs) and/or an adequate but thin prompt. The pair is genuinely valid and the same event; still usable.
- **2 Weak** — send back. Alignment clearly off (0.5-0.75s, obvious echo or visible lag) and/or an inaccurate prompt. **Or:** rejected a pair that could have been aligned.
- **1 Unacceptable** — unusable. No real attempt, or kept and aligned an unrelated pair. Also covers a missing or false prompt, and wrongly skipping a clearly syncable pair.

Grade accepted pairs on the final clips and prompt only. The annotator's own QA rating of the pair does not affect this score.

## Is It Worth Fixing?

**Yes, fix it when:**

- The alignment is off but fixable — re-anchor, re-trim, or re-sync by audio.
- A bad pair was wrongly kept — correct the call by rejecting it.
- The relationship-type label is wrong.
- The prompt is weak but the pairing and alignment are sound — rewrite the prompt.

**No, submit the grade and continue when:**

- It is already a clean 4-5 with nothing meaningful to improve.
- The pairing itself is wrong and would need a full re-source.
- There is a clean reject to confirm — grade it well and move on.

Either way your grade is recorded. Choosing No just keeps the submission as-is.

## Rework Action Table

| What you find | Action |
|---|---|
| Start not anchored (offset > 0.25s) | Re-anchor the start on the shared moment |
| Tail wanders onto a different action | Trim the tail back to where the shared event ends |
| Visuals don't match closely | Switch to audio blend and sync on the shared sound |
| Wrong relationship-type label | Correct the label |
| Weak but salvageable prompt | Rewrite it to name the transformation specifically |
| Genuinely bad pair kept | Reject the pair |

You use the identical alignment toolset as the original Fellow — drag the strip or edges, ‹ › nudge, Play both, Overlay (o), Audio blend (A↔B), Speed (0.25×/0.5×/1×), Skip (s), Reset (r).

## What To Look For

Re-run the same four checks from an auditor's seat. **Connection and Matching segment are make-or-break** — they decide whether the keep/reject call was right. Engagement and Video check shape the quality rating for kept pairs.

1. **Connection** — does the response correspond to this specific original, not just the same person, style, or topic? A pair that does not correspond but was kept should be rejected. A pair that does correspond but was rejected is a decision-accuracy failure.
2. **Matching segment** — is there a shared moment both clips can be anchored to, visual or audio? No shared moment means the Fellow was right to reject. A clear shared moment that was rejected means correcting the call.
3. **Engagement** — is the response worth watching? Use this to shape the quality rating on kept pairs, not to overturn a good keep/reject call.
4. **Video check / watermarks** — no third-party watermarks such as a moving TikTok logo or a tiled Shutterstock/Getty overlay. Creator @handles and in-scene brands are fine. If the Fellow kept a pair with a disqualifying watermark, reject it.

## Skip, Flag, And Neither

- **Skip** — you genuinely cannot audit the item: a clip will not load, the data is broken. Skipping records nothing and moves on.
- **Flag** — the item is bad data that should be pulled for everyone: a corrupt file, not a real submission.
- **Neither** — if the original Fellow's call and alignment are already exactly right, grade it well. Do not invent problems to justify an edit.

## Feedback Quality

Your score is only one part of the evaluation. The feedback you write is assessed for accuracy, clarity, and usefulness to the annotator. Read `../shared-references/reviewer-feedback.md` before writing, and follow the three-part pattern: what worked, what missed and where, what good would look like.

Be careful with 1s, 2s, and 5s. Both ends of the scale get the most scrutiny and must be clearly earned.

## Feedback Style

Your feedback is scored alongside your grade. Follow the three-part pattern in `../shared-references/reviewer-feedback.md`, and use this section for wording.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Open with what the annotator got right. There is almost always something, and a review that opens on the failure reads as a verdict rather than help.
- Quantify the alignment. Give the offset in seconds and say which tier that puts it in.
- Quote the rubric tier language that drove the score. That is what makes a 2 or a 5 defensible.
- Separate the two axes. Say whether the keep or reject call was wrong, whether the alignment was loose, or both.
- Write to a colleague, not about them. Judge the work, never the person.

Banned: "wrong", "fine", "bad pair", "as previously stated", "the annotator failed to", "this is unacceptable", any comment that restates the score without explaining it.

- Good: `Nice call keeping this pair, the connection is real. The start is about a second early, which is the 2 band. Dragging the response window one second later would have put both on the same beat and moved this into the 4 range.`
- Bad: `Incorrect alignment. Score 2.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the audit in the chat using this template.

```markdown
### The Submission
[The pair, the Fellow's keep/reject call, their category label, their alignment, and their prompt.]

### Decision Accuracy
[Was the keep/reject call right? Name the check — Connection or Matching segment — that settles it.]

### Alignment Precision
[For kept pairs: start offset, whether the segment stays on the same event, and what Play both sounds like.]

### Grade
[1-5, quoting the tier language that drove it.]

### Worth Fixing?
[Yes or No, and which row of the rework table applies.]

### Rework Performed
[What you changed, or "none — already correct" / "none — would need a full re-source".]

### Feedback To The Annotator
[Three-part pattern: what worked, what missed and where, what good would look like.]
```

## Final Checklist

- Did I grade before editing?
- Did I avoid redoing from scratch?
- Did I re-anchor any start offset greater than 0.25s?
- Did I trim tails that wandered onto a different event?
- Did I correct a wrong keep/reject call if I disagreed with it?
- Did I avoid padding an already-correct submission?
