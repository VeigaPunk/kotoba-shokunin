# E08SourcesUsedBy — S213 `used-by` append (kotoba round 77, w1, build seat)

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Measured base: lane HEAD
`6523aced1ee0ebe07dca996213bdc645a6acbd1e` (round-77 freeze). Scope of this seat: the S213
`used-by` cell of `corpus/SOURCES.md` only — the one in-place change `CORPUS.md` rule 2 permits
besides `status`/`recheck`. No lane file was written by this seat; every number below comes from
scratch clones under `/fast/scratch/hyaku/kotoba-r77/E08SourcesUsedBy/` (removed before yield) and
is pasted with its command and its own exit status.

Frozen counters were **not** edited or moved: at the measured base,
`sha256(verifiers/check_desc_craft.py)=cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`
and `sha256(verifiers/check_r75_routed_repairs.py)=989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`
— both equal the sha256 pairs pinned in `plans/round-77.md`.

## 1. The change (deliverable)

One row, one cell, `corpus/SOURCES.md` line 153 (registry row `S213`, the 138th of 151 rows; file
line 153 because the table's rows are not id-ordered):

- old `used-by` cell, verbatim: `` corpus/knowledge/skill-eval-artefacts-round70.md ``
- new `used-by` cell, verbatim: `` corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md ``
- separator **comma + space** — the separator `scripts/sources-census.sh` splits on
  (`usedby_findings()`: `IFS=',' read -r -a paths <<< "$usedby"` + `trim_cell` per member), and the
  lane's existing house style: 58 registry rows already carry multi-member `used-by` cells
  (`'SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md'`, …).

Measured on committed bytes at base vs the patched scratch commit
(`python3` over `git show HEAD:corpus/SOURCES.md` and the worktree file):

| measurement | old row | new row |
|---|---|---|
| characters | 810 | 857 (+47) |
| UTF-8 bytes excl. newline | 814 | 861 (+47) |
| sha256 of row bytes | `72683738c5ea97ee7287ec75f645989350530813d4cbb53bbcf8971b473721a6` | `478c8dfd10b9cb8e8781b7ddbd877815858f99dd09ca44d65dc34f5caf799cda` |
| `NF` (pipe-fields) | 13 | 13 |
| parsed cells | 11 | 11 |
| registry rows | 151 | 151 |
| file lines | 381 | 381 |

`+47 = len(", corpus/knowledge/description-craft-round76.md")` (45 + 2). ASCII-only addition, so
character and byte deltas agree. **No other cell moves** — cell-by-cell comparison of all 11 cells
returns `cells equal except used-by: []`, and the whole-file comparison returns
`changed line numbers [153]`. `status` stays ` mined `, `opened` stays ` 2026-10-25 `, `recheck`
stays ` 90d `, and the `anchor` cell is untouched (addendum-1 withdrew the anchor-digest clause
because rule 2 forbids an in-place `anchor` edit).

## 2. The patch, and that it applies to the lane HEAD

`E08SourcesUsedBy.SOURCES.patch` = `git diff 6523ace 2015094 -- corpus/SOURCES.md` from the scratch
clone (6 760 B, sha256 `2a05870c2064c015d410e1a6587f506b2964bb85376eccc619e4385a08b8f564`). Applied
in a **second** independent shared clone of the lane at the unmodified base:

```
$ git -C $S/applycheck apply --check .../E08SourcesUsedBy.SOURCES.patch   -> apply-check-exit=0
$ git -C $S/applycheck apply         .../E08SourcesUsedBy.SOURCES.patch   -> apply-exit=0
$ cmp $S/applycheck/corpus/SOURCES.md $S/clone/corpus/SOURCES.md          -> identical
line153 identical: True
```

## 3. Gate matrix (each gate's OWN exit status; no pipelines)

Clone `/fast/scratch/hyaku/kotoba-r77/E08SourcesUsedBy/clone` (shared clone of `6523ace`, identity
`scratch-r77`, `rev-parse --show-toplevel` asserted before the first commit). Arms:

- **base** `6523ace` — lane bytes, unmodified;
- **A** `2015094` — the `used-by` append only;
- **B** `aee7ac0` — append + the r76 drafts as fixtures (`build/entry-draft.md` →
  `corpus/knowledge/description-craft-round76.md`, `build/lesson-draft.md` →
  `corpus/lessons/round-76.md`);
- **E** `d1e2858` (second clone) — patch + a one-line entry stub + the **delivered lesson log line**
  as the only content of `corpus/lessons/round-76.md`.

| check | base | A (append, no entry) | B (append + entry + lesson) |
|---|---|---|---|
| `sources-census.sh validate --file …/SOURCES.md --today 2026-10-27` | `ok` + 20 `W04`, **exit 0** | `E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`, **exit 1** | `ok` + the same 20 `W04`, **exit 0** |
| `check_skill_evals_v2.py --repo … --rev` | `2 of 10`, exit 1 (pre-existing finding: `SKILL.md: 0 rendered lines name the entry + S211/S212/S213`) | `1 of 10`, exit 1 (`A10: census validate --file non-zero at --rev`) | `2 of 10`, exit 1 — **the same single finding as base** |
| `check_sources_append_only.py --repo … --rev` | `18 change(s) in 8 of 44 commits`, exit 1 | — | `18 change(s) in 8 of 45 commits`, exit 1, `log 20150940b S213 used-by: …cts-round70.md -> …cts-round70.md, corpus/k…` |
| `check_spec_craft.py --repo … --rev` | `3 of 3`, exit 0 | `0 of 3`, exit 1 (`not census-conformant … (conjunct (b))` ×3) | `3 of 3`, exit 0 |
| `verify_corpus_integrity.py --repo … --json` | 4 DRIFTs, exit 1 | **4 DRIFTs, identical set**, exit 1 | 5 DRIFTs, exit 1 |
| `verify_corpus_independent.py --repo … --json` | 1 DRIFT (`corpus.index.unindexed`), exit 1 | **1 DRIFT, identical**, exit 1 | 2 DRIFTs, exit 1 |
| `check_desc_craft.py --repo … --rev` (frozen C1) | `0 of 6`, exit 1 | — | `4 of 6`, exit 1 — **(e) registry: pass** |

Drift names: base = `corpus.index.tracked_files`, `corpus.index.unindexed`,
`corpus.pointers.report_total`, `corpus.pointers.commit_total`; independent base/A =
`corpus.index.unindexed`. At B the extra integrity drift is `corpus.pointers.commit_unresolvable`
and the extra independent drift is `corpus.pointers.commit_unresolvable` — traced in §7 to the
lesson draft, **not** to the `used-by` change.

Reading of the matrix: **the append is finding-neutral and drift-neutral on its own; the entry file
must land in the same commit** (arm A: census `E11`, `check_spec_craft` 3/3 → 0/3, `check_skill_evals_v2`
`A10`). The 18 append-only breaches and part of the base red are pre-existing lane state (r76 D4 /
the r76 lesson-recording gap), not caused here: the append adds exactly one **permitted-cell** log
line and no breach.

Gate self-tests run on the frozen bytes (they are the gates the L1 will land against):

```
$ python3 -B verifiers/check_skill_evals_v2.py --self-test      -> self-test: 0 failure(s)      exit=0
$ python3 -B verifiers/check_sources_append_only.py --self-test -> self-test: 0 failure(s) over 21 assertions  exit=0
```

## 4. Calibration controls (the change is load-bearing)

Both controls run as scratch commits on top of B, then the clone was reset to B:

- **C — wrong separator** `04a04feb3`: cell rewritten with `; ` instead of `, ` →
  `file E11 S213 missing used-by corpus/knowledge/skill-eval-artefacts-round70.md; corpus/knowledge/description-craft-round76.md`,
  **exit 1**. The census treats the semicolon cell as one path, so the separator choice is measured,
  not assumed.
- **D — replace instead of append** `7183c33b3`: cell set to the new entry only → census `ok`,
  **exit 0** (the census cannot see the loss), but the frozen evals gate fires
  `F7: S213 used-by lacks exact member corpus/knowledge/skill-eval-artefacts-round70.md (comma-delimited exact match required)`,
  `2 of 10`, exit 1. So the append-not-replace duty is enforced by `check_skill_evals_v2.py`, and
  the census alone would not catch a replace.

## 5. C1 conjunct (e) — the operand this seat owes

Frozen counter `verifiers/check_desc_craft.py` (sha256 as pinned, unmodified), conjunct (e) per its
docstring: *row S213's `used-by` cell lists `corpus/knowledge/description-craft-round76.md`, and the
old->new change is logged in `corpus/lessons/round-76.md`*.

```
$ python3 -B verifiers/check_desc_craft.py --repo $C --rev aee7ac0   (arm B: append + r76 drafts)
(a) snapshot chain: fail      (b) located quotes: pass     (c) act-on: fail
(d) self-audit: pass          (e) registry: pass           (f) provenance: pass
description craft backed 4 of 6
exit=1
```

Arm E isolates the delivered lesson line (patch + one-line entry stub + the § Status changes bullet
from `E08SourcesUsedBy.lesson-line.md` as the only lesson content):

```
$ python3 -B verifiers/check_desc_craft.py --repo $A --rev d1e2858
(e) registry: pass
description craft backed 1 of 6
exit=1
```

So **(e) passes on the append + the delivered log line**, and it fails at base
(`(e) row S213's used-by cell does not list corpus/knowledge/description-craft-round76.md`,
`0 of 6`, exit 1) — conjunct (e) is genuinely gated by this seat's change.

## 6. Verifying the r76 input, not trusting it

`.ufo/waves/round-76/build/sources-patch.md` was checked against current bytes:

- **Confirmed**: line 153; old row 810 chars / 814 bytes; new row 857 chars / 861 bytes;
  `+47 = 45 + 2`; `NF=13`, 11 cells; 151 rows; comma-only census split; the same-commit landing
  constraint with its two-arm `E11` / `ok` evidence; the `check_spec_craft` knock-on
  (3 of 3 → 0 of 3 when the registry names an absent entry) — all reproduced here, and the
  knock-on now has a **recovery** arm as well (`3 of 3`, exit 0 at arm B).
- **Stale / superseded**: the draft's claim that the append costs a `check_skill_evals_v2` finding
  (`2 of 10 → 1 of 10`, `F7: … exact match required`) was measured on the pre-repair gate. After
  r76's addendum-2 §4 repair the gate matches comma members (`verifiers/check_skill_evals_v2.py:289-291`:
  `used_by = [p.strip() for p in row[10].split(",")] … if ENTRY not in used_by`), and the measured
  result is **2 of 10 at base and 2 of 10 at arm B — no new finding**. The draft's CF-2 ("two
  counters disagree about the same cell") is **closed**: C1 (e) asks for membership, the evals gate
  now also asks for membership, and both hold simultaneously.
- **Unchanged and still true**: the anchor cell carries no sha256, so C1 (a) cannot be reached
  through this cell (addendum-1's four-place pin stands); rule 2 permits this edit and nothing else
  here.

## 7. Adjacent findings routed (outside this seat's write scope)

1. **The r76 lesson draft carries a commit token that the integrity gate cannot resolve.**
   `build/lesson-draft.md:183` says ``it names the upstream commit `69ef37e` and …``. `COMMIT_RE`
   in `verifiers/verify_corpus_integrity.py:151` is ``(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)` `` and
   its code-span exemption is evaluated on the **whole** match span (which starts at the word
   `commit`, outside the backticks), so the token scores as a 7-hex commit citation that does not
   resolve in the lane repo. Measured: arm G2 (append + lesson draft only) → `5` DRIFTs, exit 1,
   `commit_unresolvable_detail = ['corpus/lessons/round-76.md:183: 69ef37e']`; arm G1 (append +
   entry draft only) → `4` DRIFTs, the base set, so the entry draft is clean on this axis.
   Remedy measured, not guessed: write the upstream hash in the gate's truncated form
   (``commit `69ef37e9424…` ``, `TRUNCATED_COMMIT_RE = \A[0-9a-fA-F]{7,40}…\Z`) → arm G2b
   `4` DRIFTs, `commit_unresolvable_detail = []`. This must be fixed **before** the lesson lands,
   or the round's no-harm battery cannot read green at the final tip.
2. **C1 (a) still fails with the current lesson draft**: `(a) the lesson Gate carries no <=25-word
   quote located in the optimizing-descriptions snapshot`. The lesson scribe seat must add the
   rule-1 access record (URL, access date matching the fetch record, ≤25-word located quote naming
   the `7cc54fbb…` digest) — the counter's own words.
3. **C1 (c) still fails with the current `SKILL.md`**: `no Body craft row cites both
   corpus/knowledge/description-craft-round76.md and S213` — the `build/skill-patch.md` row is not
   applied at arm B, as expected before integration.
4. Useful state for the L1: with the r76 entry + lesson drafts in place, C1 reads **4 of 6** — (b)
   located quotes, (d) self-audit (entry audit values match the counter's recompute at these bytes)
   and (f) provenance already pass; only (a) and (c) are open.

## 8. Freshness, operability, no-harm

- **Freshness**: the row stays `status=mined`, `opened=2026-10-25`, `recheck=90d`. No date cell is
  touched, so the census `overdue` class and the recheck clock are unchanged; the row remains
  `mined`, which is the state the census requires before it validates `used-by` members at all
  (`usedby_findings()` skips rows whose status is not `mined`).
- **Operability**: the change is one line, applies clean with `git apply --check` at the lane HEAD,
  and needs the entry file in the same commit (§3). Nothing else in the registry, the counters or
  the lane index is touched by this seat.
- **No-harm (measured, not asserted)**: the two corpus gates show the **identical** drift set at
  base and at the append-only commit (4 DRIFTs / exit 1 and 1 DRIFT / exit 1, both pre-existing),
  and `check_spec_craft`, `check_skill_evals_v2` and the census return to their base values once the
  entry exists. The only state that regresses is the intermediate append-without-entry commit, which
  must not be created in the lane at all.
- **Tooling**: nothing installed or upgraded (no pacman — host-wide pause respected; no other
  channel used). All work used stock `git`, `python3`, `bash`.
- **Scratch discipline**: two `git clone --shared` clones, three commits, and one reset, all inside
  `/fast/scratch/hyaku/kotoba-r77/E08SourcesUsedBy/`; `git rev-parse --show-toplevel` asserted
  before the first commit in each clone; every git call named `-C`; no write of any kind to the lane
  tree, the fleet repo, jj state or the lane index.

## 9. Risks / open items

- The append is only safe **bundled with the entry**; if the L1 lands it alone, the census (`E11`),
  `check_spec_craft` (3/3 → 0/3) and `check_skill_evals_v2` (`A10`) all go red. Land
  `E08SourcesUsedBy.SOURCES.patch` in the same commit as
  `corpus/knowledge/description-craft-round76.md`.
- The lesson line in `E08SourcesUsedBy.lesson-line.md` is paste-ready and proven against the frozen
  conjunct-(e) parser, but the same lesson file must also satisfy (a); the line as written does not
  touch the Gate section, so both duties can coexist.
- No blocker. The patch, the log line and the receipts are complete and reproducible from the
  commands in `E08SourcesUsedBy.receipts.txt`.

VERDICT: S213 `used-by` append produced and verified — one cell (old → `…/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md`), +47 bytes, all other cells byte-identical, census `ok` exit 0 with the entry present in the same commit, 0 new append-only breaches, `check_skill_evals_v2` finding-neutral (2 of 10 before and after), and frozen C1 conjunct (e) measured passing on the delivered patch + delivered log line.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E08SourcesUsedBy.SOURCES.patch /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E08SourcesUsedBy.old-new.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E08SourcesUsedBy.lesson-line.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E08SourcesUsedBy.receipts.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E08SourcesUsedBy.md
