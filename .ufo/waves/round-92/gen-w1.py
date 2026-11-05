#!/usr/bin/env python3
"""Generate the round-92 kotoba wave spec (one v1 wave, band 8-16). Run from the lane repo."""
import json, subprocess, sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = subprocess.run(["git", "-C", LANE, "rev-parse", "master"], capture_output=True, text=True).stdout.strip()
W1 = f"{LANE}/.ufo/waves/round-92/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r92"
GOD = """You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim — let the frontier walk itself.**

"""

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only), .ufo/state/, .ufo/watchdog.log, MANIFEST.json, scripts/, templates/,
or /home/vgpnk/Projects/shokuknow (read-only: read it, never write, fetch or run a campaign tool there).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR to it, pass it to any
--work argument, and delete it before you yield (`trap 'rm -rf -- "$S"' EXIT`). Copy the receipts you need under
{W1}/<your-seat-name>/ first. /tmp only for files under 50 MB. Never write under /tmp by a hardcoded path in any committed file.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch, pull, push,
branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh. Read-only git (log, show, diff,
status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
Your ONE writable repo is a scratch clone, created exactly as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D" && git -C "$D" checkout -q {BASE}`;
every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Scratch-clone commits (identity `scratch <scratch@invalid>`, inside $D only) are allowed so a gate can name a revision.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named in your item.
Message only agent://KotobaR92 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0 and broke
every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: Kill only by the PIDs you started; contention cap (4 processes, 120 s per probe).
Attribution: never write under the lane identity or any "KotobaR92 (lane L1)" heading — your files and headings carry YOUR seat name only.
Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you may install or upgrade tools that help the task. Read /home/vgpnk/.omp/agent/RULES.md first
(official channels, update-safety gate). Record each install as tool, version, channel, reason in your final answer.
PACMAN IS PAUSED host-wide: no pacman transaction of any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official
binary in ~/.local/bin, or report the need.
Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 92, Linux host, omp)
Round base (freeze commit, lane tip at round start): {BASE}.
Plan + pre-data controls FROZEN in commit {BASE}: {LANE}/plans/round-92.md and {LANE}/plans/round-92-controls.md.
Read plans/round-92.md FULLY first. Nobody edits the plan, the controls, or any frozen predicate: an amendment is an L1 act
via plans/round-92-addendum-*.md BEFORE any scored reading; a counter defect you find is a FINDING in your answer — never
rescue a counter by changing its predicate.
Pre-data controls held: `freeze gate: 6 control(s) held — freeze may proceed` (receipt {LANE}/.ufo/waves/round-92/receipts/freeze-gate-r92.txt).
Base receipts: {LANE}/.ufo/waves/round-92/receipts/ (redbefore-*.txt, base-*.txt, census-before.txt, q73-sweep-raw.txt).
PATCH BASE: every patch you write is `git diff --binary {BASE}` from YOUR scratch clone — the freeze commit is the base, not an older tip.
Skill budget: SKILL.md is 600/600 lines — no seat edits SKILL.md, and no seat edits any corpus/lessons/round-*-verifier-spotcheck.md
(the tip battery's spotcheck-identity guard pins them). The L1 lands registry rows and SCORECARD/LOG/PROVINCE at integration.
FROZEN instruments you must not edit: verifiers/check_r86_routed_repairs_v3.py, verifiers/verify_corpus_integrity.py,
verifiers/corpus-baseline.json, verifiers/check_gate_registry.py, verifiers/verify_skill_checklist.py, verifiers/fixtures/round-91/
(byte-identical — the red-before evidence), and every verifiers/*.py not named in your item's file ownership.

## File ownership (one writer per production file; each builder writes only its own patch)
ExecCtlWorlds owns verifiers/fixtures/round-92/ (new; the C1 build).
ExecKillPin owns verifiers/check_mutation_battery.py (the C2(a) build).
ExecLadderR92 owns verifiers/check_freeze_gate.py, verifiers/floors-registry.json (freeze_gate floor ONLY),
verifiers/check_assertion_floors.py (the two in-file freeze_gate floor cells ONLY), and verifiers/check_tip_battery.py
(INSTRUMENT_PINS appends ONLY) (the C2(b) build + coupling).
ScribeCorpusR92 owns corpus/SOURCES.md (APPEND S265 and S266 only), corpus/lessons/round-92.md (new),
corpus/README.md (index rows for the new corpus files ONLY), corpus/QUALITY.md (ONE appended criterion row) — no other change.
ScoutPyDocs, ConnectorOverlapR92 and all attack/sentinel seats write NOTHING in any repo except their own receipts under {W1}/<their-seat-name>/.
Build seats write their patch and READY file under {W1}/<seat>/ and {W1}/<seat>_READY.

## Patch and handoff protocol (builders)
Each builder: edit only in its scratch clone $D; `git -C "$D" add -A -- <owned files>`; `git -C "$D" diff --cached --binary {BASE} > {W1}/<seat>/<seat>.patch`;
prove the patch applies: `git clone -q --shared {LANE} "$D2" && git -C "$D2" checkout -q {BASE} && git -C "$D2" apply --check {W1}/<seat>/<seat>.patch`
(then remove $D2). Only after the patch and its receipts exist, write the READY file named in the item (content as the item says).
A builder that cannot land its claim writes an EMPTY patch and a READY file whose content names the honest-stop reason.

## Attack and sentinel handoff (candidate build)
The candidate is {BASE} plus the builder patches named in your item. Attackers build it in their own scratch clone:
`git clone -q --shared {LANE} "$D"`, `git -C "$D" checkout -q {BASE}`, `git -C "$D" apply` each patch named in your item,
`git -C "$D" commit` (scratch identity) so a gate can name the candidate revision. Attack seats never write a patch into the lane.

## Poll and wait rules
Poll every 120 s with `sleep 120`, up to 60 minutes, for the READY files named in your item; if one never appears, report on what
exists and say so. Never write a READY file that another seat owns.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR and accept a scratch/--work argument; exit ladder 0 pass, 1 content fail, 2 could-not-evaluate
(3 = invalid spec where the plan declares it); `--self-test` prints `0 failure(s) over N assertions`. Every self-test assertion names the
arm it guards. No network inside a counter; no writes outside named paths; rev-scoped reads go through `git show <rev>:<path>`,
never a second working tree inside the lane."""

def item(role, name, text):
    return {"role": role, "name": name, "prompt": GOD + text}

items = [
item("executor", "ExecCtlWorlds", f"""## ExecCtlWorlds — C1 build: the two shortcut worlds and two honest worlds, through the public path

Build claim C1 of plans/round-92.md § C1 in YOUR scratch clone, nothing else. You own verifiers/fixtures/round-92/ (new).
Write exactly five executable scripts (bash, set -u, honour HYAKU_SCRATCH default /fast/scratch/hyaku, scratch root
{SCRATCH}/ExecCtlWorlds/ inside your own scripts, trap-cleanup, receipts printed to stdout):
1. ctl-c2-capline-only-v2.sh — builds a COMMITTED cap-only shortcut world in scratch: clone at {BASE}, set
   verifiers/check_assertion_floors.py SELF_TEST_TIMEOUT_S to a value ≥ 320, add NO INSTRUMENT_PINS admission and no
   measured-duration constant, `git add -A -- verifiers/ && git commit` (scratch identity), then run the PUBLIC gates over those
   committed bytes in that clone: `python3 -B verifiers/check_tip_battery.py --rev <worldrev>` must FAIL its instrument-pin guard
   naming the unpinned blob. Print `C2-SHORTCUT-REFUSED: instrument-pin admission missing (<the guard's finding line>)`, exit 1.
2. ctl-c2-honest.sh — at the revision given by $1 (default: the lane master tip bytes you cloned at start): assert via the public
   gates that the committed bytes carry cap ≥ 2× the measured-duration constant AND the INSTRUMENT_PINS admission for the floors
   blob at that rev AND the tip battery pin guard PASS. Print `C2-PREDICATE-MET`, exit 0.
3. ctl-c1-manifest-only-v2.sh — builds the manifest-only shortcut world COMMITTED: clone at {BASE}, append one extra `kill`
   manifest row (shape like verifiers/fixtures/round-91/ctl-c1-manifest-only.sh does, but the rows are never the point — the
   battery has no probe for them), `git commit`, then run the battery over that committed rev with --work in scratch:
   `python3 -B verifiers/check_mutation_battery.py --rev <worldrev> --work <scratch>` must read could-not-evaluate (exit 2) naming
   the rows/probe gap. Print `C1-SHORTCUT-REFUSED: rows committed and read; instrument cannot evaluate (rc 2)`, exit 1.
4. ctl-c1-honest.sh — at $1 (default lane master tip): run the battery at that rev; it must print its predicate line and exit 0.
   Print `C1-PREDICATE-MET`, exit 0. (If the tip battery run is long, run it once and reuse the receipt.)
5. controls-run.sh — the frozen counting command: runs the four scripts in order, captures rc and stdout; prints exactly
   `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` and exits 0 iff both refused worlds exited 1 with their named
   conjunct AND both honest worlds exited 0; any other combination prints the observed per-script line and exits 1.
Constraints: no script edits the lane (all worlds in scratch clones); verifiers/fixtures/round-91/ stays byte-identical; every
committed file passes `bash -n`. Receipts: {W1}/ExecCtlWorlds/probe.txt with each script's stdout/rc run once from your clone.
Patch: {W1}/ExecCtlWorlds/ExecCtlWorlds.patch (git diff --cached --binary {BASE} over verifiers/fixtures/round-92/). READY file:
{W1}/ExecCtlWorlds_READY containing `CTL-WORLDS-READY <sha of your scratch commit>` only after the apply-check passes."""),

item("executor", "ExecKillPin", f"""## ExecKillPin — C2(a) build: pin the battery's kill-set size in its self-test

Build claim C2 leg (a) of plans/round-92.md in YOUR scratch clone, nothing else. You own verifiers/check_mutation_battery.py.
Read the file first: the self-test builds fixture worlds (FX_*); G1 reads the measured revision's committed manifest via git show.
Add ONE self-test arm named `kill-set-size`: the number of `\\tkill\\t` rows the battery derives from the measured revision's
committed manifest (the same read path G1 uses) must equal a pinned constant; the constant is derived at load from the measured
rev's manifest bytes, so a manifest whose kill-row count differs from what the arms expect fails the self-test with
`FAIL arm kill-set-size ...` naming observed vs pinned. Design constraint: the arm must fire on the round-92 red-before world
(receipts/redbefore-m6-dropped-row.txt: one kill row removed, self-test stayed `0 failure(s) over 25 assertions`, rc 0) and must
stay green on the honest bytes. Do not change the battery's predicate line format, the manifest, PROBES, or any existing arm's
semantics; the self-test moves 25 → N (N ≥ 26) and still exits 0 on honest bytes.
Able-to-fail receipts under {W1}/ExecKillPin/: (1) honest `--self-test` → `0 failure(s) over N assertions`, rc 0;
(2) dropped-row world (same procedure as verifiers/fixtures/round-92-predata/rp-m6-dropped-row.sh, in YOUR scratch) →
self-test exits 1 with `FAIL arm kill-set-size`; (3) `--rev` with a manifest missing entirely → could-not-evaluate, not a crash.
Patch: {W1}/ExecKillPin/ExecKillPin.patch. READY: {W1}/ExecKillPin_READY containing `KILLPIN-READY N=<assertion count>`."""),

item("executor", "ExecLadderR92", f"""## ExecLadderR92 — C2(b) build: three fail-closed rungs in the freeze gate + the coupling

Build claim C2 leg (b) of plans/round-92.md in YOUR scratch clone. You own verifiers/check_freeze_gate.py, plus the coupling
edits: verifiers/floors-registry.json (freeze_gate floor value ONLY), verifiers/check_assertion_floors.py (the two in-file
freeze_gate floor cells ONLY — EXPECTED_INSTRUMENTS and INSTRUMENTS), verifiers/check_tip_battery.py (INSTRUMENT_PINS appends
ONLY). The three rungs, from plans/round-92.md § C2(b) (red-before receipts redbefore-ladder-*.txt):
1. `--work` under a regular file (`<file>/sub`) or naming an existing regular file: read could-not-evaluate (exit 2) with
   `COULD-NOT-EVALUATE --work <path>: not a directory` (or the FileExistsError twin: same rung, named) — never a traceback.
2. two `control <same-name>` entries → invalid spec (exit 3) naming the duplicate control and line; parse-time, before any run.
3. a declared `exit 126` or `exit 127` expectation → invalid spec (exit 3) naming the unobservable rung (the harness's own
   could-not-evaluate codes); parse-time. A control that RUNS and exits 126/127 still reads could-not-evaluate (unchanged).
Add one named self-test arm per rung (parse-duplicate, unobservable-rung, work-root) to check_freeze_gate.py's --self-test:
31 → N' (N' ≥ 34), exit 0. Honest worlds stay green: verifiers/fixtures/round-92-predata/fp-minimal.md reads held and
verifiers/fixtures/freeze-gate/r88-controls.md exits 0 — run both on your candidate and keep the receipts.
Coupling: floors-registry.json freeze_gate floor and the two in-file cells move 31 → N' together (A1 coupling; the floors
self-test's registry-drift arm enforces equality). INSTRUMENT_PINS in check_tip_battery.py: append the admission for every
floors-registry-listed instrument blob your patch changes (round-91 landing mistake class — named in the plan's touch list);
verify `python3 -B verifiers/check_tip_battery.py --rev <candrev>` still reads `guards 5 of 5` with rc 1 only from the three
carried red corpus gates (base receipt base-tipbattery.txt).
Able-to-fail receipts under {W1}/ExecLadderR92/: the three probe scripts verifiers/fixtures/round-92-predata/rp-*.sh run
against your CANDIDATE clone (rp-work rc 2 named; rp-dup rc 3 named; rp-127 rc 3 named) plus honest worlds + self-tests +
tip battery line. Patch: {W1}/ExecLadderR92/ExecLadderR92.patch. READY: {W1}/ExecLadderR92_READY containing
`LADDER-READY N'=<count>`."""),

item("scout", "ScoutPyDocs", """## ScoutPyDocs — open two Python documentation pages; record located quotes (read-only)

Read-only scout. Open, with the read tool, two sources and record located quotes. Do not write any corpus file: ScribeCorpusR92
drafts the rows.
(1) S266 candidate — the Python exception reference, NotADirectoryError: read
https://docs.python.org/3/library/exceptions.html and locate the NotADirectoryError entry and its hierarchy line (OSError
subclass). Record: HTTP status, byte size, page title, the entry's heading line number, and TWO located quotes ≤ 25 words each
with their exact line numbers — one stating what NotADirectoryError is raised for (a directory argument that is not a
directory / a path component that is not a directory), one locating it in the OSError hierarchy. Also note whether the page
names which os functions raise it.
(2) S263 anchor repair — re-open https://docs.python.org/3/library/subprocess.html (opened in round 91; the round-91
verifier spot-check routed defect 4 says the Popen.communicate contrast quote sits at HTML line 1071 with the entry dt at 1051,
while the row cites 1042). Record today's HTTP status, byte size, footer "Last updated on" line number and text, the
subprocess.run timeout paragraph line numbers (round 91 cited 289-291), the Popen.communicate section start line, and the exact
line of the contrast quote "The child process is not killed if the timeout expires".
Write everything to /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/w1/ScoutPyDocs/ScoutPyDocs.md
(status, sizes, titles, quotes with line numbers, paste the raw lines with `sed -n '<L>p'` output verbatim), then write
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/w1/SOURCE_READY containing `SOURCE-READY`. If a page is
unreachable, record the error and still write SOURCE_READY with `SOURCE-READY partial` — the scribe refuses the row instead."""),

item("scribe", "ScribeCorpusR92", f"""## ScribeCorpusR92 — draft the round-92 corpus delta in your scratch clone

Wait for {W1}/SOURCE_READY (poll 120 s, up to 45 minutes). Then read
{W1}/ScoutPyDocs/ScoutPyDocs.md — do NOT re-open the URLs unless the receipt is missing.
In YOUR scratch clone (base {BASE}), write exactly these changes:
1. corpus/SOURCES.md — APPEND exactly two rows (11 columns, no `|` inside any cell, ids continue the registry: read the last
   id in the table first; the plan expects S265 and S266 — if the last id differs, use the next unused ids and note it):
   a correction row whose teaches opens `supersedes S263 — ` (the S263 anchor repair: same URL, tier A, same scope as S263
   minus the wrong line anchor; teaches carries the corrected anchor line numbers from the scout receipt; status `mined`;
   opened today's date 2026-11-05; used-by `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md`;
   recheck `180d`), and the NotADirectoryError row (URL, kind `docs`, tier A scoped to *which exception the Python runtime
   raises when a path component is not a directory — grounding the freeze gate's fail-closed work-root rung*; teaches from the
   scout's located quote; status `mined`; used-by `corpus/lessons/round-92.md`; recheck `180d`).
2. corpus/lessons/round-92.md (new) — the lesson scaffold with: header (author ScribeCorpusR92, round 92, plan
   plans/round-92.md frozen at {BASE}, base {BASE}); `## Gate` with the two source candidates' access records (URL, access
   date, HTTP status, byte size, located quotes ≤ 25 words with line numbers — from the scout receipt), the admit/reject
   decisions with reasons, and the census before→after line (190 → 192 expected, counting command included; plan § Frontier);
   `## Mistakes` with the vacuous-control row (class · evidence .ufo/waves/round-91/w1/CriticClaims.md § Controls +
   verifiers/fixtures/round-91/ctl-c2-capline-only.sh · captured-by Q37's gap: a control need not refuse its own shortcut ·
   fix = plans/round-92.md C1) marked as the L1-confirmed row, plus a placeholder section the L1 completes at settlement;
   `## Status changes` (S263 corrected-by-S265 note); `## Sources` (the two rows, full records); `## Considerthese` line
   (2026-10-26.md re-read, nothing implemented, proposal 3 carried at the 600/600 ceiling). Do NOT write claim verdicts — the
   L1 settles those.
3. corpus/QUALITY.md — APPEND ONE criterion row: `Q83` — a §9 shortcut control refuses the shortcut it names through the
   public path: on a committed shortcut world missing the claimed conjunct the control exits non-zero naming that conjunct and
   its honest world exits zero; a control that reads only a threshold or an uncommitted tree is a census observable, never the
   whole evidence. grounded in `corpus/lessons/round-92.md` § Mistakes (the vacuous row). supersedes: —.
4. corpus/README.md — index rows for corpus/lessons/round-92.md and (if the lane's index shape has one) the QUALITY row
   pointer, in the existing table shape, nothing else.
Census discipline: `grep -cE '^\\|[[:space:]]*S[0-9]{{3,}}[[:space:]]*\\|' corpus/SOURCES.md` over your clone must read 192;
validate with `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-11-05`
(exit 0 required; W04 duplicate-URL warnings pre-exist, 33 of them). Patch:
{W1}/ScribeCorpusR92/ScribeCorpusR92.patch (git diff --cached --binary {BASE} over corpus/). READY:
{W1}/ScribeCorpusR92_READY containing `CORPUS-READY` only after validate exits 0 in your clone."""),

item("connector", "ConnectorOverlapR92", """## ConnectorOverlapR92 — cross-claim overlap and sibling copies (read-only)

Read-only. (1) Shared surfaces among the round's code changes: verifiers/fixtures/round-92/ (C1 controls) vs
verifiers/check_mutation_battery.py (C2a) vs verifiers/check_freeze_gate.py + floors-registry.json + check_assertion_floors.py
freeze_gate cells + check_tip_battery.py INSTRUMENT_PINS (C2b). Name every file two claims could both touch, with line numbers
(check_freeze_gate's self-test arms vs the floors registry drift arm; the battery's manifest read vs the C1 manifest-only
world's rows). (2) Sibling copies: grep the sibling lane repos under /home/vgpnk/Projects/shokunin/ (read-only) for
`check_freeze_gate`, `check_mutation_battery`, `ctl-c2-capline-only`, `controls-run` — name any hit with path:line.
(3) Seat-name uniqueness: check the live sibling wave registries under /home/vgpnk/Projects/shokunin/*-shokunin/.ufo/waves/
for any seat named like this wave's (ExecCtlWorlds, ExecKillPin, ExecLadderR92, ScoutPyDocs, ScribeCorpusR92,
ConnectorOverlapR92, ReviewerCtl, MutTesterCtl, ReviewerFloors, MutTesterBattery, CriticClaimsR92, SentinelScopeR92) —
Q69/M131: a name reused by a concurrent sibling wave is a finding. Write
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-92/w1/ConnectorOverlapR92/ConnectorOverlapR92.md with the
overlap list O1..On (file:line each) and the uniqueness verdict."""),

item("reviewer", "ReviewerCtl", f"""## ReviewerCtl — attack C1: can a shortcut world pass the new controls?

Wait for {W1}/ExecCtlWorlds_READY (poll 120 s, up to 60 minutes). Build the candidate ({BASE} + ExecCtlWorlds.patch) in your
scratch clone and commit it there. Then, with rc and stdout recorded:
(a) run controls-run.sh on the candidate — it must print the exact frozen line and exit 0;
(b) FORGE the cap world: raise the cap AND add an INSTRUMENT_PINS entry naming a WRONG blob sha (the real floors blob is
    different) — the tip battery's pin guard must still refuse (blob equality, not presence); the control must stay REFUSED;
(c) FORGE the honest world: does ctl-c2-honest accept bytes whose pin admission names a stale blob from an older rev?
    It must not (the admission must be checked against the rev's actual blob);
(d) re-run the two OLD controls (verifiers/fixtures/round-91/ctl-c2-capline-only.sh, ctl-c1-manifest-only.sh) at the round-92
    base bytes in a fresh clone — the red-before observations must still hold (MET exit 0 / UNMET exit 1);
(e) verify the verdict lines byte-match the frozen predicate sentences in plans/round-92.md § C1;
(f) verify controls-run.sh cannot print 2 of 2 when a script is missing or exits 2 (run it with one script temporarily
    renamed in YOUR clone).
Write {W1}/ReviewerCtl/ReviewerCtl.md with findings R1..Rn, each with the command and observed output."""),

item("mutation-tester", "MutTesterCtl", f"""## MutTesterCtl — attack the C1 controls and the kill-set pin (mutate the attacker)

Wait for {W1}/ExecCtlWorlds_READY and {W1}/ExecKillPin_READY (poll 120 s, up to 60 minutes). Build the candidate ({BASE} +
both patches) in your scratch clone and commit it there. Mutate, one at a time, each on a fresh copy, with rc recorded:
(m1) controls-run.sh's counting changed to print `2 of 2` when a refused world exited 0 — the candidate's own consumers
     (ReviewerCtl's probes, the frozen predicate) must catch it; if nothing catches it, that is a SURVIVED mutant and a finding;
(m2) ctl-c2-capline-only-v2.sh drops the check_tip_battery invocation (cap check only) — must change the refusal (the pin
     conjunct gone → the control would read MET on a pinned-blob-but-wrong-cap world? derive the discriminating world and show it);
(m3) ctl-c1-manifest-only-v2.sh passes the base rev instead of the committed world rev — the round-91 defect class
     re-instantiated; the control's own stdout conjunct (`rows committed and read`) must no longer hold — show the probe that kills it;
(m4) check_mutation_battery.py's kill-set-size arm disabled → the dropped-row world goes green again (self-test rc 0);
     the reviewer probes must catch it, else SURVIVED;
(m5) ctl-c1-honest.sh drops its exit-0 requirement → a could-not-evaluate battery run would read MET; show the discriminating probe.
Equivalents: the honest self-tests and controls stay green with no mutation. Write
{W1}/MutTesterCtl/MutTesterCtl.md — per mutant: the diff, the discriminating world or probe, killed/survived, rc evidence."""),

item("reviewer", "ReviewerFloors", f"""## ReviewerFloors — attack C2(b): re-derive the rungs at base, verify the repairs and the coupling

Wait for {W1}/ExecLadderR92_READY (poll 120 s, up to 60 minutes). Build the candidate ({BASE} + ExecLadderR92.patch) in your
scratch clone and commit it there. Then, with rc and stdout recorded:
(a) re-run the three red-before probes verifiers/fixtures/round-92-predata/rp-work-regular-file.sh, rp-duplicate-names.sh,
    rp-exit127.sh against a BASE clone — all three must observe the defect (crash / held / could-not-evaluate) exactly as the
    committed receipts redbefore-ladder-*.txt record;
(b) re-run them against the candidate — workfile → could-not-evaluate rc 2 naming the work root; dupnames → invalid spec rc 3
    naming the duplicate; exit127 → invalid spec rc 3 naming the unobservable rung; the FileExistsError twin (--work naming an
    existing regular file) must also be fail-closed now, not a crash;
(c) honest worlds: fp-minimal.md held, verifiers/fixtures/freeze-gate/r88-controls.md exit 0;
(d) `python3 -B verifiers/check_freeze_gate.py --self-test` → `0 failure(s) over N'` (N' ≥ 34, three new arms named), rc 0;
(e) floor coupling: floors-registry.json freeze_gate floor == check_assertion_floors.py EXPECTED_INSTRUMENTS freeze_gate ==
    INSTRUMENTS freeze_gate == N'; `python3 -B verifiers/check_assertion_floors.py --self-test` still `0 failure(s) over 176
    assertions` rc 0;
(f) `python3 -B verifiers/check_tip_battery.py --rev <candrev>` → `guards 5 of 5`, rc 1 from exactly the three carried red
    corpus gates (base receipt base-tipbattery.txt) — the INSTRUMENT_PINS admission is present and correct (stale-blob
    admission must FAIL: mutate the pin to the old blob and show the guard red).
Write {W1}/ReviewerFloors/ReviewerFloors.md with findings R1..Rn."""),

item("mutation-tester", "MutTesterBattery", f"""## MutTesterBattery — attack the C2 candidate end to end (mutate the repairs)

Wait for {W1}/ExecKillPin_READY and {W1}/ExecLadderR92_READY (poll 120 s, up to 60 minutes). Build the candidate ({BASE} +
both patches) in your scratch clone and commit it there. Mutate, each on a fresh copy, with rc recorded:
(m1) drop one kill row from the live manifest → battery --self-test must FAIL naming kill-set-size (base: green, 25);
(m2) the pinned kill-set constant off by one → self-test FAIL on honest bytes (a false red — this mutant is the Q18
     false-red check: the arm must distinguish pinned-correct from off-by-one without breaking the honest run);
(m3) remove the duplicate-name parse rejection → rp-duplicate-names world reads held again;
(m4) remove the 126/127 parse rejection → rp-exit127 world reads could-not-evaluate rc 2 again (never compared);
(m5) remove the --work fail-closed translation → rp-work world crashes again;
(m6) floors-registry.json freeze_gate floor left at 31 while the self-test moved to N' → floors self-test FAIL (drift arm fires);
(m7) the INSTRUMENT_PINS append omitted → tip battery instrument-pin guard FAIL.
Equivalents (must survive, i.e. stay green): honest self-tests, fp-minimal, r88-controls fixture.
Write {W1}/MutTesterBattery/MutTesterBattery.md — per mutant: diff, observed rc and line, killed/survived."""),

item("critic", "CriticClaimsR92", f"""## CriticClaimsR92 — falsify the frozen claims against the full candidate

Wait for {W1}/ExecCtlWorlds_READY, {W1}/ExecKillPin_READY, {W1}/ExecLadderR92_READY and {W1}/ScribeCorpusR92_READY
(poll 120 s, up to 60 minutes). Build the candidate ({BASE} + every patch under {W1}/) in your scratch clone and commit it
there. Read plans/round-92.md § Claims first (the frozen predicates, counters, kill rules). Then, with rc and stdout recorded:
1. C1: run controls-run.sh on the candidate; byte-compare its line against the frozen predicate sentence; run each of the four
     scripts individually; confirm the refusal stdout names the missing conjunct each time.
2. C2(a): battery --self-test on the candidate (rc 0, N ≥ 26, arm named); the dropped-row world (build it in scratch) FAILS
     naming kill-set-size; the base red-before receipt redbefore-m6-dropped-row.txt matches what you observe at base bytes.
3. C2(b): the three rung probes on base vs candidate (red-before / refused-after); self-test N' ≥ 34; floors self-test 176 rc 0;
     floor coupling; tip battery guards 5 of 5 with only the three carried red corpus gates.
4. Do-nothing control (§9): the OLD control pair refuses 0 of 2 named shortcuts (oldcapline MET; oldmanifest unmet without
     reading); no new arms exist at base (battery 25, freeze-gate 31) — the do-nothing round cannot reach the targets.
5. Q26 headline check: every clause of each predicate sentence is turned on by its counter's output or a named guard — name
     any clause neither turns on.
6. Census arithmetic: the scribe patch's SOURCES must count 192 rows and validate exit 0 (run the census command and
     sources-census.sh validate --file in your candidate clone); the plan expects 190 → 192 with S265/S266 appended and no row
     dropped.
Write {W1}/CriticClaimsR92/CriticClaimsR92.md — per claim: MET/UNMET against the frozen counter, evidence lines, defects found
(numbered, each with command + observed output). Candidate verdicts only; the L1 rules the round."""),

item("sentinel", "SentinelScopeR92", f"""## SentinelScopeR92 — scope and safety of the candidate

Wait for {W1}/ExecCtlWorlds_READY, {W1}/ExecKillPin_READY, {W1}/ExecLadderR92_READY and {W1}/ScribeCorpusR92_READY
(poll 120 s, up to 60 minutes). Build the candidate ({BASE} + every patch under {W1}/) in your scratch clone and commit it
there. Check and record:
(a) patch scope: the union of the four builder patches touches ONLY the files in plans/round-92.md § Touch list — name every
    touched path from the diffs and flag anything outside (SKILL.md, corpus/lessons/round-*-verifier-spotcheck.md,
    verifiers/fixtures/round-91/, the frozen instruments list, plans/*, SCORECARD/LOG/PROVINCE are all violations);
(b) no seat wrote outside {W1}/ and its own scratch dir: `find {LANE}/.ufo/waves/round-92 -newer {LANE}/plans/round-92.md -type f`
    reviewed; nothing at the fleet root or in sibling repos;
(c) no sysctl write, no pacman invocation, no credential material, no raw environment dumps in any seat receipt (grep the wave
    tree for `sysctl`, `pacman`, `op://`, token-shaped strings);
(d) scratch discipline: every probe/clone under {SCRATCH}/<seat>/, TMPDIR honoured, no hardcoded /tmp in patched files
    (`grep -n '/tmp/'` over the patched bytes);
(e) the wave context's bounds sentence `Kill only by the PIDs you started; contention cap (4 processes, 120 s per probe)` is
    present in every seat's brief (you can only check your own — report that bound and trust the validator-rendered briefs for
    the rest);
(f) SKILL.md byte-identical at the candidate (git diff --stat {BASE} -- SKILL.md is empty).
Write {W1}/SentinelScopeR92/SentinelScopeR92.md with findings S1..Sn."""),
]

spec = {
    "wave": "r92-w1",
    "milestone": "r92-w1: C1 shortcut/honest control worlds; C2 kill-set pin + freeze-gate rungs; S265/S266 corpus; 5 attack seats",
    "reportDir": ".ufo/waves/round-92/w1",
    "context": CONTEXT,
    "items": items,
}
out = f"{LANE}/.ufo/waves/round-92/r92-w1-spec.json"
with open(out, "w") as f:
    json.dump(spec, f, indent=1)
print("BASE", BASE)
print("wrote", out, "items", len(items))
