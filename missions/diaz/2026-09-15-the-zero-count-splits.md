# The zero count splits, and its source has a hole

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Node** — `FourExp.expPoly_zero_count`

The zero count for exponential polynomials, Waldschmidt 1971 §4 Lemma 3, is now a reduction with
four children. Two of them are already Proved.

```
expPoly_zero_count                 reduction, accepted
├── expPoly_zero_count_scaled      Open    the analytic inequality (4.14), rescaled
├── zero_count_arith               Open    choosing the radius
├── zero_count_degenerate          Proved  n ≤ 1 or all frequencies 0
└── zero_count_arith_poly          Proved  at most n − 1 zeros beats the bound
```

## The hole

The paper gets from its inequality (4.14) to the published bound (4.2) by choosing a radius and
estimating `n!·2ⁿ ≤ nⁿ`. That estimate is false for `n ≤ 5`. For `n = 2` the paper's choice of
radius genuinely fails over part of the range, not just its bookkeeping.

The bound itself survives. Optimising the radius numerically from (4.14) gives the published
bound for every `n` from 2 to 10⁵ and `x = ρΩ` up to 1000. The tightest case is `n = 2`, `x = 0`,
with a margin of 0.237. So the published statement stands, but a formal proof has to choose the
radius differently for small `n`. That is exactly what `zero_count_arith` has to prove, and its
write-up on the board says so.

This is the kind of thing a formalisation is for. The lemma is fifty years old, widely cited, and
correct; one line of its proof is not.

## How the split works

The reduction is a case split with no analysis in it. If `n ≤ 1` or every frequency is 0, the
function is one block `P(z)e^{ωz}`, so it has at most `deg P ≤ n − 1` zeros. Otherwise (4.14),
rescaled to frequencies of modulus at most 1, feeds the arithmetic.

Both small leaves were proved the same day. For the degenerate case, orders of `P(z)e^{cz}` are root
multiplicities of `P`, and they sum to at most its degree. For the arithmetic of that case, `λ ≤ 1`
is immediate, and for `λ > 1` the key step is `e^t ≥ n(1 + t − log n)` with `t = λ log n`.

The library on GitHub now holds 139 of 139 Proved results.
