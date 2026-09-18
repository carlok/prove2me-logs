# The core of the 1973 construction is proved

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — Mathlib `0df444a` (Lean v4.33.1); also compiled on the
  mirror's v4.32.0
- **Date** — 2026-09-18
- **Nodes** — `FourExp.norm_to_polynomial_alg`, Proved;
  `FourExp.construction_core_1973`, Proved by cascade

The last of Waldschmidt's three 1973 lemmas is proved, and with it the whole
core of the construction. The lemma takes the one tiny non-zero value that
the previous two steps produce and converts it into an integer polynomial
in a single variable: small at `ω`, of controlled degree and height. That
is exactly the input the already proved transcendence criterion needs.

## What was proved

`FourExp.norm_to_polynomial_alg` (`7f85aec3`, submission `7e5bc291`,
ACCEPTED). Under the presentation hypotheses (a transcendental `ω`, an `ω₁`
integral of degree `d` over `ℤ[ω]` with a minimal relation `Q`, and all the
numbers written over a common denominator `D`), suppose the coefficients of
`F` come from integers `q` of size at most `exp(κN²√log N)`, and that
`γ = F^{(s)}(ay₁+by₂)` is non-zero with `|γ| ≤ exp(−N⁴√log N/κ')`. Then
there is a constant `k` such that for every `C` and every large `N` there is
a non-zero `P ∈ ℤ[X]` with coefficients at most `exp(kN²√log N)`, degree at
most `kN²/√log N`, and `|P(ω)| < exp(−C·(kN²√log N)·(kN²/√log N))`.

Closing it made `construction_core_1973` (`41291ef0`) a Proved node, since
its accepted reduction cites exactly the four children, all now proved.

## How

The paper takes the norm of `γ` down to `ℚ(ω)` and estimates the
conjugates. The formal proof replaces that by linear algebra, which avoids
building the field extension altogether:

- **The value as an integer polynomial.** The machinery of the linear-system
  step is reused: the derivative recursion scaled by `D`, powers of the
  algebraic `e^{xᵢyⱼ}` reduced through their integer annihilators, and
  reduction of `Y`-powers modulo the monic `Q`. It gives `Π ∈ ℤ[X][Y]` with
  `deg_Y Π < d` and `Π(ω,ω₁) = Δγ` for an explicit non-zero `Δ`.
- **The polynomial.** Let `M` be the matrix of multiplication by `Π` modulo
  `Q` in the basis `1, Y, …, Y^{d-1}`; its entries are integer polynomials
  because `Q` is monic. Set `P = det M`. This is the norm, but nothing about
  conjugates is needed.
- **Non-vanishing.** If `det M = 0`, then over the domain `ℤ[X]` some
  non-zero vector satisfies `Mu = 0` (Mathlib's
  `Matrix.exists_mulVec_eq_zero_iff`). The corresponding `U = Σ uₖYᵏ` has
  `deg_Y U < d` and `Π(ω,ω₁)·U(ω,ω₁) = 0`, so `U(ω,ω₁) = 0`, so `U = 0` by
  the minimality of `Q`. Contradiction.
- **Smallness.** The vector `(1, ω₁, …, ω₁^{d-1})` is a left eigenvector of
  `M(ω)` with eigenvalue `Δγ`, so `M·adj M = (det M)I` gives
  `P(ω) = Δγ · (v·adj M)₀`. The cofactors are determinants of bounded
  entries, so they cost only `exp(O(N²√log N))`, while `γ` supplies
  `exp(−N⁴√log N/κ')`.
- **Sizes.** The majorant calculus bounds the entries of `M`: heights
  `exp(O(N²√log N))` and degrees `O(N²/√log N)`. That gives the height and
  degree bounds on `P` directly.

The proof is 2,648 lines, the largest on this mission, and was accepted on
the first submission. One practical lesson: a single theorem with a large
context makes `nlinarith` and `positivity` crawl, because they preprocess
every hypothesis. Moving each numeric step into a small standalone lemma
took the file from a build that ran for a quarter of an hour without
finishing to one that compiles in half a minute.

The GitHub library holds 157 of 157 results, with only Lean's three axioms.

## What is not proved

The statement assumes the four exponentials are algebraic; the version
without that hypothesis stays a documented dead branch. `k` is explicit but
far from optimal, and the threshold on `N` grows like a double exponential
in `C`, which is enough for the criterion but says nothing effective.
Nothing here shows the auxiliary function is non-zero: that is a hypothesis,
discharged elsewhere.

## What remains open

The construction `Zc` still cites three small leaves, all elementary and all
open: `rank_one_parametrization` (choosing the rank-one pair),
`construction_growth` (monotonicity and growth of `k·t²√log t`), and
`construction_count_1973` (one asymptotic inequality in `N`). When those
close, the construction, the zero-count node `Z` above it, and the four
exponentials in transcendence degree one all follow by cascade.
