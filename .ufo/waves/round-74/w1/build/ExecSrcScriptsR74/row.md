# Row draft — page `using-scripts` (C1, assimilation)

Source opened by this seat today (2026-10-25); no lane file edited, no `/home/vgpnk/Projects/shokuknow`
file touched. 11-column schema = the `## Registry` header of `corpus/SOURCES.md:9`; no `|` inside any cell.

## Row (primary — status `mined`, as frozen plan § C1 predicate (b) requires)

| S<next> | Agent Skills — Using scripts in skills — https://agentskills.io/skill-creation/using-scripts.md | docs | A | The open specification's own script-craft guide: one-off commands for an existing package, references to bundled scripts, self-contained scripts with inline dependencies, and script interfaces designed for an agent caller; tier A scoped to this page's own guidance, not a measurement of any client | § One-off commands; § Referencing scripts from `SKILL.md`; § Self-contained scripts; § Designing scripts for agentic use — upstream `docs/skill-creation/using-scripts.mdx` at 6102affec88b137de8e213987aa1c49fcfde48a7 (its only touching commit) and byte-identical at head 69ef37e9424c0a7ea9dd2293b559e43ec8176379 (`git ls-remote refs/heads/main`, 2026-10-25T22:37:34-03:00); live `.md` fetched 2026-10-25, HTTP 200, no redirect, 12 078 B, sha256 2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f; quote "Pin versions with `npx package@version` for reproducibility." (7 words, line 50) | Reference an existing package as a pinned one-off command (`uvx ruff@0.8.0`, `pipx run 'black==24.10.0'`, `npx eslint@9`, `bunx`) instead of bundling a script, and design any bundled script for an agent caller — flags not prompts, `--help` as the interface, structured stdout with diagnostics on stderr, meaningful exit codes, a `--dry-run` and bounded output | mined | 2026-10-25 | 90d | corpus/knowledge/spec-skill-creation-craft-round74.md |

## Alternative (assignment literal — status `queued`)

Identical to the row above with `mined` replaced by `queued`. Measured consequence, not a preference:
frozen plan § C1 predicate (b) requires `status mined` for the page to count as backed, and the plan's
own shortcut control lists "rows appended with status `queued`" as a world that must score below 3.
`queued` also removes the census `E11` check (below), so it is the cheaper row, not the weaker one.

## Observed facts behind each cell

| cell | value | command | observed |
|---|---|---|---|
| id | `S<next>` = `S223` | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; ids sorted | `148` rows; max id `S222` → next free `S223` |
| source | URL | `grep -c 'using-scripts' corpus/SOURCES.md` | `0` — no existing row, no duplicate URL |
| kind | `docs` | `grep -n 'kind !~' scripts/sources-census.sh` (fleet root) | enum `spec\|docs\|paper\|code\|tool\|dataset\|talk\|book\|community\|own-work` |
| tier | `A` | `corpus/SOURCES.md` header + contract rule 3 | page is the format maintainers' own guidance, scoped to this page |
| status | `mined` | see C1 predicate (b) | required by the frozen predicate; `queued` is the alternative above |
| opened | `2026-10-25` | `date -I` | `2026-10-25` (local, -03:00) |
| recheck | `90d` | census `E09` accepts `NNd` | `90d` |
| used-by | `corpus/knowledge/spec-skill-creation-craft-round74.md` | plan § C1 predicate (a) frozen entry path | that entry does not exist yet → **E11** until it lands (see below) |

## Two measured constraints the L1 must honour when appending this row

1. **Append inside the table, not at end of file.** A row appended after the `## Registry` table is
   `E12` and its `used-by` is never checked:
   `printf '%s\n' "$ROW" >> corpus/SOURCES.md; scripts/sources-census.sh validate --file …` printed
   `file	E12	S999 row outside Registry section`.
2. **`mined` + a `used-by` path that does not exist = `E11`, exit 1.** Minimal-registry probe
   (`fix2`), three arms:
   - `mined`, entry absent → `file	E11	S900 missing used-by corpus/knowledge/spec-skill-creation-craft-round74.md`, exit `1`
   - `queued`, entry absent → `file	ok	…/corpus/SOURCES.md`, exit `0`
   - `mined`, entry present → `file	ok	…/corpus/SOURCES.md`, exit `0`

   So this row cannot land alone: `corpus/knowledge/spec-skill-creation-craft-round74.md` must exist in the
   same commit (or an earlier one), which is also what C1 predicate (a) and (f) require.

## C1 predicate (c) — snapshot placement

This seat saved the page text at
`.ufo/waves/round-74/w1/build/ExecSrcScriptsR74/snapshot.md` (12 078 B, sha256
`2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f`, verified with `sha256sum -c snapshot.sha256`
→ `snapshot.md: OK`). The frozen predicate reads the snapshot from `.ufo/waves/round-74/snapshots/` and pins it
in `snapshots/MANIFEST.sha256`; the L1 lands it with

```
mkdir -p .ufo/waves/round-74/snapshots
cp .ufo/waves/round-74/w1/build/ExecSrcScriptsR74/snapshot.md .ufo/waves/round-74/snapshots/using-scripts.md
cd .ufo/waves/round-74/snapshots && sha256sum using-scripts.md >> MANIFEST.sha256
```

(that path is this seat's recommendation, not a fact it may land).
