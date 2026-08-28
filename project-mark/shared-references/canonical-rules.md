# Project Mark — Canonical Rules

One rule table for the whole project. Where the handbook contradicts itself, this
file decides, and says why.

## Source hierarchy

When two sources disagree, the higher one wins.

1. **The live Handshake platform** for the task in front of you.
2. **The 8/27 update** (`/827-updates`) and the **Task walkthrough**. These are the
   current spec and they superseded 8/18 wholesale.
3. **Readiness** and the **Reviewer reference**, for anything 8/27 does not touch.
4. The individual handbook pages.
5. This skill, then user preference.

## What 8/27 changed

The 8/27 update rewrote the task shape again, one week after 8/18. Anything
written against 8/18 is now stale, and that includes most of the handbook.

| Rule | 8/18 | **8/27 — current** |
|---|---|---|
| Deliverables | 2 or more | **3 or more, no upper limit** |
| Format families | 2+, your choice | **Two families are assigned to you per task.** Your deliverables must span those two; more is allowed |
| Asks per file | 2 or more | **3 or more** |
| Rubric | Generated, you review once | **Generated, you do NOT edit it.** Must reach **25+ criteria** or the task cannot advance |
| Rubric weights | Rec 50 / supporting 50 / file compliance 2–5pp | **~30% recommendation + critical components** (split across 3+ criteria, none over 20%) · **5–10% instruction-following** · **~60% supplementary questions and asks** |
| The bar | Stump: 2 of R1–4 under 50%, 1 of R5–8 under 30% | **"Stump the model" is retired.** Only the **top two** responses are graded; the rest are submitted unchecked, and the task passes when those two **average under 50%**. Response count disputed in-source — see below |
| Workflow | 9 steps | **12 steps, 3 phases, 4 hard gates** |

Unchanged by 8/27: the input package bar, the six domains, the six objectives,
honest-data traps, and $800 flat per approved task.

### Stale numbers still in the handbook

Every one of these is wrong on a page that is still live.

| Rule | Stale, and where | Canonical |
|---|---|---|
| Input file count | "6 or more" — Program details; "six-file bar" twice — Starter data kits | **10 or more, single ZIP** |
| Deliverables | "exactly one output file" — Overview, Platform walkthrough step 5; "2 to 5" — Task types, Writing the prompt; "two or more" — 8/18 card | **3 or more, no upper limit** |
| Asks per file | "3 to 5 standalone supplementary questions" — Overview, Rubric review; "at least two asks" — 8/18 | **3 or more per named file** |
| Rubric | "you complete one review pass" — Rubric review | **You do not edit it at all** |
| Rubric weights | "recommendation exactly 50%" — Rubric review | **~30 / 5–10 / ~60** |
| Scoring | "at least 2 of R1–4 below 50% and 1 of R5–8 below 30%" — Validate, Program details, Reviewer reference | **Top two average under 50%** |
| Domain count | "seven in-scope domains" — Program details | **Six** |
| Pay | "$750 first, $600 after" — pre-8/18 assessment | **$800 flat** |

### The four hard gates

Clear all four and the task is ready to submit.

| # | Gate |
|---|---|
| 01 | **Rubric reaches 25+ criteria**, weighted 30 / 5–10 / 60. The task cannot advance below 25 |
| 02 | **Top 2 model responses average under 50%.** Run 12, submit the bottom 10 unchecked |
| 03 | **A deterministic, fair stump.** Models fail for analytical and methodological reasons on honest data, never a planted defect, and ten experts working the files land on the same recommendation |
| 04 | **3+ deliverables with 3+ asks each**, across the two assigned format families |

## Input package

| Requirement | Bar | Blocking |
|---|---|---|
| Total files | 10 or more, shipped as a **single ZIP** | Yes |
| Total size | Under **50 MB** across all files | Yes |
| Single file size | Under **10 MB** | Yes |
| Licences | Public domain, **CC0, CC-BY, CC-BY-SA**. Check each dataset, not just the platform | Yes |
| Independently necessary | 4 or more — remove any one and the answer is unreachable | Yes |
| Substantial files | 2 or more — long, dense, real work to read | Yes |
| Distinct formats | 3 or more | Yes |
| Largest table | 10,000+ rows, so eyeballing fails | Yes |
| Joins | The recommendation requires joining at least two tables | Yes |
| Provenance | Source URL, pull date, and licence recorded per file | Yes |
| LLM-generated PDF / DOCX / PPTX | None | Yes |

Distractor files are allowed and encouraged. They never count toward the four
independently necessary files.

AI may locate data and write transformation scripts. AI may never create the
empirical source evidence. Scenario documents you write yourself are allowed, and
must carry explicit provenance saying what they are and how they were produced.

## Prompt contract

- **One deterministic recommendation.** One committed call, one defensible answer.
  No hedge, no blend, no "it depends".
- **3 or more named deliverables**, each with a filename and extension. **No upper
  limit.**
- **Spanning the two format families assigned to you** for that task. More families
  are allowed; the two assigned are mandatory.
- **At least three asks per deliverable** — a supplementary question with a
  determinate answer, or a concrete requirement about what that file must contain.
- **Every numeric ask states its unit and rounding.**

The four families: **Data** (CSV, TSV, JSON, XLSX, Parquet) · **Visual** (PPTX,
PNG, SVG, HTML, JPG) · **Text** (PDF, DOCX) · **Code** (PY, IPYNB, SQL, R). The
formats are examples; two of the four are assigned per task.

An ask stays valid only while it lives in the same data universe as the
recommendation. An ask that pulls in a separate dataset or a separate decision is
a second task.

**Asks must be hard and discriminating, not trivial lookups.** They carry ~60% of
the rubric, and a wrong analytical path should get them wrong.

## Golden deliverables

- Types, filenames, and count match the prompt exactly.
- **One set of numbers across all files.** A reviewer diffs them against each
  other. Disagreeing numbers across files is the single most common defect.
- Nothing extra: no unrequested answers, no AI disclaimers, no placeholders, no
  files the prompt did not ask for.
- Every number traces to a shipped input file.

## The rubric

**Generated internally from three things you already produced: the prompt
contract, the golden solution, and the requested output files. You do not write it
and you do not edit it. It arrives fixed.**

There is no review pass anymore. If the rubric looks wrong, **the fix is
upstream** — correct the prompt contract or the golden output, and the rubric is
regenerated from the corrected pieces.

Your job is to build a prompt, a golden, and an evidence package strong enough
that the generated rubric is hard for a model to satisfy.

### The 25-criteria floor

**A task cannot move on under 25 criteria.** Breadth is what forces a model to be
right across the whole task, not just on the headline call, so the surface has to
be wide.

### Weighting — three blocks totalling 100%

- [ ] About **30%** sits on the deterministic recommendation and its critical components, **split across 3 or more criteria**
- [ ] **No single criterion carries more than 20%** of the total score
- [ ] **5 to 10%** covers instruction-following: the requested files and the output-shape asks
- [ ] About **60%** covers the supplementary questions and asks, which must be **hard and discriminating, never trivial lookups**
- [ ] **Unit and rounding fold into the value criterion they belong to**, never their own criteria
- [ ] All criteria total 100%

**What instruction-following covers:** the file is present and named as asked, one
row per period, a required total row, a named column set, a specified ordering, a
page length, or printing the required figures.

Because supplementary is the largest block, **the supplementary questions carry
most of the difficulty. A wrong analytical path should get them wrong. A question
a model can answer with a surface lookup does not belong in this block.**

### What a good criterion evaluates

Criteria grade **observable outcomes in the answer** — the conclusion reached, the
values reported, the questions answered, the file delivered. They never grade how
the analyst thought.

| Topic | Good | Neutral | Bad |
|---|---|---|---|
| Reaching the conclusion | States that mobile web regressed and recommends reverting only that surface, with direction and magnitude consistent with the shipped data | Names the regression but leaves the recommended action implicit | Explains its full chain of thought before answering, showing every intermediate calculation |
| Method | Reaches a result the shipped files support, by any defensible route | Mentions a method without tying it to a result | Requires a two-proportion z-test on the deduplicated holdout specifically |
| Numbers | Reports the corrected lift with correct sign, unit and rounding, allowing equivalent representations and reasonable tolerance | Reports the right value with a missing unit | Requires the exact string "+0.62pp, z = 2.45" |

Numeric criteria are written so equivalent representations pass: "0.62 percentage
points", "+0.62pp", and "roughly six tenths of a point in favour of treatment" are
the same answer. Reasonable calculation tolerance is allowed rather than string
matching.

**Never reward disclosure.** A criterion that awards points for showing work,
naming a method, or narrating steps rewards verbosity instead of correctness. If a
step genuinely matters, the result it produced is graded, not the fact that it was
mentioned.

### What the generated rubric guarantees

You do not tune these by hand; you make them true **upstream, in the prompt and
the golden**.

- [ ] The rubric holds **25 or more criteria**
- [ ] The deterministic recommendation and its critical components carry about **30%**, spread across **3 or more criteria**
- [ ] **No single criterion is worth more than 20%**
- [ ] Instruction-following covers the requested files and output-shape asks at **5 to 10%**
- [ ] The supplementary block is about **60%** and every question in it is **hard and discriminating**
- [ ] Every requested ask is covered **exactly once**, with no two criteria overlapping or contradicting
- [ ] The golden output satisfies **every positive criterion**
- [ ] Nothing rewards methodology disclosure or chain-of-thought
- [ ] Weights sum to **100%**

### If the rubric lands under 25

The repair is in the prompt, using the five levers:

1. Three different findings, not one restated
2. One criteria-dense visual with its parts named
3. A second decision axis
4. A breakdown with an explicit grain
5. A robustness or validity check

Every criterion is a distinct, determinate answer a wrong analytical path would
get wrong. **Do not pad with rounding or units, and do not count one fact twice
because two files display it.**

## The pass bar

**"Stump the model" is retired.**

- Every rollout is **twelve responses**, scored against the fixed rubric.
- **You submit all 12.** The bottom 10 can be submitted without checking.
- **The gate is the top 2.** The task passes only when the two highest-scoring
  responses **average under 50%** against the rubric.

Confirmed on Stumping essentials, which is unambiguous. The Task walkthrough's
step 12 card says "Run 10 model responses" while also saying "submit the bottom
ten" and "only the top two are graded" — that card is simply wrong on the count.
Hard gate 02 and Stumping essentials both say 12.

**Aim the trap at the main recommendation.** It anchors the deterministic answer,
so a response that gets it fully correct should not fall below the pass threshold
merely by missing minor supplementary details. Supplementary questions deepen the
evaluation; they must never become artificial gotcha items or replace the central
recommendation as the main difficulty target.

Difficulty must stay honest: it comes from data shapes — forecasting, method
selection, a binding constraint, a decomposition, confirm-the-number, hold — never
from surface-read rejection or flipping a wrong number.

## Four fairness criteria

Always in force, on every trap.

| Criterion | Meaning |
|---|---|
| In-corpus antidote | Every deception has a correcting fact inside the files. Supersession is reconstructible from dates and documents. |
| Deterministic outcome | Ten competent analysts reach the same recommendation. All defensible cleanings converge. |
| No parsing puzzles | Every file loads with standard tooling in one or two obvious attempts. |
| No fabricated source data | No LLM-generated files, no augmentation, no model-written memos. |

## Six accepted domains

Product Analytics · Supply Chain & Logistics · Economics · Policy & Education ·
Demographic & Social Science · Nonprofit & Grant-making

## Six Axis 1 analytical objectives

Descriptive & Distribution Analysis · Anomaly Detection & Diagnostics ·
Root-Cause Analysis · Experiment & Causal Analysis · Forecasting & Predictive
Modeling · Data Extraction & Conformation (ETL / Pipeline Build)

Forecasting is an objective, not a seventh domain. Any domain can carry it, and
more of those are wanted.

## Program facts

- **$800 per approved task**, flat, paid the Wednesday after approval. The 8/18
  update raised it to this from $750 first task / $600 thereafter; material predating
  8/18 still quotes the old rate. Revisions
  are normal and unlimited; only approval before project end matters.
- Every submission is reviewed within 24 hours.
- Throttles: New Attempter 1 task → Semi-Trusted 3 tasks after the first approval
  → Trusted unlimited after 3 approvals.
- Roughly seven hours for a first task, around five after that. Estimates, not
  deadlines, and not performance thresholds.
