# SentW2SourcesHygiene

- **Role:** Sentinel — sources hygiene
- **Item:** S119 snapshot privacy, SOURCES.md round-63 search-log URL hygiene, and URI-reference sweep.
- **Severity:** Informational for S119; **low** for the strict whole-wave text finding below. No credential or session secret was found.
- **Scope:** Read-only inspection of the committed working-copy bytes; no production files, dispatch metadata, lane state, or index changed. No tools installed.

## Verdicts

1. **PASS — S119 body contains no cookie/session/credential/private-key markers or `Set-Cookie` echo.** The snapshot is a public ICMJE HTML page. It does contain the response-specific Cloudflare script at line 310, with `__CF$cv$params` fields `r` and `t`; `t` decodes to Unix time `1792796702` (`2026-10-23T23:05:02Z`). Local evidence does not establish the exact meaning of `r`; it is an opaque per-response value, not an observed credential. No bearer/JWT/API key or session/cookie value was found. **Bound:** the snapshot contains only the body; the fetch receipt did not save HTTP response headers, so this check cannot establish whether the server emitted a `Set-Cookie` header.
2. **PASS — round-63 source record is public.** The new S119 row names the public HTTPS ICMJE page. The round-63 SOURCES search-log addition at lines 221–235 contains no URL literal; it names COPE, NISO, ICMJE, and the existing Cursor source. The fetch receipt lists the three public HTTPS COPE/NISO URLs, and S049 is the public Cursor docs URL. No private/internal URL or credential-bearing query was found.
3. **FAIL under a strict whole-`.ufo/waves/round-63` scan; PASS for authored round-63 text.** The authored round-63 lesson, knowledge entry, SOURCES/LOG/plan text, W1 evidence, snapshots, receipts, and controls have no matching URI reference. The broader wave-directory scan found two matches, solely in the copied task payloads: `w2-dispatch.json:477` and `w2-spec.json:201`. They are prompt echoes, not source/lesson content, but make an unqualified “none anywhere in the round-63 directory” claim false.

## Attack commands and output

Searches below were executed with the repository `functions.grep` tool (its output is quoted verbatim where it is a no-match result). Shell-equivalent `grep` expressions are shown for reproducibility; no shell `grep`/`sed` was used.

### 1. S119 privacy markers

```text
$ grep -niE '(set-cookie|cookie|session|authorization|bearer|token|access[_-]?key|api[_-]?key|csrf|private|secret)' .ufo/waves/round-63/snapshots/S119.page
functions.grep output:
No matches found
```

The complementary marker search for Cloudflare/request metadata did find the line-310 script. The relevant body excerpt, from `.ufo/waves/round-63/snapshots/S119.page:310`, is:

```text
window.__CF$cv$params={r:'a4f4625d0c646d39',t:'MTc5Mjc5NjcwMg=='}
```

Executed local checks:

```text
$ sha256sum .ufo/waves/round-63/snapshots/S119.page
d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2  .ufo/waves/round-63/snapshots/S119.page

$ printf '%s' 'MTc5Mjc5NjcwMg==' | base64 -d && printf '\n' && date -u -d @1792796702 '+%Y-%m-%dT%H:%M:%SZ'
1792796702
2026-10-23T23:05:02Z
```

### 2. SOURCES round-63 URLs

```text
functions.grep(path="/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md:221-235", pattern="https?://|www\\.", case=false, gitignore=false, skip=0)
No matches found
```

Public URL evidence from the committed S119 row and its source probe:

```text
SOURCES.md:131: https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
ExecSourceS119.md:7: https://publicationethics.org/guidance/correction (HTTP 403)
ExecSourceS119.md:7: https://publicationethics.org/retraction-guidelines (HTTP 403)
ExecSourceS119.md:7: https://www.niso.org/publications/rp-8-2008-jav (HTTP 404)
SOURCES.md:62: https://cursor.com/docs/rules.md (S049)
```

These are publisher/standards-body documentation URLs over HTTPS. The SOURCES search-log text records the unsuccessful public probes and fallback; no URL is embedded in that log paragraph itself.

### 3. URI-reference sweep

For a literal-safe search expression, the grep pattern used was `\\x6f\\x70:\\x2f\\x2f` (hex escapes for the scheme characters). Authored-text search output:

```text
functions.grep(path="/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-63.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/knowledge/compound-clause-citation-round63.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/LOG.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-63.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/w1; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/snapshots; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/receipts; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/controls", pattern="\\x6f\\x70:\\x2f\\x2f", case=false, gitignore=false, skip=0)
No matches found
```

The whole-wave query and its match locations were:

```text
functions.grep(path="/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63", pattern="\\x6f\\x70:\\x2f\\x2f", case=false, gitignore=false, skip=0)
.ufo/waves/round-63/w2-dispatch.json:477
.ufo/waves/round-63/w2-spec.json:201
```

The matching text is the task wording itself. The tool's matched-line text is not repeated raw because that would add another forbidden occurrence to this report. Relevant match excerpts, with only the scheme characters rendered as JSON Unicode escapes, are: `w2-dispatch.json:477 … verify no \u006f\u0070:\u002f\u002f references anywhere in the round-63 landed text …`; `w2-spec.json:201 … verify no \u006f\u0070:\u002f\u002f references anywhere in the round-63 landed text …`. No other round-63 artifact matched.

## Exploit path and impact

No exploit path to credentials, authenticated access, or a user session is evidenced. The S119 body exposes a per-response request-metadata value and time in a public page; at most this can aid correlation of that particular fetch. The URI matches are confined to persisted task-prompt copies and do not identify a vault item or credential.

## Smallest safe correction / bound

No S119 secret redaction is justified by the observed bytes. Preserve the snapshot and hash as a fetch receipt, but disclose the header limitation in the source record if a reader might infer a header audit. Exact proposed note:

> The saved HTML body contains a per-response Cloudflare script at line 310; response headers were not retained, so this snapshot cannot establish whether the server emitted Set-Cookie.

For the two prompt echoes, the smallest text-only correction is to replace the URI example in the task payload with this exact wording:

> verify that no 1Password-vault URI references appear anywhere in the round-63 landed text.

This report does not modify those payloads; only the assigned report file was written.
