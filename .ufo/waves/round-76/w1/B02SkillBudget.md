# B02SkillBudget — SKILL.md line-budget measurement and insertion anchors (round 76, w1)

VERDICT: report-only — measured, no lane file edited, no claim data written. **`SKILL.md` at HEAD is 590 lines / 78,647 bytes; the 600-line box has 10 lines of room; the planned three additions land it at 593 lines (margin 7).** Every anchor below was produced by applying the current draft's two pins to a scratch clone of the committed base and reading the result back.

## 1. Baseline measurement (committed bytes)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git rev-parse HEAD
eab64394dba08a47f6797a2e23719be14675b44b
$ git log --oneline -3
eab6439 round-76: record validated wave role mix
7eed80e round-76: pre-data addendum fixes digest home and folded-render convention
4de12b6 round-76: wave w1 spec + dispatch (64 seats, v2 band, 34% attack share)
$ wc -l -c SKILL.md
  590 78647 SKILL.md
$ python3 -c "print(len(open('SKILL.md',encoding='utf-8').read().splitlines()))"
590
$ git rev-parse b7f13f4b39cbd43076a85568adca763a6f674e7a:SKILL.md
26ce572ed8dad7625083b09236e3a7943bdbbe47
$ git rev-parse HEAD:SKILL.md
26ce572ed8dad7625083b09236e3a7943bdbbe47
```

- **590 lines confirmed**, and the file ends with a newline (`wc -l` = `splitlines()` = 590).
- The lane advanced twice during this seat's run (`4de12b6` → `7eed80e` → `eab6439`); **`SKILL.md`'s blob is byte-identical at the round-76 base `b7f13f4` and at every HEAD seen** (`26ce572e…`), so every number here is rev-independent.
- The file is not byte-pinned by any frozen counter: `grep -rn 'SKILL\.md:[0-9]' corpus/` hits only sibling-lane files; no lane counter pins a `SKILL.md` line number. `check_tip_battery.py`'s `no-deletions` guard only requires `SKILL.md` to be present at `<rev>` (it is), and `verify_corpus_integrity.py` does not read `SKILL.md`.

## 2. Where the 600 comes from (the threshold is data, not a constant)

```
$ grep -n 'File ≤ 600' SKILL.md
285:- [ ] File ≤ 600 lines; overflow already moved to referenced depth files.
$ python3 - <<'PY'   # verifiers/verify_skill_checklist.py, loaded as a module
... boxes,_ = m.extract_boxes(lines)
... hits=[b for b in boxes if m.LINE_BOUND_BOX_RE.search(b['text'])]
PY
BASE boxes matching the line-bound pattern: 1
    ('Trigger-fidelity checklist', 285, 'File ≤ 600 lines; overflow already moved to referenced depth files. (e')
```

- `check_line_budget()` reads the threshold from **the box text**: `LINE_BOUND_BOX_RE` selects the box, `INT_RE` takes its first integer → **600**. Exactly **one** box matches, so the threshold is unambiguous.
- Consequence, measured: rewording that box to `File ≤ 620 lines` in a scratch clone **fails the checklist gate**, because `checklist-baseline.json` pins every box by `text_sha256`:
  ```
  REWORDED BOX: pass 10 fail 1 exit 1
     checklist.box_map_complete FAIL map entry trigger.14 has no live box (section 'Trigger-fidelity checklist');
       unmapped box at line 286 (section 'Trigger-fidelity checklist', sha256 3e23aabe9ca0…); …
  ```
  **The 600 ceiling cannot be raised by editing the box**; it would need a baseline re-record, which is a different claim. This matches the plan's refusal of considerthese proposal 1.
- The 600 is therefore a hard ceiling for this wave, and the only question is how many lines the round's additions consume.

## 3. Room and projection

| quantity | value | how measured |
|---|---|---|
| budget (box text) | **600** | `check_line_budget` reads the box |
| HEAD lines | **590** | `wc -l` = `splitlines()` |
| room at HEAD | **10 lines** | 600 − 590 |
| planned additions | **3 lines** (1 § Body craft rule row + 2 § Gate registry rows) | the current `build/skill-patch.md` pins |
| **projected final** | **593 lines** | applied and read back, not arithmetic |
| **margin to the box** | **7 lines** | 600 − 593 |

Measured by applying the current draft's two pins to a scratch clone of the committed base (`/fast/scratch/hyaku/kotoba-r76/B02SkillBudget/fleet/kotoba-shokunin`, a fleet-shaped `git clone --shared` with symlinked fleet root and sibling lanes):

```
$ wc -l -c SKILL.md
  593 81193 SKILL.md
$ git diff --numstat eab64394dba08a47f6797a2e23719be14675b44b -- SKILL.md
3	0	SKILL.md
$ python3 -B verifiers/verify_skill_checklist.py --json
FLEET-SHAPED PATCHED: pass 10 fail 1 exit 1        # 1 fail = fleet-shape artifact (MISSION.md sibling path)
… after symlinking the fleet's MISSION.md and the 17 sibling lanes:
FLEET-SHAPED PATCHED (with siblings): pass 11 fail 0 exit 0
   trigger.line_budget PASS 593 lines within budget 600 (from box at line 286)
   checklist.box_map_complete PASS 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)
```

Full battery on that same fleet-shaped patched tree, all exit 0:

| counter | exit | verdict line |
|---|---|---|
| `check_gate_registry.py --rev HEAD` | 0 | `gate registry rows conformant 62 of 62 lane verifiers; phantom 0` |
| `check_spec_craft.py --rev HEAD` | 0 | `spec craft pages backed 3 of 3` |
| `check_author_rules.py --rev HEAD` | 0 | `author-facing rules in SKILL.md 4 of 4` |
| `check_description_thresholds.py --rev HEAD` | 0 | `description thresholds backed 7 of 7 clients` |
| `check_skill_precedence.py --rev HEAD` | 0 | `skill precedence backed 5 of 5` |
| `check_instruction_authority.py --rev HEAD` | 0 | `authority ladder grounded 1 of 1` |
| `check_cn_vendor_surfaces.py --rev HEAD` | 0 | `registry home ok` |
| `check_correction_sweep.py --root .` | 0 | `correction sweep: 0 stale block(s)` |
| `verify_skill_checklist.py` | 0 | `pass 11, fail 0` |

(The 62-of-62 figure is 60 lane verifiers + the two round-76 counters, which existed as stubs in the scratch tree; see §6 for why both halves must land together.)

## 4. Exact insertion anchors (base line → patched line)

Heading text is quoted verbatim so the anchor is greppable, not just a number.

| anchor | base line | patched line | heading / surrounding text |
|---|---|---|---|
| `### Body craft — the specification's skill-creation guides` | 205 | 205 | § Compression rules › subsection heading — **do not duplicate or rename it** |
| § Body craft table header | 209 | 209 | `\| rule \| source \| what a skill author does \|` |
| last existing § Body craft row | 216 | 216 | `\| confirm discovery before trusting a path \| S224 quickstart \| …` |
| **NEW rule row** | — | **217** | inserted **after base line 216, before the blank line 217** that terminates the table |
| `## Trigger-fidelity checklist` | 218 | 219 | shifted +1 by the row above |
| line-budget box | 285 | **286** | `- [ ] File ≤ 600 lines; overflow already moved to referenced depth files.` — **text unchanged** |
| `## Gate registry` | **445** | **446** | shifted +1 (the rule row is above it) |
| last existing registry row | 512 | 513 | `\| \`verifiers/check_sibling_reread.py\` \| gate \| …` |
| **NEW registry row 1** | — | **514** | `\| \`verifiers/check_desc_craft.py\` \| gate \| …` — appended **immediately after base line 512, before the blank line 513** |
| **NEW registry row 2** | — | **515** | `\| \`verifiers/check_r75_routed_repairs.py\` \| gate \| …` |
| `## Sources` | 514 | 517 | shifted +3 |

**Two corrections to the current draft's own anchor table** (`build/skill-patch.md` line 11, and `w1/B13SkillPatch.md`):

1. **`## Gate registry` is at base 445, patched 446 — not 448.** The draft's "stays line 448" is stale from the earlier 5-line draft. Corroborates `w1/A06RevEvidence.md` finding 1.
2. **The +3 / 593 projection in the current draft is correct.** `w1/A33CritBudget.md` measured the *earlier* draft (2 preamble lines replaced by 3 = +4 total, 594); the current draft (14:06) dropped the preamble edit, so 590 + 3 = **593**. A33's arithmetic is right for the draft it read; the draft it read is no longer current.

## 5. Structural constraints the anchors must respect (all measured)

1. **The rule row must go INSIDE the existing § Body craft table.** `check_spec_craft.py`'s `skill_section()` runs from the exact heading `### Body craft — the specification's skill-creation guides` to the *next* heading (`HEADING_RE = ^#{1,3}\s`). Inserting a new `###` heading **between the heading and the table** empties that section:
   ```
   variant: new '###' heading right AFTER the Body craft heading
   spec craft pages backed 0 of 3 … exit 1
     best-practices: SKILL.md subsection has 0 counting row(s) citing S223 (want >= 2)
   ```
   A new `###` heading placed *after* the table is harmless for that counter (`3 of 3`, exit 0), but it would put the description-craft row outside the frozen § Body craft section, which is where C1 conjunct (c) looks for it. **Rule: no new heading between line 205 and line 217; the row goes at 217.**
2. **The new row must not cite S223/S224/S225.** `skill_problems()` counts, per page, only the rows whose text cites that page's `S###`; the drafted row cites `S213` only, so all three page counts are untouched (`3 of 3` measured on the patched tree).
3. **The two registry rows must sit in the same table as the existing rows.** `check_gate_registry.py` reads the **first table** under `## Gate registry` and stops at the first blank line. Placing the two rows after the blank line (a plausible paste) makes the table end early:
   ```
   variant: registry rows placed after the blank line
   verifiers/check_desc_craft.py   no registry rows naming it: 0 (need 1)
   verifiers/check_r75_routed_repairs.py  no registry rows naming it: 0 (need 1)
   gate registry rows conformant 60 of 62 lane verifiers; phantom 0   exit 1
   ```
4. **Row shape is accepted as drafted.** Splitting the drafted rows on `|` gives 8 cells for the registry rows (header order `name | kind | entry command | verdict map | self-test | pinned values | write scope | owner`) and 3 for the rule row; the verdict maps parse to exactly `0=clean, 1=failed, 2=could-not-evaluate` with no duplicated code; `kind=gate`; owner `kotoba`; write scope non-empty. Verified conformant: `62 of 62 … phantom 0`, exit 0.
5. **The trigger-fidelity checklist is untouched, so `verifiers/checklist-baseline.json` stays untouched.** Measured on the patched tree: `§ Trigger-fidelity checklist` holds **19 boxes** before and after; the section's bytes are identical (`diff <(sed -n '218,307p' base) <(sed -n '219,308p' patched)` → empty); the whole file's 45-box `(section, text_sha256)` multiset is unchanged; and `live == mapped` against the unmodified baseline. `checklist-baseline.json` needs **no** edit for this wave's SKILL.md change, and the plan's touch list does not name it.
6. **Frontmatter is byte-identical**, so C1 conjunct (d)'s audit numbers are unaffected by this patch: `diff <(sed -n '1,19p' base) <(sed -n '1,19p' patched)` → empty. Measured on the patched tree: rendered `description` length **1022** (clip-preserving `len(yaml.safe_load(...))`, the addendum's frozen convention) / **1021** stripped; first sentence **151** characters including the terminal period (**150** without), using the lane's own regex `^.*?[.!?](?=\s|$)` from `corpus/knowledge/render-mechanism-round7.md:18`. An entry audit table quoting 1022 / 151 stays valid at the tip **unless some other edit touches the frontmatter**.

## 6. Integration risks this measurement found (each reproduced; all outside this seat's write scope)

1. **The two registry rows and the two counter files must land in the same commit.** `check_gate_registry.py`'s universe is "every blob directly under `verifiers/` at the measured revision"; the rows are conformant only if exactly one row names each blob.
   - rows present, counter files absent → `PHANTOM verifiers/check_desc_craft.py` / `PHANTOM verifiers/check_r75_routed_repairs.py`, `conformant 60 of 60 … phantom 2`, **exit 1**;
   - counter files present, rows absent → `no registry rows naming it: 0 (need 1)` ×2, `conformant 60 of 62`, **exit 1**.
2. **The desc_craft row's pinned-values cell names `.ufo/waves/round-76/snapshots/MANIFEST.sha256`, which must exist at the measured revision.** With the manifest dropped from the commit: `verifiers/check_desc_craft.py  no pinned path .ufo/waves/round-76/snapshots/MANIFEST.sha256 does not exist`, `61 of 62`, **exit 1**. In the lane the whole `round-76/snapshots/` directory is currently **untracked** (`git status` → `?? .ufo/waves/round-76/snapshots/`), so the L1 must `git add` it for this row to be conformant.
3. **The new SKILL.md backticks create five new repo-rooted citation tokens** that must resolve from the repo root at the tip, or `trigger.citation_resolves` FAILs: `corpus/knowledge/description-craft-round76.md` ×3, `verifiers/check_desc_craft.py` ×3, `.ufo/waves/round-76/snapshots/MANIFEST.sha256` ×1, `verifiers/check_r75_routed_repairs.py` ×2, `corpus/lessons/round-75.md` ×1 (205 → 215 citation subjects). Measured: with the files absent → `trigger.citation_resolves FAIL line 214/215 … does not resolve`; with stub files present → `pass 11, fail 0, exit 0`. The SKILL.md edit is therefore **coupled** to the entry file, the two counters and the snapshot manifest landing.
4. **`check_tip_battery.py`'s `instrument-pin` guard is broken by the in-flight floors bump.** The D4 hygiene edit in the lane working tree (`verifiers/check_assertion_floors.py`, +22/−3 lines) produces blob `9cb860bda21ef8d24fcb0603aa85372b96f3ac41`, which is not in the guard's allow-list (`780f6fe5…`, `5034842…`):
   ```
   FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob 9cb860b… at HEAD is not a pinned blob
   guards 4 of 5; tip battery exit 0: 4 of 6   EXIT=1
   ```
   Measured on a fleet-shaped scratch clone with the bump applied; with the unmodified guard the same tree reads `guards 5 of 5`. Not this seat's files — flagged for the L1 and for the `w1/B24TipBatteryScript.md` seat.
5. **The two corpus gates are already red at the base**, so C2's R2 ("`noharm-at-tip.txt` … green integrity/independent stdout") cannot be satisfied by re-running them until the corpus index and baseline are re-recorded. Re-measured at `b7f13f4` (clean clone) and at HEAD: `verify_corpus_integrity.py --json` **exit 1** and `verify_corpus_independent.py --json` **exit 1**, with the same four DRIFTs (`corpus.index.tracked_files 145 vs 144`, `corpus.index.unindexed 1 vs 0` → `corpus/lessons/round-75-verifier-spotcheck.md`, `corpus.pointers.report_total 101 vs 99`, `corpus.pointers.commit_total 44 vs 43`). The base-battery receipt's `exit=0` for those two is a pipeline artifact: reproducing its exact shape (`… --json | tail -3; echo exit=$?`) prints `exit=0` while the verifier's own exit is 1. This corroborates `w1/B10RepairD2D3.md` F1; it is a **pre-existing red**, not caused by this round's SKILL.md edit.

## 7. Fallback compression plan (only if a later edit pushes the file past 600)

Measured on the patched tree; both levers keep every counter green in the fleet-shaped clone. **Neither is needed at 593.**

**Lever A — § Sources bullet continuations (preferred; touches no checklist box).** 14 bullets carry 57 continuation lines; joining each bullet's continuations onto its own line removes 57 lines → **593 → 536**.

| patched line | continuations | bullet (verbatim head) |
|---|---|---|
| 520 | 3 | `- Production skill files and what each demonstrates (wwkd, godspeed, sekhmet-l3,` |
| 525 | 1 | `- \`/home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md\` (8 files, 9–12 lines) —` |
| 528 | 1 | `- Host surfaces studied (opencode agent and command surfaces; 17 client AGENTS.md` |
| 530 | 5 | `- \`~/.local/share/opencode/opencode.db\` — literal-trigger mis-trips,` |
| 536 | 2 | `- \`~/.local/share/opencode/log/opencode.log\` — opencode offe` |
| 539 | 9 | `- opencode — npm \`opencode-ai\` 1.19.3 since round 47 (the \`~` |
| 549 | 6 | `- \`~/.omp/agent/sessions/**/*.jsonl\` (5842 files; \`session_i` |
| 556 | 15 | `- \`~/.local/bin/omp\` embedded JS (\`strings -n 6\`; cite ancho` |
| 572 | 1 | `- \`corpus/knowledge/harness-router-models-round9.m` |
| 574 | 1 | `- \`verifiers/README.md\` — what each lane verifier ` |
| 576 | 2 | `- \`corpus/knowledge/harness-verifier-round10.md\` —` |
| 580 | 5 | `- \`corpus/knowledge/render-mechanism-round7.md\` — mechanism ` |
| 586 | 4 | `- \`corpus/knowledge/dispatch-prompt-audit-round7.md\` — 12-it` |
| 591 | 2 | `- \`corpus/knowledge/alwayson-checklist-round7.md\` ` |

Measured on the 536-line variant: `verify_skill_checklist.py` exit 0 (`pass 11`), `check_spec_craft.py` exit 0, `check_author_rules.py` exit 0, `check_description_thresholds.py` exit 0, `check_correction_sweep.py` exit 0 (`0 stale block(s)`), `check_gate_registry.py` exit 0 (`62 of 62`).

**Lever B — checklist box continuations (larger, 107 lines → 593 → 486; baseline-safe but changes box *rendering*).** 40 boxes carry 107 continuation lines (58 in § Trigger-fidelity, 28 in § Agent-definition fidelity, 16 in § Dispatch-prompt fidelity, 5 in § Always-on). Joining a box's continuations onto its marker line leaves the *normalized* box text unchanged — `checklist-baseline.json` pins the normalized form ("first line minus `- [ ]` marker + continuations stripped, joined with one space; whitespace runs collapsed") — so the 45 box hashes and the baseline map are unchanged, and the checklist gate stays green (measured: `pass 11, fail 0`; box multiset identical; `live == mapped`).

**Lever B is the wrong first choice** for this round: it rewrites 107 lines of the four checklist sections, whereas Lever A removes 57 lines from § Sources prose only. Use Lever A first; use B only if the file must go well below 600.

**What must not be used as a lever:** the line-budget box itself (§2 — rewording it breaks the baseline map), the § Trigger-fidelity checklist box *text* (pinned by `text_sha256`), and the frontmatter (C1 conjunct (d) re-measures 1022/151 from it).

## 8. Reproduction commands (read-only on the lane; all scratch work under /fast/scratch)

```
# baseline
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git rev-parse HEAD && wc -l -c SKILL.md
git rev-parse b7f13f4b39cbd43076a85568adca763a6f674e7a:SKILL.md HEAD:SKILL.md
grep -n 'File ≤ 600' SKILL.md

# projection (scratch clone, fleet-shaped)
S=/fast/scratch/hyaku/kotoba-r76/B02SkillBudget
git clone --shared --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/fleet/kotoba-shokunin
#   + symlinks in $S/fleet/: PROTOCOL.md AXES.md CORPUS.md LOG.md SCORECARD.md AGENTS.md MANIFEST.json MISSION.md .ufo
#   + symlinks $S/fleet/<sibling>-shokunin -> /home/vgpnk/Projects/shokunin/<sibling>-shokunin
# apply the two ```text blocks of .ufo/waves/round-76/build/skill-patch.md to the base SKILL.md
wc -l -c SKILL.md && git diff --numstat <base> -- SKILL.md
python3 -B verifiers/verify_skill_checklist.py --json
python3 -B verifiers/check_gate_registry.py --rev HEAD
python3 -B verifiers/check_spec_craft.py --rev HEAD
```

No tools were installed for this seat; no lane file was created, edited or deleted by this seat; the scratch tree was removed before yielding.

**Verdict: SKILL.md is at 590 of 600 lines at HEAD, the planned three additions project to 593 (margin 7), the anchors above are the measured base→patched mapping, and the trigger-fidelity checklist needs no text change so `verifiers/checklist-baseline.json` stays untouched.**
