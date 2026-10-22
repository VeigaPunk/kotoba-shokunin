Result: MIXED — the fetch record reproduces exactly on two re-opens (49,781 B, sha256 `96794ff9…e050`, identical to the Gate's fetch), the Gate quote is a verbatim 18-word substring inside the cited § A Note for Client Implementers, and the row's reading (`teaches`) is supported by the page; one low-severity curation defect: tier `B` where the SOURCES contract's A bucket names "maintainer statement" and the lane's own vendor-engineering post (S014) is tier A.

# ReopenS037 — SOURCES row S037, its entry use and the Gate quote

Seat: KotobaR52a2.ReopenS037 (leaf). Judged revision `c8407a453788df964df5a7b835dd0ce1360de882`. No lane file written except this report; no git write, no jj, no clone (all checks are read-only over fetched bytes and lane reads).

## Re-open (ordinary means: curl, no browser)

```
$ curl -sS -o /tmp/s037/page.html \
    -w 'http_code=%{http_code} size=%{size_download} url=%{url_effective}\n' \
    https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/
http_code=200 size=49781 url=https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-22T17:50:10Z
$ sha256sum page.html
96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050  page.html
```

Second independent fetch:

```
$ curl -sS -o page2.html -w 'http_code=%{http_code} size=%{size_download}\n' \
    https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/
http_code=200 size=49781
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-22T17:54:18Z
$ sha256sum page.html page2.html
96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050  page.html
96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050  page2.html
```

Exit codes all 0. The pinned URL served the bytes directly — no redirect (`url_effective` equals the
requested URL). Response headers from HEAD at 17:55:24Z: `HTTP/2 200`,
`content-type: text/html; charset=utf-8`, `content-length: 49781`,
`last-modified: Sun, 23 Aug 2026 09:07:06 GMT`, `etag: "6a8ab83a-c275"`.

Compare with the row (`corpus/SOURCES.md:50`) and the Gate (`corpus/lessons/round-52.md:32-34`): both
record 49,781 B and sha256 starting `96794ff9…` (the Gate carries the full
`96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050`). **Byte count identical, full
hash identical** on both re-opens, 45 and 49 minutes after the 17:04:57Z Gate fetch. The row's
`opened 2026-10-22` is the same UTC day.

While this seat worked, the worktree gained a new `S039` row (another seat's write). S037's row is
byte-identical between the judged revision and the current worktree (`diff` of the `^| S037 ` line →
`identical`), and S037 stays at `corpus/SOURCES.md:50`; the added row sits after S038.

Working copies: `/fast/scratch/hyaku/kotoba-r52a2/ReopenS037/{page.html,page2.html,page.txt,clients-follow.html}`
(`page.txt` is my tag-stripped text extraction, derived, not evidence). Disclosure: the first fetch was
written to `/tmp/s037/` before the assigned scratch directory was created; the bytes were then copied to
the path above and are hash-identical there. Nothing was written in the lane, the fleet root, or a
sibling lane.

## Where the quote sits (byte-level proof, not grep)

The page is minified: 49,781 bytes with 48 newlines, so physical line numbers carry no meaning. Byte
offsets in `page.html`:

```
id=a-note-for-client-implementers            42486
"we recommend that you expose instructions…" 42714   <- rendered article copy, inside the section
id=currently-supported-host-applications     43350   <- next section starts
"For a complete list of host applications…"  43525   <- rendered copy, inside that section
```

The quote occurs **2** times in the raw bytes: byte 15386 (inside the `<script type=application/ld+json>`
BlogPosting block on physical line 1, escaped `\n`, not the article) and byte 42714 (the rendered paragraph). Only the second is the page's
visible text, and it lies after the `A Note for Client Implementers` heading and before the next
heading, i.e. inside the section the row and Gate cite.

Verbatim, from the tag-stripped text (`page.txt:103-104`):
`@@H3@@ A Note for Client Implementers#` then
"If you're building an MCP client that supports server instructions, we recommend that you expose
instructions to users and provide transparency about what servers are injecting into context. In the
VSCode example, I was able to verify exactly what was being sent to the model in the chat logs."

The second cited section (`page.txt:108-109`): "For a complete list of host applications that support
server instructions, refer to the Clients page in the MCP documentation." The link's target is
`https://modelcontextprotocol.io/clients` (one occurrence in the raw bytes).

Quote-substring tests (both exit 0):

```
$ python3 -B check.py            # substring test on the raw bytes, no whitespace normalization
gate quote n_words=18 contains_instructions=True on_page=True
entry item-5 quote n_words=14 on_page=False      # because the markdown wraps the quote across lines
deferral sentence on_page=True
char budget 4,096 on_page=False 512 on_page=False
$ python3 -B check2.py           # same test with the quote's whitespace collapsed
entry item-5 quote raw: 'at servers are injecting into\n   context'
normalized n_words=14 on_page=True
quote text: expose instructions to users and provide transparency about what servers are injecting into context
```

The first line of `check2.py` is the raw cell text: the entry (and the page) differ only by the
markdown line wrap, not by content.

## Statement verdicts

| # | statement (where) | page evidence (fetched bytes) | verdict |
|---|---|---|---|
| 1 | anchor fetch record: 17:04:57Z, 49,781 B, sha256 `96794ff9…` (`SOURCES.md:50`) | two re-opens: 17:50:10Z and 17:54:18Z, 49,781 B, sha256 `96794ff9…e050`; `last-modified 2026-08-23T09:07:06Z`, `etag "6a8ab83a-c275"` | HOLDS |
| 2 | anchor locations: "§ A Note for Client Implementers; § Currently Supported Host Applications" (`SOURCES.md:50`) | `h3 id=a-note-for-client-implementers`; `h2 id=currently-supported-host-applications`; both heading texts exact | HOLDS |
| 3 | source title and date "… user manual for your server (2025-11-03)" (`SOURCES.md:50`) | `<title>Server Instructions: Giving LLMs a user manual for your server \| Model Context Protocol Blog</title>`; `"datePublished":"2025-11-03T00:00:00Z"`; slug `2025-11-03-using-server-instructions` | HOLDS |
| 4 | Gate quote, cited "§ A Note for Client Implementers" (`round-52.md:32-34`) | rendered occurrence at byte 42714, between the h3 (42486) and the next h2 (43350); 18 words (≤25), contains `instructions`; exact substring of the fetched bytes | HOLDS |
| 5 | row `teaches` clause 1: "Client implementers are asked to expose server instructions to users and be transparent about what servers inject into context" (`SOURCES.md:50`) | "we recommend that you expose instructions to users and provide transparency about what servers are injecting into context", addressed to "an MCP client that supports server instructions"; the "Give users control — Allow reviewing, enabling, or disabling server instructions" bullet confirms the exposure is to users | HOLDS (paraphrase; qualifier note 1) |
| 6 | row `teaches` clause 2: "the post defers the list of supporting clients to the MCP Clients page" (`SOURCES.md:50`) | "For a complete list of host applications that support server instructions, refer to the Clients page in the MCP documentation", href `https://modelcontextprotocol.io/clients`, inside § Currently Supported Host Applications (byte 43525, after h2 43350) | HOLDS (target-moved note 2) |
| 7 | entry frontmatter: S037 URL + "§ A Note for Client Implementers" (`mcp-server-instructions-round52.md:1`) | URL and section as above | HOLDS |
| 8 | entry § What follows 5: the same recommendation, quoted, plus "Whether any of the five clients does so was not checked" (`:53-55`) | the 14-word fragment is a verbatim substring once the markdown line wrap is collapsed; the second clause is the entry's own limit (no client was run) | HOLDS |
| 9 | SKILL.md source range "S032–S037" (`SKILL.md:86`) and no other S037 use | `grep -n 'S037' SKILL.md` → only line 86; no table cell or prose in SKILL.md attributes a claim to S037 (grep for `blog`, `transparen`, `expose` → 0 hits); the entry does use S037 (item 5), so the range is honest | HOLDS |
| 10 | budgets/limits: none attributed to S037 (entry § What follows 2 and the per-client cells cite S033 for 4,096 and S035 for 512; `SKILL.md:91` same) | page contains no `4,096`, `4096` or `512` at all (string test False); its only numbers are example payloads ("Binary files over 10MB", "100 requests/minute", the anti-pattern "[500 words]") — so the page could not support a client budget, and none is attributed to it | HOLDS |
| 11 | tier `B`, scope "… (maintainers' blog post; explanatory, not normative spec text)" (`SOURCES.md:50`; repeated `round-52.md:32`) | see defect D1 | **BREAKS (low)** |
| 12 | kind `docs`, status `mined`, `used-by` = entry + lesson, 11 cells, `recheck 180d` | census at the judged revision: malformed rows `0`; both used-by paths exist and both contain `S037` (entry `:1,:53`; lesson `:32`); `docs` matches S014's kind for a vendor engineering post; page is static (`last-modified 2026-08-23`), 180d is defensible | HOLDS |

## Defect

**D1 — low, curation: tier `B` is below the contract's A bucket.** Evidence:

- Contract (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-28`, duplicated
  at `/home/vgpnk/Projects/shokunin/CORPUS.md:93-96`): "**A**: primary or authoritative for that scope
  (spec, official docs, source code, original paper, **maintainer statement**, the lane's own
  re-runnable gate output)."
- The page is a maintainer statement on the project's own property: byline "November 3, 2025 · 9 min ·
  Ola Hungerford **(Maintainer)**", host `blog.modelcontextprotocol.io`, footer "Copyright © Model
  Context Protocol a Series of LF Projects, LLC."
- The lane's own precedent agrees: S014, "Anthropic Engineering — Equipping agents for the real world
  with Agent Skills", kind `docs`, is tier `A` (`corpus/SOURCES.md:27`). S037 is the same shape
  (official vendor/project explainer, not independent commentary).
- S037 is the lane's **only** B row: tier histogram at the judged revision
  (`git show c8407a45:corpus/SOURCES.md` piped through the contract's census awk) → `A=36 B=1 C=1`.
- Direction is conservative: no claim, admission or counter depends on the cell. The frozen counter
  reads tier only inside its seven-client loop (`verifiers/check_mcp_instructions.py:212`,
  `if s[3] != "A"`), and S037 is not one of the seven client rows — re-tiering to A would not move
  `backed 5 of 7`.
- Recorded counter-argument: B's "strong secondary (expert write-up with reproducible detail …)" also
  fits — the post carries a 40-session evaluation and a sample repo. So the defect is the cell's
  inconsistency with the A-list example and with S014, not a false claim about the page.

Fix options for the L1: set tier `A` (and change the Gate parenthetical `tier B: maintainers' blog` in
`round-52.md:32`), or keep `B` and drop "maintainers' blog post" from the rationale in favour of the
reproducible-write-up clause — but the row's own `scope` names a maintainers' post, which is the A
example.

## Notes (not breaks)

1. **Low — the conditional is dropped in the row's reading (`teaches`).** The page says "**If you're building an
   MCP client that supports server instructions,** we recommend …". The row's `teaches` says "Client
   implementers are asked …" without that qualifier. Not material for this entry (S037 is about
   clients that read the field), but a reader could over-read it as applying to every client
   implementer. The entry's item 5 keeps "a client" and is closer to the page.
2. **Informational — the deferred list's target has moved.** `https://modelcontextprotocol.io/clients`
   answers `HTTP/2 308` with `location: /docs/2026-07-28/getting-started/intro`; following it at
   17:53:14Z gave `200`, 314,436 B, sha256 `662f0bbb91f9119c68e37cfd5aa6969b8c758bcfd2c7c39027eb9bc847604070`
   (the versioned docs intro; the followed page contains `0` occurrences of `server instructions` and `0` of
   `list of host applications`, so it does not carry the deferred list). The post's sentence is unchanged and
   the row only claims the post *defers*, so this is not a break; the 180-day recheck will need the
   docs' new location for the clients list.
3. **Low — the Gate grounds only half of `teaches`.** `teaches` has two claims; the Gate pastes one
   ≤25-word quote (clause 1) and records clause 2 only through the row's anchor. Contract rule 1 asks
   for "a ≤25-word quote with its location grounding `teaches`" (`SOURCES-CONTRACT-v1.md:45-48`); the
   deferral clause is true and located (byte 43525) but not quoted. No false statement — a coverage
   gap in the Gate record.
4. **Informational — the entry's `recheck` command does not touch S037.** `check_mcp_instructions.py`
   reads only the seven client rows and the entry's per-client table; S037's claim rides on the row's
   `180d` date recheck. Not a Q04 break (the command resolves and runs), but this is the one entry
   source outside the automatable check.

## Remaining unknowns

- Whether any client actually exposes the text to its users. The page only recommends it; no client was
  run, and the entry says so in item 5. Out of scope, not a gap in the row.
- Whether the post is edited later. The sha256 is the only revision pin the row records, but the server
  also exposes `last-modified: 2026-08-23T09:07:06Z` and `etag "6a8ab83a-c275"`, so drift is detectable
  on re-open even though the row does not carry them.
- Whether the `/clients` → `/docs/2026-07-28/getting-started/intro` redirect is permanent and where the
  supporting-clients list now lives; I did not chase it further, because the row's statement is about
  the post, not the target.

Tooling: no install or upgrade; curl (system) and python3 `-B` (system). No `model` parameter, no `ask`.
