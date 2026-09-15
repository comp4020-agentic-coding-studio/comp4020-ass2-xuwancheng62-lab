# Plan

Living design document for this course site. While the project is still in
the planning stage, this file states the currently approved plan directly —
settled decisions are written into the main body as plain fact, and a
superseded proposal is rewritten or removed rather than kept alongside the
decision that replaced it. If you're reading this mid-build, the "Open
questions" section is the honest state of what's still unresolved.

## Plan governance

This rule takes effect once implementation of the site itself begins (it
does not apply retroactively to the curriculum content already written,
which this plan treats as settled):

- Work that follows this plan needs no revision entry — just build it.
- Any proposed departure from, or change to, the approved plan must be
  presented to the project owner and explicitly approved *before* it's
  applied.
- Once approved, the relevant section of this plan is updated in place to
  describe the new approved state. One record of the approval/change is
  enough — the section update itself, or a dated "Revision history" entry
  naming the exact change — not both as a matter of routine.
- The plan is never silently rewritten to match an implementation that
  diverged from it — a divergence is either rejected, or approved and then
  recorded as above.
- "Revision history" may be periodically archived to `PLAN-ARCHIVE.md` —
  see "Documentation reorganisation — approved" below — provided the
  original record is preserved there in full, current decisions stay
  accessible in this file, and a pointer says where the history moved.

This mirrors `CLAUDE.md`'s "Planning and human–agent decision making": that
file states the standing rule, this section states this project's
application of it.

## Documentation reorganisation — approved

Approved by the project owner on 2026-09-13: split this plan into a live
document (this file, `PLAN.md`) and a new `PLAN-ARCHIVE.md`, so current
decisions stay easy to find without reading through the history of how
each one was reached. This is a documentation-organisation change only —
it does not alter any website content, learning outcome, assessment
requirement, approved design decision, spec bullet, weighting, due date,
or production asset, and it does not change what `handoffs/*.md` are or
how they're used (see `CLAUDE.md` → "Weekly handoff records", unchanged).

Rules followed for the split:

- Standing rules, current architecture/design decisions, templates,
  completion criteria, and active or unresolved work stay in this file.
- Completed implementation narratives, superseded proposals, and
  historical corrections move to `PLAN-ARCHIVE.md`, in full, under their
  original headings.
- A section moves only once its decisions are confirmed no longer in
  force by the actual current content and, where one exists, the
  relevant week's handoff — a section simply not mentioned in a handoff
  is not by itself treated as evidence it's obsolete.
- Every moved section leaves its original heading in place here, with a
  concise current-state conclusion and a link into `PLAN-ARCHIVE.md` —
  no historical prose is duplicated in both files.
- "Revision history"'s existing ledger (2026-09-04 through 2026-09-13)
  moves to `PLAN-ARCHIVE.md` in full; this file keeps a short pointer and
  starts a fresh, ongoing ledger below it.

Two sections were checked against this test and left in place, unarchived,
because their decisions are still in force or their status is not yet
closed:

- "Week 1 status" (inside "Grounding in real directing pedagogy") —
  `BIS-W01-WORKSHOP` remains `NOT STARTED` in `MANIFEST.md`, so the
  workshop's design is still load-bearing, not merely historical.
- "Weeks 7–8 — second-frame Sora 2 demonstration" — real production and
  verification are still in progress per `handoffs/week-07.md` and
  `handoffs/week-08.md` ("verification gaps remain" / "generation paused
  by owner").

## Thesis

**"Directing for the Screen"** (SLOP4555, level 4): a directing practicum
where AI stands in for cast and crew. The discipline being taught is
directing — shot construction, performance direction, editorial judgement,
sound design intent. AI generation is the rehearsal medium that makes those
skills practiceable weekly without a real cast, crew, or budget.

This distinction is load-bearing, not cosmetic: the title and every lecture
description foreground directing verbs (direct, block, cast, cut, mix), not
tool names. The failure mode being actively avoided is reading as "COMP4020
with a film theme" — a generic AI-tools course wearing directing vocabulary
as a skin. Every content decision below is checked against that bar.

## Structure

Two assessments only, to keep the thesis legible:

- **Assignment 1** (week 6, weight 40) — pre-production package: logline,
  screenplay, world bible, shot list, storyboard.
- **Final project** (week 12, weight 60) — finished 2–4 minute film plus
  director's statement.

Twelve weeks, one progression: DIRECT → WRITE → VISUALISE → PLAN → GENERATE →
PERFORM → EDIT → SOUND → SCREEN. Each week's lecture teaches one directing
skill; each week's session is the smallest exercise that practices it that
week, not a preview of a later week's skill.

**One running example threads every week** rather than a fresh clip each
time: *"Before It Stops"* — on the final night before her late mother's
apartment is cleared, a woman receives a call from the brother she hasn't
spoken to in years, and must decide whether to answer before the ringing
stops. Reasoning: the course should feel like one continuous production
building toward the final crit, not twelve disconnected topic weeks. A
single scene also keeps the storyboard, shot list, and character work from
week 4 onward legible as the *same* project a student can point to in their
director's statement.

**"Before It Stops" is this course's fixed teaching example — a lecture
device, not the owner's own separate film and not a required student
project.** It replaces the earlier placeholder, *"Table for One"* (a
daughter's one last meal with the estranged father whose diner is closing
that night), by owner-approved global substitution on 2026-09-11 — see
"Revision history". The substitution changed only the story's flavour
text: every learning outcome, weekly sequence, assessment requirement,
duration, and template this plan already settled stays exactly as
approved. "Before It Stops" exists inside the curriculum's teaching prose
(lecture/session text, used to illustrate what a logline, a bible entry, a
shot list *look like*) and, for several weeks, as genuinely produced
teaching demonstrations (see `MANIFEST.md`'s section 1, and "Week 1 status"
below) — a curriculum-illustration stand-in never counts as one of those
real demonstrations, no matter how finished it looks. Where a lecture
claims a demonstration exists, it must actually have been carried out and
produce real video/image/audio/production-process material — invented,
simulated, or merely plausible-looking stand-ins must never be presented as
real demonstrations. Real teaching-demonstration assets, once they exist,
attach directly to the Lecture page for the week they demonstrate — see
"Content and data architecture" below. (This no longer references a
separate owner-produced short film: that personal production was paused
and its tracking removed 2026-09-13 — see "Multimedia strategy" and
Revision history.)

## Process: how coherence is checked

A 12-week curriculum has failure modes a spec test can't catch: an
assessment demanding a skill never taught, a lecture claiming a skill no
session ever practices, a learning outcome nobody assesses. This is exactly
the kind of "does it hold together" judgement the brief names as
human-scored, so it gets the closest thing to automated backpressure
available: `.claude/agents/curriculum-reviewer.md`, a read-only, adversarial
subagent (Read/Grep/Glob only, no Bash — deliberately can't edit anything).
It's instructed to try to falsify coherence, not confirm it, and any change
it prompts must be presented to the project owner before being applied (see
`CLAUDE.md`).

An earlier pass against the full 12-week skeleton found four structural
gaps, all since fixed in the content itself: week 6's due-date wording
contradicted the assessment's actual due date (now names the mid-semester
break explicitly); storyboarding was required in week 6 (Assignment 1)
before ever being taught (week 4's session now includes a thumbnail-sketch
step); week 11's lecture claimed directing a voice performance that no
session practiced (week 11 now opens with a two-take line-reading direction
step before the mix); and weeks 8/10/11 were named in the final project's
marking criteria without the matching `related:` edges (added). The same
pass also found that week 12's screening sat eleven days before the actual
final deadline with no stated reason for the gap — week 12 is now
structured as Screening & Critique → Revision Period → Final Cut, the
screened cut is named a near-final cut, and the director's statement must
name one change made in response to that critique.

Two findings from that pass remain open judgement calls rather than fixes —
see "Judgement calls" below.

A follow-up pass (2026-09-04) raised two more subjective findings — week 9's
clip assembly appearing to precede week 10's editing lecture, and no lecture
teaching generative-tool mechanics. Both were dismissed outright, not added
as open judgement calls, once the teach/practise boundary in `CLAUDE.md` was
clarified to separate disciplinary knowledge from tool mechanics — see
"Judgement calls" below.

A full curriculum-reviewer pass will run again once all content is
complete: lectures, sessions, assessments, all 12 decks, and the real
operational demonstrations together, not just the text graph the earlier
pass checked. That pass stays report-only like every other run — any change
its findings prompt is presented for approval before being applied, per
`CLAUDE.md` and "Plan governance" above.

## Assumptions and ambiguities

- **"Single scene, threaded across 12 weeks" is a reading of the brief, not
  a stated requirement.** The brief asks for a course that teaches directing
  craft; nothing in it mandates either a single running example or multiple
  scenes. One scene was chosen for continuity (see "Structure").
  Assignment 1's brief language previously read as if it could imply more
  than one scene — resolved 2026-09-15 by reworking the two ambiguous
  phrases; see "Judgement calls".
- **"Does it hold together" is being answered by proxy.** The brief names
  curriculum coherence as human-judged; a pass from the `curriculum-reviewer`
  subagent plus the project owner's own sign-off is treated as satisfying
  that, since there's no other student or marker reviewing it before
  submission. That proxy is only as good as the subagent's rubric and the
  willingness to act on adversarial findings rather than wave them through.
- **The eleven-day gap between the week 12 screening and the final deadline
  is outside this repo's control, but what it means is not.** The calendar
  dates (05-17 and 05-28) can't move from here — only what the screening
  session claims and what the deadline asks for. Resolved by naming the gap
  the revision period; see "Process" above.
- **"Constructive alignment" is being checked at the whole-course level,
  not per-student-path.** The reviewer checks that skills are taught before
  assessed in the published sequence. It doesn't model a student who skips a
  session or falls behind — that's assumed out of scope for a coherence
  check of the curriculum itself.

## What's checkable vs. what needs judgement

**Machine-checkable (and where):**
- Build integrity, types, links, a11y — `pnpm typecheck`, `pnpm build`
  (which runs axe over every rendered page and fails on a dangling content
  ref or a base-path-broken link).
- Every assessment's marking criteria naming a week's content has a matching
  `related:` edge from that week — structural, gets caught by a `grep`/graph
  check, and is exactly what the reviewer pass caught for weeks 8/10/11.
- Whether a skill a session requires (e.g. "you have a storyboard thumbnail")
  was ever taught by an earlier week's lecture is the same kind of
  structural check, walking the sequence in order.
- `PROCESS.md` citations resolving to real commits, `CLAUDE.md`/reflection
  presence — `pnpm check:evidence`.

**Needs human judgement (no test will ever catch these):**
- ~~Whether the single-scene running example is actually adequate practice
  for Assignment 1's brief, or narrower than what it asks for.~~ Resolved
  2026-09-15: kept single-scene as the practice model; the brief's wording
  was the actual problem, not the practice model itself — see "Judgement
  calls" above.
- ~~Whether montage — lectured week 10 — needing no rehearsal week is a
  legitimate scope cut... or an actual gap.~~ Resolved 2026-09-15: closed as
  a gap — see "Judgement calls" above.
- Whether naming the eleven-day gap "the revision period" and requiring one
  critique-driven change in the statement actually produces better final
  cuts, or just produces a statement that dutifully names *a* change to
  satisfy the spec line.
- Whether the thesis ("directing is the discipline, AI is the medium") is
  actually legible to a student skimming the site, not just true when
  argued out loud.
- Whether the curriculum "holds together" as a lived 12-week experience, as
  opposed to holding together against the reviewer's specific rubric — the
  rubric is a proxy, not the actual standard.

## Judgement calls

Two subjective findings from the coherence review were closed on
2026-09-15 — the reasoning for each is recorded here rather than left as a
bare "open" flag:

- **Single-scene practice vs. Assignment 1's multi-scene brief language —
  resolved 2026-09-15.** Kept single-scene as the practice model.
  Reasoning: the continuity payoff (one project a student can point to
  across sessions and in the final director's statement) outweighs
  matching the brief's phrasing literally, nothing in the assessment's
  actual marking criteria requires more than one scene, and nothing taught
  in weeks 2–6 ever rehearses linking multiple scenes together — requiring
  it would create a new teach→practise→assess gap, not close one. What
  was genuinely wrong was two phrases in `assignment-1.md` that read as if
  they assumed multiple scenes ("scene headings," "Include every scene")
  when nothing substantive required it: reworded so each is compatible
  with a single continuous scene while still requiring the screenplay to
  actually span beginning to end (unchanged: the runtime-shortfall
  callout, the Week-3-practice-scene completeness check, and the
  "Screenplay completeness" rubric row, which were already correctly
  worded around length/completeness, not scene count). See
  `handoffs/week-06.md` for the full change and verification.
- **Montage lectured week 10, never rehearsed in a session — resolved
  2026-09-15.** Previously left unrehearsed on the reasoning that week 10's
  session already exercised the pacing judgement montage depends on, just
  not the montage move itself. Miles asked to close this rather than leave
  it a judgement call: `10-recut-lab.md`'s second required cut now must be
  a repeat/reorder (montage) decision instead of a second duration variant,
  and `week-10.md` gained one bridging sentence naming that requirement. See
  `handoffs/week-10.md` for the full change and verification.

A follow-up pass (2026-09-04) raised two more findings and dismissed both
once `CLAUDE.md`'s teach/practise boundary was clarified to distinguish
disciplinary knowledge from tool mechanics. Full text moved to
[PLAN-ARCHIVE.md → "Judgement calls — dismissed findings (2026-09-04
follow-up pass)"](PLAN-ARCHIVE.md#judgement-calls--dismissed-findings-2026-09-04-follow-up-pass).

## Open questions / not yet done

- Whether to revisit either of the two open judgement calls above before
  shipping.
- The full curriculum-reviewer pass described under "Process" above is
  pending until the real operational demonstrations exist (lectures,
  sessions, assessments and all 12 decks are now written and committed);
  running it earlier would only re-check the same text-plus-decks graph a
  pass could already walk today, before the real assets that pass is
  actually meant to catch problems against exist.

## Site architecture and information architecture

What exists today: Home (`/`), Lectures (index + `[slug]`), Workshops (index +
`[slug]`), Assessments (index + `[slug]`), People (index only), Policies (one
flat `.mdx` page), plus `/decks/week-01/` outside the content graph entirely
(decks carry no `related:` edge — README is explicit about this — so they're
linked by hand from a lecture page). Nav (`src/site-config.ts`) lists exactly
these five sections. That's the whole IA; nothing structural needs inventing,
which is a smaller job than it first looks.

"Workshops" is the student-facing label (`sessionLabels` in
`src/site-config.ts`) for the weekly teaching meeting; the underlying content
collection, route (`/sessions/`), and component names stay `sessions` —
only the display text changed, matching what students actually call these
meetings.

The curriculum's actual shape — one running example, nine directing verbs,
twelve weeks — is currently only visible by reading lecture pages in order.
A skimming visitor sees five disconnected listings, not a progression. Home
closes that gap: its body (currently starter placeholder anyway, so no extra
IA cost) carries a concise statement of the thesis, linking through to the
Lectures index/pages. There is no dedicated case-study page and no new nav
entry — the real per-week production material lives on the Lecture pages
themselves (see "Content and data architecture" and the week-by-week
checklist below), so Home's job is orientation, not a walk-through of the
running example.

**Should have: a real production-progression visualisation on Home, not
just prose.** A TEXT → SCRIPT → STORYBOARD → IMAGE → MOTION → EDIT → SOUND →
FILM sequence — the same production arc already named under "Multimedia
strategy" below, condensed here to fit a single visual — communicates the
course's central learning progression directly, and is not ruled out as
mere decoration. This is a should-have, not a must-have: Home still works
as a text-plus-links page if it's never built, but skipping it trades away
the clearest single opportunity to make the thesis legible at a glance,
which is explicitly named above as the human-judged bar the site has to
pass. See "Component strategy" below for what building it would need.

## Visual direction

**Fixed, not mine to touch — verified against `README.md` and
`astro.config.ts`, not assumed:** the gold/bronze/warm-grey palette shipped
by `astro-theme-slop` (`brandCss: "astro-theme-slop/slop.css"` in
`astro.config.ts`) and wired into `site-config.ts`. `README.md` names this
explicitly as part of "the platform," which "stays as it arrived" — and
draws the line there: "everything else is yours ... the visual treatment
and every word of content." The palette is a genuine hard constraint, not a
starter default that happens to still be in place.

**Approved 2026-09-04: a hybrid direction — "Director's Notebook" as the
primary metaphor, with selected production-language elements borrowed from
a "Slate & Grain" alternative that was considered and rejected as the
primary direction.** Reached after three options were drafted and reviewed;
the full text of the rejected options isn't kept here since this is the
decided state, not a live proposal.

- **Core metaphor**: a modern director's working notebook — an actual,
  current tool a director works in, not a nostalgic film prop or an
  editing-suite pastiche. The failure mode this rules out is the same one
  named under "Thesis" above: reading as a film-themed skin rather than a
  directing course.
- **Typography**: a plain, warm, modern serif or humanist sans carries all
  primary course content (lecture/session prose, bibles, screenplay text).
  A distinct, quieter secondary style — not monospace, not typewriter — is
  reserved *only* for Director's Notes and selection-rationale callouts, so
  a note always reads in a visibly different register from the content it's
  commenting on. Monospace is used sparingly, only for the small production
  labels below, never as the dominant voice anywhere on the page.
- **Spacing/layout — the annotation system**: an asymmetric layout on wide
  viewports reserves a margin column for Director's Notes / rationale,
  sitting beside the primary content it annotates and collapsing to an
  inline callout below a breakpoint. This is the one structural device the
  whole visual system is built around, not a decorative flourish.
- **Production labels**: small, restrained tags (WEEK, SCENE, SHOT, TAKE,
  SELECTED, REJECTED, and similar), used only where they carry real
  semantic meaning — e.g. marking which take was selected and why — never
  as decorative dressing and never as the primary typographic voice.
- **Imagery — decorative site/deck artwork, revised 2026-09-04**: abandons
  the earlier literal filmmaking-illustration approach (director's chairs,
  cameras, clapperboards, film reels, projectors, studio scenes,
  stock-vector people, fake production artefacts) entirely — see Revision
  history. In its place, a coherent abstract graphic system: warm cream
  background; black and warm gold as dominant colours, muted dark green as
  a strong secondary accent (extending, not replacing, the fixed
  gold/bronze/warm-grey palette above); bold flat 2D geometric forms —
  circles, rectangles, lines, frames, crops — in strongly asymmetrical
  compositions with large areas of negative space, using repetition,
  overlap and controlled misalignment. No gradients, no 3D rendering, no
  photorealism, no glossy effects, no excessive texture, no text inside the
  artwork. Individual pieces don't need to tell a story or depict what a
  page is about; they read as a family of abstract posters for the same
  cultural institution, related by shared palette, proportion and
  compositional grammar rather than by subject matter. Simple enough to sit
  comfortably beside the theme's typography; compositions stay attractive
  when cropped responsively. Images still presented as flat, inset
  artefacts with no drop shadow, no rotation, no fake-paper or grain
  texture, no corkboard/pinned treatment. Approved as a pilot-first rollout:
  one Home hero generated and reviewed before the rest of the family
  (portraits, social card, further decorative pieces) is attempted.
- **Decorative artwork vs. teaching visuals, kept strictly separate,
  added 2026-09-04**: the abstract graphic system above governs only
  decorative site/deck artwork (hero, social card, portraits, deck
  backgrounds) — its job is visual identity, atmosphere, rhythm and
  consistency, and it never needs to illustrate what a given page is
  actually about. Teaching visuals — diagrams, comparisons, frames,
  storyboards, anchor stills, and the real production assets in the
  week-by-week checklist below — are the opposite: pedagogically accurate
  and content-specific, made only where a concept genuinely needs visual
  explanation or where "Real production material, never invented"
  (CLAUDE.md) requires a real artefact, and displayed as themselves rather
  than restyled into the poster system.
- **Motion**: native CSS only (`astromotion` is ruled out for this — see
  below), restrained and functional: a fade/opacity change when a
  Director's Note appears, a treatment that visibly distinguishes a
  SELECTED take from a REJECTED one, a subtle hover state. Every animation
  communicates progression, comparison, selection, or directorial
  judgement — never atmosphere for its own sake. The theme's existing
  `prefers-reduced-motion` handling (`astro-theme-university/styles/base.css`)
  stays intact and unfought.
- **Explicitly avoided**: literal corkboards, fake paper, heavy grain,
  rotated photographs, film-reel/filmstrip decoration; monospace as the
  dominant voice; a global timeline-as-site-structure metaphor (editing is
  one stage of the course, not the frame for all of it).
- **Progressive richness across weeks is a content property, not a
  redesign.** Early weeks read as primarily text + annotation; middle weeks
  add framed imagery and production labels; later weeks add take
  comparisons and motion. This is what "Progressive integration" in
  "Implementation phases" below produces automatically as real assets
  attach — the visual system itself doesn't change week to week.
- **Home is the deliberate exception, allowed more visual ambition.** Its
  TEXT → SCRIPT → STORYBOARD → IMAGE → MOTION → EDIT → SOUND → FILM
  progression (see "Site architecture" above) is the site's one cinematic
  visual statement, still inside the same palette, typography, and motion
  restraint as every other page — not a different design language.
- **Hero imagery extended to the other four index pages, approved
  2026-09-04**: after the Home hero pilot (above) was approved, each of the
  other top-level index pages — Lectures, Workshops (`sessions`),
  Assessments, People, Policies — gets its own single decorative hero image
  from the same abstract graphic system, wired through the `heroImage` /
  `heroImageAlt` props `ContentLayout` already supports (`404.md` already
  used this mechanism). Each is a distinct composition sharing the family's
  palette/grammar, not a copy of the Home hero and not an illustration of
  that section's content — Home's production-progression visual remains the
  one place the site is more visually ambitious than this. Portraits
  (Marisol Quaye, Idris Fenn) and the social card (`card.png`) are
  regenerated under the same abstract system rather than kept as
  stylised-illustration figures, per "Imagery" above.

**`astromotion`'s capability outside deck rendering, resolved 2026-09-04:**
confirmed from source (`node_modules/astromotion/README.md` and its
integration in `astro.config.ts`) that it is exclusively a Reveal.js
slide-deck integration — its only site effect is injecting the
`/decks/[...slug]` route, and its components target a fixed 1280×720 slide
canvas, fundamentally incompatible with a responsive page layout. It has
nothing to offer an ordinary Astro page. Site-wide motion is native CSS
only, per "Motion" above.

## Multimedia strategy

**This is a real production for its actual teaching demonstrations, not a
static demo site — but not a vehicle for a separate personal film.** The
owner previously intended to also produce their own separate short film
alongside the course, mirroring the course's own progression; **that
personal production is paused as of 2026-09-13, not cancelled** — the
owner may resume it later, just not now, and it is no longer part of this
course's required tracking (see "Owner's personal-production checklist
removed" in "Revision history"). What the site still has to display
honestly, without invention, is the course's own "Before It Stops" teaching
demonstrations — real images, video takes, voice reads, ambience, Foley and
music actually produced by Codex or the owner (via Jimeng) to illustrate a
lecture's concepts, tracked row-by-row in `MANIFEST.md`'s section 1. The
job on the website side is **not** to generate a plausible-looking set of
finished assets or fake those demonstrations — it is to build the system
that displays the real outputs at each stage, cleanly, and gets visibly
richer as richer teaching material arrives.

**Two responsibilities, kept separate:**
- **The site owner's:** follow the course, produce the real teaching-
  demonstration asset a lecture actually claims exists (tracked row-by-row
  in `MANIFEST.md`, not a personal-project checklist), and hand it over.
- **The site's:** design and implement one coherent system — visual
  language, layout, component set — that teaches the course *and* displays
  those assets as they progressively arrive, textual through finished
  demonstration, without a redesign at every media-type transition.

**The progression the display system has to support**, matching the
course's own arc: **TEXT → SCRIPT → VISUAL DEVELOPMENT → STORYBOARD → IMAGE →
MOTION → EDIT → SOUND → FINAL FILM.** Concretely: every `MANIFEST.md`
teaching-demonstration row needs a display treatment for whichever of
text / image / audio / video it turns out to be, sharing one visual system
(typography, spacing, the site's own decorative graphic system for chrome —
see "Visual direction" above). Real production assets are displayed as
themselves within that system, not restyled into it — per "Decorative
artwork vs. teaching visuals" in "Visual direction" — so a text-only week-2
entry and a video-plus-audio week-11 entry read as the same course, not two
different sites bolted together.

**What this repo can and can't generate itself, separated from what the
owner supplies:** `scripts/generate-image.ts` generates stills only, and is
not the source of the teaching demonstrations' real images, video or audio
— those come from whatever workflow a given `MANIFEST.md` row's Producer
column names (Codex's Sora, or the owner using Jimeng), outside this repo,
and arrive here as files to embed. The only thing this repo's image
generator is for is the site's own presentation assets (hero, social card,
portraits, decorative deck backgrounds). Image budget is confirmed
sufficient for that limited use; this is not tracked as an open risk.

**Still open, needs checking before the display-system build (see
"Implementation phases" below):** the theme ships a `YouTubeEmbed`
component, sized for a hosted video URL — need to confirm whether
teaching-demonstration video takes will be hosted somewhere embeddable or
delivered as files the site serves directly (different component,
different build-size implications). Not deciding this now; flagging it as
the first thing to resolve once real footage exists.

## "Before It Stops" asset plan

**Teaching-example demonstrations for "Before It Stops" are tracked in
`MANIFEST.md`, not in this file.** That manifest is the single source of
truth for every asset's producer, status, dependencies, and acceptance
criteria, following the Claude Code / Codex / owner division of
responsibility below. This section states the policy that manifest has to
honour; it doesn't duplicate the manifest's rows.

**Division of responsibility:**
- **Claude Code** audits assets, maintains `MANIFEST.md`, generates the
  site's own decorative/presentation images, integrates approved assets
  into the website, and runs consistency checks. It never generates Sora
  video and never invents a production artefact.
- **Codex** generates Sora teaching videos from complete briefs (every
  brief states teaching purpose, exact scene/action, camera behaviour,
  duration, aspect ratio, continuity requirements, fixed objective,
  intended interpretation, and the observable difference students should
  notice), performs technical QA, and returns files plus metadata. Codex
  never alters the curriculum or integrates files into the website.
- **The owner** produces the genuine teaching-demonstration evidence a
  lecture actually claims exists (tracked in `MANIFEST.md`'s section 1,
  alongside Codex) and integrates it via Claude Code. The owner's own
  separate short-film production is paused as of 2026-09-13 (see
  "Multimedia strategy"); teaching examples are never presented as if they
  were that separate production, and the reverse never happens either.

**Generation discipline, unchanged from the placeholder era:** at most one
initial Sora generation and one diagnosed redirect per asset by default:
Note A → Take A → diagnosis → Note B → Take B, never a batch of
speculative takes. A real demonstration is produced only where a lecture
actually claims one exists (currently: week 1 only — see "Week 1 status"
below); a week's teaching prose describing "Before It Stops" conceptually
does not, by itself, obligate a produced asset, exactly as it didn't for
"Table for One." The site's information architecture makes adding one a
content change, not a structural one: real assets attach directly to the
Lecture page they demonstrate, per "Content and data architecture" below.

## Session content depth pass

Lectures and sessions currently exist as a skeleton: a lecture's "Outline"
is bullet points naming a topic, not prose teaching it, and a session's
`spec:` states what to produce without always saying how it's checked or
what social format the workshop activity runs in (solo work, paired
exchange, group discussion, brainstorm). This section is the approved
approach for fleshing that out — applied one week at a time, each week's
implementation approved before it happens, starting with week 1.

- **Lectures**: turn "Outline" bullets into taught prose covering the same
  points at real depth — the technique being taught doesn't change; where
  a week's outcomes were only ever implicit, stating them explicitly and
  measurably (as in week 1) is a clarification of what was already being
  taught, not a new skill added to the week.
- **Sessions**: give the workshop a named, timed activity format, and
  where it fits, a completion criterion checkable by **peer verification**
  — a classmate who wasn't given the director's note or intent judges the
  result independently. This isn't a new pattern: week 5's session already
  requires *"a classmate who has never seen your project can describe your
  protagonist back to you correctly after reading only your bible entry."*
  Extending that same shape to earlier weeks where it fits is consistent,
  not invented.
- **Decks**: touched only to stay in sync with a session's activity
  structure when that structure changes — decks remain their own
  distillation, not a copy of the lecture/session prose (see "Content and
  data architecture").

### Week 1–2 teaching corrections

Implemented and verified: the Week 2 logline draft-to-revision teaching, a
filmability walkthrough with explicit planning-estimate timings, progressive
disclosure of the Week 1 demonstration, and removal of a developer-facing
`RESEARCH.md` reference from student-facing text. Full text moved to
[PLAN-ARCHIVE.md → "Week 1–2 teaching
corrections"](PLAN-ARCHIVE.md#week-12-teaching-corrections).

### Grounding in real directing pedagogy

`RESEARCH.md` compiles sourced findings from seven academic directing
programs (AFI, NYU Tisch, USC, UCLA, Columbia, London Film School, NFTS)
and five named methodologies/masterclasses (Judith Weston, David Mamet,
Sanford Meisner, MasterClass instructors, Sydney Pollack) — every claim
sourced or explicitly flagged unverified. The templates and per-week
mapping below are built from it, fitting the course's real constraint of a
1.5-hour lecture and a 2-hour workshop each week.

**Lecture and workshop are strictly separate, course-wide.** No lecture
states a workshop's task, timing, format, or completion criteria — that
belongs entirely to the workshop's own opening. Every workshop in turn
opens with its own 5–10 minute recap of the lecture's technique before
stating its task.

**Lecture template (90 min), same shape every week:**
1. Hook (5–10 min) — re-anchor to "Before It Stops" and the
   direct→generate→evaluate→redirect loop.
2. Learning outcomes (5 min) — state the week's outcomes explicitly before
   teaching starts.
3. Core technique, taught not named (35–50 min) — the week's core skill
   worked through a concrete "Before It Stops" example, using real
   vocabulary where it fits rather than inventing course-only jargon;
   includes a real demonstration walkthrough wherever that week's asset
   exists, placeholder-labeled and never fabricated where it doesn't (see
   "Real production material, never invented" in `CLAUDE.md`).
4. Misconception contrast (15 min) — a wrong-way/right-way comparison
   (week 1's wish-vs-note table is the pattern).
5. Guided student judgement (10–15 min) — low-stakes, in-lecture judgement
   practice with no generation involved.
6. Synthesis (5 min) — recap the outcomes and the technique.

**Workshop template (120 min)**, borrowing the cross-program pattern in
`RESEARCH.md` (a regular screen-and-critique ritual; two distinct modes —
rehearsal-based when directing a performer, construction-based when
building/cutting shots, per Columbia's documented split of "Directing
Actors" vs. "standard directing exercises"):
1. Recap and task briefing (5–10 min) — the workshop's own recap of the
   lecture's technique; states the task, any locked material, format,
   timing, and completion criteria in full.
2. Main exercise (70–80 min) — the generate→direct→evaluate→redirect loop
   applied to that week's task, in rehearsal mode (weeks 1, 3, 7, 8, 11) or
   construction mode (weeks 4, 6, 9, 10). Where the exercise turns on a
   locked objective or intended interpretation, that stays fixed across
   iterations — only the note or construction decision changes between
   attempts, so a redirect is a diagnosed adjustment, not a second
   unrelated attempt.
3. Dailies review (20–25 min) — screen work in pairs/small groups before
   anything's finalized, modeled on AFI's dailies review, NYU's weekly
   Master Class, and NFTS's rushes-cinema culture: what was the note → does
   the room read it unprompted, in their own words, including what it does
   to their reading of the character's intention → what would you redirect
   next.
4. Completion check (10 min) — walk the week's `spec:` bullets as a
   checklist, peer-verified wherever the criterion is a peer-legibility
   test (weeks 1 and 5's existing pattern).

**How these four phases get written on the page is a standing rule in
`CLAUDE.md`, not here:** see "Workshop structure: explicit numbered
activities" — every workshop writes its phases as titled, timed
`Activity N` blocks with an Instructions and an Expected output part,
summing to the workshop's total. The four phases above are *what* each
activity (or group of activities) must cover; `CLAUDE.md` governs the
page structure they're written in.

**Per-week technique mapping** (outline level — full prose is written and
approved one week at a time, per "Plan governance"):

| Wk | Gap in current content | Technique to teach (sourced in `RESEARCH.md`) | Workshop mode + completion angle |
|---|---|---|---|
| 1 | Done — see "Week 1 status" below | objective→playable-action→interpretation chain, on a locked scene/objective | rehearsal; genuine redirect (objective fixed, only the note changes) + interpretation-based blind review |
| 2 | Logline stated, not tested | Mamet's objective/tactic framing: logline must name an objective *and* what's in its way, testably | rehearsal-adjacent; partner states the obstacle back from the logline alone |
| 3 | Intent note named, not taught | Weston's "moment before" — the note names the antecedent circumstance, not an adjective | rehearsal, worksheet-scaffolded (premise → decisive scene → scene change → five observable beats → screenplay form → director's note); partner reads only the isolated line/action and its note, describes the performance choice(s) it could motivate, then compares against the revealed scene |
| 4 | Shot list as vocabulary list | Mamet's shot-as-argument — build the list by asking what meaning each cut produces, not coverage | construction; partner reads only the shot list and describes the intended meaning |
| 5 | Bible fields named but not modelled | Concrete character/location entries, fixed facts versus shot state, diagnosed revision | six timed activities; blind read-back and evidence-based revision; see approved Week 5 depth pass |
| 6 | Shot list "expanded," no critique ritual | AFI's Comprehensive Review — present the package aloud, defend one cut decision | construction; partner asks 2 questions, director defends |
| 7 | Anchor→motion, no antecedent framing | Weston's moment-before applied to prompting: describe the state before the beat, not the beat itself | rehearsal; dailies-review screens both takes before selection |
| 8 | Diagnosis named, not gated by objective | Mamet's objective framing as the diagnostic rubric: does the take fail the character's want, not "look wrong" | rehearsal; group dailies-review of 3 takes before selection |
| 9 | Assembly + continuity log | AFI dailies-review ritual formalized as the workshop's structure | construction; group screens the cut, continuity log filled from the group's actual confusion points |
| 10 | Recut, no meaning-of-cut framing | Mamet's shot-as-argument extended to pacing: what does *this* cut point argue that the other doesn't | construction; partner watches both cuts blind and guesses which was "hold" vs. "cut early" |
| 11 | Line reading + sound pass, two skills blurred | Weston/Meisner-adjacent responsiveness framing for the line reading; separate construction pass for the mix | rehearsal (reading) then construction (mix), now named as two explicit phases |
| 12 | Screening already matches the ritual | Validate against the AFI/NYU/NFTS pattern explicitly; tighten to a defend-3-decisions interview format (AFI's Comprehensive Review) | already the ritual — mainly formalizing the interview/defense structure |

This mapping is editorial synthesis informed by the research, not a
literal requirement quoted from any single source — treat the "technique
to teach" column as this course's adaptation, not a claim that (e.g.) AFI
teaches "Before It Stops" directly.

**Week 1 status: `content complete; existing Take A retained for diagnosis`.**
The lecture and deck retain their real Note A → Take A → diagnosis →
Note B → Take B demonstration (`BIS-W01-DEMO`). The workshop uses a
separate, explicitly counterfactual voicemail-callback beat: what if Nadia
had not answered her brother's call? This does not change the canonical
Week 2–3 ending, where she answers on the final ring.

**Approved workshop redesign, 2026-09-13:** retain the existing served
Take A unchanged and use it as an imperfect clip for observation and
diagnosis. Students watch cold, compare their reading with the revealed
objective and intended interpretation, identify one observable problem,
write a playable redirect, and have a partner check whether the note
addresses that problem while preserving the locked scene and objective.
They revise the note and describe the change they would look for in a
future take. No student generation, prepared Take B candidates, A/B video
comparison, or verification of a generated redirect is required.

The workshop does not require the old predetermined two-second-pause
diagnosis. Students may identify timing, gaze, gesture, breath, degree,
or unwanted speaking in the actual clip, and distinguish performance
issues from generation artefacts. Existing Take A's prior production QA
failures remain recorded; retaining it for this exercise does not grant
production approval. Its incomplete generation provenance remains a
historical limitation, not a requirement to generate replacement material.
`BIS-W01-WORKSHOP` in `MANIFEST.md` tracks the retained clip and current
integration. The instructor-only brief is at
`resources/week-01/workshop-brief.md`.

The workshop remains tool-agnostic and totals 120 minutes. It practises
diagnosis and the specificity of a redirect; peer review checks the written
note, not whether a new performance actually improves. The lecture's real
A/B pair continues to demonstrate evaluation of a generated result.

Four completed sub-passes within this section — the Week 3 scene-planning
scaffold, the Week 4 shot-as-argument pass, a Week 4 revision (deck slides,
shot 5 staging, guided judgement), and the Week 4 teaching diagrams — are
implemented and verified. Full text moved to [PLAN-ARCHIVE.md → "Grounding
in real directing pedagogy — completed
sub-passes"](PLAN-ARCHIVE.md#grounding-in-real-directing-pedagogy--completed-sub-passes).

### Week 5 depth pass — approved

Approved 2026-09-12; implemented and verified per `handoffs/week-05.md`
(text/template scope complete — lecture, six-activity workshop, and
15-slide deck; visual production fields remain pending by owner
instruction, tracked live under "Week 1 status" above and in
`MANIFEST.md`). Full text moved to [PLAN-ARCHIVE.md → "Week 5 depth pass —
approved"](PLAN-ARCHIVE.md#week-5-depth-pass--approved).

### Weeks 6–12 depth pass — approved

Approved 2026-09-12; implemented and verified per `handoffs/week-06.md`
through `handoffs/week-12.md` (all seven weeks rewritten to the approved
lecture/session/deck shape; Week 7's stale ending text corrected). Full
text moved to [PLAN-ARCHIVE.md → "Weeks 6–12 depth pass —
approved"](PLAN-ARCHIVE.md#weeks-612-depth-pass--approved).

### Week 2 — good-story criterion addition — approved

Approved and implemented 2026-09-13: a named lecture criterion (emotional
hook over lengthy dialogue/internal monologue for short-form drama),
illustrated against the existing "Before It Stops" premise, plus a
matching workshop discussion point and one new deck slide. No `spec:`
bullet changed. Full text moved to [PLAN-ARCHIVE.md → "Week 2 —
good-story criterion addition —
approved"](PLAN-ARCHIVE.md#week-2--good-story-criterion-addition--approved).

### Week 6 — bible → keyframes → generated shots pass — approved

Approved and implemented 2026-09-13: a new lecture section names the
bible → keyframe → generated-shot chain (worked through shot 7's
start/end keyframes), extends the outcomes/misconception/dependency
tables, and corrects the stale "pending" claim about Nadia/kitchen/phone
references now that they've been generated (per `handoffs/week-06.md` →
"Adjacent-week impact": the kitchen's full production-approval is the one
dependency still genuinely open — see "Week 1 status" above and
`MANIFEST.md`). No `spec:` bullet or weighting change. Full text moved to
[PLAN-ARCHIVE.md → "Week 6 — bible → keyframes → generated shots pass —
approved"](PLAN-ARCHIVE.md#week-6--bible--keyframes--generated-shots-pass--approved).

### Assignment 1 — pending-decision alignment pass — approved

Approved and implemented 2026-09-13: `assignment-1.md`'s `spec:` bullets
6 and 10 and related prose now permit a bible decision to be "resolved, or
explicitly marked pending with the decision needed to close it," matching
Week 5's own taught pending model, instead of forbidding any pending
decision at submission (which had assessed voice design, a Week
11-taught skill, before Assignment 1 is due). No submission section,
marking weight, or due date changed. Full text moved to [PLAN-ARCHIVE.md →
"Assignment 1 — pending-decision alignment pass —
approved"](PLAN-ARCHIVE.md#assignment-1--pending-decision-alignment-pass--approved).

## Week-by-week asset checklist — paused 2026-09-13, moved to archive

This tracked the owner's own separate short-film production, required week
by week alongside the course — distinct from "Before It Stops" (the fixed
lecture teaching example, unaffected) and from any student's assessed
work. Owner paused that personal production on 2026-09-13: not cancelled,
possibly resumed later, just not now — see "Multimedia strategy" and
Revision history. Moved verbatim to [PLAN-ARCHIVE.md → "Week-by-week
asset checklist (owner's personal-production requirement — paused
2026-09-13)"](PLAN-ARCHIVE.md#week-by-week-asset-checklist-owners-personal-production-requirement-paused-2026-09-13),
the full per-week table preserved there as the record of exactly what it
asked for, in case the owner resumes it. `MANIFEST.md`'s `BIS-W*` teaching
demonstrations (tracked in its section 1) are untouched by this — they
never counted as satisfying this checklist and still don't.

## Content and data architecture

Four collections (`sessions`, `lectures`, `assessments`, `people`) plus a bare
`policies` page, wired by `related:` reference edges — the same graph
`curriculum-reviewer` already walks. Every collection schema ends in
`.loose()`, so extra frontmatter keys pass through without a schema change.

**No collection has an explicit learning-outcome field.** Outcomes currently
live only in prose — a lecture's "Outline" bullets, a session's `spec`
bullets. The reviewer currently infers "was this taught before it's assessed"
by reading prose, not by walking a typed edge. Not proposing a schema change
here — `.loose()` means a `tags:`/`outcomes:` array could be added
incrementally later without touching `content.config.ts` at all, and doing it
now would be solving a problem the reviewer hasn't actually hit yet.

**Real, progressively-arriving production assets attach directly to the
Lecture entry for the week they demonstrate.** There is no separate
`production` collection and no separate page for tracking them: the four
existing collections describe the *course itself* — generic, the same for
any student who takes it — and adding a structurally separate log for
these real assets would duplicate that structure for no benefit.
`lectures`' schema already ends in `.loose()`, so an asset-reference field
(or a small array of them) can be added to a lecture's frontmatter
incrementally, week by week, as real material arrives, without a
content-model migration. Per-asset detail (producer, status, dependencies,
acceptance criteria) is tracked in `MANIFEST.md`, not duplicated here. This
keeps "Before It Stops" swappable for the real project by construction: each
lecture names its own asset slot, not "the Before It Stops version of X,"
and there's no second collection to keep in sync with the first.

**All twelve lectures get a real deck.** Decks stay outside the content
graph exactly as today (no `related:` edge — README is explicit about
this). Each of the 12 decks distils that week's objectives, directing
concepts, visual/process examples, the demonstration context, the session's
task, and the expected output — a distillation written for the deck, not a
copy of the lecture's own prose. Every lecture's deck — week 1's included,
still the unedited starter deck — needs this real content written (see
"Implementation phases" and "Open questions" above).

## Component strategy

Already built and wired into the index pages: `AssessmentsGrid`,
`LecturesGrid`, `SessionsGrid`, `PeopleGrid`, `TeachingTeam`, `MarkingModel`
(`src/components/`), on top of the theme's `Card`/`CardGrid`/`ContentLayout`.
Listings are a solved problem — nothing new needed there.

What's missing:

- **One reusable media component family**, covering whatever a lecture's
  asset slot actually is: text, a single image, a single audio clip, a
  single video, and a **side-by-side version comparison** (two takes, two
  cuts, dialogue-only vs. full mix — several week rows in the checklist
  above are explicitly pairs), plus a **director's note** slot and a
  **selection rationale** slot attached to whichever asset it's commenting
  on. This family is what every Lecture page uses to show its real
  demonstration — there is no separate case-study page for it to live on
  instead.
- Exact component boundaries (one component with variants vs. a small
  family of siblings sharing a layout primitive) are implementation detail,
  not a planning decision under `CLAUDE.md`'s trigger test, since it doesn't
  change what any page or nav entry does — left open until the build phase
  that needs it (see "Implementation phases" below).

- **Should have: a production-progression visualisation component for
  Home** (see "Site architecture" above) — a sequence through TEXT → SCRIPT
  → STORYBOARD → IMAGE → MOTION → EDIT → SOUND → FILM, each stage linking to
  the lecture(s) that teach it. This is a genuinely new component, distinct
  from the media component family above (which renders one week's actual
  asset) and from `CardGrid` (which lists, but doesn't sequence). Exact
  visual treatment is implementation detail once "Visual direction" above
  is settled; the requirement itself — that Home earns its place with a
  real progression experience, not decorative prose — is the part recorded
  here.

## Responsive, accessibility and performance

**Already automated, confirmed from `README.md` and `package.json`:**
`pnpm build` runs axe over every rendered page and fails on a dangling
content ref or a base-path-broken link; `pnpm check` runs typecheck + build +
the `spec/` suite. This is a real floor, not aspirational.

**Not automated, needs a manual pass:** README names "the two marking
viewports" for decks specifically ("nothing checks whether a slide fits or
stays legible; that only shows up in a browser, at the two marking
viewports") without stating the numbers — deliberately, since restating a
fact the assessment page already owns is how the two start to disagree.
The course site's assessment page (`#marking-environment`) pins them down:
**1920×1080 (desktop)** and **390×844 (phone, the iPhone preset in Chrome
DevTools' device toolbar)** — both are full marking environments, not a
primary/secondary pair. README doesn't need editing for this; it already
points at the assessment page rather than hardcoding the numbers. Spot-check
against these two exact sizes is Phase 9's job once the deck content exists
(it now does — see phase 5).

**Performance:** `sharp` is a build dependency and the hero already ships as
`.avif`, so the image pipeline is already doing real optimisation work.
Flat, large-negative-space decorative stills should compress well. No stated performance
budget found in README — treating this as genuinely unspecified rather than
inventing a Lighthouse target that isn't asked for anywhere.

## Implementation phases

0. **Done** — 12-week curriculum skeleton drafted; curriculum-reviewer pass
   run against it; week 12 restructured per "Process" above.
1. **Starter-content removal — done.** `course-config.ts`, Home's body copy,
   both people bios, and the policies page are real content. Home's hero
   artwork, `card.png`, and both people portraits have all been regenerated
   under the abstract graphic system (see "Visual direction" above) — none
   of the four tracked starter images remain, and `pnpm check:evidence`
   passes on this row.
2. **Visual direction — done.** Global typography/spacing/motion rules live
   in `src/styles/visual-direction.css`, registered via the theme's
   `brandCss` integration option (`astro.config.ts`) rather than
   `PageLayout.astro` as first assumed: `PageLayout.astro` is only the
   layout for standalone `.mdx`/`.astro` pages (Home, the index pages,
   policies) — collection detail pages (lectures, sessions, assessments,
   people) render through the theme's `ContentLayout` directly and never see
   it. `brandCss` is the mechanism that already reaches every page (it's how
   `astro-theme-slop/slop.css` gets there).
3. **Media component family — not yet built.** The reusable text/image/
   audio/video/comparison/director's-note/rationale component family (per
   "Component strategy") remains open, deferred until real per-week
   production assets exist to size it against (see Phase 6) — nothing in
   the checklist below has a real asset yet, so there is nothing concrete to
   render through it today.
4. **Home rewrite — done.** Home carries the thesis-plus-progression
   explanation and links through to Lectures.
5. **All-12 decks — done.** Real content written for all 12 lecture decks
   (week 1's pre-dates this phase; weeks 2–12 written against this phase),
   each distilling that week's objectives, directing concepts, the
   demonstration context, the session's task, and the expected output —
   text-only, matching week 1's structural pattern (impact / content /
   quote / task / impact) but without new decorative background imagery,
   which week 1 alone was approved for (see "Visual direction" revision
   history above). Every lecture's `slides:` frontmatter now points at its
   deck. Verified with `pnpm check`: typecheck, build (axe + link checks
   across all 47 pages, astromotion's structural check across all 12
   decks), and the `spec/` suite all green.
6. **Progressive integration, ongoing** — as each week's real
   teaching-demonstration asset is produced (per `MANIFEST.md`'s section
   1), attach it to that week's Lecture page via the media component
   family and update that row's status. Not a single implementation
   phase — this runs alongside the other phases for the rest of the
   course. `spec/` grows the same way: contract tests get added for
   whatever site behavior actually ships, progressively, not written
   upfront against a feature that doesn't exist yet.
7. **Process evidence** — real `PROCESS.md` account with resolving commit
   citations; no `reflections/` entry required (`comp4020-ass2-` prefix maps
   to an empty expected-reflections list in `check-evidence.ts`).
8. **Full curriculum-reviewer pass, once all content above is complete** —
   lectures, sessions, assessments, all 12 decks, and the real operational
   demonstrations together. Report-only, as always; any change it prompts
   comes back for approval before being applied.
9. **Final check pass — spot-check done.** `pnpm check` and
   `pnpm check:evidence` green (see "Definition of done"). Manual spot-check
   against both marking viewports (1920×1080 desktop, 390×844 phone) run
   across all 12 decks' title/impact/quote slides and every table-bearing
   slide (weeks 1, 4, 6, 8, 9, 12): all render fully within bounds at both
   sizes, nothing clipped or overflowing. One methodology pitfall worth
   recording since it produced a false positive first: emulating the phone
   viewport by launching Chrome headless with `--window-size=390,844` is
   **not** equivalent to DevTools' device toolbar — Chrome enforces a
   real-window minimum width well above 390px, so content gets laid out
   against that wider enforced width and then the screenshot is cropped to
   390px, making correctly-fitting slides look clipped. Driving
   `Emulation.setDeviceMetricsOverride` directly over CDP (what DevTools'
   device toolbar itself uses) gives the true 390×844 layout and shows no
   defect. Re-run any future viewport spot-check with real device-metrics
   emulation (CDP or DevTools itself), not a resized browser window.

## Definition of done

- `pnpm check` green: typecheck, build (axe + link/ref checks), `spec/`.
- `pnpm check:evidence` green: no `STARTER_CONTENT` markers left in `src`;
  none of the four tracked starter-image hashes unchanged (`card.png`,
  `hero-home.avif`, both people `.avif` portraits — or deliberately deleted);
  `PROCESS.md` has no `TEMPLATE:` marker and at least one commit citation that
  resolves; `CLAUDE.md` present.
- Every assessment's marking criteria still has a matching `related:` edge
  (curriculum-reviewer's structural check, re-verified if content changes
  again after this pass).
- The thesis is legible from whatever a skimming visitor hits first (Home,
  per "Site architecture" above) — the human-judged bar, not a test.
- All 12 lectures have a completed, real deck, week 1 included.
- Every `MANIFEST.md` teaching-demonstration row (`BIS-W*`) whose Notes
  claim a produced asset is real, produced material — never a placeholder
  or curriculum-illustration stand-in presented as one, no matter how
  finished it looks; a row's own status only flips to `INTEGRATED` when
  the real asset actually exists. (The owner's separate personal-
  production checklist that once tracked `OWN-W01`–`OWN-W12` here was
  paused and removed 2026-09-13 — see "Multimedia strategy" and Revision
  history — and is no longer part of this bar.)
- The full curriculum-reviewer pass has run against the complete 12-week
  content, decks included, and every finding is either fixed (with sign-off)
  or recorded as a deliberate judgement call, same standard as the pass
  already completed.
- `spec/` has grown contract tests for whatever site behavior actually got
  built. It's left unchanged for now, while nothing has been implemented
  yet; tests get added progressively as implementation proceeds, not held
  frozen at its current state.
- All ~28+ currently-uncommitted files committed with a history `PROCESS.md`
  can actually cite.

## Risks

- **Conflating "Before It Stops" (a fixed curriculum teaching example) with
  a genuinely produced demonstration is the single easiest mistake to make
  from here on.** Every week's lecture/session text narrates "Before It
  Stops" as its worked example — that's fine for teaching, and several
  weeks additionally have a genuine produced demonstration pair — but the
  moment any authored teaching prose gets treated as if it were one of
  those real, produced assets (e.g. reusing week 3's "last ring" scene
  sketch as if it were an actual generated shot), the swap-out promise
  above breaks. (The owner's own separate short-film production is paused
  as of 2026-09-13, not part of this risk any more — see "Multimedia
  strategy" and Revision history.) Mitigation: `MANIFEST.md`'s section 1
  marks every `BIS-W*` row by its actual production status precisely so
  curriculum illustration can never quietly count as production evidence.
- **Three index pages plus Home carry template meta-commentary that isn't
  caught by any automated check.** `src/pages/lectures/index.mdx`,
  `sessions/index.astro`, and `assessments/index.mdx` all contain sentences
  written *to the template author* ("A course decides how many lectures it
  needs," "Set the visible singular and plural names once in
  `site-config.ts`") — none carry a `STARTER_CONTENT` marker, so
  `check:evidence`'s grep passes them silently. This is the single biggest
  gap between "checks pass" and "looks finished": worth fixing even though
  nothing forces it, and worth remembering that a green `check:evidence` run
  is not itself proof the site is done.
- **Policy content (late penalties, extensions, academic integrity) has to be
  invented** — there's no real university policy to source from. Risk: it
  reads as authoritative when it's fabricated. Mitigation: keep it generic
  and plausible, don't invent specific numbers (a % penalty, a day count)
  that would look like a citable institutional rule if they're made up.

## Process note to self

This file should have existed before the curriculum-reviewer fixes were
applied, not after — [[comp4020-a1-lessons-for-a2]] already named "detailed
PLAN.md" as part of the process that scored well on A1, and this repo went
several sessions without one. Going forward: update this file when a
structural decision is made, not just when content is written.

## Assignment 1 — worked guidance and detailed spec

Approved and implemented 2026-09-13: `assignment-1.md` now walks students
through the "Before It Stops" example (logline, screenplay beats/intent,
bible entries, five-shot storyboard draft) alongside instructions for
their own films, with the spec expanded into observable checks (screenplay
coverage, identity vs. changing state, unique shot purpose, matching shot
IDs, framing/movement/action, timing, named dependencies). No deadline,
assessment weight, or marking-category weight changed. Full text moved to
[PLAN-ARCHIVE.md → "Assignment 1 — worked guidance and detailed
spec"](PLAN-ARCHIVE.md#assignment-1--worked-guidance-and-detailed-spec).

**Detailed rubric matrix — approved and implemented 2026-09-13**, same
treatment as the Final Project's rubric addition below it in this file
("Final Project — weighted criteria and walkthrough" → "Detailed rubric
matrix"), applied here on owner request. Each of the three existing
criteria (Story and screenplay craft 30%, World and continuity design 30%,
Shot planning and storyboard 40%) splits into three dimensions, each
scored 1–10 against three bands (7–10 / 5–6 / 1–4); a criterion's mark is
its weight scaled by the average of its three dimension scores. Markdown
body content only (a "Detailed marking rubric" section) — the existing
worked-example walkthrough above it is unchanged, and no criterion name,
weight, deadline, or `spec:` bullet changed.

## Assignment 1 — shot-list scope narrowed to already-taught skills — approved

Approved and implemented 2026-09-13, after a full 12-week coherence review
(owner-approved; run by direct file read-through, per `CLAUDE.md` →
"Curriculum review," rather than the curriculum-reviewer subagent) found
that the shot-list `spec:` bullets and rubric required a per-shot
**estimated duration** (summed and individually justified against the
film's 2–4 minute runtime) and **relevant sound or cut cues** — neither of
which is taught or practised anywhere before Assignment 1's week 6 due
date (2027-04-12). Per-shot duration-as-pacing is first taught in week 10;
cut-as-directorial-choice in week 9; sound direction in week 11. No
workshop (02, 04, 06) practises assigning either field, and the Final
Project doesn't already grade this at shot-list level — it grades
editing/sound rhythm holistically in the finished film instead.

Fix applied: `assignment-1.md`'s shot-list `spec:` bullets, the section 4
task instructions, the worked example (dropped the per-shot duration
column and its derived total), the marking-criteria summary row, and both
affected rubric dimensions ("Staging legibility and continuity," "Timing
and production order") were reworded to drop the per-shot duration and
sound/cut-cue requirement. The whole-film 2–4 minute runtime constraint
stays, but as a holistic "does the shot list plausibly cover this
runtime" check (consistent with week 2's segment-level scope-test
teaching), not a per-shot-summed, individually-justified figure. No
deadline, submission format, marking-category weight (40/30/30), or
dependency/production-order requirement changed.

Two other findings from the same review — session 02's activity-numbering
format not matching every other session, and week 10's "montage and
rhythm" lecture concept never rehearsed in that week's workshop — were
identified separately. Both are now fixed (2026-09-15): session 02's
formatting gap (presentation-only — see `handoffs/week-02.md`), and week
10's montage gap (a genuine spec/content change — see "Judgement calls"
below and `handoffs/week-10.md`).

## Final Project — weighted criteria and walkthrough

Approved and implemented 2026-09-13, on owner request to make
`final-project.md` more detailed and "more executable," matching the level
of guidance Assignment 1 already has. This is a deliberate departure from
the assessment's original holistic marking (recorded in "Structure" above
as "judged as a directed film, not a demo reel," chosen to resist
checklist-style marking) — the owner reviewed that tension and approved the
change anyway.

`marking.mode` changed from `holistic` to `weighted`, with three criteria:
Directorial coherence and craft (45%), Director's statement (30%,
including the revision-period change previously only named in a `spec:`
bullet), Authorship reflection (25%). A "Complete the project" section was
added with one numbered subsection per submission part (film, director's
statement, reflection), each giving **Your task** instructions and a
**Check your work** self-verification — deliberately with **no worked
example**: the owner rejected an initial draft that illustrated each
section with the course's own "Before It Stops" material, on the grounds
that a worked example is "too inflexible" this late in the course, when
every student is already building their own locked film from their own
Assignment 1 package rather than the course's running example. A "How the
marking criteria apply" table was added, mirroring Assignment 1's rubric
table. No deadline, assessment weight (60), or `spec:` bullet changed.

This does not apply to Assignment 1's existing worked examples (week 6),
which stay as they are — students haven't locked their own story/world yet
at that point, so a worked example there doesn't compete with a project
already their own.

**Story-switch option — approved and implemented 2026-09-13.** Owner
observation: some students will want to change which film they finish with
partway through the course, and the assessment shouldn't force them to
keep building on Assignment 1's story if they'd rather not. Problem this
creates: `final-project.md`'s brief, "What you submit" list, and its
"Finish and lock the film" walkthrough subsection all currently require
the finished film to match "the world and story locked in Assignment 1,"
and Weeks 7 and 12's lectures tell students to check their work against
"the bible locked in Assignment 1" specifically — both assume one
continuous story from week 6 onward.

Approach approved: a student may finish the project with a different
story than the one they locked in Assignment 1. Two conditions attach,
both owner-confirmed rather than assumed:

- if they switch, a short **pivot plan** for the new story — an updated
  logline, the world/character bible entries it depends on, and a shot
  list — accompanies the final submission, standing in for Assignment 1's
  package as the locked reference continuity gets checked against. This is
  a submission requirement, not a separately graded or separately weighted
  artefact — it's assessed only insofar as it lets "Directorial coherence
  and craft" be checked against something fixed, the same as it always was
  against Assignment 1's package.
- the director's statement must name the switch itself as one of its
  three defended decisions, against the specific alternative of continuing
  the original story — the same "name a decision, defend it against an
  alternative" standard the statement already applies to a shot or edit
  choice.

Changed in `final-project.md`: the brief's opening quote, the "What you
submit" film bullet (plus a new conditional bullet for the pivot plan), the
"1. Finish and lock the film" and "2. Write the director's statement"
walkthrough subsections (task + check-your-work), and a new conditional
`spec:` bullet covering both the pivot plan and the statement requirement.
No criterion name, weight, due date, or the assessment's weight (60)
changed; the existing four `spec:` bullets are unchanged, this is an
addition.

Consequential wording sync, not a separate decision: Week 7's and Week
12's lectures both tell students to check work "against the bible locked
in Assignment 1" — narrowly true only for a student who didn't switch.
Reworded to "your locked pre-production package — Assignment 1's, or your
pivot plan's if you switched stories since" so the underlying teaching
point (check against something fixed, not fresh impression) still holds
for either case. No learning outcome, `spec:` bullet, or timing in either
week changed.

Explicitly assumed, absent a contrary instruction: Assignment 1 itself is
ungraded by this change — a student's Assignment 1 mark stands on whatever
story that submission described, regardless of a later switch. The pivot
plan is not resubmitted or separately marked; the Final Project's existing
three weighted criteria cover it entirely. Weeks 7–11's own `spec:`
bullets and workshop activities are unchanged — they already operate on
"your locked bible" generically and needed no rewording beyond the two
lecture sentences above.

Checked and confirmed unaffected at the time: `MANIFEST.md`'s `BIS-W*` rows
track the course's own "Before It Stops" teaching assets, not
student-submission continuity — no row, dependency, or status cell assumes
a student carries one story from Assignment 1 to the Final Project, so
none needed changing. (`MANIFEST.md` also carried a separate `OWN-W01`–
`OWN-W12` owner-evidence section at the time of this check; that section
was later paused and removed 2026-09-13 — see "Multimedia strategy" and
Revision history — unrelated to the story-switch decision recorded here.)

**Detailed rubric matrix — approved and implemented 2026-09-13**, on owner
request for markable detail beyond the one-line-per-criterion summary
table above. Each of the three criteria splits into three dimensions,
each scored 1–10 against three bands (7–10 / 5–6 / 1–4) describing what
earns that range; a criterion's mark is its weight scaled by the average
of its three dimension scores. This is markdown body content (a
"Detailed marking rubric" section in `final-project.md`), not a
frontmatter schema change — `content.config.ts`'s `weightedMarking`
criteria shape (`name` + `weight` only) is unchanged, since it drops
unrecognized keys silently and isn't `.loose()`. No criterion name,
weight, deadline, or assessment weight changed.

## Weeks 7–8 — second-frame Sora 2 demonstration

Owner instruction (2026-09-13): use the existing Week 1 Take B source frame
(the second candidate) for Week 7 and retain actual rejected generations for
Week 8. Model is explicitly `sora-2`, not legacy Sora or `sora-2-pro`.

Use `resources/week-05/images/week1-take-b-source-frame.png` (1280×720):
Nadia's face, sweater, arms and table phone are visible. Demonstrate a fixed
medium shot of the incoming call and her resistance with two notes differing
in the onset of the reach. Keep the scripted outcome and identity fixed.
The shared antecedent is that she has just finished packing her mother's
kitchen; do not invent previous missed calls or change sibling history.
Generate phone and face inserts separately if needed for the owner-approved
medium → caller insert → face close-up sequence, preserving eyeline and
ringtone continuity. The first frame and each insert must be checked against
existing identity/prop references. Legible phone text may be overlaid in
post-production and must be labelled as such.

Produce and inspect real videos before describing their results. Retain
original files, prompts, job IDs and actual failures. Week 8 reuses those
files and logs observable failures, likely cause with uncertainty, next
instruction and the reason for selection. Do not manufacture failures or
claim all three causes are demonstrated. The diagnostic classroom comparison
should disclose prompts/references before inferring causes from appearance.
Existing learning outcomes/spec, assessment weights and timings remain.
Update the two lectures/decks/examples to the actual shot and footage once
available; record unresolved requirements honestly if network/API or output
quality blocks completion. Do not mark owner evidence as fulfilled merely
because a teaching demonstration exists. Direct OpenAI access currently needs
the same local HTTP proxy used by the earlier Week 1 scripts.

## Revision history

The full ledger from 2026-09-04 through 2026-09-13 (typography/visual-
direction decisions, the "Table for One" → "Before It Stops" substitution
and its follow-on corrections, the Week 1–4 depth-pass entries, the
Weeks 5–12 approvals, the Week 2/Week 6/Assignment 1 additions, and the
two "Week 5/7/8 corrections approved" / "Review items 2/5 approved"
sub-entries) moved to [PLAN-ARCHIVE.md → "Revision
history"](PLAN-ARCHIVE.md#revision-history). Each entry there records a
departure from this plan that was proposed, approved, and then applied —
not routine work that simply followed the plan as written, per "Plan
governance" above.

A fresh ledger starts below, following the single-record rule in
`CLAUDE.md` → "Planning and human–agent decision making": routine work
needs no entry; an approved departure from what's already in force gets
its section updated in place *and* one dated entry here naming the exact
change — never both a standalone permanent section and a duplicate
history entry for the same decision.

- **2026-09-13** — Owner authorized the documentation reorganisation
  recorded in "Documentation reorganisation — approved" above: completed
  implementation narratives and superseded proposals (the Week 1–2
  teaching corrections, the four Week 3/4 sub-passes under "Grounding in
  real directing pedagogy," the Week 5 and Weeks 6–12 depth passes, the
  Week 2 good-story addition, the Week 6 bible→keyframes pass, the
  Assignment 1 pending-decision alignment pass, the Assignment 1 worked-
  guidance pass, the 2026-09-04 dismissed judgement-call findings, and
  the full pre-2026-09-13 revision ledger) moved verbatim to the new
  `PLAN-ARCHIVE.md`, each leaving a short current-status pointer at its
  original heading in this file. No content, learning outcome, spec
  bullet, marking weight, or approved design decision changed — this is a
  documentation-structure change only. "Weeks 7–8 — second-frame Sora 2
  demonstration" was checked and deliberately left in place, unarchived,
  as still-open/ambiguous work; "Week 1 status" (inside "Grounding in real
  directing pedagogy") was likewise checked and kept active, since
  `BIS-W01-WORKSHOP` remains `NOT STARTED` in `MANIFEST.md`.
- **2026-09-13** — Owner approved converting the Final Project's marking
  from holistic to weighted (Directorial coherence and craft 45%,
  Director's statement 30%, Authorship reflection 25%) and adding a
  worked-example-free "Complete the project" walkthrough (instructions +
  self-check per submission part). See "Final Project — weighted criteria
  and walkthrough" above. Assessment weight (60), due date, and `spec:`
  bullets unchanged.
- **2026-09-13** — Owner requested a detailed marking rubric (three
  dimensions per criterion, 7–10/5–6/1–4 bands) for both graded
  assessments. Added to the Final Project first, then the same treatment
  applied to Assignment 1. See "Final Project — weighted criteria and
  walkthrough" → "Detailed rubric matrix" and "Assignment 1 — worked
  guidance and detailed spec" → "Detailed rubric matrix" above. No
  criterion name, weight, deadline, or `spec:` bullet changed in either
  file.

- **2026-09-13 (Week 9)** — Owner requested completion after commissioning and delivering the five shots and assembly. Authorized real-assembly integration into Week 9 lecture/deck, replacing the hypothetical continuity example; no outcome, assessment or timing changes.

- **2026-09-13 (Week 10 real comparison)** — Owner requested both actual cuts be used as the Week 10 example. Replace hypothetical recut findings with the single reaction-duration change, playable videos and intended emotional descriptions; no assessment or timing changes.

- **2026-09-13 (story-switch option)** — Owner approved letting a student
  finish the Final Project with a different story than the one locked in
  Assignment 1, rather than requiring continuation, on condition that a
  switch comes with a short pivot pre-production plan (logline, bible
  entries, shot list) for the new story and is named as one of the
  director's statement's three defended decisions. See "Final Project —
  weighted criteria and walkthrough" → "Story-switch option" above. Also
  rewords one sentence each in Week 7's and Week 12's lectures so "checked
  against the bible locked in Assignment 1" reads as "your locked
  pre-production package" instead. Assessment weight (60), due date, and
  the four original `spec:` bullets unchanged; one new conditional `spec:`
  bullet added. Assignment 1's own weight, due date, and marking are
  untouched — its grade stands regardless of a later switch.

- **2026-09-13 — Week 11 real sound example integration approved:** owner accepted the synthesized aligned material and requested application; replace the authored hypothetical comparison with the actual voice pair and dialogue/full-pass/no-music renders, retain provenance and limits, and correct the stale prior-call antecedent. Outcomes/spec/timings unchanged.

- **2026-09-13 (owner's personal-production checklist removed — paused,
  not cancelled)** — Owner is not currently pursuing their own separate
  short-film production alongside the course; may resume it later, just
  not now. "Multimedia strategy" and "'Before It Stops' asset plan" →
  "Division of responsibility" → "The owner" rewritten in place to drop
  the expectation that the owner is producing that separate film, and the
  course overview's "'Before It Stops' is this course's fixed teaching
  example" paragraph reworded to match; none of these described what the
  course itself teaches, assesses, or how "Before It Stops" is used as a
  teaching example, so this is a policy/tracking change, not a curriculum
  change. `MANIFEST.md`'s section 3 (`OWN-W01`–`OWN-W12`, every row still
  `OWNER REQUIRED`/`TBD` — nothing produced under it is lost) removed and
  its own Revision history entry added there; "Definition of done" and the
  "Story-switch option" confirmation note above updated to stop citing the
  removed checklist. This does not touch "Before It Stops" itself (the
  fixed lecture teaching example, unaffected) or any `BIS-W*` teaching
  demonstration already produced — those continue exactly as tracked in
  `MANIFEST.md`'s section 1. Historical entries elsewhere referencing
  `OWN-W*` (in `PLAN-ARCHIVE.md`, and status notes in `resources/week-*/
  materials.md` and `handoffs/week-*.md`) are left as dated record of what
  was true when written.

- **2026-09-13 — Week 12 lecture/workshop format approved:** lecture demonstrates critique and defence on teaching excerpts; actual student screenings and three-decision defences run in workshop groups of 4–5. Timings, specs and assessment unchanged; examples use the established packing antecedent and actual cue placement without claiming an unproduced repair.

- **2026-09-13 (Week 1 workshop simplified — owner approved):** retain existing Take A unchanged; remove all workshop Take B production/selection and A/B comparison requirements. Replace them with observable diagnosis, written playable redirect, peer checking and note revision. Update session spec and activities to this scope; preserve the 120-minute total, counterfactual beat, lecture/deck demonstration and existing QA/provenance limitations.

- **2026-09-13 (Assignment 1 shot-list scope narrowed — owner approved):**
  following an owner-approved full 12-week coherence review, dropped the
  per-shot "estimated duration" and "relevant sound or cut cues"
  requirement from Assignment 1's shot list — neither is taught or
  practised before the week 6 due date (duration-as-pacing: week 10;
  cut-as-choice: week 9; sound direction: week 11). See "Assignment 1 —
  shot-list scope narrowed to already-taught skills — approved" above.
  Deadline, submission format, and marking-category weights (40/30/30)
  unchanged.
- **2026-09-15 (Week 10 montage rehearsal added — owner approved):**
  closed the previously-accepted "montage lectured, never rehearsed"
  judgement call. `10-recut-lab.md`'s spec bullet and Activities 1/3/4/5
  now require the workshop's second cut to be a repeat/reorder (montage)
  decision instead of a second duration variant; `week-10.md` gained one
  bridging sentence naming the requirement. See "Judgement calls" above.
  Workshop timing (120 min), the lecture's real Cut A/Cut B example, due
  dates, and all other weeks unchanged.
- **2026-09-15 (Assignment 1 single-scene wording clarified — owner
  approved):** closed the previously-accepted "single-scene practice vs.
  Assignment 1's multi-scene brief language" judgement call. Reworded
  `assignment-1.md`'s `spec:` bullet ("scene headings" → "a scene heading
  for each scene it contains") and its "Your task" screenplay instruction
  ("Include every scene..." → "Cover the film's beginning to its ending —
  whether that's one continuous scene or several") so neither implies a
  multi-scene requirement that was never actually graded. See "Judgement
  calls" above. No marking weight, criterion, due date, runtime
  requirement, or rubric band changed; the single-scene running example
  and teaching progression are unchanged.
