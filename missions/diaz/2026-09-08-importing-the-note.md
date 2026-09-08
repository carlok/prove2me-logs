# Two statements from the author's own note, and a settled question about how they relate

- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-08

## What was proved

`DiazModulus.ringHom_preserves_linearIndependent`
(<https://prove2.me/theorems/158e34f1-5f59-4fbb-9bd1-2247d24b9e5a>) — a ring homomorphism
`ℂ → ℂ` fixing every algebraic number preserves `Q̄`-linear independence **in both
directions**.

`DiazModulus.exp_I_transcendental`
(<https://prove2.me/theorems/612d7e08-2e29-4148-98bd-832d416517c2>) — `exp i` is
transcendental.

Both ACCEPTED, zero `sorry`.

## Where they come from

The mission author keeps a note predating this mission, whose numbered statements are
mostly already on the platform as the `Diaz.*` companion nodes — `transcendental_of_candidate`,
`exists_transcendental_on_circle`, `candidate_no_vanishing_coeff_Qbar`, and the note's main
theorem as `candidate_indistinguishable`. Two things in it were not.

`exp i` transcendental is the note's **comparison point**. The transfer argument sends a
hypothetical counterexample `u` with `|u| = r` to the ordinary circle point `t = r·exp i`,
and its force is that `t` is unremarkable. Transcendence of `exp i` is what makes `t`
transcendental over `Q̄`, which is what the Steinitz extension needs.

The note is careful about something worth repeating: **nothing is claimed about `exp t`**.
If `exp t` were algebraic then `t` would itself be a counterexample, so asserting its
transcendence would be asserting an instance of the conjecture.

The independence lemma is not in the note as a numbered statement, but it is the step its
transfer corollary needs, and it is what settles the question below.

## The question that was settled

Does this mission's `sixExponentials_cannot_refute_candidate` follow from the author's
transfer principle? Earlier writing here called the principle "the general form" of the
no-go, which was right about kind and **wrong about logic**.

**It does not follow, and neither implies the other.**

The no-go's third clause is quantified over *every* complex `u`, with no hypothesis of
being a counterexample. A statement about all `u` cannot follow from one about
counterexamples only. Its proof never uses the hypothesis: independence of the rows gives
a ratio `s ∉ Q̄`, the scaled column span is forced to equal the certificate space, that
space is stable under `s`, and a finitely generated `Q̄`-submodule of `ℂ` stable under
multiplication by `s` makes `s` integral, hence algebraic. Candidacy enters only in the
node's first clause, to certify that the span sits inside `ℒ̃`.

**What the lemma does establish is that the two compose.** Since `Φ` fixes `Q̄`, is
injective, and satisfies `Φ(conj u) = conj(Φ u)`, it carries
`span_Q̄{1, u, conj u}` into `span_Q̄{1, t, conj t}` and preserves independence exactly. So
a six-exponentials template at a counterexample would produce one at `t = r·exp i`.
Transfer would therefore reduce the no-go from all counterexamples to that single explicit
point — a genuine reduction, redundant only because the no-go already holds
unconditionally.

They are independent results about one phenomenon. **Transfer is broader**: it rules out
every vanishing statement with algebraic coefficients over `Q̄(u)`. **The no-go is
quantitative**: it gives the threshold `dim = 3` that explains why the strong four
exponentials conjecture suffices where ordinary six exponentials cannot.

## What is not proved

Neither node is new mathematics. `exp i` transcendental is classical and one line from
Hermite–Lindemann. The independence lemma is elementary; its only content is that a ring
homomorphism out of a field is injective, which is what makes the backward direction work
and without which the composition above would fail.

The transfer principle itself is the author's and predates this mission. What is
contributed here is the checked bridge and the settled implication question — previously
recorded in this repo as an open question, now answered.

## What remains open

Both leaves, unchanged. And the note's general coefficient-transfer corollary is on the
platform only in its specialised form, for the specific `2×2` matrix `Hmat u r`. The
general statement — any matrix over `Q̄(u)`, any algebraic coefficient vectors — is still
unformalised and would be the next thing to import.
