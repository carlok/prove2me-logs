# The free-ring no-go is formalised, and the prose proof survived

- **Mission** — Diaz's modulus conjecture (context; this is not a published node)
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

## What was proved

With `A = K[X, T] = MvPolynomial (Fin 2) K`, `Pstrong = span_K {1, X, X², X·T}`,
`Pord = span_K {1, X², X·T}`, and `F` a fraction field of `A`:

```
theorem nogo_strong (s : F) {Z : Submodule K A}
    (hZP : Z ≤ Pstrong) (hdim : 3 ≤ Module.rank K Z)
    (hs : ∀ z ∈ Z, ∃ w ∈ Pstrong, s * algebraMap A F z = algebraMap A F w) :
    ∃ k : K, s = algebraMap A F (C k)

theorem nogo_ord   -- the same, with Pord and 2 ≤ Module.rank K Z
```

838 lines, clean `lake build`, zero `sorry`, axioms `[propext, Classical.choice,
Quot.sound]` on every reported result. Two sharpness results are proved alongside:
`sharp_strong` and `exists_two_dim_in_Pord`.

This is **pure commutative algebra**. It makes no claim about `ℂ`, about candidates, or
about Diaz's conjecture. Its purpose is that the public note
`notes/six-exponentials-cannot-refute-a-candidate.md` no longer rests on unchecked
prose for its central argument.

## How, and what the formalisation revealed

All four branches of the prose proof closed as written — `deg g ≥ 2`, `deg g = 0`,
`deg g = 1` off `X`, and the `g ∼ X` recursion on `f`. No error, no missing
hypothesis.

Two hypotheses turned out to be stronger than needed. `K` is an arbitrary field rather
than `Q̄`, with no characteristic assumption, and the dimension condition is a cardinal
`Module.rank` bound rather than finite dimensionality.

`MvPolynomial (Fin 2) K` was chosen over `Polynomial (Polynomial K)` because total
degree is native there and additive over a domain
(`totalDegree_mul_of_isDomain`); nested, the entire degree filtration would have been
hand-built.

Sharpness is now exhibited rather than asserted: `Z = span{X, X²}` with `s = 1/X`
meets every hypothesis at rank 2 with `s ∉ K`, so the threshold 3 cannot be lowered.
That witness is the free-ring shadow of the strong four exponentials template — the one
configuration the surrounding theory requires to survive.

The full account of what else the exercise turned up — a coefficient valid only off the
diagonal, an appeal to symmetry that was really a shared lemma, an unfinished linear
solve — is in `notes/formalising-a-prose-proof.md`.

## What is not proved

**One step is verified in shape rather than in generality.** With two or more `T_b` and
some `γ_{b₀} ≠ 0`, killing `h_b` for another `b` with `γ_b = 0` uses the off-diagonal
relation `γ_{b₀} h_b + γ_b h_{b₀} = γ_{b₀} h_b = 0`. A ring with a single `T` has no
mixed monomials, so that instance does not arise in the cut-down. It has been
re-derived by hand and is correct; it is not formalised. Everything else in the
argument is independent of how many `T_b` there are.

**Nothing here transfers to `ℂ`.** That would need the evaluation map to be injective,
which is Schanuel-strength — and Schanuel already settles the conjecture, so the
transfer is worthless. The unconditional reading stays meta-mathematical.

Not published. As a platform node it would be an orphan lemma about `MvPolynomial`,
connected to no mission. Its value is verification, and that value does not depend on
publication.

## What remains open

The single unformalised step above, which would need an indexed family rather than one
`T`. And the conjecture.
