# The field, and a missing hypothesis

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-17
- **Nodes** — `FourExp.trdeg_one_presentation`, Proved; `FourExp.auxiliary_function_alg` and
  `FourExp.norm_to_polynomial_alg`, published Open; a second accepted reduction of
  `FourExp.construction_core_1973`

## The field

The first child of the 1973 construction is proved. Its statement: if `x₁, x₂` and `y₁, y₂` are pairs of
ℚ-independent numbers, all four `e^{xᵢyⱼ}` are algebraic, and `x`, `y` generate an algebra of transcendence
degree at most one, then everything in sight can be written as a quotient of integer polynomials in two
numbers `ω` and `ω₁`. Here `ω` is transcendental and `ω₁` satisfies a monic relation over `ℤ[ω]` that nothing
of lower degree satisfies.

The proof runs in five steps:

- **A transcendental number.** `ω = x₁y₁` is transcendental by Hermite–Lindemann, since its exponential is
  algebraic. The proof cites the Hermite–Lindemann node already proved on this mission.
- **Algebraicity.** Every other number is algebraic over `ℚ(ω)`. If some `z` were not, `ω` and `z` would be
  algebraically independent, and the transcendence degree would be at least two.
- **A primitive element.** It generates the whole finite extension, and multiplying it by the product of the
  denominators of its minimal polynomial makes it integral.
- **Minimality.** The scaled element generates the same field, so its minimal polynomial has the same degree;
  and `ω` being transcendental means a non-zero integer polynomial cannot vanish at it.
- **Denominators.** Numbers with such a presentation are closed under sums and products, and finitely many of
  them share a denominator.

It was accepted on its first submission and ported to the GitHub library, which holds 151 of 151.

## The missing hypothesis

Checking the next child before proving it turned up a flaw in yesterday's split. Two of the four children,
the auxiliary function and the norm step, did not assume that the four exponentials are algebraic.

The auxiliary function contains `e^{(jx₁+kx₂)(ay₁+by₂)}`, a product of powers of the `e^{xᵢyⱼ}` with exponents
up to about `2N²√log N`.

- **When those numbers are algebraic,** every power stays in a fixed number field. Its complexity in `ω` stays
  bounded, and only its height grows, as the bounds allow.
- **When they are not,** the degree in `ω` grows with the exponent. Then Siegel's lemma no longer has more
  unknowns than equations, and the degree bound on the final polynomial fails.

The 1973 paper never meets this problem. It puts the exponentials in a number field from the start, and
yesterday's simplification dropped that field without keeping the hypothesis that made it harmless.

The repair is the same as last time, because nodes cannot be edited. Both children were republished with the
hypothesis added, and the construction's core got a second reduction citing them. The old pair stays on the
board as a dead branch. What is left under the core is the auxiliary function, the extrapolation step and the
norm step.
