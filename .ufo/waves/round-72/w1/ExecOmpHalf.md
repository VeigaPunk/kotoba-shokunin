# ExecOmpHalf — the omp half of the substrate drift (round 72, wave 1)

**Verdict.** The omp half is a **pure path drift, no rebuild**: `~/.local/bin/omp.real` is
`85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, the r51 pin, and the
1,680-byte `~/.local/bin/omp` is a crash-restart wrapper whose `BIN` is that file. Every
omp-facing instrument fails **only** because its default path is the wrapper. A patch that
moves **only the omp default path** (three constants, 1,976-byte diff, sha256
`56e51ed094a6ff701600b28dd46dabd6027df353e3117d50c2be27987a35e44d`) turns exactly **one**
instrument green — `verify_harness_independent.py` (`exit 0`, `24 derived, 4 scoped out, 0
unlanded`). `verify_harness_claims.py` then runs to completion but stays `exit 1` (`17/28
checks pass`) because `verifiers/baseline.json` pins a 7-skill host against today's 75.
`compare_harness_independent.py` stays `exit 2` for a **second, independent reason**: its
scope probe recomputes a census over `~/.omp/agent/sessions`, which grows ~4 blocks/minute
while this wave runs (declared 9649, recomputed 9650 in one run; 9663 → 9667 in 60 s of my own
count) — that is a time race, not a path bug, and it blocks C2's re-pin until fixed.
`verify_surfaces.py` stays `exit 2` because its opencode default path is gone; the omp patch
does move it from 3 failures to 2, and both survivors are opencode-side.

Measured at lane HEAD `e61fd29` (wave-1 spec commit); `git diff --name-only
c69711ee08279609374d895bb0f3c8c18ccf15c9..HEAD -- verifiers/ SKILL.md` is empty, so every
verifier byte below is also the base `c69711e` byte.

## Files changed (mine only)

- `.ufo/waves/round-72/w1/build/ExecOmpHalf/omp-path-only.patch` — the scratch patch (deliverable).
- `.ufo/waves/round-72/w1/build/ExecOmpHalf/{claims-ompreal-json,claims-patched-default,patched-claims,patched-independent,patched-compare,patched-surfaces,surfaces-ompreal,surfaces-ompreal-json,surfaces-wrapper-omp}.txt` — raw instrument output.
- `.ufo/waves/round-72/w1/build/ExecOmpHalf/patch/{verify_harness_claims.py,baseline.json}` — the single-constant copy used for the first isolation run.
- `/tmp/k72-omp-strings.txt` and `/tmp/k72-oc-strings.txt` — **restored** (see F9), byte-identical to the shared inputs.
- This report. No committed lane file touched; no git write outside the throwaway clone (deleted).

## F1 — the omp binary is the r51 pin; the default path is a wrapper

```
$ sha256sum /home/vgpnk/.local/bin/omp.real
85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4  /home/vgpnk/.local/bin/omp.real
$ ls -la /home/vgpnk/.local/bin/omp /home/vgpnk/.local/bin/omp.real
-rwxr-xr-x 1 vgpnk vgpnk      1680 Oct 23 20:47 /home/vgpnk/.local/bin/omp
-rwxr-xr-x 1 vgpnk vgpnk 256702432 Oct 21 20:37 /home/vgpnk/.local/bin/omp.real
$ cat /home/vgpnk/.local/bin/omp        # line 16 of the script
BIN="${OMP_REAL:-$HOME/.local/bin/omp.real}"
```

The wrapper is a Bash restart loop (oneshot passthrough for `-p/--print/--mode=*`, restart on
rc 132–139, max 5). It never contains the ELF payload, so any instrument that opens it as the
binary sees a 1,680-byte text file.

## F2 — default runs (base state, all three instruments + the independent they depend on)

| command (from the lane root) | exit | first failing line (verbatim) |
|---|---|---|
| `python3 -B verifiers/verify_harness_claims.py` | 2 | `INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)` |
| `python3 -B verifiers/verify_harness_independent.py` | 2 | `SUBSTRATE template marker absent from the omp binary` |
| `python3 -B verifiers/compare_harness_independent.py` | 2 | `compare_harness_independent: ERROR: live instrument failed with no stdout: exit 2: INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)` |
| `python3 -B verifiers/verify_surfaces.py` | 2 | `ERROR opencode binary not found: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` |

These match `receipts/base-battery.txt` (`verify_harness_claims exit=2`, `verify_surfaces
exit=2`, `compare_harness_independent exit=2`) — re-run, not inherited.

`verify_harness_claims.py --self-test` is green independently of the substrate:
`self-test: 0 failure(s) over 10 assertions`, exit 0.

## F3 — the omp-path-only patch, and what goes green from it alone

Patch content (three one-line constant changes; nothing else):

```
verifiers/verify_harness_claims.py:53    OMP_BIN = HOME / ".local/bin/omp"        -> ".local/bin/omp.real"
verifiers/verify_harness_independent.py:123 DEFAULT_OMP_BINARY = Path(".../omp")  -> ".../omp.real"
verifiers/verify_surfaces.py:164         DEFAULT_BINARIES["omp"] = ".../omp"      -> ".../omp.real"
```

Applied inside a `git clone --shared` of the lane at `e61fd29` under `mktemp -d
/tmp/k72w1-ExecOmpHalf.XXXX` (fixtures and baseline files stay at their `__file__`-relative
positions), then each instrument run from that clone root with **no flags**:

| instrument | exit after patch | observed tail |
|---|---|---|
| `verify_harness_claims.py` | **1** | `17/28 checks pass; DRIFT: omp.db.rows, omp.db.rows_wellformed, omp.offered.skills, omp.cache.keys_reproduced, omp.cache.misses, omp.catalogue.total, oc.log.skills_rescan_max, omp.catalogue.matched, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin` |
| `verify_harness_independent.py` | **0** | `24 derived, 4 scoped out, 0 unlanded (of 28 named checks)` |
| `compare_harness_independent.py` | **2** | `false blocker: scoped row omp.catalogue.found declares observable {"candidate_blocks": 9649, "distinct_totals": [206], "files_with_skills… but recomputation gives {"candidate_blocks": 9650, …` |
| `verify_surfaces.py` | **2** | `ERROR opencode binary not found: …/node_modules/opencode-ai/bin/opencode.exe` |

**So: one instrument goes green from the omp path alone (`verify_harness_independent.py`).** The
other three stay red for reasons that the omp path does not touch: stale population baseline
(claims), a growing-census race (compare), the missing opencode lineage (surfaces).

## F4 — every omp claim, individually (`--omp-bin …/omp.real --json`, live tree)

`python3 -B verifiers/verify_harness_claims.py --omp-bin /home/vgpnk/.local/bin/omp.real --json`
→ exit 1; observed scalars `template_sha256=c1f03c8e248eb40e… template_bytes=273 db_rows=216
db_rows_wellformed=135 offered_skills=75 keys_reproduced=15 cache_misses=60
descriptions_over_cliff=74 catalogue_total=206 catalogue_matched=15 catalogue_found=True
verified_skills=75 dangling_count=0 name_mismatches=[] no_description=[] unmodelled_count=0`.

| omp check | verdict | observed | baseline |
|---|---|---|---|
| `omp.elf.template_sha256` | **PASS** | `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51` | same |
| `omp.elf.template_bytes` | **PASS** | 273 | 273 |
| `omp.db.rows` | DRIFT | 216 | 14 |
| `omp.db.rows_wellformed` | DRIFT | 135 | 14 |
| `omp.offered.skills` | DRIFT | 75 | 7 |
| `omp.offered.dangling` | **PASS** | 0 | 0 |
| `omp.cache.keys_reproduced` | DRIFT | 15 | 7 |
| `omp.cache.misses` | DRIFT | 60 | 0 |
| `omp.descriptions.over_cliff` | **PASS** | 74 | 7 (mode `positive`) |
| `omp.names.mismatches` | **PASS** | `[]` | `[]` |
| `omp.descriptions.missing` | **PASS** | `[]` | `[]` |
| `omp.descriptions.unmodelled` | **PASS** | 0 | 0 |
| `omp.catalogue.found` | **PASS** | `true` | `true` |
| `omp.catalogue.total` | DRIFT | 206 | 7 |
| `omp.catalogue.matched` | DRIFT | 15 | 7 |
| `omp.catalogue.missing_names` | DRIFT | 60 names | `[]` |
| `omp.cache.verified_skills` | DRIFT | 75 | 7 |

**8 of 17 omp checks PASS, 9 DRIFT, 0 INCONCLUSIVE once the path is right.** Every DRIFT is a
*population* row (how many skills/rows this host has); every *mechanism* row (template bytes,
key reproduction over the loaded descriptions, truncator cliff, name/description agreement,
dangling entries) passes. Independent confirmation of the population, not taken from the
instrument:

```
$ sqlite3 (read-only) ~/.omp/agent/skill-descriptions.db  "select count(*) from skill_descriptions"
216
$ find ~/.agents/skills ~/.omp/agent/skills ~/.config/opencode/skills ~/.claude/skills -maxdepth 2 -name SKILL.md | wc -l
70            # 69 + 0 + 0 + 1; +5 project walk-up = the instrument's offered_skills 75
```

## F5 — does `SKILL.md:23-46` still reproduce against `omp.real`? (claim by claim)

Extraction: the shipped module is embedded unminified; I read it from the binary, not from the
dump: `python3 -c "…find(b'packages/coding-agent/src/extensibility/skill-descriptions.ts')…"`
→ first hit at file offset **0x9a186d6**, module text saved to
`.ufo/waves/round-72/w1/build/ExecOmpHalf/omp-real-skill-descriptions-module.txt` (sha256
`c4c31fe84d05cac71c1b22201c3254525c8ac82f66f670a39c28191a591dde57`).

- **P1 — "the `<skills>` catalogue (template in the omp ELF, rendered per session)"** →
  **REPRODUCED.** `TEMPLATE_ANCHOR` occurs exactly once; 273 bytes; sha256 matches the r51
  baseline (`omp.elf.template_*` PASS). The module binds it as
  `var w = y("/$bunfs/root/compress-description-vm4w5rpa.md")`.
- **P2 — "`render` is `cache.get(key) ?? previewSkillDescription`"** (SKILL.md:27,
  `sed -n '27p'` → "`cache.get(key) ?? previewSkillDescription`: a cached LLM one-liner if the",
  word count 9) → **REPRODUCED, identifier-renamed.** Shipped:
  `description: this.#t.get(D(t)) ?? Bze(t.description)` (in `snapshot`), and `render` does the
  same with a DB fallback then `o = Bze(r.description)`. `previewSkillDescription` exists only
  as an export alias: `Bze as previewSkillDescription`.
- **P3 — "`slice(0, _8n-1)` cut with `_8n=100` (i.e. offset 99)"** (SKILL.md:29,
  `sed -n '29p'` → "`_8n=100` (i.e. offset 99) plus last-space/`…` fallback (`skill-descriptions.ts`;",
  11 words) → **VALUE REPRODUCED, IDENTIFIER DRIFTED.** Shipped: `var v = 100;` … `const r =
  t.slice(0, v - 1);` → `slice(0,99)` = 99 characters, i.e. offset 99, byte-for-byte the
  claimed arithmetic. But `_8n` is **absent from this build**: `grep -c "_8n=100"
  /tmp/k72-omp-strings.txt` → `0`, and the only `_8n` hits are unrelated symbols
  (`_8n]nF`, `_8nR`, `_8nK`). SKILL.md:567 (`_8n = 100`) and the instrument's own header
  comment (`var _8n=100, idl=160, adl=12`) carry the same stale names; this build has
  `var v = 100; var x = 160; var P = 12; var _ = 4000;` — values 100/160/12 reproduce, and a
  **fourth** constant `4000` (cache-close timeout, `setTimeout(t.resolve, _)`) is new.
- **P4 — "plus last-space/`…` fallback"** (SKILL.md:29) → **REPRODUCED but incomplete at :28-30.**
  Shipped `Bze` is: whitespace-collapse+trim → `if (t.length <= v) return t` → `slice(0, v-1)` →
  `r.match(/^.*?[.!?](?=\s|$)/)` kept **if `n.length >= 40`** → else last-space `trimEnd()` →
  `` `${o || r}\u2026` ``. The intro sentence omits the ≥40-char sentence cut; SKILL.md:156 does
  state it ("first sentence if ≥40 chars, else last-space cut + `…`; hard 99-char cliff"), so
  the omission is local to the intro. Both instruments model the guard correctly
  (`verify_harness_claims.py:243-244`, `verify_harness_independent.py:440-441`).
- **P5 — cache at `~/.omp/agent/skill-descriptions.db`** (SKILL.md:31, `sed -n '31p'` →
  "`~/.omp/agent/skill-descriptions.db`). Cache coverage is time-varying — 5/17", 8 words) →
  **REPRODUCED.** Shipped: `O(f.join(e ?? Se(), "skill-descriptions.db"), t)` and
  `CREATE TABLE IF NOT EXISTS skill_descriptions (key TEXT PRIMARY KEY, description TEXT NOT NULL)`;
  the file exists, opens read-only, 216 rows.
- **P6 — the coverage counts ("5/17 at round 7, 17 at round 9, 18 at round 13, all 17 live keys
  still reproducing, the live set is now 7")** → **DRIFTED.** Today: `offered_skills=75`,
  `keys_reproduced=15`, `cache_misses=60`, `db_rows=216`, catalogue block 206 entries with
  15 matched. The *mechanism* sentence (rows keyed per `(name, description-as-loaded)`, never
  pruned) still holds — the shipped key is `sha256(template ‖ 0x00 ‖ name ‖ 0x00 ‖ description)`
  (`function D(e)`), which is why 216 rows coexist with 15 live keys.

Net: **four of six intro claims reproduce (P1, P2, P5, and the numeric core of P3); P3's
identifier and P4's completeness are prose drift; P6's counts are stale by an order of
magnitude.**

## F6 — `verify_surfaces.py` with the omp half correct (the omp rows are already fine)

`python3 -B verifiers/verify_surfaces.py --omp-binary /home/vgpnk/.local/bin/omp.real
--opencode-strings /tmp/k72-oc-strings.txt` → **exit 1**, `5 pass / 2 fail`:

```
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s); …
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
```

Both failures name opencode ids only. Isolation of the wrapper, holding the opencode dump
fixed: `python3 -B verifiers/verify_surfaces.py --opencode-strings /tmp/k72-oc-strings.txt`
(default omp = wrapper) → **3 fail**, the extra one being
`FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted from the omp dump while the baseline declares 8 loader-group class(es) for it`.
So the omp path patch repairs exactly one surfaces check and cannot make the file green —
`p == 7` requires the opencode lineage work (C2).

## F7 — `compare_harness_independent.py` is red for a reason the re-pin will not fix

With both omp constants patched, compare still exits 2, and the message is **not** about the
live column:

```
compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found declares
observable {"candidate_blocks": 9649, "distinct_totals": [206], "files_with_skills… but
recomputation gives {"candidate_blocks": 9650, "distinct_totals": [206], "files_with_skills…;
[same for omp.catalogue.matched, omp.catalogue.missing_names]
```

Cause: the scope contract is `{"kind": "rule-spread-census", "target": "$HOME/.omp/agent/sessions"}`
(`verifiers/harness-independent-scope.json` → `probe_contract`), and both sides compute
`candidate_blocks` by walking every `*.jsonl` under that directory —
`verify_harness_independent.py:420` declares it, `compare_harness_independent.py:1139-1155`
recomputes it and demands equality. The directory is the live omp session tree, and this wave
is writing into it. My own count, same code path:

```
t0      session_files=4798  candidate_blocks=9663
t+60s   session_files=4802  candidate_blocks=9667     (+4 files, +4 blocks in 60 s)
```

A frozen-value equality over a monotonically growing directory can only pass if the two passes
land in the same instant; the observed 9649-vs-9650 is exactly that race. **C2 must not treat
`compare_harness_independent.py` as a re-pin target until the probe is made growth-stable**
(freeze the census to files older than a pinned timestamp, or compare a monotone-lower-bound
instead of equality). I did not change it — out of my seat's file scope.

## F8 — the shared string dumps vanished mid-wave; restored byte-identically

At 18:39 both `/tmp/k72-omp-strings.txt` and `/tmp/k72-oc-strings.txt` were gone (`ls` showed
them at 17:51/17:55, my first two greps succeeded, the next batch hit `No such file or
directory`). I regenerated from the pinned binaries and checked identity against the prompt's
pins:

```
$ strings -n 4 /home/vgpnk/.local/bin/omp.real > /tmp/k72-omp-strings.txt
$ sha256sum /tmp/k72-omp-strings.txt
953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f     (prompt pin: 953b19df…)
$ strings -n 4 /home/vgpnk/.opencode/bin/opencode > /tmp/k72-oc-strings.txt
$ sha256sum /tmp/k72-oc-strings.txt
020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089     (prompt pin: 020fb253…)
$ sha256sum /home/vgpnk/.opencode/bin/opencode
ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7     (plan's v2.1.4 pin)
```

Both dumps are byte-identical to the shared inputs; other seats can keep using them. Whoever
cleaned `/tmp` should not delete these two paths while wave 1 runs.

## Patch (scratch only, ready for the L1)

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-72/w1/build/ExecOmpHalf/omp-path-only.patch`
(1,976 bytes, sha256 `56e51ed094a6ff701600b28dd46dabd6027df353e3117d50c2be27987a35e44d`) — the
three constants of F3, nothing else. `git apply` clean against `e61fd29` (it is the clone's own
`git diff`). It is **not sufficient** for C2: with it, `pins OK`/`surfaces pass p of 7` still
cannot reach `3/3`/`7/7` because the opencode default path is dead and the rules OC-1…OC-6
extract 0 classes from v2.1.4.

## Limits of this report (unobserved / not done)

- I did **not** re-pin `verifiers/baseline.json` (the 9 population DRIFTs) — that is C2's
  substrate re-pin, and doing it here would edit a committed file.
- I did **not** hand-read a session `.jsonl` catalogue block (transcripts carry seat
  conversations); the 206-entry/15-match numbers are the instrument's, and P1's template half
  is confirmed from the ELF directly.
- I did **not** run the lane gates, the C1/C3 counters, or `check_substrate_pins.py` — outside
  this seat.
- No tool was installed or upgraded this seat.

## Hand-off checks for the L1

`python3 -B verifiers/verify_harness_claims.py --omp-bin /home/vgpnk/.local/bin/omp.real --json`
(expect exit 1, `8/17` omp PASS) · `python3 -B verifiers/verify_surfaces.py --omp-binary
/home/vgpnk/.local/bin/omp.real --opencode-strings /tmp/k72-oc-strings.txt` (expect exit 1,
`5 of 7`) · the patched clone runs are reproducible from the patch alone.
