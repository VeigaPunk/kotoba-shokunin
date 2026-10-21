verdict: 806 pattern-rows / 508 distinct file:line locations at BASE; only 10 code locations and 11 present-tense-doc locations are load-bearing — three `~/.opencode/bin` defaults (two hard-fail gates, one fail-open probe), two enforced pins two substrate generations stale, three dated pin-file notes, two stale code comments — and re-pathing the default cannot make C1 green because the surfaces gate's live inventory (§ B of the census) is anchored on a binary generation with zero `ConfigInstructionPlugin` occurrences in the 1.19.3 dump. The other 482 locations are dated history and must not be rewritten.

## Axes (what this census measures)

- **freshness** — do the lane's recorded substrate referents (path, sha, version, inventory) still denote the installed harnesses? Measured: BASE pins vs live binaries; BASE inventory text vs 1.19.3 string dump.
- **operability** — can each gate reach a verdict at its *default* resolution, and does a missing substrate fail closed? Measured: default constants, override flags, and the missing-binary branch in `oc_observations`.
- **calibration** — is each occurrence classified so the round edits the claims and not the receipts? Measured: per-location class, with the append-only boundary (LOG/SCORECARD/.ufo receipts) held separate from live docs and code.

## Scan definition

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; every BASE citation below was read from `HEAD` via `git grep`, so it is committed content, not a worktree guess.

Excluded: `.git/`, the 47,815,579-byte `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`, binary files (`grep -I`), and this seat's own `ScoutVerifierPathRefs.*` artifacts. Worktree-only rows are labelled separately; `plans/round-47.md` and `.ufo/waves/` are untracked at BASE (`git status --porcelain` shows exactly `?? .ufo/waves/` and `?? plans/round-47.md`).

## Counts

`git grep -nI -F -- '<pat>' HEAD -- . ':!.ufo/round-44/evidence/omp-live-18.12.2-strings.txt'` (hits), same with `-l` (files); `grep -rnI --exclude-dir=.git --exclude=omp-live-18.12.2-strings.txt --exclude=ScoutVerifierPathRefs.* -F -- '<pat>' .` (worktree). All commands exit 0 (matches found).

| pattern | BASE hits | BASE files | worktree hits | worktree files |
|---|---:|---:|---:|---:|
| `.opencode/bin` | 174 | 107 | 200 | 120 |
| `opencode/bin/opencode` | 171 | 106 | 192 | 119 |
| `18.12.2` | 55 | 27 | 71 | 36 |
| `18.12.3` | 7 | 6 | 40 | 14 |
| `v2.0.26` | 117 | 62 | 127 | 68 |
| `d9123b9b` | 219 | 129 | 233 | 139 |
| `9513ef9f` | 63 | 46 | 74 | 55 |
| **union** | **806 rows** | **205 files** | — | — |

Worktree figures are at 2026-10-21T12:59-03:00 and are moving because `.ufo/waves/round-47/build/` is being written by peers; 131 added rows / 18 files were untracked round-47 wave metadata and peer reports at that instant. Use the BASE column for anything citable.

`opencode/bin/opencode` ⊃ `.opencode/bin`: all 171 BASE hits of the first are contained in the 174 of the second; the 3-hit delta is prose that names the directory without the file path (`.ufo/round-22/scouts/P2.md:115`, `.ufo/round-23/scouts/V8.md:110`, `.ufo/round-30/scouts/M4.md:22`).

Class totals at BASE — rows (a line matching two patterns counts twice) and distinct locations:

| class | rows | distinct locations |
|---|---:|---:|
| code default | 6 | 3 |
| code pin | 7 | 5 |
| code comment / docstring | 3 | 2 |
| fixture | 5 | 5 |
| present-tense doc | 16 | 11 |
| dated history | 769 | 482 |
| **total** | **806** | **508** |

## Code (10 locations)

### Dead defaults — the pinned path no longer exists

`~/.opencode` exists but is empty: `stat` reports `size=0 mtime=2026-10-20 08:14:11`, and `ls -la /home/vgpnk/.opencode/bin` exits 2 (`No such file or directory`). The parent-directory existence check a future resolver might use would therefore pass while the binary is gone.

1. `verifiers/check_substrate_pins.py:63` — `"opencode": "/home/vgpnk/.opencode/bin/opencode"` in `BINARIES`; `--opencode-binary` override at `:306`. Hard failure at default: `.ufo/waves/round-47/before/check_substrate_pins.py.out:1` `ERROR UNREADABLE opencode_binary_sha256: [Errno 2]`, `:4` `FAIL opencode_binary_sha256: UNREADABLE`, and `.ufo/waves/round-47/before/SUMMARY.md:5` `pins: exit=2 DRIFT 3/3`.
2. `verifiers/verify_surfaces.py:130` — `"opencode": ...` in `DEFAULT_BINARIES`; `--opencode-binary` at `:1035`. Hard failure at default: `.ufo/waves/round-47/before/verify_surfaces.py.out:3` `"error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode"`, `exit_code: 2`.
3. `verifiers/verify_harness_claims.py:55` — `OC_BIN = HOME / ".opencode/bin/opencode"`, consumed at `:640` by `oc_observations(args.oc_log, args.oc_bin)`. **Fail-open**: at `:477-478`, `if binary.is_file(): builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0` — a missing binary yields `builtin=0`, never `Inconclusive`. The harness gate cannot report the missing substrate; it reports `oc.roots.names_plus_builtin` drift instead (`verifiers/baseline.json:86-88` expects 7; live roots yield 10 names, so the check fails for the root-count reason while the builtin facet is silently zero).

### Stale pins — two substrate generations behind

4. `verifiers/baseline.json:5` — `omp_binary_sha256 = 9513ef9f…` (omp 18.12.2). Live `/home/vgpnk/.local/bin/omp` is `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`, `omp/18.12.5`.
5. `verifiers/baseline.json:9` — `opencode_binary_sha256 = d9123b9b…` (opencode v2.0.26). Live referent is the npx-cached ELF `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` (opencode 1.19.3).
6. `verifiers/baseline.json:8` — `omp_round44_note` naming `omp/18.12.2` and `9513ef9f…`; dated provenance inside the pin file.
7. `verifiers/baseline.json:11` — `round18_move` naming `v2.0.26` and `d9123b9b…`; dated provenance.
8. `verifiers/surfaces-baseline.json:3` — `assembled` note `"round 18 (2026-10-14): opencode classes re-derived for the 2.x binary (sha256 d9123b9b…)"`; this is the class-table provenance for the class set the surfaces gate compares against.

The third failing pin is `verifiers/baseline.json:6` (`omp_binary_mtime`, 2026-10-19T12:35:55), which none of the seven patterns match; it is cited from the receipt, not from this scan.

### Stale code comments

9. `verifiers/verify_harness_claims.py:19` — module docstring names ``opencode `~/.opencode/bin/opencode` string `available_skills` `` as the authority for the mechanism. The path is dead, and the script's only binary read is the `customize-opencode` byte search at `:477-478`; the `available_skills` counter at `:504` is taken from the **log**, not the binary (`available_skills_hits`). The provenance line therefore names a file the gate never reads and a string it never checks on the binary.
10. `verifiers/verify_surfaces.py:143` — callee provenance list ends at `I5/Gl/Mo (2026-10-18, 18.12.2)`; the live omp is 18.12.5, so C1's re-derivation must name the 18.12.5 callees here or the provenance lies.

## Fixtures (5 locations, no path references)

`verifiers/fixtures/surfaces/baseline-clean.json:2`, `baseline-excluded-noreason.json:2`, `baseline-rekind-doc.json:2`, `baseline-rekind-partial.json:2` (`$comment`: "Round 18: opencode half re-derived for the v2.0.26 rule set (OC-1..OC-6 …") and `strings-opencode-clean.txt:1` ("synthetic opencode strings-dump fixture (round 18 — v2.0.26 rule set)"). These are synthetic regression fixtures. They carry **no** `~/.opencode/bin` reference; replacing the token `v2.0.26` in them would relabel a fixture whose shape may still be the intended regression target, which is not the same decision as moving a live claim.

## Present-tense doc (11 locations)

Dead path:

- `SKILL.md:431` — `## Sources` lists `` `~/.opencode/bin/opencode` + upstream `github.com/sst/opencode` (dev) ``.
- `corpus/knowledge/claude-md-surface.md:9` — evidence line `` `~/.opencode/bin/opencode` → 9 occurrences ``; the file is "Sourced 2026-09-28 (round 6)" with no later errata on this fact.
- `corpus/knowledge/skill-activation-telemetry.md:21` — `` `~/.opencode/bin/opencode` or `pi_natives` ``; the file's supersession block covers a different fact (render mechanism), not the binary location.

Version/inventory claims (the machine-coupled ones):

- `corpus/knowledge/instruction-surface-census-round13.md:12,23,162,169,177,223` — the round-18 errata declares § B the **live** opencode model and byte-verifies it against `d9123b9b…`/v2.0.26. This file is `DEFAULT_INVENTORY` for `verifiers/verify_surfaces.py:132`, i.e. its `## Class inventory` table and § B literals are compared by `surfaces.table_parity` and feed the opencode extraction check — a code-coupled document, not free prose.
- `corpus/README.md:74` — frontier row "omp 18.12.3 drift leaves surfaces 5/7 and pins 1/3".
- `PROVINCE.md:21` — frontier bullet "the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3)".

## Dated history (482 locations, must not be rewritten)

- `LOG.md` (append-only) and `SCORECARD.md` (round rows and planned text): `18.12.2` ×5 / ×3, `18.12.3` ×1 / ×1, `v2.0.26` ×4 / ×1, `d9123b9b` ×2 / ×1, `9513ef9f` ×3 / ×1.
- `.ufo/round-*/**`: 183 of the 205 files. Dominant rounds for `.opencode/bin`: round-21 (25 files), round-23 (21), round-46 (12), round-44 (10), round-22 (8).
- Four `corpus/knowledge` files whose headers explicitly mark the content historical: `opencode-extraction-round14.md` (2026-10-14 errata: "The subsystems described below are **historical** … preserved verbatim"), `opencode-offer-trace-round8.md` (round-8 measurement, including binary size/BuildID/mtime), `harness-verifier-round10.md:216` ("Round-24 erratum … the v2.0.26 log grammar no longer prints …"), `harness-independent-round37.md:378` (round-37 drift receipt).

Untracked-at-BASE current-round material (not counted above): `plans/round-47.md:12-13` records the 18.12.3 → 18.12.5 move and the dead path; `.ufo/waves/round-47/before/*` holds the current receipts; `.ufo/waves/round-47/build-spec.json` / `build-dispatch.json` embed this seat's prompt text and therefore contain the patterns by construction, not as references.

## Load-bearing findings

**F1 — Two hard failures and one fail-open share one dead constant.** Moving `check_substrate_pins.py:63` and `verify_surfaces.py:130` is necessary for the default-resolution green C1 promises; moving `verify_harness_claims.py:55` is necessary for its docstring and its builtin probe to mean anything. The override flags make the gates *operable now* with an explicit path, but C1's "at the default resolution" clause cannot be met without editing the constants; a value-only re-pin leaves both gates at exit 2.

**F2 — The pin set is two generations stale on both harnesses.** omp 18.12.2/`9513ef9f` vs live 18.12.5/`fdbc8136`; opencode v2.0.26/`d9123b9b` vs 1.19.3/`179ca421`. The receipt already shows the omp half as a sha drift and the opencode half as unreadable (`before/check_substrate_pins.py.out:2-4`). Re-pinning is a three-value edit (`:5`, `:6`, `:9`) plus a new dated note; `:8` and `:11` should be preserved and a `omp_round47_note` appended, following the file's own precedent.

**F3 — The missing opencode substrate is invisible to `verify_harness_claims.py`.** The fail-open at `verifiers/verify_harness_claims.py:477-478` turns "binary absent" into `builtin=0`. The only check that touches the builtin (`oc.roots.names_plus_builtin`) then fails for a different reason: live roots produce 10 names (`~/.agents/skills` 10, `~/.claude/skills` 1, `~/.config/opencode/skills` absent) against a pinned 7. So the gate's exit 1 does not localize the substrate loss, and a future host with exactly 7 root names would **pass** with the binary absent. [INFERENCE from code reading; not executed.]

**F4 — The surfaces inventory is anchored on a vanished generation.** `verify_surfaces.py:132` uses the census as its inventory. In the frozen `opencode-1.19.3.strings` dump (`strings -n 4`, 67,839,091 B): `ConfigInstructionPlugin` = **0** occurrences, the central anchor of § B's "Project source" rule; `InstructionContext` = 2 and `system-context-builtins` = 1, both of which the census calls absent in v2.0.26; `available_skills` = 3 and `customize-opencode` = 2 (the builtin name survives). [INFERENCE] A path+sha re-pin would leave `table_parity`/`opencode_extract` comparing against class literals the live binary no longer carries; C1's "re-derive, then re-pin" ordering is therefore load-bearing, not ceremonial. This is a string-level signal only — I did not attempt the re-derivation.

**F4b — The version lines differ, and the anchors are not monotone.** The retired binary reported `opencode v2.0.26`; the npx package resolves as `opencode-ai` 1.19.3 (`.ufo/waves/round-47/before/SUMMARY.md:12`). I did not establish whether these are the same release train, so a re-derivation must not assume a v2.0.26→1.19.3 delta narrative. The string counts reinforce that: `InstructionContext` and `system-context-builtins` are present again after the census recorded them gone, so the pre-2.0 round-13/14 model may be closer to 1.19.3 than the v2.0.26 model is. Re-derive from the 1.19.3 dump, not from the v2.0.26 table plus a patch.

**F5 — Three candidate "new default" referents with different stability.** (a) `~/.local/bin/opencode` is a 1,460-byte bash script (`sha256 b240efa9…`) that runs `npx --yes --prefer-online --package opencode-ai`; pinning it records a stable hash of an unstable referent. (b) the npx-cache ELF `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode` = `179ca421…`; a second variant (`opencode-linux-x64-baseline`) also exists, so "the opencode binary" is ambiguous by path alone, and the cache directory can be pruned. (c) `/fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3` = `179ca421…`, immutable but outside the lane and read-only. The pin should name which of these it means and record that the wrapper is not the substrate.

**F6 — The frontier docs were stale before the round began.** `corpus/README.md:74` and `PROVINCE.md:21` still say omp 18.12.3 / surfaces 5/7 / pins 1/3, while the same BASE's own receipt records 18.12.5 and surfaces exit 2. This is a calibration defect independent of the re-pin: the frontier text lagged one substrate move already, so updating it to the post-round values is a correction, not a claim of improvement.

**F7 — Append-only boundary.** 769 dated-history rows (482 locations) are receipts: LOG.md, SCORECARD.md, `.ufo/round-*`, and the four corpus files whose headers declare the content historical. The only dated text inside a code file that needs care is `verifiers/baseline.json:8,11` — dated provenance, preserved by appending a new note rather than editing the old ones.

**F8 — `~/.opencode` is an empty directory, not a missing one.** `size=0`, mtime `2026-10-20 08:14:11`. Any resolver that checks the parent passes; only file-level probes fail. No current lane code checks the parent, so this is a hazard for the new resolver, not an existing bug.

**F9 — Self-reference hazard for any future grep-based gate.** This report, the TSV, and peers' build reports all contain the patterns. My counts exclude `ScoutVerifierPathRefs.*`; a lane-wide gate must exclude the build directory or it will count its own evidence.

## Counterexamples (things a careless reading would get wrong)

- "opencode is gone" — false. The harness is present twice over (npx-cache ELF `179ca421…`, and a wrapper on PATH); only the pinned absolute path is gone.
- "every `.ufo` hit is stale" — false for `.ufo/waves/round-47/before/*`, which are current-round measurements of this BASE. They are still dated receipts, not live claims.
- "`18.12.2` is only history" — false. `verifiers/baseline.json:5` is the live omp pin; that occurrence is code, not history.
- "`v2.0.26` is one claim" — false. It appears as a live inventory claim (census § B), a dated note (`baseline.json:11`), and a synthetic fixture label (5 files). A global replace would corrupt the fixtures.
- "the strings dump does not matter" — excluding it changes the `18.12.2` BASE count from 64 to 55 (9 literal hits inside the 47.8 MB dump). The exclusion is required by the item and is stated here for reproducibility.
- "the tool wrapper is the binary" — false. `file ~/.local/bin/opencode` says `Bourne-Again shell script`; its sha differs from the ELF's.

## What I did NOT check

- **No gate was executed.** Exit codes quoted for the BASE gates come from `.ufo/waves/round-47/before/` receipts, not from a run by this seat. I did not run `verify_surfaces.py`, `check_substrate_pins.py`, or `verify_harness_claims.py` anywhere (the item names no gate, and the lane contract restricts fan-out gates).
- **No extraction-rule re-derivation.** The 1.19.3/18.12.5 anchor counts are `strings -n 4` substring counts from the frozen dumps; they do not establish call shapes, and `ConfigInstructionPlugin` = 0 could be a mangling artifact rather than a removed subsystem.
- **Binary files are excluded** (`grep -I`). `.jj/working_copy/tree_state` (untracked, binary) contains the 47 MB dump's filename and would add one `18.12.2` hit to a naive `grep -rn`.
- **Not every dated-history row was adjudicated line by line.** Classification there is by path plus explicit errata headers; a few `.ufo/round-46` rows cite yet another omp sha (`065b5079…`), which I noted but did not chase.
- **The npx-cache stability claim is unverified.** I read its current bytes; I did not test whether the path survives a `npx` run or cache prune, and I did not execute the wrapper (forbidden by the lane contract).
- **Archives inside `.ufo`** were not unpacked; grep sees plain files only.
- **Sibling lanes and the fleet root** were not scanned.

## Commands run (exit codes)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `git rev-parse HEAD` | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| 2 | `git status --porcelain` | 0 | `?? .ufo/waves/`, `?? plans/round-47.md` only |
| 3 | `ls -la /home/vgpnk/.opencode` | 0 | empty dir, `.` mtime 2026-10-20 08:14 |
| 4 | `ls -la /home/vgpnk/.opencode/bin` | 2 | `No such file or directory` |
| 5 | `stat -c '%n size=%s mtime=%y' /home/vgpnk/.opencode /home/vgpnk/.local/bin/opencode` | 0 | `size=0`; wrapper `size=1460` |
| 6 | `file /home/vgpnk/.local/bin/opencode` | 0 | `Bourne-Again shell script, ASCII text executable` |
| 7 | `sha256sum /home/vgpnk/.local/bin/opencode` | 0 | `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b` |
| 8 | `sha256sum /fast/scratch/kotoba-r47/shared/bin/{omp-18.12.5,opencode-1.19.3}` | 0 | `fdbc8136…`, `179ca421…` |
| 9 | `/fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 --version` | 0 | `omp/18.12.5` |
| 10 | `sha256sum /home/vgpnk/.local/bin/omp; /home/vgpnk/.local/bin/omp --version` | 0 | `fdbc8136…`; `omp/18.12.5` |
| 11 | `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode` | 0 | `179ca421…` |
| 12 | per-pattern `git grep -nI -F … HEAD -- . ':!…strings.txt'` (7×) | 0 | table above (806 rows) |
| 13 | per-pattern worktree `grep -rnI … --exclude=ScoutVerifierPathRefs.*` (7×) | 0 | table above (moving) |
| 14 | `python3 -B` root-name replication of `oc_observations` | 0 | `~/.agents/skills` 10, `~/.config/opencode/skills` absent, `~/.claude/skills` 1 → union 10 |
| 15 | `grep -c -F <anchor> /fast/scratch/kotoba-r47/shared/{opencode-1.19.3,omp-18.12.5}.strings` | 0 | oc: `ConfigInstructionPlugin` 0, `InstructionContext` 2, `system-context-builtins` 1, `available_skills` 3, `customize-opencode` 2 |
| 16 | `grep -c -F '18.12.2' .ufo/round-44/evidence/omp-live-18.12.2-strings.txt` | 0 | 9 (excluded from all counts) |

## Artifacts

- `.ufo/waves/round-47/build/ScoutVerifierPathRefs.md` — this report.
- `.ufo/waves/round-47/build/ScoutVerifierPathRefs.hits.tsv` — every row (806 BASE rows + 107 untracked-worktree rows captured at 12:58; the delta grew to 131 by 12:59 as peers wrote build reports) with `source`, `pattern`, `class`, `path`, `line`, `text`; 185,353 B.
- `.ufo/waves/round-47/build/ScoutVerifierPathRefs.counts.json` — per-pattern BASE/worktree counts, class totals, distinct-location totals.
