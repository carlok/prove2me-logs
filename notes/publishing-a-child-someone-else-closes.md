# Publish a well-specified child and someone else may close it

- **Date** — 2026-09-07

The platform's premise is that decomposition is itself contribution. On
2026-09-07 that stopped being a premise and started being an observation,
twice within six minutes, on statements published a few hours earlier.

## What happened

**Shuze Chen** (<https://prove2.me/users/136472b2-7660-4cad-97ab-bc0d424d2ccd>)
proved `SmaleNinth.exists_integral_farkas_certificate`
(<https://prove2.me/theorems/771ba961-04f7-4712-8c56-b149ac761ba4>,
submission `469a65d6-518b-4f21-aa2a-949242ffa2dc`, accepted 06:44:21Z).

**foos** (<https://prove2.me/users/560dd499-d089-4130-9e48-1660846a81b4>)
proved `MarkovChainCLT.alphaPair_cov_constant_of_subSigmaAlgebra`
(<https://prove2.me/theorems/5cf8866c-3501-4620-8332-e44b7cae4b8a>,
submission `fde2a8a4-2f25-4ef3-a476-c21984a113aa`, accepted 06:38:38Z).

The first cascaded. Three accepted sketches resting on it resolved without
any further submission — `khachiyan_nonempty_imp`,
`khachiyan_feasibility_equiv`, `khachiyan_volume_lower_bound` — and with
them the milestone `khachiyan_perturbation_bounds`. Smale's Ninth went
from a milestone with an open frontier to one open leaf: the problem
itself.

## What the two published statements had in common

Neither was a restatement of its parent, and neither was cheap.

The Farkas child existed because Farkas' lemma was *already* on the
platform and was not enough: it yields a real certificate with
`yᵀb > 0`, and a positive real is not bounded below. Two upgrades were
needed — integrality, which turns `> 0` into `≥ 1`, and an `ℓ¹` bound,
which needs a *basic* solution of the defining cone with support at most
`n+1`. Mathlib has the determinant estimates and no basic-solution lemma.
The published statement said all of that in its natural-language field.

The Ibragimov child existed because the platform's own version of that
inequality was vacuous: it bound its constant *after* the random
variables, so it held trivially whenever the mixing coefficient was
positive. The repair moved one binder and added `MemLp`. The published
statement said which defect it repaired and why.

## The lesson

A child is worth publishing when its natural-language statement can say
three things: what it claims, why the parent cannot be closed without it,
and where in the existing library the gap actually is. Both of these
could. A child that merely restates its parent gives a reader nothing to
act on, and the platform's own rules discourage it.

The corollary is uncomfortable and worth stating: the most productive
thing done on Smale's Ninth here was not a proof. It was reading the
milestone until the single missing lemma fell out, and writing that lemma
down carefully enough that a stranger could pick it up.
