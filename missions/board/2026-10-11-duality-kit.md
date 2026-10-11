# Finite-dimensional duality, built once, closes six optimisation theorems

- **Missions** — six single-theorem missions by mikedeng1 (distributionally robust optimisation, K-adaptability, quadratic matrix inequalities)
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-11

Mathlib has Farkas' lemma for closed cones and the Hahn–Banach separation theorems, but no linear
programming duality, no conic duality with a constraint qualification, no facts about the dual of
the semidefinite cone, and no S-lemma. Twenty-two open roots mention one of these. Six needed
nothing else.

## The kit

Twenty-two statements, frozen and checked on paper before any proof was written, then proved by
two builders in parallel while six provers used them as black boxes:

- finitely generated cones are closed, and Farkas' lemma for mixed inequality and equality systems;
- LP weak and strong duality with both optima attained, the infeasible/unbounded alternatives, an
  extended-real value form, and matrix corollaries;
- a Lagrange multiplier theorem for finitely many cone constraints under a generalized Slater
  condition, with an arbitrary feasible set so that it applies to measures;
- the semidefinite cone in the shape that theorem needs: the cone of matrices with nonnegative
  quadratic form, whose interior contains the positive definite matrices and whose dual is the
  positive semidefinite matrices (the symmetric cone itself has empty interior in the space of all
  matrices, so Slater would never hold there);
- the S-lemma with a Slater point, its strict form (which needs none), and its inhomogeneous form,
  proved without Dines' convexity theorem.

## Results

All six were accepted on the first submission: `DDMomentDRO.Type1.theorem_1`,
`DDMomentDRO.Type2.theorem_2`, `DDMomentDRO.Type3.theorem_3`, `KAdaptability.Bilinear.theorem_5`,
`KAdaptability.ObjMILP.theorem_2` and `QuadMatIneq.Petersen.proposition_4_16`.

Ten more roots now have their duality step available and wait on other missing theory: rank
reduction for spectrahedra, moment problems over measures on ℝⁿ, Wasserstein bookkeeping, and the
matrix S-lemma without a Slater point.
