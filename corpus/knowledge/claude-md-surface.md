# CLAUDE.md — the conditional always-on surface

Sourced 2026-09-28 (round 6). Seventh instruction-surface class; surveyed to
close the README gap.

## Evidence

- **Loader exists in both harnesses.** `grep -o 'CLAUDE.md'` on the binaries:
  `~/.opencode/bin/opencode` → 9 occurrences, `~/.local/bin/omp` → 17;
  `AGENTS.md` 30/35 respectively, `CONTEXT.md` 1. So CLAUDE.md is a
  *recognized* rules-file name on this host.
- **No captured injection.** The 32 `~/.omp/logs/http-400-requests/*.json`
  system prompts contain `AGENTS.md`/`CLAUDE.md` bytes never (0 hits); no
  session in `opencode.db` (8 distinct directories) or `~/.omp/agent/sessions`
  ever ran inside a directory containing CLAUDE.md. The surface is real but
  **cold** on this host — a latent channel that activates only when a repo
  carries the file.

## File inventory (16 found, `find -maxdepth 6`)
**ROUND-7 DRIFT:** `find ~ -maxdepth 6 -iname 'claude.md' -not -path
'*/node_modules/*'` now returns **18** (5 authored / 1 template / **12**
vendored — +2 vendored since this census). The inventory table below is the
round-6 snapshot; recount before citing.

| Class | Count | Examples |
|-------|-------|----------|
| Operator-authored rules/context | 5 | `~/Projects/HVM4/CLAUDE.md` (66L, headed "# AGENTS.md" — a rename-in-flight), `~/Projects/bounties/pendle-core-v2-public/CLAUDE.md` (21L build commands), `~/Projects/webzites/repos/llm-wiki/CLAUDE.md` (228L agent-identity file), `~/Projects/bounties/george/.../comma-lab/CLAUDE.md` (4339L — extreme outlier, contains dated operator-charter comments and a supreme-rule banner), `~/scratch/msrc-hunt2/fluentui/CLAUDE.md` (118L, nx-workspace generated) |
| Templates / dispatch artifacts | 1 | `~/.local/templates/dispatch/claude.md` (22L, `{{CONTEXT}}` template — a *dispatch prompt* wearing the name) |
| Vendored / package cache | 10 | `~/llama.cpp/CLAUDE.md` (1-line pointer to AGENTS.md), `~/go/pkg/mod/**` (7 files), `~/.bun/install/cache/**`, `~/.local/share/nvim/lazy/aether.nvim/claude.md`, `~/scratch/msrc-hunt2/azure-sdk-for-net/**` |

## Craft rules (surface class 7)

- Same load semantics as AGENTS.md (always-on when present in the repo) →
  same constraint-survival craft rule applies; a 4339-line CLAUDE.md is an
  unconditional tax on every session in that repo.
- **Dual-name collision risk**: repos carrying both AGENTS.md and CLAUDE.md
  (`llama.cpp` resolves it with a 1-line redirect file; `HVM4` has CLAUDE.md
  headed "AGENTS.md") — two files, one channel; pick one owner, redirect the
  other.
- **File-name ≠ loader contract**: `claude.md` under
  `~/.local/templates/dispatch/` is a prompt template, never loaded as rules —
  the name alone does not make a file an instruction surface; the loader does.
- Vendored CLAUDE.md in `go/pkg/mod`, bun cache, plugin dirs are inert
  (never cwd) — count them out of any surface census.

## Open

- Whether omp injects CLAUDE.md content into `session_init.systemPrompt` when
  a session runs in a CLAUDE.md dir is *unverified* — loader strings exist,
  zero in-the-wild sessions observed. Verify by launching a scratch session
  in `~/llama.cpp` or a synthetic dir with a sentinel CLAUDE.md.
