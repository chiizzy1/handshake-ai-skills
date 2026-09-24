#!/usr/bin/env python3
"""
Project Gaffer video inspector.

Turns one video — a YouTube URL, a bare video ID, or a local file — into the
evidence needed to caption it: a shot list with detected cut times, a frame for
every shot, an isolated audio track, a timestamped draft transcript, the windows
where nobody speaks, and the loud non-speech moments that are easy to miss.

Writes nothing into task material. Everything lands under --out.

    python3 gaffer_inspect.py --check-deps
    python3 gaffer_inspect.py "https://www.youtube.com/watch?v=CuFvCGSXOa8" --out /tmp/gaffer
    python3 gaffer_inspect.py clip.mp4 --out /tmp/gaffer --whisper-model medium

Cuts are reported in two tiers. Hard cuts pass --scene-threshold and become the
shot list. Anything between --soft-threshold and that value is listed separately
as a possible transition: dissolves, whip pans and camera moves inside
continuous action score low, and a single threshold either misses them or floods
the list with noise.

Every stage degrades on its own. Missing stages are recorded in the report so
nothing is silently absent.

Outputs, under <out>/<slug>/:

    INSPECTION.md          read this first
    inspection.json        same data, machine-readable
    frames/                one JPEG per shot, plus interval and transition frames
    audio.wav              16 kHz mono PCM
    video.mp4              only when downloaded
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------- defaults

SCENE_THRESHOLD = 0.30      # scene score at or above this is a hard cut
SOFT_THRESHOLD = 0.10       # between the two: a possible transition, flagged only
MIN_SHOT_SECONDS = 0.35     # cuts closer than this are one cut, strongest wins
CUT_SETTLE = 0.12           # grab a shot's frame this far after its cut
INTERVAL_IN_SHOT = 2.5      # extra frames inside any shot longer than this
MAX_FRAMES = 600            # cap; the interval widens rather than exploding
SILENCE_DB = -30            # silencedetect noise floor
SILENCE_MIN = 0.30          # shortest silence worth reporting
RMS_WINDOW = 0.5            # seconds per loudness sample
EVENT_MARGIN_DB = 4.0       # dB above the local baseline that counts as an event
EVENT_HALF_WIDTH = 5.0      # seconds either side that form the local baseline
WHISPER_MODEL = "small"     # base mangles names badly; small is the floor
LONG_TASK_SECONDS = 600     # Gaffer skips videos over 10 minutes


# ---------------------------------------------------------------- binaries

def find_ffmpeg() -> str | None:
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return shutil.which("ffmpeg")


def find_ffprobe() -> str | None:
    exe = shutil.which("ffprobe")
    if exe:
        return exe
    ff = find_ffmpeg()
    if ff:
        cand = Path(ff).parent / "ffprobe"
        if cand.exists():
            return str(cand)
    return None


FFMPEG = find_ffmpeg()
FFPROBE = find_ffprobe()


def run(cmd: list[str], timeout: int = 3600) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True,
                          errors="replace", timeout=timeout)


def median(values: list[float]) -> float:
    ordered = sorted(values)
    n = len(ordered)
    if not n:
        return 0.0
    mid = n // 2
    return ordered[mid] if n % 2 else (ordered[mid - 1] + ordered[mid]) / 2.0


# ---------------------------------------------------------------- input

YT_PATTERN = (r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/"
              r"|youtube\.com/shorts/)([A-Za-z0-9_-]{11})")
# android_vr is first on purpose. The other clients that still work at all
# expose only the 360p progressive stream, and a lower third on a 360p frame is
# about 30 pixels tall — not enough to tell an apostrophe from a compression
# artefact, which is exactly the call this project grades. android_vr exposes the
# adaptive streams, so the same video arrives at 1080p.
PLAYER_CLIENTS = [["android_vr"], ["android"], ["mweb"], ["tv"], ["web_creator"], ["web"]]
MAX_HEIGHT = 1080
MIN_HEIGHT = 480          # below this, on-screen text stops being reliably legible


def parse_video_id(source: str) -> str | None:
    m = re.search(YT_PATTERN, source)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", source):
        return source
    return None


def slugify(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_-]+", "_", text).strip("_")
    return s[:60] or "video"


def quick_height(path: Path) -> int:
    """Pixel height of a file, cheaply. 0 when it cannot be read."""
    try:
        import cv2
        cap = cv2.VideoCapture(str(path))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
        cap.release()
        if h:
            return h
    except Exception:
        pass
    if FFMPEG:  # header only, no decoding
        cp = run([FFMPEG, "-hide_banner", "-i", str(path)], timeout=60)
        m = re.search(r"Video:.*?,\s*(\d+)x(\d+)", cp.stderr)
        if m:
            return int(m.group(2))
    return 0


def download(video_id: str, dest_dir: Path, notes: list[str],
             max_height: int = MAX_HEIGHT, min_height: int = MIN_HEIGHT,
             force: bool = False) -> tuple[Path | None, str | None]:
    """Fetch a YouTube video, trying player clients until one is good enough.

    Returns (path, client_used).

    A client that merely succeeds is not enough. YouTube bot-checks clients
    unpredictably under load, and the ones that survive are often the ones
    serving only a 360p progressive stream — on which small on-screen text is
    unreadable. So a result below min_height is kept as a fallback while the
    remaining clients are tried, and the tallest is used if none clears the bar.
    """
    try:
        import yt_dlp
    except ImportError:
        notes.append("yt-dlp is not installed, so the URL could not be fetched. "
                     "Install it with: pip install yt-dlp")
        return None, None

    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / "video.mp4"
    if target.exists() and target.stat().st_size > 10_000:
        if not force:
            print(f"[=] Already downloaded: {target} "
                  f"({quick_height(target)}p) — pass --force-download to refetch")
            return target, "cached"
        target.unlink()

    url = f"https://www.youtube.com/watch?v={video_id}"
    stash = dest_dir / "_candidate.mp4"
    best: tuple[int, str] | None = None   # (height, client)
    fmt = (f"bestvideo[height<={max_height}][ext=mp4]+bestaudio[ext=m4a]/"
           f"bestvideo[height<={max_height}]+bestaudio/"
           f"best[height<={max_height}][ext=mp4]/best[ext=mp4]/best")
    for client in PLAYER_CLIENTS:
        opts = {
            "outtmpl": str(dest_dir / "video.%(ext)s"),
            "format": fmt,
            "merge_output_format": "mp4",
            "extractor_args": {"youtube": {"player_client": client}},
            "quiet": True,
            "no_warnings": True,
        }
        if FFMPEG:
            opts["ffmpeg_location"] = FFMPEG
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception:
            continue
        got = target if target.exists() else next(iter(dest_dir.glob("video.*")), None)
        if not (got and got.stat().st_size > 10_000):
            continue
        if got != target:
            got.rename(target)
        height = quick_height(target)

        if height >= min_height:
            print(f"[+] Downloaded with client {client[0]}: {height}p, "
                  f"{target.stat().st_size / 1_048_576:.1f} MB")
            stash.unlink(missing_ok=True)
            return target, client[0]

        # Not good enough. Keep the tallest so far and try the rest.
        print(f"[-] Client {client[0]} gave only {height}p, trying others")
        if best is None or height > best[0]:
            target.replace(stash)
            best = (height, client[0])
        else:
            target.unlink(missing_ok=True)

    if best:
        stash.replace(target)
        notes.append(
            f"No player client cleared {min_height}p — the best available was "
            f"{best[0]}p via {best[1]}. YouTube bot-checks clients under load, and "
            "the survivors often serve only the 360p stream. Re-running later with "
            "--force-download frequently gets a higher resolution.")
        print(f"[+] Best available: {best[0]}p via {best[1]}")
        return target, best[1]

    notes.append(f"Every yt-dlp player client failed for {video_id}. The video may be "
                 "private, removed, region-locked, or you are being rate limited. "
                 "Wait a few minutes and retry, or download it by hand and pass the "
                 "local path instead.")
    return None, None


# ---------------------------------------------------------------- probe

def probe(video: Path) -> dict:
    info = {"duration": 0.0, "container_duration": 0.0, "fps": 0.0,
            "width": 0, "height": 0, "has_audio": False}
    if FFPROBE:
        cp = run([FFPROBE, "-v", "error", "-print_format", "json",
                  "-show_format", "-show_streams", str(video)], timeout=120)
        if cp.returncode == 0:
            try:
                data = json.loads(cp.stdout)
            except json.JSONDecodeError:
                data = {}
            info["duration"] = float(data.get("format", {}).get("duration") or 0.0)
            info["container_duration"] = info["duration"]
            for st in data.get("streams", []):
                if st.get("codec_type") == "video" and not info["width"]:
                    info["width"] = int(st.get("width") or 0)
                    info["height"] = int(st.get("height") or 0)
                    rate = st.get("avg_frame_rate") or st.get("r_frame_rate") or "0/1"
                    try:
                        num, _, den = rate.partition("/")
                        info["fps"] = float(num) / float(den or 1)
                    except (ValueError, ZeroDivisionError):
                        pass
                elif st.get("codec_type") == "audio":
                    info["has_audio"] = True
            if info["duration"]:
                return info

    try:  # OpenCV fallback when ffprobe is unavailable
        import cv2
        cap = cv2.VideoCapture(str(video))
        fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        info["fps"] = fps
        info["width"] = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
        info["height"] = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
        info["duration"] = frames / fps if fps else 0.0
        cap.release()
    except Exception:
        pass

    if FFMPEG and (not info["has_audio"] or not info["container_duration"]):
        # No output file, so ffmpeg prints the stream table and exits. Adding
        # "-f null -" here would decode the entire video just to answer "is there
        # an audio stream", which on a ten-minute clip is most of the runtime.
        cp = run([FFMPEG, "-hide_banner", "-i", str(video)], timeout=60)
        if not info["has_audio"]:
            info["has_audio"] = "Audio:" in cp.stderr
        m = re.search(r"Duration:\s*(\d+):(\d\d):(\d\d(?:\.\d+)?)", cp.stderr)
        if m:
            info["container_duration"] = (
                int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
            )

    # The container duration is what the task is graded against. Frame-count /
    # fps can land a tenth of a second short, which fails the "last row ends at
    # the video end" check, so prefer the container value whenever we have it.
    if info["container_duration"]:
        info["duration"] = info["container_duration"]
    return info


# ---------------------------------------------------------------- cuts

def score_frames_ffmpeg(video: Path, floor: float) -> list[dict] | None:
    """Every frame whose scene score clears `floor`, as [{t, score}]."""
    if not FFMPEG:
        return None
    cp = run([FFMPEG, "-hide_banner", "-nostats", "-i", str(video),
              "-filter:v", f"select='gt(scene,{floor})',metadata=print:file=-",
              "-an", "-f", "null", "-"])
    if cp.returncode != 0 and "pts_time" not in cp.stdout:
        return None

    hits, pending = [], None
    for line in cp.stdout.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            pending = float(m.group(1))
            continue
        m = re.search(r"lavfi\.scene_score=([0-9.]+)", line)
        if m and pending is not None:
            hits.append({"t": round(pending, 3), "score": round(float(m.group(1)), 3)})
            pending = None
    return hits


def score_frames_opencv(video: Path, floor: float) -> list[dict] | None:
    """Histogram-correlation fallback. Coarser, and the scores are not
    interchangeable with ffmpeg's, but it finds hard cuts."""
    try:
        import cv2
    except ImportError:
        return None
    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    step = max(1, int(fps / 8))
    hits, prev, idx = [], None, 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            small = cv2.resize(frame, (160, 90))
            hist = cv2.calcHist([small], [0, 1, 2], None, [8, 8, 8], [0, 256] * 3)
            cv2.normalize(hist, hist)
            if prev is not None:
                diff = 1.0 - cv2.compareHist(prev, hist, cv2.HISTCMP_CORREL)
                if diff > floor:
                    hits.append({"t": round(idx / fps, 3), "score": round(diff, 3)})
            prev = hist
        idx += 1
    cap.release()
    return hits


def detect_gradual(video: Path, lag: float = 1.0, threshold: float = 0.25,
                   sample_fps: float = 4.0) -> list[dict] | None:
    """Dissolves and fades, which frame-to-frame scene scoring cannot see.

    A one-second dissolve changes little between neighbouring frames, so its
    scene score stays low. Comparing each frame against the frame a second
    earlier makes the same transition obvious. The peak lands mid-dissolve, so
    the reported time is pulled back by half the lag.
    """
    try:
        import cv2
    except ImportError:
        return None

    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    step = max(1, int(round(fps / sample_fps)))
    hists, times, idx = [], [], 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            small = cv2.resize(frame, (160, 90))
            hist = cv2.calcHist([small], [0, 1, 2], None, [8, 8, 8], [0, 256] * 3)
            cv2.normalize(hist, hist)
            hists.append(hist)
            times.append(idx / fps)
        idx += 1
    cap.release()

    span = max(1, int(round(lag * sample_fps)))
    if len(hists) <= span + 2:
        return []
    diffs = [(times[i], 1.0 - cv2.compareHist(hists[i - span], hists[i],
                                              cv2.HISTCMP_CORREL))
             for i in range(span, len(hists))]

    peaks = []
    for i in range(1, len(diffs) - 1):
        t, v = diffs[i]
        if v >= threshold and v >= diffs[i - 1][1] and v >= diffs[i + 1][1]:
            peaks.append({"t": round(max(0.0, t - lag / 2.0), 2),
                          "score": round(min(v, 0.999), 3)})
    return peaks


def detect_fades(video: Path) -> list[dict]:
    """Black stretches, which usually mean a fade or a hard scene break."""
    if not FFMPEG:
        return []
    cp = run([FFMPEG, "-hide_banner", "-nostats", "-i", str(video),
              "-vf", "blackdetect=d=0.10:pic_th=0.98:pix_th=0.10",
              "-an", "-f", "null", "-"])
    return [{"start": round(float(m.group(1)), 2), "end": round(float(m.group(2)), 2)}
            for m in re.finditer(r"black_start:([0-9.]+)\s+black_end:([0-9.]+)",
                                 cp.stderr)]


def cluster(hits: list[dict], min_gap: float) -> list[dict]:
    """Collapse hits closer than min_gap, keeping the strongest of each cluster.

    Flashes, camera pops and fast pans fire the detector several frames running.
    A real shot is not 0.1s long, so a cluster is one boundary.
    """
    if not hits:
        return []
    ordered = sorted(hits, key=lambda c: c["t"])
    kept = [dict(ordered[0])]
    for hit in ordered[1:]:
        if hit["t"] - kept[-1]["t"] < min_gap:
            if hit["score"] > kept[-1]["score"]:
                kept[-1] = dict(hit)
        else:
            kept.append(dict(hit))
    return kept


def split_tiers(hits: list[dict], gradual: list[dict], hard: float,
                min_gap: float) -> tuple[list[dict], list[dict]]:
    """Hard cuts drive the shot list; soft ones are only flagged for checking.

    Gradual hits never promote to hard. A dissolve is a real boundary but its
    timing is approximate, so it stays something to check rather than something
    to build segments on.
    """
    hard_cuts = cluster([h for h in hits if h["score"] >= hard], min_gap)
    soft = [{**s, "method": "scene"}
            for s in cluster([h for h in hits if h["score"] < hard], min_gap)
            if all(abs(s["t"] - h["t"]) >= min_gap for h in hard_cuts)]

    keep_out = hard_cuts + soft
    for g in cluster(gradual, max(min_gap, 1.0)):
        if all(abs(g["t"] - k["t"]) >= 1.0 for k in keep_out):
            soft.append({**g, "method": "gradual"})
    soft.sort(key=lambda s: s["t"])
    return hard_cuts, soft


def build_shots(cuts: list[dict], duration: float) -> list[dict]:
    edges = [0.0] + [c["t"] for c in cuts if 0.0 < c["t"] < duration] + [duration]
    scores = {c["t"]: c["score"] for c in cuts}
    shots = []
    for i in range(len(edges) - 1):
        start, end = edges[i], edges[i + 1]
        if end - start <= 0:
            continue
        shots.append({
            "index": len(shots) + 1,
            "start": round(start, 2),
            "end": round(end, 2),
            "duration": round(end - start, 2),
            "cut_score": scores.get(start),
            "frames": [],
        })
    return shots


# ---------------------------------------------------------------- frames

def shot_of(shots: list[dict], t: float) -> int:
    for s in shots:
        if s["start"] <= t < s["end"]:
            return s["index"]
    return shots[-1]["index"] if shots else 1


def plan_frames(shots: list[dict], soft: list[dict], duration: float,
                interval: float, max_frames: int) -> list[dict]:
    """A frame just after each cut, inside long shots, and at each soft transition."""
    while True:
        plan: list[dict] = []
        for shot in shots:
            first = min(shot["start"] + CUT_SETTLE,
                        max(shot["start"], shot["end"] - 0.02))
            plan.append({"shot": shot["index"], "t": round(first, 2), "kind": "cut"})
            t = first + interval
            while t < shot["end"] - 0.05:
                plan.append({"shot": shot["index"], "t": round(t, 2),
                             "kind": "interval"})
                t += interval
        for s in soft:
            t = min(s["t"] + CUT_SETTLE, duration - 0.02)
            if all(abs(t - p["t"]) > 0.4 for p in plan):
                plan.append({"shot": shot_of(shots, t), "t": round(t, 2),
                             "kind": "transition", "src": s["t"]})
        if len(plan) <= max_frames or interval > duration:
            plan.sort(key=lambda p: p["t"])
            return plan
        interval *= 1.6  # too many: sample long shots more sparsely and retry


def extract_frames(video: Path, plan: list[dict], out_dir: Path,
                   notes: list[str]) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    made: list[dict] = []
    tag = {"cut": "", "interval": "_i", "transition": "_t"}

    try:
        import cv2
    except ImportError:
        cv2 = None

    if cv2 is not None:
        cap = cv2.VideoCapture(str(video))
        for item in plan:
            cap.set(cv2.CAP_PROP_POS_MSEC, item["t"] * 1000.0)
            ok, frame = cap.read()
            if not ok:
                continue
            name = f"shot{item['shot']:03d}_t{item['t']:07.2f}s{tag[item['kind']]}.jpg"
            cv2.imwrite(str(out_dir / name), frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
            made.append({**item, "file": f"frames/{name}"})
        cap.release()
        if made:
            return made
        notes.append("OpenCV opened the video but returned no frames; used ffmpeg instead.")

    if not FFMPEG:
        notes.append("No OpenCV and no ffmpeg: frames could not be extracted.")
        return made

    for item in plan:
        name = f"shot{item['shot']:03d}_t{item['t']:07.2f}s{tag[item['kind']]}.jpg"
        cp = run([FFMPEG, "-hide_banner", "-nostats", "-y",
                  "-ss", f"{max(0.0, item['t'] - 2.0):.3f}", "-i", str(video),
                  "-ss", f"{min(2.0, item['t']):.3f}", "-frames:v", "1",
                  "-q:v", "2", str(out_dir / name)], timeout=120)
        if cp.returncode == 0 and (out_dir / name).exists():
            made.append({**item, "file": f"frames/{name}"})
    return made


# ---------------------------------------------------------------- audio

def extract_audio(video: Path, wav: Path, notes: list[str]) -> bool:
    if not FFMPEG:
        notes.append("ffmpeg is unavailable, so no audio could be isolated.")
        return False
    cp = run([FFMPEG, "-y", "-hide_banner", "-nostats", "-i", str(video),
              "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", str(wav)])
    if cp.returncode != 0 or not wav.exists() or wav.stat().st_size < 1000:
        notes.append("No audio track could be extracted. The video may be silent — "
                     "confirm that before writing ((No speech present)) everywhere.")
        return False
    return True


def detect_silence(wav: Path, noise_db: int, min_dur: float) -> list[dict]:
    if not FFMPEG:
        return []
    cp = run([FFMPEG, "-hide_banner", "-nostats", "-i", str(wav),
              "-af", f"silencedetect=noise={noise_db}dB:d={min_dur}",
              "-f", "null", "-"])
    spans, start = [], None
    for line in cp.stderr.splitlines():
        m = re.search(r"silence_start:\s*(-?[0-9.]+)", line)
        if m:
            start = max(0.0, float(m.group(1)))
            continue
        m = re.search(r"silence_end:\s*([0-9.]+)", line)
        if m and start is not None:
            spans.append({"start": round(start, 2), "end": round(float(m.group(1)), 2)})
            start = None
    return spans


def rms_envelope(wav: Path, window: float) -> list[dict]:
    """Per-window loudness, used to find sounds the eye misses."""
    if not FFMPEG:
        return []
    n = max(1, int(16000 * window))
    cp = run([FFMPEG, "-hide_banner", "-nostats", "-i", str(wav),
              "-af", f"asetnsamples=n={n}:p=0,astats=metadata=1:reset=1,"
                     "ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-",
              "-f", "null", "-"])
    env, pending = [], None
    for line in cp.stdout.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            pending = float(m.group(1))
            continue
        m = re.search(r"RMS_level=(-?[0-9.]+|-inf)", line)
        if m and pending is not None:
            raw = m.group(1)
            env.append({"t": round(pending, 2),
                        "db": -120.0 if raw == "-inf" else round(float(raw), 1)})
            pending = None
    return env


def speech_gaps(segments: list[dict], duration: float,
                min_gap: float = 0.6) -> list[dict]:
    """Windows with no transcribed speech — candidate ((No speech present))."""
    gaps, cursor = [], 0.0
    for seg in sorted(segments, key=lambda s: s["start"]):
        if seg["start"] - cursor >= min_gap:
            gaps.append({"start": round(cursor, 2), "end": round(seg["start"], 2)})
        cursor = max(cursor, seg["end"])
    if duration - cursor >= min_gap:
        gaps.append({"start": round(cursor, 2), "end": round(duration, 2)})
    return gaps


def sound_events(env: list[dict], windows: list[dict], margin: float,
                 half_width: float) -> list[dict]:
    """Loud moments inside the given windows. The missed-whistle detector.

    The baseline is local, not global: a whistle over steady stadium noise only
    stands out against the seconds around it, so comparing against the whole
    video's median would hide it.
    """
    if not env or not windows:
        return []
    span = max(1, int(round(half_width / max(RMS_WINDOW, 0.01))))
    audible = [i for i, e in enumerate(env)
               if e["db"] > -119
               and any(w["start"] <= e["t"] <= w["end"] for w in windows)]
    if len(audible) < 3:
        return []

    scored = []
    for i in audible:
        lo, hi = max(0, i - span), min(len(env), i + span + 1)
        near = [env[j]["db"] for j in range(lo, hi) if env[j]["db"] > -119]
        if len(near) < 3:
            continue
        base = median(near)
        scored.append({"t": env[i]["t"], "db": env[i]["db"],
                       "above_baseline": round(env[i]["db"] - base, 1)})
    if not scored:
        return []

    strong = [s for s in scored if s["above_baseline"] >= margin]
    weak = False
    if not strong:                          # flat material: show the peaks anyway
        strong = sorted(scored, key=lambda s: -s["above_baseline"])[:5]
        weak = True

    events, last = [], -99.0
    for e in sorted(strong, key=lambda x: x["t"]):
        if e["t"] - last < 1.0:             # one event, not a run of windows
            continue
        events.append({**e, "confidence": "weak" if weak else "clear"})
        last = e["t"]
    return events


def load_wav_for_whisper(wav: Path):
    """Read our own 16 kHz mono PCM into the float32 array Whisper expects.

    Whisper otherwise shells out to a bare `ffmpeg` on PATH, which does not exist
    when ffmpeg came from imageio_ffmpeg under its versioned binary name.
    """
    import wave
    import numpy as np
    with wave.open(str(wav), "rb") as wf:
        if wf.getsampwidth() != 2 or wf.getnchannels() != 1 or wf.getframerate() != 16000:
            return None
        raw = wf.readframes(wf.getnframes())
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def transcribe(wav: Path, model_name: str, notes: list[str]) -> list[dict] | None:
    try:
        import whisper
    except ImportError:
        notes.append("openai-whisper is not installed, so there is no draft "
                     "transcript. Install it with: pip install openai-whisper")
        return None

    try:
        audio = load_wav_for_whisper(wav)
    except Exception:
        audio = None
    if audio is None:
        audio = str(wav)  # let Whisper decode it, if it can find a decoder

    try:
        print(f"[*] Loading Whisper model '{model_name}' (first run downloads it)...")
        model = whisper.load_model(model_name)
        result = model.transcribe(audio, fp16=False, verbose=None,
                                  word_timestamps=True)
    except Exception as exc:
        notes.append(f"Whisper failed: {exc}")
        return None

    return [{"start": round(s["start"], 2), "end": round(s["end"], 2),
             "text": s["text"].strip(),
             "no_speech_prob": round(s.get("no_speech_prob", 0.0), 3)}
            for s in result.get("segments", [])]


# ---------------------------------------------------------------- preflight

def build_preflight(media: dict, shots: list[dict], speech: list[dict],
                    asr_ran: bool, duration: float) -> list[str]:
    """Cheap checks against the skip criteria and the known failure modes."""
    out = []

    if duration > LONG_TASK_SECONDS:
        out.append(f"**Over 10 minutes ({duration:.0f}s).** Length alone is a skip "
                   "criterion — flag `Un-annotatable` and skip.")
    else:
        out.append(f"Length {duration:.0f}s, under the 10-minute skip threshold.")

    if not media["has_audio"]:
        out.append("**No audio stream at all.** Confirm this really is a silent "
                   "video before annotating it as one.")

    ratio = 0.0
    if asr_ran:
        spoken = sum(s["end"] - s["start"] for s in speech)
        ratio = (spoken / duration * 100) if duration else 0.0
        out.append(f"Speech covers roughly {ratio:.0f}% of the runtime "
                   f"({spoken:.0f}s of {duration:.0f}s).")
    else:
        out.append("Speech coverage unknown — transcription did not run.")

    mean_shot = (duration / len(shots)) if shots else duration
    out.append(f"{len(shots)} hard-cut shot(s), mean length {mean_shot:.1f}s.")

    if asr_ran and len(shots) <= 2 and ratio > 50:
        out.append("**Possible data-sparse skip.** Plenty of speech over an almost "
                   "static picture is the project's own example of tracks that are "
                   "not equally rich. Watch it before deciding — if the visual track "
                   "genuinely has nothing to describe, flag `Un-annotatable` and skip.")
    if asr_ran and len(shots) > 3 and ratio < 5:
        out.append("Busy picture, almost no speech. Expect long "
                   "`((No speech present))` stretches and a heavy Audio caption.")

    return out


# ---------------------------------------------------------------- report

def fmt(t: float) -> str:
    return f"{int(t // 60)}:{t % 60:05.2f}"


def write_report(path: Path, d: dict) -> None:
    dur = d["media"]["duration"]
    shots, frames = d["shots"], d["frames"]
    lines: list[str] = []
    add = lines.append

    add(f"# Gaffer Inspection — {d['slug']}\n")
    add(f"- **Source:** {d['source']}")
    if d.get("youtube_id"):
        add(f"- **YouTube ID:** `{d['youtube_id']}`")
    add(f"- **Duration:** {dur:.2f}s ({fmt(dur)})")
    add(f"- **Resolution / FPS:** {d['media']['width']}x{d['media']['height']} @ "
        f"{d['media']['fps']:.2f}"
        + (f" · fetched by `{d['download_client']}`" if d.get("download_client") else ""))
    add(f"- **Cut detector:** {d['cuts']['method']}, hard ≥ "
        f"{d['cuts']['hard_threshold']}, soft ≥ {d['cuts']['soft_threshold']}")
    add(f"- **Shots:** {len(shots)} · **Possible transitions:** "
        f"{len(d['cuts']['soft'])} · **Frames:** {len(frames)} · "
        f"**Draft speech segments:** {len(d['speech'])}\n")

    add("> The transcript below is a **draft**. Whisper mangles names and repeats "
        "lines. Use it to find where speech is, then listen and write what you "
        "actually hear.\n")

    add("## Pre-Flight Checks\n")
    for check in d["preflight"]:
        add(f"- {check}")
    add("")

    if d["notes"]:
        add("## Stages Skipped or Degraded\n")
        for n in d["notes"]:
            add(f"- {n}")
        add("")

    add("## Shot List — Visual+Audio Segment Candidates\n")
    add("Each row is a detected hard cut. These are your starting Visual+Audio "
        "segment boundaries. Check every one against its frame before using it.\n")
    add("| # | Start | End | Length | Cut score | Frames |")
    add("|---|---|---|---|---|---|")
    for s in shots:
        own = [f for f in frames if f["shot"] == s["index"]]
        first = f"`{own[0]['file']}`" if own else "—"
        extra = f" +{len(own) - 1}" if len(own) > 1 else ""
        score = f"{s['cut_score']:.3f}" if s["cut_score"] is not None else "start"
        add(f"| {s['index']} | {s['start']:.2f} | {s['end']:.2f} | "
            f"{s['duration']:.2f}s | {score} | {first}{extra} |")
    add("")

    add("### Possible Transitions — Check These By Eye\n")
    if d["cuts"]["soft"]:
        add("Weaker than a hard cut. Dissolves, whip pans, graphic wipes and camera "
            "moves inside continuous action all land here, and so does ordinary "
            "motion. Some are real boundaries, some are nothing. A frame was "
            "grabbed for each one.\n")
        add("`scene` rows come from frame-to-frame scoring and their times are "
            "exact. `gradual` rows come from the dissolve scan, which compares each "
            "frame with the one a second earlier — a real boundary, but the time is "
            "approximate to within about half a second, so check the frame.\n")
        add("| Time | Score | Found by | Frame |")
        add("|---|---|---|---|")
        for s in d["cuts"]["soft"]:
            f = next((x for x in frames if x.get("src") == s["t"]), None)
            cell = f"`{f['file']}`" if f else "— covered by a nearby frame"
            add(f"| {s['t']:.2f} | {s['score']:.3f} | "
                f"{s.get('method', 'scene')} | {cell} |")
        add("")
    else:
        add("*None found.*\n")

    if d["fades"]:
        add("### Black / Fade Stretches\n")
        add("| Start | End |")
        add("|---|---|")
        for f in d["fades"]:
            add(f"| {f['start']:.2f} | {f['end']:.2f} |")
        add("")

    add("## Draft Speech Transcript\n")
    if d["speech"]:
        add("| Start | End | Draft text |")
        add("|---|---|---|")
        for seg in d["speech"]:
            text = seg["text"].replace("|", "\\|")
            flag = " ⚠️" if seg.get("no_speech_prob", 0) > 0.6 else ""
            add(f"| {seg['start']:.2f} | {seg['end']:.2f} | {text}{flag} |")
        add("")
        add("⚠️ marks segments Whisper itself doubts. Listen before trusting them — "
            "they are often `((unintelligible))` rather than words.\n")
    elif d["asr_ran"]:
        add("*Whisper found no speech. Verify by ear before captioning the whole "
            "video as `((No speech present))`.*\n")
    else:
        add("*Transcription did not run — see the skipped stages above.*\n")

    add("## No-Speech Windows — `((No speech present))` Candidates\n")
    if d["speech_gaps"]:
        add("| Start | End | Length | Audio still active? |")
        add("|---|---|---|---|")
        for g in d["speech_gaps"]:
            silent = any(s["start"] <= g["start"] + 0.05 and s["end"] >= g["end"] - 0.05
                         for s in d["silence"])
            add(f"| {g['start']:.2f} | {g['end']:.2f} | {g['end'] - g['start']:.2f}s | "
                f"{'no — fully silent' if silent else 'yes — sound present'} |")
        add("")
        add("Where audio is still active, the Speech captions get "
            "`((No speech present))` **and** the Audio caption still describes what "
            "is playing.\n")
    elif d["asr_ran"]:
        add("*Speech runs continuously — no gap long enough to flag.*\n")
    else:
        add("*Unknown without a transcript.*\n")

    add("## Loud Non-Speech Moments — Audio Caption Candidates\n")
    if d["sound_events"]:
        scope = ("windows with no speech" if d["asr_ran"]
                 else "the whole video, since speech position is unknown")
        add(f"Moments markedly louder than the seconds around them, measured across "
            f"{scope}. Whistles, impacts, applause, stingers, doors. Missing one of "
            "these is common error #5.\n")
        if any(e["confidence"] == "weak" for e in d["sound_events"]):
            add("*Marked weak: nothing cleared the margin, so these are simply the "
                "most prominent peaks. Treat them as hints.*\n")
        add("| Time | Level | Above local baseline |")
        add("|---|---|---|")
        for e in d["sound_events"]:
            add(f"| {e['t']:.2f} | {e['db']:.1f} dB | +{e['above_baseline']:.1f} dB |")
        add("")
        add("**This list cannot see sounds that happen underneath speech**, because "
            "the voice dominates the level. The referee whistle that failed a real "
            "task was blown while the commentator was talking. Listen through the "
            "speech as well as the gaps.\n")
    else:
        add("*Nothing stood out. That is not proof there is nothing — listen to "
            "`audio.wav` before claiming a segment has no sounds.*\n")

    add("## How To Use This\n")
    add("1. Open the frames in shot order. That is your Visual caption spine — one "
        "segment per shot, every cut already timestamped.")
    add("2. Work through the possible transitions. Sports and continuous action "
        "score low, so real boundaries hide in that table.")
    add("3. Read the on-screen text off the frames yourself. Nothing here does OCR, "
        "and text must be copied exactly, typos included.")
    add("4. Listen to `audio.wav` against the draft transcript. Fix every misheard "
        "word, split merged speakers, number speakers by first appearance.")
    add("5. Use the no-speech windows to place `((No speech present))`, and the loud "
        "moments as a starting list — not a finished list — for the Audio caption. "
        "Sounds under speech never reach that table.")
    add("6. Remember the two tracks segment **independently**. Shots drive "
        "Visual+Audio; utterances drive Speech.\n")
    add("Rules: `references/visual-audio-track.md`, `references/speech-track.md`, "
        "then `references/self-audit.md` before submitting.")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- deps

def check_deps() -> int:
    rows = [("ffmpeg", bool(FFMPEG), FFMPEG or "not found",
             "core — frames, audio, cut detection"),
            ("ffprobe", bool(FFPROBE), FFPROBE or "not found",
             "optional — OpenCV covers probing")]
    for mod, role in [("cv2", "optional — faster, more accurate frame seeking"),
                      ("yt_dlp", "needed only for URLs"),
                      ("whisper", "optional — draft transcript"),
                      ("imageio_ffmpeg", "optional — bundles ffmpeg")]:
        try:
            __import__(mod)
            rows.append((mod, True, "installed", role))
        except ImportError:
            rows.append((mod, False, "not installed", role))

    width = max(len(r[0]) for r in rows)
    for name, ok, detail, role in rows:
        print(f"  {'OK ' if ok else '-- '} {name:<{width}}  {detail}")
        if not ok:
            print(f"      {role}")

    if not FFMPEG:
        print("\nffmpeg is required. Install it, or: pip install imageio-ffmpeg")
        return 1
    print("\nCore dependencies present.")
    print("For everything: pip install -r requirements.txt")
    return 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Inspect one video for Project Gaffer captioning.")
    ap.add_argument("source", nargs="?",
                    help="YouTube URL, 11-character video ID, or local file path")
    ap.add_argument("--out", default="gaffer-inspections",
                    help="output root (default: ./gaffer-inspections)")
    ap.add_argument("--scene-threshold", type=float, default=SCENE_THRESHOLD,
                    help=f"hard-cut sensitivity (default {SCENE_THRESHOLD})")
    ap.add_argument("--soft-threshold", type=float, default=SOFT_THRESHOLD,
                    help=f"possible-transition floor (default {SOFT_THRESHOLD})")
    ap.add_argument("--min-shot", type=float, default=MIN_SHOT_SECONDS,
                    help=f"merge boundaries closer than this (default {MIN_SHOT_SECONDS}s)")
    ap.add_argument("--interval", type=float, default=INTERVAL_IN_SHOT,
                    help=f"extra frames inside long shots (default {INTERVAL_IN_SHOT}s)")
    ap.add_argument("--max-frames", type=int, default=MAX_FRAMES,
                    help=f"frame cap (default {MAX_FRAMES})")
    ap.add_argument("--max-height", type=int, default=MAX_HEIGHT,
                    help=f"cap download resolution (default {MAX_HEIGHT}); lower "
                         "is faster to process but harder to read text on")
    ap.add_argument("--min-height", type=int, default=MIN_HEIGHT,
                    help=f"keep trying player clients until one clears this "
                         f"(default {MIN_HEIGHT}); the tallest result is used if "
                         "none does")
    ap.add_argument("--force-download", action="store_true",
                    help="refetch even if a video is already in the output folder, "
                         "e.g. to retry for a better resolution after rate limiting")
    ap.add_argument("--whisper-model", default=WHISPER_MODEL,
                    help="tiny|base|small|medium|large-v3 (default small)")
    ap.add_argument("--no-asr", action="store_true", help="skip transcription")
    ap.add_argument("--no-gradual", action="store_true",
                    help="skip the dissolve/fade scan (faster on long videos)")
    ap.add_argument("--check-deps", action="store_true",
                    help="report tool and library availability, then exit")
    args = ap.parse_args()

    if args.check_deps:
        return check_deps()
    if not args.source:
        ap.error("a source is required (URL, video ID, or file path)")
    if not FFMPEG:
        print("[!] ffmpeg not found. Run --check-deps.", file=sys.stderr)
        return 1

    notes: list[str] = []
    out_root = Path(args.out).expanduser().resolve()
    video_id = parse_video_id(args.source)
    local = Path(args.source).expanduser()

    client_used = None
    if local.exists() and local.is_file():
        slug = slugify(local.stem)
        work = out_root / slug
        work.mkdir(parents=True, exist_ok=True)
        video, source_desc = local, str(local)
    elif video_id:
        slug = slugify(video_id)
        work = out_root / slug
        video, client_used = download(video_id, work, notes, args.max_height,
                                      args.min_height, args.force_download)
        source_desc = f"https://www.youtube.com/watch?v={video_id}"
        if not video:
            for n in notes:
                print(f"[!] {n}", file=sys.stderr)
            return 2
    else:
        print(f"[!] Not a file, a YouTube URL, or a video ID: {args.source}",
              file=sys.stderr)
        return 2

    print(f"[*] Working in {work}")

    media = probe(video)
    if not media["duration"]:
        print("[!] Could not read the video duration. Is the file complete?",
              file=sys.stderr)
        return 3
    print(f"[*] {media['duration']:.2f}s @ {media['fps']:.2f} fps, "
          f"{media['width']}x{media['height']}")
    if media["height"] and media["height"] < args.min_height:
        retry = ("Re-run with --force-download to try again — a plain re-run reuses "
                 "the file already downloaded." if video_id else
                 "Source a higher-resolution copy if on-screen text matters here.")
        notes.append(f"Only {media['width']}x{media['height']} was available. Small "
                     "on-screen text may not be legible in the frames — read banners "
                     "and captions in the task player instead, and say so if you "
                     f"still cannot make a character out. {retry}")

    print("[*] Detecting scene changes...")
    method = "ffmpeg scene filter"
    hits = score_frames_ffmpeg(video, args.soft_threshold)
    if hits is None:
        hits = score_frames_opencv(video, args.soft_threshold)
        method = "OpenCV histogram fallback"
        if hits is None:
            hits = []
            method = "none available"
            notes.append("No cut detector could run. The shot list is one whole-video "
                         "block; find the cuts by eye.")
    gradual: list[dict] = []
    if not args.no_gradual:
        got = detect_gradual(video)
        if got is None:
            notes.append("OpenCV is missing, so dissolves and fades were not "
                         "scanned for. Install opencv-python to catch them.")
        else:
            gradual = got
    hard, soft = split_tiers(hits, gradual, args.scene_threshold, args.min_shot)
    print(f"[*] {len(hard)} hard cut(s), {len(soft)} possible transition(s)")
    if not hard and soft:
        notes.append("No hard cuts at all. This edit is built from dissolves or "
                     "continuous camera work, so every boundary is in the possible "
                     "transitions table and needs checking by eye.")

    fades = detect_fades(video)
    shots = build_shots(hard, media["duration"])

    print("[*] Extracting frames...")
    plan = plan_frames(shots, soft, media["duration"], args.interval, args.max_frames)
    frames = extract_frames(video, plan, work / "frames", notes)
    for f in frames:
        for s in shots:
            if s["index"] == f["shot"]:
                s["frames"].append(f["file"])
    print(f"[*] {len(frames)} frame(s) written")

    wav = work / "audio.wav"
    silence: list[dict] = []
    env: list[dict] = []
    speech: list[dict] = []
    asr_ran = False
    if extract_audio(video, wav, notes):
        print("[*] Analysing audio...")
        silence = detect_silence(wav, SILENCE_DB, SILENCE_MIN)
        env = rms_envelope(wav, RMS_WINDOW)
        if args.no_asr:
            notes.append("Transcription skipped (--no-asr), so no-speech windows are "
                         "unknown and loud moments were scanned across the whole video.")
        else:
            got = transcribe(wav, args.whisper_model, notes)
            if got is not None:
                speech, asr_ran = got, True
                print(f"[*] {len(speech)} draft speech segment(s)")

    whole = [{"start": 0.0, "end": round(media["duration"], 2)}]
    gaps = speech_gaps(speech, media["duration"]) if asr_ran else []
    events = sound_events(env, gaps if (asr_ran and gaps) else whole,
                          EVENT_MARGIN_DB, EVENT_HALF_WIDTH)

    data = {
        "slug": slug,
        "source": source_desc,
        "youtube_id": video_id,
        "video_file": str(video),
        "download_client": client_used,
        "media": media,
        "cuts": {"method": method,
                 "hard_threshold": args.scene_threshold,
                 "soft_threshold": args.soft_threshold,
                 "raw": hits, "hard": hard, "soft": soft},
        "fades": fades,
        "shots": shots,
        "frames": frames,
        "speech": speech,
        "asr_ran": asr_ran,
        "speech_gaps": gaps,
        "silence": silence,
        "sound_events": events,
        "notes": notes,
        "preflight": build_preflight(media, shots, speech, asr_ran, media["duration"]),
    }

    (work / "inspection.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    write_report(work / "INSPECTION.md", data)

    print(f"\n[+] Report:  {work / 'INSPECTION.md'}")
    print(f"[+] Data:    {work / 'inspection.json'}")
    print(f"[+] Frames:  {work / 'frames'}")
    if notes:
        print("\n[!] Degraded stages:")
        for n in notes:
            print(f"    - {n}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
