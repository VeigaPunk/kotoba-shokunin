Result: DONE — Cursor: NOT ELIGIBLE (no non-base page on a pinned host has `.cursor/rules` and `globs` in A1 key form; the only `globs:` site's final URL is the base rules page)

Seat RecensusCursor. Read-only on the lane. No tools installed (pacman paused; nothing missing). Bytes under `/fast/scratch/hyaku/kotoba-r60/RecensusCursor/`. Counter helpers imported read-only from `verifiers/check_scoped_rules.py` (not modified). Lead token `.cursor/rules` (`token_well_formed` True). Lead key `globs`.

`date -u` for the scored refetch batch: `Fri 23 Oct 2026 10:57:38 AM UTC` (batch finished `Fri 23 Oct 2026 10:57:39 AM UTC`). User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`. Header `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`. `grep -cxF` prints `0` with exit 1 (grep's no-match status) and `1` with exit 0.

## Why none qualify

A page counts only when its own `url_key` and the final URL's `url_key` are both absent from `.ufo/waves/round-60/w0b-base-url-keys.txt`, the page names `.cursor/rules`, a line holds `globs` in A1 key form whose first value token contains `*`, a 6–25-word quote holds the token and a rule/instruction word outside it, and there is an action line. The only fetched bytes where `c.key_site(lines, L, "globs")` is True are the base rules page (line 85, `globs: src/components/**/*.tsx`). Every other pinned-host page checked fails that key site. `c.any_key_site(text, "globs")` is False on each non-base body below.

## Candidates

### 1. Help rules — base URL, and no `globs` key

- Requested and final: `https://cursor.com/help/customization/rules`
- `curl -sSL` write-out: `200 https://cursor.com/help/customization/rules 6285` (exit 0)
- sha256 `c6d2b0697e0b8f51d0d9ad7701a850cd81c389ec075e24b15e24bbd4e5afcdfc` (6285 bytes). Same sha as CensusCursor's help page.
- `c.url_key` → `//cursor.com/help/customization/rules` (exit 0). `grep -cxF` → `1` (exit 0). Already a base SOURCES URL.
- `c.any_key_site(..., "globs")` → False. The body contains no `globs` (`count` 0). Token is printed, for example line 29 (`sed -n '29p'`, `wc -w` → 11): `6. Save the file. It's stored in `.cursor/rules/` in your project.` That sentence is not a key site.

### 2. Legacy context path — request key is new, final URL is the base rules page

- Requested: `https://cursor.com/docs/context/rules`
- `curl -sSL` write-out: `200 https://cursor.com/docs/rules 17403` (exit 0)
- sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` (17403 bytes). Same sha as CensusCursor's `rules.md`.
- Request `c.url_key` → `//cursor.com/docs/context/rules`, `grep -cxF` → `0` (exit 1).
- Final `c.url_key('https://cursor.com/docs/rules')` → `//cursor.com/docs/rules`, `grep -cxF` → `1` (exit 0).
- The body does hold the lead key. `c.key_site(lines, 85, "globs")` → True. `sed -n '85,88p'`:

```
globs: src/components/**/*.tsx
alwaysApply: false
---
```

- Disqualified because the final URL is a base SOURCES URL. `docs.cursor.com/context/rules` (same minute, earlier probe `Fri 23 Oct 2026 10:55:20 AM UTC`) ends at `https://cursor.com/docs` (the index, 42554 bytes), not this page.

### 3. CLI using — non-base, quote passes, no `globs` key

- Requested and final: `https://cursor.com/docs/cli/using`
- write-out: `200 https://cursor.com/docs/cli/using 5771`
- sha256 `b070cb1f882dd8e8b9ab7434ff6f96fe1f181c4907ee242773ae6bbbedb47b0b`
- `c.url_key` → `//cursor.com/docs/cli/using`, `grep -cxF` → `0` (exit 1). `host_ok` True. Not a change-note path.
- Token line 38 (`sed -n '38p'`, `wc -w` → 56). Verbatim 16-word slice on that line (`printf | wc -w` → 16; `len(quote.replace('`','').split())` → 16): `You can create rules in the `.cursor/rules` directory to provide context and guidance to the agent.`
- `c.token_span` on the backtick-stripped quote → `(28, 41)`; `c.rule_word_outside` → True (`rules` in `create rules`). `c.norm(quote) in c.norm_page(page)` → True.
- `c.key_site(lines, 38, "globs")` → False. `c.any_key_site(text, "globs")` → False. Same for `alwaysApply`, `paths`, `description`. No A1 key site, so no scope-key line to cite. The same line's second sentence is only prose about loading rules from their configuration.

### 4. Cloud-agent best practices — non-base, quote passes, no `globs` key

- Requested and final: `https://cursor.com/docs/cloud-agent/best-practices`
- write-out: `200 https://cursor.com/docs/cloud-agent/best-practices 3683`
- sha256 `e3a197dbd3769d30846b8e7a01a2796318da85924a5fd9ec65389ebc0aae1367`
- `c.url_key` → `//cursor.com/docs/cloud-agent/best-practices`, `grep -cxF` → `0` (exit 1). `host_ok` True.
- Whole of line 33 (`sed -n '33p'`, `wc -w` → 21; counter split → 21), on the page, span `(18, 31)`, `rule_word_outside` True (`Repo rules`): `- **Repo rules**: `.cursor/rules/*.mdc` files committed to the repository, these apply to all agents using that repository. Best for repo/project-specific conventions.`
- `c.key_site(lines, 33, "globs")` → False. `c.any_key_site(text, "globs")` → False. No key site.

### 5. Learn customizing-agents — non-base, quote passes, no `globs` key

- Requested and final: `https://cursor.com/learn/customizing-agents`
- write-out: `200 https://cursor.com/learn/customizing-agents 7322`
- sha256 `19c146226526fdb26cbc8872444cb6a9d71d44b1891156649b5d0d9ae41a43d5`
- `c.url_key` → `//cursor.com/learn/customizing-agents`, `grep -cxF` → `0` (exit 1). `host_ok` True.
- Line 11 is 34 words (`sed -n '11p' | wc -w` → 34), over the 25-word cap. A 21-word verbatim slice is on the page (`printf | wc -w` → 21; span `(10, 23)`; `rule_word_outside` True via `instructions`): `stored in `.cursor/rules/` that the agent sees at the start of every conversation. You can think of them as always-included instructions`
- That sentence describes always-included rules, not a path glob. `c.any_key_site(text, "globs")` → False.

### 6. CLI configuration — non-base, token absent

- Requested and final: `https://cursor.com/docs/cli/reference/configuration`
- write-out: `200 https://cursor.com/docs/cli/reference/configuration 7756`
- sha256 `aab79ccc8949c23f30c45e0928ea80cefb5ee4ee6ff1723a3864ac61851f2a87`
- `c.url_key` → `//cursor.com/docs/cli/reference/configuration`, `grep -cxF` → `0` (exit 1).
- Body does not contain `.cursor/rules`. `c.any_key_site` for `globs`, `alwaysApply`, `paths`, and `description` is False.

### 7. Self-hosted pool — non-base, `alwaysApply: true` is not a glob value

- Requested and final: `https://cursor.com/docs/cloud-agent/self-hosted/pool`
- write-out: `200 https://cursor.com/docs/cloud-agent/self-hosted/pool 84833`
- sha256 `2297f5dd07f8532f16721c148a99a5a88f90e0adeaa4f48d83a39603030cb34e`
- `c.url_key` → `//cursor.com/docs/cloud-agent/self-hosted/pool`, `grep -cxF` → `0` (exit 1). `host_ok` True.
- Line 197 names `.cursor/rules` but is 27 words (`sed -n '197p' | wc -w` → 27), over the cap.
- `sed -n '199,202p'`:

```
```md title=".cursor/rules/repo-info.mdc"
---
alwaysApply: true
---
```

- `c.key_site(lines, 201, "alwaysApply")` → False (value `true` has no `*`). `c.key_site(lines, 201, "globs")` → False. `c.any_key_site(text, "globs")` → False.

### 8. Skills help — `paths:` is a skill key, not `.cursor/rules` / `globs`

- Requested and final: `https://cursor.com/help/customization/skills`
- write-out: `200 https://cursor.com/help/customization/skills 6569`
- sha256 `7d551fc7939d4632228c7f178f89475113a1ad503000f890271ee95a4aee3a49`
- `c.url_key` → `//cursor.com/help/customization/skills`, `grep -cxF` → `0` (exit 1).
- Body contains `.cursor/skills` and does not contain `.cursor/rules`. `c.token_well_formed(".cursor/skills")` → False and `c.token_well_formed(".cursor/skills/")` → False (segment word `skills`).
- `sed -n '48,54p'` shows `paths:` then `- "**/*.tsx"`. `c.key_site(lines, 52, "paths")` → True. That is the skills frontmatter, not the rules key.
- Lines 90 and 93 mention `` `globs` `` and `` `alwaysApply: false` `` as prose. `c.key_site(lines, 90, "globs")` → False. `c.key_site(lines, 90, "alwaysApply")` → False. `c.any_key_site(text, "globs")` → False.

## Sitemap sweep

`https://cursor.com/llms.txt` fetched `Fri 23 Oct 2026 10:54:57 AM UTC`: HTTP 200, final unchanged, 24815 bytes, sha256 `38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d`. It lists `https://cursor.com/docs/rules.md` and `https://cursor.com/help/customization/rules.md`; both drop `.md` onto base keys. `https://cursor.com/docs/rules.md` itself is HTTP 404 (probe `Fri 23 Oct 2026 10:57:10 AM UTC`, final unchanged, 389 bytes).

`https://cursor.com/docs/sitemap.xml` fetched `Fri 23 Oct 2026 10:55:52 AM UTC`: HTTP 200, final unchanged, 64892 bytes, sha256 `79a480cd4ba2da3899960d28a34edb052969e4cf12f7807cf797d8f25a1af6c1`. 376 `<loc>` URLs. Nine are base keys (`//cursor.com/docs/rules` and `//cursor.com/help/customization/rules` among them). The other 367 were fetched with the same Accept header. Bodies were kept when they contained `globs` (any case), `.cursor/rules`, or `alwaysapply` (23 bodies). A search of those bodies for `globs:` returned no matches, so none has `globs` in key form. The other 344 non-base bodies contain neither the word `globs` nor `.cursor/rules`.

Other pinned-host fetches in the `Fri 23 Oct 2026 10:55:20 AM UTC` batch, all HTTP 200, final URL unchanged, `globs` key absent:

| URL | bytes | sha256 | what it has |
|---|---|---|---|
| `https://cursor.com/docs/agent/prompting` | 4485 | `438f77bf7295d28002c81ce0658134ce7debe6dfa76bae926058b918ed378410` | neither token nor `globs` |
| `https://cursor.com/docs/customize-cursor` | 5200 | `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e` | neither |
| `https://cursor.com/docs/bugbot` | 39369 | `39fe4c9643ae79b0fbb4f740a82bc2e8756f807b262b71dc1b39302978410106` | says `` `*.mdc` files in `.cursor/rules/` `` do not apply to Bugbot; no `globs:` |
| `https://cursor.com/help/ai-features/bugbot` | 4147 | `a0842519aa4f567c5e06bcfca1ae1c9e5e5607bb00af4476d3586138e0f2ee38` | same statement; no `globs:` |
| `https://cursor.com/docs/agent/overview` | 7519 | `2b474c20c095efbc1280b9d6d6f8d7670da88a35e82ff66560282f97a90bbc91` | neither |
| `https://cursor.com/help/customization/context` | 1315 | `d50808dbe27d415ef7c28a5dfca1154c54376949b1bcfd1ff28ea134e0ba6ecc` | neither |
| `https://cursor.com/help/integrations/cli` | 2085 | `ac37e15bece8cd8b4b5b335d7541b9e8447c866b444193be6e5b9d4b750c331e` | neither |
| `https://cursor.com/docs/enterprise` | 18410 | `a811fbc1830886ffc7d332d9b0ce668bd80b90c21755b15e907f5da7b0a3b113` | neither |

`c.token_well_formed(".cursor/BUGBOT.md")` is True, but the Bugbot page documents directory traversal of `.cursor/BUGBOT.md`, not a `globs` key, and it says `.cursor/rules` does not apply there. Not the lead.

Changelog and release-note URLs that mention the token (`/docs/cli/changelog`, `/docs/release-notes/origin`) are change-note paths (`changelog` / `release` in the path) and were not scored as candidates.

## Calls pasted

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B -c "import sys; sys.path.insert(0,'verifiers'); import check_scoped_rules as c; print(c.url_key('https://cursor.com/docs/cli/using'))"
```

exit 0, output `//cursor.com/docs/cli/using`.

```
grep -cxF '//cursor.com/docs/cli/using' .ufo/waves/round-60/w0b-base-url-keys.txt
```

exit 1, output `0`. The same pair for `//cursor.com/docs/cloud-agent/best-practices`, `//cursor.com/learn/customizing-agents`, `//cursor.com/docs/cli/reference/configuration`, `//cursor.com/docs/cloud-agent/self-hosted/pool`, `//cursor.com/help/customization/skills`, and `//cursor.com/docs/context/rules` is exit 1, output `0`. For `//cursor.com/help/customization/rules` and `//cursor.com/docs/rules` it is exit 0, output `1`.

```
python3 -B -c "import sys; sys.path.insert(0,'verifiers'); import check_scoped_rules as c; lines=open('/fast/scratch/hyaku/kotoba-r60/RecensusCursor/scored/cli-using.body').read().splitlines(); print(c.key_site(lines, 38, 'globs')); print(c.any_key_site(open('/fast/scratch/hyaku/kotoba-r60/RecensusCursor/scored/cli-using.body').read(), 'globs'))"
```

output `False` then `False`. The same `any_key_site(..., 'globs')` is False for best-practices, learn-customizing, cli-config, pool, help-rules, and skills-help, and True only for the context-rules body whose final URL is `https://cursor.com/docs/rules`.
