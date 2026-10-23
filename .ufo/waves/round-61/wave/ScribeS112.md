# ScribeS112 — Claude Code A1 source

## Behavior and findings

Opened the unopened canonical Claude Code documentation page `https://code.claude.com/docs/en/claude-directory.md`. Its “Frontmatter fields by file” table maps `rules/*.md` to the `paths` field (line 94). This is documentation evidence for the Claude Code A1 key set, not a runtime test.

The cited row names the key but contains no concrete path-pattern value. For a path-value example, the already committed round-60 S103 snapshot has `paths:` followed by `"src/api/**/*.ts"` at lines 198–199. The new S112 row grounds the canonical key; do not claim its line 94 alone demonstrates a path value. This source's quoted table row contains literal `|` characters: keep the quote in the lesson's prose Gate line, not in a pipe-delimited table cell.

No locale, enterprise alias, or changelog page was used. The fetch's effective URL remained the canonical `code.claude.com` route. Existing SOURCES search for `claude-directory` returned no match before adding this row; this is an unopened URL rather than an S103 re-open.

## Fetch record

Verifier protocol read from `verifiers/check_scoped_rules.py:1169-1197`: curl uses `-sSL`, 30-second max time, the frozen browser User-Agent, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`, and write-out `\n%{http_code} %{url_effective}`. The request flags and headers below match; `-o` only directs the response body to permitted scratch storage. The first request returned HTTP 200, so no retry was needed.

Command:

```sh
date -u && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' 'https://code.claude.com/docs/en/claude-directory.md' -o /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
```

Observed output (curl's write-out has no trailing newline, so the following `wc -c` output begins directly after the URL):

```text
Fri 23 Oct 2026 07:12:44 PM UTC

200 https://code.claude.com/docs/en/claude-directory.md31144 /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14  /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
```

The command completed successfully (exit 0): HTTP status 200, body size 31,144 bytes, SHA-256 `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`.

## Exact quote and count

Command:

```sh
sed -n '94p' /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && sed -n '94p' /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page | wc -w
```

Observed output (exit 0):

```text
| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |
8
```

This is the unshaped source line, pasted exactly. `wc -w` reports 8 whitespace-delimited tokens, within the requested 6–25 range.

## Draft deliverables

### SOURCES row (11 cells; no pipe inside any cell)

```markdown
| S112 | Claude Code Docs — Explore the .claude directory — https://code.claude.com/docs/en/claude-directory.md | docs | A | Claude Code frontmatter field set for `rules/*.md` files and their path-scoped behavior (vendor documentation; not a runtime test) | § Frontmatter fields by file (`claude-directory.md:84-94`); fetched 2026-10-23T19:12:44Z (HTTP 200, 31,144 B, sha256 `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`); exact bytes target `.ufo/waves/round-61/snapshots/S112.page` | The frontmatter field map lists `paths` for `rules/*.md`, the Claude Code rule-file scope key | mined | 2026-10-23 | 90d | SKILL.md, corpus/knowledge/scoped-rules-round61.md, corpus/lessons/round-61.md |
```

### Lesson `## Gate` line

```markdown
- **S112 Claude Code** — https://code.claude.com/docs/en/claude-directory.md — accessed 2026-10-23T19:12:44Z (HTTP 200, 31,144 B, sha256 `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`; seat `ScribeS112`; snapshot target `.ufo/waves/round-61/snapshots/S112.page`) — `claude-directory.md:94` (unshaped, `wc -w` = 8): "| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |"
```

### A1 Claude Code key-set line

```python
    "Claude Code": frozenset({"paths"}),
```

Key membership citation: `S112:94`. The committed S103 example `S103:198-199` separately shows a path-like value (`paths:` / `"src/api/**/*.ts"`) if A1 needs evidence of the value form as well.

### Snapshot handoff

- L1 landing target: `.ufo/waves/round-61/snapshots/S112.page`
- Expected SHA-256: `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`
- Fetched body presently at `/fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page`. This scratch file is only a handoff convenience, not committed evidence; the L1 must land the bytes at the target and verify the hash there.

## Gates, touched surfaces, and limits

- This seat executed only the live page fetch and the exact-line/word-count commands above. The source-open measurements succeeded; no C1 counter/self-test, C2 check, C3 check, lane integration, or product tests were run by this seat.
- Lane write: this report only. No lane/fleet/sibling code, `.ufo/state`, git index, or jj files were written or mutated. The fetched page was saved only under the allowed scratch directory.
- C1 remains unverified here: key source opened, but no counter arm or predicate was exercised. C2 and C3 are outside this source-opening slice.

Installs: no installs.
Blockers: none.
Produced: S112 Claude Code canonical `rules/*.md` → `paths` source row, Gate line, key-set line, and snapshot hash handoff.
