# ScribeCorpusR99 — round 99 (r99-w1) — report

Seat: **ScribeCorpusR99** (scribe, r99-w1). Lane: kotoba-shokunin. Date: 2026-11-06 (UTC).
Files owned and written: `corpus/SOURCES.md` (the S281 row only) and `corpus/lessons/round-99.md`
(new). Nothing else in the lane was touched; no git write in the lane; the only repo the seat wrote
to is its own scratch clone under `/fast/scratch/hyaku/kotoba-r99/ScribeCorpusR99/`.

---

## 1. What landed

**`corpus/SOURCES.md` — one appended row, `S281`** (206 → 207 rows; no other row touched).

| field | value |
|---|---|
| id | `S281` (next unused; the registry's highest is `S280`) |
| source | Python documentation — argparse — `https://docs.python.org/release/3.15.2/library/argparse.html` |
| kind / tier / status | `docs` / `A` / `mined` |
| opened / recheck | 2026-11-06 / `180d` |
| used-by | `corpus/lessons/round-99.md,plans/round-99.md` |
| scope | what argparse's `action='append'` does to a repeatable option's values — each occurrence appends its value to a list, so `--check dispatch.04` leaves `args.check` holding exactly `['dispatch.04']` — the option semantics alone, not the lane's own selection behaviour |
| anchor | § The `action` keyword (section id `action`, HTML line 953; the `'append'` list item at HTML lines 989-990); located quote "'append' - This appends each argument value to a list. It is useful for allowing an option to be specified multiple times." (**22 words** by `wc -w`), quote-equal after the rendered code span is folded to its text and the sentence occurs exactly once on the page (the bare marker `'append'` occurs twice, at HTML lines 989 and 1062); the page's own version pin "Python 3.15.2 documentation" (HTML line 19) and footer "Last updated on Oct 25, 2026 (17:03 UTC)" (HTML line 2709); fetched 2026-11-06, HTTP 200, **327874 B**, sha256 `36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae` — the version-pinned snapshot, whose digest is identical across five fetches. The L1's earlier access to the **rolling alias** `https://docs.python.org/3/library/argparse.html` (HTTP 200, 334994 B, sha256 `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16`) is named in the same cell as **superseded by this pin**, with the reason |
| teaches | argparse's append action accumulates repeated option values into one list rather than keeping the last, so a repeatable `--check` flag names exactly the checks it lists — the stdlib semantics the C1 t08 arm observes when `verifiers/verify_dispatch_prompts.py:527` declares `--check` with `action="append"` |

**`corpus/lessons/round-99.md`** — a scaffold authored by this seat, with the sections the round's
item names: `## Gate` (S281's full access record, the L1's `/3/` reading superseded by the pin with
its reason, the C1 t08 grounding and its bound, and the `git-hash-object` lead kept **unrowed**),
`## Corrections` (C99-1…C99-4), `## Mistakes` (one row), `## Status changes`, `## Considerthese`,
`## Settlement` (placeholder for the L1).

## 2. The L1 ruling applied (A1) and the scout's facts folded in

The L1 ruled (`plans/round-99-addendum-1.md` A1) that S281 must cite the **version-pinned** URL,
not the rolling `/3/` alias. That is what the row cites.

- **Pinned page (the row's access record)** — 2026-11-06, HTTP 200, 327874 B, sha256 `36e8d536…`,
  reproduced by this seat's own fetch at 2026-11-06T14:20:27Z and by `ScoutSourcesR99`'s five fetches
  (13:54Z–14:13Z); quote at HTML lines **989-990**, 22 words; page title pin at HTML line 19;
  footer at HTML line 2709.
- **The L1's `/3/` reading, superseded-by-pin (reason)** — the alias is a **rolling build**: this
  seat's 14:17:07Z fetch served HTTP 200, 334994 B, sha256 `906919fd…`, and the two byte streams
  differ in **exactly five bytes** — the footer's `HH:MM` field at HTML line 2712 (`13:27` in the
  receipt's bytes, `13:47` in today's). Substituting only that field reproduces the receipt's digest
  exactly (`sed 's/(13:47 UTC)/(13:27 UTC)/' | sha256sum` → `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16`);
  `diff` reports one differing line. The quote, its 22 words and its line numbers (992-993) are
  identical in both builds. So the receipt is *real but not re-fetchable*, and the row carries the
  pin as its identity and the alias reading as superseded.
- **Scout F4** — the bare marker `'append'` occurs twice on the page (HTML lines 989 and 1062); the
  row's anchor says so, so a quote match must carry the surrounding words, not the marker.
- **Scout F5** — the registry holds no `argparse` row (`grep -rn "library/argparse.html" corpus/` →
  no hits; the only "argparse" hit is **S211**, a `kind=code` row on a GitHub URL about a different
  document), so S281 adds no `W04` and no `E04`.

## 3. Corrections recorded (append-only, in the lesson)

- **C99-1** — the round-98 report's landed-changes row says "+183 lines inside `self_test()`". The
  measured insertion is **182** lines: `git diff -U0 a33f262f… e61629f5… -- verifiers/verify_dispatch_prompts.py | grep '^@@'`
  → `@@ -1333,0 +1334,182 @@ def self_test() -> int:`. **183** is the *two-file* total
  (`git diff --numstat`: 182 for the verifier, 1 for `corpus/QUALITY.md`'s Q88 row). The report's
  bytes are filed and are not rewritten.
- **C99-2** — `SCORECARD.md`'s round-98 C1 annotation names the freeze `63cd48d9` for the
  red-before, but that receipt's own command line measures the **instrument** revision `a060b450…`.
  The value stands — the two revisions carry byte-identical `verifiers/verify_dispatch_prompts.py`
  (both `sha256 1e67db315d22b41cfe4760983708af7815860a926f6ad5f9f25137d12110690f`). The correction
  is to the *named revision* only.
- **C99-3** — **Scout F2**, the routed defect 5: S279's located quote stops before access-check
  step (4)'s second conjunct. The page's HTML lines 1518-1520 read "the caller does not have the
  CAP_SYS_PTRACE capability in the user namespace of the target process" — **16 words** by
  `wc -w` — and the rule is a **conjunction**; the same algorithm's step (3) carries the *opposite*,
  permissive `CAP_SYS_PTRACE` disjunct at HTML lines 1513-1514, so a fragment must not be able to
  flip either. The `ptrace(2)` page re-opens **byte-identically** to S279's own digest
  (`69cd309e…`, 104833 B) — unlike argparse, this page is stable and its anchor re-verifies. The
  row's `teaches` cell already states the conditional correctly; what is short is the *quote*. This
  seat does **not** amend S279 (append-only; the registry-form correction is a superseding row, the
  L1's call) — the lesson's correction note is the record.
- **C99-4** — a digest recorded against a rolling documentation alias is a **build stamp, not a
  content identity**. The same mechanism already sits on **S253** (`/3/library/tempfile.html`,
  whose recorded 75190 B also differs in length from today's 75198 B, so content moved too),
  **S270** (`/3/library/unittest.html`) and **S276** (`/3/library/pathlib.html`), each provably
  broken by the footer field alone (Scout F1). **No registry edit is made for them this round** —
  their protected cells may not change in place, so the only correct repair is a superseding row
  each: **routed to round 100**.

## 4. Mistakes row (one)

Class `governance-cell-cites-fleet-path-repo-rooted`; evidence
`.ufo/waves/round-98/w1/ScoutTipReds.md` § 2.1 row 4 (16 unique subjects introduced by `747a07c`
r82, `84c2963`/`d84c7c8` r83, `462d240` r84, `d1c0318` r87, `010d3b8` r92, `38361a2` r97) and § 4 F6
(the normalized red); captured-by `governance.citation_resolves` — it *did* fire and name the cells,
but the landing no-harm rule since round 92 accepts "the base red set" as a conjunct, so the red
never heals; fix **claim C2 plus a QUALITY criterion** (the L1 adds **Q89**); shown able to fail by
`.ufo/waves/round-99/receipts/c2-base.txt` → `C2 carried reds green 0 of 3; self-tests held 3 of 3;
frozen 4 of 4; guards ok`, `C2-PREDICATE-UNMET` rc 1.

## 5. Gates run by this seat (all read-only, in the scratch clone / a fleet-shaped sandbox)

| check | command | observed |
|---|---|---|
| SOURCES census | `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file $D/corpus/SOURCES.md` | **rc 0**, `file ok`, **rows 206 → 207**, **W04 34 → 34** (unchanged) |
| SOURCES append-only | `(cd $D && python3 -B verifiers/check_sources_append_only.py --rev HEAD --base b53e209… --repo $D)` | `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`, rc 0 |
| corpus integrity (candidate, fleet-shaped sandbox) | `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` | `tracked_files 204`, `unindexed 0`, `stale_patterns 0`, `missing_paths 0`, `report_total 175`, `report_dead 0`, `commit_total 72`, `commit_unresolvable 0`, `commit_nonhash 0` — **all nine zero-mode checks PASS** |
| corpus independent (same candidate) | `python3 -B verifiers/verify_corpus_independent.py` | `unindexed=0 stale=0 missing=0 dead=0 unresolvable=0 nonhash=0`, **rc 0** |

**Observed baseline drift (this seat's, for the L1's re-record).** ExecRedsR99 re-recorded
`verifiers/corpus-baseline.json` to 203 / 174 / 72 on the tree *without* this seat's patch. With
this seat's patch the two `equal` counts move: `corpus.index.tracked_files` **203 → 204** (this
seat's `corpus/lessons/round-99.md`) and `corpus.pointers.report_total` **174 → 175** (the lesson's
one live absolute pointer to the fleet round-98 report); `corpus.pointers.commit_total` is
unchanged at 72. Every `zero`-mode expectation holds. `verifiers/corpus-baseline.json` is
ExecRedsR99's file, so this is **reported, not patched** — the L1 re-records at integration. Per the
round's handoff note this drift is expected on a candidate that adds this seat's lesson/S281 row
after ExecRedsR99's baseline, and it is **not** a C2 failure of the ExecRedsR99-only candidate.

A side note for the L1: the `report_dead` class reads **1** in a *plain* scratch clone and **0** in a
fleet-shaped sandbox. The site is `corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md`,
whose target is the lane's own committed **symlink** `.ufo/reports/round-76/kotoba.md ->
../../../../.ufo/reports/round-76/kotoba.md`; it resolves only when the lane clone sits one level
below a directory that holds the fleet `.ufo` — i.e. only in the fleet-shaped sandbox the C2
counter builds. Not a defect in the corpus; a note on where the class is observable.

## 6. Files written

| path | what |
|---|---|
| `corpus/SOURCES.md` | +1 line: the `S281` row (appended after `S280`) |
| `corpus/lessons/round-99.md` | new, 221 lines: the round-99 lesson scaffold |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/ScribeCorpusR99.patch` | `git diff --binary b53e209…` from the seat's scratch clone; sha256 `94a39deec29cda3920a1bb16e70c0ddfbb2d3f8ba8e6e2b09943db7ef2fc92fa` |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/census-after.txt` | census validate receipt |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/append-only.txt` | append-only gate receipt |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/fetch-record.txt` | the two access records + digests + short excerpt lines (no HTML stored under the wave tree) |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/candidate-corpus.txt` | the fleet-shaped candidate measurements + the drift table |
| `.ufo/waves/round-99/w1/ScribeCorpusR99/patch-proof.txt` | patch sha256, base, and the apply proof on a second fresh clone |
| `.ufo/waves/round-99/w1/ScribeCorpusR99.md` | this report |
| `.ufo/waves/round-99/w1/ScribeCorpusR99_READY` | the READY file |

## 7. Patch and handoff

- Patch: `.ufo/waves/round-99/w1/ScribeCorpusR99/ScribeCorpusR99.patch`, base
  `b53e209603e7c480cd975ea543e415b66f695438`, two files (`corpus/SOURCES.md`, `corpus/lessons/round-99.md`).
- Apply proof: a **second fresh scratch clone** at the freeze base → `git apply --check` OK,
  `git apply` OK, and both applied files are **byte-identical** to the seat's scratch clone's
  (verified by `diff`). The verification clone was removed after the check.
- Scratch candidate revision (one commit on the base): **`74c4c2a67aae49fdaf7f23a8baafa1f1fd509281`**.
  The scratch history is deliberately a **single** commit: an earlier two-commit history made
  `check_sources_append_only.py` report a protected-cell change on S281, because the row's own
  cells were re-edited between this seat's own commits — squashing makes the gate scan exactly the
  landed diff, and the gate then reads clean.
  **The scratch clone is deleted** (the bounds' scratch directive), so that revision is a record of
  what was measured, not a resolvable object: **the L1 rebuilds the candidate by applying the three
  patches in order** (ExecRedsR99 → ScribeCorpusR99 → ExecArmsR99) into a fresh scratch clone at
  `b53e209…`, exactly as this seat did for the § 5 measurements.
- Order for the candidate build: **ExecRedsR99 → ScribeCorpusR99 → ExecArmsR99** (this seat's patch
  touches neither `corpus/README.md` nor `verifiers/corpus-baseline.json`, so it does not collide
  with ExecRedsR99's files; the only interaction is the baseline count drift reported in § 5).

## 8. Out of scope for this seat (named, not touched)

- `corpus/README.md` (ExecRedsR99's coverage-map row for `lessons/round-99.md`), `verifiers/corpus-baseline.json`
  (ExecRedsR99), `verifiers/verify_skill_checklist.py`, `verifiers/check_tip_battery.py`, `LOG.md`
  (ExecRedsR99), `verifiers/verify_dispatch_prompts.py` (ExecArmsR99) — untouched.
- **S253 / S270 / S276** — rolling-alias digest drift, measured and recorded (C99-4); the repair is a
  superseding row each, **routed to round 100**.
- **S279** — the located quote's truncation is recorded (C99-3); the registry-form fix is a
  superseding row, the L1's call.
- The **`git-hash-object(1)`** candidate the scout screened: **rejected for C2's route** (the
  `INSTRUMENT_PINS` value is *read* from a committed tree via `git rev-parse <rev>:<path>` at
  `verifiers/check_tip_battery.py:344`, not hashed from a file) and **not rowed** as a general row
  either — it grounds a fact no claim of this round rests on. Kept in the lesson as an unrowed lead
  with its flip condition.
- `considerthese/2026-10-26.md` — re-read; **all five proposals remain unimplemented** at the freeze
  (measured: `SKILL.md` 600 lines / 92672 B, 165 lines over 120 chars, 94 over 300, longest 1491 at
  line 518, `## Gate registry` at line 443 and no `verifiers/REGISTRY.md`, description 1021 chars with
  a 151-char first sentence, `.ufo` 353 MB of a 590 MB tree); none is taken this round and none is
  trivially citable as a registry row.

## 9. Findings

1. **A rolling documentation alias cannot carry a digest** (this seat's own S281 access record; the
   same class already sits on S253/S270/S276 — Scout F1). The five-byte footer field is the entire
   difference; the content is stable. A row on `/3/` records a build stamp.
2. **`ptrace(2)` is stable and `argparse` is not** — the two pages this round touched behave
   differently under the same access, and the S279 conjunct is confirmed byte-identically.
3. **A quote fragment of a conditional rule is a defect class of its own** (Scout F2): step (4)'s
   two `CAP_SYS_PTRACE` mentions have opposite polarity, so a truncated quote can flip the reading.
4. **The corpus index counts are tree-wide, not patch-local** — this seat's one lesson file moves two
   `equal` counts that the L1 re-records at integration; the `zero` expectations all hold.

**No counter defect is claimed.** Neither `verifiers/fixtures/round-99/selftest-kills.py` nor
`verifiers/fixtures/round-99/carried-reds.py` was edited, and no predicate was read as wrong.

## 10. Tooling

**No tool was installed or upgraded by this seat** (nothing was needed; the work is
`git`/`curl`/`sha256sum`/`python3 -B` stdlib and the lane's own scripts). Host rules observed: no
pacman transaction, no `/proc/sys` write, no `sysctl -w`, no git write in the lane or the fleet root,
and no scratch left behind — `/fast/scratch/hyaku/kotoba-r99/ScribeCorpusR99/` is deleted on yield.

*Report written by ScribeCorpusR99, r99-w1. Lane repo writes: `corpus/SOURCES.md` (the S281 row)
and `corpus/lessons/round-99.md` (new), both inside the seat's scratch clone and delivered as a
patch; no other lane file, the lane's index, the fleet root, `considerthese/`, `scripts/`,
`templates/` or `.ufo/state/` was written.*
