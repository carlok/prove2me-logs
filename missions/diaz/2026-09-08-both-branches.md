# Both branches decomposed, and what is left is exactly the conjecture minus its corners

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## The tree

**26 nodes, 45 edges. 7 Proved, 7 Open, of which 2 are leaves.**

```
diaz_modulus_conjecture                            Open
├── diaz_of_exp_not_real                           Open
│   ├── diaz_of_exp_not_real_on_axes               Proved
│   └── diaz_of_exp_not_real_off_axes              Open   ← leaf
└── diaz_of_exp_real                               Open
    ├── diaz_of_exp_real_self_real                 Proved
    └── diaz_of_exp_real_self_not_real             Open
        ├── diaz_of_exp_eq_one                     Proved
        └── diaz_of_exp_ne_one                     Open
            ├── diaz_of_exp_real_pure_imaginary    Proved
            └── diaz_of_exp_real_generic           Open   ← leaf
```

Plus `hermite_lindemann_holds`, `diaz_on_axes_of_hermite_lindemann` and
`pi_transcendental`, in the graph as proof dependencies.

| node | uuid |
|---|---|
| `diaz_of_exp_not_real_on_axes` | <https://prove2.me/theorems/9cea9bb5-bf23-428b-8393-c708a9d0b9df> |
| `diaz_of_exp_not_real_off_axes` | <https://prove2.me/theorems/63575de5-e604-4fd4-a00e-2e0f41b86d1f> |

## What was proved

`diaz_of_exp_not_real_on_axes`. One line from
`diaz_on_axes_of_hermite_lindemann`, with Hermite–Lindemann discharged from the
mission's own node.

**This corner is not vacuous, and that distinguishes it from its counterpart on the real
branch.** The disjunct `Im u = 0` is empty here — a real `u` gives a real `exp u`. But
`Re u = 0` is not: `u = i` gives `exp u = cos 1 + i sin 1`, and every `u = it` with `t`
not an integer multiple of `π` qualifies. So the node settles a genuine region rather
than reporting an impossibility. Worth checking each time, because the corresponding
node on the real side closed precisely *because* nothing lived in it.

## The shape of the whole decomposition

Every one of the four proved case-nodes was closed by the same move: **strip a
degenerate corner where `|u|` loses a term.**

| case | why it closed |
|---|---|
| `u` real | `u = ±\|u\|` is algebraic; Hermite–Lindemann |
| `exp u = 1` | `u = 2πin`, so `\|u\| = 2π\|n\|`; transcendence of `π` |
| `Re u = 0`, `exp u` real | `u = iπ(2n+1)`, so `\|u\| = π\|2n+1\|`; the axis node |
| `u` on an axis, `exp u` non-real | the axis node directly |

That is the entire method, applied five times. It has now run out of corners on both
branches.

## What is not proved

Two leaves, and neither is close.

**`diaz_of_exp_real_generic`** — `exp u = β` real algebraic with both parts of `u`
non-zero, so `|u|² = (log β)² + 4π²n²` or `(log|β|)² + π²(2n+1)²` with both terms
genuinely non-zero. A sum of two independent transcendental contributions, which is
exactly what none of the mission's tools reach. Its smallest instance asks whether
`√((log 2)² + π²)` is algebraic; that single question is open.

**`diaz_of_exp_not_real_off_axes`** — `u = x + iy` with `x, y ≠ 0`, `x² + y²` an
algebraic square, `eˣ(cos y + i sin y)` algebraic and non-real. Unlike the real branch
there is no parametrisation by one integer and one algebraic number, so there is no
smallest instance to point at. The larger and less structured of the two.

Nothing in this decomposition is new mathematics. Five splits, all obvious dichotomies;
four one-line proofs, all applications of nodes the mission already had; one classical
theorem (transcendence of `π`) derived in three lines because the environment lacked it.

What the work produced is a mission where the difficulty is confined to two named leaves
instead of spread over a conjecture, and where a contributor can see at a glance which
regions are settled and why.

## What remains open

The two leaves, and the honest assessment that further progress on either needs
mathematics rather than bookkeeping. The corner-stripping method is finished here.
