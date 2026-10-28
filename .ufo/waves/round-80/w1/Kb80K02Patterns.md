# Kb80K02Patterns — cross-claim pattern map, round 80 w1

Seat: executor (leaf, no spawns), `Kb80K02Patterns`. Lane HEAD measured: `c2f69d4` (plan freeze). `git diff --stat 398cbe1 c2f69d4 -- corpus verifiers SKILL.md` is empty, so every corpus and gate measurement below is the base 398cbe1 corpus. Read-only throughout; no lane file, index or commit touched. No tool installed. Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80K02Patterns` removed before yield. Receipts copied to `.ufo/waves/round-80/build/Kb80K02Patterns/`:
`sweep.txt` (sha256 prefix `90ed5ee5…`, commands inline), `integrity-head.json`, `independent-head.json`, `registry-base.txt`.

## 0. Headline findings (both change the L1's C1 plan)

1. **The plan's named `commit_unresolvable` instances are wrong.** Plan § C1 says the two gate-red tokens are `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`. Measured at HEAD (`verify_corpus_integrity.py --no-baseline --json` and `verify_corpus_independent.py --json`, both exit 1): `commit_unresolvable = 2`, detail `corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00` and `corpus/SOURCES.md:172: 7bb48f2…`. Those are rows S230 (pi-mono skills page, "resolved to `badlogic/pi-mono` commit `7bb48f21…`") and S231 (Mistral Vibe, "served commit `7bb48f21…`"). Both are third-repository objects, absent from lane and fleet (`git cat-file -t` rc=128 in both). The gemini and zed tokens are **not counted by either gate** (see §1.2). This is the stale-premise class (r73 M132 precedent).
2. **Consequence for C1.** The tip battery's six guards include both corpus gates (`verifiers/check_tip_battery.py:149-150`). Repair 5 as worded in the plan (classify `owner/repo@<hex>`) does not match S230/S231, whose owner/repo sits in a separate backtick span before the word `commit`. Unless repair 5 also recognises `` `owner/repo` commit `<hex>` ``, or S230/S231 get a correcting row, both gates stay red and `tip battery exit 0: 6 of 6` is unreachable. Flagged to L1 (see §3).

## 1. Pattern 1 — the external-commit grammar class

### 1.1 Gate visibility (measured)
- `verify_corpus_integrity.py:151` `COMMIT_RE = (?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)``; `verify_corpus_independent.py:126` `COMMIT_RE = …commit\s+`([^`\s]+)``. Both require the word `commit` immediately before a backticked token.
- The owner/repo@hex grammar (`zed-industries/zed@`cfb894a5``) has no `commit` word; a sweep for `commit `…/…`` returns none. **Both gates are blind to the whole owner/repo@hex class today.** Repair 5 therefore adds detection, it does not re-classify existing counts: `commit_total` will move on re-record.

### 1.2 Owner/repo@hex tokens by file (sweep: `sweep.txt` §A, 25 hits)
Pinned = `spotcheck-identity` (`check_tip_battery.py:318-332`: every base `corpus/lessons/*-verifier-spotcheck.md` must be byte-identical at `<rev>`). Editable = not pinned; SOURCES.md rows are append-only (correction only via a new `supersedes` row), so SOURCES hits are restricted, not free.

| File | Lines | Token(s) | Pinned? |
|---|---|---|---|
| `corpus/lessons/round-52-verifier-spotcheck.md` | 99, 100 | `anomalyco/opencode@cdf1c200`, `github/copilot-cli@7ea98dfc` | **pinned** |
| `corpus/lessons/round-54-verifier-spotcheck.md` | 37, 148 | `google-gemini/gemini-cli@451a02ff` | **pinned** |
| `corpus/lessons/round-71-verifier-spotcheck.md` | 102 | `agentskills/agentskills@69ef37e` | **pinned** |
| `corpus/lessons/round-75-verifier-spotcheck.md` | 36 | `anthropics/skills@dbd4588` | **pinned** |
| `corpus/knowledge/skill-listing-thresholds-round54.md` | 29, 44 | `google-gemini/gemini-cli@`451a02ff` (backtick form) | editable |
| `corpus/knowledge/skill-eval-artefacts-round70.md` | 5, 6 | `agentskills/agentskills@69ef37e…` | editable |
| `corpus/lessons/round-53.md` | 27, 44 | `microsoft/vscode-docs@fd64d648`; `zed-industries/zed@`cfb894a5` (the M45 rewrite) | editable |
| `corpus/lessons/round-54.md` | 13, 52 | `zed-industries/zed@`cfb894a5` (M45 record; line 52 the same rewrite) | editable — **must not be rewritten** (plan; M45) |
| `corpus/lessons/round-55.md` | 54 | `google-gemini/gemini-cli@451a02ff` | editable |
| `corpus/lessons/round-71.md` | 6, 13 | `agentskills/agentskills@69ef37e…`; `anthropics/skills@dbd4588f…` | editable |
| `corpus/lessons/round-74.md` | 37 | `agentskills/agentskills@69ef37e` | editable |
| `corpus/README.md` | 137 | `agentskills/agentskills@69ef37e` | editable |
| `corpus/SOURCES.md` | 63, 70, 74, 75 | `zed-industries/zed@`cfb894a5`` ×2, `google-gemini/gemini-cli@`451a02ff`, `anthropics/claude-code@`5ed799e5…` | append-only rows |
| `corpus/SOURCES.md` | 82, 165 | `google-gemini/gemini-cli@a713410a` (pinned URL in row), `agentskills/agentskills@69ef37e…` | append-only rows |

Totals: 25 hits; **6 pinned** (r52 ×2, r54 ×2, r71 ×1, r75 ×1); **13 editable** (knowledge/lessons/README); **6 SOURCES** (append-only). Only the 6 pinned ones cannot be edited, and none of them is a gate-visible token today.

### 1.3 Bare `commit `<hex>`` tokens (the only class both gates see)
`commit_total = 46` (integrity and independent agree), `commit_unresolvable = 2` (S230/S231, §0), `commit_quoted = 6` (context, quoted meta-findings: `claim-census-round12.md:95`, `round-53.md:44-45`, `round-54.md:13`, `round-54-verifier-spotcheck.md:147`, `round-6-aggregator-audit.md:45`), `commit_truncated = 3` (`round-71-verifier-spotcheck.md:90,120`, `round-75-verifier-spotcheck.md:18`, all pinned, context). The two unresolvable rows are in `SOURCES.md` (append-only, not pinned).

### 1.4 `HEAD:` sweep
`grep -rnE 'HEAD:' corpus/`: 28 lines in 8 files (`sweep.txt` §B). Only **one** carries the report-pointer shape that the integrity gate counts as `report_dead`: `corpus/lessons/round-77-verifier-spotcheck.md:15` (`git show HEAD:.ufo/reports/round-77/kotoba.md`), **pinned**, and it is the sole `report_dead` (`integrity-head.json` `report_dead_detail`). The other 27 lines are lane-tree `HEAD:` expressions (`HEAD:SKILL.md`, `HEAD:README.md`, `HEAD:verifiers/…`, `HEAD:SCORECARD.md`) that neither gate treats as a pointer: they are invisible to both gates and sit in editable files (`claim-census-round12.md` ×6, `corpus-integrity-round11.md` ×3, `sibling-citation-routing-round16.json` ×4, `round-6-aggregator-audit.md` ×9, `round-8-aggregator-box3-coldrun.md` ×1, `round-46.md` ×3, `checklist-execution-round16.md` ×1).

### 1.5 Repair-4 caveat (pattern-level)
The `HEAD:` pointer resolves against a **mutable ref**. Once repair 4 lands, the verdict on the pinned line depends on the fleet's `HEAD` at run time, not on a fixed revision. The gate's answer will flip when the fleet commits and the report path is absent from `HEAD`. Carried defect; the repair should record the resolved revision in its output or pin the `HEAD:` to a commit.

## 2. Pattern 2 — is any r80 repair a re-derivation of a fixed class?

Predecessors searched in `corpus/lessons/round-{46,53,54,62,66,72,73,76,77,79}*.md` and `corpus/knowledge/` (`grep -rn` for registry, symlink, report_dead, `HEAD:`, `<rev>:`, commit_unresolvable, re-record).

| r80 repair | Predecessor (name, round) | Verdict |
|---|---|---|
| **1 Registry rows** (`check_desc_craft.py`, `check_r75_routed_repairs.py` withdrawn; `check_allowed_tools.py` new) | **M47 `unregistered-gate`** (r54, `corpus/lessons/round-54.md:15`): gates landed without registry rows; fixed by `check_gate_registry.py` + rows. Repeated in **r72** (51 rows at `c69711e`, `round-72-verifier-spotcheck.md:87`) and **r73** (two rows added for `check_cn_vendor_surfaces.py` and `check_report_pointers.py`, `round-73-verifier-spotcheck.md:67`). Measured base: `check_gate_registry.py --rev 398cbe1` → `60 of 62`, exit 1, `registry-base.txt`; the two red rows are exactly the two r76 gates. | **Re-derivation of M47** — the same class, the same gate. The process gap (a gate lands without its row, and nobody checks the gate's red-at-base) recurs in r76 and the registry gate was already red at base. Repair 1 is correct; the recurrence should be routed as a process item, not as a new class. |
| **2 Symlink** `.ufo/reports/round-76/kotoba.md` | No lane-tree symlink repair found in the corpus (19 files mention `symlink`, all client-behaviour knowledge or lessons; none is a lane-artefact repair — checked by name, not read in full). The nearest predecessor is **M102** (r66, `round-66.md:18`): "foreign-repository commit misclassified as unresolved"; the fleet report reference was the named example, and it was fixed in the **gate** (`commit_resolves` lane-then-fleet, `verify_corpus_integrity.py:600-612`). `governance.citation_resolves` (`verify_skill_checklist.py` ~L1665) resolves **repo-root only** with ≤3 `..` hops — it has no fleet fallback, so the symlink is the only route to satisfy it without a gate change. | **Partial re-derivation of M102 + new mechanism.** The class (fleet-report citation unresolved in lane) was closed for the corpus gates by a gate-side fallback; the checklist gate was never given the same fallback. Repair 2 closes it by a tree artefact instead. Acceptable, but the repair must say it is the checklist-gate analogue of M102, not a fresh class. |
| **3 Index + baseline** (coverage rows, `refresh-corpus-baseline.py`) | **r66** `round66_rerecord` (`corpus-baseline.json`), **r72** `round72_tip_rerecord`, **r47** `round47` — the same index-then-re-record step, four times. The r66 rule ("re-recorded to the observed committed bytes, not fitted") applies unchanged. | **Re-derivation of a routine step**, governed by the existing rule. Not a new class. Note `unindexed` = `corpus/lessons/round-79-verifier-spotcheck.md` (pinned spotcheck, indexed in editable `corpus/README.md`). |
| **4 `<rev>:` report pointer** (`Kb79E04DeadPointer`) | **M103** (r66, `round-66.md:32`): "independent integrity implementation diverged on repository context" — the integrity gate and the independent gate read the same `HEAD:` token differently. The r79 E04 analysis (`round-79/w1/Kb79E04DeadPointer.md` §1) reproduces the same divergence: integrity reads `HEAD:.ufo/…` as a working-tree path and calls it dead; independent strips to the path and calls it alive. | **Re-derivation of M103.** The plan's repair 4 names `verify_corpus_integrity.py` only. After it lands the two gates agree on the outcome but still resolve by different methods (independent still reads the token as a lane path). Per M103, the self-test must pin both gates to the same resolution, or the divergence is carried. |
| **5 External-commit grammar** (`owner/repo@<hex>`) | **M102** (r66) named the class "foreign-repository commit misclassified as unresolved" and closed the **fleet** case by design (lane + fleet only, Q61). The residual — **third-repository** objects — is exactly what the r66 resolver excludes, so repair 5 is an **extension** of M102, not a fresh class. **M45** (r54, `round-54.md:13`): the zed `commit `cfb894a5`` → `zed-industries/zed@`cfb894a5`` rewrite was an append-only breach made **to clear `commit_unresolvable`** (the rewrite evaded the gate; it did not resolve the object). Repair 5 would legitimise that evasion route: after it lands, an owner/repo prefix turns a red token into an INFO count. | **Extension of M102 with a re-opened M45 risk.** Must (a) match the S230/S231 shape as well as `owner/repo@hex`, (b) keep an exact detail list and a non-zero INFO expectation so the count cannot silently go to zero, (c) carry the M45 evasion as a named risk in its red-before arm (a `commit `hex`` rewritten to `owner/repo@`hex`` must be counted, not hidden). |

Net: 1 and 3 are routine re-derivations; 2 and 4 are re-derivations of r66's M102/M103 in new mechanisms; 5 extends M102 and reopens M45 unless it closes the evasion path.

## 3. Recommendations to L1 (not my edits; C1 scope)

- Repair 5 must be re-specified against the measured tokens (§0.1): add a rule for `` `owner/repo` commit `<hex>` `` (S230, S231) or add a correcting row for S230/S231 under the append-only rule. Without this, C1 cannot reach `6 of 6`, and the plan's W3 expectation ("integrity still red on report_dead and commit_unresolvable") would hold for the wrong reason.
- Repair 4: pin the resolution with a red-before arm on **both** gates (M103), and record the resolved revision in the gate output.
- Plan § C1 names the wrong two tokens and the wrong file path for E04 (`round-79/build/Kb79E04DeadPointer.patch` is at `round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`, sha256 `d7169dd8…`). Correct the plan text when L1 freezes.

## 4. Carried-defects list (editable files only; proposals for disposition, nothing here edits a pinned file)

| # | File:line | Token | Class | Pinned? | Note |
|---|---|---|---|---|---|
| CD1 | `corpus/knowledge/skill-listing-thresholds-round54.md:29,44` | `google-gemini/gemini-cli@`451a02ff` | owner/repo@ backtick | editable | invisible to gates; becomes INFO after repair 5 |
| CD2 | `corpus/knowledge/skill-eval-artefacts-round70.md:5,6` | `agentskills/agentskills@69ef37e…` | owner/repo@ | editable | same |
| CD3 | `corpus/lessons/round-53.md:27` | `microsoft/vscode-docs@fd64d648` | owner/repo@ | editable | same |
| CD4 | `corpus/lessons/round-53.md:44` | `zed-industries/zed@`cfb894a5` | owner/repo@ (M45 record) | editable | the rewrite is quoted in a record; keep |
| CD5 | `corpus/lessons/round-54.md:13,52` | `zed-industries/zed@`cfb894a5` | M45 record | editable | do not rewrite |
| CD6 | `corpus/lessons/round-55.md:54` | `google-gemini/gemini-cli@451a02ff` | owner/repo@ | editable | same as CD1 |
| CD7 | `corpus/lessons/round-71.md:6,13` | `agentskills/…@69ef37e…`, `anthropics/skills@dbd4588f…` | owner/repo@ | editable | same |
| CD8 | `corpus/lessons/round-74.md:37`, `corpus/README.md:137` | `agentskills/agentskills@69ef37e` | owner/repo@ | editable | same |
| CD9 | `corpus/SOURCES.md:63,70,74,75,82,165` | six owner/repo@ hits | owner/repo@ | append-only | corrections only via `supersedes` row |
| CD10 | `corpus/SOURCES.md:171,172` (S230, S231) | `commit `7bb48f21…`` (third-repo) | bare commit, **gate-red** | append-only | the only live unresolvable pair; repair 5 must cover or a correcting row |
| CD11 | `corpus/knowledge/claim-census-round12.md` (×6), `corpus-integrity-round11.md` (×3), `sibling-citation-routing-round16.json` (×4), `lessons/round-6-aggregator-audit.md` (×9), `round-8-aggregator-box3-coldrun.md` (×1), `round-46.md` (×3), `checklist-execution-round16.md` (×1) | `HEAD:<lane path>` | HEAD: invisible to gates | editable | not report pointers; no gate reads them; record only |
| CD12 | `corpus/lessons/round-79-verifier-spotcheck.md` | unindexed | index | pinned file, editable index row | repair 3 |

Pinned, not proposed for edit: `round-52-verifier-spotcheck.md:99-100`, `round-54-verifier-spotcheck.md:37,148`, `round-71-verifier-spotcheck.md:102`, `round-75-verifier-spotcheck.md:36`, `round-77-verifier-spotcheck.md:15` (the sole `report_dead`; repair 4 is the only sanctioned route).

## 5. Verification run here (exit codes captured directly)

- `verify_corpus_integrity.py --no-baseline --json` → exit 1 (`integrity-head.json`). DRIFTs: `unindexed` 1, `report_dead` 1, `commit_unresolvable` 2 (S230/S231 detail above).
- `verify_corpus_independent.py --json` → exit 1 (`independent-head.json`). `commit_unresolvable` 2 (same tokens); `commit_hex_total` 46.
- `check_gate_registry.py --rev 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` → `gate registry rows conformant 60 of 62`, exit 1 (`registry-base.txt`).
- `sweep.txt` generated with grep commands listed inline in the file (§A owner/repo@hex 25 hits; §B HEAD: 28 lines; §C report-pointer HEAD: 1 hit; §D commit-with-slash 0 hits; §E symlink mentions 19 files).
- Not run: the tip battery (not my item); no build outputs produced; no patches.

VERDICT: C1's repair-5 spec targets the wrong tokens (gate-red pair is S230/S231 `commit `7bb48f21…``, not gemini/zed); r80 repairs 1 and 3 re-derive r54-M47 and r66/r72/r47 re-record, 2 and 4 re-derive r66 M102/M103 in new mechanisms, 5 extends M102 and reopens M45's evasion path unless specified.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80K02Patterns.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80K02Patterns/sweep.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80K02Patterns/integrity-head.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80K02Patterns/independent-head.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80K02Patterns/registry-base.txt
