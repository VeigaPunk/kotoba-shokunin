verdict: S005 still-holds — fetched 2026-10-21T15:54:22Z, HTTP 200, 514,698 bytes, sha256 `c85f56cc…0f0d`, byte-identical to the round-46 record; §4.5 "Fenced code blocks" and "Version 0.31.2 (2024-01-28)" both present; anchor and teaches cells correct, and no status/recheck/used-by change (old→new = none) is supported.

# S005 — CommonMark Spec 0.31.2, non-author re-open

Row under test: `corpus/SOURCES.md:18` at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`
(`git rev-parse HEAD`, exit 0).

> | S005 | CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ | spec | A | Fenced code block syntax the lane's box/quote extraction implements | § Fenced code blocks; version 0.31.2 | A code fence is at least three backticks or tildes preceded by up to three spaces of indentation; a backtick fence's info string may not contain a backtick | queued | 2026-10-19 | on-release | — |

## Fetch record

Page saved only in `/fast/scratch/kotoba-r47/SrcS005-9/spec.html` (Q11: nothing large written to the lane).
Metadata is in `.ufo/waves/round-47/build/SrcS005.json`.

| field | observed |
|---|---|
| URL | `https://spec.commonmark.org/0.31.2/` |
| UTC access | `2026-10-21T15:54:22Z` (verified `date -u`, not a local hour labelled `Z`) |
| HTTP status | 200 (`HTTP/2`), no redirect (`url_effective` = requested URL) |
| content-type | `text/html; charset=utf-8` |
| bytes | 514,698 |
| sha256 | `c85f56cc2101f761cc94215c677cd2c7c1ecca9c47be016479fdfe718af60f0d` |
| re-fetch | `2026-10-21T15:55:25Z`, 200, same 514,698 bytes, `cmp -s` → identical=yes (exit 0) |
| server headers | `etag: "683c9651-7da8a"`, `last-modified: Sun, 01 Jun 2025 18:05:05 GMT` |
| round-46 digest | equal to `.ufo/round-46/evidence/w2/sources/fetch-log.json:43` (`c85f56cc…0f0d`) |

The recorded 2026-10-19 timestamp in that fetch log is the known local-time-labelled-`Z` defect
(`corpus/lessons/round-46.md:77`); the digest is unaffected and today's timestamp was taken from
`date -u` on the same host.

## Anchor — holds

- `<h1 class="title">CommonMark Spec</h1>` at HTML line 116 (the `<title>` element at line 5 carries the same text).
- `Version 0.31.2 (2024-01-28)` at HTML line 117.
- `<h2 id="fenced-code-blocks" class="definition">` at HTML line 2726; heading text
  `<span class="number">4.5</span>Fenced code blocks` at line 2727. `grep -c '^<h2 id="fenced-code-blocks"'` → 1 (exit 0); the fragment `#fenced-code-blocks` resolves to exactly one id.

The cell `§ Fenced code blocks; version 0.31.2` matches the heading verbatim and is version-pinned;
contract v1 requires a heading plus a revision, which this satisfies. The missing section number
`4.5` is a precision nicety, not a defect — and contract v1 rule 2 forbids editing `anchor` in
place anyway.

## Teaches — holds, clause by clause

| teaches clause | spec evidence | location |
|---|---|---|
| "at least three backticks or tildes" | "A code fence is a sequence of at least three consecutive backtick characters (`) or tildes (~)." | §4.5 opening definition, HTML 2729-2731 |
| "preceded by up to three spaces of indentation" | "A fenced code block begins with a code fence, preceded by up to three spaces of indentation." | HTML line 2732 |
| "a backtick fence's info string may not contain a backtick" | "If the info string comes after a backtick fence, it may not contain any backtick characters." | HTML 2734-2737 |

Primary quote (15 words, ≤25): "A code fence is a sequence of at least three consecutive backtick
characters (`) or tildes (~)." — §4.5 "Fenced code blocks", opening definition, HTML lines
2729-2731 of the fetched page.

Grep corroboration on the fetched bytes: `preceded by up to three spaces of indentation` → 9
occurrences (exit 0); `it may not contain any backtick` → 1 (exit 0); `Version 0.31.2
(2024-01-28)` → 1 (exit 0).

## Status / recheck / used-by — no change recommended

| cell | old | new | reason |
|---|---|---|---|
| status | `queued` | `queued` | Contract v1: `mined` requires ≥1 path in `used-by`. `grep -rn "S005" verifiers/` → no output, exit 1; `grep -rln "S005" corpus/knowledge` → no output, exit 1. The only hit is the row's own gate entry, `corpus/lessons/round-46.md:67` (exit 0). |
| recheck | `on-release` | `on-release` | 0.31.2 is still the newest release: `https://spec.commonmark.org/` → 200, 7,860 bytes, listing `0.31.2` and older only (the lone `1.11.0` string is the jQuery script). `on-release` is the frozen-spec convention shared with S006 and S008. |
| used-by | `—` | `—` | This registry cites rows by id (cf. `SKILL.md:151`, which cites S001, S002, S003, S008); SKILL.md does not cite S005, and the verifiers cite the URL directly (`verifiers/verify_skill_checklist.py:1554-1555`), not the row. Contract v1 scopes `used-by` to knowledge entries or lessons, so pointing it at verifier code would stretch the column. |

What the round-47 lesson **should** record is a gate-level append, not a registry cell edit:

- `S005` re-opened by non-author seat `MoriR22R.SrcS005-9` at `2026-10-21T15:54:22Z`;
  sha256 `c85f56cc2101f761cc94215c677cd2c7c1ecca9c47be016479fdfe718af60f0d`; quote and location as
  above; digest equal to the author's 2026-10-19 record.
- Do **not** touch `opened` (2026-10-19): contract v1 rule 2 makes `opened` immutable; re-open
  evidence lives in the round lesson, exactly as the round-46 "L1 re-open" paragraph does
  (`corpus/lessons/round-46.md:77`).

Read-only registry census (contract v1 § Census): malformed rows `0`, status histogram
`mined=4 queued=6 rejected=1` (exit 0). S005's row is structurally clean.

## Counterexamples and precision notes

1. **Mixed-fence reading.** The teaches cell's "backticks or tildes" is true only as an
   exclusive-or; the spec's next sentence says "Tildes and backticks cannot be mixed"
   (HTML line 2730), which the cell omits. Not a falsehood, but a reader could take the cell as
   licensing `~~~` + backtick mixtures. The lane's parser does not mix (`FENCE_RE =
   re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")`, `verifiers/verify_corpus_independent.py:113`), so
   the code is stricter than the summary, not looser.
2. **Teaches under-covers the scope's own use.** The row's scope claims "the lane's box/quote
   extraction implements" this syntax, and that extraction depends on the *closing* rule —
   same fence character, run length ≥ opener, trailer blank — asserted as "CommonMark 4.5" in
   `verifiers/verify_corpus_independent.py:104-113,229-237` and
   `verifiers/verify_corpus_integrity.py:154-158`, with an unclosed fence running to EOF. The
   teaches cell states only the opener and info-string rules; §4.5 lines 2739-2741 and 2748-2750
   are the missing ground. Contract-compliant options if L1 wants that gap closed: a new row
   whose teaches opens `supersedes S005 —` (rule 2), or a `corpus/knowledge/` entry citing S005
   (which would also make `mined` legitimate). Editing the teaches cell in place is not legal.
3. **The page is not byte-frozen by its version label.** `last-modified: Sun, 01 Jun 2025
   18:05:05 GMT` postdates the 2024-01-28 release, so a silent re-render is possible in principle;
   the digest equality proves stability only across 2026-10-19 → 2026-10-21. That is a residual,
   not a reason to change the cadence: the row pins a *released version*, and per-round re-opens
   (this one included) are what supply drift evidence.

## Commands run (all exit 0 unless noted)

Working dir `/fast/scratch/kotoba-r47/SrcS005-9` for fetches; lane root for greps.

```sh
git rev-parse HEAD                     # c61a973b2e02e1ded169703ddcb06466f4edd8bd
curl -sS -o spec.html -w '...' https://spec.commonmark.org/0.31.2/
                                       # http_code=200 size_download=514698 content_type=text/html; charset=utf-8; curl_exit=0
date -u +%Y-%m-%dT%H:%M:%SZ            # 2026-10-21T15:54:22Z
sha256sum spec.html                    # c85f56cc…0f0d
curl -sS -o spec2.html ...             # code2=200 size2=514698; sha256 equal; cmp -s identical=yes
curl -sSI https://spec.commonmark.org/0.31.2/   # HTTP/2 200, etag "683c9651-7da8a", last-modified 2025-06-01
curl -sS https://spec.commonmark.org/ -o root.html  # root_code=200 root_size=7860
grep -c '^<h2 id="fenced-code-blocks"' spec.html    # 1
grep -c 'Version 0.31.2 (2024-01-28)' spec.html     # 1
grep -c 'preceded by up to three spaces of indentation' spec.html  # 9
grep -c 'it may not contain any backtick' spec.html # 1
grep -rn "S005" verifiers/             # no output, exit 1
grep -rln "S005" corpus/knowledge      # no output, exit 1
grep -n "S005" corpus/lessons/round-46.md          # line 67, exit 0
awk -F'|' '... NF!=13 ...' corpus/SOURCES.md        # malformed=0; status mined=4 queued=6 rejected=1
```

No tool installs or upgrades were needed (`tool_changes: []`); no subagents were spawned.

## What I did NOT check

- The cmark-oracle provenance of the pinned `FENCE_SHAPES` literals in
  `verifiers/verify_skill_checklist.py` (no cmark run).
- Any verifier self-test or lane gate; no scratch clone was needed because no code was edited.
- Other SOURCES rows (S001-S004, S006-S011) and the round-46 spot-check status of S005 beyond the
  digest match.
- Alternative renderings of the same version (`spec.txt`, single-page variants); only the row's
  exact URL was opened.
- Header consistency across CDN edges beyond the one HEAD call; `age: 351`/`x-cache: HIT` show the
  response was served from a Fastly cache, which is the same cache path a verifier would hit.
