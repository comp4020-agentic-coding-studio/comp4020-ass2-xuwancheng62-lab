# Week 10 handoff — Editing and dramatic rhythm

Status: content complete; real comparison example integrated; montage
rehearsal added to workshop
Last updated: 2026-09-15

## Next action

No content work outstanding for Week 10. Before changes, read this file,
`CLAUDE.md`, `PLAN.md` → "Judgement calls" and "Assignment 1 — shot-list
scope narrowed..." (records this finding's origin), and
`resources/week-10/materials.md`.

## Standing rules that apply

- `CLAUDE.md` → "Real production material, never invented", "Weekly handoff records", "Curriculum structure: teach → practise → assess", "Workshop structure: explicit numbered activities", "Planning and human–agent decision making".
- `PLAN.md` → lecture/workshop templates, "Weeks 6–12 depth pass — approved", "Week 10 — Editing and dramatic rhythm".

## Confirmed decisions

Owner requested a second cut and then explicitly authorized using the actual pair as the Week 10 example. Cut A is a byte-identical Week 9 assembly copy (31.233333 s). Cut B keeps only the first 2.067 s of shot 03 instead of 6.067 s (27.266667 s). Same sources, order, other trims and half-second ending fade; source audio trimmed with picture. No regeneration.

Lecture embeds both playable videos, timing comparison and expandable intended emotional descriptions after viewing. Deck links both versions and the comparison, replacing the hypothetical two-second face hold / early wide-to-phone cut with the actual four-second reaction reduction. Guided judgement now uses this assembly's shot numbers (2 phone, 3 reaction) and distinguishes its hypothetical phone-centric choice from actual Cut B. Outcomes and the lecture's real Cut A/Cut B example are unchanged by the 2026-09-15 pass below.

- **Montage rehearsal added to the workshop — 2026-09-15.** Closed the
  previously-accepted "montage lectured, never rehearsed" judgement call
  (`PLAN.md` → "Judgement calls"), on owner request. `10-recut-lab.md`'s
  spec bullet 1 now requires the workshop's two cuts to use *different*
  techniques: one duration-based pacing decision (unchanged Activity 2 —
  hold), one montage decision — repeating or reordering at least one shot
  (Activity 3, retitled "Second cut: montage," previously "cut away
  early"). Activity 1's setup prompt and Activities 4/5's wording were
  updated to match ("cut-away version" → "montage version"; completion
  check now asks for one duration cut and one repeat/reorder cut, not two
  duration variants). `week-10.md` gained one bridging sentence at the end
  of "Guided judgement: what does this cut argue?" naming the montage
  requirement for the workshop's second cut. Five activities still sum to
  120 minutes (10+30+30+30+20). No change to the lecture's real Cut A/Cut
  B example/videos, outcomes, timing breakdown, or due dates.
- This is a trigger-test change (a `spec:` bullet and workshop content
  both changed) — recorded in `PLAN.md`'s Revision history
  ("2026-09-15 (Week 10 montage rehearsal added — owner approved)") per
  the single-record rule, not as a new standalone `PLAN.md` section.

## Proposed / not yet confirmed

None outstanding. Preferred final-film cut remains an owner decision informed by playback, not an inferred audience result.

## Adjacent-week impact

Uses the actual Week 9 assembly/continuity record. Week 11 may build its sound pass on the selected cut; checked directly (`11-sound-pass.md` only says "bring your chosen cut from week 10") and confirmed it doesn't depend on which technique differentiates the two cuts, so it needed no change for the 2026-09-15 montage pass. Week 9 (`09-continuity-assembly.md`) likewise checked and unaffected — it only hands off "the shots you've generated... for one sequence."

## Concurrent work

Unknown; unrelated existing changes preserved. No commit or deployment made.

## This week's status

- 2026-09-15: `10-recut-lab.md` and `week-10.md` re-read end-to-end after
  the montage-rehearsal edit; spec bullet, five activities, and the
  lecture's bridging sentence are internally consistent, minutes sum to
  120. `pnpm typecheck`: 0 errors/warnings/hints. `pnpm build`: passed, 0
  accessibility violations (49 pages), no broken links, 12 decks pass
  structural checks.
- 2026-09-13: both videos and comparison integrated, canonical/served copies hash-match. Earlier timeline verification confirms only shot 03 duration differs; Cut B fully decodes without error and sampled shot 04 entry is lit. `pnpm typecheck`: 0 errors/warnings/hints. `pnpm build`: passed, no accessibility violations/broken links; internal links respect base; 12 decks pass structural checks. Google font metadata fetch failed in restricted network; build completed with font warnings.

## Not yet rechecked / verification limits

No full playback, audio listening, independent screening, emotional-effect measurement or end-to-end workshop trial claimed. Descriptions state editorial intent. Source audio duration follows picture, so this is not a sound-isolated experiment. Separate OWN-W10 assessment evidence is not inferred from teaching example integration. Nobody has run the recut workshop start to finish to confirm a real montage cut (repeat/reorder) is actually buildable from the five-shot assembly in the allotted 30 minutes — the 2026-09-15 pass is an instructions-level design, not a trialled one.

## Open questions / unresolved issues

Week 9 phone-interface/lighting differences remain in both cuts. Owner playback and blind comparison can inform final selection and precise audio/cut judgement.

## Evidence / file pointers

- `src/content/lectures/week-10.md`, `src/decks/week-10.deck.mdx`, `src/content/sessions/10-recut-lab.md`
- `resources/week-10/materials.md`, `comparison.md`, `cut-a-hold.mp4`, `cut-b-early.mp4`, both timelines and `verification.json`
- `public/resources/week-10/` (matching served videos/comparison)
- `MANIFEST.md` → BIS-W10-RECUTS; separate OWN-W10
- `handoffs/week-09.md` for source assembly decisions and review limits
