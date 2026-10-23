Result: DONE — CtlRescoreV2: CtlDoNothing S 0 of 0 / F 0 of 0 / exit 1; CtlJunk S 0 of 7 / F 0 of 7 / exit 1; CtlAllFalse S 7 of 7 / F 0 of 7 / exit 1; CtlNoReader S 0 of 4 / F 0 of 4 / exit 1; CtlFabSnapshot S 1 of 4 / F 0 of 4 / exit 1; CtlLabelShortcut S 0 of 2 / F 0 of 2 / exit 1; CtlWrongKey and CtlInventedAction have no v1 world (seats cancelled); predicate NOT MET

# CtlRescoreV2 — re-score of every v1 control world under frozen counter v2

**Seat:** `KotobaR60.CtlRescoreV2` (L1: `agent://KotobaR60`).
**Sandbox clone:** `/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2` (all git writes, all counter runs, all receipt files).
**Receipt commit:** `sandbox db75afb07519a185f68d77a6c3a862d7f8770e3f (/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2)`, branch `receipt/ctl-rescore-v2`, parent `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` (the receipt commit and its parent commit `sandbox e5e8a455ca840c1d06a155c59d0d06ad44af1a1f (/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2)` carry the world re-score artefacts; the second adds the independently re-derived exit codes).
**Freeze revision measured:** `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` (the v2 freeze, "round-60: erratum E1 before data — counter v2 (re-open of held rows; sha ca2585a4)").
**Predicate outcome:** NOT MET on every world. The maximum F over all worlds is 1; `TARGET = 3`; every `--fetch` run exits 1.

## 1. The counter that was run

Extracted from the committed freeze, never from the task text:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git --no-optional-locks show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py > /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py
$ sha256sum /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py
```

The sha256 equals the sha256 named in the task context
(`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`) and the sha256 the counter
prints about itself in every run (`counter sha256 ca2585a4…; rev <rev>`), read from
`__file__` by the counter's own `self_sha()`. The clone's own copy is byte-identical:

```
$ cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2 && sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

`TARGET` was read from the committed file, not from any text: `TARGET = 3` at
`verifiers/check_scoped_rules.py:249` of `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`
(`git show b1cd64bb…:verifiers/check_scoped_rules.py | grep -n '^TARGET'` → `249:TARGET = 3`).
The counter's self-test passes on this exact file:

```
$ cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2 && timeout 300 python3 -B v2.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
```

Exit 0. The counter was not modified, patched or re-generated; it was run as extracted.

## 2. Which worlds were re-scored, and how they were obtained

The v1 control receipts (`.ufo/waves/round-60/controls/*.md`, plus
`.ufo/waves/round-60/controls/SUMMARY.md`) name the world revision(s) of each control. Every named
world revision was re-scored under the v2 counter file. The v1 world commits live in the v1 seats'
sandboxes under `/fast/scratch/hyaku/kotoba-r60/<Seat>`; each seat's sandbox was cloned **read-only**
into this seat's directory (`worlds/<Seat>`) and the named revisions were fetched into this seat's
own clone. No v1 seat's clone was written to.

Object identity was checked before scoring — the same world commit has the same tree id in the
v1 seat's sandbox, in this seat's clone and in the read-only clone:

```
$ git -C <clone> rev-parse <world>^{tree}   (three clones per world)
CtlAllFalse        101c2140 mine=a15846da seat=a15846da clone=a15846da
CtlDoNothing       f4dcfd9 mine=4f5c3555 seat=4f5c3555 clone=4f5c3555
CtlFabSnapshot     8933ce9 mine=fc716ed2 seat=fc716ed2 clone=fc716ed2
CtlJunk            de808c7 mine=5e42d8fc seat=5e42d8fc clone=5e42d8fc
CtlLabelShortcut   415c767 mine=468f4336 seat=468f4336 clone=468f4336
CtlNoReader        eabe93f mine=008a97cb seat=008a97cb clone=008a97cb
```

(`git rev-parse <rev>^{tree}`, each exit 0.) The `CtlNoReader` probe commit `43513ee` was reached
through a git **alternates** entry pointing at the v1 seat's probe clone's object store, so the
probe's bytes were read without writing into that clone.

Two things were then done with every world, and both are reported below:

1. **Direct re-score.** The v1 world revision was scored as committed by the v1 seat, using the v2
   counter file. This is the primary measurement.
2. **Replay on the v2 freeze.** The same world was cherry-picked onto `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`
   in this seat's clone (branches `replay/ctl-*`), so the world is also measurable as a commit whose
   parent is the v2 freeze. The counter-relevant paths (`SKILL.md`, `corpus/SOURCES.md`,
   `corpus/knowledge/scoped-rules-round60.md`, `corpus/lessons/round-60.md`,
   `.ufo/waves/round-60/snapshots/`) are byte-identical between the v1 world and its replay
   (`git rev-parse <rev>:<path>` compared path by path; every path SAME), and the two runs produce
   byte-identical output (see §5).

## 3. The one table

World rev = the revision the v1 receipt names. `S` = rows backed on committed snapshots,
`F` = rows found on the live page, both as the counter prints them. Exit = the `--fetch` run's
exit code. "predicate under v2" = `C1 predicate: --fetch exit 0 (F>=TARGET)` with `TARGET = 3`.

| control | world rev | S | F | exit | predicate under v2 |
|---|---|---|---|---|---|
| CtlDoNothing (v1 freeze rev, as the v1 receipt names it) | `49c3e87d4fb5677783c55f8225c9e4f892273879` | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlDoNothing (counter's base rev, as the v1 receipt names it) | `31092dc6f875370bddd6eb1e4da4ca0d210c56af` | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlDoNothing (empty-section world) | `f4dcfd99c5e3eb43c28113958f98788a003a5b72` | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlJunk (measured world) | `de808c7bf0ce337d5e477b0c80ab3e3eab332540` | 0 of 7 | 0 of 7 | 1 | NOT MET |
| CtlJunk (restored world) | `127c6043bb6783c7e735c4cc825ac4e87f5bb6a2` | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlAllFalse (fabricated-source world) | `101c2140e7b969c20198269c72e77e424b5db2a5` | 7 of 7 | 0 of 7 | 1 | NOT MET |
| CtlNoReader (measured world) | `eabe93f6c6f02caa66f845d50f34b2e8fbe33723` | 0 of 4 | 0 of 4 | 1 | NOT MET |
| CtlNoReader (probe: world + census bytes as snapshots) | `43513eeaa274098f8d0b98941016b4418f854d20` | 1 of 4 | 1 of 4 | 1 | NOT MET |
| CtlFabSnapshot (genuine pristine baseline) | `a2893fa26d08cda5a866875af121046573b699fa` | 1 of 4 | 1 of 4 | 1 | NOT MET |
| CtlFabSnapshot (fabricated-quote world) | `8933ce9e95372cb8daedd6145e4b930fe472d239` | 1 of 4 | 0 of 4 | 1 | NOT MET |
| CtlFabSnapshot (restored world) | `b713e5b1017d784f558e5b8c674bceaca8f1cd1b` | 1 of 4 | 1 of 4 | 1 | NOT MET |
| CtlLabelShortcut (label-only world) | `415c7672e4fb27c88399f20c3830f0d7dc2a51be` | 0 of 2 | 0 of 2 | 1 | NOT MET |
| CtlLabelShortcut (restored world) | `18afea6719d9d5ad46fc3a07f567e8a1dfa5c642` | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlWrongKey | **none** | — | — | — | **no world to re-score** (seat cancelled; see §6) |
| CtlInventedAction | **none** | — | — | — | **no world to re-score** (seat cancelled; see §6) |

Two extra rows, not v1 worlds, recorded because they bracket the re-score:

| reference | world rev | S | F | exit | predicate under v2 |
|---|---|---|---|---|---|
| the v2 freeze itself (the "do nothing" state under v2) | `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` | 0 of 0 | 0 of 0 | 1 | NOT MET |

(The v1 control summary's own table is the reference this table is compared against:
`.ufo/waves/round-60/controls/SUMMARY.md`.)

## 4. Exact commands, stdout and exit codes

Every run was executed from this seat's sandbox, each capped with `timeout 900`, none wrote to the
lane. The counter resolves its lane by walking up from its own `__file__` (`lane_dir()`,
`verifiers/check_scoped_rules.py:351`), so a copy of the v2 file placed at
`/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py` resolves the lane to this seat's clone; the
run's cwd was the read-only clone of the v1 seat's sandbox. The lane that answered was confirmed
directly:

```
$ cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/worlds/CtlJunk && timeout 60 python3 -B /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py --rev 0000000000000000000000000000000000000000
could-not-evaluate: revision '0000000000000000000000000000000000000000' is not a commit in /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2
```

The command shape, per world (the `rev` is the world revision; the two forms differ only by
`--fetch`):

```
cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/worlds/<Seat> && timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py --rev <world> --fetch
cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/worlds/<Seat> && timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py --rev <world>
```

Full stdout of every `--fetch` run is quoted below. Every `.stderr` file in the receipts directory is
0 bytes — all 63 of them, verified with `find <receipts> -name '*.stderr' -size +0 | wc -l` → 0
non-empty files.

### CtlDoNothing — empty-section world `f4dcfd99c5e3eb43c28113958f98788a003a5b72` (exit 1)

```
scoped rule files backed on committed snapshots 0 of 0; found on the live page 0 of 0
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev f4dcfd99c5e3eb43c28113958f98788a003a5b72
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Without `--fetch`: `scoped rule files backed on committed snapshots 0 of 0; live not run`, exit 1.
Same for the v1 freeze rev `49c3e87d…` and the base rev `31092dc6…` (both `0 of 0; … 0 of 0`, exit 1).

### CtlJunk — measured world `de808c7bf0ce337d5e477b0c80ab3e3eab332540` (exit 1)

```
scoped rule files backed on committed snapshots 0 of 7; found on the live page 0 of 7
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev de808c7bf0ce337d5e477b0c80ab3e3eab332540
reject Claude Code: entry row S103: quote holds no rule/instruction word outside the token; S103 URL 'https://jeyzptol.invalid/yangkgxc/qomcfcpn' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S103.page: scope key 'dlppmxoe' is not in key form with a path pattern at line 3; snapshot .ufo/waves/round-60/snapshots/S103.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Codex: entry row S104: quote holds no rule/instruction word outside the token; S104 URL 'https://rrsjvcbe.invalid/ejwxwspz/efcxmzqq' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S104.page: scope key 'scxclyrg' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S104.page: action cell shares 0 of its 4 content word(s) with line 10 (need >= 2)
reject VS Code: entry row S105: quote holds no rule/instruction word outside the token; S105 URL 'https://dhafooni.invalid/aqcfxwtd/dpljmlab' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S105.page: scope key 'vyenlamf' is not in key form with a path pattern at line 6; snapshot .ufo/waves/round-60/snapshots/S105.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Copilot CLI: entry row S106: quote holds no rule/instruction word outside the token; S106 URL 'https://lhodyslf.invalid/rujbmefo/wlrubcar' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S106.page: scope key 'himzgfks' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S106.page: action cell shares 0 of its 4 content word(s) with line 7 (need >= 2)
reject Gemini CLI: entry row S107: quote holds no rule/instruction word outside the token; S107 URL 'https://fuoppwwp.invalid/agzmudxh/hsecazvg' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S107.page: scope key 'wrzupirq' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S107.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Cursor: entry row S108: quote holds no rule/instruction word outside the token; S108 URL 'https://sdqnhhio.invalid/obzrwqga/kasprnac' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S108.page: scope key 'xvirlugy' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S108.page: action cell shares 0 of its 4 content word(s) with line 5 (need >= 2)
reject opencode: entry row S109: quote holds no rule/instruction word outside the token; S109 URL 'https://lpngyjvw.invalid/dxjofmom/fmyozlsf' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S109.page: scope key 'bekqosuc' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S109.page: action cell shares 0 of its 4 content word(s) with line 12 (need >= 2)
```

Without `--fetch`: `0 of 7; live not run`, exit 1. The restored world `127c6043…` gives `0 of 0; … 0 of 0`, exit 1.

### CtlAllFalse — fabricated-source world `101c2140e7b969c20198269c72e77e424b5db2a5` (exit 1)

```
scoped rule files backed on committed snapshots 7 of 7; found on the live page 0 of 7
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 101c2140e7b969c20198269c72e77e424b5db2a5
reject Claude Code: live fetch failed: HTTP 404 at https://code.claude.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Codex: live fetch failed: HTTP 404 at https://developers.openai.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject VS Code: live fetch failed: HTTP 404 at https://code.visualstudio.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Copilot CLI: live fetch failed: HTTP 404 at https://docs.github.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Gemini CLI: live fetch failed: HTTP 404 at https://geminicli.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Cursor: live fetch failed: HTTP 404 at https://cursor.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject opencode: live fetch failed: HTTP 404 at https://opencode.ai/docs/ctl-all-false-round60-49c3e87d4fb5.md
```

Without `--fetch`: `7 of 7; live not run`, exit 1. The offline S = 7 of 7 is unchanged from v1; the
live conjunct still rejects every row.

### CtlNoReader — measured world `eabe93f6c6f02caa66f845d50f34b2e8fbe33723` (exit 1)

```
scoped rule files backed on committed snapshots 0 of 4; found on the live page 0 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev eabe93f6c6f02caa66f845d50f34b2e8fbe33723
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S103.page is missing at the revision
reject Codex: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
reject VS Code: entry row S104: snapshot .ufo/waves/round-60/snapshots/S104.page is missing at the revision
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S105.page is missing at the revision
reject Gemini CLI: SKILL.md rule token 'GEMINI.md' is not well-formed; no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S106.page is missing at the revision
reject opencode: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
```

Without `--fetch`: `0 of 4; live not run`, exit 1.

### CtlNoReader — probe `43513eeaa274098f8d0b98941016b4418f854d20` (exit 1)

```
scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 43513eeaa274098f8d0b98941016b4418f854d20
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rule token 'GEMINI.md' is not well-formed; no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
```

Without `--fetch`: `1 of 4; live not run`, exit 1. The probe's VS Code row backs and is found live;
the three base-URL rows (S103 Claude Code, S105 Copilot CLI, S106 Cursor) still fail under v2 because
no `re-opens S### —` cell names a base row for their URL.

### CtlFabSnapshot — genuine pristine baseline `a2893fa26d08cda5a866875af121046573b699fa` (exit 1)

```
scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a2893fa26d08cda5a866875af121046573b699fa
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Without `--fetch`: `1 of 4; live not run`, exit 1. The restored world `b713e5b1…` gives the same
`1 of 4; found on the live page 1 of 4`, exit 1.

### CtlFabSnapshot — fabricated-quote world `8933ce9e95372cb8daedd6145e4b930fe472d239` (exit 1)

```
scoped rule files backed on committed snapshots 1 of 4; found on the live page 0 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 8933ce9e95372cb8daedd6145e4b930fe472d239
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: live page: the quote is not on the page
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Without `--fetch`: `1 of 4; live not run`, exit 1. The fabricated quote is rejected on the live page.

### CtlLabelShortcut — label-only world `415c7672e4fb27c88399f20c3830f0d7dc2a51be` (exit 1)

```
scoped rule files backed on committed snapshots 0 of 2; found on the live page 0 of 2
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 415c7672e4fb27c88399f20c3830f0d7dc2a51be
reject Claude Code: entry row S103: quote does not hold the rule token '.claude/settings.json' (case-sensitive); S103 URL 'https://code.claude.com/docs/en/hooks.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S103.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S103.page: scope key 'paths' is not in key form with a path pattern at line 5
reject Codex: SKILL.md rule token '~/.codex/hooks.json' is not well-formed; entry row S104: quote does not hold the rule token '~/.codex/hooks.json' (case-sensitive); S104 URL 'https://learn.chatgpt.com/docs/hooks.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S104.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S104.page: scope key 'paths' is not in key form with a path pattern at line 5; snapshot .ufo/waves/round-60/snapshots/S104.page: action cell shares 3 of its 10 content word(s) with line 19 (need >= 5)
reject VS Code: SKILL.md rule token '.github/hooks/*.json' is not well-formed; entry row S105: quote does not hold the rule token '.github/hooks/*.json' (case-sensitive); S105 URL 'https://code.visualstudio.com/docs/agent-customization/hooks.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S105.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S105.page: scope key 'applyTo' is not in key form with a path pattern at line 4; snapshot .ufo/waves/round-60/snapshots/S105.page: action cell shares 2 of its 7 content word(s) with line 4 (need >= 4)
reject Copilot CLI: SKILL.md rule token '~/.copilot/hooks/*.json' is not well-formed; entry row S106: quote does not hold the rule token '~/.copilot/hooks/*.json' (case-sensitive); S106 URL 'https://docs.github.com/en/copilot/concepts/customizations/hooks.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S106.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S106.page: scope key 'applyTo' is not in key form with a path pattern at line 4
reject Gemini CLI: SKILL.md rule token '.gemini/settings.json' is not well-formed; entry row S107: quote does not hold the rule token '.gemini/settings.json' (case-sensitive); S107 URL 'https://geminicli.com/docs/hooks/best-practices.md' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S107.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S107.page: scope key 'globs' is not in key form with a path pattern at line 4
reject Cursor: SKILL.md rule token '.cursor/hooks.json' is not well-formed; entry row S108: quote does not hold the rule token '.cursor/hooks.json' (case-sensitive); S108 URL 'https://cursor.com/docs/hooks' is already a base SOURCES URL; re-open names no base row with this URL; snapshot .ufo/waves/round-60/snapshots/S108.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S108.page: scope key 'globs' is not in key form with a path pattern at line 4; snapshot .ufo/waves/round-60/snapshots/S108.page: action cell shares 4 of its 9 content word(s) with line 649 (need >= 5)
reject opencode: SKILL.md rule token '.opencode/agents' is not well-formed; entry row S108: quote does not hold the rule token '.opencode/agents' (case-sensitive); S108 URL 'https://cursor.com/docs/hooks' is already a base SOURCES URL; re-open names no base row with this URL; S108 URL 'https://cursor.com/docs/hooks' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S108.page: the quote is not on the page; snapshot .ufo/waves/round-60/snapshots/S108.page: scope key 'paths' is not in key form with a path pattern at line 5; SKILL.md action cell carries no `S### :L` citation
```

Without `--fetch`: `0 of 2; live not run`, exit 1. The restored world `18afea67…` gives `0 of 0; … 0 of 0`, exit 1.

### The v2 freeze revision itself `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` (exit 1)

```
scoped rule files backed on committed snapshots 0 of 0; found on the live page 0 of 0
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev b1cd64bb45eee744c4ec93be8631f1eddb28fddd
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
… (one such line per client)
```

## 5. The replay on the v2 freeze gives the same verdicts

Each v1 world was cherry-picked onto the v2 freeze in this seat's clone, and the replay commits were
scored with the same frozen v2 file (branches `replay/ctl-*`):

| world | v1 world rev | replay commit (this seat's sandbox) | replay S | replay F | replay exit |
|---|---|---|---|---|---|
| CtlDoNothing | `f4dcfd99c5e3eb43c28113958f98788a003a5b72` | `4d0463dea209717b1d7f635f55ac6fd7fb4cb416` | 0 of 0 | 0 of 0 | 1 |
| CtlJunk (world) | `de808c7bf0ce337d5e477b0c80ab3e3eab332540` | `147fa75997bcee99ad13134728d0a9de31029eef` | 0 of 7 | 0 of 7 | 1 |
| CtlJunk (restored) | `127c6043bb6783c7e735c4cc825ac4e87f5bb6a2` | `46e6276a76a1951af05eb6c8fdd9fce7114bdc91` | 0 of 0 | 0 of 0 | 1 |
| CtlAllFalse | `101c2140e7b969c20198269c72e77e424b5db2a5` | `72845f499ef551dd80e670798ff59cb932fe7c05` | 7 of 7 | 0 of 7 | 1 |
| CtlNoReader (world) | `eabe93f6c6f02caa66f845d50f34b2e8fbe33723` | `4655825c6548d6a20dac7d8ba511163c83e3d326` | 0 of 4 | 0 of 4 | 1 |
| CtlNoReader (probe) | `43513eeaa274098f8d0b98941016b4418f854d20` | `4a88731e0d6743523bdd93c403f1d4073f6544f2` | 1 of 4 | 1 of 4 | 1 |
| CtlFabSnapshot (pristine) | `a2893fa26d08cda5a866875af121046573b699fa` | `2f93a2aacf372f7b4ce3e4e56c46fbe616787e5b` | 1 of 4 | 1 of 4 | 1 |
| CtlFabSnapshot (fabricated) | `8933ce9e95372cb8daedd6145e4b930fe472d239` | `b07a0fcb78d7732a424f9cc4d2c0c1eef2fab232` | 1 of 4 | 0 of 4 | 1 |
| CtlFabSnapshot (restored) | `b713e5b1017d784f558e5b8c674bceaca8f1cd1b` | `1db6002515752b1d47c32204263549f8213b34ea` | 1 of 4 | 1 of 4 | 1 |
| CtlLabelShortcut (world) | `415c7672e4fb27c88399f20c3830f0d7dc2a51be` | `0ce635b439ddfc6762661bc6bc97ab2c84c7cef0` | 0 of 2 | 0 of 2 | 1 |
| CtlLabelShortcut (restored) | `18afea6719d9d5ad46fc3a07f567e8a1dfa5c642` | `0bdc596a5cc5cff73191a13ef74a5b86b40aef1a` | 0 of 0 | 0 of 0 | 1 |

The stdout of each replay `--fetch` run is **byte-identical** to the corresponding direct run once the
`rev` field is masked (verified with `sed 's/rev [0-9a-f]\{40\}/rev <REV>/' | sha256sum`; all eleven
pairs hash the same), and every stderr file is 0 bytes:

```
donothing-world        fetch-body orig=440398d458d0cfe1 replay=440398d458d0cfe1 IDENTICAL | stderr orig=0B replay=0B
junk-world             fetch-body orig=54e56f6b684485f4 replay=54e56f6b684485f4 IDENTICAL | stderr orig=0B replay=0B
junk-restored          fetch-body orig=440398d458d0cfe1 replay=440398d458d0cfe1 IDENTICAL | stderr orig=0B replay=0B
allfalse-world         fetch-body orig=103f156fed24f30a replay=103f156fed24f30a IDENTICAL | stderr orig=0B replay=0B
noreader-world         fetch-body orig=d162f727c36976b5 replay=d162f727c36976b5 IDENTICAL | stderr orig=0B replay=0B
noreader-probe         fetch-body orig=200b9b27f775e406 replay=200b9b27f775e406 IDENTICAL | stderr orig=0B replay=0B
fabsnap-pristine       fetch-body orig=57c58b7fe148b895 replay=57c58b7fe148b895 IDENTICAL | stderr orig=0B replay=0B
fabsnap-fabricated     fetch-body orig=6f9380bb43275f19 replay=6f9380bb43275f19 IDENTICAL | stderr orig=0B replay=0B
fabsnap-restored       fetch-body orig=57c58b7fe148b895 replay=57c58b7fe148b895 IDENTICAL | stderr orig=0B replay=0B
labelshort-world       fetch-body orig=ecbb14e53c57e344 replay=ecbb14e53c57e344 IDENTICAL | stderr orig=0B replay=0B
labelshort-restored    fetch-body orig=440398d458d0cfe1 replay=440398d458d0cfe1 IDENTICAL | stderr orig=0B replay=0B
```

**Independent-lane cross-check.** To show the verdicts do not depend on which clone answered, the
v2 counter file was also placed *inside* each v1 seat's read-only clone
(`worlds/<Seat>/verifiers/check_scoped_rules_v2.py`, sha256 re-verified
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`), so `lane_dir()` resolved to
that clone instead of this seat's. Six worlds were re-run that way; every S, F and exit matches §3
(`indep-allfalse` 7/0 exit 1, `indep-fabsnap` 1/0 exit 1, `indep-noreader` 0/0 exit 1,
`indep-junk` 0/0 exit 1, `indep-donothing` 0/0 exit 1, `indep-labelshort` 0/0 exit 1).

## 6. What changes from v1 to v2, and what does not

The v1 counter (`sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440`, extracted
from `49c3e87d…` into `v1.py`) was run on the same worlds as a delta reference. **Every S, F and exit
is unchanged between v1 and v2.** The only difference is one extra reason string on rows whose URL is
a base SOURCES URL: v2 appends `re-open names no base row with this URL` after
`is already a base SOURCES URL`, because the v2 base-URL conjunct now asks *why* a base-keyed row is
not a valid re-open. Examples (full diffs in the receipts):

```
noreader-probe, Claude Code
  v1: reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
  v2: reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
```

```
labelshort-world, Cursor
  v1: … S108 URL 'https://cursor.com/docs/hooks' is already a base SOURCES URL; snapshot …
  v2: … S108 URL 'https://cursor.com/docs/hooks' is already a base SOURCES URL; re-open names no base row with this URL; snapshot …
```

`CtlAllFalse`, `CtlJunk` and `CtlDoNothing` produce **no** diff at all between v1 and v2 (their rows
are not base-keyed URLs).

**Reading.** The v1 controls were built before erratum E1 and none of them carries a
`re-opens S### —` teaches cell, so v2's relaxed base-URL conjunct does not rescue any of them: a
base-keyed URL still needs a re-open naming its base row, and no v1 world has one. The one row that
does back under v2 (VS Code, whose census URL is not a base key) backs and is found live in the
`CtlNoReader` probe and in the `CtlFabSnapshot` pristine and restored worlds — the same as under v1.
Maximum F over every world is 1, against `TARGET = 3`, so the predicate is NOT MET everywhere and no
control forces a redesign.

This also confirms what `CtlNoReader`'s own v1 receipt recorded "for information only"
(`.ufo/waves/round-60/controls/CtlNoReader.md:180-186`): the same world re-scored with the v2 file
gives S 0 of 4, F 0 of 4, exit 1, with the extra `re-open names no base row with this URL` reason,
and the probe gives S 1 of 4. This seat's measurement reproduces that independently.

## 7. The two controls that have no world

`CtlWrongKey` and `CtlInventedAction` have **no v1 world to re-score**. Their v1 seats were
cancelled at the settle deadline before committing a world, and the v1 control summary records this
(`.ufo/waves/round-60/controls/SUMMARY.md`, table rows `CtlWrongKey` and `CtlInventedAction`:
"**cancelled** at the settle deadline (dispatched about 10:47Z, cancelled 12:04Z), no receipt, no
world committed in its sandbox").

Verified directly in their sandboxes at 12:16Z and 12:20Z on 2026-10-23:

```
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlWrongKey rev-parse HEAD
49c3e87d4fb5677783c55f8225c9e4f892273879
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlInventedAction rev-parse HEAD
49c3e87d4fb5677783c55f8225c9e4f892273879
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlWrongKey log --all --oneline | head -3
49c3e87 round-60: C1 freeze (census F_max 4, T_F 3; counter check_scoped_rules.py sha 6aea3be0)
bfe8cc2 round-60: plan draft amendment A1 …
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlWrongKey status --short
?? .scratch/
?? .ufo/waves/round-60/snapshots/
?? corpus/knowledge/scoped-rules-round60.md
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlInventedAction status --short
?? base_sources.txt
?? fetch/
?? probe/
```

Both sandboxes still sit at the v1 freeze `49c3e87d…` with only untracked scratch files: no commit
carries a world, and no receipt file exists for either control
(`.ufo/waves/round-60/controls/` contains `CtlAllFalse.md`, `CtlDoNothing.md`, `CtlFabSnapshot.md`,
`CtlJunk.md`, `CtlLabelShortcut.md`, `CtlNoReader.md`, `SUMMARY.md` — and no `CtlWrongKey.md` or
`CtlInventedAction.md`). The wrong-key and invented-action conjuncts therefore remain without a
pre-data control receipt under v2 as they were under v1; this seat did not manufacture a world for
them, and the gap is disclosed rather than filled.

## 8. Network

The `--fetch` runs make live requests only for rows the counter has already backed. Every request
was counted with a logging `curl` wrapper on `PATH` that appends each attempted URL to a marker log
and then `exec`s the real `/usr/bin/curl` (a passthrough, so the run's output is unaffected):

```
allfalse-world: exit=1 requests=21 distinct=7   (3 attempts each — the counter's own FETCH_ATTEMPTS = 3)
noreader-probe: exit=1 requests=1 distinct=1
fabsnap-pristine: exit=1 requests=1 distinct=1
fabsnap-fabricated: exit=1 requests=1 distinct=1
```

No page was fetched more than 3 times in any run. The one live page that backs and is found is the
VS Code custom-instructions page; fetched directly for the record:

```
$ date -u
Fri 23 Oct 2026 12:20:33 PM UTC
$ curl -sSL --max-time 30 -A '<browser UA>' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' \
    -o live-vscode.md -w 'status=%{http_code} bytes=%{size_download} final=%{url_effective}\n' \
    https://code.visualstudio.com/docs/agent-customization/custom-instructions.md
status=200 bytes=23715 final=https://code.visualstudio.com/docs/agent-customization/custom-instructions.md
$ date -u
Fri 23 Oct 2026 12:20:33 PM UTC
$ sha256sum live-vscode.md
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  live-vscode.md
```

Line 164 of those bytes is `applyTo: '**/*.py'` and line 54 mentions `applyTo`, matching the census
record for that client (`plans/round-60.md` § C1 census: VS Code `applyTo` :164).

## 9. Isolation

- All git writes happened inside `/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2` only: the receipt
  branch `receipt/ctl-rescore-v2` and the six replay branches `replay/ctl-*`. The v1 seats' sandboxes
  were cloned read-only and never written to; the `CtlNoReader` probe clone was read through a git
  alternates entry, which writes nothing into it.
- No lane file was edited. The lane's working tree shows only other seats' files
  (`corpus/SOURCES.md` modified by the build wave, plus untracked build/ and data files); this seat
  wrote exactly one file in the lane, this report.
- **The lane HEAD moved during this seat's run**, from the v2 freeze `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`
  to `49f7ff22a3c93a80d649611e9f6e4b8a4b43af35` ("round-60: erratum E2 — C1 declared exploratory
  before data (two v2 controls met the predicate by forged provenance)"), landed by the L1 at about
  09:21Z. Every measurement here is against the freeze named in this seat's item,
  `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`, and the counter file is the one committed at that
  revision. The counter file is unchanged by the later commit, so the measurements would be
  identical had they been taken at the newer HEAD:
  `git show 49f7ff22a3c93a80d649611e9f6e4b8a4b43af35:verifiers/check_scoped_rules.py | sha256sum`
  → `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`, and
  `git diff --stat b1cd64bb… 49f7ff2… -- verifiers/check_scoped_rules.py` is empty.
- The counter was never modified. The copy committed in the receipt commit hashes to the frozen v2
  sha256 (`git show HEAD:.ufo/waves/round-60/controls-v2/check_scoped_rules_v2.py | sha256sum` →
  `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`).
- Every run was capped with `timeout 900`; no unbounded recursive test run was started.
- No tool was installed (pacman is paused host-wide; nothing was missing), no model client was
  invoked, and no paid model call was made.

## 10. Receipt

**Control name:** `CtlRescoreV2` (re-score of every v1 control world under the frozen v2 counter).
**Sandbox commit:** `sandbox db75afb07519a185f68d77a6c3a862d7f8770e3f (/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2)`.
**Counter sha256 run:** `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`
(`/fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py`, extracted from `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`;
`TARGET = 3` read from `verifiers/check_scoped_rules.py:249` of that commit).
**Exact command (per world):**

```
cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/worlds/<Seat> && timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py --rev <world> --fetch
cd /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/worlds/<Seat> && timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r60/CtlRescoreV2/v2.py --rev <world>
```

**Full stdout:** quoted in full for every `--fetch` run in §4; every run's stdout and stderr are also
committed at `.ufo/waves/round-60/controls-v2/receipts/` in the sandbox commit (160 receipt files; 167
files in the whole `.ufo/waves/round-60/controls-v2/` tree, the rest being the frozen counter copy and
the six run scripts).
**Exit code:** 1 for every `--fetch` run and every run without `--fetch`. No run exited 2
(could-not-evaluate): every world revision is a commit in the clone, and `SKILL.md` exists at every
one of them. Every exit code was re-derived from scratch in a second, independent pass (all 14
worlds × both modes, 28 runs) and matched the first pass exactly:

```
CtlDoNothing       f4dcfd9 fetch_exit=1 nofetch_exit=1
CtlDoNothing       49c3e87d fetch_exit=1 nofetch_exit=1
CtlDoNothing       31092dc6 fetch_exit=1 nofetch_exit=1
CtlJunk            de808c7b fetch_exit=1 nofetch_exit=1
CtlJunk            127c6043 fetch_exit=1 nofetch_exit=1
CtlAllFalse        101c214 fetch_exit=1 nofetch_exit=1
CtlNoReader        eabe93f6 fetch_exit=1 nofetch_exit=1
CtlNoReader        43513eea fetch_exit=1 nofetch_exit=1
CtlFabSnapshot     a2893fa2 fetch_exit=1 nofetch_exit=1
CtlFabSnapshot     8933ce9e fetch_exit=1 nofetch_exit=1
CtlFabSnapshot     b713e5b1 fetch_exit=1 nofetch_exit=1
CtlLabelShortcut   415c767 fetch_exit=1 nofetch_exit=1
CtlLabelShortcut   18afea67 fetch_exit=1 nofetch_exit=1
CtlDoNothing       b1cd64bb fetch_exit=1 nofetch_exit=1
```

```
C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET
```

## 11. Risks and blockers

- **The wrong-key and invented-action conjuncts still have no pre-data control receipt under v2**
  (§7). That gap is inherited from the cancelled v1 seats, is disclosed here and in the v1 summary,
  and is not closed by this seat. [INFERENCE] The counter's own self-test arms (wrong `description`
  key at Cursor `:65`/`:99`, one-word action overlap) and the build wave's `ExecKeyForms` item are
  the remaining evidence for those two conjuncts.
- **The v2 base-URL conjunct is exercised only in its negative form by these worlds.** Every v1
  control row that carries a base-keyed URL lacks a `re-opens S### —` cell, so v2's relaxed conjunct
  is observed rejecting rather than accepting. The accepting side of that conjunct is covered by the
  sibling v2 seats `CtlReopenForged` and `CtlReopenHeldKey`, whose reports are in
  `.ufo/waves/round-60/controls-v2/`. This seat does not duplicate them.
- **Live-page drift.** F values depend on the live pages as of the run (12:05Z–12:20Z, 2026-10-23).
  The counter's live conjunct is a re-read of the live page, so a later page change could change a
  future F; the offline S values and every exit code are a property of the committed bytes only.

Report: .ufo/waves/round-60/controls-v2/CtlRescoreV2.md
