# CriticClaims — pre-score attacks on round-90 claims C1 and C2

Seat: CriticClaims (critic, leaf). Base `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`; frozen plan
`6af71591e7232a7eebbaff78e7db653a70c7218b`. Findings only. Nothing in the lane was edited; no scored
reading was made. Scratch: `/fast/scratch/hyaku/kotoba-r90/CriticClaims` (removed at yield).

## 1. Controls re-run (all six)

Command: `bash verifiers/fixtures/round-90/<ctl>.sh` from the lane root.

| control | rc | observed stdout |
|---|---|---|
| ctl-c1-absence | 1 | `C1-PREDICATE-UNMET no verifiers/check_mutation_battery.py at 0c20d8ab…` |
| ctl-c1-r89harness | 1 | `C1-PREDICATE-UNMET r89 harness present but no registered instrument (registry rows naming it: 0)` |
| ctl-c1-stub | 1 | `C1-PREDICATE-UNMET stub prints the line (rc=0) but manifest/registry guard fails (registry rows: 0)` |
| ctl-c2-windows | 1 | `C2-PREDICATE-UNMET r84 Windows-root form rc=2: could-not-evaluate: skills root absent: C:/Users/jpvei/.agents/skills` |
| ctl-c2-empty | 1 | `C2-PREDICATE-UNMET empty root rc=0: host skill surfaces measured 0: identical 0, drifted 0, lane-absent 0` |
| ctl-c2-fake | 1 | `C2-PREDICATE-UNMET fake root rc=0: host skill surfaces measured 1: identical 0, drifted 0, lane-absent 1` |

No control meets its predicate, so no claim dies on the controls. The controls are weaker than their
declarations (F12), and the C2 control set misses the real failure (F1).

## 2. Findings

Severity: **high** = blocks the claim or clause as written; **medium** = clause unmeasured or shortcut
open, bounded only by receipts; **low** = wording or hygiene.

### F1 — C2 freshness is unmeasured: the frozen predicate passes a run that compared nothing (high, blocks C2 freshness wording)

Predicate (plan C2): exits 0 printing `host skill surfaces measured N: identical I, drifted D, lane-absent A`
with `N == 83`. Frozen fleet-root argument: `--fleet-root /home/vgpnk/Projects/shokunin`.

Command (read-only, output in scratch): `python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills --fleet-root /home/vgpnk/Projects/shokunin`
→ rc=0, observed: `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`
(`LANE-ABSENT` lines: 83; `OK`/`DRIFT` lines: 0).

Cause: the 19 `<name>/SKILL.md` dirs under the fleet root are lane directories (`chousa-shokunin` …
`tsukuroi-shokunin`). None of the 83 host skill names matches one. Contrast: `--fleet-root /home/vgpnk/Projects/ompskills/.omp/skills`
→ `host skill surfaces measured 83: identical 3, drifted 0, lane-absent 80` (rc=0). The comparison target decides the outcome.

Consequence: I+D+A==N==83 holds on an all-lane-absent run, so C2 can be scored "met" while measuring no
drift. The plan's "honest all-clear" reading does not apply: nothing was compared. Route: the L1 names the comparison tree in an
addendum before scoring, or reduces the C2 wording to "measurability of the host census restored". The
frozen fleet-root argument must not be cited as evidence of freshness.

### F2 — C2 `I + D + A == N` is a tautology (medium)

`verifiers/check_host_skill_surfaces.py` lines 109–114: `counts` is built from the same `rows` list that sets
`len(rows)`, and every row takes exactly one class. The sum equals `len(rows)` by construction. Only
`N == 83` carries content, and the I/D/A split cannot fail.

### F3 — C2 population bound is a literal, with a prose command that counts a different set (medium)

The predicate pins `N == 83`. The plan's population command is prose: `ls /home/vgpnk/.agents/skills | wc -l`.
The census counts a different set: `census()` lines 49–52 count `p.is_dir()` entries that contain `SKILL.md`
and skip the rest silently.

Observed today (scratch, read-only): `ls | wc -l` → 83; `ls -A | wc -l` → 83 (no hidden entries);
`iterdir` dirs → 83; census-style count (dir + SKILL.md) → 83; non-directory entries → 5 symlinks, all
resolving (`omarchy`, `tower`, `shokunin`, `ufo`, `swarm`; targets under `~/.local/share/omarchy` and
`~/Projects/ompskills`); broken symlinks → 0.

The two sets coincide today by accident. Any file, or any directory without `SKILL.md`, separates them.
Mid-round change: one added skill → census rc=0 with `N=84` → predicate unmet. The plan has no rule for which run
counts when two runs disagree, and no rule that separates population drift from instrument failure. The
outcome is derivable only from the transcript receipt. Bounded by receipts, not by the predicate.

### F4 — C2 shortcut: installed copies that are symlinks or byte-copies of lane files pass as `identical` (medium)

The census records sha256 only, not the realpath of each installed `SKILL.md`. 83 symlinks into the fleet, or
83 byte-copies of lane files, would classify as `identical` with no host evidence. The controls cover 0 files
(ctl-c2-empty) and 1 file (ctl-c2-fake), not the copy farm. No guard catches it. On the live host the 5 symlinks
point outside the lane (F3), so this host is not gamed today. Route: the census receipt should record
`readlink -f` per row; the predicate does not change.

### F5 — C2 A1 name-uniqueness is asserted but not gated (medium)

The predicate requires only that `c2-name-collisions.txt` exist and states a `grep -c NAME-COLLISION` count.
The count is not part of the predicate, and `grep -c` also counts header lines containing the token. The claim's
"A1 name-uniqueness rule re-verified" wording is therefore unmeasured. Bounded: the receipt is report-only, but
the claim must not read the A1 rule as passed unless the count is read.

### F6 — C1 vacuous pass on an empty manifest (high, blocks the C1 predicate as written)

Predicate (plan C1): exits 0 iff `K == M` and `E == E` and `S == S_declared` and guards G1–G3 PASS, where
M, E, S_declared are the class counts of `verifiers/fixtures/mutation-battery/manifest.tsv`. An empty manifest gives
M = E = S = 0, so all three equalities hold. G1 (every probe through `git show`) and G2 (sha check of mutated
files) quantify over an empty set and pass vacuously. G3 needs only a `SKILL.md` row naming the battery, which
the L1 lands at integration. No frozen control covers an empty-manifest world (ctl-c1-stub covers a stub
printing the line, not a manifest). The self-test (Q48 arm) drives a satisfying fixture the author supplies.
Route: the L1 adds a lower bound on K (at least the r89 kill count, 13) through an addendum before any scored reading,
plus a frozen control `ctl-c1-empty`. Seats do not edit the predicate.

### F7 — C1 "two-sided" equivalence is circular (high, blocks the Q47 clause)

"Equivalent" is defined as "survives", and survival is the only check. Round-89 evidence
(`.ufo/waves/round-89/w1/MutTesterGates/equivalents.tsv`): 10 rows, 10 `survives`, 0 killed. Nothing checks that a
rewrite is behaviour-preserving. A behaviour-changing rewrite that the fixtures do not reach counts as "equivalent
survived" and passes `E == E`. `harness.py` lines 258 and 263 flag only killed equivalents (`KILLED-BY-EQUIVALENT`).
The S260 source itself says Stryker "There is no definitive way … to find and ignore them" (quote Q3, line 16 of
`s260-snapshot-equivalents.html`), so no tool can verify equivalence automatically. Route: an addendum before scoring
with an independent equivalence check (for Python instruments, `ast.dump` equality between mutant and base, computed
by the battery), or the claim states equivalence as a labelled assumption.

### F8 — C1 self-test-only kills count as kills (medium)

`.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`: 13 kills, 1 survivor. Three of the 13 kills rest on `--self-test`
alone: `fg-m2b-control-skip-last`, `fg-m3b-ladder-eval-to-1`, `fg-x1-parse-drop-exit-clause`
(`tail -n +2 mutants.tsv | grep -c 'killed by self-test:'` → 3). The predicate does not constrain probe identity, and G1–G3
do not inspect it, so a manifest whose probes are all `--self-test` would satisfy `K == M`. This is the Q37 shortcut
the guards do not catch. Route: report the probe kind per mutant; require at least one fixture-world kill per
kill-class mutant (addendum before scoring).

### F9 — C1 universality is unmeasured (medium)

M is a hand-chosen manifest: 14 mutant rows in r89 across the two instruments, with no denominator from the
instruments' code. "Depth" is measured only over the committed manifest; any universal reading ("the battery kills
the instruments' defects") is unmeasured. Route: scope the C1 wording to "over the committed manifest" unless the
L1 adds a generation denominator before scoring.

### F10 — C1 claim text contradicts the predicate on equivalent generation (medium)

The claim says the equivalent class "is generated at measurement time … not a fixed published list". The predicate
counts `E` from the committed `manifest.tsv`, so a runtime generator must reproduce a committed count, and the identity
of the equivalents is never compared. The r89 precedent is a fixed list: `harness.py` line 121 `FG_EQUIV = [`, line 176
(plan-level equivalents), line 342 `D5_EQUIV = [`. Route: align the claim sentence to "counts match the committed
manifest", or record each generated rewrite's sha in the manifest.

### F11 — C1 survivor disposition is unmeasured; a known survivor sits inside a "depth" claim (medium)

The predicate checks `S == S_declared` only. The claim promises a committed disposition reason per survivor; the
predicate does not check that a reason exists. The r89 survivor `d5-m1a-d5iii-leg-only` (mutants.tsv) reads `SURVIVED`,
with identical before/after outputs (`w_tip=0 w_healed=0 w_added_instance=1 w_silenced=1 w_rerecorded=1 w_newname=1`).
That is a real gap in the D5-III check (leg-only removal is not caught), and the r89 TSV has no reason column.
Route: the manifest gets a reason column, and the predicate (or the self-test) requires it non-empty.

### F12 — C1 controls cannot discriminate a counter that does not yet exist (medium)

- `ctl-c1-absence` only runs `git cat-file -e $B:…` (base-pinned).
- `ctl-c1-r89harness` only reads `$B:SKILL.md` and the `$B:` harness bytes (base-pinned).
- `ctl-c1-stub` runs a scratch stub that prints the success line, and its verdict is decided by
  `git show $B:SKILL.md | grep -c 'check_mutation_battery.py'`. It never reads a manifest, so the message "manifest/registry
  guard fails" does not describe what the script executes.

All three are constants over base bytes and cannot fail on a counter that reads a manifest. The first discriminating test
of the C1 predicate is the battery's own self-test, which the author supplies. The "6 control(s) held" receipt is accurate
but overstates C1's pre-data coverage. Bounded: these are declared pre-data sanity checks, not discriminators.

### F13 — C1 predicate notation `E == E` is ambiguous (low)

The frozen sentence uses `E` both for the survived count and the declared count. The printed line
`equivalents survived E of E` does not disambiguate. The implementer must choose `E_survived == E_declared`; an addendum should
pin the formula before the battery prints it.

### F14 — C2 Windows-root control tests only path absence (low, bounded)

`ctl-c2-windows` exits 2 (`could-not-evaluate: skills root absent`). It proves only that the Windows path is absent here. It
does not test that the census rejects a stale root that exists. Bounded.

### F15 — S260 candidate `teaches` asserts clauses no located quote grounds (medium; row must be fixed before admission)

Candidate row: `.ufo/waves/round-90/w1/ScoutMutSource/s260-notes.md` line 178 (the scout's proposal, parsed: 11 cells, no
embedded pipes). Its `teaches` cell reads "an equivalent mutant is indistinguishable from the original, survives by
construction and cannot be auto-ignored, so it caps the attainable score rather than exposing a test gap". Checks:
`grep -ci 'indistinguish' s260-snapshot.html s260-snapshot-equivalents.html` → 0 and 0; `grep -ci 'by construction'` → 0 and 0.
The located quote (line 16, Q3) supports only "no definitive way for Stryker to find and ignore them". "Caps the
attainable score" is a derivation from the score formula, not a page statement. Contract rule 1 requires the Gate to ground
`teaches` with a located quote of ≤25 words. Route: the scribe narrows `teaches` to what Q3/Q1a/Q1b/Q2a/Q2b state, or adds a
located quote for each asserted clause.

### F16 — S260 `status: mined` before its `used-by` file exists (medium; ordering)

The candidate row has `status` `mined` and `used-by` `corpus/knowledge/mutation-battery-round90.md`. Contract census line 80
requires that every `mined` row's used-by paths exist ("must print nothing"). At the check time,
`ls corpus/knowledge/mutation-battery-round90.md` → `No such file or directory` (rc=2). The ScribeCorpus must write the knowledge
entry before the row is set to `mined`, or the row lands as `queued`. The S260 row therefore cannot be admitted in the order the
candidate implies.

### F17 — S260 anchor cites no revision the contract accepts (low)

Contract: anchor = section/line plus "revision (version, commit, or publication date)". The candidate anchor cites byte size and fetch
date (`fetched 2026-11-05`). The page sends `last-modified` headers: `s260-headers-stryker-states.txt` →
`last-modified: Wed, 04 Nov 2026 19:10:23 GMT` (the equivalents page is `19:10:22`, the docs index `19:10:22`). The
states page's `Last-Modified` date is the revision anchor the contract asks for. Route: add it to the anchor cell.

### F18 — S261 has no candidate row in any wave output (low; cannot be checked)

Item 5 asks for S260 and S261. The only S261 reference in the scout output is `ScoutMutSource.md` line 81
("those are S261"). No own-work candidate (`corpus/lessons/…`, the r89 MutTesterGates bytes) exists in the w1 outputs, so the
S261 row cannot be checked against contract v1 here. Carried, not a pass.

## 3. Claim verdicts

- **C1 (depth):** blocked as written by F6 (vacuous pass) and F7 (circular equivalence). F8 (self-test kills) is a second
  shortcut the guards miss. Unblocked only by an addendum before any scored reading. F9–F13 bound the wording.
- **C2 (freshness):** the predicate is met on a run that compared nothing (F1), so the freshness wording is blocked. The
  measurability claim (census ran on the host's root, N == 83) stands, with the F2/F3/F4 caveats.

## 4. SOURCES candidate check (item 5)

Inputs: `SOURCE_READY` (content `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/`);
`ScoutMutSource/s260-notes.md` (candidate row, line 178); `ScoutMutSource/s260-quote-receipts.txt`; contract
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`.

Checks run:
- Quote grep against saved snapshots: `When at least one test failed while this mutant was active, the mutant is killed.` (s260-snapshot.html) → 1;
  `When all tests passed while this mutant was active, the mutant survived.` → 1; `detected / valid \* 100` → 1;
  `There is no definitive way for Stryker to find and ignore them` (s260-snapshot-equivalents.html) → 1. Lines 12, 14, 51, 52 and 16 match the receipts.
- Word counts (quote receipts, reproduced by hand): Q1a 15, Q1b 12, Q2a 12, Q2b 5, Q3 17. All ≤ 25.
- Cell count: 11 (12 pipes, none embedded). Tier `A`, scoped to the vocabulary "as the tool's own documentation states them". Kind `docs`. Opened `2026-11-05` (ISO). Recheck `180d` (cadence). Status `mined`.
- Pipes inside cells: none. Enum violations: none.
- SOURCES census (rows): 185 at base. My `rowcheck.py` on the existing table: `violations: 0`.

Result: the S260 row is structurally valid (11 cells, tier-scoped, quotes located and sized correctly), but it is not admissible
as written. F15 (teaches overreach) and F16 (mined before used-by exists) must be fixed first; F17 (anchor revision) is a low-severity improvement.
S261: no candidate in the wave outputs (F18), so the expected 185 → 187 census cannot be checked from this seat.

## 5. Scope note

The seat wrote only under `.ufo/waves/round-90/w1/CriticClaims/` and the report trailer
`.ufo/waves/round-90/w1/CriticClaims.md`. No git or jj write was run. No lane file was edited.
