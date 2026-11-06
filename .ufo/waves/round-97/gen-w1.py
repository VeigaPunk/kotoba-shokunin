#!/usr/bin/env python3
"""Generate the round-97 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520"
INSTR = "94a1021762a888d8a360ba6efa759372cef392fb"
W1 = f"{LANE}/.ufo/waves/round-97/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r97"
CTR = f"{LANE}/verifiers/fixtures/round-97/selftest-kills.py"
CTL = f"{LANE}/verifiers/fixtures/round-97/forgery-controls.py"
RCP = f"{LANE}/.ufo/waves/round-97/receipts"
GPATCH = f"{LANE}/.ufo/waves/round-96/w1/ExecCounterForgeryR96"
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
Evidence size (round-96 routed defect 6): never save a full fetched HTML page or a clone under {W1}; store the digest
(HTTP code, bytes, sha256) and a short line excerpt instead.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch, pull, push,
branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh. Read-only git (log, show, diff,
status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
Your ONE writable repo is a scratch clone, created exactly as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D" && git -C "$D" checkout -q {BASE}`;
every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Scratch-clone commits (identity `scratch <scratch@invalid>`, inside $D only) are allowed so a gate can name a revision.
The frozen v5 counter accepts REV and REPO: `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTR} c1 <rev> "$D"` measures a candidate
commit of your scratch clone without touching the lane (~60 s; also `r96c1` ~60 s and `r95c1`, the positive-control tables;
`--rules v4` reproduces the round-96 rules). The C2 runner: `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTL} v5 {BASE}` (~3 min;
modes v4, v5, v5-as-v4). One counter run at a time per seat.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR97 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR97 (lane L1)" heading — your files and headings carry YOUR seat name only.
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


## Frozen state (round 97, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Instrument commit (v5 counter + C2 runner): {INSTR}. Freeze commit (plan +
pre-data receipts): {BASE}.
Read {LANE}/plans/round-97.md FULLY first, then the headers of {CTR} and {CTL}. TWO claims:
C1 (depth): the dispatch-prompt checker's self-test (verifiers/verify_dispatch_prompts.py --self-test) kills the thirteen frozen survivors
t01..t13 (CLAIMS["c1"] in the v5 counter) — target `C1 targets killed 13 of 13 ... C1-PREDICATE-MET`.
C2 (consistency/calibration): the v5 counter refuses the committed round-96 forgery worlds g3/g7/g8 that the v4 counter reads MET with
no behavioural arm — `forgery-controls.py v5 <rev>` → `forgeries refused 3 of 3; honest held 2 of 2`.
Nobody edits the plan, the counter, the runner, the round-96 patches or any frozen predicate: an amendment is an L1 act via
plans/round-97-addendum-*.md BEFORE any scored reading; a counter defect you find is a FINDING in your answer — never rescue a counter by
changing its predicate.
Pre-data receipts: {RCP}/ (redbefore-c1-base.txt UNMET 0 of 13; redbefore-c1-base-rulesv4.txt; poscontrol-r96c1-base.txt MET;
poscontrol-r95c1-base.txt MET; c2-before-v4.txt refused 0 of 3; c2-v5-as-v4.txt refused 0 of 3; c2-v5.txt; sources-opened.txt S273 Bazel).
FROZEN ANCHORS: the counter's mutants substitute literal anchor text in verifiers/verify_dispatch_prompts.py; each must stay byte-identical
and match exactly once (see CLAIMS["c1"] AND CLAIMS["r96c1"]; e.g. `stem = m.group(2).rstrip(".,;:")`, `if note:`, `    if fails:` +
`        status = "FAIL"`, the PLACEHOLDER_RE / REPORT_PATH_RE / ROLE_ROUND_RE lines, `(state_dir / ("%s.round" % lane)).is_file()`,
`stem = stem[:-3]`). Never add another occurrence of an anchor text anywhere in the file (new self-test code included — in particular never
write a bare `if note:` or `if fails:` line in new code); mutated statements keep their line count.
ANTI-SNIFFING: a self-test arm must observe BEHAVIOUR (call evaluate_dispatch_04/08, report_paths, role_round, has_placeholder,
lane_kind, state_source or _finish on fixture inputs and read the result). The v5 counter runs every mutant source-blind AND mirrored
(mutant on disk), in a fresh clone/TMPDIR/HOME per run, in a shuffled order bracketed by three honest runs, with comment and code decoys;
reviewers refuse source readers. A kill must be a REPORTED failure in BOTH runs (a `self-test FAIL: ` line and
`<N> failure(s) over <M> assertions` with N >= 1, exit 1): an arm that crashes (uncaught exception) on a mutant is a RUN-ERROR and does not
count — every new assertion goes through the self-test's `rec(...)` tally.
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
The L1 lands SCORECARD/LOG/QUALITY at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-9*/
(round-97 included), verifiers/fixtures/dispatch-prompts/ (the committed box-proof corpus), verifiers/floors-registry.json.

## File ownership (one writer per production file; each builder writes only its own patch)
ExecArmsR97 owns verifiers/verify_dispatch_prompts.py (the self_test() function and self-test-only helpers/constants next to it ONLY;
everything from the module docstring through run_checks() and box_proof()/main() stays byte-identical).
ScribeCorpusR97 owns corpus/SOURCES.md (APPEND row S273 and, only if the scout admits one, S274), corpus/lessons/round-97.md (new),
corpus/README.md (one index row for the new lesson ONLY).
Every other seat writes NOTHING in any repo except its own receipts under {W1}/<its-seat-name>/ and its report file.
Build seats write their patch under {W1}/<seat>/<seat>.patch and then the READY file {W1}/<seat>_READY.

## Patch and handoff protocol (builders)
Each builder: edit only in its scratch clone $D; `git -C "$D" add -A -- <owned files>`; `git -C "$D" diff --cached --binary {BASE} > {W1}/<seat>/<seat>.patch`;
prove the patch applies on a second fresh scratch clone at {BASE} (`git apply --check`), then remove that clone. Only after the patch
and its receipts exist, write the READY file (content: the patch sha256 and one line saying what it does). A builder that cannot land
its claim writes an EMPTY patch and a READY file naming the honest-stop reason.

## Attack and sentinel handoff (candidate build)
The candidate is {BASE} plus the builder patches named in your item. Build it in your own scratch clone (`git apply` each patch,
then `git -C "$D" commit` with the scratch identity) so a gate can name the candidate revision; pass "$D" as the counter's REPO.
Attack seats never write a patch into the lane.

## Poll and wait rules
Poll every 120 s with `sleep 120`, up to 75 minutes, for the READY files named in your item; if one never appears, report on what
exists and say so. Never write a READY file that another seat owns.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR; exit ladder 0 pass, 1 content fail, 2 could-not-evaluate; `--self-test` prints
`0 failure(s) over N assertions`. Every new self-test assertion names the arm it guards. No network inside a counter or self-test.
"""


def item(role, name, body):
    return {"role": role, "name": name, "prompt": GOD + body}


items = [
item("executor", "ExecArmsR97", f"""## ExecArmsR97 — C1 build: the dispatch-prompt self-test kills t01..t13

Read {LANE}/plans/round-97.md § C1, the v5 counter header and CLAIMS["c1"] in {CTR}, the differential witnesses in
{LANE}/.ufo/waves/round-96/w1/MutTesterDispatchR96.md (§ Differential witnesses; F2-F5 give minimal arms), and
{LANE}/verifiers/verify_dispatch_prompts.py (has_placeholder, report_paths, role_round, lane_kind, state_source, _file_result,
evaluate_dispatch_04, evaluate_dispatch_08, _finish, _write_case, _verdict_of, self_test()).
In YOUR scratch clone at {BASE}, change ONLY self_test() and self-test-only helpers/fixture text next to it; production behaviour stays
byte-identical (git diff hunks only inside the self-test section). Add behavioural arms, each a `rec(...)` naming the arm (`t01-...`), that FAIL on:
t01: `Write it at .ufo/reports/round-7/kote.md. Then stop.` → the extracted stem is `kote` (report_paths / dispatch.04 stem PASS for lane kote);
t02: an EMPTY `<lane>.report-baseline` → round_le_latest_dispatched N/A and the file verdict is not PASS;
t03: a fleet-root role lane (state file only, no `<lane>-shokunin` repository) whose report stem differs from the lane → report_stem_is_lane_id
is N/A (not PASS);
t04: a lane known ONLY by `<lane>.report-baseline` in the state dir → it is a known lane (lane_kind fleet-root-role, not unknown);
t05: a report path whose stem carries an empty `<>` → report_path_literal FAIL / has_placeholder True;
t06: a plain FILE named `<lane>-shokunin` in the fleet dir → NOT a sibling lane (lane_kind is not sibling-lane);
t07: `.ufo/reports/7/kote.md` (no `round-` prefix) → not extracted as a report path;
t08: a role line `... round7 of ...` (no space) → no role round read;
t09: a file with no report path carries its note (`no report path found`);
t10: a mode-000 (unreadable) baseline → N/A, never a bound (skip-and-record honestly if running as root makes it readable: then the arm must
still be a reported assertion, not a crash);
t11: a lane known ONLY by a legacy `<lane>.round` state file → known lane;
t12: a prompts dir with exactly one failing file (plus one passing file) → the CHECK status is `FAIL` (assert `== "FAIL"`);
t13: a prompt with no report path → dispatch.08 file verdict N/A, not PASS.
Keep FROZEN ANCHORS byte-identical and unique (your new code must not contain any anchor text verbatim). Verify, in your clone, with receipts
under {W1}/ExecArmsR97/: `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → 0 failure(s); `--box-proof` → boxes proven 2, rc 0;
commit in your clone and run `HYAKU_SCRATCH={SCRATCH}/ExecArmsR97 python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET (13 KILLED in
both blind and mirror runs, no RUN-ERROR, decoys 13/13 held), `... r96c1 <commit> "$D"` → MET and `... r95c1 <commit> "$D"` → MET.
Patch {W1}/ExecArmsR97/ExecArmsR97.patch; report {W1}/ExecArmsR97.md; then {W1}/ExecArmsR97_READY."""),

item("executor", "ExecForgeryV5", f"""## ExecForgeryV5 — attack the v5 counter with new forgery worlds (scratch only; C2 attack)

Read the header of {CTR} (rules 1-7 and the disclosed bounds), {CTL}, and {LANE}/.ufo/waves/round-96/w1/ExecCounterForgeryR96.md (g1-g8;
patches under {GPATCH}/). Build at least FOUR NEW forgery worlds of verifiers/verify_dispatch_prompts.py on the round-96 freeze
679775abb9277a7b8d17f060b0f5b4ced2b127b6 (the commit the g-patches apply to) in your scratch clone(s), each a self-test that tries to read
MET on the `r96c1` table WITHOUT behavioural arms, aimed at v5's new rules, e.g.: (g9) stateful fake with the marker OUTSIDE the per-run dirs
(/dev/shm or $XDG_RUNTIME_DIR or the clone's `.git/objects` alternate = the source repo) that fakes failure only on runs it can tell are
not honest — can it tell? (g10) mirror-aware: compares disk vs memory and fakes failure in BOTH blind and mirror runs while staying CLEAN on
honest runs — is there any signal separating an honest run from a mirror run? (g11) seed/schedule reader: reads the counter file from the
clone (verifiers/fixtures/round-97/selftest-kills.py is in the checkout) or its argv/env/parent cmdline to learn the run schedule; (g12) a
counter-of-runs keyed on wall-clock or pid ordering. Commit each in your scratch clone (scratch identity) and run
`HYAKU_SCRATCH={SCRATCH}/ExecForgeryV5 python3 -B {CTR} r96c1 <commit> "$D"`, plus `--rules v4` for comparison. Report per world: patch (save
under {W1}/ExecForgeryV5/<world>.patch), tally lines, MET/UNMET, which rule caught it. A world that reads MET under v5 is a counter finding
(severity, minimal fix) — never edit the counter. Clean up anything you write under /dev/shm or elsewhere outside your scratch dir.
Report {W1}/ExecForgeryV5.md (early, updated)."""),

item("scout", "ScoutSourcesR97", f"""## ScoutSourcesR97 — re-open C2's source and two candidates to judge

The L1 opened (receipt {RCP}/sources-opened.txt, 2026-11-06) https://bazel.build/reference/test-encyclopedia (HTTP 200, 223640 B, sha256
6b07e08f0f4bae537544eac1afc64d98f0b19a9ae7408b8e6482f56e134d5346; quote at HTML lines 659-661, heading line 656). Re-open it yourself
(curl into your scratch dir; record HTTP code, size, sha256 — say whether it equals the L1's; a dynamic page may differ: then locate the quote
in your bytes and give your line numbers). Then open TWO candidates that could ground C1 or C2 (e.g. pytest `tmp_path` docs on a
per-test unique temporary directory; Python pathlib `Path.is_dir`/`Path.exists` docs for t06; GoogleTest `--gtest_shuffle` docs for
shuffled order; Stryker "equivalent mutant" docs) and judge each against {LANE}/corpus/QUALITY.md and /home/vgpnk/Projects/shokunin/CORPUS.md
(§ SOURCES.md tiers): admit or reject with reason and flip condition; check the registry for an existing row on each URL (`grep -n` in
{LANE}/corpus/SOURCES.md). Write {W1}/ScoutSourcesR97.md: per URL, access date, HTTP, bytes, sha256, located quote ≤25 words with HTML line and
word count (`printf '%s\\n' "<quote>" | wc -w`), verdict + reason + flip condition. Do NOT save the HTML under {W1} (digest + excerpt only).
Early, updated; no repo writes."""),

item("scribe", "ScribeCorpusR97", f"""## ScribeCorpusR97 — SOURCES row S273 and the round-97 lesson scaffold

Read {LANE}/plans/round-97.md, {RCP}/sources-opened.txt, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract), the last
rows of {LANE}/corpus/SOURCES.md (S270-S272 show the lane's 11-column shape), {LANE}/corpus/lessons/round-96.md (structure) and
{LANE}/corpus/lessons/round-96-verifier-spotcheck.md. Poll for {W1}/ScoutSourcesR97.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append row S273 https://bazel.build/reference/test-encyclopedia (Bazel Test Encyclopedia; scope: the
isolation contract a test runner gives each test — a private, initially empty temporary directory and HOME — that a kill counter's runs
must also get; anchor § Test interaction with the filesystem with HTML lines), tier per CORPUS.md, kind docs/spec, status `mined`, opened
2026-11-06, recheck a valid cadence, used-by `corpus/lessons/round-97.md,plans/round-97.md`, no `|` inside cells; append S274 ONLY if the scout
admits a candidate that grounds a claim; (2) write corpus/lessons/round-97.md as a SCAFFOLD (author ScribeCorpusR97) with `## Gate` (S273
admitted: URL, access date, HTTP, bytes, sha256, ≤25-word located quote and word count; at least one same-round REJECT from the scout's
candidates with reason and flip condition), `## Corrections` (round-96 closure routed defect 1: the frozen receipt
.ufo/waves/round-96/receipts/sources-opened.txt line 12 gives the S272 quote as 19 words; it measures 22 — a named, append-only correction
entry pointing at that receipt), `## Mistakes` (one row: class `shared-state-between-scored-runs` · evidence plans/round-96-addendum-1.md A3 and
.ufo/waves/round-96/w1/ExecCounterForgeryR96.md F1 · captured-by: none · fix: v5 rules 4-6 with committed g7/g8 control worlds, shown able
to fail by {RCP}/c2-v5-as-v4.txt refused 0 of 3), `## Status changes` (old→new for every registry cell changed; none expected),
`## Considerthese` (re-read {LANE}/considerthese/2026-10-26.md; name which proposal is still unimplemented and why it is or is not taken
this round), and `## Settlement` (placeholder for the L1); (3) add ONE index row for the lesson to corpus/README.md, shaped like the round-96
row. Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 and no new W04 (receipt under
{W1}/ScribeCorpusR97/). Patch {W1}/ScribeCorpusR97/ScribeCorpusR97.patch; report {W1}/ScribeCorpusR97.md; then {W1}/ScribeCorpusR97_READY."""),

item("connector", "ConnectorOverlapR97", f"""## ConnectorOverlapR97 — overlap scan and planning data-walk (read-only)

Part 1: does any no-harm instrument pin a blob, sha, line or assertion count of verifiers/verify_dispatch_prompts.py or of
verifiers/fixtures/round-9*/ such that adding self-test arms or the round-97 fixtures changes its reading? Read verifiers/check_tip_battery.py,
verifiers/check_assertion_floors.py + verifiers/floors-registry.json, verifiers/check_gate_registry.py and SKILL.md § Gate registry, the
mutation-battery manifest (verifiers/fixtures/mutation-battery/manifest.tsv), verifiers/checklist-baseline.json; name exact lines. Part 2
(siblings): grep the sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin (read-only) for kill counters or mutation harnesses that share
run state across runs (one TMPDIR or clone for every run; honest run only first) — the g7/g8 class — and name file:line; that is a
cross-lane finding for the report, not a write. Part 3: list three candidate round-98 claims the round-97 evidence supports, each with a
falsifiable before→after and a do-nothing control. Write {W1}/ConnectorOverlapR97.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerArmsR97", f"""## ReviewerArmsR97 — review the C1 patch

Wait for {W1}/ExecArmsR97_READY. Review {W1}/ExecArmsR97/ExecArmsR97.patch against plans/round-97.md § C1 and the context's ANTI-SNIFFING and
FROZEN ANCHORS rules: does each new arm observe behaviour (a function call's result on a fixture input), never the checker's source? Does it
kill t01..t13 for the stated reason (apply each mutant by hand in your candidate clone and name WHICH assertion fails, with its
`self-test FAIL:` line and the failure count)? Is production code byte-identical outside self_test() and its self-test helpers (`git diff`
hunks)? Do the fixtures stay under TMPDIR and get cleaned (t10's chmod 000 file restored before cleanup)? Run the v5 counter c1, r96c1, r95c1,
c1 `--rules v4`, and `--box-proof` on the candidate. Blocking findings first. Write {W1}/ReviewerArmsR97.md (early, updated)."""),

item("reviewer", "ReviewerCounterV5", f"""## ReviewerCounterV5 — review the frozen v5 counter, the C2 runner and the pre-data receipts (read-only)

Review {CTR} and {CTL} at {BASE} against plans/round-97.md: `diff` the v5 counter against the v4 counter
{LANE}/verifiers/fixtures/round-96/selftest-kills.py — are rules 1-3 unchanged in meaning; are the r96c1 and r95c1 anchors byte-equal to
v4's c1 and r95c1; does `--rules v4` reproduce v4 exactly (shared clone and TMPDIR, honest once first, no mirror, same order)? Do rules 4-7 do
what the header says (fresh world per run actually removed; HOME/XDG_CACHE_HOME set; mirror runs write the mutant to disk; honest bracket of
three with the interior one at a random position; exit ladder: feed a non-UTF-8 instrument in a scratch repo and confirm exit 2)? Any
fail-open path (an exception escaping as exit 1, a KeyError on an empty table, a decoy run silently skipped)? Does the C2 runner measure the
counter bytes AT REV (git show), build worlds only in scratch with the forgery identity, and score held/refused as its header says? Re-run, in
your own scratch, redbefore-c1-base, poscontrol-r96c1-base and c2-v5 and compare with {RCP}/. Is each predicate sentence identical in the plan
and the instrument header? Blocking findings first. Write {W1}/ReviewerCounterV5.md (early, updated)."""),

item("mutation-tester", "MutTesterDispatchR97", f"""## MutTesterDispatchR97 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecArmsR97_READY. On the candidate ({BASE} + that patch) design at least 10 NEW mutants of verifiers/verify_dispatch_prompts.py's
evaluation path that are NOT t01..t13/p00 of the round-97 table nor t01..t11 of r96c1 (ideas: lane_of() name parsing, kind detection for L1
files, _verdict_of, the box-proof manifest hashing, out_of_scope bookkeeping, state_source's split/strip, report_paths de-duplication and
sorting, the `.md` strip on other suffixes). Apply each with the counter's method (literal substitution, source-blind; reuse the v5 counter's
RUNNER/classify by import from a scratch copy) and classify KILLED / RUN-ERROR / SURVIVED at the base AND on the candidate. Name equivalent
mutants with the reason and a differential witness for each non-equivalent survivor. Write {W1}/MutTesterDispatchR97.md (early, updated) and
receipts under {W1}/MutTesterDispatchR97/."""),

item("mutation-tester", "MutTesterCounterV5", f"""## MutTesterCounterV5 — mutate the v5 counter itself (scratch copy only; C2 attack)

Copy {CTR} and {CTL} into a scratch tree (the runner reads the counter with `git show REV:...`, so build a scratch clone of the lane at {BASE},
commit each counter mutant there with the scratch identity, and point a scratch copy of the runner at that clone — never edit the lane).
Counter mutants at least: V1 mirror run dropped (KILLED on blind only); V2 honest bracket reduced to the first run; V3 isolation dropped (one
shared world); V4 HOME/XDG not reset; V5 no shuffle; V6 honest-CLEAN conjunct uses any() instead of all(); V7 exit ladder: UnicodeDecodeError
not caught; V8 mirror on_disk = original (mirror run degenerates to blind); V9 decoys held on RUN-ERROR. For each, run the C2 runner (v5 mode)
and the c1/r96c1 base and positive controls. Report a matrix: which committed control (g3/g7/g8 world, honest h1/h2, redbefore receipt)
exposes each counter mutant (verdict flip or tally deviation). A counter mutant no control exposes is a gap — report it with the minimal new
control world that would. Write {W1}/MutTesterCounterV5.md (early, updated) and receipts under {W1}/MutTesterCounterV5/."""),

item("critic", "CriticClaimR97", f"""## CriticClaimR97 — falsify the two frozen claims against the full candidate

Wait for {W1}/ExecArmsR97_READY and {W1}/ScribeCorpusR97_READY. Build the full candidate ({BASE} + ExecArmsR97.patch + ScribeCorpusR97.patch).
Run the v5 counter c1 (and `--rules v4`), r96c1, r95c1 on it and the C2 runner v5 at {BASE}; re-run the do-nothing controls (c1 at {ROUND_BASE};
C2 v4 and v5-as-v4) and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper change meet either target? Is C2 really
work of this round or only a re-labelled instrument (§9: name the axis by the surface)? Are C1 and C2 causally separable as the plan claims?
Are the thirteen targets real false greens / false reds of the dispatch boxes (read SKILL.md § Dispatch-prompt fidelity checklist dispatch.04/.08)
or contrived? Does S273 actually ground C2's rule 4 (open the page)? Does the mined mistake's fix fail on its committed control? Is the round-96
closure's routed-defect list honestly dispositioned in the plan? Write {W1}/CriticClaimR97.md (early, updated) with MET/UNMET verdicts on the
candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR97", f"""## SentinelScopeR97 — scope, safety and no-harm on the candidate

Wait for {W1}/ExecArmsR97_READY and {W1}/ScribeCorpusR97_READY (as CriticClaimR97). On the full candidate: (1) scope — `git diff --stat {BASE}`
lists only owned files; SKILL.md byte-identical; no spotcheck file, dispatch-prompts fixture, round-9x fixture or other verifier touched;
production code of verify_dispatch_prompts.py outside self_test()/helpers byte-identical; (2) no-harm — gate registry
`python3 -B verifiers/check_gate_registry.py --rev <cand>` (base 74 of 74), round-96 `selftest-kills.py c1|r95c1 <cand> "$D"` (MET),
round-95 `selftest-kills.py c1|r94c1 <cand> "$D"` (MET), `check_assertion_floors.py --self-test`, `verify_dispatch_prompts.py --box-proof`
(boxes proven 2) and its live run over /home/vgpnk/Projects/shokunin/.ufo/prompts (same verdict lines at {BASE} and the candidate — production
unchanged), census `--file` on the candidate SOURCES.md (rc 0, W04 count unchanged at 34); (3) safety — no hardcoded /tmp in new code, no
network in self-tests, no credential-shaped strings, fixtures only under TMPDIR, the chmod-000 fixture restored; the v5 counter leaves nothing
under its scratch root after a run (`ls` before/after). Each check: command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR97.md (early, updated)."""),
]

spec = {
    "wave": "r97-w1",
    "milestone": "r97-w1: C1 dispatch-prompt self-test kills t01..t13 under the v5 counter; C2 v5 refuses g3/g7/g8; S273; 5 attack seats + v5 forgery probe",
    "reportDir": ".ufo/waves/round-97/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-97/r97-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
