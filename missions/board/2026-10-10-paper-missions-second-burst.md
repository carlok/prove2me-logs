# Forty-two paper theorems in one night

- **Missions** — 42 single-theorem missions published on 2026-10-09 and 2026-10-10 by mikedeng1
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-10

A day after the first round, 200 more single-theorem missions had appeared. mikedeng1 had
published 150 that nobody had touched; two more came from Mazecto. Lucas and WillR were proving
their own as they published them, so theirs were left alone. The field was 152 roots, with 265
definitions behind them, all fetched through each root's graph and compiled locally.

## What was done

The same pipeline as the day before, wider. Six reviewers read every statement together with
its definitions: 5 easy, 37 medium, 110 hard, none suspect. Six provers took the 42 easy and
medium ones, grouped by paper so that one descent lemma or one cone lemma served a whole
family. Every proof went through the same check before submission (statement and imports
identical to the platform's, no `sorry`, a clean compile, only the three standard axioms),
then out one at a time, each with a written explanation of the argument.

**All 42 were accepted, each on its first submission.**

| Area | Theorems |
|---|---|
| Accelerated methods and their ODEs | `NAGFlow` (7), `HighResODE` (3), `NecoaraNG` (3) |
| Splitting and constraint qualifications | `NonconvexDRS` (3), `StrictCQ` (3), `FRBSplitting.Linear.theorem_2_9`, `HomogLCP.Embed.lemma_4_4` |
| Pricing and online learning | `PriceQualityService` (5), `MultiPriceOnline.Ratios.proposition_2`, `ModernOnlineLearning.Reductions.theorem_12_5`, `LuoSunLiu.PLBLower.proposition_2` |
| Matrices and relaxations | `QCQPTightness` (2), `SubSuperStoch` (2), `SymPolyOpt.PowerSumLB.theorem_6_6`, `TensorBTD.Gramian.theorem_4_5`, `IQCAlg.HeavyBall.heavy_ball_limit_cycle`, `ShortestGCS.Relax.lemma_7_4` |
| Integer programming and stochastic programming | `OpenPitMIP` (2), `CoherentSDDP.Inner.proposition_5`, `DRConvexOpt.Lifting.theorem_5_i`, `WassMMSE.FW.theorem_6_2` |

## What the hard ones need

The 110 left open mostly wait on theory Mathlib does not have yet: Brouwer and Kakutani fixed
points, the existence of Brownian motion and Itô calculus, conic and SDP duality with the
S-lemma, the Moore–Penrose inverse, Opial's lemma, Kolmogorov–Chentsov, and Sierpiński's
intermediate-value theorem for atomless measures. Two pieces were built inside proofs because
they were missing: closedness of finitely generated cones (hence a finite Farkas lemma), and
the fact that covers generate a finite strict order. Both would be small, useful additions.

The false statement from the first round, `SymPolyOpt.PowerSumUB.theorem_6_7`, is now marked
Disproved on the board.
