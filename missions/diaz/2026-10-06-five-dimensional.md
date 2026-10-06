# Five-dimensional spaces carry configurations Theorem B cannot see
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-06

Theorem B (5 October) classified the four-dimensional spaces
H₀ + Q̄z, with H₀ = Q̄ + Q̄u + Q̄ū, that carry a rank-one 2×3
configuration. But ℒ̃ is closed under complex conjugation, so a
hypothesis z ∈ ℒ̃ brings z̄ with it, and what Roy's strong six
exponentials theorem sees is H₀ + Q̄z + Q̄z̄, of dimension five. This
batch treats two families of those spaces, in five nodes.

## What was proved

- **The configuration.** Let u ∉ Q̄ with ρ = uū algebraic, a ∈ Q̄
  non-zero, and z = u/(u² − a) if aā ≠ ρ², or z = u/(u² − a)² if
  aā = ρ². Then W = H₀ + Q̄z + Q̄z̄ contains the progression b, bu²,
  bu⁴, bu⁶, so it carries the configuration (1, u²) ⊗ (b, bu², bu⁴).
- **Invisible to Theorem B.** W contains none of u², ū² and
  1/(u − b) for algebraic b ≠ 0, so no four-dimensional H₀ + Q̄w
  inside W carries a configuration.
- **The contrast.** For aā = ρ², H₀ + Q̄·u/(u² − a) is stable under
  conjugation and carries none. The conjugate z̄ is what lets the
  strong six exponentials theorem see u/(u² − a).
- **At a candidate,** with that theorem as a hypothesis:
  u/(u² − a) ∉ ℒ̃ when aā ≠ |u|⁴, and u/(u² − a)² ∉ ℒ̃ when aā = |u|⁴.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.circle_point_conjugate_pair_configuration_invisible_to_four_dimensional_extensions` | `901396cf-2688-4738-be1c-a80b6ff6e7c7` | sketch, now Proved |
| `DiazModulus.conj_stable_circle_point_extension_no_two_by_three_configuration` | `9819e926-24a6-4c12-8431-7a5f6be68dfa` | sketch, now Proved |
| `DiazModulus.candidate_div_sq_sub_not_mem_logAlgTilde` | `35486890-e3f7-4a35-a512-441fc709f738` | sketch, now Proved |
| `DiazModulus.circle_point_conjugate_pair_extension_carries_two_by_three_configuration` | `d8abac5b-9bd4-4091-a0ed-2be61713f899` | ACCEPTED |
| `DiazModulus.circle_point_conjugate_pair_extension_excludes_squares_and_reciprocals` | `f640cf63-2fec-48d4-b85e-1eff3f39da34` | ACCEPTED |

The first three are milestones 108–110; the other two joined the
mission by import. The mirror holds all 364 results, and note
version 1.20 states the batch as Proposition 5.6 and Remark 5.7.

## How

- **Partial fractions in u².** With a′ = ρ²/ā, z̄ = −(ρ/ā)·u/(u² − a′).
  Every element of W is a constant plus u⁻¹ times a cubic in u² over
  (u² − a)(u² − a′), so b = 1/(u(u² − a)(u² − a′)) and its products
  with u², u⁴ and u⁶ lie in W. Each identity is `field_simp; ring`.
- **Parity.** Clearing denominators turns a membership into
  A(u²) + u·B(u²) = 0. The same polynomial identity holds at −u, so
  adding gives A(u²) = 0, and u² is transcendental (`expand_aeval`,
  `expand_eq_zero`). The odd part rules out u² and 1/(u − b), the
  even part ū². One lemma covers both families: it only needs
  z·Q₁(u²) = u·R₁(u²) and z̄·Q₂(u²) = u·R₂(u²) with Q₁(0), Q₂(0) ≠ 0.
- **Exchange.** If H₀ + Q̄w carried a configuration, Theorem B would
  put w in H₀ + Q̄t for one of the excluded t, and
  `mem_span_insert_exchange` would put t in W.
- **Reuse.** Conjugation-closure of ℒ̃ is cited from the published
  `DiazModulus.logAlgTilde_conj_stable`, not re-proved.

## What is not proved

- **This is not a classification.** Only two families of
  five-dimensional spaces are treated. A third one, with two
  conjugation-fixed poles, and a form that drops the conjugation
  condition were found in the literature check; neither is
  formalised.
- **The exclusions at a candidate are not new.** u/(u² − a) ∉ ℒ̃ is
  one substitution in Diaz 2004, Théorème 2 at x = (u, ū), and also
  Diaz 2007, Corollaire 4(4) and Théorème 7(1); u/(u² − a)² ∉ ℒ̃ is
  Diaz 2007, Théorème 6(3). They carry Roy's theorem as a hypothesis,
  and they are vacuous if Diaz's conjecture holds.
- **The configuration does not use all five dimensions.** Its six
  products span the four-dimensional odd part of W, which does not
  contain 1. The headline node was renamed before publication for
  that reason.
- **Only the invisibility was not found in the sources read,** and its
  proof is short: parity plus Theorem B.
- **One hypothesis is unused:** the exclusion node does not need
  aā ≠ ρ² in its first family.

## What remains open

The rest of the five-dimensional case: the third family, the smooth
scroll case of the reduction, other involutions of the u-line that
commute with conjugation, and z not rational in u. None of it touches
the two statements the development reduces Diaz's conjecture to.

## Also

A check of the dependency graph of all 383 Diaz nodes found that no
theorem outside the Diaz set cites any of them. The 19 citations by
five other users all sit inside the mission. The blueprint now also
holds the earlier results that chapter 12 listed as library-only:
chapters 13 and 14, with 18 more nodes.
