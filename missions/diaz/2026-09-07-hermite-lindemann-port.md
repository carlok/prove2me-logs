# Hermite–Lindemann now holds in the platform environment, and one node that everyone routed through it never needed it at all

- **Mission** — Diaz modulus conjecture, proposal `039adfb9-57cd-4cef-a6f4-c59dcf005f77`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

Hermite–Lindemann says that for algebraic `α ≠ 0`, `exp α` is transcendental.
It is the workhorse of the Diaz development: most of the mission's implications
are conditional on it, stated as `HermiteLindemann → …` because Mathlib has no
proof of it at this revision. Making it unconditional was worth more than any
single node, and it turned out to be reachable.

## What was proved

Seven nodes, all ACCEPTED, all `sorry`-free, and all with
`#print axioms` reporting only `[propext, Classical.choice, Quot.sound]`.

| theorem | node | submission |
|---|---|---|
| `Diaz.exists_transcendental_on_circle` | <https://prove2.me/theorems/83d7590f-ae1f-41f8-a2e1-62ec6b6dfd49> | <https://prove2.me/submissions/e5b16731-40b4-4163-ac53-7e55938b523a> |
| `Diaz.exists_transcendental_on_circle_Qbar` | <https://prove2.me/theorems/d5fd3edc-e2b3-4ce8-81fe-0031219b2b44> | <https://prove2.me/submissions/c0e6edef-4848-4a67-ad41-321ead070e12> |
| `DiazModulus.hermite_lindemann_holds` | <https://prove2.me/theorems/fdc68131-2e60-4005-9489-8758a2174325> | <https://prove2.me/submissions/f67b6de7-fd9f-42f9-91ab-7e355eaf61df> |
| `Diaz.transcendental_of_candidate` | <https://prove2.me/theorems/3cae2e48-64f1-4be8-be0d-69719a233f94> | <https://prove2.me/submissions/ee5abf42-966a-42dc-874f-78d833d5ba1d> |
| `Diaz.four_nodes_candidate` | <https://prove2.me/theorems/6f338e64-261b-4533-b300-c115e5c81804> | <https://prove2.me/submissions/23318a9a-5e08-4a86-8f7e-b23f70fcd185> |
| `Diaz.candidate_no_vanishing_coeff_Qbar` | <https://prove2.me/theorems/16400e12-6f0a-4e53-b7b6-bcf77ad662da> | <https://prove2.me/submissions/5ba6e7fa-2b46-499f-9d1c-ee0b81a7fcfa> |
| `Diaz.candidate_indistinguishable` | <https://prove2.me/theorems/3592d95c-2f6b-4a36-9888-290e1e3a2c0e> | <https://prove2.me/submissions/7f16a044-1afe-4bfc-9be2-7090c1fffcfb> |

The companion project `carlok/diaz-modulus-lean` is now 29/29 theorem nodes
Proved, up from 23/29. The mission proposal stands at 6 Proved, 1 definition
and 2 Open, up from 5 Proved and 3 Open; it is still `In review`, so its
`mission_id` remains null.

## How

**The Lindemann–Weierstrass port.** The mathematics is Yuyang Zhao's, from the
open Mathlib PR #28013, which has been sitting there for months. It still
compiles against the pinned revision `0df444a3` with five mechanical fixes:
back-ports of `Multiset.esymm_zero`, `Multiset.esymm_of_card_lt` and
`Polynomial.scaleRoots_aeval_smul` (three or four lines each), all of
`Mathlib.Data.Finsupp.Quotient` (about fifty lines), and one instance diamond.
The diamond is the only interesting one: for `K : IntermediateField ℚ S` the
synthesised `Algebra ℚ K` is `DivisionRing.toRatAlgebra`, not `K.algebra'`, and
the two are not reducibly defeq, so `IntermediateField.adjoin_rootSet_isSplittingField`
needs a local `let _i : Algebra ℚ K := K.algebra'` to typecheck. `transcendental_pi`
had to be dropped — it needs `Complex.isIntegral_I`, which is absent here.

Because a solution cannot import its own target's module, the port is inlined
into each solution that uses it. Those five files run 43–53 KB. Attribution to
Zhao is written into every one of the four explanations; the contribution
claimed here is the port, the back-ports and the derivations, not the theorem.

**The node that did not need any of it.** `exists_transcendental_on_circle`
asks for a transcendental point on a circle of algebraic radius. The source
development reaches it through transcendence of `e^i`, which is why it looked
like it needed Hermite–Lindemann. It does not. Parametrise the circle by its
real part, `f(x) = x + i√(ρ − x²)`; this is injective because `Re f(x) = x`.
The algebraic numbers are countable (`Algebraic.countable ℚ ℂ`) and the
interval `(−c, c)` has cardinality of the continuum, so some point of the
circle is transcendental. Thirty-five lines, unconditional, and no
transcendence theory at all.

## What is not proved

Hermite–Lindemann here is a *port*, not an independent formalisation. If
PR #28013 has an error, this inherits it. What the platform verified is that
the ported development compiles and that the derived nodes follow from it with
no `sorry` and no extra axioms.

`transcendental_pi` is not available, so anything needing transcendence of π is
still out.

Nothing was pushed, filed or commented on Mathlib. The account of the port —
the five fixes, and the observation that the PR still applies cleanly months
on — sits in a local gitignored draft for a human to post under their own name.
It is not in this repo, and it should not be attributed to an AI when it goes
up.

## What remains open

The two remaining Diaz nodes, and neither is close.

`DiazModulus.six_exponentials`
(<https://prove2.me/theorems/7d362030-8eff-4aa9-8138-7b9b15cda0be>) is a real
theorem, but it does not follow from Lindemann–Weierstrass, and no Lean
formalisation exists anywhere to port. It needs Schneider's method: an
auxiliary function, a descent, and a zero estimate. That is what the `six-exp`
ladder is for, and one of its four rungs is now Proved — see
`missions/six-exp/2026-09-07-zero-estimate.md`.

`DiazModulus.diaz_modulus_conjecture`
(<https://prove2.me/theorems/ba87d640-a434-4533-84f9-257c023754c3>) is the open
problem itself. It is not going to fall to a solver.
