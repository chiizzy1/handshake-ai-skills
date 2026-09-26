# Project Neutron — authoring findings

What we have established by building, not by reading the handbook. Everything
here was observed; nothing is inferred from the training modules.

**Nothing here has been through platform review.** No Neutron task has been
submitted, so none of this is validated against what a reviewer accepts. Treat
it as tooling knowledge, not project guidance.

## The method that works

**Define the artefact so the answer is known exactly, then render it into
something the model must measure.** We are the source, so no figure is ever
hand-typed and the golden cannot drift from the rubric.

1. **Truth** — define geometry, placement or surfaces analytically; compute the
   quantities from that definition.
2. **Render** — draw to a raster with a graphic scale bar in the same
   coordinate system, carrying no dimensions and no answer.
3. **Verify** — measure the raster back and confirm the truth is recoverable
   inside the rubric band.
4. **Deliver** — build the golden and the rubric from the same truth.

## Five findings

### An area check that sums to the right total does not prove the parts are right

A site partition closed to 1e-12 while every individual zone was wrong. Each
ring walked both of its divider curves in the same direction, winding the
polygon as a bowtie; shoelace cancelled the signed lobes and the closure check
passed. A renderer fills a bowtie completely differently, which is the only
reason it surfaced. `neutron_sheet.is_simple()` screens for this.

### Verify against the artefact the model receives

That bug was invisible in the geometry and obvious in the JPEG. Any check that
runs on the source rather than the delivered raster can miss the defect that
matters.

### The precision of a criterion must match the stability of the quantity

Three separate cases, one rule:

- **Earthworks net.** 15 m³ from a 3,217 m³ cut and a 3,202 m³ fill. A solver
  5 % out on each — inside any fair band — lands anywhere in a 300 m³ window.
  Grade cut and fill with bands; grade the balance as a bound on the magnitude
  of the net, never as a value.
- **Traffic movements.** Major through movements held to 2–3 % across seeds;
  low-volume turns ran 5–11 %. One tolerance across all twelve either fails
  correct answers on the turns or passes wrong ones on the through movements.
- **Measured areas.** Pixel measurement recovered every region within 1.05 %,
  so a ±2 % band is fair. Tighter would not be.

Check the spread before writing the rubric, not after.

### An unstable quantity cannot be graded at all

In the SUMO probe a minor protected left ran oversaturated — 8 s of green
against 140 veh/h — giving 161 s/veh delay and a **27 %** swing between seeds.
Rebalancing the signal and easing demand ~13 % below capacity dropped the worst
spread to **10.7 %**. A queue that does not clear each cycle has no stable mean.
Design the scenario so every quantity is stable, then grade it.

### Generate from the artefact, never type it in

Every defect found while building these came from hand-writing something the
artefact already knew:

- A mojibake table whose rendering of `”` ends in an unprintable `0x9D`,
  invisible when copied — 8 records in 22,666 came out different on rebuild.
- A signal phase state string 12 characters long for a junction with 14
  controlled links, written before the network existed.
- Turn directions reversed on two approaches, because "right turn" was typed
  rather than derived from bearings.

The fix in each case was the same: read the artefact and derive the value.
`neutron_signal`-style classification (bearing in, bearing out, 0 through,
+90 right, 270 left) is the pattern.

## Rubric rules, current

Enforced by `neutron_deliverable.Rubric.report()`:

| Rule | Value |
|---|---|
| Items | 20–100 |
| Weights | 9, 7, 5, 3, 1 and their negatives only |
| Negative share | at most 35 % |
| 9-weight share | 10–15 % |
| Golden score | at least 95 % |

**The published Golden Examples violate these.** They show weights of +10, +8,
+4, +2, −8 and rubrics of 120 items, and the Structural PDF carries a note
against one of them: *"the number of rubric items exceeds our current maximum
of 100."* Follow the module, not the examples.

Avoid enumeration padding: one criterion per grid cell or per window inflates
the count without adding rigour. Grade representative items and the totals.

## Observed inconsistencies in the supplied examples

**The GIS evacuation example does not match its own description.** The write-up
calls a ~90° rotation the decisive trap (weight 9, −7 penalty) and says the
golden carries a north arrow in the upper-right. The supplied `EvacSample1.png`
and `Golden_Evac1.png` are the same orientation — comparing them directly gives
a mean difference of 14.6 against 49.0 when one is rotated 90° — and the
golden's upper-right holds the directions block, not a north arrow.

**That example's input is a Google Earth capture**, watermark and imagery date
visible. That is third-party imagery of a real place, which the input rules say
must not be used ("not findable online"). Either the rule is applied loosely to
self-made captures or the example predates it. Author synthetic sites instead.

## Tooling

`eclipse-sumo` 1.27.1 installs from PyPI with prebuilt binaries and bundles
`traci`/`sumolib` under `site-packages/sumo/tools`. No compile needed.

Not installed, and required for seven of the eleven workflows: FreeCAD,
CalculiX, IfcOpenShell, QGIS.

---

## From the rubric and stumping modules (added 2026-09-26)

Source: `Understand how rubrics work/` in the workspace. These are the
platform's own rules, and several of them invalidated work we had already
called finished.

### Pull at least two difficulty levers

Breadth and chaining slow a model down but rarely break it. The six levers:

| Lever | What it does |
|---|---|
| Conflicting constraints | two rules that cannot both be fully satisfied |
| Implicit variables | a one-line detail that flips the answer, not called out |
| Data reconciliation | sources that do not fully agree |
| Domain-knowledge outliers | a value that looks normal but is clearly non-default |
| Source-of-truth tension | two sources describe one feature; the prompt names which governs |
| Strict deliverable spec | exact format, columns, units, files |

There is also a twelve-item catalogue of how models actually fail on drawing
sets — wrong controlling dimension, misreading views, miscounting, reversing
a sequence, claiming detail not shown, unsupported verdicts. A strong task
gives a careless solver the chance to fall into one and makes it cost points.

### Never announce the trap

*"The prompt reads like a normal engineering request; the difficulty lives in
the artifacts."* Our first Kilmartin prompt carried a measurement rule
explaining exactly how to treat the existing-to-remain finish. That turned the
trap from "will it read the status column" into "will it follow an
instruction". The table rules already pinned it unambiguously; the explanatory
bullet was pure announcement and was cut.

The related rejection pattern is **solution encoded** — the prompt revealing
the reasoning. The line to hold: stating a *measurement convention* is
specification, and the delivered Cloud Park example does exactly that. Naming
the controlling value, or explaining how a category is handled, is solution.

### No fact is scored twice, and negatives describe what a grader can see

Two rules we broke in the same rubric:

- **Double jeopardy.** We had `+7 Excludes F-05 from the new total` alongside
  `-9 Includes F-05 within the new total`. One fact, scored twice. Write every
  criterion as a positive first, then convert a few to negatives — starting
  from scratch on negatives is how the duplicate appears.
- **Absence phrasing.** `-7 Omits F-05 from the workbook entirely` asks a
  grader to prove a negative. Negatives must name something observable:
  *"states the identical area value for two or more item codes"*,
  *"states a negative value for an area"*.

### All five weight bands are specified, not just the 9s

9s 10–15 %, 7s 10–20 %, 5s 15–25 %, 3s 15–25 %, 1s 15–20 %.
`neutron_deliverable` originally checked only the 9s and passed a rubric whose
7s sat at 24 %. It now checks every band.

### Other rejection patterns worth holding

**Non-timeless framing** — anchor any date with a year. "Before the tender
closes on Friday" rots on the next run and is a listed rejection reason.

**Excessive volume** — scope to the features that control the outcome.
Measuring every window on fourteen floors adds effort, not reasoning.

**Overconstraining the deliverable** — specify content, columns and units;
lock a file *template* only if a downstream consumer truly needs it.

### Environment failures are usually not your task

Rollouts that will not generate, truncated output, a run marked successful
that produced nothing usable, and missing evaluation controls after a prompt
edit are all known environment-side issues. Report with the task ID rather
than rewriting. Unsupported input formats have crashed the environment
outright — images and PDFs with embedded images only.

---

## The sandbox toolset (Available Tools, 22 August 2026)

**The tool list is the model's sandbox, not your machine.** Nothing on it needs
installing locally. You author the golden "in whatever software you are
fastest in"; the hard rule is on the model's side — the agent must be able to
complete the workflow with these tools, and a task must not require anything
outside them.

Available: Python 3.14.3 · NumPy · SciPy · pandas · **openpyxl** · NetworkX ·
scikit-image · OpenCV · Rasterio · **FreeCAD 1.0.0** · **IfcOpenShell 0.8.5** ·
pyproj · GDAL/PROJ/GEOS · **QGIS 3.40.6** · **SUMO 1.18.0** · AequilibraE ·
**Gmsh 4.13.1** · **CalculiX 2.23** · FEniCSx · LibreDWG 0.13.4.

Three exclusions to design around:

- **AutoCAD is never available.** "Questions requiring AutoCAD-only or
  ODA-specific behaviour are not supported." DWG/DXF work goes through
  LibreDWG. If a CAD workflow is ever needed locally, FreeCAD is the free
  tool the sandbox itself uses.
- **meshio is in progress** — no task may depend on it or on a mesh conversion
  that needs it.
- **QGIS SAGA processing is in progress** — native and GRASS only.

Use **AequilibraE** rather than SUMO when the question is network-level demand
rather than individual vehicle movement.

### Version drift is a real risk on the SUMO route

The sandbox runs **SUMO 1.18.0**. PyPI does not publish 1.18.0 at all — the
run either side of it is 1.17.0 or 1.19.0, and our probe installed 1.27.1,
nine minor versions ahead. Car-following defaults and output fields have moved
across that range, so a golden produced locally on 1.27.1 may not be the
numbers the sandbox produces.

Before authoring a SUMO task: pin 1.17.0 or 1.19.0, and treat the per-movement
tolerance bands as absorbing version drift as well as seed variance. Do not
assume a locally reproduced figure is the sandbox's figure.
