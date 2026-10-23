Result: DONE — Claude Code: ELIGIBLE https://code.claude.com/docs/de/memory.md token `.claude/rules/` key `paths` line 198

Re-census seat RecensusClaudeCode. One client. No lane files edited. No tools installed (pacman paused; nothing missing). Counter helpers imported read-only from `verifiers/check_scoped_rules.py` at the lane (sha of that file not re-hashed here; the freeze sha is the plan's `6aea3be0…`). Fetched bytes under `/fast/scratch/hyaku/kotoba-r60/RecensusClaudeCode/`.

The English page `https://code.claude.com/docs/en/memory.md` is base key `//code.claude.com/docs/en/memory` (S043) and was not used. A scan of the English docs dump found no other English page that has both the token and an A1 `paths` key site. The German locale of the same article does not redirect onto that base key.

## Eligible page

URL requested and final URL (no redirect): `https://code.claude.com/docs/de/memory.md`

```
$ date -u
Fri 23 Oct 2026 10:56:39 AM UTC
$ curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' -o de-memory.body 'https://code.claude.com/docs/de/memory.md'
200 https://code.claude.com/docs/de/memory.md
$ wc -c de-memory.body
63447 de-memory.body
$ sha256sum de-memory.body
c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43  de-memory.body
```

User-Agent is the counter's `CURL_UA` (`check_scoped_rules.py:300-301`). Bytes saved at `/fast/scratch/hyaku/kotoba-r60/RecensusClaudeCode/de-memory.body`.

```
$ python3 -B -c "import sys; sys.path.insert(0,'verifiers'); import check_scoped_rules as c; print(c.url_key('https://code.claude.com/docs/de/memory.md'))"
//code.claude.com/docs/de/memory
$ grep -cxF '//code.claude.com/docs/de/memory' .ufo/waves/round-60/w0b-base-url-keys.txt
0
```

`grep` exit 1 (count 0, no match). Same key for the final URL. `host_ok` True on `HOSTS["Claude Code"]`. `url_is_change_note` False. `url_is_tracker` False.

## Token

`.claude/rules/` as printed on line 18 (also the heading at line 166). `token_well_formed('.claude/rules/')` is True. `foreign_marker('Claude Code', '.claude/rules/')` is None.

```
$ sed -n '18p' de-memory.body
* [Regeln auf bestimmte Dateitypen beschränken](#organize-rules-with-claude/rules/) mit `.claude/rules/`
```

## Quote

Whole line 18, backticks kept, nothing removed. 8 words after the counter's count (`quote.replace('\`','').split()`).

```
$ sed -n '18p' de-memory.body | wc -w
8
```

`wc -w` is 8 because the backticks are not whitespace. The counter strips them and still gets 8 (`len(q.split())` → 8).

`token_span` on the backtick-stripped line is `(88, 102)`, text `.claude/rules/`. `rule_word_outside` is True. The two outside matches are the English word `rules` inside the untranslated anchor, not a German prose word:

- offset 58–63, `rules` in `#organize-rules-with-claude`
- offset 76–81, `rules` in `#organize-rules-with-claude/rules/`

The in-token match is offset 96–101 inside `.claude/rules/`. `quote_why(page, line 18)` is `[]`. `live_why(page, line 18, 'paths')` is `[]`.

[INFERENCE] A reader who wants the outside word to be prose rather than an anchor slug can reject this quote. The counter's own regex accepts it, and no 6–25-word span on this page pairs the token with a prose `rule(s)`/`instruction(s)` outside the token. The code comment `# Main project instructions` (line 181) and the heading `# API Development Rules` (line 202) are English, but neither line contains `.claude/rules/`.

## Scope key

K = `paths`. L = 198. `key_site(lines, 198, 'paths')` is True. `key_site` at 197 and 199 is False. Second site: line 231, also True.

```
$ sed -n '198,201p' de-memory.body
paths:
  - "src/api/**/*.ts"
---

```

Line 198 is `paths:` at an identifier boundary, then `:`, rest empty, so the value is the block. `value_after` returns `  - "src/api/**/*.ts"`. `first_value_token` is `src/api/**/*.ts`. `pattern_value` is True (`*` and only `[A-Za-z0-9_./*{},!-]`).

## Action line

Line 194 is the translated author line (scope a rule with YAML frontmatter `paths` so it applies only to matching files). A cell built only from words on that line passes A1.

```
$ sed -n '194p' de-memory.body
Regeln können mit YAML-Frontmatter mit dem Feld `paths` auf bestimmte Dateien beschränkt werden. Diese bedingten Regeln gelten nur, wenn Claude mit Dateien arbeitet, die den angegebenen Mustern entsprechen.
```

Call (exit 0):

```
cell = 'Regeln mit YAML Frontmatter gelten wenn Claude bestimmte Dateien und Mustern arbeitet (S901 :194)'
c.content_words(cell)
→ arbeitet, bestimmte, claude, dateien, frontmatter, gelten, mustern, regeln, wenn, yaml
shared with line 194 → the same 10 words
c.action_conjunct(lines, cell, 194) → []
c.action_conjunct(lines, cell, 193) → shares 0 of 8..10 (need >= 4)
```

`|W|` = 10, need `max(2, ceil(10/2))` = 5, shared = 10. Umlauts in `können` and `beschränkt` are not `[a-z]{4,}` runs and are not in the cell.

## Other pages checked

English docs index `https://code.claude.com/docs/llms.txt` fetched 10:54:48Z (HTTP 200, 63682 bytes, sha256 `b7064ac53215f39ad3b8cb20f1a63dba5334f6fcb7efd8e789c55fa634e3d4c0`; that one fetch used Chrome/131, not `CURL_UA`). Full dump `https://code.claude.com/docs/llms-full.txt` fetched 10:55:44Z (HTTP 200, 9614681 bytes, sha256 `1a5816202ca5cb4378a2ea8afad80d1d0102e83fe387096ffe0ca89f80fe563a`, `CURL_UA`). 232 `Source:` sections. `any_key_site(..., 'paths')` is true on exactly two of them: `//code.claude.com/docs/en/memory` (base, has the token) and `//code.claude.com/docs/en/security-guidance` (not base, no `.claude/rules` token). Sitemap `https://code.claude.com/sitemap.xml` (10:55:44Z, HTTP 200, 357067 bytes) lists locale copies, including `/docs/de/memory` and `/docs/ja/memory`.

Each row: `date -u` Fri 23 Oct 2026 10:55:07 AM UTC unless noted, HTTP 200, final URL = requested URL, `CURL_UA`. `url_key` not in the base list (`grep -cxF` would be 0; keys computed with `c.url_key`).

| page | bytes | sha256 | why not the row |
|---|---|---|---|
| `/docs/en/claude-directory.md` | 28637 | `dcdaaf756a9596854e03cd5c9a4d0952e9806215eabfe92cd6328b0a1265ffc8` | names `rules/*.md`, not `.claude/rules/`; no `paths:` key site |
| `/docs/en/best-practices.md` | 36360 | `b225977e2892002cc91ff4dfe2d6a7e2324fd455aa6325c889cecb009ca76052` | no `.claude/rules` and no `paths:` |
| `/docs/en/features-overview.md` | 27348 | `e1f0ae3d6465f43cc18b3fc1cdab43b4ca10455ddbe5917ef11d79d86b64ab82` | token and an English rules sentence (line 140); `any_key_site` for `paths` is false |
| `/docs/en/context-window.md` | 8495 | `f2cf7463cb14b4dc9607ee235b26267ed5cc6ca17ad7abd45fe83924130cdbd9` | `paths:` only inside backticks in prose; no key site |
| `/docs/en/large-codebases.md` | 34542 | `870eacc7cff99fd6593db39e5c648048dcfb36dcaa7701b78763f81c23e6319a` | token on line 111; `paths:` is prose in a table, not key form |
| `/docs/en/glossary.md` | 28423 | `8ff46b8da555b33eb7a82c9962d2c95853c6c57ae1059e72dd59eeae4c66a166` | token and a `paths:` prose sentence (line 275); no key site |
| `/docs/en/settings.md` | 42013 | `df255caa05a7c40c1806810cb587233a3a4f83dc2ea997b0f3d89a5c49071f04` | no `.claude/rules` and no `paths:` |
| `/docs/en/security-guidance.md` | 18436 | `7f697a212d833fab742bfc5d44653771174244f6865bfdc369985cd0844e6fc7` | fetched 10:56:39Z. `key_site` line 141 `paths: ["**/src/tenants/**"]` is a security-plugin field. Token count 0 |
| `https://docs.claude.com/en/docs/claude-code/memory` | 54043 after redirect | not kept | 10:56:39Z, HTTP 200, final `https://code.claude.com/docs/en/memory` — base key |
| `https://docs.anthropic.com/en/docs/claude-code/memory` | 54043 after redirect | not kept | same final base URL |

Japanese copy, same minute, not the chosen row: `https://code.claude.com/docs/ja/memory.md`, HTTP 200, final URL unchanged, 76347 bytes, sha256 `9688097c22060ec7d182f60cbfdeb89607a2df75f79e609eedd50f327fa27407`, key `//code.claude.com/docs/ja/memory` (not in the base list). Same `paths:` block at line 198 (`key_site` True). Prose is Japanese, so a 6–25-word quote's outside `rules` hit is again only an English anchor slug.

`github.com/anthropics/claude-code` contents at `main` (API 200, 10:55:44Z) has `.claude/commands` only, no rules example. Code search API returned 401 without a token. Changelog path in the base list is a change note anyway.

No experimental / preview / deprecated / beta mark on the German page (`\b` scan of `de-memory.body`: no hits).
