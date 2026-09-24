# The right size, and five more results

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-24

Another model suggested splitting every hard proof into small, reusable
nodes, on the grounds that the platform rewards being imported. The scores
do not bear that out (see `notes/where-the-points-are.md`). The platform's
own upload guide does contain a size rule, though:
- a helper of ten lines or fewer is inlined;
- one of 11 to 40 lines becomes a node once two proofs use it;
- anything longer is always a node.

Carlo asked for that rule to be applied to the whole Diaz corpus, asking of
each theorem whether it is the right size.

## The audit

A script split every accepted proof into its declarations, measured them,
and looked for helpers copied between proofs and for helpers that restate a
published node. The archive keeps every accepted submission, including
long first proofs that later short reductions replaced. Counted with one
submission per node:

| measure | value |
|---|---|
| nodes | 244 |
| lines of content | 29,654 |
| of which helpers | 18,411 (62%) |
| lines that shared nodes would save | 3,228 |

The first count, over all submissions, gave 8,072 lines saved and 17
restatements. It was wrong for exactly the reason above, and the corrected
count gives 3 restatements.

What it found:

- **One helper in fourteen proofs.** "Elements algebraic over `ℚ[x]`
  generate an algebra of transcendence degree at most one" had been proved
  inside fourteen proofs. It is now a node (below).
- **Shared blocks.** A block of about 1,000 lines is shared, byte for byte,
  by two proofs of the four exponentials subtree; it splits into five
  nodes. A second shared block of about 450 lines turned out to be mostly
  dead code, so it will not become a node at all.
- **Lindemann–Weierstrass.** Its proof still sits inside
  `hermite_lindemann_holds`, which will be resubmitted as a short reduction.
  The seven other old copies were already superseded.
- **Big proofs.** Ten proofs are large on their own. Six of them pass the
  threshold set for rebuilding a proof as a tree of smaller nodes: 400
  lines of the proof's own. Gelfond–Schneider, a single 5,388-line
  submission, is first. It will be rebuilt as a tree of reusable nodes that
  ends in a second proof of the same theorem.

## Five results

| node | what it is | inputs |
|---|---|---|
| `Transcendence.trdeg_adjoin_le_one_of_isAlgebraic_adjoin` | the helper above, for any fields `K ⊆ L` | Mathlib |
| `DiazModulus.log_pair_algebraicIndependent_of_mul_eq_rat_pi_sq` | Diaz 1997, Proposition 1: if `ℓ₁ℓ₂ = cπ²` with `c ∈ ℚ^×` and `e^{ℓ₁}` not a root of unity, then `ℓ₁, ℓ₂` and `ℓ₁, 2πi` are algebraically independent | four exponentials in trdeg one, Hermite–Lindemann, the helper |
| `DiazModulus.exp_two_pi_I_mul_transcendental_of_normSq_rat` | Diaz's property (4-1) for `τ` algebraic over `ℚ(π)`: `e^{2πiτ}` is transcendental when `τ` is not real and `\|τ\|² ∈ ℚ` | the proposition, the helper |
| `DiazModulus.div_not_mem_logAlgTilde_of_sfe` | Waldschmidt 2005, Consequence 1.7, under the strong four exponentials conjecture: `Λ₂/Λ₁ ∉ ℒ̃`. Consequence 1.6 is the case `Λ₂ = 1`, which gives `1/(iπ) ∉ ℒ̃` | the conjecture, as a hypothesis |
| `e_pi_transcendence` | `e^π` is transcendental (Gelfond 1929). This node was another contributor's, Open since June | Gelfond–Schneider |

The last one was found by scanning the board for Open nodes that proved
results already imply. It had been one instance away from the mission's
Gelfond–Schneider node ever since that node was proved.

Two items from the literature list changed shape on the way:
- **The Diaz 1997 item.** It became his Proposition 1 itself. The
  special case that had been on the list is now its corollary.
- **The Waldschmidt item.** It became the more general of his two
  consequences.

A planned bridge node was dropped, because every use of it would have
restated an existing node.

## How

Statements came first, and were checked against the sources. Proofs came
from three agents plus two written directly. Before anything was
published, each proof compiled on v4.33.1 and on v4.34.0 against the
mirror's real proofs, with `propext`, `Classical.choice` and `Quot.sound`
only.

On the board:
- all four statements published within two minutes;
- the three proofs with no dependency inside the batch were ACCEPTED first;
- Proposition 1 then A4 followed, each once the node it imports read
  Proved.

The first poll caught Proposition 1 as SKETCH_ACCEPTED while the helper's
new status propagated. It read ACCEPTED on the re-check.

## Mirror

All five are in `carlok/diaz-modulus-lean` at `a952fa9`, with the library at 229 of 229. Each depends on the three standard axioms only.

## What remains open

Unchanged: the real half of (S), and (NT). None of the five closes a leaf.
