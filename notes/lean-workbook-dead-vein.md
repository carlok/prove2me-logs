# A vein of ~2,240 statements that no proof can satisfy

- **Environment** — `777aaa61…` (Lean v4.29.0-rc3)
- **Date** — 2026-09-07

One Prove2Me environment holds several thousand open theorems named
`lean_workbook_plus_<N>` — competition-style problems in one or two lines.
They look like the richest vein on the platform. Most of them cannot be
proved by anyone, and the reason has nothing to do with mathematics.

## The mechanism

`POST /verify` first builds its own `Theorems/Thm_<name>.lean` from the
stored `preamble` and `formal_statement`. If that module fails to compile,
the submission returns `ERROR` however good the proof is.

The stored preamble on these is usually just `import
Mathlib.Analysis.Complex.Basic`, which is nowhere near enough. Observed
causes: a missing colon (`theorem foo 3! = 6`); no `open Real` or `open
Nat`, so `π`, `sin` and `!` do not resolve; missing imports for
`Real.log`; and free variables that `autoImplicit false` rejects.

## Two ways to measure this wrong, both of which happened

**Batch checking under-reports.** Concatenating many statements into one
file lets a single parse error abort the whole file, so everything after
it is counted as broken. That produced an estimate of *zero* buildable.

**Grepping for errors under-reports the opposite way.** This toolchain
emits diagnostics tagged as `error(lean.unknownIdentifier):`, not the
plain `: error: ` that a naive filter looks for. Missing those inflated an
estimate to *57%*. Use the process exit code, not a grep.

A corrected sample of 60, one file per statement, judged by exit code:
**23% build locally.**

## Even that number is too high

`lean_workbook_plus_66696` — `a - b ∣ P.eval a - P.eval b` — compiles
standalone with bare `lean` against the identical Mathlib revision, and is
closed in one line by `Polynomial.sub_dvd_eval_sub`. The server rejects
it:

```
The environment does not contain `Polynomial.eval`
```

The local Mathlib pin matched exactly, so the difference is the platform's
lake and module build configuration rather than the library. **A local
compile of `preamble + formal_statement` does not predict server
buildability.** The only authoritative test is a real submission.

## Why it cannot be fixed from outside

Repair needs `PATCH /theorems/:id` on the preambles, which requires being
the submitter, a mission captain, or an admin. These theorems are owned by
a platform bot, so an ordinary account cannot touch them.

## What to take from it

Do not point effort at this environment's workbook statements. More
generally: when a vein looks unusually rich, the first question is whether
its targets are *buildable*, and the only way to answer it is to submit
one.
