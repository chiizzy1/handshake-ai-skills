# Data selection and source screening

Use the current [operative rules](../../shared-references/canonical-rules.md).
For an existing task read its objective before committing a build. For exploratory
research, compare sources without claiming a slot or assuming assigned formats.

## Selection criteria

Inspect the actual empirical files, not just a landing-page description:

1. Observation units and linked keys: assignment, measurements, outcomes,
   dates, geography or operational records.
2. Analytical design: sampling, allocation, repeated participation, exposure,
   release timing, follow-up selection and missingness where relevant.
3. Completeness: all fields needed to identify the requested result are public.
   A withheld key or unavailable historical input is a limitation, not a trap.
4. Decision relevance: the data supports a coherent objective with plausible
   alternatives and a determinate outcome.
5. Rights and access: exact dataset license and service terms allow the
   proposed redistribution and AI/training use; check per-file exceptions.
6. Practical fit: genuine row counts, file sizes, usable formats, dependencies,
   necessary documentation and a workable subset preserving design structure.

A connected data collection can support deeper work than a finished index, but
neither microdata nor many tables establishes difficulty. Compute a defensible
analysis and plausible shortcuts, then test fresh solvers.

## Source research protocol

Search current primary publishers, repository catalogs and study documentation.
Use a repository API to inspect versions, licenses, public/restricted flags,
file names, sizes and download links. Verify actual responses and downloaded
content, not just HTTP success. Record metadata and hashes at retrieval time.

Read the study's current README and final design documentation. Published
replication code is useful for independently checking the data and methods;
a new task should require an original analysis, not repeat a printed answer.

Preserve raw files and licensed documentation. Derived subsets have explicit
scripts and provenance; don't duplicate records or arbitrarily split a table
to meet package quotas. Do not synthesize omitted assignment or outcome data.

If access is blocked, distinguish technical inability, login requirements and
a license restriction. Request exact missing material only if necessary to
continue a promising authorized task; do not claim verification or bypass a
restriction. Another independently licensed source may be preferable.

## September 7, 2026 shortlist — prospects, not proven stumps

| Source | Verified at discovery | Work still needed |
|---|---|---|
| [Detecting Drivers of Behavior at an Early Age](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/L28TD1) | Downloaded CC0 v2: eight empirical tables; school panel 13,608 rows; repeated assignments and unequal follow-up; all nine original checksums match | Resolve absent replication code and final cohort rules; test an original decision. Descriptive differences are not causal validation |
| [Tanzania cash transfers and trust](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/JNIXA4) | CC0/public metadata; README accessible; household and village tables over three waves | Check actual observation counts and analytical differences; only two substantive tables may limit package suitability |
| [BEA GDP/GDI archives](https://www.bea.gov/data/gdp/gross-domestic-product) | Downloaded workbook, 1,054 vintages; [public-domain policy](https://www.bea.gov/index.php/help/faq/145). First three-method rolling forecast test retained the same winner under hindsight in all three windows | Retire that simple concept; broader historical reconstruction remains unverified and the workbook alone is below 10,000 rows |
| [ACS PUMS](https://www.census.gov/programs-surveys/acs/microdata.html) | Public microdata and detailed design documentation, including 80 replicate weights | Inspect the actual release; weighting alone is not a demonstrated model weakness |

[BEA revision methodology](https://apps.bea.gov/scb/issues/2024/08-august/0824-revisions-to-gdp-gdi.htm)
describes different GDP/GDI release timing and revisions. A forecast design must
fix historical decision dates, target maturity, candidate methods and loss;
an unconstrained “best forecast” is not a deterministic golden.

Detailed local results and scripts are in workspace
`HANDSHAKE-AI/MARK-TASKS/source-screening-2026-09-07/SCREENING.md`.
No blind screen or official rollout was run for these candidates.

**Excluded as a default source:** [FRED/ALFRED terms](https://fred.stlouisfed.org/legal/)
prohibit AI development/training without prior written consent, including for
service content otherwise tagged public domain. A direct originating publisher
must be checked independently. Philadelphia Fed RTDSM reuse for this purpose
was not verified. Restricted THE-RCT, confirmatory Upworthy data and credentialed
clinical databases are not presumed redistributable because a catalog is public.

## Research is hypothesis generation

The older CausalPitfalls results used older models and a 1,000-token response
limit ([paper setup](https://arxiv.org/html/2505.13770v3#A6)).
Do not transfer published failure percentages to current tool-using agents.
Record the models, tools, protocol, date and actual observed error for our own
screens. Failed prior tasks establish limits of those designs, not whole domains.
