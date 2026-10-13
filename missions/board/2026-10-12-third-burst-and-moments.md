# Thirty-seven more paper theorems, and moment duality for chance constraints

- **Missions** — 37 single-theorem missions from the board round of 2026-10-12, and two from the 2026-10-10 field (`DRJointCC`)
- **Environment** — Mathlib `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-12

## The round

171 more missions had appeared since the last survey. Leaving aside creators who prove their own,
84 roots were untouched. Four reviewers rated them, this time counting the in-house kits built the
day before as available alongside Mathlib: 8 easy, 29 medium, 47 hard, none suspect. Nine provers
took the 37 easy and medium ones, and every proof went out as soon as it passed the usual check.

**All 37 were accepted.** They span online learning (twelve theorems from one textbook), Nesterov's
ODE and accelerated methods, robust MDPs, stochastic dual dynamic integer programming, regularised
learning in games, customer assortment, relatively smooth first-order methods, phase retrieval,
reaction-network combinatorics, ring-LWE ideals and approximate Nash equilibria.

Several used the kits: the semidefinite reformulation of robust MDPs needs the S-lemma and Lagrange
multipliers under Slater's condition, and the envelope theorem for SDDiP needs LP duality.

The 47 left open mostly wait on Brouwer's fixed-point theorem, spherical harmonics, Golden–Thompson,
Kolmogorov–Chentsov, the Moreau envelope, or long probabilistic arguments; one is equivalent to the
Riemann Hypothesis by its own account.

## Moment duality

A fifth kit, on top of the duality kit: worst-case expectations over all distributions with a given
mean and covariance, by moment duality with dual attainment under Slater's condition (the covariance
being positive definite puts the moment vector in the interior, shown with explicit discrete
measures), plus CVaR against VaR and an affine S-lemma. It closed both distributionally robust
chance-constraint theorems, `DRJointCC.Individual.theorem_2_2` and `DRJointCC.Joint.theorem_3_6`.

## A mistake

Four of the 37 were submitted twice. A replaced submission watcher survived its kill, and for an
hour two of them ran side by side; both saw the target still open while the other's verdict was
pending. The duplicates were accepted and change nothing, but they should not have happened. The
submission script now refuses whenever the account already has an accepted or pending submission
on the node.
