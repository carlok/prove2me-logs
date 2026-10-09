# Two poles, and Kirby's weak Schanuel conjecture at a candidate
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-09

Two items from the backlog left by R5 and by a literature check of
5 October, in seven nodes. A third item was blueprint work only: the
three results from Carlo's manuscript published on 4 October now have
entries, with the four nodes their proofs import.

## What was proved

- **Two poles.** Let u ∉ Q̄ with ρ = uū algebraic and a₁ ≠ a₂ non-zero
  algebraic, zᵢ = u/(u² − aᵢ), W = H₀ + Q̄z₁ + Q̄z₂. Then W carries the
  configuration (1, u²) ⊗ (b, bu², bu⁴), b = 1/(u(u² − a₁)(u² − a₂)),
  but contains none of u², ū², 1/(u − c), so no four-dimensional
  H₀ + Q̄w inside it carries one. R5 needed a₂ = ρ²/ā₁; this does not.
- **At a candidate,** with Roy's theorem as a hypothesis: z₁ and z₂ are
  not both in ℒ̃, and when aᵢāᵢ = ρ² their sum is not.
- **Kirby's weak form.** With only the case n = 2 of Kirby's weak
  Schanuel conjecture as a hypothesis, every candidate has Re u ≠ 0 and
  Im u ∈ πℚ^×, and Diaz's conjecture is equivalent to: t² + π² is
  transcendental for every real t ≠ 0 with eᵗ algebraic.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.circle_point_two_pole_configuration_invisible_to_four_dimensional_extensions` | `7554ba08-b9b2-4739-8cc0-acf2e0c2ab9e` | sketch, now Proved |
| `DiazModulus.candidate_sum_div_sq_sub_not_mem_logAlgTilde` | `6309030f-2cc2-42a6-92a0-5518c3d03e9f` | sketch, now Proved |
| `DiazModulus.diaz_iff_single_relation_of_weak_schanuel` | `8fd6a1b2-9aee-4669-9d18-07def040f128` | sketch, now Proved |
| `DiazModulus.circle_point_two_pole_extension_carries_two_by_three_configuration` | `9cdff91f-d194-421e-bd97-a3a72faf9979` | ACCEPTED |
| `DiazModulus.circle_point_two_pole_extension_excludes_squares_and_reciprocals` | `2ea6a548-8444-48d0-9666-c224dac35020` | ACCEPTED |
| `DiazModulus.candidate_two_pole_not_both_mem_logAlgTilde` | `9c51926f-f543-4223-ad7d-e06913f68e74` | sketch, now Proved |
| `DiazModulus.candidate_im_mem_pi_rat_of_weak_schanuel` | `aa7b3103-88ec-47f5-9bb1-86362797f1af` | ACCEPTED |

Milestones 116–118 are the first three rows. The mirror holds all 389
results, and note version 1.22 states the batch as a proposition and a
remark.

## How

- **Partial fractions** give bu², bu⁴ and bu⁶ in W, and b itself once
  u⁻¹ = ū/ρ is used; each identity is `field_simp; ring`.
- **Parity**, as in R5: every element of W is a constant plus an odd
  function of u, so a membership becomes A(u²) + uB(u²) = 0 and forces
  A = B = 0. R5's lemma applied unchanged.
- **The sum** is handled by conjugation: z̄ᵢ = −(ρ/āᵢ)zᵢ on the circle,
  so the sum and its conjugate give both terms.
- **Kirby's form.** ℚ[u, ū, eᵘ, e^ū] is algebraic over ℚ[u], so the
  hypothesis gives mu + nū ∈ 2πiℤ. Off the axes this forces n = −m and
  Im u = (k/m)π. For the equivalence, Nu with N the denominator of k/m
  has eᴺᵘ real, and the existing one-relation node closes it.

## What is not proved

- **No step towards a proof of Diaz's conjecture.** The two-pole results
  map what Roy's theorem sees at a candidate; the weak Schanuel results
  are conditional on an open conjecture.
- **The exclusions at a candidate are not new.** Both are one
  substitution in Diaz 2007, Th. 7(2), which is Fischler 2001, Lemma
  6.1, with ratio u². They carry Roy's theorem as a hypothesis and are
  vacuous if Diaz's conjecture holds.
- **Kirby's weak form says nothing about the remaining relation.** Its
  logarithms always satisfy 2·iπ ∈ 2πiℤ, so the conjecture cannot reach
  it. It is also not the "weak Schanuel" of Calegari and Mazur.
- **The rest of the five-dimensional case** is untouched: Case II of the
  reduction, other involutions of the u-line, z not rational in u.

## What remains open

The gap the development reduces Diaz's conjecture to is unchanged: a
2×2 statement on the single orbit GL₂(Q̄)·(1, u)ᵀ(1, ū)·GL₂(Q̄).
