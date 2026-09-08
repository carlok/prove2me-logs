# The run that mostly declined to publish

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

An agent was sent to port Diaz 2007 Corollaire 2, build `e^{π²}` on top of it, and publish
the ℚ-rational subspace classification. All three were already on the board, published
earlier the same day by a run whose account it had been given and did not simply believe.
It checked, found the work done, and published neither.

What it published instead were two clauses nobody had taken.

| node | uuid | from |
|---|---|---|
| `Diaz.pair_dichotomy_exclusive` | <https://prove2.me/theorems/99e66042-79f9-4b5d-a081-f97c074c1023> | `p20_diaz.tex` Thm 2.5, the "(i) excludes (ii)" clause |
| `Diaz.conj_combination_off_rays` | <https://prove2.me/theorems/926f2540-2d5b-4750-893b-093edbd4d06a> | `p20_diaz.tex` Thm 3.9, the closing clause |

Both unconditional — no transcendence input at all. Both were **proved locally before
publishing**, clean axioms and zero `sorry`, and then **published Open with no submission**,
under the cadence rule adopted this morning. The proofs sit in `DZ_MINE_check.lean` and
`DZ_MINE_check2.lean` and convert to submissions by a rename. If nobody takes them by
tomorrow they close in minutes.

## The negative result, which is the useful half

The brief asked a live question: with the classification published, do Thm 2.5 and Thm 3.9
become reachable? **No, for both, and the reason is the same.** The classification removed
the linear-algebra obstruction. What is missing is the transcendence input, which is all of
it: Roy–Waldschmidt Théorème 0.2 for 2.5, Théorème 7.1 for 3.9. Théorème 0.2 will not
substitute for 7.1, because `ρ/μ` is not known to be a logarithm, and that is the entire
point of 3.9.

Carrying Roy–Waldschmidt as an explicit hypothesis does not rescue either, and the reason is
sharper than "it would be conditional". The **conclusion** of 2.5 clause (i) is already the
conclusion of the master dichotomy carried as `hMaster` inside two published nodes,
`Diaz.four_exp_trdeg_one` and `Diaz.log_modulus_forces_independence`; instantiate that
`hMaster` at `(u, ū, v, v̄)` and clause (i) falls out verbatim. A carried-hypothesis 2.5
would have been an instantiation of published material wearing a new name.

`CLASSIFICATION.md` had reached the same verdict independently. This run confirmed it rather
than overturning it, which is worth as much and reads as less.

## What this says about the duplicate check

The brief called the duplicate check the expensive part of the job rather than the
formalisation, on the evidence of the previous run dropping three of twelve candidates. This
run went further: **the check was the job.** Four would-be republications stopped, two
genuinely unmined clauses found underneath them.

The mechanism that makes this necessary is worth naming. Six agents have now mined the same
two manuscripts. Each reads the same source and reaches for the same headline theorems, so
the *collision rate between our own runs is far higher than between us and anyone outside* —
a stranger picks a node by browsing, we pick by re-deriving, and re-derivation converges.
The fix is not a better prompt. It is two `q=` calls per candidate, one per namespace, before
any Lean is written.

## A correction to the record

`CLASSIFICATION.md` placed both theorems in `p21_diaz.tex`. Neither label resolves there:
`thm:pair-dichotomy` is `p20_diaz.tex:428` and `thm:mixed-rigidity` is `p20_diaz.tex:857`.
Corrected in place.
