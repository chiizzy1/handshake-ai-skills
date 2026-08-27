# Sourcing Real Data

The bar: **files are real and license-clean, with source, date, and licence
recorded.** A file you cannot document is a file you cannot ship.

## Where real documents come from

The handbook's own sourcing accordion was not captured locally. What follows is
the operative guidance drawn from the rules that were, plus what the 25 accepted
examples actually shipped.

Sources that reliably clear the licensing bar:

- **National and regional statistical agencies** — releases, revisions, and the
  methodology notes that accompany them. The methodology note is often the arbiter
  file a trap needs.
- **Regulators and public registries** — filings, determinations, published
  registers, enforcement notices.
- **Open data portals** with an explicit licence per dataset.
- **Published board papers, council minutes, and committee determinations** —
  these are the natural home of a governing rule that a summary contradicts.
- **Research data repositories** with permissive licences.
- **Published corporate reporting** where the licence allows redistribution.

The accepted examples lean heavily on this shape: a determination document, a
holdings or ledger table, a scan or comparison spreadsheet, and a script.

## The two blocking sourcing rules

1. **AI may be used to locate data or to write transformation scripts, but it may
   never create the empirical source evidence itself.**
2. **Scenario documents and derived files carry explicit provenance stating what
   they are and how they were produced.**

You may write a scenario document yourself. It is a scenario document, **not
source data**, and it is recorded as such. A self-written memo that is presented
as a found artifact is a fabrication.

## The tells that get a task rejected

LLM-generated PDFs, DOCX and PPTX are spotted in seconds:

- a few words per page, oceans of white space
- tables that are too clean — no footnotes, no revision marks, no inconsistent
  column widths, no orphaned header rows
- uniform sentence length and no house style
- no letterhead, no document control number, no version history
- dates that are all the same, or all suspiciously recent

Real documents are messy in ways that are hard to fake: they carry page furniture,
appendices nobody updated, a footnote contradicting a table, a revision history.
Those are also where the best traps live.

The FAQ position on LLM-created files: **not recommended**, and if you do it, it
must be indistinguishable from a real document, or the task gets rejected.

## When a supporting file earns its place

Ask the question in this order:

1. **Does the current package support the answer?** If yes — stop. Do not add
   decorative files.
2. If no, **what exactly is missing?** A definition, a piece of evidence, or a
   piece of context.
3. **Which one authoritative source supplies it?** Add only that file.

Gaps worth filling, from the handbook: definitions · historical context ·
methodology · policy constraints · targets · predictors · revisions · crosswalks.

Every one of those is also a trap surface. A definition buried in supporting
documentation, or a revision file that silently supersedes an older dataset, are
named by the handbook as among the strongest trap shapes.

## Distractors

Allowed and encouraged. They never count toward the four independently necessary
files.

A good distractor is a file a real analyst would plausibly have been handed and
would plausibly consult: last quarter's version of the same report, a summary
deck built on a stale extract, a template. A bad distractor is arbitrary noise —
it counts against fairness, not for difficulty.

The line: does the file create *search burden* or *analytical burden*? Only the
second is difficulty.

## Starter kits

A starter kit gives authentic, license-clear source material so you can skip the
hardest part of sourcing. It is **a foundation, not a finished submission.**

| Included | You may still need to add |
|---|---|
| A real, license-clear dataset package from a public source | Supplementary definitions, methodology, or policy context |
| Several related files in more than one format | Additional files so the package clears the input rules |
| Enough raw material to support a defensible decision | Realistic mess, distractors, and the traps your task depends on |
| Source, publisher, licence, and provenance notes per file | |

You still own the file count, the complexity, the mess, and the deterministic
answer. Claiming and downloading happens in the external Stash registry; nothing
in the handbook claims a package for you.
