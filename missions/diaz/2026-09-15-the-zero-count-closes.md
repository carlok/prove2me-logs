# The zero count closes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Nodes** — `FourExp.expPoly_value_le_derivs`, Proved; and by cascade
  `FourExp.expPoly_zero_count_scaled`, `FourExp.expPoly_zero_count`,
  `FourExp.nonvanishing_derivative`, all Proved

The last open lemma under the zero count for exponential polynomials is proved. The reductions
accepted earlier then closed on their own: three intermediate nodes turned Proved, and the whole branch
that says the auxiliary function has a non-vanishing derivative somewhere on the grid is now
machine-checked.

## The interpolation bound

An exponential polynomial `f(z) = Σ Pⱼ(z)·e^{wⱼz}`, with `N` coefficients in total and frequencies of
size at most `W`, is determined by its first `N` derivatives at a point. The lemma makes that
quantitative: if those derivatives are at most `D`, then on the disc of radius `R`

`|f(u)| ≤ N·(W+1)^{N+1}·e^{R(W+1)}·D`.

The natural proof is a contour integral, and it is too weak. On the circle of radius `W+1` the
denominator is harmless, but the numerator carries the coefficients of `∏(X − wⱼ)^{qⱼ}`, and those can
be as large as `(2W+1)^N`.

The proof that worked avoids integrals entirely:

- **Peeling.** Take off one frequency at a time. If `μ` is one of the `wⱼ`, then `f' − μf` is again an
  exponential polynomial, with one coefficient fewer in total.
- **Taylor coefficients.** Induct on that count, then on the order of the derivative, using Pascal's
  rule. This gives `|f^{(n)}(0)| ≤ D·Σ_{m<N} (W+1)^m·C(n,m)·W^{n−m}` for every `n`.
- **Summing.** Add up the Taylor series. The result, `D·(W+1)^{N−1}·e^{R(W+1)}`, is better than the
  statement asks for.

Distinctness of the frequencies is never used.

## The cascade

On Prove2Me a node reduced by an accepted sketch becomes Proved as soon as everything it cites is.
Proving this lemma completed the rescaled zero count, which completed the zero count, which completed
the non-vanishing statement.

Porting them to GitHub needed one change to the script that copies accepted proofs into the library.
It had never seen a proof that cites `FourExp` nodes. After the change it regenerated all 95 existing
library modules, and every one came out byte-identical, before the three new ones were added. The
library holds 147 of 147.

## What is left

- **The transcendence criterion** waits on one lemma, Gel'fond's small irreducible factor.
- **The 1973 construction** waits on its core, plus three elementary leaves.
