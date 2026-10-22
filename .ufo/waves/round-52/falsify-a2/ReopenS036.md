# ReopenS036 — SOURCES row S036, its entry use and the Gate quote

Result: MIXED — S036's fetch record, quote location, reading cell and tier reproduce exactly (43,656 B, sha256 `4aefc4dc…`), but the Gate quote is a subject-less 8-word fragment that grounds only the second half of `teaches`, and the rendered page carries a site banner (Gemini CLI replaced by Antigravity CLI for unpaid/Google One users on 2026-06-18; not optimized for Gemini 4 Argon) that neither the `.md` citation surface, the row, the entry nor SKILL.md records.

Seat: KotobaR52a2.ReopenS036 (leaf). Judged revision `c8407a453788df964df5a7b835dd0ce1360de882`. No lane file written except this report; no git write, no jj command.

## Re-open (ordinary means: curl, no browser)

```
$ curl -sS -D headers.txt -o mcp-server.md -w 'http_code=%{http_code} size=%{size_download}\n' \
      https://geminicli.com/docs/tools/mcp-server.md
http_code=200 size=43656                                   # exit 0
$ wc -c mcp-server.md ; sha256sum mcp-server.md
43656 mcp-server.md
4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd  mcp-server.md
```

Headers (`headers.txt`): `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`,
`last-modified: Fri, 16 Oct 2026 02:36:07 GMT`,
`etag: "4612ac5f5ea780539889b3e4f13df041e649f02e83e8ca3dfe0f0a06f74759a0"`, `x-cache: HIT`,
`date: Thu, 22 Oct 2026 17:50:13 GMT`. Access window 2026-10-22T17:50:12Z–17:50:13Z. The file is
1,315 lines with no trailing newline (last byte is the period of line 1315).

Compare with the row (`corpus/SOURCES.md:49`) and the Gate (`corpus/lessons/round-52.md:29-31`): row
anchor says 43,656 B, sha256 `4aefc4dc…`, fetched 2026-10-22T17:04:58Z; Gate says 43,656 B, sha256
`4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd`. **Byte count identical, full hash
identical**, and `Last-Modified` predates the recorded fetch, so nothing changed between 17:04:58Z and
17:50:13Z. Working copy: `/fast/scratch/hyaku/kotoba-r52a2/ReopenS036/mcp-server.md`.

Cited location, exact numbering from the fetched bytes:

```
$ awk 'NR>=1311 && NR<=1316 {printf "%d|%s\n", NR, $0}' mcp-server.md
1311|## Instructions
1312|
1313|Gemini CLI supports
1314|[MCP server instructions](https://modelcontextprotocol.io/specification/2025-06-18/schema#initializeresult),
1315|which will be appended to the system instructions.
```

`grep -n -i instruction mcp-server.md` → 494 (`#### Setup instructions`, unrelated), 1311, 1314, 1315.
So the section is three lines, the heading is real and unique, and the sentence at 1313-1315 is the
page's only statement about MCP `instructions`; the page states no length limit, truncation or budget
for it (`grep -n -i 'limit\|truncat\|characters\|token'` finds only tool-naming and token-config lines).

Second source route, for parity of the prose: `https://geminicli.com/docs/tools/mcp-server` answers
`301` (38 B) and follows to `https://geminicli.com/docs/tools/mcp-server/`, `200`, 337,347 B, sha256
`835ecc174d8df0983a10c56a7cfae4bc014418703b5bd5dd34feab4011ddb782`, fetched 17:50:46Z and again
17:54:30Z byte-identical, same `Last-Modified`; it contains "appended to the system instructions" once.

Host provenance (for the tier call): the HTML carries `rel="canonical"
href="https://geminicli.com/docs/tools/mcp-server/"` and links to `github.com/google-gemini/gemini-cli`
and its `website_issue.yml`; upstream `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md`
(fetched 2026-10-22T17:51:11Z, 12,107 B, sha256
`7235196f55461732c246c20ce9996cc56ba2e52641f183ccf4e6493bd93c1c94`) line 28 reads
"Learn all about Gemini CLI in our [documentation](https://geminicli.com/docs/)". So `geminicli.com`
is the vendor's own docs host, as S029 already recorded for the skills page.

Counter run against the judged revision:

```
$ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882 --fetch
MCP specification  BACKED found=True
Claude Code        BACKED found=True
VS Code            BACKED found=True
Codex              BACKED found=True
Gemini CLI         BACKED found=True
opencode           no rows naming client: 0 (need 1)
Copilot CLI        no rows naming client: 0 (need 1)
mcp instructions backed 5 of 7 clients
mcp instructions found on the live page 5 of 5
EXIT=0
```

## Statement verdicts

Each row is one statement the row, the entry, the lesson or SKILL.md makes from S036, the fetched bytes
that must support it, and the verdict.

| # | statement (where) | page evidence (fetched bytes) | verdict |
|---|---|---|---|
| 1 | anchor fetch record: `§ Instructions (mcp-server.md:1311-1315)`, 43,656 B, sha256 `4aefc4dc…`, fetched 2026-10-22T17:04:58Z (`SOURCES.md:49`) | my fetch 17:50:13Z, 43,656 B, full hash equals the Gate's; heading at `:1311`, body `:1313-1315` | HOLDS |
| 2 | Gate quote `"which will be appended to the system instructions."` cited `mcp-server.md:1315`, § Instructions (`round-52.md:30-31`) | `:1315` is exactly that string, period included; **1** occurrence on the page, **8** words (≤25) | HOLDS (fragment — see D1) |
| 3 | row `teaches`: "Gemini CLI supports MCP server instructions and appends them to its system instructions" (`SOURCES.md:49`) | `:1313` "Gemini CLI supports"; `:1314` the `[MCP server instructions](…)` link; `:1315` "which will be appended to the system instructions." | HOLDS |
| 4 | entry source line and per-client row: quote above, location "`mcp-server.md:1315`, § Instructions" (`mcp-server-instructions-round52.md:1`, `:26`) | same substring and line, verified by string test on the fetched bytes | HOLDS |
| 5 | entry reading cell: "Gemini CLI supports MCP server instructions and appends them to its system instructions (`:1313-1315`)" | the full sentence at `:1313-1315` says exactly that; the relative clause attaches to the linked noun "MCP server instructions"; no condition, no limit claimed | HOLDS |
| 6 | entry § What follows 1: "Four clients (Claude Code, VS Code, Codex, Gemini CLI) document that they put the text in front of the model" | `:1315` "appended to the system instructions"; the same site's system-prompt page defines system instructions as the CLI's system prompt (`https://geminicli.com/docs/cli/system-prompt.md`, fetched 2026-10-22T17:53:08Z, 4,632 B, sha256 `f32d65071c659670145f560e83f6422561f6b5adaa7eb577b9172c320877265f`: `:3` "The core system instructions that guide Gemini CLI can be completely replaced", `:10` "file for its system prompt") | HOLDS [INFERENCE: one paraphrase step, "appended to the system instructions" → "in front of the model"] |
| 7 | SKILL.md:93 "Claude Code, VS Code (S034), Codex and Gemini CLI (S036) put `instructions` in front of the model already" (Gemini part) | as #6 | HOLDS [same inference]; see I2 for the citation placement |
| 8 | entry claim that the page states no Gemini budget, and that budgets differ across clients (§ What follows 2) | no instruction-length, truncation or budget statement anywhere on the page; the entry states none for Gemini | HOLDS |
| 9 | tier `A`, kind `docs`, status `mined`, `opened 2026-10-22`, `used-by` = entry + lesson, `recheck 90d`, NF=13 | contract (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-27`): A = "primary or authoritative for that scope (… official docs …)"; the scope cell limits the claim to documentation; both `used-by` paths name S036; `90d` is a legal cadence | HOLDS (cadence challenged in D2) |
| 10 | C2's declared statement as the counter prints it (`5 of 7`, `--fetch` 5 of 5) | counter output above, exit 0; Gemini CLI row admitted on tier/kind/status/host/quote/lesson checks | HOLDS |

Quote assertions (read-only, exit 0):

```
gate_quote_words=8 substring_on_page=True occurrences=1
entry_has_quote=True gate_has_quote=True
subject_clause_at: [1313]
reconstructed_1313_1315: Gemini CLI supports [MCP server instructions](https://modelcontextprotocol.io/specification/2025-06-18/schema#initializeresult), which will be appended to the system instructions.
row_has_bytes=True row_has_hash_prefix=True
gate_has_bytes=True gate_has_full_hash=True
```

## Defects

**D1 — Low. The Gate quote is a dependent clause and does not by itself name its subject.**
`round-52.md:31` quotes only `:1315`, "which will be appended to the system instructions." Neither
"Gemini CLI" nor "MCP" appears in the quote; the row's `teaches` first clause ("Gemini CLI supports MCP
server instructions") is carried by `:1313-1314`, outside the quoted text. Contract rule 1
(`SOURCES-CONTRACT-v1.md:42-44`) asks for "a ≤25-word quote with its location grounding `teaches`"; the
location is exact, so a non-author re-opening at `:1311-1315` sees the whole sentence, and the frozen
counter is satisfied (8 words, contains `instructions`, found live). This is an evidence-strength
defect, not a false statement. Fix: quote the whole sentence —
"Gemini CLI supports [MCP server instructions](https://modelcontextprotocol.io/specification/2025-06-18/schema#initializeresult),
which will be appended to the system instructions." (14 words; the link markup must stay so the
counter's verbatim test on the `.md` bytes still matches) — or add `:1313-1314` as a second quoted
line beside the current fragment.

**D2 — Medium. The page's banner is invisible through the `.md` route and is recorded nowhere.**
The rendered page carries a layout-level `div.announcement-banner` (present 1× on this page and 1× on
`/docs/cli/skills/`, so it is not page-specific; the 337,347-byte HTML re-fetched identical at 17:54:30Z):

> Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026. To
> learn more, see our blog post. Gemini CLI has not been optimized for Gemini 4 Argon. To use Gemini 4
> Argon, please use Antigravity.

(two `<p>` elements inside one `div.announcement-banner`). The `.md` route the row cites contains the string "Antigravity" **0**
times (`grep -c -i antigravity mcp-server.md` → 0), and the site dump `https://geminicli.com/llms.txt`
(968,590 B, sha256 `3759fcdee73f3cd2576a781c8aaafbf0627b8c58655e63c6175af71677641e32`, 17:51:17Z) has
the page's identical sentence at line 23724 but **0** hits for "was replaced by Antigravity". Only the
HTML route exposes the notice. `grep -rni antigravity corpus SKILL.md PROVINCE.md SCORECARD.md` returns
7 hits, all unrelated (`m_antigravity` routing aliases and the `antigravity/gemini-*` provider name in
old round reports); `grep -rni "antigravity cli\|replaced by antigravity"` over the same set returns 0,
so no row, entry, lesson or SKILL.md cell records this. The statements
themselves stay true of Gemini CLI as documented (the banner scopes the replacement to "unpaid tier
and Google One users"), but the entry is the lane's only record of this client surface and it presents
Gemini CLI, without caveat, as one of four clients whose `instructions` handling a skill author can
rely on "already" — material for a craft decision four months after the vendor moved a whole user
class off the product. Fix: one clause in the Gemini reading cell and/or a bullet in the entry's
§ Limits, e.g. "The page's banner says unpaid and Google One users were moved to Antigravity CLI on
2026-06-18 and that Gemini CLI is not optimized for Gemini 4 Argon"; and reconsider the row's `recheck`
from `90d` to `on-release` for a product under transition. Generalize the method: a source fetched
through a `.md`/distill route loses layout-level notices, so any row pinned to such a route needs the
HTML route opened once for banners.

## Informational notes (not defects)

1. **I1 — the page's spec link is older than the round's spec row.** `:1314` links the MCP spec at
   `2025-06-18`, while S032 pins `2025-11-25`. Nothing in the row, entry or SKILL.md depends on the
   page's link target, so there is no conflict to reconcile.
2. **I2 — SKILL.md:93 cites two of the four clients it names.** The cell carries "(S034)" for VS Code
   and "(S036)" for Gemini CLI while also naming Claude Code and Codex; their rows (S033, S035) are
   cited in the two table rows directly above, so the names resolve, but the cell read alone loses two
   citations. Cosmetic.
3. **I3 — verb tense.** The page says "will be appended"; the row's `teaches` and the reading cell say
   "appends". Same proposition, no condition stated on the page either way.
4. **I4 — the banner predates round 52.** The skills page HTML fetched today (`https://geminicli.com/docs/cli/skills/`,
   17:54:30Z, 114,148 B, sha256 `b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640`)
   is byte-identical to the hash S029 recorded in round 50, and it carries the same banner (1×). So the
   omission in D2 is older than this round and is not a round-52 regression; it is still unrecorded
   anywhere.

## Remaining unknowns

- Whether Gemini CLI actually appends the text at runtime. No client was run; the entry says so in
  § Limits, so this is out of scope rather than a gap in the row.
- What the linked vendor blog post says about which tiers keep Gemini CLI: the banner scopes the
  replacement to "unpaid tier and Google One users" and the post was not opened by this seat, so the
  paid/enterprise picture is [UNRESOLVED].
- Whether the counter would notice a re-render of this page: `--fetch` compares normalized bytes only
  (`verifiers/check_mcp_instructions.py:243-252`); it checks no line number, so the cited location stays
  a human check (done here) and would survive a re-flow unnoticed.

## Tooling

No install or upgrade (curl and python3 from the system). No `model` parameter, no `ask`. Scratch copies
under `/fast/scratch/hyaku/kotoba-r52a2/ReopenS036/` only; no git write, no jj command, no lane file
touched other than this report.
