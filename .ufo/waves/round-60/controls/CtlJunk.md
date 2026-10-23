Result: DONE — CtlJunk: S 0 of 7; F 0 of 7; exit 1; predicate NOT MET

## Mutant and expected detector

Control: `CtlJunk`, pre-data C1 junk-world control. Axes: frozen-counter identity, seven-row shape, junk rejection, exact restoration.

Measured world: sandbox de808c7bf0ce337d5e477b0c80ab3e3eab332540 (/fast/scratch/hyaku/kotoba-r60/CtlJunk), one commit on top of the frozen revision `49c3e87d4fb5677783c55f8225c9e4f892273879`. The counter was never edited. `TARGET = 3` was read from the committed counter, line 232 (also checked in the clone).

Mutation: add the required seven exact client labels, but make all free-text evidence junk: seven well-formed random path tokens, random backticked keys, random action words and line citations, random non-pinned `.invalid` hosts, seven junk Gate quotes, and seven invented snapshot pages. Keep only required headers, client labels, source ids and parser metadata structural. The generated words and citations use `random.Random('CtlJunk-r60-frozen-49c3e87d')`; ids are S103–S109. Each quote is seven words, appears byte-exact at snapshot line 2 and in Gate, and its snapshot's actual full sha256 is printed in the SOURCES row. No real source is asserted.

Evidence in the measured sandbox commit:
- `SKILL.md:589-599`: exact heading/header and all seven junk client rows.
- `corpus/knowledge/scoped-rules-round60.md:3-11`: matching entry table, tokens, ids and quotes.
- `corpus/SOURCES.md:115-121`: the seven invented-host rows and real snapshot digests.
- `corpus/lessons/round-60.md:3-13`: Gate heading/table/quotes.
- `.ufo/waves/round-60/snapshots/S103.page:1-12` through `S109.page:1-12`: invented bytes, with each matching quote at line 2.
- World construction reuses the frozen self-test's `src_row`/`world` layout and UTF-8 page hashing (`verifiers/check_scoped_rules.py:1663-1678`), adapted to the seven assigned ids and junk text. No satisfying-fixture source claims were imported.

Expected detector: the frozen counter's exact bounded CLI below, once each with and without `--fetch` on pristine, mutated and restored revisions. The junk control should retain K=7 but count no backed or found rows; it must not satisfy F>=TARGET.

## Counter identity and time

Frozen-file command (exit 0):

```sh
timeout 30 bash -c 'git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 49c3e87d4fb5677783c55f8225c9e4f892273879:verifiers/check_scoped_rules.py | sha256sum'
```

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  -
```

Clone command (exit 0; the following counter line is identical before mutation, in the mutant world and after restoration):

```sh
timeout 30 sha256sum verifiers/check_scoped_rules.py SKILL.md corpus/SOURCES.md
```

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  verifiers/check_scoped_rules.py
ca6a65374d407864b31a330886af8724f579257c69d8d9de8196daca4f3ac750  SKILL.md
3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a  corpus/SOURCES.md
```

`timeout 10 date -u`, exit 0:

```text
Fri 23 Oct 2026 10:49:31 AM UTC
```

No manual source fetches were made; every new URL is synthetic. HTTP access status/time and fetched-byte receipts therefore do not apply. [INFERENCE] The `--fetch` runs issued no page requests: S=0 and the frozen main loop fetches only backed rows. No page was fetched more than three times. No tools were installed or updated.

## Junk-world receipt — with --fetch

Measured world: sandbox de808c7bf0ce337d5e477b0c80ab3e3eab332540 (/fast/scratch/hyaku/kotoba-r60/CtlJunk).

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev de808c7bf0ce337d5e477b0c80ab3e3eab332540 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 7; found on the live page 0 of 7
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev de808c7bf0ce337d5e477b0c80ab3e3eab332540
reject Claude Code: entry row S103: quote holds no rule/instruction word outside the token; S103 URL 'https://jeyzptol.invalid/yangkgxc/qomcfcpn' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S103.page: scope key 'dlppmxoe' is not in key form with a path pattern at line 3; snapshot .ufo/waves/round-60/snapshots/S103.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Codex: entry row S104: quote holds no rule/instruction word outside the token; S104 URL 'https://rrsjvcbe.invalid/ejwxwspz/efcxmzqq' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S104.page: scope key 'scxclyrg' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S104.page: action cell shares 0 of its 4 content word(s) with line 10 (need >= 2)
reject VS Code: entry row S105: quote holds no rule/instruction word outside the token; S105 URL 'https://dhafooni.invalid/aqcfxwtd/dpljmlab' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S105.page: scope key 'vyenlamf' is not in key form with a path pattern at line 6; snapshot .ufo/waves/round-60/snapshots/S105.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Copilot CLI: entry row S106: quote holds no rule/instruction word outside the token; S106 URL 'https://lhodyslf.invalid/rujbmefo/wlrubcar' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S106.page: scope key 'himzgfks' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S106.page: action cell shares 0 of its 4 content word(s) with line 7 (need >= 2)
reject Gemini CLI: entry row S107: quote holds no rule/instruction word outside the token; S107 URL 'https://fuoppwwp.invalid/agzmudxh/hsecazvg' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S107.page: scope key 'wrzupirq' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S107.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Cursor: entry row S108: quote holds no rule/instruction word outside the token; S108 URL 'https://sdqnhhio.invalid/obzrwqga/kasprnac' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S108.page: scope key 'xvirlugy' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S108.page: action cell shares 0 of its 4 content word(s) with line 5 (need >= 2)
reject opencode: entry row S109: quote holds no rule/instruction word outside the token; S109 URL 'https://lpngyjvw.invalid/dxjofmom/fmyozlsf' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S109.page: scope key 'bekqosuc' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S109.page: action cell shares 0 of its 4 content word(s) with line 12 (need >= 2)
```

Exit code: `1`.

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

## Junk-world receipt — without --fetch

Measured world: sandbox de808c7bf0ce337d5e477b0c80ab3e3eab332540 (/fast/scratch/hyaku/kotoba-r60/CtlJunk).

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev de808c7bf0ce337d5e477b0c80ab3e3eab332540
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 7; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev de808c7bf0ce337d5e477b0c80ab3e3eab332540
reject Claude Code: entry row S103: quote holds no rule/instruction word outside the token; S103 URL 'https://jeyzptol.invalid/yangkgxc/qomcfcpn' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S103.page: scope key 'dlppmxoe' is not in key form with a path pattern at line 3; snapshot .ufo/waves/round-60/snapshots/S103.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Codex: entry row S104: quote holds no rule/instruction word outside the token; S104 URL 'https://rrsjvcbe.invalid/ejwxwspz/efcxmzqq' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S104.page: scope key 'scxclyrg' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S104.page: action cell shares 0 of its 4 content word(s) with line 10 (need >= 2)
reject VS Code: entry row S105: quote holds no rule/instruction word outside the token; S105 URL 'https://dhafooni.invalid/aqcfxwtd/dpljmlab' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S105.page: scope key 'vyenlamf' is not in key form with a path pattern at line 6; snapshot .ufo/waves/round-60/snapshots/S105.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Copilot CLI: entry row S106: quote holds no rule/instruction word outside the token; S106 URL 'https://lhodyslf.invalid/rujbmefo/wlrubcar' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S106.page: scope key 'himzgfks' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S106.page: action cell shares 0 of its 4 content word(s) with line 7 (need >= 2)
reject Gemini CLI: entry row S107: quote holds no rule/instruction word outside the token; S107 URL 'https://fuoppwwp.invalid/agzmudxh/hsecazvg' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S107.page: scope key 'wrzupirq' is not in key form with a path pattern at line 9; snapshot .ufo/waves/round-60/snapshots/S107.page: action cell shares 0 of its 4 content word(s) with line 8 (need >= 2)
reject Cursor: entry row S108: quote holds no rule/instruction word outside the token; S108 URL 'https://sdqnhhio.invalid/obzrwqga/kasprnac' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S108.page: scope key 'xvirlugy' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S108.page: action cell shares 0 of its 4 content word(s) with line 5 (need >= 2)
reject opencode: entry row S109: quote holds no rule/instruction word outside the token; S109 URL 'https://lpngyjvw.invalid/dxjofmom/fmyozlsf' is not on a pinned host; snapshot .ufo/waves/round-60/snapshots/S109.page: scope key 'bekqosuc' is not in key form with a path pattern at line 10; snapshot .ufo/waves/round-60/snapshots/S109.page: action cell shares 0 of its 4 content word(s) with line 12 (need >= 2)
```

Exit code: `1`.

## Pristine detector receipts

Frozen revision `49c3e87d4fb5677783c55f8225c9e4f892273879`, checked out only in the isolated sandbox clone.

### With --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 49c3e87d4fb5677783c55f8225c9e4f892273879 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 0; found on the live page 0 of 0
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 49c3e87d4fb5677783c55f8225c9e4f892273879
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: `1`.

### Without --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 49c3e87d4fb5677783c55f8225c9e4f892273879
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 0; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 49c3e87d4fb5677783c55f8225c9e4f892273879
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: `1`.

## Mutation verdict

The control is rejected: all seven tokens enter K, and every row independently reports a missing rule/instruction word, a non-pinned host, a non-key/pattern scope citation, and action overlap 0/4 (need >=2). No missing/mismatching snapshot hash is reported; pinning invented bytes does not make this junk world count.

**Mutation-kill classification: INCONCLUSIVE, not killed.** The pristine detector already exits 1, so these runs cannot establish a green-to-red mutation kill. The narrower control outcome is observed, not inferred: S=0/7, F=0/7, exit 1, predicate NOT MET. No contract change, integration or claim-admission judgment is made.

## Exact restoration evidence

The sandbox world remains reachable by its commit. Its own changes were then undone with a new revert commit; no reset, history rewrite, lane checkout/index write or sibling edit occurred.

Command (exit 0, cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 90 bash -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git -c user.name=KotobaR60.CtlJunk -c user.email=kotoba-r60-ctljunk@shokunin.local -c core.hooksPath=/dev/null -c commit.gpgsign=false revert --no-edit de808c7bf0ce337d5e477b0c80ab3e3eab332540 && git rev-parse HEAD'
```

Restoration commit: sandbox 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2 (/fast/scratch/hyaku/kotoba-r60/CtlJunk). The observed revert reported `11 files changed, 128 deletions(-)` and deleted the seven invented pages plus the new entry and lesson, undoing the two existing-file insertions.

Tracked-tree hashes (`timeout 30 git --no-optional-locks rev-parse '<rev>^{tree}'`, each exit 0):

| state | tree hash |
|---|---|
| pristine | `7a840f81feb44ee2fb91a474e98dddda5766c840` |
| mutated | `5e42d8fc6b379ee5237146d75d25bdb84f6827f9` |
| restored | `7a840f81feb44ee2fb91a474e98dddda5766c840` |

Before/mutated/after SHA256s (`sha256sum` in the clone, each invocation exit 0):

| path | pristine | mutated | restored |
|---|---|---|---|
| `verifiers/check_scoped_rules.py` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` |
| `SKILL.md` | `ca6a65374d407864b31a330886af8724f579257c69d8d9de8196daca4f3ac750` | `b3310ae5a43dc13bd9845966dd5a83913e079ba891cb2ed69a3a06ff1c00e5b4` | `ca6a65374d407864b31a330886af8724f579257c69d8d9de8196daca4f3ac750` |
| `corpus/SOURCES.md` | `3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a` | `6f694938b31af5161086bbc7027b78dfe8215bed29bc500e69db3c02157171f7` | `3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a` |
| `corpus/knowledge/scoped-rules-round60.md` | absent | `6d2ef836a84a46c67943b5146aefa97c24a5a6f1f88fd2664b2b8f94e183b5a3` | absent |
| `corpus/lessons/round-60.md` | absent | `8135e8960980d3fcbde8502ca71ac84abfbb733bea8b2435e74d105fe2629552` | absent |

Mutated snapshot hash command (exit 0):

```sh
timeout 30 sha256sum verifiers/check_scoped_rules.py SKILL.md corpus/SOURCES.md corpus/knowledge/scoped-rules-round60.md corpus/lessons/round-60.md .ufo/waves/round-60/snapshots/S103.page .ufo/waves/round-60/snapshots/S104.page .ufo/waves/round-60/snapshots/S105.page .ufo/waves/round-60/snapshots/S106.page .ufo/waves/round-60/snapshots/S107.page .ufo/waves/round-60/snapshots/S108.page .ufo/waves/round-60/snapshots/S109.page
```

Full stdout:

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  verifiers/check_scoped_rules.py
b3310ae5a43dc13bd9845966dd5a83913e079ba891cb2ed69a3a06ff1c00e5b4  SKILL.md
6f694938b31af5161086bbc7027b78dfe8215bed29bc500e69db3c02157171f7  corpus/SOURCES.md
6d2ef836a84a46c67943b5146aefa97c24a5a6f1f88fd2664b2b8f94e183b5a3  corpus/knowledge/scoped-rules-round60.md
8135e8960980d3fcbde8502ca71ac84abfbb733bea8b2435e74d105fe2629552  corpus/lessons/round-60.md
36625851f49799411d48f6976cfa9ee19b1ce34fc7ca519e862824cb84f26851  .ufo/waves/round-60/snapshots/S103.page
2364399acd9b8d803dbc66f4e638d12dea52b2ac16edd9f64f2f8c0be77e54e5  .ufo/waves/round-60/snapshots/S104.page
dc1df4b034c69d68cb9f56c3c6aa90c5ff91801f1c7e155f966292070c1f3f8f  .ufo/waves/round-60/snapshots/S105.page
d8c1da9690e50eaf90ed6a3b426037ff397f5a0120e839256856e289660281a2  .ufo/waves/round-60/snapshots/S106.page
8dfff2ef8e4c5ff7202999a09f3ee51eccea090a9b226dfc3e338f712e272615  .ufo/waves/round-60/snapshots/S107.page
8de81fb66505683428a4befc342188a735101527c3f210a930e0ce2a201ccd36  .ufo/waves/round-60/snapshots/S108.page
6a49e34a283f9612efd7f0b499fb5501f2602d6b33a246f40627a2c2136d81f3  .ufo/waves/round-60/snapshots/S109.page
```

All seven pages were absent before and are absent after the revert; the equal full tracked-tree hashes establish restoration of the tracked content and modes, including removal of all added files.

## Restored detector receipts

Measured restored revision: sandbox 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2 (/fast/scratch/hyaku/kotoba-r60/CtlJunk).

### With --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 0; found on the live page 0 of 0
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: `1`.

### Without --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlJunk`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 0; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 127c6043bb6783c7e735c4cc825ac4e87f5bb6a2
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: `1`.

Only this report was written in the lane. All control construction, commits and detector executions occurred inside `/fast/scratch/hyaku/kotoba-r60/CtlJunk`. No self-test, unrelated check, model client or additional runtime was invoked.

Report: .ufo/waves/round-60/controls/CtlJunk.md
