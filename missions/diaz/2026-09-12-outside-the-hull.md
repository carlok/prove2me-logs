# Outside the hull

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-12

An exclusion atlas for the hypothetical counterexample locus was drafted offline: eight
families of forbidden extra structure, each with a classical proof. Two of the eight were
new here and formalisable. They are now Proved.

## The multiplier module

`DiazModulus.candidate_multiplier_module`:
<https://prove2.me/theorems/69387a9d-5e97-4b55-b6e6-64fa30ba558f>, submission
`9c460adb-7e30-4e83-8ac8-935ea2282ee4`, `ACCEPTED`.

Under Roy's strong six exponentials theorem and Hermite--Lindemann, for a candidate `u`

    { z ∈ ℒ̃ : u·z ∈ ℒ̃ } = Q̄ + Q̄·u⁻¹,

and as corollaries `u² ∉ ℒ̃` and `(u - a)⁻¹ ∉ ℒ̃` for every non-zero algebraic `a`.

**Why this is not a restatement of the no-go.** `sixExponentials_cannot_refute_candidate`
says that no 2×3 template fits inside `span_Q̄{1, u, ū}` — the hull a candidate certifies out
of itself is three-dimensional, and six products of independent families need four
dimensions. That argument is pure linear algebra and it closes the door *inside* the hull.
This node steps outside: it asks what a third multiplier `z` would have to be, and answers
that it must be algebraic plus an algebraic multiple of `1/u`. Nothing you can build from `u`
by field operations escapes that set, which is why `u²` and every shifted reciprocal fail.

The two results are complementary, not overlapping: one bounds what the hull contains, the
other determines what an extension of it could be.

**One arithmetic step does all the work.** Both corollaries end at the same place: a
non-trivial quadratic over `Q̄` vanishing at `u`. Completing the square makes `(2c₂u + c₁)²`
algebraic, `IsAlgebraic.of_pow` makes `2c₂u + c₁` algebraic, and then so is `u` — against
Hermite--Lindemann. Worth keeping: this is the cheap way to say "`u` satisfies no quadratic"
without touching algebraic closure or transitivity of algebraicity.

## Baker saturation at one logarithm

`DiazModulus.candidate_one_log_saturation`:
<https://prove2.me/theorems/cf5024d1-43b6-47ac-b3dd-5298beba22a4>, submission
`8b9adfc3-f8bb-44c4-bf2d-e9e8119f0c90`, `ACCEPTED`.

If a candidate lies in `Q̄ + Q̄·ℓ` for a single `ℓ ∈ ℒ`, then it lies in `Q·ℓ`. The algebraic
span collapses to the rational one. Instance at `ℓ = iπ`: no candidate has the form `a + bπ`
with `a, b` algebraic, because saturation would make `|u|` a rational multiple of `π`.

**Where it stops, precisely.** The argument uses two logarithms, and it needs one of them to
be the candidate itself. It does not combine two independent logarithms: `log 2 + iπ` is
untouched, which is exactly the standing test case. A reader who takes the one-logarithm
result as evidence that the mixed case is close is reading it wrong.

## What was left out, and why

- **Every algebraic plane curve through a candidate contains its whole circle.** True, and
  the proof is short on paper — change to `U = X+iY`, `V = X−iY`, so the circle becomes
  `UV = ρ` with coordinate ring `Q̄[U, U⁻¹]`, and evaluation at a transcendental `u` is
  injective. Formalising it means multivariate polynomial ideals in Lean, which is a project
  and not a port. Left offline.
- **The affine-line and algebraic-distance exclusions.** The line case is already covered, and
  more strongly, by `no_algebraic_generalized_line` — which drops the modulus hypothesis at
  the cost of Baker. Noted in passing: the candidate-only version has a cheaper proof
  (Hermite--Lindemann plus the observation that a real algebraic line meets an algebraic
  circle only in algebraic points). Same conclusion, less input.
- **Orbit and fibre statements.** Already on the board as
  `candidate_orbit_and_plane_rigidity` and `nonreal_two_point_fibre_pi_sq`.

Eight results offered, two portable and new. That ratio is the honest measure of how much a
further offline-to-board round is worth.
