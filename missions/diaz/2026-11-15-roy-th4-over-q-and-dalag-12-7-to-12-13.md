# Roy's Th. 4 over ℚ, and DALAG Prop. 12.7 to 12.13
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-15

Two rounds, prepared overnight and published in the morning. The
first finishes the ℚ case of the previous round: Roy's Th. 4 over ℚ
in its minimal-ratio form, and DALAG Prop. 11.19 for (ℚ, ℚ + ℒ) as
printed. The second proves three propositions of DALAG §12.1 that two
earlier errata items concern. Six nodes, all with no hypothesis.

## What was proved

- **Roy 1992, Th. 4 over ℚ:** for ℚ-free points of U ∩ (ℚ + ℒ)ᵈ and a
  rational T ≠ ℂᵈ with n′/d′ minimal, ℓ′/(d′ + ℓ′) ≤ n′/d′ ≤ n/d.
- **DALAG Prop. 11.19 for (ℚ, ℚ + ℒ):** with dim U < d, the quotient
  of U ∩ (ℚ + ℒ)ᵈ by its part in T is finite-dimensional over ℚ, and
  its dimension obeys the same bound.
- **DALAG Prop. 12.7:** under Property (A B; C 0), a K-subspace V of
  Kᵈ of dimension n that meets kᵈ only in 0 has dim_k(V ∩ Eᵈ) at most
  n(n + 1)/2.
- **DALAG Prop. 12.10:** every polynomial over a commutative ring is
  the determinant of a square matrix A₀ + X₁A₁ + ⋯ + XₙAₙ.
- **DALAG Prop. 12.13, (iv) ⇒ (iii):** if rank equals structural rank
  for matrices over E, no non-zero homogeneous polynomial vanishes at
  k-free elements of E.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.dalag_prop_11_19_rat` | `0b0a281f-2360-472a-bdba-515dc955a3a5` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_prop_12_7` | `232c6298-bc4f-4efd-8e7b-670c9819d124` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_prop_12_10` | `baf27df3-789e-4812-b4e0-2e878716cd89` | ACCEPTED |
| `DiazModulus.dalag_prop_12_13_iv_iii` | `ccacc02a-79bf-4488-8f80-78279cb7920b` | SKETCH_ACCEPTED, now Proved |

Milestones 210–213 are the four rows; the other two nodes joined by
import. All 6 are Proved: 3 were accepted outright and 3 were sketches
that upgraded when their children closed. The proofs have 1,009
lines.

## How

- Th. 4 over ℚ comes from the slope bound of the previous round, by
  the same projection along a minimising subspace as over Q̄.
- Prop. 11.19 lifts a ℚ-basis of the quotient into U and applies
  Th. 4 at T.
- Prop. 12.7 is an induction on d; its step builds V₁ as a K-subspace
  from P·V, as the printed proof needs but does not say.
- Prop. 12.13 (iv) ⇒ (iii) applies (iv) to x₀M, whose entries lie in
  E, with Prop. 12.10 and the dehomogenisation of Lemma 12.9.
- Each design was checked by an independent referee, who also wrote
  trial proofs; the statements were frozen, then proved against stubs.
  A chain with no stubs, against the mirror's library on Mathlib
  v4.35.0, builds on Lean's three axioms.

## Printed statements corrected

- **Roy 1992, Remark (i), p. 37:** Th. 4 over a subfield F of Q̄ is
  said to follow "with the same substitutions", but Roy's Theorem 1 is
  quoted over Q̄ only. A short reduction to the Q̄ case fills the gap.
- **DALAG, Remark on p. 424:** Property (A B; C 0) is carried along a
  k-linear isomorphism, which does not preserve it: ℚ + ℚ√2 is ℚ-
  isomorphic to ℚX + ℚY but lacks the Property. The statement of the
  Remark is correct, by dehomogenisation.
- **Two slips:** an index on p. 423, and a block count in the proof of
  Lemma 12.11.

The full list is `ERRATA.md` in the mirror.

## What is not proved

- **Nothing here is claimed as new.** These are formal proofs of
  classical results.
- **The other implications of DALAG Prop. 12.13,** Cor. 12.14,
  Prop. 12.2, 12.5 and 12.6.
- **Roy's Th. 4 over other subfields F of Q̄:** only F = ℚ and F = Q̄
  are formalised; the p-adic case is not.

## What remains open

Diaz's conjecture itself; these results enlarge the stock of rank
bounds in the library and exclude no new candidate.
