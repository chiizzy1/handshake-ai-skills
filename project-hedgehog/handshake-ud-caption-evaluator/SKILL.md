---
name: handshake-ud-caption-evaluator
description: Evaluate Handshake UD Caption ELO tasks. Use when an original reference image is compared against two response pairs where each pair includes a generated image and the caption used to generate it, and the task asks for Overall Match, Image Details, Caption Details, Image Hallucination, or Caption Hallucination.
---

# Handshake UD Caption Evaluator

## File Locations

- `references/...` paths are inside this skill's folder.
- `HANDSHAKE-AI/...` is a sibling folder of this skills repo in the workspace root (e.g. `<workspace>/train-ai/HANDSHAKE-AI/`).
- If a referenced external file cannot be found, use `references/rubric.md` in this skill folder as the operative rubric and state that the source file was unavailable.

## Core Rule

Use the UD Caption ELO PDFs as the source of truth:

- `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-ai-UD Caption Elo Task example-1.pdf`
- `HANDSHAKE-AI/project-hedgehog-pdfs/handshake-ai-UD Caption Elo Task example-intermidiate.pdf`
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

## Open Feedback Style

The task's free-text field is **Open Feedback**, minimum 100 characters. Write 2 to 3 sentences. Not one line, not a paragraph.

**The Persona: someone who actually put the two side by side.**

You are not an AI evaluator or a design critic. You are a careful person who compared both against the original and noticed the thing that decided it. Precise about what you saw, plain about how you say it.

This is a fidelity task, so the details are the point. Do not go so casual that you stop naming counts, labels, and positions. "The axis only goes to 12 instead of 16" is human. "The scaling is off" is vague.

1. **Name the decisive difference first.** One thing lost it. Lead with that.
2. **Use the original's own words.** If the original says "Capitol Police," write "Capitol Police," not "one of the labeled points."
3. **Short sentences. Periods.** No em dashes, no semicolons, no colons in prose.
4. **Avoid absolutes.** Not "perfectly reproduces." Use "keeps," "matches," "stays closer to." A QA reviewer who zooms in should not be able to falsify your sentence.
5. **Use "while" instead of "whereas."** "Whereas" sounds formal. "While" sounds like a person.
6. **No checklists.** Two concrete details beat six. Listing every axis reads as a rubric recital.
7. **Neutral.** No "wildly wrong," "bizarre," or "a mess." State what differs.
8. **Say "adds" or "invents," not "fabricates."** Plain verb, same meaning.

**Banned phrases:** "Upon review of," "demonstrates superior," "holistic," "semantic fidelity," "faithfully renders," "captures the essence," "notably," "it is evident that," "fails the criterion."

> **Keep these words.** "Hallucination," "hallucinates," "invents," "adds," "misses." Two of the five axes are named Image Hallucination and Caption Hallucination, so you need that vocabulary to name what you rated.

For worked examples and the four recurring comment patterns, read the Comment Style section in `references/rubric.md`.

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

### Open Feedback
[2 to 3 sentences, minimum 100 characters, following Open Feedback Style above. This is the text that goes in the task's Open Feedback box.]
```

## Final Checklist

- Original image was studied before responses.
- Image and caption were judged separately.
- Fine details and labels were checked.
- Hallucination was checked for both image and caption.
- Both Good and Both Bad were used only when the criterion is genuinely indistinguishable.
- Open Feedback is 2 to 3 sentences, at least 100 characters, and names the decisive difference rather than every axis.
- Open Feedback uses no colons, em dashes, or banned phrases, and avoids absolutes like "perfect."
