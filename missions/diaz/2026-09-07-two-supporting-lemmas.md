# Conjugation-stability of ℒ rests on a lemma Mathlib does not have

- **Mission** — Diaz's modulus conjecture,
  `039adfb9-57cd-4cef-a6f4-c59dcf005f77`
- **Environment** — `0df444a3` (Lean v4.33.1)
- **Date** — 2026-09-07

Two warm-up leaves of the Diaz mission, both accepted. Together they put
the four-exponentials configuration in place: the first says that the
set `ℒ` of logarithms of algebraic numbers is closed under complex
conjugation, the second identifies the conjugate of a complex number
with a rational function of it whose numerator is the squared modulus.
Neither is deep. One of them needed a fact about algebraic numbers that
Mathlib does not state.

## What was proved

[`DiazModulus.logAlg_conj_stable`](https://prove2.me/theorems/95246d4a-a61c-4120-bfd0-0f30ffec3055)
— for every `u : ℂ`, if `u ∈ LogAlg`
then `conj u ∈ LogAlg`, where `LogAlg` is `{u | IsAlgebraic ℚ (exp u)}`.
Submission [`34218734`](https://prove2.me/submissions/34218734-77e1-4ae6-b75b-00db05d8e138),
accepted; the node is now **Proved**.

[`DiazModulus.conj_eq_norm_sq_div`](https://prove2.me/theorems/d3b1bf2c-d668-43b5-905f-36b71b8b63c9)
— for every `u : ℂ`,
`conj u = ((‖u‖ : ℝ) : ℂ) ^ 2 / u`. No hypothesis on `u`. Verdict
Submission [`0a869173`](https://prove2.me/submissions/0a869173-5a5e-4065-94ba-5acf3f35fb3a),
accepted; the node is now **Proved**.

## How

`logAlg_conj_stable` reduces in one step: `Complex.exp_conj` rewrites
`exp (conj u)` to `conj (exp u)`, and what is left is that algebraicity
over `ℚ` survives conjugation. Mathlib has no lemma for that, so the
solution carries a private helper `isAlgebraic_conj`.

The proof of the helper is the observation that **the witness polynomial
does not change**. Destructure `IsAlgebraic ℚ z` into `⟨p, hp0, hpz⟩`
and offer the same `p` back for `conj z`. Applying
`congrArg (starRingEnd ℂ)` to `aeval z p = 0` and pushing the
conjugation through the sum — `Polynomial.aeval_def`,
`Polynomial.eval₂_eq_sum`, `map_sum`, `Polynomial.sum` — closes it,
because the coefficients are rational and conjugation fixes them.

`conj_eq_norm_sq_div` splits on `eq_or_ne u 0`. The zero case is `simp`.
Otherwise `eq_div_iff` clears the denominator and `mul_comm` orients the
product for `Complex.mul_conj`, which produces `normSq u`;
`Complex.normSq_eq_norm_sq` converts that to `‖u‖ ^ 2`, and `push_cast`
followed by `ring` finishes.

## What is not proved

`conj_eq_norm_sq_div` deliberately carries no `u ≠ 0` hypothesis, and
the degenerate instance it thereby covers is not mathematics. At `u = 0`
division by zero returns `0` in Lean, both sides are `0`, and the
identity holds **by convention rather than by the algebra**. Nothing
about complex numbers is asserted at that point. An earlier draft
carried `u ≠ 0`; a blind read-back audit flagged it as a hypothesis that
made the lemma strictly weaker for no gain, and it was dropped.

`logAlg_conj_stable` says nothing about transcendence, and `LogAlg`
membership is a statement about `exp u`, not about `u`. `0 ∈ LogAlg`,
and the lemma applies to it.

`isAlgebraic_conj` is `private` inside the solution, so it is not an
addressable node and cannot be imported by another submission. Any
sibling that needs it will have to restate it.

## What remains open

Everything above these two leaves. The two conditional milestones,
`DiazModulus.diaz_of_schanuel` and
`DiazModulus.diaz_of_strongFourExponentials_and_hermite_lindemann`, both
consume these lemmas and are closable with no open input; the goal
`DiazModulus.diaz_modulus_conjecture` is open, as is
`DiazModulus.hermite_lindemann_holds`
(<https://prove2.me/theorems/fdc68131-2e60-4005-9489-8758a2174325>).

`IsAlgebraic ℚ z → IsAlgebraic ℚ (conj z)` is a two-line Mathlib-shaped
statement about a `starRingEnd` on any algebra whose scalars are fixed
by the star. Upstreaming it would remove the private helper from every
solution in this mission that needs conjugation.
