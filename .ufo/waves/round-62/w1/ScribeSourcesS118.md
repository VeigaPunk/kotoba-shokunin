# Round 62 W1 — S118 source-scribe findings

## Outcome

**Unblocked after the initial read.** My first read of the assigned source report returned “not found” and the first report recorded that state. After the L1 notification that the report and snapshot had landed, I re-read both paths. The source report and `.ufo/waves/round-62/snapshots/S118.page` are now present. This report supersedes the initial blocked disposition; it does not claim I fetched the page or independently hashed the snapshot.

## Source provenance

`SrcRulesFrontmatter.md` records one successful `curl` invocation and no second fetch. Its fetch command was:

```sh
curl --location --retry 2 --retry-all-errors --max-time 30 --user-agent 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' --header 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' --output /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md --write-out 'final_url=%{url_effective}\nhttp_status=%{http_code}\nsize_download=%{size_download}\n' https://code.claude.com/docs/en/memory.md
```

The source report records the adjacent UTC-time command and fetch output (the fetch was performed by `SrcRulesFrontmatter`, not by this scribe):

```text
date -u +%Y-%m-%dT%H:%M:%SZ
access_time_utc=2026-10-23T20:49:56Z
final_url=https://code.claude.com/docs/en/memory.md
http_status=200
size_download=55354
sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md
exit_code=0
```

The source report identifies the fetch line as the complete, unjoined Markdown line `memory.md:250`. On re-opening the lane snapshot, I observed the same line at line 250. The L1 notification states that the snapshot digest was verified equal to the fetch digest; I did not run a checksum command independently. The fetched scratch path is provenance in the source seat's report, not a cited lane artifact.

## Exact S118 row draft

This reproduces the source seat's proposed row verbatim. It has 11 cells in the contract order; split on `|`, it has `NF=13`. It uses `re-opens S103 —`, because S103 is the earlier row for the same memory.md URL. This matches the re-open prefix pattern in S114 (`re-opens S048 —`) and S115 (`re-opens S108 —`), not the correction prefix `supersedes S0NN —`.

```text
| S118 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`), especially `paths` (`:250`); § Path-specific rules (`:194-200`); fetched 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`); snapshot `.ufo/waves/round-62/snapshots/S118.page` | re-opens S103 — opened this round because C1 E2e instances need source evidence for the `paths` rule's glob syntax and supported input forms; this row records the current-round access to the specific rule-frontmatter reference | queued | 2026-10-23 | 90d | — |
```

The `queued` / `—` tail is the source seat's pre-integration draft. If the landed lesson or a knowledge entry cites S118 and is placed in `used-by`, reconcile `status`/`used-by` with the contract's definition of `mined`; any in-place change is limited to those permitted cells and must be logged old→new in the lesson. The frozen plan says C1's E2e instances cite S118, but the round-62 lesson and knowledge entry were not present in the paths I read, so I do not guess a knowledge-entry path or claim a final status.

## Quote and lesson Gate line

The exact source line, copied without shaping, is:

```text
| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

It contains 19 prose words (23 whitespace-separated tokens if the Markdown table-pipe tokens are included), below the contract's 25-word maximum. Its location is `memory.md:250`, under § Rule frontmatter reference. Proposed round-62 lesson Gate line:

```markdown
- **S118 Claude Code (re-opens S103)** — https://code.claude.com/docs/en/memory.md — accessed 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`; seat `SrcRulesFrontmatter`; snapshot target `.ufo/waves/round-62/snapshots/S118.page`) — `memory.md:250`: "| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |"
```

The Gate line carries URL, access time, HTTP/size/hash, seat, snapshot target, quote location, and the exact quote. CORPUS.md contract v1 rule 1 requires the round lesson's Gate to retain the row's URL, access date, and located ≤25-word quote; do not call this quote shaped or byte-verified by this scribe.

## Proposed README index line

The current README ends its round-specific entries with `Round-61 lessons`; the new line belongs after that entry and before `## Frontier`. Proposed line, to add only after `corpus/lessons/round-62.md` exists:

```markdown
| Round-62 lessons | `lessons/round-62.md` | `## Gate` S118 source/access record with the unshaped ≤25-word quote at `memory.md:250`; `## Mistakes` class “erratum recorded as absorbed without an arm-level receipt” (E2f G7/G9), captured by C1's absorption matrix, fix = successor + QUALITY row; round-62 census and append-only disposition |
```

The plan requires a round-62 knowledge entry but does not name its path, and no round-62 knowledge entry was present in the read listing. Therefore no guessed knowledge-entry index line is supplied. Add its actual path to the README only once that entry exists (CORPUS.md § Rules: write an index row when the file exists, not before). No README line was written by this scribe.

## Post-landing commands

The following are to be run after the row, used-by targets, and lesson Gate land; neither command was run by this scribe. No census or Q34 pass is claimed.

Census / validation:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate kotoba --root /home/vgpnk/Projects/shokunin
```

Q34 append-only range check, using the dispatch tip as the range start and the landed revision as `HEAD` (run while `HEAD` is that landing revision; otherwise substitute the exact landing revision):

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_sources_append_only.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --base 45a7ecfac9e203297f3146c45d63f5e79367470c --rev HEAD
```

Q34 requires the output to be pasted for the claimed range. The check was not run here. Adding S118 is append-only; existing rows may only change `status`, `recheck`, or `used-by`, with each change recorded old→new in the lesson.

## Touched surfaces, limits, and artifacts

- **Only write:** this report at `.ufo/waves/round-62/w1/ScribeSourcesS118.md`.
- **Read-only surfaces:** the landed S118 source report and snapshot, `plans/round-62.md`, `CORPUS.md` § SOURCES.md contract v1, `corpus/SOURCES.md` (S103 plus S114/S115/S117 and S118 insertion context), `corpus/README.md`, `corpus/lessons/round-61.md`, `corpus/QUALITY.md` Q34, the census script, and the append-only checker.
- **No gates executed by this scribe:** no source census, Q34 check, tests, or external fetch. The source seat's recorded curl output is reproduced as provenance, not as a command run here.
- **Out of scope/not done:** no lane/fleet corpus edit, no snapshot write by this scribe, no git/jj/index mutation, no dispatch, no peer message, and no install.
- **Pending integration facts:** `corpus/lessons/round-62.md` was not present when read; the new knowledge-entry path is unspecified. The exact proposed README line is contingent on the lesson existing, and any separate knowledge index row must use the actual path.

Installs: no installs.

Blockers: none for this scoped source draft; final README/used-by reconciliation depends on the round-62 lesson and knowledge-entry landing.

Produced: S118 registry row draft, exact source Gate line and quote check, a conditional round-62 README line, and post-landing census/Q34 commands.