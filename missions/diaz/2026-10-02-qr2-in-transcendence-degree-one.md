# Diaz's (Qr2) in transcendence degree one
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-02

Asked for half an hour of thought on a new result connecting the
development's pieces, the session found no important one. It found a small
unconditional classification, and the literature check then placed it: it
is the transcendence-degree-one case of a conjecture Diaz stated in 2007.

## What was proved

Let λ, μ be non-zero logarithms of algebraic numbers such that λ, λ̄, μ,
μ̄ generate a field of transcendence degree at most one. If λμ is real,
then both are real, or both are purely imaginary, or μ ∈ ℚλ̄. If λμ is
purely imaginary, one is real and the other purely imaginary.

In Diaz's own form, conjecture (Qr2) of his 2007 paper (p. 376): for such
logarithms ℓ₀, ℓ₁ off both axes, a real or purely imaginary quotient ℓ₁/ℓ₀
is rational. For a candidate u, that is u ≠ 0 with |u| and e^u algebraic,
the logarithms algebraic over ℚ(u) whose product with u is real are
exactly the rational multiples of ū, and no such product is purely
imaginary.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.log_mul_real_trichotomy_of_trdeg_one` | `33bca469-4dbf-41b5-ade5-c29df54cd0b5` | ACCEPTED |
| `DiazModulus.log_mul_imaginary_mixed_of_trdeg_one` | `f5946b27-bd72-4cda-b34d-bf55accefdd3` | ACCEPTED |
| `DiazModulus.diaz_2007_qr2_of_trdeg_one` | `db56b6c4-cdab-496e-9aa3-40f3899e46e6` | sketch, now Proved |
| `DiazModulus.candidate_log_mul_real_iff_rat_conj` | `63bbb69f-c091-429d-ae55-5c8a054c74a5` | sketch, now Proved |

## How

The matrix with rows (λ, λ̄) and (μ̄, μ) has logarithms of algebraic
numbers as entries, since the conjugate of e^z is e^{z̄}, and its
determinant λμ − λ̄μ̄ = 2i Im(λμ) vanishes when λμ is real. The four
exponentials theorem in transcendence degree one (Waldschmidt 1973,
Brownawell 1974), already a node of the mission, makes its rows or its
columns dependent over ℚ. Dependent rows give μ = qλ̄; dependent columns
put both factors on one axis. For a purely imaginary product the matrix
with rows (λ, λ̄) and (−μ̄, μ) does the same work. (Qr2) follows by taking
λ = ℓ̄₀ and μ = ℓ₁, since ℓ̄₀ℓ₁ = |ℓ₀|²·ℓ₁/ℓ₀. A candidate is on neither
axis by Hermite–Lindemann, and ū = |u|²/u keeps everything algebraic over
ℚ(u), so the transcendence degree is at most one.

Diaz proves (Qr2) from the four exponentials conjecture with the same
matrix (p. 377), and quotes the transcendence-degree-one theorem on p.
386, but he does not combine the two. The four proofs are 52 to 86 lines
each; the statements were written before the proofs and did not change.

## What is not proved

- Nothing here is new in substance. The literature check rates all of it
  immediate from Diaz 2007; only the transcendence-degree-one form was not
  found in the sources read.
- Under Schanuel's conjecture the hypothesis forces λ and μ onto one axis,
  so the classification describes configurations that are not known to be
  impossible, not configurations known to exist.
- The candidate statement is vacuous if Diaz's conjecture holds.
- It does not reach the open statement (S): for μ = iπ and a real
  algebraic γ, λ = γ/(iπ) is already purely imaginary, and the theorem
  says nothing.
- The other result of the half hour was not formalised: the strong five
  exponentials conjecture gives λμ ∉ Q̄ + ℒ, and with it Diaz's
  conjecture, (S) and e^{π²} at once. It is Waldschmidt's 1988 remark with
  a constant added, and the same conclusion is in print under the strong
  four exponentials conjecture (Variations, 2005, p. 341).

## Publication

The four statements went up at 10:30 and the two tops became milestones 98
and 99; the mission now has 211 members. The tops came back as sketches at
10:58, the two theorems on products were accepted at 11:14, and all four
nodes are Proved and in the mission.

## What remains open

(Qr2) itself, without the hypothesis on the transcendence degree, is still
a conjecture; Diaz's Corollary 6(2) proves it when ℓ₁/ℓ₀ lies in the
Q̄-span of 1 and the logarithms. The mission's two open leaves, the real
half of (S) and (NT), are unchanged.
