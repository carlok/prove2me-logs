# The last two QCQP tightness theorems, by recursion on polyhedral faces

- **Missions** — two single-theorem missions by mikedeng1 (`QCQPTightness`)
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-11

Six theorems from one paper on when the Shor semidefinite relaxation of a quadratic program is
exact. Two fell in the first burst, two to rank-one peeling earlier today. The last two, the
convex-hull description (Theorem 1) and exactness (Theorem 3), argue over the faces of the
polyhedron Γ of multipliers.

## What was needed

Less than expected. No dimension theory and no face lattice: Theorem 1's induction runs on the
number of tight constraints, a natural number, and Theorem 3 needs no induction at all. The one
genuinely polyhedral fact is that the face of a polyhedron on which a linear objective is maximal
does not change under small perturbations of the objective. It is proved here from LP duality and
strict complementarity, without Minkowski–Weyl.

The rest of the kit: strict dual certificates for a face, a direction along which a family of
linear functionals is constant (rank–nullity), Farkas on a subspace in place of a closedness
argument, the semidefinite relaxation described through Γ (Lagrange multipliers under Slater's
condition and the dual of the semidefinite cone, from this morning's duality kit), and KKT on a
face containing a positive definite matrix.

## Results

`QCQPTightness.Exact.theorem_3` and `QCQPTightness.ConvHull.theorem_1` were accepted on the first
submission. All six theorems of the paper are now proved on the board.
