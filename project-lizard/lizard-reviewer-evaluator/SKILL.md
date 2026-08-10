---
name: lizard-reviewer-evaluator
description: Evaluate and QC Project Lizard VQA and BabyVision annotations. Use when asked to audit or review tasks from annotators, handle LLM Judge feedback, write strong justifications, or decide if tasks should be Skipped/Unusable under the zero send-back policy.
---

# Project Lizard - Reviewer Evaluator Skill

This skill guides the quality control (QC) and auditing of Project Lizard annotations (both BabyVision and VQA). Reviewers are responsible for fixing errors, verifying answers, and evaluating LLM Judge feedback. Your edits and feedback drive quality alignment across annotators — the reviewer role is fundamentally a teaching position.

## Source Hierarchy

1. The matching official PDF in `HANDSHAKE-AI/project-lizard-pdfs/` — the highest authority. The Reviewer Playbook set covers `Reviewer Flow`, `BabyVision QC & Audit Checklist`, `VQA QC & Audit Checklist`, `How to Handle LLM Judge Feedback`, `Writing Strong Justifications`, `Reviewer Simulation`, and `Reviewer Announcements`.
2. The current task UI and any visible task-specific instructions.
3. `HANDSHAKE-AI/project-lizard-extracted/group-5-reviewer/` — a searchable extraction of the same material, and a navigation aid only. It never overrides a rendered PDF page.
4. This skill's `references/...` files.
5. The annotator-side skills, `../lizard-babyvision-evaluator/SKILL.md` and `../lizard-vqa-evaluator/SKILL.md`, when judging whether an annotation met its own spec.
6. `../shared-references/...` for cross-project common errors.
7. User memory or previous answers.

State plainly when an expected official source could not be found. Do not import TELUS, Outlier, or Project Hedgehog rules into a Lizard task.

## Core Operational Mandates

### 🚨 Zero Send-back Policy
We operate on a strict single-review cycle.
- **Fix issues directly**: Do NOT use "thumbs-down" or return tasks to annotators. Make any and all necessary edits to pass an annotation in a single review session.
- **Individual unsalvageable work**: If a single annotation would take more than 10 minutes to correct, rewrite it entirely rather than deleting it. Do not add net-new annotations.
- **When NO annotations are saveable**: If none of the annotations on a task can be salvaged: move the task to Unusable if the image is not very annotatable, or contact a DOL to reassign it if the image is still workable.

### 🔄 Skip vs. Unusable Workflows
- **Only annotators can skip an image.** Reviewers cannot skip a task with the QualityCheck status.
- **Image is usable → route to Skipped**: If the image is annotatable but the annotator passed on it, delete any existing annotations and move the task to Skipped so a lead can reassign it.
- **Image is not usable → route to Unusable**: Apply only when the image itself is completely unclear, broken, or unworkable. Delete existing annotations first.
- **Critical action**: Delete any existing annotations before routing to Skipped or Unusable. These routings are heavily monitored; when in doubt, contact a DOL.
- **No more Hold**: Never move an annotator-skipped task to Hold under any circumstance.
- **SQS 1 is retired**: Use SQS 2 for unusable tasks.

### ⏱️ Shadow Task Logging (Handshake Only)
"Shadow Tasks" refer strictly to your time-tracking logs on Handshake — **never log these on Hubstaff or SuperAnnotate**.
- **Annotator-skipped images**: Log exactly **1 Shadow Task per image** (regardless of whether you route it to Skipped or Unusable).
- **Standard QC reviews**: Log **1 Shadow Task per individual annotation** (i.e., per question on the image), not just one for the overall image.

### ✅ Double-check the Rewrite Answer Before Submitting
Rewrite answer correctness is one of the top audit failure modes.
1. **Work the prompt first**: Solve the prompt from the image *before* looking at the annotator's Rewrite Answer, so you don't anchor to their value.
2. **Then compare**: Confirm the Rewrite Answer matches what you derived — value, format, units, rounding, and (for MCQs) the bare letter with no extra text.
3. **Fix, don't flag**: If the Rewrite Answer is wrong, correct it directly in the same review session — send-backs are not an option.

### 🔄 Prompt Edits & Model Regeneration
If you modify an annotator's prompt, you **must** trigger a model regeneration immediately.
- **Verify consistency**: Always ensure the new model answer is generated from the absolute latest version of your edited prompt.
- **Iterative testing**: After revising a prompt, the model may answer correctly — try regenerating multiple times if needed.
- **Enforce failure**: If the model correctly answers the prompt, continue editing and tightening the prompt further until the model fails.

### 🛡️ LLM Usage Reports
If you suspect an annotation is AI-generated, review it as normal — then fill out the LLM Usage Report Form to flag it. Do not skip, reject, or send back the task on suspicion alone.

### ⚖️ Handling Audit II Returns
Any task with a purple status (`Returned_to_QC`) indicates that Audit disagreed with a previous decision.
- **Absolute ownership**: Do not send the task back to the annotator. Make any and all edits needed to address the audit feedback yourself.
- **Feedback protocol**: Paste the Audit II feedback verbatim into both the SuperAnnotate QC feedback box and your QC feedback section on Handshake.
- **Chronological logging**: Include a date and review-cycle number in brackets — e.g., `[1/15 (2)]` — for all entries, ordered chronologically.
- **Escalations**: If you fundamentally disagree with an Audit decision, reach out to Kaz or a DOL directly for a formal review.
- **Rebuttals**: To dispute feedback, scroll down in SuperAnnotate and find the "Rebuttal Tracking" box. Click the Yes circle. Type your reasoning in the text box that appears and submit. Do NOT use the old Audit II rebuttal form (retired).

## Reviewer Flow

Work through each step in order when reviewing an annotation:

1. **Review the Image**: Confirm it is clear and usable. Check skip criteria.
2. **Check the Model Response**: Confirm rating is 👎, response box is non-empty, and model answer is incorrect.
3. **Check the Question & Note Common Errors**: Review the question using the QC checklists. Record findings in individual QC boxes for each annotation.
4. **Evaluate the LLM Judge Verdicts**: For each category verdict, verify the Judge's pass/fail is accurate and reasoning is sound. 👍 or 👎 on every row — all must be annotated before submitting. See [LLM Judge Feedback](references/llm-judge-feedback.md) for the full decision table, feedback scenarios, and worked examples.
5. **Provide Feedback on the Judge's Verdicts**: Notes are required when you disagree. State why and how the Judge is wrong. When agreeing with a correct fail that has flawed reasoning, still agree and explain the flaw.
6. **Provide Your Final Verdict**: Approve/Disapprove in the overall feedback box. This is the **ground truth** — independent of the LLM Judge's feedback. If you notice issues with the Judge's Overall Feedback summarization (e.g., self-correction), note it here too.
7. **Update or Approve the Annotation**: Make corrections directly. No send-backs.
8. **Stress-test the Model (Up to 5 Runs)**: Only run the model if you changed something. No edits = no runs. If the model answers correctly on all runs, revise until it fails.
9. **Report Findings**: Document in both Handshake Shadow Task and SuperAnnotate QC box. Keep entries consistent. Include the original prompt, the revised prompt, the error mode, and the reason for the change. This feedback is crucial — annotators cannot improve without seeing exactly what they did wrong and how it was fixed.

## Writing Strong Justifications

Every Shadow Task needs a justification. Weak justifications are the main reason we lose Audit II rebuttals. A clear, specific justification is your evidence when a decision is challenged.

A strong justification does three things:
1. **Names the error mode** — use the exact category (e.g., "Question Unclear", "Giveaways", "Image un-annotatable"), not a vague word like "wrong."
2. **Points to the specific problem** — quote or locate the part of the prompt, answer, or image that fails.
3. **Explains why it fails the rubric** — tie it to the standard, and note any edit you made.

### Template
```
[Original Prompt]
Feedback:
[Error type]: [what is wrong] in [where]. I [edit made] so it now [meets which criterion].
[Revised Prompt]
```

### Example — Good vs. Bad
**Good**: "Question Unclear: The prompt chained two operations without telling the model what single value to output. I reworded it to ask for one final answer (the industry name) so the target is unambiguous."

**Bad**: "unclear, fixed it"

Both describe the same edit — but only the strong version names the error mode, points to the specific failure, and ties it to the rubric.

### Un-annotatable Template
```
Un-annotatable: Image un-annotatable — [why, e.g. diffuse overlapping color 
with no clear quadrant], so no reliable answer exists from the image. 
Skipped; logged a single Shadow Task at SQS 2.
```

## References
- See [references/babyvision-qc-checklist.md](references/babyvision-qc-checklist.md) for the BV audit spec.
- See [references/vqa-qc-checklist.md](references/vqa-qc-checklist.md) for the VQA audit spec.
- See [references/llm-judge-feedback.md](references/llm-judge-feedback.md) for the full LLM Judge handling guide.
- See [references/sqs-scoring.md](references/sqs-scoring.md) for the SQS score rubric and logging rules.
- See `../shared-references/` for full Common Errors definitions and worked examples.
