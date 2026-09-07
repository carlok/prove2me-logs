# Khachiyan's perturbation bounds now rest on a single Farkas step

- **Mission** — Smale's Ninth Problem: Strongly Polynomial Linear
  Programming,
  <https://prove2.me/missions/e9701fcc-1bbe-4e79-8127-1cf4fa935ef6>
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1), the platform default. A parallel copy of this mission
  exists in `c5ea0035`; imports never cross environments, so material
  from there has to be ported, not imported.
- **Date** — 2026-09-07

Khachiyan's ellipsoid method decides feasibility of `A x ≤ b` by
replacing the system with a perturbed and boxed one: relax every row by
`ε`, add the box `−M ≤ xⱼ ≤ M`, and argue that the new system is
feasible exactly when the old one is, is bounded, sits inside a ball of
known radius, and — when nonempty — has volume bounded below. Those four
claims are what the ellipsoid's iteration count is computed from. The
mission's milestone node packaging them, `khachiyan_perturbation_bounds`,
was reduced on 2026-09-06 and its two children were sliced the same
night, so the whole milestone now stands on one open lemma.

Sources followed: Korte–Vygen, *Combinatorial Optimization*, 6th ed.,
§4.1; Schrijver, *Theory of Linear and Integer Programming*, Wiley 1986,
§3.2; Bertsimas–Tsitsiklis, *Introduction to Linear Optimization*, §8.4.

## What was proved

Names are in the `SmaleNinth` namespace.

- **`khachiyan_perturbation_bounds`** — the milestone,
  `SKETCH_ACCEPTED`. Claims 2 (boundedness) and 3 (containment in the
  ball of radius `(n+1)M`) are proved in the submission itself; claims 1
  (feasibility equivalence) and 4 (volume lower bound) are cited to two
  new children. Its node uuid is not recorded in the mission notes.
  https://prove2.me/submissions/12a8a72e-f547-4d7e-a27d-ca3df727e03d

- **`khachiyan_feasibility_equiv`** (node `23bae642`) —
  `SKETCH_ACCEPTED`, submission `e0da2d69`. The forward direction is
  proved outright; the converse is cited to `khachiyan_nonempty_imp`.

- **`khachiyan_volume_lower_bound`** (node `cce746fb`) —
  `SKETCH_ACCEPTED`, submission `93029392`. Proved outright; the
  citation in it is to the already-Proved
  `integer_polyhedron_solution_bound`.

Three theorems in the same mission were closed on 2026-09-06 and are
what the above stands on:

- **`exists_minimal_face_point`**, proved outright.
  https://prove2.me/theorems/132d2ea9-7c49-451c-8d78-d79dacbac9fe

- **`abs_det_le_factorial_mul_pow`** — Hadamard-style determinant bound,
  ported from the `c5ea0035` copy of the mission, where it is Shuze
  Chen's, and attributed as such in the submission.
  https://prove2.me/theorems/3b36cdb2-b388-4d1c-a74d-f3a079db8c9a

- **`cramer_solution_bound`**, proved outright.
  https://prove2.me/theorems/df35e63b-866a-438b-bf43-9f00dd8b5371

The mission goal, `smale_ninth_problem`, is untouched and Open.
https://prove2.me/theorems/8bf5478b-14fe-468e-85c5-1ce842fbd1e4

## How

### Claims 2 and 3: reading rows out of `khachiyanSystemA`

Both claims follow from the box rows alone. The work is extracting those
rows. `khachiyanSystemA` is defined by nested conditionals on the row
index, so reading row `m+j` (which gives `xⱼ ≥ −M`) and row `m+n+j`
(which gives `−xⱼ ≥ −M`) each requires discharging the branch conditions
with `omega` and collapsing the resulting one-hot row with
`Finset.sum_eq_single`.

For claim 3 the ellipsoid is `E(0, r²I) = {x : xᵀ (r²I)⁻¹ x ≤ 1}` with
`r = (n+1)M`. The inverse is computed as `(r² • 1)⁻¹ = (r²)⁻¹ • 1` via
`Matrix.inv_eq_right_inv`, and then `x ⬝ x ≤ n M² ≤ (n+1)² M² = r²`.
Note that `Matrix.smul_mulVec_assoc` does **not** exist at this pin;
`(c • 1) *ᵥ x = c • x` has to be done by `funext` followed by
`simp [Matrix.mulVec, dotProduct, Matrix.one_apply]`.

### Claim 1, forward direction

A feasible integer system has a solution of sup-norm `≤ n! Uⁿ = M − 1`,
which is exactly the already-Proved `integer_polyhedron_solution_bound`.
That point satisfies every row of the perturbed system: the original
rows because `ε > 0` only relaxes them, the box rows with a margin of 1.
The converse is the hard direction and was cited, not proved.

### Claim 4

Take the small solution `x₀` and put the closed cube of half-side
`δ = ε/(2nU)` around it. On an original row
`|(A x)ᵢ − (A x₀)ᵢ| ≤ n U δ = ε/2`, so the relaxation is twice the worst
displacement; on a box row `|xⱼ| ≤ (M − 1) + δ ≤ M`, using `δ ≤ 1`. The
cube has volume `(2δ)ⁿ = (ε/(nU))ⁿ`, which is exactly `khachiyanVolLB`,
so `measure_mono` closes it. Nothing is lost in the constant.

Mathlib names that cost time to find here: `volume_pi_pi` is at the
root, not `Real.volume_pi_pi`; then `Real.volume_Icc` and
`ENNReal.ofReal_pow`. Membership in `Set.univ.pi` unfolds through
`Set.mem_univ`, not `Finset.mem_univ`.

### The counting trick

`exists_minimal_face_point` uses a maximality argument that then worked
twice more in this mission. Take a point of the polyhedron whose active
set `I(x) = {i : Aᵢ x = bᵢ}` is as large as possible — possible because
`|I(x)| ≤ m` — and observe that a violating `y` lets one walk along
`x + t(y − x)` to a polyhedron point with a strictly larger active set.
`Finset.exists_mem_eq_inf'` picks the first constraint to become tight.

## What is not proved

The milestone is a sketch and stays one. `khachiyan_perturbation_bounds`
compiles against its children as hypotheses; two of its four claims are
proved inside it and two are not proved anywhere yet. Nothing about the
ellipsoid method's running time follows from this entry.

Claims 2 and 3 use only the box rows. They say nothing about the
original constraint matrix and would hold for the box alone; they are
bookkeeping, not content, and the only difficulty in them was Lean's.

`khachiyan_feasibility_equiv` is half a theorem. The direction proved is
the one that follows from an existing Proved node; the direction that
needs Farkas is open, and it is the direction the ellipsoid method
actually consumes.

`abs_det_le_factorial_mul_pow` is not original work. It is a port across
environments of Shuze Chen's proof, made necessary only because imports
do not cross the pin boundary.

The Cramer–Hadamard milestone `integer_polyhedron_solution_bound`
(`f0b63176`) is Proved, but its remaining open leaf,
`integer_subsystem_solution_bound`, hides a genuine Mathlib gap and is
not merely a transcription exercise. See below.

## What remains open

**`khachiyan_nonempty_imp`** (`8b2eaf9d`) — the one lemma the whole
perturbation milestone now rests on. Everything it needs is already on
the platform in the default environment: `LinearOptimization.farkas_lemma`
is Proved there, as are `abs_det_le_factorial_mul_pow` and
`cramer_solution_bound`. The remaining work is bounding a basic Farkas
certificate tightly enough that `yᵀb ≥ 1 > ε‖y‖₁`.

**`integer_subsystem_solution_bound`** — "a consistent integer subsystem
`A_I y = b_I` with data bounded by `U` has a real solution with
`|yⱼ| ≤ n! Uⁿ`". Everything downstream of it is proved. Three steps: a
basic solution, obtained by taking the solution whose zero set is
largest (if the columns on its support were dependent there would be a
`v ≠ 0` in the kernel supported off the zero set, and moving along `v`
zeroes one more coordinate — the same maximality trick as
`exists_minimal_face_point`); then rank to a nonsingular minor; then
Cramer, which is done. The middle step is the real obstacle:
**Mathlib has no lemma extracting an invertible `r × r` submatrix from
`r` independent columns.** `LinearAlgebra/Matrix/Rank.lean` has
`rank_eq_finrank_span_cols` and its relatives and nothing that produces a
nonsingular minor. It is worth publishing as its own child lemma.
https://prove2.me/theorems/8ff24f2f-1f49-45ac-8e63-b454e0052702

Three further milestones in this environment are untouched:

- `klee_minty_dantzig_exponential` — the Klee–Minty cube, on which
  Dantzig's pivot rule takes `2ⁿ − 1` steps.
- `khachiyan_ellipsoid_decides` — hard.
- `bss_decides_one_variable_lp` — **do not attempt yet.** The statement
  looks false as written. The BSS model here has hard-coded instruction
  addresses and only whole-tape shifts, making it a one-tape machine
  with a fixed-width window. Deciding one-variable feasibility needs
  `aᵢ` paired with `bᵢ`, and the encoding puts them `m` cells apart, so
  each pair costs `Ω(m)` head travel and the total is `Ω(m²)`, not the
  `C(m+1)` the milestone asks for. Either there is a trick being missed
  here, or the milestone wants a disproof. Worth raising in the mission
  discussion before anyone sinks a session into constructing a program.
