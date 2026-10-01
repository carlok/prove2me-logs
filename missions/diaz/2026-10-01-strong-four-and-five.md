# Strong four, sharp four, strong five

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-01

Three items were left over from the literature sweep: consequences of the
strong four and the strong five exponentials conjectures. Each conjecture is
carried as a hypothesis.

## Which strong four exponentials conjecture

Waldschmidt's 1988 Durham paper states the strong five exponentials
conjecture and calls it clearly weaker than the strong four exponentials
conjecture. The note and the mirror's README had read that as Conjecture
11.17 of his 2000 book, the hypothesis of `diaz_of_sfe`. In the 1988 paper the
phrase means something else. It is his Corollary 2.1, the sharp six
exponentials theorem, with two numbers y instead of three. His 2005 survey
calls this the sharp four exponentials conjecture: if the four numbers
e^{x_i y_j − β_ij} are algebraic, then x_i y_j = β_ij.

A new node connects the two readings. With Baker's theorem, the book's
conjecture implies the sharp form, and the sharp form implies the strong
five. The note lists three statements "in increasing strength" and had
assumed that order without a proof. It now has one.

## Waldschmidt's question on p. 399

This morning's node proved a case of a question in Waldschmidt's book:
if λ ∈ ℒ ∖ {0} and |u|, e^{uλ} are algebraic, then u ∈ ℚ or uλ/λ̄ ∈ ℚ. The
case was u ∈ ℒ̃, proved from Roy's strong six exponentials theorem and
Baker's theorem. The book says the full statement follows from the strong
four exponentials conjecture. That is now formalised, and it needs no Baker.

The draft had a second part: two candidates of equal modulus are ±u or ±ū.
It was dropped before posting. Under the strong four exponentials conjecture
no candidate exists at all, so the statement said nothing.

## (log a)(log b) ≠ log c

The plan was e^{λ²} and e^{π²}, as Waldschmidt derives them from the strong
five exponentials conjecture in 2005. The 1988 paper gives a more general
example on the same page as the conjecture: (log a)(log b) ≠ log c. The node
proves that, with his parameters, and keeps e^{λ²} and e^{π²} as its
special cases.

## One sentence for the note

Waldschmidt's book also records a homogeneous form of the conjecture on
algebraic independence of logarithms. At a generic candidate's own
logarithms u, ū and iπ that conjecture holds. The one relation such a
candidate satisfies, uū = |u|², is not homogeneous. So it cannot refute the
candidate through those logarithms either. That is what the earlier node on
homogeneous relations at (u, ū, iπ) proves, and the note now says so in one
sentence.

## Checks

Three nodes, 480 lines. Each compiled on the platform's Lean against stubs,
and on Mathlib v4.34 against the mirror's real proofs; each needed only
Lean's three axioms. A plug-in test checked that the new node's two
conclusions are, token for token, the hypotheses of the four existing nodes
on the sharp four and strong five conjectures.

## Publication

The three statements went up at 16:35 and became milestones 63–65; the
mission now has 177 members. The proofs were submitted at 16:42, and all
three were accepted by 16:48. The script that polls for verdicts recorded
none of them: its reads of the board failed for the whole hour it waited,
and it stopped at 17:46. Rerun at 19:09, it found the three verdicts,
attached the explanations and read them back.

The mirror ported the three at the first attempt and holds 307 of 307. The
companion note, version 1.15, corrects the item of its closing list that
had misread the 1988 remark, states the p. 399 question in full, and adds
the sentence on the homogeneous conjecture. Its appendix check against the
live board passed on all 109 identifiers.
