# What the reading found, formalised

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-24

The afternoon's reading of Diaz, Roy and Waldschmidt left a list of statements
worth porting. Carlo picked four of them. His view is that formalising their
published work and making it public has value of its own, not only new
mathematics. Twelve nodes, all Proved, all mirrored.

## What was proved

| node | what it is | inputs |
|---|---|---|
| `exp_abs_transcendental_of_conj_algebraic` | Diaz 1997, Prop. 2 = Roy–Waldschmidt 1997, Cor. 7.4 | four exponentials in trdeg one |
| `exp_abs_log_two_add_i_pi_transcendental` | Roy–Waldschmidt's example, 1997, p. 792 | the same |
| `log_pair_square_ratio_transcendental` | Waldschmidt, LN 402, p. 202 | `geometric_triple_not_logs` |
| `log_two_pi_dependent_forces_transcendence` | its case `log 2`, `iπ` | the same |
| `candidate_norm_div_log_not_log` | new coupling | four exponentials in trdeg one |
| `candidate_norm_recip_pi_not_log` | new coupling | the same |
| `diaz_of_strong_five_exponentials` | Waldschmidt 1988, p. 379 | Hermite–Lindemann |
| `recip_pi_not_log_of_strong_five_exponentials` | the same, for (S) | Hermite–Lindemann |
| `diaz_of_sharp_four_exponentials` | Waldschmidt 2005 | Hermite–Lindemann |
| `recip_pi_not_log_of_sharp_four_exponentials` | the same, for (S) | Hermite–Lindemann |
| `diaz_of_two_by_two_determinant_conjecture` | Waldschmidt 2005, Conj. 1.6 | Hermite–Lindemann |
| `recip_pi_not_log_of_two_by_two_determinant_conjecture` | the same, for (S) | Hermite–Lindemann |

**The `e^{|λ|}` companion.** For a non-real logarithm `λ` with `λ̄` algebraic
over `ℚ[λ]`, `e^{|λ|}` is transcendental. The matrix is `[[|λ|, λ̄], [λ, |λ|]]`,
of determinant `|λ|² − λλ̄ = 0`. A rational row or column relation would make `λ`
real. At `λ = iπ` it gives `e^π`, as a sanity check.
`Diaz.log_modulus_forces_independence` had the same content, but with the four
exponentials theorem as a hypothesis; this version is unconditional.

**Waldschmidt's remark.** Two `ℚ`-independent logarithms are either
algebraically independent, or `exp(ℓ₁²/ℓ₂)` is transcendental. Both triples
`ℓ₂, ℓ₁, ℓ₁²/ℓ₂` and `ℓ₁, ℓ₂, ℓ₂²/ℓ₁` are geometric progressions, so
`geometric_triple_not_logs` does the work twice. At `log 2`, `iπ` this
strengthens `log_two_diaz_or_transcendental`: the hypothesis drops from
"`√((log 2)² + π²)` is algebraic" to "`log 2` and `π` are algebraically
dependent".

**Weaker conjectures.** The mission's ceiling was the strong four exponentials
conjecture. Three other published conjectures reach the same place, each by
the same one-line instantiation:

- Waldschmidt's strong five exponentials conjecture (1988), which he calls
  weaker than the strong four exponentials conjecture;
- the sharp four exponentials conjecture;
- his 2×2 determinant conjecture (2005), applied to `H(u, |u|)`.

Each gives Diaz's conjecture and (S).

**The couplings.** For a candidate `u` and a logarithm `x` algebraic over `ℚ(u)`
outside `ℚu ∪ ℚū`, `e^{|u|²/x}` is transcendental. That generalises
`candidate_harmonic_not_log`. The same matrix with `x = iπ` shows that the real
half of (S) holds at `γ = |u|²` for every candidate algebraic over `ℚ(π)`. The
reading found neither in the literature.

## How

One helper carried the batch. Any `ℚ`-subalgebra of `ℂ` inside the algebraic
closure of `ℚ[x]` has transcendence degree at most one: map it into that closure
with `trdeg_le_of_injective`. The older template needed `x` to lie in the
subalgebra, which forced awkward exchange arguments. With the helper, every
transcendence-degree hypothesis becomes "each entry is algebraic over `ℚ[x]`",
checked one entry at a time.

The proofs were written from a small generator so the helpers stay identical
across files. They built on v4.33.1 against the local stubs, and on v4.34.0
against the mirror's real proofs before anything was published. Each depends on
`propext`, `Classical.choice` and `Quot.sound` only. Statements first, proofs
after, twelve of each, no retries.

## Also

- The note's row checker queried `q=Diaz&limit=200` without paging. With 244
  nodes, one proved result fell off the first page and showed as missing. It now
  walks the offset.
- Note v1.7 adds Appendix A rows for the statements it already made: the
  companion, Waldschmidt's remark, the 2×2 conjecture, and item (2) of "What
  would have to be proved". The couplings and the sharp four exponentials
  conjecture stay out of the note; they are in the library.

## What remains open

Unchanged: the real half of (S), and (NT), which is the conjecture itself. The
new nodes constrain counterexamples and lower the ceiling. None closes a leaf.
