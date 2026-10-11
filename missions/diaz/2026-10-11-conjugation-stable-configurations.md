# Conjugation-stable configurations that are not progressions
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-11

A research sprint (R10) answered the question that R9 left open: is
there a five-dimensional space W ⊇ H₀ = Q̄ + Q̄u + Q̄ū, stable under
complex conjugation, that carries a configuration which Theorem B's
four-dimensional spaces cannot see and that contains no geometric
progression? There is. The answer, with two older results from the
research notes, was formalised the same day (R11), in seven nodes.

## What was proved

- **The real pencil spaces.** Let u ∉ Q̄, s ∈ Q̄ real with s² = uū,
  λ ∈ Q̄ with |λ| = 1, and f real. The span of 1, u, ū, f and
  f/(s + λu) is stable under conjugation and carries the configuration
  (1, u) ⊗ (u⁻¹, 1, f/(s + λu)). Conversely, if 1, u, ū, g, ug are
  free and ḡ ∈ Q̄ + Q̄u + Q̄ug, then the span of 1, u, ū, g, ug is one
  of these spaces.
- **An invisible member with no progression.** For λ = 1 and
  f = u²/s² + s²/u², the space contains none of u², ū², 1/(u − b).
  So no four-dimensional space of Theorem B inside it carries a
  configuration. Its polar divisor has degree 5, so it contains no
  progression. R5's conjecture fails even for conjugation-stable
  spaces.
- **Index one is visible.** If h is a Möbius function of u, a
  five-dimensional Q̄ + Q̄u + Q̄u⁻¹ + Σ_{k≤3} Q̄ c hᵏ contains u², u⁻²
  or some 1/(u − b).
- **Two hypotheses.** Kirby's weak Schanuel conjecture for n = 2,
  together with Schanuel's conjecture over the kernel 2πiℚ for n = 1,
  implies Diaz's conjecture.
- **At a candidate**, under Roy's strong six exponentials theorem, f
  and f/(|u| + λu) are not both in ℒ̃.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.conj_equivariant_degree_one_space_eq_real_pencil_space` | `52da0e34-a456-43ea-aa23-27c31ae95cbe` | ACCEPTED |
| `DiazModulus.real_pencil_quartic_configuration_invisible_to_four_dimensional_extensions` | `a5c588d2-840c-4db0-bf64-b41a6ae70cb5` | sketch, now Proved |
| `DiazModulus.candidate_real_pencil_not_both_mem_logAlgTilde` | `b498918f-d12c-4ac9-bed4-d9fc8929e2d7` | sketch, now Proved |
| `DiazModulus.diaz_of_weak_schanuel_and_kernel_schanuel` | `858142e9-e8e2-4f63-ab8d-8f07e4dd167b` | ACCEPTED |
| `DiazModulus.mobius_progression_space_contains_square_or_reciprocal` | `5f4fe8a8-3b1c-45fa-8e8b-8db0e6e84bc3` | ACCEPTED |
| `DiazModulus.conj_stable_real_pencil_space_carries_two_by_three_configuration` | `e9964520-a9f1-44f5-b162-795fd27d47a7` | ACCEPTED |
| `DiazModulus.real_pencil_quartic_space_excludes_squares_and_reciprocals` | `19f4aca0-9d73-4c13-b43c-d9f02199b074` | ACCEPTED |

Milestones 121–125 are the first five rows. The mirror holds all 400
results; note version 1.24 states them as a new proposition and in
two updated remarks.

## How

- **No σ in Lean.** Conjugation stability only needs f to be a real
  complex number, so the statements use complex conjugation directly
  and never mention a field automorphism of Q̄(u).
- **The converse** is one conjugation applied twice. Writing
  ḡ = a + bu + c·ug and conjugating again gives |c|²s² = 1. After the
  shift g ↦ g + qū, ḡ = c·ug, and f = g(s + λu) with λ = cs is real.
- **Index one with one relation.** The research notes used a divisor
  argument (a complete linear system of degree 4). The Lean proof
  needs less. The dimension bound gives one relation c′u·p(u) = r(u)
  between the progression and H₀. An induction on deg p, cancelling
  common roots, produces the element. 346 lines, the largest node.
- **Proof agents.** Three agents wrote the seven proofs. Each proof
  matches its statement and has no `sorry`, and the stub-free chain
  on Mathlib v4.34 uses only the standard axioms.

## What is not proved

- **The candidate statement is not ours.** It is one substitution in
  Diaz 2007, Th. 7(1), and is attributed there.
- **The two-hypothesis conditional is short.** It is R7's reduction
  plus a standard step. Its second hypothesis contains the algebraic
  independence of e and π, which is open.
- **Index two is not formalised.** That the ratio field has index 1
  or 2, and the index-2 half of the classification, stay in the notes.
- **Open:** which f make the real pencil spaces visible, and whether
  every conjugation-stable invisible space whose configuration has a
  factor of higher degree is of this kind.
- **No step towards Diaz's conjecture.** These results map which
  spaces Roy's theorem can exclude at a candidate; none removes one.
