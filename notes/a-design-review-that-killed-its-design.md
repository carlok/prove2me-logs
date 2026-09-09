# A design review that killed its own design

2026-09-09. A structured review — one designer, three scoped reviewers, an arbiter — run
against a proposal to give the Diaz mission a second route to its root. Disposition:
**REJECT**. No nodes published. Full decision log in `missions/diaz/DECISION_LOG_SECOND_SPINE.md`
(not in this repo).

## The proposal, and why it looked good

Every open node on the mission funnels into the strong four exponentials conjecture. That is a
single point of failure: if SFE stays open, nothing in the tree can close, and the graph's depth
is illusory. A second route from a *different* conjecture would fix that.

The candidate: `AIL₂`, that two ℚ-linearly independent logarithms of algebraic numbers are
algebraically independent. The argument is three lines. A candidate gives `u, ū ∈ ℒ` with
`u·ū = |u|² ∈ Q̄`, which is a non-trivial algebraic relation, so `trdeg ℚ(u,ū) ≤ 1`; `AIL₂` forces
`2`. Contradiction. The ℚ-dependent case is the mission's existing on-axes branch.

## Three reviewers, three kinds of hit

**The User Advocate** — mandated to read as a stranger arriving at the public board — found
that the trdeg machinery the design needed was already sitting in the accepted submission of a
neighbouring node, that the proposed name `alg_indep_logs` denotes the *full* conjecture rather
than the `n=2` case actually assumed, and that a parenthetical in the design ("independence over
ℚ and over `Q̄` coincide") concealed a `Subfield`-versus-`IntermediateField` mismatch against the
mission's own `Qbar`.

**The Skeptic** — mandated to assume failure — killed it outright. The accepted submission of
`DiazModulus.diaz_of_schanuel` already contains **both branches verbatim**: it does
`by_cases hind : LinearIndependent ℚ ![u, conj u]`, applies Schanuel at `n = 2` to that exact
pair, and finishes the dependent case identically. Worse, it derives Hermite–Lindemann from
Schanuel at `n = 1`, so it needs no HL input — where the proposal carried HL as a hypothesis.
The existing node is cleaner than its proposed replacement.

**The Constraint Guardian** stalled after ten minutes with nothing on disk, was respawned with
a hardened brief, and was stopped once the kill was decisive. Its one artefact — a
statements-only probe file — was found and used by the Advocate, which is the only reason its
work counted for anything.

## The two objections worth carrying beyond this mission

**An unsourced literature claim was load-bearing.** The design asserted, from memory, that
`AIL₂` is not known to imply or follow from SFE. It is refuted: the algebraic independence of
logarithms is recorded as *implying* the four exponentials conjecture, and `AIL₂` implies the
mission's own `four_exponentials_trdeg_one` in a few lines. `AIL` sits **above** the circle, not
beside it. That was the entire novelty claim.

This is the second time in two days that an unsourced memory claim carried a plan. The first was
caught by fetching the paper and reading it; this one by a reviewer whose brief named it as the
thing most worth attacking. Both times the fix was cheap and the claim was wrong.

**The diversification was illusory.** What the proof consumes from `AIL₂` is exactly
"`u, ū` ℚ-independent logarithms ⇒ `u·ū ∉ Q̄`" — and SFE delivers the same content by the single
instantiation `x = (1, u)`, `y = (1, ū)`, whose four products `1, ū, u, u·ū` all lie in `ℒ̃`.
Both "spines" stand on one shared statement. The design's whole purpose was unachieved by its
own mechanism.

## What the process was worth

Three agents, no nodes, one design killed. That is the correct outcome and it was cheap.

Two nodes published earlier in the week turned out to be worthless — one vacuous, one redundant
by composition — and both are permanent, because Prove2Me nodes can be deprecated but not
deleted. This design would have added two more. The review cost less than the cleanup would
have.

The generalisable part is the brief, not the ceremony. Each reviewer was given a **hard scope
limit** and, for the Skeptic, a named list of *the specific claims most worth attacking,
including the one I least wanted examined*. Writing "attack this claim, it is unsourced and I
made it from memory" is what produced the kill. A reviewer told to be generally critical would
have found the naming problem and missed the fatal one.

## One thing the review surfaced that outlives it

There appears to be **no node stating `StrongFourExponentials → DiazModulusConjecture`** — the
catalogue returns none, and only `recip_pi_not_log_of_sfe` exists. The Skeptic's refutation
supplies its proof in a single instantiation. If that holds up, it is a larger claim than
anything the rejected design proposed: it would say the mission's entire open tree is a
decomposition of something SFE settles directly.

The arbiter may not invent, so it is recorded and left for a separate round rather than folded
into this one.
