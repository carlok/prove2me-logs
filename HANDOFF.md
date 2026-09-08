# Open threads at 2026-09-08 14:35

## The frontier is four leaves

```
DiazModulus.recip_pi_not_log                                   b5a16bec  (S) — ours, new
DiazModulus.norm_transcendental_of_generic_conj_pair           ed970912  EvanLLL's
..._period_aligned_norm_rat_mult                               561efd5c  looks closable
..._period_aligned_norm_free                                   1b43101e
```

**(S) is the one to push.** It closes `..._period_aligned` and
`..._period_free_pi_im_algebraic` outright, both reductions already `SKETCH_ACCEPTED`, and
it is strictly less than the conjecture. The crux is equivalent to the root, so it is not
easier than the whole problem.

**`561efd5c` looks closable via `Diaz.four_exp_trdeg_one`** — the aligned class has
transcendence degree one, which is the regime where 4EC is known. **Do not close it until
someone checks `Diaz.four_exp_trdeg_one` against Roy–Waldschmidt 1995.** Its own description
says the statement was transcribed from `p20_diaz.tex` and never verified against the source.

## Held open overnight, proofs already written

| node | uuid | proof |
|---|---|---|
| `Diaz.pair_dichotomy_exclusive` | `99e66042` | `DZ_MINE_check2.lean` |
| `Diaz.conj_combination_off_rays` | `926f2540` | `DZ_MINE_check.lean` |
| `CollapsibleCubics.cubic_collapsible_of_not_normForm_repr` | `faff93b8` | — |

`cm` proved the sibling `..._of_normForm_repr` at 12:38, twenty-two minutes after we
published it and left it alone. First time the hold rule produced a contribution.

Close whatever is unclaimed tomorrow.

## Territory

`EvanLLL` — leaf 1 and its crux, plus the `BertsekasDP.*` mission.
`quesswho` — created and actively works Collapsible Cubics; we split its root.
`cm`, `curiyu` — solvers, no territory.

## Rule that needs fixing in the next brief

When picking a mission to decompose, check its node count and recent activity, not just
whether the root says Open. Collapsible Cubics had 13 nodes and an author working it ninety
minutes before our agent arrived; the brief told the agent it was unworked.
