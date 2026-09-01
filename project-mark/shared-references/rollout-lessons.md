# Rollout Lessons — empirical field notes

## 2026-09-01 · task-02 · THE GRADED MODELS ARE OPUS 5 AND GPT-5.6

Confirmed from opencode.json in the returned workspaces: Response 1 = Anthropic
claude-opus-5, Response 2 = OpenAI gpt-5.6-sol. Both run as agents with code
execution, package installation, MCP file access, and clean-directory
self-checks.

**Design 3 result (Upworthy validity trap): both models found the documented
not-fully-randomized window, cited the exact dates and rule section, excluded
the 209%-lift bait with correct causal reasoning, and matched the golden on
every figure** (CI convention aside: they used the log-ratio interval, we used
delta — both defensible). The bait that significance testing endorses at
z = 10.2 did not survive their document reading.

Running total: 3 tasks, 5 designs, 6 graded responses, **zero misses on the
main recommendation**. Traps beaten so far: sentinel handling, cross-universe
re-ranking, label bait, cross-experiment comparison bait, documented-validity
exclusion.

**Operating conclusion, sharpened:** against Opus 5 + GPT-5.6, any trap whose
correct handling amounts to *reading the shipped corpus and applying what it
says* will fail — they read everything, every time. The remaining candidate
space is example-01-class construction: multi-stage governed estimators where
the correct method must be BUILT from structure, and the adequate-looking
shortcut survives full document reading. Unverified whether even that beats
these models — the accepted examples predate them. Before burning another
build: ask in Slack whether ANY task has passed the stump check since the
graded models were upgraded, and what shapes landed.

Verified findings from real stump checks. Read this BEFORE picking a dataset or
designing a trap. Dated entries; newest first. Append after every rollout,
pass or fail — this file is the memory that transfers between sessions.

## 2026-08-31 · task-01 · Descriptive & Distribution · CDC SVI 2022 tracts

**Three trap designs, all solved. Final stump check: both responses 82% against
a 27-criterion rubric. Bar: top-two average < 50%. Failed decisively.**

| Design | Trap family | Outcome |
|---|---|---|
| −999 sentinel corrupts county means (flips winner) | D14 plumbing | Solved by reflex; filed under "documented assumptions"; one model re-ran our own robustness test unprompted |
| Percentile standings re-ranked within an applicant pool vs averaging published national percentiles (flips winner) | F/A rank-vs-cardinal | Solved and **explained back to us** in the response summary |
| County-universe bait files (applications citing CDC county-level figures) | E3/F1 | Identified, classified as informational per the rule, set aside |

**What both models did correctly, every time:** careful rule-document reading
(section-level citations), sentinel/missing-data handling, key/grain/join
hygiene, string-FIPS with leading zeros, cross-universe re-ranking, denominator
selection from documentation formulas, no hard-coding, clean-directory
reproduction, unprompted robustness checks.

**The only points they dropped (18 of 100):** row-specific output structure
(repeating a generic flip condition across rows) and 3rd–4th-decimal
tie-convention scatter in per-theme pools. Implementation noise, not analysis.

### The two operating conclusions

**1. Gate arithmetic.** The recommendation cluster carries ~30–37 points. A
response that solves only the core already sits near 50%. The top-two average
lands under 50% **only if both top responses get the main recommendation
wrong**. A trap that does not flip the main answer cannot pass the gate, no
matter how much supplementary difficulty it adds.

**2. The difficulty ceiling is set by the dataset, not the trap.** A finished
composite index (SVI-style: scores already computed) offers only *execution*
difficulty — reading and arithmetic — and current models execute perfectly.
The accepted examples' stumps live in **statistical validity**: a registered
estimator ignored in favour of the tempting pooled comparison (example 01),
leakage, invalid designs, mishandled cohorts. That machinery must exist in the
data. If the correct solution requires nothing beyond careful reading and
careful coding, the dataset cannot stump, and no prompt engineering fixes it.

### Why sourcing must use the live web

Verified failures of memory-based sourcing during this project: guessed CDC
documentation URLs 404'd (live page had a different path); THE-RCT dataset seems
usable from memory but is restricted-access on its live ICPSR page; the task
spec itself changed twice in nine days. Any future agent must search and fetch
before claiming or downloading — and if it lacks web tools, ask the user to
fetch or screenshot rather than proceeding from recall.

### 2026-09-01 · external research corroboration (CausalPitfalls, arXiv 2505.13770)

A published benchmark of LLM statistical-pitfall failures confirms the design
direction empirically:

- **Hint gradient:** top models fall from ~60% accuracy with explicit guidance to
  ~18% with minimal guidance. Task rules that enumerate the correct checks ARE
  the hint — pin the decision metric only; let validity live in shipped
  documentation and in Gate-2 convergence, never in instructions.
- **Branding bias:** identical data yields opposite conclusions under
  semantically suggestive labels. Shipped label columns (winner/significance)
  are a measured weakness — use real ones as bait, never authored ones.
- Models are STRONG at recognising randomized designs — so a design that looks
  randomized but silently is not subverts a strength. Weakest areas: external
  validity (4–28%) and mediation; strongest: recognising RCT vs observational.
- Real data exposes deeper reasoning gaps than synthetic; code assistance does
  not rescue judgment failures (correctly computed statistics on invalid
  designs mislead more convincingly).

### 2026-08-31 · platform mechanics, second round (post-skip screenshots)

- **Task cards show their objective BEFORE claiming.** The available-tasks list
  tags each card (Experiment & Causal, Forecasting, ETL, …). You pick the card
  you want — the objective is chosen, not gambled. Format families are still
  revealed inside the task after claiming.
- A skipped task returns to the pool as Unclaimed. Confirmed by seeing our own
  former task ID back on the list.
- The "five-condition eligibility check" was a handbook-page widget only; the
  platform has no own-data gate. Sourcing is unrestricted by the flow.
- Kits are beginner scaffolding. Own sourcing is the default and the project
  description says so ("Fellows will source real occupational materials").
- Task limit for new fellows: 0/1 accepted tasks visible on the list header.

### 2026-08-31 · Upworthy Research Archive, live verification

- Licence **CC-BY 4.0** (attribution: Cornell). Data at osf.io/jd64p.
- **Exploratory file is open**: 22,666 packages / 4,873 tests. The
  **confirmatory file requires peer-reviewed analysis plans — do not use.**
  Web-scraped supplementary data needs consultation — avoid.
- **Documented randomization problems affect 22% of tests run 2013-06-25 to
  2014-01-10** — an in-archive validity window. Prime trap machinery: the valid
  population is defined by the archive's own documentation.
- Aggregate arm-level data (impressions, clicks) — supports SRM checks; no
  individual-level records.

### Platform mechanics confirmed on the way

- The stump check is **2 responses at step 3** — you learn whether the task
  works before writing the golden. Iterate there.
- Unclaiming and re-claiming a task **re-rolls the assigned objective and
  format families**. Claim first, read the assignment, then design.
- The generated rubric centred every range on our golden figures — the
  pipeline's numbers were independently validated even as the stump failed.
- The task timer has a pause button. Pause it while deciding.
- Skipping a TASK is free — staff-confirmed, no penalty. But the STARTER KIT
  claim is one per fellow, ever: skipping does not recycle it. The two claims
  are different things. After the kit is spent, input data comes from your own
  sourcing (public data, BigQuery, derived-from-real synthetic), which is
  unlimited and explicitly endorsed.
- Kits are "just a starting point" (staff): tweak, extend, make as messy as
  needed. Nothing requires the task to be built AROUND the kit — it can serve
  as context/distractor files beside self-sourced data that carries the trap.
- **Two ZIPs, two different fields** (staff broadcast, 2026-08-31): the prompt
  step takes the INPUT package; the golden step takes the 3–5 DELIVERABLE files
  as one ZIP — the same files, names and count the prompt requests, with every
  ask answered inside them. Input files do NOT go in the golden field.
