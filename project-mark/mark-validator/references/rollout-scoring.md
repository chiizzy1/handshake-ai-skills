# Rollout Scoring

## The bar (8/27)

**"Stump the model" is retired.**

- Every rollout is **twelve responses**, scored against the fixed rubric.
- **You submit all 12.** The bottom 10 can be submitted without checking.
- **The gate is the top 2.** The task passes only when the two highest-scoring
  responses **average under 50%** against the rubric.

Confirmed on Stumping essentials, which is unambiguous. The Task walkthrough's
step 12 card says "Run 10 model responses" while also saying "submit the bottom
ten" and "only the top two are graded" — that card is simply wrong on the count.
Hard gate 02 and Stumping essentials both say 12.

**Aim the trap at the main recommendation.** It anchors the deterministic answer,
so a response that gets it fully correct should not fall below the pass threshold
merely by missing minor supplementary details. Supplementary questions deepen the
evaluation; they must never become artificial gotcha items or replace the central
recommendation as the main difficulty target.

Difficulty must stay honest: it comes from data shapes — forecasting, method
selection, a binding constraint, a decomposition, confirm-the-number, hold — never
from surface-read rejection or flipping a wrong number.

## The asks now carry the weight

Under the old rubric the recommendation was 50% on its own. Under 8/27 it is
**~30%**, and the supplementary asks are **~60%**.

That inverts where difficulty has to live. Asks can no longer be minor supporting
detail — they are the majority of the score, they must be **hard and
discriminating**, and a wrong analytical path should get them wrong. An ask that
is a trivial lookup is wasted weight.

## Classify before you write anything down

| Classification | Meaning | Counts? |
|---|---|---|
| **Valid analytical stump** | Misses decisive evidence, uses a provably wrong method, mishandles data, stops at a misleading artifact, or applies invalid cleaning / filtering / QC / statistical logic | **Yes** |
| **Semantic fork** | Analyzes correctly but resolves an unpinned objective or convention differently | No — a determinism defect in your task |
| **Golden wrong** | Follows a reproducible path better supported by the files than your golden | No — repair the golden |

The third one is the one people resist. The handbook is explicit: if a model
response follows a reproducible path better supported by the shipped files than
the golden, that is a **golden-solution defect**, not a response error. Repair the
task at the source.

## Never counts as a qualifying failure

- formatting-only failures
- alternative wording
- an invalid or underspecified prompt
- a broken or unsupported golden
- a missing file
- a grader or packaging failure
- a failure caused only by an arbitrary rubric interpretation

Judge the rollout as a whole. Strong-model responses should be making real
analytical errors, not stylistic ones.

## When the rollout disappoints

The fix is almost always in the **prompt or the input files, not the rubric.**

| Symptom | Likely cause | Repair |
|---|---|---|
| Models keep getting the recommendation right | The trap is not consequential, or the prompt leaks the path | Re-run Gate 3. Check the prompt for named methods, fixed windows, narrated suspicion |
| Two experts could defensibly disagree | An unpinned definition, threshold, scope, population, metric, or window | Pin it in the prompt or ship the file that arbitrates it |
| Right answer, wrong reasons, still scored high | The rubric grades disclosure, or a criterion is too loose | One review pass. Grade the result, never the narration |
| Only the strong model fails | The trap is too shallow — the weak model never got far enough to fall in | Add a layer the weak model also reaches |
| Only the weak model fails | The trap is too obvious to a capable reader | Move the antidote further from the bait, or layer a second family |

## Too easy even when correct

A task gets rejected for being too easy, even when deterministic and correctly
solved, when:

- the prompt explains the methodology
- a document states the planted trap outright
- the decisive rule is a lookup
- the complexity never changes the answer

## Reviewer verdicts

| Verdict | Meaning |
|---|---|
| `prelim_verdict` | First-pass review found the task deterministic, correctly solved, hard enough, and not a duplicate. Provisional — still needs final review before payment |
| `final_verdict` | Comprehensive review confirms difficulty and non-duplication. **98% of tasks passing prelim also pass final** |
| Approved and Paid | Appears in the Payments dashboard. Base pay first |

Every submission is reviewed within 24 hours.
