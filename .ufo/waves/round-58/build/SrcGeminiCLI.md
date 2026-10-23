Result: DONE — Gemini CLI source evidence and S093 depth-row drafts are ready; the frozen page matcher returned True.

## Findings

- Re-opened the vendor documentation at `https://geminicli.com/docs/cli/custom-commands.md` with `curl -sSL` on 2026-10-23. `date -u` output: `Fri Oct 23 08:08:24 AM UTC 2026`; HTTP 200; 12,129 bytes; SHA-256 `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872`; 330 lines. The fetched Markdown is the page content used below.
- Best unshaped quote, at `custom-commands.md:12-13` (18 whitespace-delimited words after the counter strips backticks): `1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on.` It contains the token and `commands` outside the token. The source line break and four continuation-indent spaces between `commands` and `are` are folded to one space; no Markdown list/bold markers or other source bytes are stripped.
- The docs place global commands at `~/.gemini/commands/` and project commands at `<your-project-root>/.gemini/commands/` (`:12-17`), state project commands take precedence on same-name collisions (`:19-21`), and describe TOML `.toml` files with a required `prompt` and optional `description` (`:39-56`). A command name derives from its path under `commands`; nested paths become colon namespaces (`:25-32`). The `{{args}}` placeholder substitutes text typed after the command name (`:66-67`).
- The page does not call this form deprecated or legacy and does not point to a replacement. It labels its section `TOML file format (v1)` (`:39`) and says command definitions must use TOML and the `.toml` extension (`:41-42`). A case-insensitive page search for `deprecated|legacy|migrat|TOML file format|v2|slash command` found the v1 section, not a deprecation or migration direction.

## Frozen matcher gate

Sandbox clone command and result:

```sh
timeout 900s sh -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/SrcGeminiCLI && git -C /fast/scratch/hyaku/kotoba-r58/SrcGeminiCLI checkout -q 3de87aad29e960c95ed35840442f424c48c29729'; printf 'exit=%s\n' "$?"
```

Observed output: `exit=0`.

Required direct `fetch(url)` + `found_on_page(page, quote, token)` invocation, run from `/fast/scratch/hyaku/kotoba-r58/SrcGeminiCLI` against the frozen checkout:

```sh
timeout 900s python3 -B -c 'import importlib.util; p="/fast/scratch/hyaku/kotoba-r58/SrcGeminiCLI/verifiers/check_command_files.py"; s=importlib.util.spec_from_file_location("check_command_files", p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); u="https://geminicli.com/docs/cli/custom-commands.md"; q="1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on."; page=m.fetch(u); print(m.found_on_page(page, q, "~/.gemini/commands/"))'
```

Observed stdout: `True`; the call returned successfully (exit 0). This proves only that the counter helper's fetched page holds this quote and token. It is not a full counter run or a C1 predicate result.

Direct fetch command (the temporary file was removed by its EXIT trap):

```sh
timeout 900s sh -c 'date -u; f=$(mktemp); trap "rm -f \"$f\"" EXIT; curl -sSL -o "$f" -w "HTTP %{http_code} bytes %{size_download} final %{url_effective}\\n" https://geminicli.com/docs/cli/custom-commands.md; wc -c "$f"; sha256sum "$f"; printf "line-count "; wc -l < "$f"; printf "html-quote-candidates "; python3 -c "from pathlib import Path; p=Path(\"$f\").read_bytes(); print(p[:512].decode(\"utf-8\",\"replace\"))"'
```

Observed: date above; `HTTP 200 bytes 12129 final https://geminicli.com/docs/cli/custom-commands.md`; `12129 /tmp/tmp.IpuJXsXYr8`; SHA-256 above; `line-count 330`. The first 512 bytes begin `# Custom commands` and contain the page prose, confirming the downloaded response is Markdown, not a transformed HTML page.

## Drafts for integration

SOURCES row (single Markdown table line; contract column order):

```markdown
| S093 | Gemini CLI docs — Custom commands — https://geminicli.com/docs/cli/custom-commands.md | docs | A | Gemini CLI's documented user/project custom-command locations, TOML schema, naming and argument behavior (vendor documentation; not a runtime test) | § File locations and precedence (`custom-commands.md:8-17`); § Naming and namespacing (`:23-32`); § TOML file format (`:39-56`); § Handling arguments (`:58-67`); fetched 2026-10-23T08:08:24Z, HTTP 200, 12,129 B, sha256 `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` | Gemini CLI documents user commands under `~/.gemini/commands/` and project commands under `<your-project-root>/.gemini/commands/`; TOML files map relative paths to slash commands and define prompts with optional descriptions and argument handling | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |
```

Knowledge entry row:

```markdown
| Gemini CLI | `~/.gemini/commands/` | S093 | "1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on." |
```

SKILL.md row (the table header remains `| Client | Command files | What a file sets | Action |`):

```markdown
| Gemini CLI | `~/.gemini/commands/` (user); `<your-project-root>/.gemini/commands/` (project) | TOML `.toml` command definitions with a required `prompt` and optional `description`; command names derive from file paths under `commands/`, with nested paths becoming colon namespaces; `{{args}}` in `prompt` substitutes text entered after the command name. Supporting quotes: “Your command definition files must be written in the TOML format and use the `.toml` file extension” (`custom-commands.md:41-42`); “The name of a command is determined by its file path relative to its `commands` directory” and “Subdirectories are used to create namespaced commands” (`:25-27`); “`prompt` (String): The prompt that will be sent to the Gemini model when the command is executed” (`:46-47`); “`description` (String): A brief, one-line description of what the command does” (`:52-53`); “If your `prompt` contains the special placeholder `{{args}}`, the CLI will replace that placeholder with the text the user typed after the command name” (`:66-67`). | Tell readers where commands live and how arguments flow. |
```

Gate line (quote and line retained for the counter; fetch metadata included):

```markdown
- S093 — https://geminicli.com/docs/cli/custom-commands.md — accessed 2026-10-23T08:08:24Z; quote: “1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on.” (`custom-commands.md:12-13`); HTTP 200, 12,129 B, sha256 `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872`.
```

## Touched surfaces, limits, and out of scope

- Lane product files were not edited. The only lane file written is this report: `.ufo/waves/round-58/build/SrcGeminiCLI.md`. The sandbox clone is `/fast/scratch/hyaku/kotoba-r58/SrcGeminiCLI`; the curl temporary file was removed by the command's trap. No tools were installed or updated.
- At inspection time, the lane had no `corpus/knowledge/command-files-round58.md` or `corpus/lessons/round-58.md` to edit (the reads returned not found); the observed SOURCES registry ended at S088. These are integration drafts, not landed corpus rows or a complete C1 result.
- Not run: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` as a full judge, any full C1 predicate measurement, or other clients' build work. The helper test is the specifically requested page/quote check only. C2 is withdrawn per the frozen assignment and was not examined here.

## Artifact path

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/build/SrcGeminiCLI.md`
