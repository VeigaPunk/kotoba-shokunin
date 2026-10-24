# ScoutS049 — S049 live-context re-probe

role: scout (freshness)
item: re-probe `https://cursor.com/docs/rules.md` under default Accept and `Accept: text/markdown`; one control fetch of `https://cursor.com/docs/rules`
axes: freshness of the served bytes; whether the request-profile-dependent 404 still reproduces; append-only search-log text (no row rewrite)
clock: `date -u` `2026-10-24T03:35:37Z` (probes); request-header confirm `2026-10-24T03:35:57Z`
client: curl 8.23.0 (x86_64-pc-linux-gnu), libcurl/8.23.0 OpenSSL/3.6.5, no `-L`, no custom User-Agent, `--max-time 45`
tools installed: none
lane files mutated: this report only. Bodies under `/tmp/s049-r64/` (scratch).

## Findings

1. **The request-profile-dependent 404 still reproduces.** At `2026-10-24T03:35:37Z`, `https://cursor.com/docs/rules.md` with `Accept: text/markdown` returned HTTP 404, body 389 B, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`, body headed `# Page not found`. That digest is the same 404 body recorded on 2026-10-23 (`.ufo/waves/round-63/w1/ScoutS049.md` rules_md_md row). Response: `content-type: text/markdown; charset=utf-8`, `vary: Accept`, `x-vercel-cache: MISS`, `age: 0`, `date: Sat, 24 Oct 2026 03:35:37 GMT`. `content-length` was absent. `num_redirects=0`, `url_effective` unchanged. curl exit 0.

2. **Default Accept reproduces the 2026-10-23 re-probe, not the 2026-10-22 receipt.** Same URL, no `-H` (curl sent `Accept: */*`, confirmed on the follow-up trace). HTTP 200, body 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`, body headed `# Rules`. Byte-identical to the search-log errata (`corpus/SOURCES.md:233-234`) and to `corpus/lessons/round-63.md` (17,252 B / `dae9d3ec…`, 2026-10-23T23:03:45Z). It is not the held 2026-10-22 receipt on the S049 row (`corpus/SOURCES.md:62`: 17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z). Delta vs that receipt: −151 B; digest prefix differs. `content-type: text/markdown; charset=utf-8`, `vary: Accept`, `x-vercel-cache: HIT`, `age: 1254`, `date: Sat, 24 Oct 2026 03:14:43 GMT`. `content-length` absent. `num_redirects=0`. A second default fetch at `2026-10-24T03:35:57Z` returned the same sha256 and 17,252 B (still HTTP 200). The 200 is a cache HIT aged 1,254 s, not an origin MISS; the bytes a client receives today are still the 2026-10-23 digest.

3. **Control (no `.md`) is HTML, not the markdown receipt.** `https://cursor.com/docs/rules`, default Accept, one fetch: HTTP 200, `content-length: 540892`, body 540,892 B, sha256 `35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2`, `content-type: text/html; charset=utf-8`, `num_redirects=0`, `url_effective` unchanged, body starts `<!DOCTYPE html>`. Size matches the 2026-10-23 extensionless fetch (`.ufo/waves/round-63/w1/ExecSensorS049.md`: 540,892 B, `text/html`, no sha recorded). Byte-identity with that earlier HTML body is unresolved. This control was not fetched with `Accept: text/markdown`.

4. **Neither profile restores 17,403 B / `884c67ca…`.** The S049 row stays the dated original. No second row is implied by this re-probe. The 2026-10-23 errata stands.

## Dated digests

| when (UTC) | url | Accept sent | status | body B | sha256 | vs held receipts |
|---|---|---|---|---|---|---|
| 2026-10-22T20:09:33Z | `…/docs/rules.md` | (row; not re-fetched) | (row) | 17,403 | `884c67ca…` (prefix only on `SOURCES.md:62`; full digest not on that row) | held original |
| 2026-10-23 (errata; probe 23:03:45Z) | `…/docs/rules.md` | default | 200 | 17,252 | `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` | held re-probe |
| 2026-10-23 (errata) | `…/docs/rules.md` | `text/markdown` | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` (full digest in r63 `ScoutS049.md`, not in the search-log sentence) | held 404 |
| 2026-10-24T03:35:37Z | `…/docs/rules.md` | `*/*` (curl default, no `-H`) | 200 | 17,252 | `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` | matches 2026-10-23; does not match 2026-10-22 |
| 2026-10-24T03:35:37Z | `…/docs/rules.md` | `text/markdown` | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` | 404 reproduces; matches 2026-10-23 404 body |
| 2026-10-24T03:35:57Z | `…/docs/rules.md` | `*/*` (trace confirm) | 200 | 17,252 | same `dae9d3ec…` | repeat of the default probe |
| 2026-10-24T03:35:37Z | `…/docs/rules` | `*/*` (curl default) | 200 | 540,892 | `35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2` | control; HTML; size matches 2026-10-23 HTML fetch; sha not previously held |

## Claims

- **Supports** plan `S049 live context` (`plans/round-64.md` Sources + Routed-input): both profiles were re-probed; the 404 is still request-profile-dependent; the search-log append below does not rewrite the S049 row or the 2026-10-23 errata.
- **Supports** the standing errata (`corpus/SOURCES.md:232-242`): default Accept is HTTP 200 / 17,252 B / `dae9d3ec…`; `Accept: text/markdown` is HTTP 404 / 389 B; the 2026-10-22 17,403 B / `884c67ca…` receipt does not reproduce.
- **Does not falsify** that errata. No observation today returns the 17,403 B body.
- **Does not support** minting a new SOURCES row (out of this seat's write; the prior rejection stands on unchanged grounds).

## Exact append text

Append-only. Insert after `corpus/SOURCES.md:243` (end of the 2026-10-23 errata, which is the current EOF and sits under `## Leads (unopened)`, not under `## Search log`). Do not edit lines 62 or 220–243. Do not rewrite the S049 table row.

```markdown
- **2026-10-24 — round-64 S049 live-context re-probe (appended; the S049 row and the 2026-10-23 errata are not rewritten).** Question: does the request-profile split on `https://cursor.com/docs/rules.md` still hold, and does either profile reproduce a held receipt? Where: that URL under curl 8.23.0 default `Accept` (sent `Accept: */*`, no `-H`) and under `Accept: text/markdown`, plus one control fetch of `https://cursor.com/docs/rules` (no `.md`, default Accept). Probed 2026-10-24T03:35:37Z. Default `Accept`: HTTP 200, `content-length` absent, body 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` (`text/markdown; charset=utf-8`; `vary: Accept`; Vercel cache HIT, age 1254, `Date: Sat, 24 Oct 2026 03:14:43 GMT`). `Accept: text/markdown`: HTTP 404, `content-length` absent, body 389 B, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` (body headed `# Page not found`; Vercel cache MISS, age 0, `Date: Sat, 24 Oct 2026 03:35:37 GMT`). The 2026-10-22 receipt (17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z) does not reproduce under either profile. The 2026-10-23 default-Accept receipt (17,252 B, sha256 `dae9d3ec…`) reproduces byte-for-byte, and the request-profile-dependent 404 still reproduces. Control `https://cursor.com/docs/rules`: HTTP 200, `content-length: 540892`, body 540,892 B, `text/html; charset=utf-8`, sha256 `35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2` (0 redirects; same byte count as the 2026-10-23 extensionless HTML fetch, which recorded no digest). No S049 field is rewritten.
```

## Evidence (headers trimmed to status + content-length)

`content-length` was not present on either `.md` response. It is recorded below as absent rather than omitted. Body sizes are `size_download` and `wc -c` (they agree). Untrimmed dumps also carried `vary: Accept` and `content-type` as cited in Findings; those lines are trimmed here per the seat brief.

```text
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-24T03:35:37Z
$ curl --version | head -1
curl 8.23.0 (x86_64-pc-linux-gnu) libcurl/8.23.0 OpenSSL/3.6.5 zlib/1.3.2 brotli/1.2.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 libssh2/1.11.1 nghttp2/1.70.0 ngtcp2/1.25.0 nghttp3/1.18.0 mit-krb5/1.22.2

$ curl -sS -D - -o /tmp/s049-r64/default.body --max-time 45 -w 'writeout http_code=%{http_code} size_download=%{size_download} content_type=%{content_type} url_effective=%{url_effective} num_redirects=%{num_redirects}\n' 'https://cursor.com/docs/rules.md'
HTTP/2 200
content-length: (header absent)
writeout http_code=200 size_download=17252 content_type=text/markdown; charset=utf-8 url_effective=https://cursor.com/docs/rules.md num_redirects=0
curl_exit=0

$ curl -sS -D - -o /tmp/s049-r64/md.body --max-time 45 -H 'Accept: text/markdown' -w 'writeout http_code=%{http_code} size_download=%{size_download} content_type=%{content_type} url_effective=%{url_effective} num_redirects=%{num_redirects}\n' 'https://cursor.com/docs/rules.md'
HTTP/2 404
content-length: (header absent)
writeout http_code=404 size_download=389 content_type=text/markdown; charset=utf-8 url_effective=https://cursor.com/docs/rules.md num_redirects=0
curl_exit=0

$ curl -sS -D - -o /tmp/s049-r64/control.body --max-time 45 -w 'writeout http_code=%{http_code} size_download=%{size_download} content_type=%{content_type} url_effective=%{url_effective} num_redirects=%{num_redirects}\n' 'https://cursor.com/docs/rules'
HTTP/2 200
content-length: 540892
writeout http_code=200 size_download=540892 content_type=text/html; charset=utf-8 url_effective=https://cursor.com/docs/rules num_redirects=0
curl_exit=0

$ wc -c /tmp/s049-r64/default.body /tmp/s049-r64/md.body /tmp/s049-r64/control.body
 17252 /tmp/s049-r64/default.body
   389 /tmp/s049-r64/md.body
540892 /tmp/s049-r64/control.body
558533 total

$ sha256sum /tmp/s049-r64/default.body /tmp/s049-r64/md.body /tmp/s049-r64/control.body
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  /tmp/s049-r64/default.body
4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1  /tmp/s049-r64/md.body
35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2  /tmp/s049-r64/control.body
```

Request-header confirm (second default fetch; not one of the two dated profile fetches):

```text
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-24T03:35:57Z
$ curl -sS -D /tmp/s049-r64/default2.hdr -o /tmp/s049-r64/default2.body --max-time 30 -v 'https://cursor.com/docs/rules.md'
> GET /docs/rules.md HTTP/2
> Host: cursor.com
> User-Agent: curl/8.23.0
> Accept: */*
< HTTP/2 200
< content-type: text/markdown; charset=utf-8
< vary: Accept
content-length: (header absent)
curl_exit=0
$ sha256sum /tmp/s049-r64/default2.body
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  /tmp/s049-r64/default2.body
$ wc -c /tmp/s049-r64/default2.body
17252 /tmp/s049-r64/default2.body
```

## Unresolved

- Whether an origin MISS (cache bypass) of default Accept would still be `dae9d3ec…`. Today's 200 was a Vercel HIT aged 1,254 s. The 404 was a MISS at probe time.
- Byte-identity of the extensionless HTML body with the 2026-10-23 540,892 B fetch. That seat recorded no sha256.
- Full sha256 of the 2026-10-22 17,403 B `.md` body is only the prefix `884c67ca…` on `SOURCES.md:62`. S108/S115 record `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` for `https://cursor.com/docs/rules` at 17,403 B, a different URL. Today's bodies do not have that prefix either way.
- `Accept: text/markdown` on the extensionless control URL was not fetched.

## Verdict

The 2026-10-23 split is still what the server does: default `Accept: */*` → 200 / 17,252 B / `dae9d3ec…`; `Accept: text/markdown` → 404 / 389 B / `4f98eb06…`. The 2026-10-22 receipt does not reproduce. Append the block above; do not rewrite the row.
