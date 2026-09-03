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

Nothing about the starter is recorded here. The platform under you is fixed and
documented in `README.md`, and the
[course website](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/)
publishes this deliverable's brief and spec. Read both before you plan or build;
what the agent needs to carry from either is your call.
