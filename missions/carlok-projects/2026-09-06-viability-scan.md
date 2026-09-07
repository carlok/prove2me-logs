# Four of five candidate repositories build unchanged on the platform

- **Mission** — none; a viability scan of five existing Lean
  repositories as candidate mission proposals
- **Environment** — the platform default, Mathlib `0df444a`
  (Lean v4.33.1)
- **Date** — 2026-09-06

This is a survey, not a result. The intended pipeline is to publish
each of five of the account owner's own Lean projects on Prove2Me as a
fully-Proved dependency graph, then set a mission on top of it. Phase 0
of that pipeline asks two questions per repository and nothing else:
does it build on the platform's default environment, and are its
declarations axiom-clean. Each project was re-pinned to the platform
environment in a scratch copy and built. The owner's repositories were
not modified.

## What was proved

Nothing mathematical. What was established is that all five projects
are viable as upload candidates.

| project | lines | files | builds | drift | axioms |
|---|---|---|---|---|---|
| `moebius-transcendental-lean` | 693 | 5 | unchanged | none | clean |
| `diaz-modulus-lean` | 1526 | 13 | unchanged | none | clean |
| `curve-symmetry-lean` | 3779 | 35 | 3 fixes | below | clean |
| `erdos-straus-offset-lean` | 932 | 1 | unchanged | none | clean |
| `magma-1518-obstruction-lean` | 1608 | 15 | unchanged | none | clean |

"Clean" is the Phase 0 gate and means something specific: every
published declaration reports exactly
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx`. Two
repositories do better. In `erdos-straus-offset-lean`, `es_polynomial`
depends on no axioms at all. In `magma-1518-obstruction-lean`,
`OneGenerated1518.l359`, `FamilyF5.law1518` and `FamilyF5.not47`
depend on no axioms, and `L2.cert_47` and `H2.homotopy` on `propext`
alone.

The original pins differ from the platform's. The first three projects
and `erdos-straus-offset-lean` were on Mathlib `81a5d257`
(Lean v4.32.1); `magma-1518-obstruction-lean` uses core Lean only, no
Mathlib, and was already on Lean v4.33.0.

## How

Only `curve-symmetry-lean` drifted. Three fixes, saved as
`curve-symmetry-drift.patch`:

1. `Polynomial.finite_setOf_isRoot` was renamed to
   `Polynomial.finite_setOfPred_isRoot`. One site,
   `lean/Elimination.lean`.
2. A style lint, `letI` → `let`, in `lean/Elimination.lean` and
   `lean/RotationGroup.lean`. This only bites because the lakefile sets
   `moreLeanArgs = ["-DwarningAsError=true"]`; on a default build it
   would be a warning.
3. The real one. Two `linear_combination` calls stopped closing,
   because `ring` now treats `star z` and `(starRingEnd ℂ) z` as
   *distinct atoms*. The fix is to run `simp only [Complex.star_def]`
   on the hypotheses and the goal first, which normalizes both spellings
   to `starRingEnd`. Sites: `lean/FamilyRealLocus.lean`, inside `hvb`,
   and `lean/EqualityForm.lean`, inside `he`.

All three are Lean v4.33 compatibility fixes and are worth upstreaming
to the repositories on their own merits, independently of Prove2Me.

Two of the five needed structural notes rather than fixes.

`erdos-straus-offset-lean`: the buildable project is the `lean/`
subdirectory, an old-style `lakefile.lean` pinned to Mathlib v4.32.1.
`mathlib_draft/ErdosStraus.lean` is a separate 742-line upstreaming
draft and is *not* part of the lake build. `ESTheorem.lean` holds 33
declarations.

`magma-1518-obstruction-lean`: core Lean, no Mathlib, with three
libraries as `defaultTargets`. Only `Magma1518` is proof content, with
roots `OneGenerated1518`, `FamilyF5`, `FamilyF13`, `L2Cert` and
`H2Cert`. `Challenge.lean` holds all ten of its sorries deliberately
and `Solution.lean` is the Palomar pair. The census files under
`lean/census/` carry a native-evaluation axiom and are checked
separately by `check.sh` — they must be excluded from any upload.

## What is not proved

A build and an axiom check are not a demonstration that a repository
is upload-ready, and this scan claims nothing beyond those two checks.
No project has been decomposed, no dependency graph has been
extracted, and no proposal has been submitted.

Two repositories contain deliberately open statements that must not be
uploaded as proved content: `Challenge.lean` in `diaz-modulus-lean`,
and `Challenge.lean` in `magma-1518-obstruction-lean` with its ten
sorries. An automated uploader that walks every declaration would
publish them as theorems. The exclusion is currently a note in this
survey and not a mechanism.

The census files in `magma-1518-obstruction-lean` carry a
native-evaluation axiom. They are excluded, which is not the same as
verified.

The drift patch was applied to a scratch copy only. Nothing is fixed
upstream; the repositories still fail to build on Lean v4.33 as they
stand.

The survey also contradicts itself on where to start, and the
contradiction is left in rather than resolved.
`moebius-transcendental-lean` is described as the tightest and the
natural first upload, on 39 declarations;
`magma-1518-obstruction-lean` is described as the best first upload of
the five, on the grounds of the smallest dependency surface, no
Mathlib and near-zero axioms. Both arguments are sound and they point
at different repositories. Picking one is Phase 1 work.

## What remains open

Phases 1 through 5, none of them started. They need two Lean
meta-programs — `extract_decl_graph.lean` and
`extract_sketch_info.lean` — and then a planner, a generator and an
uploader on top of those. Proposals are drafted against
`POST /api/v1/mission-proposals`, but only the account owner can
submit one for review; what this work can produce is a clean, ordered
draft to hand over.

The candidate mission goals, as drafted:

- **moebius** — the conjugation-degree spectrum classification:
  `finite_spectrum`, `conjDegree_ne_zero`, `top_witness_exists`,
  `stratum_nonempty`, `stratum_zero`. 39 declarations.
- **diaz** — the negative answer to Diaz's modulus conjecture, with
  `Solution.lean` as the entry point.
- **curve-symmetry** — sharp symmetry bounds for real algebraic
  curves: `full_euclidean_bound`, `direct_euclidean_bound`,
  `centered_rotation_bound_with_reflection`. The largest and most
  layered of the five; best attempted last, once the pipeline has been
  proven on something smaller.
- **erdos-straus** — `unified_offset_theorem` and `constructive_offset`
  with the fixed-divisor offset families `family_d2_24k5`,
  `family_d5_60k5` and the rest. The repository's README is explicit
  that this is a construction and **not** a proof of Erdős–Straus, and
  the mission description would have to say the same.
- **magma-1518** — Tao's Zulip conjecture: one-generated
  (1518+3862)-magmas are trivial or the Z/3 shift
  (`OneGenerated1518`), together with the explicit refuting family
  (`FamilyF5`, `FamilyF13`) and the two certificate identities
  (`L2Cert`, `H2Cert`).
