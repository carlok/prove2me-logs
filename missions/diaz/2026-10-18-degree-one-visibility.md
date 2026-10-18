# Which degree-one spaces Theorem B sees, decided by degrees
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-18

Near a point u of a circle, with uū algebraic, the degree-one spaces
W_g = span(1, u, ū, g, ug) always carry the 2×3 configuration
(1, u) ⊗ (ū, 1, g). Theorem B lists the four-dimensional extensions of
H₀ = span(1, u, ū) that carry one. The research notes said when a
degree-one space contains such an extension: exactly when it is a
complete linear system, a statement about divisors on P¹, which Mathlib
does not have. This round (R17) states and proves the criterion with
polynomials only, in six nodes.

## What was proved

- **The criterion.** If 1, u, ū, g, ug are free, W_g contains a
  four-dimensional extension that carries a configuration exactly when
  u·R(u)·g = N(u) for some R ≠ 0 of degree at most 2 and N of degree at
  most 3.
- **Rational data.** For g = P(u)/Q(u) in lowest terms, that happens
  exactly when max(deg P, deg Q) ≤ 2 + [Q(0) = 0].
- **Pencil spaces.** For W(λ, f) = span(1, u, ū, f, f/(s + λu)), with
  s² = uū, |λ| = 1 and f = P(u)/Q(u) in lowest terms, the bound is
  max(deg P, deg Q + 1) ≤ 2 + [Q(0) = 0] + [P(−sλ̄) = 0]. It does not
  need f real, and for Laurent f it contains the invisibility proved in
  R14.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.rational_pencil_space_visible_to_four_dimensional_extensions_iff_natDegree_le` | `a8617db8-73ad-43a6-b2ea-6e244b7e3b1e` | sketch, now Proved |
| `DiazModulus.rational_degree_one_space_visible_to_four_dimensional_extensions_iff_natDegree_le` | `71a0fb2b-3d61-4ec6-8a95-d5486e5a2a16` | sketch, now Proved |
| `DiazModulus.degree_one_space_visible_to_four_dimensional_extensions_iff_cubic_over_quadratic` | `336fccae-dfef-4261-869c-ee51119f346a` | sketch, now Proved |
| `DiazModulus.coprime_fraction_cubic_over_quadratic_iff_natDegree_le` | `f12b2e43-ef74-4656-83cb-a6a1cb11cd44` | ACCEPTED |
| `DiazModulus.degree_one_space_cubic_over_quadratic_of_mem_square_or_reciprocal` | `068f43ed-72e8-4dc9-923c-0826ccb40c16` | ACCEPTED |
| `DiazModulus.degree_one_space_mem_square_or_reciprocal_of_cubic_over_quadratic` | `3e585daf-cd25-4a89-9ca4-22937d777548` | ACCEPTED |

Milestones 140 and 141 are the criterion and the pencil spaces. The
mirror holds all 434 results; note version 1.31 states them as one
proposition.

## How

- **One direction** writes u², ū² or 1/(u − a) in the basis
  1, u, ū, g, ug, replaces ū by ρ/u and clears denominators.
- **The other is a dimension count.** M ↦ M(u)/(uR(u)) maps the
  polynomials of degree below 5 onto W_g, because the five generators
  are images and W_g has dimension 5. So every image lies in W_g, and
  one of u², ū² or 1/(u − b), for a root b of R, is an image. The
  estimate for this node was 200–300 lines; it took 154.
- **Rational data.** Evaluation at the transcendental u is injective,
  so the condition is X·R·P = N·Q, and coprimality gives Q ∣ X·R.
- **Pencil spaces.** f = s·g + λ·u·g turns W(λ, f) into W_g with
  g = f/(s + λu); one factor X + sλ̄ cancels when P(−sλ̄) = 0.
- Three proof agents; six files of 72 to 171 lines, 725 in all, each
  compiling in 3 to 8 seconds of CPU time. On v4.35.0 two names were
  deprecated (`if_pos`, `if_neg`); the porter renames them to
  `ite_eq_left` and `ite_eq_right`, which have the same signatures.

## What is not proved

- **Ratios of degree two.** The research notes classify the
  conjugation-stable invisible spaces with a factor of degree two into
  three families. That classification is not formalised; only one
  member of each family is.
- **Data that are not rational in u** are outside these statements.
- **All six results are routine** by the blueprint's rubric, and none
  was found in the sources read.
- **No step towards Diaz's conjecture.** The results say what Theorem B
  can see, not what is in ℒ̃.

## What remains open

- **Theorem E of the research note on polynomial hulls.** Two blind
  referees found it correct and its proof condensed; it is being
  written out in full for formalisation (R18).
- **The rest of Theorem D** of that note: scoped at about 14 nodes.
