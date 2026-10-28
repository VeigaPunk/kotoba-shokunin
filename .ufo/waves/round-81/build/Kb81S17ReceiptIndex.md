# Kb81S17ReceiptIndex — round-81 w1 receipt index

Seat: `Kb81S17ReceiptIndex` (scribe, leaf; no subagents spawned). Date: 2026-10-27/28 UTC. Lane root:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Deliverable: this file — the canonical list of every receipt the round-81 report (`.ufo/reports/round-81/kotoba.md`,
drafted by `build/Kb81S04Report.md`) and the round-81 lesson (`corpus/lessons/round-81.md`, drafted by
`build/Kb81S01Lesson.md`) may cite, with the command that produces each, the claim/section that cites it, and a blocking flag.

Authority used (read, not recalled): `plans/round-81.md` § Trigger, § C1 (predicate, repairs R1–R6, E6 line set, kill rule,
worlds W0–W9), § C2 (predicate, conjuncts a–g, controls C0–C4), § Frontier, § Round shape and seats (Receipt discipline),
§ No-harm battery, § Inherited state; all 64 seat prompts in `.ufo/waves/round-81/w1-spec.json`; the r80 receipt index
(`.ufo/waves/round-80/build/Kb80S17ReceiptIndex.md`) for shape only; and the committed receipts themselves.

Citation tokens used below:

- `R:Work` = report § Work performed · `R:Landed` = § Landed changes · `R:Before→after` = § Before → after measurements ·
  `R:Sources` = § Sources & frontier · `R:SHONEN` = § SHONEN · `R:Stale` = § Stale-lane · `R:Tools` = § tool installs ·
  `R:L0` = § L0 questions.
- `L:Gate` = lesson § Gate · `L:Mistakes` = lesson § Mistakes · `L:Sources` = lesson § Sources & frontier.
- `B` = blocking: the report/lesson cannot be filed without this file existing. `NB` = cited if present; absence is a
  named gap, not a silent omission.

**Presence is not tabulated here.** The `build/` directory is written by 64 seats concurrently, so a per-row present/absent
column is stale within minutes. The live answer is the gate in § 12, which prints its own timestamped reading; its current
run is quoted there and the file `build/Kb81S17ReceiptIndex-status.txt` carries it verbatim with its own `exit=`.

---

## 1. C1 consistency (calibration sub-axis) — before-values and battery receipts

Frozen predicate: `python3 -B verifiers/check_tip_battery.py --rev <rev>` (round-81 bytes = the round-72/73/80 counter amended by
E6) prints `guards 5 of 5` and `tip battery exit 0: 6 of 6`, exit 0, in both `--repo .` (from the lane root) and absolute
`--repo <lane>` forms; at base `b2842231` it prints `tip battery exit 0: 4 of 6`, exit 1.

| # | receipt (lane-relative) | proves | producing command | cited by | block |
|---|---|---|---|---|---|
| C1-01 | `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` | base battery at `b2842231`: `guards 5 of 5`, `4 of 6`, per-gate exits (registry/floors/checklist/sweep 0; integrity/independent 1), spotcheck INFO lines | `python3 -B verifiers/check_tip_battery.py --rev b284223105f4d106f7e8f56ed4fd296c643cda0e --repo .` in a fleet-shaped world clone. The file records no `cmd=` header and no counter `exit=` (F2); plan § Trigger names the direct-exit capture | R:Before→after; L:Gate | **B** |
| C1-02 | `.ufo/waves/round-81/build/base-battery/01-tip-battery-dot.txt` | same command through the reusable runner, with `# rev= cmd= utc=` header and the counter's own `exit=` | `bash .ufo/waves/round-81/build/run-battery.sh b284223105f4d106f7e8f56ed4fd296c643cda0e /home/vgpnk/Projects/shokunin/kotoba-shokunin .ufo/waves/round-81/build/base-battery` | R:Before→after | **B** |
| C1-03 | `.ufo/waves/round-81/build/base-battery/02-tip-battery-abs.txt` | base in the absolute `--repo <lane>` form (the frozen predicate requires both forms; C1-01 covers only the dot form) | same runner invocation as C1-02 (receipt 02) | R:Before→after; L:Gate | **B** |
| C1-04…09 | `build/base-battery/{03-gate-registry,04-assertion-floors,05-skill-checklist,06-corpus-integrity,07-corpus-independent,08-correction-sweep}.txt` | base exits of the six gates, per gate, with own `exit=`; 06/07 carry the DRIFT names (`tracked_files`, `unindexed`, `report_total`, `report_dead`, `commit_unresolvable`) that § Trigger records | same runner invocation (receipts 03–08; `--json` is used for checklist/integrity/independent, see F4) | R:Before→after; R:Landed; L:Gate | **B** |
| C1-10 | `build/base-battery/09-census.txt` | census at base through the runner; note: reads the **live** lane tree, not `<rev>` (runner's own `# note=`) | same runner invocation (receipt 09) | R:Sources; L:Sources | **B** |
| C1-11 | `build/base-battery/index.txt` | per-receipt exit table + green/non-zero tally written by the runner | same runner invocation | R:Before→after | NB |
| C1-12 | `build/Kb81E10Battery.md` | the battery receipt index, one line per file (E10 prompt) | authored by seat `Kb81E10Battery` after the run | R:Before→after | **B** |
| C1-13 | `build/Kb81E11Receipts.txt` | **independent** re-derivation of the six gates at base, plus `git cat-file -e` for `HEAD:.ufo/reports/round-77/kotoba.md` and `round-76` in the lane and the fleet (expect lane 77 = 128, lane 76 = 0, fleet both 0) | E11's direct-exit runs, `cmd > f 2>&1; rc=$?` (never a pipeline, M80-1) | R:Before→after; L:Gate | **B** |

## 2. C1 — instrument, manifest, erratum and freeze receipts

| # | receipt | proves | producing command | cited by | block |
|---|---|---|---|---|---|
| C1-14 | `build/Kb81E01Integrity.patch` | R1 (report-pointer `<rev>:<path>` object resolution + report content identity: `## SHONEN` and ≥400 B) and R2a (external-commit verified binding) in `verify_corpus_integrity.py`, against `b2842231` | authored in a scratch clone by `Kb81E01Integrity`; `git -C "$S/clone" add -A && git -C "$S/clone" diff --cached --binary > …` | R:Landed; R:Before→after; L:Gate | **B** |
| C1-15 | `build/Kb81E01Integrity.blob` | the composed git-blob SHA of the patched `verify_corpus_integrity.py` — the value E6 adds to `INSTRUMENT_PINS` | `git -C "$S/clone" hash-object verifiers/verify_corpus_integrity.py` after applying the patch | R:Landed; L:Gate | **B** |
| C1-16 | `build/Kb81E02Independent.patch` | R2b, the independent second witness (`verify_corpus_independent.py`), agreeing check-for-check | as C1-14, in a separate scratch clone | R:Landed; R:Before→after; L:Gate | **B** |
| C1-17 | `build/Kb81E02Independent.blob` *(proposed name; F8)* | composed git-blob SHA of the E02-patched `verify_corpus_independent.py` — second E6 pin input | `git hash-object` on the patched file in the clone | R:Landed; L:Gate | **B** |
| C1-18 | `build/Kb81E03ExtManifest.json` | the candidate `verifiers/external-commits.json`: one object per exempt hash with `hash`, `repo`, `evidence` (committed receipt path), `pinned_at`. Landed content at index time: one entry, `7bb48f21…` → `mistralai/mistral-vibe`, evidence `.ufo/waves/round-79/snapshots/S231.fetch.json` | authored by `Kb81E03ExtManifest` from primary bytes (fetch record + live `ls-remote`) | R:Landed; L:Gate | **B** |
| C1-19 | `build/Kb81E03ExtManifest-fetch.txt` | the re-derived binding: `cat-file -t` absent in lane and fleet (rc=128 each), evidence path committed at base, live `git ls-remote` (mistral-vibe main = `7bb48f21…`; pi-mono main = `a9228305…`, 0 of 4120 advertised refs match), commit-pinned raw URL byte-identical to the snapshot (77,634 B, sha256 `fc48a5db…`) | the commands printed inside the file, each with its rc | R:Sources; L:Gate | **B** |
| C1-20 | `build/Kb81E04Baseline.patch` | R3 (`.ufo/wapes` disposition record) + R4 index mechanics: coverage-map row for `corpus/lessons/round-80-verifier-spotcheck.md` and the r81 files | authored in a scratch clone by `Kb81E04Baseline`; `mv` + recorded move for the untracked stray (git cannot `mv` untracked) | R:Landed; L:Gate | **B** |
| C1-21 | `build/Kb81E04Baseline.md` | ordered R3/R4 recipe + the expected post-integration `corpus-baseline.json` diff (expected `tracked_files` 154→156, `report_total` +1..+3, zero classes 0 — only with R1/R2 applied) | authored by E04 | R:Landed | NB |
| C1-22 | `build/refresh-corpus-baseline.py` | the r80 refresh script, ported unchanged unless broken; sole writer, refuses symlinks | `cp` from `.ufo/waves/round-80/build/refresh-corpus-baseline.py`; verify with `--help`/read of argparse | R:Landed; R:Before→after | **B** |
| C1-23 | `build/Kb81E05Erratum.patch` | E6 exactly: `LINE_CAP 40→140`; exactly two new `INSTRUMENT_PINS` blobs (C1-15, C1-17); self-test constants re-anchored to derive from `LINE_CAP`; comment cap mentions; no other line | authored in a scratch clone by `Kb81E05Erratum`, against `b2842231` | R:Landed; R:Before→after; L:Gate | **B** |
| C1-24 | `build/Kb81E05Erratum.sha256` | sha256 of the E6 patch (freeze input) | `sha256sum .ufo/waves/round-81/build/Kb81E05Erratum.patch` | R:Landed; L:Gate | **B** |
| C1-25 | `build/Kb81E05Erratum-counter.sha256` *(proposed name; F8)* | sha256 of the amended `verifiers/check_tip_battery.py` after applying E6 — the bytes the frozen predicate measures | apply the patch in the clone; `sha256sum verifiers/check_tip_battery.py` | R:Landed; L:Gate | **B** |
| C1-26 | `build/Kb81E14PinAudit.md` | pin audit + E6 cap arithmetic: counter base blob `a356e9d1…` sha256 `e33b17d7…`, `LINE_CAP 40`, six base blobs each inside its allowed tuple; added/deleted lines of E01+E02 vs the 140 cap and the 40-line base spend | `git rev-parse <rev>:<path>` (BLOB ids, not worktree `hash-object`), `git apply --numstat`, `sha256sum`; E14's recompute script is `build/Kb81E14PinAudit-recompute.py` | R:Before→after; L:Gate | **B** |
| C1-27 | `build/Kb81E14PinAudit-base.txt` | the base-only pin reading (all six base blobs PASS membership; "no patches applied") | `python3 -B .ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py` (E14's own script) | R:Before→after | NB |
| C1-28 | `build/Kb81E15Order.md` | the ordered integration recipe, dirty-tree precondition, per-group gate expectations, failure modes (refresh exit 2/3, blob mismatch, census duplicate ids) | authored by E15 | R:Landed | NB |
| C1-29 | `build/Kb81E13FixtureGuard.md` | tooling hygiene: hardcoded `/tmp`, pacman calls, network in the measured path, mutating git outside sandboxes, `external-commits.json` purity | authored by E13 over `verifiers/` + `.ufo/waves/round-81/build/*.py` and `*.sh` | R:Tools | NB |

## 3. C1 control worlds (kill-rule evidence; receipts committed before any after-value)

Both producers are needed and they are **not** the same set: `c1_controls.txt` is the plan's expected-shape sweep; `Kb81C01C1-*`
is the adversarial critic's attack.

| # | receipt | worlds / proves | producing command | cited by | block |
|---|---|---|---|---|---|
| C1-30 | `build/c1_controls.py` | the harness: isolated scratch git repo per world, `git init -q`, identity `scratch-r81`, every git call `-C`'d, toplevel asserted, honours `TMPDIR`/`--work` | authored by `Kb81E06Controls` | R:Work | NB |
| C1-31 | `build/c1_controls.txt` | per world — W0 empty commit (`4 of 6`), W1 index+baseline only (corpus gates red), W2 R1 only (≤5), W3 R2 only (≤5), W4 stubbed instrument (`instrument-pin`/`instrument-size`), W5 edited spot-check (`spotcheck-identity`), W6 lane-created commit + `owner/repo@` marker absent from the manifest (`commit_unresolvable` red), W7 dead lane hash behind a lane URL (red), W8 marker file at the fleet report path (`report_dead` red), W9 manifest entry without receipt proof (red): counter output line, exit, expected vs observed, PASS/FAIL | `python3 -B .ufo/waves/round-81/build/c1_controls.py --counter <amended counter> --base-tree <base checkout>` | R:Work; R:Before→after; L:Gate | **B** |
| C1-32 | `build/Kb81C01C1-*.txt` | the adversarial worlds: forged manifest entry binding the hash to the wrong repo; fabricated evidence with no ls-remote line; `<rev>:<path>` resolving to a non-report blob that contains `## SHONEN`; `HEAD:` divergence lane-vs-fleet; fleet marker (W10 reconstruction). Each world: counter output, exit, and whether it reached `6 of 6` wrongly | authored by `Kb81C01C1`; one receipt per world under `build/` | R:Work; L:Gate | **B** |
| C1-33 | `build/Kb81M01Instruments-*` *(proposed wildcard; F9)* | mutation receipts for R1+R2: `## SHONEN`→`## `, marker-only exemption (W8/W9 arms must go red), no fleet fallback, no ≥400 B bound | authored by `Kb81M01Instruments` in scratch clones | R:Landed | NB |
| C1-34 | `build/Kb81M02Battery-*` *(proposed wildcard; F9)* | mutation receipts for E6: revert `LINE_CAP` to 40, remove one pin, substitute a base blob in a pin tuple, 2-line stub at the new cap; plus format invariance of `fleet root … guards 5 of 5; tip battery exit 0: N of 6` | authored by `Kb81M02Battery` | R:Landed | NB |

## 4. C2 depth (sourced) — counter, entry, snapshot and controls

Frozen predicate: `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` prints `sdk allowed-tools surface documented N of 1`
and exits 0 iff N == 1 and conjuncts (a)–(g) hold; at base it prints `0 of 1`, exit 1.

| # | receipt | proves | producing command | cited by | block |
|---|---|---|---|---|---|
| C2-01 | `.ufo/waves/round-81/snapshots/S249.md` | the committed snapshot bytes of `https://code.claude.com/docs/en/agent-sdk/skills.md` (expected 28,395 B, sha256 `ac62c2df…` — re-derived, never trusted) | `curl -sS -L https://code.claude.com/docs/en/agent-sdk/skills.md -o <path>` by `Kb81E08C2Entry` (a second fetch by `Kb81R03ReopenS248`; canonical-bytes rule, F13) | R:Before→after; R:Sources; L:Gate | **B** |
| C2-02 | `.ufo/waves/round-81/snapshots/S249.fetch.json` | the fetch record: url, HTTP 200, bytes, sha256, fetched-at UTC. Conjunct (c) requires this sha256 to equal the counter pin **and** the row's anchor pin | written beside the curl by E08 (`sha256sum`, `wc -c`, `date -u`) | R:Sources; L:Gate | **B** |
| C2-03 | `build/Kb81R03Reopen-fetch.json` | the independent re-open of S249 (and S227's URL): HTTP, bytes, sha256 — flags byte instability if the sha moved | authored by `Kb81R03ReopenS248` from its own fetch | R:Sources | NB |
| C2-04 | `build/allowed-tools-sdk-round81.md` | the C2 entry text that lands as `corpus/knowledge/allowed-tools-sdk-round81.md`: `source:` S249 (URL + anchor) + S248, `verified-at: 2026-10-27`, `recheck:`, the documentary table (query-config `allowedTools`/`allowed_tools` beside frontmatter `allowed-tools`; managed-settings override), a Limits section, one located ≤25-word quote | authored by `Kb81E08C2Entry` from the snapshot bytes | R:Landed; R:Sources; L:Gate | **B** |
| C2-05 | `build/check_sdk_allowed_tools.py` | the new counter, self-contained stdlib; lands as `verifiers/check_sdk_allowed_tools.py` (the predicate's path — F7); prints the frozen line + diagnostic lines; `--self-test` drives satisfying/broken worlds | authored by `Kb81E09C2Counter`; freeze sha256 must be of the landed bytes | R:Landed; R:Before→after | **B** |
| C2-06 | `build/Kb81E09C2Counter-selftest.txt` | the counter's self-test run: full output + exit (satisfying world exits 0 with the exact line; broken conjuncts / pin mismatch / S248-usedby / quote-outside-text-view exit 1) | `python3 -B build/check_sdk_allowed_tools.py --self-test > … 2>&1; rc=$?` | R:Landed; L:Gate | **B** |
| C2-07 | `build/Kb81E09C2Counter-base.txt` | the C2 **before-value** at `b2842231`: `sdk allowed-tools surface documented 0 of 1`, exit 1 | `python3 -B build/check_sdk_allowed_tools.py --rev b284223105f4d106f7e8f56ed4fd296c643cda0e` in the base tree | R:Before→after; L:Gate | **B** |
| C2-08 | `build/c2_controls.py` | the C2 control harness: C0 base, C1 sha-mismatched pin, C2 row present but S248 `used-by` unchanged, C3 quote without committed snapshot bytes, C4 first-answer `1` with no files → 0; isolated scratch repos | authored by `Kb81E07C2Worlds` | R:Work | NB |
| C2-09 | `build/c2_controls.txt` | per world: exact output line, exit, expected vs observed, PASS/FAIL | `python3 -B build/c2_controls.py --counter <counter> --base-tree <base>` | R:Work; R:Before→after; L:Gate | **B** |
| C2-10 | `build/Kb81C02C2-*.txt` | the critic's worlds: entry byte-perfect with the snapshot at a different path (location- vs content-bound pin); S249 `used-by` updated while S248 is not (is (e) enforced?); quote relocated before the first heading (Q70); SDK page text replaced by an unrelated page at the same URL pin; the semantic hole (`allowedTools` is a query option, not frontmatter) | authored by `Kb81C02C2`, one receipt per world | R:Work; L:Gate | **B** |
| C2-11 | `build/Kb81M03C2-*` *(proposed wildcard; F9)* | mutation receipts: sha256 constant typo, `used-by` check removed, quote check weakened to substring-in-file, `N == 1` → `N >= 1` | authored by `Kb81M03C2` | R:Landed | NB |
| C2-12 | `build/Kb81S05SourcesEdits.md` | the exact SOURCES text: S249 (11 cells, tier justification, anchor with § + sha256 + located quote), S250 (`supersedes S230 —`, verified `mistralai/mistral-vibe` binding), S248 `used-by` old→new; each row verified to parse 11 cells (`awk -F'\|'` → NF 13) | authored by `Kb81S05SourcesEdits`; parse check printed in the file | R:Sources; L:Gate | **B** |
| C2-13 | `build/Kb81S11GateQuotes.md` | located-quote ledger: S249 quote (≤25 words), its snapshot line/offset and `grep -c` one-occurrence evidence; S250's located binding fact and its receipt; which bytes each touched row claims and where they live | authored by `Kb81S11GateQuotes` against the committed snapshot | R:Sources; L:Gate | **B** |
| C2-14 | `build/Kb81S08ReadmeRows.md` | coverage-map rows (`round-80-verifier-spotcheck`, `round-81`, the SDK entry) + the append-only `## Frontier` note (conjunct g) | authored by `Kb81S08ReadmeRows` | R:Sources; L:Gate | **B** |
| C2-15 | `build/Kb81S09SkillRule.md` | the SKILL.md SDK-channel rule line(s) + the `## Gate registry` row for `verifiers/check_sdk_allowed_tools.py` (conjunct f), verified by a registry run on a scratch clone | authored by `Kb81S09SkillRule`; `python3 -B verifiers/check_gate_registry.py --rev <base>` on the clone | R:Landed; L:Gate | **B** |
| C2-16 | `build/Kb81S10Province.md` | the `PROVINCE.md` `## Core` bullet extension naming the SDK channel (conjunct g), with `check_sibling_census.py --province` re-run green and `## Adjacent` untouched | authored by `Kb81S10Province` | R:Landed; L:Gate | **B** |

## 5. Frontier — census, sources, assimilation (lesson § Sources & frontier)

| # | receipt | proves | producing command | cited by | block |
|---|---|---|---|---|---|
| FR-01 | `.ufo/waves/round-81/receipts/census-before.txt` | census at round start: 31 `W04` duplicate-URL lines + `kotoba ok`; row count at base is 174 | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`. No `exit=` and no row-count line (F1); the 174 comes from `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (measured 174, exit 0) | R:Sources; L:Sources | **B** |
| FR-02 | `build/Kb81E12Census.txt` | before/after census blocks + row counts + the exact SOURCES edits applied on a scratch clone; every new row parses to 11 cells | authored by `Kb81E12Census`; census + `grep -cE` in the clone, own-exit capture | R:Sources; L:Sources | **B** |
| FR-03 | `build/Kb81S16CensusLog.md` | per-row old→new record (S248 `used-by`; S249, S250 new) and `174 -> N` row-count lines with their commands, in lesson paste-ready form | authored by `Kb81S16CensusLog` from FR-02 | R:Sources; L:Sources | **B** |
| FR-04 | `build/Kb81E16Shokuknow-slice.txt` | the quarantine-register slice, re-derived with the exact `awk -F'\|'` recipe; every line carries an S-id | E16's prescribed `awk` over `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` | R:Sources; L:Gate | **B** |
| FR-05 | `build/Kb81E16Shokuknow-collisions.txt` | staged-id collision set: `comm -12` of lane S-ids and `merge/kotoba/SOURCES.append.md` ids — proves adoption stays closed | the extraction + `comm -12` printed in the file | R:Sources; L:Gate | **B** |
| FR-06 | `build/Kb81S12AssimDisp.md` | the lesson-pasteable assimilation + considerthese disposition text (slice verdict, collision arithmetic, P2–P5 dispositioned in r80, none implemented; newest file `2026-10-26.md`) | authored by `Kb81S12AssimDisp` from FR-04/FR-05 and the considerthese file | L:Gate; R:Sources | **B** |
| FR-07 | `build/Kb81R01NegSweep.md` | the S249-class negative sweep: per URL http/bytes/sha256, ≤25-word quote or the observed absence reason, admit/reject/queued | authored by `Kb81R01NegSweep`; per-file fetch records under `build/` | R:Sources | NB |
| FR-08 | `build/Kb81E04Baseline.patch` + `dispositions/wapes.txt` | the committed evidence that `.ufo/wapes` bytes were moved out of the lane root and deleted there | `mv .ufo/wapes .ufo/waves/round-81/dispositions/wapes.txt` (recorded), then `git status --porcelain` shows no `?? .ufo/wapes` | R:Landed; L:Mistakes | **B** |

## 6. Freeze and report/lesson text receipts

| # | receipt | proves | producing command | cited by | block |
|---|---|---|---|---|---|
| FZ-01 | `.ufo/waves/round-81/receipts/freeze-shas.txt` | the freeze: amended counter sha256, the two instrument blob shas, the C2 counter sha256, each patch sha256, the manifest sha256, the S249 snapshot sha256 — **recorded before any after-value is measured** | assembled by `Kb81S15FreezeShas` from C1-13…C1-25 and C2-01/C2-05; committed copy of `build/Kb81S15FreezeShas.md` with markers resolved | R:Before→after; L:Gate; LOG § Round 81 | **B** |
| FZ-02 | `build/Kb81S15FreezeShas.md` | the draft with `{{…}}` markers + the one-sentence E6 justification (pin guard carries the anti-laundering load; size bound secondary) | authored by `Kb81S15FreezeShas` | R:Landed | **B** |
| FZ-03 | `build/Kb81S01Lesson.md` | the full `corpus/lessons/round-81.md` draft (Gate / Mistakes / Sources & frontier), all `{{…}}` markers | authored by `Kb81S01Lesson` | lesson | **B** |
| FZ-04 | `build/Kb81S02Log.md` | the `## Round 81` LOG.md entry draft, per-claim predicate lines, receipt paths, wave shape, routed-defect dispositions | authored by `Kb81S02Log` | LOG.md | **B** |
| FZ-05 | `build/Kb81S03Scorecard.md` | append-only SCORECARD annotations: C1 consistency (`4 of 6` → `6 of 6`, score held 10, amended counter sha256), C2 depth (`0 of 1` → `1 of 1`, new counter sha256, score held 9), round-82 planned row | authored by `Kb81S03Scorecard` | SCORECARD.md | **B** |
| FZ-06 | `build/Kb81S04Report.md` | the fleet report skeleton, every section in order, `{{…}}` markers for values | authored by `Kb81S04Report` | report | **B** |
| FZ-07 | `build/Kb81S06Shonen.md` | the SHONEN box-state re-derivation at base with resolvable evidence pointers per box | authored by `Kb81S06Shonen`; the mid-run support receipts are `build/Kb81S06Shonen-receipt-*` | R:SHONEN | **B** |
| FZ-08 | `build/Kb81S07Quality.md` | the Q76 candidate row (stray probe output only inside the wave dir), grounded in M81-1/R80-D2, shown able to fail | authored by `Kb81S07Quality`; support `build/Kb81S07Quality.receipts.txt` | L:Mistakes; R:Sources | NB |
| FZ-09 | `build/Kb81S13L0.md` | either the exact L0 append lines or the explicit no-L0 finding | authored by `Kb81S13L0` | R:L0 | NB |
| FZ-10 | `build/Kb81S14WaveRegistry.md` | the wave evidence index, every seat report and build file grouped by claim, PENDING for expected-but-absent | authored by `Kb81S14WaveRegistry` | R:Work; R:Stale | **B** |
| FZ-11 | `build/Kb81S17ReceiptIndex.md` | this file | authored by this seat | R:Work; L:Gate | **B** |
| FZ-12 | `build/Kb81S17ReceiptIndex-status.txt` | the presence gate's own reading with `# utc=`, `# cmd=`, `exit=` | `{ printf '# utc=…'; python3 -B .ufo/waves/round-81/build/Kb81S17ReceiptIndex-check.py; rc=$?; printf 'exit=%s\n' "$rc"; } > …` | R:Work | NB |

## 7. After-value receipts (the only admissible sources for the claim after-values)

The plan pins the *commands* but not these filenames; the names below are proposed (F10) and the L1 fixes them at integration.
**None existed at this seat's last gate run; every one is blocking for the report.**

| # | receipt | claims it carries | producing command | cited by |
|---|---|---|---|---|
| AV-01 | `receipts/after-final-dot.txt` | C1 `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, `--repo .` from the lane root at the landed tip | `bash .ufo/waves/round-81/build/run-battery.sh <tip> /home/vgpnk/Projects/shokunin/kotoba-shokunin .ufo/waves/round-81/receipts/final` (receipt 01), or the same command directly with own-exit capture | R:Before→after; L:Gate |
| AV-02 | `receipts/after-final-abs.txt` | same, absolute `--repo <lane>` form | runner receipt 02 | R:Before→after; L:Gate |
| AV-03 | `receipts/after-final-c2.txt` | C2 `sdk allowed-tools surface documented 1 of 1`, exit 0, at the landed tip | `python3 -B verifiers/check_sdk_allowed_tools.py --rev <tip> > f 2>&1; rc=$?` | R:Before→after; L:Gate |
| AV-04 | `receipts/census-after.txt` | census after the SOURCES edits: `kotoba ok`, W04 count, row count, and its **own exit** (F1) | `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba > f 2>&1; rc=$?` + the row-count `grep -cE` from FR-01 | R:Sources; L:Sources |
| AV-05 | `receipts/baseline-refresh.txt` | `refresh-corpus-baseline.py` run at the final pre-report commit + resulting `corpus-baseline.json` diff (every zero class 0) | `python3 .ufo/waves/round-81/build/refresh-corpus-baseline.py --repo . > f 2>&1; rc=$?` + `git diff -- verifiers/corpus-baseline.json` | R:Landed; L:Gate |
| AV-06 | `receipts/sibling-census.txt` | `check_sibling_census.py --skill SKILL.md` (plan § No-harm battery; the runner does **not** run it — F3) | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md > f 2>&1; rc=$?` | R:Landed; L:Gate |
| AV-07 | `receipts/report-pointers.txt` | `check_report_pointers.py --report .ufo/reports/round-81/kotoba.md` at the report commit (Q68) | `python3 -B verifiers/check_report_pointers.py --report .ufo/reports/round-81/kotoba.md --repo . --rev <tip> > f 2>&1; rc=$?` (the runner's conditional receipt 15, F4) | R:Landed |

## 8. No-harm battery (plan § No-harm battery) → receipt coverage

| plan command | runner receipt | gap |
|---|---|---|
| `check_tip_battery.py --rev <tip>` both forms | `01-tip-battery-dot.txt`, `02-tip-battery-abs.txt` | none |
| `check_gate_registry.py --rev <tip>` | `03-gate-registry.txt` | at base the C2 gate row does not exist; the **after** run is what proves R6 (F16) |
| `check_assertion_floors.py` | `04-assertion-floors.txt` (`--self-test`, ~103 s) | none |
| `verify_skill_checklist.py` | `05-skill-checklist.txt` (`--json`; plan names no flag — F4) | shape difference only |
| `verify_corpus_integrity.py` | `06-corpus-integrity.txt` (`--json`) | DRIFT names live in the JSON body; quote them from there |
| `verify_corpus_independent.py` | `07-corpus-independent.txt` (`--json`) | same |
| `check_correction_sweep.py --root .` | `08-correction-sweep.txt` | none |
| `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | `09-census.txt` | runs against the **live** lane tree, not `<rev>` (runner `# note=`); report must say so |
| `check_sibling_census.py --skill SKILL.md` | — | **not implemented by `run-battery.sh`** (F3); AV-06 |
| `check_report_pointers.py --report .ufo/reports/round-81/kotoba.md` | `15-report-pointers.txt` (only when `<report-path>` is passed) | conditional and not revision-bound (F4); AV-07 |

## 9. Before → after value map (each figure may be stated only from the named receipt)

| value | claim | admissible receipt(s) | command |
|---|---|---|---|
| `4 of 6`, exit 1, base dot form | C1 before | C1-01 (figure) + C1-02 (own exit) | `check_tip_battery.py --rev b2842231… --repo .` |
| `4 of 6`, exit 1, base absolute form | C1 before | C1-03 | runner receipt 02 |
| base gate exits 0/1/0/0/1/1 | C1 before | C1-04…09 + C1-13 (independent) | runner receipts 03–08 |
| `6 of 6`, exit 0, both forms | C1 after | AV-01, AV-02 | `check_tip_battery.py --rev <tip>` both forms |
| `instrument-size`/`instrument-pin` PASS at tip | C1 after | AV-01/02 guard lines + C1-26 cap arithmetic | counter output + `git apply --numstat` |
| `0 of 1`, exit 1 | C2 before | C2-07 | `check_sdk_allowed_tools.py --rev b2842231…` |
| `1 of 1`, exit 0 | C2 after | AV-03 | `check_sdk_allowed_tools.py --rev <tip>` |
| S249 sha256 + bytes | C2 source | C2-01, C2-02, FZ-01, and the row's anchor (C2-12) — four-way identity for conjunct (c) | `sha256sum`, `wc -c` |
| SOURCES rows `174 -> N` | frontier | FR-01 (174), FR-02/FR-03 (after) + AV-04 | the row-count `grep -cE` |
| census exit 0 / W04 count | frontier | FR-01 (no exit — F1), AV-04 (must carry exit) | `sources-census.sh validate …` |
| `report_dead` 1, `commit_unresolvable` 2 at base; 0 at tip | C1 | C1-05/06/07 at base; tip gate receipts + AV-05 at after | corpus gates + baseline diff |
| cap arithmetic (`40 + added <= 140`) | C1 | C1-26 (E14) + C1-23 (numstat) | `git apply --numstat` |
| 64 seats, 16/17/9/3/6/6/4/1/1/1, attack 17/64 | round shape | `.ufo/waves/round-81/w1-spec.json` + `w1-dispatch.json` + FZ-10 | `python3 -c` role census over the spec (this seat measured the counts: attack 17 of 64) |
| settled/dead seat counts | R:Work/R:Stale | `w1-results.json` (orchestrator, F17) + FZ-10 | orchestrator wave settle |

## 10. Inherited receipts the report/lesson may cite (committed at base; verified present by this seat)

| receipt | why r81 cites it | verified |
|---|---|---|
| `.ufo/waves/round-80/build/Kb80E04DeadPointer.patch` | R1's port source; the r80 design stopped at `cat-file -e` (existence only) and r81 adds content identity | present |
| `.ufo/waves/round-80/w1/Kb80E05GrammarFix.md` | R2's superseded design; names its own residual "line scope is spoofable by construction" | present |
| `.ufo/waves/round-80/build/refresh-corpus-baseline.py` | the R4 refresh script's source | present |
| `.ufo/waves/round-80/build/run-battery.sh` | the battery runner's source | present |
| `.ufo/waves/round-80/build/Kb80E15BaselineOrder.md` | the integration-order runbook's source | present |
| `.ufo/waves/round-80/build/Kb80C01C1-canonical-{lane-at,lane-url,fleet-marker}-tipbattery.txt` (30 `Kb80C01C1-*` files in all) | the r80 W8–W10 kill receipts; r81's W6–W8/W9 are their strengthened equivalents | present (count: 30) |
| `.ufo/waves/round-79/snapshots/S230.fetch.json` | pi-mono `main` = `bb65e3e4…`, last path-touching `25cc5c7b…` — the negative half of the S250 binding | present |
| `.ufo/waves/round-79/snapshots/S231.fetch.json` | mistral-vibe `main` = `7bb48f21…` at `2026-10-27T21:43:03Z`; the manifest's evidence path (C1-18) | present |
| `corpus/lessons/round-80-verifier-spotcheck.md` | the closure-owned spot-check file that R4 indexes (indexed, never edited) | present |

## 11. Findings (each carries its establishing command)

1. **F1 — the base census receipt is not self-describing.** `receipts/census-before.txt` has no `exit=` line and no row count
   (`grep -c '^exit=' …` → `0`), yet plan § Frontier and the lesson draft cite it for "exit 0, 174 rows". The row count is
   separately measured (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `174`, exit 0). AV-04 must
   carry its own exit and row count; same class as r80 F1/M80-1.
2. **F2 — the base tip-battery receipt carries no command and no counter exit.** `grep -c '^exit=' receipts/tipbattery-base-dot.txt`
   → `0`; the file starts `measured rev … in a fleet-shaped sandbox` and names no `cmd=`. The plan's `exit 1` is a reading of a
   4-of-6 predicate, not a recorded status. The runner receipts (C1-02/03) are the fix. Note also that `base 072048fa…` on line 2 is
   the *counter's* base blob (`verifiers/check_tip_battery.py:108 BASE = "072048fa…"`), not the lane base — citations must not
   conflate the two.
3. **F3 — `run-battery.sh` does not cover two plan battery commands.** `grep -n 'sibling' .ufo/waves/round-81/build/run-battery.sh`
   → no match. The plan § No-harm battery names `check_sibling_census.py --skill SKILL.md`; S10 also needs `check_province_core.py`.
   These need their own receipts (AV-06); the report must not claim "the full battery" from the runner alone.
4. **F4 — runner shape differences the report must state.** Report pointers are receipt 15 only when a `<report-path>` argument is
   passed, and that gate is not revision-bound; receipt 09 runs the census against the **live** lane tree (the runner prints
   `# note=census reads the LIVE lane tree … not $rev`); receipts 05–07 pass `--json` where the plan names no flag. Same
   verdicts, different capture shape — say so rather than implying byte-identical commands.
5. **F5 — producer/consumer path mismatch on the battery receipts.** `build/Kb81S01Lesson.md` cites
   `.ufo/waves/round-81/build/Kb81E10Battery/…` as the probe-output example; the runner's out-dir and the E10 prompt name
   `build/base-battery/`. The producer wins; S01's pointer is content-dead as written and must be corrected at paste (r80 F5 class).
6. **F6 — freeze file lives in two places.** Plan § C1 requires the counter sha256 in `.ufo/waves/round-81/receipts/freeze-shas.txt`
   (blocking, FZ-01); S15 writes `build/Kb81S15FreezeShas.md` (FZ-02). The `receipts/` copy is the claim artifact; the build file is
   the draft. LOG/S02 already cite the `receipts/` path.
7. **F7 — build path vs claim path.** E09 publishes `build/check_sdk_allowed_tools.py`; the C2 predicate runs
   `verifiers/check_sdk_allowed_tools.py` (absent at base). E03 publishes `build/Kb81E03ExtManifest.json`; the claim requires
   `verifiers/external-commits.json` (also absent at base). The freeze sha256 must be of the **landed** bytes, and the R6 registry
   row must land in the same commit as the counter.
8. **F8 — two freeze inputs have no pinned filename.** E05's prompt says "a counter-bytes sha256 receipt" and E02's says "gains
   E02's blob sha the same way" without naming files. Proposed: `build/Kb81E05Erratum-counter.sha256`, `build/Kb81E02Independent.blob`.
   If the L1 keeps other names, FZ-01 must inline the values so the freeze is self-contained.
9. **F9 — control receipts: one file vs per-world files.** E06's output is a single `c1_controls.txt` (per-world blocks inside);
   C01C1/C02C2 emit `Kb81C01C1-*.txt` / `Kb81C02C2-*.txt`. The plan's kill rule is satisfied only if the cited receipt shows, per
   world, expected vs observed and the counter's exact output line; the mutation-test receipts (M01/M02/M03) are named only as
   "receipts" — the wildcards in § 3/§ 4 are placeholders, not producer promises.
10. **F10 — after-value filenames are not frozen.** The plan names commands, not files. § 7 proposes the names; the L1 must fix them
    before the first after-value is run, and the freeze receipt (FZ-01) should name them so the after-value cannot be re-run into a
    different file later.
11. **F11 — census warning count drift in the lesson draft.** S01 says "32 W04 duplicate-URL warnings"; measured
    `grep -c 'W04' receipts/census-before.txt` → `31` (the 32nd output line is `kotoba ok`). Correct the number at paste; the r80
    report's `31` at 174 rows agrees with this measurement.
12. **F12 — E04's expected baseline arithmetic is a seam, not a promise.** E04's prompt expects `tracked_files 154→156` and
    `report_total +1..+3`; plan § Trigger records base `tracked_files 155≠154`. The receipt must show the actual JSON diff from the
    refresh run after all files land, never the hoped numbers.
13. **F13 — one canonical S249 snapshot must win.** E08 and R03 both fetch the page; if their sha256 differs, the counter pin, the
    row anchor and the fetch record must all point at the same bytes (R03's prompt: prefer fresher, and say so). The freeze's
    snapshot sha256 (FZ-01) is the tiebreak; a second snapshot under another name may exist but must not be the cited one.
14. **F14 — freeze ordering is a hard dependency.** E14's cap arithmetic needs E01+E02; E6's pins need the composed blobs; the
    freeze receipt must be written **before** any after-value. At the last gate run E14 had published only the base audit
    (`Kb81E14PinAudit-base.txt`, "no patches applied"), so no freeze can be complete yet. Expected mid-wave, not a defect.
15. **F15 — freshness clock roll.** E03's live `ls-remote` runs are stamped `2026-10-28T02:28:14Z` while the plan declares the
    access date `2026-10-27` and the r79 fetch is `2026-10-27T21:43:03Z`. The report's Sources section must give both stamps (plan
    date and the r81 verification UTC), and S250's row must not claim a 2026-10-27 live check it did not make. Folded into the
    freshness verdict, not a plan erratum.
16. **F16 — R6 has no base receipt of its own.** The registry gate at base cannot see the new counter row. Only the **after** tip run
    (AV-01/02 receipt 03 and AV-05) proves the registry accepts `verifiers/check_sdk_allowed_tools.py`. The report must cite the after
    run for R6, not the base one.
17. **F17 — orchestrator artifacts are not seat receipts.** `w1-results.json` (cited by S02) is produced at wave settle;
    `w1-dispatch.json`/`w1-spec.json`/`w1.ready` are wave fixtures. They are cited for the roster and settled-seat counts, never for
    a claim value.
18. **F18 — `build/` is a live directory shared by 64 seats.** The presence gate is a snapshot; a file can appear between two runs
    without any producer being wrong. Re-run the gate at integration; do not diff two snapshots as if they were one measurement.

## 12. Presence gate (re-runnable, own exit)

- Script: `build/Kb81S17ReceiptIndex-check.py` (stdlib; runs from the lane root).
- Command: `python3 -B .ufo/waves/round-81/build/Kb81S17ReceiptIndex-check.py`
- Exit semantics: `0` all fixed blocking receipts + all subjects present · `1` a fixed-path blocking receipt is missing · `2` fixed
  paths complete but a proposed subject is missing · `3` environment error (lane root/spec unreadable).
- Reading in `build/Kb81S17ReceiptIndex-status.txt` (own `exit` recorded there): **fixed rows 68, blocking 54; 9 proposed subjects;
  64 seat-report slots.** The file's current reading is authoritative over any restatement here. At `2026-10-28T02:32:34Z` it read
  `fixed missing=32 blocking missing=25`, `subjects=9 missing=9`, `seat reports 22/64`, `exit=1`; the two earlier runs in the same
  file's history read 4/64 and 16/64 seat reports, so the directory was still filling while this index was written (F18). The
  still-pending blocking set is the instruments (E01/E02/E04/E05/E06), the C2 counter and both control sets, E12/S16, S11, and the
  freeze/disposition files. Absence here is not a producer verdict.

## Limits

- Presence is not correctness: a file that exists with the wrong bytes passes this gate and fails its own counter. Byte identity
  belongs to C1-26 (pins), C2-02/C2-12 (snapshot) and FZ-01 (freeze).
- This seat ran no claim counter and no gate. Its executed checks are the presence gate in § 12 (exit 1) and the counting commands
  quoted with their figures: `grep -c 'W04'` → 31, `grep -c '^exit='` → 0 on both base receipts, SOURCES rows → 174,
  r80 `Kb80C01C1-*` files → 30, `verifiers/check_sdk_allowed_tools.py` and `verifiers/external-commits.json` → ENOENT, role census
  → 16/17/9/3/6/6/4/1/1/1 with attack 17/64, SOURCES anchor rows S230 `:171`, S231 `:172`, S248 `:189`.
- Proposed names (C1-17, C1-25, C1-33/34, C2-11, AV-01…07, F9 wildcards) are this seat's canonical proposals; when the L1 fixes a
  different name, update this index rather than leaving a second convention.
- No tool installs; pacman untouched. Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81S17ReceiptIndex/` (prompt extraction and the role
  census) is removed before yielding.

VERDICT: Receipt index complete and re-runnable — 68 fixed-path receipts (54 blocking) + 9 proposed subjects + 64 seat-report slots, each mapped to claim, report/lesson section and producing command; 18 findings, of which F1, F2, F3, F6, F7, F10 and F14 block or shape the report; presence gate reads exit 1 mid-wave with the blocking set still landing.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S17ReceiptIndex.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S17ReceiptIndex-check.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S17ReceiptIndex-status.txt
