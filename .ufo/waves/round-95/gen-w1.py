#!/usr/bin/env python3
"""Generate the round-95 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "2d886a91e57efd3555ec9076a63209e2d8bfbb8d"
W1 = f"{LANE}/.ufo/waves/round-95/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r95"
CTR = f"{LANE}/verifiers/fixtures/round-95/selftest-kills.py"
FORGE = f"{LANE}/verifiers/fixtures/round-95/build-forgeries.py"
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
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch, pull, push,
branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh. Read-only git (log, show, diff,
status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
Your ONE writable repo is a scratch clone, created exactly as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D" && git -C "$D" checkout -q {BASE}`;
every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Scratch-clone commits (identity `scratch <scratch@invalid>`, inside $D only) are allowed so a gate can name a revision.
The frozen counter accepts REV and REPO: `HYAKU_SCRATCH={SCRATCH}/<seat> python3 -B {CTR} c1 <rev> "$D"` measures a candidate
commit of your scratch clone without touching the lane (also `r94c1`, the positive-control table). One counter run at a time per seat
(about 50 s each).
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR95 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR95 (lane L1)" heading — your files and headings carry YOUR seat name only.
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

## Frozen state (round 95, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Freeze commit (plan + v3 counter + control-world builder + six forgery patches +
pre-data receipts): {BASE}.
Read {LANE}/plans/round-95.md FULLY first, then the header of {CTR}. ONE claim, C1 (depth): the battery self-test
(verifiers/check_mutation_battery.py --self-test) kills the round-94 survivors N1 (manifest read at HEAD, not --rev), N5 (target-set
refusal labelled `arm kill-set-size:`) and N11 (pin accepts exactly two rows above it). Nobody edits the plan, the counter, the builder,
the forgery patches or any frozen predicate: an amendment is an L1 act via plans/round-95-addendum-*.md BEFORE any scored reading; a
counter defect you find is a FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {LANE}/.ufo/waves/round-95/receipts/ (redbefore-c1-base.txt UNMET, 0 of 3; poscontrol-r94c1-base.txt MET;
forgery-f1..f6-*.txt all UNMET; census-before.txt rc 0).
FROZEN ANCHORS: the counter's mutants substitute literal anchor text in verifiers/check_mutation_battery.py. These must stay
byte-identical and match exactly as often as declared: `committed = git_show(lane, rev, MANIFEST).decode("utf-8")` (1x),
`raise CouldNotEvaluate("manifest must name exactly the targets %s"` (1x), `return n == want, "observed` (1x),
`ok_pin, pin_detail = kill_set_check(committed, pinned)` (1x), `print("could-not-evaluate: %s" % exc)` (3x). Never add another
occurrence of an anchor; the mutated statements keep their line count.
ANTI-SNIFFING: a self-test arm must observe BEHAVIOUR (run the checker on a fixture world and read its exit code and output). The counter
runs every mutant source-blind (the file on disk holds honest bytes) and with comment and code decoys; reviewers refuse source readers.
A kill must be a REPORTED failure (a `FAIL ` line and `<N> failure(s)` with N >= 1, exit 1): an arm that crashes (uncaught exception) on a
mutant is a RUN-ERROR and does not count — every new assertion goes through the self-test's tally (`t.check`).
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
The L1 lands SCORECARD/LOG/QUALITY at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-9*/
(round-95 included), verifiers/fixtures/mutation-battery/manifest.tsv (KILL_SET_PINNED unchanged).
Mutation-battery coupling: verifiers/check_mutation_battery.py is itself a battery PROBES target (manifest rows anchor on its bytes) —
an edit there must keep every manifest anchor matching exactly once and the battery's own `--rev` run green (round-93
c1-killpin-rev.sh honest world, round-92 controls-run.sh).

## File ownership (one writer per production file; each builder writes only its own patch)
ExecBatteryKills owns verifiers/check_mutation_battery.py (self_test() section and helpers next to it only).
ScribeCorpusR95 owns corpus/SOURCES.md (APPEND one row S270 only), corpus/lessons/round-95.md (new), corpus/README.md (one index row
for the new lesson ONLY).
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
`0 failure(s) over N assertions`. Every new self-test assertion names the arm it guards. No network inside a counter or self-test;
rev-scoped reads go through `git show <rev>:<path>`.
"""


def item(role, name, body):
    return {"role": role, "name": name, "prompt": GOD + body}


items = [
item("executor", "ExecBatteryKills", f"""## ExecBatteryKills — C1 build: the battery self-test kills N1, N5, N11

Read {LANE}/plans/round-95.md § C1, the counter header and CLAIMS["c1"] in {CTR}, {LANE}/.ufo/waves/round-94/w1/MutTesterBattery94.md
(N1, N5, N11 survivor details), and {LANE}/verifiers/check_mutation_battery.py (evaluate(), kill_set_check(), main(), self_test(),
build_fixture(), run_evaluate(), run_main(), head()).
In YOUR scratch clone at {BASE}, change ONLY the self_test() section of verifiers/check_mutation_battery.py (fixture helpers it needs may be
added next to it); production behaviour of evaluate()/kill_set_check()/main() stays byte-identical. Add behavioural arms, each a `t.check`:
1. N1 (rev != HEAD): a fixture repo with TWO commits — the first satisfies the pin, the second (HEAD) drops a kill row (or the reverse).
   run_evaluate at the FIRST commit's full hash must read the committed manifest of that commit: the satisfying-at-rev world exits 0
   without naming kill-set-size, and the reverse world (rev drops a row, HEAD satisfies) exits 2 naming kill-set-size. Both directions.
2. N5 (target-set refusal label): a rev-path fixture whose committed manifest does not name exactly the targets (a target missing or an
   extra target) must exit 2 with "manifest must name exactly the targets" in the output and WITHOUT "kill-set-size".
3. N11 (added rows): kill_set_check refuses the live manifest with TWO (and three) extra kill rows appended, naming the observed count;
   optionally a rev-path fixture with two rows above the pin exits 2 naming kill-set-size.
Keep the FROZEN ANCHORS byte-identical; keep the module pin capture/restore. Verify, in your clone, with receipts under
{W1}/ExecBatteryKills/: `python3 -B verifiers/check_mutation_battery.py --self-test` → 0 failure(s); commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecBatteryKills python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET, and `... r94c1 <your commit> "$D"`
→ R94C1-PREDICATE-MET; `bash {LANE}/verifiers/fixtures/round-93/c1-killpin-rev.sh <your commit> "$D"` → C1-PREDICATE-MET (read its
header for arguments); round-92 controls-run.sh (read its header; run it against your candidate if it accepts a REPO/REV, else report how
you checked it). Patch {W1}/ExecBatteryKills/ExecBatteryKills.patch; report {W1}/ExecBatteryKills.md; then {W1}/ExecBatteryKills_READY."""),

item("executor", "ExecBaseBattery", f"""## ExecBaseBattery — base no-harm readings and the floors-timeout measurement (no patch)

At the freeze commit {BASE} (a scratch clone), run and capture under {W1}/ExecBaseBattery/ (command, rc, final lines, wall time,
`uptime` load at start and end): gate registry `python3 -B verifiers/check_gate_registry.py --rev {BASE}`; round-93
`verifiers/fixtures/round-93/c1-killpin-rev.sh` and `c2-pinkey.sh` (read headers for arguments); round-94
`python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 {BASE} "$D"` and `c2`; round-92 `controls-run.sh`;
`python3 -B verifiers/check_assertion_floors.py --self-test`; and the tip battery `python3 -B verifiers/check_tip_battery.py --rev {BASE}`
(read its header for --repo/--fleet arguments). Routed defect 5 (round-94 closure): the tip battery's floors gate hit its 280 s timeout under
fleet load. Measure the floors gate standalone at {BASE} with wall time, read check_assertion_floors.py and check_tip_battery.py for how the
gate timeout is derived (load scaling?), and report WHY it timed out and what the smallest robust change would be (do NOT edit any file —
recommendation only). Report {W1}/ExecBaseBattery.md (early, updated)."""),

item("executor", "ExecCounterForgery", f"""## ExecCounterForgery — attack the v3 counter with new forgery worlds (scratch only)

Read the header of {CTR} (rules 1-3 and the disclosed bound) and {FORGE} (the six pre-data control worlds; receipts
{LANE}/.ufo/waves/round-95/receipts/forgery-*.txt all UNMET). Build at least THREE NEW forgery worlds of
verifiers/check_mutation_battery.py at {BASE} in your scratch clone(s), each a self-test that tries to "kill" n1/n5/n11 WITHOUT
behavioural arms, e.g.: (a) a code-object sniffer (walk `sys.modules['__main__']` functions' `__code__.co_consts`/`co_names` for the
mutant constants, skipping nothing); (b) the same, but skipping constants reachable only under `__name__ == "__decoy__"` tests;
(c) a sniffer that compares its own source file bytes to its compiled code (detects the source-blind run by recompiling the file and
comparing co_code) and fails when they differ; (d) inspect/linecache-based sniffers; (e) a sniffer that reads the counter's temp file or
argv. Commit each in your scratch clone (scratch identity) and run `HYAKU_SCRATCH={SCRATCH}/ExecCounterForgery python3 -B {CTR} c1 <commit> "$D"`.
Report per world: the patch (save under {W1}/ExecCounterForgery/<world>.patch), the counter tally line, MET/UNMET, and which rule caught it.
A world that reads MET is a counter finding (severity, minimal fix recommendation) — never edit the counter. Report
{W1}/ExecCounterForgery.md (early, updated)."""),

item("scout", "ScoutSourcesR95", f"""## ScoutSourcesR95 — re-open C1's sources and two candidates to reject

The L1 opened https://docs.python.org/3/library/unittest.html (2026-11-05; HTTP 200, 336978 B, sha256
f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d) and https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/
(HTTP 200, 27068 B, sha256 8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da; already registry row S260). Re-open both
yourself (curl, save under {W1}/ScoutSourcesR95/), record HTTP code, size, sha256 and the HTML line numbers of: unittest
`TestResult.errors` ("Each tuple represents a test which raised an unexpected exception.") and `TestResult.failures` ("Each tuple
represents a test where a failure was explicitly signalled using the assert* methods."), and the Python version the page documents;
Stryker "Runtime error" ("The running of the tests resulted in an error (rather than a failed test).") and "Killed". Then open TWO more
candidates that define error-vs-failure or run-error-vs-kill (e.g. pytest's docs on outcomes/`--tb`, JUnit 5 / Surefire report
semantics, mutmut's status codes) and judge each against {LANE}/corpus/QUALITY.md and /home/vgpnk/Projects/shokunin/CORPUS.md (§ SOURCES.md
tiers): admit or reject with reason and flip condition; check the registry for an existing row on each URL (`grep -n` in
{LANE}/corpus/SOURCES.md). Write {W1}/ScoutSourcesR95.md: per URL, access date, HTTP, bytes, sha256, located quote ≤25 words with HTML line,
verdict + reason + flip condition. Early, updated; no repo writes."""),

item("scribe", "ScribeCorpusR95", f"""## ScribeCorpusR95 — SOURCES row S270 and the round-95 lesson scaffold

Read {LANE}/plans/round-95.md, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract), the last rows of {LANE}/corpus/SOURCES.md
(S266–S269 show the lane's 11-column shape), {LANE}/corpus/lessons/round-94.md (structure) and
{LANE}/corpus/lessons/round-94-verifier-spotcheck.md. Poll for {W1}/ScoutSourcesR95.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append ONE row S270 for https://docs.python.org/3/library/unittest.html (tier per CORPUS.md, kind
docs, scope = what separates a test error (unexpected exception) from a test failure (explicitly signalled) for a kill counter, anchor
`TestResult.errors` / `TestResult.failures` with HTML lines, status `mined`, opened 2026-11-05, recheck a valid cadence, used-by
`corpus/lessons/round-95.md,plans/round-95.md`, no `|` inside cells); (2) write corpus/lessons/round-95.md as a SCAFFOLD (author
ScribeCorpusR95) with `## Gate` (S270 admitted: URL, access date, HTTP, bytes, sha256, ≤25-word located quote and its word count; S260
re-opened as corroboration with its quote — no new row, and say why (the registry already holds the URL; round-94 closure defect 1); at
least one same-round REJECT from the scout's candidates with reason and flip condition), `## Mistakes` (one row: class
`run-error-scored-as-kill` · evidence {LANE}/.ufo/waves/round-94/w1/CriticClaimsR94.md D8 · captured-by `none` · fix: rule 1 of
verifiers/fixtures/round-95/selftest-kills.py, shown able to fail by {LANE}/.ufo/waves/round-95/receipts/forgery-f6-crash-report.txt
(`run errors 1`, UNMET)), `## Status changes` (old→new for every registry cell changed; append-only means none expected), `## Considerthese`
(re-read {LANE}/considerthese/ latest file; name which proposal is still unimplemented and why it is or is not taken this round), and
`## Settlement` (placeholder for the L1); (3) add ONE index row for the lesson to corpus/README.md, shaped like the round-94 row. Run
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 and no new W04 (receipt under
{W1}/ScribeCorpusR95/). Patch {W1}/ScribeCorpusR95/ScribeCorpusR95.patch; report {W1}/ScribeCorpusR95.md; then {W1}/ScribeCorpusR95_READY."""),

item("connector", "ConnectorOverlapR95", f"""## ConnectorOverlapR95 — overlap scan and planning data-walk (read-only)

Part 1: does any no-harm instrument pin a blob, line or assertion count of verifiers/check_mutation_battery.py such that adding self-test
arms changes its reading? Read the tip battery's INSTRUMENT_PINS/BATTERY, the floors registry (verifiers/floors-registry.json and
check_assertion_floors.py; is the battery floored?), the mutation-battery manifest anchors (verifiers/fixtures/mutation-battery/manifest.tsv
rows whose target is check_mutation_battery.py) and the gate registry in SKILL.md; name exact lines. Part 2 (siblings): grep the sibling
lanes under /home/vgpnk/Projects/shokunin/*-shokunin (read-only) for kill counters that separate run errors from kills, or run mutants
source-blind / with code decoys (`decoy`, `sniff`, `RUN-ERROR`, `run error`, `source-blind`, `selftest-kills`); report prior art or overlap
with kotoba's PROVINCE ({LANE}/PROVINCE.md). Part 3: list three candidate round-96 claims the round-95 evidence would support, preferring at
least one on real prompt/skill-craft work (SKILL.md / descriptions / dispatch prompts) rather than verifier internals. Write
{W1}/ConnectorOverlapR95.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerBatteryKills", f"""## ReviewerBatteryKills — review the C1 patch

Wait for {W1}/ExecBatteryKills_READY. Review {W1}/ExecBatteryKills/ExecBatteryKills.patch against plans/round-95.md § C1 and the context's
ANTI-SNIFFING and FROZEN ANCHORS rules: does each new arm observe behaviour (a fixture run's rc/output), never the checker's source?
Does it kill N1/N5/N11 for the stated reason (apply each mutant by hand in your candidate clone and name WHICH assertion fails, with its
FAIL line)? Is production code byte-identical outside self_test() and its helpers (`git diff` hunks)? Is the module pin restored on every
path? Are fixture git calls confined to fixture dirs (no identity leak, `-C` everywhere)? Run the frozen counter c1 and r94c1 on the
candidate. Blocking findings first. Write {W1}/ReviewerBatteryKills.md (early, updated)."""),

item("reviewer", "ReviewerCounterV3", f"""## ReviewerCounterV3 — review the frozen v3 counter and control receipts (read-only)

Review {CTR} and {FORGE} at {BASE} against plans/round-95.md: does classify() implement rule 1 exactly (REPORTED-FAILURE / CLEAN /
RUN-ERROR), and is a kill only REPORTED-FAILURE? Does code_decoy() insert each changed statement correctly (multi-anchor k2: three
statements), keep behaviour, and fail closed (NotEvaluated) on shapes it cannot handle? Does the source-blind runner really leave the
honest bytes on disk during a mutant run and restore the file on every path (exceptions, timeouts)? Can the honest run differ from a normal
`python3 -B verifiers/check_mutation_battery.py --self-test` run (e.g. `__spec__`, `sys.path[0]`, `__builtins__`, dataclass module lookup)?
Re-run, in your own scratch, the base reading, the r94c1 positive control and two forgery worlds (build with {FORGE}) and compare to the
committed receipts {LANE}/.ufo/waves/round-95/receipts/. Is the predicate sentence identical in the plan and the counter header? Blocking
findings first. Write {W1}/ReviewerCounterV3.md (early, updated)."""),

item("mutation-tester", "MutTesterBattery95", f"""## MutTesterBattery95 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecBatteryKills_READY. On the candidate ({BASE} + that patch) design at least 8 NEW mutants of the --rev manifest/pin path
of verifiers/check_mutation_battery.py that are NOT the frozen n1/n5/n11/n10 (e.g. `want + 3`, `n <= want + 2`, manifest read at
`rev + "^"`, target-set refusal message reworded, target-set check skipped, kill_set_check given the working-tree text only when dirty,
pinned argument ignored on the rev path, N4: the pin check moved after the probe loop). Apply each with the counter's method (literal
substitution, source-blind if you can reuse the counter's RUNNER) and classify KILLED (reported failure) / RUN-ERROR / SURVIVED. Also
re-run the round-94 survivor N4 and say whether it is observable at all. Write {W1}/MutTesterBattery95.md (early, updated) and receipts
under {W1}/MutTesterBattery95/."""),

item("mutation-tester", "MutTesterCounter95", f"""## MutTesterCounter95 — mutate the v3 counter itself (scratch copy only)

Copy {CTR} into your scratch dir (never edit the lane file). Design at least 6 mutants of the COUNTER (e.g. classify() returns
REPORTED-FAILURE on any rc != 0; the FAIL-line conjunct dropped; code decoys skipped; the source-blind runner writes the mutant to disk; the
honest-run CLEAN conjunct dropped; decoy HELD on rc 0 without the summary) and, for each, say which committed control receipt or world
would expose it: run the mutated counter against the base {BASE}, the r94c1 positive control and the six forgery worlds (build them with
{FORGE} into your scratch). A counter mutant that no control world exposes is a gap in the control battery — report it with the minimal new
control world that would. Write {W1}/MutTesterCounter95.md (early, updated) and receipts under {W1}/MutTesterCounter95/."""),

item("critic", "CriticClaimR95", f"""## CriticClaimR95 — falsify the frozen claim against the full candidate

Wait for {W1}/ExecBatteryKills_READY and {W1}/ScribeCorpusR95_READY. Build the full candidate ({BASE} + ExecBatteryKills.patch +
ScribeCorpusR95.patch). Run the frozen counter c1 and r94c1 on it; re-run the do-nothing control at {ROUND_BASE} and at least two forgery
worlds and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper change meet the target? Is C1 named by the surface it
changes (§9) — depth, or quality work mislabelled? Is S270 actually what the kill rule rests on (open the page; is unittest's
error/failure split a fair ground for a self-test that is not unittest-based)? Does the mined mistake's fix fail on its committed control?
Does the lesson Gate carry a real same-round reject? Is the round-94 closure's routed-defect list honestly dispositioned in the plan? Write
{W1}/CriticClaimR95.md (early, updated) with a MET/UNMET verdict on the candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR95", f"""## SentinelScopeR95 — scope, safety and no-harm on the candidate

Wait for {W1}/ExecBatteryKills_READY and {W1}/ScribeCorpusR95_READY (as CriticClaimR95). On the full candidate: (1) scope — `git diff --stat {BASE}`
lists only owned files; SKILL.md byte-identical; no spotcheck file, manifest.tsv, round-9x fixture or other verifier touched;
production code of check_mutation_battery.py outside self_test()/helpers byte-identical; (2) no-harm — gate registry
`python3 -B verifiers/check_gate_registry.py --rev <cand>` (base 74 of 74), round-93 c1-killpin-rev.sh and c2-pinkey.sh (MET), round-94
selftest-kills.py c1 and c2 (MET), `check_assertion_floors.py --self-test`, census `--file` on the candidate SOURCES.md (rc 0, W04 count
unchanged at 34); (3) safety — no hardcoded /tmp in new code, no network in self-tests, no credential-shaped strings, fixture git calls only
inside fixture tmpdirs with a fixture identity. Each check: command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR95.md (early, updated)."""),
]

spec = {
    "wave": "r95-w1",
    "milestone": "r95-w1: C1 battery self-test kills N1/N5/N11 under the v3 counter; S270; 5 attack seats + counter forgery probe",
    "reportDir": ".ufo/waves/round-95/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-95/r95-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
