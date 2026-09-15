# Plan — Archive

Historical companion to `PLAN.md`. Holds completed implementation
narratives, superseded proposals, and closed-out corrections that used to
live in `PLAN.md` directly. Moved here on 2026-09-13 as part of
`PLAN.md`'s "Documentation reorganisation — approved" — see that section
for the rules the split followed and for the two sections that were
checked and deliberately left in the live plan instead of moved here.

Nothing in this file is current policy. Where a moved section's decisions
are still in force, `PLAN.md` says so at that section's original heading,
with a link back into the matching section below. Original headings and
text are preserved verbatim; nothing here has been rewritten or corrected
after the fact, including entries that a later, still-live section in
`PLAN.md` has since superseded.

## Judgement calls — dismissed findings (2026-09-04 follow-up pass)

Moved from "Judgement calls" in `PLAN.md`, which keeps the section's two
still-open trade-offs and now links here for this closed-out part.

A follow-up pass (2026-09-04) raised two more findings that, unlike the two
above, are not open trade-offs at all — they were dismissed once the
teach/practise boundary in `CLAUDE.md` was clarified to distinguish
disciplinary knowledge from tool mechanics:

- **Week 9's clip assembly, ahead of week 10's editing lecture.** Not a
  violation. Week 9's own lecture already teaches the disciplinary judgement
  week 9's workshop practises — what has to match across shots, recognising
  continuity drift, the fix-or-accept repair discipline. The workshop's "cut
  the shots together in order" step is chronological, non-evaluative tool
  mechanics (operating a timeline), which a workshop may teach itself under
  the clarified rule. Week 10's lecture teaches a distinct, later
  disciplinary layer — pacing, shot duration, montage — and week 10's own
  workshop (recutting for pacing effect) is the first place that judgement
  is required; nothing in week 9's spec asks for a pacing decision. The two
  weeks looked like one skill split across an untaught gap; they're actually
  two adjacent disciplines, each taught and practised inside its own week.
- **No lecture teaches generative-tool mechanics** (image-to-video controls,
  an editing timeline, layering audio). Not a gap. Under the clarified rule,
  tool mechanics are a workshop's job, not a lecture's — this finding was
  built on the pre-clarification reading of the boundary and doesn't survive
  it.

## Session content depth pass

`PLAN.md`'s live "Session content depth pass" section keeps the still-
current intro, the Lecture/Workshop templates, the per-week technique
mapping table, and the still-open "Week 1 status" narrative. The
completed, week-specific implementation narratives below have moved here.

### Week 1–2 teaching corrections

The Week 2 worked logline is taught through an initial draft and a revised
reference sentence: the draft's "must decide whether" leaves the want
ambiguous; the revision explicitly names Nadia's want to answer, her
self-restraint after years of estrangement, and the immediate risk of
missing this call. This clarifies the existing story without changing its
characters or canonical ending. Lecture, deck, and canonical/served text
assets use the same revised reference; the original remains labelled as a
draft for comparison.

Week 2 also models the existing filmability requirement before students
practise it: a compact progression of observable actions, a visible change,
one kitchen, Nadia on screen and Theo as the caller, and an estimated
2–4-minute screen-time plan. Timings are planning estimates, never claimed
as a completed or tested production. This adds teaching support for the
existing workshop spec, with no new assessed deliverable.

The Week 1 lecture presents Take A and an observation question before
revealing Note A and the diagnosis. Native, initially closed disclosures
then reveal the diagnosis, Take B comparison, and redirect explanation in
sequence. Existing video files and objectives are retained. The lectures
index contains student-facing introduction only; the Week 2 lecture does
not refer students to the inaccessible internal `RESEARCH.md` file.

These corrections are limited to Weeks 1–2 and the lectures index. They
preserve the Week 3 corrections, Week 1's counterfactual workshop framing,
all assessment specs, and BIS-W01-WORKSHOP's NOT STARTED status.

### Grounding in real directing pedagogy — completed sub-passes

The following sub-narratives from "Grounding in real directing pedagogy"
describe fully implemented and verified work; they've moved here. The
section's still-open "Week 1 status" narrative (`BIS-W01-WORKSHOP` remains
`NOT STARTED`) stays live in `PLAN.md`.

**Week 3 scene-planning scaffold (added 2026-09-12).** The lecture and
workshop teach Weston's antecedent-circumstance note, but neither one
taught how to get from a Week 2 premise to a two-page scene in the first
place — a blank-page problem for anyone who's never written a screenplay.
Added a taught writing-process sequence to the lecture, before the
existing real-demonstration walkthrough: premise → decisive scene → scene
change → five observable beats → screenplay form → director's note,
worked through "Before It Stops" (want: answer Theo's call; obstacle:
years of estrangement; beginning state: Nadia maintains the silence;
ending state: she answers; five observable beats from the phone ringing,
through her hand reaching toward it and stopping, to her accepting the
call on the final ring). "Observable" is defined narrowly here —
something the audience can see or hear — and the sequence deliberately
stops short of camera, framing, or editing decisions, which stay reserved
for week 4 so the shot-breakdown workshop still receives an undirected-in-
that-sense scene. A matching downloadable worksheet walks a student through
the same sequence for their own film, tracked as `BIS-W03-WORKSHEET` in
`MANIFEST.md`. This is scaffolding, not a new assessed outcome: the three
`spec:` bullets in `03-screenplay-workshop.md` are unchanged, and no
individual worksheet field is separately graded — the worksheet exists to
help students reach those same three bullets, not to add new ones. The
workshop's main exercise is restructured around the worksheet's sequence
(story anchor → scene change → five beats → screenplay conversion →
director's note), with the existing peer-verification test kept as-is at
the end and named minutes across all phases summing to the full 120-minute
session. This is editorial/practical scaffolding, not a new sourced
pedagogical technique requiring its own `RESEARCH.md` grounding — the
technique actually being taught and assessed stays Weston's "moment
before," per the mapping table above.

**Week 4 shot-as-argument pass (added 2026-09-12).** Week 4 was still
outline-only: `week-04.md` had five topic bullets and no taught prose,
`04-shot-breakdown.md`'s "In the workshop" was three unstructured
paragraphs with no timings, and both it and `week-04.deck.mdx` still
described the closing "Before It Stops" beat with its pre-correction ending
("the call would go to voicemail, her hand finally moving toward the
phone") rather than the corrected one from the Week 3 fixes above (she
accepts on the final ring and says "Hey"). Fixed as part of this pass, not
as a separate correction, since the stale wording only existed in
still-unwritten Week 4 content.

`week-04.md` rewritten to the full lecture template: shot vocabulary and
composition/blocking/camera-movement content from the old outline expanded
into taught prose; Mamet's "shot as argument" (per the mapping table's row
4 and `RESEARCH.md`) taught by name — build the list by asking what the
character wants and whether a given cut shows them getting it, not by
covering every angle; a real demonstration walkthrough shot-listing the
corrected five closing beats into five shots, each with a stated purpose
and a note on the meaning its juxtaposition produces (a genuine authored
teaching artefact, same status as `week-03.md`'s scene — not a claimed AI
generation or owner asset, so no new `MANIFEST.md` row); a coverage-
instinct/argument-instinct misconception table, matching week 1's wish/note
pattern; and a guided-judgement exercise adapted from Mamet's cut-face/
cut-fridge "hunger" example in `RESEARCH.md`. Learning outcomes stated
explicitly for the first time; the technique taught is unchanged from the
mapping table's row 4.

`04-shot-breakdown.md` restructured into five numbered Activities per
`CLAUDE.md`'s "Workshop structure: explicit numbered activities" and this
file's 4-phase workshop template (construction mode): recap and briefing
(10), build the shot list (40), sketch the thumbnails (35), dailies review
(25, peer test = partner reads only the shot list and describes each cut's
intended meaning, per the mapping table's row 4), completion check (10) —
summing to 120. The exercise itself is unchanged; both `spec:` bullets are
unchanged. `week-04.deck.mdx`'s closing quote slide corrected to the
current canonical ending; no other slides changed, since the deck stays its
own distillation rather than mirroring the new lecture prose or the
workshop's activity structure.

Week 5 (`05-world-bible-crit.md`) was checked directly as Week 4's
following neighbour and found in the same pre-depth-pass shape (no numbered
activities, no named durations) — the mapping table already marks it
"already solid... only add named durations/phases," so it needs the same
kind of pass next, not as part of this one. Recorded in
`handoffs/week-04.md`, not actioned here.

**Week 4 revision: deck slides, shot 5 staging, guided judgement (added
2026-09-12).** A review of the pass above found three gaps, fixed here.
First, `week-04.deck.mdx` had never caught up with the lecture rewrite — it
named none of Mamet's test, the five-shot worked example, or the guided
judgement. Three slides added, in the lecture's own sequence: "Mamet's test:
the shot as argument" (the fridge/hunger example and the want/get-it filter,
after the composition slide); "Five shots, one purpose each" (a compact
shot/type/purpose table replacing the old quote slide's role, kept next to
it); "Guided judgement: which pairing argues something?" (the concealment
scenario, summarized). The closing quote slide's wording was updated to
match shot 5's new staging (below), not otherwise changed. Second,
`week-04.md`'s shot 5 asserted a single close-up covering both her hand
closing over the phone and her face saying "Hey" without saying how one
shot holds both; rewritten as one continuous take — camera framed low on
the tabletop and her hand's approach, tilting up with her hand as it lifts
the phone to her ear, settling on her face for the line — naming the
framing, blocking, and camera movement that make it one shot, not two. The
canonical ending (she accepts on the final ring and says "Hey") is
unchanged. Third, the guided-judgement exercise declared the medium→wide
pairing "coverage" without a stated dramatic intention or enough spatial
detail for that judgement to follow; rewritten with an explicit intention
(concealment from a housemate visible in the background) and enough framing
detail that the medium→wide pairing's redundancy and the close-up→insert
pairing's argument both follow from the scenario, plus an explicit line
scoping the verdict to this beat's intention rather than to wide shots in
general (citing shot 1 of the week's own demonstration, a wide chosen to
argue isolation, as the counter-example). No `spec:` bullet, learning
outcome, or the running example changed; `04-shot-breakdown.md` was not
reopened, since none of the three findings targeted it.

**Week 4 teaching diagrams (added 2026-09-12).** Week 4 was content-complete
in prose but text-only; eight visual teaching assets were added so the
lecture's claims (shot sizes, five-shot continuity, shot 5's staging,
composition, angle, blocking/camera movement, the guided-judgement pairings)
are shown, not just asserted, plus a printable shot-list/storyboard
template for the workshop. This falls under "Visual direction"'s "Decorative
artwork vs. teaching visuals, kept strictly separate": these are
pedagogically accurate, content-specific diagrams, made only where a concept
needs visual explanation, displayed as themselves rather than restyled into
the abstract poster system — a different thing from the deferred media
component family (`Implementation phases` step 3), which is about displaying
the owner's own real production footage/audio and stays deferred untouched.
No `MANIFEST.md` asset row was added: these are instructor teaching
material, not owner-produced evidence, so `OWN-W03`/`OWN-W04` stay `OWNER
REQUIRED`/TBD.

Seven inline `<svg>` diagrams were added directly into `week-04.md`'s
markdown (shot-size comparison; the five-shot storyboard; shot 5 staged as
one continuous take, three stages joined by a single camera-movement arrow;
composition compared centred vs. edge-of-frame for one named beat; camera
angle compared eye-level/high/low for the same beat; an overhead
blocking/camera-movement comparison with a legend distinguishing character
and camera paths by both stroke style and token shape; and the two guided-
judgement pairings illustrated under an explicit beat/intention header).
Each SVG uses the theme's real brand tokens (`var(--at-primary)` etc., with
literal fallback hexes), carries `role="img"` and a descriptive `aria-label`,
and sits under a `<figcaption>` with an `.at-tag` "Diagram" marker; an intro
sentence at the first diagram labels all of them as teaching illustrations,
not filmed footage. New `.at-diagram-row`/`.at-diagram-row--wide` CSS was
added to `src/styles/visual-direction.css` for panel layout only — the SVGs
carry all teaching content. The eighth asset, a printable shot-list/
storyboard template, follows the Week 3 `resources/` pattern: canonical copy
at `resources/week-04/shot-list-template.html`, byte-identical served copy
at `public/resources/week-04/shot-list-template.html`, documented in a new
`resources/week-04/materials.md`, and linked once from `04-shot-breakdown.md`
("Before the workshop," one added sentence, the two `spec:` bullets/five
Activities/120-minute total all unchanged — confirmed by diff) and once from
`week-04.md`'s closing synthesis paragraph. `week-04.deck.mdx` was
deliberately not touched — folding these diagrams into slides is a separate,
later decision about decks generally, not scoped to this pass. `pnpm
typecheck` and `pnpm build` (axe accessibility + link checks over the
rendered pages, including the new inline SVGs and the standalone template
page under `public/`) both passed with 0 errors/violations after one fix: the
template's bare `<body>` initially tripped axe's landmark-region check and
was wrapped in `<main>` in both copies. See `MANIFEST.md`'s Revision history
for the matching entry.

### Week 5 depth pass — approved

Approved by the owner on 2026-09-12 ("ok do it"). The owner subsequently
confirmed that visual details remain pending while text teaching and templates
are completed. This pass extends the earlier activity-numbering-only scope;
worked entries explicitly remain incomplete visual production references.

**Problem addressed.** The prior lecture named character/location bible fields but
did not model writing or revising an entry. The workshop had a useful blind
peer check, but no numbered activities or timings. The deck repeated the
outline. Prior wording promised that identical text produces the same
person and that references remain unchanged forever; the revision should
distinguish a continuity specification from a guarantee of model output,
and stable facts from deliberate, documented revisions.

**Outcome and boundaries.** Teach students to write concrete
character/location entries and diagnose missing or ambiguous information
through a partner's independent reading. Preserve both existing workshop
`spec:` bullets verbatim, dates, teacher, links, and assessment requirements.
No image generation is required to complete this text-based workshop.
Owner evidence, including OWN-W05, remains deferred and unfulfilled.

**Lecture (90 minutes).** Recap of Week 4's continuity needs (5); explicit
outcomes (5); teach and model character fields, location fields, costume/
prop references and a short visual-style specification (45); vague versus
repeatable entry comparison (15); guided diagnosis and revision of an
ambiguous entry (15); synthesis and workshop preparation (5). The worked
example should actually author entries for Nadia, Theo and the kitchen,
using established story facts and approved visual references. Explain what
must remain fixed, what may vary per shot, and how to record an intentional
revision. Verify any tool-specific claims with primary documentation during
implementation; avoid promising that repeated wording guarantees identity.

**Workshop (120 minutes).** Keep the existing requirement to bring draft
entries for every named character and location. Make all activities explicit
with Instructions and Expected output:

| Activity | Minutes | Expected output |
|---|---:|---|
| 1. Recap and inventory | 10 | List of characters/locations and missing draft entries |
| 2. Make details repeatable | 25 | Revised entries with concrete observable fields |
| 3. Blind partner read-back | 20 | Partner's written account of the protagonist, before author explanation |
| 4. Diagnose and revise | 30 | Corrections tied to mismatches, omissions or ambiguities |
| 5. Dailies review and recheck | 25 | Peer comparison against the revised entry; note reader familiarity if no fresh partner is available |
| 6. Completion check | 10 | Both existing spec bullets checked, with any remaining gap named |

Activities 2–4 form the 75-minute main exercise. Judge read-back against
the entry's stated facts, not unspoken author intentions. Distinguish
reader omission from ambiguous writing before deciding which text to fix.

**Deck and resources.** Synchronize the deck with the approved lecture:
learning outcomes, entry fields, worked excerpts, contrast, judgement task,
peer-check process and final checklist. Produce actual authored teaching
examples and a printable/downloadable character-and-location worksheet,
with canonical files under `resources/week-05/`, served copies under
`public/resources/week-05/`, and a materials record. The worksheet should
include reference/version, fixed facts, allowed variations and peer-feedback
space as scaffolding, not new assessed requirements. Reference images remain
optional; choose image formats/tools only if visual assets are subsequently
requested. Do not fabricate a production test or a demonstrated consistency
result. Add teaching-asset records only when those assets actually exist.

**Dependencies and unresolved decisions.** CC is currently producing Week 4
images per the owner. Before authoring Nadia's appearance, wardrobe, phone
or kitchen details, inspect the accepted Week 4 references and their records;
unapproved generated details are not automatically story canon. Propose any
missing facts explicitly rather than inventing a second incompatible world.
Theo is currently represented by the incoming call in the closing example;
confirm his required representation from the accepted story material before
inventing an on-screen design. If the optional reference images are not yet
accepted, the text structure can be drafted with undecided fields clearly
identified, without presenting them as finished examples.

**Scope and implementation order.** re-read current files and
git status; resolve reference-dependent facts; author the lecture and worked
entries; structure the workshop and worksheet; synchronize slides; verify
and update the handoff. Content review stays within Weeks 4–6. Week 6's
current lecture expects the bible in the pre-production package; no Week 6
edit is proposed. Avoid Week 4 files and global styles. Re-read shared
PLAN.md/MANIFEST.md immediately before narrowly editing them; preserve CC's
work and do not treat earlier file snapshots as current.

**Acceptance and verification.** Every required workshop concept is taught
in the lecture; all character/location entries required by the existing
spec are accounted for; the worked entry demonstrates how the peer test is
judged; numbered activities total 120 minutes; slides reflect the approved
content; downloads resolve and canonical/served copies match. Inspect page,
deck and printable layout at the prescribed marking viewports. Run
`pnpm typecheck` and `pnpm build` after implementation; report failures from
concurrent work separately. Verification results are recorded in `handoffs/week-05.md`; an end-to-end
120-minute workshop trial remains unperformed.

**Implementation status (2026-09-12).** Approved text/template scope is complete.
Lecture, six-activity workshop and 15-slide deck are integrated; authored draft
entries and a three-page printable worksheet have matching served copies.
Typecheck/build passed; desktop, phone and print QA are recorded in the
Week 5 handoff. Visual production fields remain pending by owner instruction.

**Current status (per `handoffs/week-05.md`):** fully implemented and
verified — this is closed, historical work.

### Weeks 6–12 depth pass — approved

Approved by the owner on 2026-09-12 ("build all the following weeks, I will
check them when I am back in 2 hours"), extending the same depth-pass scope
already approved and precedented for Week 5 above to the remaining
outline-only weeks. The per-week technique/workshop-mode mapping table
earlier in this section (sourced from `RESEARCH.md`) is the specification
each week's rewrite follows; this entry records the implementation, not a
new technique decision.

**Problem addressed.** Weeks 6–12's lectures were `## Outline`-only bullet
lists with no worked example, misconception contrast, or guided-judgement
exercise; their sessions described the workshop in unnumbered prose instead
of the required numbered-activity format; their decks mirrored the
skeletal outlines. Week 7 additionally still described the pre-correction
ending ("her hand finally moving toward the phone, [never actually
answering]"), contradicting the corrected canonical ending already fixed
in Week 4 (she accepts on the final ring, lifts the phone, and says "Hey").

**Outcome and boundaries.** Every lecture now follows the established
six-part shape (outcomes, technique, worked example, misconception
contrast, guided judgement with a `<details>` answer, synthesis); every
session's "In the workshop" section is rewritten as numbered `Activity N`
entries summing to exactly 120 minutes, with existing `spec:` frontmatter
bullets preserved verbatim; every deck is resynchronized to its lecture and
session. No new story facts were invented — every worked example either
reuses established canon (the closing beat, the whole-short schedule from
Week 6, the corrected ending) or is explicitly disclaimed as an authored
teaching example, never presented as a report of an actual generation,
consistent with the "Real production material, never invented" rule. No
week's learning outcomes, spec bullets, or assessment weighting changed.

**Per-week specifics:**

- **Week 6 — Planning before generating.** Technique: the shot list as a
  dependency schedule, not a wish list. Worked example: a 7-shot whole-short
  schedule extending Week 4's closing five with two new shots covering the
  0:00–1:25 segment Week 2 only described in prose; every shot's "depends
  on" column is read against Week 5's still-pending bible fields. Workshop
  mode: Comprehensive-Review-style dailies, presenting the schedule aloud
  and defending one cut (a drafted-then-cut fridge-photo insert, dropped
  because it repeats the reach-and-stop insert's argument).
- **Week 7 — From frame to performance.** Technique: Weston's moment-before
  applied to prompting — a concrete antecedent circumstance, not a mood
  word. **Also corrects the stale ending text** in both the lecture and
  deck to match the canonical corrected ending. Workshop mode: rehearsal,
  with a dailies-review screening of both takes before the note behind
  each is revealed.
- **Week 8 — Directing the AI performer.** Technique: Mamet's
  objective/tactic framing reused as a three-way diagnostic rubric for a
  failed take (note, reference, or model). Workshop mode: rehearsal, with a
  group dailies-review of three takes.
- **Week 9 — Continuity and production.** Technique: AFI's dailies-review
  ritual formalized as the workshop's own structure — watch cold, log
  precisely, repair only what's flagged. Workshop mode: construction, with
  a group-screened continuity log.
- **Week 10 — Editing and dramatic rhythm.** Technique: Mamet's
  shot-as-argument extended to cut points and pacing. Workshop mode:
  construction, with a blind hold-vs-cut-early comparison (a partner
  reads each cut's argument before being told which is which).
- **Week 11 — Directing with sound.** Technique: Weston's single-note
  discipline applied to a voice, plus a Meisner-adjacent responsiveness
  framing for line reading, explicitly flagged in-lecture as this course's
  own inference rather than documented Meisner-for-directors pedagogy (per
  `RESEARCH.md`). Workshop mode: two explicit phases, rehearsal (directing
  the line) then construction (building the sound pass around it).
- **Week 12 — Screening, critique, and revision.** Technique: the
  cross-program screening-and-critique ritual (AFI dailies review, NYU's
  weekly Master Class, NFTS's rushes cinemas), tightened into a
  Comprehensive-Review-style defend-three-decisions interview. Workshop
  mode: cold group screening followed by specific-alternative critique.

**Scope and implementation order.** Re-read each week's current files and
its immediate neighbours before rewriting; content review stayed within
each week plus its adjacent weeks, never wider, per the standing
per-week-check boundary in `CLAUDE.md`. No Week 1–5 file was edited except
where already covered by the Week 5 entry above.

**Acceptance and verification.** Every lecture's worked example either
reuses established canon or is explicitly disclaimed; every session's
activities sum to 120 minutes with `spec:` bullets unchanged; every deck is
resynchronized. `pnpm typecheck` and `pnpm build` are run after
implementation, with results recorded in each week's handoff
(`handoffs/week-06.md` through `handoffs/week-12.md`). An end-to-end
120-minute workshop trial remains unperformed for all seven weeks, the same
open item recorded for Week 5.

**Implementation status (2026-09-12).** Lectures, sessions, and decks for
Weeks 6–12 are rewritten to the approved shape. Week 7's stale ending text
is corrected. Verification (typecheck/build) and per-week handoffs are the
remaining steps before this entry can be closed out.

**Current status (per `handoffs/week-06.md` through `handoffs/week-12.md`):**
fully implemented and verified, including per-week `pnpm check` results —
this is closed, historical work.

### Week 2 — good-story criterion addition — approved

**Approval basis.** Owner requested, in conversation on 2026-09-13, adding
a "what makes a good story" discussion to Week 2's workshop, specifically
that short-form drama needs an emotional hook and should avoid lengthy
dialogue and abstract internal monologue. When asked whether this should
be workshop-only or taught first, owner confirmed the fuller scope: teach
it in the lecture, then discuss/apply it in the workshop — per
`CLAUDE.md`'s teach → practise → assess rule, since this is a
disciplinary concept, not tool mechanics.

**Problem addressed.** Week 2's lecture already tests a logline's
objective/obstacle and a premise's scope, but never states a criterion
for story *quality* specific to short-form drama — why an emotional hook
matters, and why lengthy dialogue or abstract internal monologue work
against a two-to-four-minute film. The existing "Before It Stops" premise
already avoids both (no dialogue exposition of the estrangement, no
internal monologue) but the lecture never named that as a deliberate
choice.

**Approach.** Add a new lecture subsection stating this as a named
criterion, illustrated by pointing at what the existing "Before It Stops"
premise already does (and deliberately doesn't do) rather than inventing
a new example. Add a matching, short discussion point to the workshop's
existing task, folded into the existing "Write and pair up" activity
rather than a new timed activity — Week 2's session predates the
numbered-activity-with-fixed-minutes convention (`CLAUDE.md` → "Workshop
structure: explicit numbered activities"), and this addition doesn't
warrant retrofitting that convention on its own.

**Outcome and boundaries.** No `spec:` bullet changes — this is a
teaching/discussion addition, not a new completion criterion. No change
to the running example beyond naming, explicitly, a choice "Before It
Stops" already makes. One new deck slide reflecting the lecture addition;
no change to the deck's existing structure otherwise.

**Implementation status (2026-09-13).** Lecture, session, and deck
updated. No dedicated Week 2 handoff file exists; this change is small,
scoped to teaching text only, and has since been covered by the multiple
whole-project `pnpm check` passes recorded in later 2026-09-13 entries
below (e.g. the Week 6/Assignment 1 passes), all of which passed with 0
type diagnostics and no accessibility/link/deck violations.

### Week 6 — bible → keyframes → generated shots pass — approved

**Approval basis.** Owner requested, in conversation on 2026-09-13,
extending Week 6's existing shot-list-as-schedule teaching to explicitly
name the chain between a locked bible and a generated shot: a bible fixes
identity; a keyframe translates that identity into one shot's specific
still (or, for a continuous shot, a starting and an ending still); a
generated shot adds performance, action, timing, and camera movement on
top of the keyframe(s). Owner specified the worked example in detail —
"Before It Stops"'s final continuous tilt (shot 7): a starting keyframe
low on Nadia's hand and the phone on the table, an ending keyframe with
the phone at her ear for "Hey," and the directed transition between them
(she accepts and lifts while the camera tilts up, no cut) — and asked the
workflow be stated as tool-dependent (some tools take both a start and end
reference image; some take only one, in which case the end keyframe
becomes an evaluation target rather than a second input), and that
matching keyframes not be conflated with a finished shot: the movement
between them still has to be directed and evaluated separately. Owner also
asked the stale claim that Nadia, the kitchen, and the phone are all still
"pending" in Week 5's bible be replaced with the current state — these
references were generated and integrated into `week-05.md` on 2026-09-13
(`resources/week-05/materials.md`), with the kitchen's full production
approval as the one remaining open item.

**Problem addressed.** Week 6 taught the shot list as a dependency
schedule but stopped one level short of how generation actually works: it
never named the keyframe as the shot-specific artefact between a bible
reference and a generated shot, and never said that matching keyframes
doesn't by itself produce a good shot. Separately, Week 6's citation of
Week 5's bible had gone stale the moment the Nadia/kitchen/phone
references were actually generated — continuing to describe them as
"pending" was no longer accurate and would read as either an error or an
unresolved dependency that had, in fact, resolved.

**Approach.** Add a new lecture section ("Bible, keyframes, generated
shots: three different jobs") stating the three-tier chain and the
matching-isn't-sufficient point, pointing back at Week 5's own
fixed-identity-versus-changing-state table by name rather than re-deriving
it. Extend the outcomes list (a fourth outcome for the matching-isn't-
sufficient judgement) and the misconception table (a fifth row). Replace
the single "Depends on" table in "The real demonstration" with a table
tracing keyframe(s) → bible reference(s) → what the generated shot adds
per shot, giving shot 7 its two keyframes as an authored planning example
(disclaimed the same way Week 7 disclaims its own worked takes) and adding
a short paragraph distinguishing narrative order from preparation order
(shot 1, blocked on the kitchen's pending approval, vs. shot 6, already
ready, despite coming later in the story). Correct the stale "recorded
pending" claim to name the current state and the one real open item.
Revise the workshop's Activities 1, 2, 4, and 5 to practise naming
keyframes and their bible references and building a preparation list,
without changing either `spec:` bullet or the 120-minute total. Update the
deck to match, including new slides for the three-tier chain, the shot-7
worked example, matching-isn't-sufficient, tool-dependent input, and
narrative-vs-preparation order.

Two small neighbour syncs are included, since leaving them would make
Week 6 self-contradicting the moment it changes: Week 7's one sentence
citing "week 6's schedule" flagging pending references (now false) is
corrected to reflect current status; `MANIFEST.md`'s `BIS-W05-ENTRIES`
status cell, still reading "visual design pending," is updated to record
the 2026-09-13 integration, with a new revision-history line appended
(the existing 2026-09-12 entry is left as an accurate historical record,
not rewritten). Week 5's own lecture/session/handoff text is not touched —
it already states the current state correctly; only Week 6's citation of
it, and the shared manifest, were stale. `handoffs/week-05.md` is also
stale (still says no image generation was performed) but fixing it isn't
necessary for Week 6's correctness and is out of scope for this pass —
flagged in Week 6's handoff instead.

**Outcome and boundaries.** One new lecture learning outcome added; no
`spec:` bullet or assessment-weighting change. No new images, video, or
audio generated — the shot-7 keyframe description is authored planning
text, the same status as the existing shot list and worked cut. Scope
limited to Week 6 plus the two minimal Week 7/MANIFEST syncs described
above; Week 5's own files and `handoffs/week-05.md` are explicitly out of
scope.

**Implementation status (2026-09-13).** Lecture, session, and deck
updated; `week-07.md`'s one sentence corrected; `MANIFEST.md` status cell
and revision history updated.

**Current status (per `handoffs/week-06.md`):** verified —
`pnpm typecheck` 0 errors/warnings/hints, `pnpm build` passed with 0
accessibility violations, no broken links, all 12 decks passed structural
checks, both `spec:` bullets confirmed byte-identical via `git diff`; this
is closed, historical work.

### Assignment 1 — pending-decision alignment pass — approved

**Approval basis.** Owner flagged, in conversation on 2026-09-13: "a1 has
the same problems, and can not require voice or something not learned as
spec" — referring to the raw-filename fix just made in Week 6 as the same
class of problem (content assuming or requiring something the student was
never actually given or taught), applied here to a required skill instead
of a jargon term.

**Problem addressed.** `assignment-1.md` required every bible decision
"required by the planned shots" to be **resolved**, with no pending
exception (`spec:` bullet 6), and separately stated "no required decision
remains pending" outright (`spec:` bullet 10) — directly contradicting
Week 5's own explicit teaching ("An undecided field should say **pending**,
with the decision needed to close it") and the course's own worked
example, which itself leaves Nadia's voice pending throughout Weeks 5–7.
Section 3's instructions demanded students "resolve the vocal design" for
any voiced character, and section 5 required "any required pending
fields" be resolved before submission. No lecture or workshop by week 6
teaches how to actually select or generate a voice reference — that
belongs to Week 11 ("Directing with sound," "Directing a voice like a
face"), which lands after Assignment 1 is due. This was a teach →
practise → assess violation: the assignment assessed a skill not yet
taught.

**Approach.** Align A1's language with the pending model Week 5 already
teaches, rather than inventing a new policy: `spec:` bullets 6 and 10,
the "Locked" definition, section 3's voice instruction and its
Nadia/Theo follow-up sentence, section 5's dependency and closing
paragraphs, the "Work through the package" intro paragraph, and the
"World and continuity design" marking-criteria row were all revised to
read "resolved, or explicitly marked pending with the specific decision
needed to close it" instead of a bare "resolved"/"no pending decision."
The point that a pending decision blocks a *shot* (production-order
discipline, taught in Week 6) is kept; only the claim that a pending
decision blocks *submission* is removed.

**Outcome and boundaries.** Two `spec:` bullets changed in wording only —
neither adds nor removes a submission requirement, a weight, or a due
date; they now permit an already-taught state (justified pending) instead
of silently forbidding it. No change to the four submission sections, the
30/30/40 marking weights, or Week 5's own text. Most bible fields
(appearance, costume, props, locations) remain expected to be resolved,
since the tools to do so are already taught by week 6; only fields tied to
later-taught skills (voice design, chiefly) are expected to realistically
land on "pending, justified" for most students — the spec wording doesn't
carve voice out by name, since the same escape valve should apply to any
field a student genuinely can't close yet.

**Implementation status (2026-09-13).** `assignment-1.md` updated per the
above. `pnpm typecheck`: 0 errors/warnings/hints. `pnpm build`: passed — 0
accessibility violations, no broken internal links, all 12 decks passed
structural checks. Direct check: `grep` for "resolve the vocal design" and
"no required decision remains pending" in `assignment-1.md` returns
nothing.

**Current status (per `handoffs/week-06.md`, "A1 pending-decision
alignment pass — 2026-09-13"):** verified and closed — the earlier
"pending-decision" problem this pass fixed does not recur elsewhere in
the assignment; a separate, unrelated gap (Week 6's 7-shot schedule vs.
the current 5-shot screenplay draft) is tracked live as an open item in
`PLAN.md`'s "Week-by-week asset checklist" area and in `handoffs/week-06.md`
directly, not here.

## Assignment 1 — worked guidance and detailed spec

Owner instruction (2026-09-13): use "Before It Stops" to guide students through
Assignment 1 and make its spec more detailed. Scope: the existing assessment
page; preserve its deadline, assessment weight and three marking weights.

Problem: the brief names four materials but does not define their required
fields, submission format, cross-document agreement or production readiness.
Approach: specify one readable PDF with four named sections; show the existing
reference logline/premise, screenplay beats and intent, bible entries, and
five-shot storyboard planning draft alongside instructions for students'
own films. Expand spec into observable checks for complete screenplay coverage,
identity versus changing state, unique shot purpose, matching shot IDs,
framing/movement/action, estimated timing and named production dependencies.
Explain how the existing 30/30/40 marking categories judge those materials.

Assumptions and limits: the package plans the already-required 2–4 minute final
film; no arbitrary shot count, new scene count, generated footage, polished
illustration or additional assessment component is required. Existing course
examples are authored teaching drafts, not a complete assessed submission or
owner production evidence. The current five-shot screenplay estimate (24–38 s)
and pending voice decisions must be stated honestly; do not extend the story
or invent resolved design facts. Read earlier example resources only to reuse
them, not as a project-wide curriculum review. Record the outdated Week 6
seven-shot/pending-visual references in its handoff; do not rewrite the lecture
or workshop under this assessment-only instruction.

**Current status (per `handoffs/week-06.md`, "Assignment 1 update —
2026-09-13" and "A1 reference-link cleanup — 2026-09-13"):** implemented
and verified (`pnpm check` passed both times) — this is closed, historical
work. A related, still-open gap (Week 6's 7-shot schedule vs. the current
5-shot screenplay draft, which A1 already labels a method demonstration,
not a runtime-complete submission) is tracked live in `handoffs/week-06.md`,
not here.

## Revision history

Full ledger through 2026-09-13, moved here in full as part of the
2026-09-13 documentation reorganisation (see `PLAN.md`'s "Documentation
reorganisation — approved" and "Plan governance"). `PLAN.md` keeps a short
pointer to this section and starts a fresh, ongoing ledger of its own
below that pointer.

- **2026-09-12** — Owner authorized the Weeks 6–12 depth pass recorded in
  "Weeks 6–12 depth pass — approved": Weeks 6–12's lectures, sessions, and
  decks rewritten from outline-only/unnumbered-workshop form to the
  established depth-pass shape, following the per-week technique mapping
  table already approved earlier in this section. Includes correcting
  Week 7's lecture and deck, which still described the pre-correction
  ending, to match the canonical ending already fixed in Week 4. No
  learning outcome, spec bullet, or assessment weighting changed.
- **2026-09-13** — Owner authorized "Week 2 — good-story criterion
  addition — approved": a new lecture subsection and matching workshop
  discussion point on why short-form drama favors an emotional hook and
  observable behaviour over lengthy dialogue or abstract internal
  monologue, illustrated against the existing "Before It Stops" premise.
  One new deck slide added. No spec bullet, learning outcome, or
  assessment weighting changed.
- **2026-09-13** — Owner authorized "Week 6 — bible → keyframes →
  generated shots pass — approved": a new lecture section naming the
  bible → keyframe → generated-shot chain, worked through "Before It
  Stops"'s shot 7 (start/end keyframes for the final continuous tilt) as
  an authored planning example; the outcomes list, misconception table,
  "The real demonstration" table, guided judgement coda, and "What you
  take to the workshop" all extended to match; the workshop's Activities
  1, 2, 4, and 5 revised to practise naming keyframes and bible
  references without changing either `spec:` bullet or the 120-minute
  total; the deck resynchronized with five new slides. The stale claim
  that Nadia, the kitchen, and the phone were all still "pending" in
  Week 5's bible was corrected to the current state (all three generated
  and integrated 2026-09-13; only the kitchen's full production approval
  remains open). Two minimal neighbour syncs included: one sentence in
  Week 7's lecture, and `MANIFEST.md`'s `BIS-W05-ENTRIES` status cell
  plus a new revision-history line. No learning-outcome removal, spec
  bullet, or assessment weighting changed; Week 5's own files and
  `handoffs/week-05.md` left untouched and out of scope.
- **2026-09-13** — Owner authorized "Assignment 1 — pending-decision
  alignment pass — approved": `spec:` bullets 6 and 10, the "Locked"
  definition, section 3's voice instruction, section 5's dependency and
  closing paragraphs, the package intro paragraph, and the "World and
  continuity design" marking row all revised so a bible decision may be
  resolved *or* explicitly marked pending with the decision needed to
  close it, matching what Week 5 already teaches and the course's own
  worked example already does for Nadia's voice. Previously, both spec
  bullets forbade any pending decision outright and section 3 demanded
  voice be "resolved," which assessed a skill (selecting/generating an
  actual voice reference) not taught until Week 11. No submission
  section, marking weight, or due date changed.

- **2026-09-12** — Owner authorized the four Week 1–2 corrections recorded
  in "Week 1–2 teaching corrections": draft-to-revision logline teaching,
  a filmability walkthrough with explicitly untested timing estimates,
  progressive disclosure of the Week 1 demonstration, and removal of
  developer-facing index/research references. Implementation is limited to
  these weeks and their teaching text assets; no assessment spec changes.

Each entry records a departure from this plan that was proposed, approved,
and then applied — not routine work that simply followed the plan as
written, per "Plan governance" above.

- **2026-09-04** — "Visual direction" typography/spacing/motion/imagery,
  previously left open, settled as the "Director's Notebook" hybrid
  direction described in that section (with selected production-label
  elements from a rejected "Slate & Grain" alternative). `astromotion`
  confirmed deck-only and ruled out for site-wide motion. Approved before
  Phase 2 (global styles in `PageLayout.astro`) was implemented.
- **2026-09-04** — "Visual direction" imagery bullet replaced: the literal
  filmmaking-illustration approach (risograph-style director's chairs,
  cameras, studio scenes, stylised-portrait people) used to generate the
  Home hero and both people portraits is abandoned for decorative site/deck
  artwork, in favour of an abstract flat-geometric graphic system (warm
  cream, black/warm gold dominant, muted dark green accent). New
  "Decorative artwork vs. teaching visuals" bullet added to make explicit
  that this abstract system applies only to decorative chrome, never to
  pedagogical or real-production imagery. Applied after the Home hero,
  Marisol Quaye and Idris Fenn portrait pilots had already been generated
  and committed to working tree under the old direction; rollout is
  pilot-first — one new Home hero to be generated and approved before the
  portraits or any other decorative piece is redone.
- **2026-09-04** — Home hero pilot (abstract system) reviewed and approved.
  Rollout extended per owner instruction: the other four top-level index
  pages (Lectures, Workshops/`sessions`, Assessments, People, Policies) each
  get their own hero image from the same abstract system, wired through the
  existing `heroImage`/`heroImageAlt` props; both people portraits and the
  social card (`card.png`) are regenerated as non-figurative abstract
  compositions in the same family rather than kept as stylised-illustration
  figures. "Hero imagery extended to the other four index pages" bullet
  added to "Visual direction" above recording the approved scope. A separate
  suite of abstract images for the week 1 slide deck (`week-01.deck.mdx`)
  was also requested and approved, using `astromotion`'s `![bg ...]`
  background-image syntax — decorative deck backgrounds were already listed
  in scope under "Decorative artwork vs. teaching visuals" above, so no
  further plan text was needed to cover it.
- **2026-09-07** — New "Session content depth pass" section added: lectures
  move from outline bullets to taught prose, and sessions get a named
  workshop activity format plus, where it fits, a peer-verification
  completion criterion (matching the shape already used in week 5's
  session). Approved to apply one week at a time; week 1 approved first —
  lecture (`week-01.md`), session (`01-getting-started.md`, third `spec:`
  bullet added), and deck (`week-01.deck.mdx`, "This week's task" slide)
  updated accordingly.
- **2026-09-07** — Week 1's teaching design revised again, grounded in
  `RESEARCH.md`: lecture and workshop made strictly separate course-wide
  (the "Bridge to the workshop" step removed from the shared lecture
  template; workshops now open with their own recap-and-briefing step);
  both templates above updated to include explicit learning outcomes, a
  real-demonstration walkthrough slot, and guided student judgement. The
  workshop is rebuilt around one instructor-provided locked scene
  (description, reference, objective, and intended audience
  interpretation) shared by the whole class, so a redirect note adjusts
  only the playable action/timing/emphasis/degree and never the objective.
  Blind peer review reworded to require identifying the observable change,
  its location, and its effect on the partner's reading of the character's
  intention, not the note's exact wording. Week 1's per-week mapping row
  set to `in progress`, not `done` — the real Note A/Take A → Note B/Take B
  demonstration remains required and unproduced. `week-01.md`,
  `week-01.deck.mdx`, and `01-getting-started.md` updated accordingly;
  `RESEARCH.md` left as-is per instruction.
- **2026-09-11** — Owner-approved global substitution: the placeholder
  running example *"Table for One"* is replaced everywhere by *"Before It
  Stops"* (protagonist Nadia, brother Theo, on the last night before her
  late mother's apartment is cleared — full premise in "Structure" above).
  Explicitly a flavour-text swap, not a curriculum redesign: every learning
  outcome, weekly sequence, assessment requirement, duration, and template
  already approved stays unchanged. New `MANIFEST.md` created as the single
  source of truth for teaching-example asset production (Claude Code /
  Codex / owner division of responsibility, asset status pipeline,
  prioritized Sora brief queue), superseding the old "'Table for One' asset
  plan" section's per-asset detail — that section now states policy only
  and points at the manifest. Week 1's real Note A → Take A → diagnosis →
  Note B → Take B demonstration pair (produced by Codex with `sora-2`,
  QA'd, recorded in `resources/week-01/materials.md`) is integrated into
  `week-01.md` and `week-01.deck.mdx`, served from
  `public/resources/week-01/`; Week 1's status flips from `in progress` to
  `done`. `01-getting-started.md`'s workshop scene changed to a distinct
  beat from the same story (deciding whether to call back after the call
  goes to voicemail) so the exercise doesn't rehearse a diagnosis students
  just watched solved. Weeks 2, 3, 4, 5, 7, 10 and 11's lecture/deck prose
  re-skinned to the new story on the same throughline "closing scene" (the
  last ring before the call would go to voicemail, her hand finally
  moving) that the old plate-slide/Del/Mara scene occupied; weeks 6, 8, 9
  and 12 were untouched, since they never named the running example.
  `CLAUDE.md` and `PROCESS.md` left unchanged — their "Table for One"
  mentions are historical citations of when a rule was formalized or a
  commit's actual content, not statements of current curriculum content.

- **2026-09-11 (later same day).** `01-getting-started.md`'s workshop
  scene changed again, superseding the "call back after voicemail" beat
  recorded above: the workshop now uses a real film clip as its
  performance reference — Cooper watching adult Murph's recorded message
  in *Interstellar* — rather than a "Before It Stops" beat. Confirmed with
  the owner as an intentional edit, not an accident, when it appeared as
  an unplanned on-disk change mid-session; approved to keep as-is rather
  than reverting to the voicemail-callback scene. The lecture and deck
  still teach and demonstrate entirely on "Before It Stops" material —
  only the workshop's own exercise now draws on a different, real source.
  See "Week 1 status" in `PLAN.md`.

- **2026-09-11 (later still).** Reverted by owner instruction: the
  Interstellar film-clip reference is removed from `01-getting-started.md`.
  The workshop's locked scene goes back to a "Before It Stops" beat — the
  call has just gone to voicemail unanswered, and Nadia is deciding
  whether to call her brother back — distinct from the lecture's
  reach-and-withdraw beat so the workshop isn't re-solving the diagnosis
  students just watched. See "Week 1 status" in `PLAN.md`.

- **2026-09-11 (later still, same day).** Student-facing tool for week
  1's workshop settled as **Pika**, not `sora-2` (the teaching demo's
  tool). Checked at the owner's request before writing detailed,
  tool-specific workshop steps: Sora's consumer product was discontinued
  April 2026 and its API sunsets 2026-09-24, so it isn't viable for a
  semester-long student exercise regardless of what the teaching demo
  used. `01-getting-started.md` rewritten with Pika-specific steps,
  screenshot placeholders (owner supplies the actual captures, per the
  "Real production material, never invented" rule — no fabricated UI
  mockups), and explicit per-person roles for the paired dailies-review
  step. See "Week 1 status" in `PLAN.md`.

- **2026-09-11 (evening).** Owner instruction: redesign the workshop
  around the constraint that two independent text-to-video generations
  cannot reliably hold a scene's continuity, so "only the note changes
  between takes" was never actually enforceable by the previous design.
  Replaced with a diagnose-first structure on one **instructor-provided**
  anchor (image, locked base prompt, fixed settings, a prepared Take A) —
  students blind-watch and diagnose Take A, write their own Note B, then
  either remix it (tool permitting) or select and justify the best fit
  among several instructor-provided Take B candidates. Also reverted the
  workshop to **tool-agnostic** instructions — the Pika-specific steps
  from the previous entry are removed along with their screenshot
  placeholders, since naming one platform tied the exercise to that
  platform's UI for no pedagogical benefit once generation moved from
  "student does it" to "instructor supplies it." `01-getting-started.md`
  rewritten accordingly; frontmatter `spec:` bullets updated to match the
  new assessed criteria (a diagnosed observable gap, a genuine Note B
  redirect, a generated-or-selected Take B with justification, and a
  partner's independent blind read). New required teaching asset
  `BIS-W01-WORKSHOP` added to `MANIFEST.md`, status `NOT STARTED` — the
  workshop cannot run in class until it's produced; brief at
  `resources/week-01/workshop-brief.md`. See "Week 1 status" in
  `PLAN.md`.

- **2026-09-11 (night).** Second week of the "Session content depth pass"
  applied, per the mapping table's week 2 row. `week-02.md` rewritten from
  outline bullets into taught prose: explicit learning outcomes, Mamet's
  objective/tactic framing taught as "a logline is a claim with two
  testable parts, not a summary," a summary-vs-test misconception contrast,
  and guided judgement on a logline missing an obstacle — worked through
  the existing served logline/premise
  (`/resources/week-02/logline.txt`, `/resources/week-02/premise.txt`,
  already recorded in `MANIFEST.md` as `BIS-W02-LOGLINE`/`BIS-W02-PREMISE`;
  no new asset produced). `02-first-review.md` restructured into the
  approved 120-minute workshop template (recap and briefing, main exercise,
  dailies review, completion check), rehearsal-adjacent mode per the
  mapping table; third `spec:` bullet added for the new peer-verification
  step — a partner who has read only the logline states the obstacle back
  correctly before seeing the premise. `week-02.deck.mdx`'s "This week's
  task" slide updated to match the new timing and peer-verification step;
  no other slide content changed.

- **2026-09-11 (later that night).** More practice material added to week
  2, ungraded, on top of the depth pass above; the mapping table's week 2
  row and the `spec:` bullets are unchanged. `week-02.md` gets a new "More
  loglines to test" section (Jaws, Finding Nemo, Die Hard, each broken into
  objective/obstacle) between the summary-vs-test contrast and the guided
  judgement example, using real films' publicly known plots as teaching
  material — not the "real production material, never invented" rule,
  which governs this course's own demonstrated work. `02-first-review.md`
  gets a new ungraded warm-up step ("test a familiar film," 10 min) between
  the recap and the main exercise, letting students rehearse the
  objective/obstacle peer-verification mechanic on a film they already know
  before doing it for real; a longer pick-list (adding Toy Story, The
  Matrix, Alien, Mad Max: Fury Road, WALL-E) keeps partners from all
  analysing the same three films the lecture already solved.
  `week-02.deck.mdx` gets one new slide distilling the three lecture films
  into title-plus-callout form, and a one-clause update to "This week's
  task" mentioning the warm-up.

- **2026-09-11 (later still).** Third week of the "Session content depth
  pass" applied, per the mapping table's week 3 row. `week-03.md` rewritten
  from outline bullets into taught prose: explicit learning outcomes,
  Weston's "moment before" taught as "a note names the antecedent
  circumstance, not an adjective," an adjective-note-vs-antecedent-note
  misconception contrast, a real-demonstration walkthrough on a new
  teaching text (`BIS-W03-SCENE` — a short screenplay-format scene playing
  the Week 2 premise's closing beat, with two intent notes, recorded in
  `MANIFEST.md` and `resources/week-03/materials.md`), and guided judgement
  on a raw "play it furious" note. `03-screenplay-workshop.md` restructured
  into the approved 120-minute workshop template (recap and briefing, main
  exercise, dailies review, completion check), rehearsal mode per the
  mapping table; third `spec:` bullet added for the new peer-verification
  step — a partner who has read only the intent note, not the scene,
  predicts the performance choice before it's revealed. `week-03.deck.mdx`'s
  "This week's task" slide updated to match; no other slide content
  changed. `OWN-W03` and the PLAN.md owner-evidence checklist remain
  outstanding.

- **2026-09-12.** Four owner-approved corrections to the week 3 depth-pass
  content and the Week 1 workshop's framing, scoped narrowly — no full
  curriculum-reviewer pass run.
  1. `BIS-W03-SCENE`'s two director's notes were result/adjective-laden
     ("active restraint," "too fast," "not casual," "not confident," "a
     decision that outran itself"), contradicting the lecture's own
     teaching point that a note names the antecedent circumstance, not a
     result. Rewritten to name concrete antecedents instead: the held look
     is grounded in Nadia having just taped the last box from her mother's
     kitchen shut, seconds before Theo's name appears; "Hey" is grounded in
     her hand having already pressed to accept the call before she's
     registered deciding to. `resources/week-03/scene.txt` (both the
     canonical and served copies), `resources/week-03/materials.md`,
     `week-03.md`, and `week-03.deck.mdx`'s margin-note slide all updated to
     match; `MANIFEST.md`'s `BIS-W03-SCENE` row revised to v1.1.
  2. `week-03.md` restructured so the scene link and an observation
     question appear before either note or the intended reading is
     revealed — students read the scene and form their own interpretation
     first. The notes and follow-on discussion now sit behind `<details>`/
     `<summary>` accessible disclosures.
  3. The week 3 peer-verification design changed: a partner previously read
     only the note and predicted the performance choice sight of the
     scene; now the partner sees only the isolated line/action plus its
     note (not the surrounding scene or the intended interpretation),
     describes one or more performance choices the circumstance could
     motivate, and only then is the scene context revealed for comparison
     against the intended dramatic function. `03-screenplay-workshop.md`'s
     third `spec:` bullet, dailies review, and completion check rewritten
     accordingly; `week-03.deck.mdx`'s task slide updated to match. The
     first two `spec:` bullets (≤2-page scene, ≥1 intent note) are
     unchanged.
  4. The Week 1 workshop's locked scene — previously described as "a beat
     further on" in the same story, implying it was the canonical
     continuation — is corrected to an explicitly counterfactual rehearsal
     variation: weeks 2 and 3 establish that Nadia answers the call on the
     final ring, so the workshop's "call went to voicemail" beat is a
     deliberate "what if she hadn't answered?" fork, not what actually
     happens next. "Week 1 status" (in `PLAN.md`), `01-getting-started.md`,
     and `resources/week-01/workshop-brief.md` reworded accordingly; the
     workshop's media, generation instructions, objective, and intended
     interpretation are untouched. `BIS-W01-WORKSHOP` stays `NOT STARTED`
     pending regeneration and QA under the corrected framing.
  See `MANIFEST.md`'s Revision history for the matching entry.

- **2026-09-12.** Added the Week 3 scene-planning scaffold described above
  ("Week 3 scene-planning scaffold" note, this section). `week-03.md`
  gained a new "From premise to a two-page scene: the writing process"
  section, inserted after Weston's "moment before" and before "The real
  demonstration" so the cold-read order is untouched: it teaches
  premise → decisive scene → scene change → five observable beats →
  screenplay form → director's note, worked through "Before It Stops"
  (want: answer Theo's call; obstacle: years of estrangement; beginning
  state: Nadia maintains the silence; ending state: she answers; the five
  beats from the phone ringing to her hand moving on the final ring),
  defines a beat as audience-observable and explicitly excludes shot/
  camera/edit decisions as week 4's job, and shows the beats converting
  directly into a slugline/action/dialogue fragment. Learning outcomes
  left unchanged — the process is taught in service of the existing three
  outcomes, not as a new one. A new downloadable worksheet,
  `resources/week-03/scene-planning-worksheet.txt` (served copy at
  `public/resources/week-03/scene-planning-worksheet.txt`, recorded as
  `BIS-W03-WORKSHEET` in `MANIFEST.md` and in
  `resources/week-03/materials.md`), walks a student through the same
  sequence for their own film; linked from this new lecture section.
  `03-screenplay-workshop.md` restructured around the worksheet with exact
  (not ranged) minute values summing to 120: recap and briefing (10), story
  anchor (10), scene change (10), five observable beats (15), screenplay
  conversion (25), director's note (10), dailies review (30, unchanged
  peer-verification design from the 2026-09-12 corrections above), and
  completion check (10). All three `spec:` bullets are unchanged — the
  worksheet adds no new graded requirement. `week-03.deck.mdx` gained six
  new sparse slides (one idea each: the premise-to-scene sequence; choosing
  the decisive scene; the beginning/end scene change; the five "Before It
  Stops" beats; converting one beat into screenplay form; the worksheet),
  inserted after the existing "The margin note" slide and before the
  "Before It Stops" quote slide; no existing slide content changed. Row 3
  of the per-week technique-mapping table above updated to name the
  worksheet-scaffolded sequence and the corrected peer-verification design
  in one place (it had still described the pre-correction design). Week 2
  (`week-02.md`, `resources/week-02/premise.txt`) and Week 4
  (`week-04.md`, `04-shot-breakdown.md`) checked directly and left
  unchanged — Week 2 already supplies the want/obstacle this section
  reuses, and Week 4 has no shot-level content pre-empted by it. See
  `MANIFEST.md`'s Revision history for the matching entry.

- **2026-09-12.** Five corrections to the Week 3 scene-planning scaffold
  above, made after `resources/week-02/premise.txt` was itself corrected
  (location: her late mother's apartment kitchen, not just "its kitchen
  table"; ending: she accepts the call, says "Hey," then listens — not
  "her hand finally moves toward the phone rather than away").
  1. **Genuinely blind cold read.** `resources/week-03/scene.txt`
     previously carried both director's-notes inline, so the lecture's
     "read the scene before reading any further" instruction wasn't
     actually blind. Split into a clean `scene.txt` (no notes, linked
     before the reveal) and a new `resources/week-03/scene-annotated.txt`
     (both notes reinstated in the margin, linked only after both
     `<details>` reveals). Both get served copies under
     `public/resources/week-03/`. `resources/week-03/materials.md`'s
     `BIS-W03-SCENE` section and `MANIFEST.md`'s matching row rewritten
     for the two-file split.
  2. **Worksheet timing, made consistent.** The lecture and deck said to
     complete the worksheet before the workshop; the workshop said to
     bring it blank. All three now say the same thing: download and read
     the worksheet before the workshop, complete it during the workshop
     on your own Week 2 premise. `week-03.md`, `week-03.deck.mdx`, and
     `03-screenplay-workshop.md`'s "Before the workshop" section reworded
     accordingly; the worksheet file itself already matched this and
     needed no change.
  3. **"Before It Stops" example synchronized.** `week-03.md`'s opening
     paragraph, its illustrative screenplay-form code snippet (slugline
     corrected from "INT. NADIA'S KITCHEN" to "INT. MOTHER'S APARTMENT -
     KITCHEN"), the "decisive scene" paragraph, and `week-03.deck.mdx`'s
     "choosing the decisive scene" slide and closing quote slide all
     updated to the corrected location and ending, including the
     reach-and-stop beat ("her hand drifts toward it, stops") ahead of
     acceptance on the final ring. The scaffold note earlier in this
     section, and `MANIFEST.md`'s `BIS-W03-SCENE` row, reworded the same
     way. The one dated Revision history entry above that also describes
     these beats is left untouched, per this file's own rule against
     silently rewriting history.
  4. **A subtler result-oriented note, corrected.** `week-03.md`'s "wish
     for a scene" table paired "Make the ending feel inevitable" with a
     note describing Nadia's changing belief over the scene — the same
     result-first failure the section teaches against, just narrated
     instead of stated as an adjective. Replaced with a concrete
     antecedent fact already true before the scene starts ("tomorrow the
     movers empty this kitchen for good"), and the explanation rewritten
     to say so explicitly, leaving the actual performance open.
  5. **Workshops written as explicit numbered activities.** New authoring
     rule added above, in "Workshop template (120 min)": every workshop's
     "In the workshop" section is written as titled, timed "Activity N"
     blocks with an Instructions and an Expected output part, applying
     course-wide going forward. `03-screenplay-workshop.md`'s eight phases
     restructured into Activities 1–8 on this shape; the exact per-phase
     minute values (10/10/10/15/25/10/30/10, summing to 120), the three
     `spec:` bullets, and the existing peer-verification dailies-review
     design are all unchanged — only the presentation structure changed.
  See `MANIFEST.md`'s Revision history for the matching entry.

- **2026-09-12 (recurring requirements made durable).** The explicit
  numbered-activity requirement above had only ever been recorded in this
  file and in conversation history, and was at risk of being dropped on a
  future week's workshop for exactly that reason. Two fixes, both to
  process rather than to any week's taught content:
  1. The rule itself moved to `CLAUDE.md` ("Workshop structure: explicit
     numbered activities"), which every session reads as a matter of
     course — this file's "Workshop template (120 min)" section now
     points there instead of restating it.
  2. A new per-week continuity mechanism: `handoffs/TEMPLATE.md` (a
     shared shape) and one `handoffs/week-NN.md` per week, recording that
     week's status and open questions only — never a standing rule,
     which stays in `CLAUDE.md` or a `PLAN.md` template and gets linked
     to by name. `CLAUDE.md`'s new "Weekly handoff records" section
     requires reading both `CLAUDE.md` and the relevant handoff before
     starting work on a week. `handoffs/week-03.md` written as the first
     instance, checked against the numbered-activity rule (no structural
     omissions found — Week 3's workshop already had all eight activities
     titled, timed, and carrying both an Instructions and an Expected
     output part, summing to 120 minutes).
  No week's learning outcomes, `spec:` bullets, or taught technique
  changed. See `MANIFEST.md`'s Revision history for the matching entry.

- **2026-09-12 (Week 4 shot-as-argument pass).** Added the Week 4 design
  described above ("Week 4 shot-as-argument pass," this section).
  `week-04.md` rewritten from five outline bullets into the full lecture
  template (explicit outcomes; shot vocabulary and composition/blocking/
  camera-movement content expanded into taught prose; Mamet's "shot as
  argument" taught by name per the mapping table's row 4; a real
  demonstration shot-listing the five corrected closing beats into five
  purposeful shots; a coverage-instinct/argument-instinct misconception
  table; a guided-judgement exercise). `04-shot-breakdown.md` restructured
  into five numbered Activities (recap and briefing 10, build the shot list
  40, sketch the thumbnails 35, dailies review 25, completion check 10,
  summing to 120) per `CLAUDE.md`'s numbered-activity rule; both `spec:`
  bullets unchanged. Corrected a pre-existing bug found while checking
  Week 4 against Week 3 (in scope per `CLAUDE.md`'s adjacent-week check):
  `week-04.md`'s outline and `week-04.deck.mdx`'s closing quote slide still
  described the "Before It Stops" ending as going to voicemail with her
  hand "finally moving toward the phone," the pre-correction version from
  before the Week 3 "Five corrections" entry above — both now read the
  corrected ending (she accepts on the final ring and says "Hey"). No new
  `MANIFEST.md` row created — the demonstration shot list is a genuine
  authored teaching artefact, the same status as `week-03.md`'s scene, not
  an owner asset or a claimed AI generation. Week 5 checked directly as
  Week 4's following neighbour and left unchanged — it's next in line for
  the same kind of pass per the mapping table, not part of this one; see
  `handoffs/week-04.md`. See `MANIFEST.md`'s Revision history for the
  matching entry.

- **2026-09-12 (Week 4 revision: deck slides, shot 5 staging, guided
  judgement).** Added the follow-on design described above ("Week 4
  revision: deck slides, shot 5 staging, guided judgement," this section).
  `week-04.deck.mdx` gained three slides (Mamet's test, the five-shot
  table, guided judgement) and an updated closing-quote wording; no other
  slide changed. `week-04.md`'s shot 5 rewritten as one continuous
  close-up take with explicit framing, blocking, and a tilt that follows
  her hand to her face, preserving the canonical ending. The
  guided-judgement scenario rewritten with a stated concealment intention
  and enough spatial detail (a housemate visible in the background) for
  the medium→wide-is-coverage / close-up→insert-is-argument judgement to
  follow, plus an explicit line scoping that verdict to this beat rather
  than to wide shots generally. No `spec:` bullet, learning outcome, or the
  running example changed; `04-shot-breakdown.md` untouched, since none of
  the three findings targeted it. `pnpm typecheck` and `pnpm build` both
  passed after the edits. See `MANIFEST.md`'s Revision history for the
  matching entry.

- **2026-09-12 (Week 4 teaching diagrams).** Added the eight teaching
  assets described above ("Week 4 teaching diagrams," this section): seven
  inline SVG diagrams in `week-04.md` (shot sizes, five-shot storyboard,
  shot 5 staged as one continuous take, composition, camera angle,
  blocking/camera movement, and the guided-judgement pairings), new
  `.at-diagram-row`/`.at-diagram-row--wide` CSS in
  `src/styles/visual-direction.css`, and a printable shot-list/storyboard
  template (`resources/week-04/shot-list-template.html` +
  `public/resources/week-04/shot-list-template.html` +
  `resources/week-04/materials.md`) linked from `week-04.md` and from
  `04-shot-breakdown.md`'s "Before the workshop" section (one sentence
  added; two `spec:` bullets, five Activities, and 120-minute total
  unchanged, confirmed by diff). No `spec:` bullet, learning outcome, or
  running example changed; no `MANIFEST.md` asset row added;
  `OWN-W03`/`OWN-W04` untouched. `week-04.deck.mdx` deliberately not
  touched. `pnpm typecheck` passed clean; `pnpm build` initially failed on
  one axe "region" violation against the standalone template page (no
  landmark wrapping its body), fixed by wrapping its content in `<main>` in
  both the canonical and served copies, then passed with 0
  errors/violations. See `MANIFEST.md`'s Revision history for the matching
  entry.

- **2026-09-12 (Week 5 approval).** Owner approved the Week 5 depth pass and explicitly deferred unconfirmed visual design facts. Expanded mapping row 5 to lecture/examples/template/deck work with six workshop activities; existing spec bullets and owner evidence remain unchanged.

- **2026-09-13 (Assignment 1 guidance).** Owner requested "Before It Stops"
  as the worked example and more detailed assessment spec. Added the scoped
  plan above before implementation; retain all existing dates and weights.

- **2026-09-13 (Weeks 7–8 real demonstration).** Owner selected the second
  existing frame for Week 7 and requested rejected footage be used in Week 8.
  Recorded the scoped Sora 2 production plan before making assets/content.

### 2026-09-13 — Week 5/7/8 corrections approved

Owner approved review items 1, 3 and 4 with "ok，修正134". Synchronise Week 5
visual-reference status and bible version 0.2 records. Week 7 workshop keeps
one concrete moment-before fixed and writes two performance directions varying
one choice; original spec and timings stay unchanged. Week 8 retains the real
Sora rejection and adds the owner-generated Jimeng candidates and observed
hover/timing diagnosis. Platform and prompt both changed, so no causal repair
or completed three-take selection is claimed. Items 2 and 5 remain outside this
implementation. No new generation, story facts or assessment changes.

### 2026-09-13 — Review items 2/5 approved

Owner approved "修正2/5". Week 6 distinguishes opening input frames from
ending evaluation targets, adds Nadia to shot 1's dependencies and aligns
workshop/deck language without prescribing two tool inputs for every take.
Week 8 teaches observed mismatch, possible note/reference/model causes and
next verification; group review reveals instructions/references before causal
inference. Original workshop specs, timings, story and assessment remain.

## Week-by-week asset checklist (owner's personal-production requirement — paused 2026-09-13)

Moved verbatim from `PLAN.md`'s "Week-by-week asset checklist" section,
which tracked the owner's own separate short-film production, required
week by week alongside the course, entirely distinct from "Before It
Stops" (the fixed lecture teaching example) and from any student's
assessed work. Owner paused this personal production on 2026-09-13 — not
cancelled, possibly resumed later, just not now — see `PLAN.md`'s
"Multimedia strategy" and Revision history for that decision. Every row
below still read `required — not started` (or, for the few weeks whose
prose had been updated to describe a teaching-demonstration integration,
that row's own Essential-asset status) at the moment this section was
archived; nothing the owner's own project required was ever actually
produced under it. Preserved here verbatim, original headings included,
as the record of exactly what that checklist asked for, should the owner
resume it later.

This is the actual deliverable this table exists to answer, and it comes
straight from what each week's session `spec:` and each assessment's
`spec:` already say — nothing here is invented. "Essential" means it's a
literal spec bullet; "Optional/stretch" is a suggested enrichment, marked as
such, never a spec requirement dressed up as one. **Status is the same for
every row right now: `required — not started`.** Nothing has been produced
yet; "Before It Stops" satisfies none of these rows because it is a fixed
lecture teaching example, not a real asset of the owner's own project (see
above) — this holds even for week 1, whose real demonstration pair is a
genuine artefact but not the owner's own required evidence.
Update each row's status as real material arrives — that's the point of
this table living in a plan file rather than being said once and forgotten.

Default placement for everything below is that week's own **Lecture page**
(see "Content and data architecture"). Two rows additionally surface on an
existing assessment page because they *are* the graded submission, not just
evidence of it — noted inline.

### Week 1 — What does a director actually do?

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| A directed pair: two takes of one small moment (image, line reading, or short clip) from two different director's notes, plus a sentence naming what changed and why | Establishes the direct→generate→evaluate→redirect loop the whole course runs on, before any tooling complexity | image, audio, or video (your choice) + text | Essential | Required — not started |

### Week 2 — Story for the screen

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Logline (one sentence: protagonist, want, obstacle, stakes) | The fixed point every later week's work gets checked against | text | Essential | Required — not started |
| One-paragraph premise/synopsis | Tests whether the story is filmable in 2–4 minutes with 1–2 characters, one location | text | Essential | Required — not started |

### Week 3 — From story to screenplay

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| One scene, standard screenplay format, ≤2 pages | The scene carrying the most narrative weight — travels forward to week 4's shot breakdown | text | Essential | Required — not started |
| Director's intent note on at least one line/action | Separates the performance choice from the plot reason — the margin note this whole course is built around | text | Essential | Required — not started |

### Week 4 — Thinking in shots

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Numbered shot list (type + one-clause purpose per shot, no two sharing a purpose) | Turns the week 3 scene into a sequence of decisions about what the audience is allowed to see, and when | text | Essential | Required — not started |
| Rough storyboard thumbnail per shot (frame, stick figure, movement arrow) | Has to be legible enough that someone else could stage the shot from it — this draft carries forward to week 6/Assignment 1 | image (sketch — hand-drawn or digital, doesn't need to be "good") | Essential | Required — not started |

### Week 5 — Building a consistent world

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Character bible entry per named character (age, build, wardrobe, one distinguishing feature, voice) | Generative tools have no memory between calls — this is what gets re-supplied every single time | text | Essential | Required — not started |
| World/location bible entry per location (fixed light, fixed detail, what has to hold shot to shot) | Same continuity problem, applied to place instead of person | text | Essential | Required — not started |
| Visual style / reference images accompanying each bible entry (mood-board style) | Suggested enrichment, not in the session spec — makes the bible checkable at a glance, not just readable | image | Optional/stretch | Required — not started (optional) |

### Week 6 — Planning before generating / **Assignment 1**

The graded submission for this week is the whole pre-production package —
these rows surface on the **Assignment 1** page as well as the week 6
**Lecture** page, since this is the artefact actually marked.

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Locked logline and premise | Assignment 1 is judged as "could a stranger shoot your film from this" — the logline is the anchor everything else has to agree with | text | Essential | Required — not started |
| Full screenplay (all scenes, standard format, director's intent notes throughout) | Same "stranger could pick it up" bar, extended to the whole short | text | Essential | Required — not started |
| Complete character and world bible | Continuity has to survive the whole shoot, not just one scene | text | Essential | Required — not started |
| Full shot list and storyboard, sequenced start to finish | The actual production schedule generation follows from week 7 onward | text + image (storyboard) | Essential | Required — not started |

### Week 7 — From frame to performance

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Anchor image for one chosen shot, generated straight from the bible | The locked starting point every motion take that follows has to match | image | Essential | Required — not started |
| Two motion takes from that anchor, differing by one directed performance beat (timing, look, gesture) | Directing motion is the same discipline as week 1, now with a moving frame | video | Essential | Required — not started |
| A note naming which direction changed between the two takes, in performance language | Proves the difference was directed, not accidental | text | Essential | Required — not started |

### Week 8 — Directing the AI performer

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| At least three takes of one performance beat | Generation-as-rehearsal only means something if failure is expected and visible | video | Essential | Required — not started |
| One-line diagnosis per rejected take (note vs. reference vs. model) | The diagnosis decides what actually gets changed next — the core skill of the week | text | Essential | Required — not started |
| Selected take + justification against the beat's original intent | Take selection judged against intent, not against "which one looked best" | video + text | Essential | Required — not started |

### Week 9 — Continuity and production

Implementation decision authorized by the owner on 2026-09-13: use the actual five-shot, 31.23-second Week 9 assembly and its continuity log as the lecture/deck demonstration, replacing the earlier authored hypothetical findings. Keep learning outcomes, session spec and timings unchanged. Retain source provenance and disclose review limits; this teaching integration does not establish the separate owner assessment evidence.

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Assembled sequence, ≥3 shots, 30–60 seconds | First assembled footage — the raw material week 10's recut and week 11's sound pass both build on | video | Essential | Required — not started |
| Continuity log: at least one problem found + fix-or-accept decision + reason | The repair discipline the week teaches: fix what's actually broken, not everything near it | text | Essential | Required — not started |

### Week 10 — Editing and dramatic rhythm

Owner-authorized example integration (2026-09-13): use the actual Week 9 assembly as Cut A and the real second edit as Cut B. Only shot 03 reaction duration changes, from 6.067 to 2.067 seconds. Embed both versions in Week 10, show the timing comparison and one intended emotional sentence per cut, and replace hypothetical wide/phone-cut claims. Outcomes, workshop spec and timings stay unchanged; audience response and audio listening remain unverified.

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Two distinct recuts of the week 9 footage, differing in a deliberate pacing decision | Same shots, cut two ways, proves editing is a directorial decision, not a mechanical step | video (×2) | Essential | Required — not started |
| One sentence per cut on the emotional difference it produces | Names the effect on purpose, rather than just noticing it happened | text | Essential | Required — not started |

### Week 11 — Directing with sound

Owner-authorized integration (2026-09-13): use the actual independently synthesized Samantha “Hey” pair (150/105 wpm), dialogue-only/full-pass comparison and no-music control on unchanged Week 10 Cut A picture. Primary pair uses A, approved for application by the owner. Show voice provenance, event-alignment times and a beat-by-beat intended comparison; preserve Meisner caveat, outcomes, workshop spec and timings. Correct the prior-missed-call antecedent to the established interrupted packing task. Exact phoneme fit and independent audience response remain unverified; this approval does not select the final film cut or complete OWN-W11.

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Two takes of one line reading, from a single note (pace, breath, hesitation) + which was selected and why | Directing a voice is the same discipline as directing a face — proves it transfers | audio + text | Essential | Produced and integrated 2026-09-13; independent listening review pending |
| Dialogue-only cut vs. full sound-pass cut (ambience bed + ≥1 Foley/SFX moment + one placed music cue) | Makes the sound pass's effect audible by direct comparison, beat by beat | audio + video (both versions) | Essential | Produced and integrated 2026-09-13; independent listening review pending |
| Note on what the sound pass changed emotionally, beat by beat | Feeds directly into the final director's statement | text | Essential | Intended beat comparison integrated 2026-09-13; audience effects unmeasured |

### Week 12 — Screening, critique, and revision / **Final Project**

Owner-approved format (2026-09-13): lecture teaches and models quality checking, specific critique, decision defence and choice-versus-limitation through Before It Stops excerpts; it is not the full round of student screenings. Lecture timing is recap/outcomes 10, technique/worked defence 45, comparison 15, judgement practice 15, workshop briefing 5 = 90 minutes. Workshop runs parallel groups of 4–5: cold screenings, three defended decisions per director, one revision note. Five Activities keep 10/40/40/20/10 = 120 minutes; specs and Final Project assessment stay unchanged. Correct old prior-call and unverified music-repair examples while modelling the method.

The near-final cut and critique note are this week's session deliverable;
the finished film, statement and reflection are the **Final Project**
submission, due 11 days later (the revision period) — these surface on both
the week 12 **Lecture** page and the Final Project assessment page.

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Near-final cut, under 4 minutes, self-explanatory unattended | What actually gets screened and critiqued in week 12's session | video | Essential | Required — not started |
| Three directorial decisions, named and defensible against a specific alternative | The critique skill from week 9, turned on your own work | text | Essential | Required — not started |
| One specific critique note to act on during the revision period | What the 11-day gap between screening and deadline is actually for | text | Essential | Required — not started |
| **Final film**, 2–4 minutes, matching the locked Assignment 1 world (deliberate departures allowed if documented) | The culminating submission — everything from week 7 onward converges here | video (final sound mix included) | Essential | Required — not started |
| Director's statement: three decisions + one failure and its repair | Judged as a directed film, not a demo reel — this is where that judgement gets made legible | text | Essential | Required — not started |
| Reflection on authorship and tool limitations, naming one change made because of the week 12 critique | Answers the question the whole course has been building toward | text | Essential | Required — not started |
