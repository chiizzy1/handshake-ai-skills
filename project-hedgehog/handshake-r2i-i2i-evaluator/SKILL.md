---
name: handshake-r2i-i2i-evaluator
description: Evaluate Handshake Reference-to-Image, Image-to-Image, and Omni R2I ELO tasks. Use when a task has reference/input image(s), an edit or transformation prompt, and two generated responses to rate across Overall, Instruction Following, Person ID Preservation, Content/Reference Preservation, Visual Quality, and Absence of AI Artifacts.
---

# Handshake R2I/I2I Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `../../shared-references/...` is a sibling folder inside this skills repo.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use the Handshake R2I/I2I PDFs as the source of truth:

- `HANDSHAKE-AI/pdfs/Handshake-ai-Omni-R2-ELO.pdf`
- `HANDSHAKE-AI/pdfs/handshake-Image-to-Image (I2I).pdf`
- `HANDSHAKE-AI/pdfs/handshake-Omni R2I Elo — Examples.pdf`
- the image evaluation foundation PDFs in `HANDSHAKE-AI/pdfs/`

If the task is i2i Pixel Aligned / Project Hedgehog and asks Q1 instructions aligned, Q2 pixel aligned, or Q3 no AI slop, stop and use `handshake-i2i-pixel-aligned` (read `../handshake-i2i-pixel-aligned/SKILL.md`) instead. Pixel Aligned is a strict Yes/No task type, not a six-axis ELO comparison.

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Read the prompt and identify the requested change.
2. Study every reference/input image. Ask what must carry over.
3. Separate targeted changes from untargeted content.
4. Zoom into both outputs: faces, hands, text, accessories, background, material edges, and edited regions.
5. **RUN THE CONSTRAINT CHECKLIST (see below) BEFORE writing any comment.**
6. Score the six dimensions independently.
7. Use ties only when truly indistinguishable.
8. Give concise image-grounded justifications.

## When To Run The Interactive Protocol

- **Reference image and prompt arrive without the responses:** run Phase 1, then stop and wait for Response A and Response B. Run the constraint checklist when they arrive, then produce Phase 2.
- **Everything arrives at once (reference, prompt, and both responses):** skip the wait. Run the constraint checklist, then produce Phase 2 directly.

### Phase 1: Reference & Prompt Analysis

Format it exactly like this:

```markdown
**Reference Image:** [Clear description of what the reference image shows — subjects, setting, composition, key details]

**Prompt constraints:**
1. [Constraint 1]
2. [Constraint 2]
3. [Constraint 3]
...

**Must carry over:** [List of untargeted content that should be preserved from the reference — layout, background, objects, people, colors, etc.]
```

Then wait for the user to provide Response A and Response B.

### Mandatory Pre-Write Constraint Checklist

After both responses are available, complete this checklist and present it before writing the comment. Do not skip it and do not rush to the comment.

1. **List every single constraint** from the prompt (targeted changes AND reference preservation).
2. **For each constraint, check Response A:** Did it pass or fail? Write it down.
3. **For each constraint, check Response B:** Did it pass or fail? Write it down.
4. **Check for AI artifacts in BOTH images:** Hands, fingers, faces, text, anatomy, extra limbs, warped objects.
5. **Only after completing steps 1-4**, write the evaluation.

## Hard Gates

- Do not judge outputs before studying the reference image.
- Do not treat the requested edit as reference-preservation failure.
- Do not excuse unrequested changes to people, layout, objects, logos, text, or background.
- Do not use clothing alone as Person ID unless the task says clothing is identity-defining.
- Do not pick the prettier output for Overall when it misses the central edit.
- Do not tie an axis when one response visibly preserves more required reference detail.

## Six Dimensions

- Overall Preference: which output best captures the user's intent.
- Instruction Following: which output did what the prompt requested.
- Person ID Preservation: whether reference people remain recognizable. ID rides mainly on face and identity-bearing features, not clothing or pose.
- Content / Reference Preservation: whether untargeted content, layout, background, objects, accessories, colors, and fine reference details stayed accurate.
- Visual Quality: craft quality, clarity, exposure, saturation, framing, focus, and seamless edits.
- Absence of AI Artifacts: waxy skin, wrong fingers, impossible light, bad anatomy, garbled text, unnatural materials, and generation tells.

Use the exact axis labels shown by the task UI. If the UI shows an axis not listed here, rate it on the same preference scale and name it as the UI names it.

## Overall Preference Eval Task Cues

When selecting the Overall Preference, strictly follow these three hard cues:

1. **Look it up if you don't know:** When a prompt involves specialized knowledge (technical, historical, scientific, cultural, anatomical alignment), verify with your web-search tool instead of guessing. Do not assume visual plausibility equals correctness.
2. **Watch out for the overly-AI look in the edit:** Things like unnaturally crisp edges, flat lighting, plasticky textures, or over-saturated colors in the edited area are common giveaways. An edit can look impressive at first glance but feel artificial on a closer look — don't let that initial wow factor automatically win.
3. **Watch out for text issues:** AI edits often add text where it doesn't belong or keep it sharp when it should be soft (far away, off-angle, or out of focus). Cluttered or unnaturally crisp text shouldn't win on visual impact alone.

## Important Separations

- Clothing and pose are not Person ID unless the prompt or task specifically makes them identity-defining.
- Unrequested camera/framing shifts usually affect Reference Preservation.
- Accessories, logos, and background details belong to Content / Reference Preservation.
- Over-saturation belongs mostly to Visual Quality and may also signal AI Artifacts if it gives a filter-applied look.
- A correct instruction-following win is not canceled out by a small artifact in the other response.

## Phase 2: Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present the full evaluation and Open Feedback in the chat, formatted exactly like this:

```markdown
- Overall Preference: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]
- Instruction Following: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]
- Person ID Preservation: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B | N/A]
- Content / Reference Preservation: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]
- Visual Quality: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]
- Absence of AI Artifacts: [Strongly Prefer A | Slightly Prefer A | Tie | Slightly Prefer B | Strongly Prefer B]

Open Feedback: [Natural, casual paragraph following the Hard Comment Rules below]
```

If the UI shows fewer axes (some tasks ask only for Overall), give only the axes the UI asks for.

### Open Feedback Examples

Natural, non-robotic:

```markdown
Open Feedback: Response B is better because it follows the prompt's instruction and reposed the image into a warrior II yoga pose in a natural way with the gaze over the front hand, while Response A feels unnatural because the gaze is over the back hand.
```

Casual and simple, like a real person reviewing a bad edit:

```markdown
Open Feedback: Response B is better because it cleanly removes the AC unit and fully reconstructs the brick wall and mortar lines to the image boundary, while Response A doesn't look natural and looks like a bad edit in Photoshop.
```

Simple contrast without over-engineering:

```markdown
Open Feedback: Response B does a better job of capturing the snowy December feel by transforming the foreground tree into bare winter branches, while Response A leaves a full canopy of leaves on the tree, making it look more like a freak autumn snowstorm.
```

> **Copywriting Rule:** When writing Open Feedback: purge AI power words (delve, tapestry, meticulous); use no em dashes or semicolons, just periods; keep phrasing simple, concrete, and human rather than reciting a rubric.

### Hard Comment Rules

**The Persona: The Average Everyday Person**
You are NOT a professional AI image evaluator, a prompt engineer, or an art critic. You are an average person scrolling through photos on your phone.

- **Do NOT talk about:** "executing constraints," "architectural crispness," "lighting effects," "reference preservation," or "instruction following."
- **DO talk about:** What looks good, what looks weird, what's missing, what looks like a bad Photoshop edit.

1. **Keep it simple. Break it up.** Do NOT force everything into a single, rigid run-on sentence. Break your thoughts into short, casual sentences. Real people don't talk in perfect parallel contrast structures.
2. **Use everyday language.** Describe things simply. (e.g., instead of "fails the reference preservation constraint by melting the structural details," say "the bottom part looks melted").
3. **No conversational filler.** Do not use subservient filler phrases like "just like you asked," "as requested," or "as instructed." Just state what the image shows.
4. **No snark, no emotion, no color commentary.** Do not use exaggerated words like "hilariously bad," "creepy," "horrific," or "disaster." Just state the simple visual fact neutrally.
5. **No em dashes or semicolons.** Do not use em dashes (—) or semicolons (;) to string thoughts together. Use periods. Average people writing quick feedback don't use literary punctuation.
6. **Avoid absolute words.** Never say a model did something "perfectly" or "flawlessly." If a user zooms in and finds a minor flaw, your comment becomes a factual error. Use safer words like "cleanly," "nicely," or "does a good job."
7. **Use "while" instead of "whereas".** "Whereas" sounds formal and academic. "While" sounds casual and relaxed. Always prefer "while" for contrasting.
8. **Never rewrite the user's words.** If the user gives you the exact phrasing for the comment, use it VERBATIM. Only fix obvious typos. Do not paraphrase, "polish," or restructure it.
9. **Banned phrases:** "; note that", "suffers from", "fails the constraint", "structural perspective", "reference preservation constraint", "inpainting constraint", "garbled", "gibberish", "hallucinated". These scream AI or sound too colorful.
10. **Good casual alternatives:** "does a bad job", "doesn't look natural", "looks like a bad Photoshop edit", "completely misses", "looks weird", "fake text", "random letters", "unreadable text".

### Anchoring to the Prompt (Before & After)

**Rule:** Always extract the *exact specific constraint* from the prompt (e.g., "flat colors," "same red font") and base your one-sentence justification entirely around whether that specific constraint was met. Do not overcomplicate or invent generic AI reasons if the prompt gives you the exact vocabulary to use.

**❌ BAD (Robotic, overcomplicating, missing the core constraint):**

```markdown
- Overall Preference: Strongly Prefer A

Open Feedback: Response A is much better because it follows the instruction perfectly. It updates the year to "2025" while keeping the exact distressed brush texture of the original design. Response B fails the style constraint. It replaces the entire text block with a smooth, perfectly uniform digital font, losing the gritty hand-painted feel of the reference image.
```

**✅ GOOD (Natural, one sentence, anchored directly to the prompt's words):**

```markdown
- Overall Preference: Strongly Prefer A

Open Feedback: Response A is better because it follows the prompt's instruction and updates the text to 2025 while keeping the exact same font style and color, while Response B changed the font weight and shifted the color away from the original.
```

### Flawed Attempt vs. Clean Failure (The "Ugly Win" Rule)

**Rule:** A flawed or unnatural attempt at the core instruction usually beats a response that completely ignores the instruction (even if the ignored one looks "prettier"). You are strictly forbidden from rating a Tie just because both have flaws.

**Magnitude Constraint:** If a model wins via an "Ugly Win" (i.e., it successfully followed the core instruction but introduced severe artifacts or looks unnatural), the overall preference must be downgraded to **Slightly Prefer**. Save **Strongly Prefer** exclusively for models that execute the instruction cleanly without major artifacts.

**✅ Example (Falling Cake Task):**
*Prompt: "Add a cake topper of the groom and bride on the wedding cake." (Reference shows a cake falling sideways).*
*Response A: Added the topper, but it is stuck sideways on the bottom tier defying gravity (flawed attempt).*
*Response B: Did not add a topper at all (clean failure).*

```markdown
- Overall Preference: Slightly Prefer A

Open Feedback: Response A is better because it follows the instruction to add the cake topper (even though the placement is physically unnatural), while Response B completely fails to add the requested topper.
```

### Both Failed the Instruction

**Rule:** When both responses fail the core instruction, use this exact natural flow to start the comment, explaining the shared failure first, then explaining why one is slightly better (usually due to Reference Preservation).

**✅ Example:**

```markdown
- Overall Preference: Slightly Prefer B

Open Feedback: Both responses failed to remove the overlay to expose a continuous page and instead just replaced it with new boxed contents, but Response B is slightly better because it perfectly preserves the original top half of the webpage, while Response A completely regenerates the header.
```

### The Visual Audit (Check for Artifacts Even When Winning)

**Rule:** Even if one response is the obvious winner on Instruction Following, conduct a full visual audit of both images for AI artifacts. When a response wins but has artifacts, frame the comment as a single sentence using a "because -> despite -> contrast" structure.

**✅ Example (Leaning Tower of Pancakes Task):**
*Prompt: "Same leaning tower composition, but it is a stack of pancakes instead of a building, slightly tilted the same direction and angle."*
*Response A: Tilted the pancakes correctly. Leaves background people floating in the sky.*
*Response B: Failed the tilt (stood straight up). Also leaves background people floating in the sky.*

```markdown
- Overall Preference: Slightly Prefer A

Open Feedback: Response A is better because it follows the instruction to tilt the pancake stack at the requested angle, despite having severe AI artifacts like the people in the background floating in the sky, while Response B fails the instruction by making the stack stand perfectly straight.
```

### The Double-Whammy (Instruction Failure + Artifacts)

**Rule:** When one response completely fails the instruction AND introduces severe visual artifacts (like warped anatomy or distorted eyes), use a "double-whammy" comment structure. State the instruction failure first, and cap the sentence off by pointing out the severe artifact last.

**✅ Example (Pixar Style Task):**
*Prompt: "Restyle this wedding photograph into Pixar-style 3D animation with large expressive eyes and smooth skin."*
*Response B: Successfully applied 3D style and expressive eyes.*
*Response A: Failed to apply 3D style (looks like a photo) AND distorted the couple's eyes.*

```markdown
- Overall Preference: Strongly Prefer B

Open Feedback: Response B is better because it follows the instruction to restyle the photograph into a Pixar-style 3D animation with large expressive eyes and smooth skin textures, while Response A fails to apply the requested style and still looks like a real photograph but with distorted eyes.
```

## Common Misses To Check For

These are the recurring failure modes in this task type. Check each one before writing.

1. **The obvious failure hidden behind complex detail.** A blue Beetle task asked to remove a door sticker and add a '53' decal; the reflections on the decal drew all the attention while one response left a large blurry smudge where the sticker had been. Look for fundamental failures before analyzing lighting or reflections.
2. **Rewriting the user's supplied text.** When the user provides exact comment phrasing, use it word-for-word. Do not "polish" it into something professional-sounding.
3. **The robotic grocery list.** "Response A is better because it perfectly applies the warm key light, dramatic side lighting, and subtle blue backlight while preserving the crisp details..." lists every constraint like a checklist. Better: "Response A is better because the lighting looks great and you can still see the building clearly, while Response B puts these weird window blind shadows all over it and the bottom part looks melted."
4. **Assuming the primary instruction was followed.** A prompt asked to make a blue car the foreground focal point and one response left a black car blocking it. Verify the core request against the reference image every time.
5. **Overcorrecting into snark.** Avoiding robotic tone can swing too far into "hilariously bad" or "creepy floating severed hands." Make a neutral observation instead: "Response B is better because everything is set up correctly, while Response A puts the typewriter on the desk backwards."
6. **Absolute words that risk factual errors.** "Perfectly applies the lighting" becomes wrong the moment a viewer finds a microscopic flaw. Use "cleanly applies the lighting."
7. **Conversational filler.** Drop "just like you asked." Just state what the image does.
8. **Em dashes and semicolons.** "the lighting makes sense—you can see the beam" should be "the lighting makes sense. You can see the beam."

## How to See

For photographic analysis fundamentals (composition, focus, lighting), read `../../shared-references/how-to-see.md`.

## Final Checklist

- Prompt change identified.
- Reference carry-over identified.
- Targeted vs untargeted changes separated.
- Every constraint checked against both responses before writing.
- Faces checked for ID.
- Accessories/background checked for reference preservation.
- AI artifacts checked separately from visual quality.
- No cross-axis trade-off was used.
- Comment sounds like an average person, uses the prompt's exact object words, and avoids the banned phrases.
- Feedback was given in the chat. No workspace file was modified.
