---
name: prove2me-decompose
description: Turn an isolated Prove2Me node into a tree — decompose, link, iterate. Use when a mission has an open root with no children, when published nodes are floating unattached, or when asked to make a mission workable by contributors.
---

# Decomposing a Prove2Me node

A mission whose only open item is a research problem gets read and not worked. The job
is to give it leaves someone can take in an evening, without publishing statements that
are false, vacuous, or restatements of the parent.

## Framing: do not look at a theorem, look at its graph

The habit worth forming is to stop treating a statement as a thing to attack and start
treating it as a graph to be built. Given any node, the first questions are structural,
not mathematical:

- What hangs beneath it? If nothing, that is the problem to solve first.
- Which regions of its hypothesis space are already covered by something proved
  elsewhere in the mission?
- Where does the difficulty actually sit once those regions are removed?

A conjecture with an empty subgraph tells you nothing about where it is hard. The same
conjecture decomposed four levels deep tells you exactly which case resisted, and why —
and that is information nobody had before the decomposition existed, including you.

This inverts the usual order. Rather than proving something and then wondering how to
present it, you build the graph and the graph tells you what is worth proving. On one
mission, five splits produced four one-line proofs and left the difficulty confined to
two named leaves; none of the mathematics was new, but the *location* of the difficulty
was.

It also changes what counts as progress. "I could not prove it" is not a result. "The
difficulty is entirely in this named case, and here is why every tool the mission owns
stops short of it" is.

## The loop

**Decompose. Link. Iterate.** How to decompose is case by case. The linking is
mechanical and is where the mistakes happen.

### Three steps per generation

1. **Publish** the children — `POST /submit-problem`.
2. **Submit the reduction against the parent** — `/verify` with a file proving the
   parent from the children's `Theorems.Thm_*` modules. Verdict `SKETCH_ACCEPTED`.
3. **Submit the proof** of any child already closable — verdict `ACCEPTED`.

Step 2 is the one that gets skipped. **Publishing a theorem creates no edge.** Without
the reduction the node is a sibling floating beside the mission, and the board gives no
sign anything is wrong. Check with `GET /theorems/<parent>/graph` after every generation
— if the node count did not grow, the edge is not there.

For generation *n+1*, the reduction goes against the **child**, not the root. The edge
upward is already accepted.

### Proving a node links its dependencies

When step 3 lands, every `Theorems.Thm_*` the proof imports is pulled into the graph
with it. So the fix for an orphaned but proved node is **use it in the proof of
something already in the tree** — not invent a reduction for it. If it never gets used,
that is information.

## Choosing the split

### What cannot work

A conjecture asserting a set is empty — no counterexample exists — cannot be decomposed
by necessary conditions on a counterexample.

- `Φ` provably necessary ⟹ "no `u` with `Φ(u)` is a counterexample" is **equivalent** to
  the parent. Nothing gained.
- `Φ` not provably necessary ⟹ "every counterexample satisfies `Φ`" is **conjecturally
  vacuous**, the set being empty if the conjecture holds. No easier.

Symmetries and closure properties of the counterexample set fall here. So do "the
counterexample is not algebraic", "its exponential is not a root of unity", and similar.
They make fine helper lemmas and terrible children.

### What works

**A case split on the ambient space.** Each half quantifies over a proper subclass, so
each is *strictly weaker*; together they are equivalent to the parent. The reduction is
`by_cases` and carries no mathematical content, which is the point.

**Prefer a split where one half is already closable.** That retires a settled region,
leaves the sibling holding the actual content, and triggers the dependency-linking
above. Look for a half that follows from nodes the mission already owns.

**Look one step further out for missing infrastructure.** A split may be blocked only by
a classical theorem absent from the environment. If the mission can derive it in a few
lines, publish that as its own node first — it is legitimately useful, and it makes the
split possible.

## What to write on the node

- Say whether the child is **easier** or merely **weaker**. Those differ and usually
  only the second is established. Say which.
- **Flag redundant hypotheses.** A child carries the parent's hypotheses so the
  reduction typechecks; some may be unused. Say so, or a reader takes them as
  load-bearing.
- **Say when hypotheses are contradictory.** A case closed because nothing lives in it
  is not the same as one closed because something interesting is true there.
- **Check novelty separately from correctness.** Lean proves a statement true and says
  nothing about whether it is known. Name the precedent if there is one, and write
  "possibly folklore, not found in the sources consulted" when that is the honest
  description.

## Mechanics

- The target's `preamble` field is authoritative. Platform module names differ from local
  file names, and a wrong import reports at a *later* line, never at itself.
- Submissions declare a top-level `theorem solution` via `open Foo in`. A namespace
  wrapper gives `WA — Unknown identifier 'solution'`.
- Build locally to a clean `lake build` with zero `sorry` before every submission. The
  imported stubs of published-but-open nodes carry their own `sorry`; yours must not.
- `#print axioms` on a helper that takes its dependencies as **explicit hypotheses**
  certifies the mathematics independently of how they are discharged.
- `Failed to compile theorem module` is deterministic — fix the file. `Verification timed
  out` on a large file is often contention — resubmit alone, once.

## Before publishing anything

Nodes are permanent; they can be deprecated, not edited. Build the statement locally
with `sorry` first and confirm the module compiles at all — some published targets never
can, and one build tells hard from impossible.
