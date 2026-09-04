# Process overview

Written by you, for a reader: how you got from the brief to the harness and
agentic workflow behind this submission. Markers read this file and follow its
citations; they don't trawl the repo for evidence you didn't point at.

This file is the shape; the course site's
[assessment page](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/topics/assessment/#what-you-submit)
is the requirement, and its
[word counts](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/topics/assessment/#word-counts)
cover every deliverable.

## What I built

**"Directing for the Screen" (SLOP4555)**, a 12-week directing practicum
where AI stands in for cast and crew, on top of the fixed `astro-theme-slop`
starter. The discipline being taught is directing — shot construction,
performance direction, editorial judgement, sound design — with generation
as the rehearsal medium, not the subject. One running example, "Table for
One," threads every week so the storyboard, bible and shot list built in
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
a further full pass — lectures, sessions, assessments, decks and the real
operational demonstrations together — is still owed once those real
production assets exist, per `PLAN.md`'s "Process" section.

What `PLAN.md` calls out as still genuinely open, and not something I
resolved by writing more curriculum prose instead: no real production
asset exists yet for any week's checklist row (`PLAN.md`'s "Table for One"
asset plan is explicit that the running example is teaching prose, not
production evidence, until the site owner actually directs, generates and
selects the real takes), and the reusable media component family that
would display those assets doesn't exist yet either — both deferred on
purpose rather than built against a guess at what the real footage will
need.

Screenshots are welcome where one carries the point better than a sentence does.
Commit the file to this repo and link it with a **relative** path, which is what
makes it render on GitHub: `![alt text](docs/before.png)`. Images don't count
towards the word count and don't replace the citation.

## Before you ship

`pnpm check:evidence` verifies that this comment is gone, that your citations
resolve to real commits, that a crit week's reflection entry is in
`reflections/`, and that your `CLAUDE.md` is there. It checks that your account
is traceable, not that it is good: that is the marker's call.

Images aren't checked: unlike a citation whose SHA doesn't resolve, a broken
image is visible the moment this file is rendered on GitHub.
