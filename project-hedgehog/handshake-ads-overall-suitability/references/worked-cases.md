# Worked Cases

Six pairs from the guideline's Good vs Bad Calls section, with the images in `examples/`.
Source: `HANDSHAKE-AI/ads-creative/vs-1786660967-260813-ads-creative-i2i-q0-overall-ad-suitability.md`.

Each case gives the correct call, the exemplar feedback, and the wrong call that the module warns
against. **In every bad example the annotator skipped the scan and rated a first impression.**

## Contents

- [Case 1: Graphics That Attack The Product](#case-1-graphics-that-attack-the-product)
- [Case 2: Read Every Mark, Logos Included](#case-2-read-every-mark-logos-included)
- [Case 3: Both Clean, Zoom-Only Difference](#case-3-both-clean-zoom-only-difference)
- [Case 4: Both Fail, Different Ways](#case-4-both-fail-different-ways)
- [Case 5: The Product Must Match The Seed](#case-5-the-product-must-match-the-seed)
- [Case 6: A Flyer Of Invented Claims](#case-6-a-flyer-of-invented-claims)
- [What The Six Have In Common](#what-the-six-have-in-common)

## Case 1: Graphics That Attack The Product

`examples/case1-dogmat-seed.jpg`, `case1-dogmat-A.jpg`, `case1-dogmat-B.jpg`

German dog cooling mat, advertiser ECCS 3, brand PfotenVital. The seed is a two-panel comparison: a
leaking gel mat on the left under a **red X**, the advertised blanket on the right under a **green
check**, with captions and a "JETZT KAUFEN — 50% RABATT" bar and an "81.000+ Zufriedene Hundebesitzer"
badge.

**Strongly Prefer A.**

> "Every line on both responses is on the seed, so text does not decide this pair. A keeps the
> bad-vs-good split intact: the competitor mat sits under the red X and the advertised blanket under
> the green check. In B the red X and the warning caption sit on the advertised blanket itself, so the
> ad condemns the product it is selling."

B collapsed the two-panel comparison onto a single photo of the PfotenVital blanket, so its own warning
mark now points at the product being sold. **No campaign can run an ad that attacks its own product.**

Two things worth noting. The 50% discount and the 81,000+ figure look like invented specifics, and would
be dealbreakers if they were, but **both are on the seed**, so they are grounded. That is why the text
check comes first. And the brand on the seed differs from the advertiser's name in the brief, which is
fine because it is visible on the seed.

**You do not need to read German to see the failure. Follow where the X and the check point.**

**The wrong call: Slightly Prefer B, "B is cleaner and more minimal, one photo instead of a cluttered
split layout."** This treated the layout as decoration and never asked what it communicates. A minimal
look does not help when the visual logic condemns the product.

## Case 2: Read Every Mark, Logos Included

`examples/case2-technician-seed.jpg`, `case2-technician-A.jpg`, `case2-technician-B.jpg`

No advertiser, no headline, no description, no primary text. **The seed is the only source of grounded
text**, and both responses stick to it.

**Strongly Prefer B.**

> "Both keep the seed's copy and add nothing. The chest logo on A's technician is garbled; zoomed in,
> the lettering is malformed rather than readable, and A's button text is rendered in hollow outlines.
> B renders the same logo crisply and keeps every text block clean."

Both look plausible at a glance. Reading every word, **logos included**, catches it. An unreadable brand
mark on the person representing the company is disqualifying. B's busier background is at most a matter
of taste and B has no comparable defect, so only B is campaign-ready and the preference is strong.

**The wrong call: Slightly Prefer A, "A's calmer background feels more professional than B's busy street
scene."** Background mood is a polish edge at best and cannot outweigh an illegible brand mark. This
annotator formed a first impression and skipped the scan, so the garbled chest logo was never read.

## Case 3: Both Clean, Zoom-Only Difference

`examples/case3-tutoring-seed.jpg`, `case3-tutoring-A.jpg`, `case3-tutoring-B.jpg`

Korean online tutoring, advertiser Eduhome, brief copy all in Korean.

**Tie.**

> "Both keep the seed's comparison layout and every line of its Korean copy, add no text, and render
> faces, hands, and the CTA banner cleanly. The two backgrounds differ in taste only. A is slightly
> sharper at full zoom, but at normal viewing size nothing separates them."

Every check passes on both sides. **If you cannot read Korean, judge letterform quality and placement**;
the direction and brief tell you the message is a free tutoring assessment, so nothing looks out of
place. The only difference is slightly sharper type in A at maximum zoom, which is **a file property,
not an ad quality.**

Note the tie note still says what was checked. That is the standard for a tie.

**The wrong call: Slightly Prefer A, "A is a bit sharper when zoomed all the way in."** This forces a
preference out of a difference nobody would ever see. "Sharper at 200% zoom" will not hold up in review.

## Case 4: Both Fail, Different Ways

`examples/case4-laptop-seed.jpg`, `case4-laptop-A.jpg`, `case4-laptop-B.jpg`

Dual-screen laptop, advertiser Marie Claire UK, **no copy in the brief**. The direction explicitly asks
for a "bold, sans-serif, Red/Yellow price/CTA (second read)".

**Tie.**

> "B prints 'NOW £2,299', 'INTEL CORE ULTRA 9', 'RTX PERFORMANCE' and 'NEBULA DISPLAY'. The brief has
> no copy and the seed has no text beyond the logo, so every one of those is invented; only 'MARIE
> CLAIRE UK' is grounded, as the advertiser's name. A adds no marketing copy, but part of its second
> screen has broken off and floats beside the keyboard, and the sticker on the palm rest is an
> illegible smear. Both fail, and neither is closer to usable."

This is the clearest illustration of **a requested slot not grounding a value**. The direction asked for
a price, which is why B has one, but the brief supplies none, so the number came from nowhere. B's clean
spelling and retail-flyer energy do not change that.

A carries a different dealbreaker: the product is warped, with part of the second screen detached and
floating, plus an illegible sticker. **Two failing responses of similar weight make a Tie, and the
feedback names both failures.**

**The wrong call: Strongly Prefer B, "B clearly states the product's specs and pricing, which helps
inform buyers."** The guideline calls this "the miss to watch for": rewarding information without asking
where it came from.

## Case 5: The Product Must Match The Seed

`examples/case5-shoe-seed.jpg`, `case5-shoe-A.jpg`, `case5-shoe-B.jpg`

Running shoe. The direction asks for a **global warm grade**: "shift white-balance to rich amber, wash
space with warm tungsten ambient light."

**Strongly Prefer B.**

> "Both keep the logo and 'LIMITED STOCK NOW' intact and add no text. In A the shoe's grey mesh upper
> has turned tan and the heel brown, so this is no longer the shoe on the seed. B warms the whole
> scene, its backdrop goes amber, but the upper stays grey."

Both responses apply the warm grade the direction asked for. **The rule allows lighting that warms the
whole scene; it does not allow the product to change color.** The seed's mesh is neutral grey, A's is
sand-colored, and A's midsole shifted with it. B's upper still reads grey under the same warm light.

**Neither response rendered the brief's headline, and that is not required.** Dropping the brief's copy
is no more a flaw than dropping the seed's.

**The wrong call: Slightly Prefer A, "A is crisper and the warm orange glow feels more premium."** The
annotator judged mood before comparing the product with the seed. **Do the product check first. The seed
is on screen for that reason.**

## Case 6: A Flyer Of Invented Claims

`examples/case6-bankcard-seed.jpg`, `case6-bankcard-A.jpg`, `case6-bankcard-B.jpg`

Banking card, advertiser GIMC, **no copy in the brief**. The direction asks for headlines and icons
about financial benefits.

**Strongly Prefer B.**

> "A prints 'UP TO 5% CASHBACK', '0€ MONTHLY FEE' and 'AVAILABLE ACROSS EU'. The brief has no headline,
> description, or primary text, and the seed's only text is the bank's name, so those are invented
> specifics. 'BANKING MADE EFFORTLESS', 'FAST • SECURE • REWARDING' and 'SIMPLIFY. SAVE. SUCCEED.' are
> invented generic lines on top. Only the bank's name and the advertiser's name on A are grounded. B's
> only text is the bank's name, which is on the seed, and nothing else is wrong with it."

Both tiers appear on the same response here, which makes the ladder visible: the percentages and fees
are **specifics** (dealbreakers), the slogans are **generic lines** (serious flaws), and
"GET YOUR CARD TODAY" is a **generic call to action** that would have been fine on its own.

**The country codes and age range along A's bottom edge are targeting settings, not copy.** Do not sort
them as ad text, and do not rest the call on them.

**The wrong call: Strongly Prefer A, "A is a complete ad: headline, benefits, fees, markets, and a call
to action. B is just a card and a bag."** Completeness does not help when the content comes from
nowhere.

## What The Six Have In Common

**Every bad example is a first impression that skipped the scan.** Cleaner, calmer, crisper, more
premium, more complete: each is a real observation that lost to something the annotator never checked.

The correct calls split evenly across the scale, which is worth internalizing on its own:

| Case | Call | Why |
|---|---|---|
| 1 Dog mat | Strongly Prefer A | B's own warning mark points at the advertised product |
| 2 Technician | Strongly Prefer B | A's chest logo is garbled |
| 3 Tutoring | Tie | Everything passes; only a zoom-level sharpness difference |
| 4 Laptop | Tie | B invents a price and specs; A's product is warped |
| 5 Shoe | Strongly Prefer B | A recolored the product under cover of a warm grade |
| 6 Bank card | Strongly Prefer B | A is built from invented specifics and generic lines |

Four Strongly calls and two Ties, and **no Slightly among the correct answers** while every wrong answer
except one is a Slightly. A Slightly is for a real, nameable polish edge between two campaign-ready
responses. It is not where you land when you have not finished checking.
