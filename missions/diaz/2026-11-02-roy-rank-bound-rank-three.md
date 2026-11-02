# Roy's rank bound cannot exclude u⁴ at rank at most three
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — none: no Lean and no platform nodes; mirror `f5b4d6c`
- **Date** — 2026-11-02

At a Diaz candidate u, a matrix with entries in the conjugation hull of
a number z that broke Roy's rank bound (1992, Cor. 1) would prove that
z is not in ℒ̃. The rank-one case, the strong six exponentials
theorem, stops at u³. The natural next question was whether larger
matrices reach u⁴. A scoping study of 23 October had found no failure
in small graded windows, left the step to non-graded matrices open, and
guessed that a full search would take days.

## What was shown

- **A reduction.** If a matrix over a monomial space breaks the bound,
  so does a graded stable one of no larger size and rank. The limit is
  taken in the moduli space of semistable Kronecker modules, because
  degenerating the matrix itself can create zero blocks.
- **Rank at most three.** No matrix over the model of the hull of u⁴
  breaks the bound, for any size, graded or not. The same holds for the
  hull of u⁴ + cu³, although its initial space does carry one explicit
  5 × 8 failure, which does not lift.
- **Free entries.** No failure at structural rank at most three.
- **The search was cheap.** The full graded rank-three search takes
  about 4 minutes, not days.

## How it was checked

- Each part was rederived by one referee agent, and the finished note
  by another who saw only the note. They found no error in a theorem.
  Two slips in an example were corrected, and citations were checked on
  the page. One citation, to Draisma 2006, was wrong and was withdrawn.
- The graded case at rank three has a SAT run over the whole proved
  range, under two solvers, and separate exhaustive enumerations.

## What is not proved

- **Nothing here is formal.** No Lean, and the library stays at 618.
- **Rank four is open**, and so is the generic model with actual
  logarithms. Results with free entries concern formal rank only.
- **One input is second-hand:** the good-quotient property from GIT was
  checked only through later papers.
- **The rank-three and hull theorems are computer-assisted.**
- **No novelty is claimed.** The statements were not found in the
  sources read. Those omit Roy 1989, Roy 1990 and Atkinson–Lloyd, and
  the reduction assembles standard parts.

## What remains open

Diaz's conjecture. This is a barrier on one method, not progress on the
conjecture: at rank at most three, Roy's bound cannot exclude u⁴ through
its own hull. Proofs and scripts: `tex/diaz-roy-rank-three.tex` and
`scripts/roy_rank/` in the mirror.
