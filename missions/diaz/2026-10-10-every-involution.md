# Every involution of the u-line
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-10

A research sprint (R8) asked which five-dimensional spaces
W ⊇ H₀ = Q̄ + Q̄u + Q̄u⁻¹ of rational functions of u carry a
configuration that Theorem B's four-dimensional spaces cannot see. Its
main answer was formalised the same day (R9), in four nodes.

## What was proved

- **Every involution.** A Möbius involution τ of the u-line is given
  by its pencil: coprime quadratics q₁, q₂, one of degree 2. For
  non-zero l₁, l₂ in the pencil, the space
  H₀ + Σᵢ Q̄ q₁(u)ⁱq₂(u)³⁻ⁱ/(u l₁(u) l₂(u)) carries a 2×3
  configuration, the progression with ratio q₁(u)/q₂(u). It contains
  none of u², u⁻², 1/(u − b), so no four-dimensional space of Theorem
  B inside it carries one. The involution u ↦ −u is the two-pole family
  of 9 October.
- **A configuration that is not a progression.** Q̄u⁻¹ + Q̄ + Q̄u +
  Q̄u³ + Q̄u⁴ is spanned by the products of (1, u) and (u⁻¹, 1, u³) and
  contains none of those elements either.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.involution_pencil_configuration_invisible_to_four_dimensional_extensions` | `542ffb79-4eab-4af6-a4b2-041826f79ece` | sketch, now Proved |
| `DiazModulus.laurent_case_two_configuration_invisible` | `7527a895-a765-4126-bd2b-4e5db48f206e` | ACCEPTED |
| `DiazModulus.involution_pencil_space_carries_two_by_three_configuration` | `b372d03d-7bb5-469f-93a0-efc25a44f423` | ACCEPTED |
| `DiazModulus.involution_pencil_space_excludes_squares_and_reciprocals` | `212fc5e4-7258-42d6-acf0-73a839f920c5` | ACCEPTED |

Milestones 119–120 are the first two rows. The mirror holds all 393
results; note version 1.23 states them as Theorem 5.9 and Remark 5.10.

## How

- **The involution, explicitly.** With A, B, Γ the Plücker coordinates
  of the pencil and D = A² + BΓ ≠ 0, τ(X) = (AX + B)/(ΓX − A), and
  (Γu − A)²q(τu) = D q(u) on the pencil. No fixed points are needed.
- **A membership becomes one identity** N(u)L(u) = (u − β)(QL + S)(u)
  with N(β) ≠ 0. As u is transcendental it also holds at τ(u);
  eliminating S forces β to be a fixed point of τ and then D = 0.
  333 lines, the largest node.
- **Research side (R8, proved in the notes).** If the ratio of the
  progression generates Q̄(u), the space is a complete linear system of
  degree 4 and always contains u², u⁻² or some 1/(u − a). Otherwise the
  ratio field has index 2, it belongs to an involution, and the space
  is the one above.

## What is not proved

- **The converse is not formalised.** That every invisible space with
  a progression has this form is proved in the research notes (Lüroth,
  the index, a complete-linear-system lemma), not in Lean.
- **The progression step is known.** A 2×3 configuration whose
  products span four dimensions is a progression: Bachoc, Serra and
  Zémor (2017), Lemma 4.
- **Nothing at a candidate is new.** The exclusions these spaces give
  under Roy's theorem are substitutions in Diaz 2007, Th. 7(2).
- **No step towards Diaz's conjecture.** A by-product of R8: the
  "one more certified product" ask recorded in September cannot be met,
  by Diaz 2004, Th. 2 itself.
- **Open:** whether a conjugation-stable invisible space whose
  configuration is not a progression exists.
