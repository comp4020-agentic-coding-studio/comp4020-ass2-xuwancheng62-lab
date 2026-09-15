# Your harness

## Course image API credentials

For image API generation or credential-loading issues, read
`.claude/skills/course-image-api/SKILL.md`. The course key is already configured
in the repository-root `.env` as `COMP4020_IMAGE_KEY`; the existing image
wrapper requires explicitly loading that file with `node --env-file=.env`.
Check presence without printing the value before asking the owner for a key.

## Curriculum review

`.claude/agents/curriculum-reviewer.md` is a read-only subagent that checks
the 12-week curriculum for coherence and constructive alignment (lecture ↔
activity ↔ assessment, learning outcomes actually taught and assessed). It
never edits anything — it only returns a report.

**Any project-wide content consistency review needs my explicit approval
first, however it's done** — through this subagent, or by directly reading
across many weeks' files myself. "Project-wide" means anything wider than
the target week plus its immediate neighbours (below). This governs
*content* consistency — whether the curriculum still coheres end to end —
and is separate from routine build/type checks (`pnpm typecheck`,
`pnpm build`, and the a11y/link/deck checks they run): those check that the
site builds and renders correctly, not that content is mutually
consistent, and stay free to run any time, on any files, without asking.

Preparing to ship, or suspecting a review is overdue, does not by itself
authorize one — "before shipping" is a reason to *ask* for a review, not a
standing green light to run one unasked. Wanting to run a full pass is
itself a change that needs approval, like any other.

During normal per-week iteration, an automatic consistency check needs no
approval but is scoped to the week being worked on plus its immediately
preceding and immediately following week only — nothing further out (e.g.
editing week 6 may also look at weeks 5 and 7, never week 2 or week 9). If
that check turns up something that looks like an issue beyond those
neighbours, record it — in the week's handoff, under open questions — and
stop there; chasing it further needs the same explicit approval as any
other project-wide review, regardless of how minor it looks.

Before repeating any check, subagent or direct, look for whether it's
already been done and recorded (a handoff's "This week's status", a
`PLAN.md`/`MANIFEST.md` revision entry) and reuse that finding. Only
re-run a check when something changed since it was recorded that could
plausibly have invalidated it — not as a matter of routine.

Do not launch the curriculum-reviewer subagent — or relaunch it to refresh
a report already on file — without that same explicit approval. It runs
only when asked; never automatically, and never "just to be sure" after an
edit.

**Any curriculum change proposed on the back of a review — subagent or
direct — must be presented to me before it's applied.** A review can point
at a gap; deciding how to close it (add a week's practice, cut a learning
outcome, reweight an assessment) is mine to approve.

*(Revised 2026-09-11: the original "after any structural edit" clause was
being read as license to auto-launch a full 12-week review after
completing each individual week during the "Table for One" → "Before It
Stops" substitution. Narrowed so the subagent only runs on explicit
request; per-week edits are checked locally instead.)*

*(Revised 2026-09-12: generalized from "the subagent" to any project-wide
content review by any method — a direct multi-week read-through needs the
same approval a subagent run does. Pinned automatic per-week checks to the
immediate neighbours only (previously "another specific week," with no
distance limit), added recording-not-chasing for anything found further
out, added reuse of prior findings instead of routine re-checking, and
separated all of this from routine build/type checks, which stay
unrestricted throughout.)*

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

## Workshop structure: explicit numbered activities

Every workshop (the site's `sessions` collection) writes its "In the
workshop" section as explicit numbered activities — `Activity 1`,
`Activity 2`, and so on — never as unnumbered named phases. Each activity
states:

- a title and its exact timing in minutes, e.g. `### Activity 3 — Scene
  change (10 min)`;
- an **Instructions** part — what students actually do;
- an **Expected output** part — the concrete artefact or result that
  activity should leave them with.

Every workshop's activities sum to a total of 120 minutes. A single
logical phase from `PLAN.md`'s Workshop template (e.g. the main exercise)
may be split across more than one numbered activity, as long as the total
still holds — this rule governs how a workshop's phases are *presented on
the page*, not what those phases are or a session's `spec:` completion
criteria, both of which stay defined in `PLAN.md` and the session's own
frontmatter.

*(Added 2026-09-12, generalizing a rule first applied only to
`03-screenplay-workshop.md` and recorded solely in `PLAN.md`. That
placement wasn't durable enough: the requirement had to be re-derived
mid-project because nothing in the project's own instructions said every
workshop must look like this, going forward. Moved here so it survives
independently of any one week's plan entry or conversation history — see
"Weekly handoff records" below for the matching fix to per-week
continuity.)*

## Weekly handoff records

Each week keeps a short handoff file at `handoffs/week-NN.md`, written to
the shared shape in `handoffs/TEMPLATE.md`. This mechanism is shared
infrastructure, usable the same way by Claude Code, Codex, or any other
agent working this repo — it has to hold up across a change of agent, not
just a change of session.

A handoff records what's specific to that week only: its confirmed
decisions (separated from anything only proposed), its next concrete
action and what to read first, which adjacent weeks it affects and why,
known concurrent work, current status, what hasn't been rechecked since
the last verification, and open questions — never a standing rule that
applies to every week. A standing rule belongs here in `CLAUDE.md`, or in
one of `PLAN.md`'s templates; a handoff links to it by name instead of
restating it, so the rule has exactly one place to go stale. Keep each
handoff concise — about a page — and point at `PLAN.md`/`MANIFEST.md` rows
for detail instead of duplicating them.

Update a week's handoff when finishing work on that week, handing it off
to another session or agent, or before a user-requested context reset —
whichever of those happens first, not only "at the very end."

Before starting work on any week: read this file (`CLAUDE.md`) in full and
that week's handoff, if one exists — then inspect the actual current state
of the files the handoff points at. A handoff is a record of what was true
when it was last updated, not a live source. If what's on disk disagrees
with what the handoff says, or the handoff looks stale, surface that
conflict rather than silently overwriting a confirmed decision with a new
one. And if what I've just said in this conversation conflicts with either
file, what I said wins — these files are the default when nothing more
specific has been said, not a standing override of my latest instruction.

*(Added 2026-09-12, after the numbered-activity requirement above had to
be rediscovered mid-project instead of read off a durable record. Standing
rules go in the project specification; week-specific status goes in the
handoff — see `handoffs/TEMPLATE.md`.)*

*(Revised 2026-09-12: made explicit this is shared cross-agent
infrastructure, not Claude-Code-specific. Named the update triggers —
finishing a week, handing off, a user-requested context reset — instead of
leaving "before starting work" as the only checkpoint. Required inspecting
current files and surfacing conflicts or staleness rather than trusting a
handoff as ground truth, and made explicit that my latest instruction in
conversation always outranks either file.)*

## Task-scoped reading

Read standing instructions (`CLAUDE.md` and applicable `AGENTS.md`
instructions), the target week's handoff, and only the relevant `PLAN.md`
sections first. For work without a target week, use the relevant project
handoff or planning section. Inspect the actual files needed for the task;
consult the matching `MANIFEST.md` rows and resource records when working
with assets. Use headings or targeted searches to locate decisions instead
of reading the entire plan by default.

Read `PLAN-ARCHIVE.md` only to resolve a specific historical question, such
as the reason for a decision, its approval, or a conflict between records.
Read the relevant archived section rather than the whole archive. Archived
instructions are historical evidence, not current authority; check the live
plan and the owner's latest instructions before applying them.

Consult immediate neighbouring weeks when needed for consistency, within
the scope allowed by "Curriculum review" above. Expand reading when a
dependency, conflicting record, or uncertainty requires it; task-scoped
reading must not omit applicable constraints. This does not authorise a
project-wide curriculum review. Do not require reading the entire plan or
archive for every task, and reuse standing instructions already read in the
current session unless they have changed or need clarification.

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
flips: routine work that follows the plan needs no entry at all in
`PLAN.md` — routine implementation status, validation results, and
wording fixes belong in the relevant week's `handoffs/week-NN.md` instead.
A genuine new planning decision, or an approved change to an already-
implemented plan, does belong in `PLAN.md`: its section gets updated in
place, plus one dated entry in a `## Revision history` section at the
bottom of `PLAN.md` naming the exact change. A single approval/change
record is enough — don't also create a second, permanent standalone
section for the same decision; the in-place update plus its one history
entry is the whole record. Periodic explicit archiving of that history —
and of completed implementation narratives or superseded proposals
elsewhere in the file — into a paired archive file (e.g. `PLAN-ARCHIVE.md`)
is allowed, provided the original text is preserved there, the current
decision stays discoverable in `PLAN.md` at its original heading, and a
pointer at that heading says where the historical material moved. Never
silently rewrite the plan to match a drift that already happened — that's
the same rule as above, just spelled out for how the file itself should
read.

*(Added 2026-09-04, after a `PLAN.md` update that recorded ten approved
decisions as a dated ledger plus inline "Resolved 2026-09-04" patches
scattered through every section — reads as a changelog, not a plan, and had
to be rewritten clean.)*

*(Revised 2026-09-13: separated routine status/validation/wording, which
now belongs in the week's handoff, from genuine planning decisions, which
still belong in `PLAN.md`; replaced the implicit dual-record pattern
(section update plus permanent standalone section plus history entry) with
a single approval/change record; and made explicit that periodic archiving
into a paired file like `PLAN-ARCHIVE.md` is allowed as long as original
text is preserved, current decisions stay discoverable at their original
heading, and a pointer names where history moved. Prompted by a
documentation split that moved completed narratives out of `PLAN.md` into
`PLAN-ARCHIVE.md` — see `PLAN.md`'s "Documentation reorganisation —
approved".)*

Nothing about the starter is recorded here. The platform under you is fixed and
documented in `README.md`, and the
[course website](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/)
publishes this deliverable's brief and spec. Read both before you plan or build;
what the agent needs to carry from either is your call.
