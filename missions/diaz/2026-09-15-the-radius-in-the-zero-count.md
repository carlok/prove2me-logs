# The radius in the zero count

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Node** — `FourExp.zero_count_arith`, Proved

The last arithmetic step of the zero count is closed, and the gap found in its source earlier today
is repaired.

## The statement

Suppose that for every radius `R > x + 1`,

`σ·log((R−x)/(x+1)) ≤ log(n!·2^{n+1}·R/(R−1)) + 2R`,

where `n ≥ 2` and `x ≥ 0`. Then for every `λ > 0`,

`σ < n/λ + 2(1 + n^λ)(1 + x)/(λ·log n)`.

This is how the 1971 paper turns the analytic estimate into a bound on the number of zeros.

## The hole in the source

The paper chooses the radius and then uses `n!·2ⁿ ≤ nⁿ`. That inequality is false for `n ≤ 5`: at
`n = 2` it reads `8 ≤ 4`. The conclusion is still true. A numeric check earlier today found the
smallest margin, about 0.24, at `n = 2`. It just needs a different argument.

## The repair

Put `t = n^λ` and take the radius `R = x + (x+1)·max(t, 3)`. The floor at 3 is the whole trick.

With `R ≥ 3` the factor `R/(R−1)` is at most `3/2`, and the true inequality `n!·2ⁿ ≤ 2·nⁿ` is
enough. It holds with equality at `n = 2`, and the induction step is Bernoulli's `(1 + 1/n)ⁿ ≥ 2`.
Together they give `n!·2^{n+1}·R/(R−1) ≤ 6·nⁿ < e²·nⁿ`, which is exactly what the bound needs when
the radius is `t` itself.

When `t < 3` the radius is 3 instead, and one has to move the bound from 3 back down to `t`. That
comes down to `4·log t ≤ (1+t)·log 3` on `[1, 3]`. It follows from the tangent line of the logarithm
at 3 and `log 3 < 4/3`.

The proof was accepted on its first submission, with only Lean's three axioms. It is in the GitHub
library, which holds 143 of 143.

## Next

The rescaled zero count now waits only on the interpolation bound, which recovers an exponential
polynomial's values from its first derivatives at a point. That bound is true, with a better constant
than stated. The obvious contour-integral proof is too weak for it, though, so the next proof goes
through the Taylor coefficients instead.
