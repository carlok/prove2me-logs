# Orbits exchanged by conjugation, and the cyclic case
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-15

R12's research notes sort the conjugation-stable spaces that Theorem B
cannot see, and whose configuration has a factor of degree two, into
three families: two orbits of u ↦ −u fixed by conjugation, two orbits
exchanged by it, and a cyclic family. R14 formalised a member of the
first family and one of the second, whose orbits are 0 and ∞. This
round (R15) adds four nodes: the second family for finite orbits, and
a member of the third. Each family now has a formal member.

## What was proved

- **Orbits exchanged by conjugation.** For u ∉ Q̄ with |u| = s
  algebraic, g = a₁/(u − a) + a₂/(u + a), |a| ≠ s and a₁ ≠ a₂, the
  span of 1, u, u⁻¹, g, ḡ is stable under conjugation, spanned by a
  2×3 configuration and invisible to Theorem B. Conjugation sends the
  orbit ±a to ±s²/ā, a different one.
- **The cyclic case.** With v = u/s, G₁ = 1/(v − 1) + 2/(v + 1) and
  G₂ = 1/(v − 1)² + 1/(v − 1) − 2/(v + 1)² + 2/(v + 1), the span of
  1, u, ū, G₁, G₂ is five-dimensional and contains none of u², ū² and
  1/(u − e). It is stable under conjugation, the six products of
  (1, u²) and (ū, G₁, G₂) span it, and it is invisible. Modulo
  1, u, ū, the factor u² acts on G₁, G₂ as a Jordan block. No
  configuration in it has a Möbius ratio.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.conj_swapped_two_orbit_configuration_invisible_to_four_dimensional_extensions` | `dff5b4bf-d4b1-4857-9ee9-b28491871a77` | ACCEPTED |
| `DiazModulus.cyclic_pair_configuration_invisible_to_four_dimensional_extensions` | `c5f1b34c-b54c-4dd5-92a5-f15bf59cfcff` | sketch, now Proved |
| `DiazModulus.cyclic_pair_space_no_mobius_ratio_configuration` | `dfc3244d-f7c4-4044-affb-de9419ac2e1c` | ACCEPTED |
| `DiazModulus.cyclic_pair_space_excludes_squares_and_reciprocals` | `bea5ddb7-bcf8-4e0a-91d4-cb4cd4c65a2b` | ACCEPTED |

Milestones 134–136 are the first three rows. The mirror holds all 418
results; note version 1.28 adds them to its proposition on
configurations of degree two.

## How

- **The swapped space is a two-orbit space.** With ū = s²/u, ḡ is a
  constant plus γ/(u − b) + δ/(u + b), where b = s²/ā; and a² ≠ b²
  because aā + s² > 0. So R14's two-orbit theorem applies to g and ḡ,
  and the proof only adds the conjugation.
- **Clearing denominators.** For w in the cyclic space,
  u(u² − s²)²w is a polynomial of degree 6 in u; freeness and the
  exclusions are comparisons of coefficients. In terms of poles, an
  element with a pole at s also has one at −s.
- **No Möbius ratio.** As in R14, t, ut ∈ W forces t ∈ Q̄ + Q̄ū, here
  through an identity of degree 7. On the poles: the leading polar
  coefficients at s and −s are in a fixed ratio, 1 : −2 for double
  poles and 1 : 2 for simple ones, and multiplying by u flips its
  sign.
- Two proof agents; four files of 183 to 273 lines. On a warm cache
  each compiles in 3.8 to 5.7 seconds of CPU time (7.6 to 13 seconds
  of wall clock). The chain of the four proofs compiles unchanged on
  Mathlib v4.35.0, without a warning.

## Also

- **One tier name.** Since the morning, the blueprint's last chapter
  calls its second list "routine"; 37 node source lines and three
  remarks of the note still said "short". They now say "routine".
- **Item labels in the note.** Four propositions printed their items
  as 1., 2., while the text cites them as (1), (2) or (i) to (iv). The
  labels now match the citations.

## What is not proved

- **The classification itself.** That every such space belongs to one
  of the three families is proved in the research notes, modulo local
  cases R12 only sketched; it is not formalised. Lean has members of
  each family, not the families.
- **The cyclic family** has about five real parameters; one member is
  formalised.
- **For the swapped spaces,** no statement excludes a configuration
  with a Möbius ratio, as was done for W₁ and for the cyclic space.
- **No step towards Diaz's conjecture.** At a candidate every space
  here is already excluded by Roy's theorem.
