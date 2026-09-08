# Task: Prove2Me corpus → readable artefacts

Build a generator that turns a Prove2Me user's theorems into things a human can read: a
browsable set of pages, a LaTeX document, and a graph picture. Then rank them.

Self-contained and path-free. Every input is a public URL or a documented endpoint. **No
API key is needed for reading** — if you find yourself wanting one, you are doing something
this task does not ask for.

Run it from a clone of `https://github.com/carlok/prove2me-logs` on any host.

## Why this exists rather than an export button

The platform's maintainers have said an export feature is their top request and is being
built. This is deliberately a **thin generator over the public API**, not a competitor to
that. When their export ships, most of this should be deleted.

## Inputs

Base URL `https://prove2.me/api/v1`.

| endpoint | gives |
|---|---|
| `GET /users/<uuid>` | `submitted_problems` and `solved_problems`; each entry has `theorem_id`, `theorem_name`, `status`, and solved ones a `submission_id` |
| `GET /theorems/<uuid>` | `formal_statement`, `preamble`, `natural_language_statement`, `status`, `tags`, `mathlib_rev` |
| `GET /submissions/<id>/solution` | `content` — the accepted Lean source |
| `GET /theorems/<uuid>/graph` | `nodes` and `edges` |
| `GET /theorems?tags=<tag>&limit=300` | catalogue slice by tag |
| `GET /theorems?q=<fragment>&limit=200` | catalogue slice by name fragment |

A theorem row also carries `created_by` and `created_by_username`, which is how to tell
whose node a given statement is.

Reference user: `carlok`, uuid `fca9fd8a-84f4-46ca-8845-a4a2b665381d`.

### Two API traps, both confirmed the hard way

- **Filter names with `q=`, not `search=`.** `GET /theorems?q=<fragment>&limit=200` works.
  **`search=` is silently ignored** and returns the unfiltered catalogue — 62 000+ rows —
  so a `search=` query looks empty and means nothing.
- **A tag query does not see every family.** `tags=diaz-modulus-lean` returns the `Diaz.*`
  nodes and *not* the `DiazModulus.*` ones, though both belong to the same work. Any
  completeness claim must be checked against a full catalogue page plus a client-side name
  filter.

## Part 1 — the generator

Two selection modes.

**By user.** Everything a given user published or proved.

**By reachability.** Everything reachable from a root node, regardless of author — the
"all the non-standard-Mathlib theorems behind this conjecture" view. A graph walk from the
root, following edges, collecting every node it meets.

Three outputs from whichever selection:

1. **Browsable pages.** One Markdown file per theorem: title, natural-language statement,
   `formal_statement`, the accepted Lean source, status, and links to the platform. An index
   grouped by mission or tag.
2. **LaTeX.** One document of the selected theorems, grouped, each as a numbered environment
   with its statement. Compilable.
3. **A graph.** Graphviz `.dot` of the selected subgraph, rendered to SVG. Distinguish
   Proved / Open / Definition, and mark which nodes are leaves.

Requirements: idempotent — rerunning changes nothing if the platform has not; every claim
traceable to an endpoint; no credentials anywhere in output.

## Part 2 — the ranking pass

Once the corpus is generated, walk it and rank each theorem:

- **trivial** — follows in a line or two from its neighbours
- **folklore** — standard, would be in a textbook or is an exercise
- **possibly novel** — no source found for it
- **useful for X** — names what it feeds

Two constraints, and they matter more than the ranking.

**Read `diaz/novelty-search-result-claude-opus-5-2026-08-28.md` first**, in the author's own
working directory. A novelty search already exists and nobody has consulted it. Re-asking a
settled question wastes effort and risks contradicting a prior finding.

**"Possibly novel" is the strongest verdict available.** The local sources are Diaz 2007 and
little else. Waldschmidt's *Variations* papers, his book, and Roy–Waldschmidt 1995 are not
held. A ranking pass **cannot** establish novelty and must not claim to. Where a theorem's
own node text already cites a source, carry that citation into the ranking rather than
re-deriving it.

## What not to do

- Do not poll or write anything requiring authentication. This is a read-only task.
- Do not publish nodes, submit proofs, or modify anything on the platform.
- Do not email anyone. In particular do not contact Michel Waldschmidt, Guy Diaz, or their
  collaborators — a standing instruction from the repository owner.
- Do not assert a theorem is new. See above.
- Do not reimplement what the platform's own export will provide once it ships.
