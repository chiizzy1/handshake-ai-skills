---
name: handshake-ads-relevance
description: Evaluate Handshake Ads Creative I2I relevance items. Use when a task shows an original ad, a generated ad made from it, and the ad text, and asks whether the generated ad is still relevant (still sells what the original was selling) with a Pass or Fail label, a Hero or Non-Hero ad type that arrives pre-selected, and a checklist of failure reasons such as lost the core product, altered the product, added or invented irrelevant products, irrelevant use case, irrelevant casting, scene does not fit, invented scene, missing or incorrect selling points, digital product preservation, or changed a person who should be preserved; when the task says ads creative relevance or Is the Generated Ad Still Relevant.
---

# Handshake Ads Relevance

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/cheat-sheet.md`. The task's own cheat sheet, verbatim.
2. `references/rubric.md`. The full operating rules, every knowledge check, and the assessment answers.
3. `references/worked-cases.md`. The guideline's 15 graded pairs, with what the images actually show. Images in `references/examples/`.
4. `HANDSHAKE-AI/ads-creative/vs-1788462573-260903-ads-creative-i2i-relevance.md`, the guideline.

**Read `references/worked-cases.md` before your first live item.** Every bad example in it is a person
who rated the vibe, the polish, or the nouns, and never checked whether the thing being sold survived.

The one question: **does the generated ad still sell what the original ad was selling?**

The number one test on every item, in the guideline's words: **can the original ad survive an output
without its original selling points or main message?**

## Sibling Tasks, Different Questions

This is one of three questions asked about the same Ads Creative I2I outputs. They look alike and have
different scopes. Check which one you are on.

| | Relevance (this skill) | Q0 Overall Suitability | Q4 Visual Appeal |
|---|---|---|---|
| Question | Does it still sell what the original sold? | Which of two ads is more campaign-ready? | Which picture is more striking? |
| Shows | Original ad, one generated ad, ad text | Seed, direction, brief, two responses | Two responses |
| Answer | Pass or Fail, plus every failure reason that applies | Strongly/Slightly/Tie | Clearly/slightly more appealing, Similarly good/bad |
| Rendering defects (hands, garbled type) | **Out of scope** | Dealbreaker | Only if in the focal area |
| Changes to the product's body | **In scope, product preservation** | Dealbreaker | Out of scope |
| Image quality | **Out of scope** | In scope | The whole question |

Skills: `handshake-ads-overall-suitability`, `handshake-ads-visual-appeal`.

## Task Shape

- The **original ad** the advertiser uploaded, the **generated ad** the system made from it, and the **ad text**.
- An **ad type** selector, **Hero** or **Non-Hero**, pre-selected by an automated check.
- **Q1: Is the generated ad still relevant?** **Pass** ("still sells what the original ad was selling") or **Fail** ("the message did not survive: the logo, product, person, scene, or selling points broke it").
- On Fail, a checklist of **failure reasons**. The list depends on the ad type. **Check every reason that applies.**
- **Comment, optional** in the UI: "What survived or broke, in your own words." The guideline still describes it as one sentence naming the element, so the skill always drafts one. Use it or leave it.
- An **AD TEXT AND CONTEXT** block: Advertiser, Audience, Objective, Headline, Description, Primary text. Empty fields read "(not provided)", "(not specified)" or "(none)".
- A **landing page link**, as a backup only.

You will not see how the image was made. Judge what a customer would see.

## What You Are Judging

**In scope:** everything in the generated image that carries the advertiser's message, including
anything the system added.

**Out of scope:** whether the image is attractive, well lit, or looks artificial. Whether small details
render cleanly. Those belong to other tasks.

**An image can be beautifully made and completely irrelevant, and clumsy and still perfectly relevant.**

### Relevance is not rendering

| Relevance, yours | Rendering, not yours |
|---|---|
| The right thing was not shown at all: the beer bottle became a wine bottle | Things were drawn wrong: hands, limbs, garbled letters, warped scale |

**The two exceptions:**

1. A change to the product's own **color, shape, material, markings, or count** is a relevance failure. Every change to the product itself has one home, **product preservation**.
2. **A required advertiser logo must remain identifiable and faithful.** A logo that lost its design, or became unreadable, fails as a logo even though mangled letters are otherwise rendering.

You do not work out what caused either change.

### Three questions that are not yours

- **Is it different from the original?** It is supposed to be. A big change is not a Fail by itself.
- **Is it good advertising?** The advertiser already decided. You check whether their decisions survived.
- **Is it well made?** Other tasks. Beautiful and irrelevant can both be true.

## Step 1: Set The Ad Type

The pre-selection comes from an automated check and **can be wrong. Correct it before labelling**,
because it decides which failure reasons you see.

**The test: what does the customer actually pay for?**

| If the customer... | It is |
|---|---|
| Walks away owning the thing in the image | **Hero** |
| Pays for work, access, an experience, or a result | **Non-Hero** |
| Buys software, an app, or a game | **Non-Hero**, with the interface held as strictly as a product's body |

A service ad often shows physical things (the car being detailed, the windows being cleaned, the
restaurant's signature burger). **Those belong to the work, not the shelf.** Physicality is not the
test. A restaurant is Non-Hero even when its ad is a burger.

## Step 2: Read The Original Before You Open The Output

Three questions, in order:

1. **The problem.** What problem is this business solving? Usually in the headline.
2. **The payoff.** What does the buyer get? Almost always: look better, feel better, save money, make money, or save time.
3. **The support.** What else is doing sales work? Selling points, prices, demonstrations, proof, partnerships. **Two brands in one image means a collaboration, and its people and objects are part of the deal.**

**If the problem or the payoff is gone, it is a Fail, however good the image looks.**

### Translate claims into something you can look for

| The claim | What must be visible |
|---|---|
| "Most advanced compression system" | The bag reads as packed down |
| "No metering" | No gauge or usage bar |
| "$9.99 a month" | That exact figure, unchanged |
| "Fold It. Store It." | A product that folds |
| "Tub-to-Shower Conversion" | A conversion, not a room that still has the tub |

**The larger and more deliberate the advertiser made a line, the more certainly it must survive.** A price
printed larger than the headline is the clearest case. Its size in the output does not need to match. It
just has to be there.

### Signals that something must survive

- **A name printed under a person.** That person must survive.
- **Two brands in one image.** A collaboration. Its people and objects are part of the deal.
- **A price printed larger than the headline.** That number is the hook.
- **Partnership copy.**

Without those signals, you are not expected to recognise anyone. A model may change.

## Step 3: Open The Generated Ad

**Find the product first.** When the ad names a product, locate it in the generated image before looking
at anything else. Two of the guideline's worked failures are an ad whose product vanished while the mood,
the lighting and the offer text all survived.

Then work down the reasons for the ad type.

### Working rules

- **Look at the two images side by side at normal size.** A difference you only find by zooming in is not a Fail.
- **Judge the pair, not the recipe.** A style that failed on one ad can be right for another.
- **Read the copy before judging a bold change.** Copy can license a change. "Go big or go home" plus an oversized product means the exaggeration is the message. Licensing one change does not license anything else.
- **Additions must be intentional.** Placed the way a photographer would place them. A random object next to the product distracts rather than accents.
- **An interface is not raw material.** It cannot be invented or improved, only preserved.
- **Never invent what the advertiser does not have.** An invented room, view, amenity, interface, or product is false advertising, even when it looks great. The customer who shows up will not find it.
- **The landing page is a backup.** Use it when you cannot tell what the product or service is, to verify a new product angle, and before calling a scene invented, because a scene you have never seen may be real.

## The Logo Rule

**A required advertiser logo must remain identifiable and faithful.** The Fail button lists the logo
first among what can break an ad.

| Change | Verdict |
|---|---|
| Logo moved to another corner, resized | **Allowed** |
| An otherwise exact colored logo rendered in black or white | **Allowed** |
| The logo's design changed, parts dropped, or it is no longer identifiable | **Logo exists but is wrong** |
| An invented brand mark, where the original had no logo | **Logo exists but is wrong** |
| The original had a logo and it did not survive | **Required logo is missing** |

**Judge the logo's complete design, not its placement.**

**"Missing" only applies when the original owed you a logo.** An invented mark on an ad that had none is
not missing. It is present and wrong.

The two reason names are taken from the knowledge-check wording. The exact checkbox labels after Fail have
not been captured yet, so match these to whatever the UI calls them.

## The Failure Reasons

Check **every** reason that applies. Right verdict with the wrong reason is a real error here.

### Hero (product ads)

| Reason | Fails when |
|---|---|
| **Lost the core product** | The product is absent, replaced, or reduced to less than what was sold |
| **Altered the product** | Any change a customer could notice to shape, color, material, markings, or count. A new angle only if the advertiser can verify it |
| **Added or invented irrelevant products** | Anything with no source in the input. A specific invented product always fails. An object placed without intention fails for distracting |
| **Irrelevant use case** | Used in a way never intended: wrong purpose, wrong method, a demonstration of something it does not do. **Judges the action alone, not who or where** |
| **Irrelevant casting** | The person does not fit who the ad is for or what it promises, or a signalled face was changed |
| **Scene does not fit the product** | The setting contradicts where or how the product belongs, or distracts instead of accenting. A new setting is allowed when it complements |
| **Invented scene** | A scene that *is* the message (a location being sold, a season, an occasion) replaced |
| **Missing or incorrect selling points or headlines** | A critical line gone, a claim rewritten into something never said, or a prominent price missing. Rephrasing and reordering are fine |

### Non-Hero (service ads)

| Reason | Fails when |
|---|---|
| **Digital product preservation** | An app, game or software interface arrives with invented screens or platforms, lost core interface, recolored or embellished design, or covered or misaligned elements |
| **Added or invented irrelevant products** | A specific, identifiable product fabricated where there was none. Generic is fine only when selling a service or category: a delivery app may gain a generic burger, a burger brand may not gain an invented signature burger |
| **Irrelevant use case** | Work performed in a way the business never would: wrong method, wrong handling, wrong moment of the job, physically impossible. **Would this business actually do the work this way?** |
| **Irrelevant casting** | The person no longer supports the service: demographic clash, appearance that contradicts the promise, a passive pose that says nothing |
| **Changed a person who should be preserved** | A performer, speaker or named person replaced or altered past recognition, when a printed name, poster face, or partnership copy says preserve |
| **Scene does not fit the service** | Missing **subject** (the thing worked on), wrong **world** (the input's visual language), or materials with no life (the **dream** being sold) |
| **Invented scene** | A scene that carries the business replaced with a room, view or amenity the advertiser does not offer. **Check the landing page first** |
| **Missing or incorrect selling points or headline** | Same as Hero, and it **weighs more** here, because a service ad's words often carry the whole offer |

### The pairs people confuse

These are the boundaries the assessment tests. Each is decided by asking **what actually changed**.

| If | It is | Not | Worked example |
|---|---|---|---|
| The product is gone or swapped | Lost the core product | Altered | Champagne bottle became glasses and a bucket |
| The product is there but its body changed | Altered the product | Lost | Blush foldable bag became a hot-pink rigid case |
| The product is intact but used wrongly | Use case | Altered | Cream drunk from an intact, correctly labelled jar |
| The room is right but the work is wrong | Use case | Scene | Extraction cleaning became spray-and-wipe |
| The setting is the wrong world | Scene does not fit | Invented | Racecourse became an esports arena |
| The setting is an asset the advertiser does not have | Invented scene | Does not fit | Aurora beach became a luxury glass suite |
| An existing asset was isolated and the selling view lost | Scene does not fit | Invented | Villa's own hot tub moved into a studio, sea view gone |
| The person no longer fits the audience or story | Casting | Preserve | Two women became two men; a lone awkward dancer |
| A signalled person was swapped | Preserve (Non-Hero) or casting's signalled-face clause (Hero) | Casting fit | Students with names and ranks replaced |
| Something new appeared and the product survived | Added or invented | Lost | A wrench beside intact coffee pods |
| The product vanished and something else took its place | Lost the core product | Added | Charger became glasses and a pen |
| The logo moved or turned black or white, same design | Pass on logo | Logo wrong | Knowledge check |
| An invented mark appeared where no logo existed | Logo exists but is wrong | Logo missing | Knowledge check |

## Mandatory Workflow

1. **Set the ad type.** Customer owns it: Hero. Pays for work, access, experience, result, or software: Non-Hero. Correct the pre-selection if needed.
2. **Read the original.** Problem, payoff, support. Note every signal: printed names, second brands, oversized prices.
3. **Translate the claims** into things you can look for.
4. **Open the generated ad and find the product first.**
5. **Check survival** of problem, payoff and support.
6. **Check the logo.** Present, identifiable, and the same design? Placement and a black or white conversion do not matter.
7. **Read the copy** for anything that licenses a bold change.
8. **Walk the reason list** for the ad type. Check every one that applies.
9. **Confirm each reason names what actually changed**, using the confusion table.
10. **Compare side by side at normal size.** Drop anything that only shows under zoom.
11. **Write one sentence** naming the element that survived or broke.

## How To Write The Comment

The guideline asks for **one sentence on what survived or broke, naming the element.** The voice follows
the house style used across these skills, taken from the Omni ELO skill.

### The persona

**An average person looking at two ads on their phone.** Not an ad reviewer, not a brand strategist, not a
rubric.

- **Do not talk about:** "product preservation," "relevance," "core selling proposition," "message integrity," "failure reason," "brand equity."
- **Do talk about:** what is gone, what changed, what got added, what the person is doing.

### Rules

1. **Name the element.** The bottle, the headline, the $14,999, the game board, the wrench.
2. **Say what happened to it**, plainly: gone, swapped, a different color, added, moved.
3. **One sentence.** The guideline's own comments run five to twenty words.
4. **No em dashes and no semicolons.** Several of the guideline's exemplars use a semicolon. Join the two halves with "and", "but", "while" or a comma instead, which keeps it one sentence.
5. **Use "while" instead of "whereas".**
6. **Avoid absolutes.** Not "perfectly preserved." Say "kept" or "still there."
7. **No filler.** No "as the ad intended," "just like the original asked."
8. **No snark or emotion.** Not "hilariously," "absurd," "disaster." "She is drinking the cream" is enough.
9. **Banned:** "garbled," "gibberish," "hallucinated," "fails the constraint," "suffers from," "; note that." Rendering words are out of scope anyway.
10. **Do not restate the label.** The Pass or Fail is recorded. The sentence is for what you saw.
11. **Do not explain the rule.** "Invented scenes are false advertising" belongs in your head, not the comment.

### Fail comments

The guideline's own comments, adapted only where they used a semicolon:

```markdown
The bottle is gone, replaced by two glasses and a bucket.
```

```markdown
Different color, and the foldable bag became a rigid case.
```

```markdown
A random wrench appeared and the headline is gone.
```

```markdown
She is drinking the cream.
```

```markdown
The two women became two men, and the campaign is written for women.
```

```markdown
The sea view is what is being sold, and a hot tub in a studio loses the point.
```

```markdown
The game board is gone and only the art and floating score text remain.
```

```markdown
The names and ranks stayed but the people changed.
```

```markdown
Horse racing became two esports players at PCs.
```

```markdown
The tour became a luxury glass suite the advertiser does not offer.
```

```markdown
The headline and the $14,999 price are gone.
```

### Pass comments

The guideline gives no standalone Pass comment, so these follow the same shape: the element, and that it
made it over.

```markdown
The bottle, the 2 for $99 offer and the store name all made it over into the new setting.
```

```markdown
The same box, the 10X caffeine claim and the headline are all still there on a new background.
```

```markdown
The group dancing with the festival behind them keeps the all night party feel.
```

### Bad comments

- "The generated ad demonstrates strong message preservation and maintains brand integrity." Rubric voice, names nothing.
- "Fail because the product was altered." Restates the reason, names nothing.
- "It looks way better than the original." Quality is out of scope.
- "The wrench is hilariously out of place." Snark.
- "The headline text is garbled." Rendering, and a banned word.
- "Invented scenes are false advertising, so this fails." Explains the rule instead of naming the element.

## Output Format

Give the answer in the chat. Never modify the user's task files.

```markdown
**Ad type:** <Hero | Non-Hero> (pre-selected <X>, <kept | corrected because ...>)

**Original ad:** Problem <...>. Payoff <...>. Support <...>. Signals <names, second brands, oversized price, or none>.

**What survived:** <...>
**What broke:** <...>

**Label:** <Pass | Fail>
**Reasons to check:** <every reason that applies, or none>

**Comment (optional):** <one sentence, following the rules above>
```

## Final Checklist

- [ ] Ad type set by what the customer pays for, and corrected if the pre-selection was wrong.
- [ ] Problem, payoff and support read off the original before opening the output.
- [ ] Every survival signal noted: printed names, second brands, oversized prices, partnership copy.
- [ ] Claims translated into visible things, then looked for.
- [ ] The product located first in the generated ad.
- [ ] Product body compared: color, shape, material, markings, count.
- [ ] Logo checked: identifiable and the same design. Placement and black or white are allowed. Invented marks are wrong, not missing.
- [ ] Copy read for anything that licenses a bold change.
- [ ] Every applicable reason checked, and each one names what actually changed.
- [ ] Nothing failed for being different, for being ugly, or for a rendering defect.
- [ ] Nothing failed on a difference visible only under zoom.
- [ ] Landing page checked before calling a scene invented.
- [ ] Comment is one plain sentence naming the element, with no em dashes, semicolons, or rubric words.
- [ ] Answer given in the chat. No workspace file was modified.
