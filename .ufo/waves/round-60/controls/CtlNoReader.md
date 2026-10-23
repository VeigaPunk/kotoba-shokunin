Result: DONE — CtlNoReader: S 0 of 4; F 0 of 4; exit 1; predicate NOT MET

## Control and mutation

Control: `CtlNoReader`, pre-data C1 no-reader control (counter v1). Axes: frozen-counter identity, real-looking
rows that still fail because the pages were never opened and saved.

Measured world: sandbox eabe93f6c6f02caa66f845d50f34b2e8fbe33723 (/fast/scratch/hyaku/kotoba-r60/CtlNoReader), one
commit on top of the frozen revision `49c3e87d4fb5677783c55f8225c9e4f892273879`. The counter was never edited.

Mutation: everything except the page bytes is real, taken from the round-60 census reports
(`.ufo/waves/round-60/w0/Census*.md`):

- `SKILL.md` gains `### Scoped rule files by client` with the frozen header and seven rows. The four eligible
  clients carry their census token, scope key and action, each citing its own new SOURCES id and the census's
  cited snapshot line: Claude Code `.claude/rules/` / `paths` (S103 :198) / action (S103 :194); VS Code
  `.github/instructions/**/*.instructions.md` / `applyTo` (S104 :164) / action (S104 :329); Copilot CLI
  `.github/instructions/**/*.instructions.md` / `applyTo` (S105 :66) / action (S105 :60); Cursor `.cursor/rules` /
  `globs` (S106 :85) / action (S106 :131). Codex, Gemini CLI and opencode carry the census's NOT-ELIGIBLE
  finding (nested `AGENTS.md` by directory, directory-scoped `GEMINI.md`), so their tokens are not well-formed and
  they never enter K.
- `corpus/knowledge/scoped-rules-round60.md` carries the frozen entry header and the four census quotes, each
  cut byte-exact from the census seats' own fetched bytes (the Copilot CLI quote's table pipe is written
  `&#124;`, the round-59 house rule for a pipe inside a corpus table).
- `corpus/SOURCES.md` carries four new rows S103–S106 with the census URLs, tier A, status mined, opened
  2026-10-23, and the census reports' own sha256 digests of the pages.
- `corpus/lessons/round-60.md` carries `## Gate` with the four quotes and the fetch records.
- **No snapshot file is committed.** `.ufo/waves/round-60/snapshots/` does not exist in the world: the page is
  never opened and saved, so the world asserts digests for bytes it does not hold.

## Counter identity

Counter sha256 in the sandbox clone (exit 0), identical to the frozen file in the lane:

```sh
cd /fast/scratch/hyaku/kotoba-r60/CtlNoReader && sha256sum verifiers/check_scoped_rules.py
```

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  verifiers/check_scoped_rules.py
```

```sh
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 49c3e87d4fb5677783c55f8225c9e4f892273879:verifiers/check_scoped_rules.py | sha256sum
```

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  -
```

The counter's own `--self-test` in the clone (exit 0): `self-test: 0 failure(s) over 302 assertions`.

`TARGET` was read from the committed counter (`verifiers/check_scoped_rules.py`, line 232 in the frozen file):
`TARGET = 3`.

## Evidence in the measured sandbox commit

- `SKILL.md:135` — the heading `### Scoped rule files by client`; `SKILL.md:143` the frozen header
  `| Client | Rule files | Scope key | Action |`; `SKILL.md:145-148` the four eligible rows, `SKILL.md:149-151`
  the three ineligible rows.
- `corpus/knowledge/scoped-rules-round60.md:21` the frozen entry header; `:23-26` the four entry rows with their
  quotes and source ids.
- `corpus/SOURCES.md:116-119` — the four new rows S103–S106 with their census digests.
- `corpus/lessons/round-60.md:6` `## Gate`; `:10-13` the four Gate rows with the quotes.
- `git ls-tree -r --name-only HEAD -- .ufo/waves/round-60/snapshots` → no output: no snapshot is committed.
  `git show --stat HEAD` → 4 files changed, 69 insertions (`SKILL.md`, `corpus/SOURCES.md`,
  `corpus/knowledge/scoped-rules-round60.md`, `corpus/lessons/round-60.md`).

## Expected detector

The frozen counter's exact bounded CLI, once with and without `--fetch`, on the sandbox commit, run from the
clone. The no-reader world must retain K=4 (four well-formed tokens) and count no backed and no found row: a
world whose rows and sources look real but whose pages were never saved must not satisfy F>=TARGET.

## Receipt

Control: `CtlNoReader`. Sandbox commit: sandbox eabe93f6c6f02caa66f845d50f34b2e8fbe33723
(/fast/scratch/hyaku/kotoba-r60/CtlNoReader). Counter sha256 run:
`6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440` (`verifiers/check_scoped_rules.py` in the clone).

### With --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlNoReader`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev eabe93f6c6f02caa66f845d50f34b2e8fbe33723 --fetch
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 4; found on the live page 0 of 4
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev eabe93f6c6f02caa66f845d50f34b2e8fbe33723
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S103.page is missing at the revision
reject Codex: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
reject VS Code: entry row S104: snapshot .ufo/waves/round-60/snapshots/S104.page is missing at the revision
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S105.page is missing at the revision
reject Gemini CLI: SKILL.md rule token 'GEMINI.md' is not well-formed; no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S106.page is missing at the revision
reject opencode: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
```

Exit code: `1`.

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

### Without --fetch

Command (cwd `/fast/scratch/hyaku/kotoba-r60/CtlNoReader`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev eabe93f6c6f02caa66f845d50f34b2e8fbe33723
```

Full stdout:

```text
scoped rule files backed on committed snapshots 0 of 4; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev eabe93f6c6f02caa66f845d50f34b2e8fbe33723
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S103.page is missing at the revision
reject Codex: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
reject VS Code: entry row S104: snapshot .ufo/waves/round-60/snapshots/S104.page is missing at the revision
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S105.page is missing at the revision
reject Gemini CLI: SKILL.md rule token 'GEMINI.md' is not well-formed; no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; snapshot .ufo/waves/round-60/snapshots/S106.page is missing at the revision
reject opencode: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
```

Exit code: `1`.

## Isolation: the missing snapshot is what rejects the world

The reject reasons mix two independent defects, so a probe separates them. In a separate clone
(`/fast/scratch/hyaku/kotoba-r60/CtlNoReader/probe`, sandbox commit
43513eeaa274098f8d0b98941016b4418f854d20 (/fast/scratch/hyaku/kotoba-r60/CtlNoReader/probe), one commit on top of
the same world) the four census pages' own bytes — the exact files the census seats fetched, unchanged — were
committed as `.ufo/waves/round-60/snapshots/S103.page`–`S106.page`. Nothing else changed.

```sh
cd /fast/scratch/hyaku/kotoba-r60/CtlNoReader/probe && timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 43513eeaa274098f8d0b98941016b4418f854d20
```

```text
scoped rule files backed on committed snapshots 1 of 4; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 43513eeaa274098f8d0b98941016b4418f854d20
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rule token 'GEMINI.md' is not well-formed; no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rule token 'AGENTS.md' is not well-formed; no entry row names the client
```

Exit code: `1`.

Reading of the probe: with the bytes present, VS Code — the one row whose census URL is not a base SOURCES URL —
backs on the committed snapshot, which means the tokens, the quotes, the scope keys at their cited lines and the
action cells of this world are all sound; the only reason VS Code is rejected in the measured world is the
missing snapshot. The other three rows carry the separate base-URL defect (their census pages are base rows
S043, S048 and S049) and would need a re-open row under counter v2.

The two semantic conjuncts were also checked directly against the census bytes with the frozen counter's own
helpers (`key_site`, `scope_conjunct`, `action_conjunct`, `citation_why`), on the real pages: Claude Code
`paths` at line 198 and the action at line 194, VS Code `applyTo` at 164 and the action at 329, Copilot CLI
`applyTo` at 66 and the action at 60, Cursor `globs` at 85 and the action at 131 — every conjunct returned empty
(a pass) and every citation named its own source id. The world is therefore sound on everything except the pages
it never saved.

## Network

The `--fetch` run performed no network request. Proof: with an instrumented `curl` first on `PATH` (a wrapper
that appends to a marker log and exits 7), the run produced the same stdout and the marker log was never
created — `/tmp/fakebin/called.log` does not exist. The counter reaches the live-fetch stage only for a row it
has already backed, and no row was backed.

## Note on the counter version (recorded, not acted on)

The lane's HEAD moved during this seat's run: while I was scoring, commit
`b1cd64bb45eee744c4ec93be8631f1eddb28fddd` ("round-60: erratum E1 before data — counter v2") landed, freezing
counter v2 (`sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`) and adding the re-open
conjunct. My control was specified against v1 at `49c3e87`, so the receipt above is the v1 receipt, and the v1
world is left intact as v1 evidence. For information only, the same world re-scored with the v2 counter file
(`git show b1cd64bb…:verifiers/check_scoped_rules.py`, sha256 `ca2585a4…`) gives the same verdict — S 0 of 4,
F 0 of 4, exit 1, predicate NOT MET — with the extra reason `re-open names no base row with this URL` on the
three base-URL rows; and the probe with the census bytes committed gives S 1 of 4 under v2 as well. The v1/v2
comparison of every control is the separate `CtlRescoreV2` seat's item.

## Housekeeping

Only this report was written in the lane. The sandbox clone, the probe clone and every world file, counter copy
and receipt live under `/fast/scratch/hyaku/kotoba-r60/CtlNoReader/`. No lane file was edited by this seat:
`git status --short` in the lane shows exactly two untracked paths, the L1's own
`.ufo/waves/round-60/controls-v2-call.json` and this seat's report
`.ufo/waves/round-60/controls/CtlNoReader.md`; no tracked file is modified and the lane HEAD is unchanged by me.
No tool was installed (pacman is paused host-wide; nothing was missing), no model client was invoked, and no page
was fetched by this seat — the census seats' bytes were read from their scratch directories, and the four URLs in
the world were taken from the census reports.

Report: .ufo/waves/round-60/controls/CtlNoReader.md
