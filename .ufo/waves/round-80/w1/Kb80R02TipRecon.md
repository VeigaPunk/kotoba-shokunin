# Kb80R02TipRecon — independent base-gate re-derivation (round 80 w1)

Seat: Kb80R02TipRecon (scout, leaf). Date: 2026-10-27.
Measured rev: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (r80 base) in a scratch clone
(`/fast/scratch/hyaku/kotoba-r80/Kb80R02TipRecon`, fleet-shaped: every fleet-root entry
symlinked beside the clone; removed after the runs). All verdicts captured by each
command's own exit status (`cmd > f 2>&1; rc=$?; echo "exit=$rc" >> f`) — no pipelines.
Counter bytes: the lane's current `verifiers/` (same bytes the battery itself checks out
at base). Receipts: `.ufo/waves/round-80/build/Kb80R02TipRecon/` (sha256s at the bottom).

## 1. The battery, re-run

Command (the seat-prescribed form):
`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py --repo $S/clone --rev 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`

Result: `guards 5 of 5; tip battery exit 0: 6 of 6` does NOT hold at base — the line is
`fleet root /fast/scratch/hyaku/kotoba-r80/Kb80R02TipRecon; guards 5 of 5; tip battery exit 0: 1 of 6`, **exit=1**.
Guards all PASS (no-deletions, floors, instrument-size 22 added/3 deleted vs cap 40,
instrument-pin, spotcheck-identity). Gate exits: registry 1 (0.4s), floors 1 (106.9s),
checklist 1 (1.4s), integrity 1 (0.2s), independent 1 (0.5s), correction sweep 0 (0.0s).

Cross-check against the canonical base receipt
`.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` (`--repo .` form from the lane root):
byte-identical after normalising only the cmd line, wall times and the fleet-root path
(`diff` → IDENTICAL). The `1 of 6`, the guard tally and every per-gate exit agree.
**The base battery figure `1 of 6` is independently confirmed.** Differences are only
cosmetic: wall 110.0s vs 103.9s (host load), and the fleet-root line names my
fleet-shaped scratch dir instead of `/home/vgpnk/Projects/shokunin` (the scratch fleet
symlinks resolve to the same real entries, so resolution behaviour is unchanged).

## 2. The six battery gates, re-run individually (from inside the clone)

| Gate (battery argv) | Plan expectation | This re-derivation | Verdict |
|---|---|---|---|
| `check_gate_registry.py --rev 398cbe1…` | `60 of 62`, exit 1 | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1. The two red rows: `check_desc_craft.py` and `check_r75_routed_repairs.py` ("no registry rows naming it: 0 (need 1)") — exactly the two the plan names. | MATCH |
| `check_assertion_floors.py` | exit 1, `FAIL checklist observed=1863 floor=1863 self_test_failures=1` | Identical FAIL line, all other 15 rows PASS, exit 1. | MATCH |
| `verify_skill_checklist.py` | exit 1, `FAIL governance.citation_resolves: LOG.md:2818 '.ufo/reports/round-76/kotoba.md' does not resolve` | From a dir named `kotoba-shokunin`: exactly that single FAIL, exit 1. From a dir named `clone`, one extra artifact FAIL `trigger.name_directory` (`name 'kotoba-shokunin' != directory 'clone'`) — a scratch-shape artifact only; the canonical battery sandbox names the dir `kotoba-shokunin`. | MATCH (with caveat noted) |
| `verify_corpus_integrity.py` | 6 DRIFTs, exit 1 | 6 DRIFTs, exit 1 — `tracked_files` 152≠144, `unindexed` 1, `report_total` 109≠99, `report_dead` 1, `commit_total` 46≠43, `commit_unresolvable` 2. `3/9 checks pass`. | MATCH |
| `verify_corpus_independent.py` | `unindexed=1`, `commit_unresolvable=2`, exit 1 | Identical counts, exit 1. | MATCH |
| `check_correction_sweep.py --root .` | exit 0 | `correction sweep: 0 stale block(s)`, exit 0. | MATCH |

## 3. The two corpus gates' --json site lists (the independent confirmation target)

**`unindexed` = 1 — CONFIRMED.** Both gates:
`corpus/lessons/round-79-verifier-spotcheck.md` ✓ (matches plan).

**`report_dead` = 1 — CONFIRMED for the integrity gate; known extractor disagreement for the independent gate.**
- integrity `report_dead_detail`: `corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md` ✓ (matches plan; that path does not exist in the base tree — `.ufo/reports/` tops out at round-45 — and the file is spotcheck-identity-pinned, uneditable).
- independent `report_dead` = 0 for the same corpus: its extractor strips the `HEAD:` object-expression prefix and falls back to the hardcoded fleet root for bare `.ufo/reports/…` paths (`report_pointer_exists`, verifier lines 265–270; fleet root doc lines 21–23), and `/home/vgpnk/Projects/shokunin/.ufo/reports/round-77/kotoba.md` exists on the fleet. This is precisely the r79 E04-recorded disagreement that repair 4 (`verify_corpus_integrity.py` `<rev>:` pointer fix) targets. Not new, not a defect in my run — reproduced as recorded.

**`commit_unresolvable` = 2 — COUNT CONFIRMED, SITE SET DISAGREES WITH THE PLAN. (Load-bearing finding.)**
- Measured `commit_unresolvable_detail` is **identical on both gates**:
  - `corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00`
  - `corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00`
  (one token, two census-row occurrences: S230's row incorrectly attributes the commit to `badlogic/pi-mono`; the fetched S230 record instead identifies `bb65e3e4…`. S231 is the Mistral Vibe row and its fetched record identifies `7bb48f21…`. This cross-row attribution issue is separately reported by Kb80E08C2Entry.)
- The plan (plans/round-80.md line 10, and this seat's brief) names the pair
  `451a02ff @ corpus/lessons/round-54-verifier-spotcheck.md:147` and
  `cfb894a5 @ corpus/lessons/round-54.md:13`. **Against current gate bytes those two tokens are NOT counted as unresolvable** — both gates classify both as `commit_quoted` (code-span/lesson-context exclusion; verifier doc lines 25–30: "A citation inside double quotes or a matching Markdown code span is CONTEXT, not a live commit reference", with the self-test arm encoding exactly this at lines 1019–1035). They appear only in `commit_quoted_detail`.
- The plan's Trigger-section sentence "The two commit_unresolvable tokens are `owner/repo@<hex>` citations of THIRD repositories (google-gemini/gemini-cli@451a02ff, zed-industries/zed@cfb894a5)" is therefore **stale/mis-attributed for both corpus gates**: the actually-counted token is `7bb48f21…`, appearing in SOURCES rows S230 and S231. The S230 row labels it `badlogic/pi-mono`, but Kb80E08C2Entry reports that its fetched record instead identifies S230's revision as `bb65e3e4…`; 7bb48f21 is the Mistral Vibe commit in S231. Thus the measured blocker is still a third-repository citation, but the S230 citation is cross-attributed; any seat building red-before arms off the plan's named sites would test the wrong tokens.
- Absence independently verified by me, direct object probes: `git cat-file -t` → fatal / "Not a valid object name" for `7bb48f21…`, `451a02ff`, `cfb894a5` in BOTH the lane clone and the fleet root. All three are third-repo objects by construction.
- Practical consequence (named loudly, not repaired — recon scope): the acceptance read for repairs 4+5 must be the gates' `--json` site lists at the measured rev, not the plan's named pair. After repair 5 lands, `commit_unresolvable` must read 0 on both gates because the two `SOURCES.md` census-revision tokens move to the new external-commit INFO class; `451a02ff`/`cfb894a5` stay quoted-excluded either way. Repair 3's baseline refresh must re-record against the measured post-repair sites, not the plan's pair.

## 4. Secondary observations (non-blocking)

- Floors gate wall ~107s standalone (battery: 106.9s; canonical receipt: 101.0s) — load variance only; verdict identical.
- The battery's floors/checklist/independent/integrity exit lines in my run match the canonical receipt one-for-one (§1 diff).
- Scratch hygiene: `TMPDIR=$S/tmp` held the battery's sandbox clones; the trap-free recipe was followed per call (`-C` on every git invocation; toplevel asserted for both clones); scratch dir removed after receipts were written (see DELIVERABLES — nothing lives only in scratch).
- One live M80-1-adjacent catch during my own run (recorded for honesty): my first floors invocation used a relative script path from the wrong cwd and captured `exit=2` (python file-not-found) — the direct-exit discipline caught it as a harness error, not a gate verdict; the reran gate is the authoritative receipt (`gate2-assertion-floors.txt`).

## 5. Receipts (all under `.ufo/waves/round-80/build/Kb80R02TipRecon/`)

| file | content | sha256 |
|---|---|---|
| battery-repo-clone-rev-base.txt | full battery output, exit=1 | 72ed8604211149afd92e5dc269f1d37f33cadc2ff63f5d7fcf6b0a26f7a0c0ca |
| gate1-gate-registry.txt | registry, exit 1, `60 of 62` | 670e66de1160de7cce12e3ef9ffbc3c43a6852acbaf339468a0a8273b10e2728 |
| gate2-assertion-floors.txt | floors, exit 1, `FAIL checklist observed=1863 floor=1863 self_test_failures=1` | 9105612c9e59051416a1679e93ad127ea6a0a6512cc5f83ef42c27ebadfd745b |
| gate3-skill-checklist.txt | checklist from `clone`-named dir (incl. artifact FAIL), exit 1 | dc956897be67501f93622d8073664a6e1f59d5355107fcddb2d3fe1cba2857b4 |
| gate3-skill-checklist-canon-dir.txt | checklist from `kotoba-shokunin`-named dir, exit 1, single FAIL | 8c18d0218893a9ab5f8270a24b7102e7badba1b339dbb332821bc745bd1df554 |
| gate4-corpus-integrity.txt | integrity human output, exit 1, 6 DRIFTs | bd394573c5bbfffe81d262709cc43682cff85fd68b0a097a75ca766fedd75243 |
| gate4-corpus-integrity-json.txt | integrity `--json` site lists | e5f885437269d2f2382b0e2a1fe91e76301c546c32aa9a6c15008e7f8c7fc8ef |
| gate5-corpus-independent.txt | independent human output, exit 1 | b8974796f057561b7be9e4e4d6d4fc6566660dbc6c13c542d702a0cde9d2365a |
| gate5-corpus-independent-json.txt | independent `--json` site lists | b99b4b315ab51c666ddb9e5bf23cd85265ede3c102c18950fd02a1accc870000 |
| gate6-correction-sweep.txt | correction sweep, exit 0 | d66accd2cb957f5eb3ab49f345323502d24740840f1c9b6f1a4dbb719c1b1d8b |

VERDICT: base battery `1 of 6` (exit 1, guards 5/5) independently CONFIRMED against the canonical receipt; all six gate verdicts and the DRIFT/unindexed/report_dead site sets match the plan; the plan's named `commit_unresolvable` pair {451a02ff, cfb894a5} is DISPROVEN — both gates actually count `7bb48f21…` at `SOURCES.md:171-172`; S230 misattributes that hash (per Kb80E08C2Entry's fetch-record comparison), while S231 is the Mistral Vibe row.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80R02TipRecon.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R02TipRecon/{battery-repo-clone-rev-base,gate1-gate-registry,gate2-assertion-floors,gate3-skill-checklist,gate3-skill-checklist-canon-dir,gate4-corpus-integrity,gate4-corpus-integrity-json,gate5-corpus-independent,gate5-corpus-independent-json,gate6-correction-sweep}.txt
