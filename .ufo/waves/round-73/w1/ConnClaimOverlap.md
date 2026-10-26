# ConnClaimOverlap — Cross-Claim Contention Map & Causal Separability (Round 73 Wave 1)

**Verdict.** The three frozen claims (C1 coverage, C2 depth, C3 consistency) are mutually orthogonal in their primary surfaces, but they possess a strict directional coupling through repository-wide invariants and metadata gates. Specifically: **(1)** C1 and C2 are causally separable in either order; **(2)** C2 and C3 are causally separable in either order; but **(3)** C1 and C3 are **order-dependent** for standing gate verification: if C3 lands and re-records `verifiers/corpus-baseline.json` before C1 lands, C1's subsequent landing adds a tracked corpus file (`corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`), immediately causing `verify_corpus_integrity.py` to fail (`DRIFT corpus.index.tracked_files: observed=137 expected=136`) and turning Gate 4 of C3's battery RED (`tip battery exit 0: 5 of 6`). The unique valid landing sequence that avoids any intermediate red gate is **C2 → C1 → C3** (or C1 → C2 → C3), with C3 performing the final unified baseline re-record.

---

## 1. Contention Map: Shared Files and Numbers

### 1.1 `SKILL.md` (Base: 568 lines, 72,715 B at `072048f`)
- **Observed Base State:** `wc -lc SKILL.md` → 568 lines, 72,715 bytes. Frontmatter description is lines 3–20 (18 lines, 1,019 characters). Gate registry is lines 427–491 (56 rows). Checklist is lines 200–394 (45 `- [ ]` boxes).
- **C1 Edit:** Appends 1 row to `## Gate registry` (after line 490) for `verifiers/check_cn_vendor_surfaces.py`.
- **C2 Edit:** Rewrites the 18-line frontmatter description (lines 3–20). Under `plans/round-73-addendum-1.md:47-49`, the frontmatter line count is invariant (`git diff --numstat <base> <rev> -- SKILL.md` inserted − deleted inside frontmatter = 0). C2 also adds a registry row in `## Gate registry` for `verifiers/check_own_description.py`.
- **C3 / Frontier Edit:** Appends 1 row in `## Gate registry` for `verifiers/check_report_pointers.py` (mined mistake gate).
- **Contention & Resolution:** Frontmatter (lines 3–20) and Gate registry (lines 427–491) do not overlap in diff hunk offsets. Because C2 preserves frontmatter line count, line numbers after line 20 do not shift. Registry additions append at the table footer (line 491), increasing `SKILL.md` from 568 to 571 lines, which remains well below the 600-line ceiling checked by `verifiers/verify_skill_checklist.py` (`trigger.line_budget: evaluated 568 — 568 lines within budget 600`).

### 1.2 `verifiers/checklist-baseline.json` (Base: 45 boxes)
- **Observed Base State:** 45 boxes, each pinned by `text_sha256`.
- **Claim Edits:** C1 touches only `corpus/` and § Gate registry; C2 edits only lines 3–20 (frontmatter); C3 touches verifier scripts. None of the three claims modifies any of the 45 `- [ ]` checklist boxes.
- **Contention:** Zero. `checklist-baseline.json` remains untouched.

### 1.3 `verifiers/floors-registry.json` (Base: 15 instruments)
- **Observed Base State:** `instrument_total: 15`. Floors are evaluated via `--self-test` on fixture sandboxes (`check_assertion_floors.py:211-225`).
- **Claim Edits:** Adding `check_cn_vendor_surfaces.py` (C1), `check_own_description.py` (C2), or `check_report_pointers.py` does not add entries to `INSTRUMENTS` in `check_assertion_floors.py` (none is a floored harness).
- **Contention:** Zero. No floor is lowered or dropped.

### 1.4 `verifiers/corpus-baseline.json` (Base: 135 tracked files expected, 136 observed at `072048f`)
- **Observed Base State:** `"corpus.index.tracked_files": {"mode": "equal", "expect": 135}`. Observed at base is 136 because `corpus/lessons/round-72-verifier-spotcheck.md` was committed unindexed by the r72 closure.
- **C1 Edit:** Adds `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (+1 tracked file).
- **C2 Edit:** Adds 0 files under `corpus/`.
- **C3 Edit:** Requires `verify_corpus_integrity.py` to exit 0 (`tip battery exit 0: 6 of 6`). C3 must index `round-72-verifier-spotcheck.md` and re-record `corpus-baseline.json`.
- **Contention:** **CRITICAL.** If C3 re-records baseline before C1 lands, it sets `expect: 136`. When C1 lands, tracked files becomes 137, causing `verify_corpus_integrity.py` to exit 1 (`DRIFT corpus.index.tracked_files: observed=137 expected=136`), breaking C3. C3 must re-record after C1 lands (setting `expect: 137`).

### 1.5 `corpus/README.md` Index Rows
- **Observed Base State:** 140 lines of coverage-map rows; line 140 is `| Round-72 lessons | ...`.
- **C1 Edit:** Appends coverage-map row for `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (and round-73 lesson row / frontier note).
- **C2 Edit:** 0 rows.
- **C3 Edit:** Needs `corpus/lessons/round-72-verifier-spotcheck.md` indexed so `verify_corpus_integrity.py` and `verify_corpus_independent.py` observe `unindexed: 0`.
- **Contention:** Both C1 and C3 append rows to the coverage-map table at line 140.

### 1.6 `verifiers/check_gate_registry.py` & § Gate Registry
- **Observed Base State:** 56 verifier files in `verifiers/`, 56 registry rows in `SKILL.md`. `check_gate_registry.py` is pinned in `check_tip_battery.py` by `INSTRUMENT_PINS` (`95ffed389f483c3d6f93db3c08dcfdb9a2240576`) and cannot be modified.
- **Claim Edits:** `check_gate_registry.py` dynamically scans every `.py`/`.sh` file under `verifiers/`.
  - C1 adds `verifiers/check_cn_vendor_surfaces.py` → MUST commit its `SKILL.md` row in the same commit.
  - C2 adds `verifiers/check_own_description.py` → MUST commit its `SKILL.md` row in the same commit.
  - Frontier adds `verifiers/check_report_pointers.py` → MUST commit its `SKILL.md` row in the same commit.
- **Contention:** If any verifier script is committed without its `SKILL.md` registry row, `check_gate_registry.py` immediately exits 1 (`gate registry rows conformant K of M`), breaking Gate 1 of C3's battery.

### 1.7 `PROVINCE.md` (Base: 70 lines)
- **Observed Base State:** 70 lines. `check_province_core.py` enforces that `## Frontier` and `## Adjacent` are byte-identical to base.
- **Claim Edits:** C1, C2, and C3 each have surface ground to record in `## Core`.
- **Contention & Resolution:** Separate bullets at EOF of `## Core` (lines 30–31) would create diff collisions. `ScribeQualityProvince` provides the clean synthesis: one consolidated bullet combining C1, C2, and C3 appended as the final line of `## Core` before line 31 (`## Frontier`). Neither claim touches `## Frontier` or `## Adjacent`.

### 1.8 `corpus/SOURCES.md` (Base: 219 lines, 142 S### rows)
- **Observed Base State:** 142 S### rows, last row is S216. Search-log split defect at lines 207–215.
- **C1 Edit:** Appends renumbered rows S217–S226 (10 rows) to `## Registry`.
- **Inherited Defect D3 Edit:** Appends search-log correction note at EOF (ScribeSourcesCorrection).
- **C2 & C3 Edits:** None.
- **Contention:** Appends occur in distinct sections (`## Registry` table vs EOF free prose). `scripts/sources-census.sh validate` exits 0.

### 1.9 `check_tip_battery.py` Guards vs C1/C2 Files
- `no-deletions`: C1 and C2 only add files / modify text. No base-tracked file deleted. PASS.
- `floors`: `floors-registry.json` untouched. PASS.
- `instrument-size`: Neither C1 nor C2 modifies the six instrument scripts (`check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `check_correction_sweep.py`). C3 re-sets the cap via addendum to accommodate the r72 baseline. PASS.
- `instrument-pin`: Six instrument scripts remain byte-identical to pinned blobs. PASS.
- `spotcheck-identity`: Existing base spotcheck files untouched. PASS.

---

## 2. Conflict Table

| File / Number | Claim A Edit | Claim B Edit | Landing Order & Resolution |
|---|---|---|---|
| `SKILL.md` (lines 3–20) | C2 rewrites 18-line description | C1/C3: no edit to lines 1–20 | C2 lands first or second. Addendum 1 requires frontmatter line delta = 0 so line citations below line 20 do not shift. |
| `SKILL.md` (lines 427–491, § Gate registry) | C1 adds row for `check_cn_vendor_surfaces.py` | C2 adds row for `check_own_description.py`; Frontier adds row for `check_report_pointers.py` | Append rows to table before line 492. Each verifier script MUST land in the same commit as its registry row to keep `check_gate_registry.py` exit 0. |
| `SKILL.md` (total line budget ceiling 600) | C1 adds 1 line | C2 adds 1 line (registry); C3 adds 1 line | No conflict: 568 + 3 = 571 lines <= 600 lines (`verify_skill_checklist.py` line 267 passes). |
| `corpus/README.md` (coverage-map table) | C1 appends row for `chinese-vendor-skill-surfaces-round73.md` | C3 appends row for `round-72-verifier-spotcheck.md` | Both append before line 141. C1 indexes r73 knowledge doc; C3 indexes r72 spotcheck. |
| `verifiers/corpus-baseline.json` (`expect: tracked_files`) | C1 adds 1 corpus file (136 → 137) | C3 re-records baseline for r72 spotcheck (135 → 136) | **C1 MUST LAND BEFORE C3.** If C3 lands first with `expect: 136`, C1's landing causes `verify_corpus_integrity.py` DRIFT (137 != 136), breaking C3 (`5 of 6`). |
| `PROVINCE.md` (§ Core bullets) | C1 adds Chinese-vendor skill surfaces | C2 adds own description; C3 adds tip battery | Use `ScribeQualityProvince` unified bullet: single line covering C1, C2, C3 at EOF of `## Core`. `## Frontier` and `## Adjacent` stay byte-identical. |
| `corpus/SOURCES.md` (rows vs notes) | C1 appends S217–S226 to `## Registry` | D3 appends search-log correction note at EOF | Table append vs EOF prose append. `sources-census.sh validate` exits 0 before and after. |
| `verifiers/check_gate_registry.py` (universe M) | C1 adds `check_cn_vendor_surfaces.py` | C2 adds `check_own_description.py` | Scans `verifiers/` dynamically. Each claim MUST commit its registry row in `SKILL.md` atomically with its verifier. |

---

## 3. Pairwise Causal Separability

### Pair 1: C1 (Coverage) and C2 (Depth)
- **C1 without C2:** Can C1 verify alone? **YES.** Command: `python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>`. C1 inspects only its knowledge entry, `SOURCES.md`, snapshots, and quotes. It does not inspect `SKILL.md` description.
- **C2 without C1:** Can C2 verify alone? **YES.** Command: `python3 -B verifiers/check_own_description.py --rev <rev>`. C2 inspects only `SKILL.md` frontmatter and runs `check_sibling_census.py`. It does not inspect Chinese vendor surfaces.
- **Separability:** Fully causally separable. Landing order is commutative (C1 → C2 or C2 → C1).

### Pair 2: C2 (Depth) and C3 (Consistency)
- **C2 without C3:** Can C2 verify alone? **YES.** Command: `python3 -B verifiers/check_own_description.py --rev <rev>`. C2 does not execute `check_tip_battery.py`.
- **C3 without C2:** Can C3 verify alone? **YES.** Command: `python3 -B verifiers/check_tip_battery.py --rev <rev>`. At base, `verify_skill_checklist.py` already passes on the existing description (`trigger.frontmatter_parses: evaluated 4`). C2's description rewrite is not required for C3 to pass.
- **Separability:** Fully causally separable. Landing order is commutative (C2 → C3 or C3 → C2), provided C2 commits its `SKILL.md` registry row atomically with `check_own_description.py`.

### Pair 3: C1 (Coverage) and C3 (Consistency)
- **C1 without C3:** Can C1 verify alone? **YES.** `check_cn_vendor_surfaces.py` does not invoke `check_tip_battery.py`.
- **C3 without C1:** Can C3 verify alone? **YES in a sandboxed isolation, BUT NOT STABLY ACROSS INTEGRATION.**
- **The Inseparability Mechanism:**
  If C3 lands first at commit $R_{C3}$, C3 indexes `round-72-verifier-spotcheck.md` and updates `verifiers/corpus-baseline.json` with `expect: 136`. C3's `check_tip_battery.py` passes `6 of 6`.
  When C1 then lands at commit $R_{C1}$, C1 introduces `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`.
  Now running Gate 4 of the battery:
  ```bash
  $ python3 -B verifiers/verify_corpus_integrity.py
  DRIFT   corpus.index.tracked_files: observed=137 expected=136
  5/9 checks pass; DRIFT: corpus.index.tracked_files, ...
  # Exit code 1
  ```
  And evaluating C3's battery on $R_{C1}$:
  ```bash
  $ python3 -B verifiers/check_tip_battery.py --rev <rev_C1>
  gate verifiers/check_gate_registry.py exit 0
  gate verifiers/check_assertion_floors.py exit 0
  gate verifiers/verify_skill_checklist.py exit 0
  gate verifiers/verify_corpus_integrity.py exit 1
  gate verifiers/verify_corpus_independent.py exit 0
  gate verifiers/check_correction_sweep.py exit 0
  tip battery exit 0: 5 of 6
  # Exit code 1
  ```
- **Separability Verdict:** C1 and C3 are **ORDER-DEPENDENT**. C3 cannot land before C1 without causing intermediate red standing gates.

---

## 4. UFO-FSD Connector Synthesis: The Proposed Move

- **Affected Axes:** Consistency (10), Depth (9), Coverage (8.5).
- **Proposed Move:** **Canonical Three-Stage Pipeline `C2 → C1 → C3` with Unified Metadata Closure.**
  1. **Stage 1 (Depth, C2):** Land frontmatter description rewrite (strictly 18 lines, line delta = 0) + `verifiers/check_own_description.py` + its `SKILL.md` § Gate registry row.
  2. **Stage 2 (Coverage, C1):** Land `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` + `corpus/SOURCES.md` S217–S226 + `snapshots/` + `verifiers/check_cn_vendor_surfaces.py` + its `SKILL.md` § Gate registry row + `corpus/README.md` coverage-map row.
  3. **Stage 3 (Consistency, C3 + Closure):** Land `check_tip_battery.py` M127 fix (`repo.resolve().parent`) + re-set `instrument-size` cap + index `corpus/lessons/round-72-verifier-spotcheck.md` in `corpus/README.md` + perform a single, definitive `verifiers/corpus-baseline.json` re-record reflecting the full 137-file corpus state + land `PROVINCE.md` unified Core bullet (`ScribeQualityProvince`).
- **Second-Order Effects:**
  - *Runtime:* Zero host mutation. Sandboxes remain isolated under `$TMPDIR`.
  - *Contract:* `PROTOCOL.md:398` strictly respected (gate registry stays in `SKILL.md`).
  - *Substrate:* M127 path resolution bug (`Path(".").parent == Path(".")`) is permanently closed.
  - *Verification:* Eliminates all baseline thrashing; all 3 claim predicates and all standing gates are monotonically green.
- **Risks & Verification:**
  - *Risk:* Omission of a registry row for an added verifier script breaks `check_gate_registry.py`.
  - *Verification Command:*
    `python3 -B verifiers/check_gate_registry.py --rev HEAD`
    Must output: `gate registry rows conformant 59 of 59 lane verifiers; phantom 0`.
