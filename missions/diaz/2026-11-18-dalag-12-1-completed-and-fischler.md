# DALAG §12.1 completed, and Fischler 2001 Section 6
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-18

Two rounds published together as release 1.47 of the mirror. The first
finishes the linear algebra of DALAG §12.1 that the previous round
started: all of Prop. 12.13, Cor. 12.14, Prop. 12.6, Prop. 12.2 with
the Remark of p. 424, and §12.1.6. The second formalises Corollary 1.3
of Waldschmidt's *Further variations* and the results of Section 6 of
Fischler's paper on orbits and logarithms, with the stronger form of
his Theorem 1.2 that a note on p. 183 states. Twenty-eight nodes, all
with no hypothesis.

## What was proved

- **DALAG Prop. 12.13:** for a k-subspace E of K containing 1, the four
  conditions are equivalent: a basis made of 1 and algebraically
  independent elements; k-free elements with 1 algebraically
  independent; no homogeneous relation; rank equal to structural rank.
- **DALAG Cor. 12.14:** the same for E = k + E₀ with E₀ ∩ k = {0}.
- **DALAG Prop. 12.2 (D. Roy):** every matrix over the span of 1 and
  algebraically independent elements is k-equivalent to (A B; C 0)
  with A regular, for any field k.
- **The Remark of p. 424:** the same for k + E₀, with E₀ spanned by
  algebraically independent elements, without E₀ ∩ k = {0}.
- **DALAG Prop. 12.6,** in integer form and without the hypothesis
  n < d, which its proof does not use; and **§12.1.6**, that rank equal
  to structural rank gives the Property for any E containing 1.
- ***Further variations*, Cor. 1.3:** for Λ₁, Λ₂, Λ₃ in ℒ̃ with Λ₁
  transcendental and 1, Λ₂, Λ₃ free over Q̄, one of Λ₁Λ₂, Λ₁Λ₃ is not
  in ℒ̃.
- **Fischler 2001:** Lemma 6.1 (a progression of non-zero elements of
  ℒ̃ with transcendental ratio has at most three terms), Th. 1.1,
  Th. 6.2 (2), Th. 6.4 (1) and
  (2), and Cor. 6.3 (1), on powers of linear forms with coefficients in
  ℒ̃; and Th. 1.2 under the hypothesis of the note on p. 183, that no
  hyperplane defined over Q̄ contains both M and the identity.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.dalag_prop_12_13` | `b262b067-8b34-4b7b-909a-3f8521261dde` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_cor_12_14` | `76a6e58d-dbc3-43fa-8ca9-0e5e765dad9b` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_prop_12_6` | `58147bd5-0a24-41fb-b81f-a5dcf1f2a677` | ACCEPTED |
| `DiazModulus.dalag_prop_12_2_ii` | `2e6b38b4-bca5-40bf-aa28-844024cb0fde` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_prop_12_2` | `39bc33c3-09b3-4169-8089-c863c786ea5a` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_remark_12_1_3` | `417f6926-6f7c-45a6-b0e6-465003adf9c4` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.dalag_conclusion_12_1_6` | `2b65057f-29d6-4f79-b5a9-0807695a77d8` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fv_cor_1_3` | `2febd686-af69-4a37-ba86-1323dfdd816d` | ACCEPTED |
| `DiazModulus.fischler_lemma_6_1` | `1b85623e-daf9-4904-a8e3-7aaa8141b30c` | ACCEPTED |
| `DiazModulus.fischler_theorem_1_1` | `20d75a7a-cdb0-48ae-bf68-762001ec7fc3` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_theorem_6_2_two` | `2cf69b3b-df78-46fe-9a86-b3110e1fb70a` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_theorem_6_4_one` | `8c8620d4-3332-4eea-9be5-8681f7b938a2` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_theorem_6_4_two` | `54747983-8fd8-49f9-9aba-c0259dc2a9ad` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_cor_6_3` | `fca32f3a-ece1-484a-8f19-9fd46fbc0744` | SKETCH_ACCEPTED, now Proved |
| `DiazModulus.fischler_centralizer_nb` | `17475831-cba3-4d8c-ace9-229add7e52f5` | ACCEPTED |

Milestones 214–228 are the fifteen rows; the other thirteen nodes
joined by import. All 28 are Proved: 15 were accepted outright and 13
were sketches that upgraded when their children closed. The proofs
have 1,931 lines.

## How

- Prop. 12.2 follows the book's inductive proof, which needs no
  hypothesis on k. It is proved for every E in which k-free elements
  with 1 are algebraically independent, as the book remarks on p. 422,
  and Prop. 12.2 and the Remark of p. 424 both follow from that form.
- The equivalence of Prop. 12.13 runs (i) ⇒ (ii) ⇒ (iv) ⇒ (iii) ⇒ (ii)
  ⇒ (i), with (ii) ⇒ (iv) through Lemma 12.9 in place of the printed
  (i) ⇒ (iv). Prop. 12.6 takes the span of r columns of P⁻¹ for the
  intersection of hyperplanes.
- Fischler's Section 6 rests on one statement, that the Q̄-span of the
  coefficients has dimension at most 2, and at most 1 for k ≥ 3; it is
  proved from Roy's strong six exponentials theorem on a 2 × 3 corner,
  so Lemma 6.1 is not needed for it.
- Each design was checked by an independent referee, who also wrote
  trial proofs of all twelve Fischler nodes and of the Prop. 12.2
  chain; the statements were frozen, then proved against stubs. Chains
  with no stubs, against the mirror's library on Mathlib v4.35.0,
  build on Lean's three axioms.
- The proof agents used lean-lsp-mcp, a Lean language-server tool, for
  the first time in a round. Of seven nodes proved afresh, four
  compiled at the first attempt; in the other three, its tool that
  tries several tactics at once closed what was left.

## Printed statements corrected

- ***Further variations*, the remark after Th. 1.2 (p. 3):** false as
  printed. M = (1 λ; 1 λ) with λ = log 2 has rank 1 and Q̄-free columns,
  but (I M) has dependent columns. It holds with rows and columns free.
- **Fischler, proof of Prop. 5.7 (p. 183):** "dimension at least 2,
  therefore it intersects E" does not follow, since an affine subspace
  can be parallel to E. The conclusion stands, by scaling.
- **Three slips in DALAG:** block sizes on p. 419, a rank on p. 422 and
  a cross-reference on p. 431.

The full list is `ERRATA.md` in the mirror.

## What is not proved

- **Nothing here is claimed as new.** These are formal proofs of
  classical results.
- **DALAG Prop. 12.5** and the second proof of Prop. 12.2 (p. 424),
  which assumes k infinite, are not formalised.
- **Fischler:** Cor. 6.3 (2), a conditional reduction, and Cor. 6.5
  are not formalised, nor are his results on pencils. All results here
  are in the complex case only.

## What remains open

Diaz's conjecture itself; these results enlarge the stock of rank
bounds and of ℒ̃-relations in the library and exclude no new
candidate.
