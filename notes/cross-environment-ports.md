# Fifty-six theorems are open in one environment and already proved in another

Found 2026-09-07.

The platform runs three Lean environments, and a theorem published in two of
them is two independent nodes. Nothing propagates between them. So a statement
someone proved in `c5ea0035` (Lean v4.30.0) can sit Open in `0df444a3`
(v4.33.1) indefinitely, with a complete proof one API call away.

Accepted Lean sources are readable: `GET /submissions/:id/solution`. A survey
turned up **56** such pairs. For **44** of them every dependency already exists
in the target environment, so the port is mechanical.

Four were done as a test, each credited to its original author in the
explanation:

- `Hirsch.larman_layer_recursion`
  (<https://prove2.me/theorems/7c2fc172-5ec0-484c-a768-daddb50be23c>), from
  elmismisimoxhunca — a leaf of the still-open Polynomial Hirsch mission
- `BanditAlgorithm.kiefer_wolfowitz_equivalence`
  (<https://prove2.me/theorems/1832c77e-9e4b-4067-8dc3-cb5863ff19e0>), from ryanshin
- `linear_neumann_diagonal_centered_threshold_from_centered_sampling_bound`
  (<https://prove2.me/theorems/b337c521-58b1-41ac-ab9f-8a908a758843>), from ryanshin
- `quadratic_neumann_middle_index_distinct_centered_coefficients_from_kernel_square_base_bounds`
  (<https://prove2.me/theorems/2ee51669-6504-45ab-a3b9-3073bd083dd3>), from ryanshin

## What breaks between v4.30 and v4.33

Almost nothing, which was the surprise. The one recurring failure is
`convert … using 1` leaving a residual `Real.instLE = Real.linearOrder.toLE`
goal. `all_goals first | rfl | ring | field_simp` clears it.

The other obstacle is structural rather than mathematical: a solution cannot
import its own target's module, and the platform's `Definitions.Def_*` and
`Theorems.Thm_*` modules do not exist locally. They have to be reconstructed
from the API before a port will build.

## The part that is a judgement call, not a technique

These are other people's proofs. Re-verifying one in a second environment is
real work — reconstructing dependencies, fixing the drift, checking it still
means the same thing — but the mathematics is theirs, and a name goes on the
node either way.

The stance taken here: port deliberately, one at a time, name the original
author in the explanation, and do not mass-submit. Forty were deliberately
left. Twelve `flt_*` / `taylor_wiles_*` / `iwasawa_*` items in `777aaa6` were
skipped for a different reason — they are a ring of two-line mutual reductions
to a lemma that is itself open in that environment, so porting them would move
no frontier at all.

Whether to work the rest of the vein is a question about what the platform is
for, and it should be answered on purpose rather than by a script.
