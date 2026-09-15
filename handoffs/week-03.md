# Week 3 handoff — From story to screenplay

Status: content complete, pending owner evidence
Last updated: 2026-09-12

This file records what's specific to Week 3 only. Standing rules are in
`CLAUDE.md` and `PLAN.md`'s templates — see below, not restated here.

## Next action

No content work outstanding for Week 3 itself. The next concrete action is
external: the owner producing `OWN-W03` (their own scene + intent note).
Before touching this week again, read this file in full, then
`CLAUDE.md`'s "Workshop structure: explicit numbered activities" and
"Curriculum review" sections, then re-open
`src/content/sessions/03-screenplay-workshop.md` and
`src/content/lectures/week-03.md` directly rather than trusting this
summary of them.

## Standing rules that apply

- `CLAUDE.md` → "Workshop structure: explicit numbered activities" —
  `03-screenplay-workshop.md` follows this (Activity 1–8, checked below).
- `CLAUDE.md` → "Curriculum structure: teach → practise → assess" — the
  antecedent-circumstance technique is taught in `week-03.md` before the
  workshop practises it; the worksheet's mechanics are workshop-taught,
  which is allowed.
- `CLAUDE.md` → "Real production material, never invented" — applies, and
  is satisfied, not exempted: `BIS-W03-SCENE` and `BIS-W03-WORKSHEET` are
  themselves the actual authored teaching artefacts (the scene text and
  worksheet as written, not an invented stand-in for something else).
  Neither one substitutes for `OWN-W03` — the owner's own scene and intent
  note — which this rule also requires and which remains outstanding.
- `CLAUDE.md` → "Curriculum review" — any check against week 2 or week 4
  content beyond what's recorded here is project-wide-review territory and
  needs explicit approval first; see "Adjacent-week impact" below for what
  has and hasn't actually been checked.
- `PLAN.md` → "Lecture template (90 min)" and "Workshop template (120
  min)" — `week-03.md` and `03-screenplay-workshop.md` follow these
  shapes; see `PLAN.md`'s "Session content depth pass" for the week's
  specific design.

## Confirmed decisions

- The decisive scene is her late mother's apartment kitchen, across five
  beats: call → sees name, doesn't answer → ringing continues → hand
  drifts toward the phone, stops → accepts on the final ring, says "Hey,"
  then listens. Consistent across `week-03.md`, `03-screenplay-workshop.md`,
  and `week-03.deck.mdx`.
- Worksheet timing: students download and read the worksheet before the
  workshop; they complete it during the workshop, on their own Week 2
  premise. Not graded by itself.
- `BIS-W03-SCENE` is split into a clean cold-read copy
  (`resources/week-03/scene.txt`) and an annotated copy with both
  director's notes reinstated (`resources/week-03/scene-annotated.txt`),
  both with byte-identical served copies under `public/resources/week-03/`.
  The lecture links the clean copy before its `<details>` reveals and the
  annotated copy after them.
- `03-screenplay-workshop.md`'s "In the workshop" section is eight
  numbered activities (Activity 1–8), each with a title, exact timing, an
  **Instructions** part, and an **Expected output** part. Minutes: 10 + 10
  + 10 + 15 + 25 + 10 + 30 + 10 = 120.
- The session's three `spec:` bullets (scene ≤2 pages; ≥1 antecedent-
  circumstance intent note; a partner's independent isolated-line reading)
  are unchanged since they were first written.

## Proposed / not yet confirmed

None outstanding. The worksheet-timing fix and workshop restructure
proposed earlier in the project's history have both been implemented and
are recorded above as confirmed, not proposed.

## Adjacent-week impact

- **Week 2** (preceding): supplies the premise students bring into the
  Week 3 workshop (the worksheet is filled in "on your own premise" from
  Week 2). Content read directly as part of this week's own work, not
  re-verified as a standalone check in this session.
- **Week 4** (following): the deck's closing line ("next week you break
  this exact scene into shots") commits Week 4 to using this week's scene
  and beats as its running input. `PLAN.md` notes an intent to spot-check
  week 4 only if the Week 3 rewrite changed anything week 4 assumes — that
  spot-check has not been recorded as done here; treat week 4's assumptions
  about this scene as unverified until it is.
- No week beyond these two immediate neighbours has been considered, per
  `CLAUDE.md`'s adjacent-weeks-only scope for automatic checks.

## Concurrent work

`PROCESS-REFLECTION-NOTES.md` (untracked, not authored by this session)
records prior coordination on this repo with another agent referred to as
"Codex," including an approved rule limiting the scope of automatic
consistency checks — consistent with `CLAUDE.md`'s "Curriculum review"
section. Beyond that historical note, whether Codex or any other agent is
currently active on Week 3's files, and who owns which file if so, is
unknown — not established by anything read this session. Check for
uncommitted changes (`git status`) before editing.

## This week's status

- `week-03.md`, `03-screenplay-workshop.md`, and `week-03.deck.mdx` are
  written and internally consistent (see Confirmed decisions above).
- `pnpm typecheck` and `pnpm build` both passed on 2026-09-12: 0 type
  errors, 0 accessibility violations, no broken links, no deck structural
  violations. That run followed edits to `CLAUDE.md`, `PLAN.md`,
  `MANIFEST.md`, and the new `handoffs/` files only — none of Week 3's own
  content files were touched in that run.

## Not yet rechecked / verification limits

- The 2026-09-12 typecheck/build run confirms the site still builds and
  renders cleanly; it does not re-verify Week 3's content accuracy or
  internal consistency beyond what compiling and link-checking can catch.
  The content-level consistency (scene/beats/timing matching across
  `week-03.md`, `03-screenplay-workshop.md`, `week-03.deck.mdx`) was last
  confirmed by direct read earlier in the project, not re-read line by
  line in this session.
- Week 2 and Week 4 have not been rechecked against Week 3's current state
  in this session (see Adjacent-week impact above).
- Nobody has yet run the scene-planning worksheet on a real premise start
  to finish to confirm the six sections are actually fillable in the time
  given — still outstanding, see Open questions.

## Open questions / unresolved issues

- `OWN-W03` (the owner's own scene + intent note, `MANIFEST.md` section
  3) is still `OWNER REQUIRED` / TBD — the teaching text above does not
  and cannot satisfy it. Resolves only when the owner produces their own.
- `BIS-W01-WORKSHOP` (Week 1's workshop asset, unrelated to Week 3's own
  content but referenced by Week 3's premise/ending) is still `NOT
  STARTED`, pending the owner generating it with Jimeng. Not a blocker for
  Week 3's own content, but Week 1's workshop can't actually run until
  it's produced.
- Nobody has yet run the scene-planning worksheet on a real premise start
  to finish to confirm the six sections are actually fillable in the
  time given (`PROCESS-REFLECTION-NOTES.md` §2 flags this as a
  self-attempt still owed before the process/reflection writeup can claim
  the scaffold helps).

## Evidence / file pointers

- `src/content/lectures/week-03.md`
- `src/content/sessions/03-screenplay-workshop.md`
- `src/decks/week-03.deck.mdx`
- `resources/week-03/scene.txt`, `resources/week-03/scene-annotated.txt`,
  `resources/week-03/scene-planning-worksheet.txt`,
  `resources/week-03/materials.md`
- `MANIFEST.md` rows `BIS-W03-SCENE`, `BIS-W03-WORKSHEET`, `OWN-W03`
- `PLAN.md` → "Session content depth pass" and Revision history entries
  dated 2026-09-11 (later), 2026-09-12 (Week 3 scene-planning scaffold),
  2026-09-12 (Week 3 sync and workshop restructure), and 2026-09-12
  (recurring requirements made durable)
