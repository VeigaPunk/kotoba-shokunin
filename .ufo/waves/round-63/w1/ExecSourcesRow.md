# ExecSourcesRow
role: scribe
item: Draft S119 registry row and append-only S049 `.md` rejection note

## Findings

1. `corpus/SOURCES.md:12-13` defines the 11-column table; fresh row S118 is at `corpus/SOURCES.md:129`. Round plan `plans/round-63.md:122-129` requires S119 and an appended (not rewritten) S049 note. The draft row below follows the observed column order and the requested status/date/recheck/used-by values.
2. I fetched the primary publisher policy myself. Exact command:
   `date -u +'%Y-%m-%dT%H:%M:%SZ' && curl -L --fail --silent --show-error -o /tmp/kotoba-r63-S119-acta.html -w 'HTTP %{http_code}\nURL %{url_effective}\nContent-Type %{content_type}\n' 'https://actaorthop.org/actao/correctionsandappeals' && wc -c /tmp/kotoba-r63-S119-acta.html && sha256sum /tmp/kotoba-r63-S119-acta.html`
   Output:
   `2026-10-23T23:04:00Z`; `HTTP 200`; `URL https://actaorthop.org/actao/correctionsandappeals`; `Content-Type text/html; charset=utf-8`; `21024 /tmp/kotoba-r63-S119-acta.html`; `39e51269ad0eef9888e011a7bc5e9cd253dbbfb1cd1e3edcf5b76761ad1b9494  /tmp/kotoba-r63-S119-acta.html`.
   Fetched bytes at `/tmp/kotoba-r63-S119-acta.html:251-255` show the Corrections policy: necessary changes get a post-publication notice permanently linked to the original; the following Erratum/Corrigendum clause says the corrected article is not removed. The proposed quote is an exact 19-word substring of line 252. Scope is limited to the publisher's stated correction practice; it does not prohibit authorized changes to article text.
3. S049 evidence is from the non-author spot-check, not a fetch by this seat: `corpus/lessons/round-62-verifier-spotcheck.md:133` records HTTP 200 `text/markdown` (17,252 B / 30,324 B) with `Accept: */*` and HTTP 404 (389 B, `# Page not found`) with `Accept: text/markdown`; `:170-172` routes the reason correction. The appended note preserves that provenance and keeps the distinct-source rejection because S115 already holds `/docs/rules`.
4. No lane production file was edited. This report contains the proposed artifacts; the S119 fetch is in `/tmp` only. No tools were installed and no gates were run.

## Artifacts

Proposed table row, in the exact registry column order:

```md
| S119 | Acta Orthopaedica — Policy on corrections and appeals — https://actaorthop.org/actao/correctionsandappeals | docs | A | Publisher policy on preserving the published record and publishing linked correction notices | § Corrections policy (`correctionsandappeals:252`); fetched 2026-10-23T23:04:00Z (HTTP 200, 21,024 B, sha256 `39e51269ad0eef9888e011a7bc5e9cd253dbbfb1cd1e3edcf5b76761ad1b9494`); quote (19 words): “Any necessary changes will be accompanied with a post-publication notice which will be permanently linked to the original article” | Necessary changes are accompanied by permanently linked correction notices; published articles should remain unaltered to the maximum extent possible | mined | 2026-10-23 | 365d | corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md |
```

Proposed appended paragraph (not an in-place rewrite):

```text
## Corrections (append-only)

- 2026-10-23 — S049 `.md` rejection (reason correction): the rejection is content-negotiation-dependent, not evidence of a dead URL. In the two Cursor `.md`-route probe, `Accept: */*` returned HTTP 200 `text/markdown` (17,252 B / 30,324 B), while `Accept: text/markdown` returned HTTP 404 (389 B, `# Page not found`). The URLs remain non-distinct sources because S115 already records Cursor `/docs/rules`. Evidence: `corpus/lessons/round-62-verifier-spotcheck.md:133`; routed item `:170-172`.
```

## Verdict

PROPOSES — The fetched publisher policy supports a transparent, permanently linked correction notice and preservation of the record; the S049 note matches the recorded negotiation-dependent outcomes. I would change the S049 wording if a like-for-like probe contradicted the spot-check, or the S119 wording if the fetched policy no longer supported the quoted notice/preservation claim.
