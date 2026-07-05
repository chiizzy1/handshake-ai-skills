# VideoRL Queue Router

Use this file before choosing a VideoRL rubric. After routing, read the matching source file.

## Source Paths

- Main guide: `HANDSHAKE-AI/pdfs/VideoRL--Cross-Modal Anchoring Guidelines.md`
- Supporting queue files: `HANDSHAKE-AI/pdfs/Video RL/`
- Cross-modal assessment: `HANDSHAKE-AI/Assessments/VideoRL--Cross-Modal Anchoring Assessment.md`
- Long-context assessment: `HANDSHAKE-AI/Assessments/Long Context VideoRL Onboarding assessment .md`

## Queue Map

### Cross-Modal Anchoring

Use `references/cross-modal-anchoring.md`, then read the matching supporting file.

- Audio Anchored Visual Retrieval: spoken phrase -> visual answer.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Audio Anchored Visual Retrieval.md`
- Visual Anchored Audio Retrieval: silent visible action -> spoken answer.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Visual Anchored Audio Retrieval.md`
- Tracked AV Counting: visible people who speak in a bounded window, answer `X out of Y`.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Tracked AV Counting Queue.md`
- Audio-Visual Event Alignment: audio cue tied to visible action.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Audio-Visual - Event Alignment.md`
- Audio-Visual Sound Source Identification: heard sound/line -> visible source.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Audio-Visual - Sound Source Identification.md`
- Paralinguistic Understanding: how speech/vocalization sounds, not what is said.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Paralinguistic Understanding.md`

### Long Context VideoRL

Use `references/long-context-videorl.md`, then read the matching supporting file.

- Exact Temporal Order - Consequence: shuffled 6-10 events, numeric order.
  - Source: main guide section `Exact Temporal Order - Consequence (Long Video)`
- Exact Temporal Order - Repeated Events: one candidate number repeats in the answer.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Exact Temporal Order - Repeated Events (Long Video).md`
- Sparse Long-Video Retrieval: late short fact in a distractor-rich video.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Sparse Long-Video Retrieval.md`
- Long Trace-Grounded Counting: integer count over a bounded span with occurrence trace.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Long Trace-Grounded Counting.md`
- OCR Extraction / Frame-Following Dynamic Text: exact visible text after an event or chain.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/OCR Extraction -- Frame-Following Dynamic Text.md`
- Short Spatial State-Change / Physical Outcome: setup -> action -> outcome.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Short Spatial State-Change or Physical Outcome.md`
- Science & Technical Visual Reasoning: visible evidence plus domain rule.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Science & Technical Visual Reasoning.md`
- Action Anticipation & Prediction: predict immediate next action before it begins.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Action Anticipation & Prediction.md`
- Temporal Order - Fine-Grained: 4-6 subtle events, often within a scene.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Temporal Order - Fine-Grained.md`
- Temporal Ordering - How-To: 4-6 tutorial/procedure events, audio-required when marked.
  - Source: `HANDSHAKE-AI/pdfs/Video RL/Temporal Ordering - How-To.md`

## If The File Name Uses Unicode Dashes

Some source filenames use em dashes. If a literal path above does not resolve, list `HANDSHAKE-AI/pdfs/Video RL/` and choose the matching title.
