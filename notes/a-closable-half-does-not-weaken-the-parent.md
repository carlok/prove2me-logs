# A closable half does not weaken the parent, and five public nodes said otherwise

Correction, 2026-09-08. Recorded because the wrong claim is on a public mission and
because the reasoning that caught it is more useful than the claim it replaced.

## The error

The decomposition procedure said, and five reduction explanations on the Diaz mission
repeated: *each child of an ambient-space split is strictly weaker than its parent.*

That is wrong. Write the parent as `A ∧ B`. Each child is implied by the parent, so
"weaker" is fine. But the converse `B → parent` holds exactly when `A` holds — so the
moment the sibling `A` is a theorem,

```
parent ≡ A ∧ B ≡ B
```

and the residual child is **logically equivalent** to the parent. On the Diaz mission
four siblings are Proved, which makes their residual children equivalent rather than
strictly weaker. Where a sibling is not yet proved but is presumably true, the same holds
in fact if not in provability.

Worse, the procedure recommended *preferring* splits with a closable half. That advice
survives, but the stated reason did not: retiring a settled region does not reduce what
is left.

## What a split actually buys

A closable half hands the residual solver an extra hypothesis `¬Φ`, and retires a region
checkably. The value is that the difficulty is **located**, not lessened.

Which makes the real question not "how big is the closable half" but "is `¬Φ` usable":

- **usable** — local, structural, checkable at a point: `girth ≥ 4`, `no triangle`,
  `Re u ≠ 0`, `characteristic ≠ 2`.
- **weak** — a negative existential over a large search space: `no Hamiltonian path`,
  `no perfect matching whose complement is divisible`. Honest, and the solver gets almost
  nothing.

The Diaz splits survive this test: every `¬Φ` there is local (`Re u ≠ 0`, `Im u ≠ 0`,
`exp u ≠ 1`, off the axes), and both halves of every split are non-empty, which was
checked at the time. So the decomposition stands; the justification written on it did
not.

## How it was caught

By applying the same procedure to an unrelated mission — P3-partitions of cubic
3-connected graphs — where the flaw was immediately visible. There the closable half is
the traceable case, and the residual "not traceable" child is so plainly the whole
problem again that the equivalence cannot be missed.

On the source mission it was invisible, because the closable halves retired regions that
felt genuinely settled and the sibling was where the content had always been. The feeling
was right. The stated reason was not.

**Transferring a procedure to a different field is a test of the procedure, not only of
the field.** That is the general lesson, and it is why the test was worth running before
the procedure was recommended to anyone else.

## Two duals worth naming

The same review generalised the "what cannot work" rule, which had also been stated as a
special case:

- when the parent asserts **emptiness**, a *necessary condition on a counterexample* is
  conjecturally constant, so one child is conjecturally vacuous;
- when the parent asserts **existence**, a *sufficient condition for the conclusion* is
  the same trap.

The second had never been named, because the source mission had no existence claims in
it. And in the extreme case — the parent asserting that the ambient class itself is empty
— every predicate is conjecturally constant and **no split works at all**. There the
right move is helper lemmas plus a note saying why there is no tree.

## What was changed

- `skills/prove2me-decompose.md`: "What cannot work" replaced with the general form;
  the closable-half rule amended with the equivalence and the usable/weak ranking;
  new material on whether the split predicate is even expressible, whether anything is
  decidable, and whether an induction closes.
- The five reduction explanations on the Diaz mission carry a dated correction. Node
  descriptions are permanent and still contain the original phrasing; the correction says
  so rather than pretending otherwise.
