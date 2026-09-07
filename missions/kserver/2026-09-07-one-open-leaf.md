# The k-server mission now has exactly one open leaf

- **Mission** — The k-Server Conjecture,
  <https://prove2.me/missions/d22f9c72-3a9c-4fd4-8b83-c0b8756c994a>
- **Environment** — `c5ea00351c28e24afc9f0f84379aa41082b1188f`
  (Lean v4.30.0)
- **Date** — 2026-09-07

The k-server conjecture asks whether some deterministic algorithm can
move `k` servers on a metric space and serve any request sequence at a
cost within a factor `k` of the offline optimum. On Prove2Me it is
decomposed through the work function: `workFnU σ X` is the cheapest
cost of serving the prefix `σ` and finishing in configuration `X`, and
the mission's ladder of milestones bounds how much that function can
grow when one further request arrives. This entry records no new bound.
It records what the ladder looked like once opened, and the single move
that was actually available on it.

## What was proved

Eight targets were briefed. Four of them are **deprecated**: each is
superseded by its `_inj` form, which restricts the statement to
injective configurations, and all four `_inj` forms were already
Proved before this session.

| deprecated target | superseding form, already Proved |
|---|---|
| `workFnU_growth_two_server` | `workFnU_growth_two_server_inj` |
| `workFnU_growth_2k` | `workFnU_growth_2k_inj` |
| `workFnU_growth_card_succ` | `workFnU_growth_card_succ_inj` |
| `workFnU_growth_card_add_two` | `workFnU_growth_card_add_two_inj` |

The remaining four targets were live, but each already carried a
reduction accepted before this session, contributed by other users.
Those four, together with `KServer.kserver_conjecture` itself, all
funnel into one open leaf:

```
kserver_conjecture                     ─┐
workFnU_sharp_potential                 │
workFnU_growth_sharp_large              ├──►  d599af21
workFnU_growth_sharp_finite_subspaces   │
workFnU_growth_sharp_coalesced_finite  ─┘
```

That leaf is `potential_coalesced_k_ge3_finite_sharp`: the k-server
conjecture in sharp work-function form, with λ = k+1.

So the work here was not to solve targets. Seven of the eight nodes on
the board were already closed or already spoken for, and the whole
mission had been funnelled into one place. The only move that changed
anything was to move that one node.

The contribution is a reduction of the leaf, submission
`ce786430-20d3-4030-9a9a-d94660484645`, now SKETCH_ACCEPTED. It cites
exactly one new child:

- `KServer.antipodal_coalesced_growth_sum_sharp`
  https://prove2.me/theorems/30cc6393-c26b-483e-8b1b-2a7cffaa3644

which is now the unique open leaf of the entire mission.

## How

The reduction is assembled from antipodal machinery already proved on
the mission, and adds no analysis of its own.

`workFnU_antipodal_extension_restrict` says that `Sum.inl` into the
antipodal extension is an isometric embedding preserving `workFnU`
exactly, so nothing is lost by moving into the extended space.
`workFnU_growth_le_antipode` says that on an antipodal space the
work-function increment at *any* configuration is dominated by the
increment at the coalesced configuration sitting on the antipode of the
current request.

Given those two, take the potential to be

    Φ(σ) := Σ_t (antipodal increment at step t)

and take the constant `c := 0`. The step bound is then
`workFnU_growth_le_antipode` applied termwise, and the sharpness side
condition `c ≤ Φ []` is `0 ≤ 0`. Both discharge outright, which is why
the reduction leaves a single child rather than a family of them.

The child is the same mathematics as the leaf it replaces, but stated
with no existential over potentials and no quantifier over target
configurations: one explicit real per step, and one inequality.

The Lean is `lean/Solutions/KS_potential_coalesced_sharp.lean`.

## What is not proved

Nothing here proves the k-server conjecture or any instance of it. The
leaf `d599af21` was open before this session and its replacement
`30cc6393` is open after it. The reduction is a change of form: it
removes two quantifiers and pins the potential, and that is the whole
of it. `Φ` as defined above is a sum of increments that the conjecture
itself has to bound; choosing it does not bound it.

The four deprecated targets were not proved by this session and were
not proved because of it. They were already superseded when the mission
was opened. Recording them above is bookkeeping, not credit.

Two of the live targets could have been landed on paper. Working
solutions for `workFnU_growth_sharp_large` and
`workFnU_growth_sharp_coalesced_finite` compile cleanly, in
`lean/Solutions/KS_growth_sharp_large.lean` and
`lean/Solutions/KS_growth_sharp_coalesced_finite.lean`. They were
deliberately **not** submitted: they duplicate, route for route,
reductions already accepted on those targets by WillR and
jackjburleson. Submitting them would have registered two acceptances
and moved no node. The files stay in the repository as reference.

## What remains open

One node: `KServer.antipodal_coalesced_growth_sum_sharp`,
`30cc6393-c26b-483e-8b1b-2a7cffaa3644`. Closing it closes the ladder
and, through the ladder, `KServer.kserver_conjecture`. It asks for a
bound on the summed antipodal increments over an arbitrary request
sequence, which is the conjecture's own content — the reformulation
moved the statement, not the difficulty.

The definitions this rests on are copied verbatim into
`lean/Definitions/`, as `Def_KServer_model`, `Def_KServer_workfunction`,
`Def_KServer_workfunctionU` and `Def_KServer_antipodal_extension`;
`sorry`-bodied reference copies of the statements are in
`lean/Theorems/Thm_KServer_*.lean`.
