#!/usr/bin/env python3
"""Generate the round-94 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "4d3e8e4d290d67ecf94a019059f434c71f399919"
W1 = f"{LANE}/.ufo/waves/round-94/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r94"
CTR = f"{LANE}/verifiers/fixtures/round-94/selftest-kills.py"
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
or /home/vgpnk/Projects/shokuknow (read-only: read it, never write, fetch or run a campaign tool there).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR and HYAKU_SCRATCH to it, pass it to any
--work argument, and delete it before you yield (`trap 'rm -rf -- "$S"' EXIT`). Copy the receipts you need under
{W1}/<your-seat-name>/ first. /tmp only for files under 50 MB. Never write under /tmp by a hardcoded path in any committed file.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch, pull, push,
branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh. Read-only git (log, show, diff,
status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
Your ONE writable repo is a scratch clone, created exactly as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D" && git -C "$D" checkout -q {BASE}`;
every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Scratch-clone commits (identity `scratch <scratch@invalid>`, inside $D only) are allowed so a gate can name a revision.
The frozen counter accepts REV and REPO: `python3 -B {CTR} c1 <rev> "$D"` (or `c2`) measures a candidate commit of your
scratch clone without touching the lane. Set HYAKU_SCRATCH={SCRATCH}/<your-seat-name> when you run it.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR94 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: kill only the PIDs you started; contention cap 4 processes; one counter run at a time per seat.
Attribution: never write under the lane identity or any "KotobaR94 (lane L1)" heading — your files and headings carry YOUR seat name only.
Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you and every seat may install or upgrade tools that help the task. Read /home/vgpnk/.omp/agent/RULES.md first
(official channels, update-safety gate). Record each install as tool, version, channel, reason in your final answer.
PACMAN IS PAUSED host-wide: no pacman transaction of any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official
binary in ~/.local/bin, or report the need. When the pause lifts the dry-run rule applies (`pacman -Sp --print-format '%n %v'`, only
packages not yet installed; never -Sy/-Syu/-U/-R, downgrade, or a host-service restart).
REPORT FILE FIRST (round-93 closure defect 4: a seat settled without its report file): write your report file
{W1}/<your-seat-name>.md (or the path your item names) BEFORE your final answer, and update it as you go so a cut-off seat
still leaves evidence. Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 94, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Freeze commit (plan + counter + forgery patch + pre-data receipts): {BASE}.
Read {LANE}/plans/round-94.md FULLY first, then the header of {CTR}. Nobody edits the plan, the counter
(verifiers/fixtures/round-94/selftest-kills.py), the forgery patch (verifiers/fixtures/round-94/forgery-sniff.patch) or any frozen
predicate: an amendment is an L1 act via plans/round-94-addendum-*.md BEFORE any scored reading; a counter defect you find is a
FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {LANE}/.ufo/waves/round-94/receipts/ (redbefore-c1-base.txt and redbefore-c2-base.txt read UNMET with 0 targets
killed; forgery-c1-run.txt and forgery-c2-run.txt read UNMET via the decoy guard; census-before.txt rc 0).
FROZEN ANCHORS: the counter's mutants substitute literal anchor text. These lines must stay byte-identical and match exactly as
often as declared: in verifiers/check_mutation_battery.py `ok_pin, pin_detail = kill_set_check(committed, pinned)` (1x),
`print("could-not-evaluate: %s" % exc)` (3x), `return n == want, "observed` (1x); in verifiers/check_tip_battery.py the two-line
block `        for path in scripts:` / `            if path not in INSTRUMENT_PINS:` (1x). Never add another occurrence of an anchor.
ANTI-SNIFFING: a self-test arm must observe BEHAVIOUR (run the checker on a fixture world and read its exit code and output). An arm
that reads the checker's own source text to detect a mutant is a forgery (the decoy guard refuses comment-reading sniffers; reviewers
refuse the rest).
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md.
The L1 lands SCORECARD/LOG at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-91/,
round-92/, round-93/ (except the one file ExecReceiptHeaders owns), verifiers/fixtures/mutation-battery/manifest.tsv (the kill set
stays 17; KILL_SET_PINNED stays 17).
Mutation-battery coupling: verifiers/check_mutation_battery.py is itself a battery PROBES target (manifest rows anchor on its bytes) —
an edit there must keep every manifest anchor matching exactly once and the battery's own `--rev` run green (round-93 c1-killpin-rev.sh
honest world rc 0).

## File ownership (one writer per production file; each builder writes only its own patch)
ExecBatterySelfTest owns verifiers/check_mutation_battery.py (C1).
ExecTipSelfTest owns verifiers/check_tip_battery.py (C2).
ExecReceiptHeaders owns verifiers/fixtures/round-93/check-receipt-revs.sh and new files under verifiers/fixtures/round-94/receipt-headers/
(the mined-mistake fix).
ScribeCorpusR94 owns corpus/SOURCES.md (APPEND rows only), corpus/lessons/round-94.md (new), corpus/README.md (one index row for the
new lesson ONLY) — no other change.
ScoutMutSources, ConnectorOverlapR94 and all attack/sentinel seats write NOTHING in any repo except their own receipts under {W1}/<their-seat-name>/
(and their report file).
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
`0 failure(s) over N assertions` (tip battery: `self-test: 0 failure(s) over N assertions`). Every new self-test assertion names the arm it
guards. No network inside a counter or self-test; rev-scoped reads go through `git show <rev>:<path>`.
"""


def item(role, name, body):
    return {"role": role, "name": name, "prompt": GOD + body}


items = [
item("executor", "ExecBatterySelfTest", f"""## ExecBatterySelfTest — C1 build: the battery self-test kills k1, k2, k3

Read {LANE}/plans/round-94.md § C1, the counter header and CLAIMS["c1"] in {CTR}, and {LANE}/verifiers/check_mutation_battery.py
(evaluate(), kill_set_check(), main(), self_test(), build_fixture(), run_evaluate(), run_main()). Round-93 evidence of the gaps:
{LANE}/.ufo/waves/round-93/w1/MutTesterKillPin.md (m3, m6, F2).
In YOUR scratch clone at {BASE}, change ONLY the self_test() section of verifiers/check_mutation_battery.py (helpers it needs may be added
next to it); production behaviour of evaluate()/kill_set_check()/main() stays unchanged. Add behavioural arms:
1. k1 (working-tree read): a fixture whose COMMITTED manifest matches the pin but whose WORKING-TREE manifest has one kill row dropped
   (uncommitted edit) — run_evaluate at the committed head must exit 0 and must not name kill-set-size (committed bytes govern).
2. k3 (added rows): kill_set_check on the live manifest text with one extra kill row appended must be refused; and a rev-path fixture
   whose committed manifest has one kill row more than the pin (rows that otherwise evaluate) must exit 2 naming kill-set-size.
3. k2 (label-every-CNE): at least one existing rc-2 arm whose cause is NOT the kill set (e.g. the G1 short-rev and G1 commit-check
   arms, which go through main()) additionally asserts "kill-set-size" not in its output; and one rc-2 run_evaluate path (e.g. the
   anchor-miss arm) likewise.
Keep the FROZEN ANCHORS byte-identical; keep the module pin capture/restore (A1 of round 93). Verify, in your clone, with receipts under
{W1}/ExecBatterySelfTest/: `python3 -B verifiers/check_mutation_battery.py --self-test` → 0 failure(s); commit in your clone and run
`HYAKU_SCRATCH={SCRATCH}/ExecBatterySelfTest python3 -B {CTR} c1 <your commit> "$D"` → C1-PREDICATE-MET with decoys held 3 of 3;
`bash {LANE}/verifiers/fixtures/round-93/c1-killpin-rev.sh <your commit> "$D"` → C1-PREDICATE-MET (round-93 no-harm);
`bash {LANE}/verifiers/fixtures/round-92/controls-run.sh` semantics: read that script's header; run it against your candidate if it accepts a
REPO/REV, else report how you checked it. Patch {W1}/ExecBatterySelfTest/ExecBatterySelfTest.patch; report {W1}/ExecBatterySelfTest.md;
then {W1}/ExecBatterySelfTest_READY."""),

item("executor", "ExecTipSelfTest", f"""## ExecTipSelfTest — C2 build: the tip self-test measures every BATTERY pin key

Read {LANE}/plans/round-94.md § C2, CLAIMS["c2"] in {CTR}, {LANE}/verifiers/check_tip_battery.py (run_guards() coverage block,
self_test(), the pin keydrop/keyswap arms near `missing = BATTERY[5][0]`), and {LANE}/.ufo/waves/round-93/w1/MutTesterPinCov/MutTesterPinCov.md.
In YOUR scratch clone at {BASE}, change ONLY self_test() of verifiers/check_tip_battery.py: parameterize the missing-key world over EVERY
BATTERY script (six keydrop worlds; keep the existing keyswap arm), each asserting exit 1, a `FAIL guard instrument-pin: <that path> has no
INSTRUMENT_PINS key` line naming exactly that path, and `guards 4 of 5`. Keep each world cheap (reuse fixture helpers). Keep the FROZEN
ANCHOR block byte-identical; production run_guards() unchanged.
Verify with receipts under {W1}/ExecTipSelfTest/: `python3 -B verifiers/check_tip_battery.py --self-test` → `self-test: 0 failure(s)`;
commit in your clone; `HYAKU_SCRATCH={SCRATCH}/ExecTipSelfTest python3 -B {CTR} c2 <your commit> "$D"` → C2-PREDICATE-MET, decoys held 2 of 2;
`bash {LANE}/verifiers/fixtures/round-93/c2-pinkey.sh <your commit> "$D"` → C2-PREDICATE-MET. Also hand-run the round-93 m5 world: drop only
the verifiers/check_gate_registry.py key and confirm the tip battery names it. Patch {W1}/ExecTipSelfTest/ExecTipSelfTest.patch;
report {W1}/ExecTipSelfTest.md; then {W1}/ExecTipSelfTest_READY."""),

item("executor", "ExecReceiptHeaders", f"""## ExecReceiptHeaders — mined-mistake fix: the receipt check fails closed on malformed headers

Read {LANE}/verifiers/fixtures/round-93/check-receipt-revs.sh and {LANE}/.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md (D2, D3)
and receipt-revs-probes.txt beside it. Defect: a header-shaped line whose hex run is not exactly 40 (e.g. `REV=` + 41 hex) is silently
dropped, and a header indented by spaces/tabs is ignored — both read as if no receipt claim were made.
In YOUR scratch clone at {BASE}, change check-receipt-revs.sh so that a line that is header-SHAPED after stripping leading whitespace
(`REV=`, `measured rev `, `rev ` followed by a hex run, or the G1 prefix) but is not a well-formed header (hex run length not 40 / 12 for
G1, or leading whitespace) is printed `MALFORMED <path>:<line> <reason>` and counted; exit 1 if any MALFORMED or UNRESOLVED. Scratch
declarations (`world rev`, `forgery`, `/scratch/`) keep exempting a line. Add committed fixtures under
verifiers/fixtures/round-94/receipt-headers/: `good/` (well-formed headers naming {ROUND_BASE} → rc 0), `hex41/` (REV= with 41 hex),
`indented/` (an indented REV= header naming {ROUND_BASE}). Receipts under {W1}/ExecReceiptHeaders/: BEFORE (the {BASE} script) on hex41/
and indented/ → rc 0 or 2 with no finding (the fail-open evidence); AFTER → rc 1 naming MALFORMED for each; good/ → rc 0 before and after;
{LANE}/.ufo/waves/round-93/receipts/landing → still `9 resolved, 0 unresolved`, rc 0; {LANE}/.ufo/waves/round-92/receipts/landing → still
rc 1 (5 unresolved). Patch {W1}/ExecReceiptHeaders/ExecReceiptHeaders.patch; report {W1}/ExecReceiptHeaders.md; then
{W1}/ExecReceiptHeaders_READY."""),

item("scout", "ScoutMutSources", f"""## ScoutMutSources — open the source C1/C2 rest on, and candidates to reject

The L1 opened https://pitest.org/quickstart/basic_concepts/ (2026-11-05; HTTP 200, 12155 B, sha256
c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a). Re-open it yourself (curl, save under {W1}/ScoutMutSources/), confirm
HTTP code, size, sha256, the HTML line number(s) of the sentences "Killed means a test caught the mutation successfully." and "Survived
means the mutation was not detected by the covering test." and of the non-viable and timed-out definitions, and any version/date pin on
the page. Then open TWO more candidates on mutation-outcome definitions (e.g. the mutmut docs, Stryker's mutant-states page, or the
Wikipedia "Mutation testing" article) and judge each for {LANE}/corpus/QUALITY.md (read it) and CORPUS.md tiers
(/home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md): which would you admit, which reject and why (tier, primacy, stability, quote
locatable). Check the registry for an existing row on each URL (`grep -n` in {LANE}/corpus/SOURCES.md). Write {W1}/ScoutMutSources.md
with: per candidate URL, access date, HTTP code, bytes, sha256, located quote ≤25 words with HTML line, verdict + reason + flip condition.
Write the file early and update it; no repo writes."""),

item("scribe", "ScribeCorpusR94", f"""## ScribeCorpusR94 — SOURCES row S269 and the round-94 lesson scaffold

Read {LANE}/plans/round-94.md, /home/vgpnk/Projects/shokunin/CORPUS.md § SOURCES.md (row contract), the last rows of {LANE}/corpus/SOURCES.md
(S265–S268 show the lane's 11-column shape and Gate conventions), {LANE}/corpus/lessons/round-93.md (structure) and
{LANE}/corpus/lessons/round-93-verifier-spotcheck.md. Poll for {W1}/ScoutMutSources.md (up to 45 min); use its verified facts.
In YOUR scratch clone at {BASE}: (1) append ONE row S269 for https://pitest.org/quickstart/basic_concepts/ (tier per CORPUS.md, status
`mined`, used-by `corpus/lessons/round-94.md,plans/round-94.md`, recheck a valid cadence, anchor with HTML line, no `|` inside cells);
(2) write corpus/lessons/round-94.md as a SCAFFOLD (author ScribeCorpusR94) with `## Gate` (S269 admitted with URL, access date, HTTP, bytes,
sha256, ≤25-word located quote and its word count; at least one same-round REJECT from the scout's candidates with reason and flip
condition), `## Mistakes` (one row: class `receipt-header-fail-open` · evidence {LANE}/.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md
D2/D3 · captured-by `none` · fix verifiers/fixtures/round-93/check-receipt-revs.sh MALFORMED rule, shown able to fail by
{W1}/ExecReceiptHeaders/ receipts — leave the numbers as `L1 fills at settlement` if not ready), `## Status changes` (old→new for every
cell you change; append-only means none expected), `## Considerthese` (re-read {LANE}/considerthese/, latest file; name which proposal
is still unimplemented and why it is or is not taken this round), and `## Settlement` (placeholder for the L1);
(3) add ONE index row for the lesson to corpus/README.md, shaped like the round-93 row. Run
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0 (receipt under {W1}/ScribeCorpusR94/).
Patch {W1}/ScribeCorpusR94/ScribeCorpusR94.patch; report {W1}/ScribeCorpusR94.md; then {W1}/ScribeCorpusR94_READY."""),

item("connector", "ConnectorOverlapR94", f"""## ConnectorOverlapR94 — overlap scan and planning data-walk (read-only)

Part 1 (cross-claim): confirm C1 and C2 are causally separable — C1's builder touches only check_mutation_battery.py, C2's only
check_tip_battery.py; does either instrument import or run the other? Does the tip battery or the floors guard (check_assertion_floors.py)
pin a blob or an assertion count of either file such that the C1/C2 edits change a no-harm reading? (read INSTRUMENT_PINS, BATTERY,
the floors registry; name exact lines). Part 2 (siblings): grep the sibling lanes under /home/vgpnk/Projects/shokunin/*-shokunin (read-only)
for a mutant-kill counter with a decoy or anti-sniffing guard (e.g. `decoy`, `sniff`, `mutant`, `KILLED`, `selftest-kills`); report any
prior art or overlap with kotoba's PROVINCE ({LANE}/PROVINCE.md). Part 3: list three candidate round-95 claims the round-94 evidence would
support (no freeze). Write {W1}/ConnectorOverlapR94.md (early, updated); no repo writes."""),

item("reviewer", "ReviewerBatterySelfTest", f"""## ReviewerBatterySelfTest — review the C1 patch

Wait for {W1}/ExecBatterySelfTest_READY. Review {W1}/ExecBatterySelfTest/ExecBatterySelfTest.patch against plans/round-94.md § C1 and the
context's ANTI-SNIFFING and FROZEN ANCHORS rules: does each new arm observe behaviour (a fixture run's rc/output), never the checker's
source? Does it kill k1/k2/k3 for the stated reason (apply each mutant by hand in your candidate clone and read WHICH assertion fails)?
Is production code unchanged? Is the module pin restored on every path? Are manifest anchors still matched once (run the round-93
c1-killpin-rev.sh honest world on the candidate)? Run the frozen counter c1 on the candidate. Blocking findings first. Write
{W1}/ReviewerBatterySelfTest.md (early, updated)."""),

item("reviewer", "ReviewerTipSelfTest", f"""## ReviewerTipSelfTest — review the C2 patch

Wait for {W1}/ExecTipSelfTest_READY. Review {W1}/ExecTipSelfTest/ExecTipSelfTest.patch against plans/round-94.md § C2, ANTI-SNIFFING and
FROZEN ANCHORS: does the parameterized keydrop arm cover all six BATTERY scripts with a behavioural world each; does each assertion name the
exact path; is production run_guards() unchanged; does the global INSTRUMENT_PINS get restored? Apply p1/p2 by hand and read which
assertions fail. Run the frozen counter c2 and round-93 c2-pinkey.sh on the candidate; time the self-test before/after (the floors guard
has a self-test time budget — read check_assertion_floors.py for the tip-battery entry and say whether the new runtime fits). Blocking
findings first. Write {W1}/ReviewerTipSelfTest.md (early, updated)."""),

item("mutation-tester", "MutTesterBattery94", f"""## MutTesterBattery94 — mutate beyond the frozen set (C1)

Wait for {W1}/ExecBatterySelfTest_READY. On the candidate ({BASE} + that patch) design at least 6 NEW mutants of the kill-set pin path of
verifiers/check_mutation_battery.py that are NOT the frozen k0–k3 (e.g. pin read from a different rev, off-by-one `n == want + 0` variants,
the check moved after the probe runs, a kill-set count that counts `equivalent` rows, CNE label only on the rev path, an AST-level change
the decoy guard cannot see). For each: exact diff, self-test result, frozen counter result if relevant, KILLED/SURVIVED. Also attack the
counter itself: can a self-test meet C1 without behavioural arms in a way the decoy guard misses? (write the forgery in scratch only and
run the counter on it; report, never commit). Write {W1}/MutTesterBattery94.md (early, updated) and receipts under {W1}/MutTesterBattery94/."""),

item("mutation-tester", "MutTesterTip94", f"""## MutTesterTip94 — mutate beyond the frozen set (C2) and the receipt-check fix

Wait for {W1}/ExecTipSelfTest_READY and {W1}/ExecReceiptHeaders_READY. (a) On {BASE} + ExecTipSelfTest.patch design at least 5 NEW mutants of the
key-coverage block of verifiers/check_tip_battery.py beyond p0–p2 (e.g. skip the middle key, coverage only when a key count threshold holds,
FAIL filed under another guard id, coverage over INSTRUMENT_PINS keys instead of BATTERY, path compared after normalisation). (b) On
{BASE} + ExecReceiptHeaders.patch design at least 4 mutants of the MALFORMED rule (e.g. 39-hex accepted, tab indentation ignored, MALFORMED
counted but exit 0, scratch exemption swallowing a malformed header) and check whether the committed fixtures under
verifiers/fixtures/round-94/receipt-headers/ kill each. For each: exact diff, result, KILLED/SURVIVED. Write {W1}/MutTesterTip94.md (early,
updated) and receipts under {W1}/MutTesterTip94/."""),

item("critic", "CriticClaimsR94", f"""## CriticClaimsR94 — falsify the frozen claims against the full candidate

Wait for the four READY files ({W1}/ExecBatterySelfTest_READY, ExecTipSelfTest_READY, ExecReceiptHeaders_READY, ScribeCorpusR94_READY).
Build the full candidate ({BASE} + all four patches; apply order: the three executors, then the scribe). Run the frozen counter c1 and c2 on
it; re-run the do-nothing control at {ROUND_BASE} and the forgery world (apply verifiers/fixtures/round-94/forgery-sniff.patch at {ROUND_BASE})
and confirm the pre-data receipts reproduce. Attack: does a do-nothing or cheaper change meet either target? Are the claims named by the
surface they change (§9)? Is C2 really consistency/calibration and C1 depth, or is one quality work mislabelled? Is S269 actually what
the counter's outcome classes rest on? Does the mined mistake's fix fail on its committed fixtures? Check the lesson Gate for a real
same-round reject. Write {W1}/CriticClaimsR94.md (early, updated) with verdicts MET/UNMET per claim on the candidate and defects D1..Dn."""),

item("sentinel", "SentinelScopeR94", f"""## SentinelScopeR94 — scope, safety and no-harm on the candidate

Wait for the four READY files (as CriticClaimsR94). On the full candidate: (1) scope — `git diff --stat {BASE}` lists only owned files;
SKILL.md byte-identical; no spotcheck file, manifest.tsv, round-91/92 fixture or other verifier touched; (2) no-harm — gate registry
`python3 -B verifiers/check_gate_registry.py --rev <cand>` (base 74 of 74), tip battery `--rev <cand> --repo "$D" --fleet
/home/vgpnk/Projects/shokunin` (base guards 5 of 5; 3 of 6 carried reds), `check_assertion_floors.py --self-test`, the round-93 counters
c1-killpin-rev.sh and c2-pinkey.sh (MET), census `--file` on the candidate SOURCES.md; (3) safety — no hardcoded /tmp in any new committed
code, no network in self-tests, no credential-shaped strings, no git writes outside a fixture tmpdir in the new arms. Each check: command,
observed line, PASS/FAIL. Write {W1}/SentinelScopeR94.md (early, updated)."""),
]

spec = {
    "wave": "r94-w1",
    "milestone": "r94-w1: C1 battery self-test kills k1-k3; C2 tip self-test covers six pin keys; receipt-header fail-closed fix; PIT row; 5 attack seats",
    "reportDir": ".ufo/waves/round-94/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-94/r94-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
