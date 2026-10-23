Result: DONE — at base `f56f6e191762`, four eligible census tokens are unheld and two are held, so expected G is 4 if those six rows are found.

Base `f56f6e191762c27c1aa2af11a204db9e2ca4edec`. `git version 2.56.0`. Each row is `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF <t> f56f6e191762c27c1aa2af11a204db9e2ca4edec -- . ':!.ufo'`. Exit 1 with empty stdout is git's no-match code, not a git failure. `-i` folds case, so each case variant returned the same count and the same path as its lowercase form.

Case variants run for every token: segment capitals (`.Claude/Commands`, `.Codex/Prompts`, `.Github/Prompts`, `.Gemini/Commands`, `.Cursor/Commands`, `.Opencode/Commands`, `.Config/Opencode/Commands`) and all-caps (`.CLAUDE/COMMANDS`, `.CODEX/PROMPTS`, `.GITHUB/PROMPTS`, `.GEMINI/COMMANDS`, `.CURSOR/COMMANDS`, `.OPENCODE/COMMANDS`, `.CONFIG/OPENCODE/COMMANDS`).

| token (and both case variants) | exit | count | hit paths |
|---|---|---|---|
| `.claude/commands` | 1 | 0 | — |
| `.codex/prompts` | 0 | 1 | `corpus/knowledge/instruction-surface-census-round13.md` |
| `.github/prompts` | 0 | 1 | `corpus/knowledge/instruction-surface-census-round13.md` |
| `.gemini/commands` | 1 | 0 | — |
| `.cursor/commands` | 1 | 0 | — |
| `.opencode/commands` | 1 | 0 | — |
| `.config/opencode/commands` | 1 | 0 | — |

The two hits are outside `.ufo/`. `git show f56f6e19:corpus/knowledge/instruction-surface-census-round13.md` lines 102–103:

```
| `omp:github/prompts` | prompts | loader-literal | Cross-tool rule files | "Load `*.prompt.md` from `.github/prompts/` (VS Code Copilot prompt files)" |
| `omp:codex/prompts` | prompts | loader-literal | Cross-tool rule files | "Load prompts from `~/.codex/prompts` and `.codex/prompts/`" |
```

## Held rule

`verifiers/check_command_files.py` `new_ground` (`:1079-1085`) counts distinct `casefold(normalise(token))` among the found clients for which `held.get(token)` is false. `held` is keyed by the case-preserved normalised token. `held_in_text` (`:999-1018`) casefolds the token and the line, then accepts a match whose previous character is start-of-line, whitespace, or one of `` `"'([</~= `` (`HELD_PREV`, `:303`), and whose next character passes `held_right_ok` (`:1021-1030`): end of line, or not a letter, digit, `_` or `-`, and not `.` followed by a letter or digit. `held_in_base` (`:943-964`, `:1033-1056`) reads blobs via `git ls-tree -r -z` + `git cat-file --batch`, skips a blob that contains NUL, and never reads a path equal to `.ufo` or starting with `.ufo/`. A case variant is the same key and the same held answer (`:171-181`, `:1079-1085`).

Boundary on the two lines (both pass, so both tokens are held):

- `.github/prompts` in `` `.github/prompts/` ``: previous byte is `` ` `` (`HELD_PREV`); next byte is `/`, which is not a word character and not `.`+alnum.
- `~/.codex/prompts`: previous byte is `/` (`HELD_PREV`); next byte is `` ` ``.
- `` `.codex/prompts/` ``: previous byte is `` ` ``; next byte is `/`.

`omp:github/prompts` and `omp:codex/prompts` on the same lines do not contain the leading dot, so they are not matches.

## Expected G

Census tokens, normalised (strip one leading `~/` or `./` and one trailing `/`; census reports under `.ufo/waves/round-58/w0/Census*.md`). Copilot CLI has no eligible token.

| client | printed token | `normalise` | held outside `.ufo/` |
|---|---|---|---|
| Claude Code | `.claude/commands/` | `.claude/commands` | no |
| Codex | `~/.codex/prompts/` | `.codex/prompts` | yes |
| VS Code | `.github/prompts` | `.github/prompts` | yes |
| Gemini CLI | `~/.gemini/commands/` | `.gemini/commands` | no |
| Cursor | `.cursor/commands` | `.cursor/commands` | no |
| opencode | `.opencode/commands/` | `.opencode/commands` | no |

The six casefold keys are distinct. If all six eligible clients are found on those tokens, `new_ground` is **4** (Claude Code, Gemini CLI, Cursor, opencode). Codex and VS Code add 0. Case variants do not add a key and do not flip held.

`~/.config/opencode/commands/` (`Censusopencode.md`) normalises to `.config/opencode/commands`, which this grep also finds 0 times outside `.ufo/`. It is not the counted census row. Using it instead of `.opencode/commands` would still be one unheld opencode key, so G would stay 4.

## `.ufo/` is why three tokens stay unheld

The same `git grep -ilF` without `:!.ufo` finds copies the counter must ignore. All of them are under `.ufo/`; the assigned pathspec and `held_in_base` both drop them.

| token | files in the whole tree | of which under `.ufo/` | outside `.ufo/` |
|---|---|---|---|
| `.claude/commands` | 2 | 2 | 0 |
| `.opencode/commands` | 1 | 1 | 0 |
| `.config/opencode/commands` | 1 | 1 | 0 |
| `.gemini/commands` | 0 | 0 | 0 |
| `.cursor/commands` | 0 | 0 | 0 |
| `.codex/prompts` | 12 | 11 | 1 |
| `.github/prompts` | 10 | 9 | 1 |

`.ufo/` paths for the three unheld tokens that do occur there: `.claude/commands` in `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` and `.ufo/waves/round-56/build/ScoutChangelogSweep.md`; `.opencode/commands` and `.config/opencode/commands` only in `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`. Those blobs are not held occurrences. Counting them would mark Claude Code and opencode held and drop G from 4 to 2, below `NEW_TARGET` 3. Under the counter's rule they do not count.

No lane file was edited. No counter was executed. The boundary calls above are read off `held_in_text` / `held_right_ok` against the two shown lines, not a run of `held_in_base`.
