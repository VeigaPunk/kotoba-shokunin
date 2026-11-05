#!/usr/bin/env python3
"""Generate the round-93 kotoba wave spec (one v1 wave, band 8-16). Run after the freeze commit lands."""
import json, subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
ROUND_BASE = "5549fa9ed3cd91aeb0349178b5ba75dfe41711e7"
W1 = f"{LANE}/.ufo/waves/round-93/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r93"
# §3: every L2 prompt leads with /skill:godspeed followed by the host binding's verbatim directive bytes
# (round-92 closure defect 3: the lead line was missing).
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
The frozen counters accept a second argument REPO: `bash <lane>/verifiers/fixtures/round-93/c1-killpin-rev.sh <rev> "$D"` measures
a candidate commit of your scratch clone without touching the lane.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR93 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: Kill only by the PIDs you started; contention cap (4 processes, 120 s per probe; the frozen counters run longer —
one counter run at a time per seat).
Attribution: never write under the lane identity or any "KotobaR93 (lane L1)" heading — your files and headings carry YOUR seat name only.
Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you and every seat may install or upgrade tools that help the task. Read /home/vgpnk/.omp/agent/RULES.md first
(official channels, update-safety gate). Record each install as tool, version, channel, reason in your final answer.
PACMAN IS PAUSED host-wide: no pacman transaction of any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official
binary in ~/.local/bin, or report the need. When the pause lifts the dry-run rule applies (`pacman -Sp --print-format '%n %v'`, only
packages not yet installed; never -Sy/-Syu/-U/-R, downgrade, or a host-service restart).
Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 93, Linux host, omp)
Round base (lane tip at round start): {ROUND_BASE}. Freeze commit (plan + counters + forgery controls + pre-data receipts): {BASE}.
Read {LANE}/plans/round-93.md FULLY first. Nobody edits the plan, the counters (verifiers/fixtures/round-93/c1-killpin-rev.sh,
c2-pinkey.sh), the forgery patches or any frozen predicate: an amendment is an L1 act via plans/round-93-addendum-*.md BEFORE any
scored reading; a counter defect you find is a FINDING in your answer — never rescue a counter by changing its predicate.
Pre-data receipts: {LANE}/.ufo/waves/round-93/receipts/ (redbefore-c1-base.txt, redbefore-c2-base.txt, forgery-c1-run.txt,
forgery-c2-run.txt, census-before.txt).
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md
(the tip battery's spotcheck-identity guard pins them). The L1 lands SCORECARD/LOG/PROVINCE at integration.
FROZEN instruments you must not edit: every verifiers/*.py not named in your item's file ownership, verifiers/fixtures/round-91/,
verifiers/fixtures/round-92/, verifiers/fixtures/mutation-battery/manifest.tsv (the kill set stays 17; KILL_SET_PINNED stays 17).
Mutation-battery coupling (round-92 lesson, A1): verifiers/check_mutation_battery.py is itself a battery PROBES target (rows
mb-m2-g1-commit-check-skipped, mb-m15-clean-tree-guard-off, mb-m16-restore-unverified anchor on its bytes) — an edit there must keep
every manifest anchor matching exactly once and the bat-self-test baseline at exit 0.

## File ownership (one writer per production file; each builder writes only its own patch)
ExecKillPinRev owns verifiers/check_mutation_battery.py (the C1 build).
ExecPinCoverage owns verifiers/check_tip_battery.py (the C2 build).
ExecReceiptRevs owns verifiers/fixtures/round-93/check-receipt-revs.sh (new; the mined-mistake fix).
ScribeCorpusR93 owns corpus/SOURCES.md (APPEND rows only), corpus/lessons/round-93.md (new), corpus/README.md (one index row for
the new lesson ONLY) — no other change.
ScoutGitRevs, ConnectorOverlapR93 and all attack/sentinel seats write NOTHING in any repo except their own receipts under {W1}/<their-seat-name>/.
Build seats write their patch under {W1}/<seat>/<seat>.patch and then the READY file {W1}/<seat>_READY.

## Patch and handoff protocol (builders)
Each builder: edit only in its scratch clone $D; `git -C "$D" add -A -- <owned files>`; `git -C "$D" diff --cached --binary {BASE} > {W1}/<seat>/<seat>.patch`;
prove the patch applies on a second fresh scratch clone at {BASE} (`git apply --check`), then remove that clone. Only after the patch
and its receipts exist, write the READY file (content: the patch sha256 and one line saying what it does). A builder that cannot land
its claim writes an EMPTY patch and a READY file naming the honest-stop reason.

## Attack and sentinel handoff (candidate build)
The candidate is {BASE} plus the builder patches named in your item. Build it in your own scratch clone (`git apply` each patch,
then `git -C "$D" commit` with the scratch identity) so a gate can name the candidate revision; pass "$D" as the counters' REPO.
Attack seats never write a patch into the lane.

## Poll and wait rules
Poll every 120 s with `sleep 120`, up to 75 minutes, for the READY files named in your item; if one never appears, report on what
exists and say so. Never write a READY file that another seat owns.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR and accept a scratch/--work argument; exit ladder 0 pass, 1 content fail, 2 could-not-evaluate;
`--self-test` prints `0 failure(s) over N assertions`. Every self-test assertion names the arm it guards. No network inside a counter;
rev-scoped reads go through `git show <rev>:<path>`.
"""


def item(role, name, body):
    return {"role": role, "name": name, "prompt": GOD + body}


items = [
item("executor", "ExecKillPinRev", f"""## ExecKillPinRev — C1 build: the --rev path names kill-set-size

Read {LANE}/plans/round-93.md § C1 and {LANE}/verifiers/check_mutation_battery.py (evaluate(), kill_set_check(), self_test()).
In YOUR scratch clone at {BASE}, change ONLY verifiers/check_mutation_battery.py:
1. In evaluate(), right after `rows = parse_manifest(...)` and the existing target-set check (so the round-92 C1 shortcut world,
   which appends a kill row with no probe set, is still refused by its existing `could-not-evaluate: manifest mb-c1-shortcut-kill:`
   line), run kill_set_check() on the COMMITTED manifest text (the bytes of `git show <rev>:<manifest>`) and, on a mismatch, raise
   CouldNotEvaluate with a message that names the arm, e.g. `arm kill-set-size: manifest at <rev12> has 16 kill rows, pinned 17`.
   No other could-not-evaluate path may mention kill-set-size.
2. Add self-test arm(s) (named `kill-set-size rev path ...`) that build a fixture whose COMMITTED manifest drops a kill row and assert
   rc 2 with the arm named; and an arm that an unrelated baseline failure does NOT name kill-set-size. Reuse build_fixture/_git_fixture.
   Note the self-test fixtures' manifests are not the lane manifest: drive the new check through a parameter or by monkeypatching
   KILL_SET_PINNED inside the arm only — never change the module-level pin value (17).
3. Keep the round-92 manifest anchors: `grep` each `anchor` regex of the mb-* rows in verifiers/fixtures/mutation-battery/manifest.tsv
   against your edited file; each must still match exactly once.
Evidence (record rc + last lines in {W1}/ExecKillPinRev/ExecKillPinRev.md): `python3 -B verifiers/check_mutation_battery.py --self-test`
(0 failures, N > 28); commit your candidate in the scratch clone and run the frozen counter
`HYAKU_SCRATCH={SCRATCH}/ExecKillPinRev bash {LANE}/verifiers/fixtures/round-93/c1-killpin-rev.sh <candidate rev> "$D"` (expect
C1-PREDICATE-MET); run `bash verifiers/fixtures/round-92/controls-run.sh` from your clone at the candidate (expect
`shortcuts refused 2 of 2; honest held 2 of 2`; note it reads the clone's HEAD). Then write the patch and {W1}/ExecKillPinRev_READY."""),

item("executor", "ExecPinCoverage", f"""## ExecPinCoverage — C2 build: a missing battery pin key is a named instrument-pin failure

Read {LANE}/plans/round-93.md § C2 and {LANE}/verifiers/check_tip_battery.py (INSTRUMENT_PINS, BATTERY, run_guards(), self_test()).
In YOUR scratch clone at {BASE}, change ONLY verifiers/check_tip_battery.py:
1. In run_guards(), when INSTRUMENT_PINS is non-empty (the self-test's empty dict means "no pin"), every script path of the frozen
   BATTERY tuple that is not a key of INSTRUMENT_PINS appends a failure under the EXISTING guard id `instrument-pin` with a detail
   that names the path, e.g. `verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key (battery instrument unpinned)`.
   Do not add a guard id (the frozen tally reads `guards N of 5`). Do not change any existing pin tuple or BATTERY.
2. Add self-test arm(s) that set INSTRUMENT_PINS to a dict missing one BATTERY path (and one with that path swapped for a junk key)
   and assert the instrument-pin FAIL line names the missing path; keep every existing arm green.
Evidence (in {W1}/ExecPinCoverage/ExecPinCoverage.md): `python3 -B verifiers/check_tip_battery.py --self-test` (0 failures, N above the
base count — record base N too); commit your candidate in the scratch clone and run the frozen counter
`HYAKU_SCRATCH={SCRATCH}/ExecPinCoverage bash {LANE}/verifiers/fixtures/round-93/c2-pinkey.sh <candidate rev> "$D"` (expect
C2-PREDICATE-MET); run `bash verifiers/fixtures/round-92/ctl-c2-honest.sh` from your clone at the candidate (expect C2-PREDICATE-MET).
Then write the patch and {W1}/ExecPinCoverage_READY."""),

item("executor", "ExecReceiptRevs", f"""## ExecReceiptRevs — mined-mistake fix: receipt revisions must resolve

Round-92 closure defect 1 ({LANE}/corpus/lessons/round-92-verifier-spotcheck.md § Step-1 conformance, defect 1): landing receipts
named `cd355c4796fa165ff2b7d822401b4027da29e4d0`, a scratch revision that never resolved in the lane. Write ONE new file
verifiers/fixtures/round-93/check-receipt-revs.sh (bash, set -u, read-only): usage `check-receipt-revs.sh <receipts-dir> [REPO]`
(REPO default: the lane). It extracts every full 40-hex token from lines of the form `REV=<hex>`, `measured rev <hex>`,
`G1 revision identity PASS: rev <hex12>` (12-hex prefix: resolve via `git rev-parse --verify -q <prefix>^{{commit}}`), and `rev <hex>`
at line start, in every regular file under the dir; checks each with `git -C REPO cat-file -e <hex>^{{commit}}`; prints one
`UNRESOLVED <hex> <file>:<line>` per miss and a final line `receipt revisions: R resolved, U unresolved over F files`; exit 0 iff U == 0
and R >= 1, 1 if U > 0, 2 if R + U == 0 (nothing to check) or the dir is missing. Lines whose text says `world rev`, `scratch`
or `forgery` are scratch-world revisions by declaration and are counted separately as `S scratch-declared` (never as resolved).
Show it able to fail: run it on {LANE}/.ufo/waves/round-92/receipts/landing (expect exit 1 naming cd355c47…) and on
{LANE}/.ufo/waves/round-93/receipts (record what it reads); also on a scratch dir holding one fabricated `REV=` line (exit 1) and one
holding only a real lane commit (exit 0). Record all four in {W1}/ExecReceiptRevs/ExecReceiptRevs.md. Patch = the new file only;
then {W1}/ExecReceiptRevs_READY."""),

item("scout", "ScoutGitRevs", f"""## ScoutGitRevs — open the source C1 rests on, and one candidate to reject

Read-only. Open these this round (curl -sSL, record HTTP status, byte size, access date 2026-11-05, and for each claim a located
quote of at most 25 words with its line number in the fetched HTML or text):
1. https://git-scm.com/docs/gitrevisions — the `<rev>:<path>` syntax (the battery reads the committed manifest through
   `git show <rev>:<path>`): quote the sentence that says it names the blob/tree at the path in the tree-ish.
2. https://git-scm.com/docs/git-cat-file — `-e` (exit status 0 iff the object exists and is valid) — grounds the receipt-revision check.
3. Find ONE plausible but weaker candidate on the same topic (e.g. a Stack Overflow answer or a blog post about `git show rev:path`)
   and judge it against {LANE}/corpus/QUALITY.md and {LANE}/corpus/SOURCES.md's tier rules — it should be a reject (tertiary,
   undated, or not primary) unless it is genuinely primary; give the reason and the flip condition.
Check {LANE}/corpus/SOURCES.md for an existing row with the same URL (grep) and say so (a duplicate URL must be a correction row or
refused). Save fetched bytes' sha256 and the quotes to {W1}/ScoutGitRevs/ScoutGitRevs.md (do not commit raw HTML larger than 200 KB;
record sha256 instead). Message agent://KotobaR93 nothing; the scribe reads your file."""),

item("scribe", "ScribeCorpusR93", f"""## ScribeCorpusR93 — SOURCES rows and the round-93 lesson

Wait for {W1}/ScoutGitRevs/ScoutGitRevs.md (poll 120 s). Then, in YOUR scratch clone at {BASE}:
1. Append to corpus/SOURCES.md registry table the admitted row(s) (gitrevisions; git-cat-file if admitted) in EXACTLY the schema of
   the last rows (S265/S266 — 11 columns, no literal or escaped `|` inside a cell, status `mined`, used-by naming
   corpus/lessons/round-93.md and for gitrevisions also plans/round-93.md). Ids continue the registry (next after the current max S-id;
   re-derive it with `grep -oE '^ {{0,3}}\\|[[:space:]]*S[0-9]{{3,}}' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort -V | tail -1`).
   Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <your clone>/corpus/SOURCES.md` → exit 0 required.
2. Write corpus/lessons/round-93.md in the shape of corpus/lessons/round-92.md: header (author ScribeCorpusR93, scaffold — the L1
   completes settlement), `## Gate` (each admitted row with URL, access date, ≤25-word located quote and line; the scout's REJECTED
   candidate with reason and flip condition — round-92 closure defect 5 asks for a same-round reject), `## Mistakes` with the row:
   class `receipt-identity` · evidence `corpus/lessons/round-92-verifier-spotcheck.md` defect 1 (receipts named scratch rev
   cd355c4796fa…, `.ufo/waves/round-92/receipts/landing/landing-rev.txt`) · captured-by `none` · fix
   `verifiers/fixtures/round-93/check-receipt-revs.sh` (shown failing on the round-92 landing receipts — the L1 fills the observed
   line); `## Status changes` (old→new for every row touched); `## Considerthese` (re-read {LANE}/considerthese/ newest file and
   say which proposal is carried, implementing none); `## Settlement` with the line
   "Round-92 cross-reference: the round-92 lesson's 'Non-author spot-check: pending' is answered by
   corpus/lessons/round-92-verifier-spotcheck.md (closure of round 92); round-92 lesson bytes are not rewritten." and
   "L1 settlement: pending (KotobaR93)".
3. corpus/README.md: one index row for lessons/round-93.md, matching the round-92 row's form.
Patch = those three files; write {W1}/ScribeCorpusR93/ScribeCorpusR93.patch and {W1}/ScribeCorpusR93_READY."""),

item("connector", "ConnectorOverlapR93", f"""## ConnectorOverlapR93 — cross-claim overlap, sibling copies, name uniqueness (read-only)

(1) Shared surfaces: C1 (verifiers/check_mutation_battery.py) vs C2 (verifiers/check_tip_battery.py) vs the round-92 controls
(verifiers/fixtures/round-92/*.sh, which run BOTH instruments) vs the mined-mistake check. Name every place where one claim's change
could flip another's reading, with file:line (e.g. ctl-c1-manifest-only-v2.sh greps `could-not-evaluate: manifest mb-c1-shortcut-kill:`
— does C1's new check fire before it?; ctl-c2-honest.sh greps `guard instrument-pin PASS`; the battery's PROBES target BAT).
(2) Sibling copies: grep sibling lane repos under /home/vgpnk/Projects/shokunin/*-shokunin (read-only) for `INSTRUMENT_PINS`,
`KILL_SET_PINNED`, `kill-set-size`, `check_tip_battery` — name any hit path:line and whether the same silent-key-drop class applies.
(3) Seat-name uniqueness: check live sibling wave dirs /home/vgpnk/Projects/shokunin/*-shokunin/.ufo/waves/ for seats named
ExecKillPinRev, ExecPinCoverage, ExecReceiptRevs, ScoutGitRevs, ScribeCorpusR93, ConnectorOverlapR93, ReviewerKillPin,
ReviewerPinCov, MutTesterKillPin, MutTesterPinCov, CriticClaimsR93, SentinelScopeR93 — a reuse by a concurrent sibling is a finding.
Write {W1}/ConnectorOverlapR93/ConnectorOverlapR93.md with O1..On (file:line each) and the uniqueness verdict."""),

item("reviewer", "ReviewerKillPin", f"""## ReviewerKillPin — review the C1 patch

Wait for {W1}/ExecKillPinRev_READY. Review {W1}/ExecKillPinRev/ExecKillPinRev.patch against plans/round-93.md § C1: correctness of the
committed-manifest read (bytes from `git show <rev>:<manifest>`, not the working tree), placement after the target-set check, that NO
other could-not-evaluate path names kill-set-size, that KILL_SET_PINNED stays 17, the self-test arms really fail on the defect
(re-run them with the new check deleted in your scratch clone: the arms must fail), and every mb-* manifest anchor still matches exactly
once. Build the candidate and run the frozen counter yourself (REPO = your clone). Write {W1}/ReviewerKillPin/ReviewerKillPin.md with
numbered findings (blocking / non-blocking), each with the command and observed output."""),

item("reviewer", "ReviewerPinCov", f"""## ReviewerPinCov — review the C2 patch

Wait for {W1}/ExecPinCoverage_READY. Review {W1}/ExecPinCoverage/ExecPinCoverage.patch against plans/round-93.md § C2: the coverage
set is exactly the frozen BATTERY paths; the empty-dict (self-test) path is unchanged; failures land under `instrument-pin` (guard count
stays 5); no pin tuple changed; the new self-test arms fail when the coverage check is removed (prove it in your scratch clone). Build
the candidate and run the frozen counter `c2-pinkey.sh <cand rev> "$D"` and `python3 -B verifiers/check_tip_battery.py --rev <cand rev>`
(record the guard lines and the last line). Write {W1}/ReviewerPinCov/ReviewerPinCov.md, numbered findings with commands + outputs."""),

item("mutation-tester", "MutTesterKillPin", f"""## MutTesterKillPin — mutate the C1 change; does the frozen counter or the self-test kill each mutant?

Wait for {W1}/ExecKillPinRev_READY. Build the candidate in your scratch clone. Apply each mutant in turn (commit each in scratch, run the
frozen counter `c1-killpin-rev.sh <mutant rev> "$D"` and `--self-test`), restoring between mutants:
(m1) the new check deleted; (m2) comparison `!=` → `<` (only drops refused); (m3) check reads the WORKING-TREE manifest instead of
`git show <rev>:` bytes; (m4) the arm name dropped from the message; (m5) check moved BEFORE the target-set check (does round-92
controls-run.sh still read 2 of 2? run it); (m6) every CouldNotEvaluate message prefixed `kill-set-size` (the forgery shape).
Also an added-kill-row world (18 rows, all with probe targets) — is it refused naming the arm? Report per mutant: diff, counter line,
self-test line, killed/survived. Write {W1}/MutTesterKillPin/MutTesterKillPin.md."""),

item("mutation-tester", "MutTesterPinCov", f"""## MutTesterPinCov — mutate the C2 change

Wait for {W1}/ExecPinCoverage_READY. Build the candidate; apply each mutant in turn (working-tree edit is enough: the counter runs the
clone's checker; commit in scratch so the counter can name the rev), run `c2-pinkey.sh <rev> "$D"` and `--self-test`:
(m1) coverage check deleted; (m2) coverage compares key COUNT not key SET; (m3) coverage only when len(INSTRUMENT_PINS) >= 7;
(m4) failure filed under a new guard id (tally becomes N of 6); (m5) coverage set hardcoded to check_correction_sweep.py only (does
dropping verifiers/check_gate_registry.py's key slip through? build that world by hand and run the tip battery);
(m6) the empty-dict exemption removed (does --self-test break?). Report per mutant killed/survived with the observed lines. Write
{W1}/MutTesterPinCov/MutTesterPinCov.md."""),

item("critic", "CriticClaimsR93", f"""## CriticClaimsR93 — falsify the frozen claims against the full candidate

Wait for {W1}/ExecKillPinRev_READY, {W1}/ExecPinCoverage_READY, {W1}/ExecReceiptRevs_READY and {W1}/ScribeCorpusR93_READY. Build the
candidate ({BASE} + every builder patch) and commit it in scratch. Read plans/round-93.md first. Then, rc + stdout recorded:
1. C1 and C2 frozen counters on the candidate (REPO = your clone) — MET/UNMET exactly as frozen.
2. Do-nothing control (§9): read receipts/redbefore-c1-base.txt and redbefore-c2-base.txt; re-run ONE of them at {BASE} yourself and
   confirm UNMET. Forgery controls: confirm forgery-c1-run.txt / forgery-c2-run.txt read UNMET and that each patch is the shape named.
3. Clause audit (Q26): every clause of each predicate sentence is turned on by its counter's code — name any clause the counter does
   not check, or a world that passes for the wrong reason (e.g. the C1 other world failing for an unrelated cause).
4. No-harm: round-92 controls-run.sh (2 of 2 / 2 of 2), the two --self-tests, gate registry `--rev <cand>` (74 of 74), census validate on
   the candidate's SOURCES.md (exit 0) and its row count before→after.
5. The mined-mistake check: does check-receipt-revs.sh fail on .ufo/waves/round-92/receipts/landing and could it false-green (e.g. a
   short-prefix collision, a REV= line with trailing text)?
Write {W1}/CriticClaimsR93/CriticClaimsR93.md — per claim MET/UNMET with evidence, numbered defects with command + output."""),

item("sentinel", "SentinelScopeR93", f"""## SentinelScopeR93 — scope and safety of the candidate

Wait for the four builder READY files under {W1}/ (ExecKillPinRev, ExecPinCoverage, ExecReceiptRevs, ScribeCorpusR93). Check and record:
(a) patch scope: the union of builder patches touches ONLY verifiers/check_mutation_battery.py, verifiers/check_tip_battery.py,
    verifiers/fixtures/round-93/check-receipt-revs.sh, corpus/SOURCES.md (appends only — verify no existing line changed),
    corpus/lessons/round-93.md, corpus/README.md (one added row) — anything else is a violation;
(b) no seat wrote outside {W1}/ and its own scratch dir: `find {LANE}/.ufo/waves/round-93 -newer {LANE}/plans/round-93.md -type f`
    reviewed; `git -C /home/vgpnk/Projects/shokunin status --porcelain` read for untracked files naming kotoba round 93;
(c) no sysctl write, pacman call, credential material or raw env dump in any seat receipt (grep the wave tree);
(d) scratch discipline: no hardcoded /tmp in patched bytes (`grep -n '/tmp/'`), clones under {SCRATCH}/<seat>/;
(e) SKILL.md, verifiers/fixtures/round-92/, the manifest, and every corpus/lessons/round-*-verifier-spotcheck.md byte-identical at the
    candidate vs {BASE}.
Write {W1}/SentinelScopeR93/SentinelScopeR93.md with findings S1..Sn."""),
]

spec = {
    "wave": "r93-w1",
    "milestone": "r93-w1: C1 battery --rev kill-set-size naming; C2 tip-battery pin-key coverage; receipt-rev check; gitrevisions row; 5 attack seats",
    "reportDir": ".ufo/waves/round-93/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-93/r93-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
