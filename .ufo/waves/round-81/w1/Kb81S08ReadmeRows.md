# Kb81S08ReadmeRows — coverage rows + Frontier note (round 81, w1)

Role: scribe, leaf member (no subagent dispatch). Wave: round-81 w1 (v2, 64 seats). Lane base:
`b284223105f4d106f7e8f56ed4fd296c643cda0e`. Lane files edited: **none** — this seat's output is a
fragment file and two patches under `.ufo/waves/round-81/build/`.

## What was produced

1. **Three coverage-map rows** for `corpus/README.md`, in the round-79 row style (three cells; the
   basis cell carries colon-separated clauses and a `counted by …` trailer):
   - `corpus/lessons/round-80-verifier-spotcheck.md` — closure-owned; indexed, never edited. This is
     the row plan R4 asks for (the file landed at `b284223` with no index row).
   - `corpus/lessons/round-81.md` — this round's lesson (its `## Gate`/`## Mistakes`/`## Sources &
     frontier`/`## Status changes` shape, the C1/C2 base readings, R1–R6 and erratum E6).
   - `corpus/knowledge/allowed-tools-sdk-round81.md` — the SDK-channel documentary entry (S249,
     S248 `used-by` old→new, snapshot `.ufo/waves/round-81/snapshots/S249.md`, counter
     `verifiers/check_sdk_allowed_tools.py`).
2. **The append-only `## Frontier` note** for round 81: the Agent SDK `allowedTools` /
   `allowed_tools` query-config channel entering Core under the allowed-tools area (beside the
   frontmatter field, with the `allowManagedPermissionRulesOnly` override), plus what stays
   frontier — no client run, and the frontmatter rules for skills synced from claude.ai that the
   SDK page only points at. No new Frontier table row, following round 80's precedent (a note, not
   a row: the table carries areas wholly unheld; the allowed-tools area is now held in part).
3. **Two patches** that apply cleanly to a pristine clone of the base:
   `Kb81S08ReadmeRows.patch` (all four fragments, `5 +++++` lines, additions only) and
   `Kb81S08ReadmeRows.stageA.patch` (row 1 only, for landing the index repair ahead of the round-81
   files).

Fragments in the build file were diffed byte-for-byte against the file the patch produces: all four
are IDENTICAL (script check in this seat's scratch, output `IDENTICAL` ×4).

## Gates (measured, never piped — exit captured directly)

| measurement | command | result |
|---|---|---|
| base tip battery (inherited receipt, re-read) | `cat .ufo/waves/round-81/receipts/tipbattery-base-dot.txt` | `guards 5 of 5; tip battery exit 0: 4 of 6`; `verify_corpus_integrity.py exit 1`, `verify_corpus_independent.py exit 1`, four other gates exit 0 |
| corpus integrity, stage A (row 1 only) | `python3 -B <lane>/verifiers/verify_corpus_integrity.py --repo $S/clone --json --no-baseline` | rc=1; `unindexed 0` (was 1), `stale_patterns 0`, `missing_paths 0`, `report_dead 1`, `commit_unresolvable 2` |
| corpus integrity, stage B (full fragment) | same | rc=1; `unindexed 0`, `stale_patterns 2`, `missing_paths 2` — both naming only `corpus/README.md:161` and `:162`, i.e. my two forward rows |
| independent gate, base | `verify_corpus_independent.py --repo $S/clone2` (after `apply -R`) | rc=1; `unindexed 1`, `commit_unresolvable 2`, `report_dead 0` |
| independent gate, patched | same, patch applied through the `.patch` file | rc=1; `unindexed 0`, `stale 2`, `missing 2` |
| patch application | `git -C $S/clone2 apply --check Kb81S08ReadmeRows{,.stageA}.patch` | both 0 |
| SDK page bytes (data only) | `curl … -w 'http=%{http_code} bytes=%{size_download}'` + `sha256sum` | `http=200 bytes=28395`; `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` — identical to S248's committed fetch record |

I did **not** run the tip battery, the no-harm battery or any claim after-value: out of this seat's
scope, and no after-value may be scored by a seat.

## Touched surfaces

- Wrote: `.ufo/waves/round-81/build/Kb81S08ReadmeRows.md` (fragments + evidence),
  `Kb81S08ReadmeRows.patch`, `Kb81S08ReadmeRows.stageA.patch`,
  `Kb81S08ReadmeRows.integrity-stageA.json`, `Kb81S08ReadmeRows.integrity-stageB.json`,
  `Kb81S08ReadmeRows.indep-base.txt`, `Kb81S08ReadmeRows.indep-patched.txt`,
  `Kb81S08ReadmeRows.s249-fetch.md.txt`; this report.
- Read only: `plans/round-81.md`, `corpus/README.md`, `corpus/SOURCES.md` (S230/S231/S248),
  `corpus/lessons/round-80-verifier-spotcheck.md`, `SKILL.md` (§ Frontmatter craft, § Gate registry),
  `PROVINCE.md` (§ Core), `verifiers/verify_corpus_integrity.py` (index/check layer),
  `.ufo/waves/round-81/{w1-spec.json,receipts/*}`, `.ufo/waves/round-80/` paths named by the brief.
- Scratch: `/fast/scratch/hyaku/kotoba-r81/Kb81S08ReadmeRows/` (two clones under it), removed before
  yielding. No git/jj mutation outside those clones; no commit, add, stash or checkout in the lane.
- Tooling: no installs, no upgrades, no `pacman`. Nothing written outside the lane's
  `.ufo/waves/round-81/`.

## Out of scope (deliberately untouched)

`corpus/README.md` itself (L1 integrates the patch), `PROVINCE.md` § Core, `SKILL.md`
`allowed-tools` line and registry row, `corpus/SOURCES.md` (S249/S250 rows, S248 `used-by`),
`corpus/lessons/round-81.md`, `corpus/knowledge/allowed-tools-sdk-round81.md`, `verifiers/*`
(instruments, `external-commits.json`, the new counter), `verifiers/corpus-baseline.json`,
`.ufo/wapes` disposition, `MANIFEST.json`, the plan.

## Findings (reported, not repaired)

1. **S248 and the plan's S249 are the same source.** `corpus/SOURCES.md:189` already cites
   `https://code.claude.com/docs/en/agent-sdk/skills.md` (tier B, opened 2026-10-27, 28395 B,
   sha256 `ac62c2df…`); the plan gives S249 the same URL, size and hash. A second row for the same
   URL adds one W04 duplicate-URL warning (base: 31 in `receipts/census-before.txt`) and a 175th
   index token. My row cites S249 as the plan and the C2 predicate require; if the C2 seat instead
   re-opens S248 in place, one token swap in row 3 (`S249`→`S248`, drop the `used-by` clause) keeps
   it true. Assignment is the plan's, not mine.
2. **The plan's independent-gate description is imprecise at base.** Plan §Trigger: independent is
   red on "`commit_unresolvable` 2 plus `report_dead` 1". Measured at `b2842231`: `unindexed 1` +
   `commit_unresolvable 2`, `report_dead 0`, exit 1; `report_dead 1` is the integrity gate's class
   (`corpus/lessons/round-77-verifier-spotcheck.md:15`). Worth a precise sentence in the lesson's
   `## Gate`; no narrowing or repair attempted here.
3. **Forward-row ordering is load-bearing.** Rows 2–3 flip `stale_patterns`/`missing_paths` to 2 in
   both corpus gates until `corpus/lessons/round-81.md` and
   `corpus/knowledge/allowed-tools-sdk-round81.md` exist, so they must land in the same commit (or
   later in the wave) as those files. Row 1 is safe to land alone and is the only repair this seat
   can prove on its own (`unindexed` 1 → 0).
4. **The Frontier note and row 3 are C2-gated.** If C2 honest-stops, both must be dropped; landing
   them would claim an entry, a counter and a PROVINCE clause that do not exist.

## Limits

- I did not read `corpus/knowledge/allowed-tools-sdk-round81.md` or `corpus/lessons/round-81.md` —
  they do not exist yet — so row 3 and row 2 describe the entry and lesson the plan declares, with
  every technical claim in row 3 taken from the fetched page bytes (sha-pinned) rather than from
  another seat's draft. The L1 must reconcile row 2's clause list with the landed lesson and row 3's
  wording with the landed entry; the fragments are otherwise ready to apply unchanged.
- No claim after-value was measured, asserted or scored by this seat.

VERDICT: three ready-to-apply coverage rows (r80 closure indexed; r81 lesson; SDK channel entry) plus the round-81 append-only Frontier note, both patches `git apply --check` clean and their fragments byte-identical to the patched file; row 1 provably clears `unindexed` 1→0 in both corpus gates, rows 2–3 must land with their files, no claim score touched.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.stageA.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.integrity-stageA.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.integrity-stageB.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.indep-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.indep-patched.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S08ReadmeRows.s249-fetch.md.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S08ReadmeRows.md
