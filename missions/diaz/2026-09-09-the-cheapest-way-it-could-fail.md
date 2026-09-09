# The cheapest way it could fail

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Date** — 2026-09-09

`DiazModulus.recip_pi_exp_value_not_root_of_unity` is **Proved**:
<https://prove2.me/theorems/70537ec3-a818-49a5-a4ea-d4298bf0dbc0>, submission
`3f32a319-3f73-41d1-803b-437377775778`, `ACCEPTED`.

For every non-zero algebraic `γ`, the value `e^{γ/(iπ)}` is not a root of unity. If it had
finite order then `nλ = 2πim`, which forces `γ = −2π²m/n` and makes `π²` algebraic. The mission
already has `DiazModulus.pi_sq_transcendental` Proved, so that input is **discharged, not
carried**, and the node is unconditional.

## Why it is worth a node

`DiazModulus.recip_pi_not_log` and its two children ask for that value to be *transcendental*.
This settles the cheapest way that could fail. On the real-`γ` half it says something concrete:
`γ` real makes `λ` purely imaginary, so `|e^λ| = 1`, and a hypothetical algebraic value would
have to be **an algebraic number on the unit circle that is not a root of unity**. Those exist —
`(3+4i)/5` — so the leaf stays open. What the node does is fix the shape a counterexample must
have, which is the first thing anyone attacking that leaf needs.

It closes nothing, and the node text says so.

## Where it came from, and the run that produced it

From the second LLM, working local-only under a no-publish order. This run was different from
its four predecessors: it put its own round *design* through a review before starting, ran the
duplicate check and the conclusion check before writing any Lean, reported incrementally, and
made zero platform writes. It also found the result was stronger than its own design called for
— no reality hypothesis is needed, so one statement covers both axis halves — and said so.

Its four earlier runs produced, in order: a vacuous node that reached the public graph, a
vacuous local repeat, a redundant-by-composition trio, and another vacuous-plus-redundant pair.
The difference is not the model. It is that the brief acquired the two gates and the
proposal-not-publication rule, and that a human read the output before anything became
permanent.

## The gates, run rather than asserted

- **Duplicate.** `q=root_of_unity` → zero rows. `q=torsion` returns `Diaz.torsion_dichotomy`,
  which was fetched and read: it characterises `Im u ∈ πℚ` by a power of `exp u` being real —
  a different statement.
- **Conclusion.** Nothing on the mission proves this value is not a root of unity.
- **Value.** It narrows the counterexample shape on the leaf we most want strangers working on.

Five nodes published on this mission in three days failed one of the first two tests. This one
and `diaz_of_sfe` are the two where running them justified publishing.
