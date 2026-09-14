# Four exponentials gets a tree

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-14
- **Leaf** — `DiazModulus.four_exponentials_trdeg_one`

The one Open leaf of the Diaz mission that is a theorem in the literature now has a subtree. It
is four exponentials in transcendence degree one, due to Brownawell and Waldschmidt (1973–74). Six
new nodes sit under it, joined by three accepted reductions, and every node is connected in the
mission graph.

```
four_exponentials_trdeg_one            reduction, accepted
├── transcendence_criterion            Open
└── small_polynomials_of_counterexample    reduction, accepted
    ├── auxiliary_construction         Open
    └── nonvanishing_derivative        reduction, accepted
        ├── expPoly_zero_count         Open
        └── expPoly_ne_zero            Open
```

## Which proof

Three proofs exist, and two were rejected after reading them.

- **Roy–Waldschmidt 1997** is 45 pages, but its central tool is quoted from another 53-page paper
  on effective algebraic subgroups.
- **Roy–Waldschmidt 1995** sketches a route through Philippon's zero estimate.

The route taken is **Waldschmidt 1973** (12 pages), with two tools from his **1971** paper. The
first is a Gel'fond-type transcendence criterion. The second is a zero count for exponential
polynomials that needs no separation between the frequencies. The 1973 proof itself uses Gel'fond's
older zero lemma, which needs a lower bound for `|n₁ + n₂ x₂/x₁|` of Baker type. The 1971 count
removes Baker from the route entirely.

All four papers are open access. The statements were transcribed from the page images, because the
text layer garbles the formulas. The transcription caught a missing hypothesis in the criterion,
`σ₂ ≤ σ₁`, and a wrong exponent in the 1973 parameters.

## How it stays connected

An Open node joins the graph only when an accepted proof imports it, so each step went up as a
reduction.

- **The leaf follows by contradiction** from the transcendence criterion and one node holding the
  analytic core. A counterexample yields integer polynomials too small at a transcendental number.
- **That core follows by pure logic** from two nodes. One is the construction (Siegel's lemma, the
  maximum principle, norms). The other is a general statement that some derivative of an
  exponential polynomial is non-zero somewhere on a lattice.
- **The lattice statement follows from the zero count**, plus one classical fact: an exponential
  polynomial with distinct frequencies is not identically zero. That fact had to become its own
  node. The zero count weighs each zero by its analytic order, and that weight is 0 at every point
  of a function that vanishes everywhere, so the count alone cannot exclude it.

The last reduction is a real Lean proof of about 150 lines: reindexing the frequencies, the identity
theorem, orders from vanishing derivatives, and a counting argument. It compiled on the first build.
The parameters planned for the construction give about `98 t₀⁴√log t₀` zeros against a bound of
about `80 t₀⁴√log t₀`, so the margin is real.

## What is left

Four Open leaves:
- the criterion (1971 §3);
- the zero count (1971 §4);
- the construction (1973 Lemmas 4, 5, 7);
- the classical non-vanishing fact.

Each gets decomposed the same way, by accepted reductions only.
