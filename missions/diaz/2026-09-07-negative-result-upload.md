# A finished Lean repository transplants to 33 addressable nodes

- **Mission** — none. A standalone node set carrying the shared tags
  `diaz-modulus-lean` and `number-theory`
- **Environment** — `0df444a3` (Lean v4.33.1)
- **Date** — 2026-09-07

`carlok/diaz-modulus-lean` is a completed formalization of a negative
result about Diaz's modulus conjecture: for a hypothetical
counterexample `u`, complex conjugation on `Q̄(u)` is a rational
function of the generator, so no vanishing-coefficient statement over
`Q̄ ⊕ Q̄u ⊕ Q̄ū` can distinguish a candidate from an ordinary
transcendental point on the same circle. The repository was already
finished. This entry is about moving it onto the platform intact, and
about the four things that turned out not to be as briefed.

## What was proved

Nothing new. The mathematics is the repository's, at commit
`801802b8ac052dff50baf17ac4a7ceac3e994ca9`. What is stable is the
transplant: **33 items** — 4 Definitions, 29 theorem nodes and 28
accepted solutions — published with zero failures. Of the 29 nodes, 21
are Proved with an ACCEPTED solution and 8 are Open; 7 of those 8 carry
a SKETCH_ACCEPTED reduction and the eighth has no solution at all.

The headline is `Diaz.candidate_indistinguishable`
(<https://prove2.me/theorems/3592d95c-2f6b-4a36-9888-290e1e3a2c0e>),
Open with a sketch over `exists_conj_intertwining`,
`exists_transcendental_on_circle` and `transcendental_of_candidate`.

The four definition bundles:

- `Diaz_Closure` (`Diaz.hull`) —
  <https://prove2.me/theorems/2ee5c94b-018b-49b4-ae02-d42664b255f8>
- `Diaz_Rigidity` (`Diaz.Hmat`) —
  <https://prove2.me/theorems/26cf7c4e-3390-4a00-9d7e-cfa989b22309>
- `Diaz_Exponential` (`Diaz.Exp0`) —
  <https://prove2.me/theorems/f21898c0-3000-4c3f-b7dd-5a2ef2c876d7>
- `Diaz_Instantiation` (`Diaz.Qbar`, `Diaz.QbarIsAlgebraic`) —
  <https://prove2.me/theorems/9aadbc99-cffa-47ee-9410-69fa01e3bca2>

The eight Open nodes:

- `Diaz.exists_ringHom_of_transcendental` — no solution submitted;
  <https://prove2.me/theorems/7bbf5261-1a2e-4517-86c7-6a029b955652>
- `Diaz.transcendental_of_candidate` —
  <https://prove2.me/theorems/3cae2e48-64f1-4be8-be0d-69719a233f94>
- `Diaz.exists_transcendental_on_circle` —
  <https://prove2.me/theorems/83d7590f-ae1f-41f8-a2e1-62ec6b6dfd49>
- `Diaz.exists_conj_intertwining` —
  <https://prove2.me/theorems/55b6e9a4-5357-482b-82d0-eae88a18a1ac>
- `Diaz.four_nodes_candidate` —
  <https://prove2.me/theorems/6f338e64-261b-4533-b300-c115e5c81804>
- `Diaz.candidate_no_vanishing_coeff_Qbar` —
  <https://prove2.me/theorems/16400e12-6f0a-4e53-b7b6-bcf77ad662da>
- `Diaz.exists_transcendental_on_circle_Qbar` —
  <https://prove2.me/theorems/d5fd3edc-e2b3-4ce8-81fe-0031219b2b44>
- `Diaz.candidate_indistinguishable` — as above

The remaining 21 nodes are Proved and axiom-free, both in the source and
on the platform; they are listed by the tag `diaz-modulus-lean`.

## How

The interesting part is the method, not the mathematics.

**Both `axiom`s were turned into platform nodes rather than uploaded as
axioms.** `Diaz.hermite_lindemann` is consumed by exactly one
declaration, `Diaz.transcendental_of_candidate`, and every other
Hermite–Lindemann-tainted theorem reaches it through that one; so that
declaration was promoted to a node and its solution imports the existing
platform node `DiazModulus.hermite_lindemann_holds`
(<https://prove2.me/theorems/fdc68131-2e60-4005-9489-8758a2174325>),
which is itself Open. The Steinitz axiom
`Diaz.exists_ringHom_of_transcendental` is consumed only by
`Diaz.exists_conj_intertwining`, and was published first as an Open node
under its own repository name and statement, so that its consumer's
proof transplants verbatim.

Both promotions are deliberate departures from the playbook, which would
have inlined a 2-line and a 4-line proof. Promoting them is what turns
"this project assumes an axiom" into a visible edge of the dependency
graph: exactly 7 of the 28 solved nodes are Open-with-sketch, and every
one of them reaches an assumption through one of those two. Inlining
would have scattered the imports across six solutions and hidden the
structure. The 26 helpers that stayed below the threshold are still in
the upload — pasted verbatim into each consumer, each inside its own
`section` with its own module's `open`s and `variable` prefix — just not
separately addressable.

Generation was skeleton subtraction driven entirely by two extraction
passes over the elaborated environment, with **no text search anywhere**:
proof cuts come from the meta-program's `valStart`, docstring strips
from its recorded `docstring` range, and the declaration-name rewrite
from the binding's `ref` range.

The validation gate, all green before a single upload call:

1. All 4 Definitions, 30 Theorems and 28 Solutions compile under Lean
   v4.33.1 against the platform's vendored Mathlib, with no errors and
   no warnings. Solutions are `sorry`-free, and none imports its own
   target.
2. The pretty-printed elaborated type of all 28 transplanted nodes is
   **byte-identical** between the original tree and the staged tree —
   no differences at all, not even universe display names.
3. Type and value of all five definition-bundle declarations are
   byte-identical between the two trees.

The uploader records each job or submission id before polling, so an
interrupted run resumes rather than duplicates.

Four things in the brief were wrong, and were corrected against the
repository rather than trusted:

- The pinned commit's `lean-toolchain` is **v4.32.2**, not the v4.33.1
  claimed. All eight modules do compile unedited under the platform's
  v4.33.1, but that is a verified coincidence, not a pin.
- **`Diaz/Palomar.lean` does not exist at `801802b`.** It lives only on
  the divergent branch `palomar`, which is neither an ancestor nor a
  descendant of the pinned commit. The pre-built local tree was that
  file grafted onto the master files. Its two theorems,
  `exists_algHom_of_transcendental` and `coeff_indistinguishable`, are
  the only content excluded, and excluding them is correct: they have no
  source link at the commit the whole upload cites.
- Declaration counts are 55 total, split 44 clean / 9 Hermite–Lindemann
  / 1 Steinitz / 1 both — not 56 and 45. The extras were Palomar's. The
  split was verified independently with `#print axioms` over all 55; no
  `sorryAx` anywhere.
- **The two Hermite–Lindemann statements are not defeq.** The published
  node is *`a ≠ 0` algebraic ⟹ `eᵃ` transcendental*; the repository
  axiom is *`u ≠ 0`, `eᵘ` algebraic ⟹ `u` transcendental*. They are
  contrapositives, classically equivalent, and the repository direction
  follows from the published one in two lines. The reduction is sound,
  but it is a derivation, not a restatement.

## What is not proved

No case of Diaz's conjecture, and no new theorem. The transplant
preserves statements; it does not strengthen them.

Eight of the 29 nodes are Open. Seven of them are Open *with an accepted
sketch*, which means the reduction was checked and the assumption was
not: each reaches either Hermite–Lindemann or the Steinitz extension.
That is exactly the set the source project's own `#print axioms` sweep
flags, projected onto the node set — no more and no fewer.

The elaborated-type diff certifies statement fidelity and nothing else.
It does not certify that the platform's build of a proof is the
repository's build of it, and it says nothing about the two proofs that
were never uploaded.

The compile of the repository under v4.33.1 was checked, not pinned.
Nothing prevents a future revision of the platform's Mathlib from
breaking modules whose declared toolchain is v4.32.2.

## What remains open

`Diaz.exists_ringHom_of_transcendental` is a genuine Open node with no
solution: the Steinitz extension of a ring homomorphism along a
transcendental element. Closing it discharges the sketches on
`exists_conj_intertwining` and `candidate_indistinguishable`.

`DiazModulus.hermite_lindemann_holds` is the other assumption, and
`leanprover-community/mathlib4#28013` would discharge it if it landed.
Closing it collapses the sketches on six of the seven.

The two Palomar theorems remain outside the upload, and will stay there
until they are on a commit the upload can cite.
