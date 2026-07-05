# Cross-Modal Anchoring

Use this reference for onboarding questions and rows about Audio Anchored Visual Retrieval or Visual Anchored Audio Retrieval. Read the source queue file for exact details before final judgment.

## Audio Anchored Visual Retrieval

Pattern: spoken phrase anchors the moment; answer is a visual identity, object, action, attribute, or state.

Valid only when:

- The spoken anchor is quoted verbatim and occurs once.
- The visual answer is within 3 seconds before, during, or after the phrase.
- The answer is visual, not spoken words.
- The visual answer is not visible throughout the clip.
- The row fails the mute test and the audio-only test.
- There is a plausible visual distractor, ideally same category and nearby.

Common invalid cases:

- Asking what was said after the phrase: transcript retrieval, wrong queue.
- Paraphrasing or cleaning up the spoken anchor.
- Reusing a phrase that occurs multiple times.
- Asking for a visual fact visible the whole time.
- Using the only visible candidate, with no distractor.

## Visual Anchored Audio Retrieval

Pattern: silent visible action anchors the moment; answer is the spoken line near it.

Valid only when:

- The visual anchor is visible, distinctive, one-time, and silent.
- The spoken answer is within 3 seconds before, during, or after the visual cue.
- The answer is quoted verbatim, not paraphrased.
- The answer is speech, not a non-speech sound.
- The row fails the mute test and the audio-only test.
- There is a plausible audio distractor, such as another nearby line.

Common invalid cases:

- Using a clap, knock, bell, whistle, or applause as the visual anchor; audio-only can locate it.
- Asking what the visible action is; that makes the anchor the answer.
- Asking for text or visual details near the gesture; wrong answer modality.
- Having only one spoken line in the clip; audio alone gives the answer.

## Natural Assessment Explanations

For write-in assessment items, be plain:

```text
Invalid. The spoon is visible the whole time, so the phrase is not needed. I would fix it by asking about a visual detail that changes right around that line.
```

```text
Invalid. The clap makes a sound, so audio-only can find the moment. Use a silent cue instead, like raising a hand or turning to the screen.
```
