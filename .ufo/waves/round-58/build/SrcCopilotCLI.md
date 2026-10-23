Result: DONE — Drafted the Copilot CLI non-counted row, recorded S028 re-open evidence, and completed the Q30 sweep.

## Drafts (copy verbatim)

### `SKILL.md` row under `### Custom command files by client`

| Copilot CLI | No C1-countable standalone folder; uses Claude Code's .claude/commands/; plugin commands use com.github.copilot/commands/ | Skills override commands in the loading diagram (“then commands (.claude/commands/), skills override commands”, S028:456); Agent Plugins 1.0 limits the plugin path to that format (S028:154-164). | Leave non-counted: the shared standalone path is Claude Code's; the plugin namespace fails C1's dot-led and E7 path rules. |

The `Command files` cell deliberately contains no backticked span. The counter takes the first backticked span in that cell as the token (`verifiers/check_command_files.py:68-73`), so this row contributes no counted token. The plugin path is still recorded, not omitted: the docs place it in Agent Plugins 1.0 only (`cli-plugin-reference.md:154-164`), and the frozen C1 grammar rejects its non-dot-led first segment and interior dots (`check_command_files.py:90-115`).

### `corpus/lessons/round-58.md` § Gate — reopened base row

| S028 (re-opened; not a new row) | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 2026-10-23T08:08:39Z | HTTP 200; 47,200 B; sha256 `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` | “then commands (.claude/commands/), skills override commands” | `cli-plugin-reference.md:456` (contiguous substring; no bytes stripped) | SrcCopilotCLI |

Rows touched (old → new): S028 `recheck` `90d` → `2026-10-23`; no other S028 column changes. Its existing `opened` value remains `2026-10-22`; status and used-by remain as recorded.

## Findings and evidence

- `functions.grep(pattern="S028", path="/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md")` returned the S028 row at line 41. It is the GitHub Copilot CLI plugin reference at the URL above, tier A, mined, opened 2026-10-22, recheck `90d`. This is the existing base row, not a new source row.
- Re-opened S028 line 456 shows `then commands (.claude/commands/), skills override commands`; lines 154-164 identify `com.github.copilot/commands/` as the slash-command location in Agent Plugins 1.0 and state those locations apply only to that format. The CLI command reference separately says “Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`” and that the command name comes from the filename (`cli-command-reference.md:1334`). The W0 census identifies `.claude/commands/` as Claude Code's path and records the shared-path/foreign-marker disqualification (`.ufo/waves/round-58/w0/CensusCopilotCLI.md:30-42`).
- The fetched `~/.copilot` directory overview lists top-level items at `cli-config-dir-reference.md:11-35`; that list includes agents, extensions, instructions and skills, but no command or prompt directory. This is supporting evidence for the absence of a personal standalone folder, not proof about every possible user path.
- The frozen counter docstring says the token is the first backticked span in the `Command files` cell (`check_command_files.py:68-73`), and documents the disqualifications used above (`:104-121`). No counter or other lane code was executed.

## Q30 sweep

The Q30 scope here is the current GitHub Docs site, the Copilot CLI changelog, and the lane corpus. I used current served Markdown routes from `docs.github.com` as the permitted docs-site surface; I did not clone or search the full `github/docs` repository source tree.

### Changelog

Fetched `https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md` at `Fri Oct 23 08:08:39 AM UTC 2026`: HTTP 200, 289,859 bytes, sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`. Search for the candidate path/phrase patterns returned line 2932: `- Support `.claude/commands/` single-file commands as simpler alternative to skills`. No other candidate own command/prompt folder appeared in the searched changelog text.

### Current docs site

Fetched at `Fri Oct 23 08:08:39 AM UTC 2026`:

| URL | HTTP | bytes | sha256 |
|---|---:|---:|---|
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md` (S028) | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` (S031 page) | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |

Fetched at `Fri Oct 23 08:09:17 AM UTC 2026`:

| URL | HTTP | bytes | sha256 |
|---|---:|---:|---|
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md` | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md` | 200 | 10,057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | 200 | 8,730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md` | 200 | 8,379 | `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2` |
| `https://docs.github.com/en/copilot/tutorials/create-an-extension.md` | 200 | 21,012 | `6836b5a1b215a4a0a576a41fd458670186fc5055bfbb66178f5f5c7f7f43313d` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview.md` | 200 | 4,304 | `38f2e097044641c32451491df4bbe4b7e232969fe50558aa3bb4fda2ac79189b` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md` | 200 | 7,711 | `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64` |
| `https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations.md` | 200 | 17,525 | `b1c562f583a475e7bd61ac08816d480025e681fe7db73ced498390d8c6078ed9` |

The path search across these downloaded docs bodies found `.claude/commands/` in the CLI command reference (`:1334`) and the plugin-reference loading diagram (`:456`), and `com.github.copilot/commands/` in the plugin-reference table (`:159`). The latter is limited to Agent Plugins 1.0 (`:164`) and fails C1's frozen token grammar. The exact-pattern search found no `.github/prompts`, `.github/commands`, `.copilot/commands`, or `.copilot/prompts` path in these Copilot CLI docs. This is the docs-site sweep, not a claim that every GitHub Docs repository file was searched.

### Corpus search

Used the specialized `functions.grep` search over `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` (shell `grep` was not used):

- Pattern: `\.claude/commands|\.github/prompts|\.github/commands|\.copilot/commands|\.copilot/prompts|com\.github\.copilot/commands`
- Case: default sensitive; gitignore disabled.
- Result: one matching corpus file, `corpus/knowledge/instruction-surface-census-round13.md:102`, whose line attributes `.github/prompts/` to “VS Code Copilot prompt files.” No Copilot CLI-owned standalone command/prompt folder was recorded in that exact-path corpus search.

A second `functions.grep` query, `Copilot CLI|copilot-cli` (case-insensitive) across the corpus, returned existing Copilot CLI records including S028, the plugin-manifests entry, and the instruction-surface note; the exact path result above distinguishes the VS Code `.github/prompts/` record from Copilot CLI.

## Commands and results

Both curl batches were run with `timeout 900`, used `set -eu`, saved only to `/tmp/round58-srccopilotcli/`, printed `date -u`, HTTP status and downloaded byte count, then `sha256sum`. The tool output showed all listed requests completing with HTTP 200 and the hashes above; it did not print a separate process exit code.

First batch (the output began `Fri Oct 23 08:08:39 AM UTC 2026`):

```sh
timeout 900 bash -c 'set -eu; d=/tmp/round58-srccopilotcli; mkdir -p "$d"; date -u; curl -sSL -o "$d/cli-plugin-reference.md" -w "plugin HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md; sha256sum "$d/cli-plugin-reference.md"; curl -sSL -o "$d/cli-command-reference.md" -w "command HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md; sha256sum "$d/cli-command-reference.md"; curl -sSL -o "$d/changelog.md" -w "changelog HTTP %{http_code} bytes %{size_download}\n" https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md; sha256sum "$d/changelog.md"'
```

Second batch (the output began `Fri Oct 23 08:09:17 AM UTC 2026`):

```sh
timeout 900 bash -c 'set -eu; d=/tmp/round58-srccopilotcli; date -u; curl -sSL -o "$d/cli-config-dir-reference.md" -w "config HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md; sha256sum "$d/cli-config-dir-reference.md"; curl -sSL -o "$d/add-skills.md" -w "skills HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md; sha256sum "$d/add-skills.md"; curl -sSL -o "$d/add-custom-instructions.md" -w "instructions HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md; sha256sum "$d/add-custom-instructions.md"; curl -sSL -o "$d/create-custom-agents-for-cli.md" -w "agents HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md; sha256sum "$d/create-custom-agents-for-cli.md"; curl -sSL -o "$d/create-an-extension.md" -w "extension HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/tutorials/create-an-extension.md; sha256sum "$d/create-an-extension.md"; curl -sSL -o "$d/customization-overview.md" -w "overview HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview.md; sha256sum "$d/customization-overview.md"; curl -sSL -o "$d/plugins-creating.md" -w "plugins HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md; sha256sum "$d/plugins-creating.md"; curl -sSL -o "$d/comparing-customizations.md" -w "compare HTTP %{http_code} bytes %{size_download}\n" https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations.md; sha256sum "$d/comparing-customizations.md"'
```

## Scope and artifact paths

- Written lane file: `.ufo/waves/round-58/build/SrcCopilotCLI.md` (this report only). Product files, SOURCES.md, the lesson, and SKILL.md were not edited.
- External fetch artifacts: `/tmp/round58-srccopilotcli/`.
- Read-only census evidence: `.ufo/waves/round-58/w0/CensusCopilotCLI.md`.
- At inspection time, `corpus/knowledge/command-files-round58.md` and `corpus/lessons/round-58.md` did not exist yet (read returned path not found; lessons listing ended at round 57). The drafts above are ready for integration when those files are created.
- No tool installed or updated. No counter, tests, build, or lane code was run.
