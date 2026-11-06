#!/usr/bin/env python3
"""Generate the round-98 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "a33f262fc94e3cf27f3c935b5c53c1336bb94166"
INSTR = "a060b450a43673ebc54720a5192e99df188e80ce"
W1 = f"{LANE}/.ufo/waves/round-98/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r98"
CTR = f"{LANE}/verifiers/fixtures/round-98/selftest-kills.py"
CTL = f"{LANE}/verifiers/fixtures/round-98/forgery-controls.py"
CTR5 = f"{LANE}/verifiers/fixtures/round-97/selftest-kills.py"
RCP = f"{LANE}/.ufo/waves/round-98/receipts"
P97 = f"{LANE}/.ufo/waves/round-97/w1"
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
The frozen v6 counter accepts REV and REPO: `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTR} c1 <rev> "$D"` measures a candidate
commit of your scratch clone without touching the lane (~30 s; also `r97c1`, `r96c1` and `r95c1`, the positive-control tables;
`--rules v5` reproduces the round-97 rules, `--rules v4` the round-96 rules). The C2 runner:
`HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTL} v6 {BASE}` (a few minutes; modes v5, v6, v6-as-v5). At most two counter runs at a
time per seat.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR98 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR98 (lane L1)" heading — your files and headings carry YOUR seat name only.
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


## Frozen state (round 98, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Instrument commit (v6 counter + C2 runner): {INSTR}. Freeze commit (plan +
pre-data receipts): {BASE}.
Read {LANE}/plans/round-98.md FULLY first, then the headers of {CTR} and {CTL}. TWO claims:
C1 (depth): the dispatch-prompt checker's self-test (verifiers/verify_dispatch_prompts.py --self-test) kills the nine frozen survivors
t01..t09 (CLAIMS["c1"] in the v6 counter; MutTesterDispatchR97 m20, m22-m28, m31) — target
`C1 targets killed 9 of 9 ... C1-PREDICATE-MET`.
C2 (consistency/calibration): the v6 counter refuses the committed round-97 forgery worlds g10 (HEAD self-compare) and g11 (seeded schedule
replay) that v5 reads MET, while still refusing g3/g7/g8 and holding h1/h2 — `forgery-controls.py v6 <rev>` →
`forgeries refused 5 of 5; honest held 2 of 2`.
Nobody edits the plan, the counter, the runner, the round-96/97 patches or any frozen predicate: an amendment is an L1 act via
plans/round-98-addendum-*.md BEFORE any scored reading; a counter defect you find is a FINDING in your answer — never rescue a counter by
changing its predicate.
Pre-data receipts: {RCP}/ (redbefore-c1-base.txt UNMET 0 of 9; redbefore-c1-base-rulesv5.txt; poscontrol-r97c1/r96c1/r95c1-base.txt MET;
c2-before-v5.txt refused 3 of 5; c2-v6-as-v5.txt refused 3 of 5; c2-v6.txt; sources-opened.txt S277-S280 candidates).
FROZEN ANCHORS: the counter's mutants substitute literal anchor text in verifiers/verify_dispatch_prompts.py; each must stay byte-identical
and match exactly once (see CLAIMS["c1"], CLAIMS["r97c1"] AND CLAIMS["r96c1"] in {CTR}; e.g. the ROUND_FILE_RE line,
`dirs = sorted({{r for r, _s in paths}})`, `    for f in result["files"]:`, `        if entry.get("disposition") != want:`,
`        if live.get(cid) != pinned:`, `        if m and m.group(1)[0] * 3 == fence:`, `    if legacy.is_file():`, the dispatch.04 docstring +
`names = sorted(...)` pair, `        if stem.endswith(".md"):`, `stem = stem[:-3]`, `if note:`, `    if fails:`). Never add another occurrence of an
anchor text anywhere in the file (new self-test code included); mutated statements keep their line count.
ANTI-SNIFFING: a self-test arm must observe BEHAVIOUR (call lane_of, report_paths, state_source, evaluate_dispatch_04/08, _verdict_of,
dispatch_box_sha256, box_proof or _finish on fixture inputs and read the result). The v6 counter runs every mutant source-blind AND mirrored,
in a fresh git-less copy with a minimal environment per run, shuffled, bracketed by three honest runs, with comment and code decoys;
reviewers refuse source readers. A kill must be a REPORTED failure in BOTH runs (a `self-test FAIL: ` line and
`<N> failure(s) over <M> assertions` with N >= 1, exit 1): an arm that crashes on a mutant is a RUN-ERROR and does not count — every new
assertion goes through the self-test's `rec(...)` tally. Arms must not need git, network, or any environment variable beyond TMPDIR/HOME.
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
The L1 lands SCORECARD/LOG/QUALITY at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-9*/
(round-98 included), verifiers/fixtures/dispatch-prompts/ (the committed box-proof corpus), verifiers/floors-registry.json.

## File ownership (one writer per production file; each builder writes only its own patch)
ExecArmsR98 owns verifiers/verify_dispatch_prompts.py (the self_test() function and self-test-only helpers/constants next to it ONLY;
everything from the module docstring through run_checks() and box_proof()/main() stays byte-identical).
ScribeCorpusR98 owns corpus/SOURCES.md (APPEND rows S277-S280 only), corpus/lessons/round-98.md (new), corpus/README.md (one index row for the
new lesson ONLY).
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
item("executor", "ExecArmsR98", f"""## ExecArmsR98 — C1 build: the dispatch-prompt self-test kills t01..t09

Read {LANE}/plans/round-98.md § C1, the v6 counter header and CLAIMS["c1"] in {CTR}, the mutant table and differential witnesses in
{P97}/MutTesterDispatchR97.md (§ Differential witnesses, F2-F6 give minimal arms; witness driver {P97}/MutTesterDispatchR97/witness_r97.py),
and {LANE}/verifiers/verify_dispatch_prompts.py (lane_of, ROUND_FILE_RE, report_paths, state_source, evaluate_dispatch_04/08, _verdict_of,
dispatch_box_sha256, box_proof, _write_case, self_test()).
In YOUR scratch clone at {BASE}, change ONLY self_test() and self-test-only helpers/fixture text next to it; production behaviour stays
byte-identical (git diff hunks only inside the self-test section). Add behavioural arms, each a `rec(...)` naming the arm (`r98-t01-...`), that
REPORT a failure (never crash) on:
t01: a prompts-dir file `kote-round-7.md.bak` → not a dispatch prompt (lane_of returns no lane; the dispatch.04 check does not evaluate it);
t02: a prompt carrying report paths in round-7 AND round-8 dirs with file round 8 → dispatch.08 filename_report_dir_round_equal FAIL;
t03: `_verdict_of` (or the box result reader) on a multi-file result whose target file is NOT first → the file's verdict is found;
t04: a box-proof tree whose map entry has `disposition: executed:...` (not the delegation) → box_proof reads `boxes proven 0`/rc 1 (not 2);
t05: a box-proof tree whose dispatch.04 box text in the copied SKILL.md is reworded → box_proof rc 1 with the live-hash detail;
t06: dispatch_box_sha256 over text with a `~~~` line inside a ``` fenced block → the block does not close early (box hashes as honest);
t07: a DIRECTORY named `<lane>.round` in the state dir → state_source reads no state (kind none), not stale/legacy;
t08: a DIRECTORY named like a prompt (`ghost-round-7.md`) in the prompts dir → ignored (evaluated count unchanged, no EnvError);
t09: a report path `.ufo/reports/round-7/kote.MD` → the stem is `kote.MD` (not stripped), so report_stem_is_lane_id FAILs for lane kote.
Arms must work in a git-less copy with only TMPDIR/HOME set (the v6 world). Keep FROZEN ANCHORS byte-identical and unique. Verify, in your
clone, with receipts under {W1}/ExecArmsR98/: `--self-test` → 0 failure(s); `--box-proof` → boxes proven 2, rc 0; commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecArmsR98 python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET (9 KILLED blind and mirror, no RUN-ERROR,
decoys 9/9 held), the same with `--rules v5`, and `r97c1`, `r96c1`, `r95c1` → MET.
Patch {W1}/ExecArmsR98/ExecArmsR98.patch; report {W1}/ExecArmsR98.md; then {W1}/ExecArmsR98_READY."""),

item("executor", "ExecForgeryV6", f"""## ExecForgeryV6 — attack the v6 counter with new forgery worlds (scratch only; C2 attack)

Read the header of {CTR} (rules 1-10 and the disclosed bounds), {CTL}, and {P97}/ExecForgeryV5.md (g9-g12; patches under
{P97}/ExecForgeryV5/). Build at least FOUR NEW forgery worlds of verifiers/verify_dispatch_prompts.py on the round-96 freeze
679775abb9277a7b8d17f060b0f5b4ced2b127b6 (the commit the g-patches apply to) in your scratch clone, each a self-test that tries to read
MET on the `r96c1` table WITHOUT behavioural arms, aimed at v6's new rules: (g13) reads REPO and REV from /proc/<ppid>/cmdline and compares
itself with `git -C <repo> show <rev>:<instrument>` (the disclosed bound — confirm or refute it); (g14) reads /proc/<ppid>/environ for the
replay seed (rule 9's non-dumpable claim — does the read fail?); (g15) finds the lane by scanning the filesystem or $PATH-adjacent dirs without
the parent's argv; (g16) any signal that still separates an honest run from a blind/mirror run in a git-less world (file mtimes in the copy,
inode numbers, the src.py path, the reflink copy's timestamps, /proc/self/cmdline of the RUNNER). Commit each in your scratch clone (scratch
identity), save patches under {W1}/ExecForgeryV6/<world>.patch, and run `HYAKU_SCRATCH={SCRATCH}/ExecForgeryV6 python3 -B {CTR} r96c1 <commit> "$D"`
plus `--rules v5`. Report per world: tally lines, MET/UNMET, which rule caught it. A world that reads MET under v6 is a counter finding (class,
severity, minimal fix) — never edit the counter. Clean up anything you write outside your scratch dir. Report {W1}/ExecForgeryV6.md (early, updated)."""),

item("scout", "ScoutSourcesR98", f"""## ScoutSourcesR98 — re-open C2's sources and judge them

The L1 opened four URLs on 2026-11-06 (receipt {RCP}/sources-opened.txt: HTTP, bytes, sha256, HTML line excerpt, quote and word count):
https://docs.python.org/3/library/subprocess.html, https://git-scm.com/docs/git-archive,
https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html, https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html.
Re-open each yourself (curl into your scratch dir; record HTTP code, size, sha256 — say whether each equals the L1's; if a page differs, locate
the quote in your bytes and give your line numbers). Judge each against {LANE}/corpus/QUALITY.md and /home/vgpnk/Projects/shokunin/CORPUS.md
(§ SOURCES.md tiers): does it ground the v6 rule the plan says (rule 8 git-less tree, rule 9 child env, non-dumpable environ)? Admit or reject with
reason and flip condition; check the registry for an existing row on each URL (`grep -n` in {LANE}/corpus/SOURCES.md). Also open ONE more
candidate that would ground a rule or a bound (e.g. proc_pid_cmdline(5) on cmdline readability for the disclosed bound; ptrace(2) access mode
rules) and judge it. Write {W1}/ScoutSourcesR98.md: per URL, access date, HTTP, bytes, sha256, located quote ≤25 words with HTML line and word
count (`printf '%s\\n' "<quote>" | wc -w`), verdict + reason + flip condition. Do NOT save the HTML under {W1}. Early, updated; no repo writes."""),

item("scout", "ScoutTipReds", f"""## ScoutTipReds — the three carried red gates of the tip battery (read-only; round-97 closure routed defect 1)

The tip battery `python3 -B {LANE}/verifiers/check_tip_battery.py` reads `3 of 6` with `verify_skill_checklist`, `verify_corpus_integrity` and
`verify_corpus_independent` red since round 96 (receipt {LANE}/.ufo/waves/round-97/receipts/landing/tip-battery.txt). For each red gate, at
{BASE} in a scratch clone: run it, record the exact failing lines and exit code, and find the CAUSE (which check id, which file:line, which
round's commit introduced the drift — `git log -S`/`git log --follow` read-only). Classify each: (a) stale baseline/pin the lane can re-record
honestly, (b) real content defect, (c) gate defect. For each give the minimal fix and the falsifiable before→after a future round could claim,
with the do-nothing control that would NOT meet it. Do not fix anything. Write {W1}/ScoutTipReds.md (early, updated); receipts under
{W1}/ScoutTipReds/."""),

item("scribe", "ScribeCorpusR98", f"""## ScribeCorpusR98 — SOURCES rows S277-S280 and the round-98 lesson scaffold

Read {LANE}/plans/round-98.md, {RCP}/sources-opened.txt, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract), the last
rows of {LANE}/corpus/SOURCES.md (S273-S276 show the lane's 11-column shape), {LANE}/corpus/lessons/round-97.md (structure) and
{LANE}/corpus/lessons/round-97-verifier-spotcheck.md. Poll for {W1}/ScoutSourcesR98.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append rows S277 (Python subprocess Popen env — grounds v6 rule 9), S278 (git-archive — grounds rule 8),
S279 (proc_pid_environ(5) — grounds the non-dumpable counter), all `mined`, used-by `corpus/lessons/round-98.md,plans/round-98.md`, and S280
(PR_SET_DUMPABLE page) as a REJECTED row (redundant: speaks of PTRACE_ATTACH, not environ reads; flip condition) — tier per CORPUS.md, opened
2026-11-06, recheck a valid cadence, no `|` inside cells; if the scout rejects one the L1 admitted, record the disagreement in the lesson and
follow the scout only if it shows the quote absent; (2) write corpus/lessons/round-98.md as a SCAFFOLD (author ScribeCorpusR98) with `## Gate`
(each row: URL, access date, HTTP, bytes, sha256, HTML line excerpt, ≤25-word located quote and word count — the excerpt makes a re-open
verifiable even when the whole-page digest drifts, round-97 closure defect 7), `## Mistakes` (one row: class `measured-child-reads-counter-state`
· evidence plans/round-97-addendum-1.md A1/A2 and .ufo/waves/round-97/w1/ExecForgeryV5.md F1/F2 · captured-by: Q87 (its isolation names
clone/TMPDIR/HOME, not history or environment) · fix: v6 rules 8-9 with committed g10/g11 control worlds, shown able to fail by
{RCP}/c2-v6-as-v5.txt refused 3 of 5), `## Status changes` (old→new for every registry cell changed; none expected), `## Considerthese`
(re-read {LANE}/considerthese/2026-10-26.md; name which proposal is still unimplemented and why it is or is not taken this round), and
`## Settlement` (placeholder for the L1); (3) add ONE index row for the lesson to corpus/README.md, shaped like the round-97 row. Run
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 and no new W04 (receipt under
{W1}/ScribeCorpusR98/). Patch {W1}/ScribeCorpusR98/ScribeCorpusR98.patch; report {W1}/ScribeCorpusR98.md; then {W1}/ScribeCorpusR98_READY."""),

item("connector", "ConnectorOverlapR98", f"""## ConnectorOverlapR98 — overlap scan and planning data-walk (read-only)

Part 1: does any no-harm instrument pin a blob, sha, line or assertion count of verifiers/verify_dispatch_prompts.py or of
verifiers/fixtures/round-9*/ such that adding self-test arms or the round-98 fixtures changes its reading? Read verifiers/check_tip_battery.py,
verifiers/check_assertion_floors.py + verifiers/floors-registry.json, verifiers/check_gate_registry.py and SKILL.md § Gate registry,
verifiers/checklist-baseline.json; name exact lines. Part 2 (siblings): grep the sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin
(read-only) for kill counters or mutation harnesses that hand the measured child the parent's environment or a git checkout with history
(the g10/g11 class) and name file:line; a cross-lane finding for the report, not a write. Part 3: the lane reaches round 100 in two rounds:
list three candidate round-99 claims the round-98 evidence supports (one may be the tip-battery reds), each with a falsifiable before→after
and a do-nothing control. Write {W1}/ConnectorOverlapR98.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerArmsR98", f"""## ReviewerArmsR98 — review the C1 patch

Wait for {W1}/ExecArmsR98_READY. Review {W1}/ExecArmsR98/ExecArmsR98.patch against plans/round-98.md § C1 and the context's ANTI-SNIFFING and
FROZEN ANCHORS rules: does each new arm observe behaviour (a function call's result on a fixture input), never the checker's source? Does it
kill t01..t09 for the stated reason (apply each mutant by hand in your candidate clone and name WHICH assertion fails, with its
`self-test FAIL:` line and the failure count)? Is production code byte-identical outside self_test() and its self-test helpers (`git diff`
hunks)? Do fixtures stay under TMPDIR and get cleaned? Run the v6 counter c1, c1 `--rules v5`, r97c1, r96c1, r95c1 and `--box-proof` on the
candidate. Blocking findings first. Write {W1}/ReviewerArmsR98.md (early, updated)."""),

item("reviewer", "ReviewerCounterV6", f"""## ReviewerCounterV6 — review the frozen v6 counter, the C2 runner and the pre-data receipts (read-only)

Review {CTR} and {CTL} at {BASE} against plans/round-98.md: `diff` the v6 counter against the v5 counter {CTR5} — does `--rules v5` reproduce
v5 exactly (per-run `git clone --shared` with history, parent env inherited, same marker, same schedule given the same seed)? Are the r97c1,
r96c1, r95c1 anchors byte-equal to v5's c1, r96c1, r95c1? Do rules 8-10 do what the header says: the per-run world has no `.git` (check a
world mid-run), the child env holds only the six named variables (print `sorted(os.environ)` from a scratch self-test world), the counter is
non-dumpable (`/proc/<counter pid>/environ` read from a child raises PermissionError), and rule 10 turns an unexpected exception into exit 2 (feed
a world that makes the counter raise, e.g. a REPO path that is a file, or a monkeypatched copy). Any fail-open path (exception escaping as exit
1, a run silently skipped, an honest world that passes only because the git-less copy hides a failure)? Does the C2 runner measure the counter
bytes AT REV, build worlds only in scratch with the forgery identity, seed g11 only, and score held/refused as its header says? Re-run, in your
own scratch, redbefore-c1-base, poscontrol-r97c1-base and c2-v6 and compare with {RCP}/. Is each predicate sentence identical in the plan and the
instrument headers? Blocking findings first. Write {W1}/ReviewerCounterV6.md (early, updated)."""),

item("mutation-tester", "MutTesterDispatchR98", f"""## MutTesterDispatchR98 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecArmsR98_READY. On the candidate ({BASE} + that patch) design at least 10 NEW mutants of verifiers/verify_dispatch_prompts.py's
evaluation path that are NOT t01..t09/p00 of the round-98 table nor any row of r97c1/r96c1 nor m20-m34 of {P97}/MutTesterDispatchR97.md (ideas:
box_proof's map parsing and count, dispatch_box_sha256's heading/box boundaries, lane_of's L1 branch, run_checks' aggregation, main()'s exit
codes, the out-of-scope bookkeeping). Apply each with the counter's method (literal substitution; reuse the v6 counter's RUNNER/classify/
code_decoy by import from a scratch copy; git-less world and minimal env as rules 8-9) and classify KILLED / RUN-ERROR / SURVIVED at the base
AND on the candidate. Name equivalent and no-verdict mutants with the reason (they are not kill targets) and a differential witness for each
verdict-bearing survivor. Write {W1}/MutTesterDispatchR98.md (early, updated) and receipts under {W1}/MutTesterDispatchR98/."""),

item("mutation-tester", "MutTesterCounterV6", f"""## MutTesterCounterV6 — mutate the v6 counter itself (scratch copy only; C2 attack; round-97 closure defect 3)

The runner reads the counter with `git show REV:...`, so build a scratch clone of the lane at {BASE}, commit each counter mutant there with the
scratch identity, and run a scratch copy of the runner whose LANE points at that clone — never edit the lane. Counter mutants at least: W1 rule 8
off (git clone world under v6); W2 rule 9 off (inherited env under v6); W3 non-dumpable call removed; W4 rule 10 removed; W5 KOTOBA_R97_SEED kept
in the child env only; W6 the pristine copy made with hardlinks (`cp -al`) instead of a copy; plus the round-97 V4-V9 carried
({P97}/MutTesterCounterV5.md: HOME/XDG not reset, no shuffle, honest any() for all(), UnicodeDecodeError not caught, mirror on_disk = original,
decoys held on RUN-ERROR). For each, run the C2 runner (v6 mode) and the c1/r97c1 base and positive controls. Report a matrix: which committed
control (g3/g7/g8/g10/g11 world, honest h1/h2, redbefore receipt) exposes each counter mutant (verdict flip or tally deviation). A counter mutant
no control exposes is a gap — report it with the minimal new control world that would. Write {W1}/MutTesterCounterV6.md (early, updated) and
receipts under {W1}/MutTesterCounterV6/."""),

item("critic", "CriticClaimR98", f"""## CriticClaimR98 — falsify the two frozen claims against the full candidate

Wait for {W1}/ExecArmsR98_READY and {W1}/ScribeCorpusR98_READY. Build the full candidate ({BASE} + ExecArmsR98.patch + ScribeCorpusR98.patch).
Run the v6 counter c1 (and `--rules v5`), r97c1, r96c1, r95c1 on it and the C2 runner v6 at {BASE}; re-run the do-nothing controls (c1 at
{ROUND_BASE} via the counter at {BASE}; C2 v5 and v6-as-v5) and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper
change meet either target? Is C2 work of this round or a re-labelled instrument (§9: name the axis by the surface)? Are C1 and C2 causally
separable as the plan claims? Are the nine targets real false greens / false reds of the dispatch boxes (SKILL.md § Dispatch-prompt fidelity
dispatch.04/.08 and the box proof) or contrived — and is excluding m32/m34 honest? Do S277-S279 actually ground rules 8-9 (open the pages)?
Does the mined mistake's fix fail on its committed control? Is the round-97 closure's routed-defect list honestly dispositioned in the plan?
Write {W1}/CriticClaimR98.md (early, updated) with MET/UNMET verdicts on the candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR98", f"""## SentinelScopeR98 — scope, safety and no-harm on the candidate

Wait for {W1}/ExecArmsR98_READY and {W1}/ScribeCorpusR98_READY (as CriticClaimR98). On the full candidate: (1) scope — `git diff --stat {BASE}`
lists only owned files; SKILL.md byte-identical; no spotcheck file, dispatch-prompts fixture, round-9x fixture or other verifier touched;
production code of verify_dispatch_prompts.py outside self_test()/helpers byte-identical; (2) no-harm — gate registry
`python3 -B verifiers/check_gate_registry.py --rev <cand>` (base 74 of 74), round-97 `selftest-kills.py c1|r96c1 <cand> "$D"` (MET),
round-96 `selftest-kills.py c1|r95c1 <cand> "$D"` (MET), `check_assertion_floors.py --self-test`, `verify_dispatch_prompts.py --box-proof`
(boxes proven 2) and its live run over /home/vgpnk/Projects/shokunin/.ufo/prompts (same verdict lines at {BASE} and the candidate — production
unchanged), census `--file` on the candidate SOURCES.md (rc 0, W04 count unchanged at 34); (3) safety — no hardcoded /tmp in new code, no
network in self-tests, no credential-shaped strings, fixtures only under TMPDIR; the v6 counter leaves nothing under its scratch root after a
run (`ls` before/after) and its pristine export is removed. Each check: command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR98.md (early, updated)."""),
]

spec = {
    "wave": "r98-w1",
    "milestone": "r98-w1: C1 dispatch-prompt self-test kills t01..t09 under the v6 counter; C2 v6 refuses g10/g11 (and g3/g7/g8); S277-S279; 5 attack seats + v6 forgery probe",
    "reportDir": ".ufo/waves/round-98/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-98/r98-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
