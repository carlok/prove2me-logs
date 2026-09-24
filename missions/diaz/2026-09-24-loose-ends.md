# The barrier's loose ends, formalised

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-24

The morning's barrier entry left three results on paper:

- the classification of the homogeneous relations a non-generic
  candidate can carry;
- the claim that the period `iπ` never enters a configuration that
  detects a generic candidate;
- indistinguishability with `π` held fixed, over `ℚ(π)` rather than
  over `Q̄`.

All three are now formal. Ten nodes, all Proved.

## What was proved

| node | inputs |
|---|---|
| `conj_pair_quadratic_relation_iff` | none |
| `det_linear_forms_isotropic` | none |
| `anisotropic_relation_four_exp_barrier` | the two above, `det_zero_linear_forms_rank_one`, transcendence of π |
| `anisotropic_relation_on_circle` | transcendence of π |
| `det_zero_linear_forms_rank_one_field` | none |
| `generic_quadratic_relation_is_norm` | none |
| `generic_period_never_enters` | the two above |
| `circle_points_indistinguishable` | `Diaz.exists_ringHom_of_transcendental` |
| `exists_noncandidate_transcendental_on_circle` | none |
| `generic_indistinguishable_over_pi` | the two above |

**Relations.** Take `u = x + iy` off the axes with `y ∉ ℚπ`. The
rational quadratic relations among `u`, `ū`, `iπ` are exactly the
identities `Q(y, π) = s|u|²`, with `Q` a rational binary form. The
determinant of a 2×2 matrix of rational linear forms in three variables
always has a non-trivial rational zero. So a relation whose form has
none, such as `Re(u²) = π²`, is never a determinant. When `|u|²` is
algebraic it is the only relation `u` carries, and every singular 2×2
matrix over `ℚu + ℚū + ℚiπ` has dependent rows or columns. This uses the
transcendence of `π` and nothing about `e^u`. Such relations occur on
every circle of algebraic radius greater than `π`.

**The period.** Let `u` be algebraically independent of `π`. Up to a
factor, the only quadratic relation with algebraic coefficients among
`1, u, ū, iπ` is the norm `X₁X₂ − ρX₀²`. In a singular 2×2 matrix over
`Q̄ + Q̄u + Q̄ū + Q̄iπ` whose rows and columns are `Q̄`-independent, the
coefficient of `iπ` in every entry is zero.

**Indistinguishability.** Two points of a circle, both transcendental
over a conjugation-stable field `K` that contains the squared radius,
are indistinguishable over `K`. On every circle of positive radius,
countability gives a point that is transcendental over a given countable
field and has `e^t` transcendental. With `K` the algebraic closure of
`ℚ(π)`, a candidate algebraically independent of `π` cannot be told from
a non-candidate point of its circle by any vanishing statement with
coefficients algebraic over `ℚ(π)`.

## How

The period argument is the substantial one. By the norm lemma,
`det(Σ x_k C_k) = c(x₁x₂ − ρx₀²)` identically. Then `c ≠ 0`, because
otherwise the 2×2 linear-forms lemma, now proved over any field of
characteristic zero and applied over `Q̄`, gives dependent rows or
columns. For the polar form of the determinant, `C₃` is isotropic and
orthogonal to `C₀, C₁, C₂`.

The research report finished with a non-degeneracy argument. The
formalisation agent found a shorter one. The vector dual to `C₃` is a
left null vector of the 4×4 coordinate matrix of `C₀, …, C₃`. If it is
non-zero, that matrix is singular, some combination `Σ w_k C_k`
vanishes, and pairing with `C₀, C₁, C₂` kills `w₀, w₁, w₂`. Either way
`C₃ = 0`.

The anisotropic barrier compares two relations, the given `F` and the
determinant `G`. A combination of their binary parts vanishes at
`(y, π)`. If it were non-zero, `y/π` would be algebraic, and
`sρ = π²Q(y/π, 1)` would make `π` algebraic. So `G` is a multiple of
`F`. Since `G` has a rational zero and `F` has none, `G = 0`.

## Process

Same as the previous round. I wrote the ten statements, and stubs for
the citations inside the batch. Four formalisation agents ran with
`lake env lean` only. Each proof was read by hand, matched to its
statement by script, and compiled on both Lean versions before its
statement was published. Every proof was accepted on its first
submission.

## What is not proved

This closes the formal record of the barrier. It is not progress on the
conjecture. The two open statements are unchanged: the real half of
(S), and (NT). Whether a candidate can carry an anisotropic relation
such as `Re(u²) = π²` is itself open. No proved theorem excludes it.

**Correction (later the same day).** The anisotropic relations do not
survive every proved theorem. Théorème 0.2 of Roy–Waldschmidt (Ann. Sci.
École Norm. Sup. 30, 1997), the quadric version of the four exponentials
theorem in transcendence degree one, excludes every rational quadratic
relation among `u`, `ū`, `iπ` for a candidate algebraic over `ℚ(π)` with
`Im u ∉ ℚπ`. So no such candidate carries one. The formal results stand;
the texts that said otherwise were corrected. See
[the literature check](2026-09-24-literature-check.md).
