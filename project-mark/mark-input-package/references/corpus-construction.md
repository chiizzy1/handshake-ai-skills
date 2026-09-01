# Corpus Construction — building a package that can actually stump

Clearing the 10-file minimum is **not** the standard. The standard is a corpus
where the evidence is genuinely distributed and retrieval costs real effort.
Two tasks were lost by meeting the minimum with clean, flat files.

## The benchmark: what a PASSING task shipped

Accepted example 01 (`HANDSHAKE-AI/Project-Mark/examples/01-…`) shipped:

> **28 input files across 6 formats: csv · gz · ics · log · sqlite · xlsx**

- **10 × `.jsonl.gz`** — compressed JSON lines, must be decompressed and parsed
- **1 × `.sqlite`** — a queryable database, and **the decisive fact lived in it**
  (the registered estimator the whole determination turned on)
- **1 × `.ics`** — a calendar file carrying incident windows
- **1 × `.log`** — an export receipt
- **Two separate assignment files** requiring reconciliation against each other
- `input_provenance.csv` and `telemetry_completeness.jsonl.gz` — data-quality
  metadata shipped as first-class evidence

## What we shipped, and lost with

| | Files | Formats | Character | Result |
|---|---|---|---|---|
| Task 01 | 12 | 5 | flat CSV/PDF/XLSX, kit as downloaded | both models 82% |
| Task 02 | 10 | 5 | one CSV, three PDFs, scenario docs | both models solved it |
| **Example 01 (passed)** | **28** | **6** | **gz, sqlite, ics, log** | **stumped** |

Neither of our corpora had a single compressed file, database, or injected
defect. We shipped the data exactly as downloaded, twice.

## Discoverable is not the same as obvious

The fairness rules require the correcting evidence to be **in the corpus**. They
do **not** require it to be the first thing a reader trips over. That gap is
where difficulty legitimately lives.

- Task 02 put the decisive validity rule in a 7-page PDF that was **one of four
  documents**. Both models read it immediately. Of course they did.
- Example 01 put its decisive rule in a **row of a sqlite table**. The model had
  to reason "the design specification may be registered in that database" and go
  query it.

Same fairness. Completely different discovery cost. This is E-family burial
(E7 long-file burial, E-family generally) and it is explicitly legitimate:
*"The decisive fact is present, just not where a skim will find it."*

**Rule of thumb:** if the antidote is one of fewer than ~6 documents, or sits in
a file whose name announces its contents, it is not buried — it is handed over.

## Injecting mess is mandatory, not optional

The FAQ licenses this explicitly, and staff confirm it ("you can tweak them and
make them as messy as you need to"). AI may write the scripts that inject mess;
the load-bearing data must stay real. **Both our tasks skipped this entirely.**

Apply several, not one:

1. **Uncluster** — re-sort so records that belong together are scattered
2. **Null and zero values** — high counts with limited analytical impact
3. **Bootstrap/duplicate values** — repeated records that confuse without
   changing the answer, or near-duplicates requiring a documented dedup key
4. **A categorical/qualitative file** — changes the style of analysis needed
5. **Typographic and numeric inconsistencies** — misspelled headers, mixed date
   formats, comma-formatted integers, an encoding-mangled text column

**The constraint that keeps it fair:** mess creates *work*, never a different
conclusion. Every defensible cleaning path must converge on the same answer.
Mess that changes the answer is a determinism bug (Gate 2), not difficulty.

## Format hostility is legitimate

Real analysts receive gzipped exports, sqlite extracts, log files, calendar
invites and TSVs. Shipping only flat CSVs is *less* realistic, not more. Use:

`.jsonl.gz` · `.sqlite` · `.log` · `.ics` · `.tsv.gz` · `.parquet` · `.xlsx`
with multiple sheets

Constraint from the fairness rules: **no parsing puzzles.** Every file must open
with standard tooling in one or two obvious attempts. Compressed JSONL is fine;
a corrupted archive requiring bespoke reverse-engineering is not.

## The line between complexity and padding

The rules are explicit that file count is not difficulty and that decorative
files count *against* fairness. The distinction:

| Legitimate | Padding |
|---|---|
| Evidence genuinely distributed — the answer needs several files reconciled | Copies of the same data in different formats |
| A format that reflects how the data really ships | A file nobody must open to answer correctly |
| Mess that creates cleaning work on the analytical path | Random noise in fields nothing depends on |
| Distractors a real analyst would plausibly consult | Files added to reach a count |

**The test:** every file must either be load-bearing (remove-one-file makes the
answer unreachable) or be a distractor a competent analyst would genuinely open
and have to set aside for a stated reason. Nothing else ships.

## Structural depth beats a single clever trap

Example 01's answer required, in sequence: find the registered estimator in the
database, apply recorded unequal assignment probabilities, propagate
treatment-created pre-hour state across hours, clear a **two-gate** evidence
rule, then rank actions on Q90 regret. **Eight interlocking steps.**

Our task 02: compute lift, exclude one nominee, rank three. **Three steps.**

Design the governed rule with multiple conditions that each require correct
computation — a minimum-scale gate, a validity gate, a margin gate — so a model
must get several things right in sequence rather than spot one thing.
