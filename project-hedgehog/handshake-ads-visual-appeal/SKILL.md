---
name: handshake-ads-visual-appeal
description: Evaluate Handshake Ads Creative visual appeal comparisons. Use when a task shows two finished ad images (Output A and Output B) and asks which image's content is more striking and engaging to look at, ignore any overlaid text or graphics; when the buttons read clearly more appealing, slightly more appealing, or similarly good/bad; when the task says ads creative, visual appeal, or Compare Two Ad Images.
---

# Handshake Ads Visual Appeal

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use these as the source of truth, in this order:

1. `references/cheat-sheet.md` in this skill folder. This is the task's own cheat sheet, reproduced verbatim, and it is the most specific authority.
2. `HANDSHAKE-AI/ads-creative/vs-1786690831-260813-ads-creative-i2i-q4-visual-appeal.md`, the full guideline.

Before rating a live item, read `references/rubric.md` and `references/cheat-sheet.md`.

The routine the cheat sheet prescribes: first impression, a 10 to 15 second guard scan, your answer, then one or two specific sentences.

This question measures one thing only: **pull**. How strongly does each picture make you stop and look? It is subjective on purpose. Taste is expected and there is no single right answer, but you must look honestly and be able to name your reason.

This is not the six-axis R2I/I2I ELO task and not Pixel Aligned. There is no prompt to check, no reference image, and no instruction following. Do not import axes the UI does not show.

## Sibling Task, Opposite Scope

This is the **Q4** question in the Ads Creative I2I set. Its sibling `handshake-ads-overall-suitability`
(`project-hedgehog/handshake-ads-overall-suitability/SKILL.md`) is the **Q0** question, and the two have
**opposite scope rules**.

| | Q4 Visual Appeal (this skill) | Q0 Overall Suitability |
|---|---|---|
| Question | Which picture is more striking to look at? | More suitable as a high-end campaign ad? |
| Overlaid text | Explicitly out of scope | In scope, and usually decisive |
| References shown | None | Seed image, creative direction, ad brief |
| Buttons | Clearly/slightly more appealing, Similarly good/bad | Strongly/Slightly Prefer A, Tie, Slightly/Strongly Prefer B |

If the UI shows a seed image and an ad brief, and the buttons say "Strongly Prefer", you are in the
wrong skill.

**Third sibling.** The same Ads Creative outputs are also judged on **relevance**
(`handshake-ads-relevance`): one original ad against one generated ad, Pass or Fail, with failure reasons.
There, rendering defects are out of scope but any change to the product's body is a Fail.

**Text style sibling.** The same outputs are also judged on **overlay design** (`handshake-ads-text-style`,
Q6): only the text and graphics laid over the picture, on layout, placement, typography and colour.
There, spelling is out of scope and the picture is out of scope, and a sixth button covers pairs with no overlay.

**Text flaws sibling.** The same outputs are also judged on **overlay correctness** (`handshake-ads-text-flaws`,
Q5): seed, direction and brief shown, and only the overlaid text is judged, for rendering errors, lines not
grounded in the seed or brief, dropped seed text, and the wrong language. There, design and the picture are out of scope.

## Task Shape

- Two finished ad images side by side, **Output A** and **Output B**. Either one can be clicked to magnify.
- One question: "Which image's content is more striking and engaging to look at? Ignore any overlaid text or graphics."
- Five buttons:
  - Output A — clearly more appealing
  - Output A — slightly more appealing
  - Similarly good/bad
  - Output B — slightly more appealing
  - Output B — clearly more appealing
- One required feedback field: "In a sentence or two, say what made the winner more appealing — or why they're equally strong."

## What Pull Is Made Of

Pull comes from things you can point at. When you pick a winner, your reason has to be one of these.

- **Focal point:** one place the eye lands first, framed on purpose.
- **Composition and hierarchy:** a balanced arrangement that leads the eye through the picture instead of scattering it.
- **Light and exposure:** sharp focus and correct exposure where it matters, and light that gives the subject shape rather than flattening it.
- **Color:** a palette that works together and supports the subject.
- **Natural posing and proportions:** people and objects that sit convincingly in the scene.
- **Cohesion:** the elements read as one picture, not as parts assembled together.

## Appeal-Killers

The opposites of pull. Your guard scan looks for these **after** your first impression, never before it.

- Muddy or flat light. Washed-out or fighting colors.
- Clutter. Competing elements with nowhere for the eye to land.
- Dead, static staging where the subject deserved drama.
- An artificial, implausible look that breaks the scene.
- A defect in the focal area that is visible at normal size.

Give the guard scan 10 to 15 seconds. It is a check on your first impression, not a replacement for it.

## What This Question Does Not Measure

Getting this wrong is the most common failure on this task. Each of these belongs to a different rating task.

- **Flaw count.** A rendering defect matters here only when it visibly hurts the look at normal viewing size, such as a distracting artifact in the focal area. A slightly flawed image can still be the more arresting picture.
- **Realism.** "Looks AI-generated" is a different task. A clean, convincingly photographic image can still be flat and dull, and a stylized or non-photoreal image can win on appeal when both outputs share that medium. A style choice (black-and-white, tinted, an illustration look) is not a defect here.
- **Ad effectiveness.** Whether the image would sell the product is another task's question. A gorgeous picture that barely features the product can still win here.
- **The overlay.** Text and graphics laid over the picture are out of scope, including how good they look. Judge the picture behind them. A spelling error in a headline does not change your answer. If both images are essentially words on a background, judge the background canvas.
- **Your taste in styles and products.** You may find the product, the category, the color temperature, or the whole style tacky. Loud maximalism is not worse than quiet minimalism, and restraint is not objectively more appealing than energy. A style you dislike, executed with control, beats a style you like with dead staging. Judge how much pull this execution has, not whether you would buy it.
- **Pixel-peeping.** Sharpness you can only see at maximum zoom is a file property, not an edge. It does not decide this question.

## Mandatory Workflow

The whole routine takes about half a minute per item.

1. **Reject check.** Confirm the item is ratable at all. See Rejections below. If it is, keep going.
2. **First impression at full size.** Look at Output A and Output B and ask which one would stop your scroll. **Your first impression is the main instrument on this question. Do not treat it as a bias to suppress.** Most calls get made here.
3. **Guard scan, 10 to 15 seconds.** Two checks, in this order:
   - **Is the pull out of scope?** Is what grabbed you actually a slick headline or badge in the overlay, or just liking the product itself? If so, it is not your reason.
   - **Did you miss an appeal-killer?** Glance across both pictures for muddy light, clutter, dead staging, an artificial look, or a defect in the focal area.
4. **If the scan found nothing, go with your first impression.** Do not talk yourself out of a real read.
5. **Name the edge.** Point at which pull source explains the call. If you pick a side, your feedback must name that edge. If you cannot name one, your answer is Similarly good/bad.
6. **Pick the severity** using the anchors below.
7. **Write one or two specific sentences** naming what created or killed the pull.

**Zoom in to check details, not to find an edge.** These pairs often differ in file resolution, so one side may look sharper at maximum zoom. That is a file property, not an appeal edge. Use zoom to identify what a suspected defect or detail is, then judge it at normal viewing size. If you need 200 percent zoom to justify a preference, the answer is Similarly good/bad.

## The Five-Button Scale

Pick the row that matches what you found.

| What you found | Your answer |
|---|---|
| You would stop scrolling for one and pass the other without a glance | Clearly more appealing |
| Several advantages line up on one side (light, color, and composition all better) | Clearly more appealing |
| Both hold the eye, and one has a single aesthetic edge you can name | Slightly more appealing |
| Both are weak, but one is noticeably less flat | Slightly more appealing |
| Equally striking or equally flat, with no edge you can name | Similarly good/bad |

If you pick a side, your feedback must name the edge. If you cannot name one, your answer is Similarly
good/bad. Do not force a winner between two equally flat images, and do not call a tie on a real edge
because the pair felt close.

Note that two weak images are not automatically a tie. Both weak with one noticeably less flat is a
slight win.

## Text-Only Pairs

When both images are essentially just words on a background, judge the canvas behind the words. Its color, texture, and energy are the picture. The words themselves, and how good they look, stay out of scope.

## Rejections

Reject only for these three reasons:

- **Image did not load.** An image fails to load and the panel shows a load error.
- **Inappropriate content.** Nudity or sexually explicit poses, hate symbols or hate speech, or graphic violence.
- **Outputs are different mediums (photorealistic vs illustration).** One output is photographic and the other is a flat illustration or graphic. Those two cannot be fairly compared on appeal. Two illustrations are the same medium, so compare them normally. A black-and-white or tinted photo is still a photo.

Never reject for an ugly, flawed, or boring image. That is what your vote records. Never reject for
people in swimwear or underwear, for content that is merely suggestive, or because the decision is close
or difficult.

## Hard Gates

- Do not rate before forming a first impression at normal viewing size.
- Do not justify a win with defect count, AI-look, ad effectiveness, or the overlaid text.
- Do not treat a style choice as a flaw.
- Do not treat "shows the product better" as pull.
- Do not pick a winner you cannot name a pull reason for.
- Do not upgrade to clearly on one small nameable edge.
- Do not use Similarly good/bad to avoid a hard call. Style differences never "cancel out" on their own.
- Do not turn a style preference into a rule. Judge the execution, not the school of design.
- Do not tie because both images show the same subject. Same subject with different staging is a real gap.
- Do not count decoration as pull. A busier background behind the same flat subject is not an edge.
- Do not break a tie on color mood alone. Cold versus warm is a style choice, not an execution gap.
- Do not decide the answer on sharpness that is only visible at maximum zoom.
- Do not reject an item for being ugly, boring, or hard.

## Calibration Cases

Four worked pairs from the guideline, compressed. Full versions with the exemplar feedback are in
`references/rubric.md`.

| The pair | Correct call | The trap |
|---|---|---|
| Same three products. A stages one hero tube with the others defocused under a light ray. B lines all three up flat. | A — clearly | Tying because both show the same objects. Staging alone can be a full anchor apart. |
| A machine tool. A is a cluttered workbench carrying feature callouts. B is a dark studio hero shot. | B — clearly | Rewarding A because the callouts make it "feel like a finished ad." That is the overlay plus ad effectiveness. |
| The same coffee boxes in two splash shots, one icy and one warm. Equal craft. | Similarly good/bad | Picking the warm one because coffee should feel warm. Palette taste plus ad effectiveness. |
| Two flat talking-head frames. A has a patterned backdrop, B a plain gradient. | Similarly good/bad | Giving A a slight win for "visual interest." Decoration is not pull. |

The last row and the anchor row "both weak, but one is noticeably less flat" are not in conflict. Less
flat means the picture does more with light, staging, depth, or a focal idea. A busier background is not
less flat.

Two things stand out from the actual images behind these cases. **Three of the four pairs have an
overlay on at least one side**, so the guard scan's out-of-scope check earns its place on nearly every
item. And **the exemplar feedback never mentions an overlay or a text defect**, even where one is the
loudest thing in the frame. Notice it, then leave it out of the note.

## How to See

For photographic analysis fundamentals (composition and framing, focus and clarity, light and color), read `../../shared-references/how-to-see.md`.

## How to Write the Feedback

One or two sentences. Name the pull, say where it is in the picture, and say why it decided you.

The form has a minimum length, but what reviewers check is specificity. **Vague feedback on a correct
answer still fails review.**

For a tie, describe what both images do well or both do badly. A tie note has to be as specific as a
win note.

### Rules

- **Persona:** an average person who has an eye for pictures, not an art critic and not a rubric reciter.
- **Length:** one or two sentences. The field asks for that and nothing more.
- **Name the reason:** light, the focal point, color, clutter, staging, posing. Say it in plain words.
- **No rubric vocabulary:** do not write "focal hierarchy," "compositional balance," "visual pull," "cohesion," or "appeal-killers." Those are your thinking words, not your writing words.
- **No out-of-scope reasons:** never say one image looks more real, has fewer artifacts, or shows the product better.
- **No em dashes or semicolons.** Use periods.
- **No AI power words:** delve, tapestry, meticulous, striking visual narrative.
- **Avoid absolutes:** not "perfect lighting." Use "the light is much better."
- **Use "while" instead of "whereas"** when contrasting.

### Good Examples

```markdown
Output B is clearly more appealing. The light on the bottle gives it shape and the dark background makes it pop, while Output A is lit flat from the front so everything sits on the same plane.
```

```markdown
Output A is slightly more appealing. Both look good, but the model's pose in A is more natural and relaxed. B is a little stiff.
```

```markdown
Both are crisp studio shots with balanced palettes and clear focal points, so they are equally strong.
```

```markdown
Both are flat, evenly lit webcam-style frames of the same speaker, with no staging, no mood, and no focal idea in either. Output A's patterned backdrop is decoration and does not add pull.
```

```markdown
Output A stages one hero tube up front with the other two softly defocused behind it, under a visible light ray, so the eye lands in one place. Output B lines all three up flat and equally sharp, so nothing leads.
```

```markdown
Output B's low golden light and the diagonal of the road give it depth. Output A is evenly lit and flat.
```

```markdown
Output B is clearly more appealing. Your eye lands right on the burger and stays there, while Output A crams four things into the frame with nowhere to rest.
```

### Bad Examples

- *Bad (out of scope):* "Output A is more appealing because Output B has warped fingers and looks AI-generated." That is the defects task and the realism task.
- *Bad (out of scope):* "Output B is better because you can actually read the brand name and see the product clearly." That is ad effectiveness and the overlay.
- *Bad (rubric voice):* "Output A demonstrates superior compositional hierarchy and a clearly defined focal point with cohesive color grading." Say what you see instead.
- *Bad (no reason):* "Output B just looks better and grabs my attention more." Name what does the grabbing.
- *Bad (taste, not pull):* "Output A is nicer because I would never buy a product packaged like that." Your taste in the product is out of scope.
- *Bad (palette taste):* "Output A, because I love this shade of blue." Your palette taste is not an edge.
- *Bad (vague tie):* "They are both about the same." Name what both do well or both do badly.

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present the evaluation in the chat using this template:

```markdown
### First Impression
[Which one stopped you, before any analysis.]

### Output A
[What pulls and what kills the pull. Plain words.]

### Output B
[What pulls and what kills the pull. Plain words.]

### Scope Check
[One line confirming the reason is not defect count, realism, ad effectiveness, overlay, or product taste.]

### Answer
**[Output A — clearly more appealing | Output A — slightly more appealing | Similarly good/bad | Output B — slightly more appealing | Output B — clearly more appealing]**

If the item is unratable, replace this block with the reject reason and nothing else: **Reject: [Image did not load | Inappropriate content | Outputs are different mediums (photorealistic vs illustration)]**

### Feedback
[One or two sentences following the tone rules.]
```

## Final Checklist

- [ ] Reject check done. Both images loaded, content is allowed, and both share a medium.
- [ ] First impression formed at full size and treated as the main instrument, not overridden without cause.
- [ ] The winner's edge is named as one of the six pull sources.
- [ ] Guard scan ran both checks: is the pull out of scope, and did I miss an appeal-killer.
- [ ] No defect count, realism, ad effectiveness, overlay, or product taste in the reasoning.
- [ ] No answer resting on sharpness that only shows at maximum zoom. Nothing needed 200 percent zoom to justify.
- [ ] Not a reflex tie on same-subject pairs, matching palettes, or background decoration.
- [ ] Severity matches the scale. Several advantages on one side is clearly. One nameable edge is slightly.
- [ ] Feedback names the pull, says where it is in the picture, and is one or two sentences with no em dashes and no rubric words. A tie note is as specific as a win note.
- [ ] Feedback was given in the chat. No workspace file was modified.
