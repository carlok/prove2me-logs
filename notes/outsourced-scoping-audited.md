# We outsourced a scoping job to another model, then checked every claim in it

2026-09-08. `DiazModulus.four_exponentials_trdeg_one` is a 1973/74 theorem published as an
open node. Rather than spend this session's budget on it, the task went to a different LLM
running locally in its own workspace, with a self-contained brief. This is the audit.

## The setup that made it checkable

The other model got `envs/fourexp_workspace`: its own Lake project, own `Solutions/`, own
`.lake/build`, with `.lake/packages` symlinked to the shared Mathlib checkout. 24K before
building, and a file importing Mathlib compiles in under a minute because the oleans are
already there. It could not collide with our tree and it could not rebuild Mathlib.

The one rule that mattered: **every Mathlib declaration name in its inventory had to be
`#check`ed in a file that builds.** Not recalled. That is the entire reason to run a model
locally instead of in a chat window, and it is what made the output auditable afterwards.

## The audit

- **All 20 names it marked CONFIRMED are real.** Re-`#check`ed in an independent probe.
- **All negative claims hold.** Zero Mathlib files mention Wirsing, Philippon, six or four
  exponentials, Schneider–Lang, or Baker. No transcendence-of-`exp` result anywhere.
- **Its Lean builds clean.** `FE4_rankone.lean`, four theorems, `[propext, Classical.choice,
  Quot.sound]`, no `sorryAx`.
- **It stayed in its folder.** Nothing written inside the shared Mathlib; `FE4_` prefix on
  every file, as asked.

## What it did that was better than expected

**It could not obtain either original paper and said so.** Brownawell (JNT 6, 1974) is behind
ScienceDirect and a direct fetch returned HTTP 400; Waldschmidt (JNT 5, 1973) is on the
author's own page but as a scanned image with no text layer. It then explicitly did *not*
reconstruct their contents, and labelled its "classical route" sketch as the generic shape of
Gel'fond–Schneider-era proofs rather than either paper. That was the rule, and following it
cost it the most interesting section it could have written.

**It listed one row as file-listing-only and told the reader not to cite it.** Schwarz and
Jensen: the files exist, the individual lemma names were never `#check`ed, so — its words —
"do not cite any".

**It found three namespace traps by building rather than reading.** `trdeg_eq_zero`,
`trdeg_eq_zero_iff` and `trdeg_pos` are in the **root** namespace, not `Algebra.`; Mahler
measure lives under `Polynomial.`, not `MahlerMeasure.`; heights under root `Height.`, not
`NumberTheory.Height.`. All three were wrong on the first guess and errored in the first
probe build. A chat-only model would have written all three confidently and wrong.

## The verdict, and it is negative

**Not reachable at reasonable effort with this Mathlib.** The single biggest obstacle is the
**Philippon zero estimate**: even granting Wirsing's theorem, there is no route from
"determinant vanishes to high order" to "rank drop or algebraic subgroup" without it, and
essentially none of its supporting theory — algebraic groups, intersection multiplicities,
Hilbert–Samuel degree bounds — exists here. Wirsing is second, and at least self-contained.

It also killed the obvious shortcut. Six exponentials does **not** imply the target: six
exponentials is a `3×2` statement, the target is `2×2` plus a transcendence-degree hypothesis.
Formalising six exponentials would be a real milestone and the natural warm-up, but it is not
a path to this node.

## One correction, and it is ours not theirs

Its salvage list ranks "full Hermite–Lindemann" third, as substantial work. **That is already
banked on this mission.** `DiazModulus.hermite_lindemann_holds` is Proved, from a 43K local
file with zero `sorry` carrying Yuyang Zhao's 2022 copyright header — the arithmetic half that
Mathlib lacks, formalised outside Mathlib and imported here. The model scoped *Mathlib*,
which is what it was asked to do; it had no way to know our board already had this. Its own
note says "cf. mission node `hermite_lindemann_holds`", so it half-saw it.

Worth generalising: an outside scoping pass measures the library, not the mission. Anything
the mission has proved on top of the library has to be subtracted by hand afterwards.

## One claim to flag as unverified

"There is no known deduction of the transcendence-degree-one four exponentials from six
exponentials." Plausible, consistent with Roy–Waldschmidt attributing the trdeg-1 case to
entirely different arguments, but written from memory with no literature access. Same category
as the `dl > d + l` caveat carried in the free-half run. Do not quote either without checking.

## What this changes on the board

The node should stop being described as a formalisation target someone might pick up. It is a
**citation boundary**: a theorem we are entitled to use with attribution, whose formalisation
is a multi-year project nobody on this mission should start. That is a different thing to tell
a contributor, and the description should say it.
