# SUMO feasibility probe

Answering one question: can we author the Transportation workflow here? Yes.

## Install

    python3 -m pip install --user eclipse-sumo        # 1.27.1

Ships prebuilt binaries (`sumo`, `netconvert`, …) and bundles the Python tools
at `site-packages/sumo/tools`, which is where `traci` and `sumolib` live — they
are not importable until that path is added. No compile, no Homebrew.

## The workflow runs end to end

    build_network.py    nodes, edges, connections -> netconvert -> int.net.xml
    signal.py           reads the built network, classifies every controlled
                        link by turn geometry, writes a matching phase program
    run_sim.py          demand, 5 seeded runs, metrics by approach-movement

Four-leg signalised intersection, 12 movements, 100 s fixed-time cycle, 180 s
warm-up plus 600 s analysis, five seeds, SUMO default driver parameters —
the exact shape of the two delivered examples.

## The finding that matters

**Same seed twice gives bit-identical metrics.** That is what makes a golden
possible at all: the deliverable is a table of simulated numbers, and it can be
reproduced exactly.

## The finding that changes task design

**An oversaturated movement cannot be graded.**

First run: the minor protected left got 8 s of green against 140 veh/h. Delay
came out at 161 s/veh and the run-to-run spread on that movement was **27 %** —
far too wide to write a rubric band around. Every low-volume turn was unstable
for the same reason.

Rebalanced to 12 s of green and eased demand about 13 % below capacity:

| | before | after |
|---|---|---|
| worst spread (CV on delay/veh) | 27.1 % | **10.7 %** |
| minor protected left delay | 161 s/veh | 47 s/veh |
| gradable | no | **yes** |

So: **keep every movement below capacity.** A queue that does not clear each
cycle grows without a stable mean, and its delay is a different number every
seed. Check the spread before writing the rubric, not after.

## Band sizing must follow volume

Spread is not uniform across movements:

| movement class | veh in analysis | spread | band |
|---|---|---|---|
| major through | ~90–100 | 2–3 % | ±10 % is comfortable |
| minor through | ~36–39 | 3 % | ±10 % |
| turns | ~12–19 | 5–11 % | ±25 % or wider |

A single tolerance across all twelve movements either fails correct answers on
the turns or waves through wrong ones on the through movements. This is the
same lesson as the earthworks net: **the precision of a criterion has to match
the stability of the quantity it checks.**

## Two bugs, both from writing by hand what should be generated

**Turn directions swapped.** EB and WB had their left and right connections
reversed — heading east, a right turn goes south, and I had it going north.
netconvert accepted it and warned only about intersecting left turns.

**Phase state string the wrong length.** I hand-wrote a 12-character state for
a junction with 14 controlled links, and had no way to know the link order
until the network was built. `signal.py` now classifies each link by comparing
the bearing of the incoming and outgoing edges (0 through, +90 right, 270 left)
and composes the state from that.

Same principle as the take-off tasks: **generate from the artefact, never type
it in.** The network knows its own link order; ask it.

## What a real task would still need

- An input PDF carrying lane geometry, volumes, signal timing and a layout
  diagram — authored, which the kit already does for plans.
- The golden as a flat `ID | Item | Value` sheet, which is what
  `Results_Check10.xlsx` in the delivered example turns out to be.
- Per-movement bands sized by volume, as above.
- The two honesty criteria worth copying from the delivered rubric: whether the
  results were certified by a licensed professional (no), and whether metric
  values were identical across every movement row (no — a fabricating model
  tends to repeat them).
