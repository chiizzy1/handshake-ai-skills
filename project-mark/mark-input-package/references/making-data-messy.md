# Making Data Messy

From the FAQ. **Take real-world, neat datasets and make them realistically
messy.** The list is explicitly not exhaustive.

## Five techniques

1. **Uncluster your data.** If the data is sorted on alphanumeric identifiers,
   re-sort on a different factor so data that should be clustered together is
   partitioned into different groupings that do not allow easy analysis.
2. **Insert null values.** Add zero values, or values for related measures that do
   not actually contribute to the analysis, leading to high counts with limited
   impact on the analysis.
3. **Bootstrap values.** Repeat values that cause confusion in the analysis but do
   not impact the analytical outcome.
4. **Add a qualitative or categorical dataset.** Likert scale, Yes/No,
   Agree/Disagree alongside quantitative values — this **changes the style of
   analysis necessary** and can create confusion about how the quantitative values
   should be applied.
5. **Create typographic errors or numerical inconsistencies.** Misspell a header,
   change value base numbers (make some ages 350 instead of 35) — simple errors
   **easily recognised as errors** that need reconciling before analysis begins.

Note the recurring qualifier on 2 and 3: the mess **must not change the correct
answer**. It creates work, not a different conclusion.

## Synthetic data is allowed

> **Yes. You can use synthetic data.** It is important that the synthetic data
> looks realistic — values need to look as if they came from a real dataset.
>
> - Keep **whole numbers and repeated values to a minimum**, unless these are real-world values
> - Ensure a **normal distribution** in your values, or some derivation of the
>   normal curve (bimodal, heavy-tail, light-tail)

This softens the handbook's "no fabricated source data" rule considerably. Read
the two together:

| | Allowed |
|---|---|
| Synthetic data **derived from real-world data**, still presenting real-world data for the analysis | **Yes** |
| A few supporting files built to mirror the structure of real datasets | **Yes, as a last resort** |
| AI writing the **transformation scripts** | **Yes** |
| Fabricating the empirical evidence the decision rests on | **No** |
| Files that a domain expert could spot as synthetic at a glance | **No — the task gets rejected** |

The test is indistinguishability, not provenance. Onboarding: *"It must be
indistinguishable from a real document across data values, structure, and format."*

## BigQuery

**For sourcing:** BigQuery searches publicly available datasets and develops input
files that load into your zip. The FAQ links `Helpful hints BigQuery.pdf` and
notes a video guide is coming.

**For messiness:** BigQuery was not designed for this — its purpose is clarity in
large cumbersome datasets. But you can edit your commands to take a dataset on
your local drive and **insert blanks, duplicates, and uncluster groups**. The FAQ
links `messy_data_code.docx` with example code.

## What does not count as messy

Files that cannot be parsed with reasonable effort, or that need bespoke reverse
engineering with no discernible logic. Malformed-but-recoverable is fine —
unparseable is not.

**The difficulty comes from the analysis, not from a parsing puzzle.**
