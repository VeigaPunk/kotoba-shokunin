# Kb79A04LogScoreDraft — round 79 record drafts (w1, seat Kb79A04LogScoreDraft)

**What this file is.** Insertion-ready text for four lane records, drafted in wave 1 so the L1 does not
write them under landing pressure: the `LOG.md` `## Round 79` entry, the `SCORECARD.md` round-79 axis
annotations plus one Capabilities-table row candidate, the four `SHONEN.md` evidence lines, and one
`corpus/QUALITY.md` candidate row (`Q74`).

**What this file is not.** It carries no claim data, no measured after-values and no verdicts. Every
value this seat could not observe is a `{{MARKER}}` (§1); every counter value quoted below is either
pasted verbatim from a receipt that exists at this instant (named inline) or attributed to the plan
text and marked as plan-stated. This seat ran no counter: `verifiers/check_allowed_tools.py` does not
exist yet (`ls verifiers/check_allowed_tools.py` → `No such file or directory`, this wave), and the
C1 after-value is produced by a commit that does not exist yet.

Authority read before drafting: `plans/round-79.md` (whole), `verifiers/verify_skill_checklist.py`
`check_governance_citations` + `citation_subjects` + `citation_resolve` + `DOCUMENTED LIMITS`
(lines 189–263, 1529–1680, 1752–1830), `verifiers/check_tip_battery.py` (docstring 1–70,
`INSTRUMENT_PINS` 125–141), `verifiers/verify_corpus_integrity.py:495-530` (report-pointer scope),
`../PROTOCOL.md:432-447` (SHONEN canonical form), `corpus/QUALITY.md` (header + Q36/Q45/Q50/Q65/Q70/Q71/Q72/Q73),
`SCORECARD.md:1-40,300-335,460-469` (rubric, Capabilities table, r71–r78 annotation style),
`LOG.md` tail (r73–r78 entries).

---

## 1. Markers (the L1 substitutes every one of these before the commit that carries it)

| Marker | Paste exactly | Where it comes from |
|---|---|---|
| `{{HASH_F2}}` | the F2 freeze commit id (C2 counter + control receipts, before any data) | plan § Landing order, item 1 |
| `{{HASH_C1}}` | the C1 repair lane commit id | plan § Landing order, item 2 |
| `{{HASH_C2}}` | the C2 data lane commit id | plan § Landing order, item 3 |
| `{{REV_FINAL}}` | the revision the final tip battery measured (the pushed lane tip) | final no-harm battery, plan § No-harm battery |
| `{{C1_RECEIPT}}` | the full lane-relative path of the C1 tip receipt, both forms concatenated or two paths, e.g. `.ufo/waves/round-79/receipts/<name>.txt` — **must exist before the LOG commit** | the C1 after-receipt |
| `{{C2_BASE_RECEIPT}}` | the full lane-relative path of the frozen counter's base control (C0) receipt | F2 control run |
| `{{C2_N}}` | the integer the frozen C2 counter prints at `{{REV_FINAL}}` | C2 after-measurement |
| `{{C2_SCRIPT}}` | the integer the script-only world (control C4) scores on the same frozen counter | F2/w2 control run |
| `{{SHA_CTR}}` | sha256 of `verifiers/check_allowed_tools.py` at F2 | `receipts/freeze-shas.txt` part 2 |
| `{{SKILL_RULE_SECTION}}` | the `SKILL.md` section heading the C2 rule line lands under | C2 data commit |
| `{{CENSUS_R79}}` | the guard's printed row (e.g. `rows 20 verified 20; province rows 20 matched 20`) | re-run at `{{REV_FINAL}}` |
| `{{M140}}` | the round-79 mistake id in `corpus/lessons/round-79.md` § Mistakes (next free id is M140: `grep -rn 'M14[0-9]' corpus/` → no match at base, exit 1) | round lesson |

Substituting `{{C1_RECEIPT}}`, `{{C2_BASE_RECEIPT}}`, `{{CENSUS_R79}}` and `{{SKILL_RULE_SECTION}}`
creates governance citation subjects (paths that must resolve from the lane root at the measured
revision). Run the check in §6 after substitution — never before.

---

## 2. `LOG.md` — `## Round 79` entry (append at end of file; append-only, no earlier line touched)

```markdown
## Round 79 — C1 consistency (the lane's tip battery at 6 of 6), C2 depth (allowed-tools semantics per client, sourced)

- **Trigger:** rounds 77 and 78 ended as honest stops on predicates a do-nothing world reached
  (`.ufo/waves/round-77/w1/C01CritDoNothing.md:5-8`: `description craft backed 6 of 6` from a 489-byte
  stub, `r75 routed repairs closed 4 of 4` from pasted text) and on a final no-harm battery that was
  never run — round 78's own entry records the omission, and the r79 base battery is what it cost:
  `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 in both invocation forms, with only
  `check_correction_sweep.py` at exit 0 and five gates at exit 1
  (`.ufo/waves/round-79/receipts/tipbattery-base-dot.txt`,
  `.ufo/waves/round-79/receipts/tipbattery-base-abs.txt`, measured at
  `b10bcbc6b00f8f56b202ccbadca311007b5b463c`). Nothing from either frozen r77/r78 predicate is reused.
- **Action:** plan `plans/round-79.md` (F1 `2c56622`, F2 `{{HASH_F2}}` — the C2 counter and its
  control receipts, committed before any data); C1 repair `{{HASH_C1}}` — `verifiers/check_tip_battery.py`
  is frozen and unedited (sha256 `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`) and
  its six gate scripts are instrument-pinned, so the repair is records and tree state only: the two
  missing `SKILL.md` gate-registry rows, the assertion-floor self-test cause without lowering a floor,
  the corpus index and baseline, and the one dead governance token at LOG.md:2818; C2 data
  `{{HASH_C2}}` — entry `corpus/knowledge/allowed-tools-surfaces-round79.md`, rows S226–S231 appended
  to `corpus/SOURCES.md`, six raw snapshots under `.ufo/waves/round-79/snapshots/`, counter
  `verifiers/check_allowed_tools.py` (frozen at F2, sha256 `{{SHA_CTR}}`), the `SKILL.md` rule line
  (`{{SKILL_RULE_SECTION}}`) and its registry row, the `PROVINCE.md` § Core bullet, the lesson
  `corpus/lessons/round-79.md` and QUALITY Q74.
- **Outcome:** `python3 -B verifiers/check_tip_battery.py --rev {{REV_FINAL}}` prints `guards 5 of 5;
  tip battery exit 0: 6 of 6` and exits 0 in the `--repo .` form run from the lane root and in the
  absolute form, each captured with its own exit status in its own receipt (`{{C1_RECEIPT}}`); the
  base value above is unchanged and stays on record.
  `python3 -B verifiers/check_allowed_tools.py --rev {{REV_FINAL}}` prints
  `allowed-tools surfaces backed {{C2_N}} of 6` and exits 0; the base control on the same frozen
  counter prints `allowed-tools surfaces backed 0 of 6`, exit 1 (`{{C2_BASE_RECEIPT}}`; the plan
  declared the same base value before the counter existed). The script-only world scores
  `{{C2_SCRIPT}} of 6`, so the headline claims form, tokens, quotes and pins only, and the per-row
  grant-semantics labels are assigned to named non-author reviewers (Q71).
  Round-start census `.ufo/waves/round-79/receipts/census-before.txt` exited 0 with the existing W04
  warnings; round-end census and the complete no-harm battery at the final tip sit beside it in
  `.ufo/waves/round-79/receipts/`, each receipt naming the revision it measured (Q36/Q50).
- **Limits:** the battery counts six gate exits inside five diff-scope guards; it does not show that
  any gate's rule captures its claim, and this round's repair set is records-level rather than a gate
  change. C2's counter measures committed bytes only (no network at measurement) and the six surfaces
  are a census population of six, so a page that moves drops N by one against a target of five. A
  repair that had needed an instrument edit would have stopped C1; the kill rule was not reached.
- **Pointer:** `plans/round-79.md`, `.ufo/waves/round-79/receipts/`, `.ufo/waves/round-79/w1/`,
  `corpus/lessons/round-79.md`; the fleet report is outside this repository and is written last
  (a quoted meta pointer the governance gate excludes and counts): "`../.ufo/reports/round-79/kotoba.md`".
```

**Before you commit this entry.** It is retrospective: the C1 repair set in the second bullet is
plan-derived (`plans/round-79.md` § C1 target, `check_gate_registry.py` detail) — replace it with what
actually landed, and keep the enumeration only if every item is true of `{{HASH_C1}}`. Do not add a
sentence about a gate that was not re-run.

### 2.1 Why the trailing fleet-report token is quoted

The r76 entry wrote the same kind of pointer unquoted (`.ufo/reports/round-76/kotoba.md`) and that
single token is the whole `governance.citation_resolves` FAIL at base:

```
python3 -B verifiers/verify_skill_checklist.py --json
→ governance.citation_resolves FAIL 1312 | LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not
  resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; 10 quoted meta-finding(s),
  3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused
```

The exclusion is narrower than "a quoted token": the token must sit inside a backticked inline span
with the quote **outside** the span and closed on the same line, otherwise the gate either ignores it
(no span) or counts it as a live subject (`at_start` false). §6 records the three shapes measured
against `citation_subjects`. The two alternatives were checked and rejected for this round:

- the corrected form `../.ufo/reports/round-79/kotoba.md` (what the round-65 `GOVERNANCE_CORRECTIONS`
  rows rewrite dead fleet pointers to) resolves from the lane root into the fleet root, and `../` from
  this lane is `/home/vgpnk/Projects/shokunin`: `test -e ../.ufo/reports/round-76/kotoba.md` → true
  today, `test -e ../.ufo/reports/round-79/kotoba.md` → absent today, and the plan writes the fleet
  report **last**, after the lane tip the final battery measures — so that token is dead exactly at
  the revision C1 is scored on.
- Registering a new `GOVERNANCE_CORRECTIONS` row is an edit to `verifiers/verify_skill_checklist.py`,
  whose blob is pinned (`8d44c063…`, `6aab1684…`); a new row changes the blob and fails the
  instrument-pin guard. The r76 dead token therefore cannot be corrected through the corrections table
  this round (see §7, finding F1).

If the L1 prefers no fleet pointer at all in the entry, delete the last clause — the entry still
resolves completely; do not unquote it.

---

## 3. `SCORECARD.md` — round-79 axis annotations (append after the r78 paragraph, before `## planned`)

One paragraph, same shape as r71–r78 (append-only; verdicts belong to the non-author closure).

```markdown
**Round 79 axis annotations (append-only; verdicts belong to the non-author closure).** *Consistency (C1 calibration sub-axis, score held 10):* `python3 -B verifiers/check_tip_battery.py --rev <rev>` (frozen bytes sha256 `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`, not edited this round; five diff-scope guards: no-deletions, floors, instrument-size ≤ 40 added and ≤ 40 deleted, instrument-pin, spotcheck-identity) — at base `b10bcbc6b00f8f56b202ccbadca311007b5b463c` it prints `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1, in both the `--repo .` and the absolute form (`.ufo/waves/round-79/receipts/tipbattery-base-dot.txt`, `.ufo/waves/round-79/receipts/tipbattery-base-abs.txt`; only `check_correction_sweep.py` exits 0, five gate lines exit 1) → `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0 in both forms at `{{REV_FINAL}}` (`{{C1_RECEIPT}}`), the repair being records and tree state only because the counter pins its six instruments; bound: the printed count is six gate exit statuses and a form-level guard set, so it shows the lane's record matches the gates it runs and says nothing about whether a gate's rule captures its claim. *Depth (C2, sourced, score held 9):* `python3 -B verifiers/check_allowed_tools.py --rev <rev>` (built this round from `verifiers/check_cn_vendor_surfaces.py`, frozen at F2 `{{HASH_F2}}`, sha256 `{{SHA_CTR}}`) — `allowed-tools surfaces backed 0 of 6`, exit 1 at base (`{{C2_BASE_RECEIPT}}`) → `allowed-tools surfaces backed {{C2_N}} of 6`, exit 0 at `{{REV_FINAL}}`, over entry `corpus/knowledge/allowed-tools-surfaces-round79.md`, rows S226–S231 in `corpus/SOURCES.md` and six sha256-pinned raw snapshots under `.ufo/waves/round-79/snapshots/` (conjuncts (a)–(f) per surface plus tree conjuncts (g)–(i); one frozen grant label per row: `pre-approves` claude, `metadata-only` factory, `experimental` spec/msaf/pi, `unstated` vibe); the script-only world scores `{{C2_SCRIPT}} of 6`, so the headline claims form, tokens, located quotes and pins and the per-row semantics labels are reviewer judgement (Q71); population census 6 of 18 skill pages state the field (`receipts/c2-census-l1.txt`, `{{CENSUS_R79}}` re-run census at the tip); bound: exact host+path-prefix identity (Q32), quote after the first heading and free of banner/subtitle lines (Q70), committed bytes only — a page that moves drops one surface against a target of five.
```

### 3.1 Capabilities-table row candidate (do **not** insert until measured)

`SCORECARD.md:320` says rows enter only through a round that demonstrates the capability running.
So this row enters **only after the L1's measurement** — paste it after the L1 has the frozen
counter's after-receipt in hand, never from the plan.

```markdown
| allowed-tools surfaces counter (enter only after the L1's measurement) | reads the six frozen skill pages' raw committed snapshots plus their 11-cell `corpus/SOURCES.md` rows and decides three ways per surface: (i) host+path-prefix identity against a frozen six-host table, (ii) a row per surface whose ≥3 backticked tokens (including `allowed-tools`, one value-form and one grant-semantics token) each occur word-bounded in that surface's snapshot, (iii) a 5–25-word located quote that contains `allowed-tools`, lies after the page's first heading, is not a banner/subtitle line, and carries the page token that grounds the row's single frozen grant label; plus sha256 pins that must agree in the counter, the row's anchor fetch record and `MANIFEST.sha256`, and tree conjuncts (a `SKILL.md` rule line + registry row, a `PROVINCE.md` § Core bullet); prints `allowed-tools surfaces backed N of 6`, exits 0 only at N ≥ 5, reads a `--rev`'s committed bytes with no network, and scores a script-only scrape world separately so its headline cannot claim more than that world reaches (Q71); bounded: form, tokens, quotes and pins are counted; whether a grant label is true of its page is reviewer judgement | `python3 -B verifiers/check_allowed_tools.py --rev {{REV_FINAL}}` → `allowed-tools surfaces backed {{C2_N}} of 6`, exit 0; base `0 of 6`, exit 1; script-only world `{{C2_SCRIPT}} of 6` | 79 |
```

Name for the table's first cell: **allowed-tools surfaces counter** (the L1 may shorten to
`allowed-tools client-map counter`; keep it distinct from the round-73 `vendor skill surfaces` row).

### 3.2 Axis-table cells (outside this seat's drafts — flagged, not written)

The `## axes` rows `depth` and `consistency (calibration sub-axis)` carry a `Last change` cell. This
seat does not draft replacements: the rows' evidence text is the L1's judgement and the r79 evidence is
the annotation paragraph above. If the L1 updates them, the new text must cite this annotation and
keep the existing round-54 / round-60 evidence (append the round-79 marker, never replace the history).

---

## 4. `SHONEN.md` — four evidence lines (keep `[~]`; no non-author verifier exists before closure)

`../PROTOCOL.md:432` allows the canonical seed's four boxes plus one indented evidence line per box,
marks confined to the box character: `[x] <verifier-id>` or `[~]` with a resolvable pointer. No box
may be added, removed or reworded, and this round has **no** non-author verifier before closure, so
all four stay `[~]`.

- **Box 1** — `SKILL.md contains real decision tables, error patterns, checklists, cited sources`
  → **append one clause** to the existing evidence line (the rest of the line stays byte-identical):
  `; round 79 adds the allowed-tools rule line (§ {{SKILL_RULE_SECTION}}) citing corpus/knowledge/allowed-tools-surfaces-round79.md and the verifiers/check_allowed_tools.py gate-registry row at {{REV_FINAL}}`.
- **Box 2** — `At least one end-to-end domain task executed and logged in LOG.md`
  → **unchanged**. Round 79 ran no cold end-to-end task; its claim work is record and counter work.
- **Box 3** — `Instructions executable by an agent without oral context`
  → **unchanged**. The box's opening gap (no cold run since round 8) is not closed this round and must
  not be upgraded: `[~]` stays, and the round-8 `B1`/`B2` break points stand.
- **Box 4** — `No cross-domain bleed (PROVINCE.md still accurate)`
  → **append one clause**: `; round 79 opens no sibling surface — its PROVINCE.md change is one § Core bullet (the guard pins § Adjacent, not § Core) and python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md prints {{CENSUS_R79}} at {{REV_FINAL}}`.

The box-4 clause is only writable after that guard is actually re-run at the tip (Q73's rule that a
pinned section's neighbour edit is re-measured). If the run is not made, drop the clause and leave the
line byte-identical — an unmeasured `{{CENSUS_R79}}` is exactly the defect this round is repairing.

---

## 5. `corpus/QUALITY.md` — candidate row `Q74` (append after Q73)

```markdown
| Q74 | A round's landing sequence carries the tip battery as a required step, not as a report nicety: both invocation forms of the battery are run at the revision the round closes on, each receipt prints the revision it measured and the command's own exit status, and any value a report, LOG entry or closure record states is pasted from that receipt. A round whose close leaves the battery red or unrun records the exact red set as open debt inside its own LOG entry, and a closure that accepts the round without the receipt names that omission as a defect of the closure. Extends Q50 (a stated tip result needs a committed tip receipt) and Q65 (the plan's base run); does not supersede either. | round landing sequences, closure records, LOG entries and reports that state a round's tip state | M{{M140}} (`corpus/lessons/round-79.md` § Mistakes: rounds 76–78 closed with the no-harm battery unrun — round 78's LOG entry says so in terms — and the r79 base battery reads `tip battery exit 0: 1 of 6` with five gates red, `.ufo/waves/round-79/receipts/tipbattery-base-dot.txt`) | — |
```

### 5.1 Duplicate check (Q50 / Q65 / Q36)

| existing row | what it already requires | what Q74 adds | verdict |
|---|---|---|---|
| Q50 | every gate result a report **states** for the lane tip has a committed receipt naming that exact revision | Q74 bites when nothing is stated: silence no longer closes a round, and the obligation sits on the **closure record** as well as the report | extends, does not duplicate |
| Q65 | the plan's no-harm battery is run at its **own base** before the plan freezes, reds named red | Q74 is the close-side half: the run at the **closing tip**, in both forms, as a landing step | extends |
| Q36 | a receipt names the revision it measured, inside the receipt | Q36 is the receipt's own form; Q74 is who must run one, when, and what a missing one costs | no overlap |

New thing it requires, stated plainly: **the battery run is a landing step, and a closure without it
is defective** — Q50 forbids asserting a result without a receipt, Q74 forbids closing without running
one, including the rounds whose claims never touch the six gates (r76–r78 accrued three rounds of
silent debt that way). If the L1 reads that as already covered by Q50's first clause, the honest
answer is `no new criterion` and this row is dropped — do not append a row that adds nothing.

`{{M140}}` must be filled only after `corpus/lessons/round-79.md` § Mistakes records the class
(`landing`: three rounds closed without the no-harm battery; captured-by Q50/Q65, which existed and
were not run; fix: C1 itself plus the Q74 closure line). A QUALITY row whose `grounded in` names a
mistake that does not exist is worse than no row.

---

## 6. Token audit — the tokens in §2 and §3, checked by the governance gate's own predicate

**Mechanism (measured here, not assumed).** A token becomes a citation subject only inside a
backticked inline span (`verify_skill_checklist.py:350`), and the quoted exclusion needs the double
quote *outside* the span, closing on the same line: `at_start` true and `at_line_end` false
(`:1612-1657`). Three shapes were run through `citation_subjects(..., exclude_quoted=True,
exclude_schematic=True)` against a synthetic `Pointer:` line:

| line shape | subjects | quoted |
|---|---:|---:|
| `` `../.ufo/reports/round-79/kotoba.md` `` | 1 (dead) | 0 |
| `` "../.ufo/reports/round-79/kotoba.md" `` (no backticks) | 0 | 0 |
| `` "`../.ufo/reports/round-79/kotoba.md`" `` (quote outside the span, one line) | 0 | 1 |

§2 uses the third shape, so the gate **counts** the exclusion (base `10 quoted meta-finding(s)` → 11
if the entry is pasted as drafted) instead of silently not seeing an unbackticked path.

**Command (run; the table below is its output).** Each fenced `markdown` block is audited on its own,
so this draft's commentary (§2.1, §7) cannot pollute the audit:

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 - <<'EOF'
import sys; sys.path.insert(0,"verifiers")
import verify_skill_checklist as V
from pathlib import Path
repo = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
lines = Path(".ufo/waves/round-79/build/Kb79A04LogScoreDraft.md").read_text(encoding="utf-8").splitlines()
blocks, cur, head, inblk = [], [], None, False
for i, ln in enumerate(lines, 1):
    if ln.startswith("```markdown"):
        inblk, cur = True, []
        head = next((l for l in reversed(lines[:i-1]) if l.startswith("#")), "(none)")
        continue
    if inblk and ln.startswith("```"):
        blocks.append((head, cur)); inblk = False; continue
    if inblk: cur.append(ln)
for head, blk in blocks:
    subs, excl = V.citation_subjects(blk, source="blk", exclude_quoted=True, exclude_schematic=True)
    dead = [s["token"] for s in subs if not V.citation_resolve(s["token"], repo)]
    print(head, "| subjects", len(subs), "| quoted", [s["token"] for s in excl["quoted"]], "| dead", dead)
EOF
```

Measured output (2026-10-27, lane at `b10bcbc6b00f8f56b202ccbadca311007b5b463c` + untracked
`.ufo/waves/round-79/`):

| block | subjects | quoted exclusions | dead now |
|---|---:|---|---|
| §2 LOG entry | 16 | `../.ufo/reports/round-79/kotoba.md` | `corpus/knowledge/allowed-tools-surfaces-round79.md`, `verifiers/check_allowed_tools.py` ×2, `corpus/lessons/round-79.md` ×2 |
| §3 SCORECARD annotations | 8 | — | `verifiers/check_allowed_tools.py`, `corpus/knowledge/allowed-tools-surfaces-round79.md` |
| §3.1 Capabilities row | 2 | — | `verifiers/check_allowed_tools.py` |
| §5 QUALITY row | 2 | — | `corpus/lessons/round-79.md` |

Every dead token is **prospective** — created by a commit that lands before the record which cites it.
Nothing else in the drafted text is dead, and the two live-now "already" tokens that matter (the base
receipts) resolve.

| token | today | must resolve by |
|---|---|---|
| `.ufo/waves/round-77/w1/C01CritDoNothing.md:5-8` | OK | already |
| `.ufo/waves/round-79/receipts/tipbattery-base-dot.txt` | OK | already |
| `.ufo/waves/round-79/receipts/tipbattery-base-abs.txt` | OK | already |
| `.ufo/waves/round-79/receipts/census-before.txt` | OK | already |
| `.ufo/waves/round-79/receipts/` | OK | already |
| `.ufo/waves/round-79/receipts/c2-census-l1.txt` | OK | already |
| `.ufo/waves/round-79/w1/` | OK | already |
| `.ufo/waves/round-79/snapshots/` | OK | already (directory; the six snapshots land at C2) |
| `.ufo/waves/round-79/build/` | OK | already (holds this file) |
| `plans/round-79.md` | OK | already |
| `corpus/SOURCES.md` | OK | already |
| `corpus/QUALITY.md` | OK | already |
| `corpus/knowledge/sibling-overlap-census-round49.md` | OK | already |
| `verifiers/check_tip_battery.py` | OK | already |
| `verifiers/check_cn_vendor_surfaces.py` | OK | already |
| `verifiers/verify_skill_checklist.py` | OK | already |
| `verifiers/verify_corpus_integrity.py` | OK | already |
| `verifiers/check_sibling_census.py` | OK | already |
| `../PROTOCOL.md` | OK | already |
| `verifiers/check_allowed_tools.py` | DEAD (not built yet) | F2 `{{HASH_F2}}` |
| `corpus/knowledge/allowed-tools-surfaces-round79.md` | DEAD (not written yet) | C2 `{{HASH_C2}}` |
| `corpus/lessons/round-79.md` | DEAD (not written yet) | the commit carrying the LOG entry and Q74 |
| `../.ufo/reports/round-79/kotoba.md` (quoted, inside a span) | excluded, counted | never — meta pointer |
| `LOG.md:2818` | not a subject (`LOG.md` is not a citation root) | n/a |
| `{{C1_RECEIPT}}`-shaped markers | not subjects (no citation root, `{` is not a skip char but the token has no root prefix) | substitute a real path **and** re-run this audit |

Run the gate itself after insertion:

```
python3 -B verifiers/verify_skill_checklist.py --json
# base: governance.citation_resolves FAIL 1312 | LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not
#   resolve …; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused,
#   4 recorded correction(s) excused
# after: PASS, quoted meta-finding(s) 11 (10 + the r79 fleet pointer), and no r79 line in the FAIL detail
```

**Do not paste §2.1 or §7 into `LOG.md` or `SCORECARD.md`.** Both quote dead examples inside backticks
for documentation (`.ufo/reports/round-76/kotoba.md`, `../.ufo/reports/round-79/kotoba.md`); in a
governance file those would be live subjects and red.

---

## 7. Findings for the L1 (found while drafting; not claims, not repairs)

**F1 — the r76 dead token cannot be repaired through `GOVERNANCE_CORRECTIONS` this round.**
`GOVERNANCE_CORRECTIONS_HORIZON = 2723` and the last row is line 2723; the dead subject sits at
LOG.md:2818, so it needs a new row *and* a raised horizon — both inside
`verifiers/verify_skill_checklist.py`, whose blob at base is `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f`
(one of the two pinned blobs in `verifiers/check_tip_battery.py:131-133`). A new row changes that blob
→ `instrument-pin` guard red → the battery cannot read 6 of 6. The pin-compatible repairs are data:
either the corrected-form notice with an in-tree resolution, or making the cited lane path exist at the
measured revision (the token is a plain existence test, `citation_resolve`). Measure the chosen repair
with the frozen counter on its own commit before the C1 commit is called done — a repair that needs an
instrument edit is the plan's kill rule.

**F2 — both-forms evidence must be two receipts.** The counter's printed line carries the fleet root,
the guard tally and the gate count, not the invocation form (`check_tip_battery.py:392-399`); the
`Kb79CR01C1Target` seat reached the same conclusion independently. One run cannot evidence the
"both forms" clause, so C1's receipt must be two invocations with their own exit statuses (or one file
with both, each labelled).

**F3 — the checklist inside a clone path fails on the name/directory pair.** `Kb79MT01BatteryGates`
measured `trigger.name_directory` failing in its scratch clone (the check compares the frontmatter
`name` to the repo directory name). The battery's sandbox clones into `<parent>/kotoba-shokunin`
(`check_tip_battery.py:175-203`), so a sandbox whose parent directory name differs is a measurement
artifact, not a gate verdict — do not read one as a red gate.

**F4 — SKILL.md budget.** `verify_skill_checklist.py` `trigger.line_budget` = 600 lines; base 590;
`Kb79S07BudgetCensus` measured the planned +7 lines at 597. This draft adds nothing to `SKILL.md`
(all four records above live outside it).
