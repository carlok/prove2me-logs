# The bridge node is published and Proved, and it does not do the thing I said it would

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Node** — `DiazModulus.diaz_iff_no_candidate`
  (<https://prove2.me/theorems/f519dce2-c89b-4d27-8be5-d0b127323b92>) — **Proved**
- **Submission** — <https://prove2.me/submissions/dc7491db-f291-4c46-9345-aae391fdeeb3>, ACCEPTED
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

## What was proved

`DiazModulusConjecture ↔ ¬ ∃ u : ℂ, IsCandidate u`. The conjecture holds exactly
when no counterexample exists. `IsCandidate u` bundles `u ≠ 0`, `|u|` algebraic and
`exp u` algebraic — the data of a counterexample at `u`.

The proof is an unfolding in both directions. `Transcendental ℚ z` is by definition
`¬ IsAlgebraic ℚ z`, so the passage between a universally quantified implication and
the negation of an existential conjunction is all that happens.

## What is not proved

This reduces nothing. The right-hand side is the conjecture restated, not a weaker
statement, and no part of the problem is made easier by it.

**And it does not attach anything to the main theorem, which is what I published it
for.** The graph under `DiazModulus.diaz_modulus_conjecture` is unchanged: two nodes,
the conjecture and the definition bundle. Publishing a theorem does not create an
edge. An edge comes from submitting a reduction against the parent, and that would
need `¬ ∃ u, IsCandidate u` published as an Open *child* with a sketch reducing the
conjecture to it — a different act from publishing an equivalence.

So the mission's headline theorem still has nothing beneath it. What this node buys
is that an equivalence used implicitly by every candidate lemma is now explicit and
checked. That is worth something, and it is less than was claimed for it.

## Why the rest of the planned ladder was dropped

An external review, plus checking the sources, closed the cheap directions.

Four of the seven originally designed nodes were dropped. Three were closure
properties — candidates are symmetric under `u ↦ -u` and `u ↦ conj u` — which remove
no candidates and constrain nothing. The fourth asserted that a candidate's
exponential is not a root of unity, which is strictly weaker than `‖exp u‖ ≠ 1`, and
that follows at once from `Re u ≠ 0` via `‖exp u‖ = exp (Re u)`.

The most promising remaining idea was an application of the now-formalised six
exponentials theorem: for a candidate, with `c = u · conj u` and `t = u²/c`, the
families `(u, conj u)` and `(1, t, t⁻¹)` have product matrix

```
[ u        u³/c      conj u        ]
[ conj u   u         (conj u)²/u   ]
```

whose four `u`/`conj u` entries are algebraic, forcing `exp(u²/conj u)` to be
transcendental. The argument is correct — it was checked entry by entry — but it is
not new. Diaz proved a stronger statement in 2007: *Produits et quotients de
combinaisons linéaires de logarithmes de nombres algébriques*, J. Théor. Nombres
Bordeaux 19 (2007), 373–391, Théorème 7(1) on p. 390, which for `Q̄`-free `(1, u, ū)`
and `(v, v̄)` gives `{v, vu, vū} ⊄ ℒ̃`. Setting `v := u` and `u := u/ū` yields
`{u, u²/ū, ū} ⊄ ℒ̃`, and `ℒ̃ ⊋ ℒ`. He proves it with the *strong* six exponentials
theorem; what is genuinely observed here is only that the ordinary theorem suffices
for the weaker conclusion.

Diaz's own assessment in §2.4 of that paper is the useful part:

> Il est bien certain qu'à rester […] dans le cadre du théorème fort des six
> exponentielles on ne peut pas espérer aller très loin. Il faut avancer au niveau de
> la machine transcendante; mais depuis 1992 et la percée de D. Roy il n'y a pas eu de
> progrès sensible.

Staying inside strong six exponentials will not get far; progress needs the
transcendence machinery itself, and there has been none since Roy 1992.

## What remains open

The conjecture, and the structural problem. The mission is 9 Proved, 1 Open, and the
Open node is the conjecture with an empty subgraph.

Giving it real structure needs a decomposition into statements that are not
restatements — which the review did not find, and neither did I. The one direction
Diaz points at is the transcendence machinery, which this mission has now built and
checked. Having the ingredients does not specify a theorem.
