# Cor. 11.15 over ℚ, and DALAG's Lemma 12.9
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-14

The two cases the previous round left out are done. DALAG's
Cor. 11.15 is now proved for (ℚ, ℚ + ℒ) as well as for (Q̄, ℒ̃), by
Roy's route over ℚ. And DALAG's Lemma 12.9 is proved, so Cor. 12.23
also holds in the affine form of p. 435. Twelve nodes, all with no
hypothesis.

## What was proved

- **DALAG Cor. 11.15 for (ℚ, ℚ + ℒ):** if V ⊆ ℂᵈ meets ℚᵈ only in 0,
  then V ∩ (ℚ + ℒ)ᵈ is finite-dimensional over ℚ, of dimension at
  most Ψ(dim V, d_min), where d_min is the least dimension of a
  subspace spanned by rational vectors that contains V.
- **Roy 1992, Th. 5 over ℚ,** in decomposition form, on the way.
- **DALAG Lemma 12.9:** the structural rank can be computed through
  any map into affine forms that is injective on the span of the
  entries; with it, Lemma 12.8 for any such map into linear forms.
- **DALAG Cor. 12.23 in the form of p. 435:** if M = M₀ + Σ λₖNₖ with
  rational M₀, Nₖ, λₖ ∈ ℚ + ℒ and 1, λ₁, …, λₘ free over ℚ, the rank
  of M is at least half the rank of M₀ + Σ XₖNₖ over ℚ(X).

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.dalag_cor_11_15_rat` | `ef098be8-01c6-42f9-b3ed-775d006a6f48` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_lemma_12_9` | `c3a6cf3d-ae3c-407c-8cc5-e49c9b2a3da9` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_cor_12_23_affine` | `00e2717a-2559-4199-8194-0f12b8bfbace` | SKETCH_ACCEPTED, now Proved |

Milestones 207–209 are the three rows; the other nine nodes joined
by import. All 12 are Proved: 6 were accepted outright, and 6 were
sketches that upgraded when their children closed. The proofs have
2,364 lines.

## How

- Roy's Remark (i) (p. 37) extends his Th. 4 to every subfield F of
  Q̄. For F = ℚ the library's chain for Th. 4 runs again, with ℚ in
  place of Q̄ and one block of variables. Th. 5 then follows by an
  induction along a rational subspace of maximal slope, and Ψ comes
  from Roy's Lemma, proved in the previous round.
- DALAG's own proof of the ℚ case goes through Prop. 11.19, whose
  printed proof has a gap there (below); it is not used.
- A reduction to the (Q̄, ℒ̃) case through Baker's theorem was set
  aside: in dimension 3 it needs a statement that the strong four
  exponentials conjecture would give, and no proof of it was found.
- Lemma 12.9 takes two steps that the printed proof leaves to the
  reader: a dehomogenisation, done as a homomorphism of fields of
  rational functions, and Lemma 12.8 for any map injective on the
  span.
- Each design was checked by an independent referee before any Lean;
  the statements were frozen, then proved against stubs. A chain with
  no stubs, against the mirror's library on Mathlib v4.35.0, builds on
  Lean's three axioms.

## Printed statements corrected

- **DALAG Lemma 11.18 (2), p. 400:** the second clause is false. For
  k = ℚ and U = ℂ(1, √2), U meets ℚ² only in 0 but contains an
  algebraic vector.
- **DALAG, proof of Prop. 11.19 for (ℚ, ℚ + ℒ), pp. 402–403:**
  Th. 11.5 (3′) need not select the trivial subgroup. In ℂ³, for
  U = ℂ(1, √2, 0) + ℂ(log 2, log 3, log 5), a subgroup defined over
  Q̄ ties with it. The example refutes the step, not the statement.
- **DALAG, proof of Prop. 12.13, (iv) ⇒ (iii), p. 430:** the matrix
  used need not have entries in E; multiplying it by x₀ repairs the
  step. The proposition is correct.
- **Two slips** on pp. 426–427, and an item of the mirror's own list
  of passages checked and not counted as errors, which held for Q̄
  only and now says so.

The full list is `ERRATA.md` in the mirror.

## What is not proved

- **Nothing here is claimed as new.** These are formal proofs of
  classical results.
- **Roy's Th. 4 and DALAG Prop. 11.19 over ℚ** in their minimal-ratio
  form; only the slope form that the corollary needs is proved.
- **Other subfields F of Q̄:** Roy's Remark (i) covers them; only
  F = ℚ and F = Q̄ are formalised.
- **DALAG Prop. 12.7 and Prop. 12.13** are not formalised; two of the
  corrections above concern their printed proofs.

## What remains open

Diaz's conjecture itself; these results enlarge the stock of rank
bounds in the library and exclude no new candidate.
