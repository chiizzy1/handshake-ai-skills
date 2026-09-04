# Business Realism — making authored files look like documents, not output

## Why this is now a rejection criterion

From the 9/01 Slack announcement:

> **Your golden deliverable and input files MUST not look LLM-generated and look
> business-realistic.** We have been fixing these for you (to be nice), but we
> will be rejecting these from now on.

This is the price of the bar moving from 50% to 70%. The difficulty got easier;
the craft got mandatory. A task that stumps both models and ships files that read
as ChatGPT output is now a rejection, not a fix-up.

It applies to **two** categories, and the second is easy to forget:

1. **Input files you authored** — the memo, the standard, the prior-quarter
   report, the log. Anything not pulled from a real source.
2. **Golden deliverables** — the PDF, the CSV, the chart, the script you hand in
   as the correct answer. These are read as work product from a competent analyst
   and are judged the same way.

Files pulled from a real public source are already realistic. The risk is
entirely in what you write yourself.

## The tells that give it away

### Prose

| Tell | What a real document does |
|---|---|
| Uniform paragraph length, every section the same weight | Sections are lopsided. The part the author cared about runs long; the boilerplate is two lines |
| Every sentence grammatical and complete | Real internal writing has fragments, a comma splice, an aside in parentheses |
| "Furthermore", "Moreover", "It is worth noting", "In conclusion" | Plain connectives, or none — a new paragraph does the work |
| "leverage", "robust", "comprehensive", "seamless", "delve", "underscore" | The plain word. "Use", "solid", "full", "look at" |
| Perfectly parallel bullets, all the same shape and length | Bullets of wildly different lengths; one is a single word; one runs three lines |
| Nothing extraneous — every sentence load-bearing | Real documents carry dead weight: a paragraph about a process change nobody asked about, a note that stopped being relevant two quarters ago |
| No hedging, no politics | "Ops has flagged this before but we have not had the headcount to look at it" |
| Confident throughout | Real authors mark their own uncertainty: "I think", "roughly", "someone should check this" |

### Structure and metadata

| Tell | What a real document has |
|---|---|
| No document control | A doc ID, revision letter, effective date, owner, approver. `RSS-Q3-26 rev B`, not "Selection Standard" |
| No version history | A revision table: what changed in rev B and who signed it |
| No author | Real names and initials, used inconsistently — "M. Okafor" in one place, "Okafor" in another |
| Clean file properties | Author, company, created/modified timestamps. A `python-docx` file with empty core properties is a fingerprint |
| Uniform styling | Real documents drift: a section pasted from elsewhere in a different font size, a table with one column too narrow |
| No footer | Page numbers, a confidentiality line, a file path from whoever printed it |
| Everything current | A stale cross-reference to a section that was renumbered, a "TBD" nobody filled in |

### Numbers

| Tell | What a real document has |
|---|---|
| Round thresholds everywhere | Some round (10,000 impressions — a policy number), some not (a measured value with odd precision) |
| Consistent decimal places | A memo written by a person mixes `5.24%` and `roughly 3x` in the same table |
| Every figure correct | An unaudited estimate that is *close* — this is also good trap material |
| Perfectly consistent units | A column in thousands with one cell in units, flagged by a note |

### Spreadsheets specifically

Real workbooks carry: a second sheet nobody looks at; a Notes tab with three
lines and a name; column widths adjusted by hand; frozen header rows; a cell
comment; mixed number formats between columns; a stray total at the bottom that
does not quite tie.

An `openpyxl` default workbook — one sheet, default widths, no freeze, uniform
formatting — is immediately recognisable.

## What to do instead

**Give each authored document an owner and a reason to exist.** Before writing a
line, answer: who wrote this, for whom, and what were they trying to get done?
A standards document written by a compliance function reads nothing like a memo
written by a content editor lobbying for their nomination. If both of your files
sound like the same voice, neither sounds real.

**Let the authors be inconsistent with each other.** The nominating editor writes
"more than 4x the rest"; the standard writes "shall not be less than 10,000
impressions". Different registers, different precision, different formatting
conventions. This is also free trap material — the memo's loose estimate is
exactly the bait.

**Put in the boring apparatus.** Document control block, revision table, footer,
distribution list, a section that exists only because policy requires it. It
costs you ten minutes and it is most of what "business-realistic" means.

**Set the file metadata.** Author, company, title, created and modified times
that make sense relative to the scenario's dates. Empty core properties are a
tell that costs nothing to fix.

**Leave some dead weight in.** One paragraph that is context rather than
evidence. Real documents are not optimised.

## The audit to run before shipping

Run `tools/mark_realism_check.py <package_dir>` — it flags empty document
metadata, LLM-register vocabulary, suspiciously uniform structure, and default
spreadsheet formatting. It is a lint, not a judge: it catches the mechanical
tells, and the voice is still on you.

Then read each authored file end to end and ask the only question that matters:

**If this arrived in my inbox, would I believe a person wrote it for a reason?**

If the answer is "it reads like a very good summary of what such a document
would contain", it is not there yet.
