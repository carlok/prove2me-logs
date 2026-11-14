# Further variations Th. 2.1 for every Y, and Roy's φ in closed form
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-14

Three loose ends of the earlier round of the day are closed. Waldschmidt's
*Further variations*, Th. 2.1, is printed for every Q̄-subspace Y but
its proof takes a finite basis; it is now proved as printed. Roy's
closed form of φ, the bound in his Theorem 5, is proved, with DALAG's
integer table Ψ and Cor. 11.15 in its printed form. And DALAG
Cor. 12.23, the rank bound for entries in ℚ + ℒ, is proved. Fifteen
nodes, all with no hypothesis.

## What was proved

- **Further variations, Th. 2.1, for every Y,** with the hypothesis as
  printed (the dimension of Y/(Y ∩ V) as a cardinal), and in a form
  with finite witnesses.
- **Roy 1992, Lemma p. 40:** the closed form is the greatest value of
  Σ nᵢdᵢ/(dᵢ − nᵢ) over the decompositions of (n, d); its integer part
  is DALAG's Ψ(n, d).
- **DALAG Cor. 11.15** with the printed bound Ψ(dim V, d_min).
- **DALAG Cor. 12.23:** the rank of a matrix with entries in ℚ + ℒ is
  at least half its structural rank.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.fv_theorem_2_1_rank` | `e4db0982-f503-44a4-b431-c32603b2d4fa` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.roy_lemma_phi` | `057fca9b-674e-4315-a7d3-7777769c0384` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_cor_11_15_psi` | `b197af13-ef7c-4dbe-bed0-c02b3d893253` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_cor_12_23` | `db2914f2-8295-45b1-9e73-f9f77fc0aaff` | SKETCH_ACCEPTED, now Proved |

Milestones 203–206 are the four rows; the other eleven nodes joined
by import. All 15 are Proved: 6 were accepted outright, and the
rest were sketches that upgraded when their children closed. The
proofs have 1,175 lines.

## How

- One finite-dimensional Y₀ ⊂ Y serves every subspace V at once. It
  maximises a bounded integer built from the intersection I of the
  V where Y₀ falls short; that intersection is reached by at most n
  of them. Then the finite case applies to Y₀.
- Roy's Lemma is proved by superadditivity of the closed form, not
  by Roy's exchange argument.
- Each design was checked by an independent referee before any Lean;
  the statements were frozen, then proved against stubs. A chain with
  no stubs, against the mirror's library on Mathlib v4.35.0, builds on
  Lean's three axioms.

## Printed statements corrected

- **Further variations Th. 2.1:** true for every Y; only the printed
  proof is limited to finite-dimensional Y.
- **Roy 1992, proof of the Lemma (p. 41):** "k = 2" does not follow
  from the two exclusions, since parts (1, 1) escape both; for
  (n, δ) = (3, 4) the decomposition (1, 2), (1, 1), (1, 1) meets them
  with k = 3. One more exchange repairs it; the Lemma is correct.
- **DALAG:** the proof of Lemma 12.9 leaves a dehomogenisation step
  to the reader, and the table Ψ (p. 394) leaves Ψ(0, 0) undefined.

The full list is `ERRATA.md` in the mirror.

## What is not proved

- **Nothing here is claimed as new.** These are formal proofs of
  classical results.
- **Only K = Q̄** for Cor. 11.15; DALAG's (ℚ, ℚ + ℒ) case is not done.
- **Cor. 12.23 in the presentation form** of structural rank; DALAG's
  affine form would need his Lemma 12.9, which is not formalised.

## What remains open

Diaz's conjecture itself; these results enlarge the stock of rank
bounds in the library and exclude no new candidate.
