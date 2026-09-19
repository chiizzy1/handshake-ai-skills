# Worked Cases

The guideline's 15 graded pairs, one per failure reason, with the images in `examples/`. Each case gives
the official call and comment, the wrong call the guideline warns against, and **what the images actually
show**, from viewing every pair side by side.

Where the images show something the official answer does not mention, it is marked **Observed, not in
the official answer**. Those notes are calibration: they show what the graders did and did not count.

## Contents

- [Hero Cases](#hero-cases)
- [Non-Hero Cases](#non-hero-cases)
- [What The Fifteen Teach Together](#what-the-fifteen-teach-together)

## Hero Cases

### 1. Lost the core product: the vibe is not the product

`examples/case01-hero-lost-product-champagne-orig.jpg`, `-gen.jpg`

**The ad:** G.H. Mumm Cordon Rouge champagne at Auckland Duty Free, "2 FOR $99".

**Official call:** Fail. Lost the core product.
**Comment:** "The bottle is gone, replaced by two glasses and a bucket."

**What the images show.** The generated ad is otherwise almost identical: the same white plinth, the same
diagonal light shaft, the same "AUCKLAND DUTYFREE 2 FOR $99" in the same place and colors. Only the
bottle changed, into two champagne flutes and a gold ice bucket. **No bottle, no label, no Mumm branding
anywhere.**

**Why it is tempting to pass.** Everything that carries mood survived, and the offer text is word for
word. That is exactly the trap: a "2 for $99" offer for a product that is not in the picture.

**The wrong call:** Pass, "Premium glasses and a gold bucket keep the celebration feel, and the offer text
survived." This rewards the vibe instead of the product. **When the ad names a product, find it first.**

### 2. Altered the product: identity is the body, not the brand

`examples/case02-hero-altered-suitcase-orig.jpg`, `-gen.jpg`

**The ad:** a Rollink foldable suitcase. "Fold It. Store It. Forget the Bulk."

**Official call:** Fail. Altered the product.
**Comment:** "Different color, and the foldable bag became a rigid case."

**What the images show.** The original is **pale blush pink**, and a woman is shown **bending it at the
hinge** to slide it onto a closet shelf, so the fold is demonstrated on screen. The generated case is
**saturated hot pink**, held out by a single arm, fully rigid, with no fold visible.

**Observed, not in the official answer:** the **Rollink logo and the quilted diamond pattern both
survived.** That is the point of the case's title. Brand marks surviving does not protect the product,
because the customer buys the body. And the woman was cut to an arm, which removes the one thing that
proved the fold. The official answer counts it under "altered" rather than use case.

**The wrong call:** Pass, "Same brand, same closet scene, just a fresher color." Color and construction
are part of the customer's decision.

### 3. Added or invented products: additions must be intentional

`examples/case03-hero-added-coffeepods-orig.jpg`, `-gen.jpg`

**The ad:** The Killer Coffee Co. Blackout pods, "SUBTLETY IS DEAD".

**Official call:** Fail. Added or invented irrelevant products, **and** missing or incorrect selling
points.
**Comment:** "A random wrench appeared and the headline is gone."

**What the images show.** The box survived exactly: skull art, "10X THE AVERAGE CAFFEINE PER POD",
"HAZARDOUS CAFFEINE CONTENT", "BLACKOUT". The green lightning background became plain black, which is
allowed. A **large chrome adjustable wrench** now takes up the whole right half. "SUBTLETY IS DEAD" is
gone.

**Observed, not in the official answer:** the loose pods changed from **silver-green aluminium** to
**black**. The official call does not count it, likely because the box is the hero and the loose pods
are staging. On a live item where loose pods were the product, check it. The wrench also carries
lettering, which is rendering and not yours.

**Two reasons, both checked.** This case exists partly to show that. **Check every reason that applies.**

**The wrong call:** Pass, "The wrench is a quirky prop that fits the unhinged tone." Ask what the addition
does for the message. A tool the advertiser never showed, doing nothing, is a distraction.

### 4. Irrelevant use case: judge the action alone

`examples/case04-hero-usecase-cream-orig.jpg`, `-gen.jpg`

**The ad:** Elemis Pro-Collagen Marine Cream, "AGE-DEFYING RADIANCE IN 14 DAYS".

**Official call:** Fail. Irrelevant use case.
**Comment:** "She is drinking the cream."

**What the images show.** The headline, "14 DAYS", and "Award-winning marine-powered day cream for
hydrated, youthful-looking skin" all survived. A woman tips the jar into her open mouth, with cream
pouring in. **The jar and its label are intact.**

**Observed, not in the official answer:** the original's **before-and-after panel** ("Skin appears firmer
and hydrated", "Reduced fine lines and wrinkles") and its clinical-trial footnote are gone, and **three
stacked jars became one**. The official call counts neither. Two lessons: a selling-point Fail needs a
**critical** line gone, and here the headline and payoff line survived. And three display jars of one
cream are not a count claim, unlike a five-piece set, so showing one is not a product change.

**The wrong call:** Fail, altered the product, "The cream must have changed if she can drink it." Right
verdict, wrong reason. **When the wrongness is in the action, it is use case.**

### 5. Irrelevant casting: think target demographic first

`examples/case05-hero-casting-hairserum-orig.jpg`, `-gen.jpg`

**The ad:** Ellerand rice water and rosemary serum. "The shot took the weight. And your hair."

**Official call:** Fail. Irrelevant casting.
**Comment:** "The two women became two men; the campaign is written for women."

**What the images show.** An illustration of two women, before and after weight loss, the second pulling
at thinning hair and holding up loose jeans. The generated ad is a photo of **two men with long hair**
acting out the same story. The syringe, rice, rosemary and Ellerand bottle all survived, and a scale and
calendar were added behind them.

**Observed, not in the official answer:** the headline itself is gender-neutral. **The demographic signal
comes from the original's imagery**, not the words. Read who the ad shows as well as what it says. The
added scale and calendar support the weight-loss story and are not counted against it.

**Allowed here:** illustration became photography. The bad-example note confirms a model can change and
illustration can become a photo. **Who the person is** has to keep fitting.

**The wrong call:** Pass, "The illustration became a realistic photo and the models look professional."
Polish instead of fit.

### 6. Scene does not fit: some scenes are the message

`examples/case06-hero-scene-villa-orig.jpg`, `-gen.jpg`

**The ad:** Solmar Villa Holidays, "Save up to 20% on winter sun", Avgi Thesan, Zakynthos.

**Official call:** Fail. Scene does not fit the product.
**Comment:** "The sea view is what is being sold; a hot tub in a studio loses the point."

**What the images show.** The original is an infinity pool over a blue sea with an island. Every word
survived: the offer, "Book your winter sun villa now", the location pin, the arrival dates. The generated
ad is a **hot tub in a beige studio**, with a hand resting on its rim and folded towels.

**Observed, not in the official answer:** **the hot tub is in the original**, on the terrace to the right
of the pool. The generator isolated an asset the villa really has and dropped the view around it. That
is why the reason is "does not fit" and not "invented scene": nothing was invented, the selling scene was
lost. The result reads like an ad for a hot tub.

**Observed, a classification tension:** by the guideline's own test, a villa holiday is paid-for access,
which is Non-Hero. The guideline files it under Hero. Follow the reason the guideline picked. On a live
item, set the type by the customer-pays test, and if that makes it Non-Hero, the matching reason is
"scene does not fit the service".

**The wrong call:** Pass, "A new setting is allowed, and the offer text survived." New settings are
allowed when the scene is staging. Here the scene is the product.

### 7. Missing selling points: respect what the advertiser spent space on

`examples/case07-hero-sellingpoints-cardreader-orig.jpg`, `-gen.jpg`

**The ad:** KickBazar "TYPE-C MEMORY CARD READER 3 IN 1".

**Official call:** Fail. Missing or incorrect selling points or headlines.
**Comment:** "Headline and the port list are gone; only 'Transfer Data in Seconds' survived, and it looks slapped
on."

**What the images show.** The original carries the headline, a Type-C badge, the SD, micro SD and USB 3.0
port list, "HIGH SPEED DATA TRANSFER UP TO 5Gbps", four feature icons, and "ONE DEVICE. ENDLESS
POSSIBILITIES." The generated ad keeps the KickBazar logo and one line, "Transfer Data in Seconds". **The
reader itself is preserved closely**, with the same 128GB cards and USB stick inserted, on a desk with a
notebook, pen, earbuds, phone and tote bag.

**Observed, not in the official answer:** the cable in the generated ad ends in what reads as a
**full-size USB-A plug**, where the original shows a Type-C connector. For a product whose headline is
"Type-C", the connector is part of its identity. Look at it on a live item. If it holds at normal size,
"altered the product" also applies.

**Allowed here:** the added desk props are placed the way a photographer would place them. The official
call does not count them.

**The wrong call:** Pass, "The clean lifestyle shot sells better than a wall of text." Your taste replacing
the advertiser's decision.

## Non-Hero Cases

### 8. Digital product: an interface can only be preserved

`examples/case08-nonhero-digital-match3-orig.jpg`, `-gen.jpg`

**The ad:** Mistfall Match, a gothic match-3 game.

**Official call:** Fail. Digital product preservation issues.
**Comment:** "The game board is gone; only the art and floating score text remain."

**What the images show.** The original's centre is the playable grid of gems, gummies and skull tiles
with "SCORE: 145,300" and "MOVES: 18" counters. The generated ad keeps the title, the mermaid, the corals,
the jellyfish and "GOTHIC GOURMAND EDITION", and **drops the board entirely**. The counters float as loose
text, and **"MOVES: 18" now appears twice**. The subtitle "A Burton-esque Gothic Tale" and "Issue #2 The
Gingerbread Chronicles" are gone too.

**The lesson:** the decorative art is not the game. The board is what the player buys into.

**The wrong call:** Pass, "It looks like a nicer, cleaner version of the same game ad." The improvement
trap. An interface cannot be dropped or improved.

### 9. Invented products: specific inventions always fail

`examples/case09-nonhero-invented-photobooth-orig.jpg`, `-gen.jpg`

**The ad:** a photo-booth service at events.

**Official call:** Fail. Added or invented irrelevant products.
**Comment:** "A branded candy package was invented and put front and center."

**What the images show.** The original is four friends laughing with mustache and glasses props at a
sunset rooftop event. The generated ad **blurs those same people into the background** and puts a pair of
hands in front holding a **"SPARK BITES sour gummy candy, Berry Mix"** pouch, with "vegan, gluten free,
10 packs, 100g" on it. The props drop to the foreground edges.

**Two failures stack:** an invented branded product, and the service itself pushed out of focus. The
people having fun are what a photo booth sells.

**The wrong call:** Pass, "Party candy fits a party service." Generic versus specific. A generic prop can
be fine for a service. A named, packaged product the advertiser never showed cannot.

### 10. Irrelevant use case: would this business do the work this way?

`examples/case10-nonhero-usecase-sofa-orig.jpg`, `-gen.jpg`

**The ad:** Elite Care Services "SOFA CLEANING Service", 200 per seat.

**Official call:** Fail. Irrelevant use case.
**Comment:** "The extraction service became hand-spraying and wiping."

**What the images show.** The original shows an extraction wand and hose on a grey sofa, with **half the
sofa visibly cleaned**, which is a built-in before and after. The generated ad has a kneeling man
spraying a trigger bottle and wiping with a cloth, with liquid running down the front of a charcoal sofa.

**Observed, not in the official answer:** the guideline says "same cleaner, same room", but in the images
**the cleaner is a different man, the room changed from white to beige, and the sofa from grey to
charcoal.** None of that is counted, which confirms those changes are allowed. The half-clean demonstration
is also gone.

**The lesson:** method is the service. Spray and wipe is not what this business sells.

**The wrong call:** Pass, "Same person, same sofa, same cleaning service." Stopping at the nouns.

### 11. Changed a preserved person: names are signals

`examples/case11-nonhero-preserved-students-orig.jpg`, `-gen.jpg`

**The ad:** Cross & Climb coaching institute congratulating students ranked AIR 8, 7 and 10 into Army Law
College, Mohali.

**Official call:** Fail. Changed a person who should be preserved.
**Comment:** "The names and ranks stayed, the people changed."

**What the images show.** Almost everything survived: the names Aakriti, Purav, Avni, all three AIR
ranks, the headline, the grey polos with the logo, the congratulations line, the address and phone. A
courtroom background was added. **All three students were replaced** by different, older-looking models.

**Allowed here:** "MOHALI" moved into the headline, the layout changed, and a courtroom background was
added. None counted.

**The lesson:** the name printed under a person is the signal. The human in the shot is who the name
belongs to.

**The wrong call:** Pass, "Models can always be swapped, and the new ones look more polished."

### 12. Casting fit: the person must support the story

`examples/case12-nonhero-casting-festival-orig.jpg`, `-gen1.jpg`, `-gen2.jpg`

**The ad:** Breckenridge Presents "UNITED WE DANCE", "FESTIVAL ENERGY. ALL NIGHT.", First Avenue,
Minneapolis.

**Official call:** Generated ad 1 Fail, irrelevant casting. Generated ad 2 Pass.
**Comment:** "One man dancing alone in an awkward pose is not festival energy; the group with the festival behind
them is."

**What the images show.** The original is a chrome figure in a laser show over a crowd. **Generated 1** is
one smiling man in a black tee, arms out, on a plain teal backdrop, with no crowd and no stage.
**Generated 2** is four friends dancing together on a stage with the festival crowd, lights and confetti
behind them. All text survived in both.

**Observed:** the original figure is a chrome humanoid, not a real person, so there is nobody to preserve.
Casting here is purely about fit. Generated 2 also recoloured "UNITED WE DANCE" to cyan, which is allowed.

**The lesson:** presence is never enough. A crowd dancing together **is** "united we dance".

**The wrong call:** Both pass, "Each one shows somebody dancing."

### 13. Scene does not fit: stay in the world the input built

`examples/case13-nonhero-scene-horseracing-orig.jpg`, `-gen.jpg`

**The ad:** racecourseside betting tips, "GET TODAY'S TIP. Place £15 on for myself and only pay when you
win."

**Official call:** Fail. The scene does not fit the service.
**Comment:** "Horse racing became two esports players at PCs."

**What the images show.** Every word is identical. Horses racing at a course became two esports players in
headsets in a red arena.

**Observed:** the brand name is **"racecourseside"**. The world is printed in the logo.

**Why not invented scene:** an esports arena is not an asset the advertiser claims to have. It is the
wrong world, not a false amenity.

**The wrong call:** Pass, "The text is identical, and gaming is also a betting audience." Letting the copy
do all the work.

### 14. Invented scene: never invent what the advertiser does not have

`examples/case14-nonhero-invented-aurora-orig.jpg`, `-gen.jpg`

**The ad:** Akshar Travels, Northern Lights in Iceland, $4199 for 10 days and 9 nights.

**Official call:** Fail. Invented scene.
**Comment:** "The tour became a luxury glass suite the advertiser does not offer."

**What the images show.** Every word and number survived: $4199, the dates, "25+ Years", "4580+ Tours",
"570K+ Happy Customers", the three inclusions, "BOOK NOW". The couple is the same. They moved from a black
sand beach under the aurora into a **glass-walled suite** with a fireplace, lounge chair, wine glasses and
rug, watching the aurora through the glass.

**The lesson:** it looks better and would probably sell better, and that is the problem. The customer
arrives and that suite does not exist.

**The wrong call:** Pass, "It is gorgeous, still shows the aurora, and keeps every selling point."

### 15. Missing selling points: the biggest text is the biggest signal

`examples/case15-nonhero-sellingpoints-bathroom-orig.jpg`, `-gen.jpg`

**The ad:** Costco "Tub-to-Shower Conversion", Member Starting Price **$14,999**.

**Official call:** Fail. Missing or incorrect selling points or headline.
**Comment:** "The headline and the $14,999 price are gone."

**What the images show.** The original is almost all text: headline, "Member Starting Price", and $14,999
in the largest type on the page. The generated ad keeps the Costco logo and "Costco Member Special •
Limited Time", and shows a woman in a robe in a marble bathroom.

**Observed, not in the official answer:** the generated bathroom **still has a freestanding tub** next to
the walk-in shower. Even the picture no longer shows a conversion.

**The wrong call:** Pass, "The generated bathroom looks dreamy, which is what sells a remodel." The
advertiser led with a price.

## What The Fifteen Teach Together

**Every bad example rated something true.** The glasses do carry the mood. The new case is a fresher
color. The wrench does fit an unhinged tone. The lifestyle shot is cleaner. The game art is nicer. The
suite is gorgeous. Each lost to the question the rater never asked: **did what was being sold survive?**

**What is allowed, seen across the cases without being counted:**

- A different background, color scheme, or layout (cases 3, 11, 13, and assessment Q4)
- Illustration becoming a photograph (case 5)
- A different person, when nothing signals they must survive (cases 10 and 12)
- Lifestyle props placed with intention (case 7)
- Text restyled or moved (cases 11 and 12)

**What always failed:**

- The product gone, or its body changed
- An invented product, room, view or amenity
- A signalled person replaced
- The headline, a critical claim, or an oversized price gone
- The service shown done a way the business never would

**Right verdict, wrong reason is a real error.** Case 4's bad example gets Fail right and still misses.
