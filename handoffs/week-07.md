# Week 7 handoff — From frame to performance

Status: owner-generated Jimeng A/B candidates embedded; verification gaps remain
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

Lecture rewritten around Judith Weston's "moment before" as a concrete
antecedent, not a mood word — an anchor frame locked from Week 6's
schedule, then two directed takes of the same beat differing only in one
named beat before the action (Note A: "she has already let this ring out
once before" vs Note B: "this is the first time it has rung tonight").
Misconception table and a guided `<details>` judgement (diagnosing "make
her hesitation more dramatic" as a mood-word failure) included.

**Ending text corrected.** The lecture and deck previously described the
pre-fix ending ("her hand finally moving toward the phone," implying she
never answers). Both now correctly state she accepts the call on the final
ring, lifts the phone to her ear, and says "Hey" — matching the canonical
ending established in Weeks 3/4. This is the same class of bug as the
Week 4 fix already on record in `MANIFEST.md`.

Session restructured into five numbered Activities (10/20/60/20/10 = 120
minutes): recap and shot selection, write the moment before, generate the
anchor and two takes, dailies-review screening, completion check. Both
original `spec:` bullets unchanged (anchor image matching bible + two
motion takes differing by one directed beat; naming which direction
changed in performance language). Deck rewritten to match, including the
Note A/Note B/Take A/Take B slide.

## Proposed / not yet confirmed

None.

## Adjacent-week impact

Directs shot 7 of Week 6's schedule specifically (the continuous
close-up that tilts up as she accepts and says "Hey"). The ending-text fix
here brings this week back into agreement with Weeks 3/4's canonical
ending; before this pass, Week 7 was the one place in the site still
describing the old, wrong ending. Feeds Week 8, which reuses the same
anchor-frame/moment-before vocabulary for its diagnostic rubric.

## Concurrent work

None known. This pass also touched Weeks 6 and 8–12 in the same session.

## This week's status

2026-09-13 re-validation (Week 6 bible → keyframes → generated shots
pass, one-sentence sync only): `pnpm typecheck` 0 errors/warnings/hints;
`pnpm build` passed — 0 accessibility violations, no broken links, all 12
decks passed structural checks. Confirmed only the one sentence named in
"Not yet rechecked" above changed in this file; anchor-frame, moment-
before, worked takes, misconception table, and guided judgement all
unchanged.

2026-09-12 validation:
- `pnpm typecheck`: 0 errors, warnings, or hints (whole-project run
  covering Weeks 6–12 together).
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.
- Direct check: session's five Activities sum to exactly 120 minutes.
- Direct check: `grep` confirmed no remaining occurrence of the old
  "hand finally moving toward the phone" phrasing anywhere in
  `src/content/lectures/week-07.md` or `src/decks/week-07.deck.mdx`.

## Not yet rechecked / verification limits

No end-to-end 120-minute workshop trial was performed. Take A/Take B are
an authored worked example, not a report of an actual generation — no
image or video was actually produced this pass, per "Real production
material, never invented".

**Recheck performed 2026-09-13:** the Week 5 bible recheck this section
previously named as outstanding was done as part of `PLAN.md`'s "Week 6 —
bible → keyframes → generated shots pass — approved". Nadia's appearance,
the kitchen reference, and the phone reference were confirmed generated
and integrated into `week-05.md` on 2026-09-13
(`resources/week-05/materials.md`); the kitchen's full production approval
remains the one open item. Result: one sentence in this lecture's "The
anchor frame is a locked starting point" section — previously citing
"week 6's schedule" flagging several references as pending — was
corrected to state that the anchor is generated from whichever bible
reference(s) a shot needs, and that only the kitchen's pending production
approval still blocks a shot tied to it. Everything else in Week 7
(anchor-frame concept, moment-before technique, the worked Note A/Take A
vs. Note B/Take B example, misconception table, guided judgement) is
confirmed unaffected and unchanged.

## Open questions / unresolved issues

None beyond the kitchen reference's still-pending production approval
(not this week's to resolve) — Nadia's appearance and the phone reference
are no longer open, as of the 2026-09-13 recheck above.

## Evidence / file pointers

- `PLAN.md` → "Weeks 6–12 depth pass — approved" (documents the ending fix
  explicitly)
- `MANIFEST.md` → revision history, "2026-09-12 (Weeks 6–12 depth pass)"
  entry (documents the ending fix paralleling the Week 4 fix)
- `src/content/lectures/week-07.md`
- `src/content/sessions/07-anchor-to-motion.md`
- `src/decks/week-07.deck.mdx`
- `handoffs/week-06.md`, `handoffs/week-04.md` (canonical ending precedent)

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

## Jimeng website update — 2026-09-13

Owner requested website update after generating Jimeng footage. Lecture embeds
`2448` as delayed A and `3477` as earlier B via descriptive public filenames;
deck and materials reflect observed timing and uncertainty. B does not reach
immediately (around 2.5–3s versus A around 4.5s). Both hover in sampled frames;
screen/hand-pose differences prevent claiming an exact one-variable comparison.
Audio, peer review, new bible-derived anchor and inserts remain unverified.
No workshop spec or learning outcome changed. Earlier Sora pause/failure records
are historical; no new jobs submitted. This update supersedes earlier claims
that no motion comparison footage exists.

Validation: `pnpm check` passed: 0 type diagnostics, 6 tests passed, no
accessibility, broken-link or deck-structure violations. Google Fonts DNS
warnings persist. Website files updated locally; no deployment performed.
