# The working folder empties

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-13
- **Repository** — `carlok/diaz-modulus-lean`, commit `ae1a4d1`

Of the 177 local Lean files archived without review, six looked like content found nowhere
else. All six were checked against the board before anything was sent, and one turned out
not to be unique at all.

## What was already there

`DZ_TRDEG_submission` looked unpublished because it imported a local core file instead of
inlining it. With the core inlined, it is exactly the accepted sketch of the norm-rational-multiple
half. Nothing to send.

A second one was half redundant. The shape file for the two axis halves of
`recip_pi_not_log` proves that on the real half the value is not a root of unity. The board
already has that in a stronger form, with no axis hypothesis. Only the two elementary shape
facts were published: modulus one on the real half; real and different from one on the
imaginary half.

## What went up

Three new nodes, each Proved on first submission:

- `DiazModulus.transfer_breaks_exactly`. A ring endomorphism of `ℂ` that fixes the algebraic
  numbers and commutes with conjugation at a candidate `u`, but sends `u` to a non-candidate,
  keeps `|u|` exactly. It fails to commute with `exp` at `u`, is discontinuous, and does not
  stabilise `ℝ`. The transfer theorem's map loses exactly the exponential hypothesis, and
  nothing else.
- `DiazModulus.recip_pi_exp_axis_shape`, the elementary part above.
- `DiazModulus.period_free_split_nondegenerate`. Both children of the period-free split
  contain actual points, `√15 + i` and `√(16 − π⁻²) + i/π`, so neither is vacuous.

Two alternative reductions were accepted as sketches. One puts `diaz_of_exp_not_real` under
the off-axes leaf and the six-exponentials no-go, which links a Proved node that had been
hanging unattached. The other derives `recip_pi_not_log` from its axis halves by closure
under conjugation, which is not a case split.

One reduction failed to build before submission: a conjugation map bound with `have`
could not be unfolded by `rfl`, and `let` fixed it.

## The repository

The 171 redundant files are removed, and so are the six originals, whose content now sits in
the platform archive. The library holds all 136 Proved results, with nothing beyond Lean's
three axioms.
