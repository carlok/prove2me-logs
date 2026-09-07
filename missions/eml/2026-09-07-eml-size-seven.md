# The size-seven band of `EmlComplexity` is complete

- **Mission** — eml, `EmlComplexity` lower-bound bands. The mission uuid
  is not recorded in the notes; the definition node is
  https://prove2.me/theorems/4356d2c2-a5af-4cb4-b610-0a2b890f11c8
  (`Definitions/Def_EmlComplexity.lean`)
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1)
- **Date** — 2026-09-07

The object is a binary expression tree, `Tree = one | node Tree Tree`,
with `size` counting nodes and
`eval (node a b) = Real.exp (eval a) − Real.log (eval b)`. A tree is
`valid` when both children are and `0 < eval b`, so that the logarithm
is taken of a positive number. The umbrella claim,
`EmlComplexity.not_attains_two_below_nine`, is that no valid tree of
size below nine evaluates to exactly `2`. It is proved band by band, a
band being all trees of one size, and this mission completed the
size-seven band: eleven `pair_i_j` theorems, all now Proved.

https://prove2.me/theorems/6a37cfc9-32de-4073-8ad3-766720b6194e

## What was proved

The band decomposition is
`not_attains_two_pair_i_j : ∀ a b, a.size = i → b.size = j →
valid (node a b) → eval (node a b) ≠ 2`. A tree of size `n` is
`node a b` with `a.size + b.size = n − 1`, so the size-`n` band is the
`n` splits with `i + j = n − 1`, and the split `(i, j)` contains
`C_i · C_j` shapes, `C` the Catalan numbers.

**The operator is not symmetric in its two children.** The left child
goes through `exp`, the right through `log`, and `valid` constrains only
the right child. `pair_i_j` is therefore never a relabelling of
`pair_j_i`: each split is its own finite check, and the band is not
halved by symmetry.

Sizes 0 to 6 are closed at band level, by `not_attains_two_upto_two`,
`not_attains_two_size_three`, `not_attains_two_four_five` and
`not_attains_two_size_six`. Within the size-six band (`i + j = 5`),
`pair_2_3` was the existing template and this mission added the other
five. In the size-seven band (`i + j = 6`), `pair_3_3` was proved by
someone else and this mission added the remaining six. The eleven
submissions were all `ACCEPTED`, so all eleven nodes are Proved. Each is
at `https://prove2.me/theorems/<uuid>`:

| theorem | node uuid |
|---|---|
| `pair_3_2` | d061055b-73e0-4ff2-b0e6-1dc699feb77a |
| `pair_1_4` | 257f55ac-7034-4547-87b3-2d8589c3c567 |
| `pair_4_1` | fa7a5c53-ab03-41ee-a372-233e5cd58ccb |
| `pair_0_5` | 267994e7-5876-423b-80d2-03a97d550f07 |
| `pair_5_0` | 7d9fe2d3-8af9-4faa-850d-88fa99412634 |
| `pair_2_4` | 0a490b56-a11d-4ae0-bc66-13f1eb76dc2d |
| `pair_4_2` | d7c94005-adc1-4775-a434-a3675e26ce90 |
| `pair_1_5` | 5ac0f32c-519a-43de-9d64-d61362748dce |
| `pair_5_1` | 1121d4d2-408b-4935-90e1-e5cfdd2bfe24 |
| `pair_6_0` | bcb0947b-52bd-4e93-8b36-ecfae1ba8301 |
| `pair_0_6` | 13fcaac3-efbc-4b79-b33f-5bb123baefe5 |

All eleven files build locally in 4 to 19 seconds, and
`#print axioms solution` returns `[propext, Classical.choice,
Quot.sound]` for each — no `sorryAx`, no extra axiom.

## How

None of this is written by hand. A generator, `EML_gen.py`, emits a
complete standalone Lean file per split from
`generate(i, j, expcap, order, grid, sig, abbrev, nsname)`. The recipe:

1. `scaled_interval` and `expc_k` certificates: `Real.exp_bound` at
   Taylor order `ORDER` with argument `r = X/n`, `n` the least power of
   two making `|r| ≤ 1/2`, then `l^n` and `u^n` rounded onto a grid.
2. `logc_k`: invert two exponential certificates (`e^L ≤ Y ≤ e^H`) and
   apply `Real.log_exp`.
3. One `blo_i`/`bhi_i` bound lemma per *distinct subtree*, shared across
   the whole forest. This is why the files came out about five times
   smaller than the `pair_2_3` template.
4. `enum0 … enumN`, shape enumeration (`size t = n → t = T1 ∨ …`),
   proved by `cases` and `omega`.
5. `tree_k` (the value is separated from `2`) or `inv_k` (the tree is
   not `valid`) per shape pair; `solution` is `rcases` on the
   enumeration and one `exact` per pair.

### Traps, all now fixed in the generator

- `_root_.Tree` already exists in Mathlib (the deprecated
  `BinaryTree`), so `open EmlComplexity` makes `Tree` ambiguous.
  Everything is emitted fully qualified and then post-processed into
  `.node`/`.one` dot notation.
- Towers overflow numerals: `exp⁴(1) ≈ 10^1656520` cannot be written as
  one. Lower bounds are weakened to `min (lo, 16)`, which is sound
  because `exp` is monotone; overflowing upper bounds use the structural
  estimate `eval (node c d) ≤ exp (hi_c)` when `eval d ≥ 1`, hence
  `log (eval (node c d)) ≤ hi_c`.
- Astronomically small but positive values, such as `e^(−3.8·10⁶)`, have
  rational lower bound `0`. The generator tracks strictness separately
  and emits `bps_i : 0 < eval t` from `Real.exp_pos`.
- Degenerate shapes: a value that is exactly `0` is invisible to
  interval arithmetic, since the interval straddles `0` however tight
  it is. A symbolic normaliser mirroring
  `simp only [eval_node, eval_one, log_one, log_zero, log_exp,
  exp_zero, sub_zero, sub_self]` detects them, and `inv_k` descends
  through `Tree.valid_node` to contradict `0 < eval b` with the exact
  value. `Real.log_zero` matters here: `log 0 = 0` in Mathlib, so
  `node (node 1 1) (node 1 (node (node 1 1) 1))` evaluates to
  `exp (exp 1)` and not to anything undefined.
- When several nodes of a shape are degenerate, the one to pick is the
  one refutable in closed form; `bad_path` searches all of them.
- Precision is a knob. `pair_0_6` needs `order=10, grid=1e-8`, because
  the shape `node (node 1 1) (node (node (node 1 1) 1) (node 1 1))` has
  value `2.6·10⁻⁷` and its *positivity* — the precondition for taking
  its log — is the tightest inequality anywhere in the family.

### The two platform limits, and what got under them

The submission lexer caps source at 1 048 576 bytes and verification
times out at 300 s. Both bite on the 132-pair splits.

Size: `abbrev q0 q1 …` for each distinct subtree, `.node`/`.one` dot
notation, a two-letter namespace and dropping unused imports took
`pair_0_6` from 1.86 MB to 941 KB. One merged `expc_pack` lemma carries
the order-`n` Taylor remainder, so the expensive
`norm_num [Finset.sum_range_succ, Nat.factorial]` runs once rather than
once per certificate, and each certificate becomes a single term
application with seven `by norm_num` side goals — which also means the
Taylor endpoints `l` and `u`, 200-digit rationals, appear once instead
of twice. Bound lemmas are emitted as explicit terms
(`le_trans … (sub_le_sub h1 h2)`) rather than calls to `linarith`.

Time: the culprit was not the arithmetic. `rcases` on a flat 132-fold
disjunction costs about 20 s by itself and scales worse than
quadratically — a 42-fold one costs about 1 s. The fix is to group
`enum6`'s conclusion by left-subtree size, `(t = T0 ∨ … ∨ T41) ∨ (…) ∨
…`, so `solution` does a 6-way `rcases` and then a `≤ 42`-way one inside
each group; and to split the *smaller* side first, so the inner `rcases`
is not re-run 132 times. Net effect: `pair_6_0` 48 s → 13 s, `pair_0_6`
52 s → 16 s.

## What is not proved

The umbrella is still Open. `not_attains_two_below_nine` does not follow
from what is here. Two things are missing: an aggregation lemma
`¬ Attains 2 7` from the seven size-seven splits, and the entire
size-eight band.

The aggregation lemma is not hard — a tree of size 7 is `node a b` with
`size a + size b = 6`, so it is `omega` plus the seven splits — but it
does not exist, and until it does the band being "complete" is a
statement about eleven separate nodes and not about size seven.

Nothing here is a proof a human can read. Each `pair_i_j` is a
machine-generated exhaustive check over `C_i · C_j` shapes, resting on
interval arithmetic with generator-chosen Taylor order and grid. The
axiom check is the evidence that they are sound; there is no structural
insight in them, and the method plainly does not scale past the size
limits described above.

`pair_2_3` and `pair_3_3` are not this mission's. They are recorded
above so the bands read correctly, not as work claimed here.

## What remains open

The size-eight band, `i + j = 7`: nine splits, 1430 shape pairs, and
**none of those nodes exist on the platform yet**. They have to be
published as nine separate `pair_i_j` theorems before any of them can be
submitted.

A single-file size-eight proof is out of reach and should not be
attempted. The `pair_0_6` split alone, at 132 pairs, already needs
941 KB after every compression trick above, against a 1 048 576-byte
lexer cap; size eight is an order of magnitude past that in shape count.

After the nine splits: the size-eight aggregation lemma, then
`not_attains_two_below_nine` closes.
