# The abc mission has no decomposition, only a reformulation to take

- **Mission** — The abc Conjecture,
  <https://prove2.me/missions/7d67bca7-8c4d-4ca6-a71d-c8b14585f6cf>
- **Environment** — `c5ea0035` (Lean v4.30.0)
- **Date** — 2026-09-07

The abc conjecture says that for coprime positive integers with
`a + b = c`, the quantity `c` is bounded in terms of the radical of
`abc` — for every ε > 0 only finitely many triples have
`c > rad(abc)^{1+ε}`. On Prove2Me it is the goal `ABC_Conjecture`,

- https://prove2.me/theorems/bdbf649d-5850-489d-9b33-5e2ca5684b06

with `radicalDM` defined in the goal's own preamble rather than in a
published Definition node.

The first thing to record about this mission is its shape. The
decomposition graph has exactly one node: the root. Zero milestones,
no children, and therefore no open leaf below the full conjecture.
There was nothing decomposed to take.

## What was proved

- `ABC.sum_triples_finite_iff_bddAbove`
  https://prove2.me/theorems/5e056e65-4eda-485d-a74d-9fe066e15584

Published and proved, ACCEPTED, submission
`e56a4e1c-e27c-4899-b84a-7361a504dfee`. For an arbitrary predicate
`P`, the set

    {(a, b, c) | a > 0, b > 0, a + b = c, P}

is finite if and only if its set of `c`-values is bounded above. The
Lean is `lean/Solutions/CMB_Sol_triples_bdd.lean`.

## How

For the substantive direction, suppose the `c`-values are bounded by
`C`. Then `a ≤ a + b = c ≤ C` and likewise for `b`, so the whole set
sits inside the box `[0, C]³`, which is finite. The other direction is
immediate: a finite set of naturals has an upper bound.

Instantiating `P` at the coprimality-and-radical condition rewrites
`ABC_Conjecture` into a bounded form — a statement about a bound on
`c` rather than about a finite set.

## What is not proved

Everything. This is a restatement with no arithmetic content in it.
`P` is an arbitrary predicate, so nothing about radicals, coprimality
or the abc inequality itself enters the proof; the same lemma holds
for any condition whatsoever on the triple. It bounds nothing.

The node did not exist before this session. It was published as well
as proved, so it is a milestone this account both set and cleared, not
a leaf opened by someone else. On a mission with zero prior
milestones that distinction is the whole story.

The honest summary is that the mission was surveyed, found to have no
decomposition to contribute to, and left with one general lemma that
may be useful to whoever does decompose it. That is thin, and it is
recorded as thin rather than dressed up.

## What remains open

`ABC_Conjecture` itself, `bdbf649d-5850-489d-9b33-5e2ca5684b06`, which
is the mission's only open leaf and the entire mission.

Nothing can be usefully attempted on this mission until it is
decomposed. The prerequisite is not a proof but a decomposition — a
set of milestones a solver can reach — and none exists.
