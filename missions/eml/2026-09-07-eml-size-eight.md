# Every expression of size at most eight fails to hit 2, and `EmlComplexity.complexity_two` closed by itself when the last split landed

- **Mission** — eml, the elementary-expression complexity ladder
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

The mission asks how large an expression built from `e`, `+`, `−`, `×`, `÷`,
`exp` and `ln` has to be before it can equal a given constant. For the
constant 2 the ladder proceeds size by size, each size split by how the tree
divides at the root. Size 8 is the band `i + j = 7`, eight splits wide, and
the two extremes `(0,7)` and `(7,0)` had never been published — the band was
recorded as closed when it was not.

## What was proved

Twelve nodes, all verdict Proved. Six blocks, two pair assemblies, the size
statement, and the ladder step:

| theorem | node | note |
|---|---|---|
| `not_attains_two_bundle_0_7_A` | <https://prove2.me/theorems/9473ee64-0e14-4b69-b274-3ba2f47e41a9> | 132 shapes, `\|c\|=0` |
| `not_attains_two_bundle_0_7_B` | <https://prove2.me/theorems/70dfbbe2-4e0a-4bc9-9cdb-48489d7e1e43> | 165 shapes, `1≤\|c\|≤5` |
| `not_attains_two_bundle_0_7_C` | <https://prove2.me/theorems/4ecedc7a-8bbd-4cb9-90ec-d957d1181944> | 132 shapes, `\|c\|=6` |
| `not_attains_two_bundle_7_0_A` | <https://prove2.me/theorems/a958091d-a162-447f-a6a3-f77f4b93fcff> | 132 shapes, `\|c\|=0` |
| `not_attains_two_bundle_7_0_B` | <https://prove2.me/theorems/b29929a1-0f5f-45f0-b94d-deb6f6fb84a1> | 165 shapes, `1≤\|c\|≤5` |
| `not_attains_two_bundle_7_0_C` | <https://prove2.me/theorems/8fbc90c1-9090-4c13-86f4-13395d4462e7> | 132 shapes, `\|c\|=6` |
| `not_attains_two_pair_0_7` | <https://prove2.me/theorems/78680415-8e19-4c20-9344-94a6615b926d> | reduction to the three blocks |
| `not_attains_two_pair_7_0` | <https://prove2.me/theorems/b053f834-a791-4fe8-9733-fa69f389af26> | reduction to the three blocks |
| `not_attains_two_size_eight` | <https://prove2.me/theorems/20e738f1-1c05-4eb4-b0e0-847169a9a428> | `omega` over all eight splits |
| `not_attains_two_below_nine` | <https://prove2.me/theorems/6a37cfc9-32de-4073-8ad3-766720b6194e> | six-layer `omega` case split |
| `EmlComplexity.complexity_two` | <https://prove2.me/theorems/4aef18dd-2336-49b8-810b-f0a58e507c1c> | resolved with no submission |

The last row is the interesting one: `complexity_two` carried a pre-existing
sketch reducing it to `attains_two` and `below_nine`, so it flipped to Proved
the moment `below_nine` landed. Nobody proved it.

Sizes 0 through 8 of the ladder for the constant 2 are now closed, and the
`i+j=7` band has all eight splits — `0_7, 1_6, 2_5, 3_4, 4_3, 5_2, 6_1, 7_0` —
counted rather than assumed.

## How

The published statements are not the 429-shape flat conjunctions used at size
7. Each extreme was cut into three `∀`-form blocks indexed by the size of the
left child of the size-7 side (`node c d` with `|c|+|d|=6`): `|c|=0`,
`1≤|c|≤5`, `|c|=6`. That makes each published statement about 250 bytes
instead of about 55 KB, and each pair assembly 20 lines instead of a 429-way
enumeration.

Two of the six generated blocks came in over the platform's 1 MB submission
cap (1.41 MB). Two cuts brought them to 1.02 MB: rounding each `expcert`'s
Taylor endpoints onto a grid a thousand times finer than the remainder — they
were exact 220-digit rationals, and rounding down/up stays sound — and pruning
the throwaway `expcert`s that the `logcert` search loop mints but nothing
references.

No new structural rule was needed. The existing rules with `order=10`,
`sig=16` and a 10⁻⁸ log grid cover all 858 shape pairs. Block `0_7_B` alone
needs 10⁻⁹, because of a subtree of value about 1.4·10⁻⁷ of the form
`X − ln(e^X − c)` with `X = e^e`.

## What is not proved

Two bugs in the generator, not precision limits, had been masking shapes.

Six `(0,7)` shapes evaluate to *exactly* zero through `a − (a − b) = b`, for
instance `e − ln(e − (e − e^e)) = 0`. The normaliser had no such rule, so
those shapes were neither symbolically zero nor numerically refutable and
simply sat there. Separately, `valid()` consulted only the mpmath tower model,
which collapses `exp(−tower)` to 0 and therefore declared genuinely valid
trees invalid; it now consults the propagated bounds, where strict positivity
is already on record from `Real.exp_pos`.

The `ERROR` verdicts seen here were contention, not determinism. All six
blocks build locally in 18–23 s. Submitting all six at once made the three
largest (932–950 KB) return `Verification timed out after 300s`; resubmitted
one at a time, all three were ACCEPTED in under a minute each. A timeout on a
large file is worth one lone retry; a `Failed to compile theorem module` never
is.

One Lean gotcha that will recur: `open EmlComplexity in theorem solution :
∀ a b : Tree, … Tree.node a b …` does not compile. Mathlib's deprecated
`_root_.Tree` makes `Tree.node` ambiguous once the namespace is opened — the
binder type resolves, the projection does not. Assembly statements have to be
written fully qualified.

## What remains open

`not_attains_four_below_twenty_one` and `complexity_four`. Both are out of
reach by this method: they need every shape of size at most 20, which is more
than 10¹⁰ trees. Closing the constant 4 will take an argument, not an
enumeration.
