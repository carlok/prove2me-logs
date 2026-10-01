# Where the strong six exponentials route stops, and Roy's lemma

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-01

The morning's sprint had left a question open. Roy's strong six exponentials
theorem keeps a candidate's square and cube out of ℒ̃. Does it also keep out
u⁴?

## The question about u⁴

At a candidate u, ℒ̃ contains 1, u and ū = |u|²/u. If it contained u⁴, it
would contain ū⁴ too. A refutation through u's own data is a configuration
of the theorem inside the span of u^{±4}, u^{±1} and 1: two independent
numbers x₁, x₂ and three y₁, y₂, y₃, all six products in that span.

None exists. In general, for transcendental u and every k ≥ 1, such a
configuration exists exactly when k = 2 or k = 3. The proof multiplies
through by u^k, so that the products become polynomials supported on
{0, k−1, k, k+1, 2k}. The two rows of a configuration then differ by a fixed
shift of their orders at 0. For k = 1 and every k ≥ 4, no shift keeps three
exponents of that set inside it, and three independent polynomials need
three.

So the route stops at u³. This does not say that u⁴ ∈ ℒ̃ is consistent with
the theorem: a configuration could still use logarithms that have nothing to
do with u. Diaz remarks, at the end of the same 2007 section, that inside
the strong six exponentials theorem one cannot hope to go very far. This is
one precise instance of that remark, and it was not found in the sources
read.

## The rest of Diaz's section

The same reading showed that the morning's list of what remained in Diaz
2007 §2 was incomplete. It named Corollaire 3 (Q). Théorèmes 4 to 7 and
Corollaires 6 and 7 were missing from it. All of them are now formalised,
the parts that need it with Baker's theorem as a second hypothesis. Among
them:
- Théorème 7: u, u² and u³ are not all in ℒ̃;
- Corollaire 7: if τ or 1/τ lies in ℒ̃, then e^{2iπτ} and e^{−2iπ/τ} are not
  both algebraic. That is the conclusion of Diaz's modular statement (C4) of
  1997, under that extra hypothesis.

One example the paper gives for Corollaire 3 (Q), (1+i)/π ∉ ℒ, needs neither
theorem: it is a case of Diaz's own Théorème 4 of 2004.

## Roy's lemma, and a barrier in every size

Dasgupta and Kakde's Matrix Coefficient Conjecture says that a singular
square matrix of logarithms has a vanishing coefficient after a rational
change of basis. At n = 2 it is equivalent to the four exponentials
conjecture. The note already shows that the four exponentials conjecture
cannot detect a generic candidate through its homogeneous data: no 2×2
configuration fits.

The same now holds in every size. At a generic point of the circle, every
singular n×n matrix with entries in ℚu + ℚū + ℚiπ has non-zero rational v, w
with ⟨w, Mv⟩ = 0, and likewise over Q̄. Two steps:
- **Roy's lemma**, their Theorem 2.2: over an infinite field, a linear space
  of singular matrices has a common annihilating pair.
- **No homogeneous relation of any degree** holds at (u, ū, iπ).

The literature check found both in Waldschmidt's book, in other forms:
- the lemma, strengthened, as Proposition 12.5, credited to Roy (1990);
- the second step as an instance of Proposition 12.13.

It also found, on p. 437, the record of a conjecture, Property
(A B; C 0) for (ℚ, ℂ, ℒ), that for square matrices implies the Matrix
Coefficient Conjecture.

## Checks

Eleven nodes, 1,632 lines. All compiled on the platform's Lean against
stubs. The whole chain compiled on Mathlib v4.34 against the mirror's real
proofs, and each node needed only Lean's three axioms.

The v4.34 check caught one thing the platform's version would not have. The
newer Mathlib makes the algebra behind MvPolynomial a structure with a field
`coeff`, so `MvPolynomial.coeff` no longer exists there. The proof now uses
`P.coeff m`, which reads the same on both versions.

The leak scan caught a private file path in one proof's comment before
anything was posted.

## Publication

The eleven statements went up first, and the seven nodes that nothing else
imports became milestones 56–62. With the four nodes that joined through
them, the mission now has 174 members. The proofs
were verified in three waves from the top down, between 14:35 and 15:00.
Four parents were accepted as sketches, as planned, and became accepted
proofs when their leaves closed. All eleven are Proved and in the mission.

The mirror ported all eleven at the first attempt and holds 304 of 304. The
companion note, version 1.14, records the barrier in every size next to
its 2×2 case, and the limit at u³ next to the corollary on u². Its appendix
check against the live board passed on all 106 identifiers.
