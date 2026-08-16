---
name: handshake-ig-entity-tagging-video
description: Run Handshake IG Entity Tagging Videos QA items. Use when asked to check whether a tagged Instagram clip is usable, drop duplicate or same-source references, verify each reference shows the exact tagged entity, and pick and box the clearest video frame. This is the video QA gate, not creating new tags.
---

# Handshake IG Entity Tagging Videos

You are a **video quality gate**. An earlier team watched videos and tagged entities, then attached reference media that should identify the same entity. For each item you decide whether the clip is usable, whether every reference identifies the exact tagged entity, and where that entity is clearest in the video.

You are validating and refining existing tags. You are not creating new ones.

## File Locations

- `references/...` paths are inside this skill's folder.
- `../shared-references/...` are Project Hedgehog cross-task references.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Source Hierarchy

**No official PDF exists for this task.** The extracted training pages are the highest local authority.

1. The **annotator instructions** linked from the assessment page. These are open-book during the assessment and outrank everything below. They are not saved into this workspace yet — read them live and say so when you cite them second-hand.
2. `HANDSHAKE-AI/hedgehog-extracted/docs/08_ig_entity_tagging.md` — the task guideline page.
3. `HANDSHAKE-AI/hedgehog-extracted/docs/10_refresher_benchmark_812.md` — the 8.12 refresher benchmark answer key, the graded calibration set for look-alike calls.
4. The current task UI and the visible item in front of you.
5. `references/rubric.md` in this skill folder.
6. `HANDSHAKE-AI/guidelines.md` as a broad summary only.
7. User memory or prior answers.

The six checks and entity-type definitions below come from the annotator instructions, transcribed from screenshots rather than a saved page. Save the instructions page into `HANDSHAKE-AI/hedgehog-extracted/` when it can be captured.

## Entity Types

The closed list of types you tag on this task.

- **Product** — any purchasable or ownable physical object: electronics, packaged goods, cosmetics, tools, homeware, artwork, gear. **The catch-all category when nothing else fits.**
- **Location** — a place or venue: a store, restaurant, room interior, street, or scene. Matched by stable features like signage, storefront, or skyline, not a similar-looking spot.
- **Person** — a specific individual, confirmed by facial structure (jaw, eye spacing, brow line), not just similar styling, hair, or outfit.
- **Animal** — a specific individual animal, confirmed by its own markings, colouring, and features, not breed or general appearance. **Calling same-breed animals a match is treated as a serious error.**
- **Clothing** — a specific garment, matched by exact cut, colour, and details like stitching, print, or buttons, not a similar style or category of clothing.
- **Logo** — a specific brand mark or wordmark, matched by exact design, not a similar icon, colour scheme, or general brand category.

Do not treat `handshake-IG Entity Tagging Task.pdf` as the source for this task. That PDF governs `handshake-ig-entity-tagging`, which is the create-the-tag task on images, not this QA gate.

Say plainly when an expected source cannot be found. Do not import TELUS or Outlier rules into Handshake work.

## Which IG Entity Skill Applies

- **This skill** — you are handed a video with existing tags and references, and asked to pass/fail the clip, drop references, and box a frame.
- `handshake-ig-entity-tagging` — you are creating annotations from scratch and finding one reference per annotation.
- `handshake-ig-entity-verification` — you are given one yellow-box target and one reference and asked for a definitely/likely same/different verdict.

## Inspecting The Media

Do not judge a Reel you have not actually looked at. Fetch and inspect it first:

```bash
python3 handshake-ai-skills/tools/inspect_media.py --url <reel-url> --out /tmp/insp
```

This finds every scene, saves a keyframe per scene, builds a contact sheet, and
transcribes the audio with timestamps. Read the scene list and the contact sheet
before answering anything about the clip as a whole — a decisive shot can last under a second, and missing it means answering about a clip you only partly watched.

Full usage, the zoom flag for identity calls, and the two failure modes it exists
to prevent are in `../shared-references/media-inspection.md`.

## Core Rule

The connection must be exact: the same person, the same product variant, the same garment, the same place, or the same individual animal. Not merely something similar.

Recognising what kind of thing something is and confirming it is the specific one in front of you are different acts. The benchmark pattern across nearly every miss: fellows are good at spotting that two things are related, but the task needs one specific, checkable detail that proves it is the same one.

Before working a live item, read `references/rubric.md`.

## Audio Required

This task requires audio. You must pass an audio check before working on it. Incorrect audio answers count against your score.

The gate itself is a **playback test in the task UI** — it confirms your machine can actually produce sound. Extracting the audio track does not satisfy it, so check your output device and volume before starting rather than after failing it.

Once you are past the gate, `inspect_media.py` gives you the audio to reason *about*: `audio.wav` is the demuxed 16 kHz mono track, and the transcript timestamps tell you what is said and when. Use that for any question about speech, background sound, or silence. Never answer an audio question from the picture alone.

## Hard Gates

- Do not fail a video check without a concrete, nameable artifact. A feeling is not evidence.
- Do not accept a look-alike. Same brand, same product line, same breed, same silhouette, and same brand text are not identity.
- Do not keep a reference that came from this video or the same filming session, however good the identity match.
- Do not apply resolution, AI-generation, or watermark checks to references as a quality judgment. On this task those belong to the video in Phase 1 only. A reference whose blur destroys every identifying detail still fails, but on identity rather than on quality. See the scope note in `references/rubric.md`.
- Do not answer Yes on a reference whose only agreement with the target is colour and category. Name the distinguishing feature or drop it.
- Do not skip the frame review. Every kept reference needs a chosen frame and a tight box on it.
- Do not write a generic rejection note. Name the exact differing detail.
- Do not use Skip for broken data or Flag for a hard-but-legitimate call.

## The Four Phases

1. **Video** — watch the whole clip and answer three quality checks, then the two tag-editing pattern questions.
2. **Quick duplicate check** — scan all references together and drop clear duplicates and same-source media.
3. **References** — review each surviving reference one at a time through four ordered checks, then pick and box the clearest video frame.
4. **Review** — verify every answer, verdict, note, frame, and box before submitting.

### Phase 1 — Video

Watch the full clip. You can answer while it plays, but only continue once it has played through.

1. **Is the video sharp and clear?** Flag above-average pixelation, blur, or blocky compression visible without zooming in.
2. **Does this look like real footage (not AI-generated)?** Check for warping, morphing objects, impossible motion, garbled text, and the over-smoothed plastic "too perfect" look.
3. **Does the video have a watermark over it?** Check corners and centre for an overlaid stock-media or third-party mark.

Lean conservative. A check fails only when you can point to a concrete problem. If you genuinely cannot decide, use Skip. If the data is broken, use Flag.

If the interface shows "This item will be set aside," an automated check has already ruled the video out. Submit and continue — there is nothing left to judge.

**Watermark vs other text.** Only persistent stock-media, agency, or app-mark overlays stamped on the footage fail this check. Creator captions, title cards, on-product logos, baked-in source captions, and social-app sticker text are not watermarks. A brand's stylised graphic mark counts as a watermark wherever it sits in the frame; a brand name in plain neutral text does not.

### Tag Editing Patterns

Two further questions appear after the quality and audio checks. Watch the full video and answer for each pattern whenever it appears.

- **Quick jumpy cut** — Yes when there is a clear, abrupt shot boundary but foreground and background stay very similar, so the image seems to snap. It must be a real cut, not body motion, camera shake, or continuous camera movement. A conventional cut to a clearly different scene is not this pattern.
- **Very short shot (under 1 second)** — Yes if any distinct shot appears for less than one second before the next cut, including a near-static frame that flashes on screen. Do not count a brief moment inside one continuous shot.

### Phase 2 — Quick Duplicate Check

All references appear in a grid. Mark "Same source / duplicate" only when you are sure the reference is:

- the same reference, even at different angles;
- the same exact image appearing more than once;
- a frame or segment copied from this video; or
- footage from the same filming session, meaning the same time and place.

Marked references are dropped and never reach the detailed review. If you are unsure, leave it unmarked — the source decision can still be made in Phase 3.

Phase 2 is not asking whether the tag category is correct or whether the reference is an identity match.

Do not over-drop. Generic catalog product photos on plain backgrounds are allowed and are not duplicates of each other. Shared colour palette, wardrobe, or subject identity does not make references same-session. The question is source duplication, not aesthetic similarity.

### Phase 3 — References: The Six Checks

Every reference runs through these six, **in order**. The annotator instructions state that failing any one of them drops the reference, even if it passes the others.

1. **Type** — what kind of entity is this: product, location, person, animal, clothing, or logo? If the label is wrong, correct it to the best type. Choose "Nothing meaningful shown" only when the tag or reference is junk, which drops it.
2. **Same thing tagged** — the identity check. Does the reference show the *exact* same item, place, or person as what was tagged, not just something similar? If No, give a specific reason: colorway, logo placement, face, hair, stitching, model.
3. **Separate source** — does the reference come from an independent source, not a crop or frame of the same original photo or video the tag came from?
4. **Subjects** — is the reference a single, isolated subject? If more than one thing is shown, a box is required to disambiguate which one is the reference.
5. **Video frame** — is the frame chosen from the video the clearest available frame for this entity? Scrub the clip, then choose "Keep tagged frame" if the original timestamp is already best, or "Use current frame" if you found a clearer one.
6. **Frame box** — is there a box drawn tightly around the right item on the video frame? **Always required for a kept reference**, regardless of whether the reference photo itself needed one.

**How checks 5 and 6 actually behave.** Checks 1-4 are gates: a No drops the reference. Checks 5 and 6 are work performed *on* a reference that already passed, so the "dropped" framing reads as "the reference is not complete and does not count" rather than "it failed on identity." Doc 08 states the frame box is "always required for a kept reference" and that "Next reference" unlocks only when all required work is done. Either way the operational rule is the same: no frame and no box means the reference does not survive.

Drag a box across either image to zoom into fine detail. Press R or Reset to zoom back out.

### Phase 4 — Review

Verify the video answers, every kept and rejected reference, the selected frames, the boxes, and the specific rejection reasons. Use Change to revise anything, add an optional overall note, then submit.

## Identity Standards By Type

Full worked cases are in `references/rubric.md`. The short form:

- **Person** — facial structure must match: eye spacing, brow line, nose bridge, jaw, ear shape. Similar hairstyle, build, or demographic is not identity. Beyond the face, the reference must also share the relevant visible features from the tagged moment — a materially different hairstyle, hair colour, wig, or sunglasses hiding the eye region means drop and ask for a closer reference.
- **Product** — identity is the exact SKU: model, colorway, print, scent, flavour, stitching, logo placement. Same line in a different colorway is a drop.
- **Clothing** — check print scale and garment construction, not just silhouette and colour. Flower size and spacing, seams and tiers, neckline shape.
- **Animal** — individual markings decide it: chest patch, face-stripe pattern, eye colour. Breed match is not identity match.
- **Location** — the landmark itself must match. Angle, crop, and distance can change without breaking identity.
- **Logo or text** — match the exact mark, not the brand family. The same word in two contexts is two different entities.
- **Partial views** — keep only when the visible parts carry a *distinguishing* feature that agrees: a fade pattern, a perforation pattern, a print motif, a tongue label, a logo placement. Drop when the visible portion clearly disagrees, and also when it agrees on nothing more than colour and category.
- **Far, dark, or motion-blurred targets** — if the frame cannot show the details that separate this SKU from any other, drop and ask for a clearer frame or reference.

**The one test that decides every identity call.** Name the specific feature that rules out every other item of this kind. If the honest answer is "it is the same colour and the same type of thing," that is a **drop**, however sharp both images are.

This is the single most common way to get it wrong, so it is worth stating in the negative too. Every keep example in the guidance is anchored to something close to unique: the jeans keep on their fade pattern, the golf glove on its perforation pattern and stitching, the Nike Moto 2K on its tongue label. Every drop is either a contradiction or a case where *any* item of that kind would have matched — the blurred silver cylinder, the motion-blurred black pants.

Plain unbranded gear usually cannot clear this bar. A generic black paddle, a plain blue life vest, an unmarked white mug: even in a clean, sharp frame there is nothing to match on except colour and category, so a stock photo of a similar one is a drop rather than a keep. Branded, printed, patterned, signed, or otherwise marked items generally can clear it.

Occlusion is normal in video. Scrub for a clearer frame before dropping on identity — dropping a real match wastes the tag. But scrubbing only helps when a clearer frame would actually reveal a distinguishing feature. If the item has none, no frame will save it.

## Accuracy Matters

Multiple annotators vote on each item and the final decision comes from agreement. Your accuracy is tracked, and consistently disagreeing with the group removes you from the task. This is not about speed.

## Skip, Flag, And Reset

- **Skip** — you genuinely cannot decide. The item returns to the queue.
- **Flag** — the data is broken: the video will not load, references are missing, the item is corrupt. Enough independent flags remove the item.
- **Reset** — clears your answers and restarts the same item. It does not submit or skip.

## Rejection Note Style

The note is read by whoever has to fix the tag. Name the physical difference, not your confidence in it.

Baseline style from `../../handshake-evaluator/references/task-router.md` applies: short sentences, periods, no em dashes, no semicolons, no colons in prose. Write as a careful person explaining what they saw, not as an evaluator filing a report.

- Lead with the differing detail, not the conclusion. "Swoosh colour and Air Zoom unit differ" beats "not the same shoe."
- Name the part. The tongue label, the waistband, the chest patch, the crest scrollwork. Not "the design."
- Say what kind of difference it is. Print scale, construction, colorway, face, or source. That tells the reader whether a better reference would fix it.
- On a drop for want of a distinguishing feature, say so plainly rather than inventing a mismatch.
- Do not soften a decided call. If you are genuinely unsure, use Skip instead of writing a hedged note.

Banned, because each reports your confidence rather than the item: "does not appear to match", "seems different", "not quite the same", "similar but not identical", "upon closer inspection", "exhibits".

- Good: `Same Nike Heritage silhouette, but the boxed cap is bright white and the reference is cream.`
- Good: `Reference is a crop of this video. Same pose, same background, so it adds no independent evidence.`
- Good: `Plain black paddle with no marking on either side. Nothing here separates it from any other black paddle.`
- Bad: `Upon closer inspection the items do not appear to be identical.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files. Present the answer in the chat.

There are two shapes. Pick by what is actually on screen, not by habit.

### Assessment Mode

One question at a time: a multiple choice, a Yes/No on a single reference, or a free-text justification. This is the onboarding assessment and the refresher benchmarks. **Do not return the four-phase report for a single question** — it buries the answer.

```markdown
**[The answer — the option text, or Yes/No]**

[Two to four sentences. Name the check that decided it and the concrete detail. If a distractor is tempting, say in one line why it fails.]

[If the question also asks for a written justification, give it as a paste-ready block.]
```

When the question asks you to explain, the graders want the **specific differing detail**, not the general principle. "The reference is a one-piece all-yellow paddle including the shaft and T-grip, while the tagged paddle has a yellow blade on a natural wood shaft" scores. "It is not the same paddle" does not.

Flag genuine uncertainty rather than hiding it, and say what would change the answer. One attempt is allowed and progress is not saved.

### Production Mode

A full queue item with a video, tags, and references to work through all four phases.

```markdown
### Phase 1 — Video
- Sharp and clear: [Pass / Fail — name the concrete artifact if Fail]
- Real footage: [Pass / Fail — name the AI tell if Fail]
- Watermark: [None / Watermark — what it is and where]
- Quick jumpy cut: [Yes / No — where]
- Very short shot: [Yes / No — where]

### Phase 2 — Duplicates
[Each reference marked same-source or duplicate, and the condition it met. Write "none" if nothing was dropped.]

### Phase 3 — References
1. **Reference [n] — [what it shows]**
   - 1 Type: [confirmed / corrected to X]
   - 2 Same thing tagged: [Yes / No — the exact differing or matching detail]
   - 3 Separate source: [Yes / No — why]
   - 4 Subjects: [isolated / multiple — box needed?]
   - Verdict: [Keep / Drop]
   - 5 Video frame: [keep tagged frame / use frame at ~M:SS — why it is clearest]
   - 6 Frame box: [what the box encloses]

2. **Reference [n] — ...**

### Item Verdict
[Pass / Skip / Flag, with one line of reasoning.]

### Uncertain
[Any call you could not make from the visible evidence, and why. Write "none" if everything was decidable.]
```

## Final Checklist

- Video checks answered against concrete evidence, not impressions.
- Clear duplicates and same-source references dropped; independent references kept.
- Every kept reference passed type, identity, source, and isolation in order.
- Every kept reference has a chosen frame and a tight box on that frame.
- Every identity rejection names the exact differing detail.
- Skip used only for genuine indecision, Flag only for broken data.
