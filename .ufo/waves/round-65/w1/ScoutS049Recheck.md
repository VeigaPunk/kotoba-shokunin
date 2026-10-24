# ScoutS049Recheck — S049 request-profile re-probe (round 65, wave 1)

**Result: REPRODUCES — byte-identical on both request profiles.** The 2026-10-24 receipt
(17,252 B, `dae9d3ec…`) still reproduces under the default `Accept` profile at
2026-10-24T07:36:43Z, and the `Accept: text/markdown` 404 reproduces byte-identical too.
New evidence vs. round 64: both responses were Vercel cache **MISS** (age 0), which closes
the residual r64 `ScoutS049.md:111` left open ("whether an origin MISS of default Accept
would still be `dae9d3ec…`") — it is. No field of the row is due for rewrite.

Seat: `ScoutS049Recheck` (scout, leaf; no subagent dispatch). Judged on freshness.
Read-only web fetch + read-only lane inspection; this report is the only lane file
written; scratch bodies under `/tmp/s049-r65/`. No git/jj write, no tool installed or
upgraded (pacman pause honored; nothing needed), no model call, no browser.

## 1. The row and the held receipts

- `corpus/SOURCES.md:62` — S049, `https://cursor.com/docs/rules.md`, `docs`, tier A,
  `mined`; anchor records the 2026-10-22T20:09:33Z fetch: 17,403 B, sha256 `884c67ca…`
  (prefix only on the row). `recheck` field: `90d` from 2026-10-22 → scheduled recheck
  not due until ~2026-01-20.
- `corpus/SOURCES.md:241-252` and `:283-295` — the 2026-10-23 errata (the sweep note is
  present twice; a known duplication): default `Accept` → 200 / 17,252 B /
  `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`;
  `Accept: text/markdown` → 404 / 389 B.
- `corpus/SOURCES.md:335` — the 2026-10-24T03:35:37Z round-64 re-probe append: same two
  digests; 200 was a Vercel HIT (age 1,254), 404 a MISS; control `…/docs/rules` →
  540,892 B HTML, `35ff98b0…`.

## 2. Probes (run 2026-10-24T07:36:47Z, wall clock; server `Date:` 07:36:43 GMT)

```
$ curl -sS -D headers.default -o body.default --max-time 45 \
    -w 'http_code=%{http_code} size=%{size_download} ct=%{content_type} url=%{url_effective} redirects=%{num_redirects}\n' \
    'https://cursor.com/docs/rules.md'
http_code=200 size=17252 ct=text/markdown; charset=utf-8 url=https://cursor.com/docs/rules.md redirects=0
curl_exit=0

$ curl -sS -D headers.md -o body.md --max-time 45 -H 'Accept: text/markdown' \
    -w 'http_code=%{http_code} size=%{size_download} ct=%{content_type} url=%{url_effective} redirects=%{num_redirects}\n' \
    'https://cursor.com/docs/rules.md'
http_code=404 size=389 ct=text/markdown; charset=utf-8 url=https://cursor.com/docs/rules.md redirects=0
curl_exit=0

$ sha256sum body.default body.md
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  body.default
4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1  body.md

$ wc -c body.default body.md
17252 body.default
  389 body.md

$ head -2 body.default ; head -2 body.md
# Rules
# Page not found
```

Response headers (trimmed):

```
default: HTTP/2 200 | age: 0 | cache-control: public, max-age=3600 |
         content-type: text/markdown; charset=utf-8 | server: Vercel |
         vary: Accept | x-vercel-cache: MISS | date: Sat, 24 Oct 2026 07:36:43 GMT
markdown: HTTP/2 404 | age: 0 | cache-control: public, max-age=0, must-revalidate |
         content-type: text/markdown; charset=utf-8 | server: Vercel |
         vary: Accept | x-vercel-cache: MISS | date: Sat, 24 Oct 2026 07:36:43 GMT
```

## 3. Dated digests table

| When (UTC) | URL | Accept sent | HTTP | Bytes | sha256 | Cache | Verdict vs held receipts |
|---|---|---|---|---|---|---|---|
| 2026-10-22T20:09:33Z | `…/rules.md` | (row) | (row) | 17,403 | `884c67ca…` prefix only | — | held original; does not reproduce |
| 2026-10-23T23:03Z | `…/rules.md` | default / `*/*` | 200 | 17,252 | `dae9d3ec…ce0` | — | held re-probe |
| 2026-10-23T23:03Z | `…/rules.md` | `text/markdown` | 404 | 389 | `4f98eb06…fb1` | — | held 404 |
| 2026-10-24T03:35:37Z | `…/rules.md` | default (`*/*`) | 200 | 17,252 | `dae9d3ec…ce0` | Vercel HIT age 1254 | reproduces |
| 2026-10-24T03:35:37Z | `…/rules.md` | `text/markdown` | 404 | 389 | `4f98eb06…fb1` | MISS | reproduces |
| 2026-10-24T03:35Z | `…/rules` (control) | default | 200 | 540,892 | `35ff98b0…` | — | HTML control |
| **2026-10-24T07:36:43Z** | `…/rules.md` | default (`*/*`) | **200** | **17,252** | **`dae9d3ec…ce0`** | **MISS, age 0** | **reproduces — first MISS confirmation** |
| **2026-10-24T07:36:43Z** | `…/rules.md` | `text/markdown` | **404** | **389** | **`4f98eb06…fb1`** | **MISS, age 0** | **reproduces** |

## 4. Is a recheck note due?

- **Scheduled recheck:** no — the row's `recheck 90d` window runs to ~2026-01-20.
- **Corrective errata:** none needed — the standing errata and the r64 append remain
  exactly correct; nothing they state is contradicted.
- **Optional search-log append:** warranted under the lane's own convention (each
  wave's probe gets a dated append; r64 did so at `SOURCES.md:335`). A round-65 append
  would record: both digests byte-identical at 07:36:43Z **and both on cache MISS** —
  resolving the one open residual r64 logged (`ScoutS049.md:111`: the 17,252 B body had
  only been observed on a Vercel HIT). Today shows the split is served at origin, not a
  stale-edge artifact. My bounds say "the row is not rewritten"; a search-log append is
  not a row rewrite, but I leave it unwritten per the read-only scope and report the
  draft below for the L1.

### Draft append (not written)

```markdown
- **2026-10-24 — round-65 S049 re-probe (appended; the row, the 2026-10-23 errata and
  the 2026-10-24T03:35Z note are not rewritten).** `https://cursor.com/docs/rules.md`
  re-probed 2026-10-24T07:36:43Z. Default `Accept` (`*/*`, no `-H`): HTTP 200, 17,252 B,
  sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`, Vercel cache
  MISS (age 0) — closes the open residual that only a cache HIT had been observed for
  the 200. `Accept: text/markdown`: HTTP 404, 389 B, sha256
  `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`, MISS. Both `vary:
  Accept`. The request-profile split holds; the 2026-10-22 17,403 B receipt still does
  not reproduce.
```

## 5. Claims supported / not falsified

- **Supports** the standing errata (`corpus/SOURCES.md:241-252,283-295`) and the r64
  append (`:335`): the request-profile split is live at probe time.
- **Supports** the r64 scout's prediction that a MISS would return the same 200 body —
  now directly observed (both directions MISS, both digests identical). [Inference in
  r64; observed here.]
- **Does not falsify** the S049 row: its recorded receipt is dated 2026-10-22 and the
  errata already record that it no longer reproduces; nothing today restores 17,403 B.
- **No new source, no row minting** — out of scope; the rejection of a second row from
  the `.md` spelling stands (S108/S115 hold `…/docs/rules`, S088 the non-`.md` URL).

## 6. Side observation (pre-existing, not mine to fix)

The 2026-10-23 round-63 sources-sweep + S049-errata note appears twice in the search
log (`SOURCES.md:229-252` and `:271-295`, byte-similar blocks). `CriticW2Frontier` F3 /
the `:185` placement note concern round-64 notes landing under `## Leads`; this
duplication is a separate, older artifact. Recorded as context only.

## 7. Limits

- One fetch per profile (curl 8.x, same-second `Date:`). No retry, no `Cache-Control:
  no-cache` bypass probe — today's MISSes already give origin evidence.
- Full sha256 of the 2026-10-22 17,403 B body remains only the `884c67ca…` prefix on the
  row; neither today's nor prior probes can complete it.
- `Accept: text/markdown` on the extensionless `…/docs/rules` control remains unfetched
  (same residual as r64).
