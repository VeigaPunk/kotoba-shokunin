# Kb80S17ReceiptIndex — seat report

Seat: `Kb80S17ReceiptIndex` (scribe, leaf; no subagents spawned). Date: 2026-10-27.
Lane root: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Deliverable: `.ufo/waves/round-80/build/Kb80S17ReceiptIndex.md` — the canonical receipt index the round-80 report (`build/Kb80S04Report.md` → `.ufo/reports/round-80/kotoba.md`) and lesson (`build/Kb80S01Lesson.md` → `corpus/lessons/round-80.md`) draw on.

## Behavior

Built the index from the authority set, not from guesswork: `plans/round-80.md` (§ C1, § C2, § Frontier, § Round shape, § Receipt discipline, § No-harm battery) plus all 64 seat prompts extracted from `.ufo/waves/round-80/w1-spec.json`. For each receipt the index states the lane-relative path, what it proves, the command that produces it, the claim/section or report marker that cites it, and whether it is blocking. It also carries (a) a battery-value → receipt map (every before/after figure the report may state and the only file allowed to carry it), (b) an own-exit audit of the committed receipts, (c) sixteen findings with their establishing commands, and (d) a re-runnable presence gate.

## Artifacts produced (all under `.ufo/waves/round-80/build/`)

| File | How produced | Status |
|---|---|---|
| `Kb80S17ReceiptIndex.md` | authored (this seat) | 60 fixed-path rows (51 blocking), 16 mandatory subjects, 65 seat-report slots, 16 findings, marker mapping for the report's receipt-valued `{{…}}` placeholders |
| `Kb80S17ReceiptIndex-check.py` | authored; `python3 -B …-check.py` from the lane root | exit 1 at 23:34:38Z (11 blocking fixed paths + 16 subjects still missing mid-wave) |
| `Kb80S17ReceiptIndex-status.txt` | `{ printf '# utc=…'; python3 -B .ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py; rc=$?; printf 'exit=%s\n' "$rc"; } > …` | own-exit line present, `exit=1` |

Checker exit semantics (documented in the file header): `0` all fixed-path blocking receipts + all subjects present · `1` a fixed-path blocking receipt missing · `2` fixed paths complete, subject receipts missing under the proposed names.

## Measurements this seat actually took (each with its command)

- Presence sweep: `python3 -B .ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py` → at 23:34:38Z: fixed rows 60, blocking 51, blocking missing 11; subjects 16/16 missing; seat reports 45/65 present; exit 1. (`build/Kb80S17ReceiptIndex-status.txt`.)
- Base census row count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `157` (rc=0). Corroborates `build/Kb80S16CensusLog-rowcounts.txt` (`rows=157 rc=0`).
- Role/attack census: `python3 -c "…collections.Counter(i['role'] …w1-spec.json…)…"` → 16 executors, 17 scribes, 9 scouts, 3 connectors, 6 critics, 6 reviewers, 4 mutation-testers, 1 sentinel, 1 simplifier, 1 revenger; attack `17` of `64` (26.6 %).
- Own-exit audit: `grep -c '^exit=' .ufo/waves/round-80/receipts/census-before.txt` → 0; same on `.ufo/waves/round-79/receipts/{census-before,census-final}.txt` → 1 each.
- Pins: `ls .ufo/waves/round-79/snapshots/` → 18 files (6 bodies + 6 `.manifest` + 6 `.fetch.json`), **no `MANIFEST.sha256`**; `S226.manifest` = `9a67de89…  S226-spec.md`, equal to `S226.fetch.json`.
- Port source existence: `ls -d .ufo/waves/round-79/build/Kb79E04DeadPointer` → exists (the S04 draft's `Kb79E04DeadPointer/Kb79E04DeadPointer.patch` path is real, not dead).
- Committed base set: `git ls-tree -r --name-only HEAD .ufo/waves/round-80/` → `build-w1-spec.py`, `receipts/{census-before,m80-1-pipe-vs-direct,tipbattery-base-dot}.txt`, `w1-{dispatch,dispatch-output,spec}.json`.

## Findings (detail + commands in the index, § 5)

1. **F1** `receipts/census-before.txt` has no own-exit line and no row count, yet plan § Frontier and the report cite it for "exit 0, 157 rows"; the r79 census receipts did carry `exit=0` — a capture-discipline regression. Cite the rowcount receipt for 157; make the after-receipt carry both.
2. **F2** Plan § Trigger cites `receipts/tipbattery-base-abs.txt`; the file does not exist (checker row B02). The absolute-form base reading is unreceipted.
3. **F3** Plan § C2 and the E08 prompt require pins "equal in `MANIFEST.sha256`", which does not exist; pins live in per-snapshot `.manifest`/`.fetch.json`. Publish an aggregate manifest or name the per-snapshot file in the counter and report.
4. **F4** Plan § C2 cites `w1/Kb80ReopenSix.md`; the seat is `Kb80R03ReopenSix` → `w1/Kb80R03ReopenSix.md`. `build/Kb80R07ClosureScan.md` already repeats the plan's wrong name; correct the propagation, do not create a duplicate.
5. **F5** Producer/consumer path mismatches in prompts: `Kb80R01NegSweep` publishes `build/` while S05 and E12 read `w1/`; `Kb80R06ShokuknowSlice` publishes `build/` while S12 (and S01) read `w1/`. Producer path wins; affected reports must name the path used or the L1 re-runs the step.
6. **F6** The `Kb80S02Log` prompt instructs "attack share 18/64 = 28.1 %"; the dispatched spec and plan are `17/64 = 26.6 %` (count above). The LOG draft must not carry 18/64.
7. **F7** The r79 port source for repair 2 is `Kb79E02LogCitation.patch` only (`Kb80E02LogCitation.patch` does not exist); the index pins the real name.
8. **F8** `build/run-battery.sh` runs both battery forms, six gates, census, SKILL size figures and optional report pointers — it does **not** run `check_sibling_census.py` (Q72) or the C2 counter; those need separate tip receipts (EXT01, EXT03).
9. **F9** Ordering: `freeze-shas.txt` must be written and committed **before** the C1/C2 tip runs; the receipt timestamps are the audit. Pre-data control worlds are permitted before it.
10. **F10** The S04 draft points at `w1/Kb80S04Report.md` for the marker register; that path is the seat report — content must carry the register or the pointer is content-dead (V05 judges).
11. **F11** Lane hygiene: an untracked regular file `.ufo/wapes` (594 B, 2026-10-27 20:17 local) — a typo of `.ufo/waves` from a sibling seat's Q70 quote probe (content: four `words=… ok=False` lines, `exit=0`). Left in place (outside my write scope); untracked, so the L1 removes it before filing or the misroot sweep reports it.
12. **F12** Cross-seat pin composition: `build/Kb80E04DeadPointer.blob` (`051b8c5f…`) is the E04-only integrity blob; E05 edits both gates, so E5 must pin the composed E04∘E05 blob — pinning the E04-only value fails `instrument-pin` by construction and would fake an honest stop.

13. **F13** Attribution conflict (V03 audit): the plan §Trigger names `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` as the two base `commit_unresolvable` tokens, but the blockers are pure-hex backticked tokens at `corpus/SOURCES.md:171-172` (rows S230/S231, `7bb48f21…`, third-repo name in a separate code span). I verified the token shape and that `451a02ff` occurs in SOURCES only in raw URLs / `cfb894a5` not at all, but did not run the gates — FR12/FR13 site lists must settle it; a `owner/repo@<hex>`-only class would not clear C1. Do not rewrite the SOURCES rows.

14. **F14** C2/C1 seam: `build/allowed-tools-surfaces-round80.md:125` carries a full-hex commit citation (`7bb48f21…`) whose only repo hint is the bare name `mistral-vibe` — landing the C2 entry would add a third `commit_unresolvable` under the class's red-before arm shape unless the class treats a bare repo name as the external marker or the line carries an explicit owner/repo marker. Entry and class must be co-designed. Also recorded: E10 measures all 22 base added lines in `check_assertion_floors.py` (39 after E04), leaving **21** lines for grammar across both gates, while the only candidate (`Kb80S07Quality-world.patch`) measures **171 added / 5 deleted** — `instrument-size` fails at cap 60 and the plan's kill rule is live; and E10 created `.ufo/waves/round-79/snapshots/MANIFEST.sha256` in its stack world, so F3's file must be added at the tip.

15. **F15** S230 anchor erratum: `corpus/SOURCES.md:171` attributes pi-mono `main` to `7bb48f21…`, but `S230.fetch.json` records head `bb65e3e4…` / path commit `25cc5c7b…` and `7bb48f21…` is S231/mistral-vibe's commit — the row cites the wrong repository's commit. Cell not editable this round (M45): correction belongs in the lesson `## Gate` erratum and report § Sources & frontier.
16. **F16** C2 reachability: S229 names the field exactly once (raw 818), but the counter's heading heuristic treats a `#` Python comment in a code sample (text-view 168) as the first heading, so no admissible quote exists → `documented 6 of 6` is unreachable under the frozen conjuncts unless the location rule is fixed. E07/V02C2/L1 own it; seat readings differ by one text-view line (E08 95/168, S01 96/169) with the same conclusion; a declared counter erratum for heading detection is the only non-narrowing fix.

Checked clean: base cap figure matches (`instruments added 22`; 22+17+≤21 = 60) but the 21-line grammar budget is exceeded by the only published candidate (171) — the kill rule, not the base, is the constraint; `run-battery.sh` implements own-exit capture literally and writes the `# rev=… cmd=… utc=…` header; the S04 skeleton already names one receipt per battery value under `{{TIP_OUT}}/NN-*.txt` (the runner's own names); base six gate *exits* are inside `tipbattery-base-dot.txt` while the base *detail* belongs to the R02/E11 receipts.

## Gates / checks run by this seat

No claim counter, gate or battery was run — by design (this seat indexes receipts; it does not score them). The only executable check is the presence gate above (exit 1, own-exit line recorded). All counts quoted in the index carry their command.

## Touched surfaces

- Written: `.ufo/waves/round-80/build/Kb80S17ReceiptIndex.md`, `.ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py`, `.ufo/waves/round-80/build/Kb80S17ReceiptIndex-status.txt`, this report at `.ufo/waves/round-80/w1/Kb80S17ReceiptIndex.md`.
- Read-only: `plans/round-80.md`, `w1-spec.json`, the r79 drafts/snapshots/receipts, committed round-80 receipts and sibling build outputs. No product file, verifier, plan, SKILL.md, PROVINCE.md or lane git index was modified; no commit/push/checkout in the lane; no fleet-root or sibling-lane write.

## Out of scope (named, not silently dropped)

- Claim after-values (C1 6/6, C2 6/6) — L1/closure work.
- The receipt *contents* of pending seats — presence only; when a seat lands, the checker flips its row and the L1 re-runs it once at integration.
- Correcting the plan or seat prompts (frozen): findings F2–F7 are addressed by the L1 either producing the named receipt or correcting the citation at filing.
- Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80S17ReceiptIndex/` was created for prompt extraction and removed before yielding (`ls` → ENOENT).

## Limits

- The status snapshot is mid-wave: 11 blocking fixed paths and 16 subjects were absent at 23:34:38Z; absence is expected and is not a defect of any producer.
- Presence is not correctness: a file existing does not validate its bytes; the pin/contents audits belong to E16/V03 and the counters.
- The proposed subject names (TIP/EXT) are canonical proposals; the tip set's receipt names come from the committed runner, the out-dir is the L1's choice.
- Tool installs: none. pacman untouched. No network fetches were made by this seat.

VERDICT: Receipt index complete and re-runnable — 60 fixed-path receipts / 51 blocking / 16 subjects mapped to claim, section and marker; 16 receipt/lane-integrity findings, of which F1–F4, F9, F12, F15 and F16 block the report (missing base-abs receipt, census receipt without its own exit/count, missing MANIFEST.sha256, wrong re-open path, freeze ordering); presence gate at 23:34:38Z: 11 blocking fixed paths + 16 subjects still pending mid-wave.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S17ReceiptIndex.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S17ReceiptIndex-status.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S17ReceiptIndex.md
