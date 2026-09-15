# Week 7 — Before It Stops: real generation record

Status: two owner-generated Jimeng candidates available; exact one-variable comparison not verified. Earlier Sora attempt incomplete.
Source: ../week-05/images/week1-take-b-source-frame.png, 1280×720.
Date: 2026-09-13. Requested model: sora-2 (not sora-2-pro).
Network: same local HTTP proxy as Week 1; credentials were not recorded here.

## Requests and results

- A: job video_6aa6242c59fc8191890b978b75bb7e9402ed6f41691596c8;
  failed, moderation_blocked. No video exists; not a rejected performance take.
- B: job video_6aa6248fe0f081919d6a8b22ac6f7a51082a1aba3d407856;
  completed. Raw take-b.mp4: H.264 1280×720 at 30 fps, AAC audio;
  container duration 8.3 seconds (8 requested).
  SHA-256: 0f1777b9e0923a4bdfe0eed2c22ccdc2e3df92811a114d5f80602047fb7c5872.

Both use the same image and base prompt; planned reach onset A 4.0s, B 2.0s.
Shared antecedent: she has just finished packing her mother's kitchen.
No prior missed calls were added. This is a hesitation shot, not the whole
film or its final acceptance shot. Full prompts and returned job records are
stored alongside the raw output.

## Inspection and selection

Visual check: 1 fps contact sheet sampled 0–7s. B lights the phone and moves
her hand, but fingers reach the phone edge by approximately 3–4s and stay in
contact instead of stopping short. Reject for the intended self-restraint beat;
retain this real video for Week 8. Character/costume and fixed framing appear
broadly stable. Audio stream existence checked; not listened to or transcribed.
No peer review or successful timing comparison is claimed.

## Platform limit and next action

Sora docs currently state that input images containing human faces are
rejected: https://developers.openai.com/api/docs/guides/video-generation#guardrails-and-restrictions
A returned only a generic moderation error, so its exact cause is not proven.
B's success does not override the documented restriction. Do not resubmit
face-input requests to try to get past moderation. Await owner choice of a
supported generation workflow (for example owner-operated Jimeng).
Phone/face anchor copies prepared at 1280×720 are unused, not generated takes.
Week 7 still needs two acceptable motion takes and the planned phone/face
insert sequence; Week 8 has one real rejected take, not a three-take selection.

## Jimeng owner production update — 2026-09-13

Website candidates: `jimeng-take-a.mp4` is copied from original filename
containing `2448`; `jimeng-take-b.mp4` from `3477`. Originals remain unchanged.
Both are 1280×720, 60 fps, approximately 8.096 seconds, with audio streams.

A visibly reaches around 4.5s, then holds short. B screen is lit around 0.5s;
visible reach begins around 2.5–3s and stops around 3.5s, then holds hovering.
B used the owner's simplified direction: phone lights → immediate reach →
stop before contact → hold. It did not achieve an immediate response.
Review used 0.5s samples, closer reach samples and enlarged late frames;
no complete frame-by-frame, audio listening or independent peer review.
Screen appearance and hand pose differ as well as timing. These are usable
performance candidates, not a verified exactly-one-variable pair. The original
anchor is reused, not newly generated from the bible. Inserts remain outstanding.
Original file `4044` is a reserve, not the selected B.
This update supersedes the earlier instruction to await a workflow choice;
owner supplied Jimeng footage. No additional generation jobs were submitted.
