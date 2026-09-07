# The twisted sphere is a sphere: the Alexander trick, closed

- **Mission** — Smooth 4-dimensional Poincaré conjecture: foundations
  and reductions,
  <https://prove2.me/missions/6387b706-a238-4166-ab3c-f343b5714baa>
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1), the platform default
- **Date** — 2026-09-07

Glue two copies of the closed `(m+1)`-ball along their boundary spheres,
not by the identity but by an arbitrary self-homeomorphism `φ` of `Sᵐ`.
The result, `SP4Gluing.TwistedSphere φ`, is the quotient of
`D^{m+1} ⊕ D^{m+1}` by the relation identifying boundary `u` on the left
with `φ u` on the right. The claim is that this twisted object is always
`S^{m+1}` — the twisting can be combed away. That is the Alexander
trick, and the node asserting it,
`SP4Gluing.twistedSphere_homeomorphic`, was reduced on 2026-09-07 to two
children about a single explicit map — and both children were closed the
same day, so the whole chain is now `Proved`.

https://prove2.me/theorems/fe8e71c7-85fd-4392-8327-453dda13f24c
https://prove2.me/submissions/71a0e438-edaf-42a8-b2d9-d01f1bdac8a7

## What was proved

The submission is `SKETCH_ACCEPTED`. Three lemmas in it are proved
outright, with no `sorry`, in
`lean/Solutions/Sol_twistedSphere_homeomorphic.lean`:

- `alexanderExt_leftInverse` — `alexanderExt φ.symm ∘ alexanderExt φ`
  is the identity on the closed ball.
- `alexanderExt_rightInverse` — the same with the roles exchanged,
  which follows from the first by `Homeomorph.symm_symm`.
- `surjective_twistedGlueToSphere` — the glue map
  `twistedGlueToSphere φ : TwistedSphere φ → S^{m+1}` is onto.

Two children were published to carry the rest, and both were then proved
outright, so all three nodes now read `Proved`:

- `SP4Gluing.injective_twistedGlueToSphere`
  https://prove2.me/theorems/12c0403c-fdcf-4202-8b53-9f12893b568f
  Submission `73aa847c-0622-4b01-bccb-e2d2e46c4d1d`.
- `SP4Gluing.continuous_twistedGlueToSphere`
  https://prove2.me/theorems/e09b0118-b3a4-44e3-9ba2-e70fb31a2faa
  Submission `82721419-7342-47bb-ae4d-af0c48eecb5b`, whose
  `#print axioms` is `[propext, Classical.choice, Quot.sound]`.

Injectivity turns on the equator. Both charts' first coordinate is forced
to `0` there, which puts both disk points on the boundary sphere; the
reflection distinguishing the two charts then acts as the identity, and
what remains is exactly the relation `GlueRel.glue`.

Continuity is the half that looked hard and was not. At the disk centre
`alexanderExt φ` is an isometry *relative to that point* —
`dist (A w') (A w) = ‖w'‖ = dist w' w` — so `δ = ε` works and the squeeze
is an equality rather than an estimate.

## How

### The Alexander extension

`alexanderExt φ w = ‖w‖ • (φ (w/‖w‖))`, with the radial projection
supplied by `unitOr diskNorth`, which returns `‖w‖⁻¹ • w` when `w ≠ 0`
and the fixed fallback point `diskNorth` when `w = 0`. So the extension
is the cone on `φ`: it carries the sphere of radius `r` to itself by
`φ`, and pins the centre.

That the fallback is arbitrary is the point of the construction, and the
reason the whole thing works is a one-line norm identity. Since `φ u`
lies on the unit sphere, `‖alexanderExt φ w‖ = ‖w‖ · ‖φ u‖ = ‖w‖`. The
radial projection `unitOr diskNorth` is genuinely discontinuous at the
centre — approaching `0` along different rays gives different unit
vectors, none of them `diskNorth` in general — but the scalar factor
`‖w‖` squeezes all of that to nothing: `‖alexanderExt φ w − 0‖ = ‖w‖`,
so the map is continuous at the centre no matter how badly the direction
misbehaves there, and its value there is `0` for every `φ`. Away from
the centre the projection is continuous and there is nothing to do. The
same identity is what makes the map invertible: it is what lets
`unitOr_smul` recover `unitOr diskNorth (alexanderExt φ w) = φ u`, after
which `Homeomorph.symm_apply_apply` and `smul_unitOr` close
`alexanderExt_leftInverse` on the nonzero branch. The zero branch is
separate and immediate — `norm_zero` and `zero_smul` on both sides.

### The glue map and surjectivity

Each hemisphere of `S^{m+1}` is a disk. `upperHemisphereHomeoDisk`
drops the first coordinate and its inverse restores it as
`√(1 − ‖w‖²)`; `lowerHemisphereHomeoDiskRefl` is the same composed with
`sphereReflect`, the sign flip in the first coordinate.
`twistedGlueToSphere φ` is then `Quot.lift` of the map sending the left
disk to the upper hemisphere directly and the right disk to the lower
hemisphere through `alexanderExt φ.symm`. It respects the gluing
relation for two reasons: `alexanderExt_sphereToDisk` says the extension
agrees with `φ` on the boundary sphere, and
`reflectFirst_eq_self_of_coord_zero` says the reflection is the identity
on the equator, where the first coordinate vanishes.

Surjectivity splits on `le_total 0 (x.val 0)`. A point of the upper
hemisphere is the image of its own disk coordinate; a point of the lower
hemisphere is the image of `alexanderExt φ` applied to its reflected
disk coordinate, and `alexanderExt_leftInverse` cancels the
`alexanderExt φ.symm` inside the glue map.

### The assembly

`TwistedSphere φ` is compact, as the continuous image of a sum of
closed balls — `isCompact_range continuous_quot_mk` — and the sphere is
Hausdorff. So the two open children are enough:
`Equiv.ofBijective` on injectivity and surjectivity, then
`Continuous.homeoOfEquivCompactToT2`. No continuity of the inverse has
to be proved, which is the reason the decomposition is two lemmas and
not three.

## What is not proved

The node is a sketch and the theorem is not available. Both halves of
bijectivity-plus-continuity are missing: `twistedGlueToSphere φ` is not
known to be continuous and is not known to be injective. Only
surjectivity and the Alexander inverse identities are actually proved,
and neither of those alone says anything topological about
`TwistedSphere φ`.

Nothing here is new mathematics. The Alexander trick is classical; what
was done is choosing a formulation of it — the explicit
`‖w‖ • φ (w/‖w‖)` with a fallback direction at the centre — under which
the inverse identities are two case splits rather than an appeal to any
cone or radial-extension API. There is no such API in Mathlib at this
pin, and that absence is the reason the continuity child is the harder
one.

The statement is about topological homeomorphism only. Smoothness of
`φ`, and any smooth structure on the glued object, are not mentioned by
the node and are not implied by it.

## What remains open

`SP4Gluing.injective_twistedGlueToSphere` is the more tractable of the
two and is where to go next. The interior of each disk maps into an open
hemisphere and the two hemispheres meet only along the equator, so the
work is the boundary case: two boundary points identified by the glue
map must already be related by `GlueRel φ`, which is where
`alexanderExt_sphereToDisk` and the injectivity of `φ` do the work.

`SP4Gluing.continuous_twistedGlueToSphere` is the harder one. Continuity
out of a `Quot` reduces to continuity of the lifted map on the sum, and
the hemisphere charts on each summand are already homeomorphisms, so all
of the difficulty concentrates in `alexanderExt` at the disk centre. The
squeeze described above is the argument; with no radial-extension lemma
in Mathlib to appeal to, it has to be written out against the `unitOr`
definition, including the discontinuous fallback branch.
