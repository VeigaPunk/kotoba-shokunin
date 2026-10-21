verdict: PARTIAL — C1/C2/C3 counting claims reproduce at 7ad7fad, but the sibling-overlap probe finds kagi, kumitate and kaidoku still recording the removed `~/.opencode/bin/opencode` / opencode 1.18.31 / host omp 18.12.3 as live substrate; only kagi's gate is red, and for unrelated host drift.

## Method

Two canonical-layout scratch clones (the fleet `../` citations resolve):
`/fast/scratch/kotoba-r47/w2/W2SiblingOverlap/kotoba-shokunin` @ `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`
and `.../base/kotoba-shokunin` @ `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
Sibling lanes read only, at their own HEADs (recorded per row in F1). No production or sibling write, no fleet git/jj mutation, no tool installed, no `omp` session launched, the `~/.local/bin/opencode` wrapper never executed.

## F1 — sibling overlap (the assigned target)

"Live substrate" below means a present-tense host/runtime claim in a live gate, instruction file or indexed corpus entry. Dated observation records that carry an explicit observation date or a "re-probe after upgrade" anti-claim are marked DATED; they are still live records and their pointers are dead, but they are not read as a present-tense pin. Historical LOG/lesson lines are listed separately and not counted.

| lane @ HEAD | file:line | what it records | class |
|---|---|---|---|
| kagi-shokunin @ `bdf90f5` (2026-10-21 13:44 -0300) | `SKILL.md:233` | `~/.opencode/bin/opencode` named in the scope-exclusion list of "package-managed host binaries" | LIVE (undated, present tense) |
| kagi-shokunin | `corpus/knowledge/drift-gate.md:161` | same path: "Package-managed host binaries cited in the corpus (`/usr/bin/op`, `/opt/1Password/1Password-BrowserSupport`, `~/.opencode/bin/opencode`) are also unpinned" | LIVE (gate doc, present tense) |
| kagi-shokunin | `corpus/knowledge/handler-trust-boundary.md:8` | "opencode 1.18.31 binary `~/.opencode/bin/opencode`" as source basis | DATED (verified 2026-09-28) |
| kagi-shokunin | `corpus/knowledge/handler-trust-boundary.md:265` | reproduction command `strings -a ~/.opencode/bin/opencode \| grep -c 'SO_PEERCRED\|getpeereid'  # 0` | DEAD-POINTER |
| kagi-shokunin | `corpus/knowledge/handler-trust-boundary.md:276` | "Semantics are opencode 1.18.31 (`ServerAuthConfig`, plugin loader, message-body `tools` override, `/session/{id}/shell`)" — immediately followed by "An upgrade can move any of these — re-probe before citing" | DATED |
| kagi-shokunin | `corpus/knowledge/config-layering.md:4,106` | `opencode debug ...` measured on 1.18.31; "`debug` output is this-version semantics (1.18.31); an opencode upgrade can re-order precedence" | DATED |
| kagi-shokunin | `corpus/knowledge/control-plane-hardening.md:8,16` | "OpenCode 1.18.31 scratch-server auth / alternate-agent repros"; `OPENCODE_SERVER_PASSWORD` behavior 1.18.31 | DATED |
| kagi-shokunin | `corpus/knowledge/handler-on-disk-state.md:7` | "`opencode` 1.18.31, live probes 2026-09-28" | DATED |
| kumitate-shokunin @ `2fa28e5` (2026-10-21 05:17 -0300) | `corpus/knowledge/omp-task-contract.md:2,3,205,207,214` | `verified-at` header "host omp/18.12.3"; `recheck: ... omp --version → omp/18.12.3 (2026-10-19)`; body ":205" "the installed host reports `omp/18.12.3`" | LIVE-PRESENT-TENSE inside a dated entry |
| kumitate-shokunin | `corpus/SOURCES.md:17` | S004 "Installed OMP harness version on this host", anchor "host omp/18.12.3 (2026-10-19)", recheck `on-release` | DATED registry |
| kumitate-shokunin | `corpus/README.md:91` | index summary "docs-on-main vs installed `omp/18.12.3` skew named" | INDEX |
| kaidoku-shokunin @ `69e82c4` (2026-10-21 13:59 -0300) | `corpus/knowledge/2026-10-13-mcp-registrations.md:38` | "opencode (`~/.opencode/bin/opencode`) has `~/.config/opencode/opencode.json` carrying only `$schema`/`theme`/`autoupdate` — no `mcp` key" | DATED (`verified-at: 2026-10-13`) |
| kaidoku-shokunin | `corpus/README.md:15,81` | entry indexed "held"; index date 2026-10-13 | INDEX |
| tsukuroi-shokunin @ `a61db54` (2026-10-21 13:36 -0300) | `corpus/knowledge/update-safety-note.md:273` | repo-shadow row: `opencode` extra `1.18.29-1` vs omarchy `1.1.51-1`, "older, harmless" | EXCLUDED — repo-level shadow table, and `pacman -Q opencode` → "package 'opencode' was not found"; not the installed substrate |

Historical-only lines (append-only or lane note, not counted as live): kagi `LOG.md:70`, `corpus/lessons/round-6.md:39`; kumitate `LOG.md:1458`, `considerthese/2026-10-20.md:6`.

No sibling live tree records opencode `2.0.26`. No hit at all in `kake`, `kengaku`, `revenger`, `chousa`, `kama`, `kasegi`, `mado`, `tabi`, `lore`, `souji`, `mori-shokukin`, `mori-shokunin`, `tameshi-shokukin`, `tameshi-shokunin`, `audio`, `game-dev-2d`, `game-dev-3d`.
False positives screened out: `audio-shokunin/corpus/live/r66-baseline/archive-manifest.txt:5042` (`ui_depth_k1.18.wav`), `game-dev-2d-shokunin/corpus/live/r92-reviewer/manifest.sha256:804-806` (godot `...T21.18.00.log`), `tabi-shokunin/corpus/knowledge/webbridge-plugin-anatomy.md:242` (Kimi extension 2.0.23), kotodama PDF/HTML scratch bytes, `kengaku-shokunin/corpus/SOURCES.md:49` (SciPy 1.18.0).

### Gate coverage of these records

- **kagi**: the binary is deliberately outside `corpus/drift-pins.sh` — `drift-gate.md:161` and `SKILL.md:233` say so; `corpus/drift-baseline.tsv` contains only config/state files, no `~/.opencode/bin/opencode`. `corpus/SOURCES.md` has no opencode-source row. So the stale path has no gate.
- **kumitate**: `node scripts/sources-check.mjs` → exit 0, `SOURCES_CHECK: CLEAN (rows=33 ...)`. The gate validates header presence and dates only (`scripts/sources-check.mjs:381-388` checks `source:`/`verified-at:`/`recheck:` presence; `:330-335` only date overdue), it never executes the `recheck` string. S004's recheck is `on-release`, so nothing goes red at host 18.12.5.
- **kaidoku**: no freshness gate over this entry; `corpus/README.md:15` marks it "held".
- **tsukuroi**: no gate over the shadow table.

## F2 — kagi's live corpus is already materially stale, and its gate says so

`bash corpus/drift-pins.sh` (read-only) → exit 1, `DRIFT_PINS: DRIFT (files_ok=0 files_bad=15 symbols_ok=0 symbols_bad=20)`; 13 `MISSING` + 2 `DRIFT` files. Present at 2026-10-21:
`/home/vgpnk/.local/bin/the-janitor` and the whole `/home/vgpnk/.config/the-janitor/` tree are absent; `/home/vgpnk/.config/opencode/agents/janitor.md`, `tools/janitor_auth.ts`, `plugin/fnm-nudge.js` absent; `~/.config/opencode/opencode.json` changed 455 lines/644 → 5 lines/600 (sha `b270d762…`→`fb067af0…`); `~/.agents/AGENTS.md` 75→14 lines. This is kagi-owned drift, flagged by kagi's own gate; it is context for the sibling-overlap finding, not a kotoba claim, and I did not touch it.

## F3 — C1 reproduces (HOLDS)

In the after clone @ 7ad7fad:
- `python3 -B verifiers/verify_surfaces.py` → exit 0; 7 PASS: `literal_present` 42 entries, `no_uncovered_class` 8 classes, `opencode_extract` 9/9 declared classes from 7/7 rules (OC-1..OC-6), `table_parity` 42 ids, `literal_parity` 42, `kind_parity` 42, `excluded_reason` 8 reasoned.
- `python3 -B verifiers/check_substrate_pins.py` → exit 0; `PASS omp_binary_sha256 fdbc8136…`, `PASS omp_binary_mtime delta 0 ns`, `PASS opencode_binary_sha256 179ca421…`, `OK 3/3 pins hold`.

In the BASE clone @ c61a973:
- `verify_surfaces.py` → exit 2, `ERROR opencode binary not found: /home/vgpnk/.opencode/bin/opencode`.
- `check_substrate_pins.py` → exit 2, 3 FAIL/UNREADABLE, `DRIFT 3/3 pins failed`.

Discriminating cell (after code, BASE baseline+census via `git show c61a973:verifiers/surfaces-baseline.json` and `git show c61a973:corpus/knowledge/instruction-surface-census-round13.md`): `verify_surfaces.py --baseline /tmp/base-surfaces.json --inventory /tmp/base-census.md` → exit 1, 1 FAIL, `surfaces.opencode_extract` naming 3 declared-unproduced (`api-entries/instructions`, `project/AGENTS.md`, `read-hook/AGENTS.md`) and 7 extracted-undeclared ids. The re-derivation is load-bearing, not an id-count swap.

Census claims checked on the frozen dump (`python3 -c '... d.count(anchor)' opencode-1.19.3.strings`): `var n="1.19.3"` 1; `2.0.26` 0; `ConfigInstructionPlugin` 0; `ReadTool.Plugin` 0; `SessionInstructions` 0; `InstructionDiscovery` 0; `disableClaudeCodePrompt` 3; `Instructions from: ` 4; `CONTEXT.md` 1; `ReadTool.execute` 1; `Instruction.resolve` 1. These match `corpus/knowledge/instruction-surface-census-round13.md:212-260` (§ B′) and the ledger at `:287-330` (substring counts, not line counts — `grep -c` would have said 2 for `disableClaudeCodePrompt`).

Host state: `~/.local/bin/omp --version` → `omp/18.12.5`; sha256 `fdbc8136084c…` equals `verifiers/baseline.json:12` and the frozen `SHA256SUMS`. `ls ~/.opencode/bin/opencode` → ENOENT (exit 2). npx-cache ELF sha256 `179ca421d61e…` equals the baseline pin; `.../node_modules/opencode-ai/bin/opencode.exe` and `.../node_modules/opencode-linux-x64/bin/opencode` are hardlinks (same inode `43795736`, link count 2, same BuildID `c30f169b…`), so the before SUMMARY's path spelling and the pin's path spelling name one inode — not a contradiction.

Residual risk: the pinned path is inside an npx cache the wrapper refreshes with `--prefer-online` (wrapper line 31); a later `opencode` invocation can replace the bytes and turn the pins red. That is the drift gate working, but "default resolution" is a cache path, not a stable installation.

## F4 — C2 reproduces (HOLDS)

- `grep -n 'trigger.no_xml_tag' verifiers/verify_skill_checklist.py` → `:97` documentation, `:310` check id list; four fixtures `verifiers/fixtures/checklist/xml-tag-{codespan,control,dq-escape,split}`.
- `sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'` → 0 (grep exit 1).
- `python3 -B verifiers/verify_skill_checklist.py --json` @ 7ad7fad → exit 0, `{checks: 11, pass: 11, fail: 0, na: 0}`.
- Mutation (in the scratch clone only): appended ` <skills>` to the parsed `description` → exit 1, `FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '<skills>' (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)`; restored file → exit 0. `--self-test` → `0 failure(s) over 1845 assertions`, exit 0.
- BASE: frontmatter count 1; `--json` exit 1, `{pass: 9, fail: 1}`.

## F5 — C3 reproduces (HOLDS), with two low-severity provenance nits

- `GOVERNANCE_ERRATA` at `verifiers/verify_skill_checklist.py:377-384`: `(2111, 7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135, ".ufo/round-45/drafts/v10/post-r44-hunt.py", "each exited 2 because the referenced runners are absent")`, horizon 2315. `sed -n '2111p' LOG.md | tr -d '\n' | sha256sum` → `7dcbf123…` (match; the newline-inclusive hash `d7b4c628…` does not match, so the gate's no-trailing-newline canonicalization is what makes the pin true). `LOG.md` is 2326 lines at 7ad7fad; the pinned line is inside the horizon.
- `verify_skill_checklist.py --json` 11/11 exit 0; `verify_corpus_integrity.py --json` exit 0 `tracked_files 60`; `verify_corpus_independent.py --json` exit 0 `tracked_files 60`; `verifiers/fault_injection_corpus.sh` exit 0, `verdict: ALL PASS` (including `fault-f` blind-spot documented and `fault-g` gating context). `corpus/README.md:63-64` indexes `lessons/round-46-verifier-spotcheck.md` and `lessons/round-47.md`.
- BASE: checklist 9/1 exit 1; integrity exit 1 `tracked_files 59`; independent exit 1.
- Nit 1 (records, not gates): `verifiers/baseline.json:2` still says `"as_of": "2026-10-14T09:58:47.702772-03:00"` while `measured_against` was re-pinned 2026-10-21 (`:12`); `verifiers/corpus-baseline.json:2` says `"as_of": "2026-09-29…"` and its `measured_against.head` (`:5`) is `d85982d` (round-16/17) while `checks` expect the round-47 count (`:15` expect 60, `:58` round47 note). No verifier reads `as_of` (`grep -rn as_of verifiers/*.py verifiers/*.sh verifiers/*.json` → only the two definitions), so these are inert provenance fields that no longer describe the file's own measurements.
- Nit 2: `PROVINCE.md:22` pairs "the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3)" with figures it then calls "the round-44 before-column"; it is explicitly historical, but the version label (round-46 host) and the figure vintage (round-44) disagree by the lane's own M20 analysis (`corpus/lessons/round-47.md:19`). Low severity, not a claimed figure.

## Axis impact

- **Freshness**: kotoba's C1 holds locally and is discriminating; the fleet overlay in F1 shows sibling live knowledge is not on the same substrate (kagi's dead path/1.18.31 labels, kumitate's 18.12.3, kaidoku's dead path).
- **Operability**: C2 holds under mutation; no sibling gate consumes the F1 records, so none of them is red because of these records (kagi's red is the separate janitor removal in F2).
- **Calibration**: C3 holds as claimed; the two provenance fields in F5 lag their re-pins but are not gate-read.

Bounded proposal for the integrator (not executed): put the F1 table in the round-47 cross-domain section as routed-not-fixed. The only existing red signal already on disk is kagi's `corpus/drift-pins.sh` (exit 1, F2); cite it instead of opening a new fleet probe. Do not edit siblings.

Risks: sibling line numbers move with their working trees (HEADs recorded); kagi's host removal may be transient; kaidoku's substantive "unregistered" claim may still hold and was not re-read (host config); the 1.18.31→1.19.3 semantic delta is not measured.

## What I did NOT check

- Host-private content: no reads of `~/.config/opencode/opencode.json`, `~/.claude.json`, logs, SQLite DBs, MCP configs or vault; kaidoku's "no mcp key" and kagi's auth/plugin behavior are not re-verified.
- Did not execute `~/.local/bin/opencode`, did not launch `omp` sessions, did not start kagi's handler or scratch servers.
- Did not verify the claimed 2026-10-20 removal date of `~/.opencode/bin/opencode`; only absence at 2026-10-21 and the npx cache mtime 2026-10-20 18:33.
- Did not grep sibling `.ufo` archives beyond the newest three wave dirs per named lane (no hits there); no full git-history search.
- Did not re-run `verify_harness_claims.py` (21/28 is explicitly not claimed), `check_assertion_floors.py`, or `verify_surfaces.py --self-test` under additional mutations beyond the C1 discriminating cell and the C2 description mutant.
- Did not inspect `mori-shokukin`/`tameshi-shokukin` beyond the version/hash sweep; no submodules or vendor trees.
- No production or sibling writes; no tools installed; no pacman query beyond read-only `pacman -Q`.
