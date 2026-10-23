# ExecSensorS049
role: freshness probe
item: Re-verify S049 Cursor rules routes
axes: freshness; representation reproducibility

## Findings

1. **The recorded `.md` receipt does not reproduce on the current default curl request.** At `2026-10-23T23:03:45Z`, `curl -sS -L` returned HTTP 200 from the same final URL but 17,252 B and SHA-256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`; S049 records 17,403 B and `884c67ca…`, fetched `2026-10-22T20:09:33Z` (`corpus/SOURCES.md:62`). Delta: −151 B; digest differs. The response is `text/markdown; charset=utf-8`. This matches the spot-check's earlier `Accept: */*` result for this route (`corpus/lessons/round-62-verifier-spotcheck.md:133`), so the evidence indicates request/representation sensitivity, not by itself a proven content edit.
2. **The extensionless URL serves a different-sized HTML response without redirecting.** `https://cursor.com/docs/rules` returned HTTP 200, final URL unchanged, 540,892 B, `text/html; charset=utf-8`.
3. **Errata/recheck:** the row's 90-day scheduled interval is not due (the recorded fetch was one day ago). Nevertheless, append a dated errata/recheck note now documenting the current 17,252 B digest and request form, and retain the 17,403 B value as the original dated receipt rather than rewriting history. The routed spot-check already records the content-negotiation split: `Accept: */*` → 17,252 B, while `Accept: text/markdown` → HTTP 404 (`round-62-verifier-spotcheck.md:133,170-172`).

## Artifacts

Verbatim probe commands and outputs:

```text
$ date -u '+%Y-%m-%dT%H:%M:%SZ'
2026-10-23T23:03:45Z

$ curl -sS -L --max-time 60 -o /tmp/execsensor-s049-r63-rules.md -w 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\ncontent_type=%{content_type}\n' 'https://cursor.com/docs/rules.md'
url_effective=https://cursor.com/docs/rules.md
http_code=200
size_download=17252
content_type=text/markdown; charset=utf-8
$ sha256sum /tmp/execsensor-s049-r63-rules.md
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  /tmp/execsensor-s049-r63-rules.md
$ wc -c /tmp/execsensor-s049-r63-rules.md
17252 /tmp/execsensor-s049-r63-rules.md

$ curl -sS -L --max-time 60 -o /tmp/execsensor-s049-r63-rules-noext.body -w 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\ncontent_type=%{content_type}\n' 'https://cursor.com/docs/rules'
url_effective=https://cursor.com/docs/rules
http_code=200
size_download=540892
content_type=text/html; charset=utf-8
$ wc -c /tmp/execsensor-s049-r63-rules-noext.body
540892 /tmp/execsensor-s049-r63-rules-noext.body
```

No lane source files were edited; no tools were installed or updated.

## Verdict

**ATTACKS** — the held `.md` byte count and hash are not reproduced by the current default curl request. I would change this verdict if an explicitly documented request profile reproduces the held 17,403 B / `884c67ca…` receipt, or a follow-up capture confirms that the differing body is only an Accept-dependent representation.