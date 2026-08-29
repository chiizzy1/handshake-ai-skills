# Supplementary Questions — a working bank

From the FAQ. **Generic examples to form your own questions from — the FAQ says
outright these should not be copied into your prompt.** Use them as shapes.

The design rule: present questions that **do not specify a method of solving the
prompt or leak the answer**, but that either **increase support for the
recommendation** or **indicate why the alternatives would not be correct**.

They carry ~60% of the rubric under 8/27, so this is where the difficulty lives.

## Eliminating the alternatives

- "Specifically, why was Option A chosen over Option B and C?"
- "Explain the single metric or criterion that allowed you to differentiate the
  winner from the runner-up."

## Threshold for determining the recommendation

- "Identify the threshold that was used for determining the recommendation, why
  was it used?"

## Sensitivity of the recommendation

- "Identify a different condition that would cause a different option to be the
  correct recommendation, and why that condition does not occur here."
- "Identify the single factor that could flip the recommendation, and why it does
  not occur in this situation."
- "Identify the specific data points or rows in the dataset that directly support
  the final recommendation."
- "Explain why the recommendation is consistent across all stated evaluation
  criteria."

## Confidence in the recommendation

- "Explain how confident you are in the recommendation based on the evidence that
  quantifies the recommendation as true."
- "Explain the gap between the top choice and the next-best choice when you
  developed your recommendation."

## Why these shapes work

Every one of them is answerable **only from the shipped files**, has a
**determinate answer**, and **a wrong analytical path gets it wrong** — the three
properties a supplementary criterion needs.

Note what none of them do: name a method, name a file, or hint which option wins.
"Identify the threshold that was used" assumes a threshold exists and is
discoverable; it does not say what it is or where it lives.

## Turning a shape into criteria density

The five levers apply directly here. A sensitivity question like *"identify the
single factor that could flip the recommendation"* becomes several criteria when
you also require the **value** of the flip point, its **unit and rounding**, and
**why it does not occur** in this data — each is a distinct determinate answer.

That is the difference between a prompt that stalls at 20 criteria and one that
clears 25.
