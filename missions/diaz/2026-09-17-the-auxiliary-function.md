# The auxiliary function of the 1973 construction exists

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — Mathlib `0df444a` (Lean v4.33.1); also compiled on the
  mirror's v4.32.0
- **Date** — 2026-09-17
- **Nodes** — `FourExp.siegel_aux` and `FourExp.aux_linear_system`, Proved;
  `FourExp.auxiliary_function_alg`, Proved by cascade

Waldschmidt's 1973 proof of the four exponentials theorem in transcendence
degree one starts, like every proof of its kind, by building an auxiliary
function: an exponential polynomial with integer-like coefficients, not
identically zero, that vanishes to high order on a grid. Earlier the same
day the node for that step was split in two: the arithmetic that turns the
vanishing conditions into an integer linear system, and Siegel's lemma,
which solves it. Both halves are now proved, so the auxiliary function
exists as a machine-checked theorem.

## What was proved

| Theorem | Node | Verdict |
|---|---|---|
| `FourExp.siegel_aux` | `b421c5b8` | ACCEPTED |
| `FourExp.aux_linear_system` | `278448f6` | ACCEPTED |
| `FourExp.auxiliary_function_alg` | `88de0071` | Proved by cascade |

`aux_linear_system` says this. Suppose all four `e^{xᵢyⱼ}` are algebraic.
Suppose also that `xᵢ`, `yⱼ` and `e^{xᵢyⱼ}` are quotients, over a common
denominator, of integer polynomials in a transcendental `ω` and an element
`ω₁` that is integral of degree `d` over `ℤ[ω]`. Then there is a constant
`κ₁` such that, for every large `N`, there is an integer matrix with these
properties:

- Its unknowns are the coefficients of
  `F(z) = Σ c_{ijk} z^i e^{(jx₁+kx₂)z}`, with each `c` written as
  `Σ q_{μν} ω^μ ω₁^ν`.
- It has at most half as many rows as unknowns.
- Its entries are at most `exp(κ₁N²√log N)`.
- Every integer solution makes `F^{(m)}(ay₁+by₂)` vanish for
  `a < N/√log N`, `b < N√log N`, `m < N²/√log N`.

`siegel_aux` then finds a small non-zero solution.

## How

The linear system is built entirely over `ℤ[X][Y]`, with `X ↦ ω` and
`Y ↦ ω₁`:

- **Derivatives as a recursion.** The `m`-th derivative of an exponential
  polynomial is again one, with coefficients given by
  `c ↦ (i+1)c_{i+1} + β c_i`. The same recursion, scaled by the denominator,
  runs on integer polynomials and commutes with evaluation.
- **Algebraic exponentials add height, not degree.** An integer annihilator
  `m` of `e^{xᵢyⱼ}`, with leading coefficient `L`, reduces `Lⁿeⁿ` to a
  combination of `e^λ` with `λ < deg m`, whose coefficients grow at most
  geometrically in `n`. Padding each factor to a common power of `L` gives
  a non-zero constant independent of the summation indices.
- **One polynomial per unknown.** Each unknown `q_u` contributes an integer
  polynomial `Π_u`. Linearity of the recursion and of the exponential
  polynomial gives `Σ q_u Π_u(ω, ω₁) = Δ · F^{(m)}(ay₁+by₂)` with `Δ ≠ 0`.
- **Rows.** Reducing `Y`-powers modulo the monic minimal relation keeps
  `deg_Y < d`. The rows are the coefficients of `X^h Y^r` in the reduced
  `Π_u`, so if every row annihilates `q` the whole polynomial is zero.
- **Sizes.** A majorant calculus over `ℕ[X][Y]` (absolute coefficients,
  evaluation at `1`, degrees in each variable) bounds degrees and heights.
  The `X`-degree is `O(N²/√log N)`, so choosing `M` a large multiple of `S`
  gives twice as many unknowns as rows. The heights are
  `exp(O(N²√log N))`, dominated by exponents up to `4N²√log N`.

Siegel's lemma is Mathlib's `Int.exists_ne_zero_int_vec_norm_le`. The
non-vanishing of `c` comes from the minimality of the relation for `ω₁`.

The proof is 1,409 lines in one file. It compiled on both Mathlib
revisions before submission and was accepted on the first try. The older
revision needed one change: `nlinarith` calls in the final real-number
estimate ran out of heartbeats, and explicit `linear_combination`
certificates replaced them.

The GitHub library holds 154 of 154 results, with only Lean's three
axioms.

## What is not proved

The auxiliary function is only the first of Waldschmidt's three lemmas.
Nothing yet shows that it is small on a large disc (extrapolation), or that
a non-zero small value yields an integer polynomial with the bounds the
transcendence criterion needs (the norm step). So `construction_core_1973`
is still Open, and so are the construction and the four exponentials node
above it.

The statement is also narrower than the paper's. It assumes the four
exponentials are algebraic, and it fixes the parameters `S`, `t₁`, `t₂` as
floors of `N²/√log N`, `N/√log N`, `N√log N`. Other choices are not
covered.

## What remains open

Under `construction_core_1973`:

- `extrapolation`, the analytic step, which should reuse the proved Cauchy
  estimate with zeros;
- `norm_to_polynomial_alg`, the norm from `ℚ(ω, ω₁)` down to `ℚ(ω)`.

The three easy leaves under the construction, parametrisation, growth and
counting, are also still open.
