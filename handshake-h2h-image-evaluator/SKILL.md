---
name: handshake-h2h-image-evaluator
description: Evaluate Handshake H2H, Text-to-Image, and T2I Magnifier Pairwise image comparison tasks. Use when Codex must compare two AI-generated images from the same text prompt across Overall Preference, Instruction Following, Visual Quality, and Absence of AI Artifacts; when task UI says H2H, T2I, text-to-image-compare, t2i-magnifier-pairwise, magnifier pairwise, or asks which image better follows a prompt.
---

# Handshake H2H Image Evaluator

## Core Rule

**NEVER BE AGREEABLE FOR ITS OWN SAKE.** Always verify things independently. Do not rely blindly on user claims or assumptions, as the user might be wrong or missing information. If a task requires factual knowledge (like physics, anatomy, or astronomy), browse the web or use external tools to verify the ground truth before evaluating.

Use the H2H/T2I Handshake PDFs and task-specific markdown guidelines as the source of truth:

- `HANDSHAKE-AI/pdfs/handshae-ai-Image Evaluation.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-HOW-TO-SEE.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Realism & Artifacts.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-Text-to-Image (T2I).pdf`
- `HANDSHAKE-AI/pdfs/t2i-magnifier-pairwise/guidelines.md`

Before rating a live task, read `references/rubric.md`.

---

## Step-by-Step Evaluation Process

Follow these steps in this exact order. Do NOT skip any step. Do NOT start writing your evaluation until you have completed Steps 1 through 6.

### Step 1: Read the Prompt First

Read the full prompt before looking at either image. Write down in plain English what the prompt is asking for. Break it into pieces:
- What is the subject?
- How many things should there be?
- What style is requested?
- Is there specific text that needs to appear?
- Are there specific colors, positions, or relationships described?
- What is the overall mood or aesthetic?

### Step 2: Look at Both Images Side by Side

Look at both images carefully. Do NOT start writing yet. Just look. Compare them visually. Ask yourself:
- Do they look similar or very different?
- Does anything immediately jump out as wrong in either one?
- Which one feels more like what the prompt asked for?

### Step 3: Check the Big Stuff First (Macro Reality Check)

Before zooming into small details like text or textures, check the overall scene first. Do not let impressive details distract you from fundamentally broken logic.

Ask yourself these questions about each image:
- **Does the scene make physical sense?** Are objects floating? Are people in impossible positions? Do body parts connect properly?
- **Are there extra or missing limbs?** Look at the entire body before the face. Check for phantom arms, extra fingers, or melted hands.
- **Does the environment obey physics?** Do shadows fall in the right direction? Does lighting make sense?

If an image fails this basic reality check, it must be penalized heavily, even if the small details look amazing.

### Step 4: Check Consistency

This matters a lot for comics, multi-panel illustrations, and any image with repeated characters or objects.
- **Skin tone:** Does the same character keep the exact same skin color across every panel? (e.g., A tan character suddenly having a pale white hand in one panel is a massive fail.)
- **Hair and face:** Does the character look like the same person in every panel?
- **Clothing and props:** Do outfits and objects stay the same color and shape?
- **Pose and expression:** In multi-panel images (like stages of grief), do the poses actually change to match the content? If a character has the exact same pose copy-pasted across every panel, that's lazy and bad.

### Step 5: Check the Style

Does the image match the *requested* style? This is about what the prompt asked for, NOT your personal preference.
- If the prompt asks for "pixel art," check that it's actual pixel art (hard-edged blocks on a grid), not a smooth drawing with a mosaic filter.
- If the prompt asks for "hand-painted," don't penalize legitimate hand-painting techniques (like 3D block lettering) just because you personally prefer flat paint.
- If the prompt asks for "photograph," it should look like a real photo, not a digital painting.
- If the prompt asks for "illustration," it should look illustrated, not photorealistic.

**Do NOT let your personal style preferences influence the rating.** Only judge based on what the prompt actually requested.

### Step 6: Rate Each Axis

Now that you've looked carefully, rate each axis independently:
- **Instruction Following:** Did the image do what the prompt asked? Count objects, check text spelling, verify relationships.
- **Visual Quality:** How good does it look as a piece of art? Composition, color, detail, sharpness.
- **Absence of AI Artifacts:** Are there weird AI mistakes like melted hands, garbled text, extra limbs, or broken physics?
- **Overall Preference:** Combining everything above, which image is better?

Do NOT double-penalize. If something is an AI artifact, put it under Absence of AI Artifacts, not Visual Quality (unless it also ruins the overall look).

### Step 7: Write Your Evaluation

Now you can write. Follow the output format below and use the tone rules below. Read the tone examples before writing anything.

---

## Preference Severity

- **Strongly Prefer:** The winner actually succeeds at the core prompt and the loser clearly fails, OR the quality gap is so big that the loser is basically unusable.
- **Slightly Prefer:** Both images share the same fundamental issue but one handles the rest better. Or one is just a little cleaner than the other.
- **Tie:** Both images are genuinely equal on that axis. Avoid ties unless truly justified.

## Axis Separation

- Instruction Following = prompt compliance only.
- Visual Quality = craft, composition, detail, color, exposure, framing, seamlessness.
- Absence of AI Artifacts = AI tells like bad anatomy, waxy skin, garbled text, impossible lighting, distorted objects, broken logic.
- Overall Preference = holistic, based on what the user wanted. Instruction following usually matters more than small visual polish gaps.

---

## How to See (Photographic Analysis)

Good image evaluation starts with consistent observation, not personal taste. Replace vague statements like "looks good" or "feels off" with specific, observable claims.

### 1. Composition & Framing
- **Subject Placement & Rule of Thirds:** Placing a subject on a grid intersection creates tension and directs the eye naturally. A subject sitting dead center with empty space on both sides often reads as accidental.
- **Framing Scale:** Does the shot distance (wide, medium, close-up) match what the prompt asked for?
- **Visual Hierarchy:** What draws your eye first? Does it match the intended focus?
- **Negative Space:** Is the area around the subject providing intentional breathing room, or is it distractingly empty?

### 2. Focus, Detail & Clarity
Blur is NOT inherently a flaw. Shallow depth of field is a legitimate photographic choice.
- **Natural Fall-off vs. AI Artifacts:** Does the blur fall off smoothly and logically from the focal plane? Or does it dissolve into random, impossible patches?
- **Sharpness:** Is the intended subject actually in focus? Check edges and fine details.
- **Compression & Detail Loss:** Is fine detail present where it should be? Or is the image mushy in ways that look like a generation failure?

### 3. Light & Color Consistency
Light is the most common source of physical inconsistency in AI-generated images.
- **Light Source Direction:** Do all shadows fall consistently from one primary source?
- **Softness vs. Harshness:** Harsh light = sharp shadows. Diffused light = soft shadows. Does the shadow quality match the apparent light source?
- **Contrast Check:** Are highlights blown out or shadows crushed?
- **Color Temperature:** Is the image consistently warm or cool? Mixed, clashing temperatures are a red flag.
- **Saturation Consistency:** Is color intensity consistent across the image?

### 4. Cross-Panel & Asset Consistency (Comics/Multi-Shot)
When analyzing a comic page or multi-panel image, consistency is the highest priority.
- **Character Traits:** Same skin tone, hair, and face across every panel.
- **Clothing & Props:** Same colors, textures, and structural logic across shots.

---

## How to Write (Tone Rules)

**This section is critical. Read these examples EVERY TIME before writing your evaluation.**

### Rules
- **Length:** Justifications must always be 1-3 sentences total.
- **Focus:** Talk about the big, obvious differences. Don't nitpick tiny details when there's a huge structural problem.
- **Style:** Write like an average person casually explaining something to a friend. Keep it simple and natural.
- **Vocabulary:** Do NOT use big academic words or long chains of adjectives (e.g., "mushy, abstract, distorted blob"). Keep it basic and direct.
- **Punctuation:** No em dashes. No colons unless it's for a list. Use commas, periods, or "and" instead.
- **Banned Phrases:** Never use "Upon review of," "demonstrates superior," "holistic assessment," "semantic elements," "rendering the central face," "demonstrating a severe lack of," "generates a highly realistic," "fails on text generation," "AI text hallucinations," or "structural failure."

### Bad vs. Good Examples (Study These)

Every "Bad" example below is something that sounds robotic or over-analytical. Every "Good" example says the same thing but sounds like a normal person.

- *Bad (Too detailed/AI-obsessed):* "Response B is the clear winner because it maintains physically consistent weather logic. Response A hallucinates impossible horizontal rain streaks..."
- *Good (Punchy and focused):* "Response B is much better because it shows a physically consistent weather logic. Response A weather looks more like a painting."

- *Bad (Academic/Adjective Chains):* "Response A fails the prompt entirely by rendering the central face as a mushy, abstract, distorted blob, demonstrating a severe lack of detail and clarity."
- *Good (Average Human):* "Response B is much better because it actually made a realistic face that blends well with the shapes. Response A just turned the face into a blurry mess."

- *Bad (Robotic/Stiff):* "Response A is much better because it shows a realistic, physically accurate wall sit with normal human proportions. Response B totally failed on the body structure, generating a terrifying mess of extra hands and melted fingers."
- *Good (Casual/Natural):* "Response A is much better because she actually looks like a normal person doing a wall sit. Response B gave the girl a bunch of extra hands and totally messed up her arms."

- *Bad (Too simple, misses key visual observations):* "Response B is much better because it looks like a real photograph with natural water reflections. Response A totally messed up the physics by copy-pasting the exact same cloud reflection onto multiple different levels of water."
- *Good (Descriptive but conversational):* "Response B is much better because it looks like a real photograph with natural water reflections. Response A has clearly visible AI artifacts like perfectly even sized terraces with the exact same cloud reflections, and a filter effect that makes it look more like a painting than a real image."

- *Bad (Overly Analytical):* "Response A is much better because it provides a sharp, high-resolution image with crisp text. Response B has the exact same layout but is blurry, pixelated, and looks heavily compressed."
- *Good (User Example):* "Both responses correctly show the Venn relationship between Physics, Chemistry, and Biology and also correctly label their overlaps, but Response A is slightly better because it's much clearer and easier to read than Response B which is a little blurry."

- *Bad (Wordy/Over-explaining):* "Response B is much better because it provides clean, organized labels that actually point to the correct parts of the train. Response A is a confusing mess where the lines cross over each other and point to the completely wrong objects."
- *Good (Punchy/Direct):* "Response B is much better because its labels actually point to the correct parts of the train. Response A labels point to completely wrong objects."

- *Bad (Robotic/Academic Text Analysis):* "Response B is much better because it generated the complex text and table structure flawlessly. Response A failed because it has obvious AI text hallucinations, completely jumbling the KEYBOARD NAME header and messing up several letters in the table cells."
- *Good (Conversational Text Analysis):* "Response B is much better because it's writings are clear and easy to read and words spelled corectly. Response A has garbled spellings like in the first column header and in the sections of the the table."

---

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Present your evaluation directly in the chat using this exact template:

```markdown
### Input Analysis
[Explain what the prompt is asking for in plain English.]

### Response Analysis
**Response A:**
[What it got right and wrong. Be specific but conversational.]

**Response B:**
[What it got right and wrong. Be specific but conversational.]

### Final Ratings
- Instruction Following: [Response A / Response B / Tie]
- Visual Quality: [Response A / Response B / Tie]
- Absence of AI Artifacts: [Response A / Response B / Tie]
- Overall Preference: [Strongly Prefer A / Slightly Prefer A / Tie / Slightly Prefer B / Strongly Prefer B]

### Justification
[1-3 sentences. Write like you're texting a friend. No big words. Just say what you see.]
```

---

## Final Checklist (Review Before Submitting)

- [ ] I read the prompt BEFORE looking at the images.
- [ ] I looked at BOTH images carefully before writing anything.
- [ ] I checked the big stuff first (broken bodies, missing objects, wrong count).
- [ ] I checked consistency (skin tone, clothing, props across panels).
- [ ] I checked if the style matches what the prompt actually requested, not my personal preference.
- [ ] I rated each axis independently without double-penalizing.
- [ ] I avoided ties unless both images are genuinely equal.
- [ ] My justification is 1-3 sentences, written like a normal person talking.
- [ ] I re-read the tone examples before writing my justification.
