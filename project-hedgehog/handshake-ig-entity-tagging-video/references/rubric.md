# Handshake IG Entity Tagging Videos Rubric

The operative rubric for the IG Entity Tagging Videos QA task. Read this before working a live item.

## Contents

- [Source](#source)
- [What Is In Each Item](#what-is-in-each-item)
- [The Four Questions](#the-four-questions)
- [Entity Types](#entity-types)
- [Phase 1 Calibration — Video Checks](#phase-1-calibration--video-checks)
- [Phase 2 Calibration — Same Source vs Independent](#phase-2-calibration--same-source-vs-independent)
- [Phase 3 — The Six Reference Checks](#phase-3--the-six-reference-checks)
- [Identity By Type](#identity-by-type)
- [Partial And Distant Views](#partial-and-distant-views)
- [Refresher Benchmark 8.12 Calibration](#refresher-benchmark-812-calibration)
- [QA Rubric 1-5](#qa-rubric-1-5)
- [The Onboarding Assessment](#the-onboarding-assessment)
- [Knowledge Check Answers](#knowledge-check-answers)
- [Common Mistakes](#common-mistakes)
- [Final Checklist](#final-checklist)

## Source

No official PDF exists for this task. The **annotator instructions** linked from the assessment page are the top authority and are open-book during the assessment; they are not yet saved into this workspace, so read them live. The six checks and entity-type definitions here were transcribed from screenshots of that page.

Below them, the highest local authority is:

- `HANDSHAKE-AI/hedgehog-extracted/docs/08_ig_entity_tagging.md`
- `HANDSHAKE-AI/hedgehog-extracted/docs/09_entity_simulation_assessment.md`
- `HANDSHAKE-AI/hedgehog-extracted/docs/10_refresher_benchmark_812.md`

Calibration images referenced below live in `HANDSHAKE-AI/hedgehog-extracted/images/` and are indexed in `HANDSHAKE-AI/hedgehog-extracted/media_manifest.json`.

## What Is In Each Item

- **Video** — the clip being checked.
- **Tags** — coloured points on specific entities, each tied to a timestamp.
- **References** — separate media that should show the exact same entity as each tag.

This data teaches a system to make videos from reference images, which is why the connection has to be exact rather than plausible.

## The Four Questions

For each item, ask:

1. Is the full video usable? Blurry, AI-generated, or watermarked footage cannot provide reliable video data.
2. Does the reference identify the exact tagged entity? A different colorway, a look-alike, or a related product attaches the wrong identity.
3. Is the reference genuinely independent? A still copied from the video or media from the same filming session adds no new evidence.
4. Where is the entity clearest in the video? A strong frame and a tight box give downstream systems a precise target.

## Entity Types

The closed list of types tagged on this task, from the annotator instructions.

| Type | Definition | Matched by |
|---|---|---|
| **Product** | Any purchasable or ownable physical object — electronics, packaged goods, cosmetics, tools, homeware, artwork, gear. **The catch-all when nothing else fits.** | Exact SKU: model, colorway, scent, flavour |
| **Location** | A place or venue — a store, restaurant, room interior, street, or scene | Stable features like signage, storefront, or skyline — not a similar-looking spot |
| **Person** | A specific individual | Facial structure: jaw, eye spacing, brow line — not similar styling, hair, or outfit |
| **Animal** | A specific individual animal | Its own markings, colouring, and features — not breed or general appearance |
| **Clothing** | A specific garment | Exact cut, colour, and details like stitching, print, or buttons — not a similar style or category |
| **Logo** | A specific brand mark or wordmark | Exact design — not a similar icon, colour scheme, or general brand category |

Two emphases carried directly from the instructions:

- **Product is the explicit fallback type.** When an entity does not fit location, person, animal, clothing, or logo, it is a product rather than a forced fit elsewhere.
- **Calling same-breed animals a match is treated as a serious error.** This is stronger language than the guideline page uses, and it matches the QA rubric placing that failure in tier 1.

## Phase 1 Calibration — Video Checks

### Resolution

- **Pass** — subject is sharp, details readable without zooming.
- **Fail** — obvious pixelation, blur, and blocky compression visible without zooming.

Stylistic softness is not low resolution. Misclassifying it as such is a rubric-2 error.

### AI Detection

- **Pass** — normal skin texture, natural lighting, believable imperfections. Clean readable brand logos and sponsor text.
- **Fail** — over-smoothed and plastic-looking, the "too perfect" tell. Warped or garbled logos and text, inconsistent across subjects. Morphing objects, impossible motion.

### Watermarks

Only stock-media and third-party overlays fail — persistent brand, agency, or app marks stamped on the footage.

**Not watermarks:** a creator's own title card, baked-in captions or rating text from the source content, social-app sticker text added by the creator, on-product logos, social-app UI text.

**Watermarks:** a persistent third-party brand mark in the corner, a photo-agency stock watermark across the frame.

The stylised-mark rule: if the overlay is a brand's graphic logo or stylised mark, it counts as a watermark. If the brand name is spelled out in plain neutral text with no logo or icon, it does not.

### Lean Conservative

A check fails only when you can name a concrete problem — warping, garbled text, visible pixelation, a real overlay watermark. If the clip "feels off" but you cannot identify the artifact, it passes. If you genuinely cannot decide, Skip. If the data is broken, Flag.

## Phase 2 Calibration — Same Source vs Independent

**Drop as same source / duplicate:**

- Multiple reference images and edited output from one filming session — same person, outfit, table, cup, pastry, shooting context. They add no independent evidence.
- Multiple crops and near-repeats from one scene — same person, same jersey, same wall, same lighting.
- Three shots of the same product from the same studio source.

**Keep as independent:**

- Different references that each contribute to one edited composition. Do not collapse references just because they feed a single result. Separate product shots, packaging shots, and cover art stay valid.
- A product shot, a selfie, and a seated lifestyle photo of the same subject. Shared colour palette, wardrobe, or subject identity does not make them same-session.
- Generic catalog product photos on plain backgrounds. Two isolated catalog shots are not duplicates of each other — the question is source duplication, not aesthetic similarity.

## Phase 3 — The Six Reference Checks

Every reference is run through these six, **in order**. The annotator instructions state that failing any one of them means the reference gets dropped, even if it passes the others.

| # | Check | What it asks |
|---|---|---|
| 1 | **Type** | What kind of entity is this — product, location, person, animal, clothing, or logo? If the label is wrong, correct it to the best type. |
| 2 | **Same thing tagged** | The identity check. Does the reference show the *exact* same item, place, or person as what is tagged, not just something similar? |
| 3 | **Separate source** | Does the reference come from an independent source — not a crop or frame of the same original photo or video the tag came from? |
| 4 | **Subjects** | Is the reference a single, isolated subject? If more than one thing is shown, a box is required to disambiguate which one is the reference. |
| 5 | **Video frame** | Is the frame chosen from the video the clearest available frame for this entity? |
| 6 | **Frame box** | Is there a box drawn tightly around the right item on the video frame? Always required for a kept reference, regardless of whether the reference photo itself needed one. |

On check 1, "Nothing meaningful shown" applies only to junk or unusable media, and it drops the reference. On check 2, a No needs a specific reason naming the differing detail.

**References are not scored for resolution, AI generation, or watermarks.** Those checks apply only to the video in Phase 1.

That rule is narrower than it sounds, and misreading it in either direction costs marks.

**What it does mean.** Do not fail a reference as a *quality* judgment. A soft, small, badly lit, low-resolution, or watermarked reference is fine if it still establishes identity. There is no minimum resolution and no requirement that a reference be a professional product shot.

**What it does not mean.** It does not make image quality irrelevant. When blur, darkness, or compression destroys every identifying detail, the reference fails **check 2, identity** — not on quality grounds, but because it can no longer establish sameness. Same outcome, different check, and you must name the right one in the rejection note.

**Where the image-side task differs.** On the IG Entity Tagging *Task Simulation* — the image-side exercise scored 19/24, not this video QA gate — "it is a real photograph, never AI-generated" is listed among the requirements for a valid reference, and the exercise plants an explicitly AI-generated reference to test it. Treat an AI-generated reference as invalid there. The Phase 1 exemption above governs *this* task, where AI-generation checks belong to the video only.

If a live item ever puts these in tension, the task UI in front of you decides.

### How Checks 5 And 6 Behave

Checks 1-4 are true gates: a No drops the reference on the merits.

Checks 5 and 6 are work performed *on* a reference that has already passed the gates, so "dropped" there reads as "incomplete and does not count" rather than "failed on identity." The guideline page states the frame box is "always required for a kept reference," and that the "Next reference" button unlocks only when all required work for that reference is complete.

Both framings land in the same place operationally: a reference with no chosen frame and no box does not survive. Do not skip the frame review to save time — the QA rubric lists skipping required frame review as a tier-1 failure.

## Identity By Type

### People — faces must match

The reference and target must be the same individual. Align on facial structure: eye spacing, brow line, nose bridge, jaw, ear shape.

- **Keep** — same beard shape, smile lines, brow arch, eye spacing across a changed hat and background. The person does not change with setting.
- **Drop** — two men in the same team jersey with different nose shape, jaw width, and facial proportions. Matching kits are not identity.
- **Drop** — same archetype, beard and athletic build, different underlying face. Styling similarity does not carry the decision.
- **Drop** — two blonde women with different eye colour, nose shape, and jaw line. Hair colour and celebrity-adjacent styling are not identity.

### People — features must match too

Even when the face is the same person, the reference should share the relevant visible features from the tagged video moment.

- **Keep** — same face with matching beard shape and hairline across expression changes.
- **Keep** — same face, same slicked-back hair and drop earrings.
- **Keep** — same face, same round glasses and goatee, different outfit and background.
- **Drop** — same person, materially different hairstyle that no longer supports the tagged look.
- **Drop** — same person with a wig or dramatic hair-colour change.
- **Drop** — sunglasses hiding the eye region that would anchor identity, with beard and hair also differing.
- **Drop** — same face at a glance, but hair length, parting, and jewellery differ.

When features differ materially, ask for a reference closer to the tagged look rather than accepting the match.

### Products — exact SKU

Identity means the exact model, colorway, scent, or flavour. Shared packaging cues pull the eye toward false matches.

- **Keep** — Prada Cloudbust: silhouette, lug outsole, neoprene collar, and metallic toe detailing all match. Same SKU, different lighting.
- **Keep** — Nike Moto 2K: "MOTO 2K" tongue label, mesh panels, silver overlays, swoosh placement match. Wear on the target does not break identity.
- **Keep** — a book: title, author, cover art, and NYT Bestseller banner match. Same edition.
- **Keep** — Feather Fins: galaxy print, "feather" branding, and the W. Cardoso signature identify the exact set.
- **Keep** — LV Speedy: turquoise monogram canvas, vachetta handles, gold hardware, lock and key. Angle differs, special-edition SKU matches.
- **Drop** — same Nike model, different colorway. Swoosh colour, Air Zoom unit colour, and upper finish differ. Same product line is not identity.
- **Drop** — same Nike Heritage cap silhouette, bright white against cream/off-white. Colorway is part of identity.
- **Drop** — same brand's SPF 25 lip balm against SPF 25 sunscreen. Overlapping label text is not identity; these are different SKUs.
- **Drop** — patterned pouches that differ in shape, weave, stripe direction, and closure.
- **Drop** — chunky low-tops with patterned laces that differ in toe cap, midsole shape, and side panels.
- **Drop** — a plush with a similar silhouette but a different body pattern. Pattern is part of product identity.
- **Drop** — silver curb-link bracelets differing in link gauge, clasp style, and bar detail.

### Clothing — print and construction

- **Drop** — black mesh dresses that share length and sleeve but differ in print motif, neckline, and bodice construction. Same aesthetic, different garment.

Check print scale and garment construction, not silhouette and colour alone. See the benchmark cases below.

### Animals — individual, not breed

The tag is on a specific animal. Identity rests on individual markings: chest patch, face-stripe pattern, eye colour.

- **Drop** — two brown tabbies where the tagged cat has a solid white chest patch and darker face mask and the reference has narrower face stripes and no white chest. Same breed, different individual.

Accepting a same-breed look-alike attaches the wrong individual to the annotation.

### Locations — the landmark itself

- **Keep** — a close view from below and a wide waterfront view of the Statue of Liberty. Torch, crown spikes, robe silhouette, and pedestal align. Angle, crop, and distance do not break identity.
- **Drop** — a different place entirely. Generic "travel landmark" similarity is irrelevant when the tagged location and the reference show different scenery.

### Logos And Text — the exact mark

- **Keep** — a decorative crest where letterform, gold border treatment, crest silhouette, and top flourish all match.
- **Drop** — the same sponsor word on a jersey and on a trade-show sign. Same brand text, different exact entity.
- **Drop** — an Adidas trefoil target against a different emblem on a shirt. Same apparel ecosystem is not the same mark.
- **Drop** — two Manchester United crests with different crop context and mismatched emblem details.

## Partial And Distant Views

**Partial views — observe what you can see.** References often show only part of what appears in the video.

- **Keep** — cropped video frame of baggy light-wash jeans against a full product shot where wash, silhouette, and fade patterns match.
- **Keep** — a hand in a white golf glove against a laid-flat product shot where perforation pattern, stitching, and colour line up.
- **Drop** — cream mini skirts that disagree on pleating, waistband, and construction. A partial view is still enough to see a mismatch.

Read those keeps carefully, because the reason they pass is easy to misread. The jeans do not keep because both are light-wash denim; they keep on the **fade pattern**. The glove does not keep because both are white golf gloves; it keeps on the **perforation pattern and stitching**. In each case a feature close to unique to that item is visible and agrees.

**Far away matches — don't guess through the blur.**

- **Drop** — a blurred silver cylinder against a sharp trash-can product photo. Any silver cylinder would "match".
- **Drop** — motion-blurred legs in black pants against a specific tapered ankle pant. Blur hides fabric weight, cut, and hem.

When the visible evidence cannot confirm the reference is that exact item, drop and ask for a clearer frame or reference.

### The Distinguishing-Feature Test

Before answering Yes on any reference, name the specific feature that rules out every other item of this kind. If the honest answer is "same colour, same type of thing," the answer is **No**.

Note what the two blur drops above have in common with a perfectly sharp frame of a plain object: in both, *any* item of that kind would match. Blur is one way to arrive there. The other is an item that has no distinguishing features to begin with.

**Plain unbranded gear generally cannot clear the bar.** A generic black paddle against a stock black paddle, a plain blue life vest against a stock blue vest, an unmarked white mug against a catalogue mug — all drops on identity, even when both images are sharp and the colour and form agree. There is nothing present that separates this one from every other one.

**Branded, printed, patterned, or signed items generally can.** The Nike tongue label, the LV monogram canvas, the galaxy print on the fins, the ornate shop signage, a specific ditsy floral at a specific scale.

Two failure modes this prevents, in opposite directions:

- Accepting a look-alike because colour and category agree and nothing visibly contradicts. Absence of contradiction is not evidence of identity.
- Dropping a genuine match because part of the item is hidden. Occlusion and partial views are fine when a distinguishing feature is visible in the part you *can* see.

## Refresher Benchmark 8.12 Calibration

The graded answer key from the 8.12 refresher benchmark. These are the misses that actually happened.

**Case 1 — white floral dress. Not a valid reference.** The off-shoulder cut, smocked bodice, and bell sleeves match, so it reads as the same dress at a glance. But the floral print differs: in the video the flowers are smaller and more spread out with plain white space between them; in the reference they are larger and packed closer, so the print reads denser. The skirt construction also differs — the video dress flows as one continuous flared skirt, the reference has a visible seam where it gathers into a second tier. Two concrete mismatches, not an angle or lighting difference.

*The fix:* when two items share a silhouette, check the print first — are the individual motifs the same size, with similar spacing? Then check construction — same number of seams or tiers, gathering in the same place? If either is off, it is a different garment.

**Case 2 — red printed dress. Not a valid reference.** Both are red with a small white floral print and an off-shoulder cut. But the neckline differs: straight-across in the video, a sweetheart dip with a gathered tie at the bust in the reference. That is different construction, not a camera angle. The print scale also mismatches — larger and more spread out in the video, smaller and tighter in the reference.

Flagging this reference for heavy blur, or for a second cropped photo stitched into the right edge of the frame, was also counted correct. Those are real independent problems with the reference.

**Case 3 — lamp. Yes, this reference needs a box.** The reference shows three separate items on one table: the lamp, a small clock, and a vase of dried flowers. All three are real, distinct, nameable objects that could each be mistaken for the referenced item, and nothing points to the lamp specifically.

*The rule:* if more than one distinct, nameable object appears in a reference photo, a box is required around the one being referenced, no exceptions. Props and blurry background objects that clearly are not real products can be ignored — a clock and a vase cannot.

**Case 4 — H&M overlay. Yes, this counts as a watermark.** The "H&M" text is written in the exact red cursive script H&M uses as its official logo. That script is the brand's visual mark, the same as a swoosh or an apple icon. It counts even though the letters are readable as text.

Two wrong readings to avoid. First, "the brand name is spelled out so it doesn't count" — readability is irrelevant; what matters is the stylised script. Second, "it's part of a caption graphic, not a corner logo bug" — there is no such exemption. Position in the frame and inclusion in a larger caption design do not matter.

**The pattern across nearly every miss:** fellows are good at spotting that two things are related, but the task needs one specific, checkable detail that proves it is the same one. Confirming general style, colour, or category is step one, not the whole check.

## QA Rubric 1-5

- **5 Exceptional** — all video checks correct including boundary cases. Clear duplicates and same-source references handled correctly. Each detailed review uses the right type-specific identity standard. Reference boxes added only where disambiguation is needed. Clearest video frame selected after reviewing the clip, and the video item tightly boxed. Rejection notes name the exact differing detail.
- **4 Strong** — all outcome-changing verdicts correct. Type, identity, source, isolation, and frame decisions complete. Boxes usable and notes present, though one note or box could be more precise.
- **3 Acceptable** — overall outcome correct with one debatable source or identity judgment, or a minor frame/box precision issue. Required steps complete; notes understandable but possibly generic.
- **2 Weak** — errors that change the result or reduce training value: accepting look-alikes, missing a clear duplicate or same-source reference, applying the wrong identity standard, unnecessary or inaccurate reference boxes, choosing an unclear frame, boxing the wrong video item, or misclassifying stylistic softness as low resolution.
- **1 Unacceptable** — evidence of rushing or fundamental misunderstanding: patterned clicking, treating same-brand as same-product, calling same-breed animals a match, ignoring AI tells or source reuse, skipping required frame review, or careless boxes that do not identify the compared item.

## The Onboarding Assessment

The **IG Entity Tagging Videos — Annotator Onboarding Assessment** gates access to this task.

| | |
|---|---|
| Questions | 21 |
| Passing score | 15 / 21 |
| Attempts allowed | 1 |
| Estimated time | 20-25 minutes |
| Progress saved | No — complete in one sitting |
| Open book | Yes — keep the annotator instructions open and refer back at any point |

Three sections:

- **Section A — Watch and tag.** Watch a real clip from the task and list every entity you would tag. Use the six entity types, and name each entity as specifically as the footage supports rather than by broad category. Scan the whole clip before listing, and do not stop at the main subject.
- **Section B — Judge the references.** The real reference photos from that same clip. Decide which ones actually confirm the tagged entity. This is the six checks applied for real, so the identity standards and the "one specific, checkable detail" bar from the 8.12 benchmark are what is being tested.
- **Section C — Everything else.** Identity edge cases beyond the clip, evidence thresholds, duplicate-check scope, workflow controls, and the QA rubric. Expect the Skip-versus-Flag distinction, the lean-conservative rule on video checks, what Phase 2 is and is not asking, and the tier language in the 1-5 rubric.

Note that this is a different assessment from the IG Entity Tagging Task Simulation in `HANDSHAKE-AI/hedgehog-extracted/docs/09_entity_simulation_assessment.md`, which is the image-side tag-and-box exercise scored 19/24 over 24 items.

## Knowledge Check Answers

From the training page, with the reasoning that makes each one generalise.

- **Slightly soft clip, no nameable artifact** → pass both the sharpness and real-footage checks. A vague "feels off" is not evidence.
- **Three leggings references from the same studio source** → mark as same source / duplicate. Different angles of one shoot are not separate evidence.
- **Two burgundy dresses with different silhouettes** → not the same reference. Similar colour is not enough.
- **Same exact sneaker, but the reference was grabbed from the same filming session at another angle** → drop on the source check. The identity match is real; independence is what fails.

From the simulation assessment, the requirements for a valid reference photo are: it isolates the single item with nothing competing for attention; it is the exact product or item, not just similar or same-category; and it comes from a different photo or post than the one the entity was tagged in. Being AI-generated-free, same-angle, or professionally shot are **not** requirements on the reference.

Every tagged item needs a specific name, not a general category. When unsure exactly what something is, name it as specifically as the image supports and note shape, colour, and any visible packaging or text.

## Common Mistakes

- Stopping the comparison once the big details line up — silhouette, colour, category.
- Treating same brand, same product line, or same breed as identity.
- Dropping a real match because the tagged frame is occluded, instead of scrubbing to a clearer frame.
- Over-dropping in Phase 2 on aesthetic similarity rather than source duplication.
- Applying video-quality checks to references.
- Forgetting the video-frame box on a kept reference whose own reference image needed no box.
- Generic rejection notes that do not name the differing detail.
- Using Skip for broken data, or Flag for a hard but legitimate call.

## Final Checklist

- Full video watched; all three quality checks answered against concrete evidence.
- Tag editing patterns answered for every occurrence.
- Clear duplicates and same-source references dropped, independent ones kept.
- Every surviving reference passed type, identity, source, and isolation in order.
- Every kept reference has a chosen frame and a tight box on that frame.
- Every identity rejection names the exact differing detail.
- Phase 4 review completed before submitting.
