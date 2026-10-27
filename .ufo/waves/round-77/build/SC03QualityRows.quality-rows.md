# SC03QualityRows — corpus/QUALITY.md row drafts (kotoba round 77, w1)

Seat: SC03QualityRows (scribe, leaf; no subagents, no background jobs). Nothing here is applied to a
lane file. Append target is `corpus/QUALITY.md` at lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`:
89 lines, sha256 `08dbfae23b7cea190971cb1e931fedbe5a980cb577609d0bfe4336d83e8b1261`, last row `Q73`,
working tree clean against HEAD for that file.

Every measurement below was run by this seat in
`/fast/scratch/hyaku/kotoba-r77/SC03QualityRows/clone` (`git clone --shared`, `rev-parse --show-toplevel`
checked) read-only; the scratch tree was removed before yielding.

Numbering: the file ends at Q73, so the four admitted rows are **Q74–Q77 positionally**. If the L1 lands
another admitted row first, shift these four; no committed row is rewritten, and every `supersedes` cell
is `—` (extensions are named inside the criterion, the Q59/Q72 precedent, because each closest row owns a
different arm and superseding it would retire that arm).

## Candidate dispositions

| candidate | provenance | existing rows checked (why they do not reach it) | disposition |
|---|---|---|---|
| a measured field is stated with its convention (folded-scalar render vs physical lines, clip vs stripped) | M76-1 `number-drift`; `.ufo/waves/round-76/build/B08-q74-quality-row.diff` | Q13 (a count carries its command — the r75 window *did* carry its command and was still wrong, because the unit was the layout's); Q54 (word counts); Q19 (before-value re-measured with command+commit); Q56 (`byte-exact` vs shaped) | **admitted → Q74** (B08 draft revised: widened from the YAML case to any measured field, `extends Q13` clause added, evidence re-measured at `2f675548` and `6523ace`) |
| a receipt captures the gate's own exit status, not a pipeline's | M76-7 `attribution`; r76 base-battery receipt + its L1 withdrawal (`plans/round-76-addendum-2.md:7`) and corrected receipt; r54 recurrence; `plans/round-77.md:48` | Q24 (a *piped instrument* hashes empty input — input hash, not status); Q48 (self-test asserts exit 0/1 — the assertion, not the capture); Q50/Q36 (a receipt names revision and observed result — not how `$?` was taken); Q58 (a counter recomputes the corrected value) | **admitted → Q75** |
| a round that cites a lesson as promised must land the lesson or drop the citation (CD2) | `corpus/lessons/round-76-verifier-spotcheck.md:26` | Q65 (a promised row/box add is checked arithmetically *before* it is promised); Q60 (an artifact cited *with a revision* exists at it — the r76 promise carries no revision); Q68 (report pointers resolve); Q03/Q04 (a record's bytes resolve) | **admitted → Q76** |
| a recovery commit is checked for the path it adds (CD1) | M76-8 `landing`; `corpus/lessons/round-76-verifier-spotcheck.md:25` | Q49 (lane-local report paths + the misroot sweep — *satisfied* by `6ce2724`, which did commit the report into the lane); Q22 (a hash match = byte identity, not custody); Q03 (a record names the commit holding its bytes); Q68 | **admitted → Q77** (extends Q49 and Q22) |
| r76 draft's `number-drift` (slice off-by-one: 1021 vs 1022) | `.ufo/waves/round-76/build/lesson-draft.md:117` | Q74's clip/stripped clause, once landed, states exactly this | **rejected — duplicate of Q74**, no row |
| r76 draft's `vacuous` (red-before probe at the base where the counter does not exist) | `.ufo/waves/round-76/build/lesson-draft.md:118` | Q60/Q03 (an artifact cited at a revision must exist there), Q50 (a result must be observed and receipted) | **not a bar-level candidate**: a defect row already covered by the named rows; its fix is a recipe (state the frozen-counter invocation in the predicate), not a new criterion |
| r76 draft's `reference-drift` (F7 exact `used-by` pin vs the append-only registry) | `.ufo/waves/round-76/build/lesson-draft.md:119` | Q32 (an identity is matched exactly), Q73 (a pinned cell is ledgered in the counter) | **not a bar-level candidate**: the fix is a counter repair, and Q32/Q73 already bind the mechanism |

## Rows (append verbatim after Q73; the trailing `| — |` is the `supersedes` cell)

| Q74 | A measured field's number is the value of the artefact's own parse, not of its layout: the record names the parser and the slice (`yaml.safe_load` over the frontmatter keeping the block's trailing newline), says whether the number counts the rendered scalar or the physical lines, and names the ambient-variation choice (folded-scalar clip newline counted 1,022 / stripped 1,021); a raw-line sum is not the scalar's value because `length($0)` counts the two-space indent and the `description: >` marker line — the r75 window `awk 'NR>=3&&NR<=8'` sums to 392 over 6 of the block's 16 source lines (marker 3, content 4–18, fence 19) for a description that renders 1,022. | frontmatter/description size measurements, and every quantity whose unit the author chooses | M76-1 `number-drift` (`corpus/lessons/round-76.md` § Mistakes, landing r77; draft `.ufo/waves/round-77/build/SC01Lesson76.round-76.md:104`): the mistaken measurement is `corpus/lessons/round-75.md:11` (`14,76,78,73,79,72`, sum 392), listed as M76-1 in `plans/round-76.md:74` and routed as R76-D2 in `corpus/lessons/round-76-verifier-spotcheck.md`; `git show <rev>:SKILL.md \| python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"` prints `1022 1021` at `2f675548` and `6523ace` (first sentence 151). Extends Q13 (a count carries its command) and does not supersede it: the r75 window carried its command and was still wrong because the unit was the layout's; Q74 is not in the tree at `2f675548` (the file ends at Q73) and this row is its first landing. | — |
| Q75 | A receipt records the gate's own exit status, captured from the gate process (`cmd > out 2>&1; echo "exit=$?" >> out`, or `set -o pipefail` / `${PIPESTATUS[0]}` where a pipe is wanted), and a receipt whose status follows a filter of the gate's output (a trailing `tail`, `head`, `grep` or `cat`) is discarded, not cited: `false \| cat >/dev/null; echo $?` prints 0 where `false; echo $?` prints 1. The rule binds the *recorded* status only — a pipeline used as a condition (`if … \| grep -q …`) is out of scope. | receipts for gate and no-harm battery runs, wave battery scripts, and any captured `$?` | M76-7 `attribution` (`corpus/lessons/round-76.md` § Mistakes, landing r77; draft `.ufo/waves/round-77/build/SC01Lesson76.round-76.md:108`): `.ufo/waves/round-76/base-battery/base-battery.txt:2-6` and `:7-11` (committed at `6523ace`, sha256 `27412fd742ab6f1186ecf9515a0bcbc07983729e7a4f64ba0a23869ba80f48fb`; the L1 withdrew that capture at `plans/round-76-addendum-2.md:7` — "the command pipeline recorded `tail`'s exit status, not the gate process status" — and the corrected receipt `.ufo/waves/round-76/base-battery/base-gate-correction.txt:139,270`, committed at `6523ace`, carries each gate's own `exit=1`, so the repair exists and the rule does not) state `exit=0` for `verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json` while the direct exits at the same tree are 1 and 1 (re-measured there: piped 0, direct 1, both gates); the same class at r54 (`check_description_thresholds.py --rev 422ffd10 \| tail -3; echo exit=$?` → 0, `.ufo/waves/round-54/falsify/W2CriticLesson.md:87`: "that is `tail`'s exit code, not the counter's"); diagnosed in `.ufo/waves/round-76/w1/B10RepairD2D3.md:82`, `B11RepairD4.md:194`, `B24TipBatteryScript.md:242-246`; control `.ufo/waves/round-76/receipts/pipeline-exit-demo.txt`; correct-form precedent `echo "exit=${PIPESTATUS[0]}"` (`.ufo/waves/round-62/w2/FalsifyBatterySelfTests.md:270`); frozen as the round's rule in `plans/round-77.md:48`. Extends Q50 (a receipt names the observed result) and Q24 (a piped instrument hashes empty input); neither checks how the status was captured. | — |
| Q76 | A round that cites a lesson as promised — "recorded in the round-N lesson Gate", "M76-1 → Q74", an M-row pointer — must land that lesson with the promised section before its report, or drop the citation in the same round; the promise is a path claim even without a revision, so `git cat-file -e <rev>:corpus/lessons/round-<N>.md` must exit 0 (it exits 128 when the file is absent) beside `grep -n 'round-<N> lesson' plans/round-<N>.md` for the promise text, and a lesson the report itself calls incomplete ("remain incomplete") is a dropped promise, not a deferred one. | plans' promises of lesson and M-row content, round lessons, and the reports citing them | CD2 (`corpus/lessons/round-76-verifier-spotcheck.md:26`): `plans/round-76.md:11` and `:74` promise the round-76 lesson Gate and M76-1, while `git cat-file -e <rev>:corpus/lessons/round-76.md` exits 128 at `b7f13f4`, `6ce2724`, `2f675548` and `6523ace`, and `git ls-tree --name-only 6523ace corpus/lessons/` carries only `round-76-verifier-spotcheck.md`; `plans/round-77.md:44` repeats the promise. Extends Q65 (a promise is checked arithmetically before it is made) and Q60 (an artifact cited with a revision exists at it) — the revision-less promise is the form both leave open. | — |
| Q77 | A recovery or repair commit is checked for the paths it adds before its claim lands: `git show --name-status --pretty= <rev>` names exactly the declared lane path of the recovered file, that path is absent at the parent (`git cat-file -e <rev>^:<path>` exits 128), and no added path lies outside the lane tree; a `cmp`/sha256 equality proves the bytes travelled and says nothing about which path received them. | recovery commits for misrooted files, repairs that re-add a file, and the report sentence that claims them | M76-8 `landing` (`corpus/lessons/round-76.md` § Mistakes, landing r77; draft `.ufo/waves/round-77/build/SC01Lesson76.round-76.md:109`) and CD1 (`corpus/lessons/round-76-verifier-spotcheck.md:25`): `6ce2724` adds `A kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` while `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` already exists at the parent `ec7f853` (exit 0) with the same sha256 `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb`; the typo path is absent at the parent (exit 128) and the typo tree still carries 2 files at `6523ace` (`git ls-tree -r --name-only 6523ace \| grep -c '^kotoba-shokukin/'` → 2), the r75 instance added by `ac9f295` ("round-75: preserve recovered misroot seat report"). Extends Q49 (lane-local report paths and the misroot sweep — Q49 is satisfied by `6ce2724`, the commit is what failed) and Q22 (a hash match establishes byte identity, not custody); does not supersede either. | — |

## Checks (each row's own falsifier, run by this seat)

- **Q74** — `git show <rev>:SKILL.md | python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"` → `1022 1021`, exit 0, at `2f675548` and `6523ace`. The non-conforming world is the r75 command itself: `git show 2f675548:SKILL.md | awk 'NR>=3&&NR<=8{print NR ":" length($0)}'` → `3:14 4:76 5:78 6:73 7:79 8:72`, `sum=392`.
- **Q75** — the gate's own status is `python3 -B verifiers/verify_corpus_integrity.py --json >/dev/null 2>&1; echo $?` → 1 at `6523ace`, while the same command piped to `tail -3` → 0 (same for `verify_corpus_independent.py`, 1 vs 0). The r76 receipt keeps only the filtered tail plus `exit=0`. `verifiers/*.sh` carries no status capture after a pipe today (`grep -n ' | ' verifiers/*.sh` hits only condition/`printf | grep` uses in `fault_injection_corpus.sh:214,222,276,284,413`), so the gap is in receipts, not scripts.
- **Q76** — `git cat-file -e <rev>:corpus/lessons/round-76.md` → 128 at `b7f13f4`, `6ce2724`, `2f675548`, `6523ace`; `grep -n 'round-76 lesson' plans/round-76.md` → `11:`, `74:`.
- **Q77** — `git show --name-status --pretty= 6ce2724` → one line, `A kotoba-shokukin/...`; `git cat-file -e ec7f853:kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` → 128; `git cat-file -e ec7f853:.ufo/waves/round-76/w1/A18ScoutSnapshot.md` → 0, sha256 `ae39b182…`; `git ls-tree -r --name-only 6523ace | grep -c '^kotoba-shokukin/'` → 2.

## Preconditions and landing order

1. These rows land **after** the lesson rows they cite (the plan's landing order already puts lessons
   before the QUALITY row). Q76 is the row that makes that ordering binding rather than customary.
2. The anchors exist in the r77 lesson draft, verified at the cited lines: M76-1 (`:104`), M76-7 (`:108`),
   M76-8 (`:109`) of `.ufo/waves/round-77/build/SC01Lesson76.round-76.md`. If the landed
   `corpus/lessons/round-76.md` drops one of them, drop or hold the row it anchors (`corpus/QUALITY.md:5`:
   no criterion exists without a lesson behind it).
3. Q74's `grounded in` names M76-1 by its lesson home **and** by committed bytes
   (`corpus/lessons/round-75.md:11`, `plans/round-76.md:74`,
   `.ufo/waves/round-76/build/lesson-draft.md:116`), so an id renumbering in the lesson does not leave the
   row pointing at nothing.
4. Q76's promise check applies to this round's own plan: `plans/round-77.md:44` promises
   `corpus/lessons/round-76.md`, and `:52` promises the wave; both must land or drop the citation.

## Findings routed to others

- **M76-7 line refs off by one** in the lesson draft: it cites `base-battery.txt:3-7` and `:9-11`; the
  blocks are `:2-6` and `:7-11` (line 7 is the second `==` header, line 8 the first JSON line — `cat -n` on
  the 36-line receipt). My Q75 row uses the verified numbers; messaged to `SC01Lesson76`.
- **Q74 does not exist at `2f675548`** and the r76 `B08-q74-quality-row.diff` is unlanded, so no row above
  or in the lesson may cite Q74 as a landed fix; the Q74 row above is its first landing.

## Limits

- These are row drafts, not a claim, and assert no axis move. No counter, gate or lane file was touched.
- I did not re-run the two frozen counters (`check_desc_craft.py`, `check_r75_routed_repairs.py`); nothing
  here relies on them.
- The r76 closure's CD3 (round-end census) and CD4 (52 report files for 64 seats, no dead-seat count) were
  not drafted as rows: CD3 is executed by this plan's own no-harm item, and CD4 is routed as R76-D5 to the
  report; the nearest bar rows (Q27/Q40/Q49 seat accounting bound to output) may already apply. Not a
  judgement that they are covered — they were outside this seat's candidate list.
- Row text uses `\|` inside table cells where a shell pipe appears, as the file's existing rows do; the
  appended line must keep that escaping.
