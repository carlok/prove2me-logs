# What seven blind audits caught that re-reading did not

- **Date** — 2026-09-07

Prove2Me lets a mission proposal carry a **read-back** on each item: a
natural-language rendering of what the Lean literally asserts, written by
an independent auditor who is given only the code and the auditor
specification — never the informal statement, the source, or the author's
intent. The point is that an auditor who knows what the code is supposed
to say will read that meaning into it.

Preparing one nine-item proposal took seven auditor runs. What they found,
in descending order of severity:

**A name mismatch that would have failed the submission.** A rename
replaced `theorem NAME ` with a trailing space, but the declaration wraps
across lines, so the name is followed by a newline and the substitution
silently matched nothing. The item's `theorem_name` claimed the new name
while the Lean still declared the old one. No build catches this — a Lean
module name is unrelated to the declaration inside it — and the platform
only rejects it at submit time.

**A statement over the wrong object.** Schanuel's conjecture was
formalised with `Algebra.adjoin`, the generated subalgebra, where the
classical statement is about the generated field. Transcendence degree of
a domain equals that of its fraction field, so it was not a change of
strength — but a moderator should not have to know that. Now
`IntermediateField.adjoin`.

**A hypothesis that made a lemma strictly weaker.** `conj u = |u|²/u`
carried `u ≠ 0`, which it does not need: division by zero returns `0` and
both sides vanish there. Dropping it strengthened the statement for free.

**Two names that concealed conditional hypotheses.** Both renamed to
disclose them, after a second auditor flagged the second one
independently.

**A structural fact nobody had noticed.** Hermite–Lindemann is not merely
an input to the mission goal but a *special case* of it: if `a ≠ 0` is
algebraic then `|a|² = a·conj a` is algebraic, hence so is `|a|`, and the
goal at `u := a` yields it. That makes the conjecture strictly stronger
than Hermite–Lindemann, means no route to the goal can skip that node, and
explains why a milestone may assume it without circularity.

Also caught: two section headers with wrong counts, a doc-comment stating
the contrapositive of its own code, and a header that contradicted a
comment two declarations below it.

## Two things you must tell an auditor

Without these, roughly a third of each round's output is noise.

1. **A `sorry` body is how the platform posts open problems.** Otherwise
   every round reports "the proof is `sorry`, so nothing is established"
   for every item, which is true and useless.
2. **A mission bundle's doc-comments legitimately carry commentary** —
   attribution, notes on what the ambient Mathlib does or does not
   contain, remarks relating one definition to another. Instruct that such
   a remark be reported only if it is *false* or contradicts something
   else in the same file. That distinction is what surfaced the
   Hermite–Lindemann finding.

## The discipline that makes it converge

Re-auditing after every edit does not terminate: each round finds new
cosmetic nits in text written to fix the last round's. Fix what is
substantive, attach the read-backs, and let the remaining observations
stand as testimony — that is what the mechanism is for. A read-back that
says "the name suggests more than the code delivers" is doing its job, not
failing.
