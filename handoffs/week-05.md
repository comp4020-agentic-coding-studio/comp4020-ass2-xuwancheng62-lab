# Week 5 handoff — Building a consistent world

Status: approved text teaching and templates complete; visual design deferred
Last updated: 2026-09-12

## Next action

When the owner accepts Week 4 visual references, reconcile the pending fields
in `resources/week-05/bible-examples.txt` with them and propose any new story
or design facts before making them canonical. Read this file, `CLAUDE.md`,
`PLAN.md` → "Week 5 depth pass — approved", and the actual current Week 5
files first. No further text/template implementation is outstanding in the
approved, narrowed scope.

## Standing rules that apply

- `CLAUDE.md` → "Planning and human–agent decision making", "Curriculum
  review", "Curriculum structure: teach → practise → assess", "Workshop
  structure: explicit numbered activities", "Real production material,
  never invented", and "Weekly handoff records".
- `PLAN.md` → "Lecture template (90 min)" / "Workshop template (120 min)".

## Confirmed decisions

Owner approved implementation with "ok do it", then explicitly chose to
leave visual appearance/costume/kitchen fields pending while completing text
teaching and templates. Lecture now teaches concrete entries, spatial
relationships, fixed identity versus changing state, versioned references,
and diagnosis of peer read-back. It includes Nadia/Theo/kitchen draft entries,
a fully written phone-state revision and a judgement exercise with answer.
The visual drafts are explicitly not complete production bibles.

Workshop has six activities (10/25/20/30/25/10 = 120 minutes), Instructions
and Expected output in each. Both original spec bullets and all three
files' frontmatter remain byte-for-byte unchanged. Deck has 15 slides.
A three-page print worksheet and downloadable examples are linked from the
lecture, workshop and deck. No image generation was performed. OWN-W05 and
other personal evidence remain deferred, not marked complete.

## Proposed / not yet confirmed

Appearance, wardrobe, voice and detailed kitchen/prop/light references remain
pending. No unapproved visual detail has been silently promoted to canon.
Optional reference imagery is outside the completed text/template scope.

## Adjacent-week impact

Week 4 supplies the closing shot list and forthcoming accepted visual
references. Existing action preserved: reach, stop, accept on final ring,
phone to ear within the final shot, "Hey". Theo is a caller, not a new
on-screen location. Week 6 receives the revised bible with the pre-production
package. No Week 4/6 file changed; no wider curriculum review performed.

## Concurrent work

Owner reports CC working on Week 4. Pre-existing changes to Week 5 lecture/
deck were read before replacement; frontmatter preserved. Shared PLAN.md
and MANIFEST.md received only targeted Week 5 edits; other modifications
remain intact. This pass did not edit global styles or CC's Week 4 assets.
Re-read shared files before editing again; CC may continue changing them.

## This week's status

2026-09-12 validation:
- `pnpm typecheck`: 0 errors, warnings or hints.
- `pnpm build`: passed, including accessibility, internal links and deck
  structural checks; no broken links.
- Direct checks: frontmatter/spec unchanged, six activities total 120 minutes,
  canonical and served resources byte-identical.
- Isolated headless Chrome: lecture, workshop, deck and worksheet at
  1920×1080 and 390×844. No page horizontal overflow in measured pages;
  slide screenshots and layout measurements checked, including the final
  slide. Phone slides use the existing fixed-canvas scaling and have small
  type; lecture offers the corresponding responsive reading version.
- Browser print: three A4 pages, all three rendered and visually inspected;
  no clipping. QA captures/logs are temporary under `/private/tmp/w5-qa/`,
  `/private/tmp/w5-typecheck.log` and `/private/tmp/w5-build.log`.

## Not yet rechecked / verification limits

No actual classroom/peer trial or full 120-minute rehearsal was performed.
The worked answer is authored, not claimed peer evidence. Build checks do
not establish teaching quality or cross-shot visual consistency. References
are still pending, so no production reproducibility claim is made. Full
submission evidence checks were not run for this scoped pass.

## Open questions / unresolved issues

Select accepted visual references before completing the draft bible's
pending fields; confirm Theo's audible representation before producing any
reply. Personal evidence stays deferred independently of teaching resources.

## Evidence / file pointers

- `PLAN.md` → "Week 5 depth pass — approved" and Week 5 approval revision
- `src/content/lectures/week-05.md`
- `src/content/sessions/05-world-bible-crit.md`
- `src/decks/week-05.deck.mdx`
- `resources/week-05/materials.md`, `bible-examples.txt`, `bible-worksheet.html`
- `public/resources/week-05/` (served copies)
- `MANIFEST.md` → BIS-W05-ENTRIES, BIS-W05-WORKSHEET; OWN-W05 unchanged

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
