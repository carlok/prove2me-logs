# Gelfond–Schneider, rebuilt as a tree

- **Node** — `Schanuel.gelfond_schneider` (second proof), plus ten new nodes
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.34.0
- **Date** — 2026-09-24

Gelfond–Schneider was on Prove2Me as one submission. It is M. Karatarakis and
F. Wiedijk's formalization (arXiv:2603.24823), ported to the platform: 5,388
lines, every parameter held in one `Setup` structure, nothing reusable by
another proof. The platform's own guide says a helper over forty lines should
be its own node. Carlo asked for the proof to be rebuilt that way: many
reusable theorems, ending at the same statement.

## The tree

| node | lines | what it is |
|---|---|---|
| `Transcendence.liouville_house` | 32 | Liouville's inequality in house form, with an integer denominator |
| `Transcendence.expSum_first_nonvanishing` | 67 | the first non-vanishing derivative of an exponential sum at 1, …, m |
| `GelfondSchneider.common_field` | 39 | `e^l`, `β`, `e^{βl}` in one number field |
| `GelfondSchneider.system_entry_house_le` | 181 | the house of the entries of Gelfond's linear system |
| `GelfondSchneider.aux_coeffs` | 276 | the auxiliary function's coefficients, by Siegel's lemma |
| `GelfondSchneider.deriv_identity` | 74 | its derivatives at the integers |
| `GelfondSchneider.rho_denominator` | 89 | a common denominator for the first non-zero derivative |
| `GelfondSchneider.rho_house_le` | 231 | its house |
| `GelfondSchneider.deriv_upper` | 316 | an analytic upper bound for it |
| `GelfondSchneider.main_estimate` | 196 | `r^((r−3h)/2) ≤ C^r` for arbitrarily large `r` |
| `Schanuel.gelfond_schneider` | 30 | the theorem again, from the last two |

That is 1,531 lines in all. Most of the reduction came from results that
already existed:
- **`FourExp.cauchy_estimate_with_zeros`.** A node from the four exponentials
  subtree. It does the work of about 1,350 lines of the original's
  maximum-modulus argument.
- **`FourExp.expPoly_ne_zero`.** It replaces the Vandermonde block.
- **Mathlib's Siegel lemma over rings of integers.** The original carried a
  278-line fork of it, because Mathlib keeps the lemma's constant private.
  Writing the constant out in public terms makes Mathlib's own lemma usable.
- **Mathlib's analytic-order lemmas.** They replace a 200-line block.

Stating everything in logarithmic form, as the platform's node is stated,
removed a 61-line bridge from the `α^β` form.

The two `Transcendence.` nodes are general. Liouville's inequality with a
denominator is exactly what a helper inside the six exponentials descent step
proves for `c = 1`, so that proof can import it when it is split.

## How

- **Reading.** Two agents read the original. One mapped the proof into seams
  with Setup-free statements. The other compared each general tool with
  Mathlib and with the existing nodes.
- **Checking the design.** Before anything was proved, two outline proofs
  tested it. One was the glue of `main_estimate` against the stubs of the
  others; the other was `deriv_upper` from the Cauchy node. Both came back as
  complete proofs, with no interface mismatch.
- **Proofs.** Six agents wrote the other proofs in parallel.
- **Before publishing.** Each proof matched its statement character for
  character. Chained in one file on v4.34.0 against the mirror's real proofs of
  the reused nodes, all eleven used `propext`, `Classical.choice` and
  `Quot.sound` only.
- **Two changes on the way.** The Liouville node became `liouville_house`,
  because the board already has several unrelated Liouville nodes. And
  `rho_denominator` lost a hypothesis its proof never used.

Every node credits Karatarakis and Wiedijk. Everything published since 24
September 2026 is Apache 2.0 under the platform's terms, which matches their
license.

## On the board and in the mirror

The statements published within two minutes. The proofs followed in four waves:
- the eight nodes with no dependency inside the tree;
- `aux_coeffs`;
- `main_estimate`;
- the second proof of `Schanuel.gelfond_schneider` (submission `697da0e9`).

All eleven were ACCEPTED at the first attempt, each once the nodes it imports read Proved.

In `carlok/diaz-modulus-lean` (`d6f7a41`), `GelfondSchneider.gelfond_schneider` keeps its name and module. It is now 39 lines, over ten new modules, in place of the 5,380-line vendored file, so the six modules that import it are unaffected. The library counts 239 results, all on the three standard axioms.

One porter bug surfaced on the way. It looked up a cited node by declaration name, and `deriv_identity` is also a helper inside a four exponentials module, so the wrong module was imported. A node's module now owns its short name.
