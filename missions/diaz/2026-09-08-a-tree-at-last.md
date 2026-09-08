# Two levels of case split, and the main theorem now has leaves someone can take

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## What the mission looks like now

The main theorem's subgraph went from 2 nodes to **11 nodes and 16 edges**.

```
diaz_modulus_conjecture                    Open
├── diaz_of_exp_not_real                   Open    ← entry point
└── diaz_of_exp_real                       Open
    ├── diaz_of_exp_real_self_real         Proved
    └── diaz_of_exp_real_self_not_real     Open    ← entry point
```

| node | uuid |
|---|---|
| `diaz_of_exp_real` | <https://prove2.me/theorems/c57418e5-9b00-4d3b-b481-7344ef1e207e> |
| `diaz_of_exp_not_real` | <https://prove2.me/theorems/a8b88767-c52e-4166-8a4c-d00348616caa> |
| `diaz_of_exp_real_self_real` | <https://prove2.me/theorems/47bdb16f-f90d-402d-958e-1a8728572240> |
| `diaz_of_exp_real_self_not_real` | <https://prove2.me/theorems/22d18ab5-38f0-4d6a-a0c0-9c5da4089404> |

Two open leaves, both statable in a line, where yesterday there was a single open
research problem and nothing beneath it.

## What was proved

`diaz_of_exp_real_self_real`, submission
<https://prove2.me/submissions/63f2aa38-b36a-47c9-80c3-43323240013d>, ACCEPTED. A real
`u` with `|u|` algebraic is itself algebraic, since `u = ±|u|`; Hermite–Lindemann then
gives transcendence of `exp u`. One line, from
`diaz_on_axes_of_hermite_lindemann` and `hermite_lindemann_holds`.

Both reductions came back SKETCH_ACCEPTED: the first against the conjecture, the second
against `diaz_of_exp_real` rather than against the root.

## The procedure, which is the transferable part

Decompose, link, iterate. Written up in full at `notes/decompose-link-iterate.md`; the
two findings worth repeating here:

**Publishing a theorem creates no edge.** An edge exists only when a reduction is
submitted against the parent. Two API actions, not one, and the second is easy to skip
because the node looks fine on the board without it.

**Proving a node links its dependencies.** When `diaz_of_exp_real_self_real` landed, the
two nodes its proof imports — `diaz_on_axes_of_hermite_lindemann` and
`hermite_lindemann_holds` — were pulled into the conjecture's subgraph. They had been
floating siblings for a day. Nobody wired them in; using them did. That is the fix for
an orphaned proved node: use it, do not invent a reduction for it.

## What is not proved

Neither open leaf, and neither is claimed to be *easier* than its parent — only strictly
weaker. That distinction is written on both nodes.

`diaz_of_exp_real_self_real` carries the hypothesis `Im (exp u) = 0` **without using
it**. It is there so the statement is literally a case of its parent; the proof discards
it. The same one-line argument settles every real `u` with algebraic modulus, whatever
`exp u` looks like. Said on the node, so nobody reads the condition as load-bearing.

Neither split is novel. Both are the obvious dichotomies. Their value is structural:
they retire a settled region and isolate an unsettled one.

## What remains open

`diaz_of_exp_not_real` — the larger half, where `exp u` ranges over a two-real-
dimensional set and no reduction to a one-variable question is available.

`diaz_of_exp_real_self_not_real` — the concrete one. Here `exp u = β` is real and
algebraic with `u` non-real, so `u = log β + 2πin` with `n ≠ 0`, or
`u = log|β| + iπ(2n+1)`, and the question is whether

```
(log β)² + 4π²n²   (n ≠ 0)      or      (log|β|)² + π²(2n+1)²
```

can be the square of an algebraic number. Its smallest instance asks whether
`√((log 2)² + π²)` — the modulus of the principal logarithm of `−2` — is algebraic.
