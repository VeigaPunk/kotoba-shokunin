# S118 — rules-frontmatter source re-open

Report target: `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md`.

Scope: this seat wrote only this report in the lane. The downloaded page was saved under the permitted scratch directory; no lane snapshot was written. No install, build, test, lint, formatter, git, or jj action was performed.

## Fetch evidence

One `curl` invocation fetched the requested URL. It used a browser user-agent, the requested `Accept` header, `--max-time 30`, and `--retry 2 --retry-all-errors` (maximum three attempts). The successful response was HTTP 200; no second fetch was made.

Command (the exact request arguments and output destinations used):

```sh
curl --location --retry 2 --retry-all-errors --max-time 30 --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' --header 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' --output /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md --write-out 'final_url=%{url_effective}\nhttp_status=%{http_code}\nsize_download=%{size_download}\n' https://code.claude.com/docs/en/memory.md
```

Access time was captured with `date -u +%Y-%m-%dT%H:%M:%SZ` immediately before the request. The measured command result was:

```text
access_time_utc=2026-10-23T20:49:56Z
final_url=https://code.claude.com/docs/en/memory.md
http_status=200
size_download=55354
sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md
exit_code=0
```

`exit_code=0` is the successful shell command result; its final check required HTTP 200. The fetch saved the response body to scratch only.

## Raw rules-frontmatter evidence

At `memory.md:250` (within the section anchored `#rules-frontmatter-reference`), the complete raw Markdown line is:

```text
| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

This is one unjoined source line; no bytes were dropped. The quoted line is under 25 words.

## S118 registry row draft

Exactly 11 cells, in `corpus/SOURCES.md` column order (`id`, `source`, `kind`, `tier`, `scope`, `anchor`, `teaches`, `status`, `opened`, `recheck`, `used-by`):

```text
| S118 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`), especially `paths` (`:250`); § Path-specific rules (`:194-200`); fetched 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`); snapshot `.ufo/waves/round-62/snapshots/S118.page` | re-opens S103 — opened this round because C1 E2e instances need source evidence for the `paths` rule's glob syntax and supported input forms; this row records the current-round access to the specific rule-frontmatter reference | queued | 2026-10-23 | 90d | — |
```

S103 is the previous same-route row: it records a fetch at `2026-10-23T12:08:16Z`, 54,043 B, sha256 `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7`. S118's row is distinct: it documents the current-round opening needed for the C1 E2e source basis rather than treating S103's earlier opening as this round's access.

## Snapshot handoff

Target: `.ufo/waves/round-62/snapshots/S118.page`.

Expected file bytes are the complete fetched response body: 55,354 bytes, SHA-256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`. The target was not written by this read-only lane seat. The scratch copy below is a transfer artifact only, not cited as evidence; verify its hash before integration.

L1 integration command (not run by this seat):

```sh
install -D -- /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/snapshots/S118.page
```

Installs: no installs.
Blockers: none.
Produced: S118's fresh source evidence, exact 11-column registry-row draft, and the S118.page snapshot handoff with digest.
