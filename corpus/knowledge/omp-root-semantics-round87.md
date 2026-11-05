source: S256 — omp 18.15.0 plugin skill-root reader, `packages/coding-agent/src/discovery/omp-plugins.ts`, read in the installed bun ELF (`/home/vgpnk/.local/bin/omp`, sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`) and re-opened upstream at tag v18.15.0 (HTTP 200, 15 362 B, sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4`); corroborated by S255 for the catalogue render
verified-at: 2026-11-04, host `Linux 7.2.11-arch1-1`, omp/18.15.0, ELF sha256 `6737ee24…b7b0f` (276 785 328 B)
recheck: on-release (re-run `verifiers/check_omp_root_semantics.py --rev <rev>` after an omp upgrade)

# omp skill roots — which code reads each root, and what bounds that reading

The lane's round-86 ledger (`verifiers/omp-skill-roots.tsv`, 12 rows) records *which* roots omp
walks and grounds each with a quote that occurs in the binary. That is a presence floor: the
round-86 non-author closure found (CF1) that for the plugin root **no code quote can satisfy the
round-86 dot rule**, because the ELF contains no `.omp/plugins` literal and the reader is a
`join(...)` call; and (CF2) that `{cwd}/` expansion reaches every ancestor including `$HOME`.
This entry records the stronger thing: the **reader** — the code line that builds the path — per
root, plus the bound each root's expansion obeys.

## Table (12 rows; `reader_quote` verbatim, minified ELF identifiers kept)

| root_pattern | module (ELF) | reader_quote | bound |
|---|---|---|---|
| `{cwd}/.omp/skills` | `coding-agent/src/discovery/builtin.ts` | `dir: fr.join(k, Ou.projectDir, "skills"),` | project-scoped: session cwd only |
| `{cwd}/.claude/skills` | `coding-agent/src/discovery/claude.ts` | `dir: Fr.join(k, eh, "skills"),` | project-scoped |
| `{cwd}/.agent/skills` | `coding-agent/src/discovery/agents.ts` | `x.push(Rs.join(R, _, ...p));` | project-scoped |
| `{cwd}/.agents/skills` | `coding-agent/src/discovery/agents.ts` | `x.push(Rs.join(R, _, ...p));` | project-scoped |
| `{cwd}/.codex/skills` | `coding-agent/src/discovery/codex.ts` | `return Xr.join(u.cwd, ".codex");` | project-scoped |
| `{cwd}/.opencode/skills` | `coding-agent/src/discovery/helpers.ts` | `return d.join(e.cwd, r.projectDir, n);` | project-scoped |
| `{cwd}/.github/skills` | `coding-agent/src/discovery/helpers.ts` | `return d.join(e.cwd, r.projectDir, n);` | project-scoped |
| `~/.omp/agent/skills` | `coding-agent/src/discovery/builtin.ts` | `dir: fr.join(we(), "skills"),` | home root (`we()` = the config dir) |
| `~/.omp/plugins/node_modules/*/skills` | `coding-agent/src/discovery/omp-plugins.ts` | `dir: Zo.join(R.path, "skills"),` | home root; the `*` is the plugin package segment |
| `~/.agent/skills` | `coding-agent/src/discovery/agents.ts` | `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` | home root, expanded over `y1` |
| `~/.agents/skills` | `coding-agent/src/discovery/agents.ts` | `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` | home root, expanded over `y1` |
| `~/.omp/agent/managed-skills` | `coding-agent/src/autolearn/managed-skills.ts` | `return Zm.join(u, "managed-skills");` | home root, autolearn-generated |

Offsets and the mmap commands for every row: `.ufo/waves/round-87/w1/ExecLedger/receipts-elf-reads.txt`.
The counter re-derives each quote and its module ordering from the committed ledger bytes:
`python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` → `omp root semantics grounded 12 of 12`.

## Rules a skill author can act on

- **A root claim is grounded by the code that joins the path, not by a doc string that mentions the
  directory.** The round-86 plugin row's quote `var Gh = ".omp";` is a config-dir constant that names
  no `plugins`, no `node_modules` and no `skills`; it grounds nothing. The reader is
  `dir: Zo.join(R.path, "skills"),` (upstream line 70 of `discovery/omp-plugins.ts`). When you cite a
  client's search path, quote the join.
- **`{cwd}/` walk-up stops below `$HOME`.** A project-scoped root is not a home root: expanding
  `{cwd}/.agents/skills` to `$HOME` would make a user install look like a project install, and the
  two are governed by different opt-in settings. The counter's bound probe pins the expansion set to
  the session cwd and its ancestors strictly below `$HOME` (frozen chain `/home/u/proj/sub` →
  `/home/u/proj` → `/home/u`, stopping there).
- **A `..` segment never matches a root pattern.** A candidate path containing `..` after
  normalization is refused, so `{cwd}/x/../.agents/skills` cannot claim the `.agents` row by
  textual similarity; the round-86 closure's F6 world laundered roots that way.

## Bound

This entry does not claim a client run: the evidence is the ELF's own code bytes and one upstream
re-open of the module that carries the plugin reader. It does not claim that every root omp walks is
in the 12 rows — the ledger is the round-86 set, re-grounded, not re-enumerated; an unlisted root is
out of scope, not refuted. The plugin registry *files* (`~/.omp/plugins/**`) are documented from the
directory tree in `.ufo/waves/round-87/w1/ScoutPlugin/registry.txt`, not observed through a live
discovery pass.
