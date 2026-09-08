# Open threads at 2026-09-08 12:20, session stopped for token budget

Four agents ran as 2+2 (Diaz / non-Diaz). One reported in full; three were stopped
mid-flight. Nothing is lost, but three things need a look next session.

## 1. A submission left PENDING

`board-open` split **Collapsible Cubics** (`CollapsibleCubics.cubic_collapsible`,
`6c13f615-ee99-4c9e-b081-79ac6e26168c`) into two published children and submitted the
reduction against the parent at 12:18:48. It was stopped while that submission was still
`PENDING`. The verifier runs server-side, so the verdict resolves without us.

- `CollapsibleCubics.cubic_collapsible_of_normForm_repr` (Open, 12:16:04)
- `CollapsibleCubics.cubic_collapsible_of_not_normForm_repr` (Open, 12:16:00)

**Check the verdict first thing.** If it did not land, the two children are orphans on a
public board — published, unlinked, and looking like a contribution without being one.
The agent wrote no account file, so if the reduction failed the argument has to be redone.

## 2. Leaf 2 was split and the link held

`diaz-leaf2` published two children of
`DiazModulus.diaz_of_exp_not_real_irrational_angle_period_free`
(`5c573fdf-0df3-42af-9d7b-75e39a7c1f6b`) and its reduction came back `SKETCH_ACCEPTED` at
12:14:48, before the stop. That work is complete and linked.

- `..._period_free_pi_im_algebraic` (Open, 12:13:36)
- `..._period_free_pi_im_transcendental` (Open, 12:13:35)

No account file was written. The split is on the graph and readable from the submission.

## 3. Two closable halves are being held overnight

From the run that did report, both proved locally with clean axioms and published **Open**
on purpose under the cadence rule:

- `Diaz.pair_dichotomy_exclusive` — `99e66042-79f9-4b5d-a081-f97c074c1023`
- `Diaz.conj_combination_off_rays` — `926f2540-2d5b-4750-893b-093edbd4d06a`

Proofs are in `missions/diaz/lean/Solutions/DZ_MINE_check.lean` and `DZ_MINE_check2.lean`.
To close: rename to `theorem solution`, prefix `open Diaz in`, submit. **Close them tomorrow
if nobody has taken them.** The four children in §1 and §2 are held under the same rule.

## Territory, still standing

`EvanLLL` owns `DiazModulus.diaz_of_exp_real_generic` (leaf 1) and the `BertsekasDP.*`
mission. Stay off both.
