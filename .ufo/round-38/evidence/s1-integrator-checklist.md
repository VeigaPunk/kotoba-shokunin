# R38 integrator checklist — the exact command sequence to run at the landing commit

Seat S1 (scout). Every row: **what to run**, **what must be observed**, **the r37 obligation it discharges**.
Measured at `cb4e0f3` + in-flight worktree 2026-10-19 ~10:37 local; re-run everything at the landing commit.
A row whose "must observe" fails is a defect to record, not to smooth.

## 0. Preconditions (run first; do not proceed past a red here)

| # | command | must observe |
|---|---|---|
| 0.1 | `git status --porcelain` | only intended ` M` rows + `?? .ufo/round-38/`; no stray probe trees inside `verifiers/` |
| 0.2 | `sha256sum verifiers/verify_harness_independent.py verifiers/compare_harness_independent.py verifiers/verify_skill_checklist.py verifiers/check_assertion_floors.py verifiers/floors-registry.json` | record the five shas verbatim into the report; **every later row is meaningless without them** |
| 0.3 | `python3 verifiers/verify_harness_claims.py` | `28/28 checks pass`, exit 0 (substrate intact) |

## 1. The full gate battery (the round's byte-invariance claim)

| # | command | must observe |
|---|---|---|
| 1.1 | `python3 verifiers/check_assertion_floors.py` | **8** `PASS` rows, exit 0. Floors must be EXACT (observed == floor) on all 8 — 10/119/59/87/1584/62/71/59 |
| 1.2 | `python3 verifiers/check_assertion_floors.py --self-test` | exit 0, `0 failure(s) over N assertions`, N ≥ 57 (was 41 pre-r38; the C2 seat's patch raises it) |
| 1.3 | `python3 verifiers/verify_skill_checklist.py --self-test` | exit 0, `0 failure(s) over N` — **N grows** if the C3 battery extension lands; the checklist floor must move in-step in **all five carriers** (§4.1) |
| 1.4 | `python3 verifiers/verify_skill_checklist.py` | exit 0. **At `cb4e0f3` this is RED** — `FAIL governance.citation_resolves … SCORECARD.md:131/132/133`. Either fixed in-round or recorded as a carried red (see §5.3) |
| 1.5 | `python3 verifiers/verify_harness_claims.py --self-test` · `python3 verifiers/verify_corpus_integrity.py` · `python3 verifiers/verify_corpus_independent.py` · `python3 verifiers/verify_surfaces.py` · `python3 verifiers/check_substrate_pins.py` | all exit 0; corpus_integrity `9/9`, pins `OK 3/3` |
| 1.6 | `bash verifiers/fault_injection_corpus.sh --self-test` | `self-test: OK` |
| 1.7 | `python3 verifiers/verify_harness_independent.py --self-test` | exit 0, `0 failure(s) over 71 assertions` (floor 71) |
| 1.8 | `python3 verifiers/compare_harness_independent.py --self-test` | exit 0, `0 failure(s) over 59 assertions` (floor 59) |
| 1.9 | re-run 1.1 and `diff` the stdout against the same command run before the landing | byte-identical (the lane's byte-invariance idiom; r37 used stdout sha `aff5a4a6…`) |

## 2. C1 — depth (close the r37 source-blind re-derivation)

### 2.1 The counting command (R1-F3: "the counting command cannot witness the claim")

| # | command | must observe |
|---|---|---|
| 2.1.1 | `python3 verifiers/compare_harness_independent.py` | **exit 0** with the landed scope; the headline `N/M` quoted verbatim **with** the strict column, adjudicated count, provisional count and the driver's own exit reason |
| 2.1.2 | same, `--json` | machine report parses; `n_provisional` = 0 |
| 2.1.3 | `python3 verifiers/verify_harness_independent.py` | exit 0; quote `N derived, M unlanded (of 28 named checks)` |
| 2.1.4 | `python3 verifiers/compare_harness_independent.py --no-mode-predicates` | report the strict-only headline beside the protocol headline (R1-F6/V1-D6: three agreement numbers exist; the report must pin one and publish the rest) |

**At `cb4e0f3` the driver is exit 1 — `23/28 (strict 17/28), 5 open rows`**:
`oc.dup.roots_both_sided` (3 vs 0), `oc.log.skills_tag_hits` (13 vs 0),
`omp.catalogue.{found,matched,total}` (None vs live).

### 2.2 C1(a) — adjudicate the 5 open rows

| # | command | must observe |
|---|---|---|
| 2.2.1 | `grep -o 'skills="\[[^]]*\]"' ~/.local/share/opencode/log/opencode.log \| wc -l` | `13` — the literal `skills="` count (this is what IND's rule counts) |
| 2.2.2 | `grep -c -o '<skills>' ~/.local/share/opencode/log/opencode.log` | `0` — the raw `<skills>` literal count (**V1/V2/P3 corroborate the harness's 0**) |
| 2.2.3 | `grep -c 'duplicate skill name' ~/.local/share/opencode/log/opencode.log` | `0` — no duplicate-root lines (harness 0; IND's 3 counts duplicate *names*, a different population) |
| 2.2.4 | `python3 verifiers/compare_harness_independent.py --report <path>` and read the per-row table | every disagreement has a row: class (D1/D2/D4), both readings, probe command+output, ruling, action, `blind:` — per `evidence/a1-adjudication-protocol.md` §3/§7.3 |

**Ruling direction (pre-registered, evidence-backed):** both rows are **D2 definitional** with the harness's reading matching the id's name/spec sentence — `skills_tag_hits` counts a *tag* (0), not `skills="` occurrences (13); `roots_both_sided` counts duplicate *roots* (0), not duplicate *names* (3). The losing side is IND; the action is an IND rule correction (or a recorded D2 with both scopes' probe blocks — never a silent relabel).

### 2.3 C1(b) — scope the 3 catalogue rows OUT

| # | command | must observe |
|---|---|---|
| 2.3.1 | `python3 verifiers/compare_harness_independent.py --independent-json <IND JSON with catalogue rows dropped>` | **currently exit 2** — `uncovered checks (in live, missing from independent): omp.catalogue.{found,matched,missing_names,total}` |
| 2.3.2 | `python3 verifiers/compare_harness_independent.py --help` | confirm whether a scope/out-of-scope flag exists |

**MEASURED DEFECT (mine, S1): the driver has NO scoping mechanism.** Dropping the catalogue rows yields exit 2 `uncovered`, and `--expect-n 0` does not change it (proven: `rc=2` both ways). So C1(b) is **not satisfiable as written** unless the driver gains an explicit scope declaration (e.g. `--out-of-scope <id>[,<id>]` naming them, printed in the report and excluded from the denominator with the reason). The three rows' blocker is real and must be **named** (`P3`'s "named UNSUPPORTED rather than guessed" idiom) — but naming them in the report while leaving the driver at exit 2 does not close C1's counting clause.

### 2.4 C1(c) — freeze-before-compare receipt

| # | command | must observe |
|---|---|---|
| 2.4.1 | `python3 verifiers/verify_harness_independent.py --json > ind-freeze.json; sha256sum ind-freeze.json` | the sha recorded **before** the first comparison run, with the mtime ordering vs the harness capture |
| 2.4.2 | compare the two mtimes | IND freeze strictly earlier than the harness run (r37 had 13:07:10Z < 13:07:53Z) |

**MEASURED DEFECT (mine, S1): `--independent-json` has a precedence trap.** The driver's `parse_independent` reads `results` **first** (`_record_list` tries `results`, `rows`, `checks` in that order). Sabotaging `rows`+`checks` while leaving `results` intact is **invisible** (proven: identical 23/28 output). A freeze receipt built by editing `rows`/`checks` therefore does not constrain the comparison. The receipt must capture the file the driver actually reads, and the report should say which channel that is.

### 2.5 C1(d) — blindness by construction

| # | command | must observe |
|---|---|---|
| 2.5.1 | `bash .ufo/round-37/evidence/R1-make_blind_tree.sh <target>` | **currently crashes** — the script resolves `REPO` as `$HERE/../../../..` (correct from `drafts/R1/`, wrong from `evidence/`), so it archives `/home/vgpnk/Projects/shokunin` (the parent monorepo) and dies on the missing `baseline.json` |
| 2.5.2 | same with the repo passed explicitly | `harness_pin_residual_count=0`, `dot_git_present=no`, `pins_guard_in_scrub_tree=exit 0` |

**MEASURED: residual is 3 at r38's HEAD, and closable to 0 with three added lines.**
Rooted correctly the scrub reports `harness_pin_residual_count=3`, leaking from **r37's
own new files**: `verifiers/verify_harness_independent.py` (8 id tokens),
`verifiers/fixtures/harness-independent/oc-log/case.json` and `.../omp-cache/case.json`
(3 id tokens). The script's token list predates them. Adding three `rm` lines
(`verify_harness_independent.py`, `compare_harness_independent.py`,
`fixtures/harness-independent/`) yields `harness_pin_residual_count=0` with
`pins_guard_in_scrub_tree=exit 0` and `tree_files=326` — proven at
`drafts/s1/probe/make_blind_tree_c1.sh` + `drafts/s1/blind-tree-c1/`. Do not widen the
token regex instead: the script's own note warns an over-broad scan mislabels the
pins-guard shas.

### 2.6 C1(e) — the corpus doc

| # | command | must observe |
|---|---|---|
| 2.6.1 | `ls corpus/knowledge/harness-independent-round37.md` | exists (absent at `cb4e0f3`) |
| 2.6.2 | `grep -n '^## ' corpus/knowledge/harness-independent-round37.md` | the §1–§7 shape per `evidence/a1-adjudication-protocol.md` §7 (claim · agreement check-for-check · adjudications · §3b shared properties/mutants · repairs forced · residuals · reproduce) |
| 2.6.3 | `grep -c 'blind:' corpus/knowledge/harness-independent-round37.md` | ≥ the number of adjudicated rows — a row without a probe/disclosure field is not a ruling |
| 2.6.4 | `python3 verifiers/verify_corpus_integrity.py` | `9/9`, exit 0 (the new doc must be indexed) |

### 2.7 C1(f) — register both instruments

| # | command | must observe |
|---|---|---|
| 2.7.1 | `python3 -c "import json;d=json.load(open('verifiers/floors-registry.json'));print(d['instrument_total'],sorted(d['instruments']))"` | `8` and the two new names present |
| 2.7.2 | `python3 verifiers/check_assertion_floors.py` | 8 PASS rows incl. `harness_independent observed=71 floor=71` and `compare_harness_independent observed=59 floor=59` |
| 2.7.3 | `python3 verifiers/check_assertion_floors.py --self-test` | exit 0 — **this is the row that catches the hidden coupling** (below) |
| 2.7.4 | `python3 .ufo/round-37/evidence/v5-derive_floors.py --repo .` | `EXACT 8/8`, exit 0. **Measured by me at the in-flight tree: all 8 rows EXACT (10/119/59/87/1584/62/71/59), deltas 0** — this is the independent re-derivation that sees a stale floor the guard cannot (a floor is a lower bound) |

**MEASURED COUPLING (mine, S1 — this is the row most likely to be missed).** The guard's own self-test builds fixture registries and swaps a literal, with a count check: `swap(registry_text, '"instrument_total": 8', '"instrument_total": 7', "F6/total")`. Growing the registry from 6 → 8 rows **requires the anchor literal in the guard's self-test to move 6 → 8 in the same edit**. Proven: with only the four documented sites (EXPECTED table, INSTRUMENTS table, registry, docstring) and the anchor left at 6, `--self-test` fails `3 failure(s) over 41`; with the anchor at 8 as well, `0 failure(s) over 41` and the live guard prints 8/8 PASS, exit 0. The registry's `$comment` names four in-step sites; **the anchor is a fifth**. (The in-flight worktree patch has this right — `'"instrument_total": 8'` at `:432`.)

### 2.8 C1 mutant leg

| # | command | must observe |
|---|---|---|
| 2.8.1 | `python3 verifiers/verify_harness_independent.py --write-freeze <freeze.json>`, then re-run with a mutated substrate copy + `--freeze` | exit 1 naming the drifted rows (r37: 6 rows named) |
| 2.8.2 | record the expected-firing set **before** the run | per protocol §7.4 — a mismatch between the expected set and either instrument's naming set is itself an adjudicated row |

## 3. C2 — operability (V4's two residuals)

| # | command | must observe |
|---|---|---|
| 3.1 | copy the guard, inject a non-str key (`None: 7,` in `EXPECTED_INSTRUMENTS`), run it | **before `cb4e0f3`: uncaught `TypeError: can only concatenate str (not "NoneType") to str`, exit 1, class unnamed** (reproduced by me at `.ufo/round-38/drafts/s1/probe/gS.py`). After: exit 2, `FAIL registry non-string key: EXPECTED_INSTRUMENTS has None (instrument names must be str)` |
| 3.2 | copy the guard, truncate a row to 4 fields, run it | **before: exit 2 with three lines incl. the self-contradictory `FAIL registry floor drift: pins registry=62 expected=62 row=None`** (reproduced at `probe/gJ.py`). After: exit 2 with **one** line, `FAIL registry malformed row: pins (expected 5-field tuple)` |
| 3.3 | `python3 verifiers/check_assertion_floors.py --self-test` | ≥ 2 new true-discriminator fixtures for the two classes; assertion count grows from 41 |
| 3.4 | `diff <(python3 verifiers/check_assertion_floors.py) <(the pre-landing run)` | byte-identical stdout (no new PASS line, no wording change) |

**Both residuals are CLOSED in the in-flight worktree** (measured by me: `gWS.py` → `FAIL registry non-string key: …` rc=2; `gWJ.py` → single `FAIL registry malformed row: pins` rc=2; guard `--self-test` `0 failure(s) over 57 assertions` rc=0). Re-run at the landing commit.

## 4. C3 — freshness (container-relative fence + battery + routing pin)

### 4.1 The floor carriers (a half-bump is now a loud FAIL by design)

| # | command | must observe |
|---|---|---|
| 4.1.1 | `grep -n "1584\|<new count>" verifiers/check_assertion_floors.py verifiers/floors-registry.json` | the checklist floor equal in **all five carriers**: guard docstring, `EXPECTED_INSTRUMENTS`, `INSTRUMENTS`, `floors-registry.json`, **and the self-test anchor literal** (the coupling from §2.7.3 applies to every floor move, not only to the row count) |
| 4.1.2 | `python3 .ufo/round-37/evidence/v5-derive_floors.py --repo .` | `EXACT N/N`, exit 0 — the independent re-derivation, not the guard (a stale floor is a lower bound and is invisible to the guard; V5 measured `SLACK +65` and `+15` windows in r37) |

### 4.2 The fence fix

| # | command | must observe |
|---|---|---|
| 4.2.1 | apply `evidence/v6-container-relative.patch` | **applies cleanly (rc 0) after rewriting its two stale absolute-path headers** (`--- .ufo/round-37/drafts/v6/snapshots/…` and `+++ /home/vgpnk/…/drafts/v6/patched/…`) — the drafts tree was pruned in r37. Proven by me at `9ea386da` |
| 4.2.2 | `python3 .ufo/round-37/evidence/v6-oracle.py --repo .` | **needs `shapes.json` + `shapes/*.md`, which were pruned**; r38 seat R2 rebuilt them at `.ufo/round-38/drafts/r2/rebuild/`. Expect `mismatches=0` post-patch (4/36 pre-patch, all container-relative) |
| 4.2.3 | `python3 .ufo/round-37/evidence/v6-verify_battery.py --repo .` | `failing=0` after the battery extension |
| 4.2.4 | `git status --porcelain verifiers/fixtures` | empty — the 71 fixture dirs stay byte-identical |
| 4.2.5 | `ls verifiers/fixtures/checklist \| wc -l` | `71` (unchanged; the battery is INLINE `FENCE_SHAPES`, not new dirs — V7's measurement) |
| 4.2.6 | live `python3 verifiers/verify_skill_checklist.py` stdout sha | byte-invariant vs pre-landing (`b3275e1c…` was r37's) |

**Live state measured by me at `9ea386da`:** the container probe (`drafts/r2/container_probe.py`) still shows `probe lines=15 mismatches=4` — S07/S08/S07b are **open**, so the patch is genuinely unlanded.

### 4.3 The routing pin re-issue (P8's idiom)

| # | command | must observe |
|---|---|---|
| 4.3.1 | `python3 -c "import json;print(json.load(open('corpus/knowledge/sibling-citation-routing-round16.json'))['instrument'])"` | `sha256` == the **landed** `verify_skill_checklist.py` sha, with the superseded chain in `sha_superseded_from` |
| 4.3.2 | `python3 -c 'from pathlib import Path; import sys; exec(Path("corpus/knowledge/sibling-citation-routing-round16.md").read_text().split("<!-- count-code -->\n```python\n",1)[1].split("\n```",1)[0])' HEAD frozen` | exit 0 (measured by me at HEAD: exit 0, `classified 14, unclassified 0, routes 3`) |
| 4.3.3 | same command, `HEAD live` | **exit 1 `source_drift`** — this is the **pre-existing r26 condition**, not a defect of this round (P8 attributed it: the sibling scan shows the landed extractor alters no sibling extraction). Record it as carried, do not present it as a regression |

**Coupling to watch:** the pin is byte-coupled. Any seat touching `verify_skill_checklist.py` after the re-issue re-breaks 4.3.2's `instrument_drift`. Re-issue **last**, and re-run 4.3.2 immediately after.

## 5. Known carried items (record, do not smooth)

1. **Checklist gate RED at dispatch HEAD `cb4e0f3`** (measured by me): `FAIL governance.citation_resolves: evaluated 293 — SCORECARD.md:131/132/133 … 3 schematic token(s) excluded`, exit 1. r37's report row "gates green at `c8e233d`" does not hold for this gate. Either fixed in-round or recorded as carried; do not report the battery green without naming it.
2. **C1(b) has no mechanism** (§2.3) — the driver cannot scope rows out; C1's "exit 0 over the landed scope" is unreachable without a driver change.
3. **Blind-tree residual is 3, not 0** (§2.5) and the banked script's repo-root is wrong from `evidence/`.
4. **`--independent-json` precedence trap** (§2.4) — the freeze receipt must capture `results`.
5. **Stale floor list in dispatch briefs** (r37: "surfaces 82, pins 51" vs live 87/62; now 8 instruments, not 6) — `SCORECARD.md` still carries the r29 contract row.
6. **`SCORECARD.md` capability row and `SKILL.md` instrument list** still omit the floors guard / carry stale floors (r37 P5 defect 4/5, r36 C2 defect 7) — carried debt.
7. **Three-artifact coordinated-edit boundary** (registry + guard + tables) remains declared out of scope; `--script` override is covered. Named, not an unclosed class.
