# ScoutUpstream — S257 source record (round-88 w1)

Seat: scout, leaf member (no subagent dispatch). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Read-only on the lane except this seat's
own directory `.ufo/waves/round-88/w1/ScoutUpstream/` and the handoff flag
`.ufo/waves/round-88/w1/SOURCE_READY`.

Fetched artifact (scratch, deleted at the end of the run):
`/fast/scratch/hyaku/kotoba-r88/ScoutUpstream/agents.ts`

* URL: `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts`
* HTTP status: **200** (`curl -fsSL`, exit 0)
* Size: **12313 B**, **330** lines
* sha256: **976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e**
* git blob id of the fetched bytes: `2e41428ba19a5fe875143b422b7f4eccbe44c24d` — equal to the
  blob GitHub serves at `?ref=v18.15.0`, so the pin is the tag's blob, not a moving branch
* tag `v18.15.0` → commit `3fedf8d53267e32a6d7521ce725fdcc4a36fdc67`
* access date (opened): **2026-11-05**

---

## The row fields, one new `corpus/SOURCES.md` row

The row is `S257` (S256 is the last existing id; `grep -n '^| S257' corpus/SOURCES.md`
exits 1 — the id is unused). Eleven cells, `NF=13`, **no `|` character inside any cell**.

| cell | value |
|---|---|
| id | `S257` |
| source | omp 18.15.0 — agent-dirs skill-root walk-up module — https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts (tag v18.15.0, HTTP 200, 12313 B) |
| kind | `code` |
| tier | `A` |
| scope | the bound of the project walk for `{cwd}/.agents/skills` — the ancestor walk's stop condition and its home-directory exclusion |
| anchor | `packages/coding-agent/src/discovery/agents.ts`, line 149, tag v18.15.0, sha256 976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e (12313 B, 330 lines); located quote at byte offset 6119 of the fetched bytes; ELF `/home/vgpnk/.local/bin/omp` (sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f) module header `// packages/coding-agent/src/discovery/agents.ts` @173864077, bound statement @173865771, reader quote `x.push(Rs.join(R, _, ...p));` @173865724 |
| teaches | the project walk for the `.agent`/`.agents` skill roots stops at the repo root or at `$HOME` and never emits a candidate rooted at `$HOME` itself, so a `{cwd}`-rooted skill root expands to the session cwd and its ancestors strictly below `$HOME` |
| status | `mined` |
| opened | `2026-11-05` |
| recheck | `on-release` |
| used-by | `corpus/knowledge/omp-root-semantics-round88.md` |

### Ready-to-paste single-line row (the exact bytes for `corpus/SOURCES.md`)

```
| S257 | omp 18.15.0 — agent-dirs skill-root walk-up module — https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts (tag v18.15.0, HTTP 200, 12313 B) | code | A | the bound of the project walk for `{cwd}/.agents/skills` — the ancestor walk's stop condition and its home-directory exclusion | `packages/coding-agent/src/discovery/agents.ts`, line 149, tag v18.15.0, sha256 976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e (12313 B, 330 lines); located quote at byte offset 6119 of the fetched bytes; ELF `/home/vgpnk/.local/bin/omp` (sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f) module header `// packages/coding-agent/src/discovery/agents.ts` @173864077, bound statement @173865771, reader quote `x.push(Rs.join(R, _, ...p));` @173865724 | the project walk for the `.agent`/`.agents` skill roots stops at the repo root or at `$HOME` and never emits a candidate rooted at `$HOME` itself, so a `{cwd}`-rooted skill root expands to the session cwd and its ancestors strictly below `$HOME` | mined | 2026-11-05 | on-release | corpus/knowledge/omp-root-semantics-round88.md |
```

### Checks against the registry contract (`scripts/sources-census.sh`, SOURCES-CONTRACT-v1)

| contract rule | this row | verdict |
|---|---|---|
| E01 row shape `NF=13` (11 cells) | 11 cells, `\|`-free | PASS |
| E02 id form `S[0-9]{3,}` | `S257` | PASS |
| E03 id unused | `grep -n '^| S257' corpus/SOURCES.md` → no match (exit 1) | PASS |
| E04 duplicate URL+scope | this URL+scope pair is new; the URL appears in no other row | PASS |
| E05 kind enum | `code` | PASS |
| E06 tier enum | `A` | PASS |
| E07 status enum | `mined` | PASS |
| E08 opened is a past/present ISO date | `2026-11-05` (today) | PASS |
| E09 recheck cadence | `on-release` (symbolic) | PASS |
| E10 community at tier A | n/a (kind `code`) | PASS |
| E11 used-by path on disk | `corpus/knowledge/omp-root-semantics-round88.md` is **written by the ScribeEntry seat**, not by this seat — see the ordering note below | pending ScribeEntry |
| E12 row inside `## Registry` | the paste target is the Registry table | PASS |

**Ordering note (raised, not fixed).** E11 is a census *error* code, so the census must be run
after `corpus/knowledge/omp-root-semantics-round88.md` lands, or the row reads as a dangling
used-by. This seat does not own that file and did not create it. `ScribeSources` (row owner) and
`ScribeEntry` (knowledge-file owner) are the two seats that can sequence this.

## The located quote (verbatim, ≤25 words)

```
if (current === (ctx.repoRoot ?? ctx.home)) break;
```

* upstream: `packages/coding-agent/src/discovery/agents.ts` **line 149** (leading tabs trimmed;
  the raw line is `\t\tif (current === (ctx.repoRoot ?? ctx.home)) break;`), byte offset **6119**
  in the fetched body; the string occurs exactly **once** in the file.
* word count: **7** whitespace-separated tokens (limit 25).
* ELF counterpart (same code, minified identifiers): `if (R === (u.repoRoot ?? u.home))` at
  ELF offset **173865771**, statement bytes
  `'if (R === (u.repoRoot ?? u.home))\n      break;'`, inside the ELF module
  `// packages/coding-agent/src/discovery/agents.ts` (header @173864077).

Companion line, one above the stop, is the home-directory exclusion the C1 v2 bound conjunct
also needs: upstream line **144** `if (current !== ctx.home) {` (ELF @173865668).

## The walk-up loop as fetched (upstream lines 140–155)

```
export function getProjectPathCandidates(ctx: LoadContext, ...segments: string[]): string[] {
	const paths: string[] = [];
	let current = ctx.cwd;
	while (true) {
		if (current !== ctx.home) {
			for (const baseDir of AGENT_DIR_CANDIDATES) {
				paths.push(path.join(current, baseDir, ...segments));
			}
		}
		if (current === (ctx.repoRoot ?? ctx.home)) break;
		const parent = path.dirname(current);
		if (parent === current) break;
		current = parent;
	}
	return paths;
}
```

`AGENT_DIR_CANDIDATES` is `[".agent", ".agents"]` (upstream line 30; ELF
`var y1 = [".agent", ".agents"];` @173864226), and the skills loader calls this function with
the `"skills"` segment (upstream line 159 `getProjectPathCandidates(ctx, "skills")`; ELF
`async function Gne(u) {` @173865906 with `V9(u, "skills")`).

## Why this is the ground for the C1 v2 bound conjunct

The frozen C1 predicate (plans/round-88.md § C1, conjunct 4) computes a `{cwd}` row's
expansion set from the probe cwd `/home/u/proj/sub` with `HOME=/home/u` and requires the
session cwd and its ancestors **strictly below** `$HOME` — i.e. `/home/u/proj/sub` and
`/home/u/proj`, with `/home/u` itself excluded.

The fetched upstream code produces exactly that set, for a reason the two located lines give:

1. line 149 stops the walk when `current === (ctx.repoRoot ?? ctx.home)`; with no repoRoot
   the walk terminates **at** `$HOME`, so no ancestor above `$HOME` is ever visited;
2. line 144 (`if (current !== ctx.home)`) refuses to push a candidate rooted **at** `$HOME`,
   so `$HOME` is excluded from the emitted set rather than merely being the last visited node.

Trace of the probe against the fetched bytes: `/home/u/proj/sub` → push; parent
`/home/u/proj` → push; parent `/home/u` → equals `ctx.home`, so line 144 skips the push and
line 149 breaks the loop. Emitted set = `{/home/u/proj/sub, /home/u/proj}` — the frozen
expectation.

Because the stop is `repoRoot ?? home` with `repoRoot` taking precedence, a `repoRoot` at or
below `$HOME` leaves this set unchanged (measured: unset, `/home/u` and `/home/u/proj` all give
the same two ancestors), while a `repoRoot` **above** `$HOME` (measured: `/home`) adds
ancestors above `$HOME` to the set. `$HOME` itself is excluded unconditionally by line 144.
A probe fixture that sets no `repoRoot`, or one at/below `$HOME`, therefore reproduces the
frozen expectation.

The ledger rows that name this module are rows 4 and 5 of
`verifiers/omp-skill-roots-semantics.tsv` (`{cwd}/.agent/skills`, `{cwd}/.agents/skills`,
both `module=coding-agent/src/discovery/agents.ts`, `reader_quote=x.push(Rs.join(R, _, ...p));`),
plus the `~/` rows 11 and 12 whose reader is the user-home counterpart
`return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` — ELF reader quote
byte-identical at offset **173865523**, inside `function z9(u, ...p) {` at ELF @173865498
(upstream counterpart: `packages/coding-agent/src/discovery/agents.ts` line 125,
`return getUserHomeCandidates(ctx).flatMap(home =>` …, inside `getUserPathCandidates` at line
124). The reader quote of rows 4/5 is byte-identical in the ELF at offset **173865724**.

## Commands and observed output

Full transcript: `.ufo/waves/round-88/w1/ScoutUpstream/receipts.txt`.
