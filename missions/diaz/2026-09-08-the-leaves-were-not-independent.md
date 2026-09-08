# The two leaves were not independent, and the graph said otherwise for a day

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## The correction

The mission displayed two open leaves as if they were independent halves of the remaining
work. They were not. **`diaz_of_exp_not_real_off_axes` is equivalent to the whole
conjecture and implies the other leaf.**

Machine-checked, zero `sorry`, axioms `[propext, Classical.choice, Quot.sound]`:

- `realGeneric_of_offAxes : DiazOffAxes → DiazRealGeneric`
- `diaz_of_offAxes : HermiteLindemann → Transcendental ℚ π → DiazOffAxes →
  DiazModulusConjecture`

Both inputs are Proved mission nodes, taken as explicit hypotheses so nothing is assumed
silently.

**Why.** Candidacy is invariant under scaling by non-zero rationals, and rational scaling
moves `Im u` *across* `π·ℤ`. An off-axes `u` with `Im u = qπ` scales by `den q` onto a
point of the real-generic leaf; a point of that leaf divides by `|n|+1` back into the
off-axes rational-angle region. So the rational-angle half of the off-axes leaf **is** the
real-generic leaf, and the off-axes leaf — one hypothesis fewer — implies it.

## The repair

`DiazModulus.diaz_of_exp_not_real_irrational_angle`
(<https://prove2.me/theorems/c30e6b12-498c-4137-8c95-f77c4584b010>) published, and the
reduction `off-axes ⟸ real-generic ∧ irrational-angle` submitted and SKETCH_ACCEPTED. The
frontier now shows two leaves over genuinely disjoint regions: `Im u ∈ πℚ` and
`Im u ∉ πℚ`, with no scaling between them.

The dividing line, off the imaginary axis: `Im u ∈ πℚ` ⟺ `(u, conj u, 2πi)` is
`ℚ`-dependent ⟺ `exp u / |exp u|` is a root of unity.

Smallest concrete open case of the residual: **is `|Log(2+i)|` algebraic?** Note `1+i` is
*not* in it — argument `π/4`, so scaling by 4 gives `Log(−4)`, a real-branch point.

## Two corrections to what was written on the parent node

It claimed no parametrisation of off-axes counterexamples exists. One does:
`u = Log α + 2πin` with `α` algebraic, non-real, `|α| ≠ 1` — the same shape as the real
branch. And it called that node "the larger of the two leaves", which understates it: it
was the whole problem.

## Graph repair

Two of the four orphaned Proved nodes now have honest consumers, so they are in the
subgraph rather than beside it:

- `candidate_one_self_conj_linearIndependent` — on the real axis `conj u = u`, so
  `![1, u, conj u]` repeats an entry and cannot be independent. **No candidate is real.**
- `candidate_exp_angularTriple_transcendental` — on the imaginary axis `conj u = −u`, so
  `u²/conj u = −u` and the node gives transcendence of `(exp u)⁻¹`, which a candidate
  contradicts. **No candidate is purely imaginary.**

Both submitted as alternative reductions of nodes that already had one. Each dependency is
genuine: dropping the import fails with `Unknown identifier` at the point of use.

**Two remain orphaned, correctly.** `diaz_iff_no_candidate` is definitional bookkeeping —
every reduction builds `IsCandidate u := ⟨hu, hmod, halg⟩` inline without citing it.
`sixExponentials_cannot_refute_candidate` may be permanently unwireable, and the reason is
structural: clause (3) is a *no-go*, and a no-go proves no transcendence, so nothing in a
transcendence tree can consume it. Its natural consumer is conditional on an open
conjecture and can never be a child of the unconditional root. A repair for it was built
and deliberately not submitted — reaching for it mainly to create an edge would be the
manufactured dependency the procedure forbids.

## Prior art, which is the mission author's own

While this was being worked out, the mission author pointed at a note of his predating the
mission. It contains the general form of what several agents had been rediscovering
piecemeal.

Its main theorem: for any candidate `u` there is a ring homomorphism `Φ : ℂ → ℂ` fixing
`Q̄` pointwise, sending `u` to an *ordinary* point `t = r·e^i` of the same circle, and
commuting with conjugation on `Q̄(u)`. Its corollary: for `M` with entries in `Q̄(u)` and
vectors `w, v` over `Q̄`,

```
wᵀ M v = 0   ⟺   wᵀ Φ(M) v = 0
```

so **no vanishing statement with algebraic coefficients distinguishes a candidate from an
ordinary point of the circle.**

That is a no-go of the same kind as this mission's `sixExponentials_cannot_refute_candidate`
and the free-ring theorem behind it, and it is more general in scope — it quantifies over
all such vanishing statements rather than over `2×n` templates in one certificate space.
Whether the six-exponentials no-go is formally a corollary of it is a question worth
settling, not a claim made here.

The observation that the difficulty lies on effectively complex `u` — neither real nor
purely imaginary — was also already in those notes. The nodes `Diaz.exists_transcendental_on_circle`,
`Diaz.candidate_indistinguishable` and `Diaz.transcendental_of_candidate` are its
formalisation.

## What is not proved

Both leaves. Two agents spent full sessions on them and closed neither, which was the
expected outcome.

The obstruction has a name now. Baker's theorem settles degree-1 relations between two
logarithms, which is why every sibling case closed. The real-generic leaf is a **degree-2**
relation — a `Q̄`-linear combination of two products — and every available tool constrains a
single product. As Waldschmidt puts it, it is not yet known whether two algebraically
independent logarithms of algebraic numbers exist.

Specific dead ends, checked and recorded so nobody repeats them: Diaz 2004 Théorème 2 has
no valid instantiation on a candidate, its conjugation hypothesis contradicting its own
`Q̄`-freeness hypothesis; Théorème 3 applies but yields `u² ∉ ℒ̃` and can never yield
`u·conj u ∉ ℒ̃`; Waldschmidt 2005 Theorem 1.2 needs column rank ≥ 3 while certifying all
three determinants forces rank ≤ 2, which closes a gap the earlier no-go note had left
open; Roy's half-structural-rank theorem is satisfied by the candidate matrix with
equality.

Also recorded: the reduction "leaf ⟸ algebraic independence of logarithms", which looked
like the best new edge available, **is already in Diaz 2004 §5.1**. Not new.

One practical caution: `pdftotext` on the Diaz 2004 scan reverses the hypothesis of
Théorème 3. Statements there were read off rendered page images instead.

## What remains open

Both leaves, and the honest assessment that closing either needs a theorem sensitive to
`2πi` as a distinguished element rather than an anonymous basis vector of `ℒ` — which
nothing available provides.
