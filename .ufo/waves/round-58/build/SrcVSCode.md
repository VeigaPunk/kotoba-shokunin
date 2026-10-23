Result: DONE — VS Code source evidence, the S091/C1 row drafts, and the frozen-counter quote probe are complete.

## Findings

- Re-opened `https://code.visualstudio.com/docs/agent-customization/prompt-files.md` with `curl -sSL`. The required `date -u` output was `Fri 23 Oct 2026 08:08:16 AM UTC`; HTTP status `200`; saved body `13,729` bytes; SHA-256 `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685`. The fetched copy is `/fast/scratch/hyaku/kotoba-r58/SrcVSCode/prompt-files.md`; lines 21–25 give the prompt-file scope and workspace location, lines 35–49 the format/frontmatter/body, and line 70 the input syntax.
- The W0 excerpt is replaced with a more directly scoped, contiguous excerpt at lines 21–25. It is 22 whitespace-separated words under the frozen counter (after removal of backticks), includes `.github/prompts` and `prompt` outside that token, and is not stitched or paraphrased. No source words/bytes are stripped. To store this raw Markdown table excerpt in single-line Markdown table cells, its literal `|` bytes are represented as `&#124;` and line breaks are collapsed to spaces; the counter's `page_plain()` unescapes HTML entities and collapses whitespace (`verifiers/check_command_files.py:824-829`). The exact encoded quote used below returned `True` in `found_on_page`.
- Source wording does not mark prompt files or `.github/prompts` deprecated/legacy. Searching the fetched page for `deprecated|legacy` found only line 44, where “deprecated” describes *existing tool-set references*; `legacy` does not occur. Line 17 says prompt files run only in Local Chat sessions and directs authors of reusable workflows for other harnesses to create an agent skill or convert a prompt file to a skill. This supports using a skill outside Local, not calling prompt files deprecated.
- The user-level location is described as user data for a VS Code profile, not as a filesystem path (lines 21, 26). The sourced token below is the workspace default `.github/prompts` (line 25).

## Counter evidence

Sandbox: `/fast/scratch/hyaku/kotoba-r58/SrcVSCode`; `git --no-optional-locks -C /fast/scratch/hyaku/kotoba-r58/SrcVSCode rev-parse HEAD` → `3de87aad29e960c95ed35840442f424c48c29729`.

In that clone, ran `timeout 90 python3 -B -c` importing `check_command_files` from `verifiers`, then calling `page = c.fetch(URL)` and `c.found_on_page(page, quote, '.github/prompts')` with the exact URL and encoded quote below. Exit `0`; stdout `True`; stderr empty. The quote's counter test was required; this is not a full C1 counter run.

```python
import sys
sys.path.insert(0, 'verifiers')
import check_command_files as c
page = c.fetch('https://code.visualstudio.com/docs/agent-customization/prompt-files.md')
print(c.found_on_page(page, 'that the Local harness uses for prompt files. &#124; Scope &#124; Default file location &#124; &#124;-------&#124;-----------------------&#124; &#124; Workspace &#124; `.github/prompts` folder &#124;', '.github/prompts'))
```

The frozen spec requires a 6–25-word quote (`verifiers/check_command_files.py:246-250`), and the quote check normalizes markup/whitespace as cited above. The frozen clone does not contain `corpus/knowledge/command-files-round58.md` or `corpus/lessons/round-58.md`; therefore no full judge or `--rev ... --fetch` counter run was made.

## Drafts (verbatim)

### SOURCES.md row

| S091 | Visual Studio Code — Use prompt files in VS Code — https://code.visualstudio.com/docs/agent-customization/prompt-files.md | docs | A | VS Code Local-harness prompt-file locations and authoring fields (vendor documentation, not a runtime test) | § Prompt file locations (`prompt-files.md:19-28`); § Prompt file format (`:33-49`); input syntax (`:69-70`); fetched 2026-10-23T08:08:16Z, HTTP 200, 13,729 B, sha256 `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` (seat SrcVSCode) | The Local workspace default is `.github/prompts`; prompt files are Markdown `.prompt.md` files with optional frontmatter, slash names default to filenames, and input hints/placeholders can guide or gather user context | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |

### `corpus/knowledge/command-files-round58.md` entry row

| VS Code | `.github/prompts` | S091 | "that the Local harness uses for prompt files. &#124; Scope &#124; Default file location &#124; &#124;-------&#124;-----------------------&#124; &#124; Workspace &#124; `.github/prompts` folder &#124;" |

### `SKILL.md` row

| VS Code | `.github/prompts` (workspace; user-level files are in VS Code profile data) | Markdown `.prompt.md` files (`"Prompt files are Markdown files with the `.prompt.md` extension."` — `prompt-files.md:35`); optional YAML frontmatter (`"The optional YAML frontmatter header configures the prompt's behavior:"` — `:35`) with optional `description`, `name`, `argument-hint`, `agent`, `model`, and `tools` (`:39-44`). `name` is used after `/` and defaults to the filename (`"The name of the prompt, used after typing `/` in chat. If not specified, the file name is used."` — `:40`); `argument-hint` guides chat input (`"Hint text shown in the chat input field to guide users on how to interact with the prompt."` — `:41`), while `${input:variableName}` / `${input:variableName:placeholder}` can request additional user information (`"You can also use a syntax like `${input:variableName}`, `${input:variableName:placeholder}`."` — `:70`). The body is Markdown prompt text (`"The body contains the prompt text in Markdown format."` — `:49). | Use an agent skill for reusable workflows outside Local. |

### `corpus/lessons/round-58.md` `## Gate` line

- S091 — https://code.visualstudio.com/docs/agent-customization/prompt-files.md; opened 2026-10-23; lines 21–25: "that the Local harness uses for prompt files. &#124; Scope &#124; Default file location &#124; &#124;-------&#124;-----------------------&#124; &#124; Workspace &#124; `.github/prompts` folder &#124;" (22 whitespace-separated words; pipe bytes entity-encoded in this single-line record).

## Gates, limits, and surfaces

- Gate evidence: the requested `fetch(url)` + `found_on_page(page, quote, token)` probe returned `True`. This proves the live page contains the quote and token under the frozen counter's normalization; it does not establish F, G, or the overall C1 predicate.
- Frozen census collision: W0 reports Copilot CLI's documentation also prints `.github/prompts` (`.ufo/waves/round-58/w0/CensusVSCode.md:58-62`); the frozen plan says the Copilot CLI row must have no backticked path to avoid E5 disqualifying both rows (`plans/round-58.md:60,67-68`). This report drafts only VS Code.
- No product/corpus files were edited. The only lane file written is `.ufo/waves/round-58/build/SrcVSCode.md`; the fetched page is in my sandbox clone. No tools were installed. C2 and the other routed work were out of scope.
