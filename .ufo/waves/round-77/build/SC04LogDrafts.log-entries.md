# LOG.md entries — round 77 draft (seat SC04LogDrafts)

Status: **draft, not applied.** The L1 (`KotobaR77`) appends after freeze/integration; this file holds the
exact paste text plus every `[[SLOT: …]]` the integrator fills from committed bytes. Nothing below asserts a
measurement that has not been run: the two after-values, the tip hashes and the tip receipt paths are slots.

Authoring revision: lane `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (round-77 freeze). `git status
--porcelain` there shows only untracked round-77 wave bookkeeping
(`.ufo/waves/round-77/{w1-dispatch.json,w1-spec.json,w1.ready,w1.ready.dispatched,w1/}`); no tracked file
was modified by this seat.

Placement (append-only, no filed byte rewritten):

1. Paste text 1 goes **after `LOG.md:2818`**, the last line of `## Round 76 — honest stop (claims unlanded)`
   (file tail measured: `…fleet report \`.ufo/reports/round-76/kotoba.md\`.\n`, 2,818 lines, single trailing
   newline). One blank line before the heading.
2. Paste text 2 goes after paste text 1, same rule. The two are chronological and must stay in this order:
   `## Round 76 — honest stop` → `## Round 76 — completion note (written in round 77)` → `## Round 77`.

Fill rules (each is counter-visible; violating one makes the entry a false claim):

- **R-a — slots only from committed receipts.** A slot is filled from a receipt or a `git` reading, never
  from memory or from a sibling draft. A filled path must satisfy `git cat-file -e <measured-tip>:<path>`.
- **R-b — a red predicate deletes the clause.** If `check_desc_craft.py` does not print
  `description craft backed 6 of 6` / exit 0 at the measured tip, or `check_r75_routed_repairs.py` does not
  print `r75 routed repairs closed 4 of 4` / exit 0, delete that clause and write the **observed** line and
  exit code instead. Do not paste the target as if measured.
- **R-c — no pipeline exit codes.** Every receipt cited by these entries captures the gate's own status
  (`cmd > out 2>&1; echo "exit=$?" >> out`), never `… | tail` followed by `$?` (the r76 defect
  `plans/round-76-addendum-2.md` § 1 corrects).
- **R-d — strip the fences, nothing else.** The two fenced blocks are the exact bytes to append; copy from
  the line after the opening fence to the line before the closing fence, with no prefix to remove.

Slot marker form: `[[SLOT: <id> — <what to fill>]]`. The id table is at the end of this file; the fill-check
is at § Fill-check.

---

## Paste text 1 — `## Round 76` completion note (append after `LOG.md:2818`)

```markdown
## Round 76 — completion note (written in round 77, 2026-10-27)

- **What the honest stop left (measured at the round-77 freeze `6523aced1ee0ebe07dca996213bdc645a6acbd1e`):**
  both frozen counters and their self-tests landed; nothing of either claim did. No r76 commit touches the
  corpus or the skill surface — `git diff --name-only b7f13f4 6ce2724 -- SKILL.md corpus/ | wc -l` → `0`
  (the 119-file r76 diff is `.ufo/` 103, `plans/` 7, `verifiers/` 6, `LOG.md`, `SCORECARD.md` and the stray
  `kotoba-shokukin/` path of R76-D1) — so absent at that tip are
  `corpus/knowledge/description-craft-round76.md`, `corpus/lessons/round-76.md`, the S213 `used-by` append,
  the `SKILL.md` § Body craft rule row, the appended r75 correction, both C2 receipts
  (`.ufo/waves/round-76/receipts/r1-folded-render.txt`, `.ufo/waves/round-76/receipts/noharm-at-tip.txt`),
  the landing-path note `.ufo/waves/round-76/w2-registry-note.md` (only the `build/` draft exists) and the
  § Round 75 closing append. The base readings are unchanged at the round-77 base and committed:
  `description craft backed 0 of 6`, exit 1
  (`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`; the r76 base receipt
  `.ufo/waves/round-76/receipts/c1-base-final.txt` records the same verdict) and
  `r75 routed repairs closed 0 of 4`, exit 1
  (`.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`; likewise
  `.ufo/waves/round-76/receipts/c2-base-final.txt`). Both corpus gates were already red at the r76 base
  (`.ufo/waves/round-76/base-battery/base-gate-correction.txt`) and are still red at the round-77 freeze
  ([[SLOT: base-battery — the round-77 base-battery receipt carrying both gates' own exit codes]]).
  The only r76 control receipt, `.ufo/waves/round-76/receipts/c1-controls.txt`, was scored on counter blob
  `87837d7a…`, not the frozen `cf3c45d9…`, so it controls neither frozen instrument; the round-77 controls
  are re-scored on the frozen bytes before any data commit ([[SLOT: controls-receipt — path of the round-77
  control receipt scored on cf3c45d9… / 989203c4…, its per-world exit codes, and the commit carrying it]]).
- **Wave accounting (R76-D5, the 52-vs-64 reconciliation):** round 76 registered 64 seats in one wave and no
  falsify wave ran (`ls .ufo/waves/round-76/` holds `w1*` and no `w2*`). `.ufo/waves/round-76/w1-results.json`
  carries 64 results with 64 unique names, 0 empty outputs, and **no `report` field on any entry**;
  `.ufo/waves/round-76/w1/` holds 52 `.md` reports, so 12 seats have a result and no report file:
  A03RevCounterDesc, A04RevCounterRepairs, A07RevNoHarm, A08RevFreeze, A10MutRepairs, A12MutArms,
  A23ScoutSources, A31RevD4, A36ScoutReceiptGreen, B06DescCounter, B07RepairCounter, B28EvidencePackager.
  The r76 entry recorded no dead-seat count; this paragraph is the reconciliation, computed from those two
  committed files. Round 77 states its own count ([[SLOT: dead-seats — round-77 w1 seats, results,
  report files and dead-seat count from the committed results file and `.ufo/waves/round-77/w1/`]]).
- **What round 77 re-landed:** C1, measured at [[SLOT: c1-rev — the revision the C1 counter was run at]],
  `python3 -B verifiers/check_desc_craft.py --rev <rev>` → `description craft backed 6 of 6`, exit 0
  (receipt [[SLOT: c1-receipt — path of the C1 after-value receipt]]), reading the entry
  `corpus/knowledge/description-craft-round76.md` ([[SLOT: c1-entry-commit — commit that adds the entry]]),
  the `SKILL.md` § Body craft row and the S213 `used-by` append ([[SLOT: c1-row-commit — commit that adds
  the rule row and the used-by cell]]), and `corpus/lessons/round-76.md` ([[SLOT: lesson76-commit — commit
  that adds the round-76 lesson]]) whose `## Gate` carries the S213 access record the counter reads. C2,
  measured at [[SLOT: c2-rev — the revision the C2 counter was run at]],
  `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev> --work <scratch>` →
  `r75 routed repairs closed 4 of 4`, exit 0 (receipt [[SLOT: c2-receipt — path of the C2 after-value
  receipt]]), from the R1 correction and its receipt ([[SLOT: r1-receipt — path and first-line revision of
  the folded-render receipt, clip 1022 / stripped 1021 at `ac9f295…`]]), the R2 receipt re-running both
  corpus gates at `ac9f29510d3914a6edb97c8dbdb3445cab9141de` ([[SLOT: noharm-receipt — path and commit of
  the r75-tip no-harm receipt]]), the R3 note ([[SLOT: w2note — path and commit of the landed wave-2
  registry note]]) and the R4 append to § Round 75 ([[SLOT: r4-append — commit carrying the § Round 75
  closing append]]). The no-harm battery at the measured tip is [[SLOT: noharm-battery — receipt path and
  the gate's own exit codes; both corpus gates exit 0 there]].
- **Pointer:** `plans/round-76.md`, `plans/round-76-addendum-1.md`–`-6.md`,
  `corpus/lessons/round-76-verifier-spotcheck.md`, `.ufo/waves/round-76/` (`base-battery/`, `receipts/`,
  `snapshots/`, `w1/`, `build/`), `corpus/lessons/round-76.md` [[SLOT: lesson76-commit — commit that adds
  the round-76 lesson]], `.ufo/waves/round-77/receipts/`, fleet report `.ufo/reports/round-76/kotoba.md`.
```

---

## Paste text 2 — `## Round 77` entry (append after paste text 1)

```markdown
## Round 77 — C1 depth (sourced: S213 description-craft guidance admitted and turned on this lane's own description) and C2 consistency (calibration sub-axis: r75 routed defects R1–R4 closed)

- **Trigger:** the round-77 steer (hyaku run 10, attempt 1) at base `2f675548eaad2a037a899d39247c1fd7a88aaf48`
  (the r76 closure tip), re-landing the two claims round 76 froze and did not land. The routed evidence is the
  r76 non-author closure `corpus/lessons/round-76-verifier-spotcheck.md`: § 2 re-measures C1 and C2 as
  **unchanged** with both claims unlanded and no axis harmed, § 1 records the conformance defects CD1 (stray
  `kotoba-shokukin/` path committed) and CD2 (`corpus/lessons/round-76.md` promised and absent) and CD4 (52
  report files for 64 seats, no dead-seat count), and § 5 routes R76-D1–R76-D5; **R76-D3 is this round's
  C1+C2**, and R76-D1, R76-D2, R76-D4, R76-D5 are the disclosed hygiene work below. C1's own motivation is
  `considerthese/2026-10-26.md:17` proposal 3 (land the description page round 74 rejected, then audit
  kotoba's own frontmatter; fourth raise), mined at the r74 guide-advice precedent
  `corpus/knowledge/spec-skill-creation-craft-round74.md`; C2's is `corpus/lessons/round-75-verifier-spotcheck.md`
  § 6 R1–R4 (lines 77–80).
- **Action:** plan `plans/round-77.md` at the freeze commit `6523aced1ee0ebe07dca996213bdc645a6acbd1e`, which
  also carries the four base receipts
  `.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`,
  `.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`,
  `.ufo/waves/round-77/receipts/selftests-base.txt` and `.ufo/waves/round-77/receipts/census-before.txt`.
  The counters are **not edited**: at that
  commit `sha256(verifiers/check_desc_craft.py)` = `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`
  and `sha256(verifiers/check_r75_routed_repairs.py)` = `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`,
  as pinned in the plan. Counters freeze before data: the control worlds are re-scored on the frozen bytes
  before any claim commit ([[SLOT: controls-receipt — path of the round-77 control receipt]], because the r76
  control receipt was scored on `87837d7a…`); nothing of either claim lands before that freeze. One v1
  build+falsify wave `kotoba-r77-w1`, 40 seats, role census executor 12, scout 7, scribe 6, reviewer 5,
  critic 4, mutation-tester 3, sentinel 1, simplifier 1, connector 1 (attack roles 14 of 40, 35 %); the L1
  holds the canonical planner seat and carries no labrat/sonic seat ([[SLOT: wave-commit — commit that
  carries `.ufo/waves/round-77/w1-dispatch.json`, `w1-spec.json`, `w1-results.json`, `w1/` and
  `swarm-registry.json`]]). Build seats drafted under `.ufo/waves/round-77/build/`; the L1 integrates.
- **Outcome:** C1 — base `2f675548` → `description craft backed 0 of 6`, exit 1
  (`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`); after
  [[SLOT: c1-rev — the revision the C1 counter was run at]] →
  `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed 6 of 6`, exit 0
  (receipt [[SLOT: c1-receipt — path of the C1 after-value receipt]]). The six conjuncts are
  `plans/round-76.md` § C1 as corrected by `plans/round-76-addendum-1.md` (digest pinned in snapshots
  `MANIFEST.sha256`, `fetch-record.json`, the counter's digest table and the lesson `## Gate`, not in the
  S213 `anchor`), with measurement conventions per addenda 1 and 4; S213
  (`https://agentskills.io/skill-creation/optimizing-descriptions.md`) is re-opened in this round and every
  recorded digest must equal `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`
  ([[SLOT: s213-digest-check — the two independent re-opens' URL, access date, ≤25-word located quote and
  byte sha256]]). C2 — base `2f675548` → `r75 routed repairs closed 0 of 4`, exit 1
  (`.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`); after
  [[SLOT: c2-rev — the revision the C2 counter was run at]] →
  `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev> --work <scratch>` prints
  `r75 routed repairs closed 4 of 4`, exit 0 (receipt [[SLOT: c2-receipt — path of the C2 after-value
  receipt]]), R1–R4 as `plans/round-76.md` § C2 with `plans/round-76-addendum-5.md` (R2 measures the r75
  final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de`). No-harm battery at the measured tip:
  [[SLOT: noharm-battery — receipt path and each gate's own exit code]]; `SKILL.md` is
  [[SLOT: skill-lines — line count at the measured tip]] lines against the 600-line budget; census
  [[SLOT: census-after — exit code and row count]]
  (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`).
- **Disclosed hygiene (outside both counters, not claimed as axis moves):** R76-D1, the stray
  `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` (still present at the freeze and byte-identical
  to the correct copy: both sha256 `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb`, `cmp`
  exit 0) is removed in [[SLOT: d1-commit — commit that deletes the stray path]]. R76-D2,
  `corpus/lessons/round-76.md` with `## Gate` and `## Mistakes` lands in
  [[SLOT: lesson76-commit — commit that adds the round-76 lesson]] (also read by C1 conjuncts (a) and (e)).
  R76-D4, the two corpus gates are red at the freeze and both exit 1 there: neither spot-check lesson has a
  `corpus/README.md` row (`grep -cE 'round-7[56]-verifier-spotcheck' corpus/README.md` → `0`, while the
  round-46/47 spot-checks each carry one), and `verifiers/corpus-baseline.json` still carries the pre-drift
  counts ([[SLOT: base-battery — the round-77 base-battery receipt carrying both gates' own exit codes and
  the observed vs baseline counts]]). They are repaired (index rows plus a re-recorded
  `verifiers/corpus-baseline.json`) in [[SLOT: d4-commit — commit carrying the README index rows and the
  re-recorded corpus baseline]].
  R76-D5, the dead-seat count is stated per wave: round-76 w1 [[SLOT: r76-dead-seats — 64 seats, 64 results,
  52 report files, 12 seats without a report file]], round-77 w1 [[SLOT: dead-seats — round-77 w1 seats,
  results, report files and dead-seat count]].
- **Pointer:** `plans/round-77.md`, `plans/round-76.md` and `plans/round-76-addendum-1.md`–`-6.md`,
  `corpus/lessons/round-76-verifier-spotcheck.md`, `corpus/lessons/round-75-verifier-spotcheck.md`,
  `corpus/lessons/round-76.md` [[SLOT: lesson76-commit — commit that adds the round-76 lesson]],
  `.ufo/waves/round-77/` (`receipts/`, `build/`, `w1/`; [[SLOT: wave-commit — the commit that carries the
  wave files]]), `.ufo/waves/round-76/snapshots/`, fleet report [[SLOT: fleet-report — `.ufo/reports/round-77/kotoba.md`
  commit or path once filed]].
```

---

## Slot table

| id | where | fill from | resolution check |
|---|---|---|---|
| `c1-rev` | text 1 ¶3, text 2 Outcome | the revision the C1 counter was run at (the landing tip or the data commit) | `git cat-file -e <rev>^{commit}` |
| `c1-receipt` | text 1 ¶3, text 2 Outcome | the C1 after-value receipt (recommended `.ufo/waves/round-77/receipts/c1-tip-<rev>.txt`, mirroring the base name `c1-base-<rev>.txt`) | `git cat-file -e <tip>:<path>`; last two lines are the verdict line and `exit=0` |
| `c2-rev` | text 1 ¶3, text 2 Outcome | the revision the C2 counter was run at | `git cat-file -e <rev>^{commit}` |
| `c2-receipt` | text 1 ¶3, text 2 Outcome | the C2 after-value receipt (recommended `.ufo/waves/round-77/receipts/c2-tip-<rev>.txt`) | as above |
| `c1-entry-commit` | text 1 ¶3 | commit that adds `corpus/knowledge/description-craft-round76.md` | `git cat-file -e <c>:corpus/knowledge/description-craft-round76.md` |
| `c1-row-commit` | text 1 ¶3 | commit that adds the `SKILL.md` § Body craft row and the S213 `used-by` append | `git show <c>:SKILL.md \| grep -c 'description-craft-round76'` ≥ 1; `git show <c>:corpus/SOURCES.md \| sed -n '153p'` |
| `lesson76-commit` | text 1 ¶3/¶4, text 2 hygiene/pointer | commit that adds `corpus/lessons/round-76.md` | `git cat-file -e <c>:corpus/lessons/round-76.md`; file has one `## Gate` and one `## Mistakes` |
| `r1-receipt` | text 1 ¶3 | `.ufo/waves/round-76/receipts/r1-folded-render.txt` (counter constant `R1_RECEIPT`), its first-line revision and the clip/stripped pair | `git cat-file -e <tip>:<path>`; the counter recomputes 1022 at `ac9f295…` |
| `noharm-receipt` | text 1 ¶3 | `.ufo/waves/round-76/receipts/noharm-at-tip.txt` (counter constant `NOHARM_RECEIPT`); first line names `ac9f295…`, both gate transcripts and `exit 0` | the counter re-runs both gates at `ac9f295…` and compares normalized stdout |
| `w2note` | text 1 ¶3 | `.ufo/waves/round-76/w2-registry-note.md` (counter constant `W2_NOTE`); landing path, not `build/` | `git cat-file -e <tip>:<path>` |
| `r4-append` | text 1 ¶3 | commit carrying the § Round 75 closing append | `git show <c>:LOG.md` has the settlement line after `w2 falsify results pending` |
| `controls-receipt` | text 1 ¶1, text 2 Action | round-77 control scores on the frozen blobs (`cf3c45d9…`, `989203c4…`), committed before data | each control's own exit code in the receipt |
| `base-battery` | text 1 ¶1, text 2 hygiene | the round-77 base no-harm battery receipt (both corpus gates, registry, floors, checklist, census, `SKILL.md` budget), each command with its own exit code | both corpus gates' exit codes and the index/baseline numbers are printed there |
| `noharm-battery` | text 1 ¶3, text 2 Outcome | the tip no-harm receipt (verify corpus ×2, gate registry, floors, tip battery, checklist, skill-evals v2, census, `SKILL.md` budget) | every entry carries the gate's own exit code, no `\| tail` |
| `s213-digest-check` | text 2 Outcome | the two independent S213 re-opens (URL, access date, ≤25-word located quote, sha256) | digest equals `7cc54fbb…bd837`; a different digest stops C1 |
| `skill-lines` | text 2 Outcome | `git show <tip>:SKILL.md \| wc -l` | ≤ 600 |
| `census-after` | text 2 Outcome | round-end census receipt | exit 0 |
| `d1-commit` | text 2 hygiene | commit deleting `kotoba-shokukin/…/A18ScoutSnapshot.md` | `git cat-file -e <c>:kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` fails |
| `d4-commit` | text 2 hygiene | commit with `corpus/README.md` index rows and `verifiers/corpus-baseline.json` | both corpus gates exit 0 at `<tip>` |
| `r76-dead-seats`, `dead-seats` | text 1 ¶2, text 2 hygiene | the two results files plus their wave dirs | seat count minus `.md` files with matching stems |
| `wave-commit` | text 2 Action/Pointer | commit carrying `.ufo/waves/round-77/{w1-dispatch.json,w1-spec.json,w1-results.json,w1/,…}` | `git ls-files .ufo/waves/round-77` non-empty |
| `fleet-report` | text 2 Pointer | `.ufo/reports/round-77/kotoba.md` on the fleet repo | file exists |

Round-76 facts quoted by the completion note and reusable as the fill source for `r76-dead-seats`: 64 seats,
64 unique result names, 0 empty `output` fields, no `report` field on any entry, 52 `.md` reports; the 12
names are listed verbatim in text 1 ¶2.

## Pointer resolution at the authoring revision

Every path outside a slot that the paste text names, checked at `6523ace`:

| pointer | status at `6523ace` |
|---|---|
| `plans/round-77.md`, `plans/round-76.md`, `plans/round-76-addendum-1.md`–`-6.md` | present |
| `corpus/lessons/round-76-verifier-spotcheck.md` (CD1/CD2/CD4, R76-D1…D5 at lines 28 and 79–83) | present |
| `corpus/lessons/round-75-verifier-spotcheck.md` (§ 6 at line 75, R1–R4 at lines 77–80) | present |
| `corpus/knowledge/spec-skill-creation-craft-round74.md` (C1 precedent) | present |
| `considerthese/2026-10-26.md:17` (proposal 3) | present |
| `.ufo/waves/round-76/{base-battery,receipts,snapshots,w1,build}/` | present (103 tracked files under `.ufo/waves/round-76`) |
| `.ufo/waves/round-76/receipts/{c1-base-final.txt,c2-base-final.txt,c1-controls.txt,c1-selftest-final.txt,c2-selftest-final.txt}` | present |
| `.ufo/waves/round-76/base-battery/base-gate-correction.txt` | present |
| `.ufo/waves/round-76/w1-results.json` | present |
| `.ufo/waves/round-77/receipts/{c1-base-2f675548….txt,c2-base-2f675548….txt,selftests-base.txt,census-before.txt}` | present (added by `6523ace`) |
| `verifiers/check_desc_craft.py`, `verifiers/check_r75_routed_repairs.py` | present; sha256 equal the plan pins |
| `.ufo/reports/round-76/kotoba.md` (fleet root, cited as in the r76 entry) | present (8,128 B) |
| `.ufo/waves/round-77/receipts/` | directory exists; 4 of its files are tracked at `6523ace` (`git ls-files .ufo/waves/round-77` lists exactly those four); later receipts are added by the slots |
| `.ufo/waves/round-77/` (`w1/`, `build/`) | present on disk, **untracked** at `6523ace` (`??` in `git status --porcelain`) — the `wave-commit` slot must track them or the Action's seat census and the Pointer have no committed referent (F3) |
| `corpus/knowledge/description-craft-round76.md`, `corpus/lessons/round-76.md`, `.ufo/waves/round-76/w2-registry-note.md`, `.ufo/waves/round-76/receipts/r1-folded-render.txt`, `.ufo/waves/round-76/receipts/noharm-at-tip.txt`, the S213 `used-by` cell value | **absent at `6523ace`** — this is the negative reference the completion note's first bullet states. The first three and the two receipts are named there *because* they are absent; the landed tip must have all five present (slot-filled paths must satisfy `git cat-file -e <tip>:<path>`), and no other sentence may use them as a pointer. Any path a slot produces that lands elsewhere must replace both the slot and the negative reference together. |

## Fill-check before the entries are filed

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
TIP=$(git rev-parse HEAD)
# 1. no slot left inside the two new sections (scan only the appended tail, not the whole file):
tail -n +2819 LOG.md | grep -n '\[\[SLOT:' || echo "slots: 0"
# 2. every path named in the appended tail exists at TIP:
tail -n +2819 LOG.md | grep -oE '`[A-Za-z0-9_./-]+\.(md|txt|json|py)`' | tr -d '`' | sort -u |
  while read -r p; do git cat-file -e "$TIP:$p" 2>/dev/null || echo "UNRESOLVED: $p"; done
# 3. the two verdict lines the entries quote, re-read from the cited receipts:
git show "$TIP:<c1-tip receipt>" | tail -2
git show "$TIP:<c2-tip receipt>" | tail -2
```

## Flags for the L1

**F1 — two `## Round 76` sections.** Append-only forces a second heading
(`## Round 76 — completion note (written in round 77, 2026-10-27)`). Checked: no gate reads § Round 76 or
§ Round 77 today. `check_r75_routed_repairs.py:234` calls `section(LOG, "Round 75")`, whose regex
(`:229`) runs from `^## Round 75\b` to the next `^## ` heading — that boundary is `## Round 76`, which the
tail append does not move, so § Round 75's extent and content are unchanged. `check_routed_repairs_v2.py:310`
reads § Round 61, and `check_r69_routed_repairs_v2.py:108` matches `^## Round 69(?![0-9])` literally. A
future reader that takes the *last* `## Round 76` section lands on the completion note (which carries the
honest-stop facts); one that takes the first keeps the filed entry. Keep the order in § Placement.

**F2 — the completion note asserts the re-land.** It must not be pasted before the slots resolve: a
completion note filed over an unlanded claim is exactly the r76 defect this round repairs. If `c1-receipt`
or `c2-receipt` cannot be filled with `exit 0`, apply R-b and file the observed line.

**F3 — round-77 wave files are untracked at the freeze.** `git status --porcelain` at `6523ace` lists
`.ufo/waves/round-77/{w1-dispatch.json,w1-spec.json,w1.ready,w1.ready.dispatched,w1/}` as `??`. The Action's
role census (40 seats; 12/7/6/5/4/3/1/1/1; attack 14/40) is measured from `w1-dispatch.json`
(`counts.spawn` 40, `registry.members` 40); if the landed dispatch differs, recount it from committed bytes
before filing and treat the numbers as the dispatch's, not the plan's.

**F4 — the plan names no tip-receipt names.** The r77 receipts directory today holds only base artifacts.
The fill must choose names and commit them; the recommended `c1-tip-<rev>.txt` / `c2-tip-<rev>.txt` mirror
`c1-base-<rev>.txt` / `c2-base-<rev>.txt`. The round-77 assignment requires every counter run to name
`--repo $S/clone --rev <scratch commit>` (and `--work $S/work` for C2), with the gate's own exit status
captured; the receipts should record the exact `--repo`/`--rev`/`--work` used.

**F5 — C2's R1/R2/R3 artifacts land at r76 paths in round 77.** `.ufo/waves/round-76/receipts/r1-folded-render.txt`,
`.ufo/waves/round-76/receipts/noharm-at-tip.txt` and `.ufo/waves/round-76/w2-registry-note.md` are counter
constants (`R1_RECEIPT`, `NOHARM_RECEIPT`, `W2_NOTE`). The note and the entry say plainly that they landed in
round 77; the completion note is the place that records it, and its paths must not be "fixed" to
`.ufo/waves/round-77/` — that would leave all four C2 repairs open.

**F6 — R2 measures the r75 tip, not the r77 tip.** Per `plans/round-76-addendum-5.md` the receipt's first
line must be `ac9f29510d3914a6edb97c8dbdb3445cab9141de` and both corpus gates are re-run **at that revision**.
A receipt naming the round-77 tip fails R2 even if every gate is green there. Cite it as the r75-tip receipt,
not as the round-77 no-harm battery; the two are different receipts in the text.

**F7 — the r76 control receipt is on the wrong blob.** `c1-controls.txt` names counter sha256 `87837d7a…`;
the frozen C1 blob is `cf3c45d9…`. The completion note says this; do not "repair" the sentence by dropping it,
and do not cite `c1-controls.txt` as a control of the frozen instrument anywhere else.

**F8 — dead-seat accounting must match the results file's schema.** The r76 results file has no top-level
`report` field on any entry (R3's note uses that fact), so the count is seats − `.md` files with matching
stems, not `report`-field presence. For round 77 apply the same rule and state the definition in one clause.

---

## Measurement log (this seat; read-only, lane root unless stated)

| command | observed |
|---|---|
| `git rev-parse HEAD` | `6523aced1ee0ebe07dca996213bdc645a6acbd1e` |
| `git status --porcelain` | five `??` round-77 wave paths; no tracked modification |
| `wc -l LOG.md`; `tail -40 LOG.md` | 2,818 lines; last heading `## Round 76 — honest stop (claims unlanded)` at 2,812 |
| `git show HEAD:LOG.md \| tail -c 400 \| xxd` | tail bytes `…round-76/kotoba.md`.\n` (one trailing newline) |
| `grep -n '^## Round' LOG.md` | § 69 at 2,698, § 71 2,751, § 72 2,770, § 73 2,783, § 74 2,801, § 75 2,805, § 76 2,812 |
| `git show --stat 6523ace` | 5 files / +130: `plans/round-77.md` and four receipts |
| `git show HEAD:verifiers/check_desc_craft.py \| sha256sum` | `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` |
| `git show HEAD:verifiers/check_r75_routed_repairs.py \| sha256sum` | `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` |
| `git cat-file -e HEAD:<path>` for the two entries, the lesson, the w2 note, both C2 receipts | all ABSENT |
| `git cat-file -e HEAD:kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` | PRESENT (R76-D1 open at the freeze) |
| `git diff --name-only b7f13f4 6ce2724 \| grep -E '^(SKILL.md\|corpus/\|LOG.md\|SCORECARD.md)'` | `LOG.md`, `SCORECARD.md` only |
| `git diff --stat b7f13f4 HEAD -- corpus/lessons/round-75.md corpus/SOURCES.md SKILL.md corpus/README.md verifiers/corpus-baseline.json` | empty |
| `git show HEAD:SKILL.md \| grep -c 'description-craft-round76'`; `git show HEAD:SKILL.md \| wc -l` | `0`; `590` |
| `sha256sum .ufo/waves/round-76/snapshots/*.md` vs `MANIFEST.sha256` | all three match; S213 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` (own exit captured) | **exit 1**; tracked 146, unindexed 2 (`round-75-verifier-spotcheck.md`, `round-76-verifier-spotcheck.md`), `report_total` 102, `commit_total` 44 |
| `python3 -B verifiers/verify_corpus_independent.py --json` (own exit captured) | **exit 1**; `head` `6523ace`; results `INFO tracked_files 146`, `DRIFT corpus.index.unindexed 2`, `INFO report_total 102`, `INFO commit_total 44` |
| `python3` read of `.ufo/waves/round-76/w1-results.json` | wave `w1`, lane `kotoba`, round 76; 64 seats, 64 unique names, 0 empty outputs, 0 entries with a `report` field |
| `ls .ufo/waves/round-76/w1/*.md \| wc -l`; set difference vs results names | 52; 12 missing (names in text 1 ¶2) |
| `ls .ufo/waves/round-76/` | `base-battery build receipts snapshots w1` + `w1-*` — no `w2*` |
| `python3` read of `.ufo/waves/round-77/w1-dispatch.json` | `counts.spawn` 40, 40 `taskCall.tasks`; roles executor 12, scout 7, scribe 6, reviewer 5, critic 4, mutation-tester 3, sentinel 1, simplifier 1, connector 1 |
| `grep -n '^## \|^### ' corpus/lessons/round-75-verifier-spotcheck.md` / `round-76-…` | § 6 at 75 (R1–R4 at 77–80) / § 5 at 75 (R76-D1…D5 at 79–83) |
| `tail -6 corpus/lessons/round-75.md` | ends in the `## Mistakes` table — no appended correction yet |
| `grep -rln 'LOG.md' verifiers/*.py`; `grep -n 'section(…LOG'` | 18 gates name `LOG.md`; only `check_r75_routed_repairs.py:234` (Round 75) and `check_routed_repairs_v2.py:310` (Round 61) read named sections |

## What this seat did not do (scope)

- Did not edit `LOG.md`, `SCORECARD.md`, `QUALITY.md`, `SKILL.md`, `corpus/SOURCES.md`, `corpus/README.md`,
  any lesson, entry, counter, manifest, template, script or `.ufo/state/` file.
- Did not run either frozen counter and produced no receipt: the base readings quoted are the committed
  receipts `.ufo/waves/round-77/receipts/{c1,c2}-base-2f675548….txt` and the r76 base receipts; the two
  no-harm gate runs above are this seat's own read-only measurements of the **base** state (exit 1), not a
  claim measurement.
- Did not create, edit or delete anything under `~/.local/bin`; no tool install, no package manager call.
- Did not draft the round-77 SCORECARD row (SC05ScorecardDrafts), the round-76/77 lessons (SC01/SC02), the
  QUALITY rows (SC03), or the § Round 75 append (E05R3R4Repair); this draft names their artifacts only
  through slots.
