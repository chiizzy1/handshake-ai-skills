# Handshake IG Entity Tagging Rubric

Use this reference for IG Entity Tagging tasks.

## Source PDF

- `handshake-IG Entity Tagging Task.pdf`

## Task Shape

You watch an Instagram video or inspect Instagram image content and annotate every visible entity.

Entities include:

- people
- clothing
- products
- locations
- style elements
- animals
- visible text or signage

Each annotation needs a reference photo that proves what the entity is.

## Minimum Requirements

- Tag all visible entities in every image, not just the main subject.
- At least four complete annotations per image when enough entities are visible.
- One reference photo per annotation.
- The reference photo should isolate the entity so it is obvious what you are pointing at.

Most quality flags come from missing visible entities, not from picking the wrong entity.

## Strict Scan Order

Scan each image or video frame in this order:

1. People.
2. Clothing and shoes.
3. Accessories and bags.
4. Products and packaging.
5. Animals.
6. Places and landmarks.
7. Visible text, logos, and signage.
8. Style elements that are visually recognizable.

If the entity is visible enough to name at a supportable level, annotate it.

## Entity vs Reference

An entity is a valid visual concept that can be recognized in an image or video:

- Taylor Swift
- Eiffel Tower
- sushi
- Tesla Model 3
- leather backpack
- white sneakers

A reference image is a matching image that represents the entity.

A reference is like a double-click into part of the image. It gives the model grounding evidence.

Rule:

- Entity = noun.
- Reference = representation of the same noun.

Actions are not entities. Tag the thing, not the motion.

## Good Reference Images

A strong reference:

- clearly focuses on a single entity;
- avoids clutter and multiple possible matches;
- is cropped or product-style when possible;
- matches the exact product, person, place, or style when identifiable;
- is visually clear enough to compare.

Bad references:

- busy lifestyle image with multiple possible entities;
- generic item when exact model/brand is visible;
- low-quality or unclear image;
- image where the entity is tiny or obscured;
- reference that contains many similar objects.

## Specificity Standard

If exact identity is visible, use exact identity.

Examples:

- If shoes are visibly Cole Haan but exact style is unclear, do not invent the style. Use the closest supportable reference at the right level.
- If exact brand/model is visible, find that exact product.
- If only the category is visible, use a category-level reference.

Do not tag only items whose brand you know. Tag all visible entities.

## Annotation Examples

For a person walking with backpack, blazer, jeans, luggage case, and shoes, tag at least:

- person
- blazer
- jeans
- backpack
- luggage case
- shoes

If more visible entities exist, tag them too.

## Search/Reference Guidance

When finding references:

- Use reverse image search if needed.
- Use familiar visual cues first.
- Prefer official product pages or clean product images for products/clothing.
- For locations, choose images with matching signage or architecture.
- For animals, choose references matching the individual only when individual identity is visible; otherwise species/breed/category can be enough depending task.

## Common Mistakes

- Tagging only the main subject.
- Missing clothing or accessories in plain view.
- Using one group photo as a reference for several entities.
- Using a cluttered reference when a clean product image exists.
- Failing to tag visible text or signage.
- Treating an action as an entity.
- Using a generic reference when the exact product is identifiable.

## Final Checklist

- All visible entities scanned.
- At least four complete annotations where possible.
- Each annotation has one reference image.
- Each reference isolates the entity.
- The specificity level matches what is visible.
- No visible entity was skipped just because it was hard.
