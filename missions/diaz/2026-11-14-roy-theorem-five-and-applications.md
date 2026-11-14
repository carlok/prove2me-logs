# Roy's Theorem 5 and printed applications of his rank bound
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-14

The day before, Roy's Corollary 1 (a lower bound for the rank of a
matrix of logarithms) was proved with no hypothesis. This round builds
on it. It proves Roy's Theorem 5, which bounds how many linearly
independent vectors with logarithmic coordinates a subspace can hold,
and the printed results that rest on the two: from Waldschmidt's
*Variations* and *Further variations on the six exponentials theorem*,
from §12.3 of his book DALAG, and Fischler's bound for the centraliser
of a matrix of logarithms. Twenty-nine nodes, all with no hypothesis.

## What was proved

- **Roy 1992, Th. 5** (and DALAG Cor. 11.15 for Q̄ and ℒ̃): if a
  subspace U of ℂᵈ contains no non-zero algebraic vector and no proper
  rational subspace contains it, a Q̄-free family in U ∩ ℒ̃ᵈ has at
  most Σ nᵢdᵢ/(dᵢ − nᵢ) members, for some splitting of (dim U, d).
- **Variations:** Th. 3.1 (the bound d(d − 1) for a hyperplane),
  Th. 2.11, Cor. 2.12 as the author corrected it, a corrected
  Cor. 2.13, Cor. 2.14 and Cor. 3.2.
- **Further variations:** Th. 2.1 for finite-dimensional Y, and its
  main result Th. 1.2: for a 2 × 3 matrix over ℒ̃ whose rows and
  columns satisfy the stated freeness, one of the three 2 × 2 minors
  is outside ℒ̃. Also the Λ² example and Cor. 1.4.
- **DALAG §12.3:** Cor. 12.21, Cor. 12.22 (rank at least half the
  structural rank) and Cor. 12.24.
- **Fischler 2001, Th. 1.2:** if the n² entries of a matrix over ℒ̃
  are free over Q̄, its centraliser has dimension at most (n² + 1)/2,
  with Rémond's lemma on commuting subspaces of matrices.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.roy_theorem_five` | `79c50e32-fba2-4621-b5fb-b8e6e3aca4b4` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fv_theorem_1_2` | `819773b1-4ee7-43bc-a05b-20927db562ed` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_centralizer` | `b2d55de6-bd48-4a32-8e71-1ceadd420026` | SKETCH_ACCEPTED, now Proved |

Milestones 186–202 are the seventeen printed results; the other
twelve nodes joined by import. All 29 are Proved: thirteen were
accepted outright, and sixteen were sketches that upgraded when their
children closed. The proofs have 2,618 lines.

## How

- Roy's own proof of Th. 5 is used: one application of Th. 4 at a
  minimising rational quotient, then induction on the kernel. The
  minimality alone shows that the kernel configuration again has full
  rational hull, so no lemma on smallest rational subspaces is needed.
- Further variations Th. 2.1 takes one subspace of maximal slope and
  applies Roy's Corollary 1 once, to a Gram matrix; the printed
  route through a pair reduction is longer.
- Rémond's lemma is proved by induction on the dimension through an
  eigenspace, with the equality case split three ways.
- Paper proofs were written first, each round checked by an
  independent referee, and the statements frozen before any Lean. A
  chain with no stubs, against the mirror's library on Mathlib
  v4.35.0, builds on Lean's three axioms.
- The agents worked under a clean-room rule: no agent opened another
  formalisation of these results.

## Printed statements corrected

Formalising met three printed statements that are false as stated.
Each is listed, with the printed passage and the repair, in
`ERRATA.md` of the mirror.

- **Variations Cor. 2.12.** Λ₂₁ ≠ 0 with Λ₁₁/Λ₂₁ transcendental does
  not exclude a relation among 1, Λ₁₁, Λ₂₁. The author corrected it in
  Further variations §4 and in The role of complex conjugation.
- **Variations Cor. 2.13,** for the same reason. Counterexample:
  Λ₁₁ = 1, Λ₁₂ = Λ₁₃ = 0, Λ₂₁ = log 2, Λ₂₂ = Log(2 + i),
  Λ₂₃ = Log(3 + 2i). No correction was found in the sources read.
  Its proof also needs signs on two columns when one of Λ₁₁, Λ₂₁ is
  real and the other purely imaginary. The corrected form is proved.
- **DALAG Lemma 11.24:** the conclusion κ′ = 0 fails in 𝔾ₘ³. The
  formal proofs do not use the lemma.

Smaller points: DALAG's deduction of Cor. 12.24 from Cor. 12.22 gives
only rank ≥ 1 for 2 × 3 matrices (Cor. 12.24 itself is true and proved
here another way); gaps in DALAG's proofs of Cor. 11.10/11.15 and
Th. 11.21; and some slips in citations and indices.

## What is not proved

- **Nothing here is claimed as new.** These are formal proofs of
  classical results, with corrections where the printed statement
  needed one.
- **Further variations Th. 2.1 for infinite-dimensional Y.** The
  printed statement allows it; the printed proof, and this one, do not
  cover it.
- **Roy's φ in closed form.** Th. 5 is proved with "some splitting"
  in place of the maximum φ; DALAG's table Ψ needs Roy's lemma on
  p. 40, which is not formalised.
- **Not formalised:** DALAG Cor. 12.23 and the ℚ + ℒ statement after
  Cor. 12.24; Further variations Cor. 1.3; Fischler's Th. 1.1 and his
  results on orbits of algebraic groups.

## What remains open

Diaz's conjecture itself. None of these results excludes a new
candidate; they enlarge the stock of rank bounds the library can use.
