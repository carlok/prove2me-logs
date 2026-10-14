# Case II beyond degree one
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-14

R12, a research block of 12 October, answered the two questions R11
left open: which real pencil spaces W(λ, f) Theorem B sees, and whether
every conjugation-stable space it misses has a configuration factor of
degree one. This round (R14) formalises its answers in eleven nodes.

## What was proved

- **A space with no factor of degree one.** For u ∉ Q̄, s real
  algebraic with s² = uū and F = u³/s³ + u²/s², the span of
  1, u, ū, F, F̄ is stable under conjugation, the six products of
  (1, u²) and (ū, u + s, F̄) span it, and it is invisible to Theorem B.
  No configuration in it has a Möbius ratio, so it is none of R11's
  real pencil spaces. R10's question has answer no.
- **Two orbits of u ↦ −u.** The span of 1, u, u⁻¹,
  α/(u − a) + β/(u + a) and γ/(u − b) + δ/(u + b) carries a spanning
  configuration with factor (1, u²) and is invisible when α ≠ β or
  γ ≠ δ; with |a| = |b| = |u| and β/α, δ/γ real it is stable under
  conjugation. α = β, γ = δ is R7's two-pole family.
- **No factor of degree three or more.** If 1, u, u⁻¹ lie in the
  span of c, ch, ch², ck, chk and h = p(u)/q(u), then
  max(deg p, deg q) ≤ 2.
- **Visibility for Laurent f.** For a real Laurent polynomial f of
  width k in u/s, W(λ, f) is invisible when k ≥ 3, or k = 2 and
  f(−λ̄) ≠ 0, and contains u² and ū² when k = 2 and f(−λ̄) = 0.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.laurent_cubic_configuration_invisible_to_four_dimensional_extensions` | `f71c2dff-fe3c-4f65-9b0e-bac9bb16375a` | sketch, now Proved |
| `DiazModulus.laurent_cubic_space_no_mobius_ratio_configuration` | `83ef8e17-9cee-499c-871e-9c3bf39f1396` | ACCEPTED |
| `DiazModulus.two_orbit_configuration_invisible_to_four_dimensional_extensions` | `41926461-6ec2-4a66-be33-2dddce6c8db1` | sketch, now Proved |
| `DiazModulus.conj_stable_two_orbit_space` | `443a680e-ccae-4356-a4ca-0f724e487350` | ACCEPTED |
| `DiazModulus.progression_pair_span_ratio_degree_le_two` | `ca324ec5-c275-4cf4-b1bb-b71de0e7c2d1` | sketch, now Proved |
| `DiazModulus.laurent_real_pencil_configuration_invisible_to_four_dimensional_extensions` | `818db686-8350-40ab-a7b8-250bc1d48c77` | sketch, now Proved |
| `DiazModulus.laurent_real_pencil_space_contains_square_of_root` | `ae727e89-8d03-47a2-a317-c5ad17b15d54` | ACCEPTED |
| `DiazModulus.laurent_cubic_space_excludes_squares_and_reciprocals` | `ba964399-75db-4df3-b4d8-a98ddf919fe7` | ACCEPTED |
| `DiazModulus.laurent_real_pencil_space_excludes_squares_and_reciprocals` | `e8931168-fed9-411b-b9c9-9b93486be31b` | ACCEPTED |
| `DiazModulus.quadratic_over_ratio_of_mem_progression_pair_span` | `e75901ad-2b66-468f-9ffb-ad07ba72742b` | ACCEPTED |
| `DiazModulus.two_orbit_space_excludes_squares_and_reciprocals` | `5a9b5afc-69d3-4c6a-bcd2-985fa5af1bc7` | ACCEPTED |

Milestones 127–133 are the first seven rows. The mirror holds all 414
results; note version 1.26 states them as a proposition and a remark.

## How

- **No Möbius ratio without dividing.** If x₂(γu + δ) = x₁(αu + β),
  then c = αx₁ − γx₂ is non-zero and t = c·y satisfies t, ut ∈ W₁.
  Every such t lies in Q̄ + Q̄ū, which cannot hold three free values.
- **Residues.** One lemma reads a vanishing combination of 1, u, u⁻¹
  and simple fractions at each pole; it gives freeness and every
  exclusion for the two-orbit spaces.
- **The degree bound** is linear algebra over Q̄(h): three vectors in
  a plane give a quadratic relation through their 2×2 minors; then the
  degree formula of Mathlib's Lüroth file.
- **Laurent f of any width.** Multiplying a membership by
  s·vᵏ(1 + λv) with v = u/s gives a polynomial identity; its degree,
  and its values at 0 and at −λ̄, kill the two coefficients that
  matter.
- Four proof agents; eleven files of 76 to 287 lines, each compiling
  in under 15 seconds.

## What is not proved

- **A statement error, caught before publishing.** In one generated
  statement a bound variable named b captured the parameter b of the
  two-orbit space and made the clause false; the proof agent found a
  counterexample. The variable was renamed before anything was posted.
- **The general visibility criterion** (W(λ, f) is visible exactly
  when it is a complete linear system) and the normal forms of the
  degree-two case stay in the research notes.
- **The shape c·span(1, h, h², k, hk)** is derived from a
  configuration in the notes, not in Lean; the Lean statement takes
  it as a hypothesis.
- **The orbit-swapping case** of the conjugation-stable two-orbit
  spaces is not formalised.
- **No step towards Diaz's conjecture.** At a candidate every space
  here is already excluded by Roy's theorem.
