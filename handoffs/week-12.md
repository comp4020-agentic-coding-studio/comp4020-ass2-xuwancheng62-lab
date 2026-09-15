# Week 12 handoff — Screening, critique, and the revision to final cut

Status: content complete
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

Lecture rewritten around formalizing the screening-and-critique ritual
already practised piecemeal in Weeks 6 and 9, citing the cross-program
pattern from `RESEARCH.md` (AFI's Comprehensive Review, NYU's weekly
Master Class, NFTS's rushes cinemas). Teaches that critique means naming a
decision, not a feeling, and separating authorship (a deliberate choice)
from a limitation routed around. A worked defence answers three notes
raised against the running example: Theo's photo (already resolved — cut
in Week 6), the music entering too early (already fixed in Week 11), and
the call's unanswered-then-answered duration (grounded in Week 7's moment
before). Closing section ties the whole course's direct → generate →
evaluate → redirect loop back to Week 1. Misconception table and a guided
`<details>` judgement (phone case mismatch, diagnosed as a likely
continuity failure rather than a deliberate choice) included.

Session restructured into five numbered Activities (10/40/40/20/10 = 120
minutes): recap and final pass, screening round, critique and defend,
choose the revision note, completion check. All three original `spec:`
bullets unchanged (near-final cut screens <4 min unattended; name and
defend 3 decisions against specific alternatives; leave with one specific
critique note to act on). Deck rewritten to match, including the worked
defence (three notes) and the closing "direct → generate → evaluate →
redirect" slide.

2026-09-13: `src/content/assessments/final-project.md` (surfaces on this
week's lecture page per `PLAN.md` → "Content and data architecture")
expanded on owner request — see `PLAN.md` → "Final Project — weighted
criteria and walkthrough". Marking moved from holistic to weighted
(Directorial coherence and craft 45%, Director's statement 30%,
Authorship reflection 25%); a "Complete the project" walkthrough added
(Your task / Check your work per submission part — film, statement,
reflection), deliberately with no worked example, since students are
already building their own locked film by this point. Assessment weight
(60), due date, and `spec:` bullets unchanged. Does not touch
`week-12.md`, `12-screening-and-critique.md`, or `week-12.deck.mdx`
themselves.

Same day, second pass: added a "Detailed marking rubric" section splitting
each of the three criteria into three dimensions, each with 7–10/5–6/1–4
band descriptors — see `PLAN.md`'s same section, "Detailed rubric matrix"
addendum. Body content only; the `marking.criteria` frontmatter shape
(name + weight) is unchanged.

Same day, third pass: owner approved letting a student finish the project
with a different story than the one locked in Assignment 1, rather than
requiring continuation — see `PLAN.md` → "Final Project — weighted
criteria and walkthrough" → "Story-switch option". A student who switches
must submit a short pivot plan for the new story (updated logline, bible
entries, shot list) standing in for Assignment 1's package, and must name
the switch itself as one of the director's statement's three defended
decisions, against continuing the original story. Changed: the brief's
opening quote, the "What you submit" list (new conditional pivot-plan
bullet), the "Finish and lock the film" and "Write the director's
statement" walkthrough subsections, and a new conditional `spec:` bullet.
Also rewords one sentence each in `week-12.md`'s outcomes list and its "A
last pass, checked against the bible" section (and one sentence in
`week-07.md`) so "checked against the bible locked in Assignment 1" reads
as "your locked pre-production package," generalizing for a student who
switched. Assessment weight (60), due date, and the original four `spec:`
bullets unchanged. Assignment 1's own grading is untouched by this — its
mark stands on whatever story that submission described.

## Proposed / not yet confirmed

None.

## Adjacent-week impact

This is the final week — it closes the loop back to Week 1's core
direct→generate→evaluate→redirect framing and explicitly cross-references
resolved decisions from Weeks 6 (Theo's photo) and 11 (music timing),
using them as the worked example rather than inventing new ones. No
downstream week depends on it.

## Concurrent work

None known. This pass also touched Weeks 6–11 in the same session.

## This week's status

2026-09-12 validation (lecture/session/deck):
- `pnpm typecheck`: 0 errors, warnings, or hints (whole-project run
  covering Weeks 6–12 together).
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.
- Direct check: session's five Activities sum to exactly 120 minutes.

2026-09-13 validation (final-project.md, both passes above):
- `pnpm typecheck`: 0 errors, warnings, or hints.
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.

2026-09-13 validation (story-switch option, third pass):
- `pnpm typecheck`: 0 errors, warnings, or hints.
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.

## Not yet rechecked / verification limits

No end-to-end 120-minute workshop trial was performed, and no actual
class screening or critique session took place. The worked defence is an
authored teaching artefact assembled from decisions already recorded
elsewhere in this depth pass (Weeks 6 and 11), not a report of an actual
screening, per "Real production material, never invented".

## Open questions / unresolved issues

None beyond the still-pending Week 5 bible fields, which the phone-case
guided-judgement example in this lecture references directly (the
mismatch it diagnoses would be resolved once that bible field is filled
in).

## Evidence / file pointers

- `PLAN.md` → "Weeks 6–12 depth pass — approved"
- `RESEARCH.md` (lines 1–97, cross-program screening-ritual pattern)
- `src/content/lectures/week-12.md`
- `src/content/sessions/12-screening-and-critique.md`
- `src/decks/week-12.deck.mdx`
- `handoffs/week-06.md`, `handoffs/week-11.md`

## Approved lecture / small-group workshop format — 2026-09-13

Owner approved lecture teaching critique/defence on example excerpts and actual student screenings in workshop groups of 4–5. Lecture explicitly sets 10/45/15/15/5 = 90 minutes, including defence comparison, judgement practice and workshop briefing. Workshop rotates timekeeper/note-taker; after cold screenings, divide 40-minute defence round equally (8 or 10 minutes each), with alternatives for all three decisions. Activities remain 10/40/40/20/10 = 120 minutes; specs and Final Project unchanged. Deck matches.

Corrected prior-call antecedent to interrupted packing; music example defends the actual 17.6s placement without claiming an unproduced repair. Third challenge separates retaining a pause editorially from Jimeng B failing immediate-response direction. Earlier whole-class, missed-call and already-fixed mix accounts above are historical and superseded.

Validation: `pnpm check` passed, zero type diagnostics, 6 tests, no accessibility/broken-link/deck-structure violations. Scoped wording and timings checked. Final wording rebuild passed, with the latest clarification confirmed in the built lecture. Google Fonts DNS warnings persist. No actual class screening, feedback, final film, end-to-end workshop trial or deployment performed.
