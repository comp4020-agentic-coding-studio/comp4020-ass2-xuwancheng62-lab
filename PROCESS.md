# Process overview

## What I built

I built "Directing for the Screen" (SLOP4555), a twelve-week practicum where
AI stands in for cast and crew, but the discipline stays directing: shot
construction, performance direction, editorial judgement, sound. My spine
for a good course is coherence — one thesis, that students justify directing
decisions while generation supplies material to evaluate, carried from
lecture to workshop to assessment. I encoded that as teach → practise →
assess in `CLAUDE.md`, then used a read-only curriculum-reviewer subagent to
test my own twelve-week skeleton against it
([`9331148`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/9331148)).

## What became a rule, and what I left out

"Real production material, never invented" became a `CLAUDE.md` rule once I
judged that a fabricated directed take would look convincing and still be
worthless as evidence of the technique it claims to demonstrate. Assessment
wording became a deliberate spec change, not a quiet edit, after I found
Assignment 1's "resolve every decision" language outran what week 5 actually
teaches — marking a decision pending, with the work needed to close it, is
the taught skill
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).
I deliberately left cinematic judgement and real usefulness outside
automated checks: week 3's screenplay-form worksheet and week 1's narrowed
workshop — diagnosing an existing take rather than generating a fresh one —
exist because reading the course as a student would surfaced problems no
spec line catches. Neither has been tried by an actual learner.

## Testing technique against real practice, not invented method

Before writing week 4 I compiled `RESEARCH.md` from seven directing programs
and five named methodologies, so the lecture teaches Mamet's "shot as
argument," cited to *On Directing Film*, rather than a plausible-sounding
technique I invented to fill a slot
([`7054ea7`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/7054ea7)).
The same instinct closed two judgement calls I'd left open. Montage, taught
but never rehearsed, became a real recut-lab requirement. The single-scene
running example stayed as it was once I re-read Assignment 1's actual
marking rubric and found it grades runtime justification, never scene count
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).

## Producing evidence, and admitting its limits

Week 9's continuity fix — a 0.6s trim, then a checked 1.3s one, against a
real dark-to-lit cut — and week 10's two cuts (a 31.2s assembly against a
27.3s reaction-trimmed one) are real edits with real logs, not hypothetical
teaching examples. Neither proves an audience would notice the difference
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).
A large amount of already-verified work also sat uncommitted for too long
before one catch-up commit brought it in. That commit is honest about being
a catch-up, not evidence the work happened incrementally — letting real,
checked work sit that long is the failure worth naming, not just its
resolution.

## What this changed

Directing this course changed what I'd accept back from an agent: a green
build and valid links answer a different question than "can a student act
on this," or "is this a fair ask." So I built explicit decision boundaries —
wording and links proceed on their own; anything that changes what's taught
or assessed needs my approval first — and started treating verified,
uncommitted work as a debt to close immediately, not a task to reconstruct
from memory later.
