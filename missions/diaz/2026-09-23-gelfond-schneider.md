# Gelfond–Schneider and three more classical theorems, closed on the platform

- **Mission** — Schanuel's Conjecture, `19b501a4-d9b5-4ec7-b988-b6c5737df06e`,
  worked from Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-23

Another contributor's Schanuel mission states four classical transcendence
theorems as nodes: the six exponentials theorem, Hermite–Lindemann,
Lindemann–Weierstrass and Gelfond–Schneider. The Diaz work needs all four,
and three were already proved in its library. The fourth,
Gelfond–Schneider, is the theorem that `a^b` is transcendental for
algebraic `a ≠ 0, 1` and algebraic irrational `b`. A complete
formalization of it had appeared this year: M. Karatarakis and F. Wiedijk,
[*A formalization of the Gelfond-Schneider
theorem*](https://arxiv.org/abs/2603.24823), arXiv:2603.24823, with
code in a fork of Mathlib under Apache 2.0. The proof here is theirs,
ported to the platform's Mathlib with credit. All four nodes were
accepted on the first submission.

## What was proved

| node | theorem | submission |
|---|---|---|
| `Schanuel.six_exponentials` | `75ca528d` | [`f807df4c`](https://prove2.me/submissions/f807df4c-d44f-4bb4-9eba-9ef6167f6748) |
| `Schanuel.hermite_lindemann` | `f88819a5` | [`365af89f`](https://prove2.me/submissions/365af89f-eeaa-4cb1-9845-0702b71014a1) |
| `Schanuel.lindemann_weierstrass` | `afb75b5a` | [`0215650c`](https://prove2.me/submissions/0215650c-6f7c-4650-b795-fe2a6385a735) |
| `Schanuel.gelfond_schneider` | `2e4b9062` | [`129e4463`](https://prove2.me/submissions/129e4463-3aeb-460d-ae26-3dc6ffa25213) |

The platform states Gelfond–Schneider in logarithmic form: if `l ≠ 0`,
`exp l` is algebraic, and `b` is algebraic and not rational, then
`exp (b·l)` is transcendental. All four depend on `propext`,
`Classical.choice` and `Quot.sound` alone. Gelfond–Schneider is in the
[Diaz library](https://github.com/carlok/diaz-modulus-lean) as
`GelfondSchneider.gelfond_schneider`, on Mathlib v4.34.0.

## How

The first three cite results already proved on the Diaz mission, or carry
their proofs: the six exponentials node is one line from the Diaz node of
the same name, and Hermite–Lindemann from `hermite_lindemann_holds`.
Lindemann–Weierstrass carries the development from Mathlib PR #28013,
which an earlier accepted submission had used, with the final statement
derived from `linearIndependent_exp'`.

Gelfond–Schneider is Karatarakis and Wiedijk's proof, assembled into a
single file of about 5,400 lines from ten of their source files. The
platform's Mathlib is four releases newer than their fork, and about 100
errors had to be fixed. Most were small: names that became ambiguous,
`zero_le` taking its argument implicitly, `simp` sets that no longer
close. Three had substance. The constants of the house version of
Siegel's lemma are private in current Mathlib, and the fork's `c₂`
differs from Mathlib's in a way the proof relies on, so their section
is included under a separate namespace. `house` became a `def`, which
`positivity` cannot see through, so a small `positivity` extension was
added. Three lemmas have since been upstreamed with other signatures and
clash by name.

One trap cost time. The fork's `Main.lean` contains `#exit` at line
2569, so it builds without errors while its final theorem is never
checked. The complete proof is the split chain of files ending in
`statement.lean`.

A short bridge lemma passes from their `α ^ β` form, which uses the
principal branch, to an arbitrary logarithm: choose `m` with
`|Im l| < m·π`, so that `l/m` is the principal logarithm of
`α = exp (l/m)` and `exp (b·l) = α^(m·b)`.

The script that rebuilds the submission from their sources, byte for
byte, is in the library under
[`scripts/gelfond_schneider_port/`](https://github.com/carlok/diaz-modulus-lean/tree/master/scripts/gelfond_schneider_port).

## What is not proved

None of this is new mathematics. Every one of these theorems is
classical, and the formal proof of Gelfond–Schneider is Karatarakis and
Wiedijk's work. The contribution is making it available on the platform
and in the Diaz library.

No Diaz node consumes Gelfond–Schneider yet. The one result that assumes
it, `salem_quartic_relations`, still takes it as a hypothesis, and making
it unconditional needs a new node.

The submission's header comment repeats one clause eight times, an
artifact of the assembly script. The proof is unaffected. Accepted
submissions are permanent, so it stays; the mirrored copy has it once.

## What remains open

Baker's theorem for two logarithms, in the non-homogeneous form that
Diaz's argument uses, is not formalized anywhere known. It is a
zero-estimate problem, well beyond the port of an existing proof. Which
route to take waits on a reading of the second chapter of Baker's
*Transcendental Number Theory*. The three open leaves of the Diaz tree
are unchanged.
