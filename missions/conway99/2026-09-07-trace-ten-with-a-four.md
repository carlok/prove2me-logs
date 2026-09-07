# Seven is not a sum of three squares, and that closes the trace-ten case of Conway's 99-graph

- **Mission** — Conway's 99-graph problem
- **Node** — `Conway99.no_orbit_matrix_ten_of_exists_four`
  (<https://prove2.me/theorems/af322e9e-ddab-4626-bcfb-3e0c6f93f129>) — **Proved**
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

Conway asked whether a strongly regular graph with parameters `(99, 14, 1, 2)` exists.
If one did and were vertex-transitive, a group action would produce a `9×9` **orbit
matrix**: entries in `ℕ`, symmetric, every row summing to `14`, satisfying
`C² + C = 12 I₉ + 22 J₉`, and with diagonal entries in `{0, 2, 4}`.

Ruling out orbit matrices rules out the vertex-transitive case. The diagonal sum is the
natural case split. This node is the trace-`10` case in which some diagonal entry equals
`4`.

## What was proved

No orbit matrix has diagonal sum `10` with at least one diagonal entry equal to `4`.

## How

Fix `i₀` with `C i₀ i₀ = 4`. The trace and diagonal constraints force the rest of the
diagonal to be supported on two further indices `x`, `y`. Expanding `C² + C` along row
`i₀` gives, for every `z`,

    ∑ₖ C i₀ k · C z k = 14 + 3·C z i₀ + C z x + C z y

and comparing with the value `22 − C i₀ z` forced by the matrix identity yields
`C x x = C y y = C x y = 0` together with `C j x + C j y = 4` for every remaining index
`j`.

Write `R` for the six remaining indices, `a j = C x j`, `c j = a j − 2`, and
`e j l = C j l − 2` on `R × R`. The constraints become `∑ c = 0`, `∑ c² = 6`, `|c| ≤ 2`,
`∑_l e j l = −3`, `∑_l (e j l)² = 13 − 2 c j² − C j j`, `∑_l c l · e j l = −c j`, and
`∑_{j ∈ R} C j j = 6`.

Either some `c j₀ = ±2`, which dies to a sign argument — `n(n+1) ≥ 0` forces that row's
entries into `{0, −1}` and the remaining `c` values into the opposite sign — or every
`c j = ±1`. In that case `R` splits as `P ⊔ N` with `|P| = |N| = 3`, and row splitting
gives `∑_P e = −2` and `∑_N e = −1` for `j ∈ P`.

The endgame is a fact about integers rather than about graphs. **Seven is not a sum of
three squares**, so the `N`-block square sum cannot be `7`. That pins the two
`P`-off-diagonal entries of each `j ∈ P` to `{2, 0}` or to `{3, 1}` in raw `C` values.
Those two sets are disjoint, so all three rows of `P` must use the same one — and then
the three off-diagonal entries of the `P`-block would be three pairwise-distinct values
drawn from a two-element set. Contradiction.

The search space was first checked in Python, returning zero solutions. That search also
showed the full `B² + B` identity on `R` is **not** needed: the row sums, the row square
sums, and `(B + I)a = 20·1` suffice. The hand proof was written to use only those.

## What is not proved

This is one case of one case. It says nothing about orbit matrices with a different
diagonal sum, and nothing about Conway's problem for graphs that are not
vertex-transitive — which is the general case and is untouched.

The mission root `Conway99.conway_99` remains Open, as do
`conway_99_not_vertex_transitive`, `conway_99_no_orbit_matrix` and
`no_orbit_matrix_of_diag_mem`.

## What remains open

The immediate sibling: `no_orbit_matrix_ten_of_no_four`
(<https://prove2.me/theorems/45b537fd-4e72-4cfa-8ec3-26c448c45d47>), the trace-`10` case
with diagonal in `{0, 2}` only — five `2`s and four `0`s. The row profiles are
`∑_{k≠i}(C i k − 2) = −2` with square sum `10` when `C i i = 0`, and `−4` with square sum
`12` when `C i i = 2`. Once both trace-`10` cases are closed, `no_orbit_matrix_diag_sum_ten`
follows immediately.

The machinery is reusable and should port directly: `rowZ`, `sqZ`, `offZ`, `entryLe`,
`four_row`, `mem_zero_negOne`, `mem_zero_one`, `no_seven`, `pblock`. The `mem_zero_*` pair,
which turns `∑ (n² ± n) = 0` into a pointwise membership, did most of the work.
