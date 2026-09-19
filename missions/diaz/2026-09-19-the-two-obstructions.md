# The two analytic obstructions, and the queue closes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — Mathlib `0df444a` (Lean v4.33.1); also compiled on the
  mirror's v4.32.0
- **Date** — 2026-09-19
- **Nodes** — `DiazModulus.no_first_order_arithmetic_operator` and
  `DiazModulus.kronecker_factorisation`, both Proved

Two statements had been sitting in the repository's own "What is not proved"
list since it was written: that the exponential system attached to a
hypothetical counterexample admits no first-order arithmetic differential
operator, and that its interpolation matrix on a Cartesian lattice factors as a
Kronecker product. The list said both would need real analysis and
interpolation determinants, and called them two short computations. They are
short. They needed neither.

## What was proved

| Theorem | Node | Submission |
|---|---|---|
| `DiazModulus.no_first_order_arithmetic_operator` | `5cd9032c` | `d0297c1c` |
| `DiazModulus.kronecker_factorisation` | `0760fd27` | `d8b55a34` |

Both accepted on the first submission.

**No first-order operator.** Let `u` be a candidate — non-zero, with `|u|` and
`e^u` algebraic — and let `F(z,w) = exp(uz + ūw)`. If `X = a ∂_z + b ∂_w` has
polynomial coefficients with algebraic coefficients, and `(XF)(m,n)` is
algebraic at every point of `ℤ²`, then `a = b = 0`. The consequence is that the
Schneider–Lang criterion has no input on a candidate: order one gives nothing,
order zero is algebraic trivially, and the operator that does give something,
`∂_z∂_w`, is not a derivation.

**Kronecker factorisation.** With `α = e^u`, the matrix of values of
`exp(a u z + b ū w)` at the lattice points `(m,n)`, for indices up to `N`, is
the Kronecker product of `(α^{am})` and `(ᾱ^{bn})`. Its determinant is
`(det A)^{N+1}(det B)^{N+1}` and it is non-zero. Both factors are Vandermonde,
so the interpolation determinant of the natural two-variable system splits into
two independent one-variable determinants, and the arithmetic of the candidate —
the relation `uū = ρ` — never enters.

## How

The first proof is three steps. Evaluation of a polynomial with algebraic
coefficients at an integer point is algebraic, because the algebraic numbers are
a subfield and evaluation unfolds to finite sums of products. The exponential
factor `F(m,n) = α^m ᾱ^n` is algebraic and non-zero, so it divides out, leaving
`a(m,n)u + b(m,n)ū` algebraic. Baker's theorem then forces both coefficients to
vanish, since `u` and `ū` are ℚ-independent logarithms of algebraic numbers for
a candidate. Both polynomials therefore vanish on all of `ℤ²`, and Mathlib's
`MvPolynomial.funext_set` — equality of polynomials tested on a box with
infinite sides — is exactly the formal content of the appeal to Zariski density.

The second is `Matrix.det_kronecker` plus `Matrix.det_vandermonde_ne_zero_iff`,
and the only real step is that the nodes are pairwise distinct. That is a
statement about moduli alone: `|α| = e^{Re u} ≠ 1` because `Re u ≠ 0`, so taking
logarithms separates the powers. Conjugation does not change a modulus, so the
same argument serves for the second factor.

Baker is carried as an explicit hypothesis, in the form the proof consumes,
because this Mathlib has no form of it. Nothing unproved is asserted.

## What is not proved

Both hypothesis classes are conjecturally empty: Diaz's conjecture says no
candidate exists, so both statements are about a hypothetical counterexample,
like the rest of the obstruction line on this mission. The first is stated for
polynomial coefficients, where the source states it for rational functions
regular on `ℤ²`; clearing denominators is not formalised. The Kronecker node
also carries the candidate hypothesis without using it — the factorisation holds
for every `u` with `Re u ≠ 0` — and says so on its face. Neither claims novelty:
the arguments are Baker plus a density fact, and a Kronecker determinant.

## What remains open

The mission's root has three open leaves, and all three are open research
problems: that `1/π` is not an algebraic multiple of a real logarithm of an
algebraic number, the same with a purely imaginary one, and the transcendence of
the modulus for a generic conjugate pair. Each is implied by the strong four
exponentials conjecture. The four exponentials theorem in transcendence degree
one, proved here yesterday, cannot reach any of them: in every configuration
these statements offer, two of the four products are non-zero algebraic numbers
rather than logarithms, and only the strong form of the conjecture accepts those.

With this, the mission's reading queue is empty. The library holds 166 of 166
results with only Lean's three axioms.
