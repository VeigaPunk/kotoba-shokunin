Result: DONE — Re-opened the Codex custom-prompts page, selected a verbatim quote accepted by the frozen page predicate, and drafted S090 plus the C1 entry, SKILL.md, and Gate rows.

## Re-open and predicate evidence

- Re-opened `https://learn.chatgpt.com/docs/custom-prompts.md` with:
  ```sh
  timeout 90s bash -c 'date -u; curl -sSL --max-time 60 -o /tmp/kotoba-r58-codex-custom-prompts.md -w "HTTP %{http_code}\n" https://learn.chatgpt.com/docs/custom-prompts.md; wc -c < /tmp/kotoba-r58-codex-custom-prompts.md; sha256sum /tmp/kotoba-r58-codex-custom-prompts.md'
  ```
  Output:
  ```text
  Fri Oct 23 08:07:59 AM UTC 2026
  HTTP 200
  3357
  d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9  /tmp/kotoba-r58-codex-custom-prompts.md
  ```
- Chosen quote, verbatim and unshaped from `custom-prompts.md:62`: “Manage prompts by editing or deleting files under `~/.codex/prompts/`.” It is 9 whitespace-delimited words; `prompts` is outside the token. No bytes were stripped. The complete sentence directly relates managing prompts to the candidate directory.
- The page marks Custom prompts as deprecated at lines 5 and 8, and points readers to Agent Skills at `https://learn.chatgpt.com/docs/build-skills` (lines 5–6 and 10). It calls this form “deprecated”; it does not call it “legacy.”
- Created an isolated sandbox and checked out the requested freeze revision with:
  ```sh
  timeout 900s bash -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/SrcCodex && git -C /fast/scratch/hyaku/kotoba-r58/SrcCodex checkout -q 3de87aad29e960c95ed35840442f424c48c29729'
  ```
  It returned without output or error.
- In that clone, imported `verifiers/check_command_files.py`, called `fetch(url)` and `found_on_page(page, quote, token)` on the exact URL and quote:
  ```sh
  timeout 90s python3 -B -c 'from verifiers import check_command_files as m; url="https://learn.chatgpt.com/docs/custom-prompts.md"; quote="Manage prompts by editing or deleting files under `~/.codex/prompts/`."; page=m.fetch(url); print(m.found_on_page(page, quote, "~/.codex/prompts/"))'
  ```
  Output: `True`.

## Drafts for integration

SOURCES row (S090; one table line):

| S090 | OpenAI Learn — Custom prompts — https://learn.chatgpt.com/docs/custom-prompts.md | docs | A | Codex custom prompt files: user-level location, Markdown format, slash-command invocation, metadata, and arguments (documentation claim, not runtime behavior) | § Custom Prompts (`custom-prompts.md:5-10`); create prompt (`:12-23`); expected invocation (`:32-34`); metadata and arguments (`:36-46`); manage commands (`:48-62`); fetched 2026-10-23T08:07:59Z, HTTP 200, 3,357 B, sha256 `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` | The page documents user-local Markdown prompt files, an example slash-command invocation, YAML metadata and argument placeholders; it marks custom prompts deprecated and directs authors to Agent Skills for reusable guidance | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |

Knowledge entry row:

| Codex | `~/.codex/prompts/` | S090 | "Manage prompts by editing or deleting files under `~/.codex/prompts/`." |

SKILL.md row (supporting quotes and source line pointers are included in the “What a file sets” cell):

| Codex | `~/.codex/prompts/` (user scope; not shared through the repository, `custom-prompts.md:10`) | Markdown prompt files (“turn Markdown files into reusable prompts”, `custom-prompts.md:8`); filename/invocation example (“Create `~/.codex/prompts/draftpr.md` with reusable guidance”, `:18`; “Typing `/prompts:draftpr` in the slash command menu shows your custom command”, `:34`); YAML frontmatter sets `description` (“Set it in YAML front matter as `description:`”, `:40`) and `argument-hint` (“Document expected parameters with `argument-hint: KEY=<value>`”, `:41`); positional placeholders (“$1 through $9 expand from space-separated arguments you provide after the command. $ARGUMENTS includes them all”, `:42`) and named placeholders (“Use uppercase names like `$FILE` or `$TICKET_ID` and supply values as `KEY=value`”, `:43`) | Use Agent Skills for new reusable guidance. |

Gate line:

S090 — https://learn.chatgpt.com/docs/custom-prompts.md; fetched 2026-10-23T08:07:59Z (HTTP 200, 3,357 B, sha256 `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9`); `custom-prompts.md:62`: “Manage prompts by editing or deleting files under `~/.codex/prompts/`.”

## Surfaces, limits, and provenance

- Touched lane surface: only this report, `.ufo/waves/round-58/build/SrcCodex.md`. No product, corpus, or verifier files were edited. The source response was saved at `/tmp/kotoba-r58-codex-custom-prompts.md`; the sandbox clone is `/fast/scratch/hyaku/kotoba-r58/SrcCodex` at `3de87aad29e960c95ed35840442f424c48c29729`.
- The `True` result establishes that this fetched page holds the exact quote and the token according to the frozen `found_on_page` function. It does not establish full-row backing, integration into the lane, or the aggregate C1 `F`/`G` thresholds; no full counter run was assigned or performed.
- No tools were installed or updated. No out-of-scope clients or claims were evaluated.