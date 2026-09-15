---
title: Directing the AI performer
description:
  Generation as rehearsal and takes — diagnosing failure, giving actionable
  notes, and selecting a take on purpose instead of regenerating until
  something looks right
week: 8
date: 2027-04-19
teachers:
  - idris-fenn
slides: /decks/week-08/
related:
  - sessions/08-take-selection
  - assessments/final-project
---

Treat every generation as a take, not a result — rehearsal implies you
expected some of them to fail. The skill this week is naming exactly how a
take failed, and directing the next one at that specific failure.

## What you'll be able to do

- Treat a failed generation as an expected part of rehearsal, not a
  surprise to regenerate away from.
- Diagnose a failed take against the beat's objective and tactic, and
  evaluate possible note, reference or model causes and propose a check.
- Write an actionable note aimed at a named failure, and select a take by
  justifying it against the beat's original intent.

The lecture runs 90 minutes: recap 5, outcomes 5, technique and worked
diagnosis 45, comparison 15, judgement practice 15, synthesis 5.

## Generation as rehearsal

Week 7 directed a single beat by giving it a moment-before and reading the
result. This week scales that up: across several takes of the same beat,
some will fail, and a failed take is not evidence that the process is
broken — it's what rehearsal looks like. A director who is surprised every
time a take doesn't work is still treating generation as a vending
machine, not a rehearsal room. The discipline is to expect failure, and to
have a way of reading it.

## Diagnosing against objective and tactic

David Mamet's frame for a shot is that it argues something — it exists to
serve the scene's objective, through a specific tactic. That same frame
works as a diagnostic rubric for a failed take: does this take serve the
beat's objective, played through its stated tactic? If it doesn't, the
next question is *why not*. Use three areas to investigate, rather than
assuming the visible mismatch proves a single cause:

- **The note.** Does it give a playable circumstance and a visible action,
  or only a mood? Does it state when to move and where to stop? If a necessary
  instruction is missing or conflicting, revise that instruction.
- **The reference.** Does the actual supplied image support the requested
  opening pose and geometry? Check it against the locked bible and tool
  inputs. A locked reference can still be unsuitable for this action.
- **The model or workflow.** Did the generation fail to follow a clear,
  supported instruction despite suitable inputs? This is a possible cause,
  not something established by attractive wording alone. Check what was
  submitted, tool support and repeated results before assigning confidence.

Record the observed mismatch first, then a possible cause with uncertainty,
and one next check. Where useful, repeat the same supported setup to check
variability; if testing a revised note or reference, change one thing at a
time. Multiple causes may interact. Do not replace “unknown” with a confident
label merely to fill the log.

## A real rejected take from Week 7

This is an actual `sora-2` output generated from the Week 7 medium starting
frame on 13 September 2026. The original file is retained without a simulated
failure or a repaired replacement presented as if already generated.

<video src="../../resources/week-08/rejected-take-b.mp4" controls width="100%" aria-label="Rejected Sora 2 take: Nadia reaches and contacts the phone instead of stopping short"></video>

**Objective:** Nadia wants contact with Theo but holds herself back.
**Tactic in this beat:** an attempted reach that she stops before contact.
The shared moment-before is that his call interrupts the end of packing her
mother's kitchen. No earlier missed call is added to the story.

**Direction given:** light the screen at 0.8 seconds; begin the right-hand
reach at 2 seconds; stop short by 3 seconds and hold; no touch, pickup or
acceptance. Fixed medium shot, same reference throughout.

**What happened:** sampled frames around 3–4 seconds show fingers settling
onto the phone edge, with contact retained in the closing frames. The stopped
gap is missing. Her identity, costume and framing appear broadly stable,
but those strengths do not make the intended self-restraint readable.

**Decision:** reject for this beat. The generated action did not preserve
the written no-contact boundary. That is an observed mismatch, not proof
that the model alone caused it: inspect whether the starting pose, oblique
angle and instruction make the stopping boundary clear enough first.

## Later Jimeng candidates — what improved, what still failed

The owner subsequently generated Jimeng footage from the same starting image.
The revised direction kept the hand hovering instead of withdrawing it:
“Phone lights up → immediate reach → stop before contact → hold until the end.”
This supersedes the earlier proposed withdraw-to-lap note; no generated
withdrawal repair is claimed.

[Watch delayed A and earlier B in Week 7](/lectures/week-07/).

| Take | Observed behaviour | Decision against the direction |
|---|---|---|
| Original Sora B | Fingers contact the phone around 3–4s and stay | Reject: the required stopping gap is missing |
| Jimeng A (`2448`) | Reaches around 4.5s, then holds short in sampled frames | Retain as delayed-reach candidate; onset is later than the requested 4s |
| Jimeng B (`3477`) | Screen lit by about 0.5s; reaches around 2.5–3s, stops around 3.5s and holds hovering | Retain as earlier-reach candidate; reject against the strict immediate-response instruction |

**What improved:** sampled Jimeng frames show a visible gap and sustained
hovering. **What remains:** B still waits before reaching, so the immediate
impulse is not fully realised. A next direction could target only that delay:
“Begin moving the hand at the same moment the screen lights up; keep the
existing stop and hold.” This further instruction has not been tested.

The platform and prompts changed together. These observations do not prove
which change improved the stopping gap, or establish a controlled repair.
Screen appearance and final hand pose also differ. There are now multiple
real takes to discuss, but no completed three-take selection with independent
review is claimed. The original Sora A moderation block produced no footage
and is not counted as a performance take.

**Review limits:** Jimeng assessment used sampled frames and enlarged hand
views, not a complete frame-by-frame review. Audio streams exist but have not
been listened to; audible ringing and sound continuity remain unverified.

For a classroom diagnosis, screen the clip first and ask what behaviour is
visible. Then reveal the note and reference before discussing likely causes.
Appearance alone cannot tell the group whether a note, reference or model
was responsible.

## Actionable direction, not "more/better"

"Make it better" has nowhere to land, for the same reason "more dramatic"
had nowhere to land in week 7 — it names no antecedent and diagnoses no
specific failure. A note aimed at a named failure states what changes:
*"she looks at the phone before the final ring, not after it starts,"* or
*"hold the stillness half a second longer before the reach begins."* Each
names a concrete, checkable difference from the rejected take.

## Misconception contrast

| Regenerating until it looks right | Diagnosing, then directing the next take |
|---|---|
| Every failed take is a surprise | A failed take is expected, and read for its cause |
| "Try again" is the only response | Record the mismatch, a possible cause with uncertainty, and a next check before choosing a fix |
| Selection is "which one do I like" | Selection is justified against the beat's objective and tactic |
| A vague note gets vaguer with each retry | A note names the specific antecedent or failure it targets |

## Guided judgement: which of the three failed?

A practice take uses the note “her brother's call interrupts her final
packing task; wait before reaching,” with a locked character reference.
The output reaches immediately. Name the observed mismatch, a possible cause,
and the next evidence you would check.

<details>
<summary>Compare your diagnosis</summary>

The visible mismatch is an immediate reach instead of a delayed one. The
antecedent is concrete, but “wait” does not specify a duration, and locking
identity does not prove the actual input pose supports the action. Model
variability is another possibility. Inspect the submitted prompt, actual
reference and supported controls before assigning a cause. A next test could
specify a visible stillness interval while holding the reference and other
settings fixed. An unchanged repeat can instead test variability. State which
question your test answers; neither observation proves a unique cause.

</details>

For the workshop, use the same log structure: observed mismatch → possible
cause and confidence → next verification. Justify rejection by what happened,
even when its cause is unresolved.

## What you take to the workshop

Bring one performance beat from your film that hasn't worked cleanly yet.

You leave with three takes, a one-line diagnosis for each rejected one,
and a selection you can justify against the beat's original intent — the
habit of a shot log, kept for every beat from here on.
