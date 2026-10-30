# Kb82C07Evidence — Receipt chronology and sandbox-citation attack

Seat: Kb82C07Evidence (critic). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Method: static attack only — no production scoring, no after-value runs, no seat
commits, no subagents. All findings derive from files that exist (or don't) at
attack time; every hash claim below was re-measured by this seat.

## Attack surface

- 89 unique 64-hex sha256 digests cited across 37 w1 reports.
- 436 raw path tokens extracted from w1 reports; 76 survived cleaning
  (trailing markdown/backtick/line-ref stripped) as candidate absent pointers,
  each mapped to its citing report.
- 15 receipts in `.ufo/waves/round-82/receipts/` + 15-row S12 index + all
  build artifacts sized and hashed.
- Date sweep (ISO dates and timezone-qualified datetimes) across
  build/receipts/w1/snapshots against wall clock.
- Pipe/exit-capture sweep over reported commands.

## What survives the attack (checked, clean)

1. **No orphan hashes among load-bearing citations.** 45/89 digests resolve to
   round-82 artifacts directly. Every remaining traced claim verifies against
   exactly what the report names:
   - base-47dbe87 blobs via `git show`: counter `629487a1…`
     (check_substrate_repin_v2.py), `b7d7b0fca8be…` (verify_skill_checklist.py),
     `c896e5b91d…`/`ddc925e35468`-vs-base-`c896e5b91d…` world stub pairing,
     `df0c7ccaab…` (verify_surfaces.py), `d7b767d61798…`,
     `8201a3a09d5c…`, `e1f95d2fe8be…`, `f41413e2b441…`, `d6b172065f86…`
     (SOURCES.md base), S05Log's `d60d3ba3…` (Kb81S04Report-final.md).
   - HEAD files: `9b2e79a43b7f…` SCORECARD.md, `c48d3340ad83…` SOURCES.md,
     `4938523a87a0…`, `5de7a8922a54…`, `c6c83d9a5895…`, `53d28b669938…`,
     `f36644f98410…`, `fd747ca4…`, `945eb49e6ab3…`, `979a06aa893c…`,
     sibling-lane PROVINCE.md set `31af2bb6…/6c3694f9…/933e1233…/b0cb62ab…`.
   - fleet/shokuknow files: PROTOCOL.md `886e459b…`, templates/round-prompt.md
     `b48b57ca…`, SHONEN.md `c42f6bff…`, MERGE-REPORT.md `839f924a…`,
     absent-defect-register `5afe1810a6c3…`, staged append `e2bdff3fe7b1…`.
   - host measurements: omp `e7dd2b60…`, opencode `ca9b3ee2…`, opencode
     strings dump `020fb25393e5…` (re-run by this seat: MATCH),
     omp-swarm `3c95602c9…`.
   - S12 index: all 15 rows re-hashed OK.
   - Reconstruction proofs: E03 patch→`24fec2837ce5…` MATCH; S07 patch
     →`ed294d2106c2…` MATCH.
   - Historical pins `85d9daf3a05f…`/`fdbc8136084c…`/`ed62a41ec662…` are
     labeled as past-host values and equal the pin-JSON expectations in
     before-pins.txt. Not orphans.
   - Only non-verifiable digests are self-labeled sandbox transients
     (S10SourcesLog's curl'd HTML, explicitly "removed with scratch";
     S07's normalized-text intermediate). Both labeled at cite time.
2. **No future dates.** Latest in-wave datetimes
   (`2026-10-30T15:10:42Z` C06 freeze-final, `15:18:53Z` N01 host receipt)
   precede attack wall clock (15:32Z). Receipt chronology is monotone:
   before-pins 11:25 → before-c1-counter 11:29 → host-open 11:32 local
   (14:25→14:32 UTC); host binary mtime 2026-10-30T02:19:46Z precedes all
   receipts; S03 current-bytes mtime equals host-open's mtime_ns.
3. **No pipe-masked exits in the before receipts** — each ends with a
   command-owned `exit=N` line. Pipe uses elsewhere either don't capture
   exits or report grep rc=1 semantics correctly (R07Consider);
   R08Merge explicitly disclaims its echo-statused listing as evidence.

## FINDINGS

### F1 — huge unneeded evidence artifact (the 47MB strings dump) — HIGH

`build/Kb82E12Loader-omp-18.14.0-strings.txt` is **47,434,077 bytes /
2,546,730 lines** — 99.9% of the wave's entire 47 MB build footprint. It is a
raw, unfiltered `strings` dump of the 276 MB host binary, and E12 lists it as
a DELIVERABLE (Kb82E12Loader.md:126).

- The dump is byte-reproducible from the pinned host binary: its sha256
  `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319` is
  independently recorded hash-only by E11 and E02Pins
  (`build/omp-18.14.0.strings.sha256.txt`,
  `build/Kb82E02Pins-omp-18.14.0.strings.sha256.txt` — this seat re-hashed the
  dump: MATCH). Keeping the bytes adds zero evidence over keeping the digest.
- The actual evidentiary content (loader-group call pairs, instruction
  literals) was extracted into small filtered artifacts by multiple seats:
  `Kb82E11Loader_anchors_excerpt.txt` (11,125 B), `Kb82R01Host-embedded.txt`
  (89,214 B), `Kb82E15Loader-host-calls-anchors.json` (12,022 B).
- This is precisely the pattern round-80 w1 row 12 ("evidence byte budget")
  warned about, and considerthese 2026-10-26 proposal P1/P5 (evidence growth
  budget) — both recorded in-wave (R07Consider F1, Kb80K03Considerthese.md:12).
- Smallest safe correction: delete the dump from the wave tree before L1
  freeze/integration; retain the two hash-only receipts and the filtered
  extracts. Re-derivation is one `strings -n 4` away from the pinned binary.

### F2 — wrong-directory citation: Kb80K03Considerthese — MEDIUM

Kb82R07Consider.md:5 (Sources line) cites
`.ufo/waves/round-80/build/Kb80K03Considerthese.md:12`. That path does not
exist — round-80/build/ has 469 entries, none named Kb80K03*. The intended
file is `.ufo/waves/round-80/w1/Kb80K03Considerthese.md`; its line 12 is the
"evidence byte budget / compress seat logs" row, matching the citation's
intent. Absent-file pointer at the cited path; content claim itself is
accurate. Correction: `s/round-80\/build/round-80\/w1/` in R07Consider's
Sources line (L1-side integration edit; no seat file ownership violated).

### F3 — generated bytecode inside the evidence tree — LOW

`build/__pycache__/` contains `Kb82E11Loader_probe_gemini.cpython-314.pyc`
and `Kb82E12Loader-probe.cpython-314.pyc` — derived CPython artifacts, not
evidence; stale-.pyc hazard if probe sources are edited and re-run.
Correction: remove `build/__pycache__/` at integration.

## Non-findings recorded to bound re-litigation

- `.ufo/reports/round-81/kotoba.md` is genuinely absent (never landed in any
  commit) and appears in-wave only as the *known dead citation* being flagged
  (before-checklist-selftest, S04), not as evidence — correct usage.
- Scratch-path citations (`/fast/scratch/hyaku/kotoba-r82/…`) are labeled
  deletable work areas; every receipt they produced was copied into build/
  first (spot-checked E10, E06, K01). Acceptable.
- E06Controls W3's `verifiers/sandbox-fake-omp.elf` is a *proposed* world
  fixture committed inside its scratch clone (world receipt exists), not a
  claim that the lane tree contains it. Correctly scoped.
- 5 dispatched seats have no w1 report at attack time (C02Hermetic,
  C04FalseRed, C05Routed, R09Sources, and this seat) — wave still running;
  not absent-file evidence.
- `Kb82E02Pins-omp-18.14.0.strings.sha256.txt`'s recorded pathname points at
  the seat's scratch layout; it is a measurement receipt, not a pointer.

## Axes impacted

- **freshness (C1)**: F1 sits inside the loader re-derivation evidence chain
  (S251). The derivation result (extracted pairs) is unaffected; the wave's
  evidentiary bulk violates the byte-budget discipline the fleet already
  records as a tracked concern.
- **operability (C2)**: F3 is tooling-tree hygiene adjacent to the hermetic
  self-test work; F2 is reviewer-citation accuracy (governance of evidence),
  not gate behavior.

## Verification budget

Read-only static analysis + sha256sum/git-show reconstructions in this seat's
scratch (`/fast/scratch/hyaku/kotoba-r82/Kb82C07Evidence/`); no installs, no
pacman, no production mutations, no after-value scoring. Disk guard not
needed (bounded text work).

VERDICT: 3 findings — F1 HIGH (47,434,077-byte reproducible strings dump is 99.9% of wave build bytes; keep hash-only receipt), F2 MEDIUM (R07Consider cites round-80/build/Kb80K03Considerthese.md; file is at round-80/w1/), F3 LOW (build/__pycache__ bytecode in evidence tree). No orphan load-bearing hashes, no future dates, no pipe-masked exits, no absent sandbox pointers beyond F2.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C07Evidence.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C07Evidence-audit.txt
