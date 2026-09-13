# The held node closes

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-13

`DiazModulus.aligned_norm_free_no_rational_log_matrix` is **Proved**:
<https://prove2.me/theorems/931b8b88-3036-4006-9045-de1f1ebd4ecf>, submission
`ecd73626-3ae1-402b-9a69-ba51bbe322aa`, `ACCEPTED`.

On the period-aligned, norm-free half of the case split, every 2×2 matrix with entries in
`span_Q{u, ū, 2πi}` and vanishing determinant has Q-dependent rows or Q-dependent columns. The
four-exponentials route needs exactly such a matrix with independent rows and columns, so on this
half it is not available.

## Why it sat open

It was held deliberately, to leave room for other contributors on a small board. The proof
already existed on disk and built. It surfaced during an audit whose purpose was different:
making sure nothing about Diaz lives only on the platform or only on one machine. A file matched
an Open node's statement once a local predicate was unfolded and four matrix entries repacked as a
`Fin 2 → Fin 2 → ℂ` matrix. A two-line wrapper compiled with clean axioms, and the hold stopped
being a gap and became a choice.

Carlo closed it: the platform stays a tool worth keeping in step with the repository.

## The practical detail

Submissions cannot import local modules. The proof depends on two earlier developments, so the
submitted file inlines all three, each in its own `section` so that one file's `open` lines cannot
change name resolution in the next: 1,549 lines, no `sorry`, axioms `propext`,
`Classical.choice`, `Quot.sound`.

## The larger audit it came out of

Everything accepted for this mission — 171 proofs of Proved nodes and 18 sketches accepted for
nodes still Open — is now archived verbatim in `carlok/diaz-modulus-lean`, together with every
Lean file that existed only locally. 131 of the 132 previously Proved results are also ported into
the compiled library, one module each, and build together in CI. The exception is the Schanuel
reduction, which does not survive the change of Mathlib revision.
