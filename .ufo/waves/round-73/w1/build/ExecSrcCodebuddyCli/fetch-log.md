# Fetch log — C1 source opening, seat ExecSrcCodebuddyCli

## Target (assigned)
URL requested: `https://www.codebuddy.ai/docs/zh/cli/skills`
HTTP status: 200
Final URL after redirects: `https://www.codebuddy.ai/docs/zh/cli/skills` (`num_redirects=0`)
Content-Type: `text/html; charset=utf-8`
Bytes: 217520
sha256: `ee9e3b7187c5105bd1147dff41c1ecb793b695a28f3d1804344f543d6e34f2ee`
Access date: 2026-10-25 (local clock at fetch: 2026-10-25T21:00:49-03:00)
User-Agent: `Mozilla/5.0`
Command: `curl -sL --max-time 60 -A 'Mozilla/5.0' -o raw-cli-skills.html -w 'http_status=%{http_code}\nfinal_url=%{url_effective}\nsize=%{size_download}\ncontent_type=%{content_type}\n' https://www.codebuddy.ai/docs/zh/cli/skills`

Stability: a second fetch at 2026-10-25T21:02:01-03:00 returned the same 217520 bytes and the same sha256
(`cmp -s` silent → byte-identical).

## Is it a JS shell?
No. The HTML is VitePress v2.0.0-alpha.20 **server-rendered**: the article body is in the initial response.
Evidence: `grep -c -F '项目级 Skills' raw-cli-skills.html` → 3; `grep -c -F 'allowed-tools'` → 11;
`grep -c -F 'disable-model-invocation'` → 1. No additional fetch, API, sitemap or GitHub file was needed.

Alternate-source probes (all returned the SPA shell, not a text export):
| probe URL | status | bytes | content-type | verdict |
|---|---|---|---|---|
| `.../cli/skills.md` | 200 | 3884 | text/html | SPA not-found shell (lang=en-US, title `Tencent Cloud Code Assistant CodeBuddy – AI Code Editor`, empty `<body>` text) |
| `.../cli/skills.html` | 200 | 217520 | text/html | same article (byte-equal length to the canonical URL) |
| `.../cli/skills?raw=1` | 200 | 217520 | text/html | same article; query param ignored |
| `https://www.codebuddy.ai/docs/llms.txt` | 200 | 3884 | text/html | SPA shell, not llms.txt |
| `https://www.codebuddy.ai/llms.txt` | 200 | 9124 | text/html | SPA shell, not llms.txt |

No `Last updated` / `上次更新` marker exists in the page body (`grep -niE '上次更新|更新日期|Last updated|updated'`
→ the only hit is the UI string `Updated N skill override` on line 541).

## Snapshot
`snapshot.md` — 25241 bytes, 699 lines, sha256 `88468f4f5f80055a86c5107eb87d530485bc8003313a742a214c55a4cfe4f784`
(raw-cli-skills.html sha256 in the same `snapshot.sha256` file). Shaping: see `SNAPSHOT-SHAPING.md`.
