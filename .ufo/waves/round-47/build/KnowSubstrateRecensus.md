verdict: omp 18.12.5 re-derives cleanly (8/8 loader classes by a callee-agnostic shape, 0 extra), but opencode 1.19.3 is a different rule lineage (round-14 v1 shapes present, round-18 2.x shapes absent) and the default opencode path is gone, so a sha re-pin alone leaves surfaces exit 1 and pins exit 2 — L1 must re-derive opencode rules per lineage and move the default path before any "7/7 / 3/3 exit 0 at default" claim is written.

# Round-47 substrate re-census — report and draft knowledge entry

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git log -1`: `c61a973 round-46 verifier spot-check`). `git --no-optional-locks status --porcelain` → only `?? .ufo/waves/`, `?? plans/round-47.md`; production files unchanged. No production file was written; no git mutating command, no install, no pacman transaction, no opencode execution.

Draft entry: §D below (to land as `corpus/knowledge/substrate-recensus-round47.md`). Artifacts in `.ufo/waves/round-47/build/`:
- `KnowSubstrateRecensus.surfaces-snapshot.json` — `verify_surfaces.py --json` output, snapshot binaries.
- `KnowSubstrateRecensus.pins-snapshot.json` — `check_substrate_pins.py --json` output, snapshot binaries.
- `KnowSubstrateRecensus.probe-omp.py` / `.probe-omp.out.txt` — callee-agnostic omp loader extraction, 8/8.
- `KnowSubstrateRecensus.probe-oc.py` / `.probe-oc.out.txt` — opencode v1-vs-2.x anchor presence counts.

## A. Commands run (exit codes)

| # | command (cwd = BASE lane) | exit | key output |
|---|---|---|---|
| 1 | `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` | 0 | 4/4 `OK`. (A first attempt from the lane root returned 1 with `No such file` — a wrong-cwd read error, not a mismatch; `SHA256SUMS` lists `bin/…` relative paths.) |
| 2 | `python3 -B verifiers/verify_surfaces.py --json --omp-binary /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 --opencode-binary /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3` | 1 | `pass 4 / fail 3`; FAIL `surfaces.literal_present`, `surfaces.no_uncovered_class`, `surfaces.opencode_extract` (detail §C). |
| 3 | `python3 -B verifiers/check_substrate_pins.py --json --omp-binary <snap omp> --opencode-binary <snap opencode>` | 1 | `pass 0 / fail 3`, all DRIFT: omp sha `fdbc8136…` ≠ pin `9513ef9f…`; omp mtime delta `140082506863270` ns; opencode sha `179ca421…` ≠ pin `d9123b9b…`. |
| 4 | `python3 -B verifiers/check_substrate_pins.py` (default) | 2 | `ERROR UNREADABLE opencode_binary_sha256: … '/home/vgpnk/.opencode/bin/opencode'`; `DRIFT 3/3`. |
| 5 | `python3 -B verifiers/verify_surfaces.py` (default) | 2 | `ERROR opencode binary not found: /home/vgpnk/.opencode/bin/opencode`. |
| 6 | `omp --version` | 0 | `omp/18.12.5`. |
| 7 | `sha256sum ~/.local/bin/omp`; `stat` both omp files | 0 | live omp == snapshot: sha `fdbc8136…`, mtime `2026-10-21 03:30:38.135013187 -0300`, 256575456 bytes. |
| 8 | `npm view opencode-ai dist-tags.latest` (metadata only) | 0 | `1.19.3`. |
| 9 | `npm view opencode-ai time --json` (grep) | 0 | `"1.19.3": "2026-10-16T12:32:00.280Z"`. |
| 10 | `npm view opencode-ai@2.0.26 version` | 0 (npm E404) | `No match found for version 2.0.26` — the round-18 `2.0.26` line is not on this registry. |
| 11 | `sha256sum` + `package.json` of `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode` | 0 | sha `179ca421…` (== snapshot); `opencode-ai`, `opencode-linux-x64`, `opencode-linux-x64-baseline` all `1.19.3`. |
| 12 | `cat ~/.local/bin/opencode` (read only; NOT executed) | 0 | 1460-byte bash wrapper: `npx --yes --prefer-online --package opencode-ai`. |
| 13 | `python3 -B .ufo/waves/round-47/build/KnowSubstrateRecensus.probe-omp.py` | 0 | 8/8 baseline loader ids reproduced, 0 extra, missing `[]`. |
| 14 | `python3 -B .ufo/waves/round-47/build/KnowSubstrateRecensus.probe-oc.py` | 0 | anchor counts §B.2 (~53 s). |
| 15 | `strings`-level greps on the two snapshot dumps (`grep -n`, `grep -c`, `grep -o`) | 0 | line refs cited below. |

Not run: `--self-test` of either verifier; `verify_harness_claims.py`; `verify_skill_checklist.py`; corpus-integrity/independent verifiers (before-values are taken from `.ufo/waves/round-47/before/SUMMARY.md`, not re-measured).

## B. Findings (path:line at BASE)

### B.1 Substrate identity and pins

- Pins at BASE: `verifiers/baseline.json:4-9` `measured_against`: omp `9513ef9f…` (18.12.2) mtime `2026-10-19T12:35:55.628149917-03:00`; opencode `d9123b9b…` (2.0.26, round 18).
- Default binary paths: `verifiers/verify_surfaces.py:129-130` and `verifiers/check_substrate_pins.py:62-63` both name `/home/vgpnk/.opencode/bin/opencode` — absent on this host (`ls /home/vgpnk/.opencode/bin/` → No such file).
- The mtime pin is compared ns-exact at `verifiers/check_substrate_pins.py:246` (`st_mtime_ns`); the snapshot omp observes `1792564238135013187` ns — matches live `~/.local/bin/omp`.
- `verifiers/check_substrate_pins.py:61-63` BINARIES default is the only resolution; there is no fallback to the npx cache.

### B.2 Opencode distribution change (the lineage finding)

- Old channel: `~/.opencode/bin/opencode` (round 18, v2.0.26, sha `d9123b9b…`). Gone.
- New channel: `~/.local/bin/opencode` is a 1460-byte bash wrapper (mtime 2026-10-03 17:44) that runs `npx --yes --prefer-online --package opencode-ai` and `exec`s the package bin. It re-resolves on every run; not executed here.
- Resolved bin (package `opencode-ai` 1.19.3, `bin/opencode.exe`): `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, sha `179ca421…`, mtime `2026-10-20 18:33:42.152682158 -0300`, 186013824 bytes; `_npx` root `package.json` dependency `^1.19.3`. A second copy at `…/node_modules/opencode-linux-x64/bin/opencode` has the same sha and mtime (`sha256sum`, 2026-10-21); the earlier draft cited that copy as the resolved path, which was wrong. Snapshot copy is byte- and mtime-identical.
- Self-report from strings only: `var n="1.19.3"` (dump line 447186), `--user-agent=opencode/1.19.3` (dump line near 447186). Not confirmed by execution.
- Registry: `1.19.3` published `2026-10-16T12:32:00.280Z`; `2.0.26` → E404. So the round-18 2.0.26 binary did not come from the npm `opencode-ai` package. [INFERENCE] the 2.x binary came from a different channel (the `~/.opencode/bin` installer path) that is no longer in use.
- Volatility: 8 `_npx` hash dirs exist under `/home/vgpnk/.npm/_npx/`; the wrapper names `opencode-ai` with no version, and `--prefer-online` re-resolves `latest`. [INFERENCE] a later release can rewrite bytes behind the same `…/e2094862b59aac7b/…/bin/opencode` path, so the path is stable while the sha moves — the sha pin is the only detector. Falsifier: `npm view opencode-ai dist-tags.latest` ≠ `1.19.3` followed by `sha256sum` of that path ≠ `179ca421…`.

### B.3 Omp registration shapes (18.12.5)

- The verifier's callee alternation `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo` (`verifiers/verify_surfaces.py:150-165`, `OMP_CALL_RE`, `CALLEE_SHAPES`) matches **0** `(<v>, <group>, "<file>.md")` call sites in 18.12.5. The 18.12.2-era names `Co Dl Hj I5 Gl Mo` are still declared in the dump (declaration counts 12, 7, 2, 2, 10, 13) but never used in that shape.
- Callee-agnostic probe (`probe-omp.py`) finds exactly three callee names — `lq`, `Xl`, `Fo` — and reproduces the 8 baseline loader-group ids with **0 extras**:

| id (baseline) | dump line | callee | group binding |
|---|---|---|---|
| `omp:agents-md/AGENTS.md` | 895129 | `lq` | `var f$ = "agents-md"` (895126) |
| `omp:claude-md/CLAUDE.md` | 895140 | `lq` | `var m$` |
| `omp:opencode/AGENTS.md` | 899090 | `Xl` | literal |
| `omp:gemini/GEMINI.md` | 898856 (`Xl`), 898867 (`Fo`) | `Xl`,`Fo` | literal |
| `omp:gemini/SYSTEM_TEMPLATE.md` | 898992 (`Fo`), 898994 (`Xl`) | `Fo`,`Xl` | literal |
| `omp:gemini/system.md` | 898993 (`Fo`), 898995 (`Xl`) | `Fo`,`Xl` | literal |
| `omp:github/copilot-instructions.md` | 899328 | `Fo` | literal |
| `omp:windsurf/memories/global_rules.md` | 900239 | `Xl` | literal |

- Name collision: the dump declares `Xl` 6×, `Fo` 13×, `lq` 2× (`function NAME(` / `var|let|const NAME =`). A callee-name allowlist is minifier-volatile and collides with unrelated functions (e.g. `function Fo(e, t)` at dump line 666858). Keying on a name list is the mechanism of the 0/8 vacuity.
- 18.12.5 changelog: `## [18.12.5] - 2026-10-21` at `omp-18.12.5.strings:2422124`; no registration-shape item named in the first entries read.

### B.4 Opencode registration shapes (1.19.3 vs round-18 rules)

Anchor presence in `opencode-1.19.3.strings` (`probe-oc.out.txt`; line refs from `grep -n`):

| anchor family (rule) | round-18 literal (`verify_surfaces.py`) | 1.19.3 | line |
|---|---|---|---|
| OC-1 plugin | `ConfigInstructionPlugin.projectSource` | **0** | — |
| OC-1 (bare) | `projectSource` | 2 (different constructs) | 607465 |
| OC-1 walk-up | `targets:["AGENTS.md"]` | 1 | 445482 (`H.up({targets:["AGENTS.md"],start:S,stop:$})`) |
| OC-2 global | `X(r.config,"AGENTS.md")` | 1 | 443993 (`X.join(r.config,"AGENTS.md")`) |
| OC-4 read hook | `ReadTool.Plugin` | **0** | (`ReadTool.miss/list/warm/readSample` exist, 4 hits) |
| OC-4 | `SessionInstructions.load` | **0** | — |
| OC-5 env gate | `OPENCODE_DISABLE_PROJECT_CONFIG` | 9 | 442392, 443993, 445482 |
| OC-5 switch | `globUp(<v>.directory,<v>.worktree)` (2-arg) | **0** | 1.19.3 uses `globUp(T,d.directory,d.worktree)` (443993, 3-arg) |
| OC-6 API | `/instructions/entries` | 3 (SDK route `/api/session/…/instructions/entries`) | 606940 |
| OC-6 API | `session.instructions.entry.put` | **0** | — |

Round-14 v1 shapes present in 1.19.3 (the lineage the round-14 rules describe, `knowledge/opencode-extraction-round14.md`):
- name-priority array `["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]` — dump 443993;
- `X.join(r.home,".claude","CLAUDE.md")` — 443993;
- `Instruction.resolve` (`fn("Instruction.resolve")`) — 443995, with `<system-reminder>` 18 hits;
- `InstructionContext.observe`, `Key.make("core/instructions")`, `targets:["AGENTS.md"]`, `system-context-builtins` — 445482–445487.

Surfaces check result (`surfaces-snapshot.json`): `surfaces.opencode_extract` FAIL — "declared opencode class(es) produced by no rule: opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md; rule(s) matched nothing: OC-1, OC-4, OC-6". OC-2, OC-3, OC-5 pass. This matches the before-state (`before/SUMMARY.md` line 4) exactly.

Lineage conclusion: 1.19.3 bytes are not the 2.x line the round-18 rules and the five baseline opencode ids were derived from. [INFERENCE, strongly supported] the nearest rule set for this binary is the round-14 nine-id set (`opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`, `opencode:claude-home/CLAUDE.md`, `opencode:config/AGENTS.md`, `opencode:config/instructions`, `opencode:config/instructions-remote`, `opencode:read-hook/instructions`, `opencode:instruction-context/AGENTS.md`). Only OC-5's arity drifts on that set. Whether that set is re-derived (not copied) is for the executor lanes; this entry records the anchor evidence only.

### B.5 Surfaces and pins verdicts at the snapshot

- `verify_surfaces.py` (explicit snapshot binaries): exit 1, 4 PASS / 3 FAIL (`surfaces-snapshot.json`):
  - `surfaces.literal_present` FAIL — 8 loader literals "not verifiable" (no call shape).
  - `surfaces.no_uncovered_class` FAIL — "vacuity: 0 loader class(es) extracted from the omp dump" + "extractor blind: 33 declared literal(s) present in the omp dump but no registration shape extracts" (guard at `verifiers/verify_surfaces.py:538-560`).
  - `surfaces.opencode_extract` FAIL (B.4).
  - PASS: `table_parity` (38 ids), `literal_parity` (38), `kind_parity` (38), `excluded_reason` (9).
- `check_substrate_pins.py` (explicit): exit 1, 0/3 PASS (`pins-snapshot.json`); default: exit 2.

### B.6 Class re-verdicts (BASE → snapshot)

| class | BASE verdict (before/SUMMARY.md) | snapshot verdict | evidence |
|---|---|---|---|
| 8 omp loader-group ids (B.3 table) | FAIL vacuous, 0/8 | **derivable 8/8 by callee-agnostic shape, not yet landed** | `probe-omp.out.txt`; dump 895126–900239 |
| 33 omp literal-only ids | blind (not re-verdicted) | blind, unchanged | `surfaces-snapshot.json` `no_uncovered_class` detail; **carried residual** |
| `opencode:project/AGENTS.md` (OC-1) | FAIL | FAIL — no 2.x anchor; v1 analogues 443993 / 445482 | B.4 |
| `opencode:config/AGENTS.md` (OC-2) | PASS | PASS — 443993 | B.4 |
| `opencode:config/instructions` (OC-3) | PASS | PASS — schema anchor | `surfaces-snapshot.json` |
| `opencode:read-hook/AGENTS.md` (OC-4) | FAIL | FAIL — 2.x `ReadTool.Plugin` absent; v1 `Instruction.resolve` 443995 | B.4 |
| `opencode:api-entries/instructions` (OC-6) | FAIL | FAIL — route 606940 present, `session.instructions.entry.put` absent | B.4 |

## C. Counterexamples and blockers to the plan's C1 acceptance

1. **Default-path acceptance cannot pass as written.** The plan (`plans/round-47.md:24-26`) demands "pins 3/3 exit 0 at the default resolution". The default opencode path `verifiers/check_substrate_pins.py:63` is absent; `check_substrate_pins.py` returns exit 2 (`UNREADABLE`) before any hash compare (observed, run 4). A re-pin cannot make the default exit 0. L1 must either change `BINARIES`/`DEFAULT_BINARIES` (repo change; the npx-cache hash path is itself volatile — B.2) or accept exit 2 and say so.
2. **A sha re-pin is necessary, not sufficient.** With the exact 1.19.3 sha, `surfaces.opencode_extract` still FAILs (run 2). The class set and rules must move with the lineage.
3. **The 0/8 vacuity is name-keyed.** Changing `OMP_CALL_RE` to `Xl|Fo|lq` alone repeats the failure on the next minifier rename (B.3 collision counts). The callee-agnostic shape reproduces 8/8 with 0 extras (run 13); whether to adopt it is an executor/L1 decision.
4. **The `no_uncovered_class` blindness arm is silent on partial blindness.** `verifiers/verify_surfaces.py:573` emits "extractor blind" only `if not pairs` (zero extraction). Once omp extracts ≥1 pair, the 33 literal-only ids stop being reported by that arm. Recorded as a carried residual, not a closure.
5. **The lane recheck command as briefed exits 2.** `python3 -B verifiers/verify_surfaces.py --json` and `python3 -B verifiers/check_substrate_pins.py` (no binary args) exit 2 at the snapshot host (runs 4–5). Under Q04 (`corpus/QUALITY.md`, "every `recheck:` … resolves and runs today") the entry's recheck must carry explicit binary paths until the default is changed.
6. **Version numbers are not monotone across the change.** 2.0.26 (round 18; `verifiers/baseline.json:11` `round18_move`, binary rebuilt 2026-10-14) is not on npm; 1.19.3 is npm-published 2026-10-16. A reader comparing version strings will read a downgrade; the entry must state lineage, not order.

## D. Draft knowledge entry (for `corpus/knowledge/substrate-recensus-round47.md`)

```
# Substrate re-census — omp 18.12.5 / opencode 1.19.3 (round 47)

source: S012 — kotoba own work — `/fast/scratch/kotoba-r47/shared/SHA256SUMS` (4/4 OK, `sha256sum -c` run from that directory, 2026-10-21) and `verifiers/verify_surfaces.py` + `verifiers/check_substrate_pins.py` run against those snapshot binaries
verified-at: 2026-10-21 · BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd · snapshot sha256 unchanged across the run (before = after = §1 table)
recheck: python3 -B verifiers/verify_surfaces.py --json --omp-binary /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 --opencode-binary /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3 — exit 1 at BASE (4 PASS / 3 FAIL) — [L1-FILL: exit after landing]
recheck: python3 -B verifiers/check_substrate_pins.py --omp-binary <same> --opencode-binary <same> — exit 1 at BASE (0 / 3 PASS) — [L1-FILL: exit after landing]
```

Bare-default recheck (no binary args) exits 2 at BASE (`/home/vgpnk/.opencode/bin/opencode` absent). [L1-FILL: state the default after the path change, or keep this line as the documented exit-2 case.]

## 1. Substrate identity — 2026-10-21, BASE c61a973

| substrate | version | sha256 | mtime | bytes |
|---|---|---|---|---|
| omp | 18.12.5 (`omp --version` → `omp/18.12.5`, 2026-10-21) | `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` | 2026-10-21 03:30:38.135013187 -0300 (ns `1792564238135013187`) | 256575456 |
| opencode | 1.19.3 (`npm view opencode-ai dist-tags.latest` → 1.19.3, 2026-10-21) | `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` | 2026-10-20 18:33:42.152682158 -0300 | 186013824 |

Live `~/.local/bin/omp` is byte- and mtime-identical to the snapshot. The opencode bin is the npx-cache copy `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`, identical to the snapshot. Prior pins: omp `9513ef9f…` (18.12.2, 2026-10-19T12:35:55.628149917-03:00); opencode `d9123b9b…` (2.0.26, round 18).

## 2. Opencode distribution change

- Round 18: `~/.opencode/bin/opencode`, v2.0.26, sha `d9123b9b…`. Path absent now.
- Now: `~/.local/bin/opencode` (bash, 1460 bytes) → `npx --yes --prefer-online --package opencode-ai` → `opencode-ai@1.19.3`. The wrapper re-resolves on every run; it was not executed for this entry.
- npm: `1.19.3` published 2026-10-16T12:32:00.280Z; `opencode-ai@2.0.26` → E404 on npm (2026-10-21).
- Lineage, not order: 1.19.3 carries the round-14 v1 rule shapes and not the round-18 2.x shapes (§4). Version strings must not be read as a downgrade or upgrade.
- [INFERENCE] the same cache path can hold a different sha after a later release. Falsifier: a `dist-tags.latest` other than 1.19.3 followed by a sha mismatch at `…/e2094862b59aac7b/…/bin/opencode`.

## 3. Omp registration shapes — 18.12.5

- The verifier's callee set `Id|Cl|jD[ef]|Tl|dr|GW` (legacy) plus `Co|Dl|Hj` (18.11.1, `verifiers/baseline.json` round-21 note) and `I5|Gl|Mo` (18.12.2, round-44 note) matches 0 `(u, group, "<file>.md")` call sites in 18.12.5 — `probe-omp.py`, 2026-10-21.
- Callees now used with `(u, group|var, "<file>.md")`: `lq` (2 sites), `Xl` (5), `Fo` (4) — 3 names — `probe-omp.py`, 2026-10-21 — reproduce the 8 baseline loader-group ids with 0 extra.
- Names collide: `Xl` is declared 6×, `Fo` 13×, `lq` 2× in the dump. A callee-name allowlist is version-specific by construction.
- Residual: 33 declared omp literals are present in the dump with no registration shape; the no_uncovered_class blindness arm is silent once any pair extracts (`verifiers/verify_surfaces.py:573`).

## 4. Opencode registration shapes — 1.19.3

- Present (round-14 v1 lineage): name-priority array with `disableClaudeCodePrompt` gate (dump line 443993); `X.join(r.config,"AGENTS.md")` and `X.join(r.home,".claude","CLAUDE.md")` (443993); `fn("Instruction.resolve")` with `<system-reminder>` (443995); `InstructionContext.observe` + `core/instructions` + `targets:["AGENTS.md"]` + `system-context-builtins` (445482–445487); `OPENCODE_DISABLE_PROJECT_CONFIG` (9 lines).
- Absent (round-18 2.x lineage): `ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`, `SessionInstructions.load`, `session.instructions.entry.put` — 0 each (2026-10-21).
- Changed arity: the switch anchor is 3-arg `globUp(T,d.directory,d.worktree)` (443993), not the round-14 2-arg `globUp(<v>.directory,<v>.worktree)`.
- API route `/api/session/:id/instructions/entries` present (606940); the round-18 API id `session.instructions.entry.put` absent.

## 5. Class verdicts

| class | BASE | 2026-10-21 snapshot |
|---|---|---|
| 8 omp loader-group ids | FAIL, 0/8 | derivable 8/8, callee-agnostic (not yet landed) |
| 33 omp literal-only ids | blind | blind (carried) |
| opencode `project/AGENTS.md` | FAIL | FAIL (2.x anchor absent) |
| opencode `config/AGENTS.md` | PASS | PASS |
| opencode `config/instructions` | PASS | PASS |
| opencode `read-hook/AGENTS.md` | FAIL | FAIL (2.x anchor absent) |
| opencode `api-entries/instructions` | FAIL | FAIL (id absent) |

Measured counts: `surfaces` 4 PASS / 3 FAIL, exit 1; `pins` 0 / 3, exit 1 (explicit snapshot paths) — 2026-10-21.

## 6. Pins — what the L1 must re-record

- omp sha `9513ef9f…` → `fdbc8136…`; omp mtime → `2026-10-21T03:30:38.135013187-03:00`.
- opencode sha `d9123b9b…` → `179ca421…`, with a mechanism note: distribution moved from `~/.opencode/bin` (2.0.26) to the npx cache (1.19.3).
- Pin equality detects change; it does not prove provenance (`substrate-pin-guard-round23.md`).

## 7. Honest ceilings

- Strings-only: no execution, so the 1.19.3 version is self-reported in the dump (line 447186), not observed at runtime.
- Anchor presence is not rule correctness; the class set for 1.19.3 is `[INFERENCE]` until a rule set is re-derived and run.
- Host-local: the npx cache, `~/.local/bin/omp`, and the snapshot are this host's bytes, not upstream release artifacts.

## L1 fill list (after landing; not measured here)

- [L1-FILL] post-landing `verify_surfaces.py --json` pass/fail and exit, default and explicit paths.
- [L1-FILL] post-landing `check_substrate_pins.py` `OK n/3` line and exit; default-path decision.
- [L1-FILL] `--self-test` assertion counts for `verify_surfaces.py` and `check_substrate_pins.py`.
- [L1-FILL] opencode re-derived class count and rule ids for 1.19.3.
- [L1-FILL] omp declared loader-group count after the callee change.
- [L1-FILL] mechanism note text for the pin re-record.
- [L1-FILL] errata placement: append-only errata in `corpus/knowledge/instruction-surface-census-round13.md` and `corpus/knowledge/opencode-extraction-round14.md` (the round-14 file already carries a round-18 errata block at its top) plus a baseline note; the opencode 2.x → 1.19.3 re-verdict is an erratum to held ground, not new ground.
- [L1-FILL] sha256 of `verifiers/verify_surfaces.py`, `verifiers/check_substrate_pins.py`, `verifiers/baseline.json`, `verifiers/surfaces-baseline.json` after landing.
```

Corpus index row proposal (`corpus/README.md`, add after line 58; L1 applies):
`| Substrate re-census (round 47) | \`knowledge/substrate-recensus-round47.md\` + \`../verifiers/verify_surfaces.py\` + \`../verifiers/check_substrate_pins.py\` + \`../verifiers/baseline.json\` | omp 18.12.5 / opencode 1.19.3 re-census on the frozen snapshot; the opencode distribution moved from \`~/.opencode/bin\` (2.0.26) to the npx cache (1.19.3, lineage v1 shapes); 8/8 omp loader ids re-derivable; default paths and pins are the open items |`

S row proposal (`corpus/SOURCES.md`, next free id S012; L1 applies): own-work, tier A, opened 2026-10-21, recheck on-commit; anchor `verifiers/verify_surfaces.py` + `check_substrate_pins.py` run on `/fast/scratch/kotoba-r47/shared/`.

## E. What I did NOT check

- `verify_surfaces.py --self-test`, `check_substrate_pins.py --self-test`, `verify_harness_claims.py`, `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py` — not run; before-values are from `before/SUMMARY.md` only.
- Whether the 9 round-14 opencode ids are fully reproduced on 1.19.3: only anchor presence was counted; no rule set was implemented or run (executor lanes C1OcRuleRederive / C1OpencodeResolve own that).
- The other seven `_npx` hash dirs' contents beyond checking the one opencode package.
- The 33 omp literal-only ids: not inspected individually.
- Whether `~/.local/bin/omp` equals an upstream 18.12.5 release artifact (no upstream sha available here).
- The `2.0.26` provenance beyond "not on npm"; I did not search other registries or the `~/.opencode` installer history.
- Executed behaviour of either binary (not run, by design — `check_substrate_pins.py` hashes and never execs).
- `lessons/round-46.md` § Mistakes, the source of the QUALITY criteria, was not re-read; criteria Q04/Q09/Q10/Q12/Q13 were applied as quoted in `corpus/QUALITY.md`.
- Tools installed or updated: none. No pacman transaction.
