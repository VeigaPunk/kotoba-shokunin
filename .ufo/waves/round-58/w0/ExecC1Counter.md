Result: DONE — the frozen C1 counter `verifiers/check_command_files.py` is built from v2, self-tests green (0 failures / 244 assertions), and at base `f56f6e19` prints its line then `targets not frozen` and exits 2 in both modes.

## Delivered

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/w0/check_command_files.py` — 1967 lines.
  sha256 `710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e`
  (byte-identical to the sandbox copy at `/fast/scratch/hyaku/kotoba-r58/ExecC1Counter/verifiers/check_command_files.py`, verified by `sha256sum` over both paths).
- Report: this file.

No lane file other than these two was written. Nothing was installed or upgraded (no tool/version change to record). No sandbox commit was made, so no sandbox hash is cited.

## What the counter implements

Adapted from `verifiers/check_plugin_manifests.py` v2; every v2 rule not named in the ticket is unchanged (SOURCES parsing, tier A, status `mined`, base-row-id and base-URL re-citation rejection with `url_key`, segment-exact `host_ok`, tracker/docs-kind/E3 rejection, E4 cell equality, E5 shared-token disqualification, E6 6–25 words, E7 non-final-dot rule, fetch limits/redirect checks, `## Gate` quote, `--json`).

Pinned here: `BASE = f56f6e191762c27c1aa2af11a204db9e2ca4edec`, `SKILL_HEADING = "### Custom command files by client"`, `SKILL_HEADER = ("client","command files","what a file sets","action")`, `ENTRY = corpus/knowledge/command-files-round58.md`, `ENTRY_HEADER = ("client","command files","source","quote")`, `LESSON = corpus/lessons/round-58.md`, `OPENED = ("2026-10-23",)`, `TARGET = NEW_TARGET = None`.

Grammar (`token_well_formed`, now one argument — the v2 own-marker exception is gone with the old grammar; the foreign-marker guard stays in `judge`): TOKEN_RE, then after stripping one leading `~/`/`./` and one trailing `/`: ≥ 2 segments, first segment dot-led, final non-empty segment (split on `-._`) holds command/commands/prompt/prompts case-insensitively, no segment (split on `-._`) equals skill/skills/agent/agents/rule/rules/plugin/plugins/extension/extensions, no dot in a non-final segment except as its first character; directory tokens and final-segment globs are allowed. v2's `marketplace` exclusion was dropped together with the old grammar.

Quote side: `token_span` now finds the raw or normalised token only at a path-segment boundary (new `first_boundary`, shared with `token_at_boundary`), and `command_word_outside` requires `(?i)\b(commands?|prompts?)\b` outside that span.

Output: `custom command files found on the live page F of K; new ground G` with `--fetch`; `custom command files backed B of K; new ground not computed (needs --fetch)` without. With `TARGET`/`NEW_TARGET` still `None` the run prints `targets not frozen` after that line (and after the per-client `reject`/`BACKED` lines) and exits 2. With targets set: exit 0 iff `--fetch` and F ≥ TARGET and G ≥ NEW_TARGET, else 1; non-fetch runs still exit 1; 2 for could-not-evaluate.

## Runs (sandbox clone at base f56f6e19; `date -u` = Fri 23 Oct 2026 07:49:18 AM UTC)

```
$ timeout 600 python3 -B verifiers/check_command_files.py --self-test
counter sha256 710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e
self-test: 0 failure(s) over 244 assertions
SELFTEST_EXIT=0
```

```
$ timeout 600 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
counter sha256 710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
targets not frozen
NONFETCH_EXIT=2
```

```
$ timeout 600 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
counter sha256 710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
targets not frozen
FETCH_EXIT=2
```

(The `--fetch` run touched no network: with 0 backed clients no page is fetched, and `held_in_base` returns early on an empty token set.)

`python3 -m py_compile verifiers/check_command_files.py` → exit 0.

Delivered bytes re-run from an unrelated cwd (`/tmp`), so `lane_dir()` falls back to the lane and the file is proven self-locating:

```
$ timeout 600 python3 -B .../.ufo/waves/round-58/w0/check_command_files.py --self-test
counter sha256 710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e
self-test: 0 failure(s) over 244 assertions
DELIVERED_SELFTEST_EXIT=0
$ timeout 300 python3 -B .../.ufo/waves/round-58/w0/check_command_files.py --rev f56f6e19... --fetch
counter sha256 710e050b238a312c1388c5c6c5b5b3a9bbbbccd514737a3a25ae04466d54916e
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files found on the live page 0 of 0; new ground 0
targets not frozen
PIPE=2
```

## Self-test coverage (244 assertions)

- Grammar, red and green per conjunct: TOKEN_RE shape (space, empty middle segment, `@`, leading slash); ≥ 2 segments after stripping (`commands`, `./commands`, `~/prompts`, `.claude`); first segment dot-led (`commands/prompts`, `claude/commands`); final-segment command/prompt word (`.claude/other/`, `.claude/commanders/`, `.claude/commands/plan.md`); forbidden segment words (`.claude/skills/commands/`, `.claude/agents/commands/`, `.cursor/rules/commands/`, `.claude-plugin/commands/`, `.vscode/extensions/commands/`, `agent-tools`, `prompt-rules`) with greens (`.claude/agentic/commands/`); E7 (`1.0`, `opencode.ai/docs/commands/`) with green (`.github/.prompts/commands/`); directory tokens, `~/`/`./` prefixes, final-segment glob `.github/prompts/*.prompt.md`, case-insensitive word. Conjuncts that only permit (directory token, final-segment glob) carry a green arm only — there is no legitimate red for them.
- Backing conjuncts: unique row, malformed token leaving K, action ≥ 3 words, foreign marker, E5 (cross-client share, casefold share, unlisted-client row, same-client duplicate), E4 (differing/backticked/`./` raw/case-differing/empty cell), quote 2/5/6/25-token/26 words, token absent, token case difference, command word only inside the token, boundary-only token spans, S### at base, base URL and path-case alias, docs/tier/status/opened, off-host, tracker, E3 changelog + report text, missing URL, malformed SOURCES row, entry source not S###, empty quote cell, no entry row, and the header/heading readers.
- R4 end-to-end: a throw-away git repo with base and measured commits (SKILL.md section, entry, SOURCES rows, lesson Gate), the fetch stubbed with page bytes and targets patched to 2/2 — `main()` exits 0 and prints exactly `custom command files found on the live page 2 of 2; new ground 2`; the same world with the Gate quote broken exits 1 and prints exactly `... 1 of 2; new ground 1`; with the targets back at `None` it exits 2 and prints `targets not frozen`.

## Risks / judgement calls for the L1

1. Ticket wording conflict: the `Change` bullet fixes the non-fetch line as the v2 wording adapted, while the expected `--rev f56f...` observation says `found ... 0 of 0; new ground 0`. Both are honoured — the non-fetch run prints `custom command files backed 0 of 0; new ground not computed (needs --fetch)` and the `--fetch` run prints the fetch-style line; both end in `targets not frozen`, exit 2.
2. `targets not frozen` is printed after the per-client `reject`/`BACKED` diagnostics, not immediately below the summary line (v2's ordering kept); the report evidence above shows the exact stream.
3. E4 and directory tokens: `normalise()` strips one trailing `/`, so a `./`-prefixed SKILL token only matches a cell written with the raw `./` form; a cell with the bare normalised path is rejected. That is the frozen E4 rule applied to directory tokens and is pinned by a self-test arm.
4. The quote-side token match is now boundary-checked (per ticket); a quote that embeds the token mid-segment no longer counts.
5. `*` in a non-first segment still passes the v2 path regex; only the final-segment glob is named by the ticket, and the regex is the frozen path grammar, so no extra restriction was added.

No blockers.
