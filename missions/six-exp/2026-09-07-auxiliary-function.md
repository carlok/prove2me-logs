# Siegel's lemma over a number field, with the exponent switched off

- **Mission** — six-exp, a decomposition ladder for the six exponentials theorem
- **Node** — `SX.exists_aux_expSum` (`f0a028dd-7409-4134-b87b-24b2921be5ae`), rung 3 — **Proved**
- **Submission** — `b09434ad-f78b-47d4-8eb8-16f7843e66e4`, ACCEPTED 2026-09-07
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)

Rung 3 asks for the auxiliary function of Schneider's method: given `d + l < d·l`,
two families `x`, `y`, and a number field `K` containing all `d·l` numbers
`θᵢⱼ = exp(xᵢyⱼ)`, produce a constant `c` — *before* `M` — such that for every large `M`
there is an `L` with `L^d ≤ c·M^l` and a nonzero integer vector `p` on the box `[0,L)^d`,
of height at most `exp(c·L·M)`, killing the `M^l` values of `F(z) = ∑ p_λ exp(⟨λ,x⟩z)` at
the lattice points `⟨m,y⟩`, `m ∈ [0,M)^l`.

## The route that does not work, and why it is not the private constant

Every earlier note on this rung — the docstring of `Theorems/SX_Aux.lean`,
`SX_HouseWorkaround.lean`, `MATHLIB_ISSUE_DRAFT.md` — is built around
`NumberField.house.exists_ne_zero_int_vec_house_le` and the fact that its bound mentions
the `private` constant `NumberField.house.c₁ K`. That is the wrong obstruction. The
conclusion of that lemma (`Mathlib/NumberTheory/NumberField/House.lean:343`) is

    ∃ ξ : β → 𝓞 K, ξ ≠ 0 ∧ a *ᵥ ξ = 0 ∧ ∀ l, house (ξ l).1 ≤ …

The solution vector lives in `𝓞 K`. Rung 3 must hand rung 5 a `p : (Fin d → ℕ) → ℤ`,
and rung 5 (`SX.eq_zero_of_expSum_vanishes`, proved earlier) is stated over `ℤ`. Wrong
kind of solution, whatever happens to `c₁`. The private constant was never the problem.

What works is the public lemma House.lean is built on:
`Int.Matrix.exists_ne_zero_int_vec_norm_le` (`Mathlib/NumberTheory/SiegelsLemma.lean:181`),
which is constant-free and gives integer solutions. House.lean's own reduction from
`𝓞 K`-coefficients to an integer matrix — the `private def asiegel` — is about fifteen
lines to rebuild in public, and that is what `AuxSiegel.exists_int_kernel` in
`Solutions/SX_Sol_aux.lean` is.

## Turning Siegel's exponent into a linear bound

Siegel's lemma bounds the solution by `(n · max 1 ‖A‖)^(m/(n−m))` for `m` equations in
`n` unknowns. Taken naively here that exponent is `[K:ℚ]·M^l`, and the height comes out
as `exp(c·M^l·L·M)` — useless: rung 4 needs `exp(c·L·M)`. The fix is to ask for twice as
many unknowns as equations,

    2 · (card ρ · [K:ℚ]) ≤ card κ,

which forces `m/(n−m) ≤ 1` and collapses the bound to `card κ · max 1 (cc K · A)`, linear
in the entry bound. This is the single design decision the whole rung turns on, and it
costs nothing: `L` is picked as the least natural with `2·[K:ℚ]·M^l ≤ L^d`, and minimality
plus `L ≤ 2(L−1)` then gives `L^d ≤ 2^d · 2 · [K:ℚ] · M^l`, which *is* the interface's
`L^d ≤ c·M^l`. The two constraints on `L` are the same constraint read twice.

Here `cc K = [K:ℚ] · ‖((basisMatrix K)ᵀ)⁻¹‖`, assembled from
`NumberField.house.basis_repr_norm_le_const_mul_house`, `basisMatrix` and `equivReindex`,
all public.

## Denominators: one algebraic integer, not one rational integer

`IsLocalization.exist_integer_multiples_of_finite` over `nonZeroDivisors (𝓞 K)` produces a
single `b ≠ 0` with `b·θᵢⱼ ∈ 𝓞 K` for all `d·l` numbers simultaneously. There is no need
for `b` to be a rational integer: scaling every row of the system by the single nonzero
constant `b^T`, `T = d·l·L·M ≥ ∑ᵢⱼ λᵢmⱼ`, leaves the solution set alone. So the entries

    a(m,λ) = b^(T − ∑ λᵢmⱼ) · ∏ᵢⱼ u(i,j)^(λᵢmⱼ),   algebraMap (u i j) = b·θᵢⱼ

are algebraic integers with `algebraMap (a m λ) = b^T · ∏ᵢⱼ θᵢⱼ^(λᵢmⱼ)`, and `b^T ≠ 0`
carries the kernel back to `ℂ` at the end.

Submultiplicativity of the house (`house_mul_le`, `house_pow_le`, plus an indexed
`house_prod_le'` that Mathlib only has for `Finset K`, not for indexed families) then
gives `house (a m λ) ≤ H^T` uniformly in `m, λ`, with
`H = 1 + house b + ∑ᵢⱼ house (b·θᵢⱼ)`. Note `H` and `b` are fixed before `M` — this is
what lets `c` be named ahead of `M`, which the rung-2 assembly requires.

## The constant

    c = 2^d·2·[K:ℚ] + d + log(max 1 (cc K)) + d·l·log H + 1,   M₁ = 1.

The height estimate is then `L^d · max 1 (cc K · H^T) ≤ exp(c·L·M)`, using `L ≤ exp L`
for the `L^d` factor and `T = d·l·L·M` for the `H^T` factor. Everything is explicit; no
constant is left implicit or private anywhere.

## Leftovers

- `hx`, `hy` (the ℚ-linear independence of the two families) are **not used** by rung 3.
  They are consumed by rungs 4 and 5. Rung 3 is pure linear algebra over `K` plus counting.
- `d + l < d·l` is used only to get `d ≥ 1`, `l ≥ 1` (it in fact forces `d, l ≥ 2`).
- Mathlib gap worth reporting, separate from the `c₁` one: `NumberField.house_prod_le` is
  stated for `∏ x ∈ s, x` with `s : Finset K` only. The indexed form
  `house (∏ i ∈ s, f i) ≤ ∏ i ∈ s, house (f i)` is a one-line `simpa` from
  `Finset.norm_prod_le` and is what any application actually wants.

## What is not proved

This is one rung. It constructs an auxiliary function with the right height and
vanishing; it proves nothing about transcendence, and on its own it says nothing
about six exponentials.

The construction is not canonical or optimal. The constant `c` is one that works,
not a sharp one, and the choice to force Siegel's exponent below `1` rather than
estimate it is a convenience that happens to match what rung 4 needs — a different
descent would want a different `c`.

`hx` and `hy` are genuinely unused, so this rung would hold for families that are
not `ℚ`-linearly independent. That is not a defect: the independence is what rungs
4 and 5 consume. But it does mean the statement is weaker than its name suggests
when read alone.

## What remains open

Nothing under this rung. Rung 4 (`SX.descent_step`) landed shortly after this one,
which flipped rung 2 through its SKETCH_ACCEPTED reduction, and
`DiazModulus.six_exponentials` with it. The ladder is closed.
