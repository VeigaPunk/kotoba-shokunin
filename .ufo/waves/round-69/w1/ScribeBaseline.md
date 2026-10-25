# ScribeBaseline — `verifiers/corpus-baseline.json` note audit (round 69, wave 1)

**Verdict: NOT CONFIRMED.** The `note` field does not document a round-69 re-record. It is
still the round-68 record (head `605b84ba`), and the file contains zero occurrences of the
string `round-69`.

Axis: `consistency`. Scope: read the baseline, confirm the round-69 re-record, flag notes that
reference an older record without a round-69 entry. No lane file was modified.

## 1. What was read (identity)

| field | value |
|---|---|
| path | `verifiers/corpus-baseline.json` |
| sha256 | `d3f8acd44d65786bead302812035e7288c4760e7a169df53964f8917be2d488d` |
| size | 12070 B |
| at HEAD `a238989` | identical sha256 (file is unmodified: `git status --porcelain` empty for it) |
| `as_of` | `2026-10-24T23:59:00-03:00` (previous calendar day; round 69 measures 2026-10-25) |
| `measured_against.head` | `605b84ba` — "round-68: C1 depth client trust gates … and C2 consistency routed r67 repairs" |
| `measured_against.git_status` | "round-68 content commit; the census re-record is committed separately" |
| `measured_against.note` | 610 chars, begins "Re-recorded at the round-68 content commit 605b84ba." |
| `notes` keys | 17: rounds 19, 16, 21, 23, 37, 41, 46, 47, 47_closure, 48, 48_pointer, 49, 50, 50_entry, 53, 54, 66 — **no `round-69` key**, and none for 67/68 either |
| occurrences of `round-69` in file | **0** |

**Flag (primary):** `measured_against.note` references the round-68 record and there is no
round-69 entry anywhere in the file. Under the plan's C2/R68-8 (D8) this is an open routed
defect, not an observation: `verifiers/check_r68_routed_repairs.py:298-317` compares four
baseline expectations to the corpus gate's own `--no-baseline --json` measurement at `--rev`,
and all four currently disagree (see §4).

## 2. Gate measurements taken (own runs, sandboxed)

Method: `git clone --shared` of the lane into `/tmp`, then either `git reset --hard <rev>` (for
committed revs) or `cp -a corpus verifiers SKILL.md PROVINCE.md` over the clone plus
`git add -A corpus` (to measure the L1's uncommitted draft as it would land). Gate:
`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`. Never run in the lane.

| rev | tracked_files | unindexed | report_total | commit_total | note |
|---|---|---|---|---|---|
| `532cda0` (r67 closure) | 121 | 0 | 82 | 38 | |
| `fe194f6` / `e94ae32` (r67 spot-check) | 122 | 1 | 85 | 38 | +1 tracked, +3 pointers, unindexed |
| `0b082b4` (r68 plan, parent of `605b84ba`) | 122 | 1 | 85 | 38 | |
| `605b84ba` (baseline's stated head) | 124 | 0 | 85 | 38 | matches the note exactly |
| `2cf0d99` (r68 wave-1 evidence) | 124 | 0 | 85 | 38 | matches recapture receipt |
| `a5f7459` (lane base in plan) | 125 | 1 | 87 | 38 | plan C2-base control: 125, 1, 87 |
| `a238989` (lane HEAD, committed only) | 125 | 1 | 87 | 38 | plan commit added no corpus bytes |
| **draft working tree (127 tracked)** | **127** | **1** | **87** | **39** | the L1's uncommitted round-69 content |

Stable across three independent sandboxes (07:16–07:19 -03:00, 2026-10-25). Draft snapshot:
`corpus/README.md` sha256 `79a5760f…`, mtime `2026-10-25 07:08:15 -0300`.

Default mode (baseline applied) at the draft: **5/9 checks pass, exit 1**

```
DRIFT corpus.index.tracked_files  observed=127 expected=124
DRIFT corpus.index.unindexed      observed=1   expected=0 / empty
DRIFT corpus.pointers.report_total observed=87 expected=85
DRIFT corpus.pointers.commit_total observed=39 expected=38
```

`unindexed_detail`: `corpus/lessons/round-69.md` — `corpus/README.md` has a row for the entry
(line 130) and the round-68 spot-check (line 131) but **no in-table row for the round-69
lesson**.

## 3. Task-prompt targets vs measurement

| quantity | prompt target | draft measurement | matches |
|---|---|---|---|
| tracked_files | 127 | 127 | yes |
| unindexed | 0 | 1 | **no** |
| report_total | 89 | 87 | **no** |
| commit_total | 38 | 39 | **no** |

Reconciliation, from the measured deltas:

- **tracked_files 127** is correct. Base 125 + the entry + the lesson = 127.
- **unindexed 1 -> 0** requires an in-table coverage row for `lessons/round-69.md`. The draft
  has none. (Tested: adding an in-table row yields `unindexed_detail: []`.)
- **report_total 87, not 89.** Neither `corpus/knowledge/skill-name-precedence-round69.md` nor
  `corpus/lessons/round-69.md` carries a single `.ufo/reports/` pointer (grep: zero hits,
  both files). 87 is base's value carried over: 85 (r68 record) + 2 from the round-67
  spot-check's repo-relative pointers at `fe194f6`. Reaching 89 needs **two** new resolving
  report pointers that do not exist in the draft.
- **commit_total 39, not 38.** The only new commit token is `corpus/lessons/round-69.md:12`
  ``commit `a238989a` `` — resolvable (it is the plan commit). Base 38 + 1 = 39. No plausible
  re-record returns this to 38; removing the citation would be the only route, and that is the
  opposite of what a round lesson should do.

**Caution on the 89 route:** `.ufo/reports/round-69/` currently holds `audio.md`,
`game-dev-2d.md`, `kotodama.md` only — **no `kotoba.md`**. Two pointers written to
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-69/kotoba.md` read `report_dead=2` today
(observed); the gate must be 9/9, so either the report is written before the re-record or the
pointers cite an existing report.

## 4. Reachability proof (sandbox only, no lane mutation)

The tuple `127 / 0 / 89 / 39` is internally consistent. In a `/tmp` shared clone of the draft
plus (a) an in-table row for `lessons/round-69.md` and (b) two resolving report pointers, with
the baseline expectations set to `127/0/89/39`:

- `verifiers/verify_corpus_integrity.py` -> `9/9 checks pass`, exit 0
- `verifiers/verify_corpus_independent.py` -> exit 0
- `check_r68_routed_repairs.d8_index_baseline(...)` -> `[]` (no findings)

(sim commit `d9b5c0064e3fce9c4882d318d414c22c4d2861a1`, sandbox-local, not in the lane.)

The lower alternative `127 / 0 / 87 / 39` (lesson row, no new pointers) also reaches 9/9,
exit 0. Both are defensible; only 89 requires the two pointers.

D8 at the **unre-recorded** draft (sim commit
`0d802c5fa62ba549b288a925bda7252534aee99f`) returns all four findings:

```
D8: baseline corpus.index.tracked_files expects 124, the gate measures 127
D8: baseline corpus.index.unindexed expects 0, the gate measures 1
D8: baseline corpus.pointers.report_total expects 85, the gate measures 87
D8: baseline corpus.pointers.commit_total expects 38, the gate measures 39
```

So C2's "8 of 8" cannot close until the re-record lands; this baseline is a hard precondition
of the C2 predicate, not a bookkeeping afterthought.

## 5. Provenance defect in the existing round-68 note (secondary flag)

The note says `tracked_files 121 -> 124` and `report_total 82 -> 85` "because
corpus/knowledge/client-trust-gates-round68.md and corpus/lessons/round-68.md are new tracked
corpus files". Measured:

- the immediate parent of `605b84ba` (`0b082b4`) already reads **122 / 1 / 85 / 38**;
- `121 / 82` is the **round-67 closure** state (`ed4df3e` … `532cda0`), three commits earlier;
- the two intermediate commits `fe194f6`, `e94ae32` (round-67 spot-check) took tracked
  121 -> 122 and report pointers 82 -> 85, and left `unindexed 1`;
- the round-68 content commit itself added **0** report pointers (85 -> 85). Its two new files
  account for +2 tracked (122 -> 124), not +3, and for none of the report_total delta.

The note is therefore faithful about its **at-head** values (124/0/85/38 verified) but its
**before-values and attribution** are taken from a record one round old and misattribute the
round-67 spot-check's +3 pointers. If round 69 copies this pattern the same defect recurs; the
new note should state the delta from a named, measured rev and name which file added each
pointer.

## 6. What the round-69 entry should say

Values to record (gate's own measurement, to be taken after the final round-69 tree and the
lesson index row land):

```
tracked_files 127
unindexed    0
report_total 89   (or 87 if no new report pointers are added)
commit_total 39
head         <final round-69 content commit>
as_of        2026-10-25
```

`commit_total 38` in this wave's target brief is stale: 39 is the measured value and is
reproducible. The note must name `127`, `0`, `89` (or `87`), `39` and the commit it measured,
and must not restate `124/85/38` as "current".

## 7. Limits

- Measured against the working tree (the gate reads the worktree, not HEAD, per its docstring).
  The L1 may still edit; README was last written 07:08:15 -0300 and the baseline was untouched
  at 07:16.
- The 89 target depends on two report pointers that do not exist in the draft; whether the L1
  wants 87 or 89 is a content decision, but 89 is unreachable without them and unreachable
  with dead pointers.
- No round-69 lane report exists yet (`kotoba.md` absent), so any round-69 pointer is dead
  until the closure writes it.
- I did not run the full C2 counter (`check_r68_routed_repairs.py --rev`); I called its D8
  function directly to isolate the baseline finding. Other D-items were out of this seat's
  scope.
- `verifiers/corpus-baseline.json` was never edited by this seat; every experiment ran in a
  `/tmp` shared clone.

## 8. Provenance

Commands (all in `/tmp` shared clones of `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):

```
git clone --shared --quiet . $SB/lane
cp -a corpus SKILL.md PROVINCE.md verifiers $SB/lane/ && (cd $SB/lane && git add -A corpus)
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
python3 -B verifiers/verify_corpus_integrity.py            # baseline-applied mode
git reset --hard <rev> ; python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
python3 -c "import sys;sys.path.insert(0,'verifiers');import check_r68_routed_repairs as c; \
            print(c.d8_index_baseline(c.Repo('.', '<sha>')))"
```

Raw outputs kept at `/tmp/r69-scribe-gate.json` (draft), `/tmp/r69-scribe-default.txt` (draft,
baseline mode), `/tmp/r69-scribe-base.json` (`a5f7459`), `/tmp/r69-scribe-r68.json`
(`605b84ba`), `/tmp/r69-scribe-final.json` (89-pointer simulation), `/tmp/r69-alt.txt`
(87-pointer alternative). These are ephemeral; the values are restated in §§2–4.
