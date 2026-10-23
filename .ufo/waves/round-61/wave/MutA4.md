# MutA4 — A4 snapshot provenance: the date clause is author-controlled; the landed alias conjunct rejects W1 under six frozen binding conditions plus the row-level fetch scan

Result: DONE — the assigned one-line mutant (earliest-introduction walk restricted to the snapshot path) **SURVIVED every frozen round-61 world and all four eligible rows**; the original date clause **passes the actual r60 W1** (measured on a read-only clone of the r60 sandbox), which is the evidence behind erratum **E2c** (`daf4ad7`); the landed A4(iv) full-sha alias conjunct **does reject W1** under the six binding conditions the L1 froze (`511aff7d`, `921c2512`) and the row-level fetch scan (`e2132443`), all of which this seat measured as seams. Detector restored byte-identically (`8ab93093…`, `cmp` clean).

Seat: `kotoba-r61-wave-MutA4`, mutation-tester, leaf (no subagent, no dispatch, no ask tool). Date: 2026-10-23. Axis: depth (C1 arm A4). Lane tip read at final measurement: `e213244323a732cd54d462d309843d0512e29e46` (E2c/E2d `daf4ad7`; conditions 1–4 `511aff7d`; conditions 5–6 `921c2512`; row-level scan `e2132443`); plan base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`; counter v2 `ca2585a4…`.

Bounds honoured: the lane, fleet, sibling repos, `.ufo/state` and the jj/git index were read-only; no git or jj mutation was issued against them. Every world, clone, commit and date injection lives under `/fast/scratch/hyaku/kotoba-r61/MutA4/` (untrusted; cited as a re-runnable location, never as evidence). The only lane write is this report. No install was needed or made.

---

## 0. Protocol block (the assigned mutation)

| field | value |
|---|---|
| mutant | one line in the A4 reference detector: the introduction walk `intro_commit(a.repo, a.mode, …)` becomes `intro_commit(a.repo, "path-author-utc", …)`, i.e. `git log --diff-filter=A -- <snapshot path>` instead of `git log --find-object=<blob>` over history. |
| expected detector | the v3 arm-killer world for A4 — a snapshot whose exact bytes were introduced earlier at another path — must reject under the pristine arm and pass under the mutant, so the self-test kills the mutant. |
| actual output | pristine: `W2-earlier-path … A4 reject … intro=ae7988c0af3c field=2026-10-22T20:04:43Z …` exit 1. mutant: `W2-earlier-path … A4 pass … intro=cdb85de4b4c6 field=2026-10-23T19:00:00Z …` exit 0. All other seven worlds identical between pristine and mutant. |
| verdict | **SURVIVED the frozen set.** The plan's seven worlds contain no earlier-path world; W1 is the only A4-satisfying world and the mutant returns the same verdict as the pristine arm on it. After E2c, W1 still rejects through A4(iv) regardless of the walk, so the mutant's survival is a **coverage gap on clause (iii)**, not a world kill. The fixture that kills it exists but is not frozen (draft F-A4-1 below). |
| restoration | `a4.py` restored from `a4.py.pristine`; `sha256sum` both `8ab93093ea0994b336e064bb398fcf11091f941b6482a74b5e199e139eaf64de`; `cmp -s` byte-identical; the two re-run verdicts (W0 pass, W2 reject) reproduce. |

Before/mutant/restored detector hashes:

```text
8ab93093ea0994b336e064bb398fcf11091f941b6482a74b5e199e139eaf64de  a4.py.pristine
2db852d97ff4cdfd842d72964149cf3ec5412915ea35955210b25346eca54788  a4.py   (M1, path walk)
8ab93093ea0994b336e064bb398fcf11091f941b6482a74b5e199e139eaf64de  a4.py   (restored)
```

Two further one-line mutations of the same clause were measured with the same worlds (§4): committer date instead of author date (`f6b2fe82…`) and local date-string compare instead of UTC instant (`5ab3dd19…`). Both also survive the frozen set.

---

## 1. Ground: the arm changed under the probe

The plan's original A4 sentence (`plans/round-61.md`, still the base text):

> **A4 snapshot provenance** — the row's recorded sha256 must equal the committed snapshot bytes, the located quote must occur verbatim in them, and the earliest commit introducing those bytes must be no older than the row's recorded open date (rejects recycled bytes: W1, round-53 scratch under a fresh-fetch claim). Limit, declared before data: the arm authenticates internal provenance consistency of committed bytes; it cannot authenticate wall-clock fetch time against author-forged commit dates.

Mid-probe the L1 landed **E2c** at `daf4ad7` (`plans/round-61.md` addendum, 2026-10-23T19:22:09Z), extending A4 after the measurements in §6:

> **A4 (extended)** — four conjuncts: (i) the row's recorded sha256 equals the committed snapshot bytes; (ii) the located quote occurs verbatim in them; (iii) the earliest commit introducing the blob is no older than the row's recorded opened date — CONSISTENCY ONLY, not acquisition authentication (CriticA4Limit's demonstrated bound: backdated commit objects pass); (iv) NEW — the row's full 64-hex snapshot sha256 must not already be recorded in the base-revision SOURCES table, unless the row's teaches cell declares byte-identity via `supersedes S###` (the S110 precedent for honest byte-identical corrections). W1's forged S103 row pins sha `971d75bf…` in full, which base row S043 also records in full → A4(iv) rejects; the four eligible rows alias their bases only by 8-hex prefix → pass (MutA4's measured discriminator).

So this report has two parts: the probe of the original date clause (§3–§6), and the probe of the landed alias conjunct (§7). Both are A4.

Pinned values read from the committed v2 counter (no v3 source exists at the tip; the counter is still `ca2585a4…` with no history code):

```text
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && grep -n "^SNAPSHOT_DIR\|^TARGET\|^OPENED\|^BASE" verifiers/check_scoped_rules.py
243:BASE = "31092dc6f875370bddd6eb1e4da4ca0d210c56af"
248:SNAPSHOT_DIR = ".ufo/waves/round-60/snapshots"
249:TARGET = 3
254:OPENED = ("2026-10-23",)
```

Consequences:

1. **`opened` is not per-row data.** `OPENED = ("2026-10-23",)`; every counted row's opened cell is that day. The date clause compares every introduction against the same instant.
2. **There is no introduction walk in v2.** The committed snapshot block is existence + sha256 pin + quote + key/action line checks (`verifiers/check_scoped_rules.py:1068–1096`). Clause (iii) is new v3 code.
3. **v2 self-test worlds are built with plain `git commit`** and no date environment (`verifiers/check_scoped_rules.py:2256`, `:2269`), so every introducing commit is stamped "now"; the base commit contains only the SOURCES header (`:2252–2259`). Both facts matter in §7.
4. **Git object ids are SHA-1; rows pin SHA-256.** Passing a row sha256 to `--find-object` fails:

```text
$ git log --all --find-object=971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff
error: unable to resolve '971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff'
```

Map the path to its blob at the measured revision (`git rev-parse <rev>:<path>`) first. Scope the walk to ancestors of `<rev>` (`git log <rev> --find-object=<blob>`), not `--all`: an unrelated branch holding a copy would otherwise reject the measured revision.

What is **not** run: no v3 counter exists at the tip, so every verdict is an **A4-spec projection measured on a reference implementation**, not the frozen CLI's output. `ExecWorldFixtures` had not landed a report at write time; the frozen worlds are read from the plan. No live fetch was made.

Independent corroboration (not my evidence): `MutWorldW1.md` §8 and `CriticA4Limit.md` reached the same "W1 passes, dates are not authentication" conclusion by different instruments; E2c cites both. My additions are the per-path/field/timezone mutants, the alias-rule matrix and its six frozen conditions + row-level scan, the excerpt/context measurements, and the base-revision self-alias fact.

---

## 2. The reference detectors and probe worlds

`a4.py` (144 lines, scratch path `/fast/scratch/hyaku/kotoba-r61/MutA4/a4.py`, full source §10) implements the original three conjuncts with selectable realisations of the third:

- `blob-author-utc` — earliest commit adding the **blob** anywhere (`git log --all --reverse --find-object=<blob>`), **author** date (`%aI`), compared as a **UTC instant** against `<opened>T00:00:00+00:00` (intended);
- `path-author-utc` — earliest commit adding the **file at the snapshot path** (`--diff-filter=A -- <path>`) (M1);
- `blob-committer-utc` — **committer** date (`%cI`) (M2);
- `blob-author-local` — raw `YYYY-MM-DD` **string compare** of the local-offset field (M3).

`a4iv.py` (scratch path `…/MutA4/a4iv.py`) models the landed A4(iv): read the base table, collect each row's full 64-hex sha, compare with the counted row's sha, and require a `supersedes S###` declaration either anywhere in the teaches cell (`unanchored`) or at its start (`anchored`).

Nine date-clause worlds were built with real git commits (`build_worlds.sh`; build `date -u` `Fri 23 Oct 2026 07:14:50 PM UTC`, exit 0). All use row id `S103`, path `.ufo/waves/round-60/snapshots/S103.page`, the same quote, `opened = 2026-10-23`.

| world | construction | snapshot sha256 (12) | bytes |
|---|---|---|---|
| W0-fresh | today's r60 page, one fresh commit | `82d603413549` | 54,043 |
| W1a-recycled-fresh | r53 scratch page committed **fresh** (the actual r60 W1 shape) | `971d75bfce7a` | 51,971 |
| W1b-recycled-backdated | same bytes, both commit dates 2026-10-22T20:04:43Z | `971d75bfce7a` | 51,971 |
| W2-earlier-path | same bytes at `archive/S043.page` on 10-22, copied to the snapshot path on 10-23 | `971d75bfce7a` | 51,971 |
| W3-excerpt | 5-line quote-carrying excerpt, fresh commit | `d4ce3358505e` | 152 |
| W4-straddle | fresh page, author 10-22T20:00Z, committer 10-23T19:00Z | `82d603413549` | 54,043 |
| W5-tz-utc23 | fresh page, author `2026-10-22T22:30:00-03:00` (UTC 10-23T01:30Z) | `82d603413549` | 54,043 |
| W6-tz-utc22 | fresh page, author `2026-10-23T00:30:00+03:00` (UTC 10-22T21:30Z) | `82d603413549` | 54,043 |
| W7-perturbed-newline | W2's bytes plus one appended `\n` | `7162fe79ef98` | 51,972 |

Ten alias/seam worlds (`build_alias_worlds.sh` at 19:25:47Z, `build_alias_seams.sh` at 19:29:19Z, fetch-claim worlds at 19:31:04Z; all exit 0) hold a base commit and a measured commit; §7.

---

## 3. Pristine matrix (original date clause)

Receipt `/fast/scratch/hyaku/kotoba-r61/MutA4/receipts/matrix-pristine.txt` (written 2026-10-23 19:15:11Z). Intended-mode lines:

```text
W0-fresh                 rc=0 A4 pass worlds/W0-fresh mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=81453f584932 field=2026-10-23T19:00:00Z basis=utc-instant 2026-10-23T19:00:00+00:00 >= 2026-10-23T00:00:00+00:00
W1a-recycled-fresh       rc=0 A4 pass worlds/W1a-recycled-fresh mode=blob-author-utc status=mined opened=2026-10-23 blob=bbb7d6f4e735 intro=c70e1de3891e field=2026-10-23T19:00:00Z basis=utc-instant 2026-10-23T19:00:00+00:00 >= 2026-10-23T00:00:00+00:00
W1b-recycled-backdated   rc=1 A4 reject worlds/W1b-recycled-backdated mode=blob-author-utc status=mined opened=2026-10-23 blob=bbb7d6f4e735 intro=e38ef94df93c field=2026-10-22T20:04:43Z basis=utc-instant 2026-10-22T20:04:43+00:00 >= 2026-10-23T00:00:00+00:00
W2-earlier-path          rc=1 A4 reject worlds/W2-earlier-path mode=blob-author-utc status=mined opened=2026-10-23 blob=bbb7d6f4e735 intro=ae7988c0af3c field=2026-10-22T20:04:43Z basis=utc-instant 2026-10-22T20:04:43+00:00 >= 2026-10-23T00:00:00+00:00
W3-excerpt               rc=0 A4 pass worlds/W3-excerpt mode=blob-author-utc status=mined opened=2026-10-23 blob=4a9afff70bfb intro=984c9045c106 field=2026-10-23T19:00:00Z basis=utc-instant 2026-10-23T19:00:00+00:00 >= 2026-10-23T00:00:00+00:00
W4-straddle              rc=1 A4 reject worlds/W4-straddle mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=5a5edfffad7c field=2026-10-22T20:00:00Z basis=utc-instant 2026-10-22T20:00:00+00:00 >= 2026-10-23T00:00:00+00:00
W5-tz-utc23              rc=0 A4 pass worlds/W5-tz-utc23 mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=714971f244ba field=2026-10-22T22:30:00-03:00 basis=utc-instant 2026-10-23T01:30:00+00:00 >= 2026-10-23T00:00:00+00:00
W6-tz-utc22              rc=1 A4 reject worlds/W6-tz-utc22 mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=50921b3d8192 field=2026-10-23T00:30:00+03:00 basis=utc-instant 2026-10-22T21:30:00+00:00 >= 2026-10-23T00:00:00+00:00
```

Mode table (P = pass/exit 0, R = reject/exit 1):

| world | M0 blob+author+UTC (intended) | M1 path walk | M2 committer | M3 local string |
|---|---|---|---|---|
| W0-fresh | P | P | P | P |
| W1a-recycled-fresh | **P** | **P** | **P** | **P** |
| W1b-recycled-backdated | R | R | R | R |
| W2-earlier-path | R | **P** | R | R |
| W3-excerpt | **P** | **P** | **P** | **P** |
| W4-straddle | R | R | **P** | R |
| W5-tz-utc23 | P | P | P | **R** |
| W6-tz-utc22 | R | R | R | **P** |
| W7-perturbed-newline | **P** | **P** | not run | not run |

Bold cells are the only deltas. W7: one appended newline changes the blob, so `--find-object` finds only the fresh commit and the per-blob arm passes recycled content.

---

## 4. Mutation results (date clause)

Each mutant is a single-line change to the intended clause; each ran over the eight worlds (W0, W1a, W1b, W2–W6) with `--mode blob-author-utc`; each was reverted from `a4.py.pristine`.

| mutant | one-line change | hash | deltas vs pristine | frozen-world kill? |
|---|---|---|---|---|
| M1 path walk | `a.mode` → `"path-author-utc"` in `intro_commit` | `2db852d9…` | W2 R→P; all others same | **none** |
| M2 committer date | `fmt = "%cI"` unconditionally | `f6b2fe82…` | W4 R→P; all others same | **none** |
| M3 local string | `if True:` in `verdict` (local-date branch) | `5ab3dd19…` | W5 P→R, W6 R→P; all others same | **none** |

M2 receipt (written 19:20:21Z):

```text
W4-straddle              rc=0 A4 pass worlds/W4-straddle mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=5a5edfffad7c field=2026-10-23T19:00:00Z basis=utc-instant 2026-10-23T19:00:00+00:00 >= 2026-10-23T00:00:00+00:00
```

M3 receipts (written 19:20:27Z):

```text
W5-tz-utc23              rc=1 A4 reject worlds/W5-tz-utc23 mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=714971f244ba field=2026-10-22T22:30:00-03:00 basis=local-date-string 2026-10-22 >= 2026-10-23
W6-tz-utc22              rc=0 A4 pass worlds/W6-tz-utc22 mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=50921b3d8192 field=2026-10-23T00:30:00+03:00 basis=local-date-string 2026-10-23 >= 2026-10-23
```

Why none is killed by the frozen set: the plan's A4-relevant world is W1 alone. W2–W4 are rejected before A4 by the prefix/held-key conjuncts; W5/W6 by A1/A2; W7 is a rescore world. W1 and the four eligible rows all have introductions on `2026-10-23` (local and UTC), so M0–M3 return the same verdict on every input the frozen set can present to clause (iii). After E2c, W1 still rejects through A4(iv), so these mutants do not change any world verdict — they are **unobservable** in the self-test.

---

## 5. The five bypasses of the original date clause: expected verdict, measured result, guard

### 5.1 Backdated commit dates on the introducing commit

**Attack.** Commit the recycled bytes with `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` set to any value, or commit them fresh. The arm reads a field the committer chooses.

**Expected under A4 as worded.** BYPASS. Fresh dates (the actual r60 W1) pass; the arm rejects only when the author volunteers an older date. The declared limit names forged dates, but the sharper point is that **a W1 fixture must backdate to make the arm fire** — the observed attack did not.

**Measured.** W1a pass, W1b reject (same bytes). The fields are independent and both user-set:

```text
$ git show -s --format='   author=%aI committer=%cI' HEAD
1) --date only:
   author=2026-10-22T20:00:00Z committer=2026-10-23T19:20:00Z
2) after --amend --no-edit (no content change):
   author=2026-10-22T20:00:00Z committer=2026-10-23T16:16:46-03:00
3) both fields set explicitly:
   author=2026-10-22T20:00:00Z committer=2026-10-23T19:30:00Z
```

(`date -u`: `Fri 23 Oct 2026 07:16:46 PM UTC`; scratch repo `/fast/scratch/hyaku/kotoba-r61/MutA4/field-demo`.)

**Guard.** None inside git metadata. E2c correctly demotes clause (iii) to consistency-only and carries the rejection on A4(iv). Do not let a backdated fixture stand as evidence that the date clause authenticates acquisition.

### 5.2 Same bytes introduced earlier under a DIFFERENT path (per-path vs per-blob)

**Attack.** Introduce the bytes at path A on day D-1, copy them to the snapshot path on day D. A per-path walk sees only the copy; a per-blob walk sees the earlier introduction.

**Expected.** Per-path: BYPASS. Per-blob: KILL within the measured repository's history. Neither walk sees bytes never committed (external scratch) — W1.

**Measured.** W2: intended reject (`intro=…` at `2026-10-22T20:04:43Z`), M1 pass (`intro=…` at `2026-10-23T19:00:00Z`). W7: one appended newline defeats even the per-blob walk. External bytes: §6 proves the actual W1 passes.

**Guard.** `git rev-parse <rev>:<path>` → blob id; `git log <rev> --reverse --find-object=<blob>`; first commit. Limits: exact-byte identity (W7), no external history, and honest byte-identical re-opens need the declaration path (S110). Add F-A4-1 as the clause-(iii) arm-killer if the clause stays; otherwise mark it untested.

### 5.3 Quote-only shaping vs byte shaping

**Attack.** Commit a small synthetic excerpt that contains the quote and pins its own sha256. All three original conjuncts hold; the "snapshot" is not a page. A4(iv) is untouched by this attack (the bytes are new), so the excerpt still passes the extended arm unless the excerpt's sha aliases a base row.

**Expected.** BYPASS as worded.

**Measured.** W3 pass under every mode (`152 B`, sha `d4ce3358…`). Real-drift control: the r53 page's ±2-line block around the quote (411 B) still occurs verbatim in today's r60 page, while the excerpt's block does not; size ratios to the live page are 0.962 (real page) vs 0.0028 (excerpt):

```text
old-page lines=638 bytes=51971 context_block_bytes=411 block_in_live=True
excerpt  lines=5 bytes=152 context_block_bytes=151 block_in_live=False
size ratios vs live(54043 B): old=0.962 excerpt=0.0028
excerpt sha256 d4ce3358505efef3a79fec072c1700cc95a6406aac3282b7ffafa4e64d630b6c
```

**Guard.** In `--fetch` mode, require the committed snapshot's quote context (quote line plus the nearest non-empty lines each side, under the counter's existing page normalisation) to occur in the live page **and** `len(snapshot) >= 0.25 * len(live)`; offline, a byte floor (e.g. 2 KiB) and a minimum of non-empty context lines each side. This rejects W3 and passes the drifted real page, but not W1. Declared limit: a genuine contiguous excerpt copied from the live page passes; Q56 keeps "byte-exact" reserved.

### 5.4 Snapshot in the same changeset but authored before the row's opened date

**Attack / ambiguity.** One commit carries both the row and the snapshot; its author date precedes the opened date while its committer date does not (rebase, amend, jj operation timestamp). The field the arm reads decides the verdict.

**Expected.** Author-date reading: REJECT (W4). Committer-date reading: PASS (M2) — a bypass. The frozen sentence does not name the field.

**Measured.** W4: M0 reject (`field=2026-10-22T20:00:00Z`), M2 pass (`field=2026-10-23T19:00:00Z`). An honest fetch on 10-22 for a row opened 10-23 is also rejected by the author reading, so the field choice is a contract decision.

**Guard.** Pin the author date and a straddle fixture (F-A4-4), or leave clause (iii) consistency-only (E2c's choice) and do not reject on it.

### 5.5 Timezone edge on the date comparison

**Attack.** Choose a commit offset that straddles midnight. `2026-10-22T22:30:00-03:00` is `2026-10-23T01:30Z`; `2026-10-23T00:30:00+03:00` is `2026-10-22T21:30Z`. A raw `YYYY-MM-DD` compare and a UTC-instant compare disagree on both.

**Expected.** Implementation-dependent: local-string flips verdicts both ways. Not hypothetical: **76 commits** in the lane have a local date different from their UTC date, including boundary commits such as `2026-10-22T23:52:55-03:00` (= `2026-10-23T02:52:55Z`).

**Measured.** W5: M0 pass / M3 reject. W6: M0 reject / M3 pass.

**Guard.** Parse offsets (`datetime.fromisoformat`) and compare UTC instants against `<opened>T00:00:00+00:00`; pin F-A4-5/F-A4-6 if the clause stays. Document the day-granularity cliff.

---

## 6. Why E2c exists: the actual W1 passes the date clause

The original sentence says A4 "rejects recycled bytes: W1, round-53 scratch under a fresh-fetch claim". The r60 W1 (`CtlReopenForged d`) copied round-53 scratch bytes into fresh snapshots and committed them **that day**. A read-only clone of the r60 sandbox preserves the actual commits:

```text
$ git clone -q /fast/scratch/hyaku/kotoba-r60/CtlReopenForged w1-actual && cd w1-actual
$ git log --format='%h a=%aI c=%cI %s' -n 3 7f05968
7f05968 a=2026-10-23T09:08:42-03:00 c=2026-10-23T09:08:42-03:00 round60 CtlReopenForged d-copied-base-snapshots
358e43d a=2026-10-23T09:08:02-03:00 c=2026-10-23T09:08:02-03:00 round60 CtlReopenForged c-nonbase-id
76e1661 a=2026-10-23T09:07:50-03:00 c=2026-10-23T09:07:50-03:00 round60 CtlReopenForged b-wrong-base-id
```

First introduction of each W1 snapshot blob in that repository (read-only loop):

```text
.ufo/waves/round-60/snapshots/S103.page blob=bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b intro=7f05968a085ddf9fb9155b0a1047808d616b7b1b a=2026-10-23T09:08:42-03:00 c=2026-10-23T09:08:42-03:00
.ufo/waves/round-60/snapshots/S104.page blob=56a6ad07c0eec9583847973af7b903a34e4f143f intro=18afb8135ad4f95450f584b07b90b373190417c6 a=2026-10-23T09:07:17-03:00 c=2026-10-23T09:07:17-03:00
.ufo/waves/round-60/snapshots/S105.page blob=47c1554d6fb3be35e292f7dd525d3241fd2ff21e intro=18afb8135ad4f95450f584b07b90b373190417c6 a=2026-10-23T09:07:17-03:00 c=2026-10-23T09:07:17-03:00
```

The recycled S103 blob (`bbb7d6f4…`, sha256 `971d75bf…`) first enters the sandbox history in the W1 commit itself. The S104/S105 bytes are byte-identical to the pristine pages (the pages did not change between r53 and r60), so their first introduction is the pristine commit `18afb81` — also the open day. Reference-detector runs on the actual trees:

```text
$ python3 -B a4.py --repo . --mode blob-author-utc --id S103 --path .ufo/waves/round-60/snapshots/S103.page --quote-file quote.txt
A4 pass . mode=blob-author-utc status=mined opened=2026-10-23 blob=bbb7d6f4e735 intro=7f05968a085d field=2026-10-23T09:08:42-03:00 basis=utc-instant 2026-10-23T12:08:42+00:00 >= 2026-10-23T00:00:00+00:00
exit 0

$ git checkout -q 18afb81 && python3 -B ../a4.py --repo . --mode blob-author-utc --id S103 --path .ufo/waves/round-60/snapshots/S103.page --quote-file quote.txt
A4 pass . mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=18afb8135ad4 field=2026-10-23T09:07:17-03:00 basis=utc-instant 2026-10-23T12:07:17+00:00 >= 2026-10-23T00:00:00+00:00
exit 0
```

(`date -u` immediately before this block: `Fri 23 Oct 2026 07:16:04 PM UTC`; the clone and checkouts live in my scratch.)

The r53 scratch bytes were never committed: the old memory body `bbb7d6f4` is absent from the lane object database (`git hash-object` + `git cat-file -e`), while the Copilot/Cursor bodies `56a6ad07`/`47c1554d` are present only as the legitimate r60 snapshot blobs. No walk — per-path or per-blob — finds an older introduction for W1.

**Consequence.** A v3 self-test built the way v2's is (`git init` + plain `git commit`, no date environment) stamps W1's introduction "now", so W1 passes clause (iii) and `--self-test` cannot print `worlds reject 7 of 7` on the date clause. That is exactly what E2c fixed by adding A4(iv). A W1 fixture backdated to 2026-10-22 would reject — but it encodes the date the arm is supposed to detect, and the actual r60 W1 still survives clause (iii).

---

## 7. The landed A4(iv) alias conjunct: measured behaviour, six frozen conditions, row-level fetch scan

A4(iv) compares the counted row's full 64-hex sha256 with the **base-revision SOURCES table**. Measured facts:

```text
S103 sha 82d60341 full_aliases [] prefix_aliases []
S105 sha a45c9e9f full_aliases [] prefix_aliases []
S106 sha 00e45ea5 full_aliases [] prefix_aliases ['S048']
S108 sha 884c67ca full_aliases [] prefix_aliases ['S049']
base row sha forms:
  S043 full True prefix None
  S048 full False prefix 00e45ea5
  S049 full False prefix 884c67ca
base opened dates: S043/S048/S049 = 2026-10-22; S103/S105/S106/S108 = 2026-10-23
```

The alias row S043 carries the full sha `971d75bf…` at **both** candidate bases (`31092dc6`, the counter's `BASE`; `f3246d14`, the plan base), verified with `git show <rev>:corpus/SOURCES.md | grep '^| S043 '`. The four eligible rows have no full-sha alias, so the rule passes them and rejects W1's S103 — **conditionally**, as the ten alias/seam worlds show.

Alias matrix (receipt `…/receipts/alias-matrix.txt`, run 2026-10-23T19:25:50Z; base = `HEAD^` in each world):

```text
A0-alias-in-base           unanchored rc=1 A4iv reject S103: sha 971d75bfce7a is byte-identical to S043 (base table); teaches does not declare byte-identity
A0-alias-in-base           anchored   rc=1 A4iv reject S103: sha 971d75bfce7a is byte-identical to S043 (base table); teaches does not declare byte-identity
A1-alias-in-measured       unanchored rc=0 A4iv pass S103: sha 971d75bfce7a not recorded in the base table
A1-alias-in-measured       anchored   rc=0 A4iv pass S103: sha 971d75bfce7a not recorded in the base table
A2-declaration-appended    unanchored rc=0 A4iv pass S103: sha 971d75bfce7a aliases S043; teaches declares byte-identity
A2-declaration-appended    anchored   rc=1 A4iv reject S103: sha 971d75bfce7a is byte-identical to S043 (base table); teaches does not declare byte-identity
A3-declaration-replaces    unanchored rc=0 A4iv pass S103: sha 971d75bfce7a aliases S043; teaches declares byte-identity
A3-declaration-replaces    anchored   rc=0 A4iv pass S103: sha 971d75bfce7a aliases S043; teaches declares byte-identity
A4-prefix-control          unanchored rc=0 A4iv pass S103: sha 00e45ea5be05 not recorded in the base table
A4-prefix-control          anchored   rc=0 A4iv pass S103: sha 00e45ea5be05 not recorded in the base table
A5-unrelated               unanchored rc=0 A4iv pass S103: sha 82d603413549 not recorded in the base table
A5-unrelated               anchored   rc=0 A4iv pass S103: sha 82d603413549 not recorded in the base table
```

Reading it:

- **A0** is the intended kill: alias recorded in the base table, no declaration → reject. W1's actual S103 row says `re-opens S043 — …`, no `supersedes`, so W1 rejects through A4(iv). Good.
- **A1 same-changeset gap (BYPASS):** if the alias row is added in the **measured** commit, the base-table scan cannot see it → pass. This is the shape v2's self-test uses (base commit is header-only, all rows in the measured commit); a W1 fixture built that way is vacuous.
- **A2 declaration appended (BYPASS under unanchored matching):** `re-opens S043 — Scope rules frontmatter; supersedes S043` keeps A3's reopen prefix and satisfies an unanchored `supersedes` search → pass. Four words defeat the W1 kill. Under anchored matching it rejects, but then a counted row cannot also carry `re-opens` (A3 would reject it) — the seam A3×A4(iv) must be decided.
- **A3 declaration replaces:** passes A4(iv), but the row no longer starts with `re-opens`, so A3 rejects it before counting. Not a viable bypass.
- **A4 prefix control:** base records only `00e45ea5…`; the counted row's full sha is not "already recorded in full" → pass. This is why the four eligible rows pass; it is also the blind spot for pages that did not change (S106/S108).
- **A5 control:** different bytes → pass.

### 7.1 Condition: base revision and self-alias (measured failure)

A literal A4(iv) with base = the plan base `f3246d14` rejects every eligible row **against itself**: the counted rows already exist at that revision with the same full sha, and the erratum does not state a self-exclusion. Measured in a one-commit self-alias world:

```text
$ python3 -B a4iv.py --repo worlds-alias/A6-self-alias --base HEAD --id S103 --declaration unanchored
A4iv reject S103: sha 82d603413549 is byte-identical to S103 (base table); teaches does not declare byte-identity
rc=1
```

Lane fact behind it:

```text
$ git show f3246d14:corpus/SOURCES.md | grep -E '^\| S103 ' | grep -oE 'sha256 .{64}' | head -1
sha256 `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e
$ git show eb5e149:corpus/SOURCES.md | grep -E '^\| S103 ' | grep -oE 'sha256 .{64}' | head -1
sha256 `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e
```

**Frozen fix (condition 1):** use the counter's `BASE = 31092dc6` (S103–S111 absent there) **and** exclude the counted row's own id unconditionally. Both are required for robustness; either alone is fragile (a re-measure at a revision where the row existed at base would self-reject).

### 7.2 The six frozen binding conditions, and the row-level fetch scan

The L1 froze conditions (1)–(4) at `511aff7d` and (5)–(6) at `921c2512`. A4(iv) rejects W1 **iff all six hold** (quoting the plan's numbering):

1. the scan reads the SOURCES table at `BASE = 31092dc6`, where S103–S111 are absent and S043's full sha is present, **excluding the counted row's own id unconditionally** — a literal scan at the plan base `f3246d14` rejects every eligible row against itself (measured, §7.1);
2. the fixture's **base commit** contains the aliased row (S043's full-sha row); a header-only base commit lets W1 pass (measured A1);
3. the byte-identity declaration is **anchored at the teaches cell's start** (`supersedes S### —`), and a row carrying it is not counted as a fresh eligible row and must not also carry a fresh-fetch claim; an unanchored appended `supersedes` defeats the kill (measured A2);
4. the scan covers the **measured commit's table too** (self excluded), so a same-changeset alias cannot hide (verified: with base=`HEAD` on A1, the alias is found, rc=1);
5. the declared id must be a base-table row **whose recorded full sha equals the counted row's sha** — `supersedes S048 — …` while S048 records only a prefix passes a name-only check (measured A7) and must reject;
6. a declared byte-identity row must not carry a fresh-fetch assertion (`fetched <ISO>`), and the row is barred from fresh-fetch claims (measured A8: teaches-scan rejects).

Bypass baseline that motivated pins 5–6 (model before either pin; both pass, both must reject under the frozen rules):

```text
A7-declaration-wrong-row       anchored rc=0 A4iv pass S103: sha 971d75bfce7a aliases S043; teaches declares byte-identity
A8-declaration-with-fetch      anchored rc=0 A4iv pass S103: sha 971d75bfce7a aliases S043; teaches declares byte-identity
```

(receipt `…/receipts/alias-seams.txt`, run 19:29:19Z.)

Each was built and measured. None is killed by the plan's seven worlds as specified, because none of those worlds contains a second alias row or a declaration.

**Row-level fetch scan (seam 7, frozen at `e2132443`):** condition (6)'s first text scoped the fetch-claim check to "the declaration's teaches cell", while condition (3)'s text is row-level ("must not also carry a fresh-fetch claim"). A declared row whose fetch assertion sits one column over passes a teaches-only scan:

```text
A8-declaration-with-fetch  scan=none    rc=0 pass
A8-declaration-with-fetch  scan=teaches rc=1 reject "declared byte-identity row carries a fresh-fetch claim"
A8-declaration-with-fetch  scan=row     rc=1 reject
A9-fetch-in-anchor         scan=teaches rc=0 pass    <- claim in the ANCHOR cell
A9-fetch-in-anchor         scan=row     rc=1 reject
A10-fetch-in-scope         scan=teaches rc=0 pass    <- claim in the SCOPE cell
A10-fetch-in-scope         scan=row     rc=1 reject
```

(`date -u`: `Fri 23 Oct 2026 07:31:04 PM UTC`; receipt `…/receipts/fetch-claim-scope.txt`.) **Frozen at `e2132443`:** scan the whole parsed row (all 11 cells) for the fetch-claim shape, not just the teaches cell. This closed the cell-scope gap between (3)'s row-level wording and (6)'s teaches-cell wording. No eighth seam surfaced against the six conditions plus this scan; the residual gaps are the declared limits (exact-byte shaping W7, and base rows that record only prefixes, S106/S108).

---

## 8. Fixture drafts (for `ExecWorldFixtures` / `ExecSelftestArms`; target path none — self-test builders)

Each draft is a world-builder step in v2's self-test shape. "Expected line" is the reference arm's text; the frozen v3 wording may differ in phrasing, not verdict.

### F-A4-0 / F-A4-2 — the honest/backdated pair (pins the date clause's real scope)

Same recycled bytes, two worlds: fresh commit (F-A4-0, W1a) **passes** clause (iii); backdated commit `2026-10-22T20:04:43Z` (F-A4-2, W1b) **rejects**. Assert both and label the pair "date consistency, not acquisition". A lone backdated reject is not evidence of provenance authentication.

### F-A4-1 — earlier path (kills M1; clause-(iii) arm-killer)

```text
git init; mkdir archive .ufo/waves/round-60/snapshots
cp <recycled page, sha256 971d75bf…ff, 51971 B> archive/S043.page
GIT_AUTHOR_DATE=2026-10-22T20:04:43Z GIT_COMMITTER_DATE=2026-10-22T20:04:43Z git commit -m "archive"
cp archive/S043.page .ufo/waves/round-60/snapshots/S103.page
<row: sha256 971d75bf…ff, opened 2026-10-23>
GIT_AUTHOR_DATE=2026-10-23T19:00:00Z GIT_COMMITTER_DATE=2026-10-23T19:00:00Z git commit -m "snapshot"
```

Expected: `A4 reject … intro=<first> field=2026-10-22T20:04:43Z basis=utc-instant 2026-10-22T20:04:43+00:00 >= 2026-10-23T00:00:00+00:00`, exit 1; under M1 it passes. With A4(iv), the world also rejects through the alias rule if the base commit carries S043 — keep the alias row out of F-A4-1 so the reject line names clause (iii), or assert both lines.

### F-A4-3 — quote-carrying excerpt

```text
# Claude Code memory

For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.

See the rules page.
```

152 B, sha256 `d4ce3358…`; fresh commit. Under A4 as worded: pass (measured). With the §5.3 context+size guard: reject as a 152-byte excerpt (0.0028 of the 54,043-byte page), exit 1. If the guard is not adopted, record a documented limit.

### F-A4-4 — straddle (kills M2)

Fresh page, one commit, author `2026-10-22T20:00:00Z`, committer `2026-10-23T19:00:00Z`. Clause (iii) author reading rejects; M2 passes. E2c's consistency-only choice makes this a doc fixture, not a kill.

### F-A4-5 / F-A4-6 — timezone pair (kills M3)

- F-A4-5: `2026-10-22T22:30:00-03:00` (UTC 2026-10-23T01:30Z). Intended pass; M3 reject.
- F-A4-6: `2026-10-23T00:30:00+03:00` (UTC 2026-10-22T21:30Z). Intended reject; M3 pass.

### F-A4-7 / F-A4-8 / F-A4-9 — alias conjunct (the landed A4(iv); conditions 1–4)

- **F-A4-7 (kill):** base commit = header + S043 row (`sha256 971d75bf…ff`, opened 2026-10-22); measured commit = S103 row (`re-opens S043 — …`, sha `971d75bf…ff`, opened 2026-10-23) + snapshot. Expected: `A4(iv) reject S103: sha 971d75bf… is byte-identical to S043; teaches does not declare byte-identity`, exit 1. **This is the only shape that rejects W1 through A4(iv).**
- **F-A4-8 (same-changeset; condition 4):** base = header only; measured = S043 + S103 in one commit. Base-table-only passes (measured A1); the frozen measured-table scan (self excluded) rejects (verified with base=`HEAD`: `byte-identical to S043`, rc=1).
- **F-A4-9 (declaration anchoring; condition 3):** base F-A4-7, S103 teaches `re-opens S043 — …; supersedes S043`. Unanchored passes (measured A2); anchored rejects, and the frozen rule bars the declared row from the fresh count regardless. Assert reject.
- **Control:** base S048 with `sha256 `00e45ea5…`` prefix only; S106 full `00e45ea5…` → pass (measured A4-prefix-control). This is the eligibility-preserving control; a prefix-matching rule would false-reject S106/S108.

### F-A4-10 — self-alias control (must pass)

Base = the counted row itself with the same full sha (the f3246d14 shape); measured = the same row. A4(iv) must **pass**; a literal scan rejects (measured A6). This fixture pins the self-exclusion.

### F-A4-11 — declaration names the wrong row (condition 5)

Base = S043 (`971d75bf…ff`) + S048 (`sha256 `00e45ea5…`` prefix); measured = S103 with the recycled bytes and teaches `supersedes S048 — …`. A name-only anchored check passes (measured A7, rc=0); the frozen condition (5) must reject: `declared row S048 does not record the aliased sha`, exit 1.

### F-A4-12 — declared row keeps a fresh-fetch claim (condition 6 + row-level scan)

Base F-A4-7; measured S103 teaches `supersedes S043 — …; fetched 2026-10-23T12:06:23Z, HTTP 200`. A teaches-only scan rejects (A8); the frozen row-level scan must also reject when the claim is in the **anchor** (A9) or **scope** (A10) cell. Use the anchor placement as the fixture, so the row-level scope is pinned rather than the teaches cell.

### F-A4-13 — exact-byte shaping limit (declared, must stay a limit)

Base F-A4-7; measured S103 = the recycled bytes plus one appended `\n` (sha `7162fe79…`, W7). A4(iv) passes (no alias); this is the declared exact-byte limit, not a kill. If it is ever asserted as a reject, the fixture is lying about the rule.

---

## 9. Real-lane readings (read-only)

Four eligible r60 snapshots — first introduction, both dates, against `OPENED = 2026-10-23`:

```text
$ for s in S103 S105 S106 S108; do b=$(git rev-parse HEAD:.ufo/waves/round-60/snapshots/$s.page); c=$(git log --all --reverse --format=%H --find-object=$b | head -1); printf '%s blob=%s intro=%s a=%s c=%s\n' "$s" "$b" "$c" "$(git show -s --format=%aI $c)" "$(git show -s --format=%cI $c)"; done
S103 blob=022dc3bab2728a6525b78e4a02365d396f3682be intro=a8e359690bfd9974b67383a4314da69a42ae3a2e a=2026-10-23T09:28:13-03:00 c=2026-10-23T09:28:13-03:00
S105 blob=0400f45312eb5e0381b2d8c857c06712e0d2f18d intro=a8e359690bfd9974b67383a4314da69a42ae3a2e a=2026-10-23T09:28:13-03:00 c=2026-10-23T09:28:13-03:00
S106 blob=56a6ad07c0eec9583847973af7b903a34e4f143f intro=a8e359690bfd9974b67383a4314da69a42ae3a2e a=2026-10-23T09:28:13-03:00 c=2026-10-23T09:28:13-03:00
S108 blob=47c1554d6fb3be35e292f7dd525d3241fd2ff21e intro=a8e359690bfd9974b67383a4314da69a42ae3a2e a=2026-10-23T09:28:13-03:00 c=2026-10-23T09:28:13-03:00
```

(`date -u`: `Fri 23 Oct 2026 07:16:04 PM UTC`; exit 0. `a8e3596` is the empty-subject commit immediately before `7b80ae8`, both at 12:28:13Z.) All four pass the date reading; S106 is byte-identical to the page fetched the previous day — the unchanged-page case no date rule can distinguish from recycling, and precisely why A4(iv) keys on the base row's recorded sha rather than a clock.

Reference arm on the real eligible row:

```text
$ python3 -B a4.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --mode blob-author-utc --id S103 --path .ufo/waves/round-60/snapshots/S103.page --quote-file /fast/scratch/hyaku/kotoba-r61/MutA4/quote-claude.txt
A4 pass /home/vgpnk/Projects/shokunin/kotoba-shokunin mode=blob-author-utc status=mined opened=2026-10-23 blob=022dc3bab272 intro=a8e359690bfd field=2026-10-23T09:28:13-03:00 basis=utc-instant 2026-10-23T12:28:13+00:00 >= 2026-10-23T00:00:00+00:00
rc=0
```

The lane history spans 2026-09-28 … 2026-10-23 (39 commits on 09-28, 324 on 10-22, 199 on 10-23, etc.), and 76 commits have local ≠ UTC dates — the timezone edge in §5.5 is reachable in real history.

S096/S110: `.ufo/waves/round-59/snapshots/S096.page` (blob `0b393ac6…`, sha256 `c6ef9d21…`) was introduced at `ef4c371` on `2026-10-23T06:48:15-03:00`; S110's row declares `supersedes S096` and is the honest byte-identical precedent E2c cites. S096's opened date is the same day as S110's, so an opened-date comparison would not fire; the declaration form is what carries it.

---

## 10. Could not verify

- **No v3 source or CLI at the tip.** `verifiers/check_scoped_rules.py` is still v2 (`ca2585a4…`, no history code). Every A4/A4(iv) verdict is a projection on a reference detector; the frozen v3's actual output, self-test string, and reject-line wording are unmeasured. E2c is plan text, not code.
- **No frozen world fixtures.** `ExecWorldFixtures` had not published at write time; the seven worlds are read from the plan. If that seat adds an earlier-path, straddle, timezone, or alias-in-base world, the corresponding mutants are killed and this report's coverage finding is superseded (the drafts in §8 are such worlds).
- **No live fetch.** The "live page" in §5.3 is the r60 committed page (54,043 B), not a fresh HTTP response.
- **Quote checks for S105/S106/S108** were not re-run through the reference detector (only sha/date readings); their quote verdicts belong to the counter and its receipts.
- **Scratch is untrusted.** `/fast/scratch/hyaku/kotoba-r61/MutA4/` is re-runnable but is not evidence; the commands and outputs pasted here are the evidence.
- I ran no `jj` commands and no git write against the lane, the fleet, a sibling, or the r60 sandbox. The r60 sandbox was cloned; only the clone was checked out.

---

## 11. Appendix — reference detector source (`/fast/scratch/hyaku/kotoba-r61/MutA4/a4.py`, sha256 `8ab93093…`, 144 lines)

```python
#!/usr/bin/env python3
r"""Bounded reference detector for round-61 C1 arm A4 (snapshot provenance).

Scratch-only instrument.  It implements the arm as the plan words it:

    the row's recorded sha256 must equal the committed snapshot bytes,
    the located quote must occur verbatim in them, and the earliest commit
    introducing those bytes must be no older than the row's recorded open date.

Modes exist only to expose which field / which walk a realisation chose:

  blob-author-utc      earliest commit adding the BLOB (any path), author date,
                       compared as a UTC instant            <- intended A4
  path-author-utc      earliest commit adding the FILE at the snapshot path
                                                           <- mutant M1
  blob-committer-utc   earliest commit adding the BLOB, committer date
                                                           <- mutant M2
  blob-author-local    earliest commit adding the BLOB, author date, raw
                       YYYY-MM-DD prefix string compare     <- mutant M3

Exit: 0 pass, 1 reject, 2 environment error.  One line of output per run plus
the fields the verdict read, so a receipt can be re-derived by hand.
"""
import argparse
import datetime as dt
import hashlib
import os
import re
import subprocess
import sys

OPEN_DEFAULT = "2026-10-23"
SHA_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")


def git(repo, *argv, check=True):
    p = subprocess.run(["git", "--no-optional-locks", "-C", repo] + list(argv),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and p.returncode != 0:
        sys.stderr.write("git %s failed: %s\n" % (" ".join(argv), p.stderr.strip()))
        raise SystemExit(2)
    return p


def row_fields(repo, sid):
    """The SOURCES row of `sid`, split on the table pipe; field 9 is `opened`."""
    text = git(repo, "show", "HEAD:corpus/SOURCES.md").stdout
    for line in text.splitlines():
        if not line.startswith("| " + sid + " |"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 12:
            raise SystemExit(2)
        return parts
    sys.stderr.write("no SOURCES row %s\n" % sid)
    raise SystemExit(2)


def snapshot_bytes(repo, path):
    """Committed bytes of `path` at HEAD, plus the blob id git assigned them."""
    blob = git(repo, "rev-parse", "HEAD:" + path).stdout.strip()
    data = subprocess.run(["git", "--no-optional-locks", "-C", repo, "cat-file",
                           "blob", blob], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout
    return blob, data


def intro_commit(repo, mode, path, blob):
    """First commit, oldest first, that introduces the bytes under `mode`'s walk."""
    if mode.startswith("path-"):
        p = git(repo, "log", "--all", "--reverse", "--diff-filter=A",
                "--format=%H", "--", path)
    else:
        p = git(repo, "log", "--all", "--reverse", "--format=%H",
                "--find-object=" + blob)
    commits = [c for c in p.stdout.split() if c]
    if not commits:
        # Bytes exist nowhere in history: nothing introduced them.  A4 cannot
        # date an introduction it cannot find; treat as an environment miss.
        sys.stderr.write("no introducing commit found for %s\n" % blob)
        raise SystemExit(2)
    return commits[0]


def date_field(repo, commit, mode):
    fmt = "%cI" if mode.startswith("blob-committer") else "%aI"
    return git(repo, "show", "-s", "--format=" + fmt, commit).stdout.strip()


def verdict(mode, field, opened):
    if mode.endswith("-local"):
        ok = field[:10] >= opened
        basis = "local-date-string %s >= %s" % (field[:10], opened)
    else:
        instant = dt.datetime.fromisoformat(field)
        open_instant = dt.datetime.fromisoformat(opened + "T00:00:00+00:00")
        ok = instant >= open_instant
        basis = "utc-instant %s >= %s" % (instant.astimezone(dt.timezone.utc)
                                          .isoformat(), open_instant.isoformat())
    return ok, basis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--mode", required=True,
                    choices=["blob-author-utc", "path-author-utc",
                             "blob-committer-utc", "blob-author-local"])
    ap.add_argument("--id", default="S103")
    ap.add_argument("--path", default=".ufo/waves/round-60/snapshots/S103.page")
    ap.add_argument("--quote-file", default="quote.txt")
    ap.add_argument("--opened", default=None)
    a = ap.parse_args()

    parts = row_fields(a.repo, a.id)
    status, opened = parts[8], (a.opened or parts[9])
    m = SHA_RE.search("|".join(parts))
    if not m:
        print("A4 reject %s: row prints no full 64-hex sha256" % a.repo)
        return 1
    pinned = m.group(1).lower()

    blob, data = snapshot_bytes(a.repo, a.path)
    got = hashlib.sha256(data).hexdigest()
    if got != pinned:
        print("A4 reject %s: sha256 mismatch %s != row %s" % (a.repo, got[:12], pinned[:12]))
        return 1

    quote = open(os.path.join(a.repo, a.quote_file), "rb").read().strip()
    if quote not in data:
        print("A4 reject %s: quote does not occur in snapshot bytes" % a.repo)
        return 1

    commit = intro_commit(a.repo, a.mode, a.path, blob)
    field = date_field(a.repo, commit, a.mode)
    ok, basis = verdict(a.mode, field, opened)
    print("A4 %s %s mode=%s status=%s opened=%s blob=%s intro=%s field=%s basis=%s"
          % ("pass" if ok else "reject", a.repo, a.mode, status, opened,
             blob[:12], commit[:12], field, basis))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
```

The A4(iv) model (`a4iv.py`, 82 lines) is the same shape with a base-table scan and the `supersedes` declaration modes described in §2 and §7; its full text is at the scratch path if the L1 wants it verbatim.

---

Installs: no installs.
Blockers: none — all six A4(iv) conditions and the row-level fetch scan are frozen in the plan (`511aff7d`, `921c2512`, `e2132443`), each backed by a receipt here; the date clause (iii) remains consistency-only, and its self-test must not rest on a backdated fixture (F-A4-0/F-A4-2 pair). Residual, declared limits: exact-byte shaping escapes A4(iv) (W7), and base rows that record only prefixes leave unchanged-page recycling undetectable (S106/S108).
Attacked: A4 snapshot provenance — per-path vs per-blob introduction, author/committer date forgery, local-vs-UTC comparison, quote-carrying excerpts, the actual r60 W1 world, and the landed A4(iv) alias conjunct (base revision, self-alias, declaration anchoring, same-changeset scope, named-row binding, fetch-claim scope); produced the surviving-mutant matrix, five date-clause bypass verdicts with guards, the alias/seam matrices, and the full self-test fixture set (F-A4-0 through F-A4-13).
