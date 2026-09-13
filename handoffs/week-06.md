# Week 6 handoff — Planning before generating / Assignment 1

Status: content complete
Last updated: 2026-09-13 (A1 pending-decision alignment pass)

## Next action

None outstanding on the pending-decision issue: A1's `spec:` bullets, its
voice instruction, and the surrounding prose now permit "resolved, or
pending with the decision needed" throughout, matching Week 5's own
teaching (see "A1 pending-decision alignment pass — 2026-09-13" below).
Remaining difference still open: Week 6's schedule (7 shots) vs. the
current A1 five-shot screenplay draft — A1 already labels the latter a
method demonstration, not a runtime-complete submission, so this is not an
error, just an unresolved gap noted for a future pass. Read this file,
`CLAUDE.md`, and `PLAN.md` → "Week 6 — bible → keyframes → generated shots
pass — approved" and "Assignment 1 — pending-decision alignment pass —
approved" first.

## Standing rules that apply

- `CLAUDE.md` → "Curriculum structure: teach → practise → assess",
  "Workshop structure: explicit numbered activities", "Real production
  material, never invented", "Weekly handoff records".
- `PLAN.md` → "Lecture template (90 min)" / "Workshop template (120 min)",
  "Weeks 6–12 depth pass — approved", "Week 6 — bible → keyframes →
  generated shots pass — approved".

## Confirmed decisions

Lecture rewritten from outline bullets into the full template: the shot
list as a dependency schedule (not a wish list); a real 7-shot whole-short
schedule extending Week 4's closing five with two new shots covering the
0:00–1:25 segment Week 2 only described in prose; a worked cut (a
fridge-photo insert, dropped because it repeats the reach-and-stop
insert's argument), grounded in AFI's Comprehensive Review format;
misconception table; guided judgement with a `<details>` answer.

Session restructured into five numbered Activities (10/50/20/30/10 = 120
minutes): recap and inventory, expand the sequence, cut and defend,
Comprehensive Review dailies, completion check. Both original `spec:`
bullets and frontmatter unchanged. Deck rewritten to 11 slides matching the
lecture/session content.

**2026-09-13 addition: bible → keyframes → generated shots.** A new
lecture section states the three-tier chain (bible fixes identity;
keyframe fixes one shot's specific still, or a start/end pair for a
continuous shot; generated shot adds performance/action/timing/camera
movement) and that matching keyframes isn't sufficient — the movement
between them still has to be directed and evaluated, developed further in
Week 7. Outcomes list extended to 4 bullets; misconception table gained a
5th row; the "real demonstration" table now traces keyframe(s) → bible
reference(s) → what the generated shot adds per shot, with shot 7 given
two keyframes (start: low on her hand and the phone on the table; end:
phone at her ear for "Hey") as an authored planning example, disclaimed
the same way Week 7 disclaims its own worked takes. A new paragraph
distinguishes narrative order from preparation order (shot 1 vs. shot 6).
Workshop Activities 1, 2, 4, and 5 revised to practise naming keyframes
and bible references and building a preparation list; Activity 3 and both
`spec:` bullets unchanged; total still 120 minutes. Deck gained 5 new
slides; the "whole short as a schedule" slide's stale line removed.

## Proposed / not yet confirmed

None.

## Adjacent-week impact

Reuses Week 4's closing five-shot list unchanged, renumbered as shots 3–7.
Reads Week 5's bible directly. **As of 2026-09-13, this is no longer
"every shot depends on a field still marked pending":** Nadia's appearance
(`nadia-week1-reference-v1`), the kitchen's layout/lighting
(`kitchen-week1-reference-v1`), and the phone reference (carried over from
Week 4) are all now recorded there. One dependency remains genuinely open
— the kitchen reference's full geometry is inferred and its production
approval is still pending (`resources/week-05/materials.md`,
`resources/week-05/week1-derived-generation-v1.md`). Week 7 (next) also
depends on this week's schedule (it directs shot 7's beat specifically);
its one sentence citing "week 6's schedule" flagging pending references
was corrected to match (see `handoffs/week-07.md`). `MANIFEST.md`'s
`BIS-W05-ENTRIES` status cell and revision history were updated to match
this same integration.

## Concurrent work

None known. This pass also touched Weeks 7–12 in the same session; no
other agent is known to be working on these files concurrently.

## This week's status

2026-09-13 validation (bible → keyframes → generated shots pass):
- `pnpm typecheck`: 0 errors, warnings, or hints.
- `pnpm build`: passed — 0 accessibility violations across 49 pages, no
  broken internal links, all 12 decks passed structural checks.
- Direct check: session's five Activities still sum to exactly 120
  minutes (10+50+20+30+10); both `spec:` bullets confirmed byte-identical
  to before this pass via `git diff`.
- Direct check: `grep` confirmed the stale "recorded **pending**" /
  "pending decisions" / "handful of pending" phrasing no longer appears
  anywhere in `week-06.md` or `week-06.deck.mdx`.

2026-09-12 validation (prior pass):
- `pnpm typecheck`: 0 errors, warnings, or hints (run across the whole
  project, covering Weeks 6–12 together).
- `pnpm build`: passed — 0 accessibility violations across 49 pages, no
  broken internal links, all 12 decks passed structural checks.
- Direct check: session's five Activities sum to exactly 120 minutes
  (confirmed by script, not just visual read).

## Not yet rechecked / verification limits

No end-to-end 120-minute workshop trial was performed. The worked cut and
schedule are authored teaching material, not a report of an actual
Comprehensive-Review session. Build checks confirm the site renders
correctly; they don't establish teaching quality.

## Open questions / unresolved issues

- Week 6 lecture still describes a seven-shot 2:10 plan; the current Week 4
  production-planning draft follows the existing single-scene screenplay in
  five shots, estimated 24–38 seconds. A1 explicitly labels the latter as a
  method demonstration, not a runtime-complete submission. Do not invent a
  longer screenplay to close this difference.
- **Resolved 2026-09-13:** the previous entry here about pending
  visual-bible statements has been corrected by this pass (see "Adjacent-
  week impact" above); no further action needed on that point.
- `handoffs/week-05.md` itself is stale — it still says "no image
  generation was performed," which no longer matches `week-05.md`'s
  actual content or `resources/week-05/materials.md`'s 2026-09-13 entry.
  Not fixed in this pass, since it wasn't necessary for Week 6's own
  correctness and Week 5's own lecture/session text was already accurate.
  Flagging for whoever next touches Week 5.

## Evidence / file pointers

- `PLAN.md` → "Weeks 6–12 depth pass — approved", "Week 6 — bible →
  keyframes → generated shots pass — approved"
- `src/content/lectures/week-06.md`
- `src/content/sessions/06-preproduction-crit.md`
- `src/decks/week-06.deck.mdx`
- `src/content/lectures/week-07.md` (one-sentence sync)
- `resources/week-04/shot-list-template.html` (reused, not duplicated)
- `resources/week-05/materials.md`,
  `resources/week-05/week1-derived-generation-v1.md` (visual-integration
  provenance)
- `MANIFEST.md` → `BIS-W05-ENTRIES` (status cell + revision history
  updated 2026-09-13); OWN-W06 (unchanged, OWNER REQUIRED/TBD)

## Assignment 1 update — 2026-09-13

Owner requested worked guidance using “Before It Stops” and a finer spec.
The assessment page now walks through story, screenplay/intent, bible,
shot list/storyboard and dependency checks; specifies one PDF and complete
2–4 minute film coverage; explains existing 30/30/40 marking categories.
No dates or weights changed. Course draft examples retain their limitations:
short current screenplay, pending voice, no claim of actual peer testing.
Served a copy of the existing five-shot planning draft under
`public/resources/week-04/before-it-stops-shot-list.md` for the A1 link.
No new owner evidence is claimed.

Verification (2026-09-13): `pnpm check` passed: typecheck 0 errors/warnings/hints;
build passed, 49 pages checked for accessibility and internal links, no broken
links, 12 decks passed structural checks; 2 test files / 6 tests passed.
Google Fonts metadata fetch failed due to DNS; build completed with font-provider
warnings. No actual reader trial or production rehearsal was performed.

### A1 reference-link cleanup — 2026-09-13

Owner reported garbled linked files and preferred removing references.
Removed all A1 download/resource links and the Week 5 reference-page link;
kept the inline examples and added a screenplay excerpt and staging guidance.
Removed example image filenames that required leaving the page. Resource
files themselves were not edited or deleted, and no encoding repair is
claimed. The assessment spec and weights are unchanged. Verified the page
has no remaining resource links, no Unicode replacement characters and
balanced code fences; full build was not repeated for this wording/link edit.

Follow-up: the screenshot revealed stale `dist` output after link cleanup.
Rebuilt with `pnpm build` successfully (same Google Fonts DNS warnings), then
verified the generated A1 HTML contains none of the removed resource links.

### A1 pending-decision alignment pass — 2026-09-13

Owner reported A1 "has the same problems" as Week 6's raw-filename issue,
and specifically that it "can not require voice or something not learned as
spec." Confirmed: `spec:` bullets 6 and 10 required every bible decision
"resolved" with no pending exception, and section 3 demanded voice be
"resolved" outright — contradicting Week 5's own taught pending model
("An undecided field should say pending, with the decision needed to close
it") and the course's own worked example, which itself leaves Nadia's voice
pending. No lecture/workshop by week 6 teaches selecting or generating an
actual voice reference (that's Week 11). See `PLAN.md` → "Assignment 1 —
pending-decision alignment pass — approved" for the full approval record.

Fixed: `spec:` bullets 6 and 10, the "Locked" definition, section 3's voice
instruction and its Nadia/Theo sentence, section 5's dependency and closing
paragraphs, the package intro paragraph, and the "World and continuity
design" marking row now all read "resolved, or explicitly marked pending
with the decision needed to close it," matching Week 5's own language. A
pending decision still blocks a *shot* (production-order discipline,
unchanged); it no longer blocks *submission*. No submission section,
marking weight, or due date changed.

Verification (2026-09-13): `pnpm typecheck` 0 errors/warnings/hints;
`pnpm build` passed — 0 accessibility violations, no broken internal links,
all 12 decks passed structural checks. Direct check: `grep` for "resolve
the vocal design" and "no required decision remains pending" in
`assignment-1.md` returns nothing.
