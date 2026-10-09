# Mission sequence

A short sequence of missions to captain, sized so that proving the leaves ourselves, before release, is about 400 first-accepts, with one optional block that brings it to about 520. Nothing here is uploaded. This note is the plan.

## How a private shot scores

Global trust goes up by 1 for each theorem we are the first to accept. A definition adds nothing on that board, and neither does an accepted sketch: the target stays open, so the sketch is not a solved problem.

A proposal with `visibility` set to `private` does not wait on a moderator. After each draft item is confirmed, one click on **Submit Proposal** compiles and publishes the whole tree. The mission goes live as private, visible only to us. Verification is the ordinary pipeline, so those accepts count while the statements are still hidden.

**Make public** is permanent. The goal, the milestones, and everything they depend on become public at that click. A moderator then reviews the goal and the milestones. If the mission is sent back, it stays private, but the theorems that were released stay public.

A textbook is a series of capstones under one namespace, not one mission full of lemmas. The name of each mission is `{Series} {n}: {capstone}`.

## The missions

Estimated first-accepts assume we prove the leaves ourselves before release. Definitions are not counted.

### WorstCaseEq I: Theorem 3

About 50 theorems. Namespace `WorstCaseEq`.

Source: Elias Koutsoupias and Christos Papadimitriou, *Worst-case equilibria*, journal version, 2009, PDF pp. 2–5. `n` agents with weights `w_i` choose one of `m` identical links. A mixed profile is a tuple of lotteries. The social cost is the expected makespan. The contribution probability `q_i` is the probability that agent `i` sits on the lexicographically first link of maximum load.

The goal is the pair of identities in the proof of Theorem 3: the social cost equals `∑ q_i w_i`, and the expected cost of agent `i` equals `w_i` plus a sum of collision probabilities times the other weights. Formalizing that proof is the point of the mission. The load-balancing game is the base object for the price-of-anarchy literature on identical links; without these two identities the later ratio bounds have nothing to talk about.

The vocabulary is already on disk: `envs/prove2me_ws2/Definitions/Def_agt_games.lean` and `Def_WorstCaseEq_Identical_Model.lean`. `missions/carlok-projects/NOTES.md` only records one-off board items. This mission is the first real home for that model.

### WorstCaseEq II: The golden-ratio bound

About 40 theorems. Same namespace, same paper.

The goal is the two-speed bound: when the speeds are `s₁ ≤ s₂ ≤ φ s₁`, the relevant cost ratio is at most the golden ratio `φ`, with equality on the boundary `s₂ = φ s₁`. The scalar inequality `R_le_goldenRatio` is already accepted as an orphan. This mission puts that inequality back under the model, next to the Nash condition and the link costs it is about. Downstream, it is the sharp constant people quote for two-speed identical links.

### AvramDividend I: The barrier strategy

About 60 theorems. Namespace `AvramDividend`.

Source: Florin Avram, Zbigniew Palmowski, and Martijn Pistorius, *On the optimal dividend problem for a spectrally negative Lévy process*, arXiv:math/0702893. The object is a spectrally negative Lévy process and a dividend strategy. The constant barrier `π_a` pays nothing at time 0 and, for `t > 0`, reflects the process at level `a`, with a lump sum when the initial capital already sits above `a`. The payment-time set is `[0, σ) ∪ {0}`.

The goal is the barrier identities themselves: the formula below the barrier, the formula above it, and the description of the payment times as a union of truncated horizons. Those are the lemmas the scale-function arguments in the paper call without proof. The definitions are already under `Def_AvramDividend_Classical_*`.

### GouldBinomial I and II

Two missions, about 120 cited identities each, plus a shared handful of binomial lemmas. Namespace `GouldBinomial`. Together about 250 first-accepts.

Source, in order of preference: one numbered block of Henry W. Gould, *Combinatorial Identities* (Morgantown, 1972); if that block is not in hand, one numbered exercise block of Graham, Knuth, and Patashnik, *Concrete Mathematics*, chapter 5. Each mission is one such block. Every theorem carries the Gould number, or the book’s exercise number, in `source`.

The structural lemmas (symmetry, Vandermonde, the generating function for a single row) are the milestones. The numbered identities are the leaves. This is worth formalizing because those tables are still how people check a binomial sum, and a checked Lean statement is a better lookup than a scanned page. It is not a generated range: an identity with no printed number does not enter.

## Launch order

1. WorstCaseEq I, then WorstCaseEq II. The second imports the model from the first.
2. AvramDividend I. Independent of the link games; it can be drafted in parallel, and it launches after the two WorstCaseEq missions so the private queue stays one series at a time.
3. GouldBinomial I, then GouldBinomial II, only after the supporting binomial lemmas in I have been accepted.
4. Optional, and only after I and II have been audited: GouldBinomial III, another cited block of about 120 identities. That is the step from about 400 first-accepts to about 520. It is the only place the sequence grows, and it grows by another numbered block.

Each mission is a private proposal. Definitions come first in `item_order`. We prove the leaves, then the human releases it.

## Audit gates

A draft item stays in the proposal only if the Lean statement matches the cited line, including side conditions the source uses silently. For Gould and Concrete Mathematics, any identity whose natural `Nat` subtraction turns a true integer identity into a false one is dropped or restated in `ℤ` or `ℚ`, and the source line is quoted either way. No index is added because a pattern would accept it. Milestones are the lemmas the source actually uses, not a sample of the leaves.

## Left out

BookProof, including the spin-statistics matrices, stays with its captain. Diaz, the Hadamard conjecture, and Collapsible Cubics are not in this sequence. A third Gould mission is not opened unless the first two have passed the audit above. A one-parameter family, such as the sum of the first `n` integers for `n = 1, 2, …`, is not a mission in this sequence.
