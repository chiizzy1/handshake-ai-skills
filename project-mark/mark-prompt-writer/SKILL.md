---
name: mark-prompt-writer
description: Write the Project Mark task prompt. Use when drafting the stakeholder message that commits an analyst to one deterministic recommendation and names three or more output deliverables across the two assigned format families with at least three asks each. Covers the task contract, prompt anatomy, the ask taxonomy, and the no-leak rules that keep the trap invisible.
---

# Project Mark — Prompt Writer

The prompt commits the analyst to one recommendation, the files supply the
evidence, and the golden deliverables are the outputs that evidence forces.

**Draft the trap before this wording.** A prompt written first signposts the
catch: it names the metric that matters, or fixes a window that quietly rules the
trap out. Write the trap, then write the message a stakeholder would send if the
trap were invisible to them.

It should read like a message a busy stakeholder would actually send.

## The Task Contract

Every prompt carries all five:

- **One deterministic recommendation.** A single committed call with one
  defensible answer.
- **3 or more named deliverables**, each with a filename and extension. **No upper
  limit.**
- **Spanning the two format families assigned to you** for that task. Two of the
  four are assigned per task; more are allowed, those two are mandatory.
- **At least three asks per file.** A supplementary question with a determinate
  answer, or a concrete requirement about what that file must contain. These
  per-file asks *are* the body of the prompt.
- **Every numeric ask states its unit and rounding.** "In USD to the nearest
  thousand", "percentage points to one decimal". Precision is load-bearing and a
  grader diffs it across the whole set.

| Family | Formats | What it is |
|---|---|---|
| Data | CSV, TSV, JSON, XLSX, Parquet | Tables, records, structured exports |
| Visual | PPTX, PNG, SVG, HTML, JPG | Charts, decks, rendered pages |
| Text | PDF, DOCX **only** | Memos, reports, briefs |
| Code | PY, IPYNB, SQL, R | A script or notebook that runs and prints the answer |

The formats are examples, not a fixed menu.

## Asks Carry ~60% Of The Rubric

This is the single biggest change in how a prompt should be written. The
supplementary asks are the largest scoring block, and the rubric must reach **25+
criteria** or the task cannot advance.

**Asks must be hard and discriminating, not trivial lookups. A wrong analytical
path should get them wrong.**

Five levers, straight from the handbook, for getting a prompt to 25 criteria:

1. **Three different findings, not one restated.** The top reason a prompt stalls
   near 20 is every ask re-expressing the same result — a median, a p90 and a
   top-tier share are all one distribution finding. Turn the task on distinct
   facts: a headline number, a driver, a threshold, a trend.
2. **One criteria-dense visual, with its parts named.** "Include a chart" is worth
   one point. A visual is worth six or seven when you name the chart type, each
   series or panel, a labeled reference line with its value, an annotation on the
   key point, an ordering, and a title that states the finding.
3. **A second decision axis.** A recommendation resting on one number is thin.
   Force the decision to weigh two things — effect and cost, growth and retention,
   forecast and capacity limit. The trade-off adds the second value, its
   comparison, and the reconciliation between them.
4. **A breakdown with an explicit grain.** "One row per segment with these
   measures" multiplies criteria: each measure over each grouping is its own
   answer. Name the grain, the columns, and an ordering or total row.
5. **A robustness or validity check.** A backtest against a naive baseline, a
   placebo or pre-trend check, a confidence interval, a sensitivity or
   leave-one-out result, or a cross-file reconciliation.

**Underneath all five:** every criterion is a distinct, determinate answer a wrong
analytical path would get wrong. Do not pad with rounding or units, and do not
count one fact twice because two files display it.

## Five Non-Negotiable Rules

1. **One committed decision.** No hedge, no blend, no "it depends". Ten domain
   experts land on it.
2. **Vague on method, precise on answer.** Withhold scope, cleaning, window, and
   methodology. Every valid approach still converges.
3. **No leak.** Never name the trap, the file that defuses it, or hint that a
   metric is misleading.
4. **Fair and self-contained.** Everything derivable from the bundle, and the
   losing option refuted on the data.
5. **3 or more deliverables across the two assigned families, three asks each**,
   every file named with its extension, every numeric ask carrying its unit and
   rounding.

### What gets sent back

A prompt that names the method or the trap · allows a hedged answer · requires
outside knowledge · asks for a separate dataset or decision · requests only one
file · requests fewer than three files · misses one of the two assigned families ·
leaves a file with fewer than three asks · fills asks with trivial lookups.

## Prompt Anatomy

| # | Part | What goes in it |
|---|---|---|
| 1 | Stakeholder context | The trigger and the stakes: what happened, who disagrees, what is at risk |
| 2 | The decision | The one call being asked for, with the objective fixed so it cannot mean three things |
| 3 | Necessary scope or constraints | Only the constraints the stakeholder would state, such as choosing exactly one option |
| 4 | Requested deliverables | 3 or more named files across the two assigned families |
| 5 | Asks per file | Each named file states what it must answer or contain — three or more |
| 6 | No answer-path leakage | Silent on scope, cleaning, window, and method. The trap is never named or hinted |

## The Kinds Of Asks

Across the task you want more than one kind, so the evaluation reaches more than
one kind of evidence.

| Kind | What it does | Example |
|---|---|---|
| Supporting | A metric that backs the recommendation | "By what percentage did the selected product's revenue change from FY24 to FY25?" |
| Comparison | How the winner sits against the runner-up | "By how many dollars did its FY27 value exceed the runner-up?" |
| Context or flip | A related conclusion, including what would move the runner-up into first | "Excluding FY27, which year was the best entry point?" |
| Content requirement | A concrete thing the file must contain | "The PDF includes a chart of weekly retention by acquisition cohort." |

An ask stays valid only while it lives in the same data universe as the
recommendation, and supports it, compares against it, or gives it context. **An
ask that pulls in a separate dataset or a separate decision is a second task.**

### What an ask must not do

It must not enumerate the methodology, name the trap, identify the decisive file,
or walk the model through the answer path. A content requirement names *what* the
file holds, never *how* to compute it.

## Worked Shape

```
Q3 profitability fell below plan. Management must cut exactly one product
category from the next buying cycle.

Recommend the single category whose removal gives the strongest defensible
improvement in continuing-portfolio economics.

Give me a board-ready business report in category_decision.pdf that makes the
cut and defends it.
  - Name the category to remove and the continuing-portfolio margin change the
    removal produces, in percentage points to one decimal place.
  - Include a bar chart of continuing-portfolio margin by category (y-axis in
    percent, one decimal), before and after the cut, with the runner-up
    highlighted.

Attach the working numbers in category_scan.csv so Finance can audit them.
  - One row per category with revenue in whole USD, and direct margin and
    continuing-portfolio margin as percentages to one decimal place.
  - A final column naming the single evidence-backed change that would make the
    runner-up the better cut.
```

Note what it does *not* say: nothing about which categories to include, what
window to use, how to treat returns, or which margin definition governs. Those
are the analyst's work. Note also that precision requirements — units, decimal
places, whole numbers — are stated, because they are load-bearing across
deliverables and a grader diffs them.

More worked prompts in `references/worked-prompts.md`, drawn from the 25 accepted
examples.

## Leak Check

Run `../tools/mark_leak_check.py` against the draft. It validates contract shape
— three or more deliverables, the two assigned families, three asks each, filenames
carrying extensions — and flags likely leakage: named methods, narrated traps,
wording that points at the decisive file.

It is a linter, not a judge. Read its flags and decide.

Leak patterns to catch by eye:

- Naming a statistical method ("use a two-proportion z-test", "deduplicate first")
- Naming the window when the window is the trap ("over the last full quarter")
- Signalling suspicion ("be careful with the summary file", "note that some rows
  may be duplicated")
- Naming the arbiter ("the data dictionary defines the field")
- Any sentence that reads like an instruction to an analyst rather than a request
  from a stakeholder

## Output Format

```
## Prompt

<stakeholder context — 1 to 3 sentences>

<the committed ask — one sentence, no hedge available>

<constraints, only if a stakeholder would state them>

<file>.<ext>
  - <ask>
  - <ask>

<file>.<ext>
  - <ask>
  - <ask>

<cross-deliverable precision requirements, if any>

## Contract check
Deliverables: <n> (2–5) ✓/✗
Families: <list> — <n> distinct (2+) ✓/✗
Asks per file: <file> <n> · <file> <n> — all 2+ ✓/✗
One committed call, no hedge available: ✓/✗
Leak check: <clean / flags, listed>
```
