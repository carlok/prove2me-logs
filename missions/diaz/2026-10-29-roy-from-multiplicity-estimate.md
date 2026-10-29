# Roy's theorem from a multiplicity estimate
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-29

Many results in this mission assume Roy's strong six exponentials
theorem as a hypothesis, `hSSE`. A Lean proof of it exists, but it has
no licence, so it is not used. This round (C1.4) proves the theorem
from one explicit hypothesis, `hME`: an elementary form of the
multiplicity estimate, DALAG Th. 8.1 in the case G⁻ = {e}. It takes
26 nodes and one definition.

## What was proved

- **Roy's theorem, given hME.** If x ∈ ℂ² and y ∈ ℂ³ each have
  coordinates linearly independent over Q̄, then some product x_i y_j
  lies outside ℒ̃. This is DALAG Cor. 11.16 with d = 2, ℓ = 3. Its
  shape is the library's `hSSE` exactly, so every node that assumes
  `hSSE` can take `hME` instead.
- **Th. 11.21 of DALAG, given hME**, in the case d₀ ≤ n. This is the
  linear subgroup theorem the reduction uses. The interpolation
  determinant (Lemma 9.2) is proved along the way.
- **The reduction needs no Baker.** Lifts of a ℚ-basis replace the
  injectivity step of Lemma 11.18(4), the only place where DALAG uses
  Baker's theorem.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.strong_six_exponentials` | `bec66d28-1e35-4a81-bc07-151c0be6d3b6` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.linear_subgroup_transcendence` | `199ac749-9921-49a0-880f-5264eee8ee59` | SKETCH_ACCEPTED, now Proved |

The hypothesis is the definition `MultiplicityEstimateElem`,
`06d76f73-85da-4674-abc8-c9200d75632e`. Milestones 161 and 162 are
the two rows above. The other 24 nodes joined the mission by import.
All 26 are Proved: 17 were accepted outright, and 9 were sketches that
upgraded when their children closed.

## How

- Two independent designs, a synthesis, then eight parallel proof
  agents. Every node was checked against its statement with sorry = 0.
- A clean room: no agent opened another formalisation of the theorem.
- The mirror holds the 26 nodes, the definition, and one bridge,
  `Diaz.strongSixExponentials_of_multiplicityEstimateElem`. All build
  on Mathlib v4.35.0 and use only the standard axioms.
- Before the proofs, 436 exact small instances of hME were checked by
  computation, with 0 failures, so the hypothesis is not vacuous by
  construction.

## Found on the way

- **Citations.** Ten text defects were fixed before publishing. Θₙ is
  defined in DALAG §6.2.2: the book's §6.1.2 is a misprint in the
  proof of Lemma 9.2, and its "Lemma 6.1" does not exist (Schwarz's
  lemma is Lemma 2.4).

## What is not proved

- **hME itself.** It is a hypothesis. It should follow from DALAG
  Th. 8.1, but that derivation is not formal. Proving it is rounds
  C1.1 to C1.3: Hilbert functions, Macaulay unmixedness, and the
  multiplicity estimate.
- **Roy's theorem in general.** Only d = 2, ℓ = 3 is proved, the case
  the library uses.
- **Nothing here is claimed as new.** The theorem is Roy's (1992), and
  the route is DALAG §11.6–11.7.

## What remains open

- C1.1, the Hilbert-function layer, is published the same day; its own
  entry follows once its verdicts are in.
- C1.2: Macaulay unmixedness on the platform toolchain.
- C1.3: hME itself.
