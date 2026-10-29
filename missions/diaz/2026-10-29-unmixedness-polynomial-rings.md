# Macaulay's unmixedness for polynomial rings
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1)
- **Date** — 2026-10-29

The Hilbert side of hME, proved in round C1.1, assumed one thing:
Macaulay's unmixedness (hU). This round (C1.2) proves it for the
polynomial ring in finitely many variables over an algebraically
closed field. Over ℂ, the field of hME, the Hilbert side is now
unconditional.

## What was proved

- **Unmixedness, the inequality half.** For K algebraically closed and
  σ finite, every associated prime of K[X_σ]/(r₁, …, r_k), with
  r₁, …, r_k weakly regular, has height at most k
  (`UnmixedHeight (MvPolynomial σ K)`).
- **The local form.** In a Noetherian local ring with a regular
  sequence of length at least its dimension, the same bound holds for
  every weakly regular sequence in the maximal ideal.
- **Two steps of the local form:** a regular sequence in the maximal
  ideal is at most as long as dim A/𝔭 for any associated prime 𝔭, and
  regular sequences pass to quotients by weakly regular ones, losing
  at most their length.
- **The coordinates.** (X_i − a_i) is a weakly regular sequence of
  R[X_σ], σ finite, for any commutative ring R and any point a.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.unmixedHeight_mvPolynomial` | `2e8fa4bf-b790-4b5b-b6ab-724ef34ed11a` | SKETCH_ACCEPTED, now Proved |

Milestone 170 is the row, the only root of the import graph; the
other four nodes joined by import. All five are Proved: three were
accepted outright, and two were sketches that upgraded when their
children closed.

## How

- One agent proved the whole statement on the platform's toolchain
  in 28 minutes, 438 lines, starting from a spike of 28 October.
- The route goes through Rees' theorem, which the platform's Mathlib
  has, and one short Ext lemma. The depth API of newer Mathlib was
  not needed, so nothing was backported.
- A second agent split it into five nodes. Each was checked against
  its statement with sorry = 0. A chain with no stubs builds on the
  platform's toolchain using only the standard axioms, and in it the
  Hilbert side of hME over ℂ is proved with no hU.

## What is not proved

- **The equality.** Only height ≤ length is proved; the reverse
  inequality is not needed and is not stated.
- **Other fields.** K is algebraically closed; the Nullstellensatz
  gives the regular sequence at each maximal ideal.
- **hME itself.** Its multiplicity side, and the assembly from the
  two sides, are round C1.3. Roy's theorem is still proved here only
  under hME.
- **Nothing here is claimed as new.** Macaulay's unmixedness theorem
  is classical (Macaulay 1916; Bruns–Herzog, Th. 2.1.6); this is a
  formal proof of the polynomial case.
