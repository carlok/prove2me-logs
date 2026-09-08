# Four generations, and the last split leaves the difficulty with nowhere to hide

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## The tree

**22 nodes, 37 edges**, 6 Proved, 6 Open, two of them leaves.

```
diaz_modulus_conjecture                            Open
├── diaz_of_exp_not_real                           Open   ← leaf
└── diaz_of_exp_real                               Open
    ├── diaz_of_exp_real_self_real                 Proved
    └── diaz_of_exp_real_self_not_real             Open
        ├── diaz_of_exp_eq_one                     Proved
        └── diaz_of_exp_ne_one                     Open
            ├── diaz_of_exp_real_pure_imaginary    Proved
            └── diaz_of_exp_real_generic           Open   ← leaf
```

| node | uuid |
|---|---|
| `diaz_of_exp_real_pure_imaginary` | <https://prove2.me/theorems/732c1e52-07af-4da5-b6a4-c49dcaf5d57b> |
| `diaz_of_exp_real_generic` | <https://prove2.me/theorems/813352be-5c64-4e5a-b973-825a07d50640> |

## What was proved

`diaz_of_exp_real_pure_imaginary`. With `exp u` real, `|exp u| = exp (Re u)`, so
`Re u = 0` means `|β| = 1` and hence `β = ±1`; excluding `1` leaves `exp u = −1` and
`u = iπ(2n+1)`. A purely imaginary `u` lies on an axis, so
`diaz_on_axes_of_hermite_lindemann` closes it in one line.

Four of its six hypotheses are unused — only `u ≠ 0`, `|u|` algebraic and `Re u = 0` do
any work. Stated on the node, since a reader would otherwise take the real-exponential
condition to matter.

## Why this split, and what it exposes

The three cases closed above this point all died the same way: **one term of `|u|²`
vanished**, and the survivor was either algebraic outright or a rational multiple of `π`.

- `u` real: `|u|` algebraic makes `u` algebraic. Hermite–Lindemann.
- `exp u = 1`: `u = 2πin`, so `|u| = 2π|n|`. Transcendence of `π`.
- `Re u = 0`: `u = iπ(2n+1)`, so `|u| = π|2n+1|`. The axis node.

Splitting on `Re u = 0` was chosen precisely because it is the last such corner. What
remains has **both parts of `u` non-zero**, so

```
|u|² = (log β)² + 4π²n²     (β > 0, β ≠ 1, n ≠ 0)
|u|² = (log|β|)² + π²(2n+1)²  (β < 0, β ≠ −1)
```

is a genuine sum of two independent transcendental contributions, and the escape that
closed every sibling is unavailable.

## What is not proved

`diaz_of_exp_real_generic`, and nothing here suggests it is close. A sum of two
independent transcendental terms is exactly what Diaz's own partial results do not
reach, and none of the mission's proved tools — Hermite–Lindemann, transcendence of `π`,
the six exponentials theorem — touch it. The node says so.

The smallest instance is `β = −2`, `n = 0`: is `√((log 2)² + π²)` — the modulus of the
principal logarithm of `−2` — algebraic? Settling that would close one point of the
node, not the node.

Nothing in this generation is new mathematics. The split is the obvious dichotomy and
the proved half is a one-line application of an existing node. The contribution is that
the difficulty is now isolated in a single named leaf instead of spread across a
conjecture.

## What remains open

Two leaves. `diaz_of_exp_not_real`, where `exp u` ranges over a two-real-dimensional set
and no reduction to a one-variable question exists; and `diaz_of_exp_real_generic`
above.

Four generations in, every closed node came from stripping away a degenerate corner. The
method has now run out of corners on this branch, which is itself worth knowing: further
progress here needs mathematics, not bookkeeping.
