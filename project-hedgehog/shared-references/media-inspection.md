# Inspecting IG Video Media

How to actually look at a Reel before judging it. Shared by every Project Hedgehog IG video skill.

The tool is `handshake-ai-skills/tools/inspect_media.py`. It fetches a Reel from a URL, finds every scene, samples a keyframe per scene, builds a contact sheet, demuxes audio, and transcribes speech with timestamps.

## Contents

- [Why This Exists](#why-this-exists)
- [Quick Start](#quick-start)
- [Reading The Output](#reading-the-output)
- [Zooming To Settle An Identity Call](#zooming-to-settle-an-identity-call)
- [What Each Task Needs](#what-each-task-needs)
- [Degraded Mode](#degraded-mode)
- [Rules](#rules)

## Why This Exists

Two failure modes, both of which have already produced wrong answers on a live assessment.

**Fixed-interval sampling misses short scenes.** A montage Reel can carry a decisive shot under one second long. Sampling every N seconds straddles it and you never see it — you then answer confidently about a clip you did not fully watch. The tool detects scene cuts first and takes one frame per segment, so every shot is represented no matter how brief.

**Padding breaks scene detection.** Portrait Reels are often delivered inside a padded landscape canvas. A bright pad dominates the histogram badly enough that whole-frame cut detection reports **zero cuts** on a video with ten. The tool locates the real picture first and runs detection on that region only.

Both are handled automatically. The point of knowing them is to recognise a bad result: if the scan reports one enormous scene on a video that visibly cuts, or crops away content you can see in the player, something went wrong — do not proceed on those frames.

## Quick Start

```bash
# from the workspace root
python3 handshake-ai-skills/tools/inspect_media.py --check-deps

# whole pipeline from a Reel URL
python3 handshake-ai-skills/tools/inspect_media.py \
  --url https://www.instagram.com/reel/SHORTCODE/ --out /tmp/insp

# local file, visual only — much faster when you do not need audio
python3 handshake-ai-skills/tools/inspect_media.py \
  --video clip.mp4 --out /tmp/insp --no-audio
```

Useful flags:

- `--whisper-model tiny|base|small|medium|large` — `tiny` is quick and adequate for checking whether two clips carry the same lyric; go larger when exact wording matters.
- `--cut-threshold 0.60` — raise it to split more aggressively when a montage uses soft cuts, lower it when camera movement is being mistaken for cuts.
- `--no-transcript` — keep the audio track, skip the speech model.

## Reading The Output

```
out/
  <shortcode>.mp4            the video, if fetched from a URL
  frames/                    one keyframe per scene, plus fixed-ratio backstops
  contact_sheet.jpg          all keyframes with timestamps burned in
  audio.wav                  16 kHz mono PCM
  inspection_summary.json    duration, fps, content box, segments, speech
```

Look at `contact_sheet.jpg` first — it is the whole clip at a glance and it is what stops you answering about a scene you never saw. Then open individual frames from `frames/` for anything that matters.

The scene list printed to the terminal is the important part. **Read every segment before making a breadth judgement** such as "list every entity you would tag."

## Zooming To Settle An Identity Call

Identity questions are usually decided by magnification, not by the keyframe.

```bash
python3 handshake-ai-skills/tools/inspect_media.py --video clip.mp4 --out /tmp/insp \
  --zoom 7.6,230,660,240,240 --scale 6
```

`--zoom t,x,y,w,h` takes a timestamp in seconds and a rectangle in **content-box coordinates** — the same coordinate space as the saved keyframes, so measure directly off a frame in `frames/`.

Use it before dropping a reference on identity. A tiny or occluded target in a keyframe is often perfectly readable at 5-9x, and dropping a real match wastes the tag.

## What Each Task Needs

| Skill | Run this | Because |
|---|---|---|
| `handshake-ig-entity-tagging-video` | full pipeline | Phase 1 needs the whole clip watched and the audio gate answered; identity checks need zoom; frame selection needs every scene |
| `handshake-ig-audio-recreation` | full pipeline on **both** clips | The whole task is audio. Compare transcripts to confirm same song and same segment |
| `handshake-ig-temporal-alignment` | full pipeline on both clips | Transcript timestamps give the shared anchor word and let you measure the offset instead of eyeballing it |
| `handshake-ig-temporal-alignment-review` | full pipeline on both clips | Grading alignment precision means measuring the offset, and the 0.25s / 0.5-0.75s tier boundaries are numbers |
| `handshake-ig-bts` | full pipeline on both clips | The prompt must describe audio sameness or difference; scene lists prove the output stays on one scene |
| `handshake-ig-editing-convo` | full pipeline on both clips | Transcripts confirm the response actually replies, and locate the trim window around the line being reacted to |

For the alignment tasks specifically: the transcript's segment boundaries are also how you check the "never start or end mid-lyric" rule without guessing.

## Degraded Mode

Nothing is mandatory. Each tier degrades on its own and the script says what is missing:

| Tier | Needs | Without it |
|---|---|---|
| Frames, scenes, contact sheet, zoom | `opencv-python` | Nothing works — this one is required |
| Audio demux | `imageio-ffmpeg` or ffmpeg on PATH | No audio, no transcript |
| Transcript | `openai-whisper` | Audio track still extracted, no text |
| URL fetch | `playwright` or `yt-dlp` | Local files only |

Install with `python3 -m pip install --user -r handshake-ai-skills/tools/requirements.txt`, then `python3 -m playwright install chromium`.

Note that ffmpeg is frequently **not** on PATH. The bundled `imageio-ffmpeg` binary covers both the demux and the speech model, so a missing system ffmpeg is not a blocker.

## Rules

- Write output to a scratch directory. **Never write into `HANDSHAKE-AI/`** — task material is read-only input.
- Watch the whole clip before answering any breadth question. The contact sheet is the evidence that you did.
- State what you actually inspected. If a call rests on a frame you could not resolve, say so rather than inferring.
- Do not infer objects you cannot see. A canoe in frame does not license tagging a paddle or a life vest unless they are visible — check the close shots before deciding either way.
- A transcript is evidence about audio, not about the picture. It confirms lyrics and timing; it says nothing about whether a performance was genuinely re-performed.
