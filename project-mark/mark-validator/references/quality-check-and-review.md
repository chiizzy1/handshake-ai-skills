> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Quality Checks, Review, and Payment

From the FAQ. **The in-task Quality Check is a platform feature the handbook never
mentions.**

## The Quality Check scripts

> "We have developed a couple of quality check scripts that will scour everything
> as a helpful check that can be run to see where there is weakness in your task
> and suggestions for edits that you can make."

Offered specifically as the answer to *"how do I make sure I am not leaking the
answer to the model in my prompt or through my input files?"* — so run them when
the models keep solving your task.

### What blocks, and what does not

> **The only block on submitting is when the Quality Check indicates there is no
> stump in the task.** For every other Quality Check there is an option to
> **disagree and provide a rationale**.

If you believe a checker error is keeping a good task from being submitted,
message the project lead or a specialist with a **detailed** critique: where the
check is in error and why, involving the analytic rationales and assumptions, and
how your analysis and assumptions need to hold true for the task to be completed.

> **One important caveat on assumptions:** yours should be something **other
> analysts would also assume to be true** — not something you are subjectively
> applying to "trick" the model into the wrong answer, or to reach the right answer
> by an incorrect method.

### The Quality Check is not the reviewer

> The in-task Quality Check is **a preliminary check; the reviewer is the final
> judge.** Use it for small edits and to confirm you are aligning the prompt to the
> aim of the project — **not as the determination of a high-quality task.**

It does **not** see everything in the task, notably **the model responses and the
analysis report**. The reviewer sees the full task and every model response, and
makes the final call on a high-quality task versus one that merely aligns with the
project's aim.

That is why a task can pass every Quality Check, get a stump, and still come back
for edits.

## The two verdicts

| Verdict | Meaning |
|---|---|
| **prelim_verdict** | Your task is deterministic, had a correct solution, and passed the preliminary difficulty and duplicate checks. **"It is 98% there."** |
| **final_verdict** | A more comprehensive review confirming it meets the desired difficulty and is not a duplicate |

- **98% of tasks that pass prelim also pass final**, so this should not be a major concern.
- **A "prelim approved" status can therefore change.** That is the review process working, not a bug.
- Once registered **"Approved and Paid"** in final_verdict, the amount appears in the Payments dashboard.
- **"Do not try to create super templated or duplicate tasks. It will be caught at this point."**
- Some tasks previously failed final_verdict and **were still paid out — not clawed back — but future tasks must pass this threshold.**

## Tracking

| Situation | What it means |
|---|---|
| Task not on the review tracker | Not yet fully reviewed. **Allow 1–2 days** to be logged |
| **"unknown stage"** on the platform | Either submitted and not yet selected for review, or approved but not yet updated to show the payout. Check the review tracker |
| Incentives missing from **Awaiting Payment** | Expected. Awaiting Payment **only tracks work completed and does not reflect bonuses.** Incentives are paid with the weekly payment and appear under **"Payments Processed"** |

## Throttling

> "You are throttled for your first few tasks... Once you have your **first three
> or so tasks approved**, you will be unthrottled and will be allowed to submit
> multiple tasks."

Consistent with the handbook's New Attempter → Semi-Trusted → Trusted ladder.

## When the model keeps solving it

The FAQ's procedure, which complements the environment-view method:

1. Open the **analysis report** in the **"Environment"** view — click the link at
   the **bottom left of the dialog box for the model**.
2. Review **what files the model is using** and **the method of analysis** it
   performed.
3. Consider what you could fit into the prompt or the datasets to lead the model
   into an incorrect answer.
4. **Check whether a file in the input folder carries the answer to the model. If
   such a file exists, eliminate it from the inputs.**
5. Re-read the prompt **not as the author but as a reviewer**, asking:
   - *"What is being asked?"*
   - *"Am I being directed to an answer?"*
   - *"Am I being directed to an analytical process?"*
6. If you are unsure what is being asked, edit that part of the prompt. If you are
   being directed toward a specific analysis or answer, edit the prompt.

Step 4 is the one people miss — **a single file can be handing the model the
answer**, and removing it is faster than deepening the trap.
