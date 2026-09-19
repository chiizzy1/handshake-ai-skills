# Ads Creative Relevance Rubric

Operative rubric for the Ads Creative I2I **relevance** question.
Source: `HANDSHAKE-AI/ads-creative/vs-1788462573-260903-ads-creative-i2i-relevance.md`.

## Contents

- [The Question](#the-question)
- [Scope](#scope)
- [Hero Or Non-Hero](#hero-or-non-hero)
- [Reading The Original](#reading-the-original)
- [Survival Signals](#survival-signals)
- [Working Rules](#working-rules)
- [Failure Reasons](#failure-reasons)
- [Knowledge Checks](#knowledge-checks)
- [Assessment Answers](#assessment-answers)
- [Comment](#comment)
- [Common Failure Modes](#common-failure-modes)
- [Checklist](#checklist)

## The Question

Is the generated ad still relevant, meaning **it still sells what the original ad was selling**? Pass or
Fail. On Fail, check **every** reason that applies from a list that depends on the ad type.

The number one question on every item: **can the original ad survive an output without its original
selling points or main message?**

## Scope

**In scope:** everything in the generated image that carries the advertiser's message, including anything
the system added.

**Out of scope:** attractiveness, lighting, an artificial look, and whether small details render
cleanly. Other tasks judge those.

**An image can be beautifully made and completely irrelevant, and it can be clumsy and still perfectly
relevant.**

### Relevance versus rendering

Relevance asks whether **the right thing was shown at all**: the beer bottle became a wine bottle.
Rendering asks whether things were **drawn correctly**: hands, limbs, garbled letters, warped scale. You
label relevance only.

**One exception:** any change to the product's own color, shape, material, markings, or count is a
relevance failure, filed under **product preservation**. Do not work out the cause. You cannot see how the
image was built, so judge what a customer would see.

### Not your questions

- **Is it different from the original?** It is supposed to be. The system exists to make new versions. A big change has not failed for changing.
- **Is it good advertising?** The advertiser already made those decisions and printed them on the original. Check whether they survived.
- **Is it well made?** Beautiful and irrelevant can both be true.

### The logo rule

The guideline's exceptions became two: **a required advertiser logo must remain identifiable and
faithful.**

- Moving it, resizing it, or rendering an otherwise exact colored design in black or white is **allowed**.
- A changed or unidentifiable design is **"logo exists but is wrong"**.
- An invented brand mark where the original had none is also **"logo exists but is wrong"**, not missing.
- **"Required logo is missing"** applies only when the original owed you a logo and it did not survive.

This pulls one kind of lettering back into scope. Garbled type is usually rendering and not yours, but a
logo that stops being identifiable fails as a logo.

**Observed in the worked cases, under the new rule.** Case 11's Cross & Climb **emblem (the open book
with a pen nib) is dropped**, leaving the wordmark only. In case 10, the **ELITE wordmark is half hidden**
behind the brush stroke. Neither counted in the official answers, which may predate the logo rule. On a
live item, a dropped emblem is a candidate for "logo exists but is wrong", because the rule judges the
complete design.

## Hero Or Non-Hero

**What does the customer actually pay for?**

- **Hero:** a physical product as the business. The thing you take home.
- **Non-Hero:** a service, the thing done for you, a place to be, access, an experience, or a result.
- **Software, apps and games are Non-Hero**, and their interface is held as strictly as a product's body.

A service ad often shows physical things, such as the car being detailed or the windows being cleaned.
Those belong to the work, not the shelf. **Physicality is not the test.**

The type is **pre-selected by an automated check, it can be wrong, and you correct it before labelling**,
because it decides which reasons you see.

**Knowledge check.** A neighborhood restaurant ad shows its signature burger, pre-selected as Hero.
**Change it to Non-Hero.** A restaurant sells the experience and the service, and the burger belongs to the
work. "A burger is a physical product you can hold" applies the wrong test. "Keep whatever is
pre-selected" contradicts the instruction to correct it.

## Reading The Original

Every ad exists because a business is solving a problem and paying to say so. Run three questions on the
original **before looking at the output**:

1. **The problem.** Usually in the headline.
2. **The payoff.** Almost always one of: look better, feel better, save money, make money, save time.
3. **The support.** Selling points, prices, demonstrations, proof, partnerships.

Then ask whether all three survived. **If the problem or the payoff is gone, it is a Fail, no matter how
polished the image is.**

### Translate claims into visible things

A claim in words is hard to check against a picture, so turn it into something you can look for.

- "Most advanced compression system": the bag must read as packed down.
- "No metering": no gauge or usage bar.
- "$9.99 a month": that exact figure, unchanged.

**The larger and more deliberate the line, the more certainly it must survive.** A price printed larger
than the headline is the clearest case. Its size in the output need not match. It just has to be there.

## Survival Signals

- **A name printed under a person.**
- **Two brands in one image.** A collaboration, whose people and objects are part of the deal.
- **A price printed larger than the headline.**
- **A poster face, or partnership copy.**

**Without those signals you are not expected to recognize anyone.** A model can change when the casting
still fits who the ad is for and what it promises.

## Working Rules

- **How to look.** Side by side at normal size. A difference that only appears when enlarged is not a Fail.
- **Judge the pair, not the recipe.** A style that failed on one ad can be right for another.
- **Read the copy before judging a bold change.** Copy can license a change.
- **Additions must be intentional**, placed the way a photographer would.
- **An interface is not raw material.** It cannot be invented or improved, only preserved.
- **Never invent what the advertiser does not have.** An invented room, view, amenity, interface or product is false advertising, even when it looks great.
- **People.** A model can change if the casting still fits. A celebrity or partner face cannot, and the signal is on the image.
- **Landing page.** A backup, for when you cannot tell what the product or service is, to verify a new product angle, and before calling a scene invented.

## Failure Reasons

### Hero

1. **Lost the core product.** Absent, replaced, or reduced to less than what was sold.
2. **Altered the product.** Any customer-noticeable change to shape, color, material, markings, count. A new angle only if verifiable with the advertiser.
3. **Added or invented irrelevant products.** No source in the input. A specific invented product always fails. An object placed without intention fails for distracting.
4. **Irrelevant use case.** Wrong purpose, wrong method, or a demonstration of something it does not do. **Judges the action alone, not who or where.**
5. **Irrelevant casting.** Does not fit who the ad is for or what the product promises, or a signalled face was changed.
6. **Scene does not fit the product.** Contradicts where or how the product belongs, or distracts. A new setting is allowed when it complements.
7. **Invented scene.** A scene that is the message (a location being sold, a season, an occasion) replaced.
8. **Missing or incorrect selling points or headlines.** Rephrasing and hierarchy changes are fine. A critical line gone, a claim rewritten into something never said, or a prominent price missing fails.

### Non-Hero

1. **Digital product preservation.** No invented screens or platforms, no lost core interface, no recolored or embellished design, no covered or misaligned elements.
2. **Added or invented irrelevant products.** A specific, identifiable product fabricated where there was none always fails. Generic is fine only for a service or category ad.
3. **Irrelevant use case.** Wrong method, wrong handling, wrong moment of the job, or physically impossible work. **Would this business actually do the work this way?**
4. **Irrelevant casting.** Demographic clash, an appearance that contradicts the promise, or a passive pose that tells nothing.
5. **Changed a person who should be preserved.** Replaced or altered past recognition when a printed name, poster face or partnership copy says preserve.
6. **Scene does not fit the service.** The scene is the **subject** (what the work is done on), the **world** (the input's visual language), and the **dream** (the state of life being sold). Missing subject, wrong world, or lifeless materials fail.
7. **Invented scene.** A scene carrying the business replaced with a room, view or amenity not offered. Check the landing page first.
8. **Missing or incorrect selling points or headline.** Same as Hero, and it weighs more, because a service ad's words often carry the whole offer.

### Count, and when it matters

Count is part of the product's body, but **only when the count is what is sold**. A five-piece set shown
as two pieces fails. Three display jars of one cream shown as one jar did not fail in the guideline's
worked case. Ask whether the number is part of the offer ("2 for $99", "five-piece set", "3 in 1") or
just staging.

A set shown with fewer pieces fits both "reduced to less than what was sold" under lost the core product,
and "count" under altered. Check both.

## Knowledge Checks

All eight from the guideline, with the reasoning.

**1. Better looking, but less product.** The generated ad is far better looking, but the original sold a
five-piece cookware set and the output shows two pieces.
**Fail. The product that was sold did not survive, however good the image looks.**
*When an output looks better than the input but says or shows less, it fails.* "Fewer pieces is a stylistic
simplification" is the wrong answer: the set is the product.

**2. The restaurant burger.** Pre-selected Hero.
**Change it to Non-Hero.** See [Hero Or Non-Hero](#hero-or-non-hero).

**3. The endorsement.** A person with a second brand's logo beside them and a name printed under the photo.
The generated ad keeps the layout and swaps in a different, equally suitable model.
**Fail, casting. The signals mark an endorsement, so that person is part of what the advertiser paid for.**
Two signals at once. "The new model fits the demographic" applies the generic-casting test to a
signalled person. "Fail, scene, the background around a named person may never change" is the right verdict
with an invented rule and the wrong reason.

**4. Go big or go home.** The product at ten times its size, towering over a street, with that headline.
**The copy licenses the exaggeration. Judge the rest of the ad normally.** "Product alteration, size changed"
skips reading the copy. "Invented scene, streets that size do not exist" misreads never-invent, which is
about advertiser assets, not a city street.

**5. The hotel pool.** A small hotel's actual rooftop terrace replaced with a dramatic infinity pool.
**Fail, invented scene. The advertiser does not have that pool, and a customer would arrive to find it does
not exist.** "Upgrading the scene is what the system is for" is the trap. "Scene does not fit, pools and
hotels belong to different worlds" picks the wrong reason, since a pool fits a hotel perfectly well.

**6. The soaked sofa.** Same cleaner and room, but the sofa soaked and dripping.
**Fail, irrelevant use case. Same service, but work no company would sell.** "The person and the location
both survived" stops at the nouns. "Scene does not fit" blames the room, which is right.

**7. The moved white logo.** A colored advertiser logo moved to another corner and rendered in white,
same design.
**No logo failure. Size and placement may change, and an otherwise exact colored logo may become black or
white.** *Judge the logo's complete design, not its placement.* "Any change in placement or color fails"
over-reads the rule. "Fail, selling points, a logo is part of the copy" files it in the wrong place.

**8. The invented brand mark.** The original has no logo, and the generated ad adds one.
**Logo exists but is wrong. The output invented a logo with no source in the original.** *Missing applies
only when the original owed you a logo and it did not survive. An invented mark is present but wrong.*
"Neither, adding a logo is always allowed" ignores that nothing about the advertiser can begin in the
output.

### The explanations the UI shows

- **Cookware:** "When an output looks better than the input but says or shows less, it fails."
- **Restaurant:** "The customer pays for a meal experience, not a product they take home from a shelf. The pre-selection is a starting point and can be wrong; correcting it is part of the task."
- **Endorsement:** "When those signals are present the person must be preserved, even by a perfect demographic match."
- **Go big:** "The same image under different copy would be the system exaggerating for no reason."
- **Hotel pool:** "The terrace carries the business, and an invented amenity is false advertising however well it sells."
- **Sofa:** "The right person in the right place doing the work a way the business never would is a use case failure, not a scene failure."

The go-big explanation adds something the guideline body did not say: **the same oversized image under
ordinary copy would fail.** The license comes from the words, not from the image.

Checks 3, 5 and 6 all hold everything constant except one element and test whether you file the failure
under the element that changed.

## Assessment Answers

Six questions. Q1, Q2, Q3 and Q5 were decided by viewing the images, which are in `examples/q*`.

### Q1. Laboratory research vials

**Fail: irrelevant use case. The vial is shown being poured into a drinking glass, a use the ad itself
rules out.**

The original shows five labelled "PEPTIDE, For Laboratory Research Use" vials on a lit pedestal. The
generated ad shows a hand tipping one vial's powder into a glass of water. **Every badge, the Free BAC Water
Gift, "VIEW CURRENT CATALOG" and the fine print survived**, and the fine print still reads "For laboratory
research use only. Not for human or veterinary use." The ad's own copy rules out the action it now shows.

Why not the others: the vial and its label are intact, so not "altered". A drinking glass is not a product
being sold, so not "added products". And "Pass" ignores that the image demonstrates a forbidden use.

**The lesson:** read the copy, **including the fine print**, before judging the action. Same shape as the
drunk cream.

### Q2. The multi-port charger

**Fail: lost the core product. The charger is gone, and glasses and a pen are not the product.**

The original shows a UGREEN charger feeding a laptop, tablet, phone and earbuds, beside a "VS" panel of a
tangled power strip. The generated ad keeps the logo, "One Charger, Zero Clutter" and "Shop Now", and shows
**tortoiseshell glasses and a pen on a tidy cream tray**. No charger, no cables, and the before-and-after
comparison is gone.

"The tidy tray keeps the zero clutter message" is the champagne trap in a new form: the mood survived and
the product did not.

### Q3. Floating sound journey, two generated ads

**Generated ad 1 fails on casting: a posed swimsuit shot tells nothing about floating relaxation.
Generated ad 2 passes.**

The original is a person asleep on a floating bed at night, head wrapped in a towel with a cloth over the
eyes, in a striped top. **Generated 1** is a glamour shot of a woman in a black-and-white striped swimsuit,
posing and looking at the camera. The stripes carried over while the meaning flipped from rest to pose.
**Generated 2** is a person with an eye mask, wrapped in a blanket, asleep on the bed, with string lights
and fire bowls added.

Why not the others: the original person carries no name, second brand or partnership, so there is nobody
to preserve, and "both fail, neither preserves the person" invents a signal. Generated 2's new furniture and
lighting are staging changes, which are allowed. "Both pass, each shows a person on a floating bed" is
presence without story, the festival mistake again.

### Q4. Product, headline and price kept, everything else changed

**Pass. The system exists to make new versions, and the message survived.**

"Too much changed at once" and "the layout is a selling point" both treat change as failure. "Reject, heavily
changed ads cannot be judged" invents a reject path.

### Q5. The vacuum-compression travel bag

**Fail: added or invented irrelevant products. A rigid suitcase appeared with no source, and nothing in the
ad signals a comparison.**

The original shows the product cut-out (a black compression bag with its pump) and a man compressing a
black bag. The generated ad keeps the cut-out, the headline "1% TravelPack Vacuum Kit Pro", the "PACK FOR
15+ DAYS IN A CARRY-ON" claim, Trustpilot, and "ekster | The Diary Of A CEO". **The man and his bag are
replaced by an open hard-shell suitcase full of folded shirts** on a hotel table.

The suitcase is the clear failure: a product the advertiser does not sell, sitting beside a compression
bag, and with no comparison signalled it reads as if the suitcase is part of the offer. It also removes the
compression demonstration.

Why not the others: "Lost the core product" is wrong because the cut-out bag and pump survived. "Pass" misses
the suitcase. "Irrelevant casting, because the man is gone" judges a person who is no longer shown, and
casting judges the person on screen.

**A caution for live items.** "ekster | The Diary Of A CEO" is two brands in one image, which the guideline
treats as a collaboration whose people are part of the deal. On a live checklist where you check every
reason that applies, consider whether the removed man is the collaboration's face. The assessment question
is single-answer, and the suitcase is its answer.

### Q6. Product color changed from red to blue

**Fail: altered the product. Any change to the product's own body is a relevance failure.**

"Color is a rendering detail, judged elsewhere" is the exact trap the exception exists to close. "Pass, if
the blue version looks better" judges quality.

## Comment

**One sentence on what survived or broke. Name the element.**

The voice is the house style, from the Omni ELO skill: an average person looking at two ads, plain words,
short, no em dashes or semicolons, "while" not "whereas", no absolutes, no snark, no rubric vocabulary,
never "garbled", "gibberish" or "hallucinated".

The guideline's own comments sometimes use a semicolon to join two halves. Keep it one sentence by joining
with "and", "but", "while", or a comma instead.

| Guideline's version | House style |
|---|---|
| "The two women became two men; the campaign is written for women." | The two women became two men, and the campaign is written for women. |
| "The game board is gone; only the art and floating score text remain." | The game board is gone and only the art and floating score text remain. |
| "The sea view is what is being sold; a hot tub in a studio loses the point." | The sea view is what is being sold, and a hot tub in a studio loses the point. |

**When two reasons apply, the sentence names both elements**: "A random wrench appeared and the headline is
gone."

## Common Failure Modes

1. **Rating the vibe.** Mood, lighting and offer text survived, the product did not. Champagne, charger.
2. **Rating polish.** "It looks nicer." Match-3 board, aurora suite, dreamy bathroom.
3. **Stopping at the nouns.** Same person, same room, same service, wrong work. Sofa.
4. **Right verdict, wrong reason.** Cream drunk filed as "altered". Every reason must name what changed.
5. **Failing a change for being a change.** A big change is not a Fail by itself.
6. **Treating a color change as rendering.** Product body changes are relevance, always.
7. **Accepting brand marks as identity.** The logo survived, the body did not. Suitcase.
8. **Crediting an accident as creative.** The wrench is not "tone".
9. **Keeping a wrong pre-selected type.** It changes the reasons you can see.
10. **Using physicality for Hero.** A burger at a restaurant is Non-Hero.
11. **Swapping a signalled person.** Printed names, second brands, poster faces, partnership copy.
12. **Inventing a preservation signal.** An unnamed model can change.
13. **Confusing invented scene with does not fit.** Invented means the advertiser does not have it. Does not fit means the wrong world.
14. **Calling a scene invented without checking the landing page.**
15. **Skipping the copy.** "Go big or go home" licenses scale. Fine print can forbid an action.
16. **Checking one reason when two apply.** Coffee pods had two.
17. **Failing on something only visible under zoom.**
18. **Art-directing.** "The lifestyle shot sells better than a wall of text."
19. **Failing a logo for moving or turning white.** Placement and black or white are allowed.
20. **Calling an invented logo "missing".** It is present and wrong.
21. **Comment in rubric voice.** "Preserves message integrity" instead of naming the element.

## Checklist

- [ ] Ad type set by what the customer pays for, pre-selection corrected if wrong.
- [ ] Problem, payoff and support read from the original first.
- [ ] Signals noted: printed names, second brands, oversized prices, partnership copy, poster faces.
- [ ] Claims translated into visible things.
- [ ] Product found first in the generated ad.
- [ ] Product body compared: color, shape, material, markings, count, with count only where it is sold.
- [ ] Copy read, including fine print, for anything that licenses or forbids.
- [ ] Every applicable reason checked, each naming what actually changed.
- [ ] No Fail for difference, quality, rendering, or zoom-only detail.
- [ ] Landing page checked before calling a scene invented.
- [ ] Comment is one plain sentence naming the element.
