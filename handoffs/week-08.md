# Week 8 handoff — Directing the AI performer

Status: real demonstration incomplete; generation paused by owner
Last updated: 2026-09-13

## Next action

None outstanding. Read this file, `CLAUDE.md`, and `PLAN.md` → "Weeks 6–12
depth pass — approved" before making further changes.

## Standing rules that apply

- `CLAUDE.md` → "Curriculum structure: teach → practise → assess",
  "Workshop structure: explicit numbered activities", "Real production
  material, never invented", "Weekly handoff records".
- `PLAN.md` → "Lecture template (90 min)" / "Workshop template (120 min)",
  "Weeks 6–12 depth pass — approved".

## Confirmed decisions

Lecture rewritten around David Mamet's objective/tactic framing, recast as
a three-way diagnostic rubric for a rejected take: is the failure in the
note (vague/mood word), the reference (unlocked/pending bible field), or
the model (ignored a clear note)? A worked diagnosis walks three takes of
the same beat — Take A rejected for a note failure, Take B rejected for a
reference failure (traced to the still-pending kitchen reference), Take C
selected — plus a misconception table and a guided `<details>` judgement
diagnosing a model-failure case.

Session restructured into five numbered Activities (10/50/20/30/10 = 120
minutes): recap and beat selection, generate three takes, diagnose the
rejected takes, group dailies-review, completion check. Both original
`spec:` bullets unchanged (≥3 takes + one-line diagnosis per rejected;
selection justified against intent, not "looked best"). Deck rewritten to
match, including the note/reference/model table and the Take A/B/C worked
diagnosis.

## Proposed / not yet confirmed

None.

## Adjacent-week impact

Builds directly on Week 7's anchor-frame/moment-before vocabulary — this
week's "note" axis of the diagnostic rubric is the same directed-beat
concept Week 7 introduced. The "reference" axis explicitly names Week 5's
still-pending kitchen bible field as a live example of a reference
failure, without resolving it. Feeds Week 9, which assumes students can
already tell a continuity failure from an accepted variance — a related
but distinct diagnostic skill.

## Concurrent work

None known. This pass also touched Weeks 6–7 and 9–12 in the same session.

## This week's status

2026-09-12 validation:
- `pnpm typecheck`: 0 errors, warnings, or hints (whole-project run
  covering Weeks 6–12 together).
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.
- Direct check: session's five Activities sum to exactly 120 minutes.

## Not yet rechecked / verification limits

No end-to-end 120-minute workshop trial was performed. The Take A/B/C
diagnosis is an authored worked example, not a report of an actual
generation — no image or video was actually produced this pass, per "Real
production material, never invented".

## Open questions / unresolved issues

None beyond the still-pending Week 5 kitchen-reference field, used here
only as a teaching example of a reference failure, not resolved.

## Evidence / file pointers

- `PLAN.md` → "Weeks 6–12 depth pass — approved"
- `src/content/lectures/week-08.md`
- `src/content/sessions/08-take-selection.md`
- `src/decks/week-08.deck.mdx`
- `handoffs/week-07.md`, `handoffs/week-05.md` (pending bible fields)

## Sora 2 production update — 2026-09-13

Owner selected the Week 1 Take B source medium frame, requested Week 7
production and reuse of actual waste footage in Week 8. A request returned
moderation_blocked with no video. B completed (8.3s, 1280×720, 30fps, H.264/AAC)
but fingers contact the phone around 3–4s instead of stopping short; reject
for the intended hesitation beat. Raw file, prompts and job records are in
resources/week-07; actual diagnosis is in resources/week-08/materials.md.
Lectures/decks now show the real production status and share the packing-task
antecedent instead of adding previous missed calls. Week 7 shows the reused
anchor; Week 8 embeds the actual rejected video. No accepted comparison,
three-take selection, phone/face inserts or tested repair is claimed.

Owner explicitly paused generation to view the rejected video. Do not submit
more jobs. Sora documentation says human-face input images are rejected; B's
success does not override that restriction. Audio presence checked but not
listened to; inspection used 1fps samples, not a full frame-by-frame review.
Earlier “content complete”/hypothetical A/B/C accounts above are historical;
this update supersedes their example/status claims. Verification: `pnpm check` passed, 0 type diagnostics, no accessibility or
broken-link violations, 12 decks passed, 6 tests passed. Initial build image
path failure corrected before rerun; Google Fonts DNS warnings remain.

## Approved corrections — 2026-09-13

Owner approved review items 1/3/4. Week 5 reference status and version 0.2
records synchronised; kitchen extended geometry approval and voice pending.
Week 7 workshop now uses one fixed antecedent and two performance directions,
with original spec and timings preserved. Week 8 records Sora contact failure
and Jimeng hover improvement plus response-delay failure; no causal repair,
independent completed selection or audio verification claimed. Earlier status
accounts are historical where superseded. Items 2/5 remain unmodified.

Validation for this correction: `pnpm check` passed (0 type diagnostics,
6 tests, no accessibility/broken-link/deck violations). Workshops remain
120 minutes. Google Fonts DNS warnings persist. No deployment performed.

## Review items 2/5 correction — 2026-09-13

Owner approved corrections. Week 6 distinguishes planned opening inputs and
ending targets, fixes action-shot starting states and Nadia/phone dependencies,
and notes shots 1–2 need expanded geometry approval. End images are not required
for every shot. Week 8 teaches mismatch, provisional cause and next check;
review reveals prompt/reference before discussing causes. Prior categorical
model-failure accounts are superseded. Specs and 120-minute timings unchanged.
No new generation, assets, full classroom trial or deployment performed.

Validation: `pnpm check` passed: zero type diagnostics, 6 tests passed, no
accessibility, broken-link or deck-structure violations. Both workshops total
120 minutes. Google Fonts DNS warnings remain; build completed.

## Approved review wording fixes — 2026-09-13

Replaced the misconception table's categorical cause-to-fix claim with observed mismatch, possible cause with uncertainty, and a next check before choosing a fix. Owner authorized these fixes after the Week 7–10 review. Learning outcomes, spec bullets and timings unchanged.

Validation: `pnpm check` passed, zero type diagnostics, 6 tests passed, no accessibility, broken-link or deck-structure violations. Targeted wording checks passed; Week 9 workshop remains 120 minutes. Google Fonts DNS warnings persist. No new generation, playback/listening review or deployment performed.
