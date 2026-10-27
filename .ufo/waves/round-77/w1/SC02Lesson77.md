# SC02Lesson77 — round-77 lesson skeleton (kotoba, hyaku run 10, wave w1)

Seat: `SC02Lesson77` (leaf, build/scribe). Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base / freeze commit for every measurement below: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(`git rev-parse HEAD` in the lane; tracked worktree clean: `git status --porcelain --untracked-files=no` → no output).
Lane files edited: no tracked file; the only writes are three new files under `.ufo/waves/round-77/` (this report
and two `build/SC02Lesson77.*` deliverables). Lane git/jj written: none. Claim data written: none.

## 1. What the seat was asked for and what it produced

Deliverable `build/SC02Lesson77.round-77.md` is the skeleton of `corpus/lessons/round-77.md` for the L1 to fill
after data lands: sections `## Gate` (S213 re-open slots for `S01Reopen1`/`S02Reopen2`, this round's admit/reject
decisions, census before with the after slot, S213 `used-by` old→new slot, considerthese proposal 3),
`## Mistakes` (the r76 spot-check CD2 and CD1 rows mined, plus slots for what the round adds), `## Spot-check`
(a slot the non-author closure fills). Every unfilled item is literally `[[SLOT: …]]` on one line so the L1 can
`grep -c '\[\[SLOT:'` for leftovers.

| file | bytes | lines | sha256 |
|---|---|---|---|
| `.ufo/waves/round-77/build/SC02Lesson77.round-77.md` | 12,005 | 108 | `4cc865488a47d85d4698af1a213eea1da52b76a75dda53f5059da1db22cdcc37` |
| `.ufo/waves/round-77/build/SC02Lesson77.red-before.txt` | 8,464 | 172 | `c3457cd12234ff6538af76711c999f6bb4300c8db62a12eabbd9a2b27499c4ad` |

Structure check on the draft: `grep -c '\[\[SLOT:'` → 20; `awk '/\[\[SLOT:/{ if ($0 !~ /\]\]/) print NR": MULTILINE" }'`
→ no output (every slot closed on its own line); the `## Mistakes` table is 6 columns on every row
(`| id | class | evidence pointer | captured-by | fix | red-before … |`, plus the separator and the placeholder row);
headings are exactly `## Gate`, `## Mistakes`, `## Spot-check`.

## 2. Inputs read (absolute paths under the lane unless stated)

`plans/round-77.md`; `plans/round-76.md`; `plans/round-76-addendum-1..6.md`; the two frozen counters' docstrings
(`verifiers/check_desc_craft.py`, `verifiers/check_r75_routed_repairs.py`); `corpus/lessons/round-76-verifier-spotcheck.md`
(CD1 `:25`, CD2 `:26`); `corpus/lessons/round-75.md` (`:12`, the misroot row) and
`corpus/lessons/round-75-verifier-spotcheck.md:44`; `corpus/QUALITY.md` (Q01–Q73); `corpus/SOURCES.md:153` (S213);
`corpus/README.md` index; `considerthese/2026-10-26.md` (proposal 3 at `:17`); `/home/vgpnk/Projects/shokunin/CORPUS.md`
(one-row-per-mistake, the class vocabulary, and the "shown able to fail" rule at `:179`); the r76 build drafts
(`entry-draft.md`, `lesson-draft.md`, `skill-patch.md`, `sources-patch.md`, `log-draft.md`, `scorecard-draft.md`,
`w2-registry-note.md`, `B08-*`, `B10RepairD2D3.*`) as inputs only; the r76 snapshots
(`.ufo/waves/round-76/snapshots/` — `MANIFEST.sha256`, `fetch-record.json`, three pages); the r77 base receipts
(`c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`, `c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`, `selftests-base.txt`, `census-before.txt`).

Nothing from the r76 drafts was trusted into the draft: every value there is either re-measured at 6523ace or left
as a slot.

## 3. Measurements at 6523ace that the draft rests on (commands and observed results)

```
$ git -C <lane> sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py
cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e  verifiers/check_desc_craft.py
989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63  verifiers/check_r75_routed_repairs.py
                                            → both equal `plans/round-77.md:17-18`; no counter edited by this seat
$ wc -l SKILL.md                             → 590   (budget 600; plan § No-harm battery)
$ git -C <lane> cat-file -e 6523ace:corpus/lessons/round-76.md ; echo exit=$?
fatal: path 'corpus/lessons/round-76.md' does not exist in 'HEAD' ; exit=128
$ git -C <lane> ls-tree -r --name-only 6523ace | grep -c '^kotoba-shokukin/'   → 2
$ git -C <lane> ls-tree -r --name-only 6523ace | grep -E 'R75Facet48|A18ScoutSnapshot'
.ufo/waves/round-76/w1/A18ScoutSnapshot.md
kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
$ git -C <lane> cat-file -e 6523ace:.ufo/waves/round-75/w1/R75Facet48.md ; echo exit=$?   → fatal … exit=128
```

Byte identity (sha256 of `git cat-file -p <rev>:<path>`): `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md`
= `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` = `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb`;
`kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` = `a419cc6f2513d0a5a6bf0887e3694445ffd04cbaa3872c47053c3f96f4c9fdd9`
(no second copy). Introduction commits (`git log --diff-filter=A -- <path>`): `ac9f295` for the round-75 file,
`6ce2724` for the round-76 file.

Census-before, from the committed receipt `.ufo/waves/round-77/receipts/census-before.txt`:
`grep -c W04` → 20; the last data line is `kotoba  ok  …/corpus/SOURCES.md` and the final line is `exit=0`. The
draft states it as such and leaves the after-census as a slot (not rerun — the receipt is committed at freeze and
the after-state does not exist yet).

## 4. Findings

**F1 — `plans/round-77.md` § Trigger claims R76-D1 done; the tree does not have it.** The plan lists "**R76-D1**
stray `kotoba-shokukin/` path removed", but at 6523ace `git ls-tree -r --name-only 6523ace | grep -c '^kotoba-shokukin/'`
prints `2` (both files above). This is a record-vs-tree drift at the round's own base (Q03 class). The draft's
M77-2 row records the measured state and leaves the landing commit as a slot; it does not repeat the plan's sentence.

**F2 — removing the typo root naively loses a seat report (custody).** `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`
is the **only** copy of the r75 seat report: `git cat-file -e 6523ace:.ufo/waves/round-75/w1/R75Facet48.md` exits 128.
Any R76-D1 fix must restore it to the declared path first (bytes equal), then drop the typo root — exactly the
order this seat's fix demo used. (Q22: byte identity is not custody; the file is otherwise unrecoverable from the
tree.)

**F3 — the r75 lesson and the r75 closure both endorsed the misrooted path.** `corpus/lessons/round-75.md:12` says
the report was "Copied byte-exact to the same relative lane path, verified with `cmp`". The r75 closure repeats it
at `corpus/lessons/round-75-verifier-spotcheck.md:44`: "Misroot `R75Facet48` recovered: `git diff --numstat` carries
`22 0 kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`; `git ls-tree -r ac9f295…` confirms it". The numstat
line the closure cites *contains the typo path*, so the closure validated the diff against its own spelling rather
than against the seat's declared path. That is the mechanism that kept the defect alive across two rounds; the
draft's M77-2 row names it. The closure file itself is read-only for the lane (its header: written by the hyaku
closure, never edited here), so the correction belongs in a lane-owned file (slot in the draft).

**F4 — `corpus/lessons/round-76.md` does not exist, and C1 depends on it.** `git cat-file -e 6523ace:corpus/lessons/round-76.md`
exits 128, while `plans/round-76.md` (C1 (a)/(e), touch list) and `plans/round-77.md` § Trigger both name it. The
frozen C1 counter's base receipt says so in its own words: `(a) corpus/lessons/round-76.md is not committed at the
measured revision` and `(e) row S213's used-by cell does not list corpus/knowledge/description-craft-round76.md`
(`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`). So R76-D2 is not "handled" at base either, and C1 (a) cannot pass
until a real lesson lands. The draft records this in the Gate (carried-declines paragraph) and in M77-1; it does not
write the r76 lesson (not this seat's file).

**F5 — no QUALITY criterion catches either mechanism, after a shown sweep.** `grep -in '<term>' corpus/QUALITY.md`
at 6523ace: `stray` → exit 1 (no row), `top-level` → exit 1 (no row), `does not exist` → exit 1 (no row),
`misroot` → Q49, `promis` → Q18, Q65, `cat-file -e` → Q60, `landed` → Q03, Q57, `absence` → Q14, Q22, Q64.
Reading: Q49 bounds seat-report lane-locality and the final misroot sweep but only outside the lane and never bounds
the lane tree's own top-level entries; Q65 covers a plan's *promised* landing only in budget arithmetic; Q60 owns
the `git cat-file -e` mechanism but for a citation-with-revision, not a forward promise. The draft's captured-by
cells say exactly that (Q49 "partially", Q65/Q60 "nearest", `none` for the mechanism) rather than claiming a
criterion exists.

**F6 — both fixes are shown able to fail, on the same command, with the fix as the only delta.** Receipt
`build/SC02Lesson77.red-before.txt`; summary:

| check | at 6523ace (lane) | at sandbox `a0c4762f…` (fix applied) |
|---|---|---|
| check1 — no tracked top-level path outside the lane's declared roots | `kotoba-shokukin` printed, `FAIL`, exit 1 | `ok`, exit 0 |
| check2 — every `corpus/**.md` path `plans/round-76.md` names exists | 9 paths checked, `MISSING corpus/knowledge/description-craft-round76.md`, `MISSING corpus/lessons/round-76.md`, exit 1 | 9 paths, only the knowledge entry still `MISSING` (C1 data, not this seat's), exit 1 |
| check2, lesson arm (3 `corpus/lessons/*.md` paths) | `MISSING corpus/lessons/round-76.md`, exit 1 | all present, exit 0 |

The sandbox commit is `a0c4762fa55492277828a6fa8b7e65c20aa3b9d5` (sandbox clone
`/fast/scratch/hyaku/kotoba-r77/SC02Lesson77/clone`, created by `git clone --shared <lane>`; `user.name`/`user.email`
set before the only commit; `rev-parse --show-toplevel` asserted equal to the clone dir; scratch removed after the
receipt was written). It exists nowhere in the lane. The partial green on check2's all-paths arm is disclosed in the
draft: the check measures existence only (Q26), and the entry is C1 claim data.

## 5. Coordination and conflicts

- `E11StrayAndMisroot` independently reached the same facts and the same order of operations (`.ufo/waves/round-77/w1/E11StrayAndMisroot.md:52-54,108-126`:
  "R75Facet48 stray is the only copy", restore-then-delete candidate commit, "Lesson correction owed"), and adds two
  facts this seat did not test: no verifier globs `.ufo/waves/**`, and `repo_path_allowed` in the lane commit helper
  admits both the typo path and a correct `.ufo/waves/...` path. **No conflict.** Scope note: E11's script sweeps only
  the fleet root (`git -C /home/vgpnk/Projects/shokunin status --porcelain`); the *committed* lane-internal typo root is
  outside its remit, which is why the draft's check1 operates on the lane tree.
- The draft's `S01Reopen1`/`S02Reopen2` slots are deliberately unfilled (the seat assignment says to leave them).
  The artifacts that fill them exist and were read for consistency only:
  `.ufo/waves/round-77/build/S01Reopen1.access-record.txt` and `.ufo/waves/round-77/w1/S02Reopen2.md`; both report
  the optimizing-descriptions digest `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, equal to
  the r76 MANIFEST pin. This seat did not fetch the page, so their results are not absorbed into the draft.
- Sibling build outputs (`E03R1Repair.*`, `E04R2Receipt.*`, `E05R3R4Repair.*`, `E06EntryVerify.*`, `E08SourcesUsedBy.*`,
  `E10GateRepair.*`) are in flight in the same build dir; none is scored here and none is cited as a claim result.

## 6. Hygiene

- No claim data written: no knowledge entry, no `SKILL.md` row, no registry cell, no lesson row in `corpus/`; the
  draft lives only under `.ufo/waves/round-77/build/` (the freeze rule in `plans/round-77.md` § Freeze discipline).
- Counters untouched and byte-identical to the pins (F/§3). No `SKILL.md`, `SOURCES.md`, `QUALITY.md`, `README.md`,
  `LOG.md`, `SCORECARD.md` edit.
- No lane git/jj write; the only repository writes were commits inside the scratch clone. Read-only git only in the
  lane. Lane `git status --porcelain --untracked-files=no` → empty.
- Tools installed: none (no `uv`, `npx`, release binary, `cargo` or `npm` install; `pacman` never invoked).
- Concurrency: one scratch clone, no background jobs, at most one process at a time; no retry loop needed.
- Scratch `/fast/scratch/hyaku/kotoba-r77/SC02Lesson77` removed (`rm -rf --`, exit 0; `test -e` → 1). Nothing was
  written under `/tmp`.
- Wave-directory paths cited here (`.ufo/waves/round-77/…`) are uncommitted at 6523ace by design — the L1 integrates
  the wave after it settles; they exist in the worktree now and must be cited by their committing revision once they
  land (Q60). Every path this report cites outside `.ufo/waves/round-77/` exists at 6523ace.

## 7. Out of scope / open for the L1

1. Filling the 20 slots after claim data: census-after, S213 `used-by` new value, C1/C2 tip values, admits/rejects,
   the round's own mistake rows, the closure's Spot-check, and the r76-lesson landing status.
2. Deciding whether the r75 lesson's misroot row gets an appended correction beside C2 R1's correction in the same
   file (append-only; must not disturb R1).
3. Landing the restore+delete (E11's candidate commit) so that `plans/round-77.md`'s R76-D1 sentence becomes true of
   the tip, and recording which commit does it.
4. Whether the two proposed checks (lane-root allowlist, plan-promised-path existence) become verifiers: that needs a
   `SKILL.md` § Gate registry row, a floors row and their self-tests (Q35, Q48), so this seat only supplied the
   red-before/green-after evidence, not a landed gate.

VERDICT: Skeleton drafted with 20 single-line [[SLOT: …]] markers and the CD2/CD1 mistakes mined with captured-by after a shown grep, plus (1) the r77 base still carries both `kotoba-shokukin/` strays while `plans/round-77.md` claims R76-D1 removed — and the round-75 seat report exists only there, and (2) `corpus/lessons/round-76.md` is absent so C1 (a)/(e) cannot pass; both fixes carry red-before/green-after receipts on the same command (lane exit 1 → sandbox exit 0).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC02Lesson77.round-77.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC02Lesson77.red-before.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/SC02Lesson77.md
