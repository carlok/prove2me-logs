# The descent step of Schneider's method needs no order-of-growth theory — a Schwarz lemma built by hand out of `dslope` is enough

- **Mission** — six-exp, a decomposition ladder for the six exponentials theorem
- **Theorem** — `SX.descent_step` (`d2ebac57-a209-470b-a366-8430f6fe9ff3`), rung 4
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07
- **Status** — Proved, submission `f7c8160b-f861-4a05-8b94-1fe4a6342f2a`

Rung 4 was the rung we expected to lose. It is the analytic-arithmetic squeeze at
the centre of Schneider's method, and the bundle defines `SX.OrderAtMost` precisely
because Mathlib at this revision has no order-of-growth theory, no Schneider–Lang, no
Gelfond–Schneider and no auxiliary-function machinery. The lesson of the session is
that none of that is needed: the descent never uses an abstract growth class, only one
concrete Schwarz estimate, and that estimate is three dozen lines on top of the
maximum modulus principle.

## The one analytic ingredient

Everything analytic reduces to:

> `f` entire, `S` a finite set of zeros of `f` with `‖ζ‖ ≤ r`, `‖f‖ ≤ B` on `‖z‖ = R`,
> `0 < r < R`, `‖w‖ ≤ r`. Then `‖f w‖ * (R − r) ^ S.card ≤ B * (2r) ^ S.card`.

The induction is on `S.card`. The base case is
`Complex.norm_le_of_forall_mem_frontier_norm_le` on `Metric.ball 0 R`, with
`frontier_ball` and `closure_ball` to convert "on the circle" into "on the frontier".
The step divides out a single zero `ζ` using `dslope`:

- `sub_smul_dslope_of_zero` gives `(z − ζ) * dslope f ζ z = f z` when `f ζ = 0`;
- `Complex.differentiableOn_dslope` (Riemann removable singularity, with `s = univ`)
  keeps the quotient entire;
- on `‖z‖ = R` the quotient is bounded by `B / (R − r)`, which is exactly what makes
  the induction hypothesis apply with a smaller `S` and a shrunk `B`.

That is the whole of the "Schwarz lemma" the brief asked for. No order of growth, no
Hadamard factorisation, no Jensen formula. Mathlib has `Analysis/Complex/JensenFormula`
and `Analysis/Complex/Hadamard`, and neither is the right tool here: they answer
questions about counting zeros, whereas the descent already knows where its zeros are.

## Choosing the radii is what makes the constants collapse

The classical write-ups take `R` "large" and then fight the error terms. The version
that formalises cleanly fixes the *ratio* instead. With `Y = ∑ ‖y j‖`, put

    r = N·Y + 1,     R = 5r.

Then every lattice zero `∑ mⱼ yⱼ` with `mⱼ < N`, and the new point `w` with `mⱼ ≤ N`,
sits inside `‖·‖ ≤ r`; and `R − r = 4r`, so `(R−r)^n = 2^n · (2r)^n` and the whole
Schwarz factor is exactly `2^(−N^l)` with no leftover `r`. Everything else on the
right-hand side is then visibly `exp(O(L·N))`, and the final comparison is
`N^l · log 2` against `C·L·N`. Fixing the ratio rather than the radius removed what
would otherwise have been a page of real-analytic bookkeeping.

`R = 5r` (rather than `R = A·N` for a constant `A` depending on `Y`) is what keeps
`M₀` independent of `N`: the analytic price `L·X·R ≤ 5X(Y+1)·L·N` is linear in `N`,
which is the only regime in which `N^l` can win.

## The arithmetic side: `𝓞 K` is a better denominator than `ℤ`

`NumberField.house` has everything needed — `house_sum_le_sum_house`, `house_mul_le`,
`house_pow_le`, `house_intCast`, `norm_embedding_le_house`,
`norm_norm_le_norm_mul_house_pow` — with two gaps worth recording.

1. **No `Algebra.IsAlgebraic ℤ K` instance.** `Algebra.natDenominator` and
   `Algebra.IsAlgebraic.exists_integral_multiples` both want algebraicity over `ℤ`,
   and for `K` a number field that instance does not resolve (`IsAlgebraic ℚ a` does,
   via `Algebra.IsAlgebraic.isAlgebraic`, but there is no transfer to `ℤ` at hand).
   The fix is to give up on a *rational-integer* denominator: take the denominator in
   `𝓞 K` instead, via `IsLocalization.exists_integer_multiple (𝓞 K)⁰`, and multiply
   the `d·l` of them together. Liouville does not care: `‖σ (b^E)‖ ≤ house b ^ E`
   costs the same `exp(O(L·N))` as an integer denominator would.

2. **`house_prod_le` is stated for `s : Finset K`, not for an indexed family.** For
   `∏ i, ∏ j, f i j` one needs `house (∏ i ∈ s, f i) ≤ ∏ i ∈ s, house (f i)`, which is
   a three-line `Finset.induction` on top of `house_mul_le`. Worth upstreaming.

Membership in `integralClosure ℤ K` is definitionally `IsIntegral ℤ`, so the
subalgebra closure lemmas (`Subalgebra.sum_mem`, `pow_mem`, `prod_mem`,
`algebraMap_mem`) do all the integrality bookkeeping; `mem_integralClosure_iff` did not
resolve by name in this revision, but the `Iff.rfl` means it is not needed.

## A Lean trap worth naming: `set` leaves a let-binding

The first assembly of the arithmetic bound timed out at `whnf` and `isDefEq` with
200 000 heartbeats. The cause was not the size of the proof: `set Hb := max 1 (house b)`
introduces `Hb` as a *local definition*, so every `positivity` and every defeq check is
free to unfold it — through `house`, through `canonicalEmbedding`, through the whole
`NumberField` stack. Adding `clear_value` after the defining facts are established
(and replacing `positivity` by explicit `pow_nonneg`/`mul_nonneg` terms) took the
declaration from "times out" to a few seconds. On a file where `set` names anything
built from heavy definitions, `clear_value` should be reflexive.

## Where `d + l < d·l` is actually used

Once. In `SXD.endgame`. From `N^l · log 2 ≤ C·L·N` and `L^d ≤ c·M^l ≤ c·N^l`, raise
the first to the `d`-th power to get `N^(ld) (log 2)^d ≤ C^d c N^(l+d)`. The hypothesis
is exactly what lets one write `l·d = k + (l + d)` with `k ≥ 1`; cancelling `N^(l+d)`
then bounds `N ≤ N^k ≤ C^d c / (log 2)^d`, and `M₀ = max 1 (⌈·⌉₊ + 1)` contradicts it.
Every other appearance of the hypothesis in the informal proof is decorative.

## What is not proved

The descent is one step. It says that vanishing to order `N^l` propagates to
order `M^l` at the next scale; it does not by itself produce the auxiliary
function, does not run the induction, and proves nothing about transcendence.

The estimate is not sharp. Fixing `R = 5r` is a choice made so the Schwarz
factor comes out as exactly `2^(−N^l)` with nothing left over — good enough for
this ladder, and no more than that. A sharper constant would need the classical
treatment this deliberately avoids.

`SX.OrderAtMost` is defined in the bundle for this rung and is **never used**.
The bundle carries a definition that earns nothing.

## Status of the ladder

| rung | theorem | status |
|---|---|---|
| 2 | `SX.six_exponentials_of_numberField` | **Proved** (via its SKETCH_ACCEPTED reduction) |
| 3 | `SX.exists_aux_expSum` | **Proved** |
| 4 | `SX.descent_step` | **Proved** |
| 5 | `SX.eq_zero_of_expSum_vanishes` | **Proved** |

The ladder is closed, and `DiazModulus.six_exponentials` with it.

A correction to what this entry originally said. It named rung 3's obstacle as the
private `c₁ K` scouted in `SX_HouseWorkaround.lean`. That was wrong, and the
workaround was never needed: `NumberField.house.exists_ne_zero_int_vec_house_le`
returns coefficients in `𝓞 K`, and rung 3 needs them in `ℤ`, so that route could
not have worked whatever the constant's visibility. Rung 3 went through the public
`Int.Matrix.exists_ne_zero_int_vec_norm_le` instead. See
`2026-09-07-auxiliary-function.md`.

Local file: `missions/six-exp/lean/Solutions/SX_Sol_descent.lean` (620 lines, no
`sorry`; `#print axioms solution` gives only `propext`, `Classical.choice`,
`Quot.sound`). The verbatim restatement check is `Theorems/SX_VerifyDescent.lean`.
