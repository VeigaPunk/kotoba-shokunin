# ScoutOpencodeV2 — Q45 population census for C2 (round 72 wave 1)

**Verdict: population N = 6 of 7 checks are honestly passable on the opencode v2.1.4 bytes; `p == 7` is unreachable. Recommend freezing the C2 target at `p == 6` (margin 0 vs the reachable set) in a committed addendum before data.**

## 1. Substrate facts (recorded)

| fact | command | observed output |
|---|---|---|
| version | `~/.opencode/bin/opencode --version` | `opencode v2.1.4` (single line; no separate build id line) |
| binary | `ls -l ~/.opencode/bin/opencode; file ~/.opencode/bin/opencode` | `-rwxr-xr-x 1 vgpnk vgpnk 240416944 …`; `ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=588d7307f333293c728b74df19b7323c20736899, not stripped` |
| sha256 | `sha256sum ~/.opencode/bin/opencode` | `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` |
| dump | `wc -c /tmp/k72-oc-strings.txt; sha256sum /tmp/k72-oc-strings.txt` | 28,835,401 bytes; `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089` |
| default bin paths in verifier | `python3 -c "import verify_surfaces; print(verify_surfaces.DEFAULT_BINARIES)"` | `{'omp': '/home/vgpnk/.local/bin/omp', 'opencode': '/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe'}` — opencode default is the **absent** npx 1.19.3 path (base exit-2 cause); omp default is the 1,680-byte bash wrapper (`~/.local/bin/omp`, sha256 `ed62a41e…`), not `omp.real` |

For `check_substrate_repin_v2.py`'s default-path run the L1 must re-pin `DEFAULT_BINARIES` to `~/.local/bin/omp.real` (sha256 `85d9daf3…`) and `~/.opencode/bin/opencode`, else the counter would dump the wrapper script / the missing path.

## 2. Observed base state on v2.1.4 (re-run, not taken from the plan)

`cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_surfaces.py --omp-binary /home/vgpnk/.local/bin/omp.real --opencode-binary /home/vgpnk/.opencode/bin/opencode --json` → exit 1, `pass 5 fail 2`:
- `surfaces.literal_present` FAIL: `opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)`
- `surfaces.opencode_extract` FAIL: `vacuity: extraction produced 0 class(es) from 7 rule(s) … 0 extracted classes with 9 declared is a FAIL`; all 7 rules (OC-1..OC-6) report `matched= False`.
- PASS: `no_uncovered_class` (`all 8 extracted loader class(es) declared`), `table_parity` (42 ids), `literal_parity` (42), `kind_parity` (42), `excluded_reason` (8).
- Identical result with the frozen dumps (`--omp-strings /tmp/k72-omp-strings.txt --opencode-strings /tmp/k72-oc-strings.txt`). Direct extractor run: opencode generic call-shape extraction = `set()`; omp = 8 pairs, all declared. `extract_opencode_classes` returns `[]`; every rule anchor listed as missing.

## 3. Literal census for the 9 opencode classes (grep -c -F on /tmp/k72-oc-strings.txt)

| class_id (baseline `surfaces-baseline.json`, 42 total, 9 opencode) | literal | count |
|---|---|---|
| `opencode:instructions/AGENTS.md` | `AGENTS.md` | 13 |
| `opencode:instructions/CLAUDE.md` | `CLAUDE.md` | 3 |
| `opencode:instructions/CONTEXT.md` | `CONTEXT.md` | **0** |
| `opencode:config/AGENTS.md` | `AGENTS.md` | 13 |
| `opencode:claude-home/CLAUDE.md` | `CLAUDE.md` | 3 |
| `opencode:config/instructions` | `instructions` | 145 |
| `opencode:config/instructions-remote` | `https://` | 827 |
| `opencode:read-hook/instructions` | `<system-reminder>` | 15 |
| `opencode:instruction-context/AGENTS.md` | `AGENTS.md` | 13 |

Only `CONTEXT.md` is absent (0 hits; quoted `"CONTEXT.md"` = 0). `CONTEXT.md` is also the **sole** absent literal among all 42 baseline classes, so the C2 removal-ledger exact-set conjunct is automatically satisfied if that one class is ledgered.

## 4. Replacement-mechanism sweep (does v2.1.4 load instruction files by other names/config?)

The v2.1.4 dump is the **v2.x lineage** (round-18-era shapes), not the 1.19.x round-47 shapes the OC rules encode:

- present anchors: `ConfigInstructionPlugin` (14), `ReadTool.Plugin` (2), `SessionInstructions` (4), `InstructionDiscovery` (8), `__=sA.make("core/instructions")` (1), `Instructions from: ` (3), `targets:["AGENTS.md"]` (1), `OPENCODE_DISABLE_PROJECT_CONFIG` (2) + `OPENCODE_CONFIG_PROJECT_DISABLE`, `globUp` (5), `instructions/entries` (10).
- absent anchors (count 0): `disableClaudeCodePrompt`, `InstructionContext.observe`, `system-context-builtins`, `ReadTool.execute`, `Instruction.resolve`, `Key.make("core/instructions")`, `"CLAUDE.md"` quoted.

Loader evidence (windows via `python3` over the dump, offsets given; surrounding minified JS bytes dropped):
- project walk-up: `ConfigInstructionPlugin.projectSource` — `l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})` (off 21499007/21499251);
- global candidate: `D=yield*l.resolve(j1(r.config,"AGENTS.md"))` (off 21498300/21498692);
- declared config list: `DS=o({instruction:o({paths:E(t)})})` + `SessionInstructions.load` consuming `h.paths` (off 21541590, 21542343); remote half fetched in `ConfigInstructionPlugin.reconfigure` via `Ae.filter(E1)` → `Xf(Re)` ("failed to fetch instruction url") → `H.remote=new Map(...)` (off 21499987, 21500759);
- read-tool hook: `var OF="read",LF="AGENTS.md"` and `yield*r.up({targets:[LF],…})` + `l.load({sessionID,paths:Y})` (off 21570810, 21572614);
- new skill file: `@opencode/Skill`, `Skill.prepare`, `SkillDiscovery` load `SKILL.md` (`"SKILL.md"` quoted ×7) — a file name outside the 9-class census.

The only `CLAUDE.md` occurrences are non-loader (lines, byte-exact, via `sed -n '<L>p'`):
- line 20946: `CLAUDE.md` (bare 9-byte chunk);
- line 150271: `CLAUDE.md.cursor/rulesbun-blank-templatebun-react-templatebun-react-tailwind-templatebun-react-tailwind-shadcn-templatebun-typescript-library-templatedevstatic` (bun-template enumeration; the round-13 § D "template-list" false friend);
- line 1228295: `- existing instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`)` (/init prompt prose).

## 5. Per-check passability under an honest re-derivation

1. `surfaces.literal_present` — **PASSABLE** once `opencode:instructions/CONTEXT.md` is removed (ledger); every other loader-kind literal is present (counts above; omp side unchanged).
2. `surfaces.no_uncovered_class` — **PASSABLE** (already PASS on v2.1.4; opencode generic call-shape extraction is empty; omp 8 pairs all declared).
3. `surfaces.opencode_extract` — **NOT PASSABLE**. The frozen ledger conjunct keeps 8 of 9 base opencode classes byte-identical (only CONTEXT.md, the unique absent literal, may be ledgered). Honest loader evidence on v2.1.4 covers at most 5 of the 8 (`instructions/AGENTS.md`, `config/AGENTS.md`, `config/instructions`, `config/instructions-remote`, `read-hook/instructions`). `instructions/CLAUDE.md`, `claude-home/CLAUDE.md` (no loader; template/prompt mentions only) and `instruction-context/AGENTS.md` (no InstructionContext.observe/system-context-builtins subsystem) have no honest rule anchor → `declared ⊄ extracted` in every honest world.
4. `surfaces.table_parity` — **PASSABLE** (substrate-independent; keep inventory § B′ in sync with the baseline).
5. `surfaces.literal_parity` — **PASSABLE**.
6. `surfaces.kind_parity` — **PASSABLE**.
7. `surfaces.excluded_reason` — **PASSABLE**.

**Population N = 6 of 7. Recommended target: freeze `p == 6` (margin 0 vs the reachable set; `p == 7` is structurally infeasible without dishonest rules).** The committed addendum must state the census command (`verify_surfaces.py --omp-binary …omp.real --opencode-binary …opencode --json` plus the grep counts above) and this margin.
