# The Nine Steps

The conceptual relationship between the three artifacts is not the build order.

**Conceptually:** the prompt commits the decision, the input files supply the
evidence, and the golden deliverables carry the reference answers.

**Procedurally:** you build in the order below, and step 2 is the one people get
wrong.

| # | Step | Output | Skill |
|---|---|---|---|
| 1 | Select the task type and objective | A chosen domain and Axis 1 objective | `mark-task-builder` |
| 2 | **Design the trap** | A recipe of layers across families, each with bait, antidote, arbiter, impact | `mark-trap-designer` |
| 3 | Assemble the input files | A package clearing the 10/4/2/3 bar with provenance | `mark-input-package` |
| 4 | Write the prompt | One recommendation, 2–5 named deliverables, 2+ asks each | `mark-prompt-writer` |
| 5 | Build the golden set | Every named file, one set of numbers | `mark-golden-builder` |
| 6 | Review the generated rubric, once | Weights correct, coverage complete | `mark-validator` |
| 7 | Run the validation gates | Reproduce · Fork · Live trap | `mark-validator` |
| 8 | Run and evaluate the rollout | 8 scored responses clearing the count gate | `mark-validator` |
| 9 | Clear Readiness and submit | A task awaiting review on Handshake | `mark-validator` |

## Why the trap comes first

A prompt written first tends to signpost the catch. It names the metric that
matters, or fixes a window that quietly rules the trap out. Write the trap, then
write the message a stakeholder would send **if the trap were invisible to them**.

## Where the loops are

The build is not linear. Two edges send you backwards, and both are expected:

- **The rubric is downstream of the prompt and the golden.** Change either and the
  rubric returns to review.
- **A rollout response that beats your golden is a golden defect.** Repair the
  golden, then the rubric, then rerun.

Never edit the prompt or the package after the recorded rollout without rerunning
it. The graded evidence has to match what you ship.

## The handbook's own numbering

The platform walkthrough presents this as nine steps and still lists step 5 as
"Prescribe exactly one output file". That is pre-8/18 and stale. The rest of its
sequence is current.
