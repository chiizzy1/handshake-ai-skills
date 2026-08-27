# Licensing And Provenance

Three fields per file, no exceptions: **source URL · pull date · licence**.

Blocking at Readiness stage 1 and checked at Review 1.

## The record

| File | Format | Analytical role | Rows | Source URL | Pull date | Licence | Attribution | Necessary? |
|---|---|---|---|---|---|---|---|---|

`../../tools/mark_manifest.py --roles roles.json` merges this record with
SHA-256 hashes and byte sizes, and reports the counters against the bar. The
sidecar is a JSON map from filename to
`{"role":…, "necessary":true, "source":…, "pulled":…, "licence":…}`.

Generate it rather than hand-writing it:

```
python3 ../../tools/mark_manifest.py <package> --init-roles roles.json
```

That emits every filename with blank fields to fill in. If you claimed a starter
kit, most of `source`, `pulled` and `licence` can be copied straight out of the
kit's `data_dictionary.json`.

Necessity comes from the remove-one-file test, not from the script. Anything not
recorded is reported as unrecorded rather than guessed.

## Choosing sources by licence

Prefer, in order:

1. **Public domain** — most national statistical output, most government
   determinations.
2. **Open licences with attribution** — CC-BY, OGL, and equivalents. Record the
   attribution string alongside the file.
3. **Explicit permissive terms** on a research or corporate dataset.

Avoid: anything with no stated licence, anything marked non-redistributable,
anything behind terms that forbid derivative works, and anything scraped from a
source whose terms prohibit it.

If you cannot find the licence, you do not have one.

## Derived and scenario files

Both are allowed. Both must say what they are.

**Derived file** — produced by transforming a real source. Record the source it
derives from, the transformation applied, and the script that produced it. AI may
write that transformation script.

**Scenario document** — written by you to supply context a real workspace would
have. Record that it is a scenario document, who it is written as, and what it is
based on. It is **not source data** and never counts as empirical evidence.

The rule that binds both: *AI may be used to locate data or to write
transformation scripts, but it may never create the empirical source evidence
itself.*

## Provenance note format

Ship one per package, alongside the manifest:

```
<filename>
  Source:      <URL>
  Publisher:   <organisation>
  Pulled:      <YYYY-MM-DD>
  Licence:     <name, and URL to the terms>
  Attribution: <required string, if any>
  Type:        source | derived | scenario
  Derived from / based on: <files, and the transformation applied>
  Role:        <what analytical work this file does>
```

For a scenario document, `Type: scenario` and the `based on` line are the two that
matter. Their absence is what makes a self-written memo a fabrication rather than
a documented artifact.

## Size and format constraints

- ZIP files are usable for the package.
- Illegally formatted files — bad XML, invalid encodings, invalid JSON — are
  **not** within scope of "messy". Every file must load with standard tooling in
  one or two obvious attempts. Difficulty is spent on reasoning, not parsing.
- A chart may be a distractor even when the same data is supplied numerically.
  The numbers arbitrate; the chart is where a skim stops.
- File upload order does not matter.
