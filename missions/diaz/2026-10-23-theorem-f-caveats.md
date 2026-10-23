# Theorem F and Theorem E agree, and a rank-two claim corrected
- **Mission** — Diaz's modulus conjecture, `3045e100-83a7-4863-9c02-21f90105f182`
- **Environment** — `0df444a` (Lean v4.33.1); mirrored on Mathlib v4.35.0
- **Date** — 2026-10-23

Theorem F (R20, the same day) said which conjugation hulls of a
rational z carry a 2 × 3 configuration. It left three caveats: its
agreement with Theorem E on Laurent z was checked only by computation,
the uniqueness half of its key step was not formal, and no exclusion at
a candidate was stated. This round (R21a) closes all three in 6 nodes.

## What was proved

- **Agreement with Theorem E.** For a Laurent z with a five-dimensional
  hull, Theorem F's shapes D1, D2a, D2b hold exactly when Theorem E's
  classes (P), (Q), (R) do. The explicit maps: (P) is D2a for the
  pencil (X², 1); (Q) is D2b for the pencil (sX, X² + βs²); (R) is D1.
- **Uniqueness.** In Theorem NF's setting, W ∩ h⁻¹W is exactly the span
  of the configuration's products, of dimension 3.
- **At a candidate.** Under Roy's strong six exponentials theorem, a
  rational z whose hull meets Theorem F's criterion is not in ℒ̃.

| theorem | uuid | verdict |
|---|---|---|
| `DiazModulus.laurent_conj_hull_configuration_shape_iff_class` | `0e35095f-1635-43b5-b8be-fb64c275ee02` | ACCEPTED |
| `DiazModulus.candidate_rational_conj_hull_criterion_not_mem_logAlgTilde` | `33dd25ff-3644-4181-b5b2-9c9796bc19be` | ACCEPTED |
| `DiazModulus.degree_two_configuration_multiplier_space_eq` | `aa3a8cfe-98e6-4cfa-a672-a4a36d8ff7fc` | ACCEPTED |
| `DiazModulus.laurent_polynomial_class_conj_hull_two_orbit_form` | `aa05d508-a30f-4f4c-9fe6-893fbb763388` | ACCEPTED |
| `DiazModulus.laurent_involution_class_space_cyclic_form` | `00e48e2c-49f1-4fe9-822b-495d0b8e830a` | ACCEPTED |
| `DiazModulus.laurent_real_pencil_class_space_u_multiplier_triple` | `bf190dc0-3812-4920-8dcc-4e8e2e6fa6a6` | ACCEPTED |

Milestones 155–160 are the six rows: none imports another, so each
joins the mission only as a milestone.

## How

- A design agent wrote the statements and 548 exact checks. Three proof
  agents proved the six nodes in about 18 minutes: 67 to 297 lines each.
  One hypothesis no proof used was dropped. No rejection.
- The agreement is two equivalences put together; the maps are explicit
  identities of spans, checked first by exact computation.

## Found on the way

- **A public claim was too strong.** The research note said Roy's rank
  bound cannot exclude u⁴ at rank two. The search behind it covered
  graded monomial matrices only, and the reduction from all matrices to
  graded ones was not written out: degenerating a matrix can create zero
  blocks. The note now says "no graded matrix" and lists the reduction
  as open.
- **Literature.** Four open sources on products of spaces and on scrolls
  were read for Theorem NF; none contains it. A textbook prints the
  ingredients of the vector-bundle proof, but not the three shapes.
- **Roy's theorem itself.** A public repository by Shawn Krisman, also
  written with Claude, proves it on the same Lean and Mathlib commit.
  It has no licence file, so it is not used; Carlo asked about one in
  an issue on that repository.

## What is not proved

- **Theorem E is not derived from Theorem F.** The agreement uses both
  theorems, and Theorem E's explicit criteria do not follow from F.
- **Roy's theorem is still a hypothesis** wherever the library uses it.
- **Rank three** of Roy's bound is open; a small search of graded
  matrices found nothing.
- **All six results are routine.** None was found in the sources read.

## What remains open

- R21b: visibility of degree-two spaces, and uniqueness of the
  involution.
- Discharging Roy's hypothesis, if a licence for Krisman's proof comes.
