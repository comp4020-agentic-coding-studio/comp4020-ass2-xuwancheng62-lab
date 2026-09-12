# Week 4 handoff — Thinking in shots

Status: content complete, pending owner evidence
Last updated: 2026-09-12

This file records what's specific to Week 4 only. Standing rules are in
`CLAUDE.md` and `PLAN.md`'s templates — see below, not restated here.

## Next action

No content work outstanding for Week 4 itself. The next concrete action is
external: the owner producing `OWN-W04` (their own numbered shot list plus
rough thumbnail per shot, built on their own `OWN-W03` scene). Before
touching this week again, read this file in full, then `CLAUDE.md`'s
"Workshop structure: explicit numbered activities" and "Curriculum
structure: teach → practise → assess" sections, then re-open
`src/content/lectures/week-04.md` and
`src/content/sessions/04-shot-breakdown.md` directly rather than trusting
this summary of them.

## Standing rules that apply

- `CLAUDE.md` → "Workshop structure: explicit numbered activities" —
  `04-shot-breakdown.md` follows this (Activity 1–5, checked below).
- `CLAUDE.md` → "Curriculum structure: teach → practise → assess" — Mamet's
  shot-as-argument technique and the shot vocabulary/composition/blocking
  content are taught in `week-04.md` before the workshop practises them;
  the workshop introduces no new directing concept of its own.
- `CLAUDE.md` → "Curriculum review" — any check against week 3 or week 5
  content beyond what's recorded here is project-wide-review territory and
  needs explicit approval first; see "Adjacent-week impact" below for what
  has and hasn't actually been checked.
- `PLAN.md` → "Lecture template (90 min)" and "Workshop template (120
  min)" — `week-04.md` and `04-shot-breakdown.md` follow these shapes; see
  `PLAN.md`'s "Session content depth pass" → "Week 4 shot-as-argument pass"
  for the week's specific design.

## Confirmed decisions

- The real demonstration shot-lists the five closing "Before It Stops"
  beats (from `week-03.md`) into five shots: wide (kitchen/phone lighting
  up) → insert (screen reading THEO CALLING) → close-up (her still face) →
  insert (hand drifting toward the phone, stopping) → close-up (hand
  closing over the phone as she says "Hey"). Each shot's purpose is unique;
  none repeats.
- `04-shot-breakdown.md`'s "In the workshop" section is five numbered
  activities (Activity 1–5), each with a title, exact timing, an
  **Instructions** part, and an **Expected output** part. Minutes: 10 + 40
  + 35 + 25 + 10 = 120.
- The session's two `spec:` bullets (numbered shot list with type + rough
  thumbnail per shot; one-clause purpose per shot, none repeated) are
  unchanged since they were first written.
- The stale pre-correction ending ("the call would go to voicemail, her
  hand finally moving toward the phone") that had persisted in
  `week-04.md`'s outline and `week-04.deck.mdx`'s closing quote slide is
  fixed to the current canonical ending (she accepts on the final ring and
  says "Hey").

## Proposed / not yet confirmed

None outstanding. The lecture rewrite, workshop restructure, and deck fix
proposed for this pass have all been implemented and are recorded above as
confirmed, not proposed.

## Adjacent-week impact

- **Week 3** (preceding): supplies the scene, intent note, and five
  observable beats this week's shot list is built from. The stale-ending
  bug (above) was found by checking this week directly against Week 3's
  current, corrected content — now fixed.
- **Week 5** (following): checked directly and found still in the
  pre-depth-pass skeleton shape — `05-world-bible-crit.md`'s "In the
  workshop" has no numbered activities or named durations. `PLAN.md`'s
  mapping table already marks Week 5 "already solid... only add named
  durations/phases," so it's next in line for the same kind of pass. Not
  actioned here — recorded as an open question below.
- No week beyond these two immediate neighbours has been considered, per
  `CLAUDE.md`'s adjacent-weeks-only scope for automatic checks.

## Concurrent work

Unknown — nothing in this session established whether another agent
(Codex or otherwise) is currently active on Week 4's files. Check for
uncommitted changes (`git status`) before editing.

## This week's status

- `week-04.md`, `04-shot-breakdown.md`, and `week-04.deck.mdx` are written
  and internally consistent (see Confirmed decisions above).
- `pnpm typecheck` and `pnpm build` both passed on 2026-09-12: 0 type
  errors, 0 accessibility violations, no broken links, no deck structural
  violations. Run immediately after this pass's edits to `week-04.md`,
  `04-shot-breakdown.md`, and `week-04.deck.mdx`.

## Not yet rechecked / verification limits

- Content-level consistency (shot list ↔ week 3's beats ↔ deck) was
  confirmed by direct read in the session that wrote this handoff, not by
  an automated check — typecheck/build catch structural and link issues,
  not whether the shot list's five purposes are genuinely non-duplicative
  to a reader who hasn't just written them.
- Nobody has yet run the shot-breakdown workshop on a real scene start to
  finish to confirm five activities actually fit in 120 minutes as timed.

## Open questions / unresolved issues

- `OWN-W04` (the owner's own shot list + thumbnails, `MANIFEST.md` section
  1) is still `OWNER REQUIRED` / TBD — the teaching demonstration above
  does not and cannot satisfy it. Resolves only when the owner produces
  their own, built on their own `OWN-W03` scene.
- Week 5's session (`05-world-bible-crit.md`) still needs the same
  depth-pass/activity-numbering treatment this week just got — flagged,
  not actioned, per scope above. Whoever picks up Week 5 should treat this
  as its starting point, not rediscover it.
- `OWN-W03` (Week 3's owner evidence, still outstanding per
  `handoffs/week-03.md`) blocks this week's own owner evidence in turn,
  since `OWN-W04` is built on it.

## Evidence / file pointers

- `src/content/lectures/week-04.md`
- `src/content/sessions/04-shot-breakdown.md`
- `src/decks/week-04.deck.mdx`
- `MANIFEST.md` row `OWN-W04`, and the "2026-09-12 (Week 4 shot-as-argument
  pass)" revision-history entry
- `PLAN.md` → "Session content depth pass" → "Week 4 shot-as-argument pass"
  and the matching 2026-09-12 Revision history entry
