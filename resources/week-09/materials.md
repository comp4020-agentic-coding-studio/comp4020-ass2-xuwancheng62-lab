# Week 9 — production materials

Status: shot 02 v2 accepted as usable by owner on 2026-09-13.
Selected production footage: `shot-02-sora2-v2.mp4` (with generated audio).
The earlier silent version is retained as a superseded candidate.

Generated 2026-09-13 at owner request with sora-2, 4 seconds requested, 1280×720.
Input: Week 4 bis-02-phone-week1-v1.png, resized to 1280×720 as shot-02-anchor.png.
Prompt: shot-02-prompt.txt. Job: shot-02-job.json.
Original output: shot-02-sora2-raw.mp4, unchanged.
Delivery: shot-02-sora2.mp4, video stream copied, audio removed, fast-start enabled.
Measured delivery: H.264 1280×720, 4.2 seconds, no audio stream.
Visual inspection: 2 fps contact sheet across 0–3.5 seconds; THEO CALLING remains readable, no hands enter, framing broadly stable. Subtle vibration is not confirmed by these sparse samples; no full playback or peer review claimed. Cross-shot phone-screen design continuity remains to be checked against the chosen Week 7 take.

## Shot 02 v2 — owner requested vibration sound and physical movement

Generated with sora-2, 4 seconds requested. Prompt: shot-02-v2-prompt.txt; job: shot-02-v2-job.json; same anchor.
Output shot-02-sora2-v2.mp4 retains original generated audio and video, unmodified.
Measured: 4.3 seconds, H.264 1280×720 plus AAC stereo audio. Audio is non-silent, mean -19.6 dB, peak -9.2 dB.
4 fps visual samples show slight phone position/angle changes, readable THEO CALLING, no hands and broadly fixed framing. Full playback, listening, exact vibration/audio synchronization and peer review have not been verified.

Owner review — 2026-09-13: owner confirmed shot-02-sora2-v2.mp4 is acceptable and requested it be marked usable. This is owner acceptance; no independent peer review is claimed.

## Shot 01 — Jimeng owner delivery

Status: completed per owner on 2026-09-13; selected footage `shot-01-jimeng.mp4`.
Source: `/Users/miles/Downloads/jimeng-2026-09-13-7486-使用上传图片作为首帧。固定机位，Nadia 全程坐在原位，安静地看着桌上的手机。....mp4`.
Copied unchanged; source retained. SHA-256: a8d634d50f6f237f7c2f5f9be0c6ef5b245e2954995c3a98ad8b17d30ecde9c5.
Measured: 6.080 seconds, H.264 1280×720 at 60 fps, AAC audio stream.
Owner reports shot 01 completed. No visual playback, audio listening or independent review by Codex is claimed; audio-stream presence does not establish its content.

## Shot 03 — generation attempt

Sora-2 image-to-video request on 2026-09-13, 8 seconds, 1280×720. Reference: shot-03-anchor.png derived from Week 4 bis-03-face-week1-v1.png. Prompt: shot-03-prompt.txt; job: shot-03-job.json.
Status: failed, moderation_blocked. No video produced. Exact moderation cause not supplied; no retry submitted. Shot 03 remains outstanding.

## Shot 05 — Jimeng owner delivery

Status: completed per owner on 2026-09-13; selected footage `shot-05-jimeng.mp4`.
Source: `/Users/miles/Downloads/jimeng-2026-09-13-2525-桌上的手机亮着并且震动，女人看着手机，点击接通，放到耳边轻声说一次 “Hey”，....mp4`.
Copied unchanged; source retained. SHA-256: b787a81538fb5abc8a62fb179a8a337d63e3fc47c33d5a88a74a6221dab64308.
Measured: 8.096009 seconds, H.264 1280×720 at 60 fps, AAC audio stream.
Owner reports shot 05 completed. No Codex visual playback, audio listening or independent review claimed; filename describes intended action and is not verification of its performance or dialogue. Cross-shot continuity remains to be checked in assembly.

## Shot 03 — Jimeng owner delivery

Status: delivered by owner on 2026-09-13; recorded as completed shot 03. Selected footage: `shot-03-jimeng.mp4`. Supersedes the failed Sora attempt as production material; failed job record retained.
Source: `/Users/miles/Downloads/jimeng-2026-09-13-9776-使用上传图片作为首帧。固定人物近景，Nadia 全程安静地看着画面外右下方的手机....mp4`.
Copied unchanged; source retained. SHA-256: 98a60f9f6c0248227b1da3f514b1e796d6d91db4633e2b47ed94c89d3b2aeed0.
Measured: 6.080 seconds, H.264 1280×720 at 60 fps, AAC audio stream.
No Codex visual playback, audio listening or independent review claimed.

## Current sequence inventory

1. `shot-01-jimeng.mp4` — owner completed.
2. `shot-02-sora2-v2.mp4` — owner accepted usable.
3. `shot-03-jimeng.mp4` — owner delivered as shot 03.
4. Week 7 Jimeng A/B — existing reach-and-hover candidates; final choice remains to be confirmed.
5. `shot-05-jimeng.mp4` — owner completed.

Footage exists for all five positions. No assembled cut, 30–60 second runtime verification or continuity log is claimed yet.

## Assembly v1

Output: `week-09-assembly-v1.mp4`. Edit timeline: `assembly-v1-timeline.json`. Review: `continuity-log-v1.md`.
Shots 01→02→03→04→05, using Week 7 Jimeng B for shot 04 provisionally. Shot 04 begins at source 1.3 seconds to remove its dark-phone opening. Hard cuts, final 0.5-second picture/audio fade. Source audio retained. All source files unchanged.
This is a reviewable assembly draft; phone-interface continuity and listening review remain outstanding.

## Week 9 completion — 2026-09-13

Core real-production artefacts complete and integrated into lecture/deck: five-shot 31.233333-second assembly plus actual continuity log. Canonical/served copies hash-match. Typecheck and build passed, including accessibility/link/deck checks. Audio listening and independent group review are not claimed. See handoffs/week-09.md for completion scope and limits.
