# The progression spaces, classified
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-12

R8 classified, on paper, the five-dimensional spaces
W = Q̄ + Q̄u + Q̄u⁻¹ + Σ_{k≤3} Q̄ c hᵏ that contain a four-term geometric
progression. Its index-one half was formalised on 11 October (R11).
This round (R13) formalises the rest, in three nodes. A research
block (R12) answered the questions R10 and R11 had left open.

## What was proved

- **The ratio has degree at most 2.** Let h = p(u)/q(u) with p, q
  coprime and not both constant, c ≠ 0, and W five-dimensional. Then
  max(deg p, deg q) ≤ 2.
- **Degree 2 gives the involution spaces.** If the maximum is 2, W is
  the space of R9 for the pencil Q̄p + Q̄q, with some non-zero l₁, l₂ in
  the pencil.
- **The classification.** W contains u², u⁻² or some 1/(u − b), or W
  is one of R9's involution spaces. Degree 1 is R11's index-one node.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.progression_space_contains_square_or_reciprocal_or_eq_involution_pencil_space` | `d2501f32-e51d-4d24-be11-d86a26332da9` | sketch, now Proved |
| `DiazModulus.progression_space_ratio_degree_le_two` | `36e45dbf-d812-422f-8517-c1a21fd08d3f` | ACCEPTED |
| `DiazModulus.quadratic_ratio_progression_space_eq_involution_pencil_space` | `fed2dbdb-56de-4027-a142-5ac1990bb701` | ACCEPTED |

Milestone 126 is the first row. The mirror holds all 403 results;
note version 1.25 makes Remark 5.10 formal for a rational ratio.

## How

- **Degree bound.** Mathlib's proof of Lüroth's theorem contains the
  degree formula [K(X) : K(f)] = max(deg p, deg q). Two independent
  elements of the progression part that also lie in Q̄ + Q̄u + Q̄u⁻¹
  have a ratio of u-degree at most 2 inside Q̄(h); the tower law does
  the rest. Lüroth's theorem itself is not used.
- **Degree 2 without factoring cubics.** Two relations c u φᵢ(h) =
  Rᵢ(u) with deg Rᵢ ≤ 2; after removing gcd(φ₁, φ₂), the associated
  binary forms are coprime, which forces c u g(h) = κ q(u) with
  deg g ≤ 2. Splitting g gives the two pencil members.
- 252, 422 and 106 lines; each compiles in under ten seconds.

## Research (R12), notes only

- A configuration factor of degree 3 or more cannot occur in such a
  five-dimensional space.
- Degree 2 does occur in Case II. The simplest example is
  span(v⁻¹, 1, v, v³ + v², v⁻³ + v⁻²) with (1, v²) ⊗
  (v⁻¹, v + 1, v⁻³ + v⁻²): stable under conjugation, invisible to
  Theorem B, with no factor of degree one. So the answer to R10's
  question "is every such space of degree-one type?" is no.
- W(λ, f) is visible exactly when it is a complete linear system
  (polar degree 4).
- None of this was found in the sources read; it is short.

## What is not proved

- **The progression step stays on paper.** That a configuration whose
  products span four dimensions is a progression is Bachoc, Serra and
  Zémor (2017), Lemma 4; the Lean statements take the progression as
  a hypothesis.
- **The ratio is assumed rational in u**, as in R8; it does not follow
  from the dimension alone.
- **R12 is not formalised.** Its claims are labelled proof, sketch or
  conjecture in the notes, with exact checks.
- **No step towards Diaz's conjecture.** At a candidate every such
  space is already excluded by Roy's theorem.
- **A toolchain bump was reverted.** Mathlib v4.34.1 changed only the
  Lean version, but CI's export checker has no v4.34.1 build, so the
  mirror stays on v4.34.0 until v4.35.0.
