---
name: handshake-ads-overall-suitability
description: Evaluate Handshake Ads Creative overall ad suitability comparisons. Use when a task shows a seed image, the creative direction, an ad brief with advertiser/audience/objective and supplied copy, and two finished ad images (Response A and Response B), and asks which image is more suitable as an ad for a high-end marketing campaign; when the buttons read Strongly Prefer A, Slightly Prefer A, Tie, Slightly Prefer B, Strongly Prefer B; when the task says ads creative, overall suitability, or Compare Two Ad Images Overall Suitability.
---

# Handshake Ads Overall Suitability

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/rubric.md` in this skill folder.
2. `references/worked-cases.md`, six graded pairs with the images in `references/examples/`.
3. `HANDSHAKE-AI/ads-creative/vs-1786660967-260813-ads-creative-i2i-q0-overall-ad-suitability.md`, the full guideline.

**Read `references/worked-cases.md` before rating.** In all six of its bad examples the annotator rated
a first impression and skipped the scan, and the observation they rated on was usually true.

The question: **which image is more suitable as an ad for a high-end marketing campaign?**

**Judge the whole ad as one thing. Nothing visible is out of scope.** The picture, the overlaid text
and graphics, where that text came from, and how it all works together all count.

> A gorgeous photograph with an invented price or a garbled headline is a broken ad. A plain
> photograph with clean, grounded text may be the more suitable one.

## Sibling Task, Opposite Scope

This is the **Q0** question in the Ads Creative I2I set. Its sibling `handshake-ads-visual-appeal`
(`project-hedgehog/handshake-ads-visual-appeal/SKILL.md`) is the **Q4** question, and the two have
**opposite scope rules**. Do not mix them up.

| | Q0 Overall Suitability (this skill) | Q4 Visual Appeal |
|---|---|---|
| Question | More suitable as a high-end campaign ad? | Which picture is more striking to look at? |
| Overlaid text | **In scope, and usually decisive** | Explicitly out of scope |
| References shown | Seed image, creative direction, ad brief | None |
| Buttons | Strongly/Slightly Prefer A, Tie, Slightly/Strongly Prefer B | Clearly/slightly more appealing, Similarly good/bad |
| Rejects | 2 reasons | 3 reasons, including mixed mediums |

If the UI shows no seed and no brief, and the buttons say "more appealing", you are in the wrong skill.

**The trap the two tasks share.** Both modules ask a knowledge-check question about a stunning
photograph whose overlay carries a spelling error, and the correct answers are opposites. On Q4 the
overlay is out of scope and you judge the picture behind it. **Here a text defect can decide the item on
its own.** If you have been working Q4, this is where the habit will bite.

**Third sibling.** The same Ads Creative outputs are also judged on **relevance**
(`handshake-ads-relevance`): one original ad against one generated ad, Pass or Fail, with failure reasons.
There, rendering defects are out of scope but any change to the product's body is a Fail.

**Text style sibling.** The same outputs are also judged on **overlay design** (`handshake-ads-text-style`,
Q6): only the text and graphics laid over the picture, on layout, placement, typography and colour.
There, spelling is out of scope and the picture is out of scope, and a sixth button covers pairs with no overlay.

## What "High-End" Means

**High-end refers to the ad's execution, not the product's price.** A $2 sponge can have an ad that
feels expensive, with restrained composition, clean typography, and professional light. A luxury watch
can have an ad that feels cheap.

**The test: would a demanding brand team sign off on running this image with minimal or no
adjustments?** An image that clears that bar is **campaign-ready**. That is the bar each response is
judged against.

A brand team would not sign off on a claim their client never made. **Invented specifics fail the test
however polished the image is.**

## The References

Three references appear above the responses:

1. **Seed image.** The product or the original ad the model started from. It tells you what the ad is for.
2. **Creative direction.** The instructions the model worked from. Long directions collapse behind "Show more".
3. **Ad brief.** Advertiser, audience, objective, and the copy the advertiser supplied: headline, description, primary text. Empty fields read "(none)" or "(not provided)". **About half of all briefs have no copy at all.**

The UI lays these out as a seed panel on the left with a magnifier, and stacked
`CREATIVE DIRECTION THE MODEL WAS GIVEN` and `AD BRIEF` panels on the right. The rating row is labelled
**Overall Ad Suitability**, and the comment field is **Open Feedback, minimum 100 characters**.

They exist to tell you what the ad was meant to be and **where any text on a response could have come
from.** That second use is the important one.

Two things they are **not** for:

- **Not for grading adherence to the direction.** Another task measures that. A response that ignores part of the direction but works as an ad can still win. A response that follows every clause can still lose. When one response follows the direction closely and the other ignores half of it but is the cleaner ad, **the direction pushes your answer neither way.** It is not a merit for the follower and not a counterweight that forces a tie. Judge the two finished ads.
- **Not for grading whether the seed's text was kept.** Dropping a line, a badge, or a button from the seed is not a flaw here. **Garbling it is.** The same goes for the brief: **a response that never renders the brief's headline has not failed.** Nothing requires the copy to appear.

## Text: Grounded Or Invented

This is the heart of the task. Before judging polish, trace every piece of text on both responses.

**Grounded** means the text appears on the seed, in the brief (headline, description, primary text), or
is the advertiser's name. **Grounded text is fine wherever the response puts it, including on a phone
screen or a sign inside the scene.** Placement is not what makes text a problem. Origin is.

| What you see | Verdict |
|---|---|
| Text from the seed, the brief, or the advertiser's name | Grounded. Fine anywhere. |
| **Invented specifics**: prices, discounts, percentages, statistics, specs, model names, dates, awards, quotes, **and any other claim with a number in it** | **Dealbreaker** |
| A brand name that is neither the advertiser's name nor a brand visible on the seed | **Dealbreaker.** Also an invented specific |
| **Invented generic lines**: "No hassle rentals", "Reliable, affordable" | **Serious flaw.** Outweighs any polish edge, but not disqualifying on its own |
| **Generic calls to action**: "Shop now", "Learn more", "Book today" | Fine |
| Text in a language matching neither the seed's text nor the brief | **Dealbreaker**, whatever the line says |
| Incidental prop text making no claim: a call timer, a clock reading, a keyboard label | Neither grounded nor invented. Ignore it |

**Grounding has three independent sources: the seed, the brief, or the advertiser's name.** A line needs
only one. When a retailer advertises another company's product, a maker's brand visible on the seed is
grounded even though it is not the advertiser's name. A third brand appearing in none of the three is an
invented specific.

**A claim with a number in it is the fastest test for a specific.** If a line carries a figure and that
figure is not on the seed or in the brief, it is a dealbreaker.

Rules that catch people out:

- **A slot the direction asked for does not ground the value.** If the direction says "add a price" and the model adds "$49", the slot was requested but the number was invented. The value must come from the seed or the brief.
- **A chart or graphic does not launder a statistic.** An invented percentage or statistic is a specific even when it sits inside a chart, a badge, or an infographic.
- **You can check most of this without reading the language.** Letterform quality, placement, where marks point, and product identity are all language-independent. Use the direction and brief to know what the message is meant to be.
- **The language rule is symmetric.** No language is privileged. An English tagline on a Portuguese seed and brief fails exactly as a German slogan fails on English sources. It is the mismatch that disqualifies, not the identity of the language.
- **Non-Latin text is never a reason to reject.** The dealbreaker is a language that matches neither the seed nor the brief, not an unfamiliar script. **Judge its letterforms and placement, and check the parts you can read.**
- **Prop text stops being incidental the moment it makes a claim.** A call timer or a clock reading is ignorable. The same phone screen showing a price, an offer, a rating, or a message gets sorted like any other line.
- **Targeting settings are not copy.** Country codes and an age range along an edge of the frame are campaign settings, not ad text. Do not sort them as claims and do not rest the call on them.

## Dealbreakers

Any one of these means the response is not campaign-ready.

**Text and claims**

- An invented specific (see the table above).
- Text in a language matching neither the seed nor the brief.
- Garbled, misspelled, illegible, or duplicated text. **Fine print and logos included.**

**Product identity**

- The product's color, shape, badge, logo, or model differs from the seed.
- The product warped, melted, or missing.
- Lighting that warms or cools the whole scene is **allowed**. That is grading, not identity change.

**How to tell a recolor from a warm grade:** check the background and any white object in the frame. If
the backdrop and the whites shifted too, it is a grade. **A grey shoe turning tan while the backdrop
stays neutral is a recolored product**, and that is a dealbreaker: the ad now sells something the
advertiser does not have.

**Rendering and composition**

- Mangled hands, faces, or limbs. Cloned people.
- Text or graphics covering the subject or the product.
- Graphics whose logic attacks the product. **Follow where every mark points.** A comparison layout collapsed onto one photo puts the ad's own red X on the product it is selling. You do not need to read the language to check this.
- Heavy blur or smearing where a viewer would look.

## Answer Anchors

| What you found | Your answer |
|---|---|
| One response is campaign-ready and the other has a dealbreaker | Strongly Prefer the clean one |
| Both could run, and several clear advantages point the same way | Strongly Prefer that one |
| Both could run and one has a polish edge you can name | Slightly Prefer that one |
| One carries an invented generic line and the other does not | Slightly Prefer the clean one |
| Both have serious problems and one is clearly closer to usable | Slightly Prefer that one |
| No dealbreakers and no edge you can name | Tie |
| Both fail and neither is closer to usable | Tie |

**Strongly requires the winner to be actually clean, not merely better.** A dealbreaker on one side does
not by itself earn a Strongly. If the other side also has a problem, you are in the "both have serious
problems and one is closer to usable" row, which is a **Slightly**.

Worked case from the guideline: the brief has no copy, A adds "Fast, secure, rewarding" (invented
generic line, serious flaw), B adds "0% fees for 12 months" (invented specific, dealbreaker). Both
otherwise clean and equally polished. **The answer is Slightly Prefer A**, because A is not
campaign-ready either. Name both lines in the feedback.

**The contrasting case, where Strongly is right.** A is a gorgeous lifestyle shot captioned "Rated #1 by
2,000 customers"; the seed has no text and the brief has no copy. B is a plain product shot carrying
only the advertiser's name. **Strongly Prefer B.** "#1" and "2,000 customers" are invented specifics,
and B's only text is grounded with nothing else wrong, so B is the only campaign-ready response. Name
the invented line **and where you looked for it**.

Put the two side by side: what makes the second a Strongly is that the winner is clean, not that the
loser's failure is worse.

**Tie is a normal answer on this task.** Many pairs are close and expert reviewers call ties often. If
the two responses are interchangeable after a proper scan, answer Tie rather than hunting for a
tiebreaker.

If you pick a side, your feedback must name the reason. If you cannot name one, your answer is Tie.
**Do not force a preference to avoid a tie, and do not tie to avoid looking closely. Both patterns show
up in review.**

**Polish edges**, worth a Slightly Prefer: cleaner composition with one focal point, better lighting and
color harmony, consistent and aligned typography, a scene that fits the product, a "ready to ship" feel.

**Not an edge:** sharpness you can only see at maximum zoom.

**Zoom is for checking, not for finding edges.** Use it to confirm text is readable and detail intact.
Once everything reads correctly in both, a bit more resolution or slightly sharper type is not an edge.
**If you need 200% zoom to justify a preference, answer Tie.**

## Mandatory Workflow

The on-screen instruction, verbatim:

> "Pick the image that would work better as a polished ad in a high-end campaign. The seed image, the
> creative direction, and the ad brief tell you what this ad is for. An output is not campaign-ready if
> it invents specific claims (prices, specs, offers) that appear in neither the seed nor the brief,
> changes the product's color or identity, or garbles its text, however polished it looks. Then judge
> the whole ad: composition, lighting, realism, text quality, overall polish."

**Plan on one to two minutes per item.**

1. **Read the brief's copy fields first.** Headline, description, primary text. Note what copy exists, and note when the brief has none. You cannot trace text without this.
2. **Look at the seed.** What is the product, what color, what shape, what badge, what text does it carry?
3. **First impression at full size** on both responses.
4. **Dealbreaker scan, 30 to 45 seconds, on both.** Read every word on each response and sort it: on the seed, in the brief, the advertiser's name, or invented. Compare the product with the seed for color, shape, badge, model, using the background and white objects to separate a recolor from a grade. **Zoom in on hands, faces, fine print, and logos.** Look for melted or duplicated detail and heavy blur. Click an image to magnify it. **Scan both images with the same care.**
5. **Answer using the anchors.** **If the scan found nothing, your first impression stands.**
6. **Write one or two specific sentences saying what decided it.**

The scan is longer here than in the visual-appeal task for a reason. Tracing text takes time, and the
text is usually what decides the item.

## Do Not

- Reward a response for stating specs, prices, or offers. **Check where each one came from first.** More information is not better information.
- Penalize a response for dropping a line from the seed or for ignoring part of the direction.
- Penalize an intentional style (illustration, black-and-white, a bold graphic look) for not being photorealistic. Penalize style only when it reads as an accident.
- Judge the product's price. A budget product can have a high-end ad.
- Reject ugly or flawed images. Your vote is how you record those.
- Hunt for tiny differences. Interchangeable after a proper scan means Tie.

## A Dealbreaker Is Not A Reject

Keep these apart. **A dealbreaker is recorded through your vote**, by preferring the other response. It
never sends you to the reject buttons.

The reject buttons exist only for a failed load or inappropriate content. Garbled text, an invented
price, a recolored product, a language mismatch: all dealbreakers, all voted on, none rejected.

## Rejections

Only two reasons here, fewer than the visual-appeal task:

- **Image did not load.** A response or the seed fails to load.
- **Inappropriate content.** Nudity or sexually explicit poses, hate symbols, graphic violence.

Swimwear or underwear is not a reason to reject. There is **no mixed-medium reject** on this question.

## How to Write the Feedback

**The field is "Open Feedback", minimum 100 characters.** One or two specific sentences clears it
comfortably. The count is a floor, not the bar: the bar is specificity, and a padded 100 characters
fails review the same way a vague one does.

**Name the element, say where it is, say where its text came from if text decided it, and why it decided
your answer.**

The guideline's model fragment is *"A's price appears in neither the seed nor the brief"* against the
useless *"A has more information."* Note the good one is only 52 characters, **below the submit floor**.
It shows the standard for specificity, not a complete submission.

### The shape that clears 100 characters

Two clauses, one per response:

> **What the loser did, and where its text came from. Then what the winner does right.**

That is how every guideline exemplar is built, and it lands between 120 and 170 characters without any
padding. Writing only the loser's failure leaves you short and hides the fact that you checked both
sides.

For a tie, the same shape inverted: what both do well, then what you looked for and did not find.

### Rules

- **Persona:** a careful person explaining what they saw, not an evaluator filing a report.
- **Name the thing.** The headline, the price, the badge, the hand, the logo. Not a category word.
- **Trace the text out loud.** When text decides it, say where it came from or that it came from nowhere.
- **Short sentences. Periods.** No em dashes.
- **Semicolons are fine here.** The house style across these skills bans them, but this task's own exemplars use them ("...and render cleanly; nothing separates them"). The task guideline outranks the baseline. A period does the same work if you prefer one.
- **Use "while" instead of "whereas"** when contrasting. The exemplars lean on "while" heavily.
- **Say the trace, not the label.** Write "appears in neither the seed nor the brief", not "is an invented specific". "Dealbreaker", "campaign-ready", "grounded", "polish edge" are your thinking words. The exemplars never use them.
- **Do not narrate your process.** "Text does not decide this pair", "after running the scan", "on the grounding check" describe what you did, not what you saw. If both sides are equal on text, say so in passing and move to what actually differs.
- **Write it as you would say it to someone next to you**, looking at the two images. Plain words for plain things: the title, the grey boxes, the discount line, the props round the edge.
- **Avoid absolutes.** "Perfect typography" becomes wrong the moment someone zooms in.
- **No AI power words.** Delve, meticulous, seamlessly, striking visual narrative.
- **Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "it is evident that," "exhibits," "the aforementioned."
- **Never pad to reach 100.** If you are short, you have named one side only. Add what the other response does, not more adjectives.

### Good Examples

The guideline's own pair:

```markdown
Response B's headline is the brief's headline and renders crisply, while Response A prints "From $19/month", which appears in neither the seed nor the brief.
```

```markdown
Both keep the seed's copy intact, add nothing, and render cleanly; nothing separates them. Faces, hands, and the logo are clean on both.
```

```markdown
Response A adds a 40% off badge that appears on neither the seed nor the brief, so it cannot run. Response B keeps the brief's headline and sits cleanly in the top left.
```

```markdown
Both keep to the brief's copy, so it comes down to the layout. Response B's headline lines up with the product and leaves the bottle clear, while Response A's caption sits right across the label.
```

```markdown
Neither could ship. Response A garbles the headline into two overlapping lines and Response B changes the bottle from green to amber, so both fail on their own count.
```

```markdown
Both use only the brief's copy, both are lit the same way, and the type is clean on each. Nothing in either one stands out as better.
```

Every one of those clears 100 characters on content alone, between 126 and 169.

### Bad Examples

- *Bad (rewarded an invention):* "Response B has more information about the product." More information does not help when it comes from nowhere. Say where each line came from.
- *Bad (rewarded an invention):* "Response A is better because it shows the price and the discount." Trace those first.
- *Bad (graded adherence):* "Response B ignored the direction's request for a sunset background." That is another task.
- *Bad (penalized a drop):* "Response A left off the seed's badge." Dropping is allowed. Garbling is not.
- *Bad (judged the product):* "This whole product category looks cheap." Judge the execution.
- *Bad (no location):* "A's text is wrong." Say which text and where it came from.
- *Bad (rubric voice):* "Response A contains an invented specific and is therefore not campaign-ready." Say what the line actually says and where you looked for it.
- *Bad (padded to length):* "Response B is the stronger, more polished, more professional and more suitable choice for this campaign overall." Long, and names nothing.
- *Bad (process narration):* "All the copy on both responses traces to the seed, so text does not decide this pair, and the call rests on execution." Says what you checked, not what you saw. Try "Both use the same text off the seed, so the look is what separates them."
- *Bad (stiff register):* "Response A demonstrates a clear focal hierarchy with a coherent perimeter arrangement." Try "Response A keeps everything in one centred block ringed by first aid and desk props.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Brief copy:** <headline / description / primary text, or "none supplied">
**Seed:** <product, color, shape, any text it carries>

**Response A:** <text traced, product identity checked, dealbreakers found>
**Response B:** <same>

**Answer:** <Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B>

**Feedback:**
<one or two sentences>
```

## Calibration

Six graded pairs are in `references/worked-cases.md`. The correct answers were four Strongly and two
Ties, with **no Slightly among them**, while five of the six wrong answers were a Slightly.

A Slightly is for a real, nameable polish edge between two responses that could both run. **It is not
where you land when you have not finished checking.** Cleaner, calmer, crisper, more premium, more
complete: every one of those was a true observation that lost to something the annotator never scanned.

## Final Checklist

- [ ] Brief copy fields read before looking at the responses.
- [ ] Seed inspected for product color, shape, badge, logo, and text.
- [ ] Every piece of text on both responses traced to the seed, the brief, or nowhere.
- [ ] Numbers hunted specifically. Any claim carrying a figure traced, including inside charts and badges.
- [ ] Prop text checked for claims. Ignorable only while it makes none.
- [ ] Product identity checked against the seed, using the background and white objects to separate a recolor from a warm grade.
- [ ] Dealbreaker scan run on both: text, hands, faces, product integrity, covering graphics, blur.
- [ ] No credit given for specs, prices, or offers before tracing them.
- [ ] No penalty for dropped seed text or ignored direction.
- [ ] Answer matches the anchors. Strongly only when the winner is itself campaign-ready, not merely better.
- [ ] Tie used without embarrassment when the pair is interchangeable.
- [ ] Feedback names the element, its location, and where its text came from.
- [ ] Feedback given in the chat. No workspace file was modified.
