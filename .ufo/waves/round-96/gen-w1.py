#!/usr/bin/env python3
"""Generate the round-96 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "0f66016a3b35cf1e25c67caf8cf371996805cbb8"
W1 = f"{LANE}/.ufo/waves/round-96/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r96"
CTR = f"{LANE}/verifiers/fixtures/round-96/selftest-kills.py"
FORGE = f"{LANE}/verifiers/fixtures/round-96/build-forgeries.py"
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
commit of your scratch clone without touching the lane (also `r95c1`, the positive-control table, ~75 s). One counter run at a time per seat
(c1 about 5 s).
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR96 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes.
Attribution: never write under the lane identity or any "KotobaR96 (lane L1)" heading — your files and headings carry YOUR seat name only.
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


## Frozen state (round 96, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Freeze commit (plan + v4 counter + control-world builder + five forgery patches +
pre-data receipts): {BASE}.
Read {LANE}/plans/round-96.md FULLY first, then the header of {CTR}. ONE claim, C1 (depth): the dispatch-prompt checker's self-test
(verifiers/verify_dispatch_prompts.py --self-test) kills the eleven frozen survivors t01..t11 (CLAIMS["c1"] in the counter). Nobody edits the
plan, the counter, the builder, the forgery patches or any frozen predicate: an amendment is an L1 act via plans/round-96-addendum-*.md BEFORE
any scored reading; a counter defect you find is a FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {LANE}/.ufo/waves/round-96/receipts/ (redbefore-c1-base.txt UNMET, 0 of 11; poscontrol-r95c1-base.txt MET;
forgery-f1..f5-*.txt all UNMET; census-before.txt rc 0, 34 W04; base-box-proof.txt boxes proven 2; recon-sweep.txt; sources-opened.txt).
FROZEN ANCHORS: the counter's mutants substitute literal anchor text in verifiers/verify_dispatch_prompts.py; each must stay byte-identical
and match exactly once (see CLAIMS["c1"]; e.g. `if round_n <= value:`, `elif dirs != [round_n]:`, `wrong = [s for s in stems if s != lane]`,
`bad = [(r, s) for r, s in paths if`, `m = ROLE_ROUND_RE.search(lines[0])`, `stem = stem[:-3]`, the VARIABLE_RE line). Never add another
occurrence of an anchor text anywhere in the file (new self-test code included); the mutated statements keep their line count.
ANTI-SNIFFING: a self-test arm must observe BEHAVIOUR (call evaluate_dispatch_04/08, report_paths, role_round, has_placeholder,
state_source or _finish on fixture inputs and read the result). The counter runs every mutant source-blind (the file on disk holds honest
bytes) and with comment and code decoys; reviewers refuse source readers. A kill must be a REPORTED failure (a `self-test FAIL: ` line and
`<N> failure(s) over <M> assertions` with N >= 1, exit 1): an arm that crashes (uncaught exception) on a mutant is a RUN-ERROR and does not
count — every new assertion goes through the self-test's `rec(...)` tally.
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
The L1 lands SCORECARD/LOG/QUALITY at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-9*/
(round-96 included), verifiers/fixtures/dispatch-prompts/ (the committed box-proof corpus), verifiers/floors-registry.json.

## File ownership (one writer per production file; each builder writes only its own patch)
ExecArmsR96 owns verifiers/verify_dispatch_prompts.py (the self_test() function and self-test-only helpers/constants next to it ONLY;
everything from the module docstring through run_checks() and box_proof()/main() stays byte-identical).
ScribeCorpusR96 owns corpus/SOURCES.md (APPEND two rows S271, S272 only), corpus/lessons/round-96.md (new), corpus/README.md (one index
row for the new lesson ONLY).
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
item("executor", "ExecArmsR96", f"""## ExecArmsR96 — C1 build: the dispatch-prompt self-test kills t01..t11

Read {LANE}/plans/round-96.md § C1, the counter header and CLAIMS["c1"] in {CTR}, {LANE}/.ufo/waves/round-96/receipts/recon-sweep.txt,
and {LANE}/verifiers/verify_dispatch_prompts.py (has_placeholder, report_paths, role_round, state_source, _file_result,
evaluate_dispatch_04, evaluate_dispatch_08, _finish, SELF_TEST_PROMPT, _write_case, _verdict_of, self_test()).
In YOUR scratch clone at {BASE}, change ONLY self_test() and self-test-only helpers/fixture text next to it; production behaviour stays
byte-identical (git diff hunks only inside the self-test section). Add behavioural arms, each a `rec(...)` naming the arm, that FAIL on:
t01/t02/t03: a report path carrying `${{LANE}}` and one carrying bare `$LANE` (e.g. `/round-7/${{LANE}}.md`, `/round-7/$LANE.md`) must each
read report_path_literal FAIL (both forms separately: POSIX parameter expansion, braces optional);
t04: round 7 with latest dispatched baseline exactly 7 → round_le_latest_dispatched PASS (equality is allowed: `<=`);
t05: a prompts dir whose only in-scope file is N/A (e.g. missing state for dispatch.08, or no report path for dispatch.04) → the CHECK status
is N/A, never PASS, with evaluated 1;
t06: a prompt whose line 1 carries no `round <N>` token but a later line does → filename_role_round_equal FAIL;
t07: a prompt with two report paths, round-7 and round-6 dirs → filename_report_dir_round_equal FAIL;
t08: two report paths, the second with a `<lane>` placeholder → report_path_literal FAIL;
t09: two report paths whose stems are `kote` and a second stem that sorts AFTER `kote` (e.g. `other`) → report_stem_is_lane_id FAIL;
t10: a baseline file whose first field is non-integer (e.g. `abc`) → round_le_latest_dispatched N/A (not PASS);
t11: a prompt with no report path at all → every dispatch.04 conjunct N/A, file verdict N/A (not PASS).
Keep FROZEN ANCHORS byte-identical and unique (your new code must not contain any anchor text verbatim). Verify, in your clone, with receipts
under {W1}/ExecArmsR96/: `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → 0 failure(s); `--box-proof` → boxes proven 2, rc 0;
commit in your clone and run `HYAKU_SCRATCH={SCRATCH}/ExecArmsR96 python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET (all 11 KILLED,
no RUN-ERROR, decoys 11/11 held), and `... r95c1 <your commit> "$D"` → R95C1-PREDICATE-MET. Patch {W1}/ExecArmsR96/ExecArmsR96.patch;
report {W1}/ExecArmsR96.md; then {W1}/ExecArmsR96_READY."""),

item("executor", "ExecCounterForgeryR96", f"""## ExecCounterForgeryR96 — attack the v4 counter with new forgery worlds (scratch only; routed r95 defect 4)

Read the header of {CTR} (rules 1-3 and the disclosed bound) and {FORGE} (five pre-data control worlds; receipts
{LANE}/.ufo/waves/round-96/receipts/forgery-*.txt all UNMET). Build at least THREE NEW forgery worlds of verifiers/verify_dispatch_prompts.py
at {BASE} in your scratch clone(s), each a self-test that tries to "kill" t01..t11 WITHOUT behavioural arms, e.g.: (g1) a code-object
sniffer (walk the module's functions' `__code__.co_consts`/`co_names` for the mutants' constants/names); (g2) the same but skipping code
reachable only under `__name__ == "__decoy__"`; (g3) recompile-compare: recompile its own on-disk source and compare co_code/consts with the
running functions, failing when they differ (detects the source-blind run); (g4) inspect/linecache sniffers; (g5) argv/temp-file sniffers;
(g6) an arm that kills only by crashing with SystemExit(1) after printing a fake `self-test FAIL:` line but no summary. Commit each in your
scratch clone (scratch identity) and run `HYAKU_SCRATCH={SCRATCH}/ExecCounterForgeryR96 python3 -B {CTR} c1 <commit> "$D"`. Report per world:
patch (save under {W1}/ExecCounterForgeryR96/<world>.patch), the counter tally line, MET/UNMET, which rule caught it. A world that reads MET
is a counter finding (severity, minimal fix recommendation) — never edit the counter. Report {W1}/ExecCounterForgeryR96.md (early, updated)."""),

item("scout", "ScoutSourcesR96", f"""## ScoutSourcesR96 — re-open C1's two sources and two candidates to reject

The L1 opened (receipts {LANE}/.ufo/waves/round-96/receipts/sources-opened.txt, 2026-11-06) https://pitest.org/quickstart/mutators/
(HTTP 200, 67033 B, sha256 a31331daf89f246f3e02c0da92578d4ad2163c53741c3700437e75b9a1602da2) and
https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html (HTTP 200, 357953 B, sha256
0889867a53fe12508a71e8739ec23ecdddc95e6f67697c98e26acc8ff0ec1acd). Re-open both yourself (curl, save under {W1}/ScoutSourcesR96/), record
HTTP code, size, sha256 (say whether it equals the L1's) and the HTML line numbers of: PIT "The conditionals boundary mutator replaces the
relational operators <, <=, >, >= with their boundary counterpart" and the `<=` → `<` row of its table; POSIX 2.6.2 "The parameter name or
symbol can be enclosed in braces, which are optional except for positional parameters with more than one digit". Then open TWO more
candidates that could ground the same mutant classes (e.g. the GNU Bash manual Shell Parameter Expansion page, mutmut or Stryker
"Equality operator" mutator docs) and judge each against {LANE}/corpus/QUALITY.md and /home/vgpnk/Projects/shokunin/CORPUS.md (§ SOURCES.md
tiers): admit or reject with reason and flip condition; check the registry for an existing row on each URL (`grep -n` in
{LANE}/corpus/SOURCES.md). Write {W1}/ScoutSourcesR96.md: per URL, access date, HTTP, bytes, sha256, located quote ≤25 words with HTML line,
verdict + reason + flip condition. Early, updated; no repo writes."""),

item("scribe", "ScribeCorpusR96", f"""## ScribeCorpusR96 — SOURCES rows S271, S272 and the round-96 lesson scaffold

Read {LANE}/plans/round-96.md, {LANE}/.ufo/waves/round-96/receipts/sources-opened.txt, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md
(row contract), the last rows of {LANE}/corpus/SOURCES.md (S266–S270 show the lane's 11-column shape), {LANE}/corpus/lessons/round-95.md
(structure) and {LANE}/corpus/lessons/round-95-verifier-spotcheck.md. Poll for {W1}/ScoutSourcesR96.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append TWO rows: S271 https://pitest.org/quickstart/mutators/ (PIT "Mutation operators"; scope: the
documented boundary-mutation class a kill counter's relational mutant belongs to; anchor § Conditionals Boundary Mutator with HTML lines) and
S272 https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html (POSIX.1-2024 XCU 2.6.2 Parameter Expansion; scope: which
textual forms are unsubstituted shell variables a literal report path must not carry); tier per CORPUS.md, kind spec/docs, status `mined`,
opened 2026-11-06, recheck a valid cadence, used-by `corpus/lessons/round-96.md,plans/round-96.md`, no `|` inside cells (rewrite `<, <=`
lists without pipes); (2) write corpus/lessons/round-96.md as a SCAFFOLD (author ScribeCorpusR96) with `## Gate` (S271 and S272 admitted:
URL, access date, HTTP, bytes, sha256, ≤25-word located quote and word count; at least one same-round REJECT from the scout's candidates with
reason and flip condition; and an AMENDMENT of the round-95 Ant reject reason per round-95 closure routed defect 1: the Ant page keeps
`haltonerror`/`errorproperty` separate and merges errors into failures only under `haltonfailure`; the reject stands on "no definition of
an error" — append, do not edit round-95.md), `## Mistakes` (one row: class `decoy-builder-cuts-elif-chain` · evidence
{LANE}/.ufo/waves/round-96/receipts/predraft-elif-decoy.txt · captured-by: the counter's compile guard (could-not-evaluate, fail-closed) ·
fix: v4 rule 2 in verifiers/fixtures/round-96/selftest-kills.py, shown able to fail as plans/round-96.md § Frontier step says), `## Status
changes` (old→new for every registry cell changed; append-only means none expected), `## Considerthese` (re-read {LANE}/considerthese/
latest file; name which proposal is still unimplemented and why it is or is not taken this round), and `## Settlement` (placeholder for the
L1); (3) add ONE index row for the lesson to corpus/README.md, shaped like the round-95 row. Run
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 and no new W04 (receipt under
{W1}/ScribeCorpusR96/). Patch {W1}/ScribeCorpusR96/ScribeCorpusR96.patch; report {W1}/ScribeCorpusR96.md; then {W1}/ScribeCorpusR96_READY."""),

item("connector", "ConnectorOverlapR96", f"""## ConnectorOverlapR96 — overlap scan and planning data-walk (read-only)

Part 1: does any no-harm instrument pin a blob, sha, line or assertion count of verifiers/verify_dispatch_prompts.py such that adding self-test
arms changes its reading? Read verifiers/check_tip_battery.py, verifiers/check_assertion_floors.py + verifiers/floors-registry.json (floor 56:
minimum or exact?), verifiers/check_gate_registry.py and SKILL.md § Gate registry, verifiers/box_proof_case_deletion.py, the mutation-battery
manifest (verifiers/fixtures/mutation-battery/manifest.tsv), verifiers/checklist-baseline.json; name exact lines. Part 2 (siblings): grep the
sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin (read-only) for dispatch-prompt checkers or kill counters on prompt instruments
(`dispatch.04`, `report-baseline`, `selftest-kills`, `source-blind`); report prior art or overlap with kotoba's PROVINCE ({LANE}/PROVINCE.md).
Part 3: list three candidate round-97 claims the round-96 evidence supports (the recon sweep's other survivors in
{LANE}/.ufo/waves/round-96/receipts/recon-sweep.txt; SKILL.md prompt/skill craft; the considerthese 2026-10-26 proposals), each with a
falsifiable before→after and a do-nothing control. Write {W1}/ConnectorOverlapR96.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerArmsR96", f"""## ReviewerArmsR96 — review the C1 patch

Wait for {W1}/ExecArmsR96_READY. Review {W1}/ExecArmsR96/ExecArmsR96.patch against plans/round-96.md § C1 and the context's ANTI-SNIFFING and
FROZEN ANCHORS rules: does each new arm observe behaviour (a function call's result on a fixture input), never the checker's source? Does it
kill t01..t11 for the stated reason (apply each mutant by hand in your candidate clone and name WHICH assertion fails, with its
`self-test FAIL:` line)? Is production code byte-identical outside self_test() and its self-test helpers (`git diff` hunks)? Do the fixtures
stay under TMPDIR and get cleaned? Run the frozen counter c1 and r95c1 and `--box-proof` on the candidate. Blocking findings first. Write
{W1}/ReviewerArmsR96.md (early, updated)."""),

item("reviewer", "ReviewerCounterV4", f"""## ReviewerCounterV4 — review the frozen v4 counter and control receipts (read-only)

Review {CTR} and {FORGE} at {BASE} against plans/round-96.md: `diff` the v4 counter against the v3 counter
{LANE}/verifiers/fixtures/round-95/selftest-kills.py — are the changes exactly the three the plan names (claim-table instrument + failure
prefix; elif-chain climb in code_decoy; decoy marker/scratch), and do the r95c1 anchors equal the round-95 c1 anchors byte-for-byte? Is the
elif climb behaviour-neutral and fail-closed (an `else:` arm? a chain of three elifs? a mutant changing two arms)? Does classify() with the
`self-test FAIL: ` prefix classify every committed receipt line correctly? Can the honest run differ from a normal
`python3 -B verifiers/verify_dispatch_prompts.py --self-test` run (`__file__`-relative SKILL.md lookup, sys.path[0])? Re-run, in your own
scratch, the base reading, the r95c1 positive control and two forgery worlds (build with {FORGE}) and compare to the committed receipts. Is
the predicate sentence identical in the plan and the counter header? Blocking findings first. Write {W1}/ReviewerCounterV4.md (early, updated)."""),

item("mutation-tester", "MutTesterDispatchR96", f"""## MutTesterDispatchR96 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecArmsR96_READY. On the candidate ({BASE} + that patch) design at least 10 NEW mutants of verifiers/verify_dispatch_prompts.py's
evaluation path that are NOT t01..t11/p00 (start from the recon survivors in {LANE}/.ufo/waves/round-96/receipts/recon-sweep.txt that are not
frozen — rstrip of sentence-final `.`, empty baseline read as a bound, fleet-root stem PASS, fleet-root via .report-baseline dropped,
PLACEHOLDER_RE `+` vs `*`, is_dir vs exists — and add your own: report-path regex, role-line regex, the `.`/`..` stem skip, out-of-scope
reasons, _file_result precedence, evaluated counts). Apply each with the counter's method (literal substitution, source-blind if you reuse the
counter's RUNNER) and classify KILLED (reported failure) / RUN-ERROR / SURVIVED, at the base AND on the candidate. Name equivalent mutants with
the reason. Write {W1}/MutTesterDispatchR96.md (early, updated) and receipts under {W1}/MutTesterDispatchR96/."""),

item("mutation-tester", "MutTesterCounterV4", f"""## MutTesterCounterV4 — mutate the v4 counter itself (scratch copy only; routed r95 defect 2)

Copy {CTR} into your scratch dir (never edit the lane file). Port the round-95 counter mutants (see
{LANE}/.ufo/waves/round-95/w1/MutTesterCounter95.md: M1 classify on rc != 0, M2 failure-line conjunct dropped, M3/M4 decoys skipped, M5 the
source-blind runner writes the mutant to disk, M6 honest-CLEAN conjunct dropped, M7 decoy HELD on rc 0 without a summary, M8 positive forced
killed) and add v4-specific ones (M9 the failure prefix ignored or set to the r95 `FAIL `; M10 the elif climb removed; M11 the claim's
instrument path swapped). For each, run the mutated counter against the base {BASE} (c1), the r95c1 positive control (only where relevant —
it takes ~75 s) and the five forgery worlds (build them with {FORGE} into your scratch). Report a matrix: which committed control receipt or
world exposes each counter mutant (verdict flip or tally deviation vs the committed receipt). A counter mutant no control exposes is a gap —
report it with the minimal new control world that would. Write {W1}/MutTesterCounterV4.md (early, updated) and receipts under
{W1}/MutTesterCounterV4/."""),

item("critic", "CriticClaimR96", f"""## CriticClaimR96 — falsify the frozen claim against the full candidate

Wait for {W1}/ExecArmsR96_READY and {W1}/ScribeCorpusR96_READY. Build the full candidate ({BASE} + ExecArmsR96.patch + ScribeCorpusR96.patch).
Run the frozen counter c1 and r95c1 on it; re-run the do-nothing control at {ROUND_BASE} and at least two forgery worlds and confirm the pre-data
receipts reproduce. Attack: does a do-nothing or cheaper change meet the target? Is C1 named by the surface it changes (§9) — depth, or quality
work mislabelled? Are the eleven targets real false greens / false reds of the dispatch boxes (read SKILL.md § Dispatch-prompt fidelity checklist
dispatch.04/.08) or contrived? Do S271/S272 actually ground t04 and t01-t03 (open the pages)? Does the mined mistake's fix fail on its committed
control? Does the lesson Gate carry a real same-round reject? Is the round-95 closure's routed-defect list honestly dispositioned in the plan?
Write {W1}/CriticClaimR96.md (early, updated) with a MET/UNMET verdict on the candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR96", f"""## SentinelScopeR96 — scope, safety and no-harm on the candidate

Wait for {W1}/ExecArmsR96_READY and {W1}/ScribeCorpusR96_READY (as CriticClaimR96). On the full candidate: (1) scope — `git diff --stat {BASE}`
lists only owned files; SKILL.md byte-identical; no spotcheck file, dispatch-prompts fixture, round-9x fixture or other verifier touched;
production code of verify_dispatch_prompts.py outside self_test()/helpers byte-identical; (2) no-harm — gate registry
`python3 -B verifiers/check_gate_registry.py --rev <cand>` (base 74 of 74), round-95 `selftest-kills.py c1|r94c1 <cand> "$D"` (MET),
`check_assertion_floors.py --self-test`, `verify_dispatch_prompts.py --box-proof` (boxes proven 2) and its live run over
/home/vgpnk/Projects/shokunin/.ufo/prompts (same verdict lines at {BASE} and the candidate — production unchanged), census `--file` on the
candidate SOURCES.md (rc 0, W04 count unchanged at 34); (3) safety — no hardcoded /tmp in new code, no network in self-tests, no
credential-shaped strings, fixtures only under TMPDIR. Each check: command, observed line, PASS/FAIL. Write {W1}/SentinelScopeR96.md (early, updated)."""),
]

spec = {
    "wave": "r96-w1",
    "milestone": "r96-w1: C1 dispatch-prompt self-test kills t01..t11 under the v4 counter; S271/S272; 5 attack seats + counter forgery probe",
    "reportDir": ".ufo/waves/round-96/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-96/r96-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
