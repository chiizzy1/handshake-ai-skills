# Minimum Annotation Requirements

**Definition**: Every valid annotation must meet basic submission requirements.

## ✅ Pass
1. Model response is inaccurate; rating is set to 👎.
2. VQA: at least 2 skills tagged (3+ if Enumeration is one of them), with at least one anchor skill.
3. BV: at least 1 BV taxonomy selected.
4. Response field contains text (not blank).
5. Annotation tagged as MCQ or short answer.
6. Check My Work (Verify Submission) run after the final model run.

## ❌ Fail
1. Model response is correct, so 👎 cannot be validly applied. (The prompt isn't hard enough.)
2. VQA: fewer than 2 skills tagged.
3. VQA: Enumeration prompts with fewer than 3 skills.
4. VQA: no Logical Reasoning / Table-Chart-Graph Understanding / World Knowledge tagged (missing anchor).
5. BV: no BV taxonomy selected.
6. Response field is entirely empty or null (technical glitch — save, reload, or escalate, do NOT submit blank).
7. Answer type left untagged — neither MCQ nor short answer.
8. Model regenerated after the last Check My Work (Verify Submission) run without re-running validation.

## Rules Explained

### Model Generated Answer (MGA)
The model response rating must be 👎 (Thumbs Down). If 👍 is set, the annotation is invalid — it means the prompt didn't stump the model. The Model Generated Answer box must contain a response — if it's blank due to a technical error, API timeout, or system glitch, do NOT submit. Save your work, reload the page, or escalate in the #lizard-v2-tasking Slack channel.

### Ontology (VQA)
- Every VQA prompt must challenge the model on at least **2 skills**.
- Prompts involving **Enumeration** require **3+ skills** (Enumeration is easy to apply, so we require additional complexity).
- Every VQA prompt must include at least **one anchor skill**: Logical Reasoning, Table/Chart/Graph Understanding, or World Knowledge.

### Ontology (BabyVision)
- At least **1 BabyVision taxonomy** must be selected.

### Answer Type
Every annotation must be tagged as either MCQ or short answer. An untagged annotation is invalid.

### Validation Freshness
Check My Work (Verify Submission) must be run *after* the last time the model was run. If you regenerate the model response, you must run Check My Work again before submitting.

## Knowledge Check Examples

**Q**: On a VQA annotation, you tag Spatial Reasoning and Enumeration. The model fails and you rate it 👎. Does this meet the minimum annotation requirements?
**A**: No — Enumeration requires 3+ skills, and neither Spatial Reasoning nor Enumeration is an anchor skill. You need at least one of Logical Reasoning, Table/Chart/Graph Understanding, or World Knowledge.

**Q**: The Model Generated Answer box is completely blank after a system glitch. You rate the response 👎 and submit. Is this valid?
**A**: No — the response field must contain text. Refresh, reload, or flag the issue in the appropriate Slack thread before submitting.
