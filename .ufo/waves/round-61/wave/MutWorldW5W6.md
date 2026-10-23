# MutWorldW5W6 — ExecKeyForms wrong-key / invented-action rows, rebuilt end-to-end

Seat: `kotoba-r61-wave-MutWorldW5W6` (leaf). Date of measurements: 2026-10-23 UTC
(stamps below). Lane (read-only): `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at
`7827628a939b0333c89892dfcedc72e390ccfb60` (`master`; parent/base
`f3246d1493b60ea1c0d947a19c39f9e08e92f326`). Scratch (untrusted, never an evidence
source): `/fast/scratch/hyaku/kotoba-r61/MutWorldW5W6/`.

**Bottom line: REPRODUCED, no divergence.** The committed v2 counter
(`verifiers/check_scoped_rules.py`, sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`)
backs a row end-to-end — `scoped rule files backed on committed snapshots 4 of 4;
found on the live page 4 of 4`, exit 0 — with `patterns`@S103:238 as the Scope key, with
`claudeMdExcludes`@S103:339 as the Scope key, with an invented Action cell cited at
S103:209, and with the wrong key and invented action combined. This is exactly the
r60 `build/ExecKeyForms.md` record; v2 does **not** reject W5 or W6. The negative
control (same invented cell cited at the real action line S103:194) is rejected at
row level (`3 of 4`), which shows the acceptance turns on the author's citation line,
not on unconditional text matching. No claim in `build/ExecKeyForms.md` was falsified.

## What was attacked, and the expected detector

Mutants, all inside a scratch clone and each one SKILL.md table-cell edit only (the
`### Scoped rule files by client` first table; every other committed byte is the lane's):

| Mutant | Edit to the committed row | Expected from `build/ExecKeyForms.md` |
|---|---|---|
| W5-patterns | Claude Code Scope key `paths` (`src/api/**/*.ts`, S103:198) → `patterns` (S103:238) | backed end-to-end, 4 of 4 live, exit 0 |
| W5-mdExcludes | Claude Code Scope key → `claudeMdExcludes` (S103:339) | backed end-to-end, 4 of 4 live, exit 0 |
| W5-sessions | VS Code Scope key `applyTo` (S105:164) → `sessions` (S105:32) | W-wrong row: backed, 4 of 4 live, exit 0 |
| W6-invented | Claude Code Action → `Create the rule file in the project and add frontmatter so it loads only for the matching files.` cited S103:209 | `action_conjunct` passes (|W|=8, need 4, shared 6), row backed |
| W5W6-combined | `claudeMdExcludes`@339 **and** the invented Action @209 | backed end-to-end |
| NEG-real-line | invented Action cited at the real action line S103:194 | row rejected (under-determined citation control) |

Detector, run on every mutant: the committed v2 counter's own CLI, frozen invocation

```
python3 -B verifiers/check_scoped_rules.py --rev <scratch commit> --fetch
```

with the frozen predicate `exit 0 iff "found on the live page F of K" has F >= TARGET`,
`TARGET = 3` (counter line 249). Row-level `backed` and `found` are read from the same
output. A baseline failure on the unmutated clone would make the run inconclusive;
the baseline passed (below).

## Evidence hashes (read-only lane and scratch copy)

```
$ sha256sum verifiers/check_scoped_rules.py                                   # lane
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
$ sha256sum probe/counter_copy.py                                             # imported copy, chmod 444
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
$ sha256sum SKILL.md verifiers/check_scoped_rules.py                          # scratch clone at clone time
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

Committed snapshots used (bytes read from the scratch clone, which came from lane
`7827628`; sha256 and size measured 2026-10-23T19:12:51Z):

| Page | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-60/snapshots/S103.page` | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| `.ufo/waves/round-60/snapshots/S105.page` | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` |
| `.ufo/waves/round-60/snapshots/S106.page` | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `.ufo/waves/round-60/snapshots/S108.page` | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |

`S103.page` is 664 lines and its sha is the census byte sha in the r60 table; the
three other shas/sizes match the r60 table's census pages too.

## Measurement 1 — the counter's own functions on the committed snapshot bytes

The probe's method, re-run: import a read-only copy of the v2 counter (above), call its
`key_site`/`scope_conjunct`/`any_key_site`/`action_conjunct` directly on the committed
S103 snapshot. Command and output (scratch `probe/probe_import.py`; run 2026-10-23):

```
$ python3 -B probe/probe_import.py
sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  .../probe/counter_copy.py
sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  .../verifiers/check_scoped_rules.py
S103.page lines 664 sha256 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7

-- key_site / scope_conjunct (the counter's own functions) --
paths              L=198  line='paths:'
    key_site=True  scope_conjunct=[]  any_key_site=True
paths              L=231  line='paths:'
    key_site=True  scope_conjunct=[]  any_key_site=True
patterns           L=238  line='Each brace group multiplies the number of expanded patterns: `src/*.{ts,tsx}` expands to t'
    key_site=True  scope_conjunct=[]  any_key_site=True
claudeMdExcludes   L=339  line='  "claudeMdExcludes": ['
    key_site=True  scope_conjunct=[]  any_key_site=True
sessions           L=-    key_site=(not on page)
description        L=248  line='| Field | Required | Description |'
    key_site=False  scope_conjunct=["scope key 'description' is not in key form with a path pattern at line 248"]  any_key_site=False

-- action_conjunct over the invented ExecKeyForms cells --
cell: Create the rule file in the project and add frontmatter so it loads only for the matching files.
    |W|=8 need=4
    L=209 shared=6 ['file', 'files', 'loads', 'matching', 'project', 'rule']  action_conjunct=[]
    L=194 shared=3 ['files', 'frontmatter', 'matching']  action_conjunct=['action cell shares 3 of its 8 content word(s) with line 194 (need >= 4)']
cell: Keep one instruction file per topic and set the scope key to the glob pattern of the files it applies to.
    |W|=9 need=5
    L=66 shared=4 ['file', 'files', 'scope', 'topic']  action_conjunct=['action cell shares 4 of its 9 content word(s) with line 66 (need >= 5)']
```

Reproduces `build/ExecKeyForms.md` Part 1 (`patterns`@238 and `claudeMdExcludes`@339 both
pass A1; the census-named wrong keys such as `description`@248 fail) and Part 2's Claude
Code row (|W|=8, need 4, shared 6 at line 209 → PASSES; another invented cell fails).
Exit 0.

The executable snippet (the probe's method, verbatim shape):

```python
spec = importlib.util.spec_from_file_location("counter_copy", COPY)
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
lines = SNAP.read_text(errors="replace").splitlines()
assert c.key_site(lines, 238, "patterns")                      # True
assert c.scope_conjunct(lines, "patterns", 238) == []          # accepted
assert c.key_site(lines, 339, "claudeMdExcludes")              # True
assert c.scope_conjunct(lines, "claudeMdExcludes", 339) == []  # accepted
assert c.action_conjunct(lines, INVENTED, 209) == []           # accepted
assert c.action_conjunct(lines, INVENTED, 194) != []           # rejected
```

## Measurement 2 — the sweep over the four eligible committed snapshots

Every line, every token `[A-Za-z0-9_][A-Za-z0-9_-]*`, tested with the counter's own
`key_site` (`probe/probe_sweep.py`, 2026-10-23T19:11:31Z):

```
$ python3 -B probe/probe_sweep.py
Claude Code  S103.page  lines=664  sha256=82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
  passing (K, L): paths@198, paths@231, patterns@238, claudeMdExcludes@339
  non-scope-key:  patterns@238, claudeMdExcludes@339
VS Code      S105.page  lines=367  sha256=a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f
  passing (K, L): sessions@32, sessions@128, applyTo@164, sessions@221, sessions@228, Sync@287
  non-scope-key:  sessions@32, sessions@128, sessions@221, sessions@228, Sync@287
Copilot CLI  S106.page  lines=111  sha256=00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
  passing (K, L): applyTo@66, applyTo@74, applyTo@94
  non-scope-key:  -
Cursor       S108.page  lines=399  sha256=884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
  passing (K, L): globs@85, rules@146, order@307
  non-scope-key:  rules@146, order@307

totals: 16 passing (K, L) pairs, 9 on a key that is not the client's scope key
EXIT=0
```

Same totals and per-page counts as `build/ExecKeyForms.md` (16 pairs, 9 extras; Claude
Code 2, VS Code 5, Copilot CLI 0, Cursor 2). Only the within-page print order differs
(line order instead of the build's key order). No divergence.

## Measurement 3 — end-to-end worlds on real sandbox commits

Method (scratch clone `lane`, git only; no lane write): reset to `7827628`, edit the one
row in `SKILL.md`, commit, run the committed counter with `--fetch`. Full timestamped
receipt:

```
Fri 23 Oct 2026 07:11:09 PM UTC
cmd: python3 -B probe/build_variants.py
=== BASE  scratch 7827628a939b0333c89892dfcedc72e390ccfb60  skill 2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909 ===
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7827628a939b0333c89892dfcedc72e390ccfb60
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== W5-patterns  scratch 1c76d3d19b30a3220bda75d8f5f2f8c5fb698e2c  skill b3e9de9c3255f0991efb2876466f067aaf1d5ea7a5af64eae576f2ed46bbc4fe ===
  row: | Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `patterns` (S103 :238) | Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194) |
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 1c76d3d19b30a3220bda75d8f5f2f8c5fb698e2c
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== W5-mdExcludes  scratch 241f5c085ab124142aa28f1f3705f4995117c225  skill 34035091244055cd9e0bb6f545adc109a768020ede24aa255dd837eae09f91e6 ===
  row: | Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `claudeMdExcludes` (S103 :339) | Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194) |
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 241f5c085ab124142aa28f1f3705f4995117c225
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== W5-sessions  scratch 64b698d1305ef420278b19442af048bfc9c5d013  skill 22abbeb53a6f5e0623694e7781dc66c856143f82b25cfeeb827385003f0e2625 ===
  row: | VS Code | `.github/instructions/**/*.instructions.md` (Local-harness targeted instructions, S105 :32) | `sessions` (S105 :32) | Use multiple instruction files per topic and apply them selectively (S105 :329) |
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 64b698d1305ef420278b19442af048bfc9c5d013
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== W6-invented  scratch 723dbb13a27fae44b385a237bc867e244ef4e688  skill 1c9ebe7aa8c4fee34f4c321560f89ac6ef02f338dcecb8cb5df44102d5d4c4c2 ===
  row: | Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209) |
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 723dbb13a27fae44b385a237bc867e244ef4e688
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== W5W6-combined  scratch dd3701a3dbee61b8842753535ce91501574c5c1e  skill 363673811139dbd4d4297316d8755c85ce3a3410347402e6ea8e3b2f3ac61c16 ===
  row: | Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `claudeMdExcludes` (S103 :339) | Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209) |
  exit=0
  scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev dd3701a3dbee61b8842753535ce91501574c5c1e
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== NEG-real-line  scratch a75aa72e9e99695315249629acea9116ee846953  skill 4325965eb5035d15556afb522dcb04b11406f8391e5f5c5858e92e68f33ac22f ===
  row: | Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :194) |
  exit=0
  scoped rule files backed on committed snapshots 3 of 4; found on the live page 3 of 4
  counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a75aa72e9e99695315249629acea9116ee846953
  reject Claude Code: entry row S103: snapshot .ufo/waves/round-60/snapshots/S103.page: action cell shares 3 of its 8 content word(s) with line 194 (need >= 4)
  reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

SCRIPT_EXIT=0
Fri 23 Oct 2026 07:11:13 PM UTC
```

Verdicts:

| Mutant | Row-level | CLI | v2 killed it? |
|---|---|---|---|
| W5-patterns | backed 4/4, live 4/4 | exit 0 | **survived** (as recorded) |
| W5-mdExcludes | backed 4/4, live 4/4 | exit 0 | **survived** (as recorded) |
| W5-sessions | backed 4/4, live 4/4 | exit 0 | **survived** (as recorded) |
| W6-invented | backed 4/4, live 4/4 | exit 0 | **survived** (as recorded) |
| W5W6-combined | backed 4/4, live 4/4 | exit 0 | **survived** (as recorded) |
| NEG-real-line | backed 3/4, live 3/4; Claude Code rejected | exit 0 (F=3 >= TARGET) | row rejected, predicate still 0 |

The negative control matters twice: (i) it shows the Action conjunct is not a rubber
stamp — the same invented sentence fails at the real action line; (ii) even with an
eligible row rejected, the v2 CLI exits 0 because `TARGET = 3` and F = 3. A mutant that
only knocks out one eligible row cannot fail the v2 predicate. This is the frozen v2
design, not a counter defect against the build record; the plan's v3 arms A1/A2 are the
instruments that must reject W5/W6 (C1 v3 arm spec: A1 rejects `patterns`-class keys,
A2 rejects invented actions), and the C1 v3 predicate requires 4 of 4 eligible rows.

The exact text replacement used (applied only inside the scratch clone's
`### Scoped rule files by client` first table; `set_row` in `probe/build_variants.py`):

```python
REAL_SCOPE = " `paths` (e.g. `src/api/**/*.ts`, S103 :198) "
INVENTED   = " Create the rule file in the project and add frontmatter so it loads only for the matching files. "
# W5-patterns:    parts[3] = " `patterns` (S103 :238) "
# W5-mdExcludes:  parts[3] = " `claudeMdExcludes` (S103 :339) "
# W5-sessions:    VS Code parts[3] = " `sessions` (S105 :32) "
# W6-invented:    parts[4] = INVENTED + "(S103 :209) "
# NEG-real-line:  parts[4] = INVENTED + "(S103 :194) "
# line.split("|"); only the target client's row is touched; other rows/bytes unchanged.
```

## Measurement 4 — the live bytes the counter fetched for S103

The counter's `--fetch` verdict is on live bytes, not the snapshot. Documented with the
counter's own frozen curl invocation (`curl_argv`/`run_curl`) on the S103 URL
(`https://code.claude.com/docs/en/memory.md`), 2026-10-23T19:11:55Z:

```
$ python3 -B probe/probe_live.py
status=200 effective=https://code.claude.com/docs/en/memory.md bytes=55354 sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
quote_why=[]
any_key_site(paths             ) = True
any_key_site(patterns          ) = True
any_key_site(claudeMdExcludes  ) = True
EXIT=0
Fri 23 Oct 2026 07:11:56 PM UTC
```

So the live page holds the entry quote (the row's `.claude/rules/` quote) and a key-form
site for each of `paths`, `patterns`, `claudeMdExcludes`; the live leg of every positive
variant is real. The live page has drifted since r60 (now 55354 bytes vs the committed
census snapshot's 54043); `--fetch` checks quote + any K site on live bytes and passes,
which is v2's documented live rule. This drift does not falsify the r60 record (measured
at 12:16Z on the then-live/census bytes) and does not change any verdict here.

## Self-test of the copied v2 counter

```
Fri 23 Oct 2026 07:11:31 PM UTC
cmd: python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
EXIT=0
```

Matches `build/ExecKeyForms.md` (318 assertions). The imported copy is the same bytes as
the lane counter (sha above), so the direct-function measurements are the frozen v2
code's measurements.

## Divergence finding: none

Every claim the task named reproduces against the committed bytes:

1. v2 backs a row end-to-end with `patterns` as the Scope key — 4 of 4 live, exit 0.
2. v2 backs a row end-to-end with `claudeMdExcludes` as the Scope key — 4 of 4 live, exit 0.
3. v2 backs a row end-to-end with an invented Action cell — 4 of 4 live, exit 0.
4. The recorded W-wrong `sessions` mutant — 4 of 4 live, exit 0.
5. Counter-function values match the r60 table (`|W|`, `need`, shared, line; sweep totals).

Two documentary notes, not divergences:

- `build/ExecKeyForms.md` Part 3's table shows `--fetch` only for the `sessions` wrong
  key; the Claude Code `patterns`/`claudeMdExcludes` extras and the invented-action cell
  are backed end-to-end in that report's prose and non-fetch rows. This probe supplies
  the missing `--fetch` receipts for exactly those rows; the prose's claim is true.
- The live Claude Code page differs from the committed snapshot by +1311 bytes today;
  the row still passes `--fetch` because the quote and a key-form site remain. If the
  page removes `patterns`/`claudeMdExcludes` key forms, a *wrong-key* row would stop
  being "found" live while still being "backed" on the snapshot — a version of the same
  hole, not a new one.

No contract change is implied: a surviving mutant is a coverage finding. For C1 v3, W5
and W6 are confirmed live fixtures for arms A1/A2; the committed v2 counter is confirmed
to accept them (exit 0, 4 of 4 live), which is the pre-fix state the plan records.

## What was not measured

- No run of the counter against the lane revision as a data measurement; the lane run
  above is the pristine baseline only (`7827628`), and the mutants live in scratch
  commits (hashes above), never in the lane.
- No v3 draft exists in my scope; this probe only characterizes v2's acceptance of
  W5/W6. The v3 arms were not exercised.
- No sweep of the three non-eligible clients' pages (out of scope; r60 appendix).
- No mutation of the counter source itself; the counter copy is byte-identical to lane
  bytes (`ca2585a4`) and was imported read-only (`chmod 444`).

## Restoration evidence

Scratch copy (declared untrusted/disposable; restored anyway), 2026-10-23T19:12:11Z:

```
$ git -C /fast/scratch/hyaku/kotoba-r61/MutWorldW5W6/lane rev-parse HEAD
7827628a939b0333c89892dfcedc72e390ccfb60
$ sha256sum SKILL.md verifiers/check_scoped_rules.py
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

Lane untouched (only read commands; `git rev-parse`, `git cat-file`, `git show`,
`sha256sum`, `wc`, `sed -n` reads), 2026-10-23T19:11:37Z:

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD master
7827628a939b0333c89892dfcedc72e390ccfb60
7827628a939b0333c89892dfcedc72e390ccfb60
$ sha256sum SKILL.md verifiers/check_scoped_rules.py .ufo/waves/round-60/snapshots/S103.page .ufo/waves/round-60/snapshots/S105.page
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  .ufo/waves/round-60/snapshots/S103.page
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  .ufo/waves/round-60/snapshots/S105.page
```

SKILL.md's lane working-tree sha equals the scratch clone's sha at clone time, and the
counter/snapshot shas equal the pre-probe values; the only lane file written by me is
this report. Probe scripts and raw outputs remain under
`/fast/scratch/hyaku/kotoba-r61/MutWorldW5W6/probe/` (scratch, not evidence).

Installs: no installs (python3/curl/git already present; pacman untouched).

Blockers: none.

Attacked: the committed v2 counter's W5/W6 acceptance — rebuilt `patterns`@S103:238,
`claudeMdExcludes`@S103:339, `sessions`@S105:32 and an invented Action cell in scratch
commits and confirmed exit 0 with 4 of 4 backed and 4 of 4 live, matching
`build/ExecKeyForms.md`; no divergence filed.
