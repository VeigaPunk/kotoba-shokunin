Result: DONE — CtlAllFalse: S 7 of 7; F 0 of 7; exit 1; predicate NOT MET

# CtlAllFalse — fabricated-source pre-data control

Control world: sandbox 101c2140e7b969c20198269c72e77e424b5db2a5 (/fast/scratch/hyaku/kotoba-r60/CtlAllFalse). Preserved by the sandbox-only branch `ctl-all-false-world`; the working tree was subsequently restored to the freeze.

Freeze: `49c3e87d4fb5677783c55f8225c9e4f892273879`. `TARGET = 3` was read from the frozen counter at `verifiers/check_scoped_rules.py:232`, not inferred from the task text.

Claim axis: depth. Diagnostic dimensions: source authenticity (S versus F), frozen-counter fidelity, sandbox isolation, bounded fetching, and byte-exact restoration.

## Mutant, expected detector, and verdict

- Mutant: replace missing scoped-rule data with seven internally consistent but entirely fabricated records. Each client has an invented URL on its pinned host, invented dot-led rule token, invented `matchFiles` key, invented quote, matching Gate record, and fabricated committed page whose sha256 is declared in its SOURCES row. No counter code was changed.

- Expected detector: the frozen counter should accept the offline shape (S = 7 of 7) but reject the live predicate unless at least TARGET live pages actually carry the quotes and key-form sites. Both invocations were bounded by `timeout 900`.

- Observed: S = 7 of 7 without and with `--fetch`; F = 0 of 7 with `--fetch`; each fabricated URL returned HTTP 404 on all three attempts. All offline conjuncts were satisfied. Offline exit 1 is specified behavior, not an additional rejection of these rows.

- Mutation-test verdict: **INCONCLUSIVE, not a killed mutant**, because the pristine frozen world already exits 1 (0 of 0). The narrower control observation is complete: the fabricated world did not meet the declared live predicate. The offline score alone does not authenticate a source. No broader soundness verdict is claimed.


C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

## Frozen counter identity

Read-only lane command, exit 0:

```sh
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 49c3e87d4fb5677783c55f8225c9e4f892273879:verifiers/check_scoped_rules.py | sha256sum
```

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  -
```

From the clone `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse`, `timeout 10 sha256sum verifiers/check_scoped_rules.py`, exit 0, immediately after committing the control:

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  verifiers/check_scoped_rules.py
```

## World and evidence locations

At the labelled sandbox revision: `SKILL.md:135-147` contains the scoped-rule section and seven rows; `corpus/knowledge/scoped-rules-round60.md:7-15` contains the matching entry table; `corpus/SOURCES.md:115-121` contains S103–S109; `corpus/lessons/round-60.md:5-15` records the quotes in Gate. Every `.ufo/waves/round-60/snapshots/S###.page` has its quote at line 2, `matchFiles: "src/**/*.ts"` at line 4, and `Scope rules to matching source files.` at line 6. The Action cell repeats that line exactly and cites its own source.

Construction reused the frozen `CLIENTS`, `HOSTS`, `MARKERS`, `OPENED`, `normalise()` and `snapshot_path()` helpers, and the self-test world layout at counter lines 1603–1684. Fabrication is explicitly labelled in the sandbox files; no row is offered as vendor evidence.

| Client | Source id | Invented token | Invented URL |
|---|---|---|---|

| Claude Code | S103 | `.claude/scoped/` | <https://code.claude.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| Codex | S104 | `.codex/scoped/` | <https://developers.openai.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| VS Code | S105 | `.vscode/scoped/` | <https://code.visualstudio.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| Copilot CLI | S106 | `.copilot/scoped/` | <https://docs.github.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| Gemini CLI | S107 | `.gemini/scoped/` | <https://geminicli.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| Cursor | S108 | `.cursor/scoped/` | <https://cursor.com/docs/ctl-all-false-round60-49c3e87d4fb5.md> |

| opencode | S109 | `.opencode/scoped/` | <https://opencode.ai/docs/ctl-all-false-round60-49c3e87d4fb5.md> |


All quotes below were fabricated, not extracted from the live 404 responses. They are byte-exact line-2 snapshot text, with no Markdown stripped or other shaping. Their word counts were calculated with `len(quote.split())` during construction.

| Source | Fabricated quote at snapshot line 2 | Words | Snapshot bytes | Snapshot sha256 |
|---|---|---|---|---|

| S103 | Claude Code keeps scoped rules in .claude/scoped/ for matching source files. | 11 | 191 | `605caf3a2e4083a443531535c9fb5cfc37617045f2476a1d89ff6326547729f0` |

| S104 | Codex keeps scoped rules in .codex/scoped/ for matching source files. | 10 | 178 | `226c4d300ad05a5f8e8bffba01b02c9112daef9eb8fab1cc5bee755e7a51499e` |

| S105 | VS Code keeps scoped rules in .vscode/scoped/ for matching source files. | 11 | 183 | `50649aa3b8aff1adecdf2da2364dc923b5c05a74e826292ec3bdd2f8aa476697` |

| S106 | Copilot CLI keeps scoped rules in .copilot/scoped/ for matching source files. | 11 | 192 | `7ab154d4f954834ec3324292cac7d7e3f7360d47084d4a84523b51993c1c9f44` |

| S107 | Gemini CLI keeps scoped rules in .gemini/scoped/ for matching source files. | 11 | 189 | `5229cf31661f9eb9f3b13457c6fffc5d03ddadc927af54bf7dda2c40dd4dd05c` |

| S108 | Cursor keeps scoped rules in .cursor/scoped/ for matching source files. | 10 | 181 | `19dff331063cd0a2805901625f17853e82f330d73c7fcc521c90a86aabe9ed8e` |

| S109 | opencode keeps scoped rules in .opencode/scoped/ for matching source files. | 10 | 187 | `1e268c49fcf343e7c98ff68639a99a7ea079ee6f5bf2033b8a69e3d0c497f3f5` |


## Exact detector receipts

All commands below ran from `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse` with `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` removed. The same PATH and detector were used in pristine, mutated and restored runs. PATH prefixed `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse/control-receipts/bin` solely to record actual curl responses. That receipt shim invokes `/usr/bin/curl` with every original argument, returns its stdout/stderr and exit status unchanged, and adds a 35-second subprocess bound around the counter’s existing 30-second curl cap. It supplies no substitute response, does not rewrite pages, and does not bypass access controls. Source: `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse/control-receipts/bin/curl:1-46`. Raw response bodies and metadata remain under the sandbox’s `control-receipts/`.


### Pristine — without --fetch

`date -u` output:

```text
Fri Oct 23 10:48:30 AM UTC 2026
```

Command:

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

Exit code: 1. Stderr: empty.


### Pristine — with --fetch

`date -u` output:

```text
Fri Oct 23 10:48:30 AM UTC 2026
```

Command:

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

Exit code: 1. Stderr: empty.


### Mutated — without --fetch

`date -u` output:

```text
Fri Oct 23 10:49:52 AM UTC 2026
```

Command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 101c2140e7b969c20198269c72e77e424b5db2a5
```

Full stdout:

```text
scoped rule files backed on committed snapshots 7 of 7; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 101c2140e7b969c20198269c72e77e424b5db2a5
```

Exit code: 1. Stderr: empty.


### Mutated — with --fetch

`date -u` output:

```text
Fri Oct 23 10:49:53 AM UTC 2026
```

Command:

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 101c2140e7b969c20198269c72e77e424b5db2a5 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 7 of 7; found on the live page 0 of 7
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 101c2140e7b969c20198269c72e77e424b5db2a5
reject Claude Code: live fetch failed: HTTP 404 at https://code.claude.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Codex: live fetch failed: HTTP 404 at https://developers.openai.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject VS Code: live fetch failed: HTTP 404 at https://code.visualstudio.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Copilot CLI: live fetch failed: HTTP 404 at https://docs.github.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Gemini CLI: live fetch failed: HTTP 404 at https://geminicli.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject Cursor: live fetch failed: HTTP 404 at https://cursor.com/docs/ctl-all-false-round60-49c3e87d4fb5.md
reject opencode: live fetch failed: HTTP 404 at https://opencode.ai/docs/ctl-all-false-round60-49c3e87d4fb5.md
```

Exit code: 1. Stderr: empty.


### Restored — without --fetch

`date -u` output:

```text
Fri Oct 23 10:49:59 AM UTC 2026
```

Command:

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

Exit code: 1. Stderr: empty.


### Restored — with --fetch

`date -u` output:

```text
Fri Oct 23 10:49:59 AM UTC 2026
```

Command:

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

Exit code: 1. Stderr: empty.


## Actual live-fetch access receipts

Authoritative per-attempt records: `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse/control-receipts/fetches.jsonl:1-21`; exact bodies: `control-receipts/fetch-01.body` through `fetch-21.body` in the sandbox. Each row below pastes the actual `date -u` output recorded immediately before that curl. URL is the invented URL for its source id in the table above; effective URL was identical to the requested URL on all 21 attempts. All curl process exits were 0, all HTTP statuses were 404, and all curl stderr was empty. Three requests per URL, no additional manual fetches. Pristine/restored had no backed rows and therefore made no page requests. No live quote or client-wide absence claim is made.

| Attempt / body | Source | `date -u` output | HTTP | Bytes | Body sha256 |
|---|---|---|---|---|---|

| 01 / fetch-01.body | S103 | Fri Oct 23 10:49:53 AM UTC 2026 | 404 | 671 | `80cade18d34786bdda27c57f95381008cc9cfbc395e2e363d3dbb3f7ad4c2bc3` |

| 02 / fetch-02.body | S103 | Fri Oct 23 10:49:53 AM UTC 2026 | 404 | 671 | `80cade18d34786bdda27c57f95381008cc9cfbc395e2e363d3dbb3f7ad4c2bc3` |

| 03 / fetch-03.body | S103 | Fri Oct 23 10:49:53 AM UTC 2026 | 404 | 671 | `80cade18d34786bdda27c57f95381008cc9cfbc395e2e363d3dbb3f7ad4c2bc3` |

| 04 / fetch-04.body | S104 | Fri Oct 23 10:49:54 AM UTC 2026 | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |

| 05 / fetch-05.body | S104 | Fri Oct 23 10:49:54 AM UTC 2026 | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |

| 06 / fetch-06.body | S104 | Fri Oct 23 10:49:54 AM UTC 2026 | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |

| 07 / fetch-07.body | S105 | Fri Oct 23 10:49:54 AM UTC 2026 | 404 | 19510 | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |

| 08 / fetch-08.body | S105 | Fri Oct 23 10:49:55 AM UTC 2026 | 404 | 19510 | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |

| 09 / fetch-09.body | S105 | Fri Oct 23 10:49:55 AM UTC 2026 | 404 | 19510 | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |

| 10 / fetch-10.body | S106 | Fri Oct 23 10:49:56 AM UTC 2026 | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |

| 11 / fetch-11.body | S106 | Fri Oct 23 10:49:56 AM UTC 2026 | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |

| 12 / fetch-12.body | S106 | Fri Oct 23 10:49:56 AM UTC 2026 | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |

| 13 / fetch-13.body | S107 | Fri Oct 23 10:49:56 AM UTC 2026 | 404 | 31633 | `d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee` |

| 14 / fetch-14.body | S107 | Fri Oct 23 10:49:57 AM UTC 2026 | 404 | 31633 | `d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee` |

| 15 / fetch-15.body | S107 | Fri Oct 23 10:49:57 AM UTC 2026 | 404 | 31633 | `d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee` |

| 16 / fetch-16.body | S108 | Fri Oct 23 10:49:57 AM UTC 2026 | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |

| 17 / fetch-17.body | S108 | Fri Oct 23 10:49:57 AM UTC 2026 | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |

| 18 / fetch-18.body | S108 | Fri Oct 23 10:49:57 AM UTC 2026 | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |

| 19 / fetch-19.body | S109 | Fri Oct 23 10:49:58 AM UTC 2026 | 404 | 126 | `8b497bf22cd8acde33f442928582ce5fb600fc29eb4d528aa60f6e618668545e` |

| 20 / fetch-20.body | S109 | Fri Oct 23 10:49:58 AM UTC 2026 | 404 | 126 | `8b497bf22cd8acde33f442928582ce5fb600fc29eb4d528aa60f6e618668545e` |

| 21 / fetch-21.body | S109 | Fri Oct 23 10:49:59 AM UTC 2026 | 404 | 126 | `8b497bf22cd8acde33f442928582ce5fb600fc29eb4d528aa60f6e618668545e` |


## Exact restoration and before / mutated / restored hashes

The restoration was in a `finally` block, so detector failure could not skip it. Command, in this sandbox only:

```sh
timeout 30 git checkout -q 49c3e87d4fb5677783c55f8225c9e4f892273879
```

Exit 0; stdout empty; stderr empty. All 12 observed input states matched the pristine manifest after restoration (the counter plus 11 world paths). New control-only files were absent again. Both restored detector outputs and exits matched their respective pristine runs, as pasted above. The receipt files are intentionally retained outside the measured input paths.

Hash computation: `hashlib.sha256(path.read_bytes()).hexdigest()` for present inputs; `ABSENT` for missing paths. Saved manifests: `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse/control-receipts/pristine-hashes.json:1-14`, `mutated-hashes.json:1-14`, and `restored-hashes.json:1-14`.

| Input path | Before sha256 / state | Mutated sha256 / state | Restored sha256 / state |
|---|---|---|---|

| `verifiers/check_scoped_rules.py` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` | `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` |

| `SKILL.md` | `ca6a65374d407864b31a330886af8724f579257c69d8d9de8196daca4f3ac750` | `0cf75b2ab7afe500edd905c67c4485ef91ea7517a4391dcf557c4708a393e370` | `ca6a65374d407864b31a330886af8724f579257c69d8d9de8196daca4f3ac750` |

| `corpus/SOURCES.md` | `3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a` | `81b8b8fa271eb610020d3546207955f8a2421d0ebabe0d24bb673532464bd0f2` | `3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a` |

| `corpus/knowledge/scoped-rules-round60.md` | `ABSENT` | `7a88fddb76484a9071bda1965132beb0d74b09655da72da28632fe8c81af82d5` | `ABSENT` |

| `corpus/lessons/round-60.md` | `ABSENT` | `52585380210ce8aea7c017c51d379a59924301ff9cd46d28c6e62104cfedec15` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S103.page` | `ABSENT` | `605caf3a2e4083a443531535c9fb5cfc37617045f2476a1d89ff6326547729f0` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S104.page` | `ABSENT` | `226c4d300ad05a5f8e8bffba01b02c9112daef9eb8fab1cc5bee755e7a51499e` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S105.page` | `ABSENT` | `50649aa3b8aff1adecdf2da2364dc923b5c05a74e826292ec3bdd2f8aa476697` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S106.page` | `ABSENT` | `7ab154d4f954834ec3324292cac7d7e3f7360d47084d4a84523b51993c1c9f44` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S107.page` | `ABSENT` | `5229cf31661f9eb9f3b13457c6fffc5d03ddadc927af54bf7dda2c40dd4dd05c` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S108.page` | `ABSENT` | `19dff331063cd0a2805901625f17853e82f330d73c7fcc521c90a86aabe9ed8e` | `ABSENT` |

| `.ufo/waves/round-60/snapshots/S109.page` | `ABSENT` | `1e268c49fcf343e7c98ff68639a99a7ea079ee6f5bf2033b8a69e3d0c497f3f5` | `ABSENT` |


## Scope and handoff

Only this report was written in the lane. All execution, sandbox commits, page fabrication, response-body receipts and restoration occurred under `/fast/scratch/hyaku/kotoba-r60/CtlAllFalse`. No fleet/sibling source, lane Git/jj state, counter code, contract, or routing was changed; nothing was pushed. No package/tool installations or updates were needed. No build, linter, formatter, self-test, runtime judge, or paid client/model call was run.

Receipt files: `control-receipts/commands.json` (all six actual command records), `world.json` (fabricated input metadata), `fetches.jsonl` (21 real fetch receipts), the body files, three hash manifests and `restoration.json`. These are sandbox artifacts, not corpus admissions.


Report: .ufo/waves/round-60/controls/CtlAllFalse.md
