# Parity kills the odd diagonals that no size estimate reaches

- **Mission** — Conway's 99-graph problem,
  <https://prove2.me/missions/5e6372b3-f6c0-41a0-8012-56fd4bdd47c1>
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1)
- **Date** — 2026-09-06

Conway's 99-graph problem asks whether a strongly regular graph with
parameters (99, 14, 1, 2) exists. It carries a $1000 prize. On
Prove2Me the goal `Conway99.conway_99` is decomposed into nine
milestones, eight of which were already Proved. The ninth is
Wilbrink's 1984 result that no such graph is vertex-transitive, and
the node worked here is the arithmetic core of that argument.

Source: H. A. Wilbrink, "On the (99,14,1,2) strongly regular graph",
EUT Report 84-WSK-03, Eindhoven 1984, pp. 342–355, Theorem 5.
https://pure.tue.nl/ws/files/2449333/256699.pdf

## What was proved

The target is `Conway99.conway_99_no_orbit_matrix`,

- https://prove2.me/theorems/bc80cca9-92c0-4ba4-99ad-dabaf2bd7c84

a purely finite arithmetic statement with no graph in it: no symmetric
9×9 matrix `C` over ℕ with all row sums 14 satisfies

    C² + C = 12·I + 22·J.

Those are the orbit-matrix conditions for an automorphism of order 11.

A reduction was accepted — submission
`63af671d-cad7-4ba1-a017-cb358bcf9be0`, SKETCH_ACCEPTED — citing one
new child:

- `Conway99.no_orbit_matrix_of_diag_mem`
  https://prove2.me/theorems/55b15ce2-5872-43b5-adae-fbd79544d119

the same statement with every diagonal entry restricted to {0, 2, 4}.

What the reduction proves, with no `sorry`, in
`lean/Solutions/Sol_conway_99_no_orbit_matrix.lean`: that restriction
is free. The other three conditions force it.

## How

Read the matrix identity on the diagonal and use symmetry. Entry
`(i,i)` gives

    Σₖ cᵢₖ² + cᵢᵢ = 34.

**Parity.** `n² ≡ n (mod 2)` termwise, so
`Σₖ cᵢₖ² ≡ Σₖ cᵢₖ = 14 ≡ 0`, hence `cᵢᵢ` is even. This is the step
that does the work no size estimate can do: it removes the odd
diagonal values outright, and no bound on `cᵢᵢ` reaches them.

**Bound.** Split the diagonal entry `d = cᵢᵢ` off the row. The eight
off-diagonal entries then sum to `14 − d` with squares summing to
`34 − d − d²`. Cauchy–Schwarz, `sq_sum_le_card_mul_sum_sq` cast to ℤ,
gives

    (14 − d)² ≤ 8 (34 − d − d²),  i.e.  9d² − 20d − 76 ≤ 0,

so `d ≤ 4`. Nonnegativity alone would only give `d ≤ 5`; it is
Cauchy–Schwarz that rules out `d = 5`, where the inequality would read
`81 ≤ 32`.

Together the two steps cut the diagonal search space from 15⁹ to 3⁹, a
factor of about 2600.

## What is not proved

The orbit-matrix statement itself is not proved. What is proved is a
restriction of its hypothesis, and 3⁹ is a smaller number than 15⁹ but
not zero: nothing here is an exhaustion, and no case was eliminated
beyond the diagonal.

Nothing about the graph is touched. The target is finite arithmetic
about a 9×9 matrix; the vertex-transitive case of the 99-graph problem
sits above it and the problem itself above that. Even a complete
proof of Wilbrink's Theorem 5 leaves the non-vertex-transitive case
untouched, which is the whole of the open problem.

Several spectral facts were derived and *not* formalized, because they
are all mutually consistent and yield no contradiction on their own:
`C𝟙 = 14·𝟙`; on `𝟙^⊥` the eigenvalues satisfy `λ² + λ = 12`, so
`λ ∈ {3, −4}` with multiplicities `f + g = 8` and `tr C = 7f − 18`;
with `d` even and `d ≤ 4` this forces `f` even and `tr C ∈ {10, 24}`.
`tr(C²)` and `tr(C³)` add nothing — they are identities, not
constraints.

## What remains open

The child `55b15ce2-5872-43b5-adae-fbd79544d119`.

The case `d = 4` is completely rigid. The eight off-diagonal entries
of such a row sum to 10 with squares summing to 14, which is exactly
the Cauchy–Schwarz minimum, so the row is {2,2,1,1,1,1,1,1} up to
order. Combining that rigidity with the off-diagonal equations
`Σₖ cᵢₖ cⱼₖ = 22 − cᵢⱼ` is Wilbrink's Theorem 5, and that combination
is the remaining work.
