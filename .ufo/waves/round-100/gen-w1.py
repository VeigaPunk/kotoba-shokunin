#!/usr/bin/env python3
"""Generate the round-100 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "7b449a637c03d9b4c43a81b4df37cb38c2ea89ee"
INSTR = "d1e1170d950fc378bb6a28bbfc5a62802669be86"
W1 = f"{LANE}/.ufo/waves/round-100/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r100"
CTR = f"{LANE}/verifiers/fixtures/round-100/selftest-kills.py"
CTC = f"{LANE}/verifiers/fixtures/round-100/anchor-lists.py"
RCP = f"{LANE}/.ufo/waves/round-100/receipts"
P99 = f"{LANE}/.ufo/waves/round-99/w1"
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
NEVER clone, copy or extract anything into {LANE} itself (round 99: a seat left a 366 MB clone `repo/` at the lane root) — clones live
ONLY under {SCRATCH}/<your-seat-name>/.
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
lane (under a minute; also `r99c1`, `r98c1`, `r97c1`, `r96c1`, `r95c1`, the positive-control tables; `--rules v5` reproduces the round-97 rules).
C2 `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTC} <rev> "$D"` (about 4 minutes: truth table over both public citation checks, a
fleet-shaped sandbox for the real-tree gate, its self-test, the revert mutant, three frozen-byte conjuncts and the tip battery incl. the
~190 s floors gate).
At most two counter runs at a time per seat.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR100 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR100 (lane L1)" heading — your files and headings carry YOUR seat name only.
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

## Frozen state (round 100, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Instrument commit (counters): {INSTR}. Freeze commit (plan + pre-data receipts): {BASE}.
Read {LANE}/plans/round-100.md FULLY first, then the headers of {CTR} and {CTC}. TWO claims:
C1 (depth): the dispatch-prompt checker's self-test (verifiers/verify_dispatch_prompts.py --self-test) kills the six frozen survivors
t01..t06 (CLAIMS["c1"] in {CTR}; MutTesterDispatchR99 m01, m02, m03, m22, m08 and the F3 sort permutation) — target
`C1 targets killed 6 of 6 ... C1-PREDICATE-MET`.
C2 (consistency/calibration): verifiers/verify_skill_checklist.py reads comma-list line anchors (`file.md:30,37`) as line anchors —
`anchor-lists.py <rev>` → `C2 mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok`,
C2-PREDICATE-MET. The C2 counter admits ONLY: the frozen fix line in strip_token_dressing (exact bytes in the plan and the counter's FIX_LINE),
new arms inside self_test(), removal of the ONE GOVERNANCE_CORRECTIONS row whose stale token is
`corpus/lessons/round-80-verifier-spotcheck.md:30,37`, and one INSTRUMENT_PINS admission in check_tip_battery.py.
Nobody edits the plan, the counters, or any frozen predicate: an amendment is an L1 act via plans/round-100-addendum-*.md BEFORE any scored
reading; a counter defect you find is a FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {RCP}/ (redbefore-c1-base.txt UNMET 0 of 6; redbefore-c1-base-rulesv5.txt; poscontrol-r99c1/r98c1-base.txt MET;
c2-base.txt UNMET 8 of 28; c2-ctl-p1/f1..f5 controls, patches in {RCP}/ctl-worlds/; sources-opened.txt for S282-S285).
Round-99 evidence you will need: {P99}/MutTesterDispatchR99.md (+ MutTesterDispatchR99/probe_r99.py, witness_r99.py: a working witness
input for every C1 target) and /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-98/w1/ScoutTipReds.md (F5: the comma-anchor defect).
FROZEN ANCHORS (C1): the counter's mutants substitute literal anchor text in verifiers/verify_dispatch_prompts.py; each anchor of CLAIMS["c1"],
CLAIMS["r99c1"], CLAIMS["r98c1"], CLAIMS["r97c1"] and CLAIMS["r96c1"] in {CTR} must stay byte-identical and match exactly once. Never add another
occurrence of an anchor text anywhere in the file (new self-test code included; e.g. never write `    for cid in wanted:` or
`        if not path.is_dir():` again).
ANTI-SNIFFING (C1, C2): a self-test arm must observe BEHAVIOUR (call main, run_checks, read_text, strip_token_dressing, the citation checks
on fixture inputs and read the result), never read the checker's own source. The C1 counter runs every mutant source-blind AND mirrored,
git-less, minimal env, shuffled, bracketed by honest runs, with comment and code decoys; reviewers refuse source readers. A kill must be a
REPORTED failure (`self-test FAIL: ` line and `<N> failure(s) over <M> assertions`, N >= 1, exit 1): an arm that crashes on a mutant is a
RUN-ERROR and does not count — every new assertion goes through the self-test's `rec(...)` tally and catches exceptions (t04's mutant lets a
plain file reach directory iteration: it raises NotADirectoryError). Arms must not need git, network, or any environment variable beyond
TMPDIR/HOME; main() arms pass argv explicitly and capture stdout/stderr in-process; the mode-000 arm (t02) runs as uid 1000 on this host —
guard it anyway: if os.access says the chmod-000 file is still readable (root), the arm prints a skip note instead of a false failure.
PATCH BASE: every patch is `git diff --binary {BASE}` from YOUR scratch clone.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md; no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/ (all rounds),
verifiers/floors-registry.json, verifiers/corpus-baseline.json (the L1 re-records it at integration).

## File ownership (one writer per file; each builder writes only its own patch)
ExecArmsR100 owns verifiers/verify_dispatch_prompts.py (the self_test() function ONLY: one insert-only region inside it).
ExecAnchorR100 owns verifiers/verify_skill_checklist.py (the frozen fix line, new arms inside self_test(), and the removal of the one
GOVERNANCE_CORRECTIONS row — NOTHING else in the file, not even the docstring) and verifiers/check_tip_battery.py (INSTRUMENT_PINS block ONLY).
ScribeCorpusR100 owns corpus/SOURCES.md (APPEND rows S282-S285 only) and corpus/lessons/round-100.md (new).
The L1 alone writes corpus/README.md, verifiers/corpus-baseline.json, LOG.md, SCORECARD.md and corpus/QUALITY.md at integration.
Every other seat writes NOTHING in any repo except its own receipts under {W1}/<its-seat-name>/ and its report file.
Build seats write their patch under {W1}/<seat>/<seat>.patch and then the READY file {W1}/<seat>_READY.

## Patch and handoff protocol (builders)
Each builder: edit only in its scratch clone $D; `git -C "$D" add -A -- <owned files>`; `git -C "$D" diff --cached --binary {BASE} > {W1}/<seat>/<seat>.patch`;
prove the patch applies on a second fresh scratch clone at {BASE} (`git apply --check`), then remove that clone. Only after the patch
and its receipts exist, write the READY file (content: the patch sha256 and one line saying what it does). A builder that cannot land
its claim writes an EMPTY patch and a READY file naming the honest-stop reason.

## Attack and sentinel handoff (candidate build)
The candidate is {BASE} plus the builder patches named in your item, applied in the order ScribeCorpusR100, ExecAnchorR100, ExecArmsR100. Build it
in your own scratch clone (`git apply` each patch, then `git -C "$D" commit` with the scratch identity) so a gate can name the candidate
revision; pass "$D" as the counter's REPO. The candidate's corpus gates stay red (the unindexed round-99 spot-check lesson and the new
round-100 lesson; the L1 adds the coverage-map rows and re-records the corpus baseline at integration): report that drift, it is not a C1 or
C2 failure — the C2 counter does not read the corpus gates.

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
item("executor", "ExecArmsR100", f"""## ExecArmsR100 — C1 build: the dispatch-prompt self-test kills t01..t06

Read {LANE}/plans/round-100.md § C1, the counter header and CLAIMS["c1"] in {CTR}, the mutant table, § Differential witnesses and F2/F3/F5 in
{P99}/MutTesterDispatchR99.md (witness driver {P99}/MutTesterDispatchR99/witness_r99.py gives a working input for every target), and
{LANE}/verifiers/verify_dispatch_prompts.py (main, its not-a-directory loop and EnvError handler, emit_json, run_checks, read_text, self_test()).
Source S282 (Python 3.15.2 pathlib `Path.is_dir`, {RCP}/sources-opened.txt) grounds the t04 arm: cite it in that arm's comment.
In YOUR scratch clone at {BASE}, change ONLY self_test(), as ONE insert-only region. Add behavioural arms, each a `rec(...)` named
`r100-tNN-...`, that REPORT a failure (never crash) on:
t01 main() with a plain FILE as --prompts (and, separately, a missing path) → rc 2, not 0; t02 main() over a prompts dir holding a mode-000
round prompt → rc 2 (substrate), not 1; t03 main(["--json", ...]) with a plain file as --prompts → the emitted JSON payload's `exit_code` is 2;
t04 main() with a plain file as --prompts → rc 2 and an `ERROR ... not a directory` line, and the arm survives a raised exception (catch it,
record a failure); t05 read_text() on a UTF-8 file holding a non-ASCII text (e.g. `café`) returns exactly that text; t06
run_checks(..., ["dispatch.08","dispatch.04"]) returns results in REQUEST order (ids ["dispatch.08","dispatch.04"]).
Arms must work in a git-less copy with only TMPDIR/HOME set. Keep FROZEN ANCHORS byte-identical and unique. Verify in your clone, receipts under
{W1}/ExecArmsR100/: `--self-test` → 0 failure(s); `--box-proof` → boxes proven 2 rc 0; commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecArmsR100 python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET (6 KILLED, decoys 6/6 held), the same
with `--rules v5`, and r99c1, r98c1 → MET. Patch {W1}/ExecArmsR100/ExecArmsR100.patch; report {W1}/ExecArmsR100.md; then {W1}/ExecArmsR100_READY."""),

item("executor", "ExecAnchorR100", f"""## ExecAnchorR100 — C2 build: comma-list line anchors read as line anchors

Read {LANE}/plans/round-100.md § C2, the header of {CTC} (FIX_LINE, BASE_LINE, RETIRED_STALE, checklist_confined), ScoutTipReds F5
({LANE}/.ufo/waves/round-98/w1/ScoutTipReds.md), and in {LANE}/verifiers/verify_skill_checklist.py: strip_token_dressing, path_like_arg,
citation_subjects, correction_problems, check_governance_citations, GOVERNANCE_CORRECTIONS (the row for LOG.md 3598 / SCORECARD.md 529), self_test().
In YOUR scratch clone at {BASE}, within your file ownership ONLY:
(1) replace the strip_token_dressing regex line with the counter's FIX_LINE, byte for byte;
(2) add arms inside self_test() (`rec(...)`, named `r100-...`) that call strip_token_dressing and BOTH public citation checks
(check_citation_resolves on a line list, check_governance_citations(world, errata=(), corrections=()) on a fixture world under TMPDIR) and
REPORT a failure when the old regex is restored: comma pair `:30,37`, comma with range `:3,7-9`, a trailing-comma `:30,37,`, and the negative
cases that must stay red (`:30,abc`, `:30,,37`, `:,30`, a missing file with `:30,37`);
(3) remove exactly the GOVERNANCE_CORRECTIONS row whose stale token is `corpus/lessons/round-80-verifier-spotcheck.md:30,37` (with the fix,
its subject resolves and the fail-closed correction check would report it) — no other row changes, the horizon line stays;
(4) verifiers/check_tip_battery.py: admit the new checklist blob (`git -C "$D" hash-object verifiers/verify_skill_checklist.py`) in
INSTRUMENT_PINS, keeping every earlier pin, with a one-line comment naming round 100.
Measure (receipts under {W1}/ExecAnchorR100/): `--self-test` (assertion count, must be ≥ 1864) and the real-tree gate run in your clone;
commit and run `HYAKU_SCRATCH={SCRATCH}/ExecAnchorR100 python3 -B {CTC} <your commit> "$D"` → C2-PREDICATE-MET. Patch
{W1}/ExecAnchorR100/ExecAnchorR100.patch; report {W1}/ExecAnchorR100.md; then {W1}/ExecAnchorR100_READY."""),

item("scribe", "ScribeCorpusR100", f"""## ScribeCorpusR100 — SOURCES rows S282-S285 and the round-100 lesson scaffold

Read {LANE}/plans/round-100.md, {RCP}/sources-opened.txt, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract; rule 2: a
correction is a NEW row whose `teaches` opens `supersedes S0NN —`, the old row is never edited), the rows S253, S270, S276, S279, S281 of
{LANE}/corpus/SOURCES.md (shape), {LANE}/corpus/lessons/round-99.md (structure) and {LANE}/corpus/lessons/round-99-verifier-spotcheck.md (routed
defects). Poll for {W1}/ScoutSourcesR100.md (up to 45 min); use only facts it or you located in bytes you fetched yourself.
In YOUR scratch clone at {BASE}: (1) append rows (11 columns, no `|` in any cell, opened 2026-11-06, a valid recheck cadence):
S282 Python docs pathlib at https://docs.python.org/release/3.15.2/library/pathlib.html — `teaches` opens `supersedes S276 —` (S276 cites the
rolling `/3/` alias whose digest moves with the build footer); grounds the C1 t04 arm (`Path.is_dir` false for a plain file); `mined`, used-by
`corpus/lessons/round-100.md`. S283 tempfile (supersedes S253), S284 unittest (supersedes S270), both pinned to release/3.15.2, same digest
reason; `mined` only if the lesson cites them (it does: § Gate), used-by `corpus/lessons/round-100.md`. S285 ptrace(2) — `supersedes S279 —`,
adding access-check step (4)'s CAP_SYS_PTRACE conjunct (round-99 C99-3), with the located quote. Each anchor: section, HTML line(s), revision,
digest. (2) write corpus/lessons/round-100.md as a SCAFFOLD (author ScribeCorpusR100): `## Gate` (per new row: URL, access date, HTTP, bytes,
sha256, HTML line excerpt, ≤25-word located quote with `wc -w` count; plus one REJECT you opened — e.g. a candidate source for the comma-list
anchor convention — with reason and flip), `## Corrections` (C100-1: the round-99 lesson § Gate cites `verifiers/check_tip_battery.py:344` for
the `rev-parse <rev>:<path>` read; that is the line at the round-99 base `52e8e95a`; at the round-99 tip `0a65cceb` it is line 349 — cite as
`52e8e95a:verifiers/check_tip_battery.py:344` = `0a65cceb:verifiers/check_tip_battery.py:349`, verify both with `git show <rev>:<path> | sed -n Np`),
`## Mistakes` (class `line-pointer-cited-at-base-revision` · evidence round-99-verifier-spotcheck.md routed defect 1 · captured-by none · fix
C100-1 plus a QUALITY criterion (L1 adds Q90) · shown able to fail: the `sed -n 344p` at `0a65cceb` lacks `rev-parse`), `## Status changes`
(old→new for every registry cell changed in place; expected none — superseded rows stay as they are), `## Considerthese` (re-read
{LANE}/considerthese/ newest file; name which proposal is still unimplemented and whether it is taken this round), `## Settlement` (placeholder
for the L1). Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 (receipt under
{W1}/ScribeCorpusR100/; report the W04 count — one new W04 is expected for S285 sharing S279's URL). Patch
{W1}/ScribeCorpusR100/ScribeCorpusR100.patch; report {W1}/ScribeCorpusR100.md; then {W1}/ScribeCorpusR100_READY."""),

item("scout", "ScoutSourcesR100", f"""## ScoutSourcesR100 — re-open the four pinned sources independently

Fetch each yourself (curl into your scratch dir, twice, to show the digest is stable): https://docs.python.org/release/3.15.2/library/pathlib.html,
.../tempfile.html, .../unittest.html (same release path), and https://man7.org/linux/man-pages/man2/ptrace.2.html. For each: HTTP, bytes, sha256 —
equal to the L1's in {RCP}/sources-opened.txt? Locate: pathlib § Path.is_dir ("False will be returned ... something other than a directory") and
§ Path.read_text (encoding), tempfile `ignore_cleanup_errors` (the S253 quote), unittest TestResult.errors vs failures (the S270 quote), ptrace
access-mode check step (4) in full INCLUDING the CAP_SYS_PTRACE conjunct. Give HTML line numbers and a ≤25-word quote with `wc -w` per item.
Judge whether S282 grounds the C1 t04 arm (verify_dispatch_prompts.py main()'s `is_dir` substrate check) against {LANE}/corpus/QUALITY.md and
/home/vgpnk/Projects/shokunin/CORPUS.md tiers. Also open ONE candidate authority for the `file:N,M` comma-list line-anchor convention C2 reads
(e.g. a documented citation/line-reference convention) and judge admit/reject with reason and flip condition. Check the registry for existing
rows on each URL (`grep -n <host-path> {LANE}/corpus/SOURCES.md`). Write {W1}/ScoutSourcesR100.md early and update it. Do NOT save HTML under {W1}.
No repo writes."""),

item("connector", "ConnectorOverlapR100", f"""## ConnectorOverlapR100 — overlap scan and planning data-walk (read-only)

Part 1 (cross-claim): does C1's change to verify_dispatch_prompts.py self_test() change any C2 reading (the checklist delegates dispatch boxes to
`verify_dispatch_prompts.py --box-proof`; the battery's floors gate and instrument-pin guard)? Does C2's change (checklist fix line, arms, one
corrections row, a battery pin) change any C1 reading? Name exact lines. Part 2 (siblings, read-only): grep sibling lanes under
/home/vgpnk/Projects/shokunin/*-shokunin for copies or ports of `strip_token_dressing` / a `:\\d+(-\\d+)?$` line-anchor strip that would share the
comma-list false red, and for closure-landed spot-check lessons that leave a lane's own corpus index red at the next round base (this lane's
round-100 base reads `unindexed=1` for corpus/lessons/round-99-verifier-spotcheck.md); name file:line — a cross-lane finding for the report, not
a write. Part 3: this is the lane's round 100 (campaign end): list what remains open after this round (the v7 counter for g11/g16; the C2 counter
holes of round 99; any survivor the mutation seats find), each with a falsifiable before→after for a successor round. Write
{W1}/ConnectorOverlapR100.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerArmsR100", f"""## ReviewerArmsR100 — review the C1 patch

Wait for {W1}/ExecArmsR100_READY. Review {W1}/ExecArmsR100/ExecArmsR100.patch against plans/round-100.md § C1 and the context's ANTI-SNIFFING and
FROZEN ANCHORS rules: does each new arm observe behaviour, never the checker's source? Does it kill t01..t06 for the stated reason (apply each
mutant by hand in your candidate clone and name WHICH assertion fails, with its `self-test FAIL:` line and the failure count)? Is production
code byte-identical outside self_test() (`git diff` hunks)? Do fixtures stay under TMPDIR and get cleaned (incl. the chmod-000 file, restored
before removal)? Do the main() arms leak stdout/stderr redirection or argv state between arms if one raises? Run the counter c1, c1
`--rules v5`, r99c1, r98c1 and `--box-proof` on the candidate. Blocking findings first. Write {W1}/ReviewerArmsR100.md (early, updated)."""),

item("reviewer", "ReviewerAnchorR100", f"""## ReviewerAnchorR100 — review the C2 patch

Wait for {W1}/ExecAnchorR100_READY. Review {W1}/ExecAnchorR100/ExecAnchorR100.patch against plans/round-100.md § C2 and the header of {CTC}:
is the fix line byte-equal to FIX_LINE; does the new regex accept only digit lists (`N`, `N-M`, comma-joined) and refuse every other suffix;
does it change the reading of any OTHER token the checklist reads on the real tree (run the gate at {BASE} and on the candidate with `--json`
and diff every evaluated subject list — trigger.citation_resolves, governance.citation_resolves and the command checks that use path_like_arg;
name every token whose normalisation changed)? Is the removed corrections row the only data change, and is removing it honest (the subject now
resolves; LOG.md:3598's notice stays as history)? Do the new arms observe behaviour and kill the revert? Is the battery change pins-only? Run
the counter on the candidate ({BASE} + ExecAnchorR100.patch). Blocking findings first. Write {W1}/ReviewerAnchorR100.md (early, updated)."""),

item("mutation-tester", "MutTesterAnchorR100", f"""## MutTesterAnchorR100 — attack the C2 counter and the new regex (scratch only)

Read {CTC} and the six committed controls ({RCP}/ctl-worlds/*.patch, receipts {RCP}/c2-ctl-*.txt). (a) Build at least SIX NEW forgery worlds on
{BASE} in your scratch clone that try to read C2-PREDICATE-MET without the honest change, aimed at the counter's conjuncts: e.g. a fix placed
in a different function that strip_token_dressing calls; a self-test arm that sniffs its own source for BASE_LINE; a module-level monkeypatch
of strip_token_dressing outside the function; a corrections row edited instead of removed; a pin admitted by code; a checklist whose truth-table
functions special-case `corpus/lessons/x.md`. Run `HYAKU_SCRATCH={SCRATCH}/MutTesterAnchorR100 python3 -B {CTC} <commit> "$D"` on each; report
tally lines and which conjunct caught it. (b) Wait (up to 75 min) for {W1}/ExecAnchorR100_READY; on the candidate apply at least EIGHT mutants of
the new regex and the new arms (drop the `*`, `+` instead of `*`, `[\\d,-]+`, unanchored `$`, `\\s*` after commas, drop the trailing-punct rstrip, …)
and classify each KILLED/SURVIVED by the checklist self-test, with a witness token for every survivor (equivalent ones named). A world that
reads MET is a counter finding (class, severity, minimal fix) — never edit the counter. Report {W1}/MutTesterAnchorR100.md (early, updated),
receipts {W1}/MutTesterAnchorR100/."""),

item("mutation-tester", "MutTesterDispatchR100", f"""## MutTesterDispatchR100 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecArmsR100_READY. On the candidate ({BASE} + that patch) design at least 10 NEW mutants of verifiers/verify_dispatch_prompts.py
that are NOT in CLAIMS["c1"], ["r99c1"], ["r98c1"], ["r97c1"], ["r96c1"] of {CTR} nor m01-m22 of {P99}/MutTesterDispatchR99.md (ideas: the other
two not-a-directory paths (state, fleet), emit_json's other fields, the EnvError handler's --json branch, read_text's errors= mode, run_checks
duplicates, build_parser defaults). Apply each with the counter's method (reuse {P99}/MutTesterDispatchR99/probe_r99.py's approach: import
RUNNER/classify/code_decoy from a scratch copy of {CTR}) and classify KILLED / RUN-ERROR / SURVIVED at {BASE} and on the candidate, with a
differential witness per verdict-bearing survivor and the equivalent / no-verdict ones named. Write {W1}/MutTesterDispatchR100.md (early,
updated), receipts {W1}/MutTesterDispatchR100/."""),

item("critic", "CriticClaimR100", f"""## CriticClaimR100 — falsify the two frozen claims against the full candidate

Wait for {W1}/ExecArmsR100_READY, {W1}/ExecAnchorR100_READY and {W1}/ScribeCorpusR100_READY. Build the full candidate (order ScribeCorpusR100,
ExecAnchorR100, ExecArmsR100). Run C1 (c1, `--rules v5`, r99c1) and C2 on it, and on each single-patch candidate (separability). Re-run the
do-nothing controls (c1 and C2 at {ROUND_BASE}) and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper change meet
either target? Is C2 a real consistency move (the gate's self-assessment against repo state) or relabelled bookkeeping (§9: name the axis by
the surface)? Is the truth table's notion of "resolves" honest (does the real checklist ever need a comma anchor to resolve; SKILL.md
`S090 :10,18,34,40-42`)? Are the six C1 targets real false greens of the exit/decode/order contract or contrived; is excluding m19/m09/m21/m04
and admitting m03 honest? Does S282 ground the t04 arm (open the page)? Does the mined mistake's fix fail on its committed control? Is carrying
the v7 counter again honest (routed defect 4a)? Write {W1}/CriticClaimR100.md (early, updated) with MET/UNMET verdicts on the candidate and
defects D1..Dn."""),

item("sentinel", "SentinelScopeR100", f"""## SentinelScopeR100 — scope, safety and no-harm on the candidate

Wait for the three READY files (as CriticClaimR100). On the full candidate: (1) scope — `git diff --stat {BASE}` lists only owned files;
SKILL.md byte-identical; no spotcheck file or fixture touched; verify_dispatch_prompts.py production code outside self_test() byte-identical;
verify_corpus_integrity.py / verify_corpus_independent.py byte-identical; verify_skill_checklist.py changed only at the fix line, self_test()
and one corrections row; (2) no-harm — `python3 -B verifiers/check_gate_registry.py --rev <cand>`, the round-99 counter
`verifiers/fixtures/round-99/selftest-kills.py c1|r98c1 <cand> "$D"` (MET), `check_assertion_floors.py --self-test`,
`verify_dispatch_prompts.py --box-proof` (boxes proven 2) and its live run over /home/vgpnk/Projects/shokunin/.ufo/prompts (same verdict lines at
{BASE} and the candidate), the checklist's real-tree run (same PASS ids at {BASE} and the candidate), census `--file` on the candidate
SOURCES.md (rc 0), the full tip battery `python3 -B verifiers/check_tip_battery.py --repo "$D" --rev <cand> --fleet /home/vgpnk/Projects/shokunin`
(expect the two corpus gates red until the L1's index rows — report it); (3) safety — no hardcoded /tmp in new code, no network in self-tests,
fixtures only under TMPDIR, the chmod-000 fixture restored/removed, no credential-shaped strings, and `git -C {LANE} status --porcelain`
plus `ls {LANE}` show no seat-made file or clone in the lane. Each check: command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR100.md
(early, updated)."""),
]

spec = {
    "wave": "r100-w1",
    "milestone": "r100-w1: C1 dispatch-prompt self-test kills its exit-2 ladder t01..t06 (v6.2); C2 checklist reads comma-list anchors (anchor-lists v1); S282-S285; 5 attack seats",
    "reportDir": ".ufo/waves/round-100/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-100/r100-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
