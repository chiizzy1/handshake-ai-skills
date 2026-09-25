# Project Neutron — CivE/Arch

Tooling for authoring Project Neutron tasks. **No skills yet, deliberately.**

## Status

| | |
|---|---|
| Tasks submitted | 0 |
| Tasks accepted | 0 |
| Workflows proven buildable | 4 of 11 |

Nothing here has been through platform review. The tooling is validated against
its own gates; the *project* guidance is not validated against anything, which
is why this directory carries tools and findings rather than skills.

That is a deliberate correction of how Project Mark went: an elaborate skill set
was written against rules that moved twice, before a single task was accepted.
The skills here get written once a task comes back approved, and they will
describe what actually passed.

## Contents

    tools/neutron_sheet.py        drawing sheet: frame, title block, graphic
                                  scale bar, north arrow, callouts, hatch
                                  palette; shoelace and a self-intersection
                                  screen
    tools/neutron_deliverable.py  golden workbook writer; Rubric builder that
                                  enforces the current weight, count and
                                  negative-share rules
    tools/neutron_verify.py       mask render, scale-bar calibration, and the
                                  measure-back fairness check

    shared-references/authoring-findings.md   what building these established
    shared-references/sumo-feasibility.md     the SUMO probe in full

## Where the task work lives

Rehearsals and task packages sit in the workspace, not here, matching the
`project-mark` / `MARK-TASKS` split:

    HANDSHAKE-AI/NEUTRON-TASKS/
      dryrun-01/   area take-off      (Halstead Green)
      dryrun-02/   count take-off     (Wexford Quay)
      dryrun-03/   volume take-off    (Ardglass Depot)
      sumo-probe/  transportation feasibility

Each imports the kit from `tools/` by relative path.

## The eleven workflows

| Discipline | Workflow | Covered |
|---|---|---|
| Construction | take-off / bill of quantities | ✅ `dryrun-01`, `dryrun-02` |
| Construction | earthworks balancing and mass haul | ✅ `dryrun-03` |
| Transportation | corridor simulation (SUMO) | ✅ probe |
| Transportation | roadway geometry and superelevation | ✗ needs design manuals |
| Architecture/BIM | drawing review against a governing document | ✗ |
| Architecture/BIM | drawings to revised drawing | ✗ needs FreeCAD BIM |
| Structural · Arch | drawings to 3D model (IFC) | ✗ needs FreeCAD, IfcOpenShell |
| Structural | drawings to model plus analysis | ✗ needs CalculiX |
| Structural | design-load calculation and redesign | ✗ |
| GIS | least-cost path from imagery | ✗ needs QGIS |
| GIS | road-attribute and OD package | ✗ needs QGIS |

## Before writing any skill here

Read `shared-references/authoring-findings.md`. It separates what we observed
from what we assumed, and the second list is still empty on purpose.
