# Skip, Flag, and Where to Send the Task

Decide this **before** you start annotating. A skip decision made halfway through
wastes the work, and a wrong skip has consequences.

## Contents

- [The One-Line Rule](#the-one-line-rule)
- [When to Skip](#when-to-skip)
- [When to Flag Instead of Skipping](#when-to-flag-instead-of-skipping)
- [What Is Not a Skip](#what-is-not-a-skip)
- [Where to Send the Task](#where-to-send-the-task)
- [The Autochecker](#the-autochecker)
- [Shadow Tasks](#shadow-tasks)
- [Finding the Right Project](#finding-the-right-project)

## The One-Line Rule

> Whole video unworkable → skip with the right flag, no annotation.
> Part of the video unworkable → **Partially Un-annotatable** flag, and annotate
> the rest.

## When to Skip

Four criteria. If one applies, flag the video and do not annotate it.

**1. Toxic content.** Hate speech, graphic violence, **visible blood**, or other
harmful content. Flag as **"Toxic Content"** and skip.

The blood rule is absolute and was added as an update: flag as Toxic Content
**and** skip every task that has visible blood — *even if it is in a video game
or a sport.*

**2. Unintelligible audio.** The majority of speech is non-English, or the video
is only music with no describable events. Flag as **"Un-annotatable"** and skip.

A short non-English passage is **not** a skip. That is `((Non-English speech))`
with a speaker tag, business as usual.

**3. Data-sparse tracks.** If one track has plenty of material and the other has
almost nothing, that is a skip. The project's own example: a still image of a
graph with a voiceover explaining it in detail is plenty for the Speech track and
nothing for the Visual track. If all channels are not equally rich in data, flag
as **"Un-annotatable"** and skip.

**4. Videos longer than 10 minutes.** Excessive length is a skip on its own.

Two things to hold on to:

- **Skipped tasks are unpaid**, at every role. Skip only when the video truly
  qualifies, never to get past a hard one.
- **Skipping for incorrect reasons results in offboarding.** There is no skipping
  because a video is difficult.

Reviewers cannot change flags, so the flag has to be right when you set it.

## When to Flag Instead of Skipping

Use **Partially Un-annotatable** when the problem covers only part of an
otherwise workable video. Set the flag, then annotate normally.

**A stray swear word, a derogatory term, or a short stretch of explicit speech or
content.** That is what this flag is for. It does not make the video a skip.

- The flag applies to the **task as a whole**. You cannot flag one word or one
  segment.
- In the transcription, an ordinary swear word is written **exactly as spoken**,
  like any other word.
- **Hateful slurs are the exception — do not write those out.** The Autochecker
  runs a "Hateful/offensive language" check on captions, and auditors mark such
  tasks "partially un-annotatable due to derogatory term".

**Artistic nudity.** Flag as Partially Un-annotatable, because the content is not
pervasive, and annotate the rest as normal.

## What Is Not a Skip

- **The video will not play, or the task is broken.** Do not skip for this. It is
  stated explicitly in the guidance.
- **The video is hard, long to annotate, or boring.**
- **A short non-English passage.**
- **One swear word.**
- **Fast cuts, many speakers, or dense on-screen text.** That is the job.

## Where to Send the Task

Where a task goes depends on which task you are holding.

| Who | Task tag | Situation | Send to | Flags |
|---|---|---|---|---|
| 1-minute qualifying task | `Mini_Annotator` | Did the first minute, finished | **Annotator_Skip** | None, unless a stray swear word or isolated explicit moment → Partially Un-annotatable |
| 1-minute qualifying task | `Mini_Annotator` | The video genuinely needs skipping (unpaid) | **Annotator_Skip** | Toxic Content and/or Un-annotatable |
| 1-minute qualifying task | — | Autochecker sent it back | Fix every error, then **Annotator_Skip** again | — |
| Full annotator | `Precheck` | Annotated the whole video, Autochecker shows zero errors | **Submit_to_QC** | None, unless a stray swear word or isolated explicit moment → Partially Un-annotatable |
| Full annotator | `Precheck` | Genuinely skipping (unpaid) | **Annotator_Skip** | Toxic Content and/or Un-annotatable |
| Full annotator | — | Autochecker sent it back | Fix every error, then **Submit_to_QC** again | — |

### On the qualifying task, Annotator_Skip is the submit button

Sending the 1-minute qualifying task to **Annotator_Skip** does **not** mean you
skipped it. That is the normal way it is turned in.

What marks a real skip there is the **flags**. A qualifying task sent with Toxic
Content or Un-annotatable was skipped. One sent with no flags was submitted.

### The 1-minute qualifying task

Everyone except reviewers must start with one. If you have never done one, that is
your first task.

Two ways to tell you are holding one:

- The tag has **"Mini"** in the name.
- After annotating **only the first minute** of the video, the Autochecker will
  allow submitting — no matter how long the video is.

On a `Mini_Completed` task you may notice the first part is already partly done.
Do the whole task anyway; it is your own now.

## The Autochecker

**Zero errors before Submit_to_QC. Every time.**

Submitting a task that has not passed the Autochecker with zero errors means
being unable to complete future tasks until it is resolved. Check first, submit
second.

If a task comes back marked "Autochecker Rejected - No additional shadow task
allowed", you fix it without claiming another shadow task.

**What it does and does not do.** The Autochecker catches formatting and coverage
mechanics — timestamps, tags, gaps, banned language. It **cannot tell whether
what you wrote is true.** Human reviewers check for missing or incorrect content
afterwards. Passing the Autochecker does not mean the task passes.

Every task in `../references/common-errors.md` passed the Autochecker and then
scored 0% on human audit.

## Shadow Tasks

**No shadow tasks are allowed for skipped tasks.**

If the Autochecker sends your task back, the fix is part of the original task —
there is no extra shadow task for it.

## Finding the Right Project

New client tasks live in the SuperAnnotate project:

> ✅ **Video Omni Caption 2026 Phase 3 - Handshake**

If you see "no tasks available", check you are not still in:

> ❌ Video Omni Caption 2026 v2 - Handshake

which is the wrong project folder.

An empty task screen does not mean access was lost. Batches run out and refill,
and new drops are announced in Slack.

## When Something Is Not Covered Here

Ask in Slack or at office hours. The project's own instruction is blunt about it:

> Do not make assumptions that could compromise data quality!
