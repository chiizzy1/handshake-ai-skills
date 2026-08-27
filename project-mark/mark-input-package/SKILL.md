---
name: mark-input-package
description: Assemble and verify the Project Mark input file package. Use when sourcing real, license-clean data files for a Project Mark task — hitting 10+ files, 4+ independently necessary, 2+ substantial, 3+ formats, a 10,000+ row table, recoverable joins, and per-file provenance. Covers sourcing routes, starter kits, the remove-one-file test, and the manifest.
---

# Project Mark — Input Package

The file package the model receives: the datasets, documents, and reports a real
analyst in your domain could plausibly have been handed.

The test that governs everything here: **could a skilled analyst recover the
answer without guessing?**

## Hard Gates

- **No LLM-generated PDF, DOCX, or PPTX.** They are spotted in seconds. This
  rejects the task outright.
- **AI may locate data and write transformation scripts. AI may never create the
  empirical source evidence.** Blocking rule.
- **Scenario documents carry explicit provenance** stating what they are and how
  they were produced. You may write one yourself; it is a scenario document, not
  source data, and it is recorded as such. Blocking rule.
- **Every file records source URL, pull date, and licence.**
- **File count is not difficulty.** Do not add decorative files. Irrelevant files,
  duplicated information, arbitrary noise, and volume that only creates search
  burden all count *against* fairness.

## The Bar

Every line is blocking. Numbers come from Readiness stage 1, which is what a
reviewer checks first.

| Requirement | Bar |
|---|---|
| Total files | 10 or more |
| Independently necessary | 4 or more — remove any one and the answer is unreachable |
| Substantial rather than token | 2 or more — long, dense, real work to read and reconcile |
| Distinct formats | 3 or more |
| Largest table | 10,000+ rows, so eyeballing fails |
| Joins | The recommendation requires joining at least two tables |

Distractor files are allowed and encouraged. **They never count toward the four
independently necessary files.**

## Messiness That Earns Its Place

Realistic fragmentation the analyst has to work through — never random dirt, and
it never changes the correct answer once resolved.

- Signal is fragmented across files, so the model has to piece it together.
- Timestamps are inconsistent and must be reconciled.
- Data is scattered enough that the model has to seek around the environment.
- Template files or historical reports sit in the package as reference material
  to discover and use.

What does **not** count as messiness: illegally formatted files, invalid
encodings, broken XML. Difficulty is spent on reasoning, not on parsing. Every
file must load with standard tooling in one or two obvious attempts.

## Workflow

### 1. Choose a data route

**Starter kit** — authentic, license-clear source material with provenance
already documented. It is a foundation, not a finished submission. You still own
the file count, the complexity, the mess, and the deterministic answer. Claiming
and downloading happens in the external Stash registry.

**Your own sourcing** — real documents pulled from the wild. Government
statistical releases, regulator filings, published board papers, open data
portals, published methodology notes.

#### What a starter kit actually gives you

| | |
|---|---|
| Contents | **6 to 8 raw files** — several CSVs, an `overview.xlsx`, and a `data_dictionary.json` |
| The dictionary | Records source URL, licence, snapshot date, and every transform applied. **Use it as your provenance note** — it covers the blocking Readiness rows |
| What is missing | Nothing is cleaned, joined, or reconciled. No task exists. You choose the decision, design the trap, write the prompt |

**A kit does not clear the bar on its own.** 6 to 8 files against a 10+ bar means
planning on **3 to 5 added files** from the start. Check the largest table
immediately — if nothing carries 10,000+ rows, sourcing one is your first job.

> ⚠️ The Starter data kits page says twice that "six or more input files is the
> bar." **That is pre-8/18 and wrong.** The bar is 10+ in a single ZIP. Building
> to six gets the task returned.

#### The claim rules

- **One active claim at a time.** A second request while the first is open is refused.
- **An open claim means a submitted task is expected from you.**
- **Claiming is final.** The package leaves the pool until inventory cycles, and
  cannot be swapped.

Preview before claiming. Look for a decision a real domain owner would own, a
table big enough to clear 10,000 rows, and enough structure that two tables must
be joined. Claiming is done on the Stash, an external registry
(`unlock-the-stash.lovable.app`) that browses and claims only — you submit the
finished task on Handshake.

The alternative path, "I already have source data", is gated behind a
five-condition eligibility check that was not captured locally. Read it on the
platform before spending your single claim.

### 2. Record every file

One row per counted file, before you decide anything about sufficiency.

| File | Format | Analytical role | Rows | Source URL | Pull date | Licence | Necessary? |
|---|---|---|---|---|---|---|---|

`../tools/mark_manifest.py` generates this, plus SHA-256 and byte size per file,
and reports the counters against the bar above. It takes a directory or the .zip
you will ship. Gate 1 of validation requires that manifest, so produce it here
rather than later.

Start by generating the template, so you are filling blanks rather than writing
JSON from scratch:

```
python3 ../tools/mark_manifest.py <package> --init-roles roles.json   # once
python3 ../tools/mark_manifest.py <package> --roles roles.json        # every time after
```

Leave `necessary` as `null` until the remove-one-file test has actually run. The
script reports unrecorded files rather than guessing, and that is the honest
state until you have tested it.

### 3. Resolve missing evidence

Ask once: **does the current package support the answer?**

If yes — stop. Do not add decorative files.

If no — identify exactly what is missing (a definition, a piece of evidence, a
piece of context), find one authoritative source that supplies it, add only that
file. Common gaps worth filling: definitions · historical context · methodology ·
policy constraints · targets · predictors · revisions · crosswalks.

### 4. Run the remove-one-file test

Delete each counted input in turn and re-solve. Record, per file, whether the
correct answer becomes **unreachable**, **changes**, or **survives untouched**.

A counted file that survives removal is not load bearing. Give it a real
dependency or drop it from the necessary count. Ask the same question of noise:
does this file, format, or extra source actually sit on the analytical path?

You need 4 or more that come back "unreachable".

### 5. Confirm the package

Seven checks. All seven, or the package is not ready.

- [ ] **Necessary files** — ten or more counted, four or more independently necessary
- [ ] **Recoverable joins** — files connect through keys or references an analyst can recover
- [ ] **Sufficient signal** — the data supports the analysis the prompt actually requests
- [ ] **Definitions and governing rules supplied inside the package**, not assumed
- [ ] **Reproducibility** — every figure in the golden comes back out of the shipped workspace
- [ ] **No padding** — no decorative or deletable file is counted
- [ ] **No fabricated or corrupted complexity** — complications are authentic, nothing machine-generated, padded, or broken on purpose

## Licensing And Provenance

Every file needs three things recorded: **source URL**, **pull date**, **licence**.

Prefer sources that are unambiguously redistributable: public-domain government
releases, open data portals with an explicit licence, permissively licensed
published datasets. Where a licence requires attribution, record the attribution
string with the file.

A file you cannot document is a file you cannot ship.

## Notes On Formats

Aim across at least three. Substantial files should not all be the same type.

| Family | Formats | Good for |
|---|---|---|
| Data | CSV, TSV, JSON, XLSX, Parquet | The large table, the raw records, the crosswalk |
| Text | PDF, DOCX | Methodology notes, board papers, policy documents, the definitions that arbitrate |
| Visual | PPTX, PNG, SVG, HTML, JPG | Summary decks that carry the bait, charts with the detail in the annotation |
| Code | PY, IPYNB, SQL, R | Pipeline scripts, historical analysis to discover and reuse |

A chart can be a distractor when the same data is also supplied numerically — the
numbers are the arbiter, and the chart is where a skim stops.

## Output Format

```
## Input package
<n> files · <n> independently necessary · <n> substantial · <n> formats
Largest table: <file>, <n> rows
Joins required: <table> ↔ <table> on <key>

| File | Format | Role | Rows | Source | Pulled | Licence | Necessary? |

## Remove-one-file test
| File | Removing it | Verdict |
|---|---|---|
| ... | answer unreachable / answer changes / survives | necessary / distractor |

## Bar check
10+ files: <n> ✓/✗   4+ necessary: <n> ✓/✗   2+ substantial: <n> ✓/✗
3+ formats: <n> ✓/✗   10,000+ row table: <n> ✓/✗   joins: ✓/✗
Provenance complete: <n> of <n> files
```

Report the real counts. If the remove-one-file test was not actually run, say
"not run" rather than guessing which files are necessary.
