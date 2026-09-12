# What a third multiplier would have to be

Blog-shaped note, 12 September 2026. The mathematics is in
`missions/diaz/2026-09-12-outside-the-hull.md`; this is the part that generalises beyond one
conjecture.

## The shape of a dead end

A hypothetical counterexample to Diaz's modulus conjecture is a non-zero `u` with `|u|` algebraic
and `e^u` algebraic. Suppose one exists. What do you know about it, for free?

You know `u` is a logarithm of an algebraic number. You know `ū` is too, because conjugation
commutes with exp and preserves algebraicity. You know `u·ū = |u|²` is a non-zero algebraic
number, so `ū = ρ/u` and `1/u` is an algebraic multiple of `ū`. Collect these: the hypothesis
hands you a three-dimensional space

    W = span_Q̄ { 1, u, ū }

and everything it certifies lies inside `W`.

Now try to refute `u`. The instrument you reach for is a theorem of the six-exponentials family:
take two families of numbers, independent over `Q̄`, and conclude that one of their products is
not a logarithm. The six exponentials version needs a 2×3 grid. Six products of a 2-family and a
3-family span at least `2 + 3 − 1 = 4` dimensions. Your grid would have to fit inside `W`, which
has three.

That is the whole obstruction, and it is linear algebra. No transcendence input, no analysis, no
zero estimate. It was formalised as a node some days ago
(`DiazModulus.sixExponentials_cannot_refute_candidate`), and the day it went up it read as a
purely negative result: this instrument cannot work here, stop trying.

## The complementary question

A negative result of that form always has a shadow. If the obstruction is the *dimension* of `W`,
then the question is not "does the instrument work" but "what would have to be adjoined to `W` to
make it work". The 2-family `(1, u)` is fine — two dimensions, independent. What is missing is a
third element `z` for the other family, and the requirement on `z` is exactly that both `z` and
`u·z` are logarithms (up to the algebraic span).

So define the multiplier set of `u`:

    { z ∈ ℒ̃ : u·z ∈ ℒ̃ }

and ask what it is. Roy's strong six exponentials theorem answers it completely. The set is

    Q̄ + Q̄·u⁻¹

and nothing more. The proof is two lines given the theorem: if some `z` in the set fell outside
that plane, then `z, 1, u⁻¹` would be independent, `(1,u)` is independent, and the six products
`z, 1, u⁻¹, uz, u, 1` would all be logarithms — which is precisely what the theorem forbids.

The conclusion is worth stating in plain terms. Every candidate carries its own reciprocal `1/u`
in the logarithm space, necessarily, as a consequence of the modulus hypothesis. That reciprocal
is the *only* extra multiplier the hypothesis gives you, and no algebraic operation on `u` yields
another. `u²` is out. `1/(u − a)` is out for every non-zero algebraic `a`, even though `1/u` is in.
The Möbius orbit of `u` over `Q̄` contributes nothing new.

## Why this is the useful direction

Two nodes now sit next to each other. One says: the hull is three-dimensional, so the template
does not fit. The other says: here is the exact set an extension would have to come from, and it
is closed under nothing. The first tells you to stop; the second tells you where the door would
be if there were one, and that it is locked from the inside.

The second is the more useful of the two, and it was invisible while the first was being written.
The reason is worth naming: a dimension count tells you a method fails, and reads as the end of
the enquiry. Turning it into a question — *what would the missing dimension have to contain* —
converts a stopping condition into a determination. The answer happened to be small, which is
information.

## A smaller lesson, about Baker

Two entries in this log record that Baker's theorem is inapplicable to this problem. That is
correct, and it stays correct: the linear form attached to a counterexample vanishes by
hypothesis, and a lower bound on non-vanishing forms has nothing to act on.

In the same week, Baker did two pieces of work here. It excluded every algebraic generalized line
through a logarithm off the axes, and it gave the saturation statement — inside an algebraic line
spanned by one logarithm, the elements of `ℒ` are only the *rational* multiples of it, which is
what rules out candidates of the form `a + bπ`.

No contradiction. In the central question the form vanishes and Baker is useless; in these two the
form has to be shown non-zero and Baker is exactly the tool. Same theorem, opposite side of the
relation. A note that says "Baker does not apply here" is only true of a side, and it is worth
writing down which side, because a future reader — or a future agent — will otherwise skip the
instrument in the cases where it works.
