# Process overview

Updated 2026-09-13. This account distinguishes implemented changes from
classroom outcomes that have not been tested. The later decisions below
are supported by current files and working records; some are still
uncommitted and are not presented as published commit evidence.

## What I built

**"Directing for the Screen" (SLOP4555)**, a 12-week directing practicum
where AI stands in for cast and crew, on top of the fixed `astro-theme-slop`
starter. The discipline being taught is directing — shot construction,
performance direction, editorial judgement, sound design — with generation
as the rehearsal medium, not the subject. The running example, "Before It Stops," replaced the original "Table for
One" and threads the teaching material so the storyboard, bible and shot list built in
week 4 are still legible in week 12's finished cut, and two assessments
(a pre-production package, a finished film) keep the structure legible
against that same thesis.

## How I got here

The starter arrived with placeholder content across every collection and no
curriculum of its own — [`b94f8cc`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/b94f8cc15b93243b50932683439f2095b31b30d3),
then given this deliverable's course code
([`3d9a10b`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/3d9a10b0c845f444a27ae070d6ddf1c40107c314)).
The brief's own lines went into `spec/` as contract tests before any content
was written
([`ed160b1`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/ed160b1b4cf37dde4c9911eae5511945fe413982)),
so the site's own build could tell me when a structural claim in the brief
stopped holding.

Before writing twelve weeks of content by hand, I built the check that would
catch the failure mode a schema can't: an assessment demanding a skill never
taught, a lecture claiming a skill no session practises, a learning outcome
nobody assesses. `.claude/agents/curriculum-reviewer.md` is a read-only,
adversarial subagent — Read/Grep/Glob only, no Bash, so it cannot edit
anything it finds wrong — instructed to try to falsify coherence rather than
confirm it
([`cde61f1`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/cde61f111183b2a8e14c2f212f444117f93709cb)).
I also wrote a wrapper around the course's image-generation proxy
([`82769eb`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/82769eb5f4ed35329b72df4559a284df92b051f5))
ahead of the decorative-artwork work that needed it.

The largest single commit
([`9331148`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/9331148ad0bec0490039842440556533c3726399))
built out the full 12-week skeleton — every lecture, workshop session, and
both assessments — and adopted the site's visual direction: a "Director's
Notebook" typography/spacing/motion system, and an abstract flat-geometric
decorative graphic system replacing the starter's literal placeholder
imagery (hero images, both people portraits, the social card). This is
where the curriculum-reviewer paid for itself: an initial pass against the
completed skeleton found four real structural gaps — a due-date
contradiction, storyboarding required in Assignment 1 before ever being
taught, a lecture claiming a directed voice performance no session
practised, and two assessment weeks named in marking criteria without the
matching `related:` edge. All four were fixed in that same commit. A
follow-up pass raised two more findings — week 9's clip assembly apparently
preceding week 10's editing lecture, and no lecture teaching generative-tool
mechanics — that turned out not to be violations at all: they exposed that
`CLAUDE.md`'s teach/practise rule hadn't yet drawn the line between
disciplinary knowledge (must be lectured first) and tool mechanics (a
workshop's job). I clarified that rule rather than restructuring content
around a false alarm; `PLAN.md`'s "Judgement calls" section records the
reasoning for both dismissals, and two genuinely open judgement calls —
single-scene practice against Assignment 1's multi-scene brief language,
and montage lectured but never separately rehearsed — are recorded there
rather than silently resolved either way.

The one piece of that skeleton still real-content-shaped rather than
finished was the slide decks: only week 1 had one, written by hand before
the reviewer pass, background imagery included. Weeks 2–12 got theirs in
[`c2c18e2`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/c2c18e214dea35b9b52120c4df1d2384f3054bcd),
each distilling its lecture's own outline into the deck's structural
pattern (impact → content → the "Table for One" tie-in as a quote slide →
this week's task → what you leave with), deliberately without generating
new background artwork for them — the pilot-first background-image rollout
in `PLAN.md`'s visual-direction revision history was approved for week 1
only, and extending it to eleven more decks wasn't part of that approval.
`pnpm check` (typecheck, build with `axe` across every rendered page and
`astromotion`'s structural check across all 12 decks, and the `spec/`
suite) is how I know the result holds together mechanically; the
curriculum-reviewer pass is how I know it holds together as a course, and
a further full content review can only run with my explicit approval,
under [CLAUDE.md](CLAUDE.md). The earlier reviewer findings describe the
skeleton at that time, not a verification of all subsequent changes.

## Turning examples into workable activities

Reading the course as a beginner exposed a gap that structural tests did
not catch: I could see what a finished screenplay should look like, but
still did not know how to start one. I asked for a fill-in template. The
Week 3 revision added a sequence from premise to decisive scene, scene
change, five observable beats, screenplay form and a director's note.
The [worksheet](resources/week-03/scene-planning-worksheet.txt) is scaffolding,
not a separately graded product. A follow-up correction synchronized the
[lecture](src/content/lectures/week-03.md),
[session](src/content/sessions/03-screenplay-workshop.md) and
[deck](src/decks/week-03.deck.mdx): download and read before class, fill in
during the workshop. This was my own reading feedback, not a student trial.

Week 1 revealed a different constraint. Independent AI generations changed
more than the directing note, making an A/B comparison difficult to interpret.
I first chose an instructor-provided anchor and Take A with prepared Take B
candidates. That reduced student generation variability but increased
production preparation. On 13 September I chose a smaller exercise: retain
the existing imperfect Take A, diagnose one observable performance problem,
write a playable redirect, get peer feedback and revise. The
[session](src/content/sessions/01-getting-started.md) now has six activities
totalling 120 minutes; no workshop Take B is required. The
[brief](resources/week-01/workshop-brief.md) records the boundary: peer review
checks the written note, not improvement in an unproduced performance.
The lecture's real A/B demonstration remains unchanged. Take A's original
production QA failures remain in [generation-settings.txt](resources/week-01/generation-settings.txt);
using it as a diagnosis clip does not turn it into approved production footage.
The revised session passed typechecking, and hashes confirmed the original
and served web video were unchanged. No classroom trial was performed.

## Keeping assessment and student language usable

My screenshot review of Week 6 identified internal asset identifiers in
student-facing prose. The agent replaced them with descriptive labels linking
to the corresponding images. The resource filenames stayed stable. The
[Week 6 handoff](handoffs/week-06.md) records the change and build checks.
This separated traceability for maintainers from instructions students can act on.

I also challenged Assignment 1's demand that every bible decision, including
voice, be resolved. Week 5 explicitly teaches marking unresolved fields as
pending with the decision needed to close them; voice direction comes later.
After approval, the agent changed the relevant assessment spec and prose to
accept resolved decisions or explicit pending decisions. A pending decision
can still block a shot without blocking submission. The
[assessment](src/content/assessments/assignment-1.md),
[approval record](PLAN.md) and [handoff](handoffs/week-06.md) preserve this
reasoning and the recorded type/build verification.

These two changes followed different paths under the trigger test in
[CLAUDE.md](CLAUDE.md): descriptive labels were an implementation fix;
changing assessment requirements required a proposed plan and my approval.
The size of a text edit did not determine its decision-making significance.

## Managing agents and durable records

Repeated full-course checks added cost and revisited known findings. I limited
automatic content review to the target week and its immediate neighbours;
a wider review requires my approval. Build and type checks remain separate.
This rule is implemented in [CLAUDE.md](CLAUDE.md), but I have no timing data
that would establish a quantified efficiency gain.

I also reported that clearing CC's context between weeks could lose decisions,
while Codex handled cross-week tasks. A missing numbered-activity requirement
prompted a split between durable authoring rules in CLAUDE.md and short
week-specific [handoffs](handoffs/TEMPLATE.md). Those files now exist, but
their existence alone does not demonstrate successful cross-session recovery.

The asset audit in this conversation exposed the same limitation in another
form: [MANIFEST.md](MANIFEST.md) still said the Week 1 workshop was NOT STARTED,
although an anchor, prompts, settings and Take A existed and the clip was
embedded in the page. QA failures were recorded elsewhere. The agent first
repeated the manifest's status, then checked files, technical metadata and
hashes and corrected it to BLOCKED. After my approved scope reduction, it
became INTEGRATED for the written-note exercise. The revision history keeps
both transitions. This establishes a missed synchronization step; it does
not identify which earlier session or agent caused it.

## Producing evidence instead of hypothetical examples

For Week 9 I supplied Jimeng footage; Codex generated a phone insert and
assembled five shots into a 31.233333-second sequence. An attempted Sora
shot 3 was blocked by generation review and was not claimed as delivered.
A real continuity problem replaced the hypothetical example: the opening
of shot 4 showed a dark phone after the preceding lit-screen shot. A first
0.6-second trim still entered on darkness; a 1.3-second trim was checked
against the new entry frame. Originals were preserved, and accepted rough-cut
differences remained explicit in the [continuity log](resources/week-09/continuity-log-v1.md)
and [materials record](resources/week-09/materials.md).

For Week 10 I requested a second cut and approved its teaching use. Cut A
retains the assembly; Cut B shortens only shot 3's reaction from about six
to two seconds, reducing the sequence from about 31.23 to 27.27 seconds.
The [comparison](resources/week-10/comparison.md) and
[verification](resources/week-10/verification.json) record the controlled
picture change. Audio follows the trim, so this is not an experiment that
isolates sound. Neither example establishes audience response or learning
improvement. Their handoffs record successful mechanical checks, which
verify integration rather than emotional effect.

## Verification and remaining limits

The project now contains real teaching media; the old claim that no production
assets exist is obsolete. My separate personal-film checklist was paused and
removed, as recorded in MANIFEST.md; teaching examples are not evidence of
my own completed film. Kitchen production approval and independent listening
or audience review remain limited where the asset records say so.

[Working notes](PROCESS-REFLECTION-NOTES.md) preserve the original observations
and suggestions. [Reflection draft](REFLECTION.md) develops the lessons from
them. Neither substitutes for a learner trial, a full authorized content
review, or final evidence review before submission.
