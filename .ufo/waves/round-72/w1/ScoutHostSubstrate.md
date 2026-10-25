# ScoutHostSubstrate — round-72 wave-1 sweep (C2 freshness / host substrate)

**Verdict:** The drift is **path-only for omp, lineage for opencode**, exactly as the frozen plan states. Lane files name the drifted paths in **5 live verifier constants** (edit by L1), **2 present-tense SKILL.md statements** (edit), and **1 live pin data file** (opencode pin re-pin + note append; omp pins stay valid — bytes identical). Every other hit is a dated historical record (lessons, plans, scorecard, log, knowledge entries, fixtures, dated baseline notes) → leave.

## 1. Live host values measured (2026-10-25, commands run read-only)

`ls -la /home/vgpnk/.local/bin/omp /home/vgpnk/.local/bin/omp.real /home/vgpnk/.opencode/bin/opencode` + `sha256sum` + `stat`:

| path | size | sha256 | mtime | version |
|---|---|---|---|---|
| `~/.local/bin/omp` (wrapper) | 1,680 B | `ed62a41ec662fd80b3ca522896375b75cec4638e413dd2592f109a716853b2e1` | 2026-10-23 20:47:22.557636701 -0300 | — |
| `~/.local/bin/omp.real` (real binary) | 256,702,432 B | `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4` | 2026-10-21 20:37:24.615549837 -0300 | `omp/18.12.6` |
| `~/.opencode/bin/opencode` | 240,416,944 B | `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` | stat mtime `1985-10-26 05:15` (packaged build stamp) | `opencode v2.1.4` |

`omp.real` sha256 and ns-exact mtime **equal the r51 pin** (`verifiers/baseline.json` lines 5–6); the wrapper is 1,680 bytes of Bourne shell (`# omp crash-restart wrapper (installed 2026-10-23 after a SIGSEGV freeze series …)`, `BIN="${OMP_REAL:-$HOME/.local/bin/omp.real}"`, one-shot pass-through, restart on rc 132–139, max 5). So the omp half is a pure path move wrapper → `omp.real`. The opencode half is a new binary lineage (v2.1.4 at `~/.opencode/bin/opencode`); the old npm npx ELF path is gone (`[Errno 2] No such file or directory: '/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe'`).

## 2. Sweep — every lane file naming the drifted substrate paths/versions

Commands (each run from the lane root, excluding `.git` and `.ufo`):
`grep -rn --exclude-dir=.git --exclude-dir=.ufo '\.local/bin/omp' .`, `'…npx/e2094862b59aac7b' .`, `'opencode\.exe' .`, `'1\.19\.4' .`, `'1\.19\.3' .`, `'CONTEXT\.md' .`, `'GEMINI\.md' .`, plus follow-ups `'omp\.real'`, `'\.opencode/bin'`, `'2\.1\.4'`, `'18\.12\.6'`.

### Live defaults (verifier constants) — EDIT (L1 lands; counter runs at own defaults)

| file:line | kind | old | new |
|---|---|---|---|
| `verifiers/check_substrate_pins.py:65-66` | live const `BINARIES` | `/home/vgpnk/.local/bin/omp` ; `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` | `~/.local/bin/omp.real` ; `~/.opencode/bin/opencode` (also `--omp-binary`/`--opencode-binary` defaults at :308-309) |
| `verifiers/verify_surfaces.py:164-165` | live const `DEFAULT_BINARIES` | same two old paths | same two new paths |
| `verifiers/verify_harness_claims.py:53,56` | live const `OMP_BIN`/`OC_BIN` | `HOME/".local/bin/omp"` ; `HOME/".npm/_npx/e2094862b59aac7b/…/opencode.exe"` | `HOME/".local/bin/omp.real"` ; `HOME/".opencode/bin/opencode"` |
| `verifiers/verify_harness_independent.py:123` | live const `DEFAULT_OMP_BINARY` | `/home/vgpnk/.local/bin/omp` | `/home/vgpnk/.local/bin/omp.real` (no opencode-binary default exists) |
| `verifiers/verify_harness_claims.py:14,19` | docstring host-path description | same old paths | update descriptions to new paths+versions |

### Baseline pin data (live data file) — EDIT

| file:line | kind | old | new |
|---|---|---|---|
| `verifiers/baseline.json:10` | pin `opencode_binary_sha256` | `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7` (1.19.4) | `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` (v2.1.4) |
| `verifiers/baseline.json:11` | note `opencode_round53_note` | records the 1.19.4 pin/lineage | keep as dated record; append a new round-72 note (opencode_round53_note is a dated record, not edited) |
| `verifiers/baseline.json:5-6` | pins `omp_binary_sha256`/`omp_binary_mtime` | `85d9daf3…` / `2026-10-21T20:37:24.615549837-03:00` | **unchanged** (omp.real matches ns-exact) — no edit needed |

### Present-tense statements — EDIT

| file:line | kind | old | new |
|---|---|---|---|
| `SKILL.md:546-549` | present-tense host statement | “opencode — npm `opencode-ai` 1.19.3 since round 47 (the `~/.local/bin/opencode` npx wrapper; pinned ELF and lineage in `verifiers/baseline.json` and `corpus/knowledge/instruction-surface-census-round13.md` § B′; the round-8/18 `~/.opencode/bin` install is gone)” (24 words) | host runs `~/.opencode/bin/opencode` v2.1.4 (sha `ca9b3ee2…`); the npx 1.19.3 lineage is the round-47–53 record |
| `SKILL.md:563` | present-tense host statement | “`~/.local/bin/omp` embedded JS (`strings -n 6`; cite anchors, not offsets —” (14 words) | `~/.local/bin/omp.real` embedded JS (the wrapper is a 1,680-byte restart script with no embedded JS) |

SKILL.md is 600/600 lines at base; any replacement must stay within the budget (state, don't land).

### Dated historical records — LEAVE (append-only / dated / fixtures)

- **plans** (committed history): `plans/round-51.md:12,80`; `plans/round-72.md:33-45,112-138` (this round's plan, itself the record of the drift); `plans/round-47.md:13`.
- **SCORECARD.md:32** — round-53 freshness entry (historical scorecard record).
- **LOG.md:66,1681** — log lines.
- **corpus/lessons/** (append-only): round-5:33; round-47:5,38; round-48:31,46-51,53; round-49:235; round-50:48-49; round-52:15,141; round-52-spotcheck:74-75,124; round-53:4,14,32,69; round-53-spotcheck:52,62-63,160,205; round-56/57/58/59 rows quoting `.opencode/…` docs (rule-file locations, not host install paths).
- **corpus/knowledge/** (entries with explicit sourcing dates): `render-mechanism-round7.md:11-13` (round-7 binary 18.4.2/285,672,928 B/mtime 2026-09-28); `skill-activation-telemetry.md:17-21` (round-7 supersession note: template at offset 283082932 in `~/.local/bin/omp`, absent from `~/.opencode/bin/opencode` — both paths as-of round 7); `harness-verifier-round10.md:28,34` (round-10 recipe; sha `55016ef5…` era); `claude-md-surface.md:9` (round-6 sourcing: `~/.opencode/bin/opencode` → 9 occurrences); `instruction-surface-census-round13.md:47` (round-13 call-shape scan method), `:214-219` (B′ header: “re-derived 2026-10-21 for 1.19.3, round 47”), `:251` (OC-1 class literal `CONTEXT.md`), `:306-317,344` (round-47 ledger), `:547-577` (“Round-53 re-derivation (2026-10-22, opencode 1.19.4, append-only)”); `opencode-extraction-round14.md:15,50,85,106-119` (round-14 loader rules, incl. `~/.opencode/bin/opencode` dump line 107); `alwayson-rule-files-round53.md:27` (v1.19.4-era loader facts incl. deprecated `CONTEXT.md` name), `:34` (omp row: names installed binary's sha `85d9daf3…` — still the current sha, no drifted path); `instruction-surface-remeasure-round13.md:17,24,38`; `skill-listing-thresholds-round54.md:18` (v1.19.4 source); `opencode-offer-trace-round8.md:6,130` (2026-09-14 ELF); `round49/51` overlap entries naming omp 18.12.6 (current binary, no drifted path).
- **corpus/SOURCES.md** — S015:28, S016:29, S024:37, S039:52, S045:58, S046:59, S048:61, S050:63, S051:64, S060:73, S107:119 etc. (dated registry rows; S015 names the frozen 18.12.5/1.19.3 snapshot).
- **corpus/README.md:149** (round-51 Frontier row) and **:168-170** (round-53 append-only note on the Loader-rule freshness row — the C2 surface; a round-72 note gets appended, the 53 note stays).
- **verifiers/baseline.json:7-9,14** — dated `omp_round21/44/51_note` and `round47_note` (round-47 note documents the channel move and the old `~/.opencode/bin` v2.0.26 removal).
- **verifiers/fixtures/surfaces/** — `strings-opencode-1.19.4-anchors.txt`, `strings-opencode-1.19.4-decoy-*.txt`, `strings-opencode-clean.txt`, `strings-opencode-drop-*.txt`, `strings-omp-18.12.6.txt` etc.: synthetic dumps/fixtures named for the frozen versions (self-test regression arms; not host-path statements). Leave.
- **verifiers/verify_surfaces.py:20-53,180,561,1223-1245** — dated per-round callee-history comments (18.12.6 era; comment at :561 notes the old v2.0.26 binary is gone).
- `grep '2\.1\.4'` finds only `plans/round-72.md:42,45,113,129` — no other lane file names the new version yet.

## 3. Do the harness-claim instruments reach their omp claims pointed at omp.real?

Flags/constants: `verify_harness_claims.py` `--omp-bin`/`--oc-bin` (defaults `OMP_BIN`/`OC_BIN`, lines 53/56); `verify_harness_independent.py` `--omp-binary` (default `DEFAULT_OMP_BINARY`, line 123); `compare_harness_independent.py` forwards **no** binary paths — it only exposes `--live-cmd`/`--independent-cmd` overrides.

- `verify_harness_claims.py` at default (wrapper): exit 2 — `INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)`.
- `verify_harness_claims.py --omp-bin omp.real --oc-bin ~/.opencode/bin/opencode --json`: **yes, omp ELF claims reached** — `PASS omp.elf.template_sha256` (c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51), `PASS omp.elf.template_bytes` (273). Full 28-check table (observed vs baseline): **17 PASS / 11 DRIFT**. PASS: template_sha256, template_bytes, offered.dangling 0, descriptions.over_cliff 74, names.mismatches [], descriptions.missing [], unmodelled 0, catalogue.found true, oc.log.init_count_max 0, available_skills_hits 0, skills_tag_hits 0, dup.roots_both_sided 0, dup.onesided_roots [], init_count_monotone [], permission.skill_lines 0, permission.skill_allow 0, roots.plugins_cache false. DRIFT (host-state or v2.1.4 grammar, not path failures): omp.db.rows 216 vs 14, db.rows_wellformed 135 vs 14, offered.skills 75 vs 7, cache.keys_reproduced 15 vs 7, cache.misses 60 vs 0, catalogue.total 206 vs 7, catalogue.matched 15 vs 7, catalogue.missing_names [long list] vs [], cache.verified_skills 75 vs 7, oc.log.skills_rescan_max 0 vs 3, oc.roots.names_plus_builtin 75 vs 7.
- `verify_harness_independent.py --omp-binary omp.real --json`: **yes** — template rows `DERIVED` (bytes 273, sha c1f03c8e…), no SUBSTRATE error. At default (wrapper): exit 2 `SUBSTRATE template marker absent from the omp binary`.
- `compare_harness_independent.py`: **does not currently reach a claim verdict** — at defaults it errors `live instrument failed with no stdout: exit 2: INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)`; with both `--live-cmd`/`--independent-cmd` overrides pointed at omp.real, it exits 2 at the false-blocker scope guard before any comparison: `compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found: every blind-plausible rule agrees on one total [206], so the row is derivable without reading the harness's rule and is not out of scope; …` (repeated for catalogue.matched/missing_names/total). This is a pre-existing instrument-state block (live probe data now contradicts the committed scope file), independent of the binary pointing, and blocks the join.

## 4. Surfaces confirmation (read-only, live dumps)

`python3 -B verifiers/verify_surfaces.py --omp-binary ~/.local/bin/omp.real --opencode-binary ~/.opencode/bin/opencode --json` → `pass=5 fail=2 exit_code=1`. Failures: `literal_present` — “1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)”; `opencode_extract` — “vacuity: extraction produced 0 class(es) from 7 rule(s); … declared opencode class(es) produced …”. Passes: no_uncovered_class, table_parity (42 ids), literal_parity, kind_parity, excluded_reason; substrate readings confirm `omp.real` sha 85d9daf3… and opencode sha ca9b3ee2… were read from the new paths. This matches the plan's `pass 5 fail 2` with the flags.

## 5. Notes

- No tools installed/upgraded (nothing needed); no git/jj writes; no committed lane file touched. Scratch `/tmp/k72w1-surfaces.*` deleted.
- Unobserved: I did not run the lane gates or the C1/C3 counters (other seats); this report is the C2 substrate sweep only. The Q45 census (which of the 7 surfaces checks honest derivation can pass on v2.1.4 bytes) belongs to the re-derivation executor seat; my run shows the current honest default-path instruments fail exactly the two opencode-rule checks.
- Correct values today: omp → `~/.local/bin/omp.real` (sha `85d9daf3…`, mtime `2026-10-21T20:37:24.615549837-03:00`, `omp/18.12.6`); opencode → `~/.opencode/bin/opencode` v2.1.4 (sha `ca9b3ee2…`, 240,416,944 B).
