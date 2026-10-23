# Round 61 — ScribeS115 report

## Behavior and scope

Attempt 1, 2026-10-23. This leaf seat drafted the Cursor source row, Gate line, target snapshot path, and the Cursor-specific A1 key-set entry. I also attacked the source/URL boundary against the frozen A1/A3/A4 rules and reviewed the recorded round-60 key/action failures, the C2 checker’s static assertions, and the C3 scope boundary. This is a relay, not integration or a round verdict.

Only this report was written in the lane. The fetched page and the `.md` response body were stored under `/fast/scratch/hyaku/kotoba-r61/ScribeS115/`; those scratch files are untrusted working copies, not committed evidence. The L1 must land/refetch the page at the proposed snapshot path before it is used as a committed C1 input.

## Cursor fetch and quote measurements

The counter’s exact request settings were read from `verifiers/check_scoped_rules.py:321-324`: browser User-Agent and `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`; its `-w` trailer is `\n%{http_code} %{url_effective}`. I used the canonical no-suffix URL.

Command, from `/home/vgpnk/Projects/shokunin`:

```sh
mkdir -p /fast/scratch/hyaku/kotoba-r61/ScribeS115 && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page -w '\n%{http_code} %{url_effective}' https://cursor.com/docs/rules && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && date -u
```

Pasted output (the counter-style `-w` string has a leading newline but no trailing newline, so the SHA output is concatenated with the URL):

```text
200 https://cursor.com/docs/rules884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page
17403 /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page
Fri 23 Oct 2026 07:09:41 PM UTC
```

Command exit: `0`. The observed HTTP status was 200, body size 17,403 bytes, SHA-256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`, final URL `https://cursor.com/docs/rules`.

I separately checked the suffix URL called out in the assignment, with the same counter request headers:

```sh
curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS115/rules-md.body -w '\n%{http_code} %{url_effective}' https://cursor.com/docs/rules.md && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS115/rules-md.body && date -u
```

Pasted output (same no-trailing-newline behavior):

```text
404 https://cursor.com/docs/rules.md389 /fast/scratch/hyaku/kotoba-r61/ScribeS115/rules-md.body
Fri 23 Oct 2026 07:11:03 PM UTC
```

Command exit: `0`; HTTP status `404`, 389-byte response body. `curl` exits zero for an HTTP 404 here because `--fail` was not used; the HTTP status, not the process status, establishes the route result.

Quote location/count command:

```sh
sed -n '131p' /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && sed -n '131p' /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page | wc -w && date -u
```

Pasted output:

```text
Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
16
Fri 23 Oct 2026 07:11:03 PM UTC
```

Command exit: `0`. The quote is unshaped and 16 whitespace-delimited words. It is from the fetched page’s `### Glob pattern examples` section; line 32 separately grounds `.cursor/rules` and `.mdc` files. The quote is draft input until the snapshot bytes are committed and re-opened by the L1.

## Draft deliverables

### Target: `.ufo/waves/round-61/snapshots/S115.page`

Fetch bytes above: 17,403 B, SHA-256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`. They are byte-identical by digest and size to the existing S108 pin. The scratch copy is at `/fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page`; it is not a lane artifact or evidence substitute.

### Target: `corpus/SOURCES.md` — proposed S115 row

```markdown
| S115 | Cursor Docs — Rules — https://cursor.com/docs/rules | docs | A | Cursor project rule files under `.cursor/rules` and documented `globs` path-pattern scoping | § Project rules (`rules.md:30-32`); rule metadata (`:52-70`); auto-attached example (`:83-87`); § Glob pattern examples (`:129-141`); fetched 2026-10-23T19:09:41Z, HTTP 200, 17,403 B, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`; exact bytes `.ufo/waves/round-61/snapshots/S115.page` | re-opens S108 — Cursor project rule files live under `.cursor/rules` as `.mdc` files, and `globs` scopes rules to specific files or directories; multiple patterns are comma-separated | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md |
```

This row is a draft for joint integration with the named entry/lesson; `mined` is valid only if the L1 lands those `used-by` paths. If not, the row must not claim a nonexistent mined use.

### Target: `corpus/lessons/round-61.md` — proposed Gate line

```markdown
- S115 — https://cursor.com/docs/rules — fetched 2026-10-23T19:09:41Z — `.ufo/waves/round-61/snapshots/S115.page:131` (16 words): “Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.”
```

### Target: `verifiers/check_scoped_rules.py` v3 — Cursor A1 key-set entry

```python
"Cursor": frozenset({"globs"}),  # S115: .cursor/rules; rules.md:32,54-70,83-87,129-141
```

Keep this mapping client-specific. S115 supports Cursor’s `globs`; it does not authorize `paths` or `applyTo` for Cursor, nor does it turn the cross-client union into a valid key set for any client.

## Attack findings and evidence limits

### C1 / round-60 evidentiary ground

- The frozen plan requires A1’s canonical key set to be per-client and grounded in S112–S115. This source grounds Cursor’s `globs`. The existing `corpus/SOURCES.md` S108 URL is exactly `https://cursor.com/docs/rules`; S049 instead records `https://cursor.com/docs/rules.md`. My live check saw 200 at the S108 URL and 404 at the `.md` URL. Therefore S115 should re-open S108, with byte-identical URL text, rather than re-open S049. This also avoids asserting that the old `.md` route is currently available.
- The new fetch returned the same 17,403-byte digest as S108. It is a dated re-open, not new page content. The source row must not imply a content change. Under A4’s planned date comparison, the fact that this same digest was already introduced in an earlier round-60 path on the same calendar date is compatible with the date-only threshold; neither that lineage nor this fetch proves wall-clock fetch order. Keep the plan’s explicit A4 limit (commit-record consistency, not unforgeable fetch time). The L1 must pin the committed S115 path/digest and the counter’s byte-introduction lookup before claiming A4 coverage.
- The r60 `controls-v2/SUMMARY.md` reports CtlReopenForged d and CtlReopenHeldKey b met the v2 predicate (`--fetch` exit 0, 3/3); it does not establish their v3 outcomes. The r60 `build/ExecKeyForms.md` reports that wrong Scope keys `patterns` and `claudeMdExcludes` still backed a row end-to-end, and that 6/12 invented action cells passed. These are the documented reasons A1/A2 need stronger arms; I did not re-run the controls or v2 counter.
- The round-60 `controls/SUMMARY.md` reports the CtlWrongKey and CtlInventedAction seats cancelled, leaving those v1 pre-data control worlds without receipts. Do not present those two cancelled seats as executed controls. The round-60 closure §7–§8 independently names the routed defects and M90 chronology gap.
- Attack condition for the C1 integration: an allowlist that is only the global set `{paths, applyTo, globs}` would not implement the frozen per-client contract. The Cursor row above only grounds `globs`; the checker must bind the allowed key to the client as well as require the cited line’s path-like value. Also preserve A2’s distinction between words appearing somewhere on a page and the action being supported by the cited committed text; the r60 invented-action measurements show why token overlap alone is insufficient.
- No v3 self-test, committed-world run, `--fetch`, or base-vs-tip predicate was run by this seat. The C1 predicate is not claimed met or failed here.

### C2 / routed-repair attack boundary

`.ufo/waves/round-61/controls/C2-base.txt` is the committed base control read for this report: all R-a through R-f say `missing`, followed by `routed repairs verified 0 of 6` and `base-exit=1`. This is a stored receipt, not a command I reran.

Source inspection of `verifiers/check_routed_repairs.py:63-112` shows the gate checks marker strings/presence (for example R-d accepts a present census-after blob whose last non-empty line is `exit=0`; R-f checks for `merge-base --is-ancestor` and `exit 0`). Its module comment at lines 34-37 explicitly says it does not judge whether repair text is substantively honest. A file containing only the expected tail or an ancestry sentence could therefore be a candidate dishonest-pass mutation; this is a static attack surface, not an executed bypass or a C2 result. The dedicated counter-audit/mutation seats must report their actual mutation outcomes. No C2 self-test, revision run, or mutant run was performed by this seat.

### C3 bleed boundary

The plan scopes S117 as `own-work`, tier B only for “writing-revision calibration for prompt-craft self-assessment.” The read-only sibling source `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` describes a writing-revision check and P/H/N/C/T/Q claim classes; it is not evidence that kotoba’s rows are semantically true, that C1 is correct, or that kotoba has implemented kama’s counter. Keep S117 limited to the planned practice-level scope and do not let it support the scoped-rules claims or C1 outcome. I did not capture a hash/commit pin for the sibling file and did not run any C3 count/presence gate; this review is a scope boundary only.

## Gates, touched surfaces, and limits

- Executed: canonical Cursor markdown fetch (HTTP 200, exit 0); `.md` route probe (HTTP 404, curl exit 0); quote line and `wc -w` measurement (16, exit 0). Commands, outputs, and UTC dates are above.
- Not executed: any C1/C2/C3 gate, test, integration measurement, census, build, commit, push, or Git/jj mutation. No claim is made about the final round verdict or changed lane state.
- Written lane surface: `.ufo/waves/round-61/wave/ScribeS115.md` only. Scratch writes: `S115.page` and `rules-md.body` under `/fast/scratch/hyaku/kotoba-r61/ScribeS115/`; scratch is not cited as committed evidence. Read-only inputs included `plans/round-61.md`, S049/S108 rows, the v2 counter fetch constants, round-60 controls/ExecKeyForms/closure, C2 checker/base receipt, and the kama source.
- Out of scope: no product code, checker, fixture, or other seat report edited; no L1 message, dispatch, ask tool, install, or integration. `RULES.md` was not needed because no tool was installed.

Artifact path: `.ufo/waves/round-61/wave/ScribeS115.md`

Installs: no installs.
Blockers: none.
Produced: Cursor S115 source/quote/A1 drafts and bounded attacks on the frozen source/URL, C1 provenance, C2 static-check, and C3 bleed boundaries.
