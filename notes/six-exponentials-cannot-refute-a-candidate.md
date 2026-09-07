# Six exponentials cannot refute a Diaz candidate by one matrix, and there is a proof rather than a failed search

Worked out 2026-09-07, in the course of trying to decompose Diaz's modulus
conjecture. **This is a statement about a class of proofs, not about complex
numbers.** Read the limitations section before citing it; the honest summary is
"elementary, possibly folklore, not found in the three sources consulted".

## The question

A *candidate* is a hypothetical counterexample to Diaz's modulus conjecture: `u ≠ 0`
with `|u|` algebraic and `exp u` algebraic. The mission repeatedly asked whether the
six exponentials theorem can be arranged to kill one — pick two families `x` of size
2 and `y` of size 3 built from `u`, `ū`, `|u|`, `π`, `1`, check that all six products
`xᵢyⱼ` have algebraic exponentials, and derive a contradiction. Several attempts
failed. The question is whether they failed for want of cleverness.

## The model

Write `c = u·ū ∈ Q̄ˣ`. Everything a proof of this shape can know about a candidate:

- **(F1)** `ℒ̃` is a `Q̄`-subspace of `ℂ` containing `1` and every element of `ℒ`
- **(F2)** `u ∈ ℒ` and `ū ∈ ℒ`
- **(F3)** `u·ū = c ∈ Q̄ˣ`
- **(F4)** `ℒ` is a `ℚ`-subspace and, by Baker, `ℒ̃ = Q̄·1 ⊕ (Q̄ ⊗_ℚ ℒ)`

`u` and `ū` are `ℚ`-independent: `u/ū ∈ ℚ` would give `u² ∈ Q̄`, hence `u ∈ Q̄`,
contradicting Hermite–Lindemann. Extend `{u, ū}` to a `ℚ`-basis `B` of `ℒ`, put
`B' = B \ {u, ū}`, and form the free ring

```
A = Q̄[X, {T_b}_{b ∈ B'}],   R = A[X⁻¹],   φ : R → ℂ,  X ↦ u,  T_b ↦ b
```

so that `φ(cX⁻¹) = ū` by (F3). The certificate spaces are

```
W_strong = Q̄·1 ⊕ Q̄·X ⊕ Q̄·(cX⁻¹) ⊕ ⨁_b Q̄·T_b     (maps into ℒ̃)
W_ord    =        Q̄·X ⊕ Q̄·(cX⁻¹) ⊕ ⨁_b Q̄·T_b     (maps into Q̄ ⊗ ℒ)
```

`W_strong` is exactly what (F1)–(F4) certify as lying in `ℒ̃`. Note `1 ∉ W_ord` and
`c ∉ W_ord`: by Baker `1 ∉ Q̄ ⊗ ℒ`, and by Hermite–Lindemann no non-zero algebraic
number is a logarithm of an algebraic number.

## The theorem

Clearing denominators, `P_strong = X·W_strong = span_Q̄{1, X, X², X T_b}` and
`P_ord = X·W_ord = span_Q̄{1, X², X T_b}`, both inside the UFD `A`.

> Let `s ∈ Frac(A)` and let `Z` be a `Q̄`-subspace.
> 1. If `Z ⊆ P_strong`, `dim Z ≥ 3` and `s·Z ⊆ P_strong`, then `s ∈ Q̄`.
> 2. If `Z ⊆ P_ord`, `dim Z ≥ 2` and `s·Z ⊆ P_ord`, then `s ∈ Q̄`.

The proof is a gcd-and-degree argument. Write `s = f/g` in lowest terms; `g` divides
every `z ∈ Z`, and every element of either `P` has total degree at most 2. Degree ≥ 2
for `g` forces `dim Z ≤ 1`. Degree 0 forces `Z` into the degree-≤1 part, which is
`span{1, X}` for `P_strong` and `span{1}` for `P_ord`. Degree 1 splits on whether `g`
involves any `T_b`; the `T_b T_b'` coefficients of `gh` must vanish because no such
monomial appears in `P`, which collapses `h` and leaves only `g ∼ X` — and that case
recurs with `f` in place of `g`, where coprimality forbids `f ∼ X`.

## Why it answers the question

In a `2×3` template, `x₁ ≠ 0` and

```
z_j = x₁ y_j   (certified),      s = x₂/x₁ = (x₂ y₁)/(x₁ y₁).
```

The point that makes the model faithful: `s` is a **ratio of two certified entries**,
so it lies in `Frac(A)` even though the `xᵢ` individually need not be certified. The
`z_j` span a 3-dimensional space exactly when `y` is independent, and `s·z_j = x₂ y_j`
is certified. That is precisely the configuration the theorem forbids.

| theorem | template | verdict |
|---|---|---|
| strong six exponentials | 2×3, `dim Z = 3` | impossible — `s ∈ Q̄` contradicts `Q̄`-independence of `x` |
| ordinary six exponentials | 2×3, `dim Z = 3` | impossible — `s ∈ Q̄`, then Gelfond–Schneider upgrades a quotient of two non-zero logarithms to `s ∈ ℚ`, contradicting `ℚ`-independence |
| ordinary four exponentials | 2×2, `dim Z = 2` | impossible, same route |
| **strong four exponentials** | 2×2, `dim Z = 2` | **possible** — part 1 needs `dim Z ≥ 3`, and `x = (1, ū)`, `y = (1, u)` with entries `1, u, ū, c` exists |

The last row is what makes the model believable: it is the mission's already-proved
`diaz_of_strongFourExponentials_and_hermite_lindemann`. A wrong model would have
forbidden the template that demonstrably works. This one permits exactly that one and
forbids the rest.

It also supplies the mechanism: strong four exponentials succeeds precisely because
`ℒ̃` contains `1` and `Q̄`, giving the two entries `1` and `c` that `ℒ` cannot.

## What is not proved

**This is not a theorem about ℂ.** Transferring it would need `φ` injective, which is
Schanuel-strength — and Schanuel already proves the conjecture outright, so the
transfer is useless. The unconditional content is meta-mathematical: a derivation
using only (F1)–(F4) is valid in every model of those facts, including the free one,
and the free one contains no template.

It does **not** rule out multi-step arguments — using six exponentials to place
`u²/ū` outside `ℒ̃` and feeding that into something else — nor templates with extra
transcendence input, nor Waldschmidt's 2005 generalisation, which has a different
hypothesis shape and which Diaz explicitly flags as unexploited.

Diaz's own results are not counterexamples to it. Corollaire 5(2) and Théorème 7(1)
of his 2007 paper place **four** of six entries in `ℒ̃` and *conclude* about the other
two. A contradiction needs all six, and all six is what is impossible.

The proof is elementary commutative algebra. Its value is converting a search into a
theorem, not depth.

## Novelty, honestly

**No novelty is claimed.** Three sources were checked and none contains an
impossibility or no-go statement of any kind:

- Diaz, *Produits et quotients de combinaisons linéaires de logarithmes de nombres
  algébriques*, J. Théor. Nombres Bordeaux **19** (2007), 373–391 — read in full;
  every result is positive.
- Waldschmidt, *Variations on the Six Exponentials Theorem*, Algebra and Number
  Theory (Silver Jubilee Conference, Hyderabad), Hindustan Book Agency 2005, 338–355
  — full text searched; Theorems 2.1, 2.11, 3.1, 3.3 and Corollaries 2.2–2.14 are all
  positive.
- Waldschmidt, *Further Variations on the Six Exponentials Theorem*, Hardy-Ramanujan
  Journal **28** (2005), 1–9 — read; the main theorem gives sufficient conditions for
  one of three `2×2` determinants to lie outside `ℒ̃`. No limitations section.

Three papers is not a literature search. The accurate description is: elementary,
possibly folklore, not found in the sources consulted.

## As a formalisation target

Poor. It quantifies over Laurent polynomials indexed by a basis of `ℒ`. A finite
cut-down with `B' = {2πi}` — so `A = Q̄[X, T]` — captures the whole idea and would be
a manageable Lean file. Low priority; the prose is what has value here.
