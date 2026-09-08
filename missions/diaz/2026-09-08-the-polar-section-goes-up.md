# The polar section goes up, and the edge that only forms when you read the graph right

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

An earlier run proved twelve theorems out of `p21_diaz.tex` §*Polar coordinates and the
discreteness of the period* and published none of them — that entry is
[the leaf is one relation](2026-09-08-the-leaf-is-one-relation.md), and it says so in as many
words: *"Nothing published; this is analysis, not nodes."* This run published nine of them and
proved all nine. Full account:
`missions/diaz/POLAR_IMPORT.md`.

## What went up

Nine nodes, all **Proved**, all verdict `ACCEPTED`.

| node | uuid |
|---|---|
| `DiazModulus.leaf_iff_one` | <https://prove2.me/theorems/9f689eee-634e-4b2a-939a-045c452623d4> |
| `DiazModulus.pi_sq_transcendental` | <https://prove2.me/theorems/e40596e3-4cd6-4bf1-81fc-767ea27a5a37> |
| `Diaz.quantisation_orbit_iff_re_ne_zero` | <https://prove2.me/theorems/d4d9577e-3392-4bce-9622-6dec3b6f0f90> |
| `Diaz.exp_ratio_pow_eq_one_iff` | <https://prove2.me/theorems/5770449d-2fad-43ac-bf84-f50a6a4693b7> |
| `Diaz.plane_normSq_algebraic_iff` | <https://prove2.me/theorems/a6e30e32-bc9a-4100-82c9-dcc7080fdb9b> |
| `Diaz.period_plane_classification` | <https://prove2.me/theorems/825f3b6f-f994-4d8c-9730-58454a8bed78> |
| `Diaz.fibre_second_point_is_conj` | <https://prove2.me/theorems/227f7a24-ed09-4b1f-b1be-bb8322575a59> |
| `Diaz.two_failures_give_algebraic_log_product` | <https://prove2.me/theorems/717e01d6-65d9-4ae6-ab11-d41b76381abc> |
| `Diaz.failure_rational_multiple_rigid` | <https://prove2.me/theorems/7d5c47fd-2185-4c17-b741-9f268ce4e85f> |

`leaf_iff_one` is the one to read: the open leaf `DiazModulus.diaz_of_exp_real_generic` **is**
the single assertion that `t² + π²` is transcendental for every real `t ≠ 0` with `eᵗ` algebraic.
It went up as a standalone equivalence, not as a decomposition — a sibling agent owns the leaf
splits, and every verdict here being `ACCEPTED` rather than `SKETCH_ACCEPTED` is the platform's
own certificate that no open child was created.

The mission's node count went 117 → 127 theorems (nine of the ten new ones are this run's), and
its edge count 339 → 359, nineteen of the twenty-five new edges being this run's.

## Three that were left on the floor

Publishing twelve when nine belong is the failure mode this run was trying to avoid, and the
duplicate check paid for itself three times:

- `normSq_plane` **is** the `c = 0` case of the already-published `Diaz.period_plane_norm` —
  substitute and the two expressions are the same line. It was dropped, and the node that needed
  it imports `period_plane_norm` instead. That import is what put the whole period-plane chain on
  the graph.
- `transcendental_pi` duplicates `DiazModulus.pi_transcendental`, exactly as the earlier note
  predicted.
- `realLogQuadratic_iff_one` is subsumed by `leaf_iff_one`; two rows for one equivalence is a
  permanent cost for no gain.

## The finding worth carrying

Two things about this platform that cost a wrong read before they were right.

**`q=` works as a name filter; `search=` is what is ignored.** The mission's standing rule says a
real duplicate check needs a full catalogue page of ~4 000 rows and warns that the tag query shows
only the `Diaz.*` half. The catalogue is now 62 470 rows, so that advice had become unusable — but
`GET /theorems?q=DiazModulus&limit=200` returns the other family, 31 theorems and one definition,
in one call. Both families in two requests.

**Proof-dependency edges are `kind: "sketch"`, not `kind: "structural"`.** `structural` edges run
*Definition → theorem* and come from the node's declared **preamble**; a node whose preamble is
bare `import Mathlib` can never have one, which is why `Diaz.period_plane_norm`,
`Diaz.order_quantisation` and `Diaz.real_quantisation` look isolated. The edges that record *what
a proof cited* are the `sketch` ones, running `cited theorem → submission → proved theorem`, and
they form on `ACCEPTED` submissions just as they do on `SKETCH_ACCEPTED` ones. A first pass here
filtered `kind != 'sketch'`, concluded the nine new nodes were all isolated, and was about to
write that down as a platform limitation. They were not isolated: seven of the nine are attached,
including a three-deep chain `plane_normSq_algebraic_iff → period_plane_classification →
fibre_second_point_is_conj`.

The eighth and ninth are isolated on purpose. `two_failures_give_algebraic_log_product` needs
`Real.exp_add`, `Real.exp_sub` and `IsAlgebraic.{mul,inv,sub}` and nothing else; there is no
published node it consumes. Importing one to draw an edge would have been a lie about the proof,
and a false edge in a public graph is worse than an isolated node.
