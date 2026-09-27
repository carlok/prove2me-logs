# Twenty-one milestones, and a note checked against its own nodes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1)
- **Date** — 2026-09-25

Most of the mission's formal work sat outside the mission: 195 proved
results of the Diaz work were not among the mission's 81 theorems,
because a node joins a mission only when an accepted proof of a member
imports it. The platform's guide for captains names a second way
in: milestones, which for an open problem should include the significant
results of the literature, formalised. An agent read the 195 outside
results against the published literature and the companion note, and
Carlo reviewed its list before anything was linked.

## What changed

- **Milestones.** 21 theorems were linked: 4 results from the literature,
  14 statements of the companion note, and 3 theorems already in the
  mission, `four_exponentials_trdeg_one` first among them. The mission
  went from 81 to 99 theorems and from 5 to 26 milestones.
- **Seven source lines.** Two cited a §5.1 that Diaz's 2007 paper does not
  have: the modulus conjecture is §5.1 of Diaz 2004 (J. Théor. Nombres
  Bordeaux 16, 535–553). Three gave the 2004 title with the 2007 volume
  and pages. Two cited "Corollary 7" of an unpublished note, which is
  Theorem 5.1 of the public companion note.
- **Three milestone texts.**
  - The Schanuel milestone said Diaz asserts the implication in one
    sentence; Diaz 2004 states it as Proposition 1 and proves it on
    pp. 550–551.
  - The strong four exponentials milestone cited p. 15 of Waldschmidt's
    book, where the ordinary conjecture is applied; the implication is on
    p. 399, credited to Diaz 1997.
  - The six exponentials milestone cited Theorem 1.12, the general d × ℓ
    statement, while describing the 2 × 3 case.
- **Companion note v1.9.** Appendix A was compared with the Lean
  statements one by one. Four rows (Proposition 5.9, Theorems 6.1 and
  6.12, Corollary 6.13) now read "Proved, assuming Baker": their nodes
  take Baker's theorem, or its instance at u and ū, as an explicit
  hypothesis, and Section 1 now lists Baker's theorem as a third input
  used without proof. Corollary 3.4 is marked Not formalised, since no
  node states it. Proposition 3.2 is restated as its node proves it. All
  81 identifiers match the platform. Release `note-v1.9` of
  `carlok/diaz-modulus-lean` carries the PDF.

## What the leaderboard counts

It did not move. Before and after the links, carlok had 55 accepted
solutions and 73 submitted problems on the mission board, although the
mission had grown by 18 theorems, all of them his and all proved.

The counts fit one rule exactly. Each column equals the number of member
theorems minus those that were already Proved when they joined: the 21
milestone theorems, and the five nodes of the third size wave that joined
through a second proof after being proved themselves. Nodes of the four
exponentials subtree, published before their parent's sketch but still
Open when it was accepted, are counted in both columns. So a theorem
scores on the mission board only if it joins while Open.

Milestones therefore put results into the mission and its graph, not
into its score. New work counts only if it is published top-down: a
parent's proof first, accepted as a sketch while its new children are
Open, so that they join before they are proved. The fourth size wave is
published in that order.

## What is not proved

- Nothing new is proved here. Every linked theorem was already Proved;
  a link is Carlo's statement that the formal statement matches its
  source.
- The rule above is inferred from the counts, not documented. It fits
  both columns with no exception, but the platform could change it.
- The library has no proof of Baker's theorem. Four statements of the
  note are proved only with it as a hypothesis; on the board it is Open
  as `Schanuel.baker_linear_forms_in_logarithms`.

## What remains open

The statements of ten more nodes still carry stale wording: "unpublished
manuscript", "Corollary 7", "possibly known", a LaTeX label, and one
"New result" whose content is the case d = ℓ = 2 of Théorème 0.1 of Roy
and Waldschmidt (1997). Corrections are drafted and wait for Carlo's
review. About a hundred other Diaz nodes use similar wording.
