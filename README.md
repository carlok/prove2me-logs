# prove2me-logs

A working log of formalization activity on [Prove2Me](https://prove2.me),
a distributed theorem-proving platform where open problems are decomposed
into Lean 4 nodes and solved by whoever gets there first.

Profile:
[fca9fd8a-84f4-46ca-8845-a4a2b665381d](https://prove2.me/users/fca9fd8a-84f4-46ca-8845-a4a2b665381d).

The platform holds the proofs. This repository holds the account of them:
what was attempted, what the argument was, which Mathlib lemma carried the
weight, and — as often as not — what turned out to be unprovable, already
proved by someone else, or wrong.

## How to read it

`journal.md` is the index, newest first.

Entries live in `missions/<slug>/`, one folder per Prove2Me mission, named
`YYYY-MM-DD-<slug>.md`. `notes/` holds what does not belong to a single
mission: platform behaviour, measurement mistakes, methodology.

Every entry carries the mission and environment it belongs to.
Environments matter more than they look: the platform pins several Mathlib
revisions at once, imports never cross between them, and the same theorem
name can resolve to different content in two of them.

## Entry shape

`templates/entry.md`. Four sections, of which the third is not optional:

- **What was proved** — the statement, with the Lean declaration name and
  a link to the platform node
- **How** — the argument, and the lemmas that did the work
- **What is not proved** — the limits, stated as loudly as the result
- **What remains open** — the frontier below it

A result gets an entry when it is *stable*: accepted, proved, or
definitively refuted. Not when it is attempted, and not when it looks
promising.

## What this is not

Not a proof archive — the Lean sources live on the platform and in the
repositories the entries link to. Not a claim of novelty for anything
here; most of this work is closing leaves that other people opened, and
where a result is a routine transfer the entry says so. Not a complete
record: two missions with real Lean work and no written account are listed
as gaps in `journal.md` rather than papered over.

Negative results are kept deliberately. A vein of several thousand
statements that no proof can ever satisfy, a strengthening refuted by
hill-climbing, a mission whose targets were superseded before anyone
touched them — these cost sessions to establish and are worth more written
down than the routine wins.

## Cadence

An entry per stable result, written at the time. Missed results are not
backfilled from memory; if the record is thin for a period, it stays thin
and says so.

## Blog

Posts on [carlok.github.io](https://carlok.github.io) are written from
this repository by a daily task whose prompt lives in that repo, at
`scripts/PROVE2ME_BLOG_TASK.md`. It reads `journal.md` and the entries
below it, and nothing else — no API key, no polling, no state kept
anywhere.

Nothing here generates a post on its own, and nothing in the site repo
reads this one automatically. What is automatic is the projects page:
pushing here updates this repository's `pushed_at`, and the site's daily
`sort-projects` workflow re-sorts on that.

## Method

Parts of this work, including much of the Lean and most of this log, were
done with an AI assistant. Where a claim here rests on something checked
rather than assumed, the entry says how it was checked. Several
confident-sounding findings in these notes were wrong first and are
recorded with the correction attached, because the correction is usually
the useful part.

## Licence

Apache-2.0, matching Mathlib.
