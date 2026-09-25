# Worked Cases

Six pairs from the guideline's Good vs Bad Calls section, with the images in `examples/`.
Source: `HANDSHAKE-AI/ads-creative/vs-1786692229-260813-ads-creative-i2i-q5-text-flaws.md`.

Each case gives the references, what is actually on each image, the correct call with the exemplar
feedback, the wrong call the module warns against, and notes from looking at the actual images.

The quoted feedback is the guideline's, and most of it runs well past the 100 to 120 character target for
this task. Take the reason from it, not the length. Trimmed versions are in SKILL.md under How to Write the Feedback.

## Contents

- [Case 1: Garbled Blocks Decide The Pair](#case-1-garbled-blocks-decide-the-pair)
- [Case 2: Invented Lines Next To A Grounded Name, One-Sided](#case-2-invented-lines-next-to-a-grounded-name-one-sided)
- [Case 3: Looks Invented But Is In The Brief, And A Dropped Button](#case-3-looks-invented-but-is-in-the-brief-and-a-dropped-button)
- [Case 4: Wrong Language Loses To Small Misspellings](#case-4-wrong-language-loses-to-small-misspellings)
- [Case 5: One Clean Side Against A Text-Free Side](#case-5-one-clean-side-against-a-text-free-side)
- [Case 6: Both Clean, The Same Seed Copy](#case-6-both-clean-the-same-seed-copy)
- [What The Six Have In Common](#what-the-six-have-in-common)
- [Assessment Calibration](#assessment-calibration)

## Case 1: Garbled Blocks Decide The Pair

`examples/case1-fryer-seed.jpg`, `examples/case1-fryer-A.jpg`, `examples/case1-fryer-B.jpg`

**References.** Advertiser TecDo-FB. No headline. Description "Factory Direct | OEM/ODM | Wholesale Price".
A long English primary text: pressure fryer, heavy-duty 304 stainless steel, energy-saving, food safety
standards, 1 unit MOQ, OEM & ODM, full sets of certification, extended warranty, custom dimension, website
dllin.com, "Send us a DM now to receive catalog and factory wholesale price!". The seed is a factory photo;
its only text is a red Chinese banner and wall signage **inside the scene**.

**What is actually on each image:**

- **A.** A top headline "Professional OEM/ODM Factory of Commercial Pressure Fryer" (grounded, the primary text's first line). The next line starts grounded and breaks mid-sentence ("wholesale o nsieocnt project business?"), then a full line of letter salad. Below the photo, two columns: "Who were lrococcoaudines:" and "Who core balaa' accepiices:", each with bullet lists that are almost entirely pseudo-text. "Stiadepre dliin.com", "Simcbou tapofxooroor", and the CTA "Send us a DM now oe revere caterat fectiatre and fatouly whooude oride!".
- **B.** A photo band, then a navy panel: "TecDo-FB" with "Factory Direct • OEM / ODM • Wholesale" (advertiser and description), "PROFESSIONAL COMMERCIAL PRESSURE FRYER PARTNER", "✓ 1 UNIT MOQ — Test market with no large stock commitment", "304 Stainless Steel | Energy-Saving | **ISO/NSF Certified**", "OEM & ODM • Full Certifications • Global After-Sales Support • Custom Design for Restaurant, Hotel & Marine Galley", and a pill "Get Catalog & Wholesale Price → dllin.com". All crisp.

**Correct: Output B — clearly fewer text flaws.**

> "A's messaging panel is mostly pseudo-text: the heading reads 'Who were lrococcoaudines:', the web line 'Stiadepre dliin.com', and the call to action 'Send us a DM now oe revere caterat fectiatre and fatouly whooude oride!'. B's panel is readable and its lines come from the brief, except 'ISO/NSF Certified', which appears nowhere in the seed or the brief. Three garbled blocks outweigh one invented claim."

Both panels are new overlay, so every line is checked against the brief. A dissolves into letter salad from
the second line down. B paraphrases the primary text almost throughout, but "ISO/NSF Certified" names a
certification the brief never mentions: an invented specific. Both sides are flawed; A's are far heavier,
so clearly. Name B's invented line anyway.

**Wrong: Similarly good/bad.** "Both have a headline and a full messaging panel with the brand name and a
website." Called at browsing size. Both panels look like text; only one is.

**Image notes.**

- B's "Full Certifications" is grounded (the brief says "full sets of certification"). Only the named standard, ISO/NSF, is invented. **The specific is the flaw, not the topic.**
- "Global After-Sales Support" and "Custom Design" are fair paraphrases of "extended warranty … spare parts" and "custom dimension".
- The "TecDo-FB" badge on the woman's shirt in B is picture text. It neither helps nor hurts.
- The seed's Chinese banner is picture text in the factory. It does not make Chinese the ad's language; the brief's English copy does.

## Case 2: Invented Lines Next To A Grounded Name, One-Sided

`examples/case2-rental-seed.jpg`, `examples/case2-rental-A.jpg`, `examples/case2-rental-B.jpg`

**References.** Advertiser "Millenium Rentals 2" (one N). No headline, description or primary text. The
seed is a phone photo of a blue sedan in a loading yard; the only marks are the small Ford oval on the
grille and some paper in the car's window.

**What is actually on each image:**

- **A.** The car on a studio floor against flat navy and grey blocks. **No overlaid text.** (It also turned the sedan into a hatchback: a picture flaw, out of scope.)
- **B.** A navy header: "MILLENIUM RENTALS 2", "FORD FIESTA • READY WHEN YOU ARE", a bullet list "NO HASSLE RENTALS / FLEXIBLE TERMS / BOOK TODAY", and a strip "RELIABLE • AFFORDABLE • AVAILABLE NOW".

**Correct: Output A — clearly fewer text flaws.**

> "Only B has overlaid text. Its headline is the advertiser's name as the brief spells it, but the brief has no copy and the seed has no text, so 'FORD FIESTA', 'NO HASSLE RENTALS', 'FLEXIBLE TERMS', 'READY WHEN YOU ARE' and 'RELIABLE • AFFORDABLE • AVAILABLE NOW' all come from nowhere. A has no overlaid text, and the seed had none to drop."

Start with the grounded line: "MILLENIUM" copies the brief's one-N spelling, so it is correct as written.
Everything else fails. The model name is an invented specific; the four marketing lines are invented
generic lines. "BOOK TODAY" alone would be fine as a generic CTA. Four generic lines plus a model name
weigh clearly against zero flaws.

**Wrong: No overlaid text to compare.** "A has no text, so there is nothing to compare." B has plenty,
and it is flawed. A one-sided pair always has an answer other than this button.

**Image notes.**

- The guideline treats "FORD FIESTA" as invented even though a tiny Ford oval sits on the seed's grille. "Fiesta" appears nowhere, and a model name is a specific. Do not stretch a badge into a model name.
- Do not "fix" MILLENIUM to MILLENNIUM in your head. The brief sets the spelling.
- B is a tidy, professional banner. That is Q6's business. Here it loses clearly.

## Case 3: Looks Invented But Is In The Brief, And A Dropped Button

`examples/case3-chingari-seed.jpg`, `examples/case3-chingari-A.jpg`, `examples/case3-chingari-B.jpg`

**References.** Advertiser "Chingari App By Tech4Billion". Headline "🎁 First 3 Private Calls FREE". Primary
text "I'm still here if you want another conversation 😉💬 / Don't keep me waiting 💋📹 / Open Chingari now 📲".
The seed's overlay: the orange "Chingari" logo top right and a yellow "Call Now" pill button.

**What is actually on each image:**

- **A.** The woman in a warm interior holding a phone. Overlay: the Chingari logo top right. **No Call Now button.** The phone screen shows the Chingari app, "Private Call", "Connected • 02:14" and a "First 3 calls FREE" chip.
- **B.** The woman in an arched hallway. Overlay: the Chingari logo top right and the yellow "Call Now" pill. Same as the seed.

**Correct: Output B — slightly fewer text flaws.**

> "Both keep the seed's logo. A dropped the seed's 'Call Now' button; B kept it. A's phone screen is writing on a screen inside the photo, so it is picture text and counts neither way. Read anyway, it is the brief's headline ('Private Call', 'First 3 calls FREE'), not an invention."

Two traps. The phone is picture text, so nothing on it counts. And annotators who read it anyway tend to
call "First 3 calls FREE" an invented offer, but the brief's headline is "First 3 Private Calls FREE".
"Connected • 02:14" is incidental prop text. What counts: A dropped the seed's generic button, a secondary
element, so slightly.

**Wrong: Output B — clearly fewer text flaws.** "A invents a 'Private Call' feature and a free-calls offer
that the advertiser never made." Right side, wrong reason and wrong strength.

**Image notes.**

- The phone screen is the most readable text in A, which is exactly why it pulls the eye. Classify before you read.
- "Call Now" is a generic CTA. Adding it would not be a flaw; dropping the seed's copy of it is, but only slightly.

## Case 4: Wrong Language Loses To Small Misspellings

`examples/case4-game-seed.jpg`, `examples/case4-game-A.jpg`, `examples/case4-game-B.jpg`

**References.** Advertiser "Club Pilates 浅草吾妻橋". Audience IN. No copy. The seed is **all design**: a game
lobby with English labels (Teen Patti, Point Rummy, Crash, JHANDI MUNDA, Explorer Slots, Andar Bahar, Car
Roulette, Dragon VS Tiger, Safari of Wealth, Refer & Earn, VIP GIFT, Service, Email, Activity, ADD CASH),
"GIVEAWAY 850", "JACKPOT 21102.16", "₹71058.42", "[player_ZlVhJ] withdraws [5000 Rs]".

**What is actually on each image:**

- **A.** The lobby reproduced almost exactly, with small errors in small labels: "Andar Banar", "Safari of Waalth", "Emnil", "LUCKY 3RATTI". **"GIVEAWAY 850" is gone** from the lower half.
- **B.** A rebuilt 3D adventure scene. English kept: "JACKPOT 21102.16" (twice), "GIVEAWAY 850", "Teen Patti", "Car Roulette". Added: the advertiser name "Club Pilates 浅草吾妻橋" (twice) and **four Japanese lines**: "— 無限の冒険が今、始まる! —", "今すぐ参加 ・ 豪華ギフト&バイクをゲット!", "850 GIVEAWAY リアルタイムジャックポット実施中", and a button "今すぐ登録 → 限定特典". Nearly all the seed's tiles and menu labels are gone.

**Correct: Output A — clearly fewer text flaws.**

> "B adds four lines of Japanese ('無限の冒険が今、始まる!' and three more). The seed's text is English and the brief has no copy, so the language matches neither reference; B also drops most of the seed's game tiles and menu labels. A keeps the seed's text with several small misspellings: 'Andar Banar' for 'Andar Bahar', 'Emnil' for 'Email', '3RATTI' for '3PATTI'."

A has several slightly-tier rendering flaws. B has a clearly-tier language flaw **and** dropped most of the
seed's core text. The advertiser's name carries Japanese characters, but **a name does not set the
language**. B's crisp rendering is why this looked like a B win when only rendering counted. "GIVEAWAY 850"
and "JACKPOT 21102.16" on B are grounded.

**Wrong: Output B — clearly fewer text flaws.** "B's text is sharp and correctly formed. A misspells several
labels." This judged rendering only. Check language and fidelity before you count typos.

**Image notes.**

- The exemplar lists three of A's typos. There are more at zoom ("Safari of Waalth"), and A also lost the giveaway banner. It still wins clearly: many small slips do not reach a language flaw plus wholesale dropped text.
- "Club Pilates" on a card-game ad is odd, but it is the advertiser's name, so it is grounded wherever it appears.

## Case 5: One Clean Side Against A Text-Free Side

`examples/case5-footwear-seed.jpg`, `examples/case5-footwear-A.jpg`, `examples/case5-footwear-B.jpg`

**References.** Advertiser "Khimar High Quality". Audience ID. Primary text in **Indonesian**: "Ga perlu jait
kebaya mahal-mahal, aku co di shopee sebagus ini luv / Beli di sini 👉 <shopee link>". The seed is a
five-photo collage of sandals; its only words are printed on the white shoebox lids: "Ready for your day.."
and "From : Lady Modesta shoes". **No overlaid text.**

**What is actually on each image:**

- **A.** Sandals on a marble table beside two shoeboxes. The lids repeat the seed's print, partly garbled (a mangled "Lady Modesta shoes" and a scribbled top line). **No overlaid text.**
- **B.** Sandals on rattan shelves. Overlay: a white serif headline "Ready for your day..", a caption "From : Lady Modesta shoes", and a letter-spaced footer "KHIMAR HIGH QUALITY • LADY MODESTA SHOES".

**Correct: Similarly good/bad.**

> "Only B has overlaid text: 'Ready for your day..' and 'From : Lady Modesta shoes' are printed on the seed's shoe boxes, and the footer is the advertiser's name plus that box line. All clean. A has no overlaid text; the print on its boxes is picture text. The seed had no overlaid text to drop, so A has zero flaws and the pair is similar."

Classify first. The seed has no overlay. A's garbled box print is picture text. B lifts the seed's box
wording into a headline and adds the advertiser's name: all grounded, all clean. Zero against zero.

**Wrong: Output B — clearly fewer text flaws.** "A's box labels are garbled; B's text is clean." The garbled
print is in the photo. Scope decides whether you may judge a defect at all.

**Image notes.**

- **Language check:** the brief copy is Indonesian, but the seed's box print is English, so B's English is in the ad's language. The rule is "matches the seed's text **or** the brief's copy".
- B's double period "day.." copies the seed's box exactly. Not a punctuation slip.
- The same pair appears in the Q6 Text Style module, where B wins clearly on design. Same images, opposite question, different answer.

## Case 6: Both Clean, The Same Seed Copy

`examples/case6-technician-seed.jpg`, `examples/case6-technician-A.jpg`, `examples/case6-technician-B.jpg`

**References.** No advertiser name, no copy. The seed is a window-cleaner ad on green: "Regular & Reliable",
"Window Cleaner", "Areas We Cover", Peterborough, Stamford, Bourne, Spalding, and a button "CLICK HERE FOR
YOUR FREE QUOTE". The technician's shirt carries an "INCREDIBLE WINDOW CLEANING" logo.

**What is actually on each image:**

- **A.** Blue smoky background. Every overlay block copied word for word; the headline in chrome and the button in glossy orange. **The shirt logo is garbled** ("INCREDIBL… WINDOW CLEAN…", broken letters).
- **B.** Dark background with orange sparks, the man moved right. Every overlay block copied word for word. The shirt logo reads cleanly.

**Correct: Similarly good/bad.**

> "Every overlaid block (headline, area list, button) is the seed's copy, kept and legible in both outputs, and nothing was added. The chest logo on A's technician is garbled, but it is printed on the shirt inside the photo, so it is picture text."

The seed is the only source of grounded text, and both stick to it. A's glossy button still reads. The only
defect in the pair is on the shirt. With it excluded, the overlays are equal.

**Wrong: Output B — clearly fewer text flaws.** "A's company logo is unreadable pseudo-lettering; B renders it
crisply." Accurate but out of scope. As a flat designed lockup over the image, it would count.

**Image notes.**

- A's chrome headline and B's italic headline are style differences. Q6 territory.
- With no brief copy and no advertiser, "grounded" means "on the seed" and nothing else.

## What The Six Have In Common

- **Every wrong answer reached outside the overlay's correctness**: to browsing-size impressions, to the no-text button as a shrug, to phone-screen and box and shirt text, to rendering alone.
- **Two correct answers are clearly on fidelity or language, one is clearly on garbling, one is slightly, two are ties.**
- **Neither tie had a flawless pair of images.** Both had a garbled defect, in the picture. The ties are ties because the overlay layer is equal.
- **The no-text button is never right in these six**, and it is the wrong answer in one.

## Assessment Calibration

The module's six assessment questions, with answers derived from the guideline and the images (the module
does not show a key). Full text is in the guideline file.

| Q | The item | Answer | Why |
|---|---|---|---|
| 1 | Seed carries headline and logo. A keeps both cleanly. B has no overlay | **A** | B erased the seed's core text. The one-sided rule's exception |
| 2 | OTP bank card flyer, brief has no copy. A: a full flyer. B: only the "otpbank" wordmark | **B** | B's wordmark is on the seed (card and bag). A invents "UP TO 5% CASHBACK", "0€ MONTHLY FEE", "AVAILABLE ACROSS EU" and several generic lines |
| 3 | Gold watch restaged with props. No designed text layer on either | **No overlaid text to compare** | Only the dials carry words. B's dial print is garbled, but it is picture text |
| 4 | Brief headline "Free delivery on your first order". B prints "Free delivery, 24-hour dispatch" | **A** (clearly) | "24-hour dispatch" is an invented specific, not a generic line |
| 5 | Portuguese supplement ad, seed has no text. A: no text. B: "BEFORE / AFTER" labels | **A** | English matches neither reference. The direction's "negative space for labels" does not ground them |
| 6 | Plazavea recruiting flyer in Spanish. Both copy the text cleanly; A dropped the "¡TÚ PUEDES SER PARTE!" sticker | **B** (slightly) | One dropped secondary element |
