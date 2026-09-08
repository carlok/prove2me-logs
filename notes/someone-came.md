# Someone came, eleven minutes after publication, and we had already closed it

2026-09-08. The first outside contribution to the Diaz mission, and the first measurement
of whether decomposition actually recruits anyone.

## What happened

```
04:26:25   node published      DiazModulus.diaz_of_exp_eq_one
04:32:39   carlok proves it
04:37:42   curiyu proves it
```

`curiyu` created their account at **03:49** — thirty-seven minutes before the node existed.
They found it within eleven minutes of publication, wrote an independent proof, and it was
ACCEPTED. Their account stands at 7 solved problems and trust 2.

The node is the `exp u = 1` case of Diaz's conjecture: closable because its hypotheses are
contradictory, `u = 2πin` with `n ≠ 0` forcing `|u| = 2π|n|`, so an algebraic modulus would
make `π` algebraic.

## What it proves about the method

**Decomposition recruits.** Before today the mission's only open item was a
twenty-two-year-old conjecture and nobody had ever submitted to it. Within hours of the
frontier carrying leaves sized for one sitting, a brand-new account found one and closed
it. Eleven minutes.

That is the whole thesis of the decompose-link-iterate procedure, tested once and confirmed
once.

## What it proves about us

**We wasted their time.** They finished five minutes after the node was already Proved.
Whatever they spent on it bought them nothing, and the mission gained nothing it did not
already have.

This was foreseeable and was in fact foreseen. The question "publish nodes we can prove, or
hold the proofs back" was raised explicitly earlier in the same session, with the
recommendation to hold. We published and closed anyway, because closing felt like progress.

A node published and proved by its author within six minutes is not an entry point. It is
an announcement.

## The scale of what we consumed

Four closable halves were produced and self-closed that morning, inside forty-five minutes:

```
diaz_of_exp_real_self_real        published 04:08:05   self-proved 04:11:02   (3 min)
diaz_of_exp_eq_one                published 04:26:25   self-proved 04:32:39   (6 min)
diaz_of_exp_real_pure_imaginary   published 04:41:18   self-proved 04:44:23   (3 min)
diaz_of_exp_not_real_on_axes      published 04:50:46   self-proved 04:53:35   (3 min)
```

The contributor caught one only because they happened to be looking during a six-minute
window. Three others opened and shut without anyone having a chance.

The supply was never the problem. Every honest split produces exactly one closable half —
that is what makes a split worth publishing. Manufacturing small nodes to attract help
would be worse than useless, since nodes are permanent and a board padded with easy
statements that advance nothing becomes busywork.

## The rule that follows

Written into `skills/prove2me-decompose.md`:

> When a split produces a genuinely closable half, decide deliberately whether to close it.
> Closing it yourself makes the graph look complete and gives the mission progress. Leaving
> it open is what actually recruits. You cannot have both, and the default should be to
> leave at least one closable leaf open at any time.
>
> Publish both halves of a split and do not prove the closable one for a set window; a day
> is a reasonable default. Batch the publications — not for volume, for visibility, since a
> frontier that moves all at once is discoverable and a trickle is not. After the window,
> close what nobody took, so the mission does not look stalled.

Adopted cadence: **batch out at the end of the day**, hold the closable halves overnight,
close the unclaimed ones the next day.

## The tension underneath

What attracts help is what does not need help.

The node taken was closable because its hypotheses were *contradictory* — a vacuous corner,
not a small piece of the problem. The mission's genuinely open leaves are a degree-2
relation in two logarithms and an open question of Waldschmidt's. No cadence makes those
approachable.

So the realistic goal is not help on the hard part. It is a **visible gradient**: something
takeable now, something takeable with effort, and a plain statement of why the top is hard.

## Follow-up

Six hours later a second stranger did something stronger: published a new open node and
attached it as a reduction of the mission's hard leaf, in forty seconds, and left it open.
[Someone else split the hard leaf](someone-decomposed-it.md).

## What is not claimed

One contributor, one node, one data point. Nothing here shows that harder leaves attract
anyone, and the node they took was the easiest thing on the board by construction.

The mission's `vote_count` is still zero across every node in the conjecture tree, so
attention is not otherwise measurable. And thirty-six of the thirty-seven submissions on
that tree are still the author's own.
