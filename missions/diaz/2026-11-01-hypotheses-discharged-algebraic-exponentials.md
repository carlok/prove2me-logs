# Two carried hypotheses discharged for algebraic exponentials
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-01

Three legacy nodes of the mission carry a transcendence statement as an
explicit hypothesis: `Diaz.quadric_trdeg_two` carries `hIU`, a form of
Roy and Waldschmidt's Théorème 0.2 (1997), and `four_exp_trdeg_one` and
`log_modulus_forces_independence` carry a dichotomy `hMaster` derived
from it. A feasibility study for proving Théorème 0.2 in general found
that each node uses its hypothesis only once, on a 2×2 determinant.
For logarithms of algebraic numbers that case is the four exponentials
theorem in transcendence degree one, which the mission already proves.

## What was proved

- **`quadric_trdeg_two_alg`.** If e^u and e^v are algebraic,
  |v|² = m|u|² for a rational m ≠ 0, and u, ū, v, v̄ are linearly
  independent over ℚ, then u, ū, v, v̄ have transcendence degree at
  least 2. This is the conclusion of `quadric_trdeg_two` without `hIU`.
- **`log_modulus_forces_independence_alg`.** If λ is not real and e^λ
  and e^{|λ|} are algebraic, then λ, λ̄, |λ| have transcendence degree
  at least 2 (Waldschmidt's book, Exercise 15.16(c), after Diaz 1997,
  Proposition 2). This is the conclusion of
  `log_modulus_forces_independence` without `hMaster`.
- `four_exp_trdeg_one` needed no new node: without `hMaster` its
  conclusion is `four_exponentials_trdeg_one`, already Proved.

| theorem | uuid | milestone | status |
|---|---|---|---|
| `DiazModulus.quadric_trdeg_two_alg` | `a68b73cd-4b25-421f-98fe-0973b0a91588` | 183 | Proved |
| `DiazModulus.log_modulus_forces_independence_alg` | `e0acdbfe-3627-4cbe-ba9a-63c8b63f2636` | 184 | Proved |

The pages of the three legacy nodes now point to the unconditional
forms. The page of `quadric_trdeg_two` also states the scope of `hIU`
precisely: it is stated for any subfield K, it is Théorème 0.2 when K
consists of algebraic numbers, and it fails for K = ℂ (take the point
(1, √2) and the quadric 2X₁² − X₂²).

## How

- Both proofs apply `log_pair_rigid_of_trdeg_one`, the four
  exponentials theorem in transcendence degree one on the matrix of
  the quadric. If the transcendence degree were at most one, it would
  put v in ℚu ∪ ℚū, or |λ| in ℚλ ∪ ℚλ̄; the first contradicts the
  linear independence, the second makes λ real.
- Each proof has 37 lines. Both were accepted outright, and in the
  mirror they depend only on Lean's three standard axioms. The library
  goes from 616 to 618 results.

## What is not proved

- **Théorème 0.2 in general.** The feasibility study estimates a full
  proof, along Waldschmidt's book (Th. 15.30 with Prop. 12.25), at
  roughly 9,000–17,000 lines, the size of the round that proved Roy's
  strong six exponentials theorem. It is deferred, and so is the
  classical 2×2-determinant case as a theorem of its own.
- **Théorème 0.1** is dropped from the plan: its proof rests on a
  paper of Waldschmidt (Crelle 493, 1997) that was not read.
- **No novelty is claimed.** Both results are classical consequences
  of the four exponentials theorem in transcendence degree one.

## What remains open

Diaz's conjecture itself, which the companion note reduces to two
open statements. The legacy nodes keep their hypotheses as stated;
the unconditional forms sit beside them.
