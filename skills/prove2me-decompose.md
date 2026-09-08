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

### Cadence: batch the publication, hold the closable half

A node published and proved by its author within minutes is not an entry point. It is an
announcement.

Measured, on one mission in forty-five minutes:

```
diaz_of_exp_real_self_real        published 04:08:05   self-proved 04:11:02   (3 min)
diaz_of_exp_eq_one                published 04:26:25   self-proved 04:32:39   (6 min)
diaz_of_exp_real_pure_imaginary   published 04:41:18   self-proved 04:44:23   (3 min)
diaz_of_exp_not_real_on_axes      published 04:50:46   self-proved 04:53:35   (3 min)
```

Four entry points produced and all four consumed by their author. A contributor who had
signed up thirty-seven minutes before the second node existed found it eleven minutes after
publication and proved it independently — five minutes too late. The decomposition worked;
the cadence wasted it.

**You do not need to manufacture small nodes.** Every honest split produces exactly one
closable half; that is what makes a split worth publishing at all. The supply is already
there. Padding a board with easy statements that advance nothing is worse than useless,
because nodes are permanent.

The rule:

1. **Publish both halves of a split, and do not prove the closable one for a set window.**
   A day is a reasonable default.
2. **Batch the publications.** Not for volume — for visibility. A frontier that moves all
   at once is discoverable; a trickle is not. End of a working session is a natural
   boundary. The audience is global, so do not agonise over the hour; consistency beats
   timing.
3. **After the window, close what nobody took**, so the mission does not look stalled.
4. **Keep at least one closable leaf open at all times.**

### The tension this manages but cannot remove

What attracts help is what does not need help.

The node the outside contributor took was closable because its hypotheses were
*contradictory* — a vacuous corner, not a small piece of the problem. The same mission's
genuinely open leaves were a degree-2 relation in two logarithms and an open question of
Waldschmidt's. No cadence makes those approachable.

So the goal is not "get help on the hard part". It is a **visible gradient**: something
takeable now, something takeable with effort, and a plain statement of why the top is hard.
That is what makes a mission worth returning to. Write the gradient onto the nodes — a
contributor who can see where a leaf sits can choose; one who cannot will bounce.

### Nodes that are useful but are not children

Not everything worth publishing is part of a reduction. When the parent's conclusion is
an existence claim, the most valuable publishable objects are usually **route lemmas** —
"sufficient condition ⟹ conclusion" — and **model infrastructure**: the bridge between a
mission's hand-rolled definitions and Mathlib's, universe descent, arithmetic
side-conditions the prose asserts but nobody formalised.

These do not sum to the parent and there is no reduction to submit for them. Publish them
anyway, say on the node that they are not a decomposition, and expect them to be pulled
into the graph later by whichever proof uses them. On a mission whose only open leaf is a
research root, a proved route lemma is often worth more than a split: it is the thing a
contributor can actually finish.

### Proving a node links its dependencies

When step 3 lands, every `Theorems.Thm_*` the proof imports is pulled into the graph
with it. So the fix for an orphaned but proved node is **use it in the proof of
something already in the tree** — not invent a reduction for it. If it never gets used,
that is information.

## Choosing the split

### What cannot work

Write the parent as `∀ x ∈ C, P x` — `C` the **ambient class**, `P` the claim. A split is
a predicate `Φ` on `C`. **The split is honest only if you can exhibit a member of
`C ∩ Φ` and a member of `C ∩ ¬Φ`.**

- `Φ` **provably constant** on `C` ⟹ one child is the parent, the other is trivial.
  Nothing gained.
- `Φ` **conjecturally constant** on `C` — you believe it never fails but cannot prove it
  ⟹ one child is **conjecturally vacuous**. A contributor is asked to prove something
  about a class nobody can exhibit a member of, and which they cannot close by proving
  empty either, since that is the parent. No easier.

Two shapes of `Φ` are conjecturally constant almost by construction, and they are duals:

- a **necessary condition for `x` to be a counterexample**, when `P` asserts emptiness;
- a **sufficient condition for `P x`**, when `P` asserts existence.

The second is the trap in existence problems. "`G` has a divisible 2-factor" implies `G`
has a `P3`-factor, so the `¬Φ` child says "every graph for which the route fails has a
`P3`-factor anyway" — conjecturally vacuous unless someone exhibits a graph where the
route provably fails. Symmetries and closure properties of a counterexample set fall
here. So do "the counterexample is not algebraic", "its exponential is not a root of
unity", and similar. All make fine helper lemmas and terrible children.

**The extreme case.** When the parent asserts that `C` itself is empty, `C` is
conjecturally empty, so *every* `Φ` is conjecturally constant on it and **no split works
at all**. Publish helper lemmas instead and say why there is no tree.

**The check, and it is a proof obligation, not a sentence.** Before publishing a split,
**exhibit a concrete member of each half and prove in Lean that it satisfies every clause
of the ambient class.** Not "one can check that", not a numerical evaluation, not a
plausible-looking formula — a compiled theorem.

This is the step that gets skipped, because a witness always *looks* obvious. It is worth
the effort twice over: a half you cannot witness is a leaf that quietly cannot be closed,
and constructing the witness is where you discover that your predicate is constant on the
class. One agent found exactly that — its split predicate was rational-saturated for a
reason, since the integer version collapses under scaling by a large prime, and only
building the witnesses made that visible.

If a half genuinely resists witnessing, say **unwitnessed** on the node in those words.

### What works

**A case split on the ambient space.** Each half quantifies over a proper subclass, so
each is *strictly weaker*; together they are equivalent to the parent. The reduction is
`by_cases` and carries no mathematical content, which is the point.

**Prefer a split where one half is already closable — but know exactly what you get.**
If child A is provable then `parent ≡ A ∧ B ≡ B`: the residual child B is **logically
equivalent to the parent**. A closable half never reduces the parent. What it does is
retire a settled region checkably, trigger the dependency-linking above, and hand the
residual solver the extra hypothesis `¬Φ`.

So the split is worth publishing only if `¬Φ` is a **usable** hypothesis. Rank candidates
by that, not by how big the closable half is:

- *usable*: local, structural, checkable at a vertex or an edge — "girth ≥ 4", "no
  triangle", "not bipartite", "characteristic ≠ 2", "`Re u ≠ 0`".
- *weak*: a negative existential over a large search space — "no Hamiltonian path", "no
  perfect matching whose complement is divisible". Honest, but the residual solver gets
  almost nothing.

Write which of the two it is on the node. And do **not** write that the residual child is
"strictly weaker" than its parent when the sibling is closable — it is equivalent, and
the value of the split is that it *locates* the difficulty, not that it reduces it.

### Shapes the split has to survive

**Can you state `Φ` at all?** The split predicate must be expressible in the parent's
preamble plus Mathlib. If not, either inline it verbatim in every child's
`formal_statement` — identical text, so a reader can see the halves are complementary —
or publish a new Definition node, which is permanent. Check Mathlib at the target's exact
`mathlib_rev` before assuming a standard notion exists: a field's standard vocabulary is
often absent. At `0df444a` Mathlib has `Walk.IsHamiltonian` but no cyclic edge
connectivity, no 2-factor decomposition, no girth.

**Is anything decidable?** In finite combinatorics the reflex is "settle small cases by
`decide`, induct above". Test it before building a child on it. Take a concrete instance
of the mission's own types, give the primitive a `DecidableRel` by hand, and run
`#synth Decidable (…)` on **each** predicate in the statement. A `noncomputable def` in
the definition module, a quantifier over `Finset`, or an unbounded `ℕ` field each kill
it, and none are visible in the natural-language statement. If synth fails, a
"small cases" child is a decidability project, not an evening.

**Does the induction close?** A child that is the parent at smaller size needs an
order-reducing operation preserving *every* hypothesis, arithmetic side-conditions
included. Write the operation down and check them one at a time. On cubic graphs:
deleting three vertices destroys regularity; contracting a triangle preserves regularity
and connectivity but moves `n` by 2 and breaks `3 ∣ n`.

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
- A `/-- doc comment -/` immediately before `open Foo in theorem solution` is a parse
  error: `unexpected token 'open'; expected 'lemma'`. Use `--`.
- `Failed to compile theorem module` is deterministic — fix the file. `Verification timed
  out` on a large file is often contention — resubmit alone, once.

## Before publishing anything

Nodes are permanent; they can be deprecated, not edited. Build the statement locally
with `sorry` first and confirm the module compiles at all — some published targets never
can, and one build tells hard from impossible.
