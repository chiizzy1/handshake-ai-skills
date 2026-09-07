> Historical reference: examples and earlier handbook wording below must be
> read under [the operative rules](../../shared-references/canonical-rules.md).
> New tasks use the September 5 specification. Old quotas, model-failure rates,
> compulsory noise/burial, and platform mechanics below are not current directives.

# Fairness — the canonical statement

Four rules, always in force, on every trap, on every page in Validate.

| Criterion | Meaning |
|---|---|
| **In-corpus antidote** | Every deception has a correcting fact inside the files. Supersession must be reconstructible from dates and documents. |
| **Deterministic outcome** | Ten competent analysts reach the same recommendation. All defensible cleanings converge. |
| **No parsing puzzles** | Every file loads with standard tooling in one or two obvious attempts. Difficulty is spent on reasoning, not input and output. |
| **No fabricated source data** | No LLM-generated files, no augmentation, no model-written memos. You may write scenario documents yourself, but a self-written memo is a scenario document, not source data, and it is recorded as such. |

## Discoverable

The model must be able to find — inside the prompt, the files, and standard domain
knowledge — everything it needs to reject the wrong path.

A fair trap **may** ship evidence that encourages the wrong reading. The material
that overturns it must be present.

Not discoverable when:

- a required rule or definition is absent
- a necessary file was never shipped
- the analyst has to guess an unstated threshold
- the deciding fact lives outside the provided materials

**The strongest traps live between files:** reconciling a summary against
authoritative raw records, joining at the wrong grain, a definition buried in
supporting documentation, one file that silently supersedes another.

## Consequential

Catching the trap has to matter. If the recommendation, an interpretation, or a
decisive intermediate result would be identical whether or not the model corrects
course, the trap is **decorative**.

Gate 3 tests this mechanically: repair one trap at a time, leaving the others in
place, and re-solve. A trap whose repair changes nothing is decorative. A trap
that only catches careless reading or an absurd analytical choice is not a trap.

## Deterministic

Ten competent analysts, using the files and accepted domain knowledge correctly,
land on the same call.

If the final answer changes depending on a reasonable but unpinned choice of
metric, scope, population, threshold, time window, or definition, the task is
**underspecified**, not hard.

The winner must also survive estimation variation: confidence intervals, forecast
uncertainty, and reasonable metric choices. **A knife-edge winner that needs one
exact computation fails.**

## Fair

Semantic ambiguity, missing information, and arbitrary gotchas are disqualifying
even when they make a task hard.

The prompt and supporting documents must never narrate the trap: never say which
file is misleading, which metric is wrong, which join to avoid, or which
conclusion is expected.

### No complexity for its own sake

A task is not harder because it has more files, rows, or formats. Every piece of
material has to serve a realistic analytical purpose.

Irrelevant files · duplicated information · arbitrary noise · volume that only
creates search burden — all count **against** fairness, not for difficulty.

## Valid failure versus invalid difficulty

| Topic | Valid | Invalid |
|---|---|---|
| Source of the failure | A genuine analytical mistake: wrong cohort, invalid method, missed reconciliation | An undefined term, unstated threshold, or missing fact |
| What correcting it looks like | Recovering evidence already in the workspace and revising the recommendation | Guessing at a definition nobody pinned down |
| Whether experts would agree on the fix | Every competent analyst converges on the same corrected answer | Equally reasonable experts could defensibly disagree |
| What ships in the prompt | Evidence that makes the correct path findable | A hint, or narration, of what the trap is |

## Know your enemy — the twelve model failure behaviours

**These behaviours are reliable and reproducible. Design against them rather than
against intelligence.**

> **A good task requires the model to do at least three of these correctly, and
> each non-default behaviour roughly halves the pass rate.**

That is the most useful quantitative rule on the project: three non-default
behaviours ≈ one eighth the pass rate. It is why layering works and why a single
trap gets caught about half the time.

**The wrong path has to be plausible, never careless.** The behaviours in prose:

- the familiar metric instead of the appropriate one
- an aggregate trusted without checking the population beneath it
- a default join
- a skipped QC rule
- correlation read as causation
- an unsuitable validation strategy
- an authoritative-looking summary that conflicts with the underlying records

> **The numbered list of twelve no longer exists.** The Fundamentals page was
> merged into Stumping essentials in the 8/27 restructure —
> `/trap-design/fundamentals` now redirects there — and the list was condensed to
> the prose above. The `Targets 02 … 08 …` fields on every trap, and the FAQ's
> "Stumping 2–3 / 5, 10 / 6, 8, 9" references, are orphaned pointers to content
> that was compressed away.
>
> **Do not invent the numbers.** If a user asks what "Targets 04" means, say the
> numbering was retired and give the prose behaviour instead.

### When relevant: forecasting and predictive modeling

Predictive work follows the same four fairness rules. **The trap is a
methodological choice, never the mere requirement to fit a sophisticated model:**

- target leakage discoverable from timestamps
- a split that ignores time
- the wrong forecast horizon
- an evaluation metric that flatters the losing model
- a structural break inside the training window
- subgroup performance hidden by a headline score
- poor calibration
- a correct prediction translated into the wrong decision

**Leakage and validation-scheme errors are graded as analytical failures, not
style notes** (C13, B17). A reported metric the run never produced is a
reconciliation failure (E12).

## Measuring difficulty

Wall-clock solve time is **not** evidence.

**Evidence coverage** — count the inputs a correct answer must actually touch, and
confirm the relationships between them are recoverable. If the recommendation is
reachable from fewer than the load-bearing set, the task is under-built.

**Decision materiality** — for each trap, state what the recommendation loses when
it is missed: the decision itself, its scope, its justification, or its
robustness.

## Preflight

Confirm all five before going looking for a trap.

- [ ] The failure is a genuine analytical or methodological mistake, not a different final sentence
- [ ] No reasonable expert could defensibly choose a different definition, threshold, or scope and still be right
- [ ] The evidence that corrects the wrong path is present in the workspace, not narrated in the prompt
- [ ] A careful analyst using the materials correctly always lands on the same recommendation
- [ ] Catching the trap changes the recommendation or a decisive intermediate result, not just wording
