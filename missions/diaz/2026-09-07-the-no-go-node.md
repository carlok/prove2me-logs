# The no-go argument is now a theorem, for the part of it that is about complex numbers

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Node** — `DiazModulus.sixExponentials_cannot_refute_candidate`
  (<https://prove2.me/theorems/de25fa09-b094-4a91-a49a-1b0face79465>) — **Proved**
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

A note published earlier the same day claimed that no `2×3` six-exponentials template
can refute a candidate. The argument behind it was prose. This records the part of it
that is now machine-checked, and is equally explicit about the part that is not.

## What was proved

For `u : ℂ` and `V = span_Q̄ {1, u, conj u}`, three clauses in one theorem:

1. If `u` is a candidate, `V ≤ ℒ̃`.
2. If `u` is a candidate and Hermite–Lindemann holds, `dim_Q̄ V = 3`, and a `2×2`
   template fits inside `V`.
3. For **every** `u`, with no hypothesis: no `2×3` template fits inside `V`.

A *`2×n` template* is a pair of `Q̄`-linearly independent families with all `2n`
products `x i * y j` in `V`. Six exponentials is `n = 3`; four exponentials is `n = 2`.

## How

Clause 1 is what stops this being a fact about an arbitrary subspace: `1 ∈ ℒ̃`,
`u ∈ ℒ` by hypothesis, `conj u ∈ ℒ` because `exp(conj u) = conj(exp u)`, and
`c = u·conj u = |u|²` is algebraic. So `V` is a genuine space of `ℒ̃`-memberships and
the theorem speaks about the hypotheses the exponentials theorems consume.

Clause 3 is the no-go. Its proof is **not** the free-ring gcd-and-degree argument from
the note. Over `ℂ` it collapses to linear algebra. Independence of `x` gives `x 0 ≠ 0`
and `s = x 1 / x 0 ∉ Q̄`. Put `z j = x 0 * y j`; independence transfers, so `span z`
has dimension `n`, and when `dim V ≤ n` that forces `span z = V`. Then `s·V ⊆ V`,
because `s · z j = x 1 * y j ∈ V`. A non-zero finitely generated `Q̄`-submodule of `ℂ`
stable under multiplication by `s` makes `s` integral over `Q̄`
(`isIntegral_of_smul_mem_submodule`), hence algebraic over `ℚ`, hence in `Q̄` —
contradicting `s ∉ Q̄`.

At `n = 2` the step `span z = V` fails, since `2 < 3`. That is the entire reason the
strong four exponentials template survives while no six-exponentials one does. The
core lemma is stated for arbitrary `n` so the mechanism is visible: **the threshold is
the dimension of the certificate space and nothing else.**

Clause 2 is the sharpness check and sits deliberately in the same theorem. The `2×2`
template it exhibits — `x = ![1, conj u]`, `y = ![1, u]`, entries `1, u, conj u, c` —
is the one behind the mission's proved
`diaz_of_strongFourExponentials_and_hermite_lindemann`. Proving "permits the good
template" and "forbids the bad one" together makes the pair consistent by
construction rather than by assertion.

This also makes quantitative what was previously a qualitative remark: `ℒ̃` works
where `ℒ` does not because `1` and `Q̄` push `dim V` from 2 to 3.

## A correction to the statement that was proposed

The shape originally handed to the solver hypothesised `x 0 ≠ 0`. **That version is
false**: `x = (1,1)` with `y = (1, u, conj u)` puts all six products in `V` while `y`
stays independent. The hypothesis has to be `LinearIndependent Qbar x`, which is what
six exponentials requires anyway. The error was caught before publication.

## What is not proved

The general free-ring theorem in
`notes/six-exponentials-cannot-refute-a-candidate.md` is **still prose**. Every branch
of its proof has been re-read by hand with no error found, and hand-reading is not
verification.

The gap does not close by trying harder. The general version quantifies over a
certificate space containing a `T_b` for every other basis logarithm, so it is
infinite-dimensional and the dimension argument says nothing there. Forbidding `2×3`
templates with entries anywhere in `ℒ̃` **is the strong six exponentials conjecture**,
which is open. What is proved here is the `u`-generated fragment — the largest piece
that is a theorem about `ℂ` rather than about a class of proofs.

No novelty is claimed. Elementary linear algebra plus integrality; possibly folklore.

## What remains open

Formalising the free-ring theorem as pure commutative algebra — a statement about
`Q̄[X, T]` making no claim about `ℂ`. That would verify the note's argument without
extending its reach, and is a separate task.

And the conjecture, and the structural problem: `diaz_modulus_conjecture` still has an
empty subgraph.
