# Roy's rank bound for matrices of logarithms, with no hypothesis
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-13

Roy 1992, Cor. 1 bounds from below the rank of a matrix whose entries
are linear combinations, with algebraic coefficients, of 1 and
logarithms of algebraic numbers: the rank is at least dθ/(1 + θ), θ a
structural quantity read off the zero blocks the matrix can be brought
to by algebraic row and column operations. Roy's strong six
exponentials theorem is its 2 × 3 case, proved with no hypothesis on
30 October. This round proves the general d × l statement, and Roy's
Theorem 4 with it, on the same footing.

## What was proved

- **Roy's Corollary 1.** A d × l matrix M with entries in ℒ̃,
  d ≥ 1, has invertible algebraic P and Q, and 0 < d′ ≤ d, l′ ≤ l,
  such that the top right d′ × (l − l′) block of PMQ vanishes and
  d·l′ ≤ rank(M)·(d′ + l′). With no hypothesis.
- **Roy's Theorem 4,** for Q̄ and ℒ̃, in the form of DALAG Prop.
  11.19: at a rational subspace S minimising
  (n − dim(U ∩ S))/(d − dim S), the image of the data in ℂᵈ/S
  satisfies ℓ′d′ ≤ n′(d′ + ℓ′), and n′/d′ ≤ n/d.
- **On the way:** lifts through Roy's map Υ, its dimension counts
  (DALAG Lemma 11.18), the image of an integer kernel, the rank of
  the relations returned by the linear subgroup theorem, a space of
  periods, and coordinates adapted to a rational subspace.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.roy_rank_bound` | `f6b34940-416d-40d8-be41-c0c7890e96a5` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.roy_theorem_four` | `7ba07b5d-f9b6-420a-8d92-fa5e712f7de8` | SKETCH_ACCEPTED, now Proved |

Milestone 185 is the first row; the other nine nodes joined by
import. All ten are Proved: six leaves were accepted outright, and
four sketches upgraded when their children closed. The ten proofs
have 2,392 lines.

## How

- The route is an induction on d. If the subspace U is semistable
  (no rational S has a larger share of U than ℂᵈ), the linear
  subgroup theorem, DALAG Th. 11.21, already in the library from the
  multiplicity estimate, is applied once, at Υ⁻¹(U). Otherwise ℂᵈ
  splits along a rational subspace of maximal slope, and both pieces
  satisfy the same hypothesis with smaller d.
- Th. 11.21 returns an obstruction space over ℂ. Its algebraic part
  is all the argument needs, so no rationality of the obstruction is
  assumed. The periods 2πi enter through one extra rational subspace.
- DALAG and Roy reach Theorem 4 through other intermediate
  statements: DALAG through Th. 11.5 (3′) and Lemma 11.24, Roy
  through his Th. 2. The route here avoids both.
- A paper proof was written first and checked by an independent
  referee. The ten nodes were proved in parallel against stubs, and
  a chain with no stubs, against the mirror's library on Mathlib
  v4.35.0, builds on Lean's three axioms.
- The mirror holds the ten modules (2,497 lines, commit `b5eb6ae`).
  On Mathlib v4.35.0 one proof needs a larger instance-search budget;
  the platform's v4.33.1 compiles it as published.
- The agents worked under a clean-room rule: no agent opened another
  formalisation of these results.

## What is not proved

- **Nothing here is claimed as new.** Roy's Corollary 1 and Theorem 4
  are classical (Roy 1992; DALAG §11.6 and §12.3). Two steps, the
  rank of the relations and the space of periods, were not found in
  the sources read in the form stated; both are routine.
- **Only K = Q̄.** Theorem 4 is formalised for K = Q̄ and
  ℒ̃ = Q̄ + Q̄ℒ, the case DALAG Prop. 11.19 states.
- **Not Roy's Theorem 5.** The bound with ψ (DALAG Cor. 11.15) is
  not formalised.
- **The applications are not formalised.** Waldschmidt's Further
  variations, Th. 2.1, applies the corollary to the matrix (xᵢyⱼ);
  Fischler 2001 and DALAG §12.3 use it too.

## What remains open

Diaz's conjecture itself. Cor. 1 is the input a rank-four exclusion
of u⁴ would need (the 2 November memo showed rank at most three
cannot exclude it); no such exclusion is known.
