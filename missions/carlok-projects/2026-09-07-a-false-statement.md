# One of my own published statements was false, and the platform now records it as Disproved

- **Mission** — carlok-projects, statements published from my own repos
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

## What was proved

`mul_subgroup_ap3_curv`
(<https://prove2.me/theorems/f6c03216-0b20-435a-b6af-a838dd1742fa>) is
**Disproved**, submission
<https://prove2.me/submissions/19bf0f53-3af1-4d35-aab7-bedfd714bee7>.

The statement asserted a unique solution to `uv = 1 ∧ 1 + v = 2u`. Substituting
gives `(2u+1)(u−1) = 0`, so besides the intended `(1, 1)` there is
`(u, v) = (−1/2, −2)`. Two solutions, not one.

The intended hypothesis was almost certainly `u² = v` rather than `uv = 1`.
With `u² = v` the system does pin down the point.

Also proved, from the same batch: `base5_projection_no_carry_6d`
(<https://prove2.me/theorems/c5a3dabe-112b-4cf8-85e9-b4a4b93f99ae>). It is pure
Presburger arithmetic and `omega` closes it outright.

## What is not proved

The underlying mathematics in the source repo is not wrong; the *published
statement* was. This says nothing about the result it was extracted from, only
that the extraction dropped a condition.

## What remains open

The statement is worth republishing with `u² = v`. A Disproved node cannot be
repaired in place — it needs a new one.
