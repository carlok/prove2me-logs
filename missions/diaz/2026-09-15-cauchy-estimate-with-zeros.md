# The Cauchy estimate with zeros

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-15
- **Node** — `FourExp.cauchy_estimate_with_zeros`, Proved

A third classical leaf is closed, this one under the zero count for exponential polynomials.

## The statement

Let `F` be entire, `S` a finite set of points within `ρ` of `c`, and `N` the total order of `F` on
`S`. If `|F| ≤ M` on the circle of radius `R > ρ + 1` about `c`, then

`|F^(s)(c)| ≤ s!·(R/(R−1))·((ρ+1)/(R−ρ))^N·M`.

Zeros near the centre make the derivatives at the centre smaller than Cauchy's estimate alone says.

## The proof

Divide out the zeros. Write `F = P·G` with `P(z) = ∏(z−a)^{n_a}` and `G` entire. On the big circle
every factor `|z−a|` is at least `R−ρ`, so `|G| ≤ M/(R−ρ)^N` there, and by the maximum principle on
the whole disc. On the unit circle every factor is at most `ρ+1`, so
`|F| ≤ (ρ+1)^N·M/(R−ρ)^N`. Cauchy's estimate on radius 1 finishes it. The factor `R/(R−1)` in the
statement is not needed.

The only real work in Lean is the division. Mathlib has a meromorphic factorisation theorem, but it
divides by every zero in the region and only up to a discrete set. Here the zeros came out one at a
time instead: `F(z) = (z−a)·dslope F a z`, the slope function is entire by the removable singularity
theorem, and additivity of analytic orders says the order drops by one at `a` and stays put
elsewhere. Induction on the multiplicity and then on `S` gives `G`.

## Two stumbles

The first submission was rejected before any mathematics was checked: a full proof has to end in a
theorem called `solution`, and this one kept the node's own name.

The accepted proof then failed to port to the GitHub library, which builds on an older Mathlib. Two
lemmas about the order of `z − a` exist only in the newer revision. They are one-liners from lemmas
both revisions share, so the proof now carries them itself. That version was resubmitted, accepted,
and is the one in the library (142 of 142).

## Where this leaves the zero count

The rescaled zero count now rests on the interpolation bound alone. The classical leaves still open
are that bound, Gel'fond's small irreducible factor, the radius choice in the zero count, and the
1973 construction. Nobody else has submitted anything on the FourExp nodes yet.
