# Kb81K03Considerthese — considerthese open proposals × round-81 plan cross-read

Seat: Kb81K03Considerthese (leaf, read-only). Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; `git status --porcelain` at base shows only `?? .ufo/wapes`, `?? .ufo/waves/round-81/`, `?? plans/round-81.md`. No clone, no scratch dir, no counter or battery run, no tool installed. Every number below is from a command named in § 7 or from a committed receipt I name.

Sources read: `considerthese/2026-10-26.md`, `2026-10-25.md`, `2026-10-24.md`; `plans/round-81.md`, `round-80.md`, `round-79.md`; `corpus/lessons/round-80.md` § Gate; `corpus/lessons/round-80-verifier-spotcheck.md`; `.ufo/waves/round-80/w1/Kb80K03Considerthese.md` (r80 precedent); verifier source for `check_tip_battery.py`, `verify_corpus_integrity.py`, `verify_skill_checklist.py`; receipts `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`, `census-before.txt`, `.ufo/waves/round-80/build/Kb80E04DeadPointer/integrity-base.json`, `.ufo/waves/round-79/snapshots/S230.fetch.json`, `S231.fetch.json`.

## 0. Summary

Blocking or fix-before-freeze items for L1 (details in § 4):

| id | sev | item |
|---|---|---|
| F1 | BLOCK (C1) | Control W8 expects `report_dead → red` for a marker at `.ufo/reports/round-76/kotoba.md`. Nothing the battery counts binds that path. As designed, the world reaches 6 of 6 → kill rule. R1 does not cover it. |
| F2 | BLOCK (C1) | R1 resolves `<rev>:<path>` "citing repo first". A lane-created commit holding a ≥400-byte file with `## SHONEN` passes content identity. This world is not in the W-list. |
| F3 | BLOCK (C1) | R2 "VERIFIED" binding is lane-authored: manifest + receipts are committed lane bytes, and the counter reads no network. A forged manifest row plus receipt reaches 6 of 6. Not in the W-list. |
| F4 | FIX (C1) | E6 arithmetic: the plan says "40 base-spent". The measured base spend is **22 added / 3 deleted**. Headroom under `LINE_CAP = 140` is **118 added**, not 100. The plan's own 60–120 estimate can exceed 118. |
| F5 | FIX (C1) | R2 cites `S230.fetch.json` as binding evidence for `7bb48f…`. That file does not contain the hash. Only `S231.fetch.json` does (1 match), and S230's own receipt contradicts the S230 row. |
| F6 | FIX (C2) | `S249` duplicates the already-opened row `S248` (same URL, same 28395 B, same sha256 `ac62c2df…`). S248 is `queued`, `used-by —`. The plan's "old→new" for S248 is really "— → new". |
| F7 | FIX (C1/C2) | Plan wording: the `W9` and "receipt proof" controls don't say the receipt must be content-checked. The r80 kill was an existence check. Same failure class. |
| F8 | NOTE | `SKILL.md` is at 596 lines (cap 600). The C2 rule edit plus one registry row takes it to 597–598. |

Disposition conflicts with r81: **no hard conflict**. P5 (evidence budget) is not defeated by the r81 wave size, but its premise figure is stale by one wave (§ 2).

## 1. Open proposal ledger (considerthese 2026-10-24, -25, -26)

Dispositions are from committed lessons/plans. "open" means no committed disposition was found.

| src | item | recorded disposition (evidence) | state at b284223 |
|---|---|---|---|
| 10-24 #1 | dogfood 99-char rule on the description | r75 called the premise stale (line-based measure); M76-1 showed the folded scalar was mis-measured (`corpus/lessons/round-76-verifier-spotcheck.md`, M76-1) | **open**. Re-measured today: description 1,021 chars, first sentence 151 chars (joined folded scalar, python over `SKILL.md` frontmatter). The 10-26 premise is correct. |
| 10-24 #2 | every round carries a reader-facing claim | no plan cites it | **satisfied in form** by r81 C2 (SKILL.md rule line + entry). Not dispositioned. |
| 10-24 #3 = 10-25 #4 | "two harnesses here" intro | `corpus/lessons/round-74.md:72` ("item 4 worked") | **done** (r74). |
| 10-24 #4 | reader diff per reflection | none | **open**. |
| 10-24 #5 | robust read path / fallback | none (operator/process) | **open**. |
| 10-25 #1 | byte/line ceiling for SKILL.md | declined r76 (`plans/round-76.md:11`; `corpus/lessons/round-76-verifier-spotcheck.md:64`); rejected r79 with measured figures (`corpus/lessons/round-79-verifier-spotcheck.md:63`) | **open-rejected**. Current `SKILL.md`: **596 lines / 80,920 B** at b284223 (`wc -lc`). r80 seat recorded 78,647 B at base `398cbe1`. The 10-26 figures (590 / 78,569) are stale. |
| 10-25 #2 | move `## Gate registry` out of SKILL.md (10-26 P2) | r80 § Gate: **L0 matter per Q67** (`corpus/QUALITY.md:83`) | **open-deferred**. The section is now lines 448–519 = **26,308 B** (`sed -n 448,519p | wc -c`). The r80 seat recorded 24,897 B at `398cbe1`. The r76 L0 pointer `.ufo/l0-questions.md:174` was not confirmed (see § 6). |
| 10-25 #3 | route each knowledge entry's author rules into the audit checklist | `plans/round-72.md:69-71` ("the one considerthese proposal worked") | **done** (r72). |
| 10-25 #5 | description self-audit | 10-26 P3 (below) | **open**, see next row. |
| 10-26 P3 | land the r74-rejected description page; audit description | r80 § Gate: needs a rejected-closure to clear; r74 flip unmet | **blocked**. Not touched by r81. |
| 10-26 P4 | close rounds "provisional" until falsify wave runs | r80 § Gate: operator/L0. Evidence: `.ufo/waves/round-79/` has no `w2*` and no `w2-results.json`; r79 plan line 74 says w2 "unavailable" | **open, operator/L0**. r81 folds attack into one v2 wave: 6 critics + 6 reviewers + 4 mutation-testers + 1 sentinel = 17/64 = 26.56 % (arithmetic checked). |
| 10-26 P5 | evidence byte budget / compress seat logs | r80 § Gate: operator-owned retention policy | **open, operator-owned**. See § 2. |

## 2. Disposition conflicts with round 81 (P5 focus)

**No hard conflict.** Measured:

- Tracked `.ufo` at HEAD b284223: **15,648 files, 188,415,336 B** (`git ls-tree -r -l HEAD -- .ufo | awk`).
- Tracked `.ufo` at `398cbe1` (r80 base): 14,841 files, **174,588,093 B**. This is the figure r80's P5 disposition cites. It is the **r80 base**, not the r81 base.
- Difference: 13,827,243 B. The r80 wave alone is `.ufo/waves/round-80` = 805 tracked files, **13,826,625 B**. The 618 B residual is not attributed.
- Largest single tracked item: `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` = **47,815,579 B** (≈25 % of tracked `.ufo`). Top-level totals: `.ufo/waves` 93.9 MB, `.ufo/round-44` 49.6 MB, `.ufo/round-46` 26.6 MB.
- Disk: `/fast/scratch/hyaku` 591.3 G free (`disk-guard.sh status`). Not a constraint.

What this means for r81:

1. **Wave size fits any cap.** The r80 wave cost 13.8 MB tracked. The r81 build/receipts are text-heavy and of the same order.
2. **The operability cost is the clone, not the commit.** Every seat recipe (`git clone --shared` + checkout) materializes all 15,648 `.ufo` files, about 188 MB, per clone. For 64 seats that is about 12 GB transient in `/fast/scratch`. Fits, but the 105 s battery copies the whole tree too (`check_tip_battery.py` builds its sandbox by `git clone --shared --no-checkout` + checkout).
3. **P5's "compress seat logs" would not touch the largest item** (a 47.8 MB text evidence file), and in-place compression would change bytes that the r81 freeze cites. r80's reason stands.
4. **Fix the premise:** P5's figure is the r80 base; the r81 base figure is 188.4 MB. Any budget must cite its base commit.

## 3. Silent dependencies on unlanded r79/r80 work

| item | state at b284223 (evidence) | r81 dependency |
|---|---|---|
| r79 w2 falsify wave | never settled: no `.ufo/waves/round-79/w2*`, no `w2-results.json` (`ls .ufo/waves/round-79/`) | none of r81's items consume w2 output. But the "frozen counter" pattern (controls before data) that r81 uses is the one r79 w2 was meant to re-run. Not inherited. |
| r79 E02 symlink | **landed**: `.ufo/reports/round-76/kotoba.md → ../../../../.ufo/reports/round-76/kotoba.md` (lane, 22:24) | r81 R1/W8 rely on this path. See F1: the symlink makes this path existence-only. |
| r79 / r80 E04 (`<rev>:<path>` report pointer) | **not landed**. `verify_corpus_integrity.py:273-277` `report_pointer_exists` is `resolve_pointer(...).is_file()` plus a fleet fallback for bare `.ufo/reports/` paths. No object-expression branch. | r81 R1 supersedes it. The r80 E04 patch (`+17/−0`, `Kb80E04DeadPointer.patch`) must be ported fresh, not cited as landed. |
| r80 E05 (marker grammar) | **not landed**, and **superseded** by R2 (plan says so). | none; do not port the marker arm. |
| r80 E06 counter erratum (`LINE_CAP` 40→60 + pins) | **not landed**. `check_tip_battery.py:111` `LINE_CAP = 40`; `INSTRUMENT_PINS` unchanged. | r81 E6 starts from 40 (correct). The r80 canonical 6-of-6 receipts (`Kb80C01C1-canonical-*.txt`) were produced by the killed stack. They are killing-world reproductions, not r81 evidence. |
| r80 C1 frozen counter | killed (`corpus/lessons/round-80-verifier-spotcheck.md`) | r81 re-freezes; no r80 pin reused. |
| r80 `refresh-corpus-baseline.py` | r81 copy is **byte-identical** to r80 (`cmp` IDENTICAL). Fail-closed: refuses nonzero zero-mode classes unless `--carry` (script lines 45, 281). | R4 can rely on it. A baseline cannot silently record residuals. |
| r80 `verifiers/external-commits.json` | absent (no such file). Plan says new, committed in r81. | R2 creates it. |
| `.ufo/wapes` | untracked, 594 B, at lane root. R3 moves it to `.ufo/waves/round-81/dispositions/` (dir exists, empty). | fine. |

## 4. Plan defects (fix before freeze; declare before data)

### F1 (BLOCK, C1) — control W8 is unreachable as written

Plan W8: "a marker file substituted at the fleet report path (expect `report_dead` → red)". The plan's R1 test case is `.ufo/reports/round-76/kotoba.md`.

Evidence that nothing counted binds that path:
- `integrity-base.json` (r80 base receipt) lists `report_pointers_quoted_detail` = `corpus/README.md:68 round-48`, `corpus/lessons/round-57.md:86 round-56`; `report_dead_detail` = `corpus/lessons/round-77-verifier-spotcheck.md:15 HEAD:.ufo/reports/round-77/kotoba.md`. No round-76 entry in any pointer list (`grep -n round-76` on that file: none).
- The only corpus mention of `.ufo/reports/round-76/kotoba.md` is backticked inside a `git log` command: `corpus/lessons/round-76-verifier-spotcheck.md:14`. Integrity does not count it.
- The round-76 path is cited by `LOG.md:2818` (outside `corpus/`). That is checked by `verify_skill_checklist.py` `governance.citation_resolves`, which resolves by existence: `citation_resolve` ends in `(base / ...).exists()` (line 1550) and `safe_resolve` uses `os.path.exists` / `(b / head).exists()` (lines 957, 962). `exists()` follows the symlink.

So a 7-byte marker at the fleet path leaves `verify_corpus_integrity` green (no counted pointer) and `verify_skill_checklist` green (existence). Under the plan as written, W8 reaches **6 of 6** and triggers the kill rule. R1 does not reach it.

Options for L1 (choose before freeze, do not narrow after data):
- (a) bind the LOG citation with content identity. Changes `verify_skill_checklist.py`, which is a **pinned** instrument (`check_tip_battery.py` pins it). E6 does not declare that pin, so this needs an amended E6 before data.
- (b) restate W8 against a pointer integrity counts (a corpus-cited report path) and declare the LOG/symlink existence path a named residual.

### F2 (BLOCK, C1) — citing-repo-first lets a lane commit forge a report

R1: "resolves as a git object expression — citing repo first, then fleet". The content identity arm (`## SHONEN` and ≥400 B) is a marker distinction only. A lane-created commit that contains a 400-byte file with `## SHONEN` at `.ufo/reports/round-77/kotoba.md` and is cited as `<lane-rev>:.ufo/reports/round-77/kotoba.md` passes. The plan's controls only test a 7-byte marker, so this is not measured.

Evidence the lane can hold report files: `git ls-files .ufo/reports` lists `.ufo/reports/round-20/…`, `round-21/…` through `round-24/…` (the first five shown). Round-76 and round-77 reports are fleet-only (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-7[67]/kotoba.md`).

Options: resolve `.ufo/reports/` tokens fleet-only for rounds whose reports are fleet-only, or add a control "lane commit with ≥400 B `## SHONEN` file at a pointer path" with expected red, declared pre-data. [INFERENCE: the forged-commit world is not run; it follows from the R1 text and the `report_pointer_exists` fallback order.]

Also, the plan's R1 text repeats the same command twice (`git cat-file -e <rev>:<path>` "then `git cat-file -e <rev>:<path>` in the fleet root"). The fleet arm needs `git -C <fleet>`. Fix the wording.

### F3 (BLOCK, C1) — the "VERIFIED" binding is lane-authored

R2 binds a hash to a repo through `verifiers/external-commits.json` plus "the committed fetch/ls-remote receipt". The counter reads committed bytes and no network. Manifest and receipts are lane-committed. So a lane seat can add a manifest row and a receipt (a text file containing the lane-created hash, the repo URL and the words "ls-remote"), and the counter sees an internally consistent binding. Its W9 ("manifest entry with no committed receipt proof") does not cover this. The r81 counter cannot prove provenance offline.

This is the lesson already in `considerthese/2026-10-24.md` #3 ("hashes don't prove provenance") and the r61 pins rule. Options: (i) disclose that the binding is manifest-attested and reviewer-checked, not provenance, and drop "VERIFIED" from the claim text; or (ii) add the forged-manifest world with an expected verdict declared pre-data (expected: green, so the claim is then reported as a known residual). [INFERENCE: not run.]

Also: W9's "no committed receipt proof" must read as content checks, not existence: receipt absent → red; receipt lacks the hash or the repo string → red; receipt is a 7-byte marker → red. The r80 kill was an existence check that passed a marker.

### F4 (FIX, C1) — E6 cap arithmetic is wrong

Plan kill rule: "(40 base-spent + measured added ≤ 140)". The 40 is the old cap, not the spend. The counter compares the **total** numstat added (`check_tip_battery.py:316 added > LINE_CAP`) against the cap.

Measured base spend (`.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`): `instruments added 22 / deleted 3 lines (cap 40)`. The 22 is `check_assertion_floors.py` (r80 floors bump; numstat for that file in the r80 E05 stack: `22 3`).

Corrected headroom: added ≤ 140 − 22 = **118** repair lines; deleted ≤ 140 − 3 = **137**.

Check against r80: E04 patch `+17/−0` (integrity), E05 patch `+10/−3` (independent) and `+11/−2` (integrity). Composed r80 stack: integrity `+28/−2`, independent `+10/−3`, plus base `22/3` = **added 60**, which is exactly r80's cap arithmetic (22 + 17 + 21 = 60).

The r81 estimate "60–120 added" for the two-gate repair. The top of the estimate (120) exceeds the 118 headroom by 2. Reword the kill rule to "22 base-spent (`tipbattery-base-dot.txt`) + repair-added ≤ 140", and state that the freeze receipt records the measured numstat of the reviewed blobs before data.

### F5 (FIX, C1 R2 / S230 row) — the binding receipt is S231, not S230

R2 says the S230/S231 tokens bind to `mistralai/mistral-vibe` "(r80 receipts: `S230.fetch.json`, `S231.fetch.json`)". Measured:
- `S231.fetch.json`: contains `7bb48f213ac677f943d5c791199ed3dddf302f00` once. Its note: `'main' resolved to commit 7bb48f… by git ls-remote at 2026-10-27T21:43:03Z` for `mistralai/mistral-vibe`. **This is the binding receipt.**
- `S230.fetch.json`: contains `7bb48f` **zero** times. Its note: "main at fetch time = `bb65e3e4971…`" for `badlogic/pi-mono`. This **contradicts** the S230 row's claim (`corpus/SOURCES.md:171`: "resolved to `badlogic/pi-mono` commit `7bb48f…`"). That contradiction is the R80-D4 root cause. It is recorded by committed bytes.

The manifest entry for `7bb48f…` must cite `S231.fetch.json`. The S250 supersede row should cite `S230.fetch.json` for pi `main = bb65e3e4…` and `S231.fetch.json` for vibe `main = 7bb48f…`. The counter's content check is "receipt file contains the hash and the repo string". `S231` passes it; `S230` does not contain the hash.

Also: `corpus/SOURCES.md:172` (S231) says "served commit `7bb48f…`". Both rows carry the hash; only S231's receipt backs it.

### F6 (FIX, C2) — S249 duplicates S248

`corpus/SOURCES.md` row S248 (verified, line 189):
- URL `https://code.claude.com/docs/en/agent-sdk/skills.md` (identical to the plan's S249 URL).
- Tier B; `fetched 2026-10-27, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`. Same as the plan's S249 fetch record.
- Located quote ("In SDK sessions, you can pre-approve tools …", line 348) already present.
- Status **`queued`**, `used-by` **`—`**, opened 2026-10-27.

The plan's S249 "new row" is a second row for an already-opened page with identical bytes. The plan's (e) reads "S248 `used-by` old→new"; the old value is `—`.

Options: (i) promote S248 (`queued` → `mined`, used-by = `corpus/knowledge/allowed-tools-sdk-round81.md`) and do not add S249. The counter's (b) and (c) then point at S248 and its snapshot. (ii) keep S249 and state why a second row for the same bytes is needed. The census (`.ufo/waves/round-81/receipts/census-before.txt`, 31 W04 "duplicate url" lines plus `ok`) has no precedent for a same-day same-bytes pair.

Also: row count at base is 174 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`). The plan's S249/S250 numbering is correct.

### F7 (FIX, C1/C2) — controls that depend on content, not existence

Same failure class as r80's kill, in two places:
- R1 "≥400 bytes + `## SHONEN`" is content identity by a marker, not by the report's bytes.
- W9 and any "receipt proof" need the content checks listed in F3.

For every "proof" file the counter reads, the control list needs one world per failure: absent, wrong content, marker-sized.

### F8 (NOTE) — SKILL.md headroom

`wc -lc SKILL.md` at b284223 = **596 / 80,920**. The 600-line cap is a checklist budget (r76 note). The C2 rule edit (f) and the one registry row (C1 R6 = C2 (f)) add 0–2 lines → 596–598. Any other seat edit to SKILL.md breaks the cap. Tell L1 to put the SKILL.md edits in one commit and run the checklist after it.

Also: the registry row for `check_sdk_allowed_tools.py` sits in C1's repair set (R6) while `check_gate_registry` is one of C1's six gates. C1 6-of-6 therefore depends on C2 shipping its counter file (if it ships, row required; if it does not, no row). Order the C2 counter freeze before the C1 measurement.

## 5. Plan premises verified true (keep)

- `tipbattery-base-dot.txt`: `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1 (gates: registry 0, floors 0, checklist 0, integrity 1, independent 1, correction 0). Matches the plan's Trigger.
- `corpus/SOURCES.md:171-172` each contain `7bb48f…` once (S230, S231). Matches the plan's `commit_unresolvable 2` locator.
- `corpus/lessons/round-77-verifier-spotcheck.md:15` contains `HEAD:.ufo/reports/round-77/kotoba.md` (the `report_dead` token). Matches.
- Attack share: 6 + 6 + 4 + 1 = 17; 17/64 = 26.56 %. Seat floors (16+17+9+3+6+6+4+1+1+1) = 64.
- Description 1,021 chars / first sentence 151 chars (re-measured; 10-26 premise correct).
- `refresh-corpus-baseline.py` in r81 build is byte-identical to r80 (`cmp`), fail-closed on residuals.
- S230/S231 page bytes: S230 4,793 B `5b980552…`; S231 77,634 B `fc48a5db…`; both receipts agree with their rows on bytes and sha256.

## 6. Not verified / limits

- No counter or battery run. F2 and F3 forged-world outcomes are [INFERENCE] from the source text, not executed.
- `.ufo/l0-questions.md` (fleet, 126,802 B) has no match for "Gate registry" (`grep -n`). The r76 pointer `:174` was not read; the L0 filing for P2 is unconfirmed.
- The r80 `wc`/byte figures (78,647; 24,897 at `398cbe1`) are the r80 seat's, not re-measured by me. My figures are at `b284223`.
- The 618 B residual in the `.ufo` delta (§ 2) is unattributed.
- `Kb80K03`'s claim that r76/r78/r79 had no w2 wave is cited from its table; I did not re-derive it beyond r79's missing w2 files.
- No network: S249 not re-fetched; the plan's fetch record is taken as stated and matches S248's committed record.

## 7. Commands (all read-only)

- `ls considerthese/ | sort | tail -n 6`; `read` of considerthese 10-24/10-25/10-26; `read` of plans 79/80/81 (+ raw lines 26, 30, 40 of plan 81).
- `grep -rn "considerthese" corpus/lessons plans SCORECARD.md LOG.md` (dispositions).
- `wc -lc SKILL.md` → `596 80920 SKILL.md`; section `sed -n 448,519p SKILL.md | wc -c` → `26308`; `grep -n '^## ' SKILL.md`.
- `git -C . ls-files -z .ufo | xargs -0 du -cb` → 188,415,336 (15,648 files); `git ls-tree -r -l 398cbe1… -- .ufo | awk` → 174,588,093 (14,841); `git ls-tree -r -l HEAD -- .ufo/waves/round-80 | awk` → 13,826,625 (805).
- `git ls-tree -r -l HEAD -- .ufo | sort -k4 -n | tail -n 6` → `omp-live-18.12.2-strings.txt` 47,815,579.
- `grep -n "7bb48f" .ufo/waves/round-79/snapshots/S230.fetch.json` → 0; `…/S231.fetch.json` → 1.
- `grep -n "^| S248 " corpus/SOURCES.md` (cells 1–11 via awk) → status `queued`, used-by `—`.
- `sed -n 273,279p verifiers/verify_corpus_integrity.py` (`report_pointer_exists`); `sed -n 1529,1552p verifiers/verify_skill_checklist.py` (`citation_resolve`).
- `grep -n -E "report_pointers_|report_dead" .ufo/waves/round-80/build/Kb80E04DeadPointer/integrity-base.json`.
- `cmp` of the two `refresh-corpus-baseline.py` copies → IDENTICAL.
- Frontmatter description measure (python, read-only): `desc_chars 1021 first_sentence_chars 151`.
- `git apply --numstat` on `Kb80E04DeadPointer.patch` (17/0), `Kb80E05GrammarFix.patch` (10/3, 11/2), `Kb80E04DeadPointer/arms-only.patch` (11/0); `numstat-six.txt` (`check_assertion_floors` 22/3, `independent` 10/3, `integrity` 28/2).
- `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` → `/fast/scratch/hyaku` 591.3G free.

## 8. Actions for L1 before freeze (ordered)

1. Decide F1 (bind the LOG/symlink path via an amended E6 pin, or restate W8 and declare the residual). No narrowing after data.
2. Decide F2 and F3: add the forged-report and forged-manifest worlds with declared expected verdicts, or declare residuals in the claim text.
3. Fix the E6 arithmetic (F4): 22 base spend, 118 repair headroom, and the wording of the cap.
4. Fix R2's evidence pointer (F5): `S231.fetch.json` for `7bb48f`; S230 row corrected via S250.
5. Replace S249 with promoting S248, or justify the duplicate (F6).
6. Ensure the W9 and R1 controls test content, not existence (F7).
7. Put the SKILL.md edits in one commit and check the 600-line budget (F8).

VERDICT: No hard conflict between open considerthese dispositions and r81; the plan's C1 kill-rule controls (W8 as written, citing-repo forgery, lane-authored manifest), the E6 headroom arithmetic and the S230/S231 receipt pointer need fixing before freeze, and C2 should promote S248 rather than add a duplicate S249.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81K03Considerthese.md
