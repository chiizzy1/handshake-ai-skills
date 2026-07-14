---
name: handshake-ud-caption-evaluator
description: Evaluate Handshake UD Caption ELO tasks. Use when an original reference image is compared against two response pairs where each pair includes a generated image and the caption used to generate it, and the task asks for Overall Match, Image Details, Caption Details, Image Hallucination, or Caption Hallucination.
---

# Handshake UD Caption Evaluator

## Core Rule

Use the UD Caption ELO PDFs as the source of truth:

- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-1.pdf`
- `HANDSHAKE-AI/pdfs/handshake-ai-UD Caption Elo Task example-intermidiate.pdf`
- `HANDSHAKE-AI/guidelines.md` section `UD Caption Elo Task`

Before rating a live task, read `references/rubric.md`.

## Workflow

1. Study the original image first.
2. Write a compact original fact ledger before reading response captions or other agents' opinions.
3. Identify the key visual facts: object count by type/color, layout, labels/text, colors, geometry, style, background, and important small details.
4. Read Response A caption and inspect Response A image.
5. Read Response B caption and inspect Response B image.
6. Rate the five criteria independently:
   - Overall Match
   - Image Details
   - Caption Details
   - Image Hallucination
   - Caption Hallucination
7. Do not let a good image rescue a bad caption, or a good caption rescue a bad image.

## Mandatory Original Fact Ledger

Before rating, write down the original image facts from the original image only. Do this before reading or trusting response captions, prior ratings, or another agent's explanation.

For diagrams and structured images, explicitly record:

- main object count by type/color;
- panel titles and layout;
- grid/table dimensions when visible;
- axis/label text and directions;
- object positions and relationships;
- whether repeated panels, such as initial/final views, are visually identical.

If a response caption, generated image, prior rating, or another agent claims a fact that conflicts with this ledger, trust the original image and call out the conflict. Never adopt another agent's premise without re-checking it against the original.

## Hard Gates

- Do not judge the generated images before studying the original.
- Do not rate a structured diagram until the original object count and layout have been recorded.
- Do not reward a caption for being long if it adds unverifiable details.
- Do not reward a generated image for polish when it changes the original layout or content.
- Do not merge image and caption scores. The task asks for both.
- Do not tie hallucination axes when one side invents a visible object, label, date, measurement, or technical detail.

## Key Principle

This is a fidelity task. Polished, photorealistic, or detailed output is not automatically better. The winner is the response that more faithfully captures the original.

## Justification Style

Write justifications in simple, natural sentences. Avoid colon characters and em dashes in the justification prose. Do not write like an English professor. Name the main visual difference, keep it brief, and move on.

Prefer a short two sentence explanation over a polished paragraph.

Avoid this style because it is too long:

`Response A is better because it keeps the page layout closer to the original. The two problems stay in the same order, the answer choices are preserved, and the text block still feels like the same cropped document page. Response B looks cleaner, but it changes the formatting more by splitting the variables into neat separate lines and adding sidebar details that do not match the original crop as well. Its caption also describes those extra sidebar details too confidently, while A stays closer to what is actually visible.`

Write more like this:

`Response A is better because it is closer to the same cropped document page with Problems 113 and 111 in the right order. Response B looks cleaner, but it changes the formatting more and adds sidebar details that are not as faithful to the original.`

## Output Format

**CRITICAL RULE**: Never modify the user's task or markdown files directly. Instead, present your answers and ratings in a clean markdown format directly in the chat using the exact template below.

```markdown
### Input Analysis
[Explain the meaning of what the input image asks for. Establish the objective visual facts, layouts, counts, and text from the original image.]

### Response Analysis
[Analyze Response A's image and caption, pointing out strengths and weaknesses compared to the original facts.]
[Analyze Response B's image and caption, pointing out strengths and weaknesses compared to the original facts.]

### Final Ratings
- Overall Match: [Response A / Response B / Both Good / Both Bad]
- Image Details: [Response A / Response B / Both Good / Both Bad]
- Caption Details: [Response A / Response B / Both Good / Both Bad]
- Image Hallucination: [Response A / Response B / Both Good / Both Bad]
- Caption Hallucination: [Response A / Response B / Both Good / Both Bad]

### Justification
[Provide a brief, natural-language explanation of why you chose these ratings based on your analysis above.]
```


## Final Checklist

- Original image was studied before responses.
- Image and caption were judged separately.
- Fine details and labels were checked.
- Hallucination was checked for both image and caption.
- Ties were avoided unless genuinely indistinguishable.
