# The first cloud run

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-12

A cloud agent with a fresh machine, a Prove2Me key, a GitHub token and a public brief ran the
whole loop once: it proved a statement, published and submitted it, mirrored it into
`carlok/diaz-modulus-lean`, updated the companion note, and opened an issue as its report.

`DiazModulus.candidate_no_real_algebraic_line` is **Proved**:
<https://prove2.me/theorems/e561bb83-10d1-42d0-b2aa-1d5fb8d4a1d9>, submission
`02f87c60-27d0-4c05-ab14-a06fa9c7201a`, `ACCEPTED`. For a candidate `u = x + iy` there is no
relation `Ax + By = C` with `A, B, C` real algebraic and `(A, B) ≠ (0, 0)`, by
Hermite–Lindemann alone.

## Why this target

None of the twenty open Diaz nodes is closable in a session. A dozen are a case decomposition of
the root, one is equivalent to the root, one is a 1970s theorem blocked on a zero estimate nobody
has formalised. A brief that said "take an open node" would have produced a failed run with
nothing to learn from. So the brief named two statements already proved on paper in the note and
flagged there as unformalised, and pre-approved exactly those. The agent took the easier one,
which is the one the other rests on.

## What the review found

Everything load-bearing checked out when verified independently rather than read from the
report: node Proved with a clean citation, explanation attached, repository statement matching
the published one, axioms `propext`, `Classical.choice`, `Quot.sound`, CI green on that commit,
and every appendix row still matching the live board.

Three misses, none serious and all instructive:

- **A platform uuid in the body of the note.** The note keeps identifiers to its appendix.
  Taken out, and the publishing script now refuses any uuid.
- **"Vacuity" read as "are the hypotheses necessary".** The report showed the statement fails
  without the candidate hypothesis. The check the brief meant is whether the *conclusion* was
  already proved — a different question.
- **A redundancy by composition it did not notice.** The statement is the degree-one case of
  `DiazModulus.candidate_vanishing_ideal`, proved earlier the same day: a non-zero polynomial of
  degree at most one cannot be divisible by `X² + Y² − ρ`. That is not a reason to reject the
  node — its proof needs much less — but it is exactly the failure the briefs name, and the
  vacuity query cannot catch it. The brief now says so with this as the example.

## The operational lesson

The agent can only edit the published copy of the note, so the working copy falls behind by
exactly its hunks. Bring them back before the next sync, every time, or the next sync silently
reverts the agent's work.

The next run takes the other pre-approved statement: `|u − a|` is transcendental for every
non-zero algebraic `a`, citing this node.
