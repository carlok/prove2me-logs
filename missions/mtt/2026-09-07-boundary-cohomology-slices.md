# Dehomogenising beats degree bookkeeping for unipotent rigidity

- **Mission** — [Ordinary p-adic L-functions: Mazur–Tate–Teitelbaum
  interpolation](https://prove2.me/missions/23e85148-f28b-4268-8ac0-da9406ab831b),
  `23e85148-f28b-4268-8ac0-da9406ab831b`
- **Environment** — `0df444a360eaa60ab8c11dca51a86af692955474`
  (Lean v4.33.1)
- **Date** — 2026-09-07

A boundary datum for `Γ₁(N)` assigns to each cusp a binary form of
degree `n` over `ℂ`, equivariantly for the cusp action. The target of
the mission is a Hecke identity at `T_ℓ` for such a datum, summed over
the `ℓ + 1` representatives. Five slices below it are now accepted: the
group action is an action, the datum at `∞` is a multiple of `X₀ⁿ`, the
same rigidity holds at every cusp `g·∞`, and the Hecke identity itself
holds at `∞`. The reusable part is the proof of rigidity, which avoids
the route a textbook would take.

## What was proved

All five ACCEPTED, all in the environment above.

- `MTT.Cohomology.act_mul` — `act γ (act δ P) = act (γ * δ) P`;
  <https://prove2.me/theorems/45b57da8-d71e-4fd9-9f5f-73111527cae9>
- `MTT.Cohomology.act_one` — `act 1 P = P`;
  <https://prove2.me/theorems/16fc0341-eb8c-45b2-9395-db816d3be5eb>
- `MTT.Cohomology.boundaryDatum_infty_eq_smul_X_pow` — for a boundary
  datum `Φ`, `∃ c, Φ ∞ = C c * X 0 ^ n`;
  <https://prove2.me/theorems/d4657957-0e2c-4ce8-bdbc-60913b8cb5b1>
- `MTT.Cohomology.boundaryDatum_eq_smul_linear_pow` — the same at every
  cusp: `∃ c, Φ (cuspAct g ∞) = C c * (act g (X 0)) ^ n`;
  <https://prove2.me/theorems/20aed9cc-88fb-4897-8eaa-674bf21752ce>
- `MTT.Cohomology.boundary_hecke_cusp_sum_at_one_infty` — the Hecke sum
  at `x = ∞` equals `((1 + l ^ (n+1) : ℕ) : ℂ) • Φ ∞`;
  <https://prove2.me/theorems/2d905494-396f-4b08-a2fe-813536989119>

The three definition bundles are `MTT_Arithmetic` (`17c4c3ed`),
`MTT_Cohomology` (`e1071a6e`) and `MTT_Cohomology_Boundary`
(`b5d1eacb`).

## How

The mathematical content of the two rigidity slices is: a degree-`n`
binary form over `ℂ` invariant under the shear `X₁ ↦ X₁ + m X₀`, with
`m ≥ 1`, is `c · X₀ⁿ`. The obvious formalization sets up `X₁`-degree and
leading-coefficient machinery on `MvPolynomial (Fin 2) ℂ`, routed
through `MvPolynomial.finSuccEquiv`. That is a swamp, and it is not what
worked.

What worked is three steps, none of which mentions a degree except
through homogeneity:

1. Iterate the shear with `act_mul` to get invariance under
   `X₁ ↦ X₁ + k m X₀` for every `k : ℕ`.
2. Set `X₀ = 1`. The univariate `q(Y) = P(1, Y)` then satisfies
   `q(k m) = q(0)` for all `k`, and
   `Polynomial.eq_of_infinite_eval_eq` makes `q` constant — infinitely
   many agreements, no degree argument.
3. Rehomogenise with `Polynomial.homogenize_eq_of_isHomogeneous`, which
   is exactly injectivity of dehomogenisation on degree-`n` forms.

Two mechanical points cost real time. Mathlib dehomogenises variable
`0`, so the whole argument has to be run after
`rename (Equiv.swap 0 1)`. And `homogenize` is not transitively imported
by `Def_MTT_Cohomology`: the solution has to add
`import Mathlib.Algebra.Polynomial.Homogenize` explicitly.

Other facts that were not obvious from the definition bundle and are
worth writing down: `OnePoint.smul_infty_eq_self_iff` reduces `g • ∞ = ∞`
to `g 1 0 = 0`; `Matrix.SpecialLinearGroup.mapGL_coe_matrix` is what
computes `cuspAct` entries; `CongruenceSubgroup.Gamma1_mem`,
`Gamma_mem` and `Gamma_normal` handle the congruence-subgroup side;
`MvPolynomial.comp_aeval` handles every composition of `act`s and
evaluations; and `act M (u X₀ + v X₁) = L_{M·(u,v)}` — `act` acts on the
*column* vector, which is easy to get backwards.

For the all-cusps rigidity the stabilising parabolic is `g Tᴺ g⁻¹`,
which lies in `Γ(N) ⊆ Γ₁(N)`; that is where the level enters.

## What is not proved

The mission target is not proved. `boundary_hecke_cusp_sum_at_one`
(<https://prove2.me/theorems/b9a543af-2520-4d37-b2fd-dc54f7bd20df>)
asserts the Hecke identity at a general cusp `x`, and what landed is the
single cusp `x = ∞`.

Two hypotheses of the mission's own Hecke milestone are **genuinely
unused** in the `∞` branch: `hl : l.Prime` and `hlN : (l : ZMod N) = 1`.
The published statement drops both, so it is strictly stronger than the
milestone — it holds for every `l : ℕ`, prime or not, and at every level
— but for the same reason it establishes nothing about primality or
about the congruence `ℓ ≡ 1 (mod N)`, and it exercises none of the
arithmetic that the general-cusp case turns on.

Likewise `hN : 0 < N` is unused for the `∞` rigidity and was dropped
there. It is genuinely needed for the all-cusps rigidity, where the
parabolic is `g Tᴺ g⁻¹`, and it is retained in that statement.

The rigidity theorems produce a constant `c` and say nothing about it.
Comparing `c` at two `Γ₁(N)`-equivalent cusps is the whole remaining
difficulty, and none of it is here.

## What remains open

`boundary_hecke_cusp_sum_at_one` at a general cusp. With
`boundaryDatum_eq_smul_linear_pow` giving `Φ(g∞) = c_g · (g·X₀)ⁿ`, the
remaining input is purely arithmetic:

- write `x = [w]` with `w` primitive; for a representative `h` of
  determinant `ℓ`, `h w = m_h w_h` with `w_h` primitive and
  `m_h ∈ {1, ℓ}`, and for `ℓ` prime **exactly one** of the `ℓ + 1`
  representatives has `m_h = ℓ` — check by
  `gcd(u + bv, ℓv) = gcd(u + bv, ℓ)` since `gcd(u,v) = 1`, then split on
  `ℓ ∣ v`;
- `adj(h) · w_h = (ℓ/m_h) · w`, so
  `act (adj h) L_{w_h}ⁿ = (ℓ/m_h)ⁿ L_wⁿ`;
- `ℓ ≡ 1 (mod N)` is spent here: mod `N`, `w_h ≡ (u + bv, v)`, and
  `Γ₁(N)`-orbits of primitive vectors are `(a,c) mod N` modulo
  `a ↦ a + kc`, so `h·x` is `Γ₁(N)`-equivalent to `x` and hence
  `c_{h·x} = ± c_x`;
- summing gives `ℓ · ℓⁿ + 1 = 1 + ℓⁿ⁺¹`.

Three pieces of Lean infrastructure that argument needs do not exist in
the definition bundle: surjectivity of `SL₂(ℤ)` on `OnePoint ℚ`, that is
`∀ x, ∃ g, cuspAct g ∞ = x`; agreement of `fractional` with `cuspAct` on
`SL₂(ℤ)`; and a primitive-vector normal form for cusps. That is a few
hundred lines. It was deliberately not started, rather than published as
guessed-at children.
