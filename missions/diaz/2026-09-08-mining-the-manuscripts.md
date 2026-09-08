# Fifty-eight theorems out of two manuscripts, and the graph that was missing under them

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

The mission's author keeps a corpus of LaTeX manuscripts on this conjecture. Nine agents
read two of them — `p21_diaz.tex` (62 numbered statements, 3206 lines) and `p20_diaz.tex`
(57, 3040) — formalised what was formalisable, and published it.

**`Diaz.*` went from 29 nodes to 87, all Proved.**

## What was published

| source | nodes |
|---|---|
| `p21` normal form (106–234) | 5 |
| `p21` rigidity (235–1014) | 11 |
| `p21` open boundary (1015–2128) | 13 |
| `p21` polar and conjugation-degree (2129–3060) | 7 |
| `p20` appendices A/C/D | 13 |
| legacy ports and `e^{π²}` | 5 |
| rational-subspace classification | 2 |
| transfer corollary | 2 |

## Three things that were deliberately not done, and then were

**Other people's theorems.** Four `p20` statements are Waldschmidt's or Roy's by the
manuscript's own admission, and were skipped. Porting a cited classical result with
attribution is legitimate — Mathlib carries Weierstrass — so they went up. But only Diaz
2007 is held locally, so the other three are published as **carried hypotheses**: named,
feeding a consequence, citation boundary inside the statement, and each says on its face
that the cited item was transcribed from `p20_diaz.tex` and not verified against the
original. Nothing unverified is asserted.

**Definition nodes.** Statements 51–54 and 57 were skipped rather than create permanent
`Logs_E` and `Λ_p` definitions. Both were authorised — and **neither was needed**. Checking
the abstraction route first showed every one of them touches its setting through a very
short list of properties: `Logs_E` only via `Logs_E ∩ Q̄ = {0}`, which becomes the
hypothesis `¬ IsAlgebraic ℚ u`; `Λ_p` only via "contains 1, closed under `+` and `Q̄·`";
`ℂ_p` only as a field. Six nodes, zero new definitions.

Sharpest instance: **statement 57's plane half never uses `σ(σx) = x`**, so the Galois
involution drops out entirely and `σu` becomes a free element.

**`e^{π²}`.** The manuscript's theorem *Non-real two-point fibres force `e^{π²}`
transcendental* was left unstated because it needs Diaz's own Corollaire 2 (P)(1) and the
augmented logarithm space `ãLogs`. Publishing Corollaire 2 as a legacy port unblocked it.

`ãLogs` turned out not to be the obstacle the earlier report recorded: as a `Submodule`
pinned by an equation it is a definition rather than a hypothesis blob, and it supplies the
last step's `Q̄`-scalar closure for free.

## What the `e^{π²}` node does and does not say

`Diaz.nonreal_two_point_fibre_pi_sq` concludes
`π² ∉ ãLogs ∧ Transcendental ℚ (exp (π²))` — under hypotheses that are all visible in the
statement:

- `hSSE`, Roy's strong six exponentials, carried and not proved;
- a non-real algebraic `α` with **two distinct** logarithms `u ≠ v`, both of algebraic
  modulus squared.

The second is not known to be satisfiable. **Nothing on this mission asserts transcendence
of `e^{π²}`.** Both conditions sit in the statement rather than in prose.

Corollaire 2 itself could not be a bare assertion, since the platform requires a Lean proof
and Roy's theorem is not in Mathlib. It is published as Diaz's own derivation: Roy's
Théorème 3(3) implies Corollaire 2 (P)(1).

Citation correction: Corollaire 2 is on **p. 381**, not p. 380 as `p21_diaz.tex` cites.
Checked against the local full text.

## The graph that was missing

The 74 nodes published today were flat — each proved independently, almost no edges. The
diagnosis on inspection: nearly every proof **re-derived inline what was already published
as its own node**. Six carried a 42 KB verbatim copy of the Lindemann–Weierstrass port that
`Diaz.transcendental_of_candidate` owns. A dozen carried private copies of published lemmas.

Twenty-two resubmissions, all ACCEPTED, no statement altered:

| | before | after |
|---|---:|---:|
| dependency edges among the 74 | 16 | 45 |
| nodes with a theorem-level parent | 11 | 33 |
| nodes with neither parent nor child | 57 | 22 |
| connected components | 59 | 32 |
| largest component | 15 | 27 |

`Diaz.transcendental_of_candidate` now sits in a 45-node, 92-edge reachable subgraph.

**Twenty-two nodes stay isolated, with reasons.** Four `Exp0_*` rpow computations, four 2×2
matrix identities, three one-`ring` identities, and eight genuinely independent statements.
A plane-norm node that would have linked `norm_mem_iff` to `four_nodes` was **declined** —
that is the manufactured-dependency failure, and a false edge in a public graph is worse
than an honest gap.

## What is not proved

No statement in either manuscript was found false or unprovable as written. That is roughly
120 statements checked across nine agents.

Nothing published today is new mathematics. It is the author's own work, plus four cited
results carried as hypotheses, formalised.

Three refinements came out **stronger** than the manuscripts: `Diaz.fibre_at_most_two` needs
neither `α` algebraic nor `α ≠ 0`; `Diaz.axis_triple_indep` drops two hypotheses;
`Diaz.no_holo_stab` drops non-degeneracy. And `Diaz.normalization_not_invariant` assumes
Hermite–Lindemann redundantly — the mission owns its contrapositive unconditionally.

Deliberate gaps, each stated on its node: statement 53's analytic tail (density on the
circle); the `φ(m) ≥ √(m/2)` step, which Mathlib cannot supply — `Data/Nat/Totient.lean`
has only upper bounds — so `Diaz.order_quantisation` stops at `π²/m²`.

## Corrections owed to the manuscripts

- **Theorem 2.5 does not need `lem:axis`.** Its proof splits on `dim S = 1` versus `2` and
  kills the first case by contradiction. Unnecessary: if `S = ℂ·M₀` with `M₀` rational and
  `N = cM₀` has no zero entry, the line case is subsumed and gives conclusion (i) directly.
- **Two proofs are heavier than needed.** *Homogeneous exhaustion* needs neither binary-form
  factorisation nor Gelfond–Schneider. *Determinantal descent* in dimension two needs no
  cone-density argument.
- **A reading hazard.** In *Real projection normal form*, `Q = (1/√2)!![1,i;1,−i]` has
  `QᵀQ = !![1,0;0,−1]`, not `I`. The claim is a congruence and is correct, but a reader
  assuming `Q` orthogonal will misread what follows.
- Statement 51(b)'s proof cites part (a) where it needs `Logs_E ∩ Q̄ = {0}` directly, and its
  "gives `|γ| = 1`" is unused.

## What remains open

Thm 2.5 needs Roy–Waldschmidt **Théorème 0.2** and nothing else deep — everything
downstream is now published, and Hermite–Lindemann is *not* on its critical path. Thm 3.9
needs **Théorème 7.1**, which 0.2 cannot substitute for, since `ρ/μ` is not known to be a
logarithm.

And the conjecture, whose two open leaves are untouched by any of this.
