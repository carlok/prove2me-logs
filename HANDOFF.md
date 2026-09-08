# Open threads at 2026-09-08 17:10 UTC

## The frontier — four leaves, four different kinds of thing

| leaf | uuid | what it is |
|---|---|---|
| `DiazModulus.recip_pi_not_log_real_gamma` | `29c99457` | **start here** — Gelfond–Schneider-shaped half of (S) |
| `DiazModulus.recip_pi_not_log_imag_gamma` | `dea45a44` | the other half of (S) |
| `DiazModulus.four_exponentials_trdeg_one` | `2c0f35ea` | **citation boundary, not a task** — see below |
| `..._period_aligned_norm_free` | `1b43101e` | the matrix route is proved impossible; needs a new idea |
| `DiazModulus.norm_transcendental_of_generic_conj_pair` | `ed970912` | EvanLLL's; equivalent to the whole root |

**(S) has been split and the split is linked.** `DiazModulus.recip_pi_not_log`
(`b5a16bec`) now has two children, reduction `SKETCH_ACCEPTED`. It is not a case distinction:
`S₀ = {γ ∈ Q̄ : γ/(iπ) ∈ ℒ}` is a ℚ-subspace closed under conjugation, so `γ ∈ S₀` forces
`Re γ ∈ S₀` and `i·Im γ ∈ S₀`. Attack `real_gamma` first — γ real makes `γ/(iπ)` purely
imaginary, so the target is a modulus-one algebraic point that is provably not a root of
unity. Account in `missions/diaz/SPLIT_S.md`, Lean in `DZ_SPLITS_core.lean`.

Two further leaves already reduce to (S), so closing both children closes four nodes.

**Do not try to prove `four_exponentials_trdeg_one`.** It is Roy–Waldschmidt 1995 Thm 1,
proved by Brownawell 1974 and Waldschmidt 1973, and an audited scoping pass found essentially
none of the machinery in Mathlib — the blocker is Philippon's zero estimate, with Wirsing's
theorem second. Its description now says all this. Six exponentials does **not** imply it
(3×2 versus 2×2 plus a trdeg hypothesis). The source is held at
`missions/diaz/sources/roy-waldschmidt-1995-quadratic-relations.pdf`.

## Held open overnight — close tomorrow if unclaimed

| node | uuid | proof sitting in |
|---|---|---|
| `Diaz.pair_dichotomy_exclusive` | `99e66042` | `DZ_MINE_check2.lean` |
| `Diaz.conj_combination_off_rays` | `926f2540` | `DZ_MINE_check.lean` |
| `CollapsibleCubics.cubic_collapsible_of_not_normForm_repr` | `faff93b8` | — |

`DiazModulus.aligned_norm_free_no_rational_log_matrix` (`931b8b88`) is also open and provable
today from `DZ_FREE_*.lean`, held under the same rule.

None had a submission as of 17:07.

## Contributors, and their ground

- **`EvanLLL`** — leaf 1 and its crux, plus the `BertsekasDP.*` mission. Off limits.
- **`quesswho`** — created and actively works Collapsible Cubics; still publishing there
  (`pi_div_psi_le_iff_exists_theta`, Open, 14:55). We split their root; tread carefully.
- **`cm`** — closed `CollapsibleCubics.cubic_collapsible_of_normForm_repr` at 12:38, twenty-two
  minutes after we published it and left it alone. First time the hold rule produced a
  contribution.
- **`curiyu`** — closed `diaz_of_exp_eq_one` this morning, five minutes after we had already
  self-closed it. The reason the hold rule exists.

## Two claims carried forward unverified

Neither is depended on by anything formalised; both were written from memory with no
literature access. Do not quote either without checking.

1. "Six exponentials = the matrix rank statement for `dl > d + l`" (free-half run).
2. "There is no known deduction of the transcendence-degree-one four exponentials from six
   exponentials" (outsourced scoping pass).

## Process notes worth keeping

- When picking a mission to decompose, check its **node count and recent activity**, not just
  whether the root says Open. Collapsible Cubics had 13 nodes and an active author ninety
  minutes before our agent arrived; the brief called it unworked.
- Agents must write their account file **as they go**. Three were stopped mid-run today and
  two left nothing recoverable.
- Twice today an argument assumed independence the configuration itself denies — `π` as a
  transcendence generator inside an algebra not containing it, and `1, t², t/π, tπ, π²` on a
  class where the quartic relation is exactly a dependence among them. Both conclusions
  survived; both derivations did not. Expect a third.
