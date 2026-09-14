# The first FourExp leaf closes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-14
- **Node** — `FourExp.expPoly_ne_zero`, Proved

Of the four Open leaves under the four exponentials subtree, one was a classical fact that could
be proved outright rather than decomposed: an exponential polynomial `Σⱼ Pⱼ(z) e^{ωⱼz}` with distinct
frequencies and some non-zero coefficient is not identically zero. It was needed because the zero
count, which counts zeros by analytic order, sees nothing at all in a function that vanishes
everywhere.

The proof was accepted on its first submission and uses only Lean's three axioms. It avoids
confluent Vandermonde determinants by inducting on `Σ (deg Pⱼ + 1)`. Multiply by `e^{−ω₀z}` and
differentiate; the block at `ω₀` loses a degree, and each other block `Pⱼ` becomes `Pⱼ' + cⱼPⱼ` with
`cⱼ ≠ 0`, which has the same degree and vanishes only when `Pⱼ` does. At the bottom, a polynomial
times `e^{ω₀z}` that is identically zero must be the zero polynomial.

On GitHub it is archived and ported into the library, which now holds all 137 Proved results. The
same day, the archive gained `archive/prove2me/open/`: the statements and write-ups of every Open
FourExp node, kept current by the refresh script, so an accepted reduction never imports text
that exists only on the platform. This node's two files there disappeared on the next refresh, as
they should.

Three Open leaves remain: the transcendence criterion, the zero count, and the 1973 construction.
