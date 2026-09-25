---
name: handshake-ads-text-flaws
description: Evaluate Handshake Ads Creative text flaws comparisons. Use when a task shows a seed image, a creative direction, an ad brief and two finished ad images (Output A and Output B) and asks whose overlaid text and graphics have fewer flaws (rendering, fidelity to the seed and brief, language), ignoring design and the picture behind them; when the buttons read clearly fewer text flaws, slightly fewer text flaws, similarly good/bad, or No overlaid text to compare; when the task says ads creative, Fewer Text Flaws, grounded text, or Compare Two Ad Images.
---

# Handshake Ads Text Flaws

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, this SKILL.md is the operative rubric. Say that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `HANDSHAKE-AI/ads-creative/vs-1786692229-260813-ads-creative-i2i-q5-text-flaws.md`, the full guideline. It is the complete source material for this task: there is no separate cheat sheet or instruction PDF.
2. This SKILL.md, which compresses the guideline and adds what the example images show.
3. `references/worked-cases.md`, the six graded pairs with their images in `references/examples/`.

Before rating a live item, read `references/worked-cases.md` once per session.

This question measures one thing: **which output's overlaid text has fewer flaws, checked against the
references.** A flaw is a rendering error, text that did not come from the seed or the brief, seed text
that was dropped or changed, or text in the wrong language. Nothing else is judged. Not the design, not
the picture, not how closely the output followed the direction.

> A flawless photo under a garbled headline loses here, and a broken photo under clean, grounded text can
> win. An ugly overlay with correct, grounded text has zero flaws. A beautiful one with a misspelling has one.

## Four Siblings, Four Scope Rules

This is the **Q5** question in the Ads Creative I2I set. The same finished ads are judged by sibling
questions with **conflicting scope rules**. Working one right after another is where mistakes happen.

| | Q5 Text Flaws (this skill) | Q6 Text Style | Q4 Visual Appeal | Q0 Overall Suitability |
|---|---|---|---|---|
| Skill | `handshake-ads-text-flaws` | `handshake-ads-text-style` | `handshake-ads-visual-appeal` | `handshake-ads-overall-suitability` |
| Judge | **Only the overlay's correctness and grounding** | Only the overlay's design | Only the picture | The whole ad |
| Spelling / garbled text | **The core of the question** | Out of scope. Costs nothing | Out of scope | Dealbreaker |
| Layout, fonts, colour | **Out of scope**, except contrast too low to read | The whole question | Out of scope | In scope |
| The picture | Out of scope | Out of scope, except as the surface | The whole question | In scope |
| References shown | **Seed, creative direction, ad brief** | None | None | Seed, creative direction, ad brief |
| Buttons | Clearly/slightly fewer text flaws, Similarly good/bad, **No overlaid text to compare** | Clearly/slightly better style, Similarly good/bad, No overlaid text to compare | Clearly/slightly more appealing, Similarly good/bad | Strongly/Slightly Prefer, Tie |

**How to tell Q5 from its neighbours.** Q5 and Q0 both show the seed, direction and brief; Q5's buttons say
"fewer text flaws", Q0's say "Prefer". Q5 and Q6 share the six-button layout and the no-text button;
Q6 shows no references and its buttons say "better style".

**The shared trap.** A misspelled headline in a well-designed overlay. On Q6 it costs nothing. **Here it is
a flaw**, and design cannot buy it back. The reverse also holds: a font you find hideous, sitting awkwardly
over the product, is **zero flaws here** if every word is correct, legible and grounded.

A fifth sibling, `handshake-ads-relevance`, compares one original ad with one generated ad, Pass or Fail.

## Task Shape

- **Seed image** (the product or the original ad). What the model started from. Any text on it is a reference.
- **Creative direction** the model was given. Long directions are collapsed behind "Show more".
- **Ad brief:** advertiser, audience, objective, headline, description, primary text. Empty fields show "(none)" or "(not provided)". **About half of all briefs have no copy at all.**
- **Output A and Output B**, the two finished ads you compare. Click an image to magnify it.
- One question: "Which image's overlaid text and graphics have fewer flaws? Ignore the picture behind them."
- Six buttons:
  - Output A — clearly fewer text flaws
  - Output A — slightly fewer text flaws
  - Similarly good/bad
  - Output B — slightly fewer text flaws
  - Output B — clearly fewer text flaws
  - No overlaid text to compare
- One feedback field: "In a sentence or two, name the text flaw that decided it — or say why there was no overlaid text to compare."
- Two reject buttons below the form: "Image did not load" and "Inappropriate content".

## What The References Are For

The seed, the direction and the brief tell you **what the ad was meant to say and in which language.**
Use them to sort every line of overlaid text.

| Reference | What it gives you |
|---|---|
| **Seed image** | Grounded wording, from its overlay **and from its picture text** (box print, packaging, dial). Also the overlay copy that must be kept. Also the language, if it has text |
| **Ad brief copy fields** (headline, description, primary text) | Grounded wording, paraphrasable when meaning and facts match. Also the language |
| **Advertiser name** | Always grounded, spelled exactly as the brief spells it. **Does not set the language** |
| **Creative direction** | Context only. It can ask for a **type** of element (a price, a CTA, labels). **It never supplies the value** |

Two things the references are not for:

- **Not an adherence check.** Ignoring the direction is not a flaw here. Another task measures that.
- **Not a design brief.** Layout, placement, fonts and colour belong to Q6.

## What Counts As Overlaid Text

| Overlaid text (judged) | Picture text (never judged) |
|---|---|
| Headlines, captions, subheads | A product label, packaging copy, box print |
| Price badges, seals, stickers, footnotes | A street sign, a shop sign, a sign in the background |
| Buttons and calls to action | Print on a T-shirt or any garment, a chest logo |
| Banners, bands, messaging panels | Writing on a phone, laptop or app screen inside the photo |
| Logos and wordmarks placed on the image | A watch dial, a clock, a keyboard label |
| Labelled icons, feature rows, checklists | Branding printed on a product or bag in the scene |

**Test:** mentally strip the photo away. Whatever would still float on a blank canvas is overlay.

**All-design ads.** A flyer, a chart, an app or game screen: **every line on it is overlaid text.** The game
lobby in Case 4 is all overlay.

**Picture text only** means that output **has no overlaid text**. A garbled shirt logo or box print is a
picture flaw other tasks cover.

**Picture text on the seed is still a reference.** An output that lifts the seed's box wording into a
headline has grounded text (Case 5).

## The Three Flaw Families

Read **every word** on each output, fine print, button labels and logos included, with the references open.

1. **Rendering.** Misspellings, wrong or missing characters, broken word order, punctuation errors, repeated words, illegible or blurry letterforms, garbled pseudo-letters that imitate writing. A foreign or accented character dropped into a word where it does not belong. Text **cut off at an edge, colliding with other text, or too low-contrast to read**.
2. **Fidelity.** Overlaid text has to come from somewhere.
   - **Grounded:** on the seed (overlay or picture text), in the brief's copy fields, or the advertiser's name. A paraphrase is fine when meaning and facts match.
   - **Invented:** anything else. A requested slot filled from nowhere is invented.
   - **Seed overlay text dropped or changed** is also a fidelity flaw.
   - **Not flaws:** generic calls to action ("Shop now", "Learn more", "Book today"); incidental prop text that makes no claim (a call timer, a clock reading, a keyboard label); copying the seed's or brief's **own** spelling, even when it looks wrong.
3. **Language.** Overlaid text in a language that matches **neither the seed's text nor the brief's copy** is a flaw, whatever it says. The advertiser's name does not set the language. Non-Latin text is **never** a reason to reject. In a script you cannot read, judge letterform integrity and check the parts you can read. **Do not guess at spelling.**

**Brands.** A brand name is grounded if it is the advertiser's name **or visible on the seed** (a maker's
logo on the product counts). A third brand from nowhere, or a model name the references never state, is an
invented specific.

## Flaw Weights

Two tiers. **The tier decides between clearly and slightly.**

| Weighs "clearly" | Weighs "slightly" |
|---|---|
| A garbled, illegible or pseudo-lettered block | A single minor typo or one wrong character |
| An **invented specific**: a price, number, spec, certification, percentage, date, claim, or a brand or model name other than the advertiser's | A punctuation slip |
| **Dropped or changed core text**: the headline, the offer, the price, the brand name | **One** invented generic line ("Reliable, affordable") |
| Text in a language that matches neither the seed nor the brief | **One** dropped secondary element: a badge, a seal, a footnote, a generic button |
| **Several** "slightly" flaws on one side against a clean other side | |

**Specific versus generic.** A line that states something checkable (a number, a certification, a service
promise such as "24-hour dispatch", a named model) is a specific. A line of mood words that promises
nothing concrete ("Comfort you can trust", "Fast, secure, rewarding") is generic.

**Combining.** When both sides have flaws, the side whose flaws weigh less has fewer text flaws.

- One flaw each, one tier apart: **slightly**.
- A garbled block, or two or more clearly-tier flaws, against a side with only small slips: **clearly**.
- No flaw type outranks another automatically; **count and weight together make the call.**

## Out Of Scope

| Out of scope | Why it tempts you | What to do instead |
|---|---|---|
| **The picture.** Warped hands, melted products, odd lighting, wrong product colour | Loud, visible defects | Ignore. A broken photo under clean text can win |
| **Style.** Layout, placement, font choice, colour taste | An ugly overlay feels flawed | Zero flaws if every word is right and grounded. Contrast counts only when it makes text hard to read |
| **Picture text.** Labels, signs, garments, screens, dials | Garbled lettering looks like a text flaw | It is a picture flaw. Only the overlay layer is compared |
| **Adherence to the direction** | "B ignored the requested price" | Ignoring the direction is not a flaw. Filling its slot from nowhere is |
| **Word count** | "B has more information" | More text is not fewer flaws. Often it is more |
| **Extreme-zoom sharpness** | Pairs differ in resolution | Once every word reads correctly in both, extra sharpness is not fewer flaws |
| **Spelling you cannot verify** | An unfamiliar script or language | Judge letterforms and language match only |
| **The reference's own spelling** | An unusual brand spelling looks like a typo | Copying it is correct. "Fixing" it is a fidelity flaw |

## Mandatory Workflow

One to two minutes per item.

1. **Reject check.** Every image loaded (outputs and seed), and the content is allowed. See Rejections.
2. **Read the references.** Note any text on the seed, overlay and picture text, and its language. Skim the direction for requested text elements. Read the brief's copy fields and the advertiser name, **exactly as spelled**.
3. **Find the overlaid text.** For each output, strip the photo away and list what is on the design layer. Sort anything ambiguous into overlay or picture.
4. **Check the special cases, in this order:**
   1. **Neither output has any overlaid text or graphics** (picture text does not count): answer **No overlaid text to compare**. The only time that button is right.
   2. **Only one output has overlaid text:** see The One-Sided Rule. Never press the no-text button to escape it.
5. **Zoom and read every word on both sides**, fine print, button labels and logos included. Most text flaws are invisible at browsing size.
6. **Sort each line:** on the seed, in the brief, the advertiser's name, or invented; kept, dropped or changed; in the ad's language or not. **Also check what the seed had that the output lost.**
7. **List the flaws on each side with their tier**, then combine with the weights.
8. **Pick the answer** with the anchors below.
9. **Scope check before you commit.** Did the picture, the design, picture text, the direction, word count or zoom sharpness sneak into your reason? Remove it and re-decide.
10. **Write one or two sentences** naming the flaw that decided it: the line, where it sits, which output, which reference it is or is not in.

## Answer Anchors

| What the scan left you with | Your answer |
|---|---|
| One side has a clearly-tier flaw (garbled block, invented specific, dropped core text, wrong language) and the other side is clean | **Clearly fewer text flaws** for the clean side |
| Both sides have flaws, and one side's weigh much more (a garbled panel against one wrong word) | **Clearly fewer text flaws** for the lighter side |
| One side has a single slightly-tier flaw (one typo, one generic line, one dropped badge) and the other side is clean | **Slightly fewer text flaws** for the clean side |
| Both sides have flaws, one flaw each, one tier apart | **Slightly fewer text flaws** for the lighter side |
| Both overlays clean: all text grounded, nothing dropped, everything readable | **Similarly good/bad** |
| Both flawed, with no meaningful difference in weight | **Similarly good/bad** |
| Only one output has overlaid text, it is clean, and the seed had no overlaid text to preserve | **Similarly good/bad** |
| One output erased the seed's overlay copy; the other kept it cleanly | **Clearly fewer text flaws** for the side that kept it (**slightly** if only a minor element was erased) |
| Neither output has any overlaid text or graphics | **No overlaid text to compare** |

**Name it or tie.** If you pick a side, the feedback must name the flaw. If you cannot name one, the
answer is Similarly good/bad. Don't force a side to avoid "similar", and don't call "similar" on overlays
you have not read.

**Finding a defect does not mean a side wins.** It decides the pair only when it is in scope (Case 6).

## The One-Sided Rule

"No overlaid text to compare" needs **both** sides empty. Check for picture text first: a watch dial or a
shop sign can fill an image with words while the overlay layer stays empty on both sides.

If only one output has overlaid text, judge that text. **Then look at the seed before you score the
text-free side:**

| The seed | The text-free output | Compare with the other side |
|---|---|---|
| Had **no** overlaid text (the usual case: a bare product photo, a video still) | **Zero flaws** | Ties a clean text output (Similarly good/bad). Beats a flawed one |
| **Carried overlay copy**, and the output erased it | **Dropped-text flaw**: clearly if the core message or brand text is gone, slightly if only a minor element went missing | Weigh it against whatever the other output's text has |

**The fidelity rule wins over the "zero flaws" reading.** An output that erased the seed's copy is not a
zero-flaw text-free output.

Never press the no-text button to escape a one-sided pair, and never when both outputs have text, even a
little, even identical. The same clean wording on both sides is Similarly good/bad.

## Rejections

Reject only for these two reasons:

- **Image did not load.** An output **or the seed image** fails to load and the panel shows a load error.
- **Inappropriate content.** Nudity or sexually explicit poses, hate symbols or hate speech, graphic violence.

Do not reject for garbled or invented text (the vote records that), for an image with no text (the
one-sided rule or the no-text button covers it), for text in a language or script you cannot read, for
people in swimwear or underwear, or because the call is hard.

## Hard Gates

- Do not count picture text (labels, packaging, signs, garments, screens, dials) as overlay, for or against.
- Do not let the picture's defects or the overlay's design move the vote.
- Do not treat a value as grounded because the direction asked for that element.
- Do not penalize an output for ignoring the direction.
- Do not let the advertiser's name set the language.
- Do not "correct" the brief's spelling of a name. Copying it is right; changing it is the flaw.
- Do not call a line invented before checking every brief field **and** the seed's picture text.
- Do not score a text-free output as zero flaws when the seed carried overlay copy it erased.
- Do not press No overlaid text to compare unless **both** outputs lack overlaid text.
- Do not press No overlaid text to compare because two overlays match. That is Similarly good/bad.
- Do not reward more text, more information or sharper pixels.
- Do not guess at spelling in a script you cannot read.
- Do not pick a side you cannot name a flaw for.
- Do not reject for garbled text, missing text, a foreign script or a hard call.

## Calibration Cases

Six graded pairs from the guideline. Full versions, image notes and the exemplar feedback are in
`references/worked-cases.md`.

| The pair | Correct call | The trap |
|---|---|---|
| Pressure fryer. A's panel is letter salad after the headline. B's panel paraphrases the brief but adds "ISO/NSF Certified" | B — clearly | Calling it similar at browsing size, because both panels look like text |
| Car rental, brief with no copy. A has no text. B adds the advertiser's name plus "FORD FIESTA" and four marketing lines | A — clearly | Pressing No overlaid text to compare because A is empty |
| Chingari app. A's phone screen shows "Private Call" and "First 3 calls FREE"; A dropped the seed's "Call Now" button | B — slightly | Calling the screen text an invented offer. It is picture text, and it matches the brief anyway |
| Game lobby. A copies the seed with small misspellings. B rebuilds it in Japanese | A — clearly | Rewarding B's crisp rendering. Language and dropped seed text outweigh typos |
| Sandals. A's only words are garbled box print. B lifts the box wording into a clean headline | Similarly good/bad | Penalizing A's box print, or rewarding B for having text |
| Window cleaner. Both keep the seed's copy exactly. A's shirt logo is garbled | Similarly good/bad | Counting the shirt logo, which is picture text |

Three things stand out from the actual images:

- **The flaw that decides is often not the loudest one.** Case 4's B renders its Japanese perfectly, and Case 2's B is a clean, professional banner. Both lose clearly on fidelity and language.
- **Picture text can be garbled on the winning side.** Case 5's A has mangled box print and still ties; Case 6's A has a broken shirt logo and still ties.
- **Language is checked against the seed's text as well as the brief.** Case 5's brief copy is Indonesian, but the seed's box print is English, so B's English headline is grounded and in the ad's language.

## How to Write the Feedback

The form asks: *"In a sentence or two, name the text flaw that decided it — or say why there was no
overlaid text to compare."*

**Name the line, where it sits, which output, and which reference it is or is not in.**

### Rules

- **One or two sentences.** The deciding flaw first. Add the other side's flaws when they matter to the tier.
- **Quote the line.** "B prints 'NOW £2,299'", not "B has a wrong price".
- **Say where it sits** when it helps: headline, badge, button, footer, panel.
- **Say which reference it is or is not in:** "the brief has no copy and the seed has no text", "from the seed's boxes", "the brief's headline".
- **For a one-sided pair, say which side has text** and why the text-free side scores as it does.
- **For a tie, say what both keep** and that nothing separates them.
- **For the no-text button, say where the words actually are** ("every word is on the watches themselves").
- **Never mention design, the picture's quality, or how much text there is** as a reason.
- **No rubric vocabulary** in the note: not "clearly-tier", "fidelity flaw", "grounded" as a label on its own. Say what is wrong in plain words.
- **No em dashes. No AI power words** (delve, meticulous, seamlessly, elevate).

### Good Examples

From the guideline:

```markdown
B prints 'NOW £2,299' and a processor badge; the brief has no copy and the seed has no text, so those are invented. A has no overlaid text, and the seed had none, so A has zero flaws.
```

```markdown
Both keep the seed's headline and button letter for letter and add nothing; nothing separates them.
```

```markdown
Only B has overlaid text: the two lines from the seed's boxes and the advertiser's name, all clean. A's box print is picture text. One clean side against a text-free side is similar.
```

```markdown
Neither output has overlaid text; every word is on the watches themselves.
```

### Bad Examples

- ❌ "A's text looks better." Names nothing.
- ❌ "B has more information about the product." More text is not fewer flaws. Say where each line came from.
- ❌ "Both have a headline and a full messaging panel with the brand name and a website." Called at browsing size; one panel was unreadable.
- ❌ "A has no text, so there is nothing to compare." The no-text button needs both sides empty.
- ❌ "A invents a 'Private Call' feature and a free-calls offer." That is phone-screen picture text, and it matches the brief's headline.
- ❌ "B's text is sharp and correctly formed. A misspells several labels." Judged rendering only and missed the language flaw.
- ❌ "A's box labels are garbled; B's text is clean." Box print is picture text.
- ❌ "A's company logo is unreadable pseudo-lettering." It is on the technician's shirt.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present the evaluation in the chat using this template:

```markdown
### References
**Seed text:** [overlay and picture text on the seed, with language, or "none"]
**Brief copy:** [headline / description / primary text, or "no copy"]. **Advertiser:** [name as spelled]
**Direction asks for:** [any requested text elements, or "nothing text-specific"]

### Overlay Inventory
**Output A:** [every overlaid line, each tagged: seed / brief / advertiser / invented / generic CTA. Picture text listed separately and marked as picture. Seed elements dropped.]
**Output B:** [same]

### Special Case
[None | Neither has overlaid text | Only A/B has overlaid text (seed had / had no overlay copy)]

### Flaws
**Output A:** [each flaw with family and tier, or "none"]
**Output B:** [same]

### Scope Check
[One line confirming no picture, design, picture text, adherence, word count or zoom sharpness in the reasoning.]

### Answer
**[Output A — clearly fewer text flaws | Output A — slightly fewer text flaws | Similarly good/bad | Output B — slightly fewer text flaws | Output B — clearly fewer text flaws | No overlaid text to compare]**

If the item is unratable, replace this block with the reject reason and nothing else: **Reject: [Image did not load | Inappropriate content]**

### Feedback
[One or two sentences naming the deciding line, its place, its output and its reference.]
```

## Final Checklist

- [ ] Every image, including the seed, loaded, and the content is allowed.
- [ ] Seed text, brief copy fields and the advertiser name read before the outputs.
- [ ] Every piece of text sorted into overlay or picture. Picture text was not judged.
- [ ] Special cases checked: neither has overlay, one-sided (and whether the seed carried copy).
- [ ] Every word read at zoom, fine print and buttons included.
- [ ] Every overlaid line traced to the seed, the brief, the advertiser, or marked invented or generic CTA.
- [ ] Seed overlay elements checked for drops and changes on both sides.
- [ ] Language checked against the seed's text and the brief's copy, not the advertiser's name.
- [ ] Flaws tiered, then combined by count and weight. Clearly only for a clearly-tier gap.
- [ ] No picture, design, adherence, word count or zoom sharpness in the reasoning.
- [ ] No overlaid text to compare used only when both sides are empty.
- [ ] Feedback names the line, place, output and reference in one or two sentences.
- [ ] Feedback was given in the chat. No workspace file was modified.
