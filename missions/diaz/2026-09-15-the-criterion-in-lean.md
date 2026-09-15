# Gel'fond's criterion, as a Lean argument

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Node** — `FourExp.transcendence_criterion`

The transcendence criterion under the four exponentials subtree, Waldschmidt 1971 §3, is now two
accepted reductions deep. It rests on three classical lemmas, each published as an Open node.

```
transcendence_criterion               reduction, accepted
└── transcendence_criterion_continuous    reduction, accepted
    ├── height_dvd_le                 Open    Gel'fond: height of a divisor
    ├── small_irreducible_factor      Open    Gel'fond: small value → small irreducible factor
    └── dvd_of_small_values           Open    resultant bound (Lang)
```

## First reduction: continuity for free

The 1971 proof inverts the growth functions `σᵢ`, which needs them continuous. The paper assumes
this without comment, since only integer values enter. In Lean that remark is a proof: replace each
`σ` by its piecewise-linear interpolation through the integers. The polynomial hypotheses see only
integer values and do not change. Continuity, strict monotonicity, `σ₂ ≤ σ₁` and the growth
condition `σ(x+1) ≤ aσ(x)` all pass through, the last two as convex combinations.

The condition has to be required only for `x ≥ 1`. On `(0, 1)` interpolation can break the growth
condition, even when the original function satisfies it.

A tempting shortcut failed first, on paper: redoing the argument on integers alone. With the
published constant `C = max(10+ε, (4+ε)a₁a₂)` the margins do not close, for example at
`a₁ = a₂ = 1.5`. The real-variable argument is not optional.

## Second reduction: the argument itself

About 450 lines of Lean, following the paper with one change of technique. The paper's scale
`z_q = max(σ₁⁻¹(log h/3), σ₂⁻¹(δ/(1+ε/2)))` becomes the infimum of a closed set:
`{x ≥ 1 : log h(Q) ≤ 3σ₁(x), deg Q ≤ (1+ε/2)σ₂(x)}`. The infimum belongs to the set, and both
inequalities cannot be strict there, because continuity would then give a smaller point. That one
fact does two jobs. It gives the paper's inequality (3.9), and it supplies the final contradiction
once the resultant bound has forced `Q | P_N`.

The step the paper passes over in half a sentence took the most care: the scales go to infinity.
In Lean it is a finiteness argument. Integer polynomials of bounded degree and height form a finite
set, their values at a transcendental number are bounded away from zero, and yet the small factors
get arbitrarily small at `α`.

The three children are classical and their statements were taken from the page images. Proving
them is next, along with the last undecomposed leaf, the 1973 construction.
