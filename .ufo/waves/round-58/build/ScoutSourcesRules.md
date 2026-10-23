Result: MIXED — six census pages are new pinned docs URLs and do not raise W04; the Copilot CLI command-reference page is already a base SOURCES URL (S031, S038, S056).

Checked the seven page cells in `plans/round-58.md:55-63` (the census table inside § C1; there is no separate `## Census`). Cells are host/path plus a line anchor, not full URLs. Resolved as `https://` plus that path, dropping the `:line` anchor. The Copilot cell is prose (`docs.github.com command reference :1334`); the URL is the one `CensusCopilotCLI.md:13` ties to line 1334.

Base registry: `git --no-optional-locks show f56f6e191762c27c1aa2af11a204db9e2ca4edec:corpus/SOURCES.md` → 93473 bytes, sha256 `d461b723edc98ffdfe388c334f7da8bc1d97a952fa01a749de193b5d3ba45f70`, 88 rows, 69 `url_key`s. Keys, pins, and change-note tests are the functions in a scratch copy of `verifiers/check_command_files.py` (`url_key` :494-512, `base_url_keys` :515-523, rejection of the row's first URL at :724-730, `HOSTS` :257-274, `host_ok` :546-559, `url_is_change_note` :536-543). W04 is `scripts/sources-census.sh` `url_of` (:600-605: first `http(s)` URL, drop `#fragment`, drop one trailing `/`, lowercase the host only — does not drop `.md`, query, or `www.`) and the across-scope test (:643-645).

| Client | Census URL | `url_key` already a base row? | Host in that client's pin? | Path contains changelog/release/releases/news/blog? | W04 on this URL string? |
|---|---|---|---|---|---|
| Claude Code | `https://code.claude.com/docs/en/slash-commands.md` | No. Key `//code.claude.com/docs/en/slash-commands`. Not S022/S053/S065 (`//code.claude.com/docs/en/skills`). | Yes. Pin `code.claude.com`. | No. | No. |
| Codex | `https://learn.chatgpt.com/docs/custom-prompts.md` | No. Key `//learn.chatgpt.com/docs/custom-prompts`. | Yes. Pin `learn.chatgpt.com`. | No. | No. |
| VS Code | `https://code.visualstudio.com/docs/agent-customization/prompt-files.md` | No. Key `//code.visualstudio.com/docs/agent-customization/prompt-files`. | Yes. Pin `code.visualstudio.com`. | No. | No. |
| Copilot CLI | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` | Yes. `url_key` drops `.md`, so this equals `//docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference`, the first URL of S031 (`corpus/SOURCES.md:44`), S038 (`:51`), and S056 (`:69`). Re-citation rejected at `check_command_files.py:729-730`. | Yes. Pin `docs.github.com`. | No. `reference` is not `release`. | No for this `.md` string. Yes for the base spelling without `.md` (same `url_key`). |
| Gemini CLI | `https://geminicli.com/docs/cli/custom-commands.md` | No. Key `//geminicli.com/docs/cli/custom-commands`. Not S029 `//geminicli.com/docs/cli/skills`. | Yes. Pin `geminicli.com`. | No. | No. |
| Cursor | `https://cursor.com/docs/reference/deeplinks.md` | No. Key `//cursor.com/docs/reference/deeplinks`. Not S088 `//cursor.com/docs/reference/plugins`. | Yes. Pin `cursor.com`. | No. | No. |
| opencode | `https://opencode.ai/v2/docs/commands/` | No. Key `//opencode.ai/v2/docs/commands` (trailing `/` dropped). Not S064 `//opencode.ai/v2/docs/skills`. | Yes. Pin `opencode.ai`. | No. | No. |

W04 evidence (scratch only; lane `SOURCES.md` not edited):

- `timeout 60 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-23 --file /fast/scratch/hyaku/kotoba-r58/ScoutSourcesRules/corpus/SOURCES.md` → exit 1. Eight W04 lines. The only one on a census host/path is `file	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes`. S031 and S038 share one scope, so they do not warn; S056's scope differs. None of the other six census keys appear.
- Same command on `SOURCES-plus.md` (those seven URLs appended as S089–S095, each with its own new scope, plus probe S999 = the Copilot URL with `.md` removed) → exit 1. S089–S095 produced only `W03` (mined, used-by `—`). No `W04` for S092. S999 produced `file	W04	S999 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes`.

No tools installed or updated.
