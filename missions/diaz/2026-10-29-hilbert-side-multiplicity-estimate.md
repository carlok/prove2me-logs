# Hilbert functions for the multiplicity estimate
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-29

Roy's theorem is now proved from one hypothesis, hME, an elementary
multiplicity estimate. This round (C1.1) proves the Hilbert-function
layer that a proof of hME needs: 30 nodes and one definition. It works
at finite level only, with inequalities between dimensions of boxes
of polynomials, and no Hilbert polynomials.

## What was proved

- **Hilbert functions of filtrations.** Rank–nullity, monotonicity,
  translates, and the sum bound over ideals that pairwise separate
  (C1, C2), for any filtration of a commutative algebra.
- **The chain bound** (DALAG Th. 8.8, at finite level). If every prime
  over (ps₀) + (V) has height at least |ps₀| + r, then
  2^{r(r−1)/2} uʳ h_{(ps₀)+(V)}(uD) ≤ h_{(ps₀)}(2ʳ uD). It assumes
  Macaulay unmixedness as an explicit hypothesis, hU.
- **The torus model** of 𝔾ₐ^{A₀} × 𝔾ₘ^{A₁}, inside K[X, Y, Z]:
  - reduced monomials give a basis modulo (YᵢZᵢ − 1), over any field;
  - the torus generators form a weakly regular sequence;
  - translations act by automorphisms;
  - the Hilbert function of the torus on a box is the exact count.
- **The Hilbert side of hME.** On hME's boxes,
  λ·2^{r(r−1)/2} ≤ 2^{rd} D₀^{d₀} (2D₁)^{d₁}, under hU.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.torus_hilbert_side` | `39150e2c-013e-4f31-9f09-52f18c2cd231` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.le_hME_constant` | `4bf0048f-e5f2-49db-be46-bd3dc458f192` | ACCEPTED |
| `DiazModulus.exists_card_mul_boxHilb_le_translates` | `c5e44038-0aa5-4a61-8975-bed482e17f60` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.torus_coeff_poly` | `933cb638-27e5-431a-945b-80dac0905c2f` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.exists_translation_algEquiv` | `8d749754-5bc6-4c85-854c-2e0115d34b6a` | ACCEPTED |
| `DiazModulus.exists_boxHilb_family` | `dbf4245c-31dc-4084-abb9-a8fd13a06b85` | ACCEPTED |
| `DiazModulus.box_ray_lower_bound` | `9b192530-242a-417d-8ef9-1d4b8db171fe` | ACCEPTED |

Milestones 163–169 are the seven rows, the roots of the import graph;
the other 23 nodes joined by import. The vocabulary is the definition
`DiazHilbertBox`, `7d734b18-096d-492f-9219-32d4489bc1bc`. All 30 are
Proved: 19 were accepted outright, and 11 were sketches that upgraded
when their children closed.

## How

- Two designs and a synthesis; six parallel proof agents, 5 to 13
  minutes each. The proofs came in far under the planned lengths:
  about 2,000 lines against 3,280.
- Every node was checked against its statement with sorry = 0, and a
  chain with no stubs builds on the platform's toolchain using only
  the standard axioms.
- An infinite field is assumed only where prime avoidance needs it.
- The mirror holds the 30 nodes and the definition, as
  `Diaz/HilbertBox.lean`; all build on Mathlib v4.35.0 and use only the
  standard axioms.

## What is not proved

- **Unmixedness (hU), here.** It is a hypothesis of the chain bound
  and of the Hilbert side. Round C1.2, later the same day, proves it
  for polynomial rings over an algebraically closed field: see
  [the next entry](2026-10-29-unmixedness-polynomial-rings.md).
- **hME itself.** C1.1 gives its Hilbert side only. The multiplicity
  side, and the assembly, are round C1.3.
- **No Hilbert polynomials.** Eventual polynomiality is not proved and
  not needed.
- **Nothing here is claimed as new.** The results are finite-level
  forms of DALAG Ch. 5 and 8 (Ch. 8 by D. Roy); none was found in this
  form in the sources read, and all are routine.
