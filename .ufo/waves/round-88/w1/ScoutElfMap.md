# ScoutElfMap — round-88 w1 — ELF evidence for the binding token sets

Seat: ScoutElfMap. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Read-only seat. No production file was written; no counter was edited; the ELF was never executed.

Deliverables (under `.ufo/waves/round-88/w1/`):

| path | content |
|---|---|
| `ScoutElfMap/ELF_MAP.tsv` | 12 ledger rows + `# unledgered` block + 6 unledgered rows (sha256 `21e3c518df2eafc17a233ad4232b7b0a852db47f9a9be522acf32ab938444897`) |
| `ScoutElfMap/receipts.txt` | 238 lines: every mmap command and its observed output, one `RE-FIND` line per non-empty offset (48 total, 0 mismatches) |
| `ScoutElfMap/*.py` | the read-only scan scripts (reproduction) |
| `ELF_MAP_READY` | the sha256 of `ELF_MAP.tsv` |

## ELF pin

`sha256(/home/vgpnk/.local/bin/omp) = 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` — **matches the pin**.
Size 276 785 328 bytes. Opened with `mmap.mmap(fd, 0, access=mmap.ACCESS_READ)`; only `sha256`, `bytes.find`,
`re.finditer` and slice reads were used. `omp` was never executed by this seat (not even `--version`).

Ledger read from committed bytes at the frozen tip:
`git -C <lane> show 4df1e8005016c75390a5e06b209462df58c95918:verifiers/omp-skill-roots-semantics.tsv` → 12 data rows.

## ELF_MAP.tsv columns

`root_pattern<TAB>module<TAB>module_offset<TAB>reader_offset<TAB>binary_quote_offset<TAB>join_line_token<TAB>binding_token_candidate`

* `module_offset` — the **last** occurrence of `// packages/<module>` in the ELF (the one the r87 counter's
  conjunct 3 compares against: "the header's last occurrence"). For `builtin.ts` there are two (173809529,
  173814223); for `codex.ts` two (173869756, 173878972); for `helpers.ts` two (172783788, 172784226); for
  `agent-plugins.ts` two (173702219, 173777080); for `claude-plugins.ts` two (173848057, 173849184); for
  `utils/src/dirs.ts` two (166865730, 166884479). All other modules carry exactly one.
  The column carries the **last** occurrence, which for every one of the 12 rows is also the
  nearest preceding header of any kind before the reader quote (verified independently by a
  nearest-header sweep over a 400 kB window — the two agree in all 12 cases).
* `reader_offset` — the **first** occurrence of the row's `reader_quote`. Every one of the 12 quotes occurs
  **exactly once** in the ELF, so "first" and "only" coincide.
* `binary_quote_offset` — the **first** occurrence of the row's `binary_quote` in the ELF (conjunct 5).
  For 11 of 12 rows this first hit is inside the compiled **string table** (offsets 114486488–114492692),
  not in the bundled TypeScript; the second hit is the TS source line
  (`var Js = "Native OMP configuration from ~/.omp and .omp/";` etc.) and is recorded in `receipts.txt`
  as an `also at …` line. **Row 9 is the exception**: its `binary_quote` is `var Gh = ".omp";`, which is a
  TypeScript source line, so its only occurrence (166884553) is source, not string table.
* `join_line_token` — the token on the nearest join-token line (`join(` / `.join(` / `resolve(` / `path.join`)
  through which the row's root literal, or the variable that carries it, flows.
* `binding_token_candidate` — the token a v2 counter's per-row binding token set should name:
  it is present on the row's own reader line **and** is produced by the root literal or its declared
  reader variable.

## The 12 ledger rows (ELF_MAP.tsv block 1)

| # | root_pattern | module_offset | reader_offset | binary_quote_offset | join_line_token | binding_token_candidate |
|---|---|---|---|---|---|---|
| 1 | `{cwd}/.omp/skills` | 173814223 | 173819979 | 114486488 | `Ou.projectDir` | `Ou.projectDir` |
| 2 | `{cwd}/.claude/skills` | 173837493 | 173840364 | 114489000 | `eh` | `eh` |
| 3 | `{cwd}/.agent/skills` | 173864077 | 173865724 | 114490024 | `_` | `_` |
| 4 | `{cwd}/.agents/skills` | 173864077 | 173865724 | 114490024 | `_` | `_` |
| 5 | `{cwd}/.codex/skills` | 173878972 | 173879095 | 114490716 | `".codex"` | `".codex"` |
| 6 | `{cwd}/.opencode/skills` | 172784226 | 172785704 | 114492072 | `r.projectDir` | `r.projectDir` |
| 7 | `{cwd}/.github/skills` | 172784226 | 172785704 | 114492692 | `r.projectDir` | `r.projectDir` |
| 8 | `~/.omp/agent/skills` | 173814223 | 173820135 | 114486488 | `we()` | `we()` |
| 9 | `~/.omp/plugins/node_modules/*/skills` | 173914407 | 173914936 | 166884553 | `R.path` | `"skills"` |
| 10 | `~/.agent/skills` | 173864077 | 173865523 | 114490024 | `y1` | `y1` |
| 11 | `~/.agents/skills` | 173864077 | 173865523 | 114490024 | `y1` | `y1` |
| 12 | `~/.omp/agent/managed-skills` | 173809642 | 173809938 | 114486660 | `"managed-skills"` | `"managed-skills"` |

Every reader line, and the declaration that produces each root literal:

```
173819979  '      dir: fr.join(k, Ou.projectDir, "skills"),'      Ou  = ZO.native                (173814381)
173840364  '        dir: Fr.join(k, eh, "skills"),'              eh   = ".claude"                 (173837626)
173865724  '        x.push(Rs.join(R, _, ...p));'                y1   = [".agent", ".agents"]      (173864226)
173879095  '  return Xr.join(u.cwd, ".codex");'                  ".codex" literal on the line
172785704  '  return d.join(e.cwd, r.projectDir, n);'            r    = ZO[t]                     (ZO table 172784276)
173820135  '    dir: fr.join(we(), "skills"),'                   we()  = c.agentDir               (166891720)
173914936  '    dir: Zo.join(R.path, "skills"),'                 R.path = plugin root; "skills" literal
173865523  '  return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'   y1 on the line
173809938  '  return Zm.join(u, "managed-skills");'              "managed-skills" literal; u = we()
```

## The 6 unledgered joins (ELF_MAP.tsv block 2, after `# unledgered`)

Round-87 `w3/ScoutPatternsR87/derived-roots.txt` § C lists six code sites with **no** ledger row.
Each offset was re-read in the ELF. **All six are reader code lines (a join token is present on the line).**
None is a doc/string-table line. Their `binary_quote_offset` is `NONE` — there is no ledger row, hence no
`binary_quote` cell, to quote.

| root | offset | module (header offset) | line | join token? | verdict |
|---|---|---|---|---|---|
| `~/.claude/skills` | 173840218 | discovery/claude.ts (173837493) | `const x = p ? Fr.join(p, "skills") : null;` | yes | READER_CODE_LINE |
| `~/.codex/skills` | 173882129 | discovery/codex.ts (173878972) | `const x = p ? Xr.join(p, "skills") : null;` | yes | READER_CODE_LINE |
| `~/.config/opencode/skills` | 172785499 | discovery/helpers.ts (172784226) | `return d.join(e.home, r.userAgent, n);` | yes | READER_CODE_LINE (generic site) |
| `<agent-plugin>/skills` | 173778070 | discovery/agent-plugins.ts (173777080) | `const _ = await FS(u, Ym.join(u, "skills"));` | yes | READER_CODE_LINE |
| `<claude-plugin>/skills` | 173851107 | discovery/claude-plugins.ts (173849184) | `const k = li.join(u.path, p.fallback);` | yes | READER_CODE_LINE |
| `~/.omp/plugins/node_modules/*` | 166892485 | utils/src/dirs.ts (166884479) | `return h.join($o(p), "node_modules");` | yes | READER_CODE_LINE |

`binary_quote_offset` for these rows is written `NONE` in the TSV with the reason recorded in
`receipts.txt` and in the table above — **no quote was fabricated**.

## Findings for the v2 counter (C1 conjuncts 2, 3, 5)

**F1 — rows 3/4, 6/7 and 10/11 share their reader line VERBATIM.**
Three pairs of ledger rows point at the same ELF line, so no token on that line can distinguish the pair:

* rows 3 & 4 → 173865724 `x.push(Rs.join(R, _, ...p));`
* rows 6 & 7 → 172785704 `return d.join(e.cwd, r.projectDir, n);`
* rows 10 & 11 → 173865523 `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));`

Consequence for the binding-token set: the sets for those three pairs **must be identical within each pair**
or the honest ledger cannot reach N == 12. A per-row set that differs inside a pair is not satisfiable.
This is a property of the ELF, not a defect of the ledger — the roots genuinely are produced by one shared
`join` site each.

**F2 — the discriminating literal is often NOT on the join line.**
For rows 1, 2, 3/4, 6/7, 8 the root literal lives in a *declaration*, not in the join line:

| row | root literal | where it actually is | ELF offset |
|---|---|---|---|
| 1 | `.omp` | `var Gh = ".omp";` → `ZO.native.projectDir` → `Ou.projectDir` | 166884553 / 172784276 / 173814381 |
| 2 | `.claude` | `var eh = ".claude";` | 173837626 |
| 3/4 | `.agent` / `.agents` | `var y1 = [".agent", ".agents"];` (literals at 173864236 / 173864246) | 173864226 |
| 6/7 | `.opencode` / `.github` | `var ZO = { … }` table (`projectDir:` entries at 172784806 / 172785190) | 172784276 |
| 8 | `~/.omp/agent` | `we()` → `c.agentDir` (`this.agentDir = P ? h.resolve(P) : a;`) | 166891720 / 166888545 |

A binding-token check that demands the *literal* on the reader line would refuse rows 1, 2, 3, 4, 6, 7, 8
and drive N below 12. The token set must name the **variable** that produces the literal
(`Ou.projectDir`, `eh`, `_`/`y1`, `r.projectDir`, `we()`) — as the map's `binding_token_candidate` column does.
Note the plan's own wording: the set "names at least one token that the row's root literal **or its declared
reader variable** produces" — the second clause is what these rows need.

**F3 — row 5's reader quote grounds only the `.codex` segment, not `/skills`.**
`return Xr.join(u.cwd, ".codex");` @173879095 builds `{cwd}/.codex`. The `/skills` join is a *separate*
line, `const k = Xr.join(R, "skills");` @173882193 (which is exactly the offset round-87's
`derived-roots.txt` lists for `{cwd}/.codex/skills`). The ledger's `reader_quote` for row 5 therefore
grounds the parent directory only. The binding token `".codex"` is on the line and is the right token, but a
counter that also wants the `skills` segment for this row must look at 173882193, not 173879095.
**This is a ledger observation, not a counter defect — the ledger is FROZEN and read unchanged.**

**F4 — the `binary_quote` column is a string-table column, not a source column (except row 9).**
For 11 of 12 rows the first `binary_quote` hit sits in the compiled string table (114486488–114492692); the
TS source copy is the second hit. Conjunct 5 ("the row's `binary_quote` occurs verbatim in the ELF") is
therefore satisfiable from the string table alone, with no source code involved — a doc string and a
compiled string table are both "in the ELF". Row 9's `binary_quote` is the TS line `var Gh = ".omp";` and
exists only in source. A counter that wants conjunct 5 to discriminate code from documentation must
additionally require the quote to occur on a line carrying the row's binding token, or require the *source*
occurrence; the map records both occurrences so either choice can be made from the receipt.

**F5 — the unledgered roots are genuinely read, but two of them are generic composition sites.**
`~/.config/opencode/skills` @172785499 (`return d.join(e.home, r.userAgent, n);`) serves every `ZO[t]`
provider — the `skills` segment arrives as the argument `n` at the call site
`Ac(u, "opencode", "skills")` @173903123. `<claude-plugin>/skills` @173851107
(`const k = li.join(u.path, p.fallback);`) likewise takes `"skills"` as `p.fallback`
(descriptor `fallback: "skills"` @173852593). Both are reader code (join token present) but neither carries
the root's own name on the line. If the v2 counter ever widens to the unledgered roots, these two need the
call-site argument, not the join line, to bind them.

**F6 — a near-miss offset correction.**
Round-87's `derived-roots.txt` § C lists `~/.omp/plugins/node_modules/*` at 166892485; the join token
`h.join($o(p), "node_modules")` actually starts at **166892506** — 166892485 is 21 bytes earlier, on the
same line's leading `function Pu(p) {`. The line content is the same, so the r87 classification is unaffected;
only the byte offset of the token differs. The map records the r87 offset (so the two rounds are comparable)
and the exact token offset in the reason column.

## Reproduction

```
export TMPDIR=/fast/scratch/hyaku/kotoba-r88/ScoutElfMap
cd /fast/scratch/hyaku/kotoba-r88/ScoutElfMap
python3 -B final.py      # writes ELF_MAP.tsv + receipts.txt, re-finding every offset
python3 -B scan.py       # per-row occurrence dumps (reader / binary / nearest join lines)
python3 -B ctx.py        # source context around every join site + the 6 unledgered offsets
```

`final.py` is self-contained: it pins the ELF sha256, reads the ledger from `git show` at the frozen tip,
and emits one `RE-FIND … (match=True)` line per non-empty offset. **48 RE-FIND lines, 0 mismatches**
(12 ledger rows × 3 offsets = 36, plus 6 unledgered rows × 2 offsets = 12).

## Risks / unknown

* The `binding_token_candidate` column is a **candidate** set, not the frozen set. The frozen sets are the
  v2 counter author's to write; the map supplies the evidence (offset, token text, declaration offset) for
  each. Under the plan's kill rule, the v2 counter's sets must be written and hashed **before** the first
  honest or forged score — this seat's map must be consumed before that score, not amended after it.
* Rows 3/4, 6/7 and 10/11 (F1) mean three per-row sets will be equal within their pair. If the v2 author
  wants them to differ, the discriminating evidence is the *declaration* offset
  (173864236/173864246 for `.agent`/`.agents`; 172784806/172785190 for `.opencode`/`.github`), which is
  a different (and stricter) conjunct than "the reader line carries the token".
* The ELF was read as a flat byte image; the TypeScript inside it is a bun bundle, so "the module" is a
  `// packages/<…>` comment banner, not a real file boundary. A row's module is the banner nearest preceding
  its reader quote — verified to agree with the ledger's `module` cell in all 12 rows.
* No `lsp`/language server applies to a byte image; every fact here is a literal byte offset in the pinned
  ELF, re-found and printed.

## Tooling

No tool was installed or upgraded. The task needed only `python3` (stdlib `mmap`, `re`, `hashlib`,
`subprocess`), already present. PACMAN was not touched.
