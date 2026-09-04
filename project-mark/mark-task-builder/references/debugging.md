# Debugging A Task

From the FAQ. **When a task doesn't behave, the fix is almost always in the prompt
or the input files, not the rubric** — and since 8/27 you cannot edit the rubric
at all, so upstream is the only repair.

## Models keep getting the recommendation right

**The most common failure.** The task is too easy, and the fix is in the evidence,
not the rubric.

| Likely cause | Fix |
|---|---|
| The obvious first analysis is also the correct one | Build an **adversarial obvious path**, or make files support **conflicting conclusions** |
| The decisive number is stated in a summary tab or a single file | **Require the hard computation** and hide the decisive fact in an unlinked file |
| The data is clean and pre-joined | Add an **integrity landmine**, split across files and grain, and leave inputs raw |

## Two experts could defensibly disagree (non-deterministic)

A reviewer says the answer isn't the single defensible one, or the model
"optimized a different objective" and was arguably right.

**Cause:** the business objective and your ground-truth recommendation aren't
tightly aligned, or the prompt leans on a hidden assumption or an arbitrary
threshold.

**Fix:** bind the objective to exactly one recommendation. **Re-read the prompt as
an adversary optimizing a different but legitimate goal** — if that path reaches a
different answer, constrain the objective or the data until it can't. Then tighten
the determinism basis: name the explicit constraints that close off every other
conclusion.

## Right answer, wrong reasons, but it still scored high

The model lands on the recommendation through luck or a shortcut, but the rubric
gives it a passing score.

**Cause:** the rubric rewards surface features or is gameable.

> ⚠️ The FAQ's fix here — make criteria atomic and binary, strip process words
> ("calculated", "understood") and vibe words ("thorough"), add negative-weight
> penalties — **is pre-8/27 advice from when fellows edited the rubric. You no
> longer can.** The rubric is generated and fixed.
>
> The equivalent repair now is upstream: the rubric is generated from your prompt
> and golden, so make the asks harder and more discriminating so a shortcut cannot
> satisfy them. A question a model can answer with a surface lookup does not belong
> in the supplementary block.

## The top responses still score too high

Your best-scoring responses land above 70%, so the task does not pass.

**The bar:** 12 model responses. The bottom 10 can be submitted without checking;
the task passes only when the **top 2 average under 70%** against the rubric.
First check you reset the task before the rollout — populated later fields leak
the golden and rubric into the models' context and inflate the scores.

- **If the top two clear 70%:** the task isn't hard enough. Deepen the trap or the
  computation until the strongest responses miss.
- **If a top response scores high on verbosity and partial credit:** confirm the
  rubric isn't awarding points for surface features the answer shouldn't earn.

## Practical limits

| Limit | Value |
|---|---|
| Total size of all files | **under 50 MB** |
| Any single file | **under 10 MB** |
| Ship as | **a single ZIP** — keeps uploads under the limits, preserves folder structure, makes file order irrelevant |
| Acceptable licences | public domain, **CC0, CC-BY, CC-BY-SA** (attribute where required) |

Check the licence on **each individual dataset**, not just the platform — most
platforms host mixed licences. Ask a Team Lead before using anything with an open
copyright question.

**Sizing rule of thumb:** use file sizes realistic for the job you are modelling.
Avoid extremes like a 3-million-row spreadsheet or a 1,000-page PDF. Files should
be large enough to be realistic and require skimming, but still workable.

## Malformed files

**Allowed, when recoverable.** Wrong or mixed encodings, invalid JSON or XML that
a tolerant parser or forced encoding can recover, or a handful of bad rows in an
otherwise valid file — that is exactly the realistic mess wanted.

**Out of scope:** files that cannot be parsed with reasonable effort, or that need
bespoke reverse engineering with no discernible logic. **The difficulty should come
from the analysis, not from a parsing puzzle.**

## Creating your own input files

**Only as a last resort**, and only for a few supporting files alongside real
sourced data. Take inspiration from the structure of real datasets or the decision
they support, and build your own similar data. Never directly use, copy, or ship
copyrighted or non-free-use data.

If you go this route the file **must be indistinguishable from a real document
across data values, structure, and format. If a domain expert could tell it is
synthetic at a glance, the task will get rejected.**

Using an LLM to create a file is **not recommended**; same bar applies if you do.

AI **may** write scripts that inject realistic mess into real data — duplicates,
missing values, reformatted dates, encoding issues, distractor columns. The
load-bearing data must still be real.

## Troubleshooting

**Upload problems:** check each file is under 10 MB and the total under 50 MB, then
copy your prompt and files into a new task. You can skip from the top right.

**A model run exceeding 30 minutes:** edit the prompt slightly and rerun, or copy
your prompt and skip the task.
