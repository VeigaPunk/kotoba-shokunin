Result: DONE — Re-opened Claude Code Hooks at the same bytes recorded by S096, confirmed the mislabeled and actual heading lines, and drafted S110 plus its Gate entry.

## Findings

- `corpus/SOURCES.md:108` records S096 with `§ Hook events (:31-65)` and source sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`. Re-opened the canonical URL `https://code.claude.com/docs/en/hooks.md` at 2026-10-23T12:08:24Z: HTTP 200, 274,129 bytes, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` (exact match to S096).
- Fetched-byte line check: line 17 is `## Hook lifecycle`; line 31 is `| Event | When it fires |`; line 65 is `| `SessionEnd` | When a session terminates |`; line 1219 is `## Hook events`. This confirms `:31-65` is the lifecycle event summary table and the page's actual Hook events heading begins at `:1219`. The same discrepancy is already noted at `corpus/lessons/round-59.md:83-85`.
- The contract requires append-only corrections: `CORPUS.md:112-118` allows no in-place anchor edit and says a correction row opens `supersedes S0NN —`; S102 provides the matching row style at `corpus/SOURCES.md:114`.

## Draft SOURCES row S110

```markdown
| S110 | Claude Code Docs — Hooks (S096 anchor correction) — https://code.claude.com/docs/en/hooks.md | docs | A | Claude Code hook configuration locations, event summary table, and documented hook-event heading (vendor documentation; not runtime behavior) | § Hook lifecycle (`hooks.md:17`); event summary table (`:31-65`); § Hook events (`:1219`); fetched 2026-10-23T12:08:24Z, HTTP 200, 274,129 B, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` (R4 re-open; byte-identical to S096) | supersedes S096 — its `:31-65` anchor is the lifecycle event summary table under § Hook lifecycle (`:17`), not § Hook events; that heading begins at `:1219` | mined | 2026-10-23 | 90d | corpus/lessons/round-60.md |
```

## Draft Gate line

```markdown
- **S110 Claude Code (S096 anchor correction)** — https://code.claude.com/docs/en/hooks.md — accessed 2026-10-23T12:08:24Z (HTTP 200, 274,129 B, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`; seat `ScribeR4S096`) — `hooks.md:1219`: "## Hook events"
```

The `round-60.md` lesson file was not present in the observed lane view when checked (`read` returned not found; the lessons listing showed `round-59.md` but no `round-60.md`), so this Gate line is a draft and was not appended to the lesson.

## Commands and observed results

- `timeout 120s bash -c 'mkdir -p /fast/scratch/hyaku/kotoba-r60/ScribeR4S096 && date -u && curl --location --silent --show-error --output /fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md --write-out "HTTP %{http_code}\n" https://code.claude.com/docs/en/hooks.md && wc -c < /fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md && sha256sum /fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md'` — exit 0; output:
  ```text
  Fri Oct 23 12:08:24 PM UTC 2026
  HTTP 200
  274129
  c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  /fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md
  ```
- `timeout 30s bash -c 'nl -ba /fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md | sed -n "17p;31p;65p;1219p"'` — exit 0; output:
  ```text
      17  ## Hook lifecycle
      31  | Event | When it fires |
      65  | `SessionEnd` | When a session terminates |
    1219  ## Hook events
  ```

## Surfaces, limits, and artifact

- Only this report was written in the lane. No SOURCES or lesson edit was made; the S110 row and Gate entry above are drafts for the L1 integrator. The fetched page copy is outside the lane at `/fast/scratch/hyaku/kotoba-r60/ScribeR4S096/hooks.md`.
- Out of scope: changing S096 in place, any product or verifier code, and any build/test execution.
- Report path: `.ufo/waves/round-60/build/ScribeR4S096.md`.
