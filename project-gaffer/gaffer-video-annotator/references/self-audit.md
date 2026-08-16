# Pre-Submission Self-Audit

Run this before every submission. It is built from the ten things auditors
actually fail people for.

The Autochecker will not catch any of this. It checks format and coverage
mechanics. Everything below is about whether what you wrote is **true**,
**complete**, and **in the right place** — which only a person can check.

**Name your evidence.** For each check, be able to say what you actually looked
at — the frame filename, the timestamp in `audio.wav`, the row in `INSPECTION.md`.
If you could not run a check — no audio, no local file, unreadable text, a stage
the inspector had to skip — say so plainly instead of claiming it. Never claim a
verification you did not perform.

**Pass 0 — did you inspect at all?** If you have not run
`../scripts/gaffer_inspect.py` and read its report, stop and do that first. Read
its skipped-stages section too: anything it could not do is something you must do
by hand, not something you may assume. See `../references/video-inspection.md`.

## Contents

- [Pass 1 — Coverage](#pass-1--coverage)
- [Pass 2 — Truth](#pass-2--truth)
- [Pass 3 — Placement](#pass-3--placement)
- [Pass 4 — Speech Track Detail](#pass-4--speech-track-detail)
- [Pass 5 — Visual Track Detail](#pass-5--visual-track-detail)
- [Pass 6 — Audio Track Detail](#pass-6--audio-track-detail)
- [Pass 7 — Format and Routing](#pass-7--format-and-routing)
- [The Three Questions](#the-three-questions)

## Pass 1 — Coverage

Is everything that happened in there?

- [ ] **Speech track runs edge to edge.** Add up the segment windows. They should
      cover 0.0 to the end of the video with no gaps and no overlaps.
- [ ] **Visual+Audio track runs edge to edge**, separately.
- [ ] **Every speech segment is transcribed to its own end.** Take the longest
      segment and check the last words against the clock. A caption that reads as
      a finished paragraph can still stop 49 seconds early — that is exactly what
      happened in the missing-speech failure.
- [ ] **Silence is tagged, not omitted.** Every silent stretch carries
      `((No speech present))` on both Speech captions.
- [ ] **Every cut has a timestamp.** Count the shot changes you can see, then
      count the stamps in your captions. If a segment covers thirty seconds with
      one sentence, it is wrong.
- [ ] **Every on-screen text is present** — banners, lower thirds, scoreboards,
      tickers, watermarks, station IDs, signage, clothing text, and text inside
      any screen shown in the frame.
- [ ] **Every change to on-screen text is captured.** A number that updates twice
      is three facts.
- [ ] **Every speaker who says anything has a number**, including one-word
      interjections and off-screen voices.
- [ ] **Every speaker in a window is described** in Speech Caption 2, not just the
      main one.
- [ ] On a Mini task: the first 60 seconds are complete, on both tracks.

## Pass 2 — Truth

Is everything in there something that actually happened?

- [ ] **Every sound named is a sound you heard.** Go through the Audio captions
      and point at each claim. "Soft piano music" failed a task because there was
      no piano.
- [ ] **Every object, colour and garment is one you saw.** Not one you expect to
      be there.
- [ ] **No inferred roles, jobs, relationships or identities.** No "reporter", no
      "anchor", no "mother", no "professional". If a name or title is on screen,
      you may use it; otherwise describe the person.
- [ ] **No inferred nationalities.** Accents are heard, so "a German accent" is
      fine. "The speaker is German" is not.
- [ ] **Accents judged from the voice only**, never from clothing, setting, flags
      or subject matter.
- [ ] **Every transcribed line makes sense as English.** Anything that does not —
      "a pure wit gun" — is a mishearing. Go back and listen at reduced speed.
- [ ] **Uncertain things are hedged, not asserted.** "what appears to be a avocado
      mash" is correct. Do not name something you cannot identify, and do not
      leave it out.
- [ ] **Negative claims are true.** "No stutters, sighing, laughter, or other
      non-verbal sounds are present" is a claim an auditor will check.

## Pass 3 — Placement

Is it at the right second, in the right caption?

- [ ] **Every inner timestamp sits inside its own segment window.** A caption for
      `[43.0-54.6]` may not describe anything at `[55.0]`.
- [ ] **Timestamps match the video.** Spot-check three of them by scrubbing to the
      exact moment. The timestamp failure in this project drifted by four to
      sixteen seconds while the descriptions themselves were excellent.
- [ ] **Laughter, coughs, sneezes and breaths are in the Audio caption**, not in
      Speech Caption 2.
- [ ] **Stutters and fillers are in the Speech captions**, not in Audio.
- [ ] **Sung lyrics and unison chants are in the Speech track** with a speaker
      number; the instruments are in the Audio caption.
- [ ] **No visual references in Speech Caption 2.** "as he raises his arm" belongs
      in the Visual caption.
- [ ] **No speech content in the Audio caption.** Unintelligible background
      chatter is ambience and belongs there; anything with words does not.

## Pass 4 — Speech Track Detail

- [ ] Speaker numbers follow **first-speaking order across the whole video** and
      never change.
- [ ] A returning speaker reuses their original number.
- [ ] Fillers kept: `um`, `uh`, `you know`, `I mean`.
- [ ] Repeats and false starts kept: `I, I think`, `that- that`.
- [ ] Cut-off words use a **hyphen**, not an ellipsis: `we shou-`, `th- the`.
- [ ] Nothing has been tidied — no fixed grammar, no completed sentences, no
      corrected facts. A misspoken year stays misspoken.
- [ ] The right tag in the right place:
      `((No speech present))` = nobody is talking;
      `((unintelligible))` = words spoken, cannot be made out;
      `((Non-English speech))` = words spoken, not in English.
- [ ] Simple non-English that a lay viewer would understand is **transcribed**,
      not tagged.
- [ ] Speech Caption 2 names, for each speaker: voice and accent, tone, pace,
      volume, and the timed events — pauses, breaths, stutters, fillers, emphasis
      with the word quoted, and pitch changes.
- [ ] Caption 1 and Caption 2 agree with each other. A stutter written as `more-`
      in Caption 1 should appear as a stutter in Caption 2.
- [ ] Emphasis that changes meaning — stress on one word, sarcasm — is captured.
      This one is mandatory.
- [ ] Ordinary swear words written as spoken. Hateful slurs not written out.

## Pass 5 — Visual Track Detail

- [ ] Shot type and camera movement named for each segment.
- [ ] People described fully: hair, every garment with colour, jewellery,
      glasses, watches, hats, microphones.
- [ ] Position in frame, posture, gestures, and where they are looking.
- [ ] Background and setting described — furniture, objects, screens, lighting.
- [ ] On-screen text quoted **exactly**, character for character.
- [ ] Typos on screen **preserved**, not corrected. `IVE` stays `IVE`.
- [ ] Partly hidden text written only as far as it is readable — `"TEX"`, not
      `"TEXAS"`.
- [ ] Text too small or blurred to read called out as illegible.
- [ ] Text styling noted where visible: colour, position, what it sits on.
- [ ] Persistent elements introduced in full once, then carried forward — "The
      watermark is unchanged" — and never dropped.
- [ ] Numbers copied digit for digit, and re-stated each time they change.
- [ ] In a montage, every shot has its own stamped entry.
- [ ] People without names are identified consistently by a stable feature —
      "player 6", "the woman in the blue-green dress" — with the feature
      introduced in full the first time.

## Pass 6 — Audio Track Detail

- [ ] Music is **described**, not just named: tempo, instruments, volume, mood.
- [ ] Ambience named — crowd, room tone, traffic, static, stadium.
- [ ] Every discrete effect stamped: impacts, whistles, footsteps, doors, horns,
      swooshes, bell dings, engines, applause.
- [ ] Listen to the segment once more **with the picture ignored**. The rugby
      failure missed two referee whistles in an otherwise good caption.
- [ ] Continuing sounds carried forward rather than re-introduced —
      `Background music ((persists))`, or "The upbeat bass music continues in the
      background."
- [ ] No padding about your own listening or about what is absent.

## Pass 7 — Format and Routing

- [ ] Timestamps are seconds with one decimal, in square brackets.
- [ ] Timestamp and speaker-tag style is consistent across the whole task.
- [ ] Speaker tags are `[Speaker 1]`, numbered, never named.
- [ ] The Autochecker shows **zero errors**.
- [ ] Flags are set correctly — see `../references/skip-flag-routing.md`.
- [ ] Destination is right: full annotator → **Submit_to_QC**; Mini qualifying
      task → **Annotator_Skip**.
- [ ] The user's task files were not modified. Captions are in the chat reply.

## The Three Questions

If you only have a minute, ask these:

1. **Is everything that happened in here?** Cuts, text, sounds, speakers, the
   whole clock.
2. **Is everything in here something that actually happened?** No invented music,
   no inferred jobs, no misheard words.
3. **Is it in the right place?** Right second, right window, right caption, right
   track.

Almost every 0% audit in this project failed one of those three.
