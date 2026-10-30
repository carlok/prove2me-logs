# The multiplicity estimate, and Roy's theorem with no hypothesis
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-30

Round C1.4 proved Roy's strong six exponentials theorem from one
hypothesis, hME: the case G⁻ = {e} of the multiplicity estimate,
DALAG Th. 8.1. Rounds C1.1 and C1.2 proved its Hilbert side over ℂ.
This round (C1.3) proves the multiplicity side and assembles hME. So
Roy's theorem is now proved on the platform with no hypothesis.

## What was proved

- **The multiplicity estimate.** hME, the case G⁻ = {e}, G⁺ = G of
  DALAG Th. 8.1 for G = 𝔾ₐ^{A₀} × 𝔾ₘ^{A₁} over ℂ, written in
  coordinates. For G⁻ = {e} and finite Σ it is a case of Th. 2.1 of
  Philippon 1986.
- **Roy's strong six exponentials theorem, unconditional.** For x in
  ℂ² and y in ℂ³, each free over Q̄, some xᵢyⱼ is outside the span of
  1 and the logarithms of algebraic numbers (Roy 1992, Cor. 2).
- **On the way:** zero sets and heights on the torus, Dedekind's
  lemma with polynomial coefficients, the invariant derivations of G,
  the tangent duals of DALAG Lemmas 8.14–8.16 with Wüstholz's
  argument, and the descent of §8.4.1 to an obstruction subgroup.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.multiplicityEstimateElem` | `382b9f05-eddb-4ee3-932d-3edb5fb187bf` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.strong_six_exponentials_unconditional` | `baa9e124-e0cd-4e73-a079-5fbd02908e93` | SKETCH_ACCEPTED, now Proved |

Milestones 171 and 172 are the rows; the other thirty nodes joined by
import, over one more published definition, `DiazMultiplicity`. All
32 are Proved: fifteen were accepted outright, and seventeen were
sketches that upgraded when their children closed.

## How

- Two agents designed the round independently, one along DALAG §8.4
  and one for the cheapest correct route; a synthesis fixed 32 nodes.
- Eight agents proved them in parallel against stubs. A ninth
  rechecked each proof against its statement with sorry = 0.
- A chain with no stubs, all four rounds (96 nodes, 11,221 lines),
  builds on the platform's toolchain and gives Roy's theorem with no
  hypothesis on the three standard axioms.
- The mirror holds the 32 nodes and two bridges:
  `Diaz.strongSixExponentials`, Roy's theorem with no hypothesis, and
  `Diaz/RoyUnconditional.lean`, which restates each of the 25 results
  that took it as a hypothesis without it.
- The agents worked under a clean-room rule: no agent was to open
  another formalisation of the theorem.

## What is not proved

- **Th. 8.1 in general.** Only the case G⁻ = {e}, G⁺ = G is proved,
  for this G and in coordinates; that is the case Roy's theorem uses.
- **Nothing here is claimed as new.** The multiplicity estimate is
  classical (Philippon 1986; DALAG Ch. 8, by D. Roy), and so is Roy's
  theorem (Roy 1992). This is a formal proof of the known arguments.
