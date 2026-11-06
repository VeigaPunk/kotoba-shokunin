#!/usr/bin/env python3
"""Generate the round-99 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "52e8e95ac4faf4ded84d7b82cbc204792590d0f7"
INSTR = "c0489d14156a7687d10ae5389d72eaa923b2bc29"
W1 = f"{LANE}/.ufo/waves/round-99/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r99"
CTR = f"{LANE}/verifiers/fixtures/round-99/selftest-kills.py"
CTC = f"{LANE}/verifiers/fixtures/round-99/carried-reds.py"
RCP = f"{LANE}/.ufo/waves/round-99/receipts"
P98 = f"{LANE}/.ufo/waves/round-98/w1"
# §3: every L2 prompt leads with /skill:godspeed followed by the host binding's verbatim directive bytes.
GOD = """/skill:godspeed

You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim — let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.

"""

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only), .ufo/state/, .ufo/watchdog.log, MANIFEST.json, scripts/, templates/,
or /home/vgpnk/Projects/shokuknow (read-only).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR and HYAKU_SCRATCH to it, pass it to any
--work argument, and delete it before you yield (`trap 'rm -rf -- "$S"' EXIT`). Copy the receipts you need under
{W1}/<your-seat-name>/ first. /tmp only for files under 50 MB. Never hardcode /tmp in any file you write for the lane.
Evidence size: never save a full fetched HTML page or a clone under {W1}; store the digest (HTTP code, bytes, sha256) and a short
line excerpt instead.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch, pull, push,
branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh. Read-only git (log, show, diff,
status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
Your ONE writable repo is a scratch clone, created exactly as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D" && git -C "$D" checkout -q {BASE}`;
every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Scratch-clone commits (identity `scratch <scratch@invalid>`, inside $D only) are allowed so a gate can name a revision.
Counters (frozen at the instrument commit; header = specification):
C1 `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTR} c1 <rev> "$D"` measures a candidate commit of your scratch clone without touching the
lane (a few minutes; also `r98c1`, `r97c1`, `r96c1`, `r95c1`, the positive-control tables; `--rules v5` reproduces the round-97 rules).
C2 `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTC} <rev> "$D"` (about 5 minutes: it builds a fleet-shaped sandbox of the commit, runs
the three carried gates, their self-tests, four frozen-byte conjuncts and the full tip battery incl. the ~200 s floors gate).
At most two counter runs at a time per seat.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR99 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR99 (lane L1)" heading — your files and headings carry YOUR seat name only.
Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you and every seat may install or upgrade tools that help the task. Read /home/vgpnk/.omp/agent/RULES.md first
(official channels, update-safety gate). Record each install as tool, version, channel, reason in your final answer.
PACMAN IS PAUSED host-wide: no pacman transaction of any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official
binary in ~/.local/bin, or report the need. When the pause lifts the dry-run rule applies (`pacman -Sp --print-format '%n %v'`, only
packages not yet installed; never -Sy/-Syu/-U/-R, downgrade, or a host-service restart).
REPORT FILE FIRST: write your report file {W1}/<your-seat-name>.md (or the path your item names) BEFORE your final answer, and
update it as you go so a cut-off seat still leaves evidence. Final answer: a short JSON with files_written, evidence (commands and the
observed lines), findings, risks.



## Frozen state (round 99, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Instrument commit (counters): {INSTR}. Freeze commit (plan + pre-data receipts): {BASE}.
Read {LANE}/plans/round-99.md FULLY first, then the headers of {CTR} and {CTC}. TWO claims:
C1 (depth): the dispatch-prompt checker's self-test (verifiers/verify_dispatch_prompts.py --self-test) kills the twelve frozen survivors
t01..t12 (CLAIMS["c1"] in {CTR}; MutTesterDispatchR98 n01-n05, n07-n11, n13, n14) — target
`C1 targets killed 12 of 12 ... C1-PREDICATE-MET`.
C2 (consistency/calibration): the three tip-battery gates red since round 81/88 (verify_skill_checklist, verify_corpus_integrity,
verify_corpus_independent) read green at the landing without weakening a gate — `carried-reds.py <rev>` →
`C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok`, C2-PREDICATE-MET. The C2 counter allows ONLY: corpus
content/index fixes, an equal-mode baseline re-record, appended GOVERNANCE_CORRECTIONS rows + the horizon line in verify_skill_checklist.py
(data only — no other byte of that file may change), one appended LOG.md correction notice, and INSTRUMENT_PINS admissions in
check_tip_battery.py. verify_corpus_integrity.py / verify_corpus_independent.py stay byte-identical.
Nobody edits the plan, the counters, or any frozen predicate: an amendment is an L1 act via plans/round-99-addendum-*.md BEFORE any scored
reading; a counter defect you find is a FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {RCP}/ (redbefore-c1-base.txt UNMET 0 of 12; redbefore-c1-base-rulesv5.txt; poscontrol-r98c1/r97c1-base.txt MET;
c2-base.txt UNMET 0 of 3; c2-ctl-w1..w5 forgery controls UNMET, patches in {RCP}/ctl-worlds/; sources-opened.txt S281 candidate).
Round-98 evidence you will need: {P98}/MutTesterDispatchR98.md (+ MutTesterDispatchR98/probe_r98.py, witness_r98.py) and
{P98}/ScoutTipReds.md (+ ScoutTipReds/ receipts: governance-failures-base.txt, controls.txt, fix-measured.txt).
FROZEN ANCHORS (C1): the counter's mutants substitute literal anchor text in verifiers/verify_dispatch_prompts.py; each anchor of CLAIMS["c1"],
CLAIMS["r98c1"], CLAIMS["r97c1"] and CLAIMS["r96c1"] in {CTR} must stay byte-identical and match exactly once. Never add another occurrence of
an anchor text anywhere in the file (new self-test code included).
ANTI-SNIFFING (C1): a self-test arm must observe BEHAVIOUR (call lane_of, report_paths, state_source, evaluate_dispatch_04/08, _verdict_of,
dispatch_box_sha256, box_proof, _finish, run_checks, main or read_text on fixture inputs and read the result). The counter runs every mutant
source-blind AND mirrored, git-less, minimal env, shuffled, bracketed by honest runs, with comment and code decoys; reviewers refuse source
readers. A kill must be a REPORTED failure in BOTH runs (`self-test FAIL: ` line and `<N> failure(s) over <M> assertions`, N >= 1, exit 1): an
arm that crashes on a mutant is a RUN-ERROR and does not count — every new assertion goes through the self-test's `rec(...)` tally and guards
exceptions. Arms must not need git, network, or any environment variable beyond TMPDIR/HOME; main() arms pass argv explicitly and capture
stdout in-process (no subprocess needed); the unreadable-file arm (t09) runs as uid 1000 on this host; guard it anyway: if os.access says the chmod-000 file is
still readable (root), the arm prints a skip note instead of a false failure.
PATCH BASE: every patch is `git diff --binary {BASE}` from YOUR scratch clone.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md; no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/ (all rounds),
verifiers/floors-registry.json.

## File ownership (one writer per file; each builder writes only its own patch)
ExecArmsR99 owns verifiers/verify_dispatch_prompts.py (the self_test() function and self-test-only helpers/constants next to it ONLY).
ExecRedsR99 owns corpus/README.md (coverage-map rows only, INCLUDING one row for corpus/lessons/round-99.md, which ScribeCorpusR99 writes),
corpus/lessons/round-81.md (line 8's hash quoting only), verifiers/corpus-baseline.json, verifiers/verify_skill_checklist.py (the
GOVERNANCE_CORRECTIONS block and GOVERNANCE_CORRECTIONS_HORIZON line ONLY), verifiers/check_tip_battery.py (INSTRUMENT_PINS block ONLY), and
ONE correction notice appended at the END of LOG.md (the first append after the base; the L1 appends its round entry after it).
ScribeCorpusR99 owns corpus/SOURCES.md (APPEND row S281 only) and corpus/lessons/round-99.md (new).
Every other seat writes NOTHING in any repo except its own receipts under {W1}/<its-seat-name>/ and its report file.
Build seats write their patch under {W1}/<seat>/<seat>.patch and then the READY file {W1}/<seat>_READY.

## Patch and handoff protocol (builders)
Each builder: edit only in its scratch clone $D; `git -C "$D" add -A -- <owned files>`; `git -C "$D" diff --cached --binary {BASE} > {W1}/<seat>/<seat>.patch`;
prove the patch applies on a second fresh scratch clone at {BASE} (`git apply --check`), then remove that clone. Only after the patch
and its receipts exist, write the READY file (content: the patch sha256 and one line saying what it does). A builder that cannot land
its claim writes an EMPTY patch and a READY file naming the honest-stop reason.

## Attack and sentinel handoff (candidate build)
The candidate is {BASE} plus the builder patches named in your item, applied in the order ExecRedsR99, ScribeCorpusR99, ExecArmsR99. Build it
in your own scratch clone (`git apply` each patch, then `git -C "$D" commit` with the scratch identity) so a gate can name the candidate
revision; pass "$D" as the counter's REPO. Note: the corpus baseline's equal counts depend on every corpus file of the tree, so on a candidate
that adds ScribeCorpusR99's lesson/S281 row after ExecRedsR99's baseline, verify_corpus_integrity may drift by those files — the L1 re-records
the baseline at integration; report the observed drift, do not treat it as a C2 failure of the ExecRedsR99-only candidate.

## Poll and wait rules
Poll every 120 s with `sleep 120`, up to 75 minutes, for the READY files named in your item; if one never appears, report on what
exists and say so. Never write a READY file that another seat owns.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR; exit ladder 0 pass, 1 content fail, 2 could-not-evaluate. No network inside a counter or
self-test.
"""


def item(role, name, body):
    return {"role": role, "name": name, "prompt": GOD + body}


items = [
item("executor", "ExecArmsR99", f"""## ExecArmsR99 — C1 build: the dispatch-prompt self-test kills t01..t12

Read {LANE}/plans/round-99.md § C1, the counter header and CLAIMS["c1"] in {CTR}, the mutant table, § Differential witnesses and F2-F5 in
{P98}/MutTesterDispatchR98.md (witness driver {P98}/MutTesterDispatchR98/witness_r98.py gives a working input for every target), and
{LANE}/verifiers/verify_dispatch_prompts.py (lane_of, L1_FILE_RE, evaluate_dispatch_04/08, _verdict_of, box_proof, _finish, run_checks, main,
read_text, self_test()). Source S281 (argparse `action='append'`, {RCP}/sources-opened.txt) grounds the t08 arm: cite it in that arm's comment.
In YOUR scratch clone at {BASE}, change ONLY self_test() and self-test-only helpers/fixture text next to it. Add behavioural arms, each a
`rec(...)` named `r99-tNN-...`, that REPORT a failure (never crash) on:
t01 `kote-L1.md.bak` in the prompts dir is out of scope (dispatch.04 evaluates 0 files); t02 a `kote-round-7.md` whose role line says round 8
→ dispatch.08 FAIL; t03 box_proof with the map's dispatch.04 text_sha256 = 64 zeros → rc 1, not `boxes proven 2`; t04 box_proof with SKILL.md
deleted → rc 1; t05 box_proof with a PASS-labelled duplicate of a must-fail case → rc 1; t06 run_checks(..., ["dispatch.04","dispatch.08"])
returns both checks; t07 main() on a prompt with a wrong report stem → exit 1; t08 main(["--check","dispatch.04", ...]) where 04 passes and 08
would fail → exit 0 and one result line; t09 a mode-000 prompt file → EnvError (substrate error), not an empty-text N/A; t10 box_proof whose
control case `file` is a prefix (`kote-round-7`) of the evaluated name → rc 1 (`not evaluated`); t11 two dispatch.04 map entries, bad first and
good second → last wins, `boxes proven 2` rc 0; t12 one FAILing round file beside one N/A round file → dispatch.08 status FAIL.
Arms must work in a git-less copy with only TMPDIR/HOME set. Keep FROZEN ANCHORS byte-identical and unique. Verify in your clone, receipts under
{W1}/ExecArmsR99/: `--self-test` → 0 failure(s); `--box-proof` → boxes proven 2 rc 0; commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecArmsR99 python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET (12 KILLED, decoys 12/12 held), the same
with `--rules v5`, and r98c1, r97c1 → MET. Patch {W1}/ExecArmsR99/ExecArmsR99.patch; report {W1}/ExecArmsR99.md; then {W1}/ExecArmsR99_READY."""),

item("executor", "ExecRedsR99", f"""## ExecRedsR99 — C2 build: the three carried tip-battery reds green, data-only

Read {LANE}/plans/round-99.md § C2, the header of {CTC}, {P98}/ScoutTipReds.md (§ 2 causes, § 3 minimal fix, § 4 F1-F9) and its receipts
{P98}/ScoutTipReds/ (governance-failures-base.txt lists every bad subject; fix-measured.txt / controls.txt). Re-measure at {BASE} first (the
round-98 landing added files since the scout ran: e.g. round-98-verifier-spotcheck.md is now unindexed too): run the three gates in a
fleet-shaped sandbox (the counter does this; or read its `red` lines on {BASE}: {RCP}/c2-base.txt).
In YOUR scratch clone at {BASE}, within your file ownership ONLY:
(1) corpus/README.md: one coverage-map row per unindexed corpus file, shaped like the existing round-80..90 spot-check rows, PLUS one row for
corpus/lessons/round-99.md (written by ScribeCorpusR99; the row may precede the file in your candidate — say so).
(2) corpus/lessons/round-81.md line 8: write the absent test-world hash in the quoted form both corpus gates classify as context (meaning
unchanged; quote the before/after line in your report).
(3) LOG.md: append ONE correction notice at the end (stale tokens double-quoted so the notice adds no live subject; corrected tokens resolve),
naming every stale subject → corrected token pair. Fleet-root files are corrected to the lane's `../` form (e.g. `../.ufo/reports/round-82/kotoba.md`)
ONLY if that file exists at the fleet root; a token that never existed is corrected to the file that does exist (the round-83 notice names it).
(4) verifiers/verify_skill_checklist.py: append GOVERNANCE_CORRECTIONS rows (log line, line sha256, subject file, subject line, stale token,
corrected token) for every live dead subject, re-pin the existing row 2621 (SCORECARD.md 158 → its current line), raise
GOVERNANCE_CORRECTIONS_HORIZON to cover the notice; the `:30,37` comma-anchor token is handled as a correction row (data), NOT by changing
strip_token_dressing — the counter's frozen conjunct refuses any other byte change in that file.
(5) verifiers/check_tip_battery.py: admit the new checklist blob in INSTRUMENT_PINS (nothing else).
(6) verifiers/corpus-baseline.json: re-record ONLY the equal-mode expectations from `verify_corpus_integrity.py --no-baseline --json` taken
AFTER (1)-(2) (ScoutTipReds F9), with an updated note naming round 99.
Never touch verify_corpus_integrity.py / verify_corpus_independent.py. Measure: commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecRedsR99 python3 -B {CTC} <your commit> "$D"` → C2-PREDICATE-MET; also each gate's own output and
`verify_skill_checklist.py --self-test`. Receipts under {W1}/ExecRedsR99/. Patch {W1}/ExecRedsR99/ExecRedsR99.patch; report {W1}/ExecRedsR99.md
(include the correction table: subject, stale, corrected, why the corrected token is the truth — not an excuse); then {W1}/ExecRedsR99_READY."""),

item("scribe", "ScribeCorpusR99", f"""## ScribeCorpusR99 — SOURCES row S281 and the round-99 lesson scaffold

Read {LANE}/plans/round-99.md, {RCP}/sources-opened.txt, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract), the last rows of
{LANE}/corpus/SOURCES.md (S277-S280 show the 11-column shape), {LANE}/corpus/lessons/round-98.md (structure) and
{LANE}/corpus/lessons/round-98-verifier-spotcheck.md (routed defects 2-5). Poll for {W1}/ScoutSourcesR99.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append row S281 (Python argparse docs, `action='append'` — grounds the C1 t08 arm), tier per CORPUS.md,
`mined`, used-by `corpus/lessons/round-99.md,plans/round-99.md`, opened 2026-11-06, recheck a valid cadence, no `|` inside cells; if
ScoutSourcesR99 proposes a further row that the round actually cites, add it only if the scout located the quote; (2) write
corpus/lessons/round-99.md as a SCAFFOLD (author ScribeCorpusR99): `## Gate` (S281: URL, access date, HTTP, bytes, sha256, HTML line excerpt,
≤25-word located quote with `wc -w` count), `## Corrections` (C99-1: the round-98 report's "+183 lines inside self_test()" is 182 lines
(`@@ -1333,0 +1334,182 @@`), 183 was the two-file total; C99-2: the SCORECARD round-98 C1 annotation names the freeze `63cd48d9` for the
red-before, the receipt measured the instrument commit `a060b450` (equal bytes, value stands); C99-3: S279's `teaches` omits step (4)'s second
conjunct — denial needs the caller to lack CAP_SYS_PTRACE (use ScoutSourcesR99's located line)), `## Mistakes` (one row: class
`governance-cell-cites-fleet-path-repo-rooted` · evidence {P98}/ScoutTipReds.md § 2.1 row 4 and § 4 F6 · captured-by: governance.citation_resolves
fired, but the landing no-harm rule since round 92 accepted an unchanged red set · fix: claim C2 plus a QUALITY criterion (L1 adds Q89) ·
shown able to fail: {RCP}/c2-base.txt `carried reds green 0 of 3`), `## Status changes` (old→new for every registry cell changed; none
expected), `## Considerthese` (re-read {LANE}/considerthese/ newest file; name which proposal is still unimplemented and whether it is taken this
round — it is not, unless trivially citable), `## Settlement` (placeholder for the L1). Run
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 and W04 not above 34 (receipt under
{W1}/ScribeCorpusR99/). Patch {W1}/ScribeCorpusR99/ScribeCorpusR99.patch; report {W1}/ScribeCorpusR99.md; then {W1}/ScribeCorpusR99_READY."""),

item("scout", "ScoutSourcesR99", f"""## ScoutSourcesR99 — re-open S281 and the S279 conjunct

(1) Re-open https://docs.python.org/3/library/argparse.html yourself (curl into your scratch dir; HTTP, size, sha256 — equal to the L1's in
{RCP}/sources-opened.txt?); locate the `'append'` quote and its HTML lines; judge whether it grounds the t08 arm (verify_dispatch_prompts.py:527
`--check ... action="append"`) against {LANE}/corpus/QUALITY.md and /home/vgpnk/Projects/shokunin/CORPUS.md tiers; check the registry for an
existing row on the URL (`grep -n argparse {LANE}/corpus/SOURCES.md`). (2) Re-open https://man7.org/linux/man-pages/man2/ptrace.2.html and locate
access-check step (4) in full, including the CAP_SYS_PTRACE conjunct (round-98 closure routed defect 5): give the HTML lines and a ≤25-word quote
for the conjunct. (3) Open ONE candidate that would ground C2's honest route (e.g. a documented convention for append-only correction notices,
or git's own docs on what `git hash-object` names, which the INSTRUMENT_PINS admission relies on) and judge it admit/reject with reason and flip
condition. Write {W1}/ScoutSourcesR99.md: per URL, access date, HTTP, bytes, sha256, located quote with HTML line and `wc -w` count, verdict.
Do NOT save HTML under {W1}. Early, updated; no repo writes."""),

item("connector", "ConnectorOverlapR99", f"""## ConnectorOverlapR99 — overlap scan and planning data-walk (read-only)

Part 1 (cross-claim): does C1's change to verify_dispatch_prompts.py self_test() change any C2 gate's reading (the checklist delegates
dispatch boxes to `verify_dispatch_prompts.py --box-proof`; check_assertion_floors / floors-registry pin its assertion count; check_gate_registry)?
Does C2's change (corpus README rows, baseline, checklist corrections, battery pins, a LOG.md notice) change any C1 reading? Name exact lines.
Part 2 (siblings, read-only): grep the sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin for landing no-harm rules that accept an
unchanged red set of their own gates (the ScoutTipReds F6 class), and for governance files citing fleet paths repo-rooted; name file:line — a
cross-lane finding for the report, not a write. Part 3: round 100 is the lane's last round: list three candidate claims the evidence supports
(the v7 counter for g11/g16; the dispatch_prompts floor raise; the strip_token_dressing comma-anchor gate fix), each with a falsifiable
before→after and a do-nothing control. Write {W1}/ConnectorOverlapR99.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerArmsR99", f"""## ReviewerArmsR99 — review the C1 patch

Wait for {W1}/ExecArmsR99_READY. Review {W1}/ExecArmsR99/ExecArmsR99.patch against plans/round-99.md § C1 and the context's ANTI-SNIFFING and
FROZEN ANCHORS rules: does each new arm observe behaviour, never the checker's source? Does it kill t01..t12 for the stated reason (apply each
mutant by hand in your candidate clone and name WHICH assertion fails, with its `self-test FAIL:` line and the failure count)? Is production
code byte-identical outside self_test() and its self-test helpers (`git diff` hunks)? Do fixtures stay under TMPDIR and get cleaned (incl. the
chmod-000 file)? Does the t07/t08 main() arm leak stdout or argv state between arms? Run the counter c1, c1 `--rules v5`, r98c1, r97c1 and
`--box-proof` on the candidate. Blocking findings first. Write {W1}/ReviewerArmsR99.md (early, updated)."""),

item("reviewer", "ReviewerRedsR99", f"""## ReviewerRedsR99 — review the C2 patch for laundering

Wait for {W1}/ExecRedsR99_READY. Review {W1}/ExecRedsR99/ExecRedsR99.patch against plans/round-99.md § C2 and the header of {CTC}. For EVERY
appended GOVERNANCE_CORRECTIONS row and LOG.md notice line: is the subject genuinely stale (dead at {BASE}), is the corrected token the truth
(open the file it names; does the original context mean that file?), or is it an excuse that silences a real defect (the round-70 notice
was withdrawn as laundering — {LANE}/corpus/lessons/ M118 / QUALITY Q64; grep them)? Are the coverage-map rows real index entries? Is the
round-81.md quoting change meaning-preserving? Is the baseline re-record equal-mode only and taken after the content fix? Does the checklist
change stay data-only (diff it) and the battery change pins-only? Run the counter on the candidate ({BASE} + ExecRedsR99.patch) and each gate
directly. Blocking findings first. Write {W1}/ReviewerRedsR99.md (early, updated)."""),

item("mutation-tester", "MutTesterRedsR99", f"""## MutTesterRedsR99 — attack the C2 counter (scratch only)

Read {CTC} and the five committed forgery controls ({RCP}/ctl-worlds/*.patch, receipts {RCP}/c2-ctl-*.txt). (a) Build at least SIX NEW forgery
worlds on {BASE} in your scratch clone that try to read C2-PREDICATE-MET without fixing the content, aimed at the counter's conjuncts: e.g. a
correction row whose corrected token resolves but excuses an unrelated dead subject; a corrections block holding a non-literal expression; a
horizon raised past rows that do not exist; INSTRUMENT_PINS entries computed by code; a checklist that prints 11 PASS lines from a forged
path but still passes its self-test; a baseline-and-README combination that hides unindexed files by pattern; a LOG.md notice that rewrites an
earlier line. Run `HYAKU_SCRATCH={SCRATCH}/MutTesterRedsR99 python3 -B {CTC} <commit> "$D"` on each; report tally lines and which conjunct
caught it. (b) Copy the counter into scratch and apply at least SIX counter mutants (drop each conjunct in turn; weaken CHECKLIST_PASS_MIN;
accept N/A lines; skip literal_eval) and report which control world (w1-w5 + yours) exposes each. A world that reads MET is a counter finding
(class, severity, minimal fix) — never edit the counter. Report {W1}/MutTesterRedsR99.md (early, updated), receipts {W1}/MutTesterRedsR99/."""),

item("mutation-tester", "MutTesterDispatchR99", f"""## MutTesterDispatchR99 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecArmsR99_READY. On the candidate ({BASE} + that patch) design at least 10 NEW mutants of verifiers/verify_dispatch_prompts.py
that are NOT in CLAIMS["c1"], ["r98c1"], ["r97c1"], ["r96c1"] of {CTR} nor n01-n20 of {P98}/MutTesterDispatchR98.md (ideas: main()'s argument
handling and exit-2 ladder, run_checks' result order, read_text's decode path, box_proof's case/file bookkeeping, the L1/round regex groups).
Apply each with the counter's method (reuse probe_r98.py's approach: import RUNNER/classify/code_decoy from a scratch copy of {CTR}) and classify
KILLED / RUN-ERROR / SURVIVED at {BASE} and on the candidate, with a differential witness per verdict-bearing survivor and the equivalent /
no-verdict ones named. Write {W1}/MutTesterDispatchR99.md (early, updated), receipts {W1}/MutTesterDispatchR99/."""),

item("critic", "CriticClaimR99", f"""## CriticClaimR99 — falsify the two frozen claims against the full candidate

Wait for {W1}/ExecArmsR99_READY, {W1}/ExecRedsR99_READY and {W1}/ScribeCorpusR99_READY. Build the full candidate (order ExecRedsR99,
ScribeCorpusR99, ExecArmsR99). Run C1 (c1, `--rules v5`, r98c1) and C2 on it, and on each single-patch candidate (separability). Re-run the
do-nothing controls (c1 and C2 at {ROUND_BASE}) and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper change meet
either target? Is C2 a real consistency move or relabelled bookkeeping (§9: name the axis by the surface)? Are the twelve C1 targets real false
greens of the dispatch boxes or contrived; is excluding n12/n18/n19/n20 honest? Does S281 ground the t08 arm (open the page)? Does the mined
mistake's fix fail on its committed control? Is the round-98 closure's routed-defect list honestly dispositioned in the plan (defect 1 carried —
is that a narrowing)? Write {W1}/CriticClaimR99.md (early, updated) with MET/UNMET verdicts on the candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR99", f"""## SentinelScopeR99 — scope, safety and no-harm on the candidate

Wait for the three READY files (as CriticClaimR99). On the full candidate: (1) scope — `git diff --stat {BASE}` lists only owned files;
SKILL.md byte-identical; no spotcheck file or fixture touched; verify_dispatch_prompts.py production code outside self_test() byte-identical;
verify_corpus_integrity.py / verify_corpus_independent.py byte-identical; (2) no-harm — `python3 -B verifiers/check_gate_registry.py --rev <cand>`,
the round-98 counter `verifiers/fixtures/round-98/selftest-kills.py c1|r97c1 <cand> "$D"` (MET), `check_assertion_floors.py --self-test`,
`verify_dispatch_prompts.py --box-proof` (boxes proven 2) and its live run over /home/vgpnk/Projects/shokunin/.ufo/prompts (same verdict lines at
{BASE} and the candidate), census `--file` on the candidate SOURCES.md (rc 0, W04 not above 34), the full tip battery
`python3 -B verifiers/check_tip_battery.py --repo "$D" --rev <cand> --fleet /home/vgpnk/Projects/shokunin`; (3) safety — no hardcoded /tmp in new
code, no network in self-tests, fixtures only under TMPDIR, the chmod-000 fixture restored/removed, no credential-shaped strings. Each check:
command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR99.md (early, updated)."""),
]

spec = {
    "wave": "r99-w1",
    "milestone": "r99-w1: C1 dispatch-prompt self-test kills t01..t12 (v6.1 counter); C2 carried tip-battery reds green 3 of 3, data-only; S281; 5 attack seats",
    "reportDir": ".ufo/waves/round-99/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-99/r99-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
