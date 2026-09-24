# Reviewer (R1) Workflow

A different job from annotating. You are **R1** — the last line of defence before
work goes up the pipeline. You fix and approve other people's tasks.

Sources: the Reviewer Vault, and the reviewer onboarding session
(`HANDSHAKE-AI/project-gaffer/reviewer_onboarding/transcript.md`). Where the
onboarding gives a presenter's personal workflow rather than a rule, it is marked
**suggested**.

## Contents

- [Where You Sit](#where-you-sit)
- [Which Reviewer Task Is This?](#which-reviewer-task-is-this)
- [Mini_R1 — The 1-Minute Review](#mini_r1--the-1-minute-review)
- [Your Score](#your-score)
- [The Clock](#the-clock)
- [The Workflow, In Order](#the-workflow-in-order)
- [The 45-Minute Decision](#the-45-minute-decision)
- [Thumbs Up, Save, and Feedback](#thumbs-up-save-and-feedback)
- [The 10 Criteria](#the-10-criteria)
- [SQS — Grading the Annotator](#sqs--grading-the-annotator)
- [Proportionality](#proportionality)
- [Run the Autochecker Twice](#run-the-autochecker-twice)
- [Tasks Sent Back to You](#tasks-sent-back-to-you)
- [When a Reviewer Gets a Full Annotation](#when-a-reviewer-gets-a-full-annotation)
- [Pages Not Yet Captured](#pages-not-yet-captured)

## Where You Sit

```text
R1 (you) → AutoChecker → R2 → approved
                                 ↘ ~20% pulled for external audit
   ↖ failures at any stage come back to you
```

You were promoted past the annotator step. **R2 is the level above you**, and
they promote good reviewers into it.

An **annotation** is one segment with a numbered ID, consisting of two captions.

> "You guys are the last line of defence… we want you to be the last ones to
> touch these annotations before we send them up the pipeline."

## Which Reviewer Task Is This?

The tag on the task you claimed decides the job, the routing and the shadow
tasks.

| Tag | Job | Send to | Shadow tasks |
|---|---|---|---|
| `R1` | Review a full task | **Hold**, or **QC_Return** if sending back | One |
| `Mini_R1` | **1-minute review** — sample 10 annotations | **Hold**, or **QC_Return** only in the case below | One |
| `Reviewer_Annotation_2_Shadow_Tasks_Approved` | **You annotate the whole task yourself** | **Hold** — or **Skipped** if the video is a valid skip | **Two** (none if skipped) |

Flags always stay as **whatever the task came with**.

When you are annotating a `Reviewer_Annotation` task yourself, **the annotator
rules apply** — including the skip and flag criteria in
`../references/skip-flag-routing.md`.

### The one unpaid return

If the **Autochecker** bounces a task back after you submitted it to Hold, that
is the **only unpaid return**. Do **not** open a new shadow task for it — just
fix and resubmit. Leftover time can be logged on your existing shadow task.

## Mini_R1 — The 1-Minute Review

A different procedure from a full review. You are sampling, not fixing
everything.

**Sample 10 annotations: the first 5 of the Speech track and the first 5 of the
Audio+Visual track, in order from the top.** If a track has fewer than 5, just
check what is there — a 9-annotation task means you check 9.

**10 minutes maximum. About one minute per annotation. Stop at the fourth FAIL.**

> ### The grading standard
> **Not on the card = not a FAIL. Unsure = not a FAIL.**
> Anything catchable mechanically is the Autochecker's job, not yours. You are
> checking two things only: **accuracy** and **missing detail**.

Grade each sampled annotation against the 10 criteria below, then log in the
shadow task the count of failed annotations — **0, 1, 2, 3, or 4+** — followed by
the error types.

**Routing is decided by one question**, and only one branch goes back:

| What you found | Send to |
|---|---|
| 0–3 failing annotations | **Hold** |
| 4+ failing, **but** a 1-minute task (both tracks) could be reviewed, fixed and submitted within 30 minutes | **Hold** — select "4+ yet the 1-min task COULD be reviewed+fixed within 30 min" |
| 4+ failing **and** it could **not** be done in 30 minutes | **QC_Return** |

Everything other than that last row goes to Hold.

## Your Score

Roughly **20% of what you send to Hold gets audited**.

| Score | Consequence |
|---|---|
| 95% | The target |
| 90% | The threshold — what keeps the client happy |
| Below 90% | Risk of **demotion** |
| Well below | Risk of **offboarding** |

Habitually pushing bad work to Hold gets noticed, because those submissions are
sampled and reviewed.

## The Clock

The time rules drive almost every decision you make, so learn them first.

| Situation | Time you get |
|---|---|
| Normal review | **Half** what an annotator gets for that video length |
| You decide within the first **45 minutes** | — |
| Sent back, then returned to you | **90 minutes flat**, whatever the video length |
| Returned from R2 or Audit | **20 minutes** |
| Holding a claimed task | ~**48 hours** before it is taken back |

Two consequences worth internalising:

- **A task can be sent back once, maximum.** The second time you hold it, you
  cannot send it back again — and you have 90 minutes regardless of whether it is
  a 2-minute or a 10-minute video.
- **Fixing it yourself gives you more time and more credit.** Your clock scales
  with video length; the 90-minute return clock does not.

The current limit is announced in **Slack** and applies to tasks claimed after
the announcement. It **does not reset** when the AutoChecker rejects a task; it
**does reset** when R2 returns it with comments.

## The Workflow, In Order

1. Request the reviewer task in **SuperAnnotate**.
2. Start your **shadow task** on the Handshake platform. It is a timer, not real
   tasking. The sequence is: **Start timer** → paste the **`.json` ID** from the
   top-left of your SuperAnnotate task → *"Annotating or reviewing a full task"*
   → role **Reviewer** → the **length of your video**. Only then does the timer
   show your real allowance.

   The black arrow may read "submit" at intermediate steps — that is not
   submitting the task. The real submit button is larger and centred.

   **You may exceed the allotted time without consequence, but you are only paid
   for the time the timer generated.**
3. Run the **Autochecker** before you start analysing.
4. Spend up to **45 minutes** deciding: fix it yourself, or send it back.
5. Fix the task.
6. Document errors and the **SQS** in the shadow task.
7. **Thumbs up every track**, plus the overall feedback box.
8. Run the **Autochecker again**.
9. Submit in **SuperAnnotate first**, then the shadow task on Handshake.

**Suggested:** start your fixing in the **Audio+Visual** tracks and leave Speech
until the end. The transcription arrives largely pre-populated — the work there
is speech characteristics and verifying verbatim accuracy. The visual element
carries the brunt.

## The 45-Minute Decision

Inside the first 45 minutes, skim both tracks and answer one question:

> **Is this a reasonable annotation?** Not perfect — reasonable. Accurate, and
> somewhat complete.

Then choose. **Default to fixing it yourself**, within reason. Send back only
when quality makes revision impossible in the time you have.

Decide this **quickly**. Discovering at minute 80 that the task is unsalvageable
is the worst outcome available.

## Thumbs Up, Save, and Feedback

**Every track needs a thumbs up and a save.** Miss either and the task will not
pass the Reviewer AutoChecker. This includes the **general QC feedback box** at
the bottom — the one that does not move — which needs its own thumbs up.

Checking your work:

- The **QC column** shows `1` for thumbs up, `0` for thumbs down, blank for
  neither. All 1s means you are done.
- The **Verify Submission** button checks thumbs-ups **only**. It is *not* the
  Autochecker. Pressing it does not mean you have run the Autochecker.

Feedback rules differ by destination, and this is the part people get wrong:

| Destination | Thumbs | Feedback |
|---|---|---|
| **Hold** | Thumbs **up** every track | **Leave every feedback field clear.** Do not leave feedback |
| **Back to annotator** | Thumbs up good tracks, thumbs down bad ones | Leave feedback — **suggested:** put it all in the general box rather than per-track |

Feedback is never punished by omission, but it is worth giving on a return so
whoever picks the task up next knows why.

## The 10 Criteria

Each one fails the annotation. Anything mechanical is already caught by the
Autochecker — **your attention belongs on content that is wrong or missing**.

> **Not on this card = not a FAIL. Unsure = not a FAIL.** This is the consistency
> rule the project states outright. Do not invent criteria, and do not fail an
> annotation you are uncertain about.

### I. Incorrect

| # | What | Track |
|---|---|---|
| 1 | Words that weren't said / incorrect verbatim transcription | Speech Transcription |
| 2 | Wrong sound, wrong visual description — **especially on-screen text** — or wrong speech characteristic | Video, Audio, Speech Characteristics |
| 3 | Wrong speaker, or different voices not given different numbers | Speech Transcription, Speech Characteristics |
| 4 | A timestamp in the caption is wrong, or speech/visual/audio cut off at segment edges | any |

One "they're"/"they are" swap is not a fail; the same slip **as a pattern** is.
Rounding on timestamps is fine.

### II. Missing

| # | What | Track |
|---|---|---|
| 5 | A word was not transcribed | Speech Transcription |
| 6 | **Sound — missing music or ambient noise, especially continuing while people talk** | Audio |
| 7 | Camera cut, screen change, or replay | Video |
| 8 | Any overlay or on-screen text, **including when it changes** | Video |
| 9 | A clear main figure or object, with at least one mention of what they are doing | Video |
| 10 | Speech characteristics too generic to mean anything | Speech Characteristics |

**Criterion 6 is the single most common miss on the project.** One stray missing
"um" is not a fail; dropped words or many dropped fillers are. On criterion 9, a
description too vague to picture counts as missing.

Also verify, before submitting: **every event has a timestamp, and every speaker
is labelled.**

## SQS — Grading the Annotator

A 1–5 score, entered in the **shadow task**. There is no field for it in
SuperAnnotate.

| SQS | Meaning | Effect on the annotator |
|---|---|---|
| **1** | **LLM usage**, or annotation so poor it is unusable — e.g. a data-rich segment summarised in one or two sentences while on-screen text, main characters and scene changes go unmentioned | **Immediate offboarding** |
| **2** | Slightly better than a 1 | **Multiple 2s risk removal** |
| **3** | Borderline. Still pretty bad work — this is the hard call | — |
| **4** | Pretty good, minor errors. Usually fix these yourself | — |
| **5** | Near perfect. You are effectively recommending them as a reviewer | — |

**LLM usage is strictly prohibited and is the one place the project tells you
exactly what to score.** Hallucinations are the tell: things described in
Caption 1 that never appear in the video, and things in the video that never
appear in the caption. If you see it, **give a 1 and send it back**.

The shadow task also asks separately how confident you are that LLM was used,
on a scale from near-certain-yes to near-certain-no. That is for population
records; answer it honestly.

**Think about the consequence before scoring.** If you send back genuinely bad
work with a score that leaves the annotator on the project, they may do nothing
with it — and it returns to you, with 90 minutes on the clock regardless of
length.

## Proportionality

The scores are subjective above 1, and the project is explicit about the mindset:

> "Your goal isn't to just fail people for minor things… The perspective I'd say
> you should take is: what is fixable in the time that I have?"

A worked example from the onboarding: a video with 100+ tracks across both
tracks, of which five have problems and one or two are significant. **That is not
a bad annotation.** The rest being good is what matters.

Reviewing is not a hunt for failures. It is a judgement about what can be
finished.

## Run the Autochecker Twice

Once **before** your 45-minute analysis, once **immediately before** submitting
to Hold.

Results **batch roughly every 10 minutes**, and the page shows a "refreshed as
of" time. If you finish at 11:29 and the page says 11:30, that run does not
include your edits. Wait until the stamp advances — then read it.

**Suggested:** check once more after that, to be sure nothing slipped.

Submitting to Hold without a clean Autochecker run risks the task bouncing
straight back to you.

## Tasks Sent Back to You

### From R2

- Comments come from **a small sample** and may not list every error.
- **Review every annotation and correct the whole task**, not only the rows
  mentioned.
- Resubmissions may be checked against a **different** sample.
- You get **20 minutes**, claimed via a shadow task.

### From Audit

- Start a **new shadow task** — do not reclaim an old one — and select the
  **20-minute revision** option.
- Correct **only the annotation-ID rows the auditor flagged**.
- Save using **both Save controls**, then submit to **Completed_Passed_Audit**.
- No comment needed unless you are sending it back.
- Disagree with the decision? Use the **Audit Dispute Form**, not a return.

Note the asymmetry: **R2 return → re-review everything. Audit return → fix only
what was flagged.**

### A task that is already upvoted

- **Never reviewed it before?** Ignore the existing upvotes and review the whole
  task fresh.
- **Reviewed it before?** It came back from R2 — follow the R2 path and pick the
  matching returned-task option in the shadow task.

## When a Reviewer Gets a Full Annotation

Reviewers are sometimes assigned full annotations. The task tag tells you which:

| Tag | Job |
|---|---|
| `R1` | Complete a **review** |
| `reviewer annotation to shadow task approved` | Complete a **full annotation** |

Because a reviewer's clock is half an annotator's, a full annotation gets **two
shadow tasks** to make up the difference. The order matters:

1. **Complete the whole annotation in SuperAnnotate first** — even if it runs
   past the time the first shadow task allotted.
2. Submit it to Hold, then submit shadow task **one**.
3. Open shadow task **two**, run through the same selections, and use **Edit
   Time** to claim the remaining time.

Worked example from the onboarding: a 2–3 minute video allots 1h15m per shadow
task. If the annotation actually took 2h30m, shadow task one pays 1h15m and you
edit shadow task two to 1h15m — 2h30m total.

**Do not end the first shadow task early to bank it.** If life intervenes and you
miss the 48-hour window, you have claimed half the work and lost the task.

## Pages Not Yet Captured

Captured: the Vault, Reviewers — Where to Send Tasks, Reviewing Qualification
Tasks, the Shadow Task slide decks, and the reviewer onboarding session.

Still missing:

- **Reviewer Instructions**
- **Reviewer Focus Areas**
- The three request forms — Task Request, Audit Dispute, Task Removal — which are
  collapsed in the captured HTML
- The **Reviewer AutoChecker**'s own checks, beyond the thumbs-up requirement

The vault itself is password-protected; the password is in Slack under the
important-documents dropdown.

Extract these before treating this file as complete, and say plainly that they
were unavailable if a question turns on them.
