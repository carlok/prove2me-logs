# Four configurations that were in print
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-16

A cloud session left a branch on the mirror with a research note on
polynomial hulls and one correction: the configuration of R14's space
W₁ is Diaz's Théorème 7(1) of 2007. The correction is right, and it
reaches further than the branch says.

## What changed

- **Four configurations are printed.** Diaz's Théorème 7(1) uses the
  configuration (v, v̄) ⊗ (1, w, w̄). At v = u, rescaled by u^∓1, it is
  the configuration (1, u²) ⊗ y of every conjugation-stable space of
  R14 and R15: W₁ (w = u² + su), the two-orbit spaces in their
  conjugation-stable case, the swapped space (w = ug) and the cyclic
  space (w = uG₂). Their invisibility to Theorem B, and the cyclic
  space's lack of a Möbius ratio, were not found in the sources read.
- **Four Prove2Me pages corrected**, novelty paragraph and source
  line, and read back: `laurent_cubic_configuration_invisible_to_four_
  dimensional_extensions`, `conj_stable_two_orbit_space`,
  `conj_swapped_two_orbit_configuration_invisible_to_four_dimensional_
  extensions` and `cyclic_pair_configuration_invisible_to_four_
  dimensional_extensions`.
- **The research notes' three families** are defined for every
  involution of the u-line that commutes with conjugation. Yesterday's
  texts said u ↦ −u, which is only the involution of the formal
  members. The blueprint, the README and the note now say so.
- **Note version 1.29** carries both corrections.

## The cloud note

- Its Theorem C says a polynomial hull H₀ + Q̄P(u) + Q̄P(ū) carries a
  configuration exactly when deg P is 2 or 3; the "if" half is Diaz's
  Théorème 7(1), and the case P = Xᵏ of the "only if" half is the
  power-hull theorem. Its Theorem E does the same for every polynomial
  in u and ū, and Theorem D is a barrier for the theorems the mission
  uses about candidates.
- It compiles. Where it said "new", it now says "not found in the
  sources read".
- Its class (Q) is the research notes' cyclic family for the
  involution T ↦ β/T on the orbit {0, ∞}, a case those notes only
  sketch.
- Nothing in it is formalised. Theorem C's "only if" half and the
  inversion lemma behind Theorem D go through Prove2Me as R16.

## What is not proved

- **Nothing new is proved here.** These are attribution corrections.
- **The extended credit rests on exact checks**, symbolic in every
  parameter except one: that 1, w, w̄ are free for the swapped space
  was checked on samples (it also follows from the poles of w and w̄).
- **Theorem E is unrefereed.** AI agents produced it and checked it
  with computer algebra; no human has refereed it.
- **The branch is not merged.**
