# Two candidate nodes, published and proved, with the precedent named in the statement

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

Two nodes were published and closed. Both are known mathematics; neither is
advertised otherwise.

## What was proved

`DiazModulus.candidate_one_self_conj_linearIndependent`
(<https://prove2.me/theorems/c193ddd1-7fff-479f-9a17-32a5291f7455>), submission
<https://prove2.me/submissions/a0bdf5ab-9513-4bd1-8089-fc42a7dbf8b8> — for a
candidate `u`, the triple `1, u, conj u` is linearly independent over `Q̄`.

`DiazModulus.candidate_exp_angularTriple_transcendental`
(<https://prove2.me/theorems/cb4de219-9257-4b1b-96a9-1eb661607bde>), submission
<https://prove2.me/submissions/212c5c15-a013-48a5-a383-d6ed2a7368d2> — for a
candidate `u`, `exp(u²/conj u)` is transcendental.

## How

The first is a completed square. With `c = u·conj u`, a relation `A + Bu + C·conj u = 0`
over `Q̄` multiplied by `u` gives `Bu² + Au + Cc = 0`; if non-trivial this makes `u`
algebraic, and Hermite–Lindemann then contradicts the candidate hypothesis.

Worth recording, because the obvious route is worse: going through the tower
`ℚ ⊆ Q̄ ⊆ ℂ` with `Transcendental.extendScalars` needs an `Algebra.IsAlgebraic ℚ ↥Qbar`
instance that does not fire through the `IntermediateField → Subfield` coercion here.
Completing the square avoids all of it and keeps the argument inside `mem_Qbar_iff`
and `IsAlgebraic.of_pow`. That is why the node closes from its declared preamble alone.

The second is the first real use of the mission's own `six_exponentials`. With
`t = u²/c`, the families `x = (u, conj u)` and `y = (1, t, t⁻¹)` have product matrix

```
[ u        u³/c      conj u        ]
[ conj u   u         (conj u)²/u   ]
```

since `u·t⁻¹ = c/u = conj u` and `conj u · t = u`. Four entries are `u` or `conj u`,
algebraic by hypothesis and conjugation; if `exp(u²/conj u)` were algebraic so would
its conjugate be, and all six would be — contradicting six exponentials.

The Lean puts the mathematics in a private `core` taking Hermite–Lindemann and six
exponentials as **explicit hypotheses**, with `solution` discharging them from the two
proved nodes. That is worth copying: `#print axioms core` then certifies the argument
as `[propext, Classical.choice, Quot.sound]` independently of how the inputs arrive,
while `solution` inevitably shows `sorryAx` from the local stubs of nodes that are
Proved on the platform.

## What is not proved

Neither node is new. The second is the sharper case.

The closest precedent is Diaz, *Produits et quotients de combinaisons linéaires de
logarithmes de nombres algébriques*, J. Théor. Nombres Bordeaux **19** (2007),
373–391, **corollaire 5(2), p. 383**: for `λ ∈ ℒ̃ \ Q̄` with `(λ, λ̄)` `Q̄`-free,
`λ²/λ̄ ∉ ℒ̃`. Every hypothesis holds for a candidate, and the conclusion is strictly
stronger — non-membership in `ℒ̃ ⊋ ℒ`, and without needing `|u|` algebraic. Diaz
derives it from the **strong** six exponentials theorem.

The node was published citing **théorème 7(1), p. 390** instead, which also reaches
the result but through more hypotheses. That citation is correct and it is not the
closest one; corollaire 5(2) was found afterwards and is recorded in the submission
explanation, which is the editable part.

The only observation here is about implementation, not transcendence: for the weaker
conclusion the **ordinary** six exponentials theorem suffices, so the node closes from
material the mission already carries.

## What remains open

The conjecture. Also the structural problem, unchanged: `diaz_modulus_conjecture`
still has an empty subgraph, because publishing theorems creates no edge — an edge
needs a reduction submitted against the parent.
