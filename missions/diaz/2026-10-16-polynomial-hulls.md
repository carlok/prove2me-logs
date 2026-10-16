# Polynomial hulls, and a barrier
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-16

A cloud session's research note on polynomial hulls left four results
unformalised that the mission's tools could reach. This round (R16)
proves them in ten nodes.

## What was proved

- **Theorem C.** For u ∉ Q̄ with uū algebraic and P ∈ Q̄[X], the span
  of 1, u, ū, P(u) and P(u)‾ carries a 2×3 configuration exactly when
  deg P is 2 or 3. So at a candidate, Roy's theorem excludes P(u)
  through its own hull in those degrees and in no others. The case
  P = Xᵏ is the mission's power-hull theorem.
- **Real polynomials in Re u and Im u** with algebraic coefficients
  carry no configuration in their hull. Roy's theorem cannot exclude
  (Re u)² or Re u · Im u one number at a time.
- **Adjoining a generic point and its inverse.** Over subfields K ⊆ F,
  a configuration in V₀ + Ku + Ku⁻¹, with V₀ ⊆ F and u transcendental
  over F, has its products in V₀.
- **A barrier.** Under Roy's theorem, ℒ̃ + Q̄u + Q̄ū carries no
  configuration when uū is algebraic and u is transcendental over the
  field of ℒ̃: Roy's theorem alone cannot refute such a point.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.polynomial_hull_two_by_three_configuration_iff` | `17c20a1d-c0b5-45a0-a8c7-bc6a564ad926` | sketch, now Proved |
| `DiazModulus.real_polynomial_hull_no_two_by_three_configuration` | `5522d7c1-37d5-462c-bbb4-10356969dc24` | ACCEPTED |
| `DiazModulus.logAlgTilde_adjoin_circle_point_no_two_by_three_configuration` | `a9928ead-a08c-4806-bf98-12eadd4e0808` | sketch, now Proved |
| `DiazModulus.polynomial_hull_no_two_by_three_configuration` | `87a6c7b0-c6f8-41f2-ae69-b8fe54a02fa9` | sketch, now Proved |
| `DiazModulus.rank_one_config_inverse_adjoin` | `2b48a58c-dbe5-48ba-92e4-af1c01de5be3` | sketch, now Proved |
| `DiazModulus.config_shifted_polynomial_spans` | `b54c411d-622a-4c97-8c55-51676e45fce0` | ACCEPTED |
| `DiazModulus.five_point_sumset_rigid` | `d4afe990-7edc-4c6f-ac8e-7c681c9585a9` | ACCEPTED |
| `DiazModulus.polynomial_submodule_degrees_card` | `f20af94c-8f92-4d07-8838-cab4283833a0` | ACCEPTED |
| `DiazModulus.rank_one_polynomial_matrix_factor` | `f74e3c82-c115-4080-9a85-c16721ed20da` | ACCEPTED |
| `DiazModulus.shifted_polynomial_hull_orders` | `bf29ff12-d2bb-498d-8123-688a1fae9100` | ACCEPTED |

Milestones 137–139 are the first three rows. The mirror holds all 428
results; note version 1.30 states them as one proposition.

## How

- **Two valuations at once.** Multiplying a configuration by uᵏ turns
  it into two spaces of polynomials whose products lie in P₀ times the
  shifted hull. Orders at 0 and degrees both add along products, and
  each space has as many orders, and as many degrees, as its dimension.
  The order sets of the hull are {−k, −1, 0, 1, m}, and a sumset of
  sizes 2 and 3 inside such a set is rigid: m = 2 and {−1, 0, 1, 2}.
  Applied to the orders and to the reflected degrees, this gives a
  product whose order exceeds its degree.
- **The barrier** writes u·xᵢyⱼ as a quadratic over F, factors the
  rank-one matrix of these quadratics, and shows that a non-zero
  constant coefficient would make x or y dependent; swapping u and u⁻¹
  removes the leading ones. Unlike the note's proof, it does not need
  the factor to be coprime.
- Six proof agents; ten files of 39 to 275 lines, each compiling in 2
  to 6 seconds of CPU time. A literature agent checked the note's
  claims against the local copies of Diaz, Roy, Waldschmidt and Bachoc,
  Serra and Zémor. It found nine attribution and wording problems in
  the note: eight are fixed, and one citation title waits for Carlo.

## What is not proved

- **Theorem E**, the note's classification of every polynomial in u
  and ū, is not formalised and has not been refereed by a person.
- **The rest of the note's barrier** (Baker's and Gel'fond–Schneider's
  theorems, the six exponentials theorem over Q and the four
  exponentials theorem in transcendence degree one, in the same model)
  is not formalised.
- **All ten results are routine** by the blueprint's rubric: the
  configurations of degrees 2 and 3 are Diaz's, and the converse uses a
  printed valuation method.
- **No step towards Diaz's conjecture.** The results say what Roy's
  theorem cannot do.
