# Inspecting the Video Before You Write

You cannot caption a video by watching it once in your head. Run the inspector
first. It gives you the cut times, a frame per shot, isolated audio, a draft
transcript, the silent windows, and the loud non-speech moments.

## Contents

- [Running It](#running-it)
- [What You Get](#what-you-get)
- [Reading the Report](#reading-the-report)
- [How Good Is the Cut Detection](#how-good-is-the-cut-detection)
- [What It Cannot Do](#what-it-cannot-do)
- [Tuning](#tuning)
- [When a Stage Fails](#when-a-stage-fails)

## Running It

```bash
GP=~/.venvs/gaffer-tools/bin/python      # see Setup below

$GP ../scripts/gaffer_inspect.py --check-deps

$GP ../scripts/gaffer_inspect.py "https://www.youtube.com/watch?v=VIDEO_ID" \
    --out /tmp/gaffer
```

It takes a YouTube URL, a bare 11-character video ID, or a local file path. Pass
`--out` pointing somewhere scratch. **Never write into `HANDSHAKE-AI/`** — task
material is read-only.

Plain `python3` works too, as long as `--check-deps` passes on it. The dedicated
environment exists for one reason: yt-dlp dropped Python 3.9 after 2025.10.14,
macOS ships 3.9, and YouTube extraction breaks often enough that being pinned to
an old yt-dlp will eventually cost you downloads.

### Setup

Full instructions are in `../scripts/requirements.txt`. The short version, which
needs no sudo:

```bash
python3 -m pip install --user uv
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
uv python install 3.13
uv venv ~/.venvs/gaffer-tools --python 3.13
uv pip install --python ~/.venvs/gaffer-tools/bin/python -r ../scripts/requirements.txt
```

Downloads come back at up to 1080p by default. That matters more than it sounds:
on a 360p frame a news lower third is about 30 pixels tall, which is not enough
to tell an apostrophe from a compression artefact — and this project fails tasks
over exactly that. Use `--max-height` to trade resolution for processing speed.

**Read on-screen text in the task player when you can.** The frames are for
timing and for detail you cannot pause on. If a banner is still unclear at full
resolution, say it is illegible rather than guessing — that is the correct answer
here, not a cop-out.

Only ffmpeg is genuinely required. Install the rest with:

```bash
python3 -m pip install --user -r ../scripts/requirements.txt
```

A 27-second clip takes about 11 seconds end to end including transcription.
Longer videos are dominated by Whisper; use `--no-asr` for a quick look at the
shots, then run again in full.

## What You Get

Under `<out>/<slug>/`:

| File | What it is |
|---|---|
| `INSPECTION.md` | The report. Read this first. |
| `inspection.json` | Same data, machine-readable. |
| `frames/` | One JPEG per shot, plus interval frames in long shots and one per possible transition. |
| `audio.wav` | 16 kHz mono. Listen to this, not the video. |
| `video.mp4` | Only when it was downloaded. |

Frame names carry their own timestamps: `shot004_t0025.76s.jpg` is shot 4 at
25.76 seconds. A `_i` suffix means an interval frame inside a long shot, `_t`
means a possible transition.

## Reading the Report

**Pre-Flight Checks** — length against the 10-minute skip rule, whether there is
an audio stream, how much of the runtime is speech, and the shot count. If it
warns about a possible data-sparse skip, watch the video before deciding.

**Shot List** — every detected hard cut, with its score and frames. This is your
starting set of Visual+Audio segment boundaries. Check each one against its
frame; a detector can fire on a camera flash.

**Possible Transitions** — everything that scored below the hard-cut threshold.
Real boundaries hide here in sports and continuous action. Look at every frame in
this table.

**Draft Speech Transcript** — Whisper output with timestamps. A draft, never the
transcript. Segments marked ⚠️ are ones Whisper itself doubts; those are often
`((unintelligible))`.

**No-Speech Windows** — gaps between transcribed speech, each marked with whether
audio is still playing. These are your `((No speech present))` candidates. Where
sound is still present, the Speech captions get the tag **and** the Audio caption
still describes what is playing.

**Loud Non-Speech Moments** — moments markedly louder than the seconds around
them. Whistles, bat impacts, applause, stingers. A starting list for the Audio
caption.

## How Good Is the Cut Detection

Three detectors run. Frame-to-frame scene scoring finds hard cuts. A one-second
lag comparison finds dissolves and fades. `blackdetect` finds black stretches.
Measured against the golden examples, whose true boundaries are known:

**Hard-cut content — near exact.** On the cooking show promo it found 22 hard
cuts. The audited task has 22 Visual+Audio segments. They line up.

**Dissolve-heavy content — good, within about half a second.** On the on-screen
text promo, frame-to-frame scoring found **zero** cuts, because every transition
is a dissolve. The gradual scan recovered five of the six real boundaries — 5.3,
11.4, 17.2, 29.9 and 35.7 against a truth of 5.3, 11.4, 17.4, 29.4 and 35.6 — and
flagged three more real events the audited caption describes, at 23.3, 32.4 and
37.9. Gradual times are approximate. Check the frame.

**Continuous action — partial, by design.** On the rugby clip it found 4 hard
cuts, and the soft tier caught 1.3, 9.6, 19.1 and 26.2 against a truth of 1.4,
9.6, 19.0 and 26.7. Two real boundaries at 6.5 and 12.5 appear in no table —
there is no visual discontinuity at those points, because the camera simply keeps
following play. **Nothing will find those for you.** That is what the interval
frames are for.

**Silence detection — accurate.** On the live cricket clip the no-speech windows
came out as 0.00–4.72 and 15.58–27.08. The audited task uses 0.0–4.6 and
15.9–27.1.

**Loudness — useful, not complete.** On the same clip it flagged 19.50 at +10.8
dB over baseline. The audited Audio caption reads "At [19.5] the bat striking the
ball can be heard."

## What It Cannot Do

Know these before you trust it.

- **It does not read on-screen text.** There is no OCR. You read the text off the
  frames yourself, exactly as shown, typos included. The task player is the better
  source when you have it; the frames are for timing and for detail you cannot
  pause on.
- **It cannot hear sounds underneath speech.** The voice dominates the level, so
  a whistle blown while the commentator talks never reaches the loud-moments
  table. That is exactly the failure in common error #5. Listen through the
  speech.
- **It does not identify speakers.** Whisper gives you text, not who said it.
  Merged speakers are a graded error, so listen for voice changes across every
  segment boundary yourself.
- **It misses boundaries with no visual change.** See above.
- **Whisper mishears.** Names, jargon and accents come out wrong, and it
  sometimes repeats a line several times. "A pure wit gun" failed a real task.
  Every word you submit must be a word you heard.

The report exists to stop you missing things. It is not a caption, and nothing in
it can be pasted into a task.

## Tuning

| Flag | Default | Use when |
|---|---|---|
| `--scene-threshold` | 0.30 | Lower it if obvious cuts are being missed; raise it if flashes create fake shots. |
| `--soft-threshold` | 0.10 | Lower it for sports and continuous action to surface more candidates. |
| `--no-gradual` | off | Skip the dissolve scan. It decodes the whole video, so it is the slow part on long clips. |
| `--max-height` | 1080 | Drop to 720 or 480 to speed up a long video. Only do it when the video has no small on-screen text. |
| `--min-shot` | 0.35 | Raise it if one cut is being reported several times. |
| `--interval` | 2.5 | Lower it for busy footage inside long takes. |
| `--whisper-model` | `small` | `medium` or `large-v3` for accents, names and crosstalk. Slower. |
| `--no-asr` | off | A fast first pass when you only want the shot list. |
| `--max-frames` | 600 | Raise for long, dense videos. The interval widens automatically instead of exceeding it. |

Do not use `tiny` or `base`. The project's own extracted corpus was built with
`base`, and it turned a player's name into "Boatek Van the San Shul" and repeated
one commentary line six times.

## When a Stage Fails

Every stage degrades on its own and records what happened under **Stages Skipped
or Degraded** in the report. Missing yt-dlp only affects URLs. Missing Whisper
still leaves you shots, frames and silence windows.

Read that section every run. If a stage was skipped, you did not verify what it
would have verified, and your self-audit must say so rather than claiming the
check. Run `--check-deps` to see what is installed.
