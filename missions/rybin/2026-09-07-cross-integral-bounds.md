# Both open leaves of the Rybin problem sit under one normalised bound

- **Mission** — rybin, CUHK-Shenzhen AI Math Problem 1,
  `c36fd4df-ef29-4fbc-9bb6-1f6acf3c0733` (OpenProblem)
- **Environment** — `c5ea0035` (Lean v4.30.0)
- **Date** — 2026-09-07

The capstone `RybinAI2026.P01.matrix_integral_inequality` asserts a
triangle-like inequality for a distance between positive definite
matrices,

    distance (A+B) (C+D) ≤ max (distance A C) (distance B D),

where

    distance A B = ∫u ∫v |uᵀ(A−B)v| / ((uᵀAu)(vᵀBv)) dσ dσ

over the unit sphere `S^{n-1}` with `σ = volume.toSphere`,
unnormalised. The auxiliary `crossIntegral X Y P Q` decouples the two
denominator matrices from the numerator; `distance X Y` is
`crossIntegral X Y X Y` by `rfl`. The two definition modules were
fetched from the platform into `lean/Definitions/`:
`Def_rybin2026_p01_matrix_integral` and
`Def_rybin2026_p01_cross_integral`.

## What was proved

The mission had two open leaves which are, once unfolded, the *same*
statement:

- `crossIntegral_sum_le_max`
  https://prove2.me/theorems/9d7e410f-842c-4484-b5cb-fdba175553c4
- `matrix_integral_kernel_sum_le_max`, the unfolded form, carrying an
  additional and unused hypothesis `0 < n`
  https://prove2.me/theorems/69af46da-06cc-4ca2-b8e0-ddf93662f3b1

Both say `K_A + K_B ≤ max (I_A, I_B)`, where

    K_A = ∫∫ |β_{A−C}| / (β_{A+B} β_{C+D}),   I_A = distance A C
    K_B = ∫∫ |β_{B−D}| / (β_{A+B} β_{C+D}),   I_B = distance B D

This is the denominator-normalisation half of the problem. The
numerator half, `crossIntegral_triangle_split`, was proved by hnagoya
and does not feed into it.

A new child was published:

- `RybinAI2026.P01.crossIntegral_normalized_sum_le_one`
  https://prove2.me/theorems/1ba870d0-6d36-41b7-97e6-6dd6a6a2b012

with statement `K_A·I_B + K_B·I_A ≤ I_A·I_B`, the cleared-denominator
form of `K_A/I_A + K_B/I_B ≤ 1`. It is strictly stronger than either
leaf. Both leaves were then proved in full over that child and
submitted; both are SKETCH_ACCEPTED:

- `Solutions/RYB_Sol_crossIntegral_sum_le_max.lean` → `9d7e410f`
- `Solutions/RYB_Sol_kernel_sum_le_max.lean` → `69af46da`

## How

Write `a = β_A/β_{A+B}`, `b = 1−a`, `c = β_C/β_{C+D}`, `d = 1−c`, and
put

    dP₁ = |β_{A−C}| / (β_A β_C),   total mass I_A
    dP₂ = |β_{B−D}| / (β_B β_D),   total mass I_B

Then `K_A = ∫ a c dP₁` and `K_B = ∫ b d dP₂`, and pointwise
`ac + bd ≤ 1`. That pointwise bound is what the child records, in the
cleared form that avoids dividing by `I_A` and `I_B`.

Own content in the two submitted solutions: `cross_nonneg`,
`cross_mono_denom` — denominator inflation, reusable elsewhere on this
mission — and the `max` case-split assembly. The continuity and
integrability machinery was transferred from the already accepted
`crossIntegral_triangle_split` proof rather than rebuilt.

## What is not proved

The child is not proved. Both leaves are SKETCH_ACCEPTED, which means
accepted as a reduction, so what stands today is conditional on
`crossIntegral_normalized_sum_le_one` and on nothing weaker.

The abstract two-measure version of the child — the same inequality
for arbitrary measures `P₁`, `P₂` with those masses — is **false**.
The coupling matters: `A` occurs in both the numerator of `dP₁` and
the denominators of `a` and `b`. Only uniform comparisons are known,
via `matrix_integral_inequality_scalar_threshold`.

The evidence for the child is numerical, not proof. Under
`K_A/I_A + K_B/I_B ≤ 1`: 4000 random quadruples in dimensions 2, 3 and
4, plus hill-climbing in dimensions 2, 3, 4, 5, 6 and 8 (10 restarts ×
900 steps, 5·10⁴ sample pairs, best candidate re-evaluated on 5·10⁵).
No violation in any dimension, with a supremum of approximately
`0.99992`, identical across dimensions. Read as: true, and sharp. Read
also as: a search, which is not a proof.

The same search shows the two leaves have slack. The ratio
`(K_A + K_B) / max (I_A, I_B)` reaches only about `0.82`, so the
statements actually being reduced are strictly weaker than the child
being used to reduce them.

One strengthening is **refuted**. The mediant form

    ∫∫ (|β_{A−C}| + |β_{B−D}|) / (β_A β_C + β_B β_D) ≤ max (I_A, I_B)

reaches `1.104` in dimension 2. It is false, not merely unproved. Do
not attempt it.

## What remains open

The child `1ba870d0-6d36-41b7-97e6-6dd6a6a2b012`. Closing it closes
both leaves as already submitted.

It needs a non-uniform argument — a change of measure comparing `P₁`
and `P₂` — and the obvious route does not scale. The denominator here
is degree −2 in each variable, while the cone-measure change of
variables wants degree −n, so the `P^{-1/2}` normalisation trick only
closes in dimension 2.
