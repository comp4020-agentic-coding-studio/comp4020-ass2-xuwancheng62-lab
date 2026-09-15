# Week 2 handoff — Pitch and premise review

Status: content complete
Last updated: 2026-09-15

This file records what's specific to Week 2 only. Standing rules are in
`CLAUDE.md` and `PLAN.md`'s templates — see below, not restated here.

## Next action

No content work outstanding for Week 2 itself. Before touching this week
again, read this file in full, then `CLAUDE.md`'s "Workshop structure:
explicit numbered activities" section, then re-open
`src/content/sessions/02-first-review.md` directly rather than trusting
this summary of it.

## Standing rules that apply

- `CLAUDE.md` → "Workshop structure: explicit numbered activities" —
  `02-first-review.md` now follows this (Activity 1–5, checked below). It
  did not before this pass: its opening phase was an unnumbered "Recap and
  task briefing," the four activities that followed used bold inline
  labels instead of `### Activity N` headings, none had separate
  **Instructions**/**Expected output** parts, and their timings were given
  as ranges (5–10 + 10 + 70–80 + 20–25 + 10 min) rather than fixed minutes
  summing to exactly 120.
- `CLAUDE.md` → "Planning and human–agent decision making" (the trigger
  test) — this was treated as a presentation-only fix, not a planning
  decision: the rule itself says numbered-activity formatting "governs how
  a workshop's phases are presented on the page, not what those phases are
  or a session's `spec:` completion criteria." No `spec:` bullet, no
  learning outcome, and no substantive instruction to students changed —
  only headings, timing allocation, and the Instructions/Expected-output
  split. No `PLAN.md` planning-decision entry was made for this reason;
  `PLAN.md`'s "Assignment 1 — shot-list scope narrowed..." section (which
  first recorded this as an open finding) was updated in place to point
  here instead.
- `CLAUDE.md` → "Curriculum structure: teach → practise → assess" —
  unaffected by this pass; not re-checked here beyond confirming no
  content changed.

## Confirmed decisions

- `02-first-review.md`'s "In the workshop" section is now five numbered
  activities:
  1. Recap and task briefing (10 min)
  2. Warm-up: test a familiar film (10 min)
  3. Write and pair up (70 min)
  4. Dailies review (20 min)
  5. Completion check (10 min)

  Total: 120 minutes. Each activity is a `### Activity N — Title (X min)`
  heading with a bold **Instructions** part and a bold **Expected output**
  part, matching the convention in `04-shot-breakdown.md`.
- The former unnumbered "Recap and task briefing" phase became Activity 1
  (it was Activity 1 in substance already — every other session numbers
  its recap this way).
- Fixed single-value timings replaced the original ranges. The original
  70–80 min "Write and pair up" phase was fixed at 70 min and the original
  20–25 min "Dailies review" phase was fixed at 20 min so the total lands
  on exactly 120; the other three phases already had single values (10, 10,
  10) and were kept as-is.
- No wording of what students actually do was changed beyond what
  splitting into Instructions/Expected-output required — the "Swap roles"
  instruction (previously its own bold aside inside the old Activity 3) is
  now folded into Activity 4's Instructions rather than removed.
- The `spec:` frontmatter bullets (logline naming protagonist/want/
  obstacle; premise filmable in 2–4 min with 1–2 characters and one
  location; partner's independent obstacle read) are unchanged.

## Proposed / not yet confirmed

None outstanding.

## Adjacent-week impact

- **Week 1** (preceding): not reopened this pass; no dependency between
  Week 1's content and this formatting-only fix.
- **Week 3** (following): not reopened this pass; `03-screenplay-workshop.md`
  is the session this numbered-activity convention was originally written
  for (per `CLAUDE.md`'s note under "Workshop structure: explicit numbered
  activities"), so it's already compliant.
- No week beyond these two immediate neighbours was considered, per
  `CLAUDE.md`'s adjacent-weeks-only scope for automatic checks.

## Concurrent work

Unknown — nothing in this session established whether another agent
(Codex or otherwise) is currently active on Week 2's files. Check for
uncommitted changes (`git status`) before editing.

## This week's status

- `02-first-review.md` restructured into five numbered activities (see
  Confirmed decisions above).
- `pnpm typecheck` and `pnpm build` both run on 2026-09-15 after this
  edit: typecheck 0 errors/0 warnings/0 hints; build succeeded, 0
  accessibility violations (49 pages), no broken links, no deck
  structural violations (12 decks checked).

## Not yet rechecked / verification limits

- Nobody has run this workshop start to finish to confirm five activities
  actually fit in 120 minutes as timed (same caveat as recorded for other
  weeks, e.g. `handoffs/week-04.md`).
- Content-level consistency with Week 3's screenplay workshop (which reads
  this week's logline/premise as its starting point) was not re-checked
  beyond confirming no `spec:` bullet or substantive instruction changed.

## Open questions / unresolved issues

None specific to Week 2. The other two findings from the 2026-09-13
12-week review (week 10's untaught-in-workshop montage concept, and the
already-tracked single-scene/multi-scene brief-language ambiguity) are
unrelated to this week and remain tracked in `PLAN.md`'s "Judgement calls"
section.

## Evidence / file pointers

- `src/content/sessions/02-first-review.md`
- `PLAN.md` → "Assignment 1 — shot-list scope narrowed to already-taught
  skills — approved" (records this finding's origin and now points here)
- `src/content/sessions/04-shot-breakdown.md` (the compliant format this
  pass matched)
