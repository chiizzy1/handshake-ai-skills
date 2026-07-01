# Handshake Text-to-Video Rubric

Use this reference for Handshake Text-to-Video, T2V Benchmark, and Less AI Generated Benchmark tasks.

## Source

- `HANDSHAKE-AI/T2V/instructions.md`
- Current task UI and prompt

## Core Principle

AI-generated video breaks across time. A clip can look acceptable in a still frame and fail when scrubbed. Always evaluate temporal continuity, not just frame quality.

## Standard Workflow

1. Read the prompt fully.
2. Identify requested subjects, actions, setting, style, audio, and ending state.
3. Watch Response A and Response B at normal speed.
4. Watch again, pausing at suspicious action/contact/detail moments.
5. Use frame sampling or frame-by-frame scrubbing for the suspect moments.
6. Compare the videos for:
   - prompt adherence;
   - temporal consistency;
   - physical plausibility;
   - interaction/contact realism;
   - subject/object persistence;
   - style consistency;
   - audio presence and synchronization.
7. Choose which response looks less AI-generated.
8. For the more AI-generated video, identify which artifact categories are clearly present.

## The Seven Artifact Categories

### 1. Flicker And Shimmer

Surfaces or textures ripple, pop, crawl, or rewrite between frames with no physical cause.

Look at:

- grass, mist, walls, tables, fabric, hair, skin, scan lines, game-like static, repeated background texture.

Diagnostic:

- Freeze on a texture and advance frame by frame. If pixels rewrite while geometry stays intact, classify it as flicker/shimmer.

### 2. Morphing And Deformation

Solid shapes change form during motion.

Look at:

- hands, faces, limbs, paddles, balls, table edges, gates, gravestones, flashlight, hood, shoulders, architecture.

Diagnostic:

- Track a rigid object or body part across several frames. If it bends, stretches, fuses, melts, or changes anatomy, classify it as morphing/deformation.

### 3. Object Persistence Failures

Objects vanish, reappear, duplicate, swap, or teleport without physical reason.

Look at:

- balls, paddles, hands, feet, flashlights, birds, gravestones, gates, crowd details, props.

Diagnostic:

- If an object exists in one frame and is gone in the next with no exit path or occlusion, classify it as object persistence failure.

### 4. Physics Violations

Gravity, momentum, collision, bounce, inertia, sliding, falling, or contact mechanics break.

Look at:

- ball bounces and reversals, falls, slips, knee slides, paddle hits, flashlight swing, cloth movement, body momentum.

Diagnostic:

- When an object changes direction or speed, rewind a few frames and find the cause. If there is no plausible cause, classify it as physics violation.

### 5. Identity Drift

A subject, costume, body, face, or environment gradually changes identity/design across the clip.

Look at:

- clothing color, body proportions, face structure, hood shape, flashlight design, cemetery layout, player identity.

Diagnostic:

- Compare the subject near the start and end. If the same subject slowly becomes visually different, classify it as identity drift.

### 6. Interaction Inconsistency

Objects or bodies overlap or should interact, but the expected contact response does not happen.

Look at:

- paddle-ball contact, player-floor contact, hand-object contact, character-gate proximity, flashlight beam hitting surfaces, bodies colliding or passing through objects.

Diagnostic:

- When two things touch or overlap, ask whether the second thing reacts. If not, classify it as interaction inconsistency.

### 7. Text And Detail Distortion

Text, signs, labels, fine detail, or repeated details garble or change between frames.

Look at:

- scoreboards, labels, logos, signs, gravestone markings, UI-like text, repeated stones, scan-line detail, tiny background objects.

Diagnostic:

- Freeze on readable or repeated detail and advance several frames. If it changes, garbles, or repeats unnaturally, classify it as text/detail distortion.

## Spatial Artifacts Still Matter

Still-image defects also apply inside video:

- anatomy and faces;
- plasticky or painted textures;
- bad edges or halos;
- distorted text;
- background repetition.

In video, these defects may also pulse, crawl, morph, or drift over time.

## Stylized Prompt Rule

Do not require photorealism from prompts that ask for cartoons, low-poly game footage, retro render, scan lines, anime, or other stylized looks.

Instead ask:

- Is the chosen style stable?
- Does it look like a skilled human could have produced it in that style?
- Does any part slip into a different rendering mode?
- Are intended artifacts, such as scan lines, stable and stylistically appropriate?

## Audio Review

If the prompt asks for audio, inspect whether the soundtrack matches visible events.

For sports/action prompts:

- paddle hits should align with paddle-ball contact;
- ball bounces should align with visible table/floor contact;
- shoe squeaks should align with foot slides and sudden movement;
- crowd reactions should align with intense moments.

For atmospheric/stylized prompts:

- caws, static, ambience, footsteps, doors, or flashlight/electrical effects should fit the scene and timing.

Audio failures can support preference decisions. Do not force audio-only problems into visual artifact categories unless the task explicitly treats audio as an artifact category.

## Preference Strength

Strongly prefer a response when:

- one video has far fewer or less severe AI tells;
- one video follows the prompt much better;
- the other video has obvious temporal collapse, impossible physics, or missing key prompt elements.

Slightly prefer a response when:

- both videos are flawed but one is modestly cleaner;
- differences are real but not decisive;
- one is visually cleaner while the other follows the prompt slightly better.

Tie only when:

- both are similarly realistic/generated-looking and similarly faithful;
- no meaningful difference can be defended from visible/audio evidence.

## Counting Artifact Categories

The benchmark asks how many artifact issue types are visible in the more AI-generated video.

Count categories, not events.

If one category appears multiple times, count it once.

If the available options are 3, 4, 5, and 6:

- choose 3 for three or fewer clear categories;
- choose 4 for four clear categories;
- choose 5 for five clear categories;
- choose 6 for six or more clear categories.

Do not pad the count with uncertain categories.

## Rationale Format

Use concise artifact bullets:

- `Physics violation: around 0:02, the ball changes direction without a visible paddle hit or bounce.`
- `Object persistence: the ball disappears between frames and reappears near the table with no path.`
- `Interaction inconsistency: the paddle swing does not line up with the ball contact or hit sound.`

Avoid:

- generic wording like `it looks weird`;
- overly long explanations;
- guessing about offscreen events when visible evidence is enough.

