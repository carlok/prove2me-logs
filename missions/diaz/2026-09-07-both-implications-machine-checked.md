# Both implications Diaz asserts in one sentence are now machine-checked

- **Mission** — Diaz's modulus conjecture (proposal `In review`),
  `039adfb9-57cd-4cef-a6f4-c59dcf005f77`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1)
- **Date** — 2026-09-07

Diaz records, in a single sentence and without proof, that his modulus
conjecture follows from Schanuel's conjecture and from the strong four
exponentials conjecture. As far as could be established neither
derivation has been written out anywhere. Both are now formal.

## What was proved

| node | uuid | submission |
|---|---|---|
| `diaz_on_axes_of_hermite_lindemann` | `36d1a5d8` | `67fef296` |
| `diaz_of_schanuel` | `b1434763` | `9f52c1d5` |
| four exponentials (name below) | `3c858325` | `9f0385db` |

The third node is
`DiazModulus.diaz_of_strongFourExponentials_and_hermite_lindemann`.

With `logAlg_conj_stable` and `conj_eq_norm_sq_div` closed earlier the
same day, the proposal now carries **5 of 9 nodes and 3 of 5 milestones
proved while still in review**.

## How

**The axes.** `‖u‖² = u · conj u` holds for every complex `u`, and on
either axis conjugation acts as a sign, so `u²` differs from `‖u‖²` by
one. `IsAlgebraic.of_pow` then climbs from `u²` back to `u`. Working
through the bundle's `Qbar` subfield rather than `IsAlgebraic` directly is
what keeps it short: Mathlib has no `IsAlgebraic.neg` or
`IsAlgebraic.mul` to hand, but a subfield has every closure property for
free.

**Four exponentials.** One `2×2` configuration, `(u, ‖u‖; 1, ‖u‖/u)`,
whose four products are `u`, `‖u‖`, `‖u‖` and `conj u`. Both independence
hypotheses reduce to a single shared lemma — clearing the denominator in
`s·1 + t·(‖u‖/u) = 0` turns it into literally the equation for the pair
`(u, ‖u‖)` — and that lemma holds because `u ∉ Q̄`, which is
Hermite–Lindemann applied to the contradiction hypothesis.

**Schanuel.** Apply it at `n = 2` to `(u, conj u)`; the four adjoined
elements all lie in `Q̄(u)`, whose transcendence degree over `ℚ` is at
most 1, contradicting the bound of 2. The bookkeeping is `trdeg_add_eq`
(Stacks 030H) used twice, through `ℚ ⊂ Q̄ ⊂ Q̄(u)` and through
`Q̄ ⊂ Q̄[u] ⊂ Q̄(u)`, with the polynomial surjection
`Polynomial Q̄ ↠ Q̄[u]` bounding the middle term via
`Polynomial.trdeg_of_isDomain = 1`.

Three Lean facts that cost time and are not discoverable by guessing:
`Algebra.IsAlgebraic ℚ ↥(algebraicClosure ℚ ℂ)` does not fire as an
instance and must be passed explicitly; the scoped block
`IntermediateField.algebraAdjoinAdjoin` supplies the `IsFractionRing`,
`IsScalarTower` and `FaithfulSMul` instances that `trdeg_add_eq` demands,
turning the middle step from a page into a line; and
`Algebra.trdeg ℚ ↥(F.restrictScalars ℚ) = Algebra.trdeg ℚ ↥F` is `rfl`.

## What is not proved

All three are **conditional**. Two take `HermiteLindemann` as an explicit
hypothesis, which the mission discharges in its own node and which is
still open. The Schanuel route takes no such hypothesis — Schanuel at
`n = 1` *is* Hermite–Lindemann — but it assumes Schanuel, which is open.
Nothing here bears on whether a non-zero logarithm of an algebraic number
can have algebraic modulus.

The axis milestone is weaker than its name suggests, and its own entry
says so: on the axes, `‖u‖` algebraic is *equivalent* to `u` algebraic, so
the distinguishing feature of Diaz's question has no force there and the
conclusion is an instance of the assumed hypothesis.

## What remains open

`hermite_lindemann_holds` and `six_exponentials` — both classical
theorems, both absent from every pinned Mathlib revision on the platform
— and the goal itself. Hermite–Lindemann is also a *special case* of the
goal, so no route can avoid it. Mathlib PR #28013 would supply it; it has
100 commits across five contributors and is actively developed, so the
sensible thing is to wait for it or attack the node independently, not to
transcribe it.
