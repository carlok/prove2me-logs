# Rational squared moduli: at most one pair ±t, and two open statements that cannot both fail

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-29

This sprint set aside twenty minutes of uninterrupted thought for a new
result near Diaz's question, and only then ran a literature check. The
check covered everything held locally: Diaz 2004 and 2007, Roy and
Waldschmidt 1995 and 1997, Waldschmidt 1973, 1974 and 2005, and
Waldschmidt's book on linear algebraic groups, with page images read
wherever a statement mattered.

## What came out

Diaz's conjecture at the point `t + iπ`, where `e^t` is algebraic, says
that `t² + π²` is transcendental. The companion note asks whether
`√((log 2)² + π²)` is algebraic, and nothing proved answers it. The four
exponentials theorem in transcendence degree one, which the library
already proves, turns out to say something about all such numbers at
once.

| node | what it says |
|---|---|
| `DiazModulus.nongeneric_rational_modulus_orbit` | non-zero logarithms of algebraic numbers that are algebraic over `ℚ(π)` and have rational squared modulus are rational multiples of one another, up to complex conjugation |
| `DiazModulus.torsion_rational_modulus_unique` | if `t₀² + π²` and `t₁² + π²` are both rational, with `e^{t₀}`, `e^{t₁}` algebraic, then `t₁ = ±t₀` |
| `DiazModulus.log_two_log_three_not_both_rational` | `(log 2)² + π²` and `(log 3)² + π²` are not both rational |
| `DiazModulus.recip_pi_log_of_torsion_rational_modulus` | if `t² + π²` is rational for a real `t ≠ 0` with `e^t` algebraic, then `e^{iγ/π}` is transcendental for every rational `γ ≠ 0` |

So Diaz's conjecture can fail at a rational value of `t² + π²` for at
most one pair `±t`. And such a failure would settle the statement (S)
at every rational `γ ≠ 0`: at rational data the two open statements
cannot both fail. Since `(log 3)² − (log 2)² = log(3/2)·log 6`, the
third row can also be read as: if `(log 2)² + π²` is rational, then
`log(3/2)·log 6` is not.

None of the four was found in the sources read. Each follows in a few
lines from theorems already in the literature: the four exponentials
theorem in transcendence degree one (Waldschmidt 1973, Corollaire 4;
Roy–Waldschmidt 1995, Theorem 1), and for the last row Waldschmidt's
remark in *Nombres transcendants*, p. 202. The node pages say exactly
that, and claim no more.

## What went wrong first

A second group of statements rested on Waldschmidt's 1973 theorem in its
algebraic-independence form. They were derived from the text file of
the paper, where the hypothesis came through garbled. The theorem needs
the two algebraic exponentials in one column of the matrix. The text
file seemed to allow a diagonal pair. The literature check read the page
image and caught it. Three dichotomies were withdrawn.

One survived in the right form, and the check then found it is one
substitution in the published theorem, and one line from Exercise
15.15(e) of the book. It went up as a specialisation, with the 1973
theorem carried as an explicit hypothesis, because that theorem has no
formal proof yet:

- `DiazModulus.pi_e_exp_pi_sq_indep_of_exp_i_rat_div_pi`: if `e^{ir/π}`
  is algebraic for a rational `r ≠ 0`, then two of `π`, `e`, `e^{π²}`
  are algebraically independent. At `r = 1`: `e^{i/π}`, the smallest
  case of (S), is transcendental, or an open problem listed in the book
  (§15.3.5) is solved.

The lesson is the one already in the rules: read the page, not the OCR.

## Publication

The four statements went up first. The two top results were linked as
milestones, and the proofs were verified parents first while their
children were still Open. The children therefore joined the mission by
import, and the sketches upgraded to accepted proofs once the last child
closed. All five proofs were checked before anything was posted: on
v4.33.1, against their statements, for axioms, and chained on v4.34
against the mirror, where only Lean's three axioms remain.

The five nodes are mirrored in `carlok/diaz-modulus-lean`, which again
holds every proved result of the mission: 267 of 267. The companion note
follows the library, as it always does. Version 1.11 adds the first
three as Corollaries 3.8, 6.9 and 6.10, and the specialisation as a
paragraph beside the Brownawell–Waldschmidt corollary, with its own
status in the appendix: proved, assuming Waldschmidt 1973.
