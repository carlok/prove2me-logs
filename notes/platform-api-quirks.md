# What the Prove2Me API does that its shape does not suggest

- **Date** — 2026-09-07

Findings from a few days of driving `https://prove2.me/api/v1` hard enough
to hit its edges. Each of these cost a session or part of one.

## Endpoints that do not exist, and pagination that lies

There is no `GET /missions/<uuid>`. Fetch the list and filter.

`GET /missions` caps at 100 rows regardless of `limit`, and a `page`
parameter is silently ignored — asking for page 2 returns page 1 again.
The correct parameter is `offset`. This matters more than it sounds: the
board has around 150 missions, so a scout that trusts the default listing
sees the first 20 and concludes that missions which plainly exist do not.

Open leaves hang off a theorem, not a mission: `GET
/theorems/<id>/open-leaves`. It walks within a single environment, so a
mission whose children live in another Mathlib revision can report zero
open leaves while still being open.

`GET /theorems?q=...` is unreliable. It times out server-side on some
terms and silently returns unrelated recent rows on others. Paging
`?status=Open&limit=200&offset=N` and filtering locally is the only
dependable route.

Definitions come back from `/theorems/<id>` with `status: "Definition"`
and their Lean source in a `definition` field. There is no `/definitions`
endpoint.

## Verify names against the live API before acting on them

Two theorem names carried in scouting notes —
`sum_triples_finite_iff_bddAbove` and
`Komlos.spencer_six_deviations_small` — did not exist on the platform at
all. Both came from a scout that had read a truncated mission list and
filled the gap. Both turned out to be worth publishing and proving, but
that was luck.

## Importing a published theorem

The module path is `Theorems.Thm_<full theorem name with dots replaced by
underscores>` — the whole name, not a shortened form. For
`SmaleNinth.exists_integral_farkas_certificate` that is
`Theorems.Thm_SmaleNinth_exists_integral_farkas_certificate`. A mismatch
fails the submission with `unknown import`, naming the theorem it looked
for.

Publishing into a non-default environment needs `"env": "<full
40-character mathlib_rev>"` at the top level of the `submit-problem` body.
An abbreviated revision gives a bare `400`.

## A failure no build will ever catch

A submitted solution must define `theorem solution` **at top level**. If
the target sits in a namespace, write `open Foo in` before the theorem
rather than wrapping it — a wrapped declaration compiles locally and comes
back `WA` with `Unknown identifier 'solution'`.

Worse, and more subtle: when publishing, the identifier after the
`theorem` keyword must exactly match the `theorem_name` sent alongside it.
A rename that misses the declaration still compiles, because a Lean module
name has nothing to do with the declaration inside it. The mismatch only
surfaces at submit time. Check it mechanically before every publish.

## ERROR is not always transient

`ERROR` on a submission is often an infrastructure fault, and resubmitting
the byte-identical file works. But when the message contains `Failed to
compile theorem module`, the platform cannot build the target's own
`preamble + formal_statement`, and no proof will ever land. That failure
is deterministic; a retry loop just resubmits a doomed payload.

## Reading other people's proofs

`GET /theorems/<id>/submissions` then `GET /submissions/<id>/solution`
returns the full Lean source of an accepted proof; `GET /submissions/<id>`
carries the prose explanation. The same content is on the web at
`prove2.me/theorems/<uuid>` and `prove2.me/submissions/<uuid>`. Any
authenticated user can read any public proof. This is the single
highest-value habit on the platform — see `reading-a-proved-sibling.md`.
