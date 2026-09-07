# What formalising a hand-checked proof actually turned up

2026-09-07. A prose argument in this project — the six-exponentials no-go — had been
re-read by hand twice with no error found, and a public note rested on it. It was then
formalised. This records what that exercise produced, because "we checked it by hand"
and "it compiles" turned out to differ in specific, small ways rather than in the
dramatic way one hopes for or fears.

**The headline: the proof survived.** All four branches closed as written. Nothing had
to be repaired, no hypothesis was missing, and the theorem is true.

## What changed anyway

**A characteristic-2 slip.** The prose wrote the coefficient of `T_b T_b'` in a product
`gh` as `γ_b h_b' + γ_b' h_b`, then set `b = b' = b₀` to conclude `h_{b₀} = 0`. That
formula is valid only for `b ≠ b'`; the diagonal coefficient is `γ_b h_b`, not
`2γ_b h_b`. Over `Q̄` the difference is invisible, which is why two hand readings
missed it. Taken literally the step would fail in characteristic 2. Using the correct
diagonal is what let the formal version be stated over an arbitrary field.

**A branch that was shorter than advertised.** The prose justified one case by
appealing to "the computation just performed". That appeal is legitimate but not for
the reason it looks like: the two situations are not symmetric — one polynomial divides
elements of the subspace, the other multiplies them. They coincide because both reduce
to the same statement about a product of two degree-≤1 polynomials. In Lean that became
a single lemma serving both, and the case needed less than the prose set out.

**A step the prose mentioned but did not finish.** For the second variant, one
sub-case leaves a linear relation `α h₁ + β h₀ = 0` that the write-up notes and leaves
hanging. Solving it produces a second line, `K·(α − βX)`, alongside the expected `K·X`.
Not an error, but not done either.

**A sharpness witness that had been asserted.** The claim that the dimension threshold
cannot be lowered was stated. It is now exhibited: `Z = span{X, X²}` with `s = 1/X`
satisfies every hypothesis at rank 2 while `s ∉ K`. Pleasingly, that witness is the
free-ring shadow of the one configuration the surrounding theory says must survive.

**Two hypotheses turned out to be unnecessary.** The field need not be `Q̄`, and finite
dimensionality can be replaced by a cardinal rank bound. Neither weakening was
noticed by hand, because hand proofs use the ambient assumptions without tracking
whether they are load-bearing.

## What formalisation did not do

It did not close the gap between the free-ring statement and any statement about
complex numbers. That transfer needs an injectivity which is Schanuel-strength, and
Schanuel already settles the question the argument was aimed at.

It also did not cover one step in full generality. The cut-down uses a single `T`, so a
relation that only appears with two or more of them is verified in shape rather than in
generality. Everything else is independent of that count.

## The lesson, such as it is

Formalising a correct proof did not find a hole. It found a coefficient valid only off
the diagonal, an appeal to symmetry that was really an appeal to a shared lemma, an
unfinished linear solve, an unexhibited witness, and two hypotheses that were never
needed. None of that changes the theorem. All of it changes what can honestly be
written about the theorem — which, for a public note, is the whole point.
