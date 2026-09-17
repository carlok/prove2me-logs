# The auxiliary function is small on a larger grid

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — Mathlib `0df444a` (Lean v4.33.1); also compiled on the
  mirror's v4.32.0
- **Date** — 2026-09-17
- **Nodes** — `FourExp.extrapolation`, Proved

The second of Waldschmidt's three 1973 lemmas is proved. The auxiliary
function `F` vanishes to high order on a small grid, and this lemma shows
that its derivatives are then tiny on a grid fourteen times larger in each
direction. It is the analytic half of the transcendence argument. The
earlier step made `F` vanish, and the next step turns one tiny, non-zero
value into an integer polynomial that contradicts the transcendence
criterion.

## What was proved

`FourExp.extrapolation` (`478273e3`, submission `60352656`, ACCEPTED). Let
`y₁, y₂` be linearly independent over ℚ and `x₁, x₂` arbitrary. For every
`κ > 0` there are `κ'` and `N₀` with the following property for `N > N₀`.
Suppose the coefficients of
`F(z) = Σ c(i,j,k) z^i e^{(jx₁+kx₂)z}` are at most `exp(κN²√log N)`, and
`F^{(m)}(ay₁+by₂) = 0` for `a < N/√log N`, `b < N√log N`, `m < S`. Then
`|F^{(s)}(ay₁+by₂)| ≤ exp(−N⁴√log N/κ')` for `s < S/2`, `a < 14t₁`,
`b < 14t₂`. The proof gives `κ' = 32`.

## How

It is the Schwarz lemma, run through the already proved
`FourExp.cauchy_estimate_with_zeros`:

- **Zeros.** The small grid has `t₁t₂` distinct points, distinct because
  of the independence of `y₁, y₂`. Mathlib's
  `natCast_le_analyticOrderAt_iff_iteratedDeriv_eq_zero` turns the
  vanishing derivatives into order at least `S` at each point. An infinite
  order would force `F ≡ 0` (`analyticOrderAt_eq_top_iff_eq_zero`), which
  is trivial.
- **Radii.** `ρ = 14(t₁|y₁| + t₂|y₂|)` bounds every distance involved. With
  `R = (ρ+1)N` the contraction ratio `(ρ+1)/(R−ρ)` is at most `1/(N−1)`.
  This choice keeps the argument independent of how the `yⱼ` sit in the
  plane.
- **Numbers.** The zeros gain `exp(−N⁴√log N/16)`, since `t₁t₂S` is at
  least `N⁴/(8√log N)` and `log(N−1) ≥ (log N)/2`. The costs are the
  factorial, the number of terms, the growth `Z^S` and `e^{2NXZ}` of `F` on
  the large circle. All of them are `exp(O(N³√log N))`, so for large `N`
  the total is below `exp(−N⁴√log N/32)`.

The proof is 448 lines. The first version put all the asymptotics in one
lemma and timed out. Split into seven lemmas with explicit
`linear_combination` certificates, it compiled on both Mathlib revisions
and was accepted on the first submission. The GitHub library holds 155 of
155 results.

## What is not proved

The hypothesis `s < S/2` is used only as `s ≤ S`. The lemma is stated for
the fixed 1973 parameters (`S`, `t₁`, `t₂` as floors, the factor 14), not
for general ones. It says nothing about non-vanishing: `F` could be
identically zero, and ruling that out belongs to the step that uses the
lemma.

## What remains open

Under `construction_core_1973` only `norm_to_polynomial_alg` is left: take
the norm from `ℚ(ω, ω₁)` down to `ℚ(ω)` and bound the resulting integer
polynomial. When it closes, the core closes by cascade. The three easy
leaves under the construction are still open.
