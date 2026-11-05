# ScoutUpstream — the upstream ground for the C1 v2 bound conjunct (round-88 w1)

Seat: scout, leaf member (no subagent dispatch). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. **Read-only on the lane**
except this seat's own directory `.ufo/waves/round-88/w1/ScoutUpstream/` and the handoff flag
`.ufo/waves/round-88/w1/SOURCE_READY`. No counter, ledger, plan, corpus, LOG or SCORECARD byte
was touched. The ELF was read with `mmap`/`re` only — never copied into the lane, never executed.

**Scope.** Open the upstream omp source for the *bound conjunct* (the home-directory stop of
the project walk-up) at tag `v18.15.0`, hash it, locate the bound line, ground the same code
in the ELF bytes, and hand the S257 row fields to `ScribeSources`.

**Files written by this seat**

| path | bytes | what |
|---|---|---|
| `.ufo/waves/round-88/w1/ScoutUpstream/SOURCE_ROW.md` | 8 675 | the S257 row fields, the ready-to-paste single-line row, the located quote, the contract check table |
| `.ufo/waves/round-88/w1/ScoutUpstream/receipts.txt` | 4 145 | the exact commands and their observed output |
| `.ufo/waves/round-88/w1/SOURCE_READY` | 65 | the sha256 of the fetched upstream file (handoff flag) |
| `.ufo/waves/round-88/w1/ScoutUpstream.md` | this file | the seat report |

---

## 1. The fetch

```
$ curl -fsSL -o agents.ts -w "http_status=%{http_code}\nsize_download=%{size_download}\nurl_effective=%{url_effective}\n" \
    'https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts'
http_status=200
size_download=12313
url_effective=https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts
curl_exit=0

$ sha256sum agents.ts
976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e  agents.ts

$ wc -lc agents.ts
  330 12313 agents.ts
```

* **HTTP 200, 12313 B, 330 lines, sha256 `976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e`.**
* Access date **2026-11-05** (UTC, host clock).
* The remote file was **never piped into a shell**: `curl -fsSL -o <file>` wrote it to the
  scratch dir, and every later command read the file from disk.

### The pin is the tag's blob, not a moving branch

```
$ git hash-object agents.ts
2e41428ba19a5fe875143b422b7f4eccbe44c24d

$ curl -fsSL 'https://api.github.com/repos/can1357/oh-my-pi/contents/packages/coding-agent/src/discovery/agents.ts?ref=v18.15.0'
blob_sha 2e41428ba19a5fe875143b422b7f4eccbe44c24d size 12313

$ curl -fsSL 'https://api.github.com/repos/can1357/oh-my-pi/git/ref/tags/v18.15.0'
tag_ref refs/tags/v18.15.0 -> 3fedf8d53267e32a6d7521ce725fdcc4a36fdc67 commit
```

The fetched bytes' git blob id equals the blob GitHub serves at `?ref=v18.15.0`, and the tag
resolves to commit `3fedf8d53267e32a6d7521ce725fdcc4a36fdc67`. The sha256 pin is therefore
stable, not a branch tip that can move.

---

## 2. The located quote — the bound of the project walk

```
$ grep -n 'current !== ctx.home\|current === (ctx.repoRoot ?? ctx.home)\|parent === current\|paths.push(path.join' agents.ts
144:		if (current !== ctx.home) {
146:				paths.push(path.join(current, baseDir, ...segments));
149:		if (current === (ctx.repoRoot ?? ctx.home)) break;
151:		if (parent === current) break;
```

**The quote (verbatim, 7 words — limit 25):**

```
if (current === (ctx.repoRoot ?? ctx.home)) break;
```

* upstream `packages/coding-agent/src/discovery/agents.ts` **line 149** (leading tabs trimmed;
  raw bytes `\t\tif (current === (ctx.repoRoot ?? ctx.home)) break;`), byte offset **6119** in the
  fetched body; the string occurs exactly **once** in the file.
* **ELF counterpart** (same code, minified identifiers): `if (R === (u.repoRoot ?? u.home))` at
  ELF offset **173865771**, statement bytes
  `'if (R === (u.repoRoot ?? u.home))\n      break;'`, inside the ELF module
  `// packages/coding-agent/src/discovery/agents.ts` (module header @**173864077**).
* The companion line the same bound needs — the exclusion of `$HOME` itself — is upstream line
  **144** `if (current !== ctx.home) {` (ELF @173865668).

### The loop as fetched (upstream lines 140–155)

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
`var y1 = [".agent", ".agents"];` @173864226); the skills loader calls the walk with the
`"skills"` segment (upstream line 159; ELF `async function Gne(u) {` @173865906).

---

## 3. Why this is the ground for the C1 v2 bound conjunct (not a paraphrase)

The frozen C1 predicate (`plans/round-88.md` § C1, conjunct 4) computes a `{cwd}` row's
expansion set from probe cwd `/home/u/proj/sub` with `HOME=/home/u` and requires the session
cwd and its ancestors **strictly below** `$HOME` — i.e. `/home/u/proj/sub` and `/home/u/proj`,
with `/home/u` itself excluded.

The fetched upstream code produces exactly that set, and the two located lines say why:

1. **line 149** stops the walk at `current === (ctx.repoRoot ?? ctx.home)`; with no repoRoot the
   walk terminates **at** `$HOME`, so no ancestor above `$HOME` is ever visited;
2. **line 144** (`if (current !== ctx.home)`) refuses to push a candidate rooted **at** `$HOME`,
   so `$HOME` is excluded from the *emitted* set rather than merely being the last visited node.

Trace of the probe against the fetched bytes: `/home/u/proj/sub` → push; parent `/home/u/proj`
→ push; parent `/home/u` → equals `ctx.home`, so line 144 skips the push and line 149 breaks.
Emitted set = `{/home/u/proj/sub, /home/u/proj}` — the frozen expectation.

Two details a counter could get wrong, both settled by the fetched bytes rather than by reading
the predicate:

* The walk's stop is `repoRoot ?? home`, **not** `home` alone, and `repoRoot` **wins** when
  present. Measured against the fetched bytes (same loop, `repoRoot` varied):

  | `repoRoot` in the probe | emitted ancestors (excluding `$HOME`) |
  |---|---|
  | unset (the frozen probe's reading) | `/home/u/proj/sub`, `/home/u/proj` |
  | `/home/u` (equal to `$HOME`) | `/home/u/proj/sub`, `/home/u/proj` |
  | `/home/u/proj` (at/below `$HOME`) | `/home/u/proj/sub`, `/home/u/proj` |
  | `/home` (above `$HOME`) | `/home/u/proj/sub`, `/home/u/proj`, **`/home`** |

  So a `repoRoot` **at or below** `$HOME` leaves the frozen strictly-below-`$HOME` set intact,
  but a `repoRoot` **above** `$HOME` adds ancestors above `$HOME` to the set (`$HOME` itself
  stays excluded — line 144 excludes it unconditionally). **The probe fixture must therefore
  not set a `repoRoot` above `$HOME`** for the frozen expectation to hold. This is a note
  about how the fixture must be constructed, not a request to change the predicate sentence.
* The `~/` roots (ledger rows 11 and 12) are **not** produced by this loop at all — they come
  from the separate user-home function `getUserPathCandidates` (upstream line 124–128; ELF
  `function z9(u, ...p) {` @173865498, reader quote byte-identical at ELF @173865523). The
  `~/` reader quote in the ledger is that function's `flatMap`, not the walk's `push`.

### Ledger rows that name this module

```
$ grep -n 'agents.ts' verifiers/omp-skill-roots-semantics.tsv
4:{cwd}/.agent/skills   …  coding-agent/src/discovery/agents.ts  x.push(Rs.join(R, _, ...p));
5:{cwd}/.agents/skills  …  coding-agent/src/discovery/agents.ts  x.push(Rs.join(R, _, ...p));
11:~/.agent/skills      …  coding-agent/src/discovery/agents.ts  return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));
12:~/.agents/skills     …  coding-agent/src/discovery/agents.ts  return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));
```

The item's "ledger row 4" is `{cwd}/.agent/skills` (row 4, 1-based with the header as row 1);
row 5 is its `.agents` twin. Both rows' `reader_quote` is **byte-identical in the ELF** at
offset **173865724** — this is the ground for the ledger's reader column, and it is the
`paths.push(path.join(current, baseDir, ...segments));` of upstream line 146.

### ELF side, re-derived from the bytes (read-only mmap, `re` only)

```
elf_size 276785328
ELF @173864077  // packages/coding-agent/src/discovery/agents.ts
ELF @173864226  var y1 = [".agent", ".agents"];
ELF @173865591  function V9(u, ...p) {
ELF @173865668  if (R !== u.home) {
ELF @173865724  x.push(Rs.join(R, _, ...p));
ELF @173865771  if (R === (u.repoRoot ?? u.home))
ELF @173865851  if (k === R)

$ sha256sum /home/vgpnk/.local/bin/omp
6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f
```

The ELF's sha256 equals the frozen pin `6737ee24…b7b0f`. The module is present under its
upstream path header, so the upstream file and the shipped ELF carry **the same code**, with
only identifier minification between them (`current`→`R`, `ctx`→`u`, `path`→`Rs`,
`getProjectPathCandidates`→`V9`, `getUserPathCandidates`→`z9`). The export map at ELF
@192373120 confirms the name mapping: `V9 as getProjectPathCandidates`, `z9 as getUserPathCandidates`.

---

## 4. The S257 row handed to `ScribeSources`

Full field table and the exact single-line row are in
`.ufo/waves/round-88/w1/ScoutUpstream/SOURCE_ROW.md`. Summary:

| cell | value |
|---|---|
| id | `S257` (S256 is the last existing id; `grep -n '^| S257' corpus/SOURCES.md` exits 1) |
| kind / tier / status | `code` / `A` / `mined` |
| opened / recheck | `2026-11-05` / `on-release` |
| used-by | `corpus/knowledge/omp-root-semantics-round88.md` |
| scope | the bound of the project walk for `{cwd}/.agents/skills` — the ancestor walk's stop condition and its home-directory exclusion |
| teaches | the project walk for the `.agent`/`.agents` skill roots stops at the repo root or at `$HOME` and never emits a candidate rooted at `$HOME` itself, so a `{cwd}`-rooted skill root expands to the session cwd and its ancestors strictly below `$HOME` |

**The row contains no `|` character inside any cell** (the contract's E01 requires `NF=13`).

### The row is landed, and the census was run against it

`ScribeSources` had already landed the row by the time this seat checked. It is **byte-identical**
to the ready-to-paste row in `SOURCE_ROW.md` (all 11 cells compared cell by cell: zero diffs),
and it carries the correct shape:

```
$ awk -F'|' 'NR==198{print "NF="NF}' corpus/SOURCES.md
NF=13                                    # 11 cells, no '|' inside any cell

$ grep -c '^| S257 ' corpus/SOURCES.md
1                                       # exactly one S257 row, id not duplicated
```

### One contract risk — MEASURED, not predicted (raised for the wave, not fixed by this seat)

Census rule **E11** requires every `used-by` path to exist on disk at census time.
`corpus/knowledge/omp-root-semantics-round88.md` is owned by the `ScribeEntry` seat and does
**not** exist yet (only the round-87 file `corpus/knowledge/omp-root-semantics-round87.md` is
on disk). This seat does not own that file and did not create it.

The census was run against the lane as it stands now and this is the **observed** result:

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --root /home/vgpnk/Projects/shokunin kotoba
kotoba	E11	S257 missing used-by corpus/knowledge/omp-root-semantics-round88.md
…  (33 × W04 "duplicate url … across scopes", unchanged from the plan's recorded baseline)
EXIT=1
```

* **E-codes: 1** — the single one is `E11` on S257's used-by.
* **W-codes: 33** — the plan's round-start baseline ("before: exit 0, 33 W04") is unchanged.
  S257's URL is unique in the registry, so it adds **no** W04 either.
* Registry rows: 183.

So the lane's census goes from exit 0 to exit 1 solely because S257's `used-by` names a file
that has not landed yet. The fix is **purely sequencing**, and it belongs to two other seats:

1. `ScribeEntry` lands `corpus/knowledge/omp-root-semantics-round88.md` (the file's owner), after
   which the E-code clears by itself; or
2. `ScribeSources` adds `corpus/knowledge/omp-root-semantics-round87.md` to S257's `used-by`
   alongside the round-88 path, so the row has at least one existing used-by.

The census must therefore be run **after** `ScribeEntry` lands, if the wave wants a clean exit 0.
This seat did not touch `corpus/SOURCES.md` and does not own either file; it is reported, not
repaired.

---

## 5. What this seat did **not** do

* Did not edit `corpus/SOURCES.md` (owned by `ScribeSources`), `corpus/README.md`,
  `corpus/knowledge/omp-root-semantics-round88.md` (owned by `ScribeEntry`), any counter, any
  ledger, `plans/round-88.md`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `MANIFEST.json`,
  `.ufo/state/`, `scripts/`, `templates/`, the fleet root, a sibling lane, or `shokuknow`.
* Did not run any git or jj write in the lane or the fleet.
* Did not copy the ELF into the lane; did not execute the ELF (not even `omp --version` — it was
  not needed here).
* Did not run the lane's counters: they belong to the `ExecLiveBound` / `ExecMonotoneD5` seats,
  and their results are not this seat's evidence.

## 6. Tooling

**No install, no upgrade, no download of any tool.** The seat used only what the host already
carries: `curl` 8.23.0 (OpenSSL 3.6.5), `python3` (stdlib only, `python3 -B`), `grep`, `sed`,
`wc`, `sha256sum`, `git hash-object` (read-only blob hashing of a scratch file). The generic
tooling directive was satisfied vacuously — no package was missing, and PACMAN IS PAUSED
host-wide, so no pacman transaction of any kind was attempted.

## 7. Scratch hygiene

One scratch dir, `/fast/scratch/hyaku/kotoba-r88/ScoutUpstream/`, created with `mkdir -p` and
exported as `TMPDIR` for every command. It held the fetched `agents.ts`, the two API JSON
bodies, and the receipt-capture script. It is deleted before this yield (`rm -rf -- "$S"`).
The fetched bytes are not needed downstream: everything downstream needs is in the receipts
file and in `SOURCE_ROW.md`.

---

**Findings (for the wave, not repairs)**

1. The upstream `agents.ts` at `v18.15.0` grounds the C1 v2 bound conjunct exactly, on two
   lines (149 stop, 144 exclusion) that together produce the frozen probe's strictly-below-
   `$HOME` set. The row's `scope`/`teaches` cells are written from the fetched bytes.
2. **Probe-fixture caution for `ExecLiveBound`:** the walk's stop is `repoRoot ?? home`, with
   `repoRoot` taking precedence. The frozen expectation (cwd `/home/u/proj/sub`, `HOME=/home/u`,
   expansion `{/home/u/proj/sub, /home/u/proj}`) holds when the probe sets **no repoRoot**, or a
   repoRoot **at or below** `$HOME` (measured: unset, `/home/u` and `/home/u/proj` all give the
   same two ancestors). A repoRoot **above** `$HOME` (measured: `/home`) adds ancestors above
   `$HOME` to the set — `$HOME` itself stays excluded, because line 144 excludes it
   unconditionally. The predicate sentence is frozen and unchanged; this is a note about how the
   fixture must be constructed, not a request to change the predicate.
3. **Census E11 — MEASURED, live.** The lane's sources census now exits **1** with exactly one
   E-code: `E11 S257 missing used-by corpus/knowledge/omp-root-semantics-round88.md`, because
   that file (owned by `ScribeEntry`) has not landed. The W-code count is unchanged at 33 (the
   plan's baseline), so S257 adds no warning. Fix is sequencing-only: `ScribeEntry` lands the
   knowledge file, or `ScribeSources` adds the round-87 knowledge path to S257's `used-by`. Not
   this seat's file; reported, not repaired.
4. The ledger's `~/` rows (11, 12) are grounded by a *different* upstream function
   (`getUserPathCandidates`, ELF `z9` @173865498 / reader @173865523) than the `{cwd}` rows
   (4, 5), which are grounded by the walk's `push` (ELF @173865724). A counter that treats the
   `~/` rows as walk outputs would be wrong; the ledger's own reader quotes already keep them
   apart.
