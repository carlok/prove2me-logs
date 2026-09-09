# The tree was never the reduction

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-09

`DiazModulus.diaz_of_sfe : StrongFourExponentials → DiazModulusConjecture` is **Proved**:
<https://prove2.me/theorems/0148ccca-b726-4238-8cb8-48eba0967a85>, submission
`9d08897b-121a-4869-bd1b-6ddcd1b89e15`, `ACCEPTED`.

Fifteen lines, one instantiation.

## The proof

Let `u ≠ 0` with `‖u‖` algebraic and suppose `e^u` were algebraic. If `u` is algebraic,
Hermite–Lindemann ends it. Otherwise `u` and `ū` are both transcendental, so `(1, u)` and
`(1, ū)` are `Q̄`-linearly independent, and the strong four exponentials conjecture applies to
`x = (1, u)`, `y = (1, ū)`. Its four products are

```
1        ū        u        u·ū = ‖u‖²
```

`1` is in `ℒ̃` by definition; `u` and `ū` because `e^u` and `e^ū = conj(e^u)` are algebraic;
and `‖u‖²` because it is algebraic and `Q̄·1 ⊆ ℒ̃`. Contradiction.

Hermite–Lindemann discharges from the Proved `DiazModulus.hermite_lindemann_holds`, so SFE is
the only surviving hypothesis.

## Where it came from

Not from looking for it. It fell out of a structured design review that **rejected** the design
it was reviewing. The Skeptic, refuting a claim that a proposed second route was "off the
four-exponentials axis", observed in passing that SFE delivers the same content by this
instantiation. The rejected design is in
[a design review that killed its own design](../notes/a-design-review-that-killed-its-design.md);
this is the thing that outlived it.

The arbiter role in that review forbids inventing, so it was recorded and left for a separate
round rather than folded into the one being rejected. That separation is why it exists as its
own node with its own checks rather than as a footnote on a bad design.

## What it costs the mission's story

This mission carries roughly sixty nodes: four generations of case splits, a polar normal form,
a transcendence-degree certificate, four-exponentials matrix machinery, a no-go theorem for the
matrix route on one half. Every open leaf of that tree is implied by SFE. And SFE reaches the
root directly, without any of it.

So the tree is not a reduction that made the problem easier. That description was never right,
and the node's own text says so.

**What the tree actually did**, and this survives: it isolated hypotheses **strictly weaker
than SFE** that still suffice. `DiazModulus.recip_pi_not_log` — no non-zero algebraic `γ` has
`γ/(iπ)` a logarithm of an algebraic number — follows from SFE, is not known to imply it, and
two open leaves reduce to it. That is the honest product of a decomposition like this one:
weaker sufficient conditions, not a ladder of progressively easier problems.

Worth being blunt about the difference, because a reader arriving at a sixty-node tree will
assume the first thing and be misled.

## The check that mattered

The two tests this mission now applies before publishing anything both passed, and were run
rather than asserted:

- **Vacuity** — is the conclusion already Proved unconditionally? No; `DiazModulusConjecture`
  is the open root.
- **Redundancy by composition** — does the graph closure already contain the edge? No.
  `q=strong_four` returns zero rows, and the only SFE node was `recip_pi_not_log_of_sfe`, which
  targets a *leaf*. Getting from a leaf back to the root requires every other leaf, so no path
  existed.

Four nodes published on this mission in two days failed one of those two tests. This is the
first one where running them was what justified publishing rather than what stopped it.
