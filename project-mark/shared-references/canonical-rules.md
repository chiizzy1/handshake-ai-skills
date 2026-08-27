# Project Mark — Canonical Rules

One rule table for the whole project. Where the handbook contradicts itself, this
file decides, and says why.

## Source hierarchy

When two sources disagree, the higher one wins.

1. **The live Handshake platform** for the task in front of you.
2. **Readiness** (`/readiness`) and **Reviewer reference** (`/reviewer-reference`).
   These are the blocking gates: Readiness is what you must clear to submit, and
   the reviewer reference is what a reviewer actually grades against.
3. **The 8/18 update** (`/818-updates`). It changed the task shape, and the older
   pages were not all updated behind it.
4. The individual handbook pages.
5. This skill, then user preference.

## The rules the 8/18 update changed

Several handbook pages still carry pre-8/18 wording. These are the resolutions.
Building against the stale column gets a task returned.

| Rule | Stale wording, and where it still appears | Canonical |
|---|---|---|
| Input file count | "6 or more files" — Program details, approval criteria | **10 or more files** |
| Deliverables | "exactly one PDF, DOCX, or Python output" — Overview, Platform walkthrough step 5 | **2 or more deliverables across at least two format families.** See the ceiling note below |
| Supplementary questions | "3 to 5 supplementary questions" as a standalone section — Overview, Rubric review | **Folded into per-file asks: at least two asks per named deliverable** |
| Trap shape | "flip the wrong number" | **Retired.** Honest data, no planted lie |
| Domain count | "seven in-scope domains" — Program details | **Six accepted domains** |
| Input file bar, again | "six or more input files is the bar" — **Starter data kits**, stated twice | **10 or more, in a single ZIP** |
| Output-file compliance in the rubric | "the prescribed file format", singular | Covers **the whole prescribed set** |

The count of 10 files is confirmed three ways: the 8/18 update, the Input files
package checklist, and the first blocking row of Readiness. The count of 6 appears
only in Program details and is stale.

### The deliverable ceiling

Sources disagree on whether there is an upper bound, and the disagreement does not
matter in practice.

| Source | Says |
|---|---|
| 8/18 spec card | "The prompt requests **two or more** output files" — no ceiling |
| Task types, Writing the prompt | "2 to 5 deliverables" — but adds "the number is a floor; more is fine" |
| Live platform | Assigns a **per-task minimum** within the task itself |

All three agree **2 is the floor**. Treat the live per-task minimum as binding and
2 to 5 as the normal range. An assessment answer of "between 2 and 5, never more"
is wrong, because every source that names 5 also says more is fine.

## Input package

| Requirement | Bar | Blocking |
|---|---|---|
| Total files | 10 or more, shipped as a **single ZIP** | Yes |
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
- **2 or more named deliverables**, each with a filename and extension. Two is a
  floor; the normal range is 2 to 5, and the live task assigns its own minimum.
- **At least two format families** across the set.
- **At least two asks per deliverable** — a supplementary question, or a concrete
  requirement about what that file must contain.

The four families: **Data** (CSV, TSV, JSON, XLSX, Parquet) · **Visual** (PPTX,
PNG, SVG, HTML, JPG) · **Text** (PDF, DOCX) · **Code** (PY, IPYNB, SQL, R). The
formats are examples; the rule is variety across families.

An ask stays valid only while it lives in the same data universe as the
recommendation. An ask that pulls in a separate dataset or a separate decision is
a second task.

## Golden deliverables

- Types, filenames, and count match the prompt exactly.
- **One set of numbers across all files.** A reviewer diffs them against each
  other. Disagreeing numbers across files is the single most common defect.
- Nothing extra: no unrequested answers, no AI disclaimers, no placeholders, no
  files the prompt did not ask for.
- Every number traces to a shipped input file.

## Rubric weights

Generated internally from the prompt contract and the golden set. You get **one
review pass** — fix genuine problems, leave phrasing alone.

| Component | Weight |
|---|---|
| The single main recommendation, one atomic criterion | Exactly 50% |
| Supplementary answers, qualitative conclusion, output-file compliance | The other 50% |
| Output-file compliance | 2 to 5 points, taken **out of** the supporting 50, never added on top |
| Any single supplementary question | No more than 25% |
| Total | Exactly 100% |

Criteria grade observable outcomes, never disclosed methodology. A criterion that
awards points for showing work, naming a method, or narrating steps rewards
verbosity instead of correctness.

## The stumping bar

Eight responses per rollout, scored against the confirmed rubric.

- Responses 1 to 4 are **strong-model**. A qualifying stump scores **below 50%**.
- Responses 5 to 8 are **weak-model**. A qualifying stump scores **below 30%**.
- **Count gate:** at least **2 of Responses 1 to 4** and at least **1 of Responses
  5 to 8** must qualify.

Aim the trap at the recommendation. It carries 50% on its own, so a response that
gets it fully correct cannot drop below the strong-model threshold on minor
supplementary details alone.

**Never counts as a qualifying failure:** formatting-only failures · alternative
wording · an invalid or underspecified prompt · a broken or unsupported golden ·
a missing file · a grader or packaging failure · an arbitrary rubric
interpretation.

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
