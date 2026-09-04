# Your harness

## Curriculum review

`.claude/agents/curriculum-reviewer.md` is a read-only subagent that checks
the 12-week curriculum for coherence and constructive alignment (lecture ↔
activity ↔ assessment, learning outcomes actually taught and assessed). It
never edits anything — it only returns a report. Invoke it once a full
12-week skeleton exists, after any structural edit, or before shipping; not
against a half-built skeleton.

**Any curriculum change proposed on the back of its report must be presented
to me before it's applied.** The subagent can point at a gap; deciding how
to close it (add a week's practice, cut a learning outcome, reweight an
assessment) is mine to approve.

## Curriculum structure: teach → practise → assess

A standing structural rule, checked alongside constructive alignment. It
draws one boundary that matters: **disciplinary knowledge** (directing
concepts, methods, vocabulary, cinematic principles, directorial judgement)
must be lecture-taught before a workshop practises it; **tool mechanics**
(how to operate whatever's needed to perform that week's exercise — image-
to-video controls, a timeline, layering audio) are not subject to that
sequencing and may be taught in the workshop itself.

- Lectures teach and model disciplinary knowledge: directing concepts,
  methods, vocabulary, cinematic principles, and ways of making directorial
  judgements.
- Workshops (the site's `sessions` collection — see `sessionLabels` in
  `src/site-config.ts`) may teach the operational mechanics of the tools
  needed for that week's exercise. They then use those tools to practise,
  apply, and develop the disciplinary knowledge already taught/modelled in
  the corresponding or earlier lecture.
- Workshops must not introduce required *directing/filmmaking concepts*
  that have never been taught or modelled in a lecture. Tool mechanics are
  exempt from this — teaching them for the first time in a workshop is
  intentional, not a violation.
- Assessments require students to independently integrate disciplinary
  knowledge and practical/tool skills they've already encountered through
  lectures and workshops.

*(Added 2026-09-04, formalizing agreement on lecture/workshop/assessment
sequencing. Clarified same day, after a curriculum-reviewer pass flagged
week 9's clip assembly and the absence of tool-mechanics lecture content as
possible violations, to make explicit that tool mechanics were always meant
to be a workshop's job, not a lecture's — the earlier wording didn't say so
and read as if it barred both.)*

## Real production material, never invented

The lectures describe real operational demonstrations (a directed take, a
bible entry, a cut, a sound pass). Every one of these must actually be
carried out and produce a real image/video/audio/production-process
artefact — never an invented, simulated, or merely plausible-looking
stand-in presented as if it were real. If asked to produce or fake one of
these directly, decline and say why; the fix is to actually perform the
demonstration, or to leave that checklist row `required — not started`
until someone does. This applies regardless of how good the fabricated
version would look — a convincing fake is a worse outcome here than an
honest gap.

*(Added 2026-09-04, formalizing a decision made about "Table for One" and
the week-by-week asset checklist in `PLAN.md`.)*

## Planning and human–agent decision making

**The trigger test.** Write `PLAN.md` (or update it) before implementing if
the change would:

- add, remove, or restructure a week's lecture, session, or assessment;
- change what any week teaches or assesses — a learning outcome, a spec
  line (a session's or assessment's `spec:` frontmatter bullets — not the
  `spec/*.test.ts` directory, a different thing with the same name), a
  marking criterion;
- change the running example (the story, its characters, or how it's used
  across weeks);
- change an assessment's weighting, due date, or what it asks for;
- add, remove, or restructure a site page or navigation entry.

Anything else — wording, fixing a broken link, formatting — is
implementation detail. **If you can't tell which side a change falls on,
it's a planning decision.**

Then: name the problem, the proposed approach, and the assumptions or
ambiguities in `PLAN.md` before touching content. Once I approve it, it's
frozen — don't silently rewrite it to match what got built; if the work
needs to depart from the plan, stop and say so, and I'll decide whether to
accept the departure or amend the plan deliberately. This rule outranks any
default that biases toward pressing on without asking — on a trigger-test
change, stopping is correct, not a failure to be helpful.

*(Added 2026-09-03, adapted from `comp4020-ass1-xuwancheng62-lab`'s
`CLAUDE.md`, after the curriculum-reviewer's four confirmed fixes got
applied to this repo with no `PLAN.md` in place at all.)*

**How `PLAN.md` itself gets written depends on whether implementation has
started.** While still planning, write each approved decision directly into
the relevant section as plain fact — rewrite or delete a superseded
proposal rather than leaving it beside its replacement, and don't scatter
dated "resolved on this date" markers through the prose. Once
implementation of what the plan describes has actually started, that
flips: routine work that follows the plan needs no entry, but an approved
departure gets its section updated in place *and* a dated entry appended to
a `## Revision history` section at the bottom of `PLAN.md` naming the exact
change. Never silently rewrite the plan to match a drift that already
happened — that's the same rule as above, just spelled out for how the file
itself should read.

*(Added 2026-09-04, after a `PLAN.md` update that recorded ten approved
decisions as a dated ledger plus inline "Resolved 2026-09-04" patches
scattered through every section — reads as a changelog, not a plan, and had
to be rewritten clean.)*

Nothing about the starter is recorded here. The platform under you is fixed and
documented in `README.md`, and the
[course website](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/)
publishes this deliverable's brief and spec. Read both before you plan or build;
what the agent needs to carry from either is your call.
