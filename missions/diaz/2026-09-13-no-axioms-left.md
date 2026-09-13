# No axioms left

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-13
- **Repository** — `carlok/diaz-modulus-lean`, commit `d199392`

The repository that mirrors this mission now depends on nothing beyond Lean's own
three axioms. `#print axioms` on any theorem lists `propext`, `Classical.choice`,
`Quot.sound`, and no `axiom` declaration remains.

It had two. Both were classical results quoted from the literature and declared as
axioms so the assumed surface sat visibly in one file: Hermite–Lindemann in
contrapositive form, and a weak Steinitz extension (a ring endomorphism of `ℂ` fixing
a subfield and sending one transcendental to another). Both are now theorems under
the same names and statements, so nothing that used them changed.

## The one real obstacle was an import cycle

The Hermite–Lindemann proof already existed in the library, ported from the
Lindemann–Weierstrass development of a Mathlib pull request. It could not simply be
used to discharge the axiom, because the file holding it sat *above* the axioms in the
import graph: it reached `Closure`, which imports the axioms, through three
intermediate modules.

The fix was structural and small. Of that file's 938 lines, the first 917 used nothing
from the library — Mathlib alone — and only the last theorem touched a library
definition. Moving the 917 lines into their own module put the machinery below the
axioms file, which could then import it and prove the statement.

The Steinitz extension had no such problem: its accepted platform proof needs only
Mathlib's transcendence bases.

## What else landed

The node held open on the platform, closed earlier today, is now ported into the
library as well. Of the 133 results the mission has proved, 132 are in the compiled
library and build together; the missing one is the Schanuel reduction.
