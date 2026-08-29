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


## The six-step start, before you claim

From the onboarding docs. **Steps 1 to 3 happen before you claim a task.**

1. **Pick a topic you are familiar with** and can use to try to stump the model.
2. **Find a dataset** that can support that topic.
3. **Think "what can I ask someone to determine from this data?"** — develop the
   question and the solution. Then think **"how can I get someone to give me the
   wrong answer?"** and use those stumps to alter the data files or the prompt.
4. **Develop your golden response** — the single deterministic answer — and the
   deliverables that will be part of your solution.
5. **Build the list of "what do I need to know about the input files and prompt to
   solve this correctly"** → this becomes your **critical components**.
6. **List the steps to go logically from question to answer**, detailed enough that
   anyone can solve it correctly → this becomes your **step-by-step**.

Note the ordering in step 3: the question and the stump are developed **together**,
and the stumps drive changes to the data and the prompt. This is the same
"trap first" principle the handbook states, expressed as a procedure.

## Brainstorming a task

Three questions to work through against your dataset:

- **What can the dataset support?**
- **When might someone (or a model) make a mistake analysing it?**
- **How can I make the evidence messy in a realistic way that might force that
  mistake?**

Then list out:

- **three to four stumping strategies** you will employ, naming what each does and
  how it takes the model away from the correct answer
- **three to five key assumptions** you will have to make in the analysis

## Two rules from onboarding

- **No duplicated or repeated tasks.** Every task needs unique prompts, data, and
  solution methodology.
- **No LLM-generated files.** If you insist on using them they must not look like
  LLM slop — spend time on formatting, wording, colour scheme. **If they look like
  LLM output they are sent back and not approved.**
