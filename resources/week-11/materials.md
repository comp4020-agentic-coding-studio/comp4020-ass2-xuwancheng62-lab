# Week 11 — sound materials in production

Started 2026-09-13 at owner request. Working picture: Week 10 Cut A (31.233333 seconds), provisional, not owner final-cut selection. No picture regeneration or change.

## Produced

- `source-audio-cut-a.wav`: actual original Cut A audio extracted to stereo 48 kHz PCM; not isolated dialogue, not a new directed take.
- `ambience-kitchen-candidate.wav`: original procedural low hum and filtered noise, proposed quiet kitchen sound signature. Not a location recording or approved bible entry.
- `sfx-incoming-call-candidate.wav`: original synthesized phone motif, starts 6.067s, ends 23.167s. Timing targets shot boundaries; actual screen activation and acceptance synchronization remain to check.
- `music-reach-cue-candidate.wav`: original sustained A3/E4 dyad, enters 16.4s at reach-shot entry, fades out at end. Editorial intent: place the musical claim on attempted contact rather than on the first phone light.
- `sound-bed-audition.wav`: ambience/SFX/music audition only, without dialogue or picture; not the completed full sound pass.
- `generate-stems.py`: reproducible original synthesis, fixed random seed.
- `stem-verification.json`: WAV format, duration, peak and hashes. Technical verification does not imply listening review.

## Initial voice brief — superseded by synthesis below

Canonical line: **Hey.** Shared circumstance: Theo's call interrupts Nadia's final packing task in her mother's kitchen; she eventually accepts. No previous missed call or voicemail added.

Keep speaker identity, wording, recording setup and delivery pace fixed. Vary only hesitation before the word:

- A: begin “Hey” promptly after a quiet inhalation.
- B: after the same quiet inhalation, hold a half-second before beginning “Hey.”

Generate/record two actual performances; do not construct B by adding silence to A and call it a directed second take. Listen before choosing; selection and rationale remain pending. Voice identity is awaiting owner input.

## Direct synthesis and aligned renders — 2026-09-13

Owner explicitly requested direct synthesis and alignment. Two actual independent macOS Samantha syntheses say “Hey.”: A at 150 wpm, B at 105 wpm; vary delivery pace only, not added silence. Original AIFF and trimmed 48 kHz WAV/MP3 takes retained. A is 0.360729s, B 0.396708s. A is provisionally used in the main pair for its shorter timing window, not presented as an audition-based emotional selection.

- `dialogue-only.mp4`: unchanged Cut A picture, only synthesized A dialogue.
- `full-sound-pass.mp4`: same picture and dialogue, plus ambience, aligned call SFX and music.
- `full-sound-pass-take-b.mp4`: optional alternate slower voice, same sound design.
- `no-music-control.mp4`: same dialogue/ambience/SFX as primary full pass, music removed.
- `build-aligned-mixes.py`, aligned WAV mixes and `alignment-verification.json`: reproducible rendering, timings and verification.

Original source audio is excluded from all new renders to avoid retaining unknown music, speech or ringing; extracted original audio remains separately available. All picture streams copied without re-encoding.

Alignment on the Cut A timeline: incoming-call SFX begins 6.067s (caller insert), stops 24.1s near the visible answer interaction; music enters 17.6s near actual reach onset rather than at the shot boundary; “Hey” begins 27.8s, after the phone reaches her ear around 27.7s. Ending reviewed at 4fps with 10fps samples from 27.3–28.9s. Mouth remains open across multiple frames: this is event-aligned ADR, not verified phoneme-exact lip sync. No picture change or time stretch applied.

## Beat comparison — intentions to audition

| Beat | Dialogue-only | Full pass — intended contribution |
|---|---|---|
| Wide / waiting | Quiet | Continuous low hum proposes a still kitchen |
| Caller insert | Quiet | Phone motif makes the interruption audible |
| Reaction | Quiet | Repeated phone motif sustains pressure while the picture holds |
| Reach / hover | Quiet | Sustained music enters with attempted contact, drawing attention to the choice |
| Acceptance / “Hey” | Synthesized line | Ring ceases at answer interaction; ambience and cue continue beneath the same line |

These are mix intentions, not measured audience reactions. Remaining: playback/listening, exact mouth fit, voice approval, final Cut A/B selection, approved location sound signature and an audition-based voice-selection rationale. No final film, learner assessment completion or deployment claimed.

## Review checklist

Listen to original audio for existing speech/ringing/music before replacing or retaining it. Check the actual acceptance action and mouth movement for “Hey”; shot entry alone is not proof of sync. Confirm sound signature, cue timing, mix balance and no clipping by playback. Compare versions before describing emotional results; until then, descriptions are intentions.

## Content issue found while preparing

Week 11 guided judgement still mentions an earlier unanswered ring tonight; this conflicts with the established packing-task antecedent. The old handoff also calls phone/wardrobe fields pending. These stale statements were recorded, not changed as part of asset production. Current voice/sound identity remains unapproved. No teaching examples integrated yet. Asset production has continued below without changing that teaching text.

## Website integration — owner approved 2026-09-13

Actual voice pair, primary dialogue/full-pass, no-music control, B alternate and comparison integrated into Week 11 lecture/deck. Seven served files hash-match canonical copies. Owner approved applying the primary mix; A remains the primary teaching selection, independent review and final-film cut choice are not inferred. Earlier not-integrated accounts above are historical. The lecture now uses the established packing-task antecedent.
