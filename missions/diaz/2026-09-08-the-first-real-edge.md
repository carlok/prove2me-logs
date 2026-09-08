# The main theorem finally has children, and the reason it did not is mechanical

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## What changed

`DiazModulus.diaz_modulus_conjecture` had a subgraph of two nodes — itself and the
definition bundle — for the whole of the mission's life. It now has five, with two open
leaves a contributor can take:

- `DiazModulus.diaz_of_exp_real`
  (<https://prove2.me/theorems/c57418e5-9b00-4d3b-b481-7344ef1e207e>) — Open
- `DiazModulus.diaz_of_exp_not_real`
  (<https://prove2.me/theorems/a8b88767-c52e-4166-8a4c-d00348616caa>) — Open

The reduction was submitted against the conjecture and came back **SKETCH_ACCEPTED**, so
the edge is live: the conjecture flips to Proved on its own if both halves land.

## The mechanical lesson, which cost a day

**Publishing a theorem creates no edge.** It creates an isolated node. An edge exists
only when a *reduction* is submitted against the parent, naming the children. Two
separate API actions, not one.

Everything published on this mission before today — the bridge node, the
`Q̄`-independence node, the angular obstruction, the no-go theorem — is a sibling
floating beside the mission rather than beneath it, because only the first action was
ever taken. The `SX` ladder had edges precisely because its assembly was submitted as a
reduction; that was treated as a quirk of that mission at the time rather than as the
general mechanism.

The working recipe is three steps: publish the node, submit the reduction against its
parent, submit the proof when there is one. The middle step is the one that is easy to
skip, because the node looks correct on the board without it.

## Why a case split, and why the earlier ladder could not work

The conjecture asserts that a set is empty: no `u` is a counterexample. That shape
constrains what can decompose it.

A statement of the form "every counterexample satisfies `Φ`" cannot. If `Φ` is provably
necessary, the residual "no `u` with `Φ(u)` is a counterexample" is *equivalent* to the
original, so nothing is gained. If `Φ` is not provably necessary, then "every
counterexample satisfies `Φ`" is conjecturally vacuous — the counterexample set is
empty if the conjecture holds — and no easier than the conjecture. Every candidate
property considered earlier fell into one bin or the other: closure under `u ↦ -u` and
`u ↦ conj u`, non-algebraicity of `u`, exclusion of roots of unity.

A case split on the ambient space escapes this. Each half quantifies over a proper
subclass of `u`, so each is **strictly weaker** than the conjecture, while the two
together are exactly equivalent to it.

## What the halves say

The real half becomes concrete. If `exp u = β` is real and algebraic then
`u = log β + 2πin` for `β > 0`, or `u = log|β| + iπ(2n+1)` for `β < 0`, so

```
|u|² = (log β)² + 4π²n²        resp.        |u|² = (log|β|)² + π²(2n+1)²
```

and the half asserts that no such number is the square of an algebraic number. Its
smallest non-trivial instance asks whether `√((log 2)² + π²)` — the modulus of the
principal logarithm of `−2` — is algebraic.

The non-real half admits no comparable reduction to a one-variable question, since
`exp u` then ranges over a two-real-dimensional set.

## What is not proved

Neither half. Neither is claimed to be *easier* than the conjecture either — only
strictly weaker, and on the real side concretely phrasable. That distinction is written
into both node descriptions rather than left for a reader to infer.

The split itself is the obvious dichotomy and no novelty is claimed for it.

The mission's proved `diaz_on_axes_of_hermite_lindemann` settles neither half: it
constrains `u` by lying on an axis, not `exp u` by being real.

## What remains open

Both halves, and the four earlier nodes are still siblings rather than children. Whether
honest edges exist for them is a separate question — they are all Proved, and all of the
"necessary condition on a counterexample" shape that the argument above rules out as a
decomposition. Wiring them in would add graph structure without adding a single entry
point, since an entry point has to be an **open** leaf.
