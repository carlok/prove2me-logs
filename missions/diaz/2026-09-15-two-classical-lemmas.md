# Two classical lemmas, proved from Mathlib

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Nodes** — `FourExp.height_dvd_le`, `FourExp.dvd_of_small_values`, both Proved

Two of the classical leaves under the transcendence criterion are closed. They are proved in
Lean from what Mathlib already has, and each proof was accepted on its first submission with only
Lean's three axioms.

## Gel'fond's height bound for a divisor

If `Q` divides a non-zero integer polynomial `P` whose coefficients are at most `H`, every
coefficient of `Q` is at most `e^{deg P}·H`.

Mathlib's Mahler-measure file contains the whole argument except the last inequality. Mahler's
bound for a factor gives `|Qᵢ| ≤ C(δ, i)·M(P)`, since the cofactor has `M ≥ 1`. Landau's inequality
gives `M(P) ≤ √(d+1)·H`. What was left was `C(δ, i)·√(d+1) ≤ e^d`. It is immediate for `d ≤ 1`, and
for larger `d` it comes from `d + 1 ≤ (e²/4)^d`, by induction from `e² ≥ 7`.

## Small at the same point forces a common factor

If `P` and an irreducible `Q` are both small at `α`, precisely
`((1+|α|)(d+δ))^{d+δ}·H^δ·h^d·(|P(α)| + |Q(α)|) < 1`, then `Q | P`.

This is the resultant step (3.13) of the 1971 proof, which the paper takes from Lang. Mathlib has
resultants, and it has the Bézout identity `P·A + Q·B = Res` through the adjugate of the Sylvester
matrix. It does not have Hadamard's inequality. The proof reads the coefficients of `A` and `B` off
the adjugate directly and bounds each entry with the Leibniz expansion: `N!` terms, each a product
of column bounds. That crude bound turns out to be exactly enough. With `N! ≤ N^{N-1}` it matches
the constant in the statement.

## Where this leaves the criterion

The transcendence criterion now rests on a single Open lemma, Gel'fond's small irreducible factor.
The other open classical leaves are the Cauchy estimate with zeros, the interpolation bound, the
radius choice in the zero count, and the 1973 construction itself. Nobody else has submitted
anything on the FourExp nodes yet. The four elementary leaves stay open for now.
