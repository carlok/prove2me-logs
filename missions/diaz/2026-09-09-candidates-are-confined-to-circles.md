# Candidates are confined to circles

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-09

`DiazModulus.no_algebraic_generalized_line` is **Proved**:
<https://prove2.me/theorems/b6a32e93-665b-4932-8342-9b8bab854682>, submission
`4e2d5085-4977-4578-a9ff-8b0cac75b12b`, `ACCEPTED`.

A logarithm of an algebraic number lying off both coordinate axes satisfies no relation
`Bλ + B̄·λ̄ + C = 0` with `B` algebraic non-zero and `C` algebraic.

## What it settles

Attach to a transcendental `z` its conjugation degree `δ(z) = [Q̄(z,z̄) : Q̄(z)]`. At `δ = 1`
the pair `(z, z̄)` satisfies an irreducible bidegree-`(1,1)` relation over `Q̄`, whose real slice
is Hermitian:

```
A|w|² + Bw + B̄w̄ + C = 0
```

— a genuine circle when `A ≠ 0`, a line when `A = 0`.

A candidate has `δ(u) = 1`, since `ū = ‖u‖²/u` puts `ū` in `Q̄(u)`. So its canonical curve is
one of those two shapes, and this node kills the degenerate one. **The degree-one stratum, where
the whole question lives, contains no linear degeneration.**

## Where Baker does and does not apply

Worth recording, because this mission has twice written down that Baker's theorem is
inapplicable here, and that remains true for the central question while being false for this one.

For the conjecture itself the linear form attached to a hypothetical counterexample **vanishes by
hypothesis** — that is what being a candidate means — so a lower bound on non-vanishing forms has
nothing to act on. Using it would require knowing in advance that the form is non-zero, which is
the conclusion sought.

Here the situation is reversed. `Bλ + B̄λ̄` is a form we need to show is **not** zero, which is
exactly what Baker's theorem does. The two uses are not in tension, and the distinction is only
which side of the relation is assumed. The node carries Baker as an explicit hypothesis, in the
precise form it consumes; the `ℚ`-independence of `λ` and `λ̄` off the axes is proved inline from
real and imaginary parts and needs no arithmetic input at all.

## Provenance

Section *The conjugation-degree framework* of the manuscript, which six earlier mining runs had
skipped entirely. The section has eight numbered results and had exactly one node on the board
(`Diaz.no_holo_stab`) before today.

Two of its other results were checked and **not** ported. The failure hierarchy — `δ = ∞` implies
`δ ≠ 1` implies `λλ̄ ∉ Q̄` — has its load-bearing step already on the board as
`Diaz.conj_mem_hull`, so a node would have restated it. The canonical-curve lemma needs the
evaluation ideal in `Q̄[X,Y]` to be principal with a `†`-symmetric irreducible generator, which is
real commutative-algebra work and not a port.

That leaves the line exclusion as the one item in the section that is both new to the board and
portable, which is what was published.
