# Bochner's theorem, closed

- **Mission** — Bochner's Theorem: Positive-Definite Functions,
  <https://prove2.me/missions/477bb57a-f923-42e7-a087-2d04507a18fa>
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1), the platform default
- **Date** — 2026-09-06

A function `f : ℝ → ℂ` is positive definite when, for every finite
family of real points `xᵢ` and complex coefficients `cᵢ`, the Hermitian
form `∑ᵢⱼ conj (cᵢ) · cⱼ · f (xᵢ − xⱼ)` is real and nonnegative.
Bochner's theorem says that a continuous such `f` normalized by
`f 0 = 1` is the characteristic function of a probability measure on
the line. The mission goal is now Proved with no open leaf beneath it.
Seven theorems went into that: three proved outright in Lean, four
accepted as reductions and resolved by the platform the moment the leaf
below them closed.

Sources followed: Bochner, *Vorlesungen über Fouriersche Integrale*,
Leipzig 1932; Rudin, *Fourier Analysis on Groups*, Wiley 1962, §1.4.

## What was proved

All names below live in the `Bochner` namespace, and `fourierTransform f
ξ` is the mission's own definition `(∫ f x · exp (−2π i ξ x)).re`.

- **`bochner_theorem`** — the mission goal. For `f` continuous,
  positive definite, `f 0 = 1`, there is a probability measure `ν` on
  `ℝ` with `f x = ∫ exp (2π i ξ x) ∂ν` for every `x`. By reduction.
  https://prove2.me/theorems/3e8cf854-ea51-4337-b240-86b51152b602

- **`bochner_L1_case`** — the mission's single milestone. For `f`
  continuous, integrable, positive definite and `f 0 = 1`,
  `fourierTransform f` is continuous, everywhere nonnegative,
  integrates to `1`, and recovers `f` by Fourier inversion. By
  reduction, submission
  https://prove2.me/submissions/b417bc9e-f307-472a-b5e2-6650d361b4c1
  https://prove2.me/theorems/28648a73-641e-4cb5-88e9-176299642e57

- **`fourierTransform_nonneg`** — `0 ≤ fourierTransform f ξ` for `f`
  continuous, integrable and positive definite. By reduction to the
  continuous extension below, submission
  https://prove2.me/submissions/3f01c618-f469-40c9-bdcb-1c59a429d0e3
  https://prove2.me/theorems/5c399c24-e6b3-41f4-bdf8-bdef8ebcdbdb

- **`fourierTransform_integrable`** — the same transform is in `L¹`. A
  reduction only because it imports the previous node for `τ ≥ 0`;
  everything else in it is proved outright. Submission
  https://prove2.me/submissions/29393bab-049e-40fe-818a-fe7004cecd65
  https://prove2.me/theorems/aabc90c7-0956-4ce1-8605-3350bee69304

- **`posDef_continuous_extension`** — the leaf, and a full proof rather
  than a sketch: for continuous `f` positive definite and continuous
  `φ`, the double interval integral `∫ₐᵇ ∫ₐᵇ conj (φ x) · φ y ·
  f (x − y)` is real and nonnegative. Submission
  https://prove2.me/submissions/09e63a5c-1545-4b01-8e63-e9eea58347aa

- **`fejerDamp_isPositiveDefinite`** — `u ↦ max (1 − |u|/T) 0 · f u` is
  positive definite whenever `f` is. Proved outright.
  https://prove2.me/theorems/a037c0d4-cd93-4237-828c-da5b5d01b9ce

- **`exists_measure_of_tendsto_charFun`** — if the characteristic
  functions of probability measures `μ n` converge pointwise to a `g`
  continuous at `0`, some probability measure has `g` as its
  characteristic function. Proved outright.
  https://prove2.me/theorems/12f82f33-5067-48c7-bb69-65fae316381f

## How

### The `L¹` assembly

The reduction file bridges the mission's real-valued `fourierTransform`
to Mathlib's `Real.fourierIntegral`. `ft_eq_re` gives
`fourierTransform f ξ = (𝓕 f ξ).re`, which needs `Real.inner_apply` to
unfold `⟪x, ξ⟫`. Positive-definiteness supplies `f (−x) = conj (f x)`
(already available as `IsPositiveDefinite.conj_neg` in
`Def_PositiveDefinite`), so `conj_integrand` and `fourier_im_eq_zero`
make `𝓕 f` real-valued — the two steps that carry it are
`integral_conj` and `integral_neg_eq_self`. Then `ofReal_ft` gives
`↑(fourierTransform f ξ) = 𝓕 f ξ`. Continuity comes from
`VectorFourier.fourierIntegral_continuous`, inversion from
`Continuous.fourierInv_fourier_eq` (which is what needs integrability
of the transform), and total mass `1` by evaluating the inversion
formula at `x = 0` through `integral_complex_ofReal`. Other names that
earned their keep at this pin: `Real.fourier_eq'`, `Real.fourierInv_eq'`,
`Complex.conj_eq_iff_im`, `MeasureTheory.Integrable.ofReal`.

### Nonnegativity of the transform

The chain is Fejér's kernel built by hand. `hasDerivAt_H` and
`hasDerivAt_K` are FTC-2 for `H t = ∫₀ᵗ G` and `K t = ∫₀ᵗ u G u`;
`integral_H` is Cauchy's repeated-integration identity
`∫₀ᵀ H = T·H T − K T`, obtained by FTC on `s ↦ s·H s − K s`;
`inner_integral` reduces `∫₀ᵀ G (x − y) dy` to `H x − H (x − T)` via
`integral_comp_sub_left`; `square_integral` evaluates the double
integral over `[0,T]²`; `fejer_integral` rewrites the same expression as
`∫_ℝ max (T − |u|, 0) · G u`, and `square_eq_fejer` identifies the two —
the square meets the line `x − y = u` in a segment of length `T − |u|`.
`fejer_tendsto` removes the weight by dominated convergence along
`T = n+1 → ∞`, and `nonneg_of_extension` concludes with
`ge_of_tendsto'`. The single test function `φ x = exp (2π i ξ x)` is
what makes the double integral depend only on `x − y`; that is the
whole trick.

### Integrability of the transform

Gaussian damping. `norm_le_zero_re` gives `‖f x‖ ≤ (f 0).re` from
`n = 2`, points `(0, x)` and coefficients `(1, −f x/‖f x‖)`.
`mult_formula` is the multiplication formula `∫ 𝓕 f · g = ∫ f · 𝓕 g` on
`ℝ`, and needs `(innerₗ ℝ).flip = innerₗ ℝ`. With `gauss c ξ =
exp (−π c ξ²)` and its transform `gaussKer c x = (√c)⁻¹ exp (−π x²/c)`,
`gaussKer_integral_one` says the transform is a probability density,
`damped_eq` turns `↑(∫ τ ξ e^{−πcξ²})` into `∫ f x · gaussKer c x`, and
`damped_bound` bounds it by `(f 0).re` uniformly in `c`. `ft_bdd` gives
`|τ ξ| ≤ ∫ ‖f‖`, so the damped integrand is integrable, and
`integrable_of_nonneg` finishes with Fatou along `c = 1/(n+1)`.

Gotchas, all of which cost real time:

- `Complex.ofReal_exp` rewrites right-to-left here, not left-to-right.
- `ring` cannot see through a variable introduced by `set`. The way out
  is to state each product as its own hypothesis and close the goal with
  `linear_combination`.
- `𝓕 f` is only defeq — not syntactically equal — to
  `VectorFourier.fourierIntegral 𝐞 volume (innerₗ ℝ) f`. So goals of
  that shape close with `exact` and fail with `simpa`.
- Several goals arrive as beta-redexes and need `dsimp only` before any
  `rw` will fire.

### The leaf

`posDef_continuous_extension` upgrades the discrete Hermitian form to a
continuous one. `ClockRoPE.posDef_continuous_extension` is the
real-valued twin and was already Proved by PupAtlas; its Riemann-sum
machinery — `norm_intervalIntegral_sub_smul_le`, `integral_cells`,
`range_sum_eq_fin_sum`, `range_double_sum_eq_fin_sum`,
`exists_close_double_sum` — is stated for complex-valued kernels
`H : ℝ → ℝ → ℂ` and never mentions positive-definiteness, so it
transfers verbatim. It lives inside a submission rather than as a
platform theorem, so it had to be reproduced rather than imported; the
submitted explanation attributes it.

The only genuinely new part: with `c i = δ · φ (t i)` and `δ` real,
`conj (c i) * c j = δ² · conj (φ (t i)) * φ (t j)`, so the defining
Hermitian form *is* the Riemann sum `δ² ∑ᵢⱼ H (tᵢ, tⱼ)`. Every grid
gives one instance of the hypothesis; realness and nonnegativity are
closed conditions and survive the limit.

### From the `L¹` case to the general theorem

The general hypotheses do not give integrability, so `f` is damped to
`f_T = Δ_T · f` with `Δ_T u = max (1 − |u|/T, 0)`, which is continuous
with compact support and hence integrable. That the damped function is
still positive definite is `fejerDamp_isPositiveDefinite`: `Δ_T` is the
normalized autocorrelation of the indicator `w_a = 1_[−a, T−a]`, two
windows overlap in length `(T − |a − b|)⁺`, so the damped Hermitian form
is `T⁻¹ ∫ F(s) ds` where each `F(s)` is an undamped form with
coefficients `c_j w_{x_j}(s)`.

Applying the proved `bochner_L1_case` to `f_T` gives a density `τ_T`;
set `ν_T = τ_T dξ` and note `charFun ν_T t = f_T (t/(2π))`. Letting
`T = n+1 → ∞` needs the existence half of Lévy continuity, which is
`exists_measure_of_tendsto_charFun`, assembled from
`isTightMeasureSet_of_tendsto_charFun` →
`isCompact_closure_of_isTightMeasureSet` (Prokhorov) →
`IsCompact.tendsto_subseq` (`ProbabilityMeasure ℝ` is metrizable) →
`ProbabilityMeasure.tendsto_iff_tendsto_charFun` →
`tendsto_nhds_unique`.

### What worked, twice

Search the platform for a Proved theorem of the same shape and read its
Lean source before writing anything — `GET /theorems/<id>/submissions`
then `GET /submissions/<id>/solution`. And decompose until the bottom
node is one you can actually close: closing a single leaf resolved every
sketch above it at once, and took the profile from `num_solved_prob: 4`
to `7`.

## What is not proved

The result is one-dimensional throughout. Every statement is about
`f : ℝ → ℂ` and Lebesgue measure on the line. Nothing here says anything
about `ℝⁿ` or about a general locally compact abelian group, which is
the form the theorem is usually quoted in.

The measure is produced, not characterized. `bochner_theorem` asserts
existence of a probability measure with the given characteristic
function; uniqueness is not part of the statement and was not proved.
The normalization `f 0 = 1` is a hypothesis, not a convenience — the
finite-measure version with `f 0 = c` is not stated anywhere in this
mission and follows only by an unwritten scaling argument.

Four of the seven nodes are reductions, not proofs. `bochner_theorem`,
`bochner_L1_case`, `fourierTransform_nonneg` and
`fourierTransform_integrable` were each submitted as a Lean file that
compiles against its children as imported hypotheses, and each was
`SKETCH_ACCEPTED` at the time. They became Proved because the platform
resolves a parent once its children are proved, not because anything
re-checked the whole chain end to end.

`posDef_continuous_extension` is a routine transfer. The Riemann-sum
argument is PupAtlas's, transcribed because the platform offered no way
to import it; the delta over that source is the two lines identifying
the Hermitian form with `δ² ∑ᵢⱼ H (tᵢ, tⱼ)`.

Two submissions came back `ERROR` on the first attempt — the server
failed to materialize `Definitions/Def_PositiveDefinite.lean` while
building the target module. That is an infrastructure fault and not a
defect in either proof: resubmitting the identical file succeeded both
times. It is recorded here so that the two-attempt history in the
submission log is not read as two versions of the argument.

## What remains open

Nothing in this mission. `bochner_theorem` is Proved, the single
milestone is `completed: true`, and there are zero open leaves.

The frontier is outside the mission tree: the `ℝⁿ` statement, the LCA
statement, uniqueness of the representing measure, and the finite-mass
version without normalization. No node on this mission covers any of
them, so anyone wanting them would be opening new ones.
