#!/usr/bin/env python3
"""
Multi-modal inspection for Handshake IG video tasks.

Fetches an Instagram Reel (or reads a local file), finds every scene, samples one
keyframe per scene, builds a contact sheet, demuxes audio, and transcribes speech
with timestamps. Read-only with respect to task material: everything is written
to an output directory you choose, never into HANDSHAKE-AI/.

    # whole pipeline from a Reel URL
    python3 tools/inspect_media.py --url https://www.instagram.com/reel/ABC123/ --out /tmp/insp

    # local file, visual only, no audio or transcript
    python3 tools/inspect_media.py --video clip.mp4 --out /tmp/insp --no-audio

    # magnify a detail to settle an identity call
    python3 tools/inspect_media.py --video clip.mp4 --out /tmp/insp --zoom 7.6,230,660,240,240 --scale 6

    # what is installed
    python3 tools/inspect_media.py --check-deps

Why scene detection rather than fixed-interval sampling: a montage Reel can carry
a decisive shot under one second long. Sampling every N seconds straddles it and
you never see it. Cuts are detected first, then one frame is taken per segment, so
every shot is represented no matter how short.

Cuts are detected on the *cropped* content region. Portrait Reels are frequently
delivered inside a padded landscape canvas, and a bright pad dominates the
histogram badly enough that whole-frame detection reports zero cuts on a video
that plainly has ten.

Degrades instead of failing. OpenCV alone gives frames, cuts, sheets and zooms.
FFmpeg adds audio. Whisper adds the transcript. Playwright or yt-dlp adds URL
fetching. Missing pieces are reported, and the rest still runs.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

# --- optional dependencies, each gates one tier of the pipeline ---------------

try:
    import cv2
    import numpy as np
    HAVE_CV2 = True
except ImportError:
    HAVE_CV2 = False

try:
    import imageio_ffmpeg
    HAVE_IIO = True
except ImportError:
    HAVE_IIO = False

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")


def ffmpeg_bin() -> str | None:
    """ffmpeg is often absent from PATH; imageio-ffmpeg ships its own binary."""
    import shutil
    return shutil.which("ffmpeg") or (
        imageio_ffmpeg.get_ffmpeg_exe() if HAVE_IIO else None
    )


def have(mod: str) -> bool:
    import importlib
    try:
        importlib.import_module(mod)
        return True
    except Exception:
        return False


def check_deps(verbose: bool = True) -> dict:
    caps = {
        "frames": HAVE_CV2,
        "audio": bool(ffmpeg_bin()),
        "transcript": have("whisper"),
        "download": have("playwright") or have("yt_dlp"),
    }
    if verbose:
        rows = [
            ("frames, cuts, contact sheet, zoom", "opencv-python", caps["frames"]),
            ("audio demux to 16k mono PCM", "ffmpeg / imageio-ffmpeg", caps["audio"]),
            ("timestamped speech transcript", "openai-whisper", caps["transcript"]),
            ("fetch a Reel from a URL", "playwright / yt-dlp", caps["download"]),
        ]
        for what, pkg, ok in rows:
            print(f"  {'OK  ' if ok else 'MISS'}  {what:34s}  ({pkg})")
        if all(caps.values()):
            print("\nAll tiers available.")
        else:
            print("\nDEGRADED MODE. Missing tiers are skipped; the rest still runs.")
            print("Install with: python3 -m pip install --user -r tools/requirements.txt")
            print("Then:         python3 -m playwright install chromium")
    return caps


# --- 1. fetch ----------------------------------------------------------------

SHORTCODE = re.compile(r"instagram\.com/(?:reel|reels|p|tv)/([A-Za-z0-9_-]+)")


def shortcode_of(url: str) -> str | None:
    m = SHORTCODE.search(url)
    return m.group(1) if m else None


def download_via_embed(shortcode: str, dest: Path) -> bool:
    """Load the public embed page headless and capture the MP4 off the wire.

    The embed endpoint renders without a login, which is what makes this work
    where a normal profile URL would bounce to a sign-in wall.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False

    seen: list[str] = []
    target = None
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent=UA)

        def on_response(resp):
            ctype = resp.headers.get("content-type", "")
            if ("video" in ctype or ".mp4" in resp.url) and resp.status == 200:
                seen.append(resp.url)

        page.on("response", on_response)
        try:
            page.goto(f"https://www.instagram.com/reel/{shortcode}/embed/",
                      wait_until="networkidle", timeout=30000)
        except Exception:
            pass  # networkidle often times out on IG; the DOM check still works

        el = page.query_selector("video")
        if el:
            src = el.get_attribute("src") or ""
            if src.startswith("http"):
                target = src
        browser.close()

    if not target and seen:
        target = seen[0]
    if not target:
        return False

    req = urllib.request.Request(
        target, headers={"User-Agent": UA, "Referer": "https://www.instagram.com/"})
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest.exists() and dest.stat().st_size > 0


def download_via_ytdlp(url: str, dest: Path) -> bool:
    try:
        import yt_dlp
    except ImportError:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    opts = {"outtmpl": str(dest), "quiet": True, "no_warnings": True,
            "format": "mp4/best", "http_headers": {"User-Agent": UA}}
    try:
        with yt_dlp.YoutubeDL(opts) as y:
            y.download([url])
    except Exception:
        return False
    return dest.exists() and dest.stat().st_size > 0


def fetch(url: str, dest: Path) -> bool:
    """Try the embed scraper first, then yt-dlp. Either alone is often enough."""
    if dest.exists() and dest.stat().st_size > 0:
        print(f"[=] already downloaded: {dest}")
        return True
    sc = shortcode_of(url)
    if sc:
        print(f"[*] instagram shortcode {sc} — trying embed capture")
        try:
            if download_via_embed(sc, dest):
                print(f"[OK] {dest} ({dest.stat().st_size/1e6:.2f} MB)")
                return True
        except Exception as e:
            print(f"[!] embed capture failed: {type(e).__name__}: {e}")
    print("[*] trying yt-dlp")
    if download_via_ytdlp(url, dest):
        print(f"[OK] {dest} ({dest.stat().st_size/1e6:.2f} MB)")
        return True
    print("[X] could not retrieve the video")
    return False


# --- 2. geometry: find the real picture inside any padding -------------------

def content_box(frames: list) -> tuple[int, int, int, int]:
    """Return (x0, x1, y0, y1) of the actual picture within a padded frame.

    Padding is flat, so it carries almost no variance along its own axis. The
    picture is the widest run of high-variance columns and rows.

    Variance is pooled across several frames with an elementwise max, never
    measured on one. A single frame lies: a shot with a dark dashboard along the
    bottom, or a blown-out sky along the top, has genuinely flat picture rows and
    a one-frame probe will happily crop them away as if they were padding. A band
    is only padding if it stays flat for the whole video.
    """
    h, w = frames[0].shape[:2]
    col_sd = np.zeros(w, np.float32)
    row_sd = np.zeros(h, np.float32)
    for f in frames:
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)
        col_sd = np.maximum(col_sd, g.std(axis=0))
        row_sd = np.maximum(row_sd, g.std(axis=1))

    # Only strip leading and trailing bands that are essentially constant for the
    # whole video. Two deliberate choices, both to avoid eating real picture:
    # the threshold is near zero rather than merely "low", because a soft sky or
    # a dark ceiling is low-contrast but still content; and only edge bands are
    # trimmed, never the widest interior run, which could crop to a bright middle.
    FLAT = 3.0

    def trim(sd):
        n = len(sd)
        lo, hi = 0, n - 1
        while lo < n and sd[lo] < FLAT:
            lo += 1
        while hi > lo and sd[hi] < FLAT:
            hi -= 1
        return (0, n - 1) if lo >= hi else (lo, hi)

    x0, x1 = trim(col_sd)
    y0, y1 = trim(row_sd)
    return x0, x1, y0, y1


# --- 3. scene detection ------------------------------------------------------

def scan(path: Path, cut_threshold: float = 0.60) -> dict:
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise SystemExit(f"cannot open {path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    probes = []
    for r in (0.10, 0.30, 0.50, 0.70, 0.90):
        cap.set(cv2.CAP_PROP_POS_FRAMES, min(int(n * r), max(n - 1, 0)))
        ok, p = cap.read()
        if ok:
            probes.append(p)
    x0, x1, y0, y1 = content_box(probes) if probes else (0, w - 1, 0, h - 1)
    padded = (x1 - x0 + 1, y1 - y0 + 1) != (w, h)

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    prev, cuts, i = None, [], 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        roi = f[y0:y1 + 1, x0:x1 + 1]
        hsv = cv2.cvtColor(cv2.resize(roi, (96, 128)), cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [24, 24], [0, 180, 0, 256])
        cv2.normalize(hist, hist)
        if prev is not None:
            if cv2.compareHist(prev, hist, cv2.HISTCMP_CORREL) < cut_threshold:
                cuts.append(i)
        prev, i = hist, i + 1
    cap.release()

    bounds = [0] + cuts + [n]
    segments = [{"index": k,
                 "start_frame": bounds[k], "end_frame": bounds[k + 1],
                 "start_s": round(bounds[k] / fps, 2),
                 "end_s": round(bounds[k + 1] / fps, 2),
                 "duration_s": round((bounds[k + 1] - bounds[k]) / fps, 2)}
                for k in range(len(bounds) - 1)
                if bounds[k + 1] > bounds[k]]

    return {"path": str(path), "fps": round(fps, 3), "frames": n,
            "duration_s": round(n / fps, 2), "width": w, "height": h,
            "content_box": {"x0": x0, "x1": x1, "y0": y0, "y1": y1},
            "padded": padded, "segments": segments}


# --- 4. keyframes and contact sheet ------------------------------------------

def keyframes(path: Path, meta: dict, out: Path) -> list[dict]:
    """One frame per detected scene, plus fixed ratios as a safety net."""
    out.mkdir(parents=True, exist_ok=True)
    fps, n = meta["fps"], meta["frames"]
    b = meta["content_box"]

    picks: dict[int, str] = {}
    for seg in meta["segments"]:
        picks[(seg["start_frame"] + seg["end_frame"]) // 2] = f"scene{seg['index']:02d}"
    for r in (0.05, 0.20, 0.35, 0.50, 0.65, 0.80, 0.95):
        idx = int(n * r)
        picks.setdefault(idx, f"ratio{int(r*100):02d}")

    cap = cv2.VideoCapture(str(path))
    saved = []
    for idx in sorted(picks):
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, f = cap.read()
        if not ok:
            continue
        crop = f[b["y0"]:b["y1"] + 1, b["x0"]:b["x1"] + 1]
        t = idx / fps
        fn = out / f"{picks[idx]}_{t:06.2f}s.jpg"
        cv2.imwrite(str(fn), crop, [cv2.IMWRITE_JPEG_QUALITY, 95])
        saved.append({"tag": picks[idx], "frame": idx,
                      "t_s": round(t, 2), "path": str(fn)})
    cap.release()
    return saved


def contact_sheet(frames: list[dict], dest: Path, cols: int = 5,
                  tile_w: int = 280) -> Path | None:
    if not frames:
        return None
    tiles = []
    for fr in frames:
        img = cv2.imread(fr["path"])
        if img is None:
            continue
        th = int(tile_w * img.shape[0] / img.shape[1])
        t = cv2.resize(img, (tile_w, th))
        cv2.rectangle(t, (0, 0), (118, 22), (0, 0, 0), -1)
        cv2.putText(t, f"{fr['t_s']:.2f}s", (4, 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        tiles.append(t)
    if not tiles:
        return None
    hmax = max(t.shape[0] for t in tiles)
    tiles = [cv2.copyMakeBorder(t, 0, hmax - t.shape[0], 0, 0,
                                cv2.BORDER_CONSTANT, value=(20, 20, 20)) for t in tiles]
    while len(tiles) % cols:
        tiles.append(np.full_like(tiles[0], 20))
    rows = [np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]
    cv2.imwrite(str(dest), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 92])
    return dest


def zoom(path: Path, meta: dict, spec: str, scale: float, dest: Path) -> Path:
    """spec = "t,x,y,w,h" in content-box coordinates. Magnify to settle a detail."""
    t, x, y, w, h = (float(v) for v in spec.split(","))
    b = meta["content_box"]
    cap = cv2.VideoCapture(str(path))
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * meta["fps"]))
    ok, f = cap.read()
    cap.release()
    if not ok:
        raise SystemExit(f"no frame at {t}s")
    crop = f[b["y0"]:b["y1"] + 1, b["x0"]:b["x1"] + 1]
    x, y = int(x), int(y)
    sub = crop[max(0, y):int(y + h), max(0, x):int(x + w)]
    if sub.size == 0:
        raise SystemExit("zoom region is outside the content box")
    big = cv2.resize(sub, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(str(dest), big, [cv2.IMWRITE_JPEG_QUALITY, 96])
    return dest


# --- 5. audio and speech -----------------------------------------------------

def extract_audio(video: Path, wav: Path) -> bool:
    exe = ffmpeg_bin()
    if not exe:
        return False
    wav.parent.mkdir(parents=True, exist_ok=True)
    cmd = [exe, "-y", "-i", str(video), "-vn",
           "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", str(wav)]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True)
    except Exception:
        return False
    return wav.exists() and wav.stat().st_size > 0


def load_wav_mono16k(wav: Path):
    """Decode our own 16 kHz mono PCM WAV into the float32 array Whisper wants.

    Handing Whisper a *path* makes it shell out to `ffmpeg` on PATH, which is the
    very thing that is missing here — the failure surfaces from inside the
    library rather than from this script. Passing an array skips that entirely,
    and we already wrote the file in exactly the format it expects.
    """
    import wave
    with wave.open(str(wav), "rb") as w:
        if w.getnchannels() != 1 or w.getsampwidth() != 2 or w.getframerate() != 16000:
            raise ValueError("expected 16 kHz mono 16-bit PCM")
        raw = w.readframes(w.getnframes())
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def transcribe(wav: Path, model_name: str = "base") -> list[dict]:
    try:
        import whisper
    except ImportError:
        return []
    model = whisper.load_model(model_name)
    res = model.transcribe(load_wav_mono16k(wav), fp16=False,
                           word_timestamps=True, verbose=False)
    return [{"start": round(s["start"], 2), "end": round(s["end"], 2),
             "text": s["text"].strip()} for s in res.get("segments", [])]


# --- 6. driver ---------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Fetch and inspect an IG Reel: scenes, keyframes, audio, transcript.")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--url", help="Instagram Reel (or other) URL")
    src.add_argument("--video", help="path to a local video file")
    ap.add_argument("--out", default="./inspection", help="output directory")
    ap.add_argument("--no-audio", action="store_true", help="skip audio demux")
    ap.add_argument("--no-transcript", action="store_true", help="skip Whisper")
    ap.add_argument("--whisper-model", default="base",
                    help="tiny | base | small | medium | large")
    ap.add_argument("--cut-threshold", type=float, default=0.60,
                    help="lower finds fewer cuts (0-1)")
    ap.add_argument("--zoom", help='"t,x,y,w,h" in content-box coordinates')
    ap.add_argument("--scale", type=float, default=5.0, help="zoom magnification")
    ap.add_argument("--check-deps", action="store_true")
    a = ap.parse_args()

    if a.check_deps:
        check_deps()
        return 0
    if not (a.url or a.video):
        ap.error("one of --url or --video is required")
    if not HAVE_CV2:
        print("opencv-python is required for every mode except --check-deps.")
        return 2

    out = Path(a.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    if a.url:
        video = out / ((shortcode_of(a.url) or "video") + ".mp4")
        if not fetch(a.url, video):
            return 1
    else:
        video = Path(a.video).expanduser().resolve()
        if not video.exists():
            print(f"no such file: {video}")
            return 1

    print(f"[*] scanning {video.name}")
    meta = scan(video, a.cut_threshold)
    print(f"    {meta['duration_s']}s @ {meta['fps']}fps, {meta['width']}x{meta['height']}"
          + (f", padded -> content {meta['content_box']}" if meta["padded"] else ""))
    print(f"    {len(meta['segments'])} scene(s):")
    for s in meta["segments"]:
        print(f"      {s['index']:>2}  {s['start_s']:>6.2f}-{s['end_s']:>6.2f}s  ({s['duration_s']}s)")

    frames = keyframes(video, meta, out / "frames")
    print(f"[OK] {len(frames)} keyframes -> {out/'frames'}")
    sheet = contact_sheet(frames, out / "contact_sheet.jpg")
    if sheet:
        print(f"[OK] contact sheet -> {sheet}")

    if a.zoom:
        z = zoom(video, meta, a.zoom, a.scale, out / "zoom.jpg")
        print(f"[OK] zoom -> {z}")

    speech, wav = [], None
    if not a.no_audio:
        wav = out / "audio.wav"
        if extract_audio(video, wav):
            print(f"[OK] 16kHz mono PCM -> {wav}")
            if not a.no_transcript:
                if have("whisper"):
                    print(f"[*] transcribing with whisper:{a.whisper_model}")
                    speech = transcribe(wav, a.whisper_model)
                    for s in speech:
                        print(f"      [{s['start']:>6.2f}-{s['end']:>6.2f}] {s['text']}")
                    if not speech:
                        print("      (no speech detected)")
                else:
                    print("[!] whisper not installed — transcript skipped")
        else:
            wav = None
            print("[!] ffmpeg unavailable — audio and transcript skipped")

    meta.update({"keyframes": frames,
                 "contact_sheet": str(sheet) if sheet else None,
                 "audio_wav": str(wav) if wav else None,
                 "speech": speech})
    summary = out / "inspection_summary.json"
    summary.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"[OK] summary -> {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
