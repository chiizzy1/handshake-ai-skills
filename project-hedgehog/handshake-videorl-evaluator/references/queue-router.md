# VideoRL Queue Router

Use this file before choosing a VideoRL rubric. After routing, read the matching reference file.

## Source Paths

No VideoRL guideline or assessment files exist under `HANDSHAKE-AI/` at time of writing. **If source files are unavailable, the three reference files in this skill folder are operative:**

- `queue-router.md` (this file) — queue identification.
- `cross-modal-anchoring.md` — the cross-modal queues.
- `long-context-videorl.md` — the long-context queues.

If VideoRL guideline or assessment files are later added to the workspace, they outrank these reference files. Search the workspace by queue title rather than assuming a fixed path.

## Queue Map

### Cross-Modal Anchoring

Use `cross-modal-anchoring.md`. If a workspace guideline file for the queue exists, read it too.

- Audio Anchored Visual Retrieval: spoken phrase -> visual answer.
  - If a workspace guideline file exists, match the title "Audio Anchored Visual Retrieval".
- Visual Anchored Audio Retrieval: silent visible action -> spoken answer.
  - If a workspace guideline file exists, match the title "Visual Anchored Audio Retrieval".
- Tracked AV Counting: visible people who speak in a bounded window, answer `X out of Y`.
  - If a workspace guideline file exists, match the title "Tracked AV Counting Queue".
- Audio-Visual Event Alignment: audio cue tied to visible action.
  - If a workspace guideline file exists, match the title "Audio-Visual - Event Alignment".
- Audio-Visual Sound Source Identification: heard sound/line -> visible source.
  - If a workspace guideline file exists, match the title "Audio-Visual - Sound Source Identification".
- Paralinguistic Understanding: how speech/vocalization sounds, not what is said.
  - If a workspace guideline file exists, match the title "Paralinguistic Understanding".

### Long Context VideoRL

Use `long-context-videorl.md`. If a workspace guideline file for the queue exists, read it too.

- Exact Temporal Order - Consequence: shuffled 6-10 events, numeric order.
  - If a workspace guideline file exists, match the section "Exact Temporal Order - Consequence (Long Video)".
- Exact Temporal Order - Repeated Events: one candidate number repeats in the answer.
  - If a workspace guideline file exists, match the title "Exact Temporal Order - Repeated Events (Long Video)".
- Sparse Long-Video Retrieval: late short fact in a distractor-rich video.
  - If a workspace guideline file exists, match the title "Sparse Long-Video Retrieval".
- Long Trace-Grounded Counting: integer count over a bounded span with occurrence trace.
  - If a workspace guideline file exists, match the title "Long Trace-Grounded Counting".
- OCR Extraction / Frame-Following Dynamic Text: exact visible text after an event or chain.
  - If a workspace guideline file exists, match the title "OCR Extraction -- Frame-Following Dynamic Text".
- Short Spatial State-Change / Physical Outcome: setup -> action -> outcome.
  - If a workspace guideline file exists, match the title "Short Spatial State-Change or Physical Outcome".
- Science & Technical Visual Reasoning: visible evidence plus domain rule.
  - If a workspace guideline file exists, match the title "Science & Technical Visual Reasoning".
- Action Anticipation & Prediction: predict immediate next action before it begins.
  - If a workspace guideline file exists, match the title "Action Anticipation & Prediction".
- Temporal Order - Fine-Grained: 4-6 subtle events, often within a scene.
  - If a workspace guideline file exists, match the title "Temporal Order - Fine-Grained".
- Temporal Ordering - How-To: 4-6 tutorial/procedure events, audio-required when marked.
  - If a workspace guideline file exists, match the title "Temporal Ordering - How-To".

## If A File Name Does Not Match

Some source filenames use em dashes or other unicode punctuation. Never rely on an exact literal path: list the candidate directory and choose the entry whose title matches the queue. If nothing matches, use this skill's reference files and say the source file was unavailable.
