Result: HOLDS — none of the six eligible census tokens is held in the base tree outside `.ufo`, so `held_in_base` would mark each normalised token new ground.

Recount of the frozen census tokens (`plans/round-59.md` lines 65–72) at `a975cbbf00534443c49bf02e29c813a3db0bf0f8`. opencode has no eligible token (line 73) and is not in this count. No tool was installed.

## What the counter actually searches

`held_in_base` (`verifiers/check_hook_files.py` lines 1211–1227) is called only for found rows, with `r["norm"]` (lines 2401–2409). `norm` is `normalise(token)` (lines 899, 934): strip one leading `~/` or `./` and one trailing `/`; case is kept (lines 633–644). The hit test is `held_in_text` (lines 1170–1201): Python `casefold()` on the token and on each line, then a path-segment boundary. Left: start of line, whitespace, or one of `` `"'([</~= `` (`HELD_PREV`, line 313). Right: end of line, or not a letter, digit, `_` or `-`, and not `.` followed by an ASCII letter or digit (`HELD_NEXT_BAD`, line 314). A NUL blob is skipped (lines 1204–1207). Paths `.ufo` and `.ufo/*` are not read (lines 1131–1133). `new_ground` (lines 1254–1260) counts distinct `casefold(norm)` values among found rows whose `held` bit is false. Without a found row, G stays 0 even when every token is unheld (lines 2398–2409).

Two consequences for the spellings below. A line that only has `~/.codex/hooks.json` still holds the search key `.codex/hooks.json`, because the character before `.codex` is `/`, which is in `HELD_PREV`. A line that only has `.cursor/hooks.json/` still holds `.cursor/hooks.json`, because `/` is a legal right boundary. The `*` in `.github/hooks/*.json` is a literal character (`str.find`, and `git grep -F`); `.github/hooks/audit.json` does not hold it.

## Method

Tree population, read-only, `date -u` `Fri 23 Oct 2026 09:36:17 AM UTC`: `git ls-tree -r --full-tree a975cbbf00534443c49bf02e29c813a3db0bf0f8` → 11694 entries, 11163 under `.ufo`, 531 outside. Of those 531, 531 are blobs (no gitlink) and 1 is binary (`verifiers/fixtures/pins/mini.bin`, 93 bytes, one NUL). No `.gitattributes` at this revision (`git cat-file -e` exit 128), so git grep is not skipping text via an attribute. git 2.56.0.

Own count: `git --no-optional-locks -C <lane> grep -i -l -F -e <literal> a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo'`, then a boundary check written to the rules above and checked against the counter's own examples (exact line, case change, long s U+017F, letter/digit/`_`/`-` suffix, dot-before-alnum, trailing slash, `~/` prefix, literal `*` versus `.github/hooks/audit.json`): 0 failures of 32. Comparison arm: the same check over all 530 non-NUL blobs via `ls-tree -z` + `cat-file --batch`, which is `held_in_base`'s population, including Python `casefold` (so a long-s spelling git's `-i` might miss would still show up). Script: `/fast/scratch/hyaku/kotoba-r59/ScoutHeldGround/recount.py`. Run `Fri 23 Oct 2026 09:37Z`, exit 0.

Every git grep below exited 1 with empty stdout and empty stderr (git's "no match"). The casefold scan found the same files: none. `in_scan_not_grep` and `in_grep_not_scan` were empty for every spelling, so the two methods do not disagree on this tree.

`mini.bin` does not contain any of the six search keys, nor the substrings `hooks.json` or `settings.json`. Skipping it changes nothing.

## Per token

Search key is the normalised form, the string `held_in_base` would be given. "Boundary files" are git-grep hits that also pass the boundary check. There were no grep hits, so the boundary check rejected nothing.

| Client | Printed census token | Search key (`normalise`) | grep -il -F files | Boundary files | Casefold scan files | `held_in_base` | New ground if the row is found |
|---|---|---|---|---|---|---|---|
| Claude Code | `.claude/settings.json` | `.claude/settings.json` | 0 | 0 | 0 | False | yes |
| Codex | `~/.codex/hooks.json` | `.codex/hooks.json` | 0 | 0 | 0 | False | yes |
| VS Code | `.github/hooks/*.json` | `.github/hooks/*.json` | 0 | 0 | 0 | False | yes |
| Copilot CLI | `~/.copilot/hooks/*.json` | `.copilot/hooks/*.json` | 0 | 0 | 0 | False | yes |
| Gemini CLI | `.gemini/settings.json` | `.gemini/settings.json` | 0 | 0 | 0 | False | yes |
| Cursor | `.cursor/hooks.json` | `.cursor/hooks.json` | 0 | 0 | 0 | False | yes |

The six `casefold(norm)` values are distinct (6 of 6). Six found rows would make G = 6. That matches the frozen census (`G_max = 6`, every eligible token 0 hits).

Files for every row: none.

## Normalised spellings that are not the search key

Also grepped, same command, each exit 1, 0 files; the casefold scan also 0. These are not what `held_in_base` looks up, except where noted.

| Client | Spelling | Why it was checked | Files |
|---|---|---|---|
| Claude Code | `.claude/settings.json/` | trailing `/` (counter strips one before searching; a hit here would still hold the key) | 0 |
| Claude Code | `~/.claude/settings.json` | leading `~/` (a hit here holds the key, left char `/`) | 0 |
| Codex | `~/.codex/hooks.json` | printed form; longer than the search key | 0 |
| Codex | `.codex/hooks.json/` | trailing `/` | 0 |
| VS Code | `.github/hooks/*.json/` | trailing `/` on the literal glob | 0 |
| VS Code | `~/.github/hooks/*.json` | leading `~/` on the literal glob | 0 |
| VS Code | `.github/hooks/audit.json` | the census seat's example file; not the frozen token, and not a match for the literal `*` | 0 |
| VS Code | `.github/hooks` | directory prefix of the glob, casefold scan | 0 |
| Copilot CLI | `~/.copilot/hooks/*.json` | printed form | 0 |
| Copilot CLI | `.copilot/hooks/*.json/` | trailing `/` | 0 |
| Gemini CLI | `.gemini/settings.json/` | trailing `/` | 0 |
| Gemini CLI | `~/.gemini/settings.json` | leading `~/` | 0 |
| Cursor | `.cursor/hooks.json/` | trailing `/` | 0 |
| Cursor | `~/.cursor/hooks.json` | leading `~/` | 0 |

`./` never appears on these tokens. `normalise` would strip one leading `./` the same way it strips `~/` (counter self-test, lines 1431–1432). No census token has that prefix, so there was no separate `./` literal to count.

## Near misses that are not these tokens

The parent directories do occur. They are other file kinds, and the hook-file string is not a substring of them, so neither git grep nor `held_in_text` counts them. Counts are a casefold substring scan of the 530 text blobs, not boundary hits.

- `.claude/` in 37 files. Example `LOG.md:446`: `` `n = [<config>/AGENTS.md, ~/.claude/CLAUDE.md]` ``. Not `.claude/settings.json`.
- `.codex/` in 18 files. Example `LOG.md:484`: `` `~/.codex/AGENTS.md` ``. Not `.codex/hooks.json`.
- `.copilot/` in 9 files. Example `SKILL.md:87`: `` `~/.copilot/agents` ``. Not `.copilot/hooks/*.json`.
- `.gemini/` in 17 files. Example `LOG.md:2506`: `.gemini/commands` had zero base hits in the round-58 census. Not `.gemini/settings.json`.
- `.cursor/` in 19 files. Same `LOG.md:2506` line names `.cursor/commands`. Not `.cursor/hooks.json`.
- `.github/hooks` in 0 files.
- The substring `hooks/*.json` in 0 files.
- Bare `settings.json` in 5 files, none of them the census path. `SKILL.md:89` is the Gemini agents flag `` `experimental.enableAgents: false` in `settings.json` ``. `verifiers/verify_surfaces.py:62` names `` `omp:gemini/settings.json` ``, a different path (no `.gemini/` segment).
- Bare `hooks.json` in 3 files, all the plugin path `hooks/hooks.json`, whose first segment is `hooks`, not a dot-directory. `SKILL.md:103` and `corpus/knowledge/plugin-manifests-round57.md:58` (Gemini extensions); `plugin-manifests-round57.md:59` (Cursor plugin discovery of `hooks/hooks.json`). That string does not contain `.cursor/hooks.json` or `.github/hooks/*.json`.

## Agreement with the counter

For each search key, `held_in_base` would return False. `new_ground` would count it once the row is found. Nothing in the normalised spellings (stripped `~/`, trailing `/`, literal `*.json`) turns a False into a True on this tree. The census pre-count (`git grep -ilF … | wc -l` = 0, plan line 75) used the same git flags and the same pathspec; the boundary check adds no file and removes no file, because the substring is absent.

Confidence: high. The blob set was enumerated the way `ls_tree_blobs` enumerates it, and both the prescribed git grep and a casefold scan of those blobs were empty.

Unresolved: none for these six tokens. G on a real `--fetch` run still depends on which rows are found; this recount only fixes the held bit.
