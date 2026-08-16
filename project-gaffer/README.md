# Project Gaffer

Project Gaffer skills for the Handshake AI platform.

Gaffer is a **video captioning production project**, not a rating project. The
worker watches a short video and writes the captions themselves. Quality is
measured by a human audit score after submission, not by picking a label.

## Task Families

- **Video Omni Caption**: Watch a video and write four captions across two
  tracks — Speech Transcription, Speech Characteristics, Visual, and Audio —
  with timestamps and speaker tags, then self-audit before submitting.

## Naming Convention

All Project Gaffer skill folders use the `gaffer-` prefix, to prevent clashes
with Project Hedgehog (`handshake-*`) and Project Lizard (`lizard-*`).

## Source Material

The extracted project site, golden examples, common-error audits, assessment
questions, and per-video frame/audio inspections live outside this repo, in the
read-only task material:

- `HANDSHAKE-AI/project-gaffer/extracted/PROJECT_GAFFER_MASTER_DOC.md`
- `HANDSHAKE-AI/project-gaffer/extracted/MASTER_VIDEO_SPEECH_INSPECTION_REPORT.md`
- `HANDSHAKE-AI/project-gaffer-assessment/questions.md`
