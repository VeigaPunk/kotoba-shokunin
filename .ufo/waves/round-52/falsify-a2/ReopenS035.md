# ReopenS035 — SOURCES row S035, its entry use and the Gate quote

Result: HOLDS — S035's fetch record reproduces byte-for-byte (26,995 B, sha256 `c78df8c7…`), the Gate quote is a verbatim 19-word substring at the cited line 197, and every statement the entry and SKILL.md make from S035 (reading cell, 512-character authoring advice, cross-tool/constraints/rate-limits use) is on the page; two low/informational notes, no defect in the claim.

Seat: KotobaR52a2.ReopenS035 (leaf). Judged revision `c8407a453788df964df5a7b835dd0ce1360de882`. No lane file written except this report; no git write, no jj.

## Re-open (ordinary means: curl, no browser)

```
$ date -u +%Y-%m-%dT%H:%M:%SZ                                   # 2026-10-22T17:50:08Z
$ curl -sS -o codex-mcp.md -w 'http_code=%{http_code} size=%{size_download}\n' \
      https://developers.openai.com/codex/mcp.md
http_code=308 size=15
$ curl -sSI https://developers.openai.com/codex/mcp.md | sed -n '1,10p'
HTTP/2 308
location: https://learn.chatgpt.com/docs/extend/mcp.md?surface=cli
$ curl -sSL -o codex-mcp.md -w 'url_effective=%{url_effective} http_code=%{http_code} size=%{size_download}\n' \
      https://developers.openai.com/codex/mcp.md
url_effective=https://learn.chatgpt.com/docs/extend/mcp.md?surface=cli http_code=200 size=26995
$ wc -c codex-mcp.md ; sha256sum codex-mcp.md              # at 2026-10-22T17:50:11Z
26995 codex-mcp.md
c78df8c70b7f31f73557f77ad4208ff97656808fb423e6f4eb81151f8b009284  codex-mcp.md
```

Exit codes: all 0 (the 308 is HTTP, not a curl failure). 587 lines.
Working copies: `/fast/scratch/hyaku/kotoba-r52a2/ReopenS035/codex-mcp.md`.

Compare with the row (`corpus/SOURCES.md:48`) and the Gate (`corpus/lessons/round-52.md:26-28`):
row anchor says 26,995 B, sha256 `c78df8c7…`, fetched 2026-10-22T17:04:58Z; Gate says 26,995 B, sha256
`c78df8c70b7f31f73557f77ad4208ff97656808fb423e6f4eb81151f8b009284`. **Byte count identical, full hash identical.**
The 46-minute difference is the expected re-open time, not drift.

## Statement verdicts

Each row below is one statement, the page text that must support it, and the verdict.

| # | statement (where) | page evidence (fetched bytes) | verdict |
|---|---|---|---|
| 1 | anchor: fetch record 26,995 B / `c78df8c7…` / 17:04:58Z (`SOURCES.md:48`) | my fetch 17:50:11Z, 26,995 B, sha256 `c78df8c7…84`; full hash equals the Gate's | HOLDS |
| 2 | anchor: "server instructions bullet and the paragraph after it (`mcp.md:197-199`)" (`SOURCES.md:48`) | `:188` `## Supported MCP features`; `:197` the bullet; `:198` blank; `:199` the next paragraph | HOLDS |
| 3 | Gate quote, cited `mcp.md:197` (`round-52.md:28`) | `:197` `- **Server instructions**: Codex reads the MCP \`instructions\` field returned during initialization and uses it as server-wide guidance alongside the server's tools.` — exact substring, **1** occurrence, **19 words** (≤25) | HOLDS |
| 4 | row `teaches`: "reads the `instructions` field returned at initialization as server-wide guidance beside the tools, and asks server authors to keep the first 512 characters self-contained" | `:197` "returned during initialization … server-wide guidance alongside the server's tools"; `:199` "Keep the first 512 characters self-contained" addressed to "If you build or maintain an MCP server for Codex" | HOLDS |
| 5 | entry quote + location (`mcp-server-instructions-round52.md:26`, quote 19 words, `mcp.md:197`) | same substring on the page, quote cell verified as an exact substring by string test | HOLDS |
| 6 | entry reading cell: "Codex uses the text as server-wide guidance and advises keeping 'the first 512 characters self-contained' (`:199`)" | `:197` guidance; `:199` the 512 advice at the cited line; quoted fragment "the first 512 characters self-contained" is verbatim | HOLDS |
| 7 | entry § What follows 1: "Codex names its use for 'cross-tool workflows, constraints, and rate limits' (`:199`)" | `:199` "use `instructions` for cross-tool workflows, constraints, and rate limits that apply across the server"; fragment verbatim | HOLDS |
| 8 | entry § What follows 2: "Codex asks for the first 512 characters to stand alone" | `:199` "Keep the first 512 characters self-contained so the most important guidance is available when Codex is deciding how to use the server" — advice, correctly not stated as a truncation | HOLDS |
| 9 | SKILL.md:91 `why`: "Codex uses it as server-wide guidance and asks for a self-contained first 512 characters (S035)" | as #6/#8 | HOLDS |
| 10 | SKILL.md:93: "Claude Code, VS Code (S034), Codex and Gemini CLI (S036) put `instructions` in front of the model already" (Codex part) | `:197` "uses it as server-wide guidance alongside the server's tools"; `:199` "available when Codex is deciding how to use the server". "In front of the model" is a fair rendering, not a literal string | HOLDS [INFERENCE: one paraphrase step] |
| 11 | tier `A`, kind `docs`, scope "What Codex documents … (vendor documentation, not a measurement of omp or opencode)" | contract (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-27`): A = "primary or authoritative for that scope (… official docs …)"; scope is limited to documentation, and the entry's Limits say no client was run | HOLDS |
| 12 | status `mined`, `used-by` = entry + lesson, NF=13, recheck `90d`, opened `2026-10-22` | both used-by paths exist; row parses to 13 fields; `90d` matches the other vendor-docs rows (S033, S036); `mined` is honest with 2 citing paths | HOLDS |

The budget question in particular: the page never says Codex truncates `instructions` at 512 characters. `:199`
is an authoring request ("Keep … so the most important guidance is available"). The entry states it as advice and
contrasts it with Claude Code's 4,096-character cut (S033), so the two budgets are not conflated. A grep for
`character|token|limit` over the page finds no other statement about `instructions` length (`:325` is
`output_token_limit` for tools, unrelated).

Quote-substring test (read-only, exit 0):
```
lesson:28 n_words=19 substring_on_page=True | Codex reads the MCP `instructions` field returned during initialization and uses it as server-wide guidance alongside th…
entry:26  n_words=19 substring_on_page=True
entry:26  n_words=5  substring_on_page=True | the first 512 characters self-contained
```

## Notes (not breaks)

1. **Low — freshness: the pinned URL is now a redirect alias.** `https://developers.openai.com/codex/mcp.md`
   answers `308` with `location: https://learn.chatgpt.com/docs/extend/mcp.md?surface=cli`. The served bytes
   are identical today (hash match above), so the row is not wrong. But
   `verifiers/check_mcp_instructions.py:80` pins Codex hosts to `developers.openai.com` and
   `github.com/openai/codex`, and `:150-158` `host_ok` checks the URL string, while `:169-172` `fetch` uses
   `urllib.request.urlopen`, which follows redirects. If the alias is retired, `--fetch` fails and re-opening
   the row's URL fails, while the row still reads live. The row's `anchor` also names no heading, only line
   numbers `:197-199` plus the sha256; naming "§ Supported MCP features" would survive a re-render.
2. **Informational — page-scope qualifier not carried.** `:185-186` says "The supported server features below
   apply to MCP servers configured on a Codex host. Hosted plugin tools can have different capabilities."
   Neither the entry's Codex row nor SKILL.md:91-93 repeats this. The statements are still true of Codex-the-host
   (the row's subject); a reader who extended the rule to ChatGPT hosted plugins would be going past the source.
3. The page serves no `Last-Modified` or `ETag` (HEAD and GET headers inspected), so there is no publication
   date to record; the sha256 in the row is the only available revision pin, and it is present and exact.

## Remaining unknowns

- Whether Codex behaves as its page says (no client was run; the entry says so in § Limits, so this is out of
  scope, not a gap in the row).
- Whether `developers.openai.com/codex/mcp.md` stays a redirect alias; the row's URL and the counter's host pin
  both depend on it, and nothing in the lane records the alias.
- Nothing else: every S035-derived statement in the entry and SKILL.md was located on the fetched bytes.

Tooling: no install or upgrade; curl (system), python3 (system, `-B`). No model parameter, no `ask`.
