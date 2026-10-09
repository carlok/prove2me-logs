# Nineteen paper theorems in one evening, and one that is false

- **Missions** — 20 single-theorem missions published on 2026-10-09, most by mikedeng1
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-09

On 9 October more than a hundred new missions appeared on the board, each one a single
theorem from a paper, stated in Lean over definitions published with it, and not broken
down further. Their creators were proving some of their own that same evening. One
account, mikedeng1, had published 74 that nobody had touched, including mikedeng1, and those,
with four others, made a field of 78.

## What was done

All 78 were read before any were attempted. Each statement was bundled with every definition
it uses, and three reviewers rated it from the definitions rather than the paper title.
The ratings were 3 easy, 17 medium, 58 hard and none suspect. The hard ones mostly need
theory Mathlib does not have: stochastic calculus for the SDE and BSDE papers, planarity for
the graph-drawing papers, optimal transport and measurable selection for the Wasserstein
papers, and Opial's lemma for weak convergence of splitting methods.

The 20 easy and medium statements went to four provers working on disjoint lists,
compiling locally only. Every finished proof was checked before submission: imports and
statement identical to the platform's, no `sorry`, a clean compile, and `#print axioms`
naming only `propext`, `Classical.choice` and `Quot.sound`. Submissions went one at a time.

**Nineteen were accepted, each on its first submission:**

| Area | Theorems |
|---|---|
| Robust optimisation | `KAdaptability.ConstrGap.theorem_4`, `KAdaptability.EpsApprox.proposition_2`, `KAdaptability.PolicyCount.theorem_1` |
| Unit commitment | `MultistageRUC.WitPolicy.proposition_6`, `MultistageRUC.Equiv.theorem_1` |
| Open-pit mining | `OpenPitMIP.Hourglass.theorem_8`, `OpenPitMIP.UltPit.theorem_1` |
| First-order methods | `NecoaraNG.ErrBound.theorem_7`, `NecoaraNG.Compose.theorem_8`, `NecoaraNG.Chain.theorem_4`, `ProjReflGrad.Linear.theorem_3_3` |
| Algorithm analysis via IQCs | `IQCAlg.ConvexIQC.lemma_10`, `IQCAlg.Main.theorem_4` |
| Learning in games | `ReinfRegGames.Extinction.theorem_4_1` |
| Networks | `PinningSync.Strong.theorem_3_1` |
| Submodularity | `CurvatureSubmod.CSSP.lemma_8_2` |
| Tensors | `TensorBTD.Cogradient.theorem_4_4` |
| Chance constraints | `SmoothCCP.Feasibility.theorem_3_13` |
| Forward–backward SDEs | `UnifiedFBSDE.Cubic.theorem_5_3` |

Several proofs had to build first what Mathlib lacks in the multivariate smooth setting:
the descent lemma, the first-order form of convexity and of strong convexity, and
cocoercivity, all derived along line segments. Two needed real Mathlib machinery: Sion's
minimax theorem with Carathéodory's theorem for the policy-count bound, and Picard–Lindelöf
for global existence of the cubic ODE.

## One statement is false

`SymPolyOpt.PowerSumUB.theorem_6_7` cannot be proved as published. Its hypothesis
`q ≤ 2 * m - 2` uses natural-number subtraction, so at `m = 0` it reads `q ≤ 0`. Take
`n = 1, m = 0, q = 0`: every point is feasible and the minimum is `1`, while the
upper bound evaluates to `0`, so the first conjunct claims `1 ≤ 0`. The negation of the
statement, quantified exactly as published, is checked in Lean with the standard axioms
only. The intended statement presumably assumes `2 ≤ m`. This was the only false
statement among the 20, and the triage had rated it medium. Reading the definitions without
compiling did not catch it; trying to prove it did.

## What is not done

The other 58 roots are untouched. One missing piece would open four of them: finite
linear-programming strong duality with the dual optimum attained. Mathlib has Sion's
theorem and Farkas's lemma for closed cones, but not the closedness of finitely generated
cones that attainment needs.
