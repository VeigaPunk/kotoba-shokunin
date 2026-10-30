# Kb82E20Census — source census, S248 open, S251 shape (executor, leaf)

Round 82 w1. Lane `kotoba-shokunin`, base `47dbe8781657de563ff867caca6244d28e3db504`.
Scratch clone `/fast/scratch/hyaku/kotoba-r82/Kb82E20Census/clone` (shared, `git -C` asserted; rev-parse
= `47dbe8781657de563ff867caca6244d28e3db504` before any read). No lane file edited, no lane git/jj
mutation, no subagent dispatch, no installs (pacman untouched). Tools used as-found: fleet
`scripts/sources-census.sh` (806 lines, read in full), lane `verifiers/verify_corpus_integrity.py`,
system `curl 8.x`/`gawk`/`git`. Fetched page bytes treated as data only.

## 1. Independent source census at base (before receipt)

All commands run against my own clone at base; each captures its own exit (no pipelines).

| step | command | result |
|---|---|---|
| validate | `sources-census.sh validate /fast/…/Kb82E20Census/clone` | **exit 0**, 32 × W04 duplicate-URL-across-scopes + `clone ok …/corpus/SOURCES.md` |
| counts | `sources-census.sh census <clone>` | **exit 0**: rows **176**, tier **A137/B22/C17**, status **mined 151 / queued 8 / rejected 17**, invalid 0, missing 0 |
| overdue | `sources-census.sh overdue <clone>` | **exit 0**, 173 cadence lines, **0 overdue** |
| script selftest | `sources-census.sh selftest` | **exit 0**, `selftest ok` (all arms killed) |
| corpus integrity | `python3 -B verifiers/verify_corpus_integrity.py --repo <clone> --json --no-baseline` | **exit 1** (base red, debt): commit_total 50, **commit_unresolvable 1**, commit_external 2, commit_nonhash 0, commit_truncated 5 |

Independent awk histogram over the registry table (matches the script exactly):

- status: mined 151, rejected 17, queued 8 → queued ids **S005, S006, S007, S009, S010, S013, S014, S248**
- tier: A 137, B 22, C 17 · kind: docs 149, spec 10, code 6, own-work 5, paper 4, community 2
- rows are `S001…S250` dense, 176 rows; last registry line 191 (S250), table closes before `## Paths`

Cross-check against the fleet before-receipts (read-only): `receipts/before-census.txt` (32 W04, exit 0,
`kotoba ok`) and `receipts/before-source-counts.txt` (`{"malformed":0,"rows":176,"status":{"mined":151,"queued":8,"rejected":17},"tiers":{"A":137,"B":22,"C":17}}`) — **byte-for-byte agreement** on every count.

**Schema findings (the census the fleet runs):**

- Table contract 11 columns ⇒ `NF==13`; E01 malformed, E02 id shape, E03 duplicate id, E04 duplicate
  URL+scope without `supersedes S0NN`, E05 kind enum `spec|docs|paper|code|tool|dataset|talk|book|community|own-work`,
  E06 tier `^[ABC]$`, E07 status `queued|mined|rejected`, E08 opened ISO ≤ today, E09 recheck ISO/`NNd`/symbolic,
  E10 community-at-A, E11 used-by path on disk, E12 row-shaped source outside `## Registry`.
- **E11 is mined-only** (`usedby_findings`: `[ "$status" = mined ] || continue`) — re-confirmed below.
- Append-only rule (verifiers/check_sources_append_only.py): in-place edits permitted only to
  `status`, `recheck`, `used-by`; any other cell change or row deletion is a breach; a correction is a
  **new row** whose teaches opens `supersedes S0NN —`.
- Base integrity red (debt, not new): the one unresolvable commit citation is
  `corpus/lessons/round-81.md:8: 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`.

## 2. S248 — queued-but-used, source opened live

Row (SOURCES.md:189): Claude Code — Agent SDK: Agent Skills, `https://code.claude.com/docs/en/agent-sdk/skills.md`,
docs, tier B, status **queued**, opened 2026-10-27, recheck 90d, used-by **corpus/knowledge/allowed-tools-sdk-round81.md**
(non-`—` while queued → "queued-but-used"). LOG.md:2856 records the round-81 used-by transition `—` → entry.

**Opened the source today** (seat fetch, not the pinned snapshot):

- `curl -fsSL -A Mozilla/5.0 --max-time 60 https://code.claude.com/docs/en/agent-sdk/skills.md` →
  **HTTP 200, exit 0, 28 395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`** —
  **byte-identical** (`cmp` rc=0) to the committed round-81 snapshot `.ufo/waves/round-81/snapshots/S249.md`.
  The pin holds as of 2026-10-30; the page has not moved since 2026-10-27.

**Quote verification against the committed snapshot** (python3, hashlib + text view = backticks deleted,
list markers stripped, whitespace collapsed):

- Quote 2 "The list pre-approves the named tools rather than restricting the others." → **present**,
  raw line 389, exactly as the anchor claims.
- Quote 1 "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's
  allowed-tools frontmatter or with the allowedTools option" → **0 occurrences in the text view AND 0 in
  the raw bytes**. Raw line 348 actually reads
  `…with the skill's [`allowed-tools`](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill) frontmatter or with the \`allowedTools\``
  — the hyphenated key is a Markdown link and both keys carry backticks. This is exactly the defect the
  round-81 entry documented ("An inherited quote is unbackable in this view… the defect is recorded rather
  than repaired"); I re-derived it independently at base.

**Assessment for a queued→mined proposal:**

- Schema: `status` is a permitted in-place cell; the live re-open supports the page identity (HTTP 200,
  byte-identical pin) and one of two located quotes; used-by already resolves to a live knowledge entry
  that cites S248 in its `source:` line.
- Honesty: flipping to mined would attach a row whose first located quote is **unbackable as written** —
  a false-content shape the census's E/W codes cannot see (no quote re-verification exists in
  sources-census.sh). The anchor cell is protected, so the defect cannot be repaired in place.
- **Qualified proposal to L1:** if S248 goes mined this round, do it as the single mutable-cell change
  `status: queued -> mined`, logged old→new in the round-82 lesson, with the unbackable-quote defect
  explicitly carried (page pin and quote 2 verified today). The contract-correct repair of the anchor is a
  **supersede row** (new id, e.g. S252, teaches opens `supersedes S248 —`, corrected link-shaped anchor) —
  note S251 is already reserved for the loader receipt, so the supersede needs its own id. My seat does not
  execute either change (registry is not mine to write).

## 3. S251 — reserved own-work loader row, shape validated in scratch (not written)

Drafted from own-work precedents S015/S020/S250 (no URL in the source cell → E04/W04 arms never engage;
`on-release` cadence; teaches carries sha256 facts in plain prose, never `` commit `<hex>` `` grammar):

> `| S251 | kotoba own work — host loader re-derivation of the installed omp 18.14.0 ELF at /home/vgpnk/.local/bin/omp, loader-group calls and instruction literals, run 2026-10-30, exit 0 | own-work | A | … | … | … | mined | 2026-10-30 | on-release | corpus/knowledge/host-loader-rederivation-round82.md, corpus/lessons/round-82.md |`

(full draft: `build/Kb82E20Census-s251-draft-row.md`). Validated on a copy of the base tree
(`s251check/`, toplevel asserted):

| check | result |
|---|---|
| `awk -F'|'` cell count | NF=13 → 11 cells |
| `validate s251check` | **exit 0**, `s251check ok`, same 32 W04, no E/W mentioning S251 |
| `census s251check` | **exit 0**: rows **177**, tier.A **138**, mined **152**, queued 8, rejected 17, invalid 0, missing 0 |
| `overdue s251check` | **exit 0**, cadence line `S251 recheck=on-release opened=2026-10-30`, not overdue |
| integrity `--no-baseline` on the copy | commit_total **50** (unchanged), unresolvable 1 (same round-81 site), external 2, nonhash 0, truncated 5 → the row grammar adds **zero** commit-citation sites |
| control: fixture knowledge file deleted, row `mined` | **exit 1** `E11 S251 missing used-by corpus/knowledge/host-loader-rederivation-round82.md` → mined S251 must land same-commit as its used-by targets |
| control: row `queued`, used-by paths missing | **exit 0**, `s251check ok`, zero E11 → E11 is mined-only (round-81 M3 re-confirmed on this row shape) |

Numbers/hex in the teaches/anchor cells are placeholders for the loader seat's real derivation receipt;
the shape, enum values, cadence and landing constraints above are what this seat validates.

## 4. Risks / blockers

- S248's unbackable quote is inherited debt; if L1 flips it mined without logging the defect, a future
  quote-audit will find a mined row with a false anchor. Flagged in §2 with both honest paths.
- Base corpus integrity is red at 1 unresolvable site (`corpus/lessons/round-81.md:8`); not in my scope to
  repair, recorded so after-values are not scored against a silently moving baseline.
- S251 content depends on the C1 loader seat's receipt existing; if the row lands before the receipt and
  knowledge entry commit, E11 fires (control shown). No other blockers.

Postscript (12:05, after receipts were frozen): the lane working tree's `corpus/SOURCES.md` shows an
uncommitted one-cell change `S248 status queued -> mined` (mtime 11:33, not this seat's write — this seat
never edits the registry). The anchor cell is unchanged, so the unbackable-quote defect §2 documents now
rides on a mined row. The append-only gate requires the old→new transition to be logged in the round-82
lesson; L1 should confirm that log line lands with the commit. Base receipts in `build/` were captured
before this change and remain the honest before-state.

No tool was installed or upgraded this seat. Pacman untouched. Scratch
`/fast/scratch/hyaku/kotoba-r82/Kb82E20Census/` removed on exit after receipts copied.

VERDICT: independent base census green and matching fleet receipts (176 rows, mined151/queued8/rejected17,
A137/B22/C17, 32 W04, 0 overdue, integrity baseline recorded with one pre-existing red); S248 source opened
live — HTTP 200, byte-identical pin `ac62c2df…`, quote 2 verified, quote 1 unbackable as written (defect
re-derived); queued→mined proposed qualified with transition-log text; S251 draft row shape-validated in
scratch (11 cells, no E/W, E11 landing constraint demonstrated), registry untouched.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E20Census.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-census-validate-before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-census-counts-before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-census-overdue-before.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-integrity-before.json
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-s248-open.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-s251-draft-row.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E20Census-s251-shape-validation.txt
