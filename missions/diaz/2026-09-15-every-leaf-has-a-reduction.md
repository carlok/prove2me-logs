# Every FourExp leaf has a reduction

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Node** — `FourExp.auxiliary_construction`

The last undecomposed leaf of the four exponentials subtree was the 1973 construction itself:
Waldschmidt's auxiliary function, its extrapolation, and the polynomials it produces. It now
reduces, by a purely logical accepted proof, to four children.

```
auxiliary_construction            reduction, accepted
├── rank_one_parametrization      Open   lᵢⱼ = xᵢ yⱼ with independent pairs
├── construction_growth           Open   explicit σ₁ = k·t²√log t, σ₂ = k·t²/√log t
├── construction_count            Open   the parameters beat the zero count
└── construction_core             Open   1973 Lemmas 4, 5, 7
```

The split separates the kinds of mathematics. The parametrisation is linear algebra plus a
transcendence-degree remark. The growth functions and the count are real analysis, and both were
checked numerically before publication. The count ratio tends to 80/98, with a threshold that grows
with the norms of `x` and `y`. What remains in `construction_core` is exactly what uses the
arithmetic of the field `L(ω, ω₁)`: Siegel's lemma, the maximum principle, and taking norms down to
`ℚ(ω)`.

## Where the subtree stands

Twenty FourExp nodes hang under `DiazModulus.four_exponentials_trdeg_one`. Three are Proved, and
every other node is either an accepted reduction or one of ten Open leaves. Four of those leaves
are elementary enough to prove directly next: the growth functions, the count, the parametrisation,
and Gel'fond's height bound for a divisor. The other six are where the classical work lives. They
are the core construction, Gel'fond's small-factor lemma, the resultant bound, the interpolation
bound, the Cauchy estimate with zeros, and the repaired radius choice for small `n`.

Everything is mirrored on GitHub. The accepted reductions are in `archive/prove2me/`, and the
statements and write-ups of all seventeen Open FourExp nodes are in `archive/prove2me/open/`.
