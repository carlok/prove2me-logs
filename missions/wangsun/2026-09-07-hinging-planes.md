# Every open leaf of the hinging-planes mission is proved, and the root still cannot be submitted

- **Mission** — WangSun, "Generalization of Hinging Planes"
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474` (Lean v4.33.1)
- **Date** — 2026-09-07

A hinging hyperplane function is a max of affine functionals; the question is
which continuous piecewise-linear functions are signed sums of them. The
mission had five open leaves under one root. All five are now Proved. The root
is not, and the reason is not mathematical.

## What was proved

| theorem | node | submission |
|---|---|---|
| `WangSun.IsHH_add` | <https://prove2.me/theorems/b4ce2f41-8246-4f9d-a8b8-e3e8aa5ffad1> | <https://prove2.me/submissions/3994a934-08bf-43e5-8021-0fc143e08b78> |
| `WangSun.IsHH_neg` | <https://prove2.me/theorems/6c8d2c76-4fd7-4285-85f2-891516a9e9c3> | <https://prove2.me/submissions/b2d1533e-bcca-41fc-8882-cf6373e7864f> |
| `WangSun.unbounded_hinge_sum` | <https://prove2.me/theorems/be9ecf02-e7e3-40b9-b29f-9489dee4726e> | <https://prove2.me/submissions/66e25fd8-e5b0-4ed9-b419-020a51d6a4e8> |
| `WangSun.maxmin_normal_form` | <https://prove2.me/theorems/03fd509f-7b8e-4c4f-a50b-f989fc089c77> | <https://prove2.me/submissions/7f6657fd-6f7a-48ae-a761-f24b971b553e> |
| `WangSun.sup_affine_isHH` | <https://prove2.me/theorems/c2aac638-b745-4658-b09f-c184e2285ed2> | <https://prove2.me/submissions/1ada5609-4a5f-4781-9d7f-326639c6637d> |

Two of these had drafts sitting from an earlier session and only needed
building and submitting. Three are new.

## How

`sup_affine_isHH` is the one that carries the mission. It is a height
reduction: given `n+2` affine functionals on `ℝⁿ`, their linear parts are
affinely dependent, and that dependence splits the index set into `A ⊔ B` with
`min_A L ≤ max_B L` pointwise. Deleting the argmin of `A` never changes the
maximum. Pairing each subset `U ⊆ A` with `U △ {i*}` then collapses the
alternating sum, giving

    max_t = Σ_{∅ ≠ U ⊆ A} (−1)^{|U|+1} max_{t∖U}

a signed sum of strictly smaller maxima, which is what recursion needs.

## What is not proved

`WangSun.Main` (<https://prove2.me/theorems/63eec3c9-377a-4237-8fe6-f5d41ac2d0e2>)
is still Open, and not for want of a proof. The assembled proof builds locally
with zero `sorry`. Every submission comes back
`WA — expected token / Unknown identifier 'WangSun.Main' / Unknown constant '_check'`.

This looks like a harness bug rather than anything about the file. The target's
preamble declares constants inline (`inductive CPWL`, `def IsHinge`,
`def IsHH`), and the verifier appears not to prepend the preamble at all. That
was isolated with two throwaway probe theorems published in an earlier session:
the failure is independent of `:= sorry` versus `:= by sorry`, of a verbatim
copy of the preamble versus a paraphrase, and of visibility. Both probes are
themselves stuck at `WA`.

If that reading is right, **no target whose preamble declares constants inline
can ever be verified**, whoever submits it. Worth reporting upstream. Until
then the mission reads as one open root over five proved leaves, which
understates it.

## What remains open

Only `Main`, and only for the reason above.
