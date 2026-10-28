# Kb80E12Census — census runner (round 80, wave w1)

Seat: Kb80E12Census (leaf executor; no subagents, no background jobs, 4 concurrent curls max).
Date: 2026-10-27. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch (removed before yield): `/fast/scratch/hyaku/kotoba-r80/Kb80E12Census/`.

## What this seat did

Ran the corpus census at the r80 base in its own-exit form, applied the round-80 SOURCES.md edit set
in a scratch clone of the lane, re-ran the census and the row-count commands over the integrated
result, and published the before/after blocks with the exact edit list.

**Nothing in the lane tree was modified.** Every git mutation happened in a scratch clone under the
seat's own scratch directory; the lane was touched read-only.

## Measured results

| measurement | base (lane tree) | after (scratch, integrated edit set) |
|---|---|---|
| `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **exit 0**, `ok`, 157 rows, 24 W04 | **exit 0**, `ok`, 174 rows, 31 W04 (both the explicit-lane-dir form and the lane-label form over a synthetic root) |
| `sources-census.sh census --root … kotoba` | exit 0; rows 157, tier.A 135, tier.B 21, tier.C 1; mined 149, queued 7, rejected 1 | exit 0; rows 174, tier.A 135, tier.B 22, tier.C 17; mined 149, queued 8, rejected 17 |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 157 (rc=0) | 174 (rc=0) |
| `grep -cE '^\|[[:space:]]{0,3}S[0-9]{3,}[[:space:]]*\|'` | 157 (rc=0) | 174 (rc=0) |
| `check_sources_append_only.py --rev <tip> --repo .` | 18 breaches / 45 commits, exit 1 (pre-existing) | 18 breaches / 46 commits, exit 1 (**unchanged**: 0 new breaches, 17 rows added, 0 removed, 6 permitted `used-by` log lines) |
| C2 counter conjunct (b) harness (`ENTRY` rebound to the round-80 entry) | **6 of 6 fail** | **0 of 6 fail** |

The 7 new W04 lines (all "duplicate url … across scopes", raised by new rows whose URL an older mined
row already carries under a different scope) are listed verbatim in the receipt. W04 does not change
the exit status.

## The edit list applied

1. **Six `used-by` cells (S226–S231), cell 11 only.**
   `corpus/lessons/round-79.md` -> `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md`
   (comma form, 11 cells per row before and after, other 10 cells byte-identical).
2. **Twelve new rejection rows S232–S243**, derived by this seat from `Kb80R01NegSweep.md`'s
   per-client fetch records and re-fetched independently (12/12 with 0 hits of `allowed[-_]tools`
   and of the broad `allowed.{0,2}tools` sweep). Each row: 11 cells, tier C, `rejected`, opened
   2026-10-27, recheck 90d, used-by `corpus/lessons/round-80.md`, an anchor cell with a verified
   5–25-word located quote plus the fetch record, and a `teaches` cell grounded on the counted token
   absence over the pinned bytes (Q62: an observed fact, never an assertion about what the source
   lacks).
3. **Five rows S244–S248** from `Kb80S05SourcesEdits.md`, applied verbatim (`git apply --check` exit 0,
   `git apply` exit 0) — this seat did not author them and does not vouch for their content.

Net: 157 -> 174 rows (+17), 0 rows removed.

## Load-bearing findings

- **The `used-by` cell must be comma-separated.** It satisfies the C2 counter's (b) conjunct
  (`row[10].split(",")`; `ENTRY not in listed`) and the census's E11 path check (`IFS=',' read -a
  paths`). A `+`-joined cell satisfies neither — measured, not assumed.
- **E11 is live and ordering-sensitive.** With the two `used-by` target files absent, the same
  174-row table yields 12 E11 findings and exit 1. The entry file (Kb80E08C2Entry) and the lesson
  file (Kb80S01Lesson) must land before or with the SOURCES.md edit.
- **Two independent row texts exist for S232–S243.** This seat's text is published as a patch
  (`Kb80E12Census-S232-S243.patch`, verified to apply cleanly over S05's patch and to reproduce the
  measured file byte-for-byte, sha256 `743ec030c17a4ac835f1e79404a043c649a1f6a84aad07784e1ad0fff4f75b28`)
  and as plain 11-cell text (`Kb80E12Census-S232-S243.rows.txt`). `Kb80S16CensusLog.md` states it
  derived the same 12-row block at the same id range from the same NegSweep records but does not
  publish its text. The L1 must pick one; the id ranges (S232–S243 vs S244–S248) and the counts do
  not conflict, and the 7 new W04 lines are identical under either text.
- **The round-80 counter is currently byte-identical to the r79 draft** (sha256
  `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6` for both), so its `ENTRY`
  constant is still the round-79 path and its headline is still "backed N of 6" with target N >= 5.
  The conjunct-(b) harness here rebinds `ENTRY` by hand; the round-80 bytes must be the counter
  seat's own.

## Addendum (published after the first yield; lane HEAD had moved to `a481913`)

Verifying my own receipt surfaced four facts that bear on the C1 stack, measured by this seat with its
own exit capture. Full write-up with every command: `.ufo/waves/round-80/build/Kb80E12Census-C1StackFindings.txt`.

1. **The plan's two `commit_unresolvable` tokens were the wrong ones.** At base both corpus gates read
   `commit_unresolvable=2` at `corpus/SOURCES.md:171` and `:172` — the same hash
   `7bb48f213ac677f943d5c791199ed3dddf302f00`, in rows S230/S231. The plan's `451a02ff` / `cfb894a5`
   are `commit_quoted` context, already excluded. The line shape is "resolved to `badlogic/pi-mono`
   commit `7bb48f21…`" — the repo name is a separate backticked token on the same line, so an
   in-token `owner/repo@<hex>` grammar clears nothing; the class must work at line scope. **The L1
   has since landed this correction as `plans/round-80.md` § Addendum 2 (commit `a481913`), crediting
   Kb80V03Instruments; this seat measured it independently and agrees.**
2. **The size cap is tighter than the plan's arithmetic.** The `instrument-size` guard diffs against
   the counter's pinned r72 base `072048fa`, not `398cbe1`: base 22/3 added/deleted, +E04 = 39/3,
   +E04 + the published grammar world = **210/8** — a hard `FAIL guard instrument-size: instruments
   gain 210 lines > 60` under `LINE_CAP = 60`, with only `60 - 39 = 21` added lines available for the
   class across BOTH gates. E04 alone is green on that guard (`guards 5 of 5`, `1 of 6`, exit 1).
3. **The two blob ids E06 must pin**, derived by composing E04 with the published grammar world
   (order-independent): `c500949706c886bc1ac4ec3985ba9e7b4767a2cc` (integrity) and
   `77814259ea88e252010bcecedd142b21b91be297` (independent) — valid for the published bytes only;
   recompute on E05's landed tree if those differ.
4. **S230's anchor names the wrong repository's commit.** `git fetch … badlogic/pi-mono 7bb48f21…` →
   "not our ref"; `git ls-remote … mistralai/mistral-vibe refs/heads/main` → `7bb48f21…`; pi-mono
   serves 404 at that sha, mistral-vibe 200; and pi-mono's file at the fetch-time head its own fetch
   record names (`bb65e3e4971…`) hashes to exactly the committed `snapshots/S230-pi.md`. The bytes are
   right; only the anchor's commit id was copied from S231. The grammar class will therefore mislabel
   the row ("repo badlogic/pi-mono" for a mistral-vibe commit) inside the very INFO class the repair
   opens, and the anchor is a protected cell (only `status`/`recheck`/`used-by` may change in place),
   so the correction is a supersede row, never an in-place edit (M45). Reported, not repaired — also
   found independently by Kb80E08C2Entry and Kb80V03Instruments.

## Evidence honesty

Every figure above carries its command and its own exit status; no verdict was read through a
pipeline. The before block is the lane tree at base; the after block is a scratch clone carrying the
integrated edit set plus two **placeholder** files (the entry and the lesson) that exist only to
satisfy E11 — they are not in any published patch, and they prove the row arithmetic, not the
content of the entry or the lesson. The L1's post-integration census on the real tree supersedes this
receipt on the same counts.

## Verification the main agent should run after integration

    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotoba
    grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
    grep -cE '^\|[[:space:]]{0,3}S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
    python3 -B verifiers/check_sources_append_only.py --rev <tip> --repo .

Expected: exit 0 and `ok`; rows 174 (if this seat's S232–S243 text is adopted) or 174 (if S16's is —
the count is the same either way); W04 31; append-only breach count unchanged at 18.

VERDICT: census measured at base and after the integrated edit set — exit 0 in both, 157 -> 174 rows (W04 24 -> 31, warning class), 11-cell rows verified, every new row quoted from bytes opened this round; plus four cross-seat findings for the C1 stack (the base unresolvable tokens are at SOURCES.md:171-172 and the class must work at line scope — the L1 has since landed this as plan Addendum 2; the LINE_CAP=60 budget leaves 21 added lines for a grammar class whose published shape spends 171, so instrument-size hard-fails at 210; the two composed blob ids E06 must pin; and S230's anchor names mistral-vibe's commit for pi-mono, which the grammar class would mislabel).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-S232-S243.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-S232-S243.rows.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-before.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-after-174.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-after-root-174.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-after-independent-patch.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-mode-before.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-census-mode-after-root.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-rows-before.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-rows-after.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-e11-control.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-appendonly.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-fetch-records.tsv, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E12Census.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-C1StackFindings.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-numstat.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-int-e04-grammar.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-ind-e04-grammar.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-battery-e04only.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E12Census-battery-e04-grammar.txt
