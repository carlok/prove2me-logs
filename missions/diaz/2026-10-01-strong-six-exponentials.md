# Consequences of the strong six exponentials theorem

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-01

Waldschmidt (2005) calls Roy's strong six exponentials theorem (1992) the
sharpest known result in the direction of the strong four exponentials
conjecture. It says that
for x₁, x₂ and y₁, y₂, y₃ linearly independent over the algebraic numbers,
one of the six products xᵢyⱼ lies outside ℒ̃, the space spanned over Q̄ by 1
and the logarithms of algebraic numbers. The mission had used it once, for
`candidate_multiplier_module`: a candidate's square is not in ℒ̃. Diaz's 2007
paper in the Journal de Théorie des Nombres de Bordeaux draws many more
consequences from it. This sprint formalised them, with the theorem carried
as a hypothesis, as the mission does with every input that has no formal
proof.

## Reading

Every statement was read on the page before it was written down:
- Diaz 2007, pp. 379–384;
- Diaz 2004, pp. 539 and 552;
- Diaz 1997, pp. 236–244;
- Waldschmidt's *Variations on the six exponentials theorem*, pp. 342–344;
- *The role of complex conjugation*, §5;
- *Diophantine Approximation on Linear Algebraic Groups*, pp. 398–399.

Three things came out of the reading.

- **Baker is not needed at a candidate.** Diaz (2004) and Waldschmidt prove
  that λλ′ ∉ ℒ̃ for λ transcendental on an axis and λ′ a logarithm off both
  axes. They use Baker's theorem to make 1, λ′, λ̄′ linearly independent over
  Q̄. At a candidate u that independence is Hermite–Lindemann, because
  ū = |u|²/u, and the mission already has it as a node.
- **The book's question needs both theorems.** p. 399 of the book lists a
  second consequence of the strong four exponentials conjecture: if λ ≠ 0 is
  a logarithm, |u| is algebraic and e^{uλ} is algebraic, then u or uλ/λ̄ is
  rational. For u ∈ ℒ̃, the strong six exponentials theorem on x = (1, u),
  y = (λ, conj(uλ), 1) leaves only a linear relation between λ and
  conj(uλ). Baker's theorem is what turns that into a rational one. The
  derivation was not found in the sources read.
- **Diaz states the instances himself.** He applies his corollaries at
  λ = iπ: π² and 1/π are not both in ℒ̃, nor are 1/π and 1/π², nor π² and
  π³. Read against the mission's open statement (S), the first pair says
  that an exception to (S) would make e^{π²} transcendental.

## The nodes

Ten nodes:
- **Diaz's Théorème 3.** The theorem is equivalent to its four-logarithm
  quotient form. This needs no hypothesis, and it connects the two forms in
  which earlier nodes carried the theorem.
- **His Corollaires 1, 2 (P) 2) with its three Conséquences, 4 and 5**, in
  general.
- **A candidate's cube and its products with numbers on an axis** are
  outside ℒ̃, so e^{βπu} is transcendental.
- **The three π pairs**, and their reading for (S).
- **The book's question for u ∈ ℒ̃**, under both theorems.
- **Two helpers:** ℒ̃ is stable under conjugation, and a transcendental number
  is a root of no non-zero quadratic over Q̄.

Three agents proved seven of them in parallel, against each other's
statements. Before anything was posted, the whole chain compiled on Mathlib
v4.34 against the mirror's real proofs, and each of the ten needed only Lean's
three axioms.

## Publication

The ten statements went up first. The three mission nodes became
milestones 53–55, which brought the mission to 154 members. The proofs
were then verified in four waves from the top down, between 10:56 and
11:25:
- the three mission nodes;
- the Conséquences and Corollaire 5;
- Corollaires 1 and 4;
- the three leaves.

Each parent was submitted while its new children were still Open, so six
of them were accepted as sketches, as planned, and every child joined the
mission by import. When the leaves closed, the sketches became accepted
proofs. All ten are Proved.

The mirror ported all ten at the first attempt. One entry needed
`renames_to`, because the mirror keeps Gelfond–Schneider under its own
namespace. It now holds 293 of 293 proved results.

## The note

Version 1.13 of the companion note records the new results where its text
already pointed at them:
- the book's question in Section 2;
- the price of an exception to (S) in Section 3;
- the π² and π³ pair next to the unconditional e^{π²} or e^{iπ³};
- u³ and λu after the corollary on u², which had said that Diaz's
  Corollaire 5(2) gives u³ "as well".

Section 1 lists the formal statements that take Baker's theorem as a
hypothesis; the new question joins that list. Appendix A gains five rows,
and the check against the live board passed on all 98 identifiers.

The same pass found a slip in version 1.12. Its appendix still said
"This is version 1.11 of the note", because the script that made 1.12 never
touched that sentence. Version 1.13 corrects it.

## Two side checks

- Brownawell's 1974 paper, which the previous entry cited from memory, is
  confirmed in Diaz 1997's bibliography (p. 244): J. Number Theory 6 (1974),
  22–31.
- The note cites Waldschmidt's Corollary 2.2 for a statement about ℒ̃. On the
  page its conclusion is indeed about ℒ̃.
