# Round 74 bookkeeping blocks — draft

Seat `ScribeLessonProvinceR74` (wave 1, build). Every block below is a **draft for the L1 to land**; this
seat never edits a lane file. Rules used:

- A value the cursor cannot read is `<<…>>`. No number is invented. Before-values are quoted **verbatim** from
  the frozen plan (`plans/round-74.md` at `329e7d91d7d750031c35d264f0e34af1d0ce8385`), which is what the plan
  itself declares them to be; they are *not* receipts committed by this seat.
- House forms read before drafting: `corpus/lessons/round-73.md`, `corpus/lessons/round-72.md` (lesson shape),
  `SCORECARD.md:464` (Round-73 annotation), `SCORECARD.md:185-305` (Move log; the round-55 rows at `:304-305`
  are the last rows in the table), `LOG.md:2783-2797` (Round 73 entry), `corpus/README.md:128-144` and `:225`
  (index rows and the Round-73 Frontier note), `SHONEN.md`, `corpus/QUALITY.md:78` (Q62),
  `corpus/lessons/round-73-verifier-spotcheck.md:155-172` (§ 6, the seven routed items).
- Frozen ids of this round (from `plans/round-74.md`): C1 entry `corpus/knowledge/spec-skill-creation-craft-round74.md`;
  C2 entry `corpus/knowledge/sibling-overlap-census-round74.md`; C1 counter `verifiers/check_spec_craft.py`;
  C2 counter `verifiers/check_sibling_reread.py`; C1 subsection `### Body craft — the specification's skill-creation guides`.

## 0. Fill map — who settles each placeholder

| placeholder class | settled by |
|---|---|
| `<<FROZEN-SHA>>` for either counter | the counter file's sha256 once the L1 freezes it (the file does not exist at HEAD: `ls verifiers/check_spec_craft.py verifiers/check_sibling_reread.py` → both absent) |
| `<<C1-N>>`, `<<C2-N>>` after-values | `python3 -B verifiers/check_spec_craft.py --rev <rev>` / `... check_sibling_reread.py --rev <rev>` at the landing rev, receipt under `.ufo/waves/round-74/receipts/` |
| `<<C1-BASE-RECEIPT>>`, `<<C2-BASE-RECEIPT>>` | the do-nothing control receipts committed before data (`plans/round-74.md` § C1 / § C2 "Do-nothing control") |
| `<<Q45-N>>` | the wave-1 Q45 census seat's count of pages carrying ≥ 2 quotable rule tokens (`plans/round-74.md` § C1, before data) |
| new `S###` ids, `<<RENUM-*>>` | the renumber map by document (URL), written in scratch under `.ufo/waves/round-74/assimilation/` before any append |
| `<<SNAP-*>>`, `<<QUOTE-*>>`, `<<ACCESS-DATE>>` | each page's committed snapshot under `.ufo/waves/round-74/snapshots/` plus its `FETCH-LOG.tsv` line (URL, HTTP status, `date -I`, bytes, sha256) |
| `<<GATE-REG-N>>` | `python3 -B verifiers/check_gate_registry.py --rev <rev>` (the plan's target is `60 of 60` after two new rows) |
| `<<LINE-COUNT>>`, `<<SOURCES-ENTRIES>>` | `wc -l SKILL.md` (570 at base) and the `## Sources` entry count at the landing rev |
| `<<W1-DISPATCHED>>`, `<<W2-SEATS>>` | `.ufo/waves/round-74/w1-dispatch.json` / the wave-2 spec |
| `<<M-IDS>>`, `<<STATUS-*>>` | the round's mined-mistake rows and the registry diff at landing |

## 1. `corpus/lessons/round-74.md` — skeleton

```markdown
---
author: kotoba L1 (hyaku run 7, round 74, attempt 1)
date: 2026-10-25
round: 74
lane: kotoba
---

# Round 74 lessons — kotoba

Claims (frozen in `plans/round-74.md` at `329e7d91d7d750031c35d264f0e34af1d0ce8385`; base lane tip
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`): **C1 depth** (sourced, assimilation): the Agent Skills
`skill-creation/` guides — `best-practices`, `using-scripts`, `quickstart` — reach `SKILL.md`'s guidance,
counted by `verifiers/check_spec_craft.py --rev <rev>`; **C2 freshness** (advisory): the sibling census is
re-pinned and re-read at the frozen fleet heads, counted by `verifiers/check_sibling_reread.py --rev <rev>`.
Round shape: two v1 waves (wave 1 dispatched `<<W1-DISPATCHED>>`; wave 2 `<<W2-SEATS>>`).

## Gate

Assimilation theme (addendum §10; nothing written, run or fetched inside `/home/vgpnk/Projects/shokuknow`):
**the specification's skill-creation guides** from `merge/kotoba/` — staged entry
`knowledge/corpus/knowledge/spec-script-craft-rules.md` (staged S236, S237) and the S232 best-practices row cited
by the staged `spec-description-trigger-discipline.md` (both filenames read from the package listing, not taken
from the plan's prose).

**Id collision check** (`.ufo/waves/round-74/assimilation/`): the lane registry holds 148 ids (`reg-ids`), the
package stages 188 (`staged-ids`), `collisions` lists 20 — `S203`–`S222`, the lane's own rows from rounds 69–73,
which the package numbered earlier. **Guard proof:** `<<GUARD-PROOF-PATH>>` (the 0–3-space pattern yields the id of
an indented scratch row and the column-zero pattern does not; a duplicate-id mirror is caught).
**Renumber map, by document (URL), not arithmetic:** `<<RENUM-BEST-PRACTICES>>`; `<<RENUM-USING-SCRIPTS>>`;
`<<RENUM-QUICKSTART>>`. Staged rows are campaign-schema and are rewritten in the 11-column lane schema in scratch
(no `|` in a cell; `recheck` `<<REC-CHECK>>`; `used-by` the one admitted entry; `opened` `<<ACCESS-DATE>>`; the
anchor carries the fetch record). The staged rows' own `scope`, `anchor` and `teaches` cells are not copied.
Scratch census validation before the registry append: `<<VALIDATE-FINAL-PATH>>` (base registry + new rows + entry,
`scripts/sources-census.sh validate --file …` exit `<<0>>`).

**Rows opened this round** (each fetched by a wave-1 seat and re-opened by the L1; `opened` = a round-74 date):

- **S<<BEST-PRACTICES-ID>>** — https://agentskills.io/skill-creation/best-practices.md; snapshot
  `.ufo/waves/round-74/snapshots/<<SNAP-BEST-PRACTICES>>:<<L>>`; access date `<<ACCESS-DATE>>`
  (`<<HTTP-STATUS>>`, `<<BYTES>>` B, sha256 `<<SHA>>`); quote (whitespace-collapsed snapshot text, ≤25 words,
  code spans are the snapshot's own backticks): `<<QUOTE-BEST-PRACTICES>>`
- **S<<USING-SCRIPTS-ID>>** — https://agentskills.io/skill-creation/using-scripts.md; snapshot
  `.ufo/waves/round-74/snapshots/<<SNAP-USING-SCRIPTS>>:<<L>>`; access date `<<ACCESS-DATE>>`
  (`<<HTTP-STATUS>>`, `<<BYTES>>` B, sha256 `<<SHA>>`); quote: `<<QUOTE-USING-SCRIPTS>>`
- **S<<QUICKSTART-ID>>** — https://agentskills.io/skill-creation/quickstart.md; snapshot
  `.ufo/waves/round-74/snapshots/<<SNAP-QUICKSTART>>:<<L>>`; access date `<<ACCESS-DATE>>`
  (`<<HTTP-STATUS>>`, `<<BYTES>>` B, sha256 `<<SHA>>`); quote: `<<QUOTE-QUICKSTART>>`

Fetch record: `.ufo/waves/round-74/snapshots/FETCH-LOG.tsv`; snapshots pinned in `snapshots/MANIFEST.sha256`.

**Q45 census (before data):** `<<Q45-N>>` of 3 pages carry at least two rule tokens the entry can quote
(`<<Q45-COMMAND>>`). The target stays `N == 3` if the census reaches 3; otherwise it is lowered **before data** in a
committed addendum stating the census command and margin (`<<ADDENDUM-PATH or "no addendum: census reached 3">>`).

**Admitted:** `corpus/knowledge/spec-skill-creation-craft-round74.md` (`<<N>>` page rows, documentary evidence
only). Expansion credit: `<<grep command>>` printed `<<N>>` line(s) at the base (`receipts/base-sweeps.txt`).
**Acted on:** `SKILL.md` `### Body craft — the specification's skill-creation guides` (`<<line range>>`), whose
action cells cite `S<<BEST-PRACTICES-ID>>`, `S<<USING-SCRIPTS-ID>>`, `S<<QUICKSTART-ID>>`; `PROVINCE.md` § Core
names the entry (`<<line>>`).

**Entry rewrites forced by this round's opening** (staged cells the live bytes do not carry; each re-derived on the
live page, evidence `<<SEAT-REPORT-PATHS>>`): `<<REWRITE-1>>`; `<<REWRITE-2>>`; `<<REWRITE-n>>`.

**Rejected, with reason and flip** (Q62: each on an observed fact — a quote absent, an anchor wrong, a scope
mismatch — never on an assertion about what the source lacks): `<<REFUSED-STAGED-ENTRY>>` — reason
`<<OBSERVED-FACT>>`; flip: `<<FLIP>>`. `<<REFUSED-ROW>>` — reason `<<OBSERVED-FACT>>`; flip: `<<FLIP>>`.
Staged rows not appended: `<<STAGED-IDS>>` (no admitted entry cites them; CORPUS rule 4).

**Quarantine:** the 13-row register slice (`assimilation/quarantine-slice`) is re-derived this round; the two rows
this round's entry can cite are hand-checked: **S236** `<<present after fold / absent / unverifiable>>` —
`<<evidence file:line>>`; **S237** `<<present after fold / absent / unverifiable>>` — `<<evidence file:line>>`
(the staged slice files both under the "cited source could not be fetched, so no quote was checked" class; the
class premise is decided by this round's fetch, not by the staged note). `<<any other slice row an admitted entry
cites: verdict + evidence>>`. No refused row is appended.

**Spot-check sample for the non-author closure (≥1 admit, ≥1 reject):** admit `<<S-ID>>` (`<<one-line reason>>`)
and `<<S-ID>>`; reject `<<S-ID or staged entry>>` (`<<one-line reason>>`) and `<<staged claim>>` (refuted by
`<<file:line>>`).

**considerthese:** `considerthese/2026-10-25.md` § Self-improvement suggestions item 4 (the SKILL.md frame "the two
harnesses here") is the one proposal worked: one frame sentence in the same `SKILL.md` edit (`<<line>>`), recorded
here and never counted by the counter. Proposals `<<list>>` stay open.

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| <<M-ID>> | <<class>> | <<the command and its observed output, or the file:line>> | <<Q-number or "none">> | <<fix, and whether it is shown able to fail>> |

## Routed defects (r73 spot-check § 6)

1. **Falsify wave** (`corpus/lessons/round-73-verifier-spotcheck.md:157`, second time asked): wave 2 of this
   round, lane-unique seat names ending `R74` (Q69), round total ≥ 64 — `<<W2-SEATS>>` seats, `<<state>>`.
2. **Index the closure file in the first commit** (`:159`): done in the plan commit `329e7d9`
   (`corpus/README.md` row for `lessons/round-73-verifier-spotcheck.md`); `<<verify_corpus_integrity.py reading at the landing rev>>`.
3. **D2 and D3 corrected by appended notes, never rewrites** (`:161`): SKILL.md is 570 lines not 572
   (`wc -l SKILL.md` → `<<N>>`, `<<correction site>>`); the r73 report's M128 "green-after cited" sentence is
   corrected by an appended note in this round's report; `check_report_pointers.py` run on the r74 report —
   `report pointers resolved N of M; unresolved <<0>>`.
4. **M129 structural guard** (`:164`): not built this round; the "fix" label on the SOURCES.md search-log
   ordering is **retracted** here (a fix counts only once shown able to fail — CORPUS additional rules).
5. **Fold C1 (r73) into `SKILL.md`** (`:166`): `<<decision row or checklist box on the .agents/skills/ root,
   landed as routed item not a claim>>`; the read-only package gets a resolvable path
   `<<path written in SKILL.md>>` (`/home/vgpnk/Projects/shokuknow/merge/kotoba/`).
6. **`compare_harness_independent.py` exit 2** (`:168`): `<<repinned / declared could-not-evaluate in the
   registry; the volatile-host-constant diagnosis and the L0 question line>>`.
7. **SHONEN boxes stay `[~]`** (`:170`): no non-author verifier is available to this lane; `<<recount lines
   updated or "none">>`.

## Round honesty

`<<Wave 1 dispatched/settled/silent; wave 2 run or not; the claim count (2); any withdrawal and its addendum;
the seat total against the 64-seat floor and the reason if it is missed.>>`

## Falsify corrections

`<<"None: wave 2 …" or the list — each correction names the fresh seat, the file:line it changed and the receipt;
corrections are appended, never rewrites of filed bytes.>>`

## Status changes

`S<<a>>`–`S<<b>>` `mined` at landing (new rows, no change to an existing row). `<<Every other `status`, `recheck`
or `used-by` change as old→new; or "None.">>`
```

> House-form note: `## Round honesty` sits between `## Routed defects` and `## Falsify corrections` in **both**
> `round-72.md` and `round-73.md`, though the seat brief's section list does not name it. Kept in the skeleton;
> the L1 may drop it, but dropping it breaks the shape of the two exemplars.

## 2. `SCORECARD.md` — Round 74 axis annotations (append as a new line after `:464`)

```markdown
**Round 74 axis annotations (append-only; verdicts belong to the non-author closure).** *Depth (C1, score held 9):* `python3 -B verifiers/check_spec_craft.py --rev <rev>` — `spec craft pages backed 0 of 3` exit 1 at `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` → `spec craft pages backed <<C1-N>> of 3` exit `<<0|1>>` at `<<C1-TIP>>` (conjuncts: `source:`/`verified-at:`/`recheck:` lines and two located rule tokens per page in the sha256-pinned snapshots, an 11-cell `mined`/tier-A registry row opened on a round-74 date with `used-by` naming the entry and a census-conformant registry, a located 5–25-word quote, the `SKILL.md` subsection `### Body craft — the specification's skill-creation guides` with two action rows carrying that page's own tokens, `PROVINCE.md` § Core naming the entry); `held at base: <<C1-HELD>>`, the do-nothing figure. *Freshness (C2, score held 8, advisory):* `python3 -B verifiers/check_sibling_reread.py --rev <rev>` — `sibling rows re-pinned and re-read 0 of 20` exit 1 at `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` → `sibling rows re-pinned and re-read <<C2-N>> of 20` exit `<<0|1>>` at `<<C2-TIP>>` (conjuncts: one row per lane in the round-49 shape passing the base's sha256-pinned `check_sibling_census.py` row checks; the row commit equal to the lane's frozen head and an ancestor of its branch head; `delta` equal to the counter's recomputation of `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`; `PROVINCE.md` § Adjacent carrying the same commit and classification; no `none` row for a lane whose pinned bytes name `kotoba`); world scores `<<CARRY-FORWARD-WORLD-SCORE>>` for the pure carry-forward and `<<OTHER-WORLD-SCORES>>` for the rest. Base: 15 of 20 siblings' `SKILL.md` or `PROVINCE.md` differ from their r49 pins, 50–312 commits behind (`plans/round-74.md` § Before-values). Wave 2 `<<ran N seats / not run>>`; no non-author verifier yet; bounds: documentary evidence only (no client run, no version string pinned), C1 counts form/sources/tokens and not whether a rule is true of the page, C2 counts pin/delta/cells/quote location and not the classification, and the rows are valid at their pins rather than at the round end. Scores held pending the closure.
```

## 3. `SCORECARD.md` `## Move log` — two rows (append after `:305`, the last round-55 row)

```markdown
| 74 | depth | `spec craft pages backed 0 of 3` @ `1e03d19`, exit 1 — plan table: `0 registry rows; 0 hits of calibrating control, defaults not menus, favor procedures, fragility of the task, one-off commands, pipx run, uvx ruff in corpus SKILL.md PROVINCE.md` | `spec craft pages backed <<C1-N>> of 3` @ `<<C1-TIP>>`, exit `<<0|1>>`; `held at base: <<C1-HELD>>` | `verifiers/check_spec_craft.py` (frozen sha256 `<<FROZEN-SHA-C1>>`), `corpus/knowledge/spec-skill-creation-craft-round74.md`, `.ufo/waves/round-74/snapshots/MANIFEST.sha256`, `plans/round-74.md` |
| 74 | freshness | `sibling rows re-pinned and re-read 0 of 20` @ `1e03d19`, exit 1 — plan table: `20 rows; 15 of 20 siblings' SKILL.md or PROVINCE.md differ between the row's pinned commit and the lane's branch head; pins 50–312 commits behind for the 15` | `sibling rows re-pinned and re-read <<C2-N>> of 20` @ `<<C2-TIP>>`, exit `<<0|1>>` | `verifiers/check_sibling_reread.py` (frozen sha256 `<<FROZEN-SHA-C2>>`), `corpus/knowledge/sibling-overlap-census-round74.md`, `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`, `plans/round-74.md` |
```

> Shape note: the two round-55 rows (`SCORECARD.md:304-305`) carry the counter's exact print plus its revision and
> exit code in `Before`, the same in `After`, and counter/entry/plan in `Evidence`. The table's last row is round
> 55 — rounds 56–73 have no Move-log rows — so these two rows continue it after an 18-round gap; a backfill is not
> this seat's work and is not proposed here.

## 4. `LOG.md` — `## Round 74` entry (append after `:2799`)

```markdown
## Round 74 — C1 depth (skill-creation craft, sourced), C2 freshness (sibling census re-pinned at the frozen fleet heads)

- **Trigger:** the round-74 steer (hyaku run 7, attempt 1); the r73 closure's seven routed defects
  (`corpus/lessons/round-73-verifier-spotcheck.md` § 6), the second ask for a falsify wave; assimilation theme
  `<<theme from merge/kotoba/>>`; base `1e03d19` read `tip battery 4 of 6` (the unindexed r73 closure file) and
  15 of 20 sibling rows stale against their pins (`receipts/base-battery-l1.txt`, `receipts/sibling-staleness-base.tsv`).
- **Action:** plan `329e7d9` (plan, base receipts, r73 closure index row, id scratch, sibling freeze heads);
  `<<addenda>>`; wave 1 (`<<W1-DISPATCHED>>` seats) — `<<counters built / sources opened / rows derived / controls>>`;
  C2 landed `<<C2-TIP>>` (`corpus/knowledge/sibling-overlap-census-round74.md`, `PROVINCE.md` § Adjacent,
  `<<N>>` re-pinned rows); C1 landed `<<C1-TIP>>` (`SKILL.md` § Body craft — the specification's skill-creation
  guides + the considerthese frame sentence, the entry, `<<N>>` SOURCES rows, `PROVINCE.md` § Core, registry rows,
  lesson); `<<routed items landed: D2/D3 notes, M129 retraction, .agents/skills/ row, harness L0 line>>`;
  wave 2 `<<N>>` seats `<<ran / not run and why>>`.
- **Outcome:** `python3 -B verifiers/check_spec_craft.py --rev <<C1-TIP>>` → `spec craft pages backed <<C1-N>> of 3`,
  exit `<<0|1>>` (base `0 of 3`, exit 1; `held at base: <<C1-HELD>>`); `python3 -B verifiers/check_sibling_reread.py
  --rev <<C2-TIP>>` → `sibling rows re-pinned and re-read <<C2-N>> of 20`, exit `<<0|1>>` (base `0 of 20`); tip battery
  `<<N of 6>>` in both invocation forms; `check_gate_registry.py` `<<GATE-REG-N>>`; `SKILL.md` `<<LINE-COUNT>>` of 600
  lines. Receipts: `.ufo/waves/round-74/receipts/`.
- **Pointer:** `plans/round-74.md`, `<<addenda>>`, `corpus/lessons/round-74.md`, `.ufo/waves/round-74/`.
```

## 5. `corpus/README.md` — three index rows and two Frontier notes

### 5a. Coverage map rows (append after `:144`, the r73 closure row; each row must land in the same commit as its file — `corpus.index.unindexed` is checked at that rev)

```markdown
| Skill-creation craft (round 74) | `knowledge/spec-skill-creation-craft-round74.md` | the open specification's own authoring guides — `skill-creation/best-practices.md`, `using-scripts.md`, `quickstart.md` (S<<BEST-PRACTICES-ID>>, S<<USING-SCRIPTS-ID>>, S<<QUICKSTART-ID>>, renumbered by document from the read-only staged package; documentary evidence, no client run): the body-craft rules the executing agent can act on, `<<one clause per page>>`; counted by `../verifiers/check_spec_craft.py --rev <rev>` (`spec craft pages backed N of 3`, `0 of 3` at base `1e03d19`); acted on in `../SKILL.md` § Body craft — the specification's skill-creation guides; three page snapshots pinned in `../.ufo/waves/round-74/snapshots/MANIFEST.sha256` |
| Sibling overlap census re-pin (round 74) | `knowledge/sibling-overlap-census-round74.md` | the round-49 census re-pinned and re-read at the frozen fleet heads (`../.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`, 20 lanes): each row carries the lane's frozen head, the r49-pin→head `delta` for `SKILL.md`/`PROVINCE.md`, and a quote re-read at the pinned commit (`<<N>>` rows unchanged, `<<N>>` changed); counted by `../verifiers/check_sibling_reread.py --rev <rev>` (`sibling rows re-pinned and re-read N of 20`, `0 of 20` at base `1e03d19`); rows are valid at their pins, not at the round end, and the classification judgement belongs to the closure's seats |
| Round-74 lessons | `lessons/round-74.md` | `## Gate` the three skill-creation rows with this round's located quotes, snapshots and fetch records, the id-collision result (`<<N>>` collisions renumbered by document), the Q45 census (`<<Q45-N>> of 3`), the staged claims admitted and refused with their flips, the S236/S237 quarantine verdicts; `## Mistakes` `<<M-IDS>>`; `## Routed defects` for the seven r73 items; `## Falsify corrections` from wave 2; the sibling re-pin with its freeze file |
```

### 5b. Frontier notes (append after `:225`, the Round-73 note, before `## Known gaps` at `:227`)

```markdown
**Round 74 (append-only note; new area *skill-creation craft*):** the specification's own authoring guides move to Core in part: `best-practices`, `using-scripts` and `quickstart` are held in `knowledge/spec-skill-creation-craft-round74.md` (S<<BEST-PRACTICES-ID>>–S<<QUICKSTART-ID>>, renumbered by document from the read-only staged package) and counted by `../verifiers/check_spec_craft.py --rev <rev>`; the acting row set is `../SKILL.md` § Body craft — the specification's skill-creation guides. This is documentary evidence: no client was run, no version string is pinned, and each guide's advice is recorded as the page states it. Still not held: `<<the skill-creation pages not opened this round>>`; whether a skill written to these rules routes or executes better — no measured effect of the rules exists in this lane.

**Round 74 (append-only note; sibling census re-pinned):** the round-49 sibling-overlap census is re-pinned and re-read at the fleet heads frozen in `../.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` (20 lanes) and counted by `../verifiers/check_sibling_reread.py --rev <rev>`; `<<N>>` of 20 rows show changed `SKILL.md`/`PROVINCE.md` bytes against their r49 pins. The rows are valid at their pins, not at the round end, and the classification of a boundary stays a reviewer judgement the counter does not make.
```

## 6. `SHONEN.md` — evidence lines a round-74 landing would update (proposals only; boxes stay `[~]`)

- **Box 1 (`SKILL.md` decision tables, error patterns, checklists, cited sources).** Proposal: refresh the counts it
  already carries — § Sources `<<SOURCES-ENTRIES>>` entries (`awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /'
  SKILL.md | wc -l` → `<<N>>`), gate registry `<<GATE-REG-N>>` (`gate registry rows conformant <<N>> lane verifiers;
  phantom 0`), `SKILL.md` `<<LINE-COUNT>>` of 600 lines; add the new `### Body craft` subsection as an inventory
  item. Do not change `[~]`.
- **Box 2 (end-to-end domain task logged in `LOG.md`).** Proposal: `<<if the C1 pages are re-fetched and re-read by
  a non-author seat, cite that as the round's executed domain task with its receipt; otherwise leave the existing
  cold-run evidence untouched>>`. Box stays `[~]`; promotion is operator-owned.
- **Box 3 (instructions executable without oral context).** Proposal: no new evidence — no fresh cold run this
  round; the line's existing "no fresh non-author cold run since" clause stays true. Explicitly record that this
  round did **not** create one.
- **Box 4 (no cross-domain bleed; `PROVINCE.md` still accurate).** Proposal: refresh the census pointer and the
  guard line — `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md
  --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20` (value pending; the current line
  cites the r49 entry and `:37`), and re-grep `grep -n '^## Adjacent' PROVINCE.md` after the § Adjacent append
  (`<<line>>`). Box stays `[~]`.

## 7. What this skeleton deliberately does not decide

- Whether the Q45 census lowers `N == 3` (a pre-data addendum, not this seat's call).
- The renumber map, the guard-proof path, snapshot names, access dates and quotes — wave-1 executor/scout work.
- Which staged entries are admitted: the skeleton has slots, not verdicts; a refusal needs an observed fact (Q62).
- The two counter sha256 values (the counters do not exist at HEAD: `ls verifiers/check_spec_craft.py
  verifiers/check_sibling_reread.py` → both absent; `.ufo/waves/round-74/snapshots/` → absent).
- Any backfill of the Move-log rounds 56–73.
