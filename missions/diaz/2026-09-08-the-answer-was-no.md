# The answer was no, and the no is a theorem

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

The task was "find the rational `c`". There isn't one, and now there is a machine-checked
proof that there cannot be.

## The setting

The period-aligned leaf split on whether `‖u‖² ∈ ℚ·β`, with `β = π(Im u + rπ)`. The
rational-multiple half closed earlier the same day onto
`DiazModulus.four_exponentials_trdeg_one`, using the matrix

```
[ u        ν      ]        det = u·conj u − ν·c·2πi = A + 2cβ
[ c·2πi    conj u ]
```

which vanishes exactly at `c = −A/(2β)`. On the free half that `c` is irrational, and the
entry `c·2πi` then fails to be a logarithm of an algebraic number: `exp(2πic)` is algebraic
**iff** `c` is rational, by Gelfond–Schneider. So the question was whether some *other*
matrix works.

## The answer

None does. Published as `DiazModulus.aligned_norm_free_no_rational_log_matrix`,
<https://prove2.me/theorems/931b8b88-3036-4006-9045-de1f1ebd4ecf>, Open under the hold rule
though provable today from local files.

Every element of the certified span `L₃ = span_ℚ{u, ū, 2πi}` can be written
`λ = p·Re u + q·β/x + s·x` with `p,q,s ∈ ℚ` and `x = πi`. Expand `det = 0` in that basis and
substitute the aligned quartic relation. The imaginary part gives `βG + π²H = 0`, hence
`G = H = 0`. The real part is a quadratic in `π²` whose middle coefficient is
`P·A + (2rP + J)·β = 0` with `P, J ∈ ℚ`. On the sibling half this is solvable with `P ≠ 0`;
on the free half `A/β ∉ ℚ` **forces `P = 0`**, and then every determinant and polarisation
form vanishes identically. So every element of the rational span of the three coefficient
matrices has rank ≤ 1, and a rational common kernel or common image line gives ℚ-dependent
rows or columns.

The four-exponentials hypothesis package is therefore *unsatisfiable* over the certified span.
Applying the same computation to every `2×2` minor extends this to any rank-≤1 `d×l` matrix.

Eleven results, `lake build` clean, zero `sorry`, `#print axioms` on all of them
`[propext, Classical.choice, Quot.sound]`. The published statement is *proved* from the core
rather than paraphrased, so what is on the board is the theorem.

Both early checks came back too. Clearing denominators does not help — the constraint is
ℚ-linear in `(A, β)`, not integral, so the degree of `A/β` is irrelevant and restoring it
always needs an algebraic irrational multiple of `2πi`. And the half is not vacuous: the
witness `wC` with `‖wC‖² = 16√2` was rebuilt and verified, then the no-go was instantiated at
it, so the theorem is provably non-empty.

## A correction to something we published

The description of the free node `1b43101e-b00e-4168-9769-ddd07242b0c6`, and §2.3 of
`LEAF_ALIGNED.md`, derived this same conclusion "monomial by monomial in
`1, t², t/π, tπ, π²`". That presumes those five are ℚ-linearly independent on the aligned
class. **They are not.** The aligned quartic relation

```
t²π² + r²π⁴ − (A + 2rβ)π² + β² = 0
```

is exactly a dependence among them — and it is the same relation that puts the class in
transcendence degree one, which is what made the *sibling* half closable. The two facts are
the same fact, used once correctly and once not.

The conclusion survives. The published derivation did not, and has been corrected in place on
the node with the reason recorded in its edit history. The valid argument needs only
`Transcendental ℚ π`, `Re u ≠ 0` and `β ≠ 0`.

Worth naming the pattern: this is the second time today a step went wrong by assuming
independence that the configuration itself denies. The first was choosing `π` as a
transcendence generator inside an algebra that does not contain it. Both times the object had
*less* freedom than the argument assumed, and both times the conclusion happened to survive.

## What the result does not claim

The agent kept the scope limits explicit, and they matter. The statement is exactly as strong
as its span: it says nothing about `Q̄`-coefficient combinations — that is the strong four
exponentials conjecture — and nothing about non-matrix routes. It closes one avenue
completely and leaves the leaf open.

One caveat carried forward unverified: the identification "six exponentials = the matrix rank
statement for `dl > d + l`" was written from memory, with no literature access in that run.
Nothing formalised depends on it, since the Lean covers `2×2` and the `d×l` extension is
prose. It should be checked before anyone quotes it.
