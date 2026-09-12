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
  describe the new approved state, and a revision record is appended to
  "Revision history" at the bottom stating the date/time and the exact
  change made.
- The plan is never silently rewritten to match an implementation that
  diverged from it — a divergence is either rejected, or approved and then
  recorded as above.

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
device, not the owner's film and not a required student project.** It
replaces the earlier placeholder, *"Table for One"* (a daughter's one last
meal with the estranged father whose diner is closing that night), by
owner-approved global substitution on 2026-09-11 — see "Revision history".
The substitution changed only the story's flavour text: every learning
outcome, weekly sequence, assessment requirement, duration, and template
this plan already settled stays exactly as approved. "Before It Stops"
exists inside the curriculum's teaching prose (lecture/session text, used to
illustrate what a logline, a bible entry, a shot list *look like*) and, for
week 1 only, as a genuinely produced demonstration pair (see "Week 1
status" below) — it is never a stand-in for the owner's own required
production evidence, which the week-by-week asset checklist tracks
separately and which this teaching example must never be presented as. The
lectures' operational demonstrations are a separate matter: the site owner
must actually perform those workflows and produce real video/image/audio/
production-process material from their own project — invented, simulated,
or merely plausible-looking stand-ins must never be presented as real
demonstrations. Real owner assets, once they exist, attach directly to the
Lecture page for the week they demonstrate — see "Content and data
architecture" below.

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
  scenes. One scene was chosen for continuity (see "Structure"), but
  Assignment 1's own brief language describes a screenplay/shot list/
  storyboard package in terms that could imply more than one scene.
  Unresolved — see "Judgement calls".
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
- Whether the single-scene running example is actually adequate practice for
  Assignment 1's brief, or narrower than what it asks for.
- Whether montage — lectured week 10 — needing no rehearsal week is a
  legitimate scope cut (not every taught concept needs a practiced session)
  or an actual gap the reviewer was right to flag.
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

Two subjective findings from the coherence review remain open by choice,
not by oversight — the reasoning for each is recorded here rather than
left as a bare "open" flag:

- **Single-scene practice vs. Assignment 1's multi-scene brief language.**
  Kept single-scene. Reasoning: the continuity payoff (one project a
  student can point to across sessions and in the final director's
  statement) outweighs matching the brief's phrasing literally, and nothing
  in the assessment's actual marking criteria requires more than one scene
  — only the descriptive brief text reads that way. Flagged as the
  assumption most worth a second pair of eyes before shipping.
- **Montage lectured week 10, never rehearsed in a session.** Left
  unrehearsed. Reasoning: not every lectured concept needs its own practice
  session — week 10's session (recutting one sequence twice) already
  exercises the pacing judgement montage depends on, just not multi-scene
  intercutting specifically. Judged this close enough rather than adding a
  session purely to check a box.

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

**This is a real production, not a static demo site.** The owner's own
video subject is still undecided; it is not "Before It Stops," which is a
fixed lecture teaching example and stays one regardless of what the owner
eventually chooses to direct. Regardless of the owner's chosen subject, the
site's owner will genuinely carry out the operations
demonstrated in the lectures and produce the resulting images, video takes,
voice reads, ambience, Foley, music and finished video. The job on the
website side is **not** to generate a plausible-looking set of finished
assets or fake the lecture demonstrations — it is to build the system that
displays the real outputs at each stage, cleanly, and gets visibly richer as
richer material arrives.

**Two responsibilities, kept separate:**
- **The site owner's:** follow the course, produce the real creative/
  production asset for each week (below), and hand it over.
- **The site's:** design and implement one coherent system — visual
  language, layout, component set — that teaches the course *and* displays
  those assets as they progressively arrive, textual through final film,
  without a redesign at every media-type transition.

**The progression the display system has to support**, matching the
course's own arc: **TEXT → SCRIPT → VISUAL DEVELOPMENT → STORYBOARD → IMAGE →
MOTION → EDIT → SOUND → FINAL FILM.** Concretely: every asset slot in the
week-by-week checklist below needs a display treatment for whichever of
text / image / audio / video it turns out to be, sharing one visual system
(typography, spacing, the site's own decorative graphic system for chrome —
see "Visual direction" above). Real production assets are displayed as
themselves within that system, not restyled into it — per "Decorative
artwork vs. teaching visuals" in "Visual direction" — so a text-only week-2
entry and a video-plus-audio week-11 entry read as the same course, not two
different sites bolted together.

**What this repo can and can't generate itself, separated from what the
owner supplies:** `scripts/generate-image.ts` generates stills only, and is
not the source of the real production's images, video or audio — those come
from whatever the course's own workflow directs the owner to use, outside
this repo, and arrive here as files to embed. The only thing this repo's
image generator is for is the site's own presentation assets (hero, social
card, portraits, decorative deck backgrounds). Image budget is confirmed
sufficient for that limited use; this is not tracked as an open risk.

**Still open, needs checking before the display-system build (see
"Implementation phases" below):** the theme ships a `YouTubeEmbed`
component, sized for a hosted video URL — need to confirm whether the
owner's actual video takes will be hosted somewhere embeddable or delivered
as files the site serves directly (different component, different
build-size implications). Not deciding this now; flagging it as the first
thing to resolve once real footage exists.

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
- **The owner** produces all genuine personal-project evidence the course
  requires (the week-by-week asset checklist below). Teaching examples are
  never presented as the owner's work, and the reverse never happens
  either.

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
| 5 | Already solid | (keep as-is) | already peer-verified; only add named durations/phases |
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

**Week 1 status: `content done, workshop blocked on an asset`.** The
lecture and deck are complete and runnable as-is. The workshop's written
instructions are complete, but the workshop itself cannot run in class
until `BIS-W01-WORKSHOP` (below) is produced. The design above is applied
in `week-01.md`,
`week-01.deck.mdx`, and `01-getting-started.md`: a single
instructor-provided locked scene (description, reference, character
objective, and intended audience interpretation) shared by the whole
class, so a redirect (Note B) is a diagnosed adjustment to that same
objective, never a second unrelated note. The lecture's real demonstration
walkthrough is integrated: a genuine Note A → Take A → diagnosis →
Note B → Take B pair, generated with `sora-2` and QA'd by Codex (see
`resources/week-01/materials.md` for the full production/QA record and
`MANIFEST.md` for its manifest entry), served from
`public/resources/week-01/`.

The workshop's own locked scene **is** a "Before It Stops" beat — a
distinct one from the lecture's, so the exercise doesn't just re-solve
the diagnosis students already watched. **Corrected 2026-09-12: it is an
explicitly counterfactual rehearsal variation, not the story's canonical
continuation.** Weeks 2 and 3 establish the canonical ending — Nadia
answers on the final ring before the call would go to voicemail — so the
workshop instead asks "what if she hadn't answered?": the call has gone
unanswered to voicemail, and Nadia is deciding whether to call her
brother back. Same story, same characters, same table, a deliberate
fork away from what actually happens, not "a beat further on" in the
same timeline. (A same-day departure to a real film clip — Cooper
watching Murph's message in *Interstellar* — stood briefly as an
approved alternative but was reverted by owner instruction on
2026-09-11; see "Revision history".)

**Redesigned 2026-09-11 (evening): diagnose-and-redirect on an
instructor-provided anchor, not two independent student generations.**
The previous design asked each student to generate Take A and Take B
themselves from the same locked material, on the claim that only the
note would differ between them — but two independent text-to-video
generations cannot reliably hold character, set, composition, props,
lighting, and timing constant, even with a fixed prompt. (The lecture's
own real demo pair used `sora-2`'s remix/video-to-video path specifically
to hold continuity, and its own QA record in `resources/week-01/
materials.md` still notes a minor continuity drift — reframing — between
takes; independent generation is strictly worse than that.) The workshop
now runs on one **instructor-provided** anchor image, locked base prompt,
fixed generation settings, and a prepared Take A for the voicemail-callback
beat — students never generate Take A themselves. They watch it blind,
diagnose one observable gap against the revealed objective and
interpretation, write their own Note B as a redirect, and either apply it
via remix/video-to-video (if the class's tool supports it reliably) or
select and justify the best fit among several instructor-provided Take B
candidates (if it doesn't) — a `direct → generate → evaluate → redirect`
loop that assesses diagnostic and redirect judgment, not generation luck.
This is a new required teaching asset, tracked as `BIS-W01-WORKSHOP` in
`MANIFEST.md` — **not yet produced** (brief at
`resources/week-01/workshop-brief.md`); the workshop as written cannot
actually run in class until it is. See "Revision history".

The workshop stays deliberately **tool-agnostic**: it names no specific
platform, since the previous attempt to lock in one (Pika, chosen after
Sora's discontinuation) still left every step describing that one
platform's UI, which is a maintenance and vendor-lock liability the
loop itself doesn't need. Whatever generation/remix tool is available to
a given offering of the course, the instructions hold.

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

## Week-by-week asset checklist

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

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Assembled sequence, ≥3 shots, 30–60 seconds | First assembled footage — the raw material week 10's recut and week 11's sound pass both build on | video | Essential | Required — not started |
| Continuity log: at least one problem found + fix-or-accept decision + reason | The repair discipline the week teaches: fix what's actually broken, not everything near it | text | Essential | Required — not started |

### Week 10 — Editing and dramatic rhythm

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Two distinct recuts of the week 9 footage, differing in a deliberate pacing decision | Same shots, cut two ways, proves editing is a directorial decision, not a mechanical step | video (×2) | Essential | Required — not started |
| One sentence per cut on the emotional difference it produces | Names the effect on purpose, rather than just noticing it happened | text | Essential | Required — not started |

### Week 11 — Directing with sound

| Asset | Why the course needs it | Format | Essential/Optional | Status |
|---|---|---|---|---|
| Two takes of one line reading, from a single note (pace, breath, hesitation) + which was selected and why | Directing a voice is the same discipline as directing a face — proves it transfers | audio + text | Essential | Required — not started |
| Dialogue-only cut vs. full sound-pass cut (ambience bed + ≥1 Foley/SFX moment + one placed music cue) | Makes the sound pass's effect audible by direct comparison, beat by beat | audio + video (both versions) | Essential | Required — not started |
| Note on what the sound pass changed emotionally, beat by beat | Feeds directly into the final director's statement | text | Essential | Required — not started |

### Week 12 — Screening, critique, and revision / **Final Project**

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
any student who takes it — and adding a structurally separate log for the
owner's own real assets would duplicate that structure for no benefit.
`lectures`' schema already ends in `.loose()`, so an asset-reference field
(or a small array of them) can be added to a lecture's frontmatter
incrementally, week by week, as real material arrives, without a
content-model migration. Assignment 1's and the Final Project's own asset
rows additionally surface on their existing Assessment pages, since those
are the graded submissions — noted per-week in the checklist above. This
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
6. **Progressive integration, ongoing** — as the owner supplies each week's
   real asset (per the checklist above), attach it to that week's Lecture
   page via the media component family and update that row's status. Not a
   single implementation phase — this runs alongside the other phases for
   the rest of the course. `spec/` grows the same way: contract tests get
   added for whatever site behavior actually ships, progressively, not
   written upfront against a feature that doesn't exist yet.
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
- Every **Essential** row in the week-by-week asset checklist above is
  satisfied by the owner's real, produced material. A placeholder, or a
  curriculum-illustration stand-in (including any "Before It Stops" prose,
  and including week 1's genuine lecture-demonstration pair),
  never counts as completing an Essential row, no matter how finished it
  looks — the checklist's own "required — not started" status only flips
  to done when the real asset actually exists. Optional/stretch rows are
  not required to be complete.
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
  the owner's still-undecided real production is the single easiest mistake
  to make from here on.** Every week's lecture/session text narrates
  "Before It Stops" as its worked example — that's fine for teaching, and
  week 1 additionally has a genuine produced demonstration pair — but the
  moment any of that prose or that pair gets treated as if it were a real
  asset satisfying a checklist row (e.g. reusing week 3's "last ring" scene
  sketch as if it were the owner's actual screenplay), the swap-out promise
  above breaks. The owner's own film is a separate, still-undecided choice;
  it cannot be filled in by default because a teaching example was already
  present. Mitigation: the checklist above marks every row `required — not
  started` precisely so curriculum illustration
  can never quietly count as production evidence.
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

## Revision history

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
  See "Week 1 status" above.

- **2026-09-11 (later still).** Reverted by owner instruction: the
  Interstellar film-clip reference is removed from `01-getting-started.md`.
  The workshop's locked scene goes back to a "Before It Stops" beat — the
  call has just gone to voicemail unanswered, and Nadia is deciding
  whether to call her brother back — distinct from the lecture's
  reach-and-withdraw beat so the workshop isn't re-solving the diagnosis
  students just watched. See "Week 1 status" above.

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
  step. See "Week 1 status" above.

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
  `resources/week-01/workshop-brief.md`. See "Week 1 status" above.

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
     happens next. "Week 1 status" above, `01-getting-started.md`, and
     `resources/week-01/workshop-brief.md` reworded accordingly; the
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
