# A partner for √((log 2)² + π²), and a Sidon set of candidates

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-23

Three research agents were each given one angle on the Diaz problem,
with the proved transcendence theorems as their only tools. The angles
were: barriers to methods, exclusions for counterexamples, and classical
constants near the open boundary. The barriers agent stalled and
produced nothing. The other two returned correct results, which were
checked by hand line by line. Three formalisation agents then wrote the
Lean proofs. Each proof was re-checked for exact statement match and for
the absence of `sorry`, and compiled on both Lean versions before
anything was published. Thirteen nodes, all Proved.

## What was proved

The headline concerns the question the companion note singles out as
the smallest open instance of Diaz's conjecture: is
`√((log 2)² + π²)` algebraic? Nothing answers it, but it now has a
partner.

- `diaz_number_forces_transcendence` — if `t² + π²` is algebraic for a
  real `t` with `e^t` algebraic, then `e^{it²/π}`, `e^{π²/t}` and
  `e^{(t²+π²)/(iπ)}` are all transcendental.
- `log_two_diaz_or_transcendental` — at least one of
  `√((log 2)² + π²)` and `2^{i log 2/π}` is transcendental.

The third number in the first node says that the two statements the
development still depends on cannot fail at the same number. Those are
the rational-angle question and the real half of (S). The two research
agents found this coupling independently.

With two candidates the six exponentials theorem starts working:

- `log_ratio_multipliers` — the logarithms that `u/v` multiplies back
  into logarithms, for `|u|²/|v|²` rational.
- `candidate_conj_product_rational`, `conj_ratio_multiplier_relation` —
  two lemmas.
- `candidate_quotient_rigid`, `candidate_product_relation_trivial` — the
  arguments of the candidates on a circle of algebraic radius form a
  Sidon set, up to conjugation. This is the first constraint of any
  kind on candidates that are algebraically independent.
- `candidate_neg_one_pow_ratio` — `(−1)^{u/ū} = e^{iπu/ū}` is
  transcendental for every candidate.

The rest:

- `candidate_harmonic_not_log` — the harmonic mean of `u` and `ū` is
  not a logarithm.
- `recip_pi_or_pi_cube`, `exp_i_div_pi_or_exp_i_pi_cube_transcendental`
  — `e^{i/π}` or `e^{iπ³}`.
- `log_square_duality`, `two_pow_log_three_or_three_pow_log_two` —
  `2^{log₃ 2}` or `3^{log₂ 3}`.

## How

For the headline, the hypothesis `t² + π² ∈ Q̄` is used only once: it
makes `t` algebraic over `ℚ(π)`, which supplies the
transcendence-degree hypothesis of the four exponentials theorem in
degree one. The rest is the geometric triple `iπ, t, t²/(iπ)`: its
first two entries are logarithms (of `−1` and of `α`), so the third
is not.

For two candidates, six exponentials needs a rank-one `2×3` array of
logarithms. One candidate certifies only three dimensions. The note's
dimension theorem shows that this is exactly why six exponentials
cannot refute a single candidate. A second candidate `v` with `|u|²/|v|²`
rational supplies a fourth: `u/v` multiplies `v` to `u` and `ū` to a
rational multiple of `v̄`. Gelfond–Schneider then converts "algebraic
real part of `pq`" into "`q` is a rational multiple of `p̄`".

## What is not proved

No open node closed. The two statements the Diaz tree depends on are
exactly as open as before. The candidate results are exclusions for
hypothetical counterexamples, vacuous if Diaz's conjecture holds. The
constants results are disjunctions: none of `√((log 2)² + π²)`,
`2^{i log 2/π}`, `e^{i/π}` or `2^{log₃ 2}` is proved transcendental on
its own. Every statement is a short consequence of classical theorems.
None is claimed as new.

## What remains open

The real half of (S) and (NT), and in particular the question itself:
is `√((log 2)² + π²)` algebraic?

**Note (24 September, after reading the literature).** Most of these results are
classical or special cases of published ones. `e^{i/π}` or `e^{iπ³}` is
Waldschmidt 1973 (J. Number Theory 5, p. 192), and the other partners of (S) are
his Corollaire 4. The square duality and the involution lemma are the ℚ-linear
forms of Diaz 2007, Corollaire 4(3) and 4(4). The headline has a stronger known
form: `2^{i log 2/π}` is transcendental as soon as `log 2` and `π` are
algebraically dependent (Waldschmidt, Lecture Notes 402, p. 202). See
[Reading everything: attributions](2026-09-24-sweep.md).
