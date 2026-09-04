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
time: *"Table for One"* — a daughter's one last meal with the estranged
father whose diner is closing that night. Reasoning: the course should feel
like one continuous production building toward the final crit, not twelve
disconnected topic weeks. A single scene also keeps the storyboard, shot
list, and character work from week 4 onward legible as the *same* project a
student can point to in their director's statement.

**"Table for One" is a placeholder subject, not a creative decision.** The
site owner has not chosen the real video's subject yet; "Table for One" may
be retained or replaced when that decision is made. Until a subject is
chosen, "Table for One" exists only inside the curriculum's teaching prose
(lecture/session text, used to illustrate what a logline, a bible entry, a
shot list *look like*) and does not count as completed production work. The
lectures' operational demonstrations are a separate matter: the site owner
must actually perform those workflows and produce real video/image/audio/
production-process material from them — invented, simulated, or merely
plausible-looking stand-ins must never be presented as real demonstrations.
The placeholder stays useful anyway, because it's small and already fully
worked out in text, making it the cheapest way to test the site's structure
before the real subject and its assets exist. Real assets, once they exist,
attach directly to the Lecture page for the week they demonstrate — see
"Content and data architecture" below.

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

- `PROCESS.md` — still the unfilled template; needs the actual account once
  the curriculum content is committed (currently 28+ files uncommitted).
- Whether to revisit either of the two open judgement calls above before
  shipping.
- The full curriculum-reviewer pass described under "Process" above is
  pending until the decks and the real operational demonstrations exist;
  running it earlier would only re-check the same text graph the completed
  pass already covered.

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

**This is a real production, not a static demo site.** The video's subject
is still undecided; it is not automatically "Table for One." Regardless of
the chosen subject, the site's owner will genuinely carry out the operations
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
card, portraits) and — kept deliberately minimal, see below — the "Table for
One" placeholder used to test the display system before real material
exists. Image budget is confirmed sufficient for that limited use; this is
not tracked as an open risk.

**Still open, needs checking before the display-system build (see
"Implementation phases" below):** the theme ships a `YouTubeEmbed`
component, sized for a hosted video URL — need to confirm whether the
owner's actual video takes will be hosted somewhere embeddable or delivered
as files the site serves directly (different component, different
build-size implications). Not deciding this now; flagging it as the first
thing to resolve once real footage exists.

## "Table for One" asset plan

**No asset generation for "Table for One" while it is only the
placeholder.** It is currently a placeholder used only to prove the site's
structure and asset-display components work, not a small production
heading toward a finished result of its own. Generating a large
"final-looking" asset set for it now would prematurely turn a placeholder
into the real video's subject. If the owner later deliberately selects this
story, its status changes and the lecture demonstrations must still be
genuinely produced rather than filled with placeholder assets.

What "Table for One" gets, and no more:
- it stays inside lecture/session **prose only** — no new images, audio or
  video generated for it beyond what the site's own presentation needs
  (hero image, social card — see "Visual direction" above, unrelated to the
  film's story).
- if a placeholder is genuinely needed to test one specific display
  component (e.g. confirming an anchor-frame image slot renders correctly
  before real footage exists), generate the single minimum image needed for
  that test, labelled visibly as a placeholder, and delete it once real
  material replaces it. Not a batch, not up front.
- the site's information architecture makes swapping it out a content
  change, not a structural one: real assets attach directly to the Lecture
  page they demonstrate, per "Content and data architecture" below.

## Week-by-week asset checklist

This is the actual deliverable this table exists to answer, and it comes
straight from what each week's session `spec:` and each assessment's
`spec:` already say — nothing here is invented. "Essential" means it's a
literal spec bullet; "Optional/stretch" is a suggested enrichment, marked as
such, never a spec requirement dressed up as one. **Status is the same for
every row right now: `required — not started`.** Nothing has been produced
yet; "Table for One" satisfies none of these rows because it exists only as
teaching prose, not as a real asset of the owner's own project (see above).
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
keeps "Table for One" swappable for the real project by construction: each
lecture names its own asset slot, not "the Table for One version of X," and
there's no second collection to keep in sync with the first.

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
viewports") — the actual viewports haven't been pinned down yet. Need to
find that in the brief/spec before claiming deck legibility is covered,
rather than assuming desktop+mobile and being wrong.

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
9. **Final check pass** — `pnpm check`, `pnpm check:evidence`, and a manual
   spot-check at the actual marking viewports once identified.

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
  curriculum-illustration stand-in (including any "Table for One" prose),
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

- **Conflating "Table for One" (currently curriculum teaching prose) with the
  owner's still-undecided real production is the single easiest mistake to
  make from here on.** Every week's lecture/session text still narrates
  "Table for One" as its worked example — that's fine for teaching, but the
  moment any of that prose gets treated as if it were a real asset
  satisfying a checklist row (e.g. reusing week 3's Del/Mara scene sketch as
  if it were the owner's actual screenplay), the swap-out promise above
  breaks. The owner may still choose this subject later, but that requires
  an explicit creative decision; it cannot happen by default because the
  placeholder was already present. Mitigation: the checklist above marks
  every row `required — not started` precisely so curriculum illustration
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
