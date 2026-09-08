# Decompose, link, iterate — and the linking step is the one that gets skipped

The working rule for building a mission graph on Prove2Me, arrived at the slow way.

## The rule

**Try to decompose. Link. Iterate.** How to decompose is case by case and cannot be
reduced to a recipe. The linking is mechanical and is where the mistakes happen.

## Three steps, and the middle one is invisible if you skip it

1. **Publish** the children.
2. **Submit a reduction against the parent**, proving the parent from the children.
   It comes back `SKETCH_ACCEPTED`, and the parent then flips to `Proved` on its own
   once every child is proved.
3. **Submit the proof** of any child you can already close.

Step 2 is the one that gets missed, because a published node looks perfectly correct on
the board without it. It simply is not attached to anything. Several nodes were
published on the Diaz mission across a full day before anyone noticed that the mission's
main theorem still had a subgraph of exactly two nodes — itself and its definition
bundle.

For a second generation, the reduction goes against the **child**, not the root. The
transitive edge upward is free, because the first reduction is already accepted.

## Proving a node also links its dependencies

This was not obvious and is worth knowing. When step 3 lands, every `Theorems.Thm_*`
module the proof imports is pulled into the graph with it.

Proving `diaz_of_exp_real_self_real` from `diaz_on_axes_of_hermite_lindemann` and
`hermite_lindemann_holds` moved both of those into the conjecture's subgraph. They had
been floating siblings for a day. Nobody wired them in; using them did.

So the fix for an orphaned but proved node is not to invent a reduction for it. It is to
**use it in the proof of something that is already in the tree**. If it never gets used,
that is information about the node.

## Choosing the split: what cannot work

A conjecture asserting that a set is empty — no counterexample exists — cannot be
decomposed by necessary conditions.

- If `Φ` is provably necessary for a counterexample, the residual "no `u` with `Φ(u)` is
  a counterexample" is **equivalent** to the original. Nothing gained.
- If `Φ` is not provably necessary, then "every counterexample satisfies `Φ`" is
  **conjecturally vacuous**, since the set is empty if the conjecture holds. No easier
  than the conjecture.

A seven-node ladder of exactly this shape was designed for the Diaz mission and had to
be thrown away. Closure of the counterexample set under `u ↦ -u` and `u ↦ conj u`,
non-algebraicity of `u`, exclusion of roots of unity: all in one bin or the other.

## Choosing the split: what does work

**A case split on the ambient space.** Each half quantifies over a proper subclass, so
each is strictly weaker than the parent, and the two together are exactly equivalent
to it.

**Prefer a split where one half is already closable.** The Diaz real branch was split on
whether `u` itself is real, not because that dichotomy is deep, but because the real
half follows in one line from results the mission already owned — a real `u` with
algebraic `|u|` is algebraic, and Hermite–Lindemann finishes. Splitting there retires a
settled region and leaves the sibling holding the actual content. It also triggers the
dependency-linking above.

## What to write on the node

Say whether the child is *easier* or merely *weaker*. Those differ, and only the second
is usually established. Both Diaz halves are strictly weaker than their parent; neither
is known to be easier, and both node descriptions say so.

Flag redundant hypotheses. `diaz_of_exp_real_self_real` carries `Im e^u = 0` only so
that it is literally a case of its parent; the proof discards it. Left unsaid, a reader
would take the condition to be doing work.
