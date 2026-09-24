# Worked Cases

Four pairs from the guideline's Good vs Bad Calls section, with the images in `examples/`.
Source: `HANDSHAKE-AI/ads-creative/vs-1786693813-260813-ads-creative-i2i-q6-text-style.md`.

Each case gives the correct call, the exemplar feedback, the wrong call the module warns against, and
notes from looking at the actual images.

The quoted feedback is the guideline's, and most of it runs past the 100-character limit for this task.
Take the reason from it, not the length. Trimmed versions are in SKILL.md under How to Write the Feedback.

## Contents

- [Case 1: A Restrained Lockup Against A Wall Of Text](#case-1-a-restrained-lockup-against-a-wall-of-text)
- [Case 2: Same Words, Different Design](#case-2-same-words-different-design)
- [Case 3: The Same Overlay In Both Is A Tie](#case-3-the-same-overlay-in-both-is-a-tie)
- [Case 4: Only One Output Has An Overlay](#case-4-only-one-output-has-an-overlay)
- [What The Four Have In Common](#what-the-four-have-in-common)

## Case 1: A Restrained Lockup Against A Wall Of Text

`examples/case1-course-A.jpg`, `examples/case1-course-B.jpg`

An online-course ad for "AI Mastery Toolkit 2.0". Both outputs promote the same offer.

**What is actually on each image:**

- **A.** Overlay: the headline "START LEARNING AI TODAY" in white with "LEARNING AI" in yellow, and one outlined pill "NO CODING • BEGINNER FRIENDLY". Everything else, including the big "AI MASTERY TOOLKIT 2.0" title, the subtitle and the four icons, is **printed on the product box**, so it is picture, not overlay.
- **B.** The same headline and pill, then a purple brush-stroke "GET INSIDE ME,", six coloured feature rows with icons, two tip lines, a green-tick checklist, a red "ONLY ₹197" price flash, a "PREMIUM BONUSES." bar, a six-item bonus strip, and three trust tiles. At least five type treatments, and every colour on the wheel.

**Correct: Output A — clearly better style.**

> "A is one bold headline and one badge with room to breathe, so the eye goes straight to the offer. B stacks feature rows, a checklist, a price flash and bonus strips in a dozen type styles, and nothing stands out first."

Both overlays are readable and on-message, so a quick glance says "both fine". The lenses separate
them. A has hierarchy, one typeface family and space. B has too much text and too many fonts, so no
element leads. Campaign-ready against a design failure is the first anchor row: clearly, not slightly.

**Wrong: Output B — slightly better style.** "B gives the buyer far more information and shows everything
included in the offer." Information count is not a style lens, and B's volume is what destroys its
hierarchy.

**Image notes.**

- **B is riddled with typos**: "greal results", "scale your with AI", "FREELANCER CLIENT RIT", "DISCOVER MULTIPAYS EARN MNEY". **The exemplar feedback does not mention one of them.** The call rests on layout and typography alone. This is the scope rule in action: B would lose clearly even if every word were spelled right.
- A's overlay is small. Most of what looks like A's "design" is the box cover. Do not credit A, or penalize it, for the box.

## Case 2: Same Words, Different Design

`examples/case2-hotel-A.jpg`, `examples/case2-hotel-B.jpg`

A hotel-stay ad for BÂRMA Courchevel. Both outputs carry identical wording and the same logo.

**What is actually on each image:**

- **A.** A solid dark-green band across the top holding the serif headline "Votre hiver à Courchevel" and the caps line "LES RÉSERVATIONS SONT OUVERTES !". A second solid green band across the bottom holding the bear logo and "BÂRMA COURCHEVEL". The photo is squeezed into the middle.
- **B.** The same headline and caps line in white, set directly on the textured wall above the bed. The bear logo and wordmark sit small on the green blanket at the bottom. No bands.

**Correct: Output B — slightly better style.**

> "Same lines in both, but B sets them straight into a quiet zone of the photo, which reads airy and premium. A walls them into two heavy solid bands that look pasted on."

The identical-overlay tie is for identical designs. Here the words match but the treatment does not.
That is a nameable placement-and-layout edge, and B is the one that could run in a high-end campaign.
**Slightly, not clearly, because A has no outright failure.** Its bands are aligned and readable, just
heavier-handed.

**Wrong: Similarly good/bad.** "The text is word-for-word the same in both, so the style is the same." A
same-overlay tie needs the same font, size, position and treatment.

**Image notes.**

- The band colour in A picks up the blanket's green, so colour is not A's problem. The edge is placement and layout. Name those.
- This case sets the line between slightly and clearly. Heavy but tidy is slightly. Covering the subject or having no hierarchy is clearly.

## Case 3: The Same Overlay In Both Is A Tie

`examples/case3-salon-A.jpg`, `examples/case3-salon-B.jpg`

A Hungarian hair-extension salon ad. Each output shows a review card, a headline, a subhead and a
button.

**What is actually on each image:**

- **Both.** A gold gradient review card with five stars, the quote "Végre dús a hajam a fejtetőn is, teljesen láthatatlan!" and a beige "elégedett ügyfél" footer. A dark serif headline "Prémium orosz haj, láthatatlan dúsítás". A sans subhead "Fájdalommentes nanokapszulás technika Budapesten". A gold "Időpontot foglalok" button. Same fonts, colours and positions.
- **What differs:** the photo crop and the file resolution (A is larger and framed slightly wider).

**Correct: Similarly good/bad.**

> "Both outputs carry the identical review card, headline, subhead and button, with the same fonts, colours and positions. The overlays are the same design, so they tie."

The models often keep the original overlay and change only the picture, so expect this often. The prompt
asks you to say when the overlays are the same. Do not look to the photos for a winner.

**Wrong: No overlaid text to compare.** "There is no difference between the overlays, so there is nothing
to compare." That button means the overlays are **missing**, not that they match.

**Image notes.**

- The crop difference makes the card sit at a slightly different spot relative to the chair. That is the picture moving under a fixed overlay, not a design difference. It does not break the tie.
- Resolution difference is a file property. Ignore it.

## Case 4: Only One Output Has An Overlay

`examples/case4-footwear-A.jpg`, `examples/case4-footwear-B.jpg`

A sandal ad for Lady Modesta shoes.

**What is actually on each image:**

- **A.** Sandals on a marble table beside two white shoeboxes. The only words are small printed lines on the box lids ("Ready for your day..", "From : Lady Modesta shoes", plus some garbled lines). That is packaging: **A has no overlay at all.**
- **B.** Sandals on rattan shelves. Overlay: a large white serif headline "Ready for your day..", a small sans caption "From : Lady Modesta shoes" at top left in the dark space, and a small letter-spaced footer "KHIMAR HIGH QUALITY • LADY MODESTA SHOES" at bottom centre.

**Correct: Output B — clearly better style.**

> "A's only words are printed on the shoeboxes inside the photo, so that is packaging, not overlay. B's overlay (serif headline, small caption, letter-spaced footer) sits well in the empty space and is campaign-ready."

Two rules meet. The scope rule makes A text-free. The one-sided rule says judge the lone overlay on its
merits. It is campaign-ready, so its output wins clearly. Had it been a mess, the text-free output would
have won. A middling one would be Similarly good/bad.

**Wrong: Similarly good/bad.** "A's box lettering is a bit mushy but B's text is nicer, so roughly even
overall." This grades packaging as overlay, the scope mistake the task warns about most.

**Image notes.**

- B's headline ends in a double period ("day.."). That is punctuation, not design, so it is out of scope.
- A's box print is partly garbled. Also out of scope twice over: it is in-scene and it is a rendering issue.
- **Do not answer No overlaid text to compare.** Only A is empty. That button needs both sides empty.

## What The Four Have In Common

- **Every wrong answer reached outside the overlay's design**: to information count, to word matching, to the no-text button as a shrug, to in-scene lettering.
- **No exemplar note mentions spelling**, even where the image is full of typos (Case 1) or odd punctuation (Case 4).
- **Two of the four correct answers are clearly, one is slightly, one is a tie.** Clearly came with a design failure (Case 1) or a lone campaign-ready overlay (Case 4). Slightly came with a single edge over a tidy but heavy loser (Case 2).
- **The no-text button is never the right answer in these four**, and it is the wrong answer in one. It is for pairs where both sides have nothing laid over the photo.
