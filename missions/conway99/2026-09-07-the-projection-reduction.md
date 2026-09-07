# `M = C − 2J + 4I` satisfies `M² = 7M`, and that turns the orbit-matrix conditions into a rank-4 projection

- **Mission** — Conway's 99-graph problem
- **Target** — `Conway99.no_orbit_matrix_ten_of_no_four`
  (<https://prove2.me/theorems/45b537fd-4e72-4cfa-8ec3-26c448c45d47>), still **Open**
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

Nothing was submitted. This records a reduction that is built and checked, an
exhaustive computation that says which verdict to chase, and a precise account of
where the Lean proof stops.

## The premise this started from was wrong

The sibling `no_orbit_matrix_ten_of_exists_four` was Proved earlier the same day, and
the plan was to port its machinery — in particular the `mem_zero_*` pair, which turns
`∑ (n² ± n) = 0` into a pointwise membership. **That does not port.** For the row
profiles of this case there is no vanishing quadratic to exploit.

The platform's own text for the node says as much: this is the residual case of
Wilbrink's Theorem 5, the one he eliminated with "six hours on a programmable pocket
calculator". It was never a corollary of its sibling.

## What was built

Put `M = C − 2J + 4I`. The orbit-matrix conditions — symmetry, row sums `14`,
`C² + C = 12I + 22J`, diagonal in `{0,2,4}` — become

- `M² = 7M`, row sums `0`, `M i i = C i i + 2`, `tr M = 28`

so `M/7` is a rank-4 projection. Everything below is elementary and none of it is
specific to trace 10:

- `7·(xᵀMx) = ‖Mx‖²`, hence `M ⪰ 0` and, more usefully, **`xᵀMx = 0 ⟹ Mx = 0`** —
  a rank collapse rather than an inequality, which is what makes it a tool;
- `−2 ≤ M i j ≤ 2` off the diagonal, hence `C i j ≤ 4`, from `n² + n ≥ 0` termwise;
- for `i ≠ j` with `C i i = C j j = 0`: `C i j = 0` forces `M k i + M k j = 0` for
  every `k`, and `C i j = 4` forces `M k i = M k j`.

`missions/conway99/lean/Solutions/C99_nofour_aux.lean` — builds clean, zero `sorry`.
Declarations: `Msq`, `MrowSq`, `quad_key`, `psd`, `kernel_of_quad_zero`, `Mle`,
`sum_ind`, `quad_ind`, `pair_nonneg`, `collapse_neg`, `collapse_pos`.

## Which verdict to chase

An exhaustive search — diagonal `[2,2,2,2,2,0,0,0,0]` without loss of generality,
row by row with every pair equation checked — returns **0 solutions** over roughly
70 million nodes. So the statement is true and `Proved` is the target; a `Disproved`
attempt would be wasted.

## What is not proved

The node itself. The reduction is machinery, not a proof, and the mission root is
untouched.

The search is a computation, not a certificate. It says where to aim; it is not a
Lean proof and nothing here converts it into one.

## Where it stops, precisely

Ordering rows with the zero-diagonal block first, survivors after each row run
`2716 → 162197 → 156705 → 40680 → 3456 → 0`. The zero block plus its cross block
leaves **40680 ordered completions**, which is **23 classes** up to `S₄ × S₅` — those
are listed in `missions/conway99/search/nf6.log`. Twenty-three is human scale; forty
thousand is not, and a Lean proof that merely "picks four indices" walks the ordered
tree rather than the quotient.

There is a clean conceptual route: the `w_i` generate a rank-4 integral lattice with
`7L* ⊆ L`, which forces `det L = 1`, so `L ≅ ℤ⁴`, and a small search finishes. It
needs **"rank-4 positive-definite unimodular ⟹ ℤ⁴"**, which Mathlib does not have at
this revision. That is the gap, and it is a real piece of lattice theory rather than
a missing lemma.

## What remains open

`no_orbit_matrix_ten_of_no_four`, and `no_orbit_matrix_diag_sum_ten`
(<https://prove2.me/theorems/79b57254-3075-4bec-b78d-59638c243d1d>) behind it. The
reduction above and the 23-class target are now written down, which is the useful
part of this pass.
