# Roy–Waldschmidt 1995, checked against the paper rather than the manuscript

2026-09-08. `Diaz.four_exp_trdeg_one` carried a warning in its own description: *"Neither
the statement nor its attribution has been verified against the original; both were
transcribed from `p20_diaz.tex`."* An agent then found that one of the aligned leaf's two
children looks closable from that node, which made the warning load-bearing. So the paper
was fetched and read.

**Source now held**: `missions/diaz/sources/roy-waldschmidt-1995-quadratic-relations.pdf`,
from Waldschmidt's own publication page. D. Roy and M. Waldschmidt, *Quadratic relations
between logarithms of algebraic numbers*, Proc. Japan Acad. Ser. A **71** (1995), 151–153.
Three pages, matching the cited range.

## What the paper says

> **Theorem 1.** Let `x₁` and `x₂` be two complex numbers which are linearly independent
> over ℚ, and similarly let `y₁`, `y₂` be two linearly independent complex numbers. Assume
> that the field `ℚ(x₁, x₂, y₁, y₂)` has transcendence degree 1 over ℚ. Then one at least of
> the four numbers `e^{x₁y₁}`, `e^{x₁y₂}`, `e^{x₂y₁}`, `e^{x₂y₂}` is transcendental.
>
> For a proof of this result, we refer to [1] Cor. 7 and [6] Cor. 4.

with, in the bibliography, `[1]` Brownawell, *The algebraic independence of certain numbers
related to the exponential function*, J. Number Th. **6** (1974), 22–31, and `[6]`
Waldschmidt, *Solution du huitième problème de Schneider*, J. Number Th. **5** (1973),
191–202. The paper opens by saying the four exponentials conjecture "has been solved only in
one special case, namely when the transcendence degree of the field which is spanned by the
four logarithms is 1", and later: "Theorem 1 is the special case of Theorem 2 when `P` is
`X₁X₄ − X₂X₃` with `n = 4`."

## Verdict on the manuscript's remark

`p20_diaz.tex`'s *Position in the literature* remark says the corollary is Theorem 1 of the
1995 announcement, attributed there to Brownawell Cor. 7 and Waldschmidt Cor. 4, and that
the note observes Theorem 1 is the specialization at `P = X₁X₄ − X₂X₃`, `n = 4`.

**All of that is correct**, sentence by sentence, against the paper. The transcription into
the node is faithful too. One naming slip: the manuscript calls the generalization
"Théorème 0.2"; in this note it is **Theorem 2**. `Théorème 0.2` is the numbering of the
Ann. Sci. ENS **30** (1997) paper, a different item in the same bibliography. The
mathematics is the same; the label is from the other paper.

## Two gaps the check exposes

**Transcendence degree `≤ 1` versus `= 1`.** Roy–Waldschmidt say *degree 1*. The node says
`≤ 1`. At `K = Q̄` the degree-0 slice is vacuous — all four `λᵢⱼ` algebraic and non-zero with
`exp λᵢⱼ` algebraic contradicts Hermite–Lindemann, which this mission carries Proved as
`DiazModulus.hermite_lindemann_holds`. So at `Q̄` the gap closes on this board. Over a
general subfield it does not.

**The node is stated over an arbitrary `K : Subfield ℂ`.** The paper is about `Q̄` only. For
large `K` the hypothesis `exp λ ∈ K` is far weaker and nothing in the source reaches it. The
node is more general than what it cites, and the extra generality is unsupported.

## The finding that matters

**`Diaz.four_exp_trdeg_one` carries `hMaster` that it does not need.** Its conclusion, at
`K = Q̄`, *is* Roy–Waldschmidt Theorem 1 — proved by Waldschmidt in 1973 and Brownawell in
1974. A theorem, not a conjecture. The node was conditioned on a carried dichotomy because
nobody held the source; we hold it now.

So the aligned child
`DiazModulus.diaz_of_exp_not_real_irrational_angle_period_aligned_norm_rat_mult`
(`561efd5c-2eb5-4258-a55b-a7c035576bac`) is closable, and the clean route is to publish
Roy–Waldschmidt Theorem 1 at `K = Q̄` as an attributed legacy node — which the mission's own
policy now permits, since the policy's test is whether the source is held, and it is.

## Follow-through, same day

The verification changed the graph. `DiazModulus.four_exponentials_trdeg_one`
(`2c0f35ea-b824-4ce3-a701-01b48dc27a97`) was published as the attributed legacy port — the
statement at `K = Q̄`, unconditional, with `source` pointing at Waldschmidt's own copy rather
than a paywalled DOI, and the body naming Roy–Waldschmidt for the statement and Brownawell
1974 / Waldschmidt 1973 for the proof, as the paper itself does.

`..._period_aligned_norm_rat_mult` then reduced to it: submission
`e9a7f7d5-d00b-4272-9fac-b9da64be5dce`, `SKETCH_ACCEPTED`, two-hop edge present. The child no
longer depends on a conjecture carried as `hMaster`. It depends on a 1973/74 theorem whose
source is on disk. It is still Open, and that is correct — nobody has formalised Brownawell's
or Waldschmidt's argument, and the platform's `Proved` means a Lean proof.

**A correction to the brief that sent the agent there.** The brief said to take the
transcendence basis as `{π}`. That cannot work: the statement's algebra is
`Algebra.adjoin ℚ {l₁₁,l₁₂,l₂₁,l₂₂}`, and `π` need not lie in it — the four entries reach `π`
only through `πi` and through `θ = β/π − rπ`. The generator that works is `x = πi = l₃/(2c)`,
which is in the algebra because `c` is rational and non-zero. Nothing is lost: `π² = −x²`, and
the quartic relation is even in `π`.

The same slip is in `LEAF_ALIGNED.md` §2.4 and in the child's own description, both of which
say "`t` is algebraic over `Q̄(π)`, so trdeg = 1". The formal object is a `ℚ`-algebra that does
not contain `π`.

No Mathlib gap: `Algebra.IsAlgebraic.trdeg_le_cardinalMk` at a singleton was enough, once the
generator was right. The bridge lemma written for it, `trdeg_le_one_of_adjoin_singleton`,
should be reusable for any future trdeg-one node here.

## The next gap, now isolated

The trdeg-one certificate uses only the **aligned** hypothesis, not the rational-multiple one,
so it is available on the free sibling `..._period_aligned_norm_free`
(`1b43101e-b00e-4168-9769-ddd07242b0c6`) too. What that half lacks is a **rational** `c`
making the determinant vanish. That is the whole remaining gap on it, stated exactly.
