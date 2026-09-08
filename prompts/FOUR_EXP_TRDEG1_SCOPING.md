# Scoping task: four exponentials in transcendence degree one

You are asked to **plan a formalisation, not to perform one.** Read the whole brief before
starting. The deliverable is a decomposition and an inventory, and a wrong inventory is worse
than a short one.

## The theorem

Let `λ₁₁, λ₁₂, λ₂₁, λ₂₂` be non-zero logarithms of algebraic numbers — that is,
`exp λᵢⱼ ∈ ℚ̄` for each — with

```
λ₁₁ λ₂₂ = λ₁₂ λ₂₁        and        trdeg_ℚ ℚ(λ₁₁, λ₁₂, λ₂₁, λ₂₂) ≤ 1.
```

Then the two rows, or the two columns, of the matrix `[[λ₁₁, λ₁₂], [λ₂₁, λ₂₂]]` are linearly
dependent over `ℚ`.

Equivalently, and this is how the source states it: if `x₁, x₂` are ℚ-linearly independent
complex numbers, `y₁, y₂` likewise, and `ℚ(x₁, x₂, y₁, y₂)` has transcendence degree 1 over
`ℚ`, then at least one of `e^{x₁y₁}, e^{x₁y₂}, e^{x₂y₁}, e^{x₂y₂}` is transcendental. The two
forms are identified in the source itself.

This is the four exponentials **conjecture** restricted to transcendence degree one, where it
is a **theorem**.

## Sources

- D. Roy and M. Waldschmidt, *Quadratic relations between logarithms of algebraic numbers*,
  Proc. Japan Acad. Ser. A **71** (1995), 151–153. This is the statement (their Theorem 1) and
  a sketch of a new proof. Author's copy:
  <https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/ProjectEuclid/ProcJapanAcad71-1995.pdf>
  Publication list: <https://webusers.imj-prg.fr/~michel.waldschmidt/texts.html>
- The original proofs, to which that note refers:
  - W. D. Brownawell, *The algebraic independence of certain numbers related to the
    exponential function*, J. Number Theory **6** (1974), 22–31, Corollary 7.
  - M. Waldschmidt, *Solution du huitième problème de Schneider*, J. Number Theory **5**
    (1973), 191–202, Corollary 4.
- Background: M. Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*,
  Springer 2000, Chapter 11 for the four exponentials circle.

## Target environment

Lean 4 with Mathlib at revision `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1).
Statements must typecheck against that Mathlib. Transcendence degree there is
`Algebra.trdeg ℚ` of `Algebra.adjoin ℚ` of a set; "logarithm of an algebraic number" is
`IsAlgebraic ℚ (Complex.exp l)`.

## What to produce

### 1. A proof skeleton in prose

Which of the two original routes — Brownawell's or Waldschmidt's — is the better
formalisation target, and why. Then that proof broken into numbered steps, each step a
statement a competent Lean author could attempt in isolation. Say what each step needs from
the ones before it. Aim for the granularity where a step is one to three days of work, not
one where a step is a paper.

### 2. A Mathlib inventory, three columns

For every ingredient the skeleton uses:

| ingredient | present in Mathlib at this revision? | if present, the declaration name |

**Do not guess declaration names.** If you are not certain a declaration exists under a name
you can recall, write `UNVERIFIED — check` and describe what to search for instead. A
confidently wrong `Mathlib.Foo.bar_baz` costs a reader more time than an honest gap. Mark the
whole column as unverified if you have no way to check the revision.

Ingredients to consider at minimum: Siegel's lemma / Thue–Siegel, auxiliary function
construction, Laurent's interpolation determinants, zero estimates on commutative algebraic
groups (Philippon), Liouville's inequality in the height form, absolute logarithmic height and
Mahler measure, Wirsing's approximation theorem, Gel'fond's transcendence criterion,
transcendence-degree API.

### 3. The missing-prerequisite list, ordered

Everything the inventory marks absent, ordered so that each entry depends only on earlier
ones. For each: a one-line Lean **statement** (not proof), and an estimate of difficulty in
the categories *routine*, *substantial*, *research project*.

### 4. An honest verdict

State plainly whether this is formalisable with current Mathlib at reasonable effort, and if
not, name the single biggest obstacle. "This is not currently feasible and here is why" is an
acceptable and useful answer. It is more useful than an optimistic plan.

## Hard rules

- **Produce no Lean proof containing `sorry` and present it as progress.** Statements are
  wanted; fake proofs are not.
- **Do not invent citations, theorem numbers, or Mathlib declaration names.** If you cannot
  verify something, label it unverified and say what would verify it.
- If you have web access, check the sources above rather than reciting from memory; the 1995
  note is three pages and freely available at the link given.
- Distinguish throughout between the four exponentials **conjecture** (open), the six
  exponentials **theorem** (proved, Siegel–Lang–Ramachandra), and the transcendence-degree-one
  case (proved, and the subject of this task). Conflating the first two is a common error.

## Output format

Markdown. Sections 1–4 in that order. No preamble, no summary of the task back to me.
