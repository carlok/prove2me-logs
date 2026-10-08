# Separation, a normal form, and Laurent hulls
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-08

A working note, drafted by another Claude session, put the rank-one
results of the past week into one mechanism over any subfield K of ℂ.
It was checked proof by proof (no mathematical error; seven fixes of
wording and scope), compared with the local sources, and ported as
eighteen nodes. One corollary of the note was dropped as trivial.

## What was proved

- **Separation.** For K ≤ F, a K-space V₀ ⊆ F and w₁, …, w_m
  algebraically independent over F, every p×q configuration over K
  (p, q ≥ 2) in V₀ + Kw₁ + … + Kw_m lies in V₀.
- **The normal form.** For u transcendental over K with uū ∈ K, the
  2×2 configurations in H₀ = K + Ku + Kū are exactly
  x = μ·P(1, u), y = μ⁻¹·Q(1, ū) with P, Q ∈ GL₂(K). With generic
  numbers added, configurations stay 2×2 inside H₀, and their constant
  terms form the invertible matrix P·diag(1, ρ)·Q. At a candidate,
  every row and column then has an entry outside the Q̄-span of the
  logarithms (with Baker's theorem).
- **Laurent hulls.** span_K{uˢ : s ∈ S}, S finite, carries a p×q
  configuration iff S contains A + B with |A| = p, |B| = q. For
  {0, ±1, ±k, ±l} with 4 ≤ k < l this happens iff
  l ∈ {k+1, k+2, 2k−1, 2k, 2k+1, 3k}; the hull of
  {0, ±1} ∪ {±4ʲ : j ≥ 1} carries none.
- **Tools.** The count of orders at 0, linear Cauchy–Davenport in K[X],
  p + q ≤ dim V₀ + 1 in K(u), and the critical 2×2 lemma.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.rank_one_config_separation` | `6412e225-68f7-4d31-b833-9e358b8177f0` | sketch, now Proved |
| `DiazModulus.circle_point_two_by_two_normal_form` | `098df255-2e44-445e-a9ed-7b42a829b29d` | ACCEPTED |
| `DiazModulus.laurent_hull_config_iff` | `183b9e0a-8947-48a2-bff4-40106fca6b4b` | sketch, now Proved |
| `DiazModulus.candidate_two_by_two_config_entry_not_mem_span_logAlg` | `b75876be-a526-429b-b5a6-8efe1b704206` | sketch, now Proved |
| `DiazModulus.power_pair_hull_two_by_three_iff` | `41b0da9a-8258-4cd0-9035-a24bd38c09d3` | sketch, now Proved |
| `DiazModulus.four_pow_hull_no_two_by_three` | `6c47ce09-6fa5-4025-90d3-ec6ef78e2208` | sketch, now Proved |
| `DiazModulus.candidate_power_pair_not_both_mem_logAlgTilde` | `3706795a-5cd8-46fe-a412-48bb68de49e7` | ACCEPTED |
| `DiazModulus.two_by_two_config_critical_progression` | `f27b3462-2ab3-4f63-9294-ba165ea51ef5` | ACCEPTED |
| `DiazModulus.rank_one_config_separation_two` | `fccd2c36-8b8a-4d53-b05f-e6d7a9c0803f` | ACCEPTED |
| `DiazModulus.polynomial_submodule_trailing_degrees_card` | `f604634b-5bd4-409c-ae3b-680a1e0bf0d4` | ACCEPTED |
| `DiazModulus.polynomial_submodule_mul_finrank_ge` | `493fa5ef-b99c-411b-8f1e-80c5901c9183` | sketch, now Proved |
| `DiazModulus.rank_one_config_card_le_finrank_add_one` | `13e9574b-ef87-4cc0-8354-7049fc6d19c6` | sketch, now Proved |
| `DiazModulus.circle_point_config_card_le_four` | `b4cc3f07-7c37-4d0b-8723-2024abea4bac` | sketch, now Proved |
| `DiazModulus.generic_circle_point_config_is_two_by_two` | `4c3f8499-e9a2-4f38-b083-0ea578528eb4` | sketch, now Proved |
| `DiazModulus.circle_point_config_constant_matrix_det_ne_zero` | `51102291-6ce5-46ee-babb-35310b185431` | sketch, now Proved |
| `DiazModulus.two_sumset_iff_difference_count` | `353f44e5-54a3-4e7c-928f-2a60c3e964ca` | ACCEPTED |
| `DiazModulus.power_pair_difference_count_iff` | `c3c5d970-67d0-41e7-a528-b46b89849269` | ACCEPTED |
| `DiazModulus.algebraic_mem_span_logAlg_eq_zero` | `1feadbfa-c58a-4f8a-b3ce-6917220d9668` | ACCEPTED |

Milestones 111–115 are the five nodes nothing else imports; the rest
joined the mission by import. The mirror holds all 382 results, and
note version 1.21 states the batch as one theorem and one proposition.

## How

- **Separation without factorising.** Write xᵢyⱼ = cᵢⱼ + ℓᵢⱼw. Only the
  leading coefficient of det(C + wL), det L = 0, is used; a non-zero
  column of L gives z with zy₁, zy₂ ∈ F, and comparing coefficients of
  w kills every row of L by the independence of y. Induction on m over
  F(w₁, …, w_{m−1}) with `AlgebraicIndependent.transcendental_adjoin`.
- **No factor lemma for the dimension bound.** Clear denominators, use
  the minor identity A_{i1}A_{1j} = A_{11}A_{ij} in K[X], and apply
  Cauchy–Davenport to the order sets
  (`cauchy_davenport_add_of_linearOrder_isCancelAdd`).
- **The normal form** factors the 2×2 polynomial matrix through a gcd
  and bounds degrees by two; 270 lines, the largest node.
- **The u^{4^j} family** by a size gap instead of the note's base-4
  digits: distinct non-zero absolute values differ by a factor of at
  least 4, so three pairs with one difference cannot fit.
- **Checks.** Six agents in parallel against built stubs; then the
  eighteen proofs chained without stubs on the mirror's library: only
  propext, Classical.choice and Quot.sound.

## What is not proved

- **No transcendence result.** Diaz's conjecture, (S) and (NT) are
  untouched; the batch is about what rank-one statements can and
  cannot reach.
- **The pairs of powers at a candidate are not new.** Each case is one
  substitution in Diaz 2007 (Cor. 2(P)(1), Th. 7(1), Cor. 5); they
  carry Roy's theorem as a hypothesis and are vacuous if Diaz's
  conjecture holds.
- **The tools are standard.** Linear Cauchy–Davenport is a case of
  Eliahou–Lecouvey, as stated by Bachoc, Serra and Zémor (2017, Th. 2);
  the critical 2×2 lemma is the dimension-2 case of their Lemmas 4–5.
- **The u^{4^j} result is about one route only.** It says Laurent
  hulls give Roy's theorem no configuration; other configurations in
  ℒ̃ are not considered.
- **Not ported:** the note's polar-divisor bound and its genus remark
  (Mathlib has no divisors on curves); the note's no-vanishing
  corollary, which holds for any configuration by independence alone.

## What remains open

Separation, the normal form and the Laurent criterion were not found
in the sources read. Nothing here narrows the gap the development
reduces Diaz's conjecture to: a 2×2 statement covering the single orbit
GL₂(Q̄)·(1, u)ᵀ(1, ū)·GL₂(Q̄), with its invertible constant matrix.
