# Process overview

## What I built

I built “Directing for the Screen” (SLOP4555), a twelve-week course using AI
cast and crew to practise directing. My idea of a good course was one
coherent subject developed through teaching, practice and assessment:
students should learn to justify directing decisions, with generation
providing material they can evaluate
([`9331148`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/9331148)).

## How I got here

### Encoding course promises

I translated measurable requirements into `spec/` checks for twelve-week
coverage, assessment totals and deck availability
([`ed160b1`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/ed160b1)).
The stronger teaching promise needed interpretation, so I encoded teach →
practise → assess in `CLAUDE.md` and used a read-only curriculum reviewer
to challenge the connections. Its findings included storyboarding being
assessed before it was taught. But it also treated workshop tool operation
as knowledge missing from lectures. I rejected that interpretation and
clarified the instruction: directing concepts belong in lectures; tool
mechanics can be introduced in workshops. This preserved the course's
purpose while correcting the ambiguity that produced the false alarm
([`9331148`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/9331148)).

### Defining agent authority

After curriculum fixes were applied without a plan, I adapted the
planning-and-approval rule from Assignment 1. Routine edits could proceed;
changes to teaching or assessment needed my decision. I also required real
production artefacts for demonstrations. These rules changed what I would
accept from an agent: plausible prose and an apparently helpful redesign
could still violate the task
([`9331148`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/9331148)).

### Judging actual usefulness

I deliberately left usefulness and cinematic judgement outside automated
pass/fail checks. Reading Week 3, I understood the finished screenplay but
could not begin writing one. I requested a worksheet connecting premise,
observable beats and screenplay form, then checked that lecture, workshop
and slides agreed on its use. That gave me a concrete acceptance criterion;
no learner trial has established its effectiveness
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).

### Preserving context across agents

Keeping these standards available across sessions became a practical
problem. I cleared Claude Code's context when starting a new week and
used Codex for cross-week work. This kept tasks focused, but neither agent
automatically inherited the other's conversation. When Week 3 lost the
required numbered activities, I moved the shared authoring rule into
`CLAUDE.md`. Weekly handoffs reference standing rules and preserve local
state, avoiding duplicated instructions that could drift apart
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).

### Making handoffs actionable

I specified when and how to hand over: update the record when finishing a
week, transferring work or clearing context. Each short handoff separates
confirmed decisions from proposals, names the next action and first files
to read, records neighbouring dependencies and known concurrent edits,
and states what verification covered. Incoming sessions read the rules and
relevant handoff, then inspect current files. An outdated manifest had
already caused an agent to repeat the wrong asset status, so discrepancies
must be surfaced. A handoff cannot guarantee that concurrent edits are
safe or that recorded status remains current
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).

### Controlling review scope and acknowledging limits

Repeated full-course reviews exposed another context cost: agents revisited
known findings and expanded small tasks. I limited routine content review
to the target week and its immediate neighbours, required reuse of
relevant findings, and reserved wider reviews for explicit approval.
Routine build and type checks remain separate. This trades review coverage
for focus; distant dependencies can still be missed. I have not measured
efficiency gains or demonstrated reliable recovery after handoff. Likewise,
the large catch-up commit records completed work but weakens evidence of
its sequence. These limits matter when carrying the workflow into another
project
([`38a8340`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-xuwancheng62-lab/commit/38a8340)).

The two reflection answers are in [Assignment 2 reflection](reflections/assignment2.md).
