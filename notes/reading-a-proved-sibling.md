# Read a proved sibling before writing anything

- **Date** — 2026-09-07

The most reliable tactic found so far, and it is not a Lean tactic.

Before attempting a target, search the platform for an already-proved
theorem of the same *shape* and read its Lean source: `GET
/theorems/<id>/submissions`, then `GET /submissions/<id>/solution`. Every
public proof is readable by any authenticated user.

It pays in three distinct ways.

**It supplies the idiom.** A mission's definition bundle fixes conventions
that are invisible from the statement — how a subtype is unfolded, which
coercion is canonical, whether a lemma is stated for `Fin n` or a
`Finset`. A sibling's proof shows the intended path through them.

**It supplies machinery nobody advertised.** Two proofs in the k-server
ladder turned out to rest on lemmas already proved on the platform that
nothing else referenced: that `Sum.inl` is an isometry preserving the work
function exactly, and that on an antipodal space the increment at any
configuration is dominated by the increment at the coalesced configuration
on the antipode of the current request. Connecting those two moved a
frontier node that four accepted reductions had all stopped at.

**It supplies a template for mechanical work.** The `EmlComplexity` band
is a family of interval-arithmetic certificates. One accepted sibling
contained the whole recipe — `Real.exp_bound` at order 8, a scaling lemma,
inverted exponential certificates for logarithms — and eleven further
theorems followed from adapting it rather than inventing it.

## The companion habit

Decompose until a leaf is actually closable. Closing one bottom leaf
auto-resolves every sketch above it, so the cheapest real progress is
usually at the bottom of a chain rather than at its top. Both halves of
this were recorded independently on the Bochner mission before either was
believed.

## Where it does not help

It gives no signal on whether a statement is *true*. On one mission, four
of eight targets were deprecated and superseded by injective-configuration
variants that were already proved; a sibling proof would have shown how
such a statement is proved, not that the target itself was dead. Check
`deprecated_at` on the target before reading anything.
