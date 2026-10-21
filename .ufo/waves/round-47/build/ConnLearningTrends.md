verdict: as planned, expansion `unchanged`, quality `unchanged` (one step from `harmed`), discernment `unchanged`; one corpus write-back in C1's own evidence path can move quality to `improved` while leaving the three declared axes' verdicts untouched, and expansion stays `unchanged` unless a knowledge entry is admitted on the Loader-rule freshness frontier row.

# ConnLearningTrends — LEARNING.md trends vs round-47 planned outputs

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Predictions below are labelled; every observed fact carries its command and exit code. Scratch clone: `/fast/scratch/kotoba-r47/ConnLearningTrends/lane` (clone + `checkout --detach` exit 0, `rev-parse HEAD` = BASE). No production file was written.

## 1. The observable set the plan actually produces

`plans/round-47.md:20-37` declares three claims; none admits a `corpus/knowledge/` entry:

| claim | planned write | LEARNING.md observable it can hit |
|---|---|---|
| C1 freshness | `verifiers/verify_surfaces.py` re-derivation + `verifiers/baseline.json` re-pin (`measured_against` at `verifiers/baseline.json:5,9`), surfaces 7/7, pins 3/3 | freshness (axis), not an entry |
| C2 operability | XML-tag check in `verifiers/verify_skill_checklist.py` + fixtures; `SKILL.md` description loses `<skills>` (`SKILL.md:14`) | operability (axis) |
| C3 calibration | erratum registry in the governance citation check + one index row for `corpus/lessons/round-46-verifier-spotcheck.md`; 0 DRIFT on both corpus gates | calibration (axis) |

The plan adds one sentence, `plans/round-47.md:15-16`: “the SOURCES workflow still runs as the frontier step.” That is a source-row workflow, not a knowledge admission (`corpus/SOURCES.md:3-5`: entry admission lives in `corpus/QUALITY.md`, not in SOURCES).

## 2. Predicted verdicts

| trend | prediction | reason at BASE | flip condition |
|---|---|---|---|
| **expansion** | `unchanged` | no planned write is a `knowledge/` entry; a lesson index row is conformance, not admission. Precedent: round 46 landed `corpus/QUALITY.md`, `corpus/SOURCES.md` and `corpus/lessons/round-46.md` with index rows and still recorded “expansion unchanged (no knowledge entry)” (`corpus/lessons/round-46-verifier-spotcheck.md:17`); round 20 recorded the same (`SCORECARD.md:207`) | a net-new admitted `corpus/knowledge/` entry on uncovered (frontier) ground with a `mined` `source:` row — evidence checklist in §4 |
| **quality** | `unchanged` as planned; `harmed` if C1's re-derivation falsifies a live claim in `corpus/knowledge/instruction-surface-census-round13.md` and the entry is left unmarked | no knowledge entry is named in C1/C2/C3; the substrate facts C1 re-derives are kept in `verifiers/baseline.json:8` notes (the round-44 precedent), which are not entries with `verified-at:` (`corpus/QUALITY.md:23`, Q12). 32 of 34 knowledge entries already lack the Q12 triple (`corpus/lessons/round-46.md:34` command re-run: 32) | §5: an append-only errata + `verified-at:`/`recheck:` pair on the census entry, with the recheck run |
| **discernment** | `unchanged` | no corpus admit/reject is planned; the lane's own seats do not qualify as non-author (`/home/vgpnk/Projects/shokunin/LEARNING.md:42-46`: “A subagent the lane dispatched is still the lane”), so the 200-seat wave cannot self-spot-check | a fresh orchestrator-dispatched reviewer samples ≥1 admit **and** ≥1 reject and records `agree`/`disagree` with reasons (precedent table `corpus/lessons/round-46-verifier-spotcheck.md:8-13`) |

Do not confuse the freshness axis verdict with the quality trend. C1 can score `freshness: improved` and still leave `quality: unchanged`; `LEARNING.md:85-86` maps quality to the freshness axis, but the trend’s observable is entries (`LEARNING.md:34`), not verifier code.

## 3. Evidence each verdict will need (exact commands, at the landed tree)

### 3.1 expansion `unchanged` (what the report must be able to show)

1. `git diff --stat c61a973b..<landed> -- corpus/knowledge/` → empty. This is the whole verdict; if it is non-empty, run §4.
2. `git diff c61a973b..<landed> -- corpus/README.md` → only the C3 lesson row (column-2 token `lessons/round-46-verifier-spotcheck.md`); no `knowledge/` row added.
3. `git show <landed>:corpus/SOURCES.md | grep -E '^\| S0' | grep -c '| mined |'` → any movement is a source row, not an entry; a mined own-work row alone is not expansion.
4. `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 0 is conformance/calibration, not expansion (proved by the round-46 counterexample above).

Measured at BASE (scratch clone):
- `python3 -B verifiers/verify_corpus_integrity.py` → exit 1, `7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed`; unindexed detail `corpus/lessons/round-46-verifier-spotcheck.md`.
- `python3 -B verifiers/verify_corpus_independent.py --json` → exit 1, `unindexed: 1`, same detail, `tracked_files: 59`.

### 3.2 quality `unchanged` vs `improved` vs `harmed`

C1 cannot be verifier-only when a class moves. `surfaces.table_parity` requires the class-id set in `corpus/knowledge/instruction-surface-census-round13.md` `## Class inventory` (`:64`) to **exactly equal** the baseline set, both directions (`verifiers/verify_surfaces.py:76-80`), and `verifiers/surfaces-baseline.json:2` declares the baseline “DERIVED from the class inventory tables” of that entry. So:

- If C1 adds, removes or re-verdicts a class, the census entry is edited in the same change or `table_parity` FAILs (`inventory id absent from the baseline -> "extra row"` / `baseline id with no inventory row -> "missing row"`).
- Evidence for `improved`: `git diff c61a973b..<landed> -- corpus/knowledge/instruction-surface-census-round13.md` shows an **append-only** errata block naming the 18.12.5/1.19.3 shas and the re-derived callee/anchor set, plus a head `verified-at: 2026-10-21` and a `recheck:` that runs. `corpus/QUALITY.md:15` (Q04) requires the recheck to run today; `:23` (Q12) requires the triple.
- Evidence for `harmed` (the live claim C1 will test): `corpus/knowledge/instruction-surface-census-round13.md:12-13` says “§ A stays live — the same `.md` registration shapes persist under renamed callees (`Id|Cl|jD[ef]` → `Tl|dr|GW`, allowlist re-pinned in the verifier)”. At 18.12.5 the measured state is **0 of 8 omp loader classes extracted** while 33 declared literals are present (`surfaces.no_uncovered_class` detail). That is consistent with “renamed again” but not proof of it. If C1 classifies the change as anything other than a rename and leaves line 13 standing, `LEARNING.md:34`’s harm condition (“an entry is found false or stale and left unmarked”) is met.
- Examined and **not** harm: `corpus/knowledge/instruction-surface-census-round13.md:272` records “`--self-test` 75 assertions” (current floor 87, `verifiers/floors-registry.json:37-39`) inside a Before/After table, and `corpus/knowledge/substrate-pin-guard-round23.md:30-34` records a landing battery (“live: … OK 3/3 pins hold”). Both are dated records under the round-24 convention (present-tense sites corrected, dated records kept); neither is a live claim this round falsifies.

Measured at BASE: `python3 -B verifiers/verify_surfaces.py --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --json` → exit 1, `4 PASS / 3 FAIL`; FAILs `surfaces.literal_present`, `surfaces.no_uncovered_class` (“vacuity: 0 loader class(es) extracted … baseline declares 8”), `surfaces.opencode_extract` (“produced by no rule: opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md; OC-1/OC-4/OC-6 matched nothing”). Default resolution: `python3 -B verifiers/verify_surfaces.py --json` → exit 2, `opencode binary not found: /home/vgpnk/.opencode/bin/opencode` (`verifiers/verify_surfaces.py:130`). Pins: `python3 -B verifiers/check_substrate_pins.py` → exit 2, `DRIFT 3/3 pins failed` (omp sha expect `9513ef9f…` got `fdbc8136…`; mtime delta `140082506863270 ns`; opencode path unreadable, default at `verifiers/check_substrate_pins.py:63`).

### 3.3 discernment `unchanged`

Evidence required to keep the verdict honest:
1. `corpus/lessons/round-47.md` § Gate lists candidates considered/admitted/rejected with reasons, or states “none admitted / no candidate opened” (round-46 precedent `corpus/lessons/round-46.md:49-55`).
2. If any admit/reject exists, a non-author table of the `corpus/lessons/round-46-verifier-spotcheck.md:8-13` shape with ≥1 admit and ≥1 reject, `agree`/`disagree` + reason, and an identity that is neither the lane nor a seat the lane dispatched (`LEARNING.md:42-46`). This seat is lane-dispatched and cannot supply it.
3. If `corpus/QUALITY.md` gains a row, `git diff` must show its `grounded in` cell naming a `## Mistakes` row id in `corpus/lessons/round-47.md`; an ungrounded row is `harmed` (`LEARNING.md:35`).

The C3 erratum registry is a gate rule, not a `QUALITY.md` criterion; it does not move discernment by itself. If the integrator wants it read as a criterion, it needs a lesson row first (see §7 risk 3).

## 4. The expansion boundary — `improved` vs `unchanged`

`LEARNING.md:33` has two cells that can disagree, and the round must score against the stricter one:

- Observable: “admitted `knowledge/` entries on ground the coverage map did not hold, each `source:` citing a `mined` `corpus/SOURCES.md` row (`own-work` rows included); **frontier areas entered; new kinds of source; a capability admitted to `SCORECARD.md`**”.
- `improved when`: “**net new admitted entries on uncovered ground, each citing its coverage-map row**”.

There is no recorded BASE precedent where a capability row alone flipped expansion: the only recorded trend blocks key it to knowledge admission (`corpus/lessons/round-46-verifier-spotcheck.md:17`, `SCORECARD.md:207`), and round 46 landed a corpus conformance set without credit (“Corpus conformance landed without credit”). Recommendation: score against the `improved when` cell; treat the observable list as admissible *only* when it names an admitted entry.

Decision procedure that makes expansion `improved` (all seven must hold):

1. **A new file** under `corpus/knowledge/` — not an edit, not a lesson, not a README row, not a `verifiers/baseline.json` note.
2. `source:` names an S### row plus URL/anchor; that row’s status in `corpus/SOURCES.md` is `mined` (Q12, `corpus/QUALITY.md:23`).
3. `verified-at:` and a `recheck:` that runs exit 0 today (Q04, `corpus/QUALITY.md:15`).
4. A **net-new row** in `corpus/README.md` § Coverage map (`:7-63`) whose Area is absent from `git show c61a973b:corpus/README.md` — an added row is what “citing its coverage-map row” means.
5. The Area is a Frontier row at BASE, not a held one: the round touches exactly one, `Loader-rule freshness` (`corpus/README.md:74`; `PROVINCE.md:21`). Other Frontier rows (`corpus/README.md:70-75`) are not in this round’s scope.
6. The entry carries claims the BASE map did not hold — the 18.12.5 callee set, the 1.19.3 opencode anchor set, the `description` XML-tag validity rule — **not** a restatement of the round-13 class inventory. A new version of held ground is quality, not expansion.
7. `LOG.md` records the frontier→core move (`LEARNING.md:78-79`: “Moving frontier ground into core is ordinary growth, recorded in `LOG.md`”), and the corpus gate is green with `tracked_files` re-recorded (59→60).

If step 1 is absent, the verdict is `unchanged` no matter how many gates turn green. That is the counterexample round 46 already paid for.

## 5. The measured trap in C3 (index row is not enough for 0 DRIFT)

The plan (`plans/round-47.md:34-37`) predicts “0 DRIFT”. At BASE the primary gate has **two** reds: `corpus.index.unindexed` (fixed by the row) and `corpus.index.tracked_files`, an `equal` check pinned at 58 (`verifiers/corpus-baseline.json:13`) against observed 59. I simulated both halves in the scratch clone:

- add the index row only → `8/9 checks pass; DRIFT: corpus.index.tracked_files`, exit 1;
- then set `checks.corpus.index.tracked_files.expect = 59` → `9/9 checks pass`, exit 0; `verify_corpus_independent.py` exit 0.

So C3’s evidence must include the baseline re-record with a note of the established form (“Expectation refresh, not a fitted denominator”, `verifiers/corpus-baseline.json:51`), or the “0 DRIFT” claim is false at landing.

## 6. Other counterexamples and contradictions at BASE

1. **Two planned C3s disagree.** `SCORECARD.md:36` still carries the pre-re-target plan: “C3 — capability (sources curation with outside re-open) … a knowledge entry admitted under `corpus/QUALITY.md` Q12 citing a `mined` row”. `plans/round-47.md:14-16` says that C3 “is replaced by a calibration claim”. The plan file is canonical, but the SCORECARD row is a record-vs-plan divergence the round inherits (Q03 class). Calibration evidence must reconcile it, not launder it.
2. **C1’s re-derivation record has no corpus home.** Round 44 stored its substrate facts in `verifiers/baseline.json:8` (`omp_round44_note`) and `verifiers/surfaces-baseline.json:3`. If round 47 repeats that pattern, the re-derivation is invisible to the quality trend even though the work was done.
3. **The census entry is the gate’s inventory, not documentation.** `verify_surfaces.py --inventory` defaults to `corpus/knowledge/instruction-surface-census-round13.md` (help text, `--inventory` default). A verifier-only re-verdict either fails `table_parity` or forces the corpus edit; the plan does not name it.
4. **C2 leaves a stale promise.** `SKILL.md:151` says “This file’s own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47).” Removing the token (`SKILL.md:14`) without updating line 151 leaves a false present-tense record — calibration drift caused by C2, which C3 is supposed to prevent.
5. **The Frontier rows are stale at BASE and will be wrong in the opposite direction after landing.** `PROVINCE.md:21` and `corpus/README.md:74` both say “omp 18.12.3 … surfaces 5/7, pins 1/3”. At BASE it is 18.12.5 with surfaces 4/7 (frozen dumps) and pins 3/3 failing; after C1 it is 7/7 and 3/3. A landed tree where the gate is green and the Frontier row still claims drift is a calibration defect inside C3’s own claim (“records match repo state”).
6. **The quality baseline is thin.** 32 of 34 knowledge entries lack `source:`+`verified-at:`+`recheck:` (M16, `corpus/lessons/round-46.md:34`; re-run at BASE → 32). Any single entry re-verified this round is a visible improvement precisely because the field is near-empty; a bare table edit without the triple moves nothing on the trend.

## 7. Proposed move (one, bounded)

**Write the re-derivation back where the gate reads it.** Fold C1’s re-derived 18.12.5/1.19.3 facts (callee allowlist, opencode anchors, class re-verdicts with their sweeps) into `corpus/knowledge/instruction-surface-census-round13.md` as an append-only round-47 errata block, add the Q12 head triple (`source:` citing a `mined` own-work row from the round’s SOURCES workflow + S003 where the tag rule is the claim, `verified-at: 2026-10-21`, `recheck:` = `python3 -B verifiers/verify_surfaces.py --json` and `python3 -B verifiers/check_substrate_pins.py`), and update the two Frontier rows (`PROVINCE.md:21`, `corpus/README.md:74`) to the post-landing state.

Why this is the non-obvious move: the plan treats C1 as verifier work, but `surfaces-baseline.json` declares itself *derived from* that entry and `table_parity` makes the derivation bidirectional. The write-back is therefore already forced whenever a class moves — the only choice is whether it is recorded as a re-verification or as a silent table edit. Recording it converts `quality: unchanged` into `quality: improved` (stale entry re-verifies with a running recheck, `LEARNING.md:34`) and removes the `harmed` risk on line 13, without adding a claim, a seat, or a new axis. It also strengthens C3’s calibration evidence by fixing the two Frontier rows the round discharges — they currently contradict the landed state.

Decision rule: if the re-derivation finds a class/rule the BASE coverage map did not hold, admit it as a **separate net-new entry** with its own coverage-map row and claim expansion under §4; otherwise do not claim expansion. One move, two possible verdicts, decided by evidence.

Risks:
- **Table edit vs errata.** Touching `## Class inventory` rows changes the class set the gate compares; any row change must move `verifiers/surfaces-baseline.json` in the same change or `table_parity` fails. Append the errata above the inventory, do not rewrite historical sections (the lane’s append-only convention).
- **Ephemeral recheck.** A `recheck:` citing `/fast/scratch/kotoba-r47/shared/...` or the npx cache dies by the next round (Q04). Point it at the default-resolution verifier commands, which C1 is already fixing.
- **Ungrounded criterion.** If the erratum registry is presented as a new bar rather than a gate mechanism, add a `## Mistakes` row in `corpus/lessons/round-47.md` and cite it (see §3.3); otherwise leave `corpus/QUALITY.md` untouched.
- **Self-attested quality.** The write-back is lane-authored. It can support `quality: improved` (an entry re-verified), but it cannot support discernment — that still needs the outside spot-check.

Verification of the move: `git diff` on the entry shows an append-only block (no deleted lines); the head has the Q12 triple; both verifier commands exit 0 at the default resolution; `python3 -B verifiers/verify_surfaces.py --json` reports `surfaces.table_parity` PASS; `python3 -B verifiers/verify_corpus_integrity.py --json` exit 0 (no new tracked file, so no baseline bump for this move); the Frontier rows no longer contain `18.12.3` or `5/7`.

## 8. What I did NOT check

- The landed round-47 tree does not exist; every verdict above is a prediction against the plan text.
- I did not run `verifiers/verify_skill_checklist.py` in the lane path (contract restricts lane-wide gates). Its per-check statuses here are the before-summary values (9 PASS / 1 FAIL `governance.citation_resolves` at `LOG.md:2111`). A run in my scratch clone produced three FAILs that are **clone artifacts**, not lane defects: `trigger.name_directory` compares the skill name to the directory (`lane` ≠ `kotoba-shokunin`), and `trigger.citation_resolves`/`governance.citation_resolves` resolve `../.ufo/...` against the clone’s parent, which has no `.ufo`. Disclosed, not used as evidence.
- I did not classify whether the 18.12.5 omp change is a callee rename or a loader-shape change; that is C1’s job and is the pivot of the quality verdict (§3.2).
- I did not read the live npx wrapper or execute it (contract forbids); the 1.19.3 facts come from the frozen snapshot dumps.
- I did not verify the erratum registry design (no implementation exists at BASE) nor whether a line-number-keyed registry can survive LOG.md appends; a line+token+line-hash pin is the fail-closed shape to test.
- I did not examine fleet-level `LEARNING.md` implementations outside this lane, nor any sibling lane’s corpus.

## 9. Commands run (exit codes, key output)

All in `/fast/scratch/kotoba-r47/ConnLearningTrends/lane` unless noted.

| command | exit | key output |
|---|---|---|
| `git clone -q --no-hardlinks … && git checkout --detach c61a973b…` | 0 | `rev-parse HEAD` = `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `python3 -B verifiers/verify_corpus_integrity.py` | 1 | `7/9 checks pass; DRIFT: corpus.index.tracked_files (59 vs 58), corpus.index.unindexed (1: corpus/lessons/round-46-verifier-spotcheck.md)` |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | `unindexed: 1`, `tracked_files: 59`, same detail |
| `python3 -B verifiers/verify_surfaces.py --omp-strings …/omp-18.12.5.strings --opencode-strings …/opencode-1.19.3.strings --json` | 1 | 4 PASS / 3 FAIL (`literal_present`, `no_uncovered_class` 0/8, `opencode_extract` OC-1/OC-4/OC-6) |
| `python3 -B verifiers/verify_surfaces.py --json` (default) | 2 | `opencode binary not found: /home/vgpnk/.opencode/bin/opencode` |
| `python3 -B verifiers/check_substrate_pins.py` | 2 | `DRIFT 3/3 pins failed`; omp sha expect `9513ef9f…` got `fdbc8136…`; mtime delta `140082506863270 ns` |
| index-row simulation (scratch edit) | 1 | `8/9 checks pass; DRIFT: corpus.index.tracked_files` |
| + `corpus-baseline.json` expect 58→59 (scratch edit) | 0 | `9/9 checks pass`; independent `exit 0` |
| `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` (lane, read-only) | 0 | `1`; token on `SKILL.md:14`; no tag check in the instrument (`grep -c -i 'xml tag\|xml-tag\|<skills>' verifiers/verify_skill_checklist.py` → `0`) |
| M16 rebuild command (`source`+`verified-at`+`recheck` sweep) | 0 | `32` unprovenanced of `34` knowledge entries |
| `grep -n 'omp_binary_sha256\|opencode_binary_sha256' verifiers/baseline.json` | 0 | `:5` omp `9513ef9f…`, `:9` opencode `d9123b9b…` — both stale vs 18.12.5/1.19.3 |
