# Week 11 handoff — Directing with sound

Status: real sound comparison integrated; owner approved application
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

Lecture rewritten around directing a voice like a face (line readings as
performance, not narration), ambience/Foley as a location's "second
bible," and music as a directorial statement rather than wallpaper. A
worked comparison scores the final beat two ways: without music, and with
a sustained cue entering under the reach-and-stop insert. Misconception
table and a guided `<details>` judgement (a swelling string cue starting
too early, diagnosed and corrected to start under the reach rather than
the first ring) included.

**Sourcing note:** this is the first lecture in the course to invoke
Meisner. The lecture explicitly hedges that "directing a voice like a
face" as a technique *for directors* is this course's own inference, not
documented Meisner-for-directors pedagogy — `RESEARCH.md` (line 144–145)
found no Meisner-authored or Institute-published curriculum specifically
for directors. Any future edit to this section must preserve that hedge
rather than presenting it as established pedagogy.

Session explicitly structured in two phases (rehearsal, then construction)
via five numbered Activities (10/30/10/40/30 = 120 minutes): recap and
line selection, direct two takes (rehearsal), select and lay in
(rehearsal), build the sound pass (construction), compare and completion
check (construction). All three original `spec:` bullets unchanged (≥2
directed takes + selection justification; two cut versions, dialogue-only
vs full pass; beat-by-beat emotional-change naming). Deck rewritten to
match, including the cue-timing diagnosis.

## Proposed / not yet confirmed

None.

## Adjacent-week impact

Lays sound onto the cut produced in Week 10 (specifically the "cut as
argument" version selected there), and the corrected cue-timing example
here is referenced directly by Week 12's worked defence ("the music enters
too early... already fixed in week 11"). Rehearsal-vs-construction split
follows the Columbia pattern noted in `RESEARCH.md`.

## Concurrent work

None known. This pass also touched Weeks 6–10 and 12 in the same session.

## This week's status

2026-09-12 validation:
- `pnpm typecheck`: 0 errors, warnings, or hints (whole-project run
  covering Weeks 6–12 together).
- `pnpm build`: passed — 0 accessibility violations, no broken internal
  links, all 12 decks passed structural checks.
- Direct check: session's five Activities sum to exactly 120 minutes.

## Not yet rechecked / verification limits

No end-to-end 120-minute workshop trial was performed. The music/no-music
comparison and cue-timing diagnosis are authored worked examples, not a
report of an actual mix session — no audio was actually generated or
mixed this pass, per "Real production material, never invented".

## Open questions / unresolved issues

None beyond the still-pending Week 5 bible fields (phone case/wardrobe
details relevant to Foley), not this week's to resolve. The Meisner hedge
above should be treated as a standing constraint on this section, not
merely a one-time note.

## Evidence / file pointers

- `PLAN.md` → "Weeks 6–12 depth pass — approved" (notes the Meisner hedge
  explicitly)
- `RESEARCH.md` (lines 125–174, esp. 144–145 Meisner caveat)
- `src/content/lectures/week-11.md`
- `src/content/sessions/11-sound-pass.md`
- `src/decks/week-11.deck.mdx`
- `handoffs/week-10.md`, `handoffs/week-12.md`

## Sound asset production started — 2026-09-13

Owner requested Week 11 material production. Created actual original procedural ambience, incoming-call SFX and sustained music cue, plus a combined sound-bed audition under `resources/week-11/`; extracted Cut A original audio separately. Cut A is only a provisional working picture. WAV duration/format/peaks/hashes checked; audition decodes without error and does not clip. No listening, approved sound bible, two directed voices, selected take, sync dialogue, final mix or comparison response claimed. Voice-production choice asked of owner; see `materials.md` for the shared-antecedent brief and remaining outputs.

Earlier handoff pending phone/wardrobe claims are stale. Week 11 guided judgement still invents a prior unanswered ring; recorded as a content issue, not edited during material production. No source videos, teaching pages, deployment or individual assessment evidence changed.

## Direct synthesis authorized and rendered — 2026-09-13

Owner requested direct synthesis with alignment. Independently synthesized Samantha “Hey” A/B at 150/105 wpm; pace is the single directed variable. Primary pair provisionally uses A; selection is technical, not claimed as listening-based performance judgement. Produced dialogue-only/full-pass videos, B alternate and no-music control on unchanged Cut A picture. Source audio omitted. Call SFX 6.067–24.1s, cue 17.6s, dialogue 27.8s after phone reaches ear around 27.7s. Actual visual samples support event alignment; exact phoneme lip-sync and auditory review remain unverified. See `materials.md` and `alignment-verification.json`. No website integration or assessment completion claimed.

## Owner-approved website integration — 2026-09-13

Applied actual A/B voice pair, dialogue-only/full-pass videos, no-music control, B alternate and intended beat comparison to Week 11 lecture/deck. Primary A application approved by owner; final-film selection and independent auditory judgement not inferred. Corrected guided judgement to the shared interrupted-packing antecedent; Meisner caveat retained. Previous authored-example, prior-call and no-integration accounts above are historical and superseded. Outcomes, three session spec bullets and 120-minute timing unchanged.

Validation: `pnpm check` passed (zero type diagnostics, 6 tests); no accessibility, broken-link or deck-structure violations. Seven public copies hash-match. Targeted reference/antecedent/caveat checks passed. Google Fonts DNS warnings remain. Technical media checks are recorded in `alignment-verification.json`; exact lip fit, audience review and classroom trial remain unverified. No deployment or assessment-completion claim. No further local integration required; use `resources/week-11/materials.md` and `comparison.md` before further sound changes.
