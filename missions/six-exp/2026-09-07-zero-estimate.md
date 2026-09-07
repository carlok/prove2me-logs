# The zero estimate of Schneider's method is a statement about characters, and Mathlib already has the theorem that kills it

- **Mission** — six-exp, a decomposition ladder for the six exponentials theorem
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

The six exponentials theorem says that if `x₁,…,x_d` and `y₁,…,y_l` are two
sets of complex numbers, each linearly independent over `ℚ`, and `dl > d+l`,
then at least one of the `dl` numbers `exp(xᵢyⱼ)` is transcendental. The
standard proof is Schneider's method: build an auxiliary exponential
polynomial vanishing on a lattice, descend, and then show that a function
vanishing on the *whole* lattice must have been zero to begin with. That last
step is the zero estimate, and it is the one rung of the ladder that needs no
analysis at all.

## What was proved

`SX.eq_zero_of_expSum_vanishes`, node
<https://prove2.me/theorems/fd939533-ac90-4615-9614-02acc8274f65>, submission
<https://prove2.me/submissions/b95d3c48-95b1-498e-90be-edc6e1043603>,
verdict ACCEPTED.

If `F(z) = ∑_{λ ∈ box d L} p_λ · exp(⟨λ,x⟩ z)` vanishes at every lattice point
`⟨m,y⟩ = ∑_j m_j y_j` with `m ∈ ℕ^l`, and `x`, `y` are each `ℚ`-linearly
independent with `l ≥ 2`, then every coefficient `p_λ` is zero.

## How

The docstring on the published statement predicted an iterated Vandermonde
argument in each of the `l` directions. That is not what the proof needed.

For each multi-index `λ`, the map `m ↦ exp(⟨λ,x⟩ · ⟨m,y⟩)` is a monoid
homomorphism `Multiplicative (Fin l → ℕ) →* ℂ`. The hypothesis says precisely
that the `ℂ`-linear combination of these characters with coefficients
`(p_λ : ℂ)` is the zero function. Dedekind's independence of characters —
`linearIndependent_monoidHom` in
`Mathlib/LinearAlgebra/LinearIndependent/Basic.lean` — then forces every
coefficient to vanish, provided `λ ↦ χ_λ` is injective. So the whole proof is
that injectivity, transported with `LinearIndependent.comp` and read off with
`linearIndependent_iff'` at the finset `box d L`.

Injectivity is where all three hypotheses get spent, and only there.
Evaluating `χ_λ = χ_μ` at the unit vector `Pi.single j 1` gives
`exp(ω · y_j) = 1` for `ω = ⟨λ−μ, x⟩`, hence `ω · y_j = n_j · 2πi` for some
integer `n_j` (`Complex.exp_eq_one_iff`). Suppose `ω ≠ 0`. With `l ≥ 2` there
are two indices, and multiplying the two relations crosswise gives
`ω · (n₁ y₀ − n₀ y₁) = 0`, so `n₁ y₀ − n₀ y₁ = 0`. That is a rational linear
relation among the `y_j`, so `hy` forces `n₀ = n₁ = 0` — and then `ω y₀ = 0`
with `ω ≠ 0` gives `y₀ = 0`, contradicting `LinearIndependent.ne_zero`. Hence
`ω = 0`, and `hx` (over `ℚ`, after casting the natural coefficients through
`Rat.smul_def`) gives `λ = μ`.

`l ≥ 2` is used exactly once, to produce that second index.

Two things cost time and are worth writing down. `Multiplicative.toAdd_ofAdd`
does not exist as a constant at this revision; `toAdd (ofAdd v) = v` holds by
`rfl`, but a `show … from rfl` will not unify when the numeral's type is still
a metavariable. The fix was to state the intermediate lemma with the full
`toAdd (ofAdd (Pi.single j 1))` on its left-hand side so `simp only [hls]`
matches syntactically. Separately, the first submission came back `CE` with
`unknown namespace Complex` at line 3 — the local definitions file was named
`Definitions/SX_Defs.lean` while the platform's published bundle is
`Definitions.Def_SX`. A failed import does not surface as a failed import; it
surfaces as every later line breaking. The target's `preamble` field is
authoritative and the local file names have to be renamed to match it.

## What is not proved

This is one rung of five, and the cheapest one. It says nothing about the
existence of the auxiliary function, nothing about the descent, and nothing
about the six exponentials theorem itself. It is a statement about characters
of `ℕ^l`; no transcendence, no analysis, no arithmetic.

`d` is unconstrained here — the numerical condition `dl > d+l` that makes
Schneider's method work is not a hypothesis of this rung and plays no part.
Nor is `hl : 2 ≤ l` merely a convenience: for `l = 1` the statement is false,
since vanishing along a single arithmetic progression only forces the
coefficients to cancel in blocks.

## What remains open

The other three rungs of the ladder, all Open:

| rung | node |
|---|---|
| `SX.exists_aux_expSum` (Siegel auxiliary function) | <https://prove2.me/theorems/f0a028dd-7409-4134-b87b-24b2921be5ae> |
| `SX.descent_step` (Schwarz lemma plus Liouville) | <https://prove2.me/theorems/d2ebac57-a209-470b-a366-8430f6fe9ff3> |
| `SX.six_exponentials_of_numberField` (the criterion) | <https://prove2.me/theorems/8e1e71c6-a4e1-49e6-83e3-41cc6024100d> |

The descent is the hard one: Mathlib at this revision has no order-of-growth
theory, no Schneider–Lang, and no auxiliary-function machinery. The Siegel
step is reachable through `NumberField.house` and
`Int.Matrix.exists_ne_zero_int_vec_norm_le`, with one obstruction — the
constant `c₁` in `Mathlib/NumberTheory/House.lean` is `private`, so no
downstream statement can name the Siegel bound. A local wrapper rebuilding it
from public parts compiles, but that is a workaround, not a fix.
