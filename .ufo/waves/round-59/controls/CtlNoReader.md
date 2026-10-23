# CtlNoReader — C1 pre-data control (real rows, entry, SOURCES rows and Gate; no page snapshot committed)

Result: DONE — CtlNoReader: S 0 of 6; F 0 of 6; G 0; exit 1; predicate NOT MET

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

Claim C1, frozen counter `verifiers/check_hook_files.py` at the freeze revision
`67b68e0f9a0c48e5aa5ced63e6117cfca69da491` (`TARGET = 4` at `verifiers/check_hook_files.py:253`,
`NEW_TARGET = 5` at `:254`, both read from that committed file). Control seat:
`KotobaR59.CtlNoReader`. This report is the only lane file written. No lane content, no lane git
write, no jj command, no fleet-root write.

## Sandbox

Clone `/fast/scratch/hyaku/kotoba-r59/CtlNoReader`, `git clone` of the lane then
`git checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491`; `git log --oneline -1` before the
control commit printed `67b68e0 round-59: freeze addendum — Events conjunct limit and semantic seats
named before controls`.

Control world, one sandbox commit on top of the freeze revision:

**sandbox `5e88a7413bc1580107231adba644884d34c235e1` (/fast/scratch/hyaku/kotoba-r59/CtlNoReader)**

Superseded intermediate build, same clone, not the world scored in the receipt below: sandbox
`6154cab6e106f3e978ed935101f71d4d834afca0` (`/fast/scratch/hyaku/kotoba-r59/CtlNoReader`) appended
the six SOURCES rows after the file's trailing lead lists; it was rebuilt with the rows at the end of
the registry table. Both builds were scored with and without `--fetch` and printed the same seven
reject lines, and the shell reported exit 1 for those runs; the runs pasted below are the `5e88a74`
ones.

Counter identity, read in the clone at the measured revision:

```
$ sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

The digest equals the frozen counter's sha256 named in the context. The clone was never edited under
`verifiers/`; the counter's own second output line prints the same digest on both runs.

Diff of the control world against the freeze revision (the whole of it; no `verifiers/` change, no
snapshot file):

```
$ git diff --stat 67b68e0f9a0c48e5aa5ced63e6117cfca69da491..5e88a7413bc1580107231adba644884d34c235e1
 SKILL.md                               | 18 ++++++++++++++++++
 corpus/SOURCES.md                      |  6 ++++++
 corpus/knowledge/hook-files-round59.md | 16 ++++++++++++++++
 corpus/lessons/round-59.md             | 22 ++++++++++++++++++++++
 4 files changed, 62 insertions(+), 0 deletions(-)

$ git ls-tree -r --name-only 5e88a7413bc1580107231adba644884d34c235e1 | grep -c '^\.ufo/waves/round-59/snapshots/'
0
```

## The world, and the reader step it skips

The world is the six eligible clients' real census material, laid out exactly where the counter reads
it:

| Client | SKILL.md token (first backticked span) | Events cell | Entry source | Quote source | SOURCES sha256 copied from |
|---|---|---|---|---|---|
| Claude Code | `.claude/settings.json` | `SessionStart`, `PreToolUse` | S096 | `code.claude.com/docs/en/hooks.md:910` | `CensusClaudeCode.md` |
| Codex | `~/.codex/hooks.json` | `PreToolUse`, `SessionStart` | S097 | `learn.chatgpt.com/docs/hooks.md:44` block | `CensusCodex.md` |
| VS Code | `.github/hooks/audit.json` | `preToolUse`, `postToolUse` | S098 | `code.visualstudio.com/docs/agent-customization/hooks.md:77-82` | `CensusVSCode.md` |
| Copilot CLI | `~/.copilot/hooks/*.json` | `preToolUse`, `postToolUse` | S099 | `docs.github.com/en/copilot/concepts/customizations/hooks.md:28` | `CensusCopilotCLI.md` |
| Gemini CLI | `.gemini/settings.json` | `BeforeTool`, `AfterModel` | S100 | `geminicli.com/docs/hooks/best-practices.md:413` | `CensusGeminiCLI.md` |
| Cursor | `.cursor/hooks.json` | `preToolUse`, `postToolUse` | S101 | `cursor.com/docs/hooks.md:50` | `CensusCursor.md` |

- `SKILL.md` gains the `### Hook files by client` section with the frozen header
  `| Client | Hook config | Events | Action |` and one row per eligible client; `opencode` has no row
  (`Censusopencode.md` returns NOT ELIGIBLE: its hook code lives only in `.opencode/plugins/`, a banned
  segment word), so `K = 6`.
- `corpus/knowledge/hook-files-round59.md` holds the entry table `| Client | Hook config | Source | Quote |`,
  the same six tokens, one `S09x` id each, and the census quote for that page. The two multi-line
  census quotes (Codex's location list, VS Code's `Create ...` block) are rendered with spaces where
  the page has newlines, because a Markdown table cell is one line; the counter compares quotes
  whitespace-normalised (`gate_section`/`quote_in_gate`, `ws()` at `verifiers/check_hook_files.py:681`).
- `corpus/SOURCES.md` gains six new rows S096–S101 at the end of the registry table, each
  `docs | A | ... | mined | 2026-10-23 | 90d`, on that client's pinned host, and each printing a full
  64-hex sha256. Every sha256 was copied from the W0 census report of that page, never computed from
  committed bytes here:

  ```
  $ for s in <the six full 64-hex digests above>; do echo -n "${s:0:12} -> "; grep -l "$s" .ufo/waves/round-59/w0/Census*.md | tr '\n' ' '; echo; done
  c6ef9d211e8c -> CensusClaudeCode.md CensusCopilotCLI.md CensusVSCode.md
  57166ef03e70 -> CensusCodex.md CensusVSCode.md
  98c5be6b693a -> CensusCopilotCLI.md CensusVSCode.md
  23370e092d2e -> CensusCopilotCLI.md
  fb44fbcfaccc -> CensusGeminiCLI.md
  8436af768468 -> CensusCopilotCLI.md CensusCursor.md CensusVSCode.md
  ```
- `corpus/lessons/round-59.md` gains `## Gate` with one admitted bullet per row and that row's quote,
  byte-identical to the entry cell (the Gate check is whitespace-normalised).

**The control's one omission: no `.ufo/waves/round-59/snapshots/S###.page` is committed.** The work of
opening the page and saving its bytes was skipped; consequently the sha256 the counter compares against
each SOURCES row is a census value with no committed bytes behind it. There are no snapshot bytes at
the revision, so `git show <rev>:.ufo/waves/round-59/snapshots/S09x.page` returns absent for every row
and the pin cannot be satisfied by construction.

The world is otherwise complete on purpose: a preflight run of the same frozen counter's own `judge()`
over the built files with `snapshot_of=lambda sid: None` shows the missing snapshot is the **only**
reject reason per row (script `.preflight.py`, kept in the clone):

```
$ timeout 300 python3 -B .preflight.py
k (well-formed tokens): 6
backed: []
--- Claude Code token='.claude/settings.json' backed=False
   why: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page is missing at the revision
--- Codex token='~/.codex/hooks.json' backed=False
   why: entry row S097: snapshot .ufo/waves/round-59/snapshots/S097.page is missing at the revision
--- VS Code token='.github/hooks/audit.json' backed=False
   why: entry row S098: snapshot .ufo/waves/round-59/snapshots/S098.page is missing at the revision
--- Copilot CLI token='~/.copilot/hooks/*.json' backed=False
   why: entry row S099: snapshot .ufo/waves/round-59/snapshots/S099.page is missing at the revision
--- Gemini CLI token='.gemini/settings.json' backed=False
   why: entry row S100: snapshot .ufo/waves/round-59/snapshots/S100.page is missing at the revision
--- Cursor token='.cursor/hooks.json' backed=False
   why: entry row S101: snapshot .ufo/waves/round-59/snapshots/S101.page is missing at the revision
--- opencode token=None backed=False
   why: SKILL.md rows naming client: 0 (need exactly 1)
   why: no entry row names the client
```

So the token grammar, the foreign-name guard, E5, the Events cell, E4, the 6–25-word bound, the
token-at-boundary and hook-word-outside checks, the Gate quote, the new tier-A `mined` `2026-10-23`
docs row, the pinned host, the tracker/change-note rejection, the base-URL rejection and the full
64-hex sha256 pin all pass. The reader conjunct — pages opened, bytes saved, bytes committed, bytes
pinned — is the one the world does not perform, and it is the one that stops the row.

## Receipt

Command run in the clone, from `/fast/scratch/hyaku/kotoba-r59/CtlNoReader`:

```
timeout 900 python3 -B verifiers/check_hook_files.py --rev 5e88a7413bc1580107231adba644884d34c235e1 --fetch
```

Full stdout (7 reject lines; stderr empty, 0 bytes):

```
hook files backed on committed snapshots 0 of 6; found on the live page 0 of 6; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 5e88a7413bc1580107231adba644884d34c235e1
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page is missing at the revision
reject Codex: entry row S097: snapshot .ufo/waves/round-59/snapshots/S097.page is missing at the revision
reject VS Code: entry row S098: snapshot .ufo/waves/round-59/snapshots/S098.page is missing at the revision
reject Copilot CLI: entry row S099: snapshot .ufo/waves/round-59/snapshots/S099.page is missing at the revision
reject Gemini CLI: entry row S100: snapshot .ufo/waves/round-59/snapshots/S100.page is missing at the revision
reject Cursor: entry row S101: snapshot .ufo/waves/round-59/snapshots/S101.page is missing at the revision
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: **1**.

Second run, the same revision without `--fetch`:

```
timeout 900 python3 -B verifiers/check_hook_files.py --rev 5e88a7413bc1580107231adba644884d34c235e1
```

```
hook files backed on committed snapshots 0 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 5e88a7413bc1580107231adba644884d34c235e1
reject Claude Code: entry row S096: snapshot .ufo/waves/round-59/snapshots/S096.page is missing at the revision
reject Codex: entry row S097: snapshot .ufo/waves/round-59/snapshots/S097.page is missing at the revision
reject VS Code: entry row S098: snapshot .ufo/waves/round-59/snapshots/S098.page is missing at the revision
reject Copilot CLI: entry row S099: snapshot .ufo/waves/round-59/snapshots/S099.page is missing at the revision
reject Gemini CLI: entry row S100: snapshot .ufo/waves/round-59/snapshots/S100.page is missing at the revision
reject Cursor: entry row S101: snapshot .ufo/waves/round-59/snapshots/S101.page is missing at the revision
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit code: **1** (the non-fetch run is not the predicate; it exits 1 by rule). No `targets not frozen`
line appears, so both targets are frozen in the file actually run.

Predicate arithmetic: `S = 0`, `F = 0`, `G = 0`, `TARGET = 4`, `NEW_TARGET = 5`. `0 >= 4` is false
and `0 >= 5` is false, so `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)` is **NOT MET**.
A no-reader world does not satisfy C1.

## Fetches, tools, limits

- No HTTP request was made by this seat. The `--fetch` run fetches only backed rows
  (`main()` at `verifiers/check_hook_files.py:2388`: `for r in backed:`), and 0 rows were backed, so
  the run reached no client page and could not reach a bot challenge. Quotes and sha256 values come
  from the W0 census reports, which record the original fetches (`Census*.md`, 09:02–09:05Z).
- No tool was installed or upgraded (no pacman, uv, npm or cargo transaction).
- One `timeout 900`-capped process at a time; no background jobs, no pattern kills.
- Limits, stated plainly: this control measures that the frozen counter refuses a world that skipped
  the snapshot step while passing every other conjunct. It does not measure whether the six quotes are
  byte-exact on their live pages (census-reported, not re-verified here), and it does not test the
  `--fetch` live arm at all. [INFERENCE] Adding a committed `.page` whose bytes are the fetched page,
  with the row's sha256 equal to those bytes, is what would move such a world from 0 to backed; that
  world was not built here, because building it is the reader step this control exists to omit.
