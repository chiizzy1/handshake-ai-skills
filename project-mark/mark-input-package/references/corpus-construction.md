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

### Mess must never make a value unknowable

An injected inconsistency is fair when a careful reader can recover the true
value, and unfair when two competent readers recover two different values. The
distinction is easy to lose in date formatting, which is where we lost it.

Task 02 v2 rendered dates in three formats. `09/02/2014` parses to 9 February
under day-first and 2 September under month-first — two real dates, no way to
choose. Worse, the shortlist memo used day-first in one row and month-first in
another. Because the s4.2 gate turned on which fielding period a date fell in, a
day-first reader could land in a different period and select a different nominee
with entirely sound reasoning.

The fix was a construction rule, not a spot correction: **emit month-first dates
only where the day exceeds 12**, so no rendered date parses to two real dates.
Then sweep every distinct value and assert zero ambiguity — the guarantee has to
hold by construction, because a reseed will otherwise reintroduce it. The
generator had produced a fair corpus by luck; luck is not a property you can
ship.

The same test applies to any injected inconsistency:

- **Ambiguous units** — `1.5` meaning thousands in one row and units in another
- **Ambiguous decimal separators** — `1.234` as European thousands or a fraction
- **Truncated identifiers** that collide once shortened
- **Encoding mangling applied to the join key** rather than to display text
  (mangle headlines, never IDs)

Write the sweep as an assertion in the build, not a one-time check. Ask of every
injected value: *can a careful reader recover the original with certainty?* If
not, it is not mess — it is a coin flip you have hidden in the data.

## Format hostility is legitimate

Real analysts receive gzipped exports, sqlite extracts, log files, calendar
invites and TSVs. Shipping only flat CSVs is *less* realistic, not more. Use:

`.jsonl.gz` · `.sqlite` · `.log` · `.ics` · `.tsv.gz` · `.parquet` · `.xlsx`
with multiple sheets

Constraint from the fairness rules: **no parsing puzzles.** Every file must open
with standard tooling in one or two obvious attempts. Compressed JSONL is fine;
a corrupted archive requiring bespoke reverse-engineering is not.

**Run the manifest after every repartition, and read the row count.** The
10,000-row requirement is measured per file, not across the corpus. Splitting
22,666 records into five half-year files caps the largest at 9,278 and fails the
bar; splitting the same records by year puts 14,336 in one file and passes.
Format hostility and the row-count bar pull against each other — the finer the
partition, the more searching a model must do, and the closer the largest file
creeps to the floor. Check the number rather than assuming the total carries it.

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
