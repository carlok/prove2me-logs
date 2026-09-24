# The statement (S) can fail in one direction only, and Diaz needs only one

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-23

Gelfond–Schneider and the four exponentials theorem in transcendence
degree one are now both proved on the platform. This entry records what
they give when turned back on the Diaz problem and on a few classical
constants. They decide no open statement. Between them they shrink the
open boundary from three statements to two, prove that two open
statements cannot both be false, give an unconditional fragment of an
exclusion that previously needed Roy's strong six exponentials theorem,
and show that at least one of `e^{π²}` and `e^{iπ³}` is transcendental.

## What was proved

| node | kind |
|---|---|
| `DiazModulus.recip_pi_log_rational_line` | Proved |
| `DiazModulus.recip_pi_log_on_axis` | Proved |
| `DiazModulus.recip_pi_not_log_real_or_imag` | Proved |
| `DiazModulus.log_pair_rigid_of_trdeg_one` | Proved |
| `DiazModulus.candidate_monomial_not_log` | Proved |
| `DiazModulus.geometric_triple_not_logs` | Proved |
| `DiazModulus.exp_pi_sq_or_exp_i_pi_cube_transcendental` | Proved |
| `DiazModulus.pi_log_two_or_pi_log_three_transcendental` | Proved |
| `DiazModulus.two_three_five_pow_pi_transcendental` | Proved |
| `…period_aligned_norm_free`, new reduction | via the real half only |
| `…period_free_pi_im_algebraic`, new reduction | via the real half only |

The statement (S) says that `e^{γ/(iπ)}` is transcendental for every
non-zero algebraic `γ`. It splits into a real half and an imaginary half,
and both are open. Let `S₀` be the set of algebraic `γ` with
`e^{γ/(iπ)}` algebraic. Then `S₀` is either `{0}` or a single rational
line, and that line lies on the real or on the imaginary axis. So the two
halves cannot both fail. That disjunction has no hypotheses: it is an
unconditional theorem about two open statements.

The Diaz tree reached (S) along two branches, and both only ever
produce a real `γ`. The two new reductions record this, so the
imaginary half is no longer on the tree. The formal development now
stops at the real half and at the statement (NT), which is equivalent
to the conjecture itself.

Separately, let `u` and `v` be non-zero logarithms of algebraic numbers
with `|u|²/|v|²` rational, such that `u, ū, v, v̄` have transcendence
degree at most one. Then `v` is a rational multiple of `u` or of `ū`.
For a hypothetical Diaz candidate `u` this makes `e^{c u^k}`
transcendental whenever `k ≥ 2` and `|c|²|u|^{2(k−1)}` is rational. One
example is `e^{u²/|u|}`.

The same two theorems, applied to classical constants rather than to
hypothetical counterexamples, give three unconditional statements.

- At least one of `e^{π²}` and `e^{iπ³}` is transcendental. The number
  `e^{π²}` alone is open. It is the example Waldschmidt gives of what an
  inhomogeneous extension of the rank theory would reach, which is
  where Diaz's conjecture is stuck.
- At least one of `π log 2` and `π log 3` is transcendental. Neither is
  known to be.
- At least one of `2^π`, `3^π`, `5^π` is transcendental. That is the six
  exponentials theorem at `x = (1, π)`, `y = (log 2, log 3, log 5)`.

## How

The (S) results are one application of Gelfond–Schneider. If `γ₁` and
`γ₂` are in `S₀`, then `γ₁/(iπ)` and `γ₂/(iπ)` are logarithms of
algebraic numbers with algebraic ratio `γ₁/γ₂`, and Gelfond–Schneider
forces that ratio to be rational. Conjugation maps `S₀` to itself,
because `\bar γ/(iπ) = −\overline{γ/(iπ)}`. So `\bar γ = qγ`, and
comparing parts puts `γ` on an axis. A real exception and an imaginary
one would be proportional, which is impossible.

The pair theorem is one application of the four exponentials theorem in
transcendence degree one, to the matrix `[[u, v], [c v̄, ū]]` with
`c = |u|²/|v|²`. Its determinant vanishes, and a row or column relation
puts `v` in `ℚu` or `ℚū`. The transcendence-degree bound for the
candidate corollary reuses the argument already written for the
period-aligned branch. Every number in play is algebraic over `ℚ[u]`,
because `ū = |u|²/u`.

For `e^{π²}` the matrix is `[[w, wz], [wz, wz²]]` with `w = iπ` and
`z = −iπ`, whose entries are `iπ`, `π²` and `−iπ³`. A rational relation
between its rows would make `z` rational. For `π log 2` the ratio of
the two numbers is `log 2/log 3`, which Gelfond–Schneider would force
to be rational, and `2^d = 3^n` has no solutions. For `2^π, 3^π, 5^π`
the one piece of real work is the `ℚ`-independence of `log 2`, `log 3`,
`log 5`. Clearing denominators and exponentiating gives
`2^A 3^B 5^C = 1`, and the 2-, 3- and 5-adic valuations
(`padicValRat.zpow`) force `A = B = C = 0`.

## What is not proved

No open node closed. The real half of (S), and (NT), are exactly as
open as before. The rational-line and axis theorems describe the
exceptional set of (S), which is empty if (S) is true. The candidate
corollary, like every exclusion in this mission, is vacuous if Diaz's
conjecture holds. The substantive results are the disjunction, the
removal of the imaginary half from the tree, and the three statements
about constants. Each of those is a disjunction. None of `e^{π²}`,
`π log 2` or `2^π` is proved transcendental on its own.

None of this is new mathematics. Each statement is a short consequence
of a classical theorem, and is possibly known.

## What remains open

The real half of (S): for real algebraic `γ ≠ 0`, is `e^{−iγ/π}`
transcendental? Then (NT), which is the conjecture. The imaginary half
also stays open, but Diaz no longer depends on it.

**Note (24 September, after reading the literature).** The structure of `S₀`
described here is Diaz's: J. Théor. Nombres Bordeaux 16 (2004), Théorèmes 4 and
5, at `v = −1/π`. See [Reading everything: attributions](2026-09-24-sweep.md).
