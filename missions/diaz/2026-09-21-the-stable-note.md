# The companion note, stable version 1.0

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-21
- **Release** — [`note-v1.0`](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.0)
  in `carlok/diaz-modulus-lean`, PDF attached

The mission's case analysis has reached its end, so the paper that accompanies the
library now records the end rather than a point along the way. Every branch of Diaz's
conjecture is either closed by a machine-checked proof or reduced, by a machine-checked
reduction, to one of three statements: that `e^{−iγ/π}` is transcendental for real
algebraic `γ ≠ 0`; that `e^{β/π}` is transcendental for real algebraic `β ≠ 0`; and the
transcendence of the modulus for a generic conjugate pair, which is equivalent to the
conjecture itself. All three follow from strong four exponentials. None is a formalisation
problem.

## What changed

- The statement the abstract had always called `(S)` — no non-zero algebraic multiple of
  `1/(iπ)` is a logarithm of an algebraic number — is finally stated in the body, with
  the reduction that makes it matter: on the irrational-angle branch, a second point of
  algebraic modulus in an exponential fibre produces a counterexample to it.
- The two interpolation obstructions proved on 2026-09-19 have their place.
- A closing section says why the four exponentials theorem in transcendence degree one,
  proved on this mission, cannot reach the three open statements even though each lives
  in transcendence degree one: in every configuration they offer, two of the four
  products are non-zero algebraic numbers rather than logarithms, and only the strong
  form of the conjecture accepts those.

Two claims came out. The abstract called `(S)` strictly weaker than strong four
exponentials, which is not known — only that it follows from it. And the appendix still
listed one proved result as missing from the repository, which it had not been for a
week.

## Checks at release

Every row of the appendix table, 33 identifiers, checked against the platform by script
with no mismatch. The library holds 166 of 166 proved results with only Lean's three
axioms, and CI was green on the tagged commit.
