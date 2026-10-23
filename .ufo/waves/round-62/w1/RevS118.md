# RevS118 — independent re-verification of the S118 source open

Report target: `.ufo/waves/round-62/w1/RevS118.md`.
Scope: reviewer seat, freshness axis. Verified the S118 open (`https://code.claude.com/docs/en/memory.md`) by a second independent fetch, recomputed sha256, checked the located quote at its cited line, and checked the draft row text against `CORPUS.md` § SOURCES.md contract v1. Read-only on lane/fleet; my only lane write is this report; scratch under `/fast/scratch/hyaku/kotoba-r62/RevS118/`. No git/jj mutation, no dispatch, no edits to any counter or corpus file.

## Verdict

**S118 row OK** (the row as drafted in `w1/SrcRulesFrontmatter.md:45`; it is not yet landed in `corpus/SOURCES.md` — the registry still ends at S117). No contract-violating defects found. Two advisories and one integration-time note are listed under Residual risk.

## Second fetch record (this seat, distinct from the first)

```text
access_time_utc=2026-10-23T20:54:38Z          (date -u taken at send; first fetch 20:49:56Z — ≈4m42s later)
final_url=https://code.claude.com/docs/en/memory.md
http_status=200
size_download=55354
sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/RevS118/memory.md
exit_code=0
```

UA used (different from the first fetch's `Mozilla/5.0 (X11; Linux x86_64) … Chrome/131.0.0.0 Safari/537.36`):

```text
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 (RevS118 re-verify fetch; round-62 wave1)
```

Command shape otherwise as the plan prescribes: `--location --retry 2 --retry-all-errors --max-time 30`, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`, output to scratch only.

## Byte comparison — three r62 copies identical, zero drift

```text
sha256sum:
  02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/RevS118/memory.md            (my fetch, 20:54:38Z)
  02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  .ufo/waves/round-62/snapshots/S118.page                    (committed snapshot)
  02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/SrcRulesFrontmatter/memory.md (first fetch, 20:49:56Z)
wc -c: 55354 on all three
cmp: IDENTICAL to snapshot / IDENTICAL to Src scratch copy
date -u at compare: Fri 23 Oct 2026 08:55:13 PM UTC
```

Every SrcRulesFrontmatter claim reconciles: HTTP 200, 55,354 B, sha256 `02632438…a801`, single fetch, snapshot bytes = fetched bytes. The `Report:` claim "no lane snapshot was written" by that seat is consistent with the snapshot landing via the L1 handoff (`install -D` command at `SrcRulesFrontmatter.md:59`); the committed snapshot's sha matches the report's declared expected digest.

## Located quote — verbatim, ≤25 words, at the cited line

`sed -n '250p'` on my fetch (identical output on the committed snapshot):

```text
| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

- Byte-identical to the quote block in `SrcRulesFrontmatter.md:35`.
- Word count: `sed -n '250p' memory.md | wc -w` → **23** (raw line including markup; ≤25 either way).
- Line 250 sits inside `#### Rule frontmatter reference` (heading at :244; intro line :246; table header :248-249), matching the row's anchor `memory.md:244-250`, especially `paths` (`:250`).
- `#### Path-specific rules` is at :192; the cited body range `:194-200` verbatim covers "Rules can be scoped to specific files using YAML frontmatter with the `paths` field. …" plus the `paths:\n  - "src/api/**/*.ts"` YAML example. ✓

## Upstream drift vs the S103-era snapshot (contextual — not the two-fetch check)

The two r62 fetches do **not** differ byte-wise; the drift clause of my brief does not fire. For completeness I diffed the committed S103-era bytes (`.ufo/waves/round-60/snapshots/S103.page`, sha256 `82d60341…b6e7`, 54,043 B — matching S103's row record) against today's fetch:

```text
diff S103.page memory.md  →  44 change ops (all 'c'), 94 changed lines, 0 adds, 0 deletes
```

Every change is a relative-link absolutization (`(/docs/en/<page>` → `(https://code.claude.com/docs/en/<page>`); no sentence text changed. The `paths` table row at :250 contains no external link and is byte-identical across versions, so S103's cited line numbers (`:246-250`, `:194-200`) still land on the same content in today's bytes. Upstream bytes grew 54,043 → 55,354 (+1,311) purely from URL prefixes.

## Contract v1 check — 11 columns, cell by cell (draft row at `SrcRulesFrontmatter.md:45`)

```text
| S118 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`), especially `paths` (`:250`); § Path-specific rules (`:194-200`); fetched 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`); snapshot `.ufo/waves/round-62/snapshots/S118.page` | re-opens S103 — opened this round because C1 E2e instances need source evidence for the `paths` rule's glob syntax and supported input forms; this row records the current-round access to the specific rule-frontmatter reference | queued | 2026-10-23 | 90d | — |
```

- **Shape**: `awk -F'|'` on the draft → NF=13 = 11 columns, contract order `id|source|kind|tier|scope|anchor|teaches|status|opened|recheck|used-by`; no `|` inside any cell (checked — no `|` char in the row body outside delimiters).
- **id**: S118 unused in `corpus/SOURCES.md` (grep finds S099–S115, S117; no S118). S116 is deliberately unassigned — `corpus/lessons/round-61.md:18` records "S116 — no source row assigned". Skipping it is documented, not a collision.
- **source**: title matches the page H1 (`# How Claude remembers your project`, memory.md:5); URL identical to S103's row (re-open precedent: S114 shares S106's URL, S115 shares S108's).
- **kind** `docs`, **tier** `A` (official vendor docs for the stated scope; `docs`+`A` legal, `community`+A check passes — none present).
- **scope**: scoped claim, carries the "(vendor documentation; not a runtime test)" hedge used by S102–S115.
- **anchor**: `§ Rule frontmatter reference (memory.md:244-250)` and `§ Path-specific rules (:194-200)` both verified verbatim above; fetch record (date, HTTP, bytes, sha) all match my independent measurement; snapshot path exists with matching sha.
- **teaches**: `re-opens S103 —` — the prefix the frozen spec assigns (`w1-spec.json` SrcCensusChecks item), matching precedent S115 (`re-opens S108 —`, immediate predecessor) and S114 (`re-opens S048`). Contract rule 2 names `supersedes S0NN —` for *corrections*; S118 records a same-source re-access, not a correction, so `re-opens` is the right prefix family. The post-prefix text names a grounded benefit (`paths` glob syntax, YAML-list/comma-string forms — exactly what the quote at :250 supports).
- **status** `queued` + **used-by** `—`: consistent pair; enum-legal.
- **opened** `2026-10-23` = fetch date; **recheck** `90d` cadence.

Scratch simulation (copy of `corpus/SOURCES.md` + draft row appended after S117) run against the contract's frozen census commands, `date -u` 2026-10-23T20:56Z:

```text
rows:            116
malformed rows:  0        (NF=13 check)
tier histogram:  A=113 B=2 C=1
status histogram: mined=107 queued=8 rejected=1
duplicate ids:   (none)
enum violations: (none)
```

## Residual risk / advisories (non-blocking)

1. **Anchor string mismatch (upstream, not a row defect).** The plan and S112's upstream table (`S112.page:94`) name `#rules-frontmatter-reference`; the heading in `memory.md` is `#### Rule frontmatter reference`, which slugifies to `#rule-frontmatter-reference` (no `s`). No other heading produces the `rules-` slug. The draft row cites line numbers only, so nothing in the row depends on the fragment — wave 2 may still want the discrepancy recorded in the lesson Gate note.
2. **`teaches` wording.** The benefit clause is buried after bookkeeping prose ("opened this round because C1 E2e instances need source evidence…"). Grounded and honest, but less benefit-forward than S115's precedent. Optional polish at integration; not a contract violation.
3. **status/used-by at landing.** If `corpus/lessons/round-62.md`'s Gate cites S118 (contract rule 1 requires the Gate record), S115's precedent lands such rows as `mined` with the lesson listed in `used-by`. Landing `queued`/`—` while a committed file cites it would leave a mild staleness; the L1/integration decides.
4. **ScribeSourcesS118 is stale.** Its report claims "blocked on source" — written before `SrcRulesFrontmatter.md` existed; harmless ordering artifact, no action needed.
5. **Not verified by me (out of scope)**: the lesson `## Gate` line for S118 (ScribeLesson62's report was absent from `w1/` at check time — seat still running), Q34 append-only range run, and the full `scripts/sources-census.sh validate` (I ran the contract's frozen manual census block on a scratch copy instead; all seven checks pass).

Installs: no installs (curl/awk/diff/sha256sum already present; pacman paused per guard).
Blockers: none.
Attacked: the S118 source open — second fetch byte-identical to the committed snapshot and first fetch; quote verified verbatim at `memory.md:250` (23 words); draft row conformant to contract v1 — **S118 row OK**.
