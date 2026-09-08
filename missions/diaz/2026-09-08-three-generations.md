# Three generations, and π had to be proved along the way

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## The tree

**17 nodes, 26 edges**, up from 2 yesterday.

```
diaz_modulus_conjecture                        Open
├── diaz_of_exp_not_real                       Open    ← entry point
└── diaz_of_exp_real                           Open
    ├── diaz_of_exp_real_self_real             Proved
    └── diaz_of_exp_real_self_not_real         Open
        ├── diaz_of_exp_eq_one                 Proved
        └── diaz_of_exp_ne_one                 Open    ← entry point
```

Plus `pi_transcendental`, `hermite_lindemann_holds` and
`diaz_on_axes_of_hermite_lindemann`, pulled in as proof dependencies rather than placed
deliberately.

| node | uuid |
|---|---|
| `pi_transcendental` | <https://prove2.me/theorems/e1503dd8-3f58-4316-9f6b-def1dd438436> |
| `diaz_of_exp_eq_one` | <https://prove2.me/theorems/2d041e86-17d2-42c5-884b-7a697d9800ba> |
| `diaz_of_exp_ne_one` | <https://prove2.me/theorems/9182eef2-1c37-4982-859b-566c87120292> |

## What was proved this round

**`pi_transcendental`.** Mathlib at this revision does not have transcendence of π —
the Lindemann–Weierstrass development present here stops short, because the usual
derivation wants `i` integral over `ℚ` in a form not available. It follows from the
mission's own `hermite_lindemann_holds` in three lines: `i` is algebraic as a root of
`X² + 1`; if π were algebraic then `iπ` would be a non-zero algebraic number; Hermite–
Lindemann would make `exp(iπ) = −1` transcendental, and it is not.

Lindemann, 1882. Nothing new; what is new is that the environment now has it.

**`diaz_of_exp_eq_one`.** The case `exp u = 1`, which closes *because its hypotheses are
contradictory*. There `u = 2πin` with `n ≠ 0`, so `‖u‖ = 2π|n|` and
`π = ‖u‖ / (2|n|)`; `|u|` algebraic would put π in `Qbar`. No `u` satisfies the
hypotheses.

Worth stating plainly: the conclusion is *false* at such `u` read naively — `exp u = 1`
is algebraic. The case is closed because nothing lives in it, not because something
interesting holds there. That is on the node.

## The pattern that made it work

Each generation looked for a split with one half already reachable. Generation two split
on whether `u` is real, because the real half follows in one line from `diaz_on_axes`.
Generation three split on whether `exp u = 1`, because that half reduces to π — and when
π turned out to be missing from the environment, deriving it was three lines from a node
the mission already owned.

That last step is the one worth naming: **a split blocked only by missing infrastructure
is not blocked.** Publish the infrastructure as its own node first. It is legitimately
useful on its own, and it makes the split possible.

## What is not proved

Neither open leaf. Neither is claimed *easier* than its parent — only strictly weaker.

`diaz_of_exp_eq_one` carries two of its parent's hypotheses without using them; the Lean
discards both. `Im u ≠ 0` is in fact automatic there, since `u = 2πin` with `n ≠ 0` is
never real.

Nothing this round is new mathematics. π is Lindemann's, the splits are obvious
dichotomies, and the contribution is structural: three levels of tree where there was
one isolated conjecture.

## What remains open

`diaz_of_exp_not_real` — `exp u` ranges over a two-real-dimensional set, no reduction to
a one-variable question.

`diaz_of_exp_ne_one` — `exp u = β` real algebraic, `β ≠ 1`, `u` non-real. So
`u = log β + 2πin` with `n ≠ 0`, or `u = log|β| + iπ(2n+1)`, and the question is whether
`(log β)² + 4π²n²` or `(log|β|)² + π²(2n+1)²` can be an algebraic square. Smallest
instance: is `√((log 2)² + π²)` algebraic?

## Side product

The procedure is written up as a reusable skill, `skills/prove2me-decompose.md` in this
repo — the three steps, what splits cannot work and why, and what to write on a node.
