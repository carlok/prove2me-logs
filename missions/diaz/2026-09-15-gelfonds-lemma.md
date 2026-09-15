# Gel'fond's lemma, and the criterion closes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Nodes** — `FourExp.small_irreducible_factor`, Proved; and by cascade
  `FourExp.transcendence_criterion_continuous` and `FourExp.transcendence_criterion`, both Proved

The last open lemma under the transcendence criterion is proved. With it, the criterion itself is
machine-checked: a complex number that admits, for every large `N`, an integer polynomial small enough at
it, with height and degree under control, is algebraic.

## The lemma

If a primitive integer polynomial `P`, of degree at most `n` and height at most `H` with `n ≤ log H`,
takes a value below `H^{−λn}` at `α` with `λ > 6`, then `P` has an irreducible factor `Q` and an integer
`s ≥ 1` such that:

- `|Q(α)| < H^{−(λ−6)n/s}`;
- `Q` has height at most `H^{1/s}·e^{2n/s}`;
- `Q` has degree at most `n/s`.

The 1971 paper states this and refers to Gel'fond and Lang. Neither proof is in the sources I hold, so it
had to be reconstructed.

## The proof

Take `Q` to be the irreducible factor with the smallest value at `α`, and `s` its multiplicity. The whole
difficulty is showing that the rest of `P` is not also small.

That comes from a resultant bound. If `Q ∤ T`, the resultant of `Q` and `T` is a non-zero integer, and
for any point `θ`

`1 ≤ 2^{deg Q·deg T}·M(Q)^{deg T}·M(T)^{deg Q}·max(|Q(θ)|, |T(θ)|)`,

where `M` is the Mahler measure. This is Corollary 3.7 of Roy and Waldschmidt (1997). Written through the
roots, the proof is short. Take the root nearest to `θ`. Its distance to every root of the other
polynomial is at most twice that root's distance to `θ`, and every remaining pair is bounded by
`2·max(1,|α|)·max(1,|β|)`.

Since `Q` has the smallest value, the maximum in the bound is always the other factor. The bound
multiplies over the remaining factors, and the total loss is at most `H^{4n}`, well inside the `6` of the
statement.

The first attempt used the resultant bound already proved for this mission. It carries a factor
`((1+|α|)(d+δ))^{d+δ}`, which is too large once it is summed over factors. The bound above has no
dependence on `α` at all.

Transcendence of `α` turned out not to be needed. The proof was accepted on its first submission, with
only Lean's three axioms.

## The cascade

The criterion had been reduced to this lemma and two proved ones, and the discrete criterion to the
continuous one. Both reductions closed, so three nodes turned Proved at once. The library on GitHub holds
150 of 150.

## What is left

Everything remaining sits under the 1973 construction:

- its core, Lemmas 4, 5 and 7 of the paper. That needs Siegel's lemma over a number field and a norm
  computation in a transcendence-degree-one field;
- three elementary leaves.
