# Some published targets can never be proved by anyone, and it is worth knowing which

Swept 2026-09-07 across all 4018 Open theorems on the platform. Of those, 2988 are
`lean_workbook_*` in environment `777aaa6`, the vein already recorded as largely
unprovable as stored (`lean-workbook-dead-vein.md`).

Chasing every remaining classical-sounding name turned up a category worth naming
separately: **targets whose own module does not compile**. No submission can succeed
against these, however good the proof, because the failure is in the published
statement rather than in anything a solver writes.

## The four confirmed cases

| target | why it cannot be closed |
|---|---|
| `Basel_Problem` | preamble lacks `open Real`, so `π` is an unknown identifier and the target module itself fails to compile |
| `Sum_of_Angles_of_Triangle…` | same `π` problem |
| `huang_base_case` | its preamble imports `Theorems.Thm_huang_entry_sketch_def`, which exists only as a Definition — permanently unbuildable |
| `Inverse_Completion_of_Integral_Domain_Exists` | elaborates with `K : Type u_2` independent of `D : Type u_1`, so it asks for a field in an arbitrary universe receiving an injection from `D`. Not provable. Zero submissions. |
| `Unique_Factorization_Theorem` | `[EuclideanDomain D]` carries its own `CommRing` instance, disconnected from the `[CommRing D]` the goal uses. What is left is "every commutative domain is a UFD", which is false. Zero submissions. |

These were reached independently and then found to match verdicts already recorded in
`missions/bs-easy-777/NOTES.md`. Two passes agreeing is the reason to trust them.

## One statement that is false, and still not worth disproving

`Triangle_Angle_Side_Angle_Equality` (`517b6655`, environment `777aaa6`) is **false as
stated**: `a, c, d, f` are unconstrained reals with no link to the angle hypotheses,
so `a = d` does not follow. It is also unverifiable for the same `π` reason as the
others, so a `Disproved` attempt cannot land either. Recorded rather than attempted.

## The general shape

A `WA` verdict carrying both `Unknown identifier '<target name>'` and
`Unknown constant '_check'` is the signature of a target whose preamble declares
constants inline that the verifier does not prepend — a different failure, seen on
`WangSun.Main`, and equally unfixable from the solver's side.

Both categories share a lesson: **before investing in a target, build its statement
locally with `sorry` and confirm the module compiles at all.** It costs one build and
it is the only way to tell "hard" from "impossible".
