# New-Task Runbook

The end-to-end sequence for starting a Project Mark task, with live-web research
as mandatory steps — not fallbacks. Distilled from tasks 01–02; the evidence
behind each rule is in `../../shared-references/rollout-lessons.md`.

## 1 · Claim first, read the assignment

Claim the task slot before designing anything. Record the **assigned objective**
and the **two required format families** (revealed inside the task). Re-claiming
re-rolls them. The timer has a pause button.

## 2 · Research pass (browse the live web — mandatory, ~30–60 min)

Two searches, before any data is chosen:

a. **Model-failure research for this objective.** Search for published
   benchmarks and papers on what LLMs get wrong at this task type. One such
   search (CausalPitfalls) reshaped an entire trap design: the hint gradient,
   branding bias, subverting model strengths. Never design from intuition about
   model weaknesses when measurements exist.
b. **Candidate datasets carrying the machinery the objective needs** —
   registered designs, weights and MOEs, vintages, validation structure. Start
   from the vetted map in `data-selection.md`, then search for fresher or
   better-fitting sources.

Record what both searches find in `rollout-lessons.md`.

## 3 · Screen candidates

Apply the ceiling test to each candidate (`data-selection.md`): *what does the
correct solution require beyond careful reading and careful coding?* If
nothing — walk away. Pre-computed indices cannot stump.

## 4 · Verify live, then fetch with provenance

- Fetch the **actual licence page** and read the terms.
- Find real download URLs through **repository APIs**, not page-scraping or
  guessed paths — e.g. OSF: `api.osf.io/v2/nodes/<id>/files/osfstorage/`
  returns every file with its download link. Guessed URLs 404'd repeatedly.
- Download with `../../tools/mark_fetch.py`, which hashes and records
  provenance at fetch time.

**When a source is blocked** — bot protection, JavaScript-rendered pages,
logins, or anything the session cannot reach — **do not abandon it and do not
substitute from memory. Hand the user the exact URL and precisely what to
save** (print-to-PDF for pages, Save As for files, screenshots for app
screens). That pattern recovered an entire project handbook and the decisive
CDC documentation. The user has standing instructions to fetch on request.

## 5 · Mine the data and verify the flip BEFORE writing anything

Find the trap empirically: compute the naive path and the correct path from
the real data and confirm they give different answers with safe margins. Run
the Gate-2 estimator sweep now, not after the build. **Identify candidates by
exact IDs, never by date-plus-size heuristics** — a same-day lookalike test
once nearly poisoned a whole golden.

## 5b · Build the corpus to the passing standard

Before authoring anything, read
`../../mark-input-package/references/corpus-construction.md`. Distribute the
evidence across files and formats, inject mess deliberately (mandatory), bury
the arbiter where it requires seeking rather than reading, and give the governed
rule multiple conditions. Ten clean CSVs clears the bar on paper and has lost
twice.

## 6 · Author the scenario documents

Every number transcribed from the real data, scenario footers on, provenance
recorded as authored. The rule document pins the **metric only** — the hint
gradient (60%→18%) means every validity check named in a rule is a check the
models will simply execute.

## 7 · Prompt, golden, gates

Prompt in business voice; lint with `mark_leak_check.py`; grep for leak
vocabulary (valid/random/window/balance/period and task-specific terms).
Golden scripts compute everything from the archive — nothing hard-coded.
Then: manifest with roles, freeze the ZIP, Gate 1 clean-directory rerun,
Gate 3 remove-one-file with stated reasons, reconcile the deliverables.

## 8 · The stump check is the experiment

Run step 3 on the platform and read both responses as data. Append the
outcome to `rollout-lessons.md` — pass or fail — and append any newly vetted
data source to the map in `data-selection.md`. The next task starts smarter
than this one only if both files grow.
