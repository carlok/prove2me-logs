# A barrier on generic data, a dilogarithm dichotomy, and three results from the manuscript
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-04

Asked to try for a bold new result built on the results the literature checks had not found in print,
the session found no positive route to Diaz's conjecture. Every route tried ends at a strong 2×2
statement in transcendence degree one, which is open. What came out instead is:
- a barrier theorem;
- a dichotomy between two open questions about classical constants;
- three results of Carlo's unpublished manuscript, which turned out to be direct instances of
  Waldschmidt 1973.

## What was proved

- **The barrier.** Let u ≠ 0 have uū algebraic, and let w₁, …, w_m be numbers with u, w₁, …, w_m
  algebraically independent over Q̄. Then no Q̄-independent x₁, x₂ and y₁, y₂, y₃ have all six products in
  Q̄ + Q̄u + Q̄ū + ΣQ̄w_j.
  - For a candidate, this means Roy's strong six exponentials theorem cannot refute it on generic data,
    whatever logarithms are added.
  - The case m = 0 is Roy's (1995, Th. 3.4).
- **The dichotomy.** Li₂(1/2) = π²/12 − (log 2)²/2 is irrational, or e^{iγ/π} is transcendental for every
  rational γ ≠ 0. Both are open.
  - Waldschmidt lists the irrationality of Li₂(1/2) as unknown (*Open Diophantine Problems*, 2004,
    p. 274); it is known for Li₂(1/q) only when q ≥ 6 or q ≤ −5.
  - The general form: if a·t² + b·π² is rational for a real logarithm t ≠ 0 and a ≠ 0, then e^{iγ/π} is
    transcendental.
- **From the manuscript:**
  - Theorem 2.5: two candidates with a rational ratio of squared moduli are rational multiples of each
    other, or of the conjugate, exactly when they are algebraically dependent.
  - Theorem 2.3: for distinct candidates whose difference is real or purely imaginary, a rational ratio
    of squared moduli, equal moduli, and v = ±ū are equivalent.
  - Theorem 3.9: for a candidate u and a logarithm μ outside ℚu ∪ ℚū, the numbers u, μ and e^{uū/μ}
    generate transcendence degree at least two.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.generic_circle_point_no_two_by_three_configuration` | `2f818ada-bb16-408c-9e9d-66186a87e8fb` | ACCEPTED |
| `DiazModulus.recip_pi_log_of_rational_quadratic_relation` | `de445e9d-80c9-4aef-864b-71b412e9ea1a` | ACCEPTED |
| `DiazModulus.dilog_half_irrational_or_exp_i_div_pi_transcendental` | `f9999428-837c-4d87-a70f-5790d5c414eb` | sketch, now Proved |
| `DiazModulus.candidate_pair_dichotomy` | `05ec7995-333b-4521-bada-128a331448cc` | ACCEPTED |
| `DiazModulus.candidate_axis_ratio` | `4ceacade-6c53-4820-83b2-764b4e7061c3` | sketch, now Proved |
| `DiazModulus.candidate_mixed_rigidity` | `778ee6fb-417e-413f-9290-d3cc0e0ea607` | ACCEPTED |

The four tops are milestones 103–106, and all six nodes are mission members (248 in all).

## How

- **The barrier** is algebra.
  - Multiplied by u, the space becomes values of polynomials of total degree at most two that are
    constant once the first variable is set to zero. Algebraic independence makes evaluation injective.
  - A rank-one 2×3 matrix of such polynomials factors as (h, g) ⊗ (c₀, c₁, c₂). Total degrees add, and
    setting X₀ = 0 is a ring map.
  - Each case then puts two free vectors in a line or three in a plane.
  - The proof is 292 lines and imports nothing from the project.
- **The dichotomy** applies the four exponentials theorem in transcendence degree one to the matrix with
  rows (t, t²/(iπ)) and (iπ, t). Its entries are logarithms once e^{iγ/π} is assumed algebraic. It is
  Brownawell's Corollary 5 (1974) in general form.
- **The three results from the manuscript** each take one line from Waldschmidt's 1973 theorem: as
  Corollaire 4 at (mu, ū, v), or as the Théorème at x = (u, μ), y = (ū/μ, 1). The manuscript had derived
  them from Roy–Waldschmidt 1997, so its triage had marked them as not yet formalisable.

## What the checks found

- **Citations.** No work citing Diaz 2004 or 2007, Roy–Waldschmidt 1995 or 1997, Waldschmidt 1973, 1988
  or 2005, or DALAG states any of the results checked. Diaz 2007 has a single citer, Waldschmidt's *Role*.
- **Priority.** Brownawell 1974 (Cor. 5 and 7) is one substitution away from several earlier results of
  the mission, now credited. Fischler 2001 (Lemma 6.1) predates Diaz 2007 Th. 7(2) on the geometric
  progressions behind the power hull.
- **A correction.** A referee agent caught an overstatement in the research notes, now corrected. A
  hypothesis z ∈ ℒ̃ brings z̄ ∈ ℒ̃ with it, so a classification of four-dimensional spaces is not a list
  of everything the strong six exponentials theorem excludes.
- **A dropped duplicate.** The unconditional form of `Diaz.log_modulus_forces_independence` was dropped
  before publishing: it is the contrapositive of the Proved
  `DiazModulus.exp_abs_transcendental_of_conj_algebraic`.

## Open

- The classification of the five-dimensional spaces ⟨1, u, ū, z, z̄⟩, and the rank-two bounds.
- Eight nodes that another contributor (Nickrobbins95) added to the mission on 3–4 October are archived
  but not yet mirrored.
