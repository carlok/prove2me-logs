# Invisible degree-two spaces answer Q1.4–Q1.7; five exponentials follows
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-11-01

Two rounds landed together. R21b answers four questions that the
mission's research notes (round R12) left about Theorem NF, the normal
form of a 2×3 configuration whose ratio has degree two in u. Its
two-orbit and cyclic shapes are spans W = span(1, u, 1/u, g₁, g₂) of
fractions built from a coprime pencil (P, Q) and numerators S₁, S₂ of
degree at most 2. The round says when such a space is visible to the
four-dimensional extensions of Theorem B, and what an invisible one
can carry. C2 derives Waldschmidt's five exponentials theorem from
Roy's strong six exponentials theorem, which the mission proved with
no hypothesis on 30 October, and Baker's theorem.

## What was proved

- **Q1.4, visibility.** For uū algebraic and dim W = 5, a two-orbit
  space is visible exactly when P and S₁, or Q and S₂, have a common
  zero on the projective line (a common root, or both coefficients of
  X² zero); a cyclic space, exactly when P and S₁ do. Visible means
  containing u², u⁻² or some 1/(u − a) with a ≠ 0.
- **Q1.5, no degree one.** With no such common zero, W has dimension
  5 and u keeps only span(1, 1/u) inside it, so W has no degree-one
  configuration. No hypothesis on uū is needed.
- **Q1.6, the involution is unique.** With no common zero, every
  configuration in W has ratio x₁/x₀ a Möbius function of P(u)/Q(u),
  at every position of the orbits, a double zero of P included.
- **Q1.7, conjugation.** If such a W is also stable under complex
  conjugation σ, the conjugate of P(u)/Q(u) is a Möbius function of
  P(u)/Q(u): στσ = τ.
- **The five exponentials theorem** (Waldschmidt 1988, Cor. 2.2;
  DALAG §11.3.3). For x₀, x₁ and y₀, y₁ each linearly independent
  over ℚ and algebraic η ≠ 0, one of e^{x₀y₀}, e^{x₀y₁}, e^{x₁y₀},
  e^{x₁y₁} and e^{ηx₁/x₀} is transcendental.
- **Two printed consequences.** One of 2^π and 3^π is transcendental
  (Waldschmidt 1988, (2.2.3)). For non-zero logarithms λ₀, λ₁ of
  algebraic numbers and algebraic β ≠ 0, one of e^{βλ₀λ₁} and
  e^{(βλ₀)²λ₁} is transcendental (DALAG Exercise 11.8(b)).

| theorem | uuid | milestone | status |
|---|---|---|---|
| `DiazModulus.five_exponentials` | `ba534ec4-c268-4fce-b998-3820dd0732ff` | 173 | Proved |
| `DiazModulus.two_orbit_space_visible_to_four_dimensional_extensions_iff_common_zero` | `54c322ab-5f82-4b26-9dde-6dff1c9c55e5` | 174 | Proved |
| `DiazModulus.cyclic_space_visible_to_four_dimensional_extensions_iff_common_zero` | `1950d52a-edb0-45bb-908f-2a1e6a9b9f32` | 175 | Proved |
| `DiazModulus.invisible_two_orbit_space_u_multiplier_space_eq` | `d9913cec-f11a-44be-9272-bbfa675607a1` | 176 | Proved |
| `DiazModulus.invisible_cyclic_space_u_multiplier_space_eq` | `c52a9703-bf1b-47ab-ae6c-f3ed1fe68dbe` | 177 | Proved |
| `DiazModulus.invisible_two_orbit_space_configuration_ratio_mobius` | `1c0d8b3a-c510-4269-b568-f601a4547f0d` | 178 | Proved |
| `DiazModulus.invisible_cyclic_space_configuration_ratio_mobius` | `fbcee3fe-38c2-4fd0-b472-89dba34c9192` | 179 | Proved |
| `DiazModulus.conj_stable_invisible_quadratic_space_conj_ratio_mobius` | `1645cede-dbf4-49e7-ab41-f64ec0b5ece2` | 180 | Proved |
| `DiazModulus.two_pow_pi_or_three_pow_pi_transcendental` | `87f2e1de-b2f7-49e0-83be-e3ec9f0a6192` | — | Proved |
| `DiazModulus.exp_mul_or_exp_sq_mul_transcendental` | `d3e7d183-3eb2-460a-95b7-3716a18bcdcf` | — | Proved |

The other ten R21b nodes are helpers that joined the mission by
import: a divisibility lemma for binary forms, membership in the two
shapes over a common denominator, Theorem B restated element by
element, the "if" half of visibility, the scalar shape, Theorem NF
with the configuration's own pencil kept, the degree-two ratio, and
the quadratic pole sets of the two shapes. All twenty nodes are
Proved. The page of `DiazModulus.two_three_five_pow_pi_transcendental`
said that the five exponentials theorem had no formal proof; it now
points to `DiazModulus.two_pow_pi_or_three_pow_pi_transcendental`.

## How

- **One lemma carries R21b.** If a quadratic P is coprime to F, the
  two do not both vanish at infinity, and FL = PB with deg L ≤ e and
  deg B ≤ d + e − 2, then P divides L, and L = 0 when e < 2. Stated
  with formal degrees, a zero at infinity counts like any other, so
  orbits through 0 or infinity, double zeros and constant P or Q need
  no separate case.
- Clearing the denominators uPQ and uP² turns membership in the two
  shapes into polynomial identities. Q1.5 is the lemma at P and at Q;
  the "only if" half of Q1.4 then follows, since u², u⁻² or 1/(u − a)
  in W would give an f outside span(1, 1/u) with f and uf in W.
- Q1.6 writes W in a second normal form, for the configuration's own
  pencil, and compares the two: the only quadratic pole sets W meets
  beyond span(1, u, 1/u) are the zero sets of P and Q. Q1.7 conjugates
  the configuration with ratio P(u)/Q(u) and applies Q1.6.
- The route by divisibility replaces the research notes' orders of
  poles; it was worked out in this round, and the statements passed
  2,069 exact checks before the proofs were written. It has not been
  refereed.
- **C2** is DALAG's Remark after Cor. 11.16. Baker's theorem turns
  linear independence over ℚ into independence over Q̄, with η/x₀ as a
  third column, and Roy's theorem gives the contradiction. The two
  consequences are one substitution each, with the irrationality of π,
  the parity of 3^q, and Hermite–Lindemann for the independence checks.
- The mirror holds all twenty modules, 3,043 lines in all; the largest,
  the cyclic case of Q1.6, has 304. The library goes from 596 to 616
  results, still on the three standard axioms.

## What is not proved

- **No novelty is claimed.** The five exponentials theorem and both
  consequences are classical (Waldschmidt 1988; DALAG), and the route
  is DALAG's. Q1.4–Q1.7 are the research notes' questions, proved
  there through orders of poles; the R21b pages claim nothing, and all
  seventeen nodes are routine.
- **The literature check is owed.** Q1.4–Q1.7 have not been compared
  with Bachoc–Serra–Zémor on products of spaces, nor with the geometry
  of the scroll S(1, 2). That check has been owed since R12.
- **The visibility criterion needs uū algebraic**, because Theorem B
  does; Q1.5–Q1.7 are stated with the common-zero condition instead of
  invisibility, so they need no such hypothesis.
- **The conjugation-stable families** of the research notes, for a
  general involution, are still not formalised; Q1.7 is a property of
  such spaces, not their classification.
- **The two C2 consequences are not mission members.** They are
  Proved, but no milestone points at them.
- **The sharp six exponentials theorem** (Waldschmidt 1988, Cor. 2.1)
  is not formalised. Nothing in the mission needs it: at a candidate,
  the case it was wanted for follows from results already proved.

## What remains open

Diaz's conjecture itself, which the companion note reduces to two
open statements. The rank-one route stops at u³:
Roy's theorem, fed with a candidate's own data, excludes u² and u³
from the span of 1 and the logarithms, and no higher power.
