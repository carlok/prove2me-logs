# Baker's theorem as a hypothesis, discharged
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-02

Three of the mission's results had been proved with Baker's theorem as an
explicit hypothesis, because no proof of Baker's theorem was available.
Baker's theorem was proved in the mission earlier the same day, so each of
them now has an unconditional form, and the companion note's four rows
marked "Proved, assuming Baker" become plain "Proved".

## What was proved

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.no_algebraic_generalized_line_unconditional` | `13fcac6a-e039-453b-a9d8-9991dee320aa` | accepted |
| `DiazModulus.candidate_one_log_saturation_unconditional` | `b6fa5e39-dced-4c6f-94af-c88e74976fe1` | accepted |
| `DiazModulus.no_first_order_arithmetic_operator_unconditional` | `269d8402-b48a-4e0d-a58e-5aabc60e7293` | sketch, now Proved |
| `DiazModulus.candidate_qbar_independent_one_u_conj` | `3752afd3-faa1-4ba9-a355-bd1b0ed1754c` | accepted |

The first three are their parent nodes without the hypothesis: no
logarithm off the axes lies on an algebraic generalized line; a candidate
that is an algebraic affine function of a logarithm is a rational multiple
of it, and no candidate is a + bπ; and the exponential system of a
candidate has no first-order arithmetic differential operator. The fourth
is the one piece with content of its own: for a candidate u, the numbers
1, u and ū are linearly independent over the algebraic numbers, which is
Baker's theorem at a candidate.

## How

Two of the proofs are a single application of the parent node to
`DiazModulus.baker_two_logs`, the two-logarithm form of Baker's theorem
proved in the mission, and, for the saturation result, to the proof of
Hermite–Lindemann. The fourth node shows that u and ū are linearly
independent over ℚ, since su + tū = 0 gives (s + t) Re u = 0 and (s − t)
Im u = 0 and a candidate lies on neither axis; it then applies Baker's
theorem with a constant term to the linear form −(pu + qū) + pu + qū = 0.
The third node passes that result to its parent.

## What is not proved

- Nothing new mathematically: each statement is its parent's, and the
  fourth is an instance of Baker's theorem.
- The case of Waldschmidt's question on p. 399 of his book still carries
  Baker's theorem, beside Roy's strong six exponentials theorem, which is
  not proved here.
- Like every statement about a candidate, these are vacuous if Diaz's
  conjecture holds.

## Membership

Checking the batch showed that the three parent nodes, although Proved and
cited in the note's appendix, had never been members of the mission. The
three new unconditional nodes became milestones 100 to 102; their accepted
proofs import the parents, and the parents joined the mission by import.
The mission now has 244 members.

## What remains open

Roy's strong six exponentials theorem is still a hypothesis wherever it is
used. The mission's two open leaves, the real half of (S) and (NT), are
unchanged.
