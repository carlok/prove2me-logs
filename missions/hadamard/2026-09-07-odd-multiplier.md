# The Hadamard target's determinant is a corollary of orthogonality

- **Mission** — The Hadamard Conjecture,
  <https://prove2.me/missions/65110803-c4c2-4b2a-ba61-8e404136c328>
- **Environment** — `c5ea0035` (Lean v4.30.0)
- **Date** — 2026-09-07

The Hadamard conjecture asserts that for every `k` there is a matrix
of order `4k` with entries ±1 and pairwise orthogonal rows. Such a
matrix attains the maximum determinant possible for a ±1 matrix of its
order. The mission target worked here,
`Hadamard.odd_multiplier_exists`,

- https://prove2.me/theorems/304080d5-831e-4353-8d64-a132bf567acd

asks for the odd-`k` case, and asks for it in *determinant* form: a
±1 matrix `M` of order `4k` with `|det M| = (4k)^(4k/2)`.

## What was proved

A reduction was accepted — submission
`1c8ac5a7-bff2-4cbb-9ace-91117984bad1`, SKETCH_ACCEPTED — citing one
new child:

- `Hadamard.exists_orthogonal_pm_one`
  https://prove2.me/theorems/e4944c69-30f1-4637-a3c4-67b84958a6cb

the same existence statement for the same matrix, but with the
condition `M * Mᵀ = (4k) • 1` in place of the determinant equality.

What the reduction proves is the bridge: `M Mᵀ = n • 1` implies the
extremal determinant.

## How

`det (M Mᵀ) = det (n • 1) = nⁿ` by `Matrix.det_smul`, which gives
`(c • A).det = c ^ Fintype.card n * A.det`. Separately
`det (M Mᵀ) = (det M)²`. Hence `|det M| = √(nⁿ) = n^(n/2)`, taken as
an `rpow`. The real-power step is `Real.sqrt_eq_rpow`,
`Real.rpow_natCast`, `Real.rpow_mul`. It needs `n > 0`, which the
hypothesis `Odd k` supplies.

The reason the slice is worth carving off is that it is a conversion
every future construction would otherwise repeat. Sylvester doubling,
Paley, Williamson, Baumert–Hall — every known family builds a matrix
and checks row orthogonality. None of them computes a determinant.
Leaving the target in determinant form makes each of them pay for the
translation.

## What is not proved

No matrix is constructed, for any `k`. The mission is exactly as far
from a Hadamard matrix as it was before.

The bridge is one-directional. Orthogonality implies the extremal
determinant; the converse — that a ±1 matrix attaining the maximum
determinant must satisfy `M Mᵀ = n • 1` — is true, by the equality
case of Hadamard's inequality, and is not formalized here. So the
child is formally stronger than the target, not equivalent to it.

`Odd k` is used only to obtain `n > 0`. The determinant argument is
indifferent to the parity of `k` and would run identically for even
`k`; the target's distinguishing hypothesis contributes nothing beyond
positivity. Whatever difficulty the odd case carries, it is entirely
inside the child.

## What remains open

The child `e4944c69-30f1-4637-a3c4-67b84958a6cb`: existence, for odd
`k`, of a ±1 matrix of order `4k` with `M Mᵀ = (4k) • 1`. That is the
Hadamard conjecture restricted to odd multiplier, undiminished. The
odd case is the hard one — the doubling constructions handle powers of
two for free — and nothing in this reduction touches it.
