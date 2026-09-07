# Ads Creative Overall Suitability Rubric

Operative rubric for the Ads Creative I2I **Q0 Overall Suitability** question.
Source: `HANDSHAKE-AI/ads-creative/vs-1786660967-260813-ads-creative-i2i-q0-overall-ad-suitability.md`.

Its sibling is `handshake-ads-visual-appeal`, the **Q4** question on the same creative set. The two have
opposite scope rules: Q4 ignores the overlay and judges the picture, Q0 judges the whole ad including
the overlay and where its text came from.

## Contents

- [The Question](#the-question)
- [Campaign-Ready](#campaign-ready)
- [The Three References](#the-three-references)
- [Text: Grounded Or Invented](#text-grounded-or-invented)
- [Dealbreakers](#dealbreakers)
- [Answer Anchors](#answer-anchors)
- [Flashcards](#flashcards)
- [Flashcards, Text And Product Deck](#flashcards-text-and-product-deck)
- [Knowledge Checks](#knowledge-checks)
- [Out Of Scope](#out-of-scope)
- [A Dealbreaker Is Not A Reject](#a-dealbreaker-is-not-a-reject)
- [Rejections](#rejections)
- [The Contrasting Pair](#the-contrasting-pair)
- [Feedback](#feedback)
- [Worked Cases](#worked-cases)
- [Common Failure Modes](#common-failure-modes)
- [Checklist](#checklist)

## The Question

"Which image is more suitable as an ad for a high-end marketing campaign?"

**Judge the whole ad as one thing. Nothing visible is out of scope.** The picture, the overlaid text and
graphics, where that text came from, and how it all works together.

The guideline's own summary of the trade:

> A gorgeous photograph with an invented price or a garbled headline is a broken ad. A plain photograph
> with clean, grounded text may be the more suitable one.

That sentence is the whole task. Polish loses to a broken claim.

## Campaign-Ready

**"High-end" refers to the ad's execution, not the product's price.**

A $2 sponge can have an ad that feels expensive: restrained composition, clean typography, professional
light. A luxury watch can have an ad that feels cheap.

**The test: would a demanding brand team sign off on running this image with minimal or no
adjustments?** Clearing that bar is what *campaign-ready* means, and it is the bar each response is
judged against.

A brand team would not sign off on a claim their client never made. **An invented specific fails the
test however polished the image is.**

## The Three References

Shown above the responses, in this order:

1. **Seed image.** The product or the original ad the model started from. Establishes what the ad is for, and the product's true color, shape, badge, logo, and text.
2. **Creative direction.** What the model was told. Long directions collapse behind "Show more".
3. **Ad brief.** Advertiser, audience, objective, and the copy the advertiser supplied: headline, description, primary text. Empty fields read "(none)" or "(not provided)". **About half of all briefs carry no copy at all.**

Their purpose is to tell you what the ad was meant to be and, more importantly, **where any text on a
response could legitimately have come from.**

### What they are not for

- **Not adherence grading.** A response that ignores part of the direction but works as an ad can win. A response that follows every clause can lose. Another task measures adherence.
- **Not seed-text preservation.** Dropping a line, a badge, or a button from the seed is not a flaw. **Garbling it is.**

A brief with no copy at all is a common and important case: it means almost any claim text on a
response is ungrounded, because there was nothing to ground it in but the seed.

## Text: Grounded Or Invented

The core mechanic. Trace every piece of text on both responses before judging anything else.

**Grounded** = appears on the seed, appears in the brief (headline, description, primary text), or is
the advertiser's name. **Grounded text is fine wherever the response puts it, including on a phone
screen or a sign inside the scene.** Placement never makes text a problem. Origin does.

| Category | Examples | Verdict |
|---|---|---|
| Grounded | Seed text, brief headline/description/primary text, advertiser name | Fine anywhere |
| **Invented specific** | Prices, discounts, percentages, statistics, specs, model names, dates, awards, quotes, **and any other claim with a number in it** | **Dealbreaker** |
| **Invented brand** | A brand name that is neither the advertiser's name nor a brand visible on the seed | **Dealbreaker.** A specific |
| **Invented generic line** | "No hassle rentals", "Reliable, affordable" | **Serious flaw.** Outweighs any polish edge. Not disqualifying alone |
| Generic call to action | "Shop now", "Learn more", "Book today" | Fine |
| Language mismatch | Text in a language matching neither the seed's text nor the brief | **Dealbreaker** |
| Incidental prop text | A call timer, a clock reading, a keyboard label. Makes no claim | Ignore it |

### Three sources, not one

Grounding has **three** independent sources: the seed, the brief, or the advertiser's name. A line needs
only one of them. Do not collapse them into "does it match the advertiser".

**Worked case.** The seed shows a running shoe with a visible maker's logo. The advertiser in the brief
is a retailer with a different name. Response A prints the maker's name; Response B prints a third brand
appearing nowhere.

**A's name is grounded**, because it is a brand visible on the seed, even though it is not the
advertiser. **B's name is an invented specific**, a dealbreaker.

A retailer advertising someone else's product is where the three sources visibly come apart, and it is
the setup this check is built on. The two wrong answers are the two ways to collapse them: requiring the
advertiser's name specifically, or letting category expectation ("a shoe ad names a brand") stand in for
provenance.

### The number heuristic

**Any claim with a number in it is a specific.** That is the fastest scan you can run: find every figure
on both responses, then ask whether it appears on the seed or in the brief. If it does not, that
response has a dealbreaker.

**A chart or graphic does not launder a statistic.** An invented percentage or statistic is a specific
even when it sits inside a chart, a badge, or an infographic. The container is irrelevant.

### The rules that catch people out

**A requested slot does not ground the value.** If the direction asked for a price and the model
supplied one, the slot was requested but the number was invented. The value itself must trace to the
seed or the brief. The same applies to a call-to-action slot filled with a specific offer.

**Non-Latin text is never a reason to reject.** The dealbreaker is a language matching neither source,
not an unfamiliar script. Do not confuse "I cannot read this" with "this is wrong". **Judge its
letterforms and placement, and check the parts you can read.**

**Prop text stops being incidental the moment it makes a claim.** A call timer, a clock reading, or
keyboard letters are ignorable. The same phone screen showing a price, an offer, a rating, or a message
gets sorted like any other line.

### The severity ladder

Three tiers, and they behave differently:

1. **Invented specific** → dealbreaker. The ad cannot ship. Beats any amount of polish on that side.
2. **Invented generic line** → serious flaw. Outweighs a polish edge on the other side, but the ad is not disqualified. One side carrying one and the other not is worth a *Slightly Prefer*.
3. **Generic CTA** → nothing. Not a flaw at all.

## Dealbreakers

Any one means the response is not campaign-ready.

**Text and claims**

- An invented specific.
- Text in a language matching neither the seed nor the brief.
- Garbled, misspelled, illegible, or duplicated text. **Fine print and logos included.**

**Product identity**

- The product's color, shape, badge, logo, or model differs from the seed.
- The product warped, melted, or missing.
- **Allowed:** lighting that warms or cools the whole scene. That is grading, not an identity change.

**The diagnostic.** Check the background and any white object in the frame. If the backdrop and the
whites shifted too, it is a grade. If only the product moved, it is a recolor. **A grey shoe turning tan
while the backdrop stays neutral is a recolored product, not a warm grade**, and the ad now sells
something the advertiser does not have.

**Rendering and composition**

- Mangled hands, faces, or limbs. Cloned people.
- Text or graphics covering the subject or the product.
- Graphics whose logic attacks the product.
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

### The contrasting pair

These two cases sit next to each other in the guideline and together they define the Strongly boundary.

**Strongly.** A is a gorgeous lifestyle shot captioned "Rated #1 by 2,000 customers"; the seed has no
text and the brief has no copy. B is a plain product shot carrying only the advertiser's name.
**Strongly Prefer B.** "#1" and "2,000 customers" are invented specifics, a dealbreaker however good the
photograph is. B's only text is grounded and nothing else is wrong with it, so B is the only
campaign-ready response.

**Slightly.** The brief has no copy. A adds "Fast, secure, rewarding"; B adds "0% fees for 12 months".
Both otherwise clean and equally polished. **Slightly Prefer A**, because A's invented generic line
means A is not campaign-ready either.

Same shape, different answer, and the variable is not the loser. In both cases the loser has a
dealbreaker. **What decides Strongly versus Slightly is whether the winner is itself clean.**

### Strongly requires a clean winner

**A dealbreaker on one side does not by itself earn a Strongly.** The first anchor row requires the
other response to be *campaign-ready*, not merely better. When both sides carry problems, you are in
the "both have serious problems and one is closer to usable" row, and that is a **Slightly**.

**Worked case.** The brief has no headline, description, or primary text. Response A shows the
advertiser's name plus "Fast, secure, rewarding". Response B shows the advertiser's name plus "0% fees
for 12 months". Both otherwise clean and equally polished.

**Slightly Prefer A.** B's line is a claim with numbers appearing nowhere in the seed or the brief: an
invented specific, a dealbreaker. A's line is an invented generic line: a serious flaw, so A is not
campaign-ready either, but it is clearly closer to usable. Both have problems and one is closer to
usable, so the anchor is Slightly. **Name both lines in the feedback.**

That last instruction matters. A feedback note that only names B's failure hides the fact that you saw
A's.

### Tie is normal here

The guideline says so directly: "Tie is a normal answer on this task", and "Many pairs in this task are
close, and expert reviewers call ties often." If the two responses are interchangeable after a proper
scan, answer Tie. Do not hunt for a tiebreaker.

If you pick a side, your feedback must name the reason. If you cannot name one, your answer is Tie.

**Two opposite failures, both caught in review:** forcing a preference to avoid a tie, and tying to
avoid looking closely. The knowledge check covers the first, where a clean scan finds no dealbreakers
and no nameable edge. The answer is Tie, with feedback saying what both do well. Picking "whichever you
would personally click on" substitutes taste for evidence, and rejecting the pair as too close to call
confuses a hard decision with a reject reason.

### Polish edges

Worth a *Slightly Prefer* when both sides could run:

- Cleaner composition with one focal point
- Better lighting and color harmony
- Consistent, aligned typography
- A scene that fits the product
- A "ready to ship" feel

**Not an edge:** sharpness you can only see at maximum zoom.

### Zoom discipline

Zoom is for checking, not for finding edges. Use it to confirm text is readable and detail is intact,
which is part of the dealbreaker scan. Once everything reads correctly in both responses, a difference
visible only at maximum zoom (a bit more resolution, slightly sharper type) is not an edge.

**If you need 200% zoom to justify a preference, answer Tie.**

## Flashcards

**High-end feel.** Judge the execution, not the price of the product.

**What do we call an image that a demanding brand team would run with minimal or no adjustments?**
Campaign-ready. It is the bar each response is judged against.

**A gorgeous image whose price tag appears nowhere in the seed or the brief. What kind of problem is
that?** A dealbreaker: an invented specific. The image cannot ship, however good the rest of it looks.

**Both responses could ship, but one has cleaner typography and a calmer composition. What does that one
have?** A polish edge. That is enough for Slightly Prefer, not for Strongly Prefer.

The last two cards are the task's central calibration: a dealbreaker is a *Strongly*, a polish edge is a
*Slightly*, and they are not on the same scale.

## Flashcards, Text And Product Deck

A second four-card deck sits in the grounded/invented section.

**The brief has no copy. Response A prints the advertiser's name and "Book today". Grounded or
invented?** Both fine. The advertiser's name is grounded, and a generic call to action is allowed.

**The direction asks for "a bold price as the second read". The brief has no price. Response B prints
"NOW $49".** An invented specific, so a dealbreaker. The direction requested the slot; the value came
from nowhere.

**Response A adds "Comfort you can trust", in neither the seed nor the brief.** An invented generic
line: a serious flaw. It outweighs any polish edge A has, but it does not disqualify A on its own.

**The seed and the brief are in English. Response B adds a slogan in German.** A dealbreaker. Text in a
language that matches neither the seed nor the brief disqualifies the response, whatever the slogan
says.

The four cards walk the whole severity ladder in order: fine, dealbreaker, serious flaw, dealbreaker.
Card 1 and card 2 are the pair worth internalizing, because both involve a slot the direction or the
format invited and the answers differ entirely on whether the *value* traces to a source.

## Knowledge Checks

**A spelling error in the overlay, on an otherwise stunning photograph.** It affects your answer.
*This question judges the whole ad, overlaid text included. A text defect can decide it on its own.*

Note this is the **exact inverse** of the Q4 visual-appeal knowledge check, which uses the same
scenario and answers "No, overlaid text is out of scope, judge the picture behind it." Same creative
set, same-looking question, opposite rule. If you have worked Q4 recently, this is where the habit
will bite.

**A budget laundry detergent can still produce a high-end ad.** Yes.
*The bar is how the ad is made: composition, light, typography, polish, and text the advertiser actually
supplied. Not what it sells.*

**A follows the direction closely, B ignores half of it but is the cleaner, more finished ad, and
neither has a dealbreaker.** The direction pushes the answer **neither way**.
*It is context here. Judge the two finished ads, so B's polish edge is the only nameable difference and
B wins.*

The two wrong answers on that last one are the two ways people get it wrong: treating adherence as a
merit ("toward A"), or treating it as a counterweight that cancels polish ("toward a Tie"). It is
neither. It carries no weight at all.

## Out Of Scope

**Photorealism.** An intentional style such as flat illustration, black-and-white, or a bold graphic
look is fine when executed well. Penalize style only when it reads as an accident.

**Your taste in products.** You may find the product boring or the category unappealing. Judge how well
the ad is executed, not what it sells.

**The direction as a checklist.** It is context. A response earns nothing for following it and loses
nothing for ignoring it.

**Tiny differences.** You are not hunting for them. Interchangeable after a proper scan means Tie.

## A Dealbreaker Is Not A Reject

The two get conflated, and one knowledge check is built on the confusion.

**A dealbreaker is recorded through your vote.** You prefer the other response and name the failure in
your feedback. It never sends you to the reject buttons.

The reject buttons cover only a failed load and inappropriate content. Garbled text, an invented price,
a recolored product, a language mismatch: every one is a dealbreaker, every one is voted on, none is
rejected.

### The language rule is symmetric

No language is privileged. **An English tagline added to a Portuguese seed and brief is a dealbreaker**,
exactly as a German slogan is on English sources. It is the mismatch that disqualifies, not the identity
of the language, and not whether you personally can read it.

Nor is it a downgrade to the serious-flaw tier. An invented *generic line* is the serious flaw. A
language mismatch is a dealbreaker outright, whatever the line says.

## Rejections

Only two, fewer than the Q4 visual-appeal question:

- **Image did not load.** A response or the seed fails to load.
- **Inappropriate content.** Nudity or sexually explicit poses, hate symbols, graphic violence.

Swimwear or underwear is not a reason to reject. **There is no mixed-medium reject on this question.**
Never reject an ugly or flawed image; the vote is how those are recorded.

## Feedback

**The field is "Open Feedback", minimum 100 characters.** Its prompt reads "In a sentence or two, say
what made your chosen image more suitable as an ad, or why they're equally good."

The count is a floor and nothing more. The guideline is explicit that "the real bar is specificity", so
100 characters of padding fails exactly as a vague note does.

Name the element, where it is, where its text came from if text decided it, and why it decided your
answer.

- ✅ "A's price appears in neither the seed nor the brief."
- ❌ "A has more information."

The guideline's own examples:

- ✅ "B's headline is the brief's headline and renders crisply, while A prints 'From $19/month', which appears in neither the seed nor the brief."
- ✅ "Both keep the seed's copy intact, add nothing, and render cleanly; nothing separates them." (tie note)
- ❌ "A looks better." Names nothing.
- ❌ "B has more information about the product." More information does not help when it comes from nowhere.

For ties, describe what both images do well or equally badly. **Vague feedback on a correct answer still
fails review.**

### Length is a symptom, not a target

The guideline's model fragment, *"A's price appears in neither the seed nor the brief"*, is **52
characters**: it teaches specificity, not submission length. Every full exemplar in the guideline runs
120 to 170 characters, and they get there the same way:

> **What the loser did and where its text came from. Then what the winner does right.**

If you are short of 100, you have written about one response only. **Add the other side, never more
adjectives.** A padded 100 characters fails review exactly as a vague one does.

### Say the trace, not the label

The exemplars never write "invented specific", "dealbreaker", "campaign-ready", or "polish edge". They
write what is on the image and where it came from: "appears in neither the seed nor the brief", "the
chest logo is garbled", "the upper stays grey". The rubric's category names are thinking words. The
feedback names what you saw.

### Semicolons

Allowed here. The house baseline bans them, but this task's exemplars use them ("...and render cleanly;
nothing separates them", "so every one of those is invented; only 'MARIE CLAIRE UK' is grounded"). The
task guideline outranks the baseline.

Persona: a careful person explaining what they saw. Short sentences, no em dashes, "while" rather than
"whereas", no absolutes, no AI power words. When text decides the item, **say where it came from or say
that it came from nowhere.** That trace is the evidence.

## Worked Cases

Six graded pairs with images live in `worked-cases.md` and `examples/`. Read them before rating.

The single pattern across all six bad examples: **the annotator rated a first impression and skipped the
scan**, and the thing they rated on was usually true. B really was cleaner. A really did have a calmer
background. A really was sharper at full zoom. Each lost to something never checked.

## Common Failure Modes

1. **Rewarding invented information.** A price, a spec, or a stat reads as helpful detail. Trace it first. More information is not better information.
2. **Treating a requested slot as grounding.** The direction asking for a price does not make the number real.
3. **Grading adherence.** Penalizing a response for ignoring part of the direction. Another task's job.
4. **Penalizing a dropped line.** Dropping seed text is allowed. Garbling it is the flaw.
5. **Calling a warm grade a color change.** Whole-scene lighting shifts are allowed. Only the product's own color, shape, badge, logo, or model matters for identity.
6. **Rejecting non-Latin text.** Never a reject reason. The dealbreaker is a mismatch to both sources.
7. **Inflating to Strongly when your winner is also flawed.** Strongly needs a campaign-ready winner. Dealbreaker against serious flaw is a Slightly.
8. **Missing a number inside a graphic.** A percentage in a chart or a badge is still an invented specific.
9. **Calling grounded text misplaced.** Grounded text on a phone screen or an in-scene sign is fine. Origin decides, not placement.
10. **Letting polish beat a dealbreaker.** The gorgeous image with the invented price loses. This is the most important single rule on the task.
11. **Flattening the severity ladder.** An invented generic line is not the same as an invented price. One is a slight preference, the other is a strong one.
12. **Ignoring prop text that started making claims.** A clock is ignorable. A phone screen quoting a rate is not.
13. **Avoiding Tie.** Expert reviewers tie often here. An unnameable edge is not an edge.
14. **Inflating a polish edge to Strongly.** Cleaner typography plus a calmer composition is a *Slightly*, unless several clear advantages stack.
15. **Judging the product's price** instead of the ad's execution.
16. **Feedback without a trace.** "A's text is wrong" does not say which text or why.
17. **Confusing a dealbreaker with a reject.** Dealbreakers are voted on. Rejects are for failed loads and inappropriate content only.
18. **Treating English as a neutral default.** An English line on non-English sources is a mismatch like any other.
19. **Treating targeting settings as copy.** Country codes and age ranges on an edge are campaign settings, not claims.
20. **Penalizing a response for not rendering the brief's headline.** Nothing requires the brief's copy to appear.
21. **Reading a layout as decoration.** Where the marks point is part of the ad. A collapsed comparison layout can turn a warning mark on the advertised product.
22. **Padding to reach 100 characters.** Adjectives instead of the second half of the comparison.
23. **Writing in rubric labels.** "An invented specific, therefore not campaign-ready" instead of quoting the line and saying where you looked for it.
24. **Naming only the loser's failure.** When both sides carry problems, name both lines. A note that mentions only B's invented price hides that you also saw A's filler.

## Checklist

- [ ] Brief copy fields read before looking at the responses. Noted when the brief supplies none.
- [ ] Seed inspected for product color, shape, badge, logo, and text.
- [ ] Every piece of text on both responses traced to seed, brief, or nowhere.
- [ ] Requested slots not mistaken for grounded values.
- [ ] Every figure on both responses traced, including inside charts, badges, and infographics.
- [ ] Prop text checked for claims. Ignorable only while it makes none.
- [ ] Product identity checked using the background and white objects to separate a recolor from a warm grade.
- [ ] Dealbreaker scan run on both, 30 to 45 seconds: text, hands, faces, product integrity, covering graphics, blur.
- [ ] No credit for specs, prices, or offers before tracing.
- [ ] No penalty for dropped seed text or ignored direction.
- [ ] Severity ladder respected: specific invention is a dealbreaker, generic invention is a serious flaw, generic CTA is nothing.
- [ ] Answer matches the anchors. Strongly only when the winner is itself campaign-ready.
- [ ] When both sides carry problems, both are named in the feedback.
- [ ] Tie used without embarrassment when the pair is interchangeable.
- [ ] Feedback names the element, its location, and the origin of any deciding text.
- [ ] Delivered in the chat. No task file modified.
