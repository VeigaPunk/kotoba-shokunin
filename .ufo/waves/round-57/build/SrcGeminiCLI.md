Result: DONE — official Gemini CLI docs establish `gemini-extension.json` as the required extension-root manifest and support the S083 draft below.

## Finding and provenance

Gemini CLI calls these packages **extensions** in this reference. The page states that extensions load from `<home>/.gemini/extensions` and that every extension has a `gemini-extension.json` file at its root (`extensions-reference.md:106-107`). The exact manifest token is `gemini-extension.json`; it is spelled that way on the page. Its final segment is `.json` and contains both the Gemini marker and `extension`, satisfying the frozen v2 token shape for Gemini CLI.

Fetched the official pinned-host page with:

```sh
mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI && date -u && curl -L -sS -o /fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI/extensions-reference.md -w 'curl exit-status transfer; http_code=%{http_code}\nurl_effective=%{url_effective}\nsize_download=%{size_download}\n' https://geminicli.com/docs/extensions/reference.md; printf 'curl_exit=%s\n' "$?"; wc -c /fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI/extensions-reference.md; sha256sum /fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI/extensions-reference.md
```

Observed date line: `Fri 23 Oct 2026 04:46:46 AM UTC`; curl exit 0; HTTP 200; final URL `https://geminicli.com/docs/extensions/reference.md`; downloaded 12,022 bytes; SHA-256 `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72`.

### Quote for the entry and `## Gate`

> Update an extension to the version specified in its `gemini-extension.json`

This is the exact text of fetched physical line 69 (line terminator omitted); 10 words after stripping Markdown backticks, with `extension` outside the token. No text bytes were removed or rewritten. The fetched bytes show the quote at `extensions-reference.md:69`.

### What an extension can contain, as documented

- Extension root / load path and required manifest: `<home>/.gemini/extensions`; each extension root must contain `gemini-extension.json` (`extensions-reference.md:106-112`).
- MCP server configurations are defined by the manifest's `mcpServers` field and loaded on startup; the page also recommends `${extensionPath}` for extension-local files (`:146-157`).
- Context is loaded from the configured `contextFileName`; if unset, an extension-root `GEMINI.md` is loaded when present (`:158-161`).
- Custom commands are TOML files under `commands/`; directory structure determines command names (`:229-238`).
- Hooks are defined in extension-root `hooks/hooks.json`, separately from `gemini-extension.json` (`:240-244`).
- Agent skills go under `skills/`, with a `SKILL.md` example (`:246-250`).
- Sub-agent Markdown definition files go under the extension-root `agents/`; the reference labels sub-agents a preview feature under active development (`:252-259`).
- Extensions can contribute policy rules and safety checkers; `.toml` files in root `policies/` are loaded when the extension is activated (`:261-269`).
- The manifest also documents extension settings (`:180-205`) and a planning directory setting (`:168-173`). This page does not describe LSP contributions; that is a limit of this page, not a claim that Gemini CLI lacks LSP support.

A case-insensitive search of `corpus/SOURCES.md` for `geminicli.com/docs/extensions` returned no matches, so this page URL is not a previously listed base source URL. The URL is on the frozen Gemini CLI pinned host `geminicli.com`.

## Draft rows (not integrated)

SOURCES column shape copied from `corpus/SOURCES.md` header and rows S072-S078; proposed tier A, status `mined`, opened `2026-10-23`, and the requested used-by path:

```md
| S083 | Gemini CLI docs — Extensions reference — https://geminicli.com/docs/extensions/reference.md | docs | A | Gemini CLI extension manifest location and documented extension contents (vendor documentation; not runtime behavior) | § Extension format, `extensions-reference.md:104-112`; `mcpServers` and `contextFileName`, `:146-161`; Custom commands, `:229-238`; Hooks, `:240-244`; Agent skills, `:246-250`; Sub-agents, `:252-259`; Policy Engine, `:261-269`; fetched 2026-10-23T04:46:46Z, HTTP 200, 12,022 B, sha256 `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` (seat SrcGeminiCLI) | Every extension requires a root `gemini-extension.json`; documented contents include MCP servers, context, commands, hooks, skills, sub-agent definitions, and policy rules/safety checkers | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

Proposed SKILL.md table row (first backticked span is the manifest token; Action has 7 words):

```md
| Gemini CLI | `gemini-extension.json` (each extension root; extensions load from <home>/.gemini/extensions) | MCP servers; context files; TOML commands; hooks; skills; sub-agent Markdown; policy rules and safety checkers | Inspect extension contents before applying skill guidance |
```

Proposed knowledge-entry row (manifest cell exactly matches the SKILL.md token; quote is the line-69 quote above):

```md
| Gemini CLI | gemini-extension.json | S083 | "Update an extension to the version specified in its `gemini-extension.json`" |
```

## Gates, surfaces, and limits

- The source satisfies this seat's source evidence: official docs on a frozen Gemini CLI host, fetched live (HTTP 200), new base-URL path, and a quote with 10 words, the exact token, and `extension` outside the token.
- The C1 v2 predicate was **not run**. These are draft rows only; the entry quote must also be recorded in the round-57 lesson `## Gate`, and the integrated seven-client world must be assessed with the frozen `--fetch` counter before claiming any C1 predicate result. No F/K/G result is claimed here.
- No Q30 sweep was run because this page positively documents a JSON manifest; no claim that Gemini CLI has no manifest was made.
- Only this assigned report was written in the lane. The fetched page is the scratch artifact `/fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI/extensions-reference.md`. No product docs, SOURCES rows, lesson text, counters, or code were edited; no tool was installed; no commit or sandbox counter run was made. C2 and runtime extension behavior are out of scope for this source seat.

Artifacts: `.ufo/waves/round-57/build/SrcGeminiCLI.md`; `/fast/scratch/hyaku/kotoba-r57/SrcGeminiCLI/extensions-reference.md`.
