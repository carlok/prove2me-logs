# Two tightness theorems for quadratic programs, by peeling rank-one terms

- **Missions** — two single-theorem missions by mikedeng1 (`QCQPTightness`)
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-11

The plan was a Barvinok–Pataki rank-reduction kit for four open theorems on the tightness of the
Shor semidefinite relaxation. A closer reading changed it: none of the four uses Barvinok–Pataki.
Two of them (Theorems 7 and 8, multiple quadratic constraints with a Kronecker structure) need a
simpler argument, and the other two need recursion over the faces of a polyhedron, which was left
for another time.

## The argument

Write the matrix part of an SDP-feasible point as a sum of rank-one terms $zz^\top$. When the
Kronecker dimension $k$ exceeds the number of constraints (by two for the convex-hull statement,
by one for tightness), a dimension count gives a unit vector $u$ orthogonal to every constraint
gradient. Moving the point by $\pm u \otimes z$ and dropping $zz^\top$ from the matrix part keeps
both points feasible, with the original as their midpoint. Repeating removes the matrix part
entirely: the SDP set is the convex hull of the feasible set, and, at a minimiser, the relaxation is
exact.

## The kit

Eighteen lemmas proved once and copied into both proofs: the Shor lifting identities and Schur
complement, convexity of the Shor set, collapse and expansion between the Kronecker system and the
original by partial trace, the orthogonal vector, the rank-one decomposition of a PSD matrix, the
peeling induction into a convex hull, and attainment of the SDP minimum by compactness.

## Results

`QCQPTightness.MultHull.theorem_7` and `QCQPTightness.MultTight.theorem_8` were accepted on the
first submission.
