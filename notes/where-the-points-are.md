# Where the points are, measured

2026-09-08. A strategy question — what is the highest-return area on this board — answered
with queries rather than intuition. The answer is that the volume game is over.

## The numbers

- **4044** theorems Open across the whole platform.
- **2988 of them, 74%, are `lean_workbook_*`.**
- **8507** `lean_workbook` problems are already **Proved**, and the most recent one closed on
  **2026-02-28**. Six months of nobody touching the residue.
- The global leaderboard is `trust`, which tracks solved count. The top three — 5188, 4335,
  3845 — were built on this family while it was live.

## Why the residue is not a vein

The open `lean_workbook` problems live in env `777aaa61…` (Lean v4.29.0-rc3), not the v4.33.1
environment most current work uses. **Testing them in the wrong environment produces
meaningless failures**, and that is very likely where the older folklore that "local compiles
do not predict acceptance" came from. It certainly produced one here before the environment
was checked.

Tested in the *right* environment, a 32-problem sample still does not elaborate:

- the `∑ x in s` binder is gone from the language at that revision — the only occurrences left
  in Mathlib are inside docstrings;
- `Complex.abs` has been removed;
- and some statements are false as stored. `lean_workbook_plus_57587` asserts
  `∑ C(n,k)² = C(2n,n)²`; the identity has no square on the right.

There are free points scattered in it — `lean_workbook_plus_60563` has hypothesis `hf : f x = x`
and goal `f x = x`, so `exact hf` closes it — but not enough to be a strategy, and `∑ in`
means most of the file will not compile to begin with. `LeanWorkbookFaithful.*` turns out to be
one node by one user, not a successor family.

## What that leaves

About **1056** non-workbook open theorems, which are real mission mathematics. The largest
single family is 38 nodes. Nothing there is cheap.

So there is no volume play left, and the honest planning consequence is to stop looking for
one. What remains scores two ways, and only one of them is on the global board:

- **First accepted solution** on a mission node — one point, to whoever lands it first. A
  `SKETCH_ACCEPTED` reduction scores nothing, because the target stays Open. That is why the
  best outside contribution to the Diaz mission this week earned its author zero.
- **Published problems** — one point per node created, on the *mission* leaderboard only. The
  global `num_submitted_prob` field is `0` for all 461 users, leaders included.

## The tension worth naming

The scoreboard pays for closing. The cadence adopted this morning — publish the closable half,
hold it overnight — deliberately does not close. Holding costs points and buys contributors,
and today it bought one: a stranger closed a held node twenty-two minutes after we walked away
from it.

That is a choice, not an oversight. But it should be made knowing the price.
