# Open threads at 2026-09-19

Rewritten after the four exponentials subtree closed. The sections below the frontier are older
and are kept because they are still true; the dated ones say so.

## The frontier — three leaves, all open mathematics

`GET /theorems/<root>/open-leaves` on `DiazModulus.diaz_modulus_conjecture` returns three, and
nothing else in the tree is Open:

| leaf | uuid | what it is |
|---|---|---|
| `DiazModulus.recip_pi_not_log_real_gamma` | `29c99457` | half of (S): `1/π` is not an algebraic multiple of a purely imaginary logarithm |
| `DiazModulus.recip_pi_not_log_imag_gamma` | `dea45a44` | the other half: `π ≠ β/log α` |
| `DiazModulus.norm_transcendental_of_generic_conj_pair` | `ed970912` | another contributor's; equivalent to the whole root |

Each node's own description records that it is implied by the strong four exponentials
conjecture. None of them is a formalisation task.

**(S) is split and the split is linked.** `DiazModulus.recip_pi_not_log` (`b5a16bec`) has two
children, reduction `SKETCH_ACCEPTED`. It is not a case distinction:
`S₀ = {γ ∈ Q̄ : γ/(iπ) ∈ ℒ}` is a ℚ-subspace closed under conjugation, so `γ ∈ S₀` forces
`Re γ ∈ S₀` and `i·Im γ ∈ S₀`. `real_gamma` is the easier-looking half — γ real makes `γ/(iπ)`
purely imaginary, so the target is a modulus-one algebraic point that is provably not a root of
unity. Account in `missions/diaz/SPLIT_S.md`.

**`four_exponentials_trdeg_one` is Proved** (2026-09-18, node `2c0f35ea`), together with
everything under it, and by cascade with the branch node
`..._period_aligned_norm_rat_mult`. The earlier instruction here — do not attempt it, the
blocker is Philippon's zero estimate — was wrong about the route, not merely pessimistic.
Waldschmidt's own 1973 proof with the 1971 toolbox needs no zero estimate and no Baker; the
scoping pass that said otherwise had read the 1995 sketch and not the 1973 paper. The
development is 26 nodes in the `FourExp` namespace and about 8,800 lines of Lean; see
`missions/diaz/2026-09-18-four-exponentials-trdeg-one.md`.

Its sibling `..._period_aligned_norm_free` (`1b43101e`) is what still blocks that branch, and it
reduces to the two (S) halves above.

## Held open overnight (2026-09-08; all long since resolved)

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
- **`amorphic`** (uuid `06020dba…`, renamed from `cm` on 2026-09-09) — took **three** held
  nodes, all within about half an hour of publication: the CollapsibleCubics child at 12:38,
  and both `Diaz.pair_dichotomy_exclusive` and `Diaz.conj_combination_off_rays` at 12:43.
  Trust 23 → 50 overnight. **Track contributors by uuid, not username**, and sweep submissions
  on our open nodes rather than theorem authorship — two of these three were invisible for a
  day to a `created_by` check.
- **`curiyu`** — closed `diaz_of_exp_eq_one` this morning, five minutes after we had already
  self-closed it. The reason the hold rule exists.

## Two claims carried forward unverified

Neither is depended on by anything formalised; both were written from memory with no
literature access. Do not quote either without checking.

1. "Six exponentials = the matrix rank statement for `dl > d + l`" (free-half run).
2. "There is no known deduction of the transcendence-degree-one four exponentials from six
   exponentials" (outsourced scoping pass). Still unverified, and now of less consequence: the
   theorem has a machine-checked proof of its own.

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
