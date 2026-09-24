# The literature check, and a correction

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-24

Carlo asked for two more barrier nodes and then a literature check. The
check found an error in what the morning had published. The error was in
prose, not in any formal statement: every Lean theorem stands as proved.

## The correction

The barrier round claimed that an anisotropic relation such as
`Re(u²) = π²` survives every proved theorem, and that `e^u` is not known to
be transcendental at the points carrying one. Both claims are wrong.

Théorème 0.2 of Roy and Waldschmidt (Ann. Sci. École Norm. Sup. 30, 1997)
is the quadric version of the four exponentials theorem in transcendence
degree one. ℚ-linearly independent logarithms of algebraic numbers in a
field of transcendence degree one satisfy no non-trivial rational quadratic
relation. A candidate algebraic over `ℚ(π)` with `Im u ∉ ℚπ` has exactly
such logarithms in `u`, `ū`, `iπ`. So it carries no rational quadratic
relation at all, anisotropic or not. The generic case was already covered
by algebra.

The note's own boundary section already said that at transcendence degree
one the homogeneous quadric statements are unconditional. The barrier
round's text contradicted it, and nobody checked.

Corrected the same day:

- the text of four nodes: `conj_pair_quadratic_relation_iff`,
  `anisotropic_relation_four_exp_barrier`, `anisotropic_relation_on_circle`
  and `candidate_nongeneric_four_exp_barrier`;
- the companion note, now version 1.5;
- the text of the version 1.4 release;
- the mirror's README;
- the two earlier log entries, by appended notes.

What the anisotropic nodes still say is narrower: no 2×2 configuration sees
such a relation. Roy and Waldschmidt reach it through larger matrices, via
the Clifford algebra of the form.

## What else the check found

- **Roy–Waldschmidt 1997**, the remark after Théorème 0.2: dropping
  homogeneity would give `e^{ℓ²}` transcendental, while `e^{π²}` is open.
  This is the homogeneous/inhomogeneous point the barrier makes, stated in
  1997 for quadrics in transcendence degree one.
- **Roy–Waldschmidt 1997, Corollaire 7.4**: for non-real `λ ∈ ℒ` with `λ`,
  `λ̄` algebraically dependent, `e^{|λ|}` is transcendental. This is the
  homogeneous companion of Diaz's question. Their example is
  `√((log 2)² + π²)`, the note's smallest open instance.
- **Diaz 2007** has no example of a `λ` with `|λ| ∉ ℒ̃` and asks how to
  keep only `|λ|`. It states no barrier.
- **Waldschmidt 2005** (two papers) and his recent four exponentials
  survey: the strong conjecture implies Diaz's; Roy's structural-rank
  conjecture; partial results on 2×2 determinants. No statement of the
  barrier. The survey cites Roy 2002, Cor. 8.3, for why the machinery fails
  on four exponentials. That is a barrier on the method, a different kind.

Verdict: the barrier statements were not found in these sources. They are
elementary and may be folklore. Novelty stays unestablished, not asserted.
Not read: Waldschmidt's book beyond pages checked earlier, Roy 1992, Roy 2002.

## What was proved

| node | inputs |
|---|---|
| `generic_no_strong_six_exp_configuration` | the field linear-forms lemma, the norm lemma |
| `generic_qbar_homogeneous_four_exp_barrier` | the same two |

For `u` algebraically independent of `π`:

- `generic_no_strong_six_exp_configuration`: no 2×3 configuration lies over
  `Q̄ + Q̄u + Q̄ū + Q̄iπ`. So Roy's proved strong six exponentials theorem
  gives nothing against a generic candidate, even with `iπ`. This extends
  the dimension theorem from `1, u, ū` to four generators, where counting
  dimensions no longer decides.
- `generic_qbar_homogeneous_four_exp_barrier`: algebraic coefficients
  without a constant still give no 2×2 configuration.

The first proof splits on one minor. If it vanishes identically, the
linear-forms lemma applies. If not, the Cramer identity for the three
minors of a 2×3 matrix makes the norm form times a linear form vanish.
Four test points kill the linear form, and what remains at `e` is an
algebraic relation among the `y_j`.

## What was dropped

Two further nodes were proved locally but not published. One says a
quadratic relation yields a 2×2 configuration with algebraic
coefficients; the other is its conditional corollary. Roy–Waldschmidt
already shows that candidates carry no such relation, so their premise is
vacuous for candidates.

## Lesson

The research agent had the proved arsenal but not the literature. Its
claim "(iii) not killed by anything I can find" was published without
being checked against Roy–Waldschmidt 1997. That paper had been in
`missions/diaz/sources/` since 2026-09-14, downloaded for the four
exponentials work. A claim of the form "nothing known excludes X" gets a
check against the sources already on disk before it is published.
