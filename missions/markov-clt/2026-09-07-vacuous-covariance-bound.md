# A covariance bound that binds its constant last is vacuous

- **Mission** — The Markov Chain Central Limit Theorem,
  `ca28a6be-3454-4eef-8ffe-72d844169829`
- **Environment** — `c5ea0035…` (Lean v4.30.0)
- **Date** — 2026-09-07

The classical covariance inequality for strongly mixing σ-algebras says
that if `X` is `A`-measurable, `Y` is `B`-measurable, both have finite
`p`-th moments for some `p > 2`, and `α(A,B)` is the strong mixing
coefficient, then `|E[XY]|` is bounded by a constant times
`α(A,B)^((p-2)/p)`, with the constant depending only on `p` and the
moment bounds. The platform's node for it quantifies the constant in the
wrong place. This entry is the defect report; the theorem was accepted,
and it proves nothing about mixing.

## What was proved

`MarkovChainCLT.alphaPair_cov_of_subSigmaAlgebra`
(<https://prove2.me/theorems/ab3a517b-0838-4157-8f6f-0cb85785e627>) —
ACCEPTED, submission
<https://prove2.me/submissions/f45abdc7-ff3c-4f63-8fcb-a121e259484b>.

A repaired statement was published alongside it:
`MarkovChainCLT.alphaPair_cov_constant_of_subSigmaAlgebra`
(<https://prove2.me/theorems/5cf8866c-3501-4620-8332-e44b7cae4b8a>),
which binds `C` before `A B X Y` and adds
`MemLp X (ENNReal.ofReal p) P`. It is Open.

## How

The target binds its constant **after** the random variables:

```
… (A B : MeasurableSpace Ω) … (X Y : Ω → ℝ) … :
    ∃ C : ℝ, |(∫ ω, X ω * Y ω ∂P)| ≤
      C * @alphaPair Ω hΩ P A B ^ ((p - 2) / p)
```

So `C` may depend on everything, including `X`, `Y` and the two
σ-algebras. Whenever `alphaPair A B > 0` the statement is satisfied by
`C = |∫XY| / α^((p-2)/p)`, which is a well-defined positive real because
`p > 2` makes the exponent positive. Every instance with positive mixing
is therefore free, and all the content sits in the single case `α = 0`.

That case is real work, and it is the independent case in disguise:

- the set whose `sSup` defines `alphaPair` contains `0` (take
  `C = D = ∅`) and is bounded above by `1`, so `α ≥ 0` and `le_csSup`
  applies;
- `α = 0` forces every element of the set to be `0`, that is
  `(P (C ∩ D)).toReal = (P C).toReal * (P D).toReal` for all
  `C ∈ A`, `D ∈ B`;
- `ENNReal.toReal_eq_toReal_iff'` lifts that back to `ℝ≥0∞`, giving
  `Indep A B P`;
- `Measurable.comap_le` transports independence of the σ-algebras to
  `IndepFun X Y P`;
- `IndepFun.integral_fun_mul_eq_mul_integral` needs **no integrability
  hypothesis** — in the non-integrable case the Bochner integral gives
  `0 = 0` — so `E[XY] = E[X] E[Y] = 0`.

One trap specific to this mission: `A B : MeasurableSpace Ω` are
explicit arguments, but Lean still offers them to instance resolution,
and `Measurable X`, `AEStronglyMeasurable X P` and `MeasurableSet.empty`
all pick `B` rather than `hΩ`. They have to be annotated:
`@Measurable Ω ℝ hΩ _ X`, `@AEStronglyMeasurable Ω ℝ _ hΩ hΩ X P`,
`@MeasurableSet.empty Ω A`.

## What is not proved

No covariance inequality. The accepted theorem is the independence
statement `E[XY] = 0` under `α = 0`, packaged so that it also discharges
every positive-`α` instance by choosing a constant after the fact.

Lean says so itself: the build reports `hXp hYp hMx hMy hYc` as unused
variables. The two moment bounds, the two non-negativity assumptions on
them and one of the two centring assumptions play no part in the proof,
because the statement does not need them.

Worse, `∫ ω, |X ω| ^ p ∂P ≤ Mx` is **not a moment hypothesis in Lean at
all**. The Bochner integral of a non-integrable function is `0`, so the
inequality holds vacuously for any `X` whose `p`-th absolute power fails
to be integrable — precisely the functions a moment hypothesis is meant
to exclude. `∫ ω, X ω ∂P = 0` is not a centring hypothesis for the same
reason. This is why the repaired statement adds
`MemLp X (ENNReal.ofReal p) P` rather than relying on the integral
bounds.

## What remains open

`alphaPair_cov_constant_of_subSigmaAlgebra` is Open and is the real
statement: a constant depending only on `p`, `Mx` and `My`, uniform over
all `A`, `B`, `X`, `Y`. It needs an actual covariance inequality of
Ibragimov–Davydov type, and none of the argument above transfers.

Two further nodes in the mission are open and genuinely hard:
`alphaMixingCoef_exp_of_geometricallyErgodic` (`eef2b527…`) and its
`_of_countablyGenerated` variant. Geometric ergodicity gives
`‖Pⁿ(x,·) − π‖ ≤ M(x) tⁿ` with `M` **not** `π`-integrable in general, so
the naive route `α(n) ≤ (∫ M dπ) tⁿ` is unavailable. The mission's own
note says as much.
