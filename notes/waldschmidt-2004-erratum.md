# An erratum that is easy to miss, and it lands in exactly this neighbourhood

Found 2026-09-07 while checking the literature around the six exponentials theorem.
Recorded because the corrected result is one anybody working on products and
quotients of logarithms is likely to reach for, and the correction lives in a
different paper from the statement.

## The correction

Section 4 of

> M. Waldschmidt, *Further Variations on the Six Exponentials Theorem*,
> Hardy-Ramanujan Journal **28** (2005), 1–9

is an erratum to

> M. Waldschmidt, *Variations on the Six Exponentials Theorem*, in Algebra and Number
> Theory (Proceedings of the Silver Jubilee Conference, University of Hyderabad,
> ed. R. Tandon), Hindustan Book Agency, 2005, 338–355.

It reads:

> We take the opportunity of this paper to point out a mistake in the statement of
> Corollary 2.12 p. 347 of [8]: the assumption that `Λ₂₁` *is not zero and `Λ₁₁/Λ₂₁`
> is transcendental* should be replaced by the assumption that *the three numbers
> `1`, `Λ₁₁` and `Λ₂₁` are linearly independent over the field of algebraic numbers*.
> Otherwise a counterexample is obtained for instance with `Λ₂₁ = 1` and `Λ₂ⱼ = 0`
> for `2 ≤ j ≤ 5`.

## Why it matters here

Corollary 2.12 is the `2×5` statement, and it is what the 2004 paper uses to prove
**Corollary 2.13**, the `2×3` result concluding that one of
`Λ₁₁Λ₂₂ − Λ₂₁Λ₁₂` and `Λ₁₁Λ₂₃ − Λ₂₁Λ₁₃` is not in `ℒ̃`. That determinant statement is
directly in the neighbourhood of Diaz's modulus conjecture — it is the kind of result
one reaches for when trying to constrain a candidate — so anyone citing 2.12 or 2.13
from the 2004 paper needs the corrected hypothesis.

The trap is ordinary and worth naming: the erratum is in a *different paper*, in a
section titled only "Erratum to [8]", after the references of most people's reading.
Citing the 2004 corollary from memory, or from a copy that predates the 2005 paper,
gets the wrong hypothesis.

## What this note is not

It is not a criticism of anything, and not a finding of our own — Waldschmidt
published the correction himself, promptly, in the next paper. It is recorded here
only so that this project's own citations stay right, and so that the next person
reading the 2004 paper in isolation knows to look.
