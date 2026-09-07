# The Diaz mission is live, and its headline theorem has nothing underneath it

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

The proposal submitted earlier was approved at 14:22 UTC. It is now a public
mission of type `OpenProblem`, filed under Number Theory:
<https://prove2.me/missions/3045e100-83a7-4863-9c02-21f90105f182>.

The question is Guy Diaz's, from 2004, and still open: if `|u|` is algebraic
and `u ≠ 0`, is `e^u` transcendental? Note `e^u`, not `e^{|u|}` — the latter
follows immediately from Hermite–Lindemann, and the whole difficulty is that
`u` itself need not be algebraic.

## What was proved

Nothing new here. This entry records the approval and, more usefully, an
honest look at what the mission offers somebody arriving at it cold.

Six of the nine items are Proved: `logAlg_conj_stable`, `conj_eq_norm_sq_div`,
`hermite_lindemann_holds`, `diaz_on_axes_of_hermite_lindemann`,
`diaz_of_schanuel`, and
`diaz_of_strongFourExponentials_and_hermite_lindemann`. One is a definition.
Two are Open.

## What is not proved

Both Open nodes are out of reach for a casual contributor, and one of them is
worse than it looks.

`DiazModulus.six_exponentials`
(<https://prove2.me/theorems/7d362030-8eff-4aa9-8138-7b9b15cda0be>) at least
has a decomposition: the `SX` ladder is attached beneath it, four rungs, of
which `SX.eq_zero_of_expSum_vanishes` is now Proved. The other three are
Siegel's lemma, the Schwarz–Liouville descent, and the criterion that assembles
them. Each is a serious piece of work, and the descent in particular needs
analysis that Mathlib does not have at this revision.

`DiazModulus.diaz_modulus_conjecture`
(<https://prove2.me/theorems/ba87d640-a434-4533-84f9-257c023754c3>) has **no
decomposition at all**. Its graph is two nodes: the theorem and the definition
it depends on. The six proved reductions are conditional siblings —
`Schanuel → Diaz`, `SFE + HL → Diaz`, and so on — not children, so none of them
opens a path into the conjecture itself.

The practical effect is that the mission's only entry points are "formalise the
six exponentials theorem" and "settle a twenty-two-year-old open problem".

## What remains open

The mathematics, obviously. But the actionable gap is structural: the main
theorem needs a decomposition with a spread of difficulty under it, the way
`six_exponentials` has the `SX` ladder. Published children sized for a single
sitting are what actually attracts contributors — the two cases where somebody
else closed one of our nodes, Shuze Chen on the Smale's Ninth Farkas
certificate and foos on the Markov CLT covariance lemma, were both nodes small
enough to pick up and finish.

A mission whose smallest open item is a research programme gets read and not
worked.
