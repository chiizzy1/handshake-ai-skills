---
name: handshake-ads-text-style
description: Evaluate Handshake Ads Creative text style comparisons. Use when a task shows two finished ad images (Output A and Output B) and asks whose overlaid text and graphics are better designed (layout, placement, typography, colour), ignoring spelling and the picture behind them; when the buttons read clearly better style, slightly better style, similarly good/bad, or No overlaid text to compare; when the task says ads creative, Better Text Style, overlay, or Compare Two Ad Overlays.
---

# Handshake Ads Text Style

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, this SKILL.md is the operative rubric. Say that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `HANDSHAKE-AI/ads-creative/vs-1786693813-260813-ads-creative-i2i-q6-text-style.md`, the full guideline. It is the complete source material for this task: there is no separate cheat sheet or instruction PDF.
2. This SKILL.md, which compresses the guideline and adds what the example images show.
3. `references/worked-cases.md`, the four graded pairs with their images in `references/examples/`.

Before rating a live item, read `references/worked-cases.md` once per session.

This question measures one thing: **how well the overlay is designed.** The overlay is the text and graphics laid over the picture: headlines, captions, price badges, buttons, banners and logos. Nothing else is judged. Not the spelling, not the picture, not how much the overlay says.

This is not the six-axis R2I/I2I ELO task and not Pixel Aligned. There is no prompt, no seed, no brief and no instruction following. Do not import axes the UI does not show.

## Three Siblings, Three Scope Rules

This is the **Q6** question in the Ads Creative I2I set. The same finished ads are judged by sibling
questions with **conflicting scope rules**. Working one right after another is where mistakes happen.

| | Q6 Text Style (this skill) | Q4 Visual Appeal | Q0 Overall Suitability |
|---|---|---|---|
| Skill | `handshake-ads-text-style` | `handshake-ads-visual-appeal` | `handshake-ads-overall-suitability` |
| Judge | **Only the overlay's design** | Only the picture | The whole ad |
| Overlay | The whole question | Out of scope | In scope, usually decisive |
| Spelling / garbled text | **Out of scope. Costs nothing** | Out of scope | **Dealbreaker** |
| The picture | Out of scope, except as the surface under the overlay | The whole question | In scope |
| References shown | None | None | Seed, creative direction, ad brief |
| Buttons | Clearly/slightly better style, Similarly good/bad, **No overlaid text to compare** | Clearly/slightly more appealing, Similarly good/bad | Strongly/Slightly Prefer, Tie |
| Rejects | 2 reasons | 3 reasons, incl. mixed mediums | 2 reasons |

**The shared trap.** All three modules test a well-made ad with a misspelled headline, and the right
answers differ. On Q0 the typo can decide the item. On Q4 the overlay is ignored entirely. **Here the
overlay is judged, but the typo is not.** A beautifully set headline with a spelling error can win
clearly.

If the UI shows a seed and a brief, you are on Q0 or Q5. If the buttons say "more appealing", you are on Q4.
A fourth sibling, `handshake-ads-relevance`, compares one original ad with one generated ad, Pass or Fail.

**The closest sibling is Q5 Text Flaws** (`handshake-ads-text-flaws`). It has the same six-button layout,
including No overlaid text to compare, but its buttons say "fewer text flaws" and it shows the seed,
direction and brief. It is the mirror of this question: there, a misspelling, a garbled block, an invented
line or the wrong language decides the pair, and layout, placement, fonts and colour cost nothing. The
same pair can win clearly on one and tie on the other.

## Task Shape

- Two finished ad images side by side, **Output A** and **Output B**.
- One question: "Which image's overlaid text and graphics are better designed — layout, placement, typography, colour? Ignore spelling and ignore the picture behind them."
- Six buttons:
  - Output A — clearly better style
  - Output A — slightly better style
  - Similarly good/bad
  - Output B — slightly better style
  - Output B — clearly better style
  - No overlaid text to compare
- One feedback field. **Keep the note between 50 and 100 characters.** See How to Write the Feedback.
- Two reject buttons: "Image did not load" and "Inappropriate content".

## What Counts As Overlay

| It is overlay | It is picture (never judged) |
|---|---|
| Headlines, captions, subheads | A product label |
| Price badges, rating stars, review cards | Packaging copy, box print, a book or brochure cover in the scene |
| Buttons and calls to action | A street sign, a shop sign |
| Banners, bands, strips, ribbons | Print on a T-shirt or any garment |
| Logos and brand lockups placed on the image | Writing on a phone or laptop screen inside the photo |
| Icons, checklists and feature rows laid on top | The product's own printed name and graphics |

**Test:** mentally strip the photo away. Whatever would still be floating on a blank canvas is the
overlay. Whatever would go with the photo is picture.

**If in-scene words are the only text an image has, that image has no overlaid text.** Its lettering can be
garbled or mushy. That belongs to other tasks and changes nothing here.

A product box can carry a whole designed cover (headline, subtitle, icons). It is still picture. In the
course-ad case, most of Output A's words are on the box. Its overlay is only the headline and the pill
under it.

## The Four Lenses

Every reason you give must come from one of these.

- **Layout.** Balanced, or crowded and cluttered? Does one message lead the eye, or does nothing stand out? An awkward empty gap where something should be, or elements jammed against the edges?
- **Placement.** Does the text sit well on the image, or fight it? **Covering the subject's face or the product is the classic failure.** Labels and badges should line up with what they point at.
- **Typography.** Typefaces, sizes and weights well chosen and consistent? **Too many fonts is a failure.** So is wrongly grouped text: unrelated lines fused together, or related lines scattered.
- **Colour.** Enough contrast to read comfortably? Does the palette work with the picture? Banner colours that clash with the background or the product, or look random, fail.

## The Bar: Campaign-Ready

For each overlay ask: **could this run in a high-end marketing campaign, for a luxury brand, with little
or no adjustment?**

- Clears that bar: **campaign-ready**.
- **Design failure:** the overlay covers the subject or product, has no hierarchy (nothing stands out), clashes with its own picture, or uses far too many fonts.
- Between the two: aligned and readable but heavier-handed, less refined, or less integrated. This is where "slightly" lives.

## Out Of Scope

| Out of scope | Why it tempts you | What to do instead |
|---|---|---|
| **Spelling and correctness.** Misspellings, garbled letters, broken words, mushy characters | It is the loudest flaw in the frame. **The most common mistake on this task** | Judge how the text is set, not whether it is right |
| **The picture.** Product, people, scene, lighting, and their flaws | Two outputs with identical overlays still look different | Use the picture only as the surface: contrast against it, harmony with it, what the overlay covers |
| **Word count.** More text, more badges, louder effects | "Shows everything included" feels like value | More is not better design. Bare minimalism that reads unfinished is not better either. Ask whether it looks designed: intentional, organized, polished |
| **Pixel crispness.** Letterform sharpness at maximum zoom | Pairs often differ in resolution | Zoom to see alignment, spacing, grouping and consistency, not to compare sharpness |

## Mandatory Workflow

About a minute per item.

1. **Reject check.** Both images loaded, and the content is allowed. See Rejections.
2. **Find the overlays.** For each output, strip the photo away and list what is laid over it. Sort every piece of text into overlay or in-scene. Zoom if you need to see how the text is set.
3. **Check the special cases, in this order:**
   1. **Neither output has any overlay** (in-scene words do not count): answer **No overlaid text to compare**. This is the only time that button is right.
   2. **Only one output has an overlay:** judge that overlay alone. See The One-Sided Rule below. Never press the no-text button to escape it.
   3. **Same overlay in both**: same words, **same font, same size, same position, same treatment**. Answer **Similarly good/bad** and say the overlays are the same. Do not look to the photos for a winner. Same words set differently is **not** this case. Go to step 4.
4. **Run the four lenses on both overlays** and ask the campaign question of each.
5. **Name the edge.** Which lens, and where it shows. If you cannot name one, the answer is Similarly good/bad. **A difference you can see is not automatically an edge.** An ornament or a proportion change that neither helps nor hurts does not move the vote.
6. **Pick the severity** with the anchors below.
7. **Scope check before you commit.** Did spelling, the picture, word count or sharpness sneak into your reason? If so, remove it and re-decide.
8. **Write a 50 to 100 character note** naming the lens and the place, or saying the overlays are the same.

## Answer Anchors

| What you found | Your answer |
|---|---|
| One overlay is campaign-ready, the other has a design failure (covers the subject, no hierarchy, clashing colours, too many fonts) | **Clearly better style** for the clean one |
| Several design advantages that all point the same way | **Clearly better style** |
| One nameable design edge (cleaner alignment, calmer layout, better colour harmony), both otherwise comparable | **Slightly better style** |
| Both overlays weak, but one is meaningfully closer to usable | **Slightly better style** |
| The same overlay in both (same words, same font, same position) | **Similarly good/bad**, and say so in the note |
| Two designs with no difference you can name, both polished or both equally weak | **Similarly good/bad** |
| Neither output has any overlaid text or graphics | **No overlaid text to compare**, and only then |
| Only one output has an overlay | See The One-Sided Rule |

**Clearly versus slightly.** Clearly needs either a design failure on the losing side or several edges
stacked on the winning side. When the loser is aligned and readable, just heavier-handed or less
integrated, and the edge is one lens, it is **slightly**. The hotel case is the model: identical copy, B
integrates it into the photo, A walls it into solid bands. The answer is slightly, because A's bands are
not an outright failure.

**Same words is not same design.** The tie rule is for identical designs. If both outputs carry the same
copy but one sets it better (smarter placement, calmer treatment, stronger contrast), that is a real style
difference and it decides the vote.

## The One-Sided Rule

When only one output has an overlay, a text-free output has no design to judge. Judge the lone overlay
on its own merits against the campaign bar:

| The lone overlay is | Answer |
|---|---|
| Campaign-ready | **Clearly better style** for the output that has it. Stated in the footwear case |
| Broken (a design failure) | **Clearly better style** for the text-free output |
| Middling (neither campaign-ready nor failed) | **Similarly good/bad** |

The guideline states the severity only for the campaign-ready row ("the output that has it wins
clearly"). The broken row follows from the same sentence: "Had the lone overlay been a mess, the clean
output would have won **instead**", which mirrors that win. It also follows from card 4: a design failure
against a clean side is clearly.

Never answer No overlaid text to compare on a one-sided pair. That button needs **both** sides empty.

## Rejections

Reject only for these two reasons:

- **Image did not load.** An image fails to load and the panel shows a load error.
- **Inappropriate content.** Nudity or sexually explicit content, hate symbols or hate speech, graphic violence.

Never reject for an ugly, cluttered or amateurish overlay (the vote records that), for a pair with no
overlaid text (that is the sixth button), for people in swimwear or underwear, or for a hard or close
call. There is **no mixed-medium reject** on this question.

## Hard Gates

- Do not let a spelling error, garbled letter or broken word move the vote. Not even a little.
- Do not grade in-scene text (packaging, labels, signs, garments, screens) as overlay.
- Do not press No overlaid text to compare unless **both** outputs lack an overlay.
- Do not press No overlaid text to compare because two overlays match. That is Similarly good/bad.
- Do not tie on matching words when the designs differ.
- Do not break a same-overlay tie with the picture.
- Do not reward more information, more badges or louder effects.
- Do not reward bare minimalism that reads as unfinished.
- Do not decide on letterform sharpness at maximum zoom.
- Do not pick a side you cannot name a lens and a place for.
- Do not upgrade to clearly on one edge when the loser has no outright failure.
- Do not reject for an ugly overlay, a missing overlay, or a hard call.

## Calibration Cases

Four graded pairs from the guideline. Full versions, image notes and the exemplar feedback are in
`references/worked-cases.md`.

| The pair | Correct call | The trap |
|---|---|---|
| Course ad. A: one headline and one pill badge. B: feature rows, checklist, price flash, bonus strips, a dozen type styles | A — clearly | Rewarding B for "more information." Volume is what kills B's hierarchy |
| Hotel ad. Identical French copy and logo. A in two solid green bands. B set straight onto a quiet wall | B — slightly | Tying because the words match. Same words, different treatment |
| Salon ad. Identical review card, headline, subhead and button. Only the photo crop differs | Similarly good/bad | Pressing No overlaid text to compare because there is "nothing to compare" |
| Footwear ad. A's only words are printed on shoeboxes. B has a serif headline, caption and letter-spaced footer | B — clearly | Grading A's mushy box print as overlay and calling it even |

Two things stand out from the actual images:

- **The course ad's Output B is full of typos** ("greal results", "EARN MNEY", "CLIENT RIT"), and the exemplar feedback **never mentions them**. The call rests entirely on layout and typography. That is the scope rule working as intended.
- **The salon pair differs in crop and resolution**, and the call still ignores it. Those are picture and file properties.

## How to Write the Feedback

**Length: 50 to 100 characters.** Count before you submit. One sentence usually fits; two short ones
can. Anything over 100 gets cut, anything under 50 gets padded with a place or the other side.

**Name the lens and where it shows.** If the two overlays are the same, say so. The prompt asks for it.

The guideline's own exemplar notes run 92 to 218 characters. **Use them for what to say, not for
length.** The trimmed versions below carry the same reason inside the limit.

### Rules

- **50 to 100 characters, spaces and punctuation included.**
- **One element, one place, one lens.** The headline, the badge, the banner, the button, the logo. "Sits clear of the product", "covers half the product", "on the quiet wall".
- **Mention the loser only if it fits.** The winner's edge comes first. Add the loser's flaw when the characters allow.
- **Say the lens in plain words:** "nothing stands out", "a dozen type styles", "sinks into the sky", "looks pasted on".
- **No rubric vocabulary:** do not write "campaign-ready", "design failure", "lens" or "typographic consistency". Those are thinking words.
- **Never mention spelling**, the picture's quality, or how much the overlay says.
- **Short words beat long ones.** "A" and "B", not "Output A" and "Output B".
- **Semicolons are fine.** The guideline's own exemplar uses one. No em dashes.
- **No AI power words:** delve, meticulous, seamlessly, elevate, striking visual narrative.
- **Avoid absolutes:** not "perfect typography". Use "clean, consistent type".

### Good Examples

Each is the guideline's exemplar reason, trimmed to fit. Character counts in brackets.

```markdown
B's headline and badge sit clear of the product, while A's banner covers half of it.
```

(84) Placement, both sides.

```markdown
A is one headline and one badge with room to breathe. B stacks a dozen type styles.
```

(83) Layout and typography, course ad.

```markdown
Same lines, but B sets them on a quiet wall while A walls them into heavy green bands.
```

(86) Same words, different design, hotel ad.

```markdown
Same review card, headline and button in both, with the same fonts and spots. A tie.
```

(84) Same-overlay tie, salon ad.

```markdown
A's only words are printed on the shoeboxes. B's serif headline sits well in the space.
```

(87) One-sided pair, footwear ad.

```markdown
Neither has anything laid over the photo. The only words are on the bottle's label.
```

(83) No overlaid text to compare.

```markdown
Only A has an overlay, and its clashing banners sit right across the model's face.
```

(82) One-sided pair, broken overlay loses.

### Bad Examples

- ❌ "B looks more professional." Names no lens and no place, and is under 50.
- ❌ "A's headline is misspelled, so B wins." Wrong task. Spelling never decides this question.
- ❌ "B gives the buyer far more information and shows everything included in the offer." Information count is not a style lens.
- ❌ "The text is word-for-word the same in both, so the style is the same." Same words, different design is not a tie.
- ❌ "There is no difference between the overlays, so there is nothing to compare." With the no-text button, this throws away a real tie.
- ❌ "A's box lettering is a bit mushy but B's text is nicer, so roughly even overall." Grades packaging as overlay.
- ❌ "B's photo is warmer and suits the headline better." The picture is never the tie-breaker.
- ❌ The guideline's full course-ad note, pasted as is. Right reason, but at 218 characters it is over twice the limit.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present the evaluation in the chat using this template:

```markdown
### Overlay Inventory
**Output A:** [every overlay element, or "none". In-scene text listed separately and marked as picture.]
**Output B:** [same]

### Special Case
[None | Neither has an overlay | Only A/B has an overlay | Same overlay in both]

### Lenses
**Output A:** [layout, placement, typography, colour. Campaign-ready, middling, or design failure.]
**Output B:** [same]

### Scope Check
[One line confirming no spelling, picture, word count or sharpness in the reasoning.]

### Answer
**[Output A — clearly better style | Output A — slightly better style | Similarly good/bad | Output B — slightly better style | Output B — clearly better style | No overlaid text to compare]**

If the item is unratable, replace this block with the reject reason and nothing else: **Reject: [Image did not load | Inappropriate content]**

### Feedback
[50 to 100 characters following the tone rules.] ([count] chars)
```

## Final Checklist

- [ ] Both images loaded and the content is allowed.
- [ ] Every piece of text sorted into overlay or in-scene. In-scene text was not graded.
- [ ] Special cases checked in order: neither, one-sided, same overlay.
- [ ] No overlaid text to compare used only when both sides are empty.
- [ ] Same-overlay tie used only for the same design, not just the same words.
- [ ] Four lenses run on both overlays, campaign question asked of each.
- [ ] The winner's edge is named as a lens and a place.
- [ ] Clearly only with a design failure on the losing side or several stacked edges. One edge is slightly.
- [ ] No spelling, picture quality, word count or zoom sharpness in the reasoning or the note.
- [ ] Feedback is 50 to 100 characters and names the element and the place, or states the overlays are the same.
- [ ] Feedback was given in the chat. No workspace file was modified.
