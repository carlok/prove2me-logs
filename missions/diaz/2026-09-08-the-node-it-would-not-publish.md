# The node it would not publish

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-08

A second LLM ran the Diaz brief twice, in the same tree, under the same account. Both runs
published nothing. One of them should have.

## What it got right

Both runs did the expensive, unglamorous parts properly. Duplicate checks before any Lean
(`q=Diaz` 145 rows, `q=DiazModulus` 51). Grep-verified — not recalled — that this Mathlib has
no Gelfond–Schneider, no transcendence consequence of Lindemann–Weierstrass beyond the
analytical part, and no transcendence of `π`. No git. No other contributor's ground touched.
Every uuid from a live response. Reports written as it went.

Run 2 also did a literature check nobody had done: `e^{1/π}` is not known transcendental, and
the neighbouring numbers — `e^{π²}`, `π^e`, `e^e`, `e+π` — are all open. That is worth having,
and it is consistent with what our node claims.

## What it got wrong

Run 2 machine-checked this, clean, `sorry`-free:

> **Strong four exponentials + Hermite–Lindemann ⟹ `DiazModulus.recip_pi_not_log`.**

and then did not publish it, reasoning that "a conditional route would be an orphan".

That reasoning is inverted. The result is not a conditional dangling in space — it is a
**theorem**, provable outright on this board, because Hermite–Lindemann is already the Proved
node `DiazModulus.hermite_lindemann_holds` and can be discharged rather than carried. What is
left as a hypothesis is the strong four exponentials conjecture alone.

Published as `DiazModulus.recip_pi_not_log_of_sfe`,
<https://prove2.me/theorems/f812a768-18d6-4dab-b39a-7be82b3db489>, and the proof — its proof,
with Hermite–Lindemann discharged from the platform node — came back **ACCEPTED**. So the node
is Proved and it cites `hermite_lindemann_holds`, which is a real edge, not a decorative one.

The sharp observation in its proof is worth repeating: **no `π`-transcendence input is needed.**
Both rows `(1, λ)` and `(1, iπ)` are `Q̄`-independent as soon as `λ` and `iπ` are transcendental,
and Hermite–Lindemann alone gives both — `iπ` because `e^{iπ} = −1` is algebraic, and
`λ = γ/(iπ)` because `e^λ` was assumed algebraic. A run earlier the same day had reached for
`pi_transcendental` in a similar spot.

## The lesson, which is about briefs and not about that model

The brief said, twice and in bold: do not self-close, and do not leave orphans. It did not say
what to do with a result that is *neither* — a theorem worth publishing whose statement carries
an open hypothesis. Faced with two prohibitions and no permission, the model published nothing.

Two prohibitions with no stated positive case is a brief that selects for inaction. The next
version needs the third clause: **a statement you can prove outright, whose hypotheses are named
open conjectures, is publishable and should be published and proved in the same run.** That is
how a mission records *what strength would settle a question*, and half the Diaz graph is built
that way.

Value delivered across two runs before this correction: zero nodes. After: one Proved node
pinning the exact strength that would close `recip_pi_not_log`, and through it two further open
leaves.
