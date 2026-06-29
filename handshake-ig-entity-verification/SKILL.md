---
name: handshake-ig-entity-verification
description: Evaluate Handshake IG Entity Verification tasks. Use when Codex must compare a yellow-box target entity against a reference image or green-box reference, choose definitely/likely same or different, skip, flag bad data, or write a short reason using entity-specific identifying features.
---

# Handshake IG Entity Verification

## Core Rule

Use `HANDSHAKE-AI/pdfs/handshake-IG Entity Verification.pdf` as the source of truth.

Before verifying a live item, read `references/rubric.md`.

## Workflow

1. Read the entity type and label first.
2. Look at the yellow box on the target image. Only verify what is inside that box.
3. Look at the green box on the reference, or the whole reference if no green box exists.
4. Pick 1-3 identifying features that matter for the entity type.
5. Choose the verdict based on whether those features match.
6. Write a short reason naming the features used.

## Hard Gates

- Do not judge outside the yellow box.
- Do not ignore a green box on the reference.
- Do not call a match definite when angle, occlusion, blur, or distance hides key features.
- Do not use same breed, color, brand line, or clothing style as identity by itself.
- Do not flag hard-but-legitimate comparisons. Use Skip when the item is valid but you cannot tell.
- Do not use Skip for broken data that should be flagged.

## Verdict Scale

- Definitely same: identifying features clearly match.
- Likely same: probably same, but quality, angle, occlusion, or distance leaves room for doubt.
- Likely different: probably different, but evidence is not fully decisive.
- Definitely different: identifying features clearly do not match.
- Skip: legitimate item, but you cannot confidently tell this time.
- Flag as bad data: source is broken and should not be verified by anyone.

## Entity Feature Rules

- Person: face structure, hairline, distinguishing marks. Hair color and clothing are not identity by themselves.
- Clothing: logo placement, strap width, cut, hardware. Color/style alone are not enough.
- Product: exact product variant, size, scent, flavor. Not just brand or line.
- Location: signage, distinctive architecture, fixed landmarks. Not same kind of place.
- Animal: individual markings, eye color, chest patch. Breed match is not identity match.

## Final Checklist

- Entity type and label read first.
- Only yellow-box target region was judged.
- Reference region checked correctly.
- Verdict confidence matches evidence quality.
- Skip and flag were not mixed up.
- Reason names concrete identifying features.
