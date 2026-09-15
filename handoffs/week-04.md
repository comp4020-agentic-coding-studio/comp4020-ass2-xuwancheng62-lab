# Week 4 handoff — Thinking in shots

Status: content complete (two passes), pending owner evidence
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
`src/content/lectures/week-04.md`, `src/content/sessions/04-shot-breakdown.md`,
and `src/decks/week-04.deck.mdx` directly rather than trusting this summary
of them.

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
  and "Week 4 revision: deck slides, shot 5 staging, guided judgement" for
  the week's specific design.

## Confirmed decisions

- The real demonstration shot-lists the five closing "Before It Stops"
  beats (from `week-03.md`) into five shots: wide (kitchen/phone lighting
  up) → insert (screen reading THEO CALLING) → close-up (her still face) →
  insert (hand drifting toward the phone, stopping) → close-up, one
  continuous take, camera tilting up with her hand as it closes over the
  phone and lifts it to her ear, settling on her face for "Hey." Each
  shot's purpose is unique; none repeats.
- Shot 5 is staged as a single executable shot, not an unstaged combination:
  camera framed low on the tabletop and her hand's approach; as her hand
  closes over the phone and lifts it, the camera tilts up in the same
  movement, arriving on her face for the line. The canonical ending (she
  accepts on the final ring and says "Hey") is unchanged.
- The guided-judgement exercise now names an explicit dramatic intention
  (concealment from a housemate visible in the background) and enough
  spatial detail for the medium→wide-is-coverage / close-up→insert-is-
  argument judgement to follow from the scenario, plus an explicit line
  scoping that verdict to this beat's intention rather than to wide shots
  generally (citing shot 1 of this week's own demonstration — a wide
  chosen to argue isolation — as the counter-example).
- `week-04.deck.mdx` now has three additional slides matching the lecture:
  "Mamet's test: the shot as argument," "Five shots, one purpose each" (a
  compact shot/type/purpose table), and "Guided judgement: which pairing
  argues something?" — inserted in the lecture's own sequence. The closing
  quote slide's wording was updated to match shot 5's new staging.
- `04-shot-breakdown.md`'s "In the workshop" section is five numbered
  activities (Activity 1–5), each with a title, exact timing, an
  **Instructions** part, and an **Expected output** part. Minutes: 10 + 40
  + 35 + 25 + 10 = 120. Untouched by this pass — none of its three findings
  targeted the workshop.
- The session's two `spec:` bullets (numbered shot list with type + rough
  thumbnail per shot; one-clause purpose per shot, none repeated) are
  unchanged since they were first written.
- The stale pre-correction ending ("the call would go to voicemail, her
  hand finally moving toward the phone") that had persisted in
  `week-04.md`'s outline and `week-04.deck.mdx`'s closing quote slide was
  fixed to the current canonical ending in the prior pass, and stays fixed
  here.
- Eight teaching visual assets added: seven inline SVG diagrams in
  `week-04.md` (shot-size comparison; the five-shot storyboard; shot 5
  staged as one continuous take, three stages joined by a single
  camera-movement arrow; composition compared centred vs. edge-of-frame for
  one named beat; camera angle compared eye-level/high/low for the same
  beat; an overhead blocking/camera-movement comparison with a legend
  distinguishing character and camera paths by stroke style and token
  shape; and the two guided-judgement pairings illustrated under an
  explicit beat/intention header) plus a printable shot-list/storyboard
  template (`resources/week-04/shot-list-template.html`). All diagrams use
  the theme's real brand tokens, carry `role="img"`/`aria-label`, and are
  marked as teaching illustrations, not filmed footage, via an intro
  sentence and an `.at-tag` "Diagram" marker on each. `week-04.deck.mdx` was
  deliberately not touched this pass — see `PLAN.md`'s "Week 4 teaching
  diagrams" entry.

## Proposed / not yet confirmed

None outstanding. The three findings from this pass (deck slides behind
the lecture; shot 5 unstaged; guided judgement under-specified) were
proposed via plan mode, approved, and implemented — recorded above as
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
- `pnpm typecheck` and `pnpm build` both passed on 2026-09-12, after this
  pass's edits to `week-04.md` (shot 5, guided judgement) and
  `week-04.deck.mdx` (three new slides, closing-quote wording): 0 type
  errors, 0 accessibility violations, no broken links, no deck structural
  violations (12 decks checked).
- `pnpm typecheck` and `pnpm build` re-run again on 2026-09-12 after adding
  the eight teaching diagrams/template: typecheck passed clean; build
  initially failed one axe "region" violation against the standalone
  template page (`resources/week-04/shot-list-template.html`, no landmark
  wrapping its body — `public/` is copied into the built site and scanned
  the same as any rendered page), fixed by wrapping the template's content
  in `<main>` in both the canonical and served copies, then passed with 0
  accessibility violations and no broken links.

## Not yet rechecked / verification limits

- Content-level consistency (shot list ↔ week 3's beats ↔ deck) was
  confirmed by direct read in the session that made these edits, not by an
  automated check — typecheck/build catch structural and link issues, not
  whether the shot list's five purposes are genuinely non-duplicative, or
  whether the new deck slides read as concise summaries rather than
  contradicting the lecture, to a reader who hasn't just written them.
- `04-shot-breakdown.md` was not reopened this pass — none of the three
  findings targeted the workshop, so its content-level consistency is only
  as current as the prior pass's direct read, not re-verified here.
- Nobody has yet run the shot-breakdown workshop on a real scene start to
  finish to confirm five activities actually fit in 120 minutes as timed.
- Shot 5's new staging (a tilt following the hand to the face) has not been
  physically test-shot; it's a directable spec on paper, not confirmed
  against an actual camera/blocking rehearsal.
- `week-04.deck.mdx` was deliberately not touched by the teaching-diagrams
  pass — folding these diagrams into slides is a separate, later decision
  about decks generally, not scoped to this pass. Its content-level
  currency is only as good as the prior pass's direct read, not re-verified
  here.
- The camera-angle comparison diagram was built as a side-view schematic
  only (camera-to-subject geometry + view cone/sightline), without a
  separate "resulting frame" thumbnail sub-panel per angle — a minor scope
  simplification from the original ask, not flagged as needing a follow-up
  unless the reader finds the schematic-only version insufficient.

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
- `src/styles/visual-direction.css` (new `.at-diagram-row`/
  `.at-diagram-row--wide` rules)
- `resources/week-04/shot-list-template.html`,
  `public/resources/week-04/shot-list-template.html`,
  `resources/week-04/materials.md`
- `MANIFEST.md` row `OWN-W04`, and the "2026-09-12 (Week 4 shot-as-argument
  pass)", "2026-09-12 (Week 4 revision: deck slides, shot 5 staging,
  guided judgement)", and "2026-09-12 (Week 4 teaching diagrams)"
  revision-history entries
- `PLAN.md` → "Session content depth pass" → "Week 4 shot-as-argument pass,"
  "Week 4 revision: deck slides, shot 5 staging, guided judgement," and
  "Week 4 teaching diagrams," and the matching three 2026-09-12 Revision
  history entries

## Complete current-scene shot list integration — 2026-09-12

Owner requested and authorized the complete Before It Stops shot list and
website integration. Canonical file:
`resources/week-04/before-it-stops-shot-list.md`; byte-identical served text:
`public/resources/week-04/before-it-stops-shot-list.txt`. Week 4 lecture now
has an on-page five-shot summary and download; workshop links the worked
example. Entire current one-scene screenplay is covered, including packing
and final listening; final tilt remains one take. No owner evidence status
changed. Visual reference selection, physical rehearsal and real blind peer
verification remain pending. `pnpm build` passed after integration, with no
broken links; log: `/private/tmp/w4-shot-list-build.log`. No new browser visual
pass or wider curriculum review was performed for this text/link addition.

## Shot-size image update — 2026-09-12

Owner authorized updating the website images. The shot-size SVG was replaced
with four labelled image examples: wide-v2, existing medium, closeup-v2 and
existing insert. Canonical PNGs remain under resources/week-04/images; served
copies under public/resources/week-04/images match. Caption explicitly notes
these are AI teaching category examples with differing actions/room details,
not continuity-matched production frames. Other diagrams and deck unchanged.
`pnpm build` passed after integration, no broken links. No additional browser
visual pass performed; images themselves were visually reviewed previously.

## Pairing image replacement — 2026-09-12

Owner authorized image generation/replacement. Existing medium supplied the
reference for a consistent four-panel sheet via built-in imagegen. Four
individual panels replace the lecture pairing SVG, with pair headings and
explicit Cut to labels. Phone back/fingers are legible in insert; housemate
present in medium/wide and absent in close-up. Independent concealment
exercise, not Before It Stops story canon. Originals retained; served copies
match canonical files. Build passed after file generation, no broken links.
Images visually inspected; no new browser screenshot pass performed. See
resources/week-04/materials.md for paths and generation provenance.

## Shot-list website removal — 2026-09-12

Owner requested removing the previously added full-scene list integration.
Removed lecture five-shot summary section, workshop download paragraph and
served text file. Canonical resources/week-04/before-it-stops-shot-list.md
retained. Earlier integration entry above is historical and superseded.
Existing original lecture demonstration and all image updates remain.
