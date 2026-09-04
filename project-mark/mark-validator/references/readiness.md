# Readiness — the 51 checks

For each check: review the requirement, verify it against your task, add an
evidence note naming the file or step that proves it, then mark it complete.
Nothing is scored and nothing leaves the browser.

Handbook Readiness state is **not** a Handshake status and **not** an approval.

## Coverage

All **41 blocking requirements** below were captured from the "unresolved blocking
requirements" list. The other 10 of 51 were already confirmed in that session and
are the Policy and input-package rows — reproduced in the first group.

Each check names the page you fix it on, which is the fastest routing you have.

> ⚠️ **One check on this page is stale.** "Prompt adds three to five related
> supplementary questions drawn from the defined buckets" is pre-8/27 wording. The
> current contract is **3+ deliverables each carrying 3+ asks**, with no standalone
> supplementary section. Build to the current contract; the check text lags.

## Policy and input package → fix in *02 Input Files*

1. A task ships with **at least ten input files**.
2. At least **four** of the shipped files are independently necessary: remove any one and the solution can no longer be reached.
3. At least **two** of the inputs are substantial rather than token: long, dense files that take real work to read and reconcile.
4. Optional distractor files are allowed and encouraged, but never count toward the four independently necessary files.
5. AI may be used to locate data or write transformation scripts, but never to create the empirical source evidence itself.
6. Scenario documents and derived files carry explicit provenance stating what they are and how they were produced.

Rows 1 to 3 want your real count. `../../tools/mark_manifest.py` produces all
three plus the evidence note.

## Task shape → fix in *Task types*

7. Task clearly belongs to **one accepted Project Mark domain**.
8. Task has **one clear primary analytical objective** from the taxonomy.
9. Task requires **meaningful analytical reasoning** from evidence to recommendation.
10. Domain, analytical objective, and reasoning-phase tags use the **defined taxonomy values**.

## Prompt → fix in *03 Prompt*

11. Prompt asks for **exactly one deterministic main recommendation** that 10 domain experts would converge on.
12. Prompt adds three to five related supplementary questions drawn from the defined buckets. *(stale — see warning above)*
13. Prompt **leaks no methodology and no answer path**.
14. Prompt prescribes **three or more deliverables spanning at least two assigned format families**, and every golden output file matches its assigned format and filename.

## Rubric and rollout → fix in *Writing the prompt*

15. Recorded rollout clears the scoring gate: across **12 model responses, the top 2 average below 70%** against the rubric (9/01; was 50%). Reset the task before the check — populated later fields leak the golden into the models' context.
16. The generated rubric is **fixed with 25 or more criteria**, and the fellow does not edit it.
17. Rubric weighting holds: the recommendation and its critical components take about **30% across three or more criteria**, supplementary questions take about **60%**, instruction-following takes **5 to 10%**, **no single criterion exceeds 20%**, and all criteria total **100%**.

## Golden deliverable → fix in *04 Golden Deliverable*

18. The golden output **completely answers the main recommendation and every supplementary question**, and was **committed before any model was run**.
19. The golden output carries **no obvious LLM artifacts**.
20. **The five parts of the solution agree:** main recommendation, supplementary answers, step-by-step results, the determinism basis, and the golden output file.

## Trap design → fix in *Fundamentals*

> The Readiness page routes these 14 to "Fundamentals", a page that was merged
> into **Stumping essentials** in the 8/27 restructure. Work them against
> `../../mark-trap-designer/references/fairness.md` and `invalid-stumps.md`.

21. The trap targets a **named, reproducible model failure**.
22. The **expected trapped conclusion** is documented.
23. The **corrected conclusion** is documented.
24. Missing the trap **materially affects the requested decision**.
25. The trap appears in a **realistic source, field, period, or workflow**.
26. Its placement **resembles organic data mess**.
27. The trap-carrying file remains **straightforward to load**.
28. File names and formatting **do not announce the trap**.
29. **No unnecessary clue in the prompt** points toward it.
30. **A correcting fact exists inside the corpus.**
31. The antidote is **not readable in the same glance or the same analytical step as the bait**.
32. The evidence path is **discoverable using normal analytical work**.
33. **Dates, definitions, or authority rules resolve any conflict.**
34. **No outside knowledge or arbitrary assumption** is required.

## Trap composition → fix in *Composition & Recipes*

35. **At least one missed trap changes or invalidates the recommendation.**
36. Every remaining trap independently affects scope, justification, or robustness. **None is decorative.**
37. **All traps push toward the same corrected recommendation.**
38. **The result is not a knife edge.**
39. The conclusion **survives reasonable alternative cleaning choices**.

## Trap validation → fix in *Validation & Iteration*

40. **The lazy path lands on the intended wrong answer.**
41. **Removing each trap** changes the analysis or makes the answer unreachable.
42. **Defusing each trap leaves a visible trace** in the final analysis.
43. **A cold solver can locate every antidote** without designer knowledge.
44. The final trap stack has **no second defensible interpretation**.

## The trap trace table

Lives inside the Trap validation stage, on its own tab. **Fill one row per trap:**
a purpose, a location, a correction path, and an observable effect. Rows persist
in your browser.

## Final handoff to Handshake

Three steps, in this order, all done by you.

**1. Export evidence.** Available whether or not blockers remain. Both formats
carry the same readiness record: **Markdown** to read and paste, **JSON** to
re-import later.

**2. Open Handshake.** The external platform where tasks are actually submitted
and reviewed. Opening it does not submit your task and nothing is sent for you.
Your task plan and readiness checks are stored locally in the browser.

**3. Confirm submission requirements.** What a submission must contain is decided
on Handshake, not in the handbook. **Program details: submission and approval
requirements is the authoritative source** — read it against your export before
you submit.

> If a check cannot be satisfied because **the task shape itself is the problem**,
> read `../../mark-trap-designer/references/invalid-stumps.md` before revising
> further.
