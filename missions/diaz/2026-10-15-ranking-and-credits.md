# What was not found, ranked; and credits owed
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-10-15

The blueprint's last chapter lists the results not found in the
sources read, split into "not routine" and "short". This round ranked
the first list, tested the second for promotion, and swept the site
for text that time had made wrong. No new theorem was proved.

## The ranking

A rubric was fixed before any ranking: distance from print, depth,
reach, and use in the library, each scored 1 to 3, with the robustness
of "not found" as a caveat. A result is not routine when its proof has
a step that was not found in the sources and that a specialist would
not call routine, whatever its length. Two referee agents scored every
candidate blind to each other and to my own order. They agreed on the
order within one place; they disagreed on where the line falls.
Carlo chose the strict line.

1. **Theorem B**: the four-dimensional extensions of a point of a
   circle that carry a 2×3 configuration are exactly those containing
   u², ū² or some 1/(u − a).
2. **Case I classified**, promoted from the second list: a
   five-dimensional space holding a four-term progression with ratio
   rational in u is visible or is one of the involution spaces.

Separation, the Laurent-hull criterion and the 2×2 normal form moved
to the second list, which they now open. Both referees found that each
applies a printed method: Waldschmidt's book, Prop. 12.2, for
separation; Bachoc, Serra and Zémor, §7, for the hulls; their
critical-pair lemma for the normal form. The double borders in the
dependency graph moved from ten nodes to six.

## Corrections

- **A lemma presented as new was in print.** "A configuration in
  dimension four is a progression", the key step of Theorem B, is
  Lemma 4 of Bachoc, Serra and Zémor (2017). Our own literature check
  of 10 October said so; the blueprint and the node's Prove2Me page
  were never updated. Both now credit it.
- **Fischler's Lemma 6.1 is about logarithms**; Diaz's Théorème 7(2)
  is its form for ℒ̃. Several texts had equated them.
- **"The strong six exponentials route stops at u³"** holds for single
  powers through their hulls; pairs of higher powers can still be
  excluded. The note, the blueprint and the README now say so.
- **Three accepted proofs by other contributors were mirrored without
  credit**: two by amorphic and one by curiyu, all of 8 September.
  Their modules, the README and the blueprint now name them.
- A sweep fixed stale text across five chapter intros and the README:
  counts, section lists, cross-references, versions, the size rule
  (five proofs break it, not two) and a helper said to be imported
  that sixteen proofs carry locally.

Note version 1.27 carries the attribution corrections.

## Mathlib v4.35.0

Lean and Mathlib v4.35.0 are out, with matching commits of the export
checker that stopped the v4.34.1 bump. A trial in a separate worktree
built all 9,439 jobs after three fixes: a rewrite rule for the new
`contDiff_apply` in two ported modules, applied by the porter only on
v4.35, and one changed class in the Lindemann–Weierstrass port. The
axiom audit and the porter's check are clean, and CI passed on the
branch. It is not merged yet.

## What is not proved

- **Nothing new is proved here.** The ranking is an editorial
  judgment on a fixed rubric; the referees are agents, not experts.
- **"Not found" stays provisional**: two claims have now fallen to
  sources read after they were made.
- **Five proofs still break the size rule**; splitting them means new
  platform nodes.
- **The v4.35.0 move waits for Carlo's go**; CI is green on its branch.
