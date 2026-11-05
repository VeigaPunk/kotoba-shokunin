#!/usr/bin/env python3
"""Generate r90-w1-spec.json — kotoba round 90, one v1 wave, 13 seats (band 8-16)."""
import json

GS = """You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim — let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.
"""

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
W1 = LANE + "/.ufo/waves/round-90/w1"
RCPT = LANE + "/.ufo/waves/round-90/receipts"
SCRATCH = "/fast/scratch/hyaku/kotoba-r90"
BASE = "0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5"
PRE = "6af71591e7232a7eebbaff78e7db653a70c7218b"

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only), .ufo/state/, .ufo/watchdog.log, MANIFEST.json, scripts/, templates/,
or /home/vgpnk/Projects/shokuknow (read-only: read it, never write, fetch or run a campaign tool there).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR to it, pass it to any
--work argument, and delete it before you yield (`trap 'rm -rf -- "$S"' EXIT`). Copy receipts you need
under {W1}/<your-seat-name>/ first. /tmp only for files under 50 MB. Never write under /tmp by a
hardcoded path in any committed file.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch,
pull, push, branch, or any mutating jj command). Never run scripts/hyaku/jj-lane.sh or fleet-commit.sh.
Read-only git (log, show, diff, status, ls-files, rev-parse, cat-file, archive, merge-base) is fine.
A scratch repo is created only as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D"`; every later git call names `-C "$D"`, and
`git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named
in your item. Message only agent://KotobaR90 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0
and broke every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: Kill only by the PIDs you started; contention cap (4 processes, 120 s per probe).
Attribution: never write under the lane identity or any "KotobaR90 (lane L1)" heading — your files and
LOG/lesson headings carry YOUR seat name only. Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you may install or upgrade tools that help the task. Read
/home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate). Record each install as
tool, version, channel, reason in your final answer. PACMAN IS PAUSED host-wide: no pacman transaction of
any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official binary in ~/.local/bin, or report the need.
Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 90, Linux host, omp 18.15.0)
Round base: {BASE} (lane tip at round start). Plan + pre-data controls committed: {PRE}.
Plan (FROZEN — read fully first): {LANE}/plans/round-90.md and {LANE}/plans/round-90-controls.md at {PRE}.
Nobody edits the plan, the controls plan, or any frozen predicate: an amendment is an L1 act via
plans/round-90-addendum-*.md BEFORE any scored reading; a counter defect you find is a FINDING in your
answer — never rescue a counter by changing its predicate.
The pre-data control battery is already held: `freeze gate: 6 control(s) held`, exit 0
({RCPT}/freeze-gate-r90.txt). Before-state receipts already committed: {RCPT}/census-before.txt,
before-c1-absence.txt, before-c2-sweep.txt, base-floors.txt, base-integrity.json, base-d5v3.txt,
base-registry.txt, base-tipbattery.txt, base-checklist.json, base-siblingcensus.txt, base-skillmd-size.txt.
FROZEN instruments (byte-identical; never edit): verifiers/check_freeze_gate.py,
verifiers/check_r86_routed_repairs_v3.py, verifiers/verify_corpus_integrity.py,
verifiers/corpus-baseline.json, and every verifiers/*.py not named in File ownership below.
Round-89 evidence (readable, committed): {LANE}/.ufo/waves/round-89/w1/MutTesterGates/ (mutants.tsv,
equivalents.tsv, harness.py, summary.json), corpus/lessons/round-89-verifier-spotcheck.md (routed notes).
Skill budget: SKILL.md is 600/600 lines — a seat that needs a registry row does NOT edit SKILL.md;
the L1 lands registry rows with offsetting joined wrapped lines at integration.

## File ownership (one writer per production file; no two seats write the same file)
ExecFloorsBump owns verifiers/floors-registry.json (ONLY the instrument_total bump 18 -> 19; no other row
changes) and verifiers/check_assertion_floors.py (guard tables + F6 literal + docstring; the bump completion).
ExecIndexRow owns corpus/README.md (one index row for corpus/lessons/round-89-verifier-spotcheck.md plus at
most one append-only note; nothing else in the file changes).
ExecBattery owns verifiers/check_mutation_battery.py and everything under verifiers/fixtures/mutation-battery/.
ExecHostCensus owns {RCPT}/c2-host-census.txt and {RCPT}/c2-name-collisions.txt (no other receipts paths).
ExecFloorsBump and ExecIndexRow may write {RCPT}/floors-*.txt and {RCPT}/index-*.txt respectively.
ScoutMutSource, ScoutHostRoots, ReviewerRepairs, ReviewerBattery, CriticClaims, MutTesterBattery,
ConnectorOverlap, SentinelScope write only under {W1}/<their-seat-name>/.
ScribeCorpus owns corpus/knowledge/mutation-battery-round90.md, corpus/knowledge/host-census-round90.md,
corpus/SOURCES.md (ONLY rows S260 and S261 appended), corpus/QUALITY.md (ONLY the Q82 row appended),
and corpus/lessons/round-90.md (scaffold; the L1 completes the settlement).
The L1 integrates plans/, SCORECARD.md, LOG.md, SKILL.md (registry rows) and the commits.

## Handoff files (poll every 120 seconds with `sleep 120`, up to 45 minutes; if one never appears, report on what exists and say so)
{W1}/SOURCE_READY    — ScoutMutSource, after the S260 record is complete (content: the URL).
{W1}/ROOTS_READY     — ScoutHostRoots, after the root population data is complete (content: the surface count).
{W1}/FLOORS_READY    — ExecFloorsBump, after the guard's --self-test passes (content: the script sha256).
{W1}/INDEX_READY     — ExecIndexRow, after the integrity gate reads unindexed 0 (content: the observed line).
{W1}/BATTERY_READY   — ExecBattery, after check_mutation_battery.py --self-test passes (content: sha256).
{W1}/CENSUS_READY    — ExecHostCensus, after both receipts exist (content: the measured line).
{W1}/SCRIBE_READY    — ScribeCorpus, after the scaffold files are written (content: the file list).
{W1}/CONNECTOR_READY — ConnectorOverlap, after the sibling scan (content: the boundary sentence).

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR and accept a scratch/--work argument; exit ladder 0 pass,
1 content fail, 2 could-not-evaluate (3 = invalid spec where the plan declares it); `--self-test` prints
`0 failure(s) over N assertions`. Every self-test assertion names the arm it guards. No network inside a
counter; no writes outside named paths; rev-scoped reads go through `git show <rev>:<path>`, never a
second working tree inside the lane.
"""

items = [
    {
        "role": "scout",
        "name": "ScoutMutSource",
        "prompt": GS + f"""## ScoutMutSource — open the SOURCES row S260 (round-90 §2b, C1's sourced row)

1. Open a mutation-testing practice primary source grounding the mutant/killed/survived vocabulary and
   the equivalent-mutant notion (claim C1's sourced row, `plans/round-90.md` § C1). Try, in order,
   stopping at the first HTTP-200 success:
   (a) https://mutmut.readthedocs.io/en/latest/ (and its "How it works" / glossary subpages)
   (b) https://stryker-mutator.io/docs/ (general mutation-testing page)
   Fetch with `curl -sL --max-time 60` into {W1}/ScoutMutSource/s260-snapshot.<ext> (the exact bytes).
2. Record in {W1}/ScoutMutSource/s260-notes.md: URL fetched, HTTP status, access date 2026-11-05,
   byte size (`wc -c`), sha256 (fetch-time metadata only — r89 spot-check note 1: ground quotes in
   line anchors + size + title, never the digest), page title, and TWO located quotes ≤ 25 words each
   (`wc -w` on the quoted segment) with their line numbers in your saved snapshot, grounding
   (i) the killed/survived vocabulary and (ii) the equivalent-mutant or score notion. Q42/Q53: paste
   `sed -n '<L>p'` output for each quoted line; name exactly which bytes were shaped, if any.
3. Record at least one REJECTED route with reason + flip for the lesson Gate (e.g. a 403/paywalled
   route, or Wikipedia as C-tier lead-only — rejected as sole support for a tier-A-scoped claim).
4. Write {W1}/SOURCE_READY (content: the URL) when done. Write scope: only
   {W1}/ScoutMutSource/. Final answer: short JSON per the context.""",
    },
    {
        "role": "scout",
        "name": "ScoutHostRoots",
        "prompt": GS + f"""## ScoutHostRoots — measure this host's skills-root population (data only)

1. Enumerate the live skills root read-only: every directory under /home/vgpnk/.agents/skills holding
   a SKILL.md (`for d in /home/vgpnk/.agents/skills/*/; do [ -f "$d/SKILL.md" ] && echo "$d"; done | wc -l`).
   The plan froze N == 83 from `ls | wc -l` at plan time — verify the SKILL.md-holding count and record
   BOTH numbers with their commands. If they differ, record the difference; do not reconcile it silently.
2. Check for other candidate roots on this host (read-only): ls -d ~/.omp/agent/skills ~/.omp/skills
   ~/.config/opencode/skills 2>&1; record what exists and what does not.
3. Raw data only, no census run (ExecHostCensus owns the census): list the directory names
   (`ls /home/vgpnk/.agents/skills`), and note which, if any, match a fleet lane name
   (`ls /home/vgpnk/Projects/shokunin | grep -v -e '^\\.' -e '\\.md$' -e '\\.sh$' -e '\\.json$' -e '\\.conf$'`).
4. Write {W1}/ScoutHostRoots/roots-data.md with every command + observed output, then
   {W1}/ROOTS_READY (content: the SKILL.md-holding count). Write scope: only {W1}/ScoutHostRoots/.
   Final answer: short JSON per the context.""",
    },
    {
        "role": "executor",
        "name": "ExecFloorsBump",
        "prompt": GS + f"""## ExecFloorsBump — complete the r89 floors half-bump (carry-in repair)

Red at base ({RCPT}/base-floors.txt): `FAIL registry size drift: instrument_total=18 but 19 entries in
verifiers/floors-registry.json` and `FAIL registry row vanish: freeze_gate (listed in
verifiers/floors-registry.json, absent from both guard tables)`. The registry's own $comment declares the
BUMP-IN-STEP RULE: registry file, BOTH in-file tables (EXPECTED_INSTRUMENTS, INSTRUMENTS) and the guard
docstring change together.

1. Read verifiers/check_assertion_floors.py: find both tables and the F6 self-test arm that swaps the
   literal `'"instrument_total": 18'` in the real registry text.
2. Complete the bump in ONE change: add `freeze_gate` (floor 30, path `verifiers/check_freeze_gate.py` —
   copy the floor from verifiers/floors-registry.json) to BOTH in-file tables, bump
   `instrument_total` 18 -> 19 in floors-registry.json, update the F6 swap literal to the new total,
   and update the guard docstring instrument list. No other row changes (verify: the only diff hunks
   touch freeze_gate entries and the total).
3. Prove it: `python3 -B verifiers/check_assertion_floors.py --self-test` -> `0 failure(s) over N
   assertions`, exit 0; live run `python3 -B verifiers/check_assertion_floors.py` -> exit 0. Save both
   transcripts + rc as {RCPT}/floors-selftest.txt and {RCPT}/floors-live.txt (Q36: each receipt names
   the measured revision: append `git rev-parse master` output).
4. Regression arm (Q05, shown able to fail) in SCRATCH ONLY: copy the lane to
   {SCRATCH}/ExecFloorsBump/halfbump/ (cp -a or git archive), revert your guard edits there (back to
   the two tables without freeze_gate and total 18 while the registry keeps 19), run the guard in that
   copy -> it must print BOTH base FAIL lines; save {RCPT}/floors-regression.txt.
5. Write {W1}/FLOORS_READY (content: the guard script sha256, `sha256sum
   verifiers/check_assertion_floors.py`). Write scope: the two owned production files + your receipts +
   {W1}/ExecFloorsBump/. Final answer: short JSON per the context.""",
    },
    {
        "role": "executor",
        "name": "ExecIndexRow",
        "prompt": GS + f"""## ExecIndexRow — index the round-89 verifier spot-check (carry-in repair)

Red at base ({RCPT}/base-integrity.json): `corpus.index.unindexed 1` —
`corpus/lessons/round-89-verifier-spotcheck.md` is not indexed in corpus/README.md (an index row is a
claim: write the row when the file exists).

1. Find the row format used for the round-87/88 spot-check files in corpus/README.md (## Coverage map
   area) and add ONE matching index row for corpus/lessons/round-89-verifier-spotcheck.md. Change
   nothing else in the file except at most one short append-only note naming why the row lands late
   (the file landed after the r89 landing measurement).
2. Prove it: `python3 -B verifiers/verify_corpus_integrity.py --json` -> `unindexed 0`, exit 0. Save
   transcript + rc as {RCPT}/index-integrity.txt (receipt names `git rev-parse master`).
3. Regression arm (Q05) in SCRATCH ONLY: copy corpus/ + the gate to {SCRATCH}/ExecIndexRow/ and remove
   your row there -> the gate reads `unindexed 1` again; save {RCPT}/index-regression.txt.
4. Write {W1}/INDEX_READY (content: the observed unindexed line). Write scope: corpus/README.md + your
   receipts + {W1}/ExecIndexRow/. Final answer: short JSON per the context.""",
    },
    {
        "role": "executor",
        "name": "ExecBattery",
        "prompt": GS + f"""## ExecBattery — build the mutation-battery runner (round-90 C1, frozen predicate)

Read {LANE}/plans/round-90.md § C1 first — the predicate, guard set, two-sided rule (Q47), kill rule and
manifest classes are FROZEN there. Build exactly that instrument.

1. `verifiers/check_mutation_battery.py` (python3 -B, stdlib only): args `--rev REV` (required, full
   hash), `--work DIR` (required, scratch), `--self-test`. It reads the committed manifest
   `verifiers/fixtures/mutation-battery/manifest.tsv` (columns: id, target, class, recipe, disposition;
   classes kill | equivalent | survivor). Targets: `verifiers/check_freeze_gate.py` and
   `verifiers/check_r86_routed_repairs_v3.py` at the FINAL bytes of --rev (`git show <rev>:<path>` into
   scratch — guard G1: never the working tree).
2. Recipes (read {LANE}/.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv and port its kill rows for the
   final bytes as anchor-regex edits; d5-m1a-d5iii-leg-only enters class `survivor` with its recorded
   disposition): each kill recipe mutates the scratch copy and runs the frozen probe set — fg probes:
   `--self-test` (baseline exit 0), `--plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md`
   (baseline exit 0), `--plan verifiers/fixtures/freeze-gate/r88-controls.md` (baseline exit 1);
   d5 probes: `--self-test` (baseline exit 0) and `--base-receipt
   .ufo/waves/round-89/receipts/d5v3-base-receipt.json` (baseline = whatever the base reads —
   {RCPT}/base-d5v3.txt shows `closed 4 of 5, instance drift 4`; the BASELINE is observed on the
   unmutated copy first and recorded). kill = any probe exit or stdout line flips vs the recorded
   baseline. Equivalents are GENERATED at measurement time (Q47): the battery applies three
   semantics-preserving rewrite recipes (comment line insert, docstring line reword, trailing
   whitespace) to each target; every probe must stay identical.
3. Guards: G1 every probe reads revision bytes copied to scratch; G2 the battery sha256s each mutated
   file's revision bytes, records it, and exits 2 on a mismatch (`could-not-evaluate`); G3 the gate
   registry must name the battery: `git show <rev>:SKILL.md | grep -c 'check_mutation_battery.py'` >= 1,
   else exit 1 (a stub world without a registry row cannot pass — the ctl-c1-stub control world).
4. Output: `mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors
   S of S` and exit 0 iff K == M and E == E and S == S_declared and G1–G3 PASS; exit 1 content fail;
   exit 2 could-not-evaluate (an anchor no longer matches the revision bytes — honest, never skipped).
5. `--self-test` (Q48): drives `main()` on a satisfying fixture asserting exit 0 and the EXACT line,
   beside a broken-conjunct world asserting exit 1, plus one guard arm each for G1/G2/G3. Target
   `0 failure(s) over N assertions`, exit 0.
6. Prove it on the landing candidate: `python3 -B verifiers/check_mutation_battery.py --rev <rev>
   --work {SCRATCH}/ExecBattery/work` -> the success line, exit 0 (the SKILL.md registry row does not
   exist yet — run the G3 guard against the CURRENT SKILL.md and record that G3 reads 0 rows naming it:
   that means the full predicate reads exit 1 until the L1 lands the row. Record BOTH readings in
   {W1}/ExecBattery/battery-run.txt: (a) with --allow-unregistered (add this opt-in flag ONLY to let
   the pre-registry run print the K/E/S counts; it must NOT be part of the frozen predicate line), and
   (b) the frozen form, expected exit 1 until the row lands. Save the self-test transcript as
   {W1}/ExecBattery/battery-selftest.txt.
7. Write {W1}/BATTERY_READY (content: sha256 of the script). Write scope: the two owned production
   paths + {W1}/ExecBattery/. Final answer: short JSON per the context.""",
    },
    {
        "role": "executor",
        "name": "ExecHostCensus",
        "prompt": GS + f"""## ExecHostCensus — the host installed-skill census on this host's live root (round-90 C2)

Read {LANE}/plans/round-90.md § C2 first — the frozen predicate binds the live root
/home/vgpnk/.agents/skills, N == 83, and two committed receipts.

1. Wait for {W1}/ROOTS_READY (poll 120 s); read ScoutHostRoots' data — if the SKILL.md-holding count
   differs from 83, STOP and report the finding instead of measuring against a wrong bound.
2. Run: `python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills
   --fleet-root /home/vgpnk/Projects/shokunin` -> expect exit 0 and
   `host skill surfaces measured 83: identical I, drifted D, lane-absent A` with I + D + A == 83.
   Save the transcript + rc as {RCPT}/c2-host-census.txt, first line `measured-rev: <output of
   git -C {LANE} rev-parse master>` (Q36).
3. The A1 name-uniqueness ledger (round-72 A1 / round-84 C2 method): extract the frontmatter `name:`
   from each installed SKILL.md (read-only), group by value, and write one line per duplicate-name pair
   `NAME-COLLISION <name> <dir1> <dir2>` into {RCPT}/c2-name-collisions.txt; add a final line
   `NAME-COLLISION count: <N> — grep -c 'NAME-COLLISION' <receipt> <date>` and the surface total.
   Cross-root check: only one live root exists on this host (ScoutHostRoots' data) — record that.
   Findings are read-only: name drifted/identical findings for the report; fix nothing outside the lane.
4. Write {W1}/CENSUS_READY (content: the measured line). Write scope: the two owned receipt files +
   {W1}/ExecHostCensus/. Final answer: short JSON per the context.""",
    },
    {
        "role": "reviewer",
        "name": "ReviewerRepairs",
        "prompt": GS + f"""## ReviewerRepairs — attack the floors bump and the index row

Wait for {W1}/FLOORS_READY and {W1}/INDEX_READY (poll 120 s, up to 45 min), then attack both repairs
from their committed bytes. You never edit production files; findings only.

1. Floors bump: diff `git diff {PRE} -- verifiers/floors-registry.json verifiers/check_assertion_floors.py`
   — verify ONLY the freeze_gate entries + instrument_total + F6 literal + docstring changed; verify the
   guard's tables and the registry agree row-for-row; re-run the guard live and in a scratch half-bump
   world yourself (build your own, do not trust the seat's) and confirm the two FAIL lines return.
2. Index row: verify the new README row names the existing file and matches the sibling-row format; run
   the integrity gate yourself; build your own scratch no-row world and confirm `unindexed 1` returns.
3. Check the repairs introduced no new red: run {RCPT}/base battery commands 1 and 2 yourself and
   compare against the base receipts. Any new red = a FINDING.
4. Write {W1}/ReviewerRepairs/review.md: verdict per repair (sound / defect with path:line), every
   command you ran and its observed line. Write scope: only {W1}/ReviewerRepairs/. Final answer:
   short JSON per the context.""",
    },
    {
        "role": "reviewer",
        "name": "ReviewerBattery",
        "prompt": GS + f"""## ReviewerBattery — attack the mutation-battery instrument

Wait for {W1}/BATTERY_READY (poll 120 s, up to 45 min), then attack
verifiers/check_mutation_battery.py from committed bytes. Findings only; never edit it.

1. Predicate identity (kill rule): the docstring's predicate sentence must equal `plans/round-90.md` § C1's
   sentence (modulo the flag list); any drift is a FINDING.
2. Guard reality: forge a world in scratch — a probe receipt naming a different revision, a mutated file
   whose sha256 was edited after recording, a manifest with a missing class column — and confirm the
   battery refuses (exit 2/1 as its ladder declares). Confirm G3 fires on a SKILL.md without the row.
3. Recipe reality: apply one kill recipe by hand to a scratch copy of the final bytes and diff it — the
   mutation must change real code, not a comment; confirm the killed probe flips for the reason the
   receipt names (not a crash; a crash-on-mutant is a FINDING — a mutant should change a verdict, not
   segfault).
4. Baseline honesty: run the d5 probe baseline yourself ({RCPT}/base-d5v3.txt shows the base reading);
   confirm the battery's recorded baseline equals your observation, and that a flip on the r89-receipt
   probe would be reported as a kill, not swallowed.
5. Self-test honesty: run `--self-test`; confirm the broken-conjunct arm really breaks a conjunct
   (mutate the fixture the arm uses in your scratch copy and confirm the arm fails).
6. Write {W1}/ReviewerBattery/review.md: verdicts, commands, observed lines. Write scope: only
   {W1}/ReviewerBattery/. Final answer: short JSON per the context.""",
    },
    {
        "role": "critic",
        "name": "CriticClaims",
        "prompt": GS + f"""## CriticClaims — pre-score falsification of both round-90 claims

Read {LANE}/plans/round-90.md and plans/round-90-controls.md fully. Both claims are FROZEN; your job is
to falsify them before any candidate score, from committed bytes. Findings only.

1. Re-run all six controls yourself (`bash verifiers/fixtures/round-90/ctl-*.sh`); confirm each exit 1
   with the declared marker. Any control that meets its predicate = the claim dies before data.
2. Q26/Q31 headline audit: does each predicate sentence measure every clause its claim asserts? Is any
   clause (provenance, coverage, universality) asserted but unmeasured? Name it.
3. Q37 shortcut sweep: name the cheapest real-input shortcut per claim that neither control world covers
   (e.g. for C2: a skills root with 83 non-skill directories; for C1: a manifest whose probes are all
   `--self-test` only) and say whether the frozen guards catch it.
4. Population bound: C2 freezes N == 83 — is the bound pinned to a measurable population command (not a
   bare number), and what happens to the predicate if the host's root changes mid-round? The answer must
   be derivable from the plan + receipts; if not, it is a FINDING.
5. SOURCES candidate: check the S260/S261 plan (row contract v1: 11 columns, no pipes in cells, tier
   scoped, used-by) against {W1}/ScoutMutSource/ outputs when SOURCE_READY exists.
6. Write {W1}/CriticClaims/attacks.md: numbered findings (F1, F2, ...) each with severity, evidence
   command + observed line, and whether it blocks a claim or is bounded. Write scope: only
   {W1}/CriticClaims/. Final answer: short JSON per the context.""",
    },
    {
        "role": "mutation-tester",
        "name": "MutTesterBattery",
        "prompt": GS + f"""## MutTesterBattery — mutate the mutation-battery runner (attack the attacker)

Wait for {W1}/BATTERY_READY (poll 120 s, up to 45 min). Mutate verifiers/check_mutation_battery.py in
SCRATCH copies; the lane is never written.

1. Baselines first (pristine): `--self-test` -> `0 failure(s) over N assertions`, exit 0; the frozen
   run `--rev <tip> --work <scratch>` -> record its exact output and exit (it may read exit 1 while the
   SKILL.md registry row is absent — that is the recorded G3 baseline, not a defect).
2. Declared mutants (at least 8, ported from the r89 style): sign flips (exit 0 <-> 1), guard skips
   (G1/G2/G3 each), manifest-class skip (drop the survivor class from the count), output-line drift
   (the printed line diverges from the frozen sentence), equivalent-class skipped at generation,
   rev-bytes path switched to the working tree (G1 violation). Each mutant must be KILLED by the
   `--self-test` or by a probe flip vs the pristine baseline; record killed-by which arm.
3. Equivalents: at least 2 semantics-preserving rewrites must survive (comment/docstring), recorded.
   SURVIVED kill-class mutants are recorded honestly with reasons — never declared killed.
4. Tables: {W1}/MutTesterBattery/mutants.tsv and equivalents.tsv (same columns as the r89 tables);
   transcripts under {W1}/MutTesterBattery/transcripts/. Write scope: only {W1}/MutTesterBattery/.
   Final answer: short JSON per the context.""",
    },
    {
        "role": "connector",
        "name": "ConnectorOverlap",
        "prompt": GS + f"""## ConnectorOverlap — sibling-overlap scan for the two round-90 surfaces

Read-only across sibling lanes; you never edit anything outside {W1}/ConnectorOverlap/.

1. The mutation METHOD is tameshi's (reusable fixture and mutation method; each lane's gate stays its
   own — tameshi PROVINCE.md). Check tameshi-shokunin/ (read-only, pinned `git -C
   /home/vgpnk/Projects/shokunin/tameshi-shokunin rev-parse HEAD`): does tameshi's corpus/SKILL already
   hold a committed mutation-battery-over-lane-gates instrument, and does kotoba's planned battery stay
   inside "each lane's gate stays its own"? Write the boundary sentence for the report (one or two
   sentences: what kotoba's capability adds on kotoba's own gates; what it does not absorb).
2. The host installed-skill census: check whether any sibling's corpus claims the same surface
   (`grep -rl 'host skill surfaces\\|installed-skill' /home/vgpnk/Projects/shokunin/*/corpus 2>/dev/null`).
   If another lane claims it, name the overlap and the owning lane; kotoba's r82 capability precedent
   stands (drift findings route to owning lanes, never fixed from kotoba).
3. Scan the OTHER lanes' newest lessons for round-90-relevant findings (`ls -t
   /home/vgpnk/Projects/shokunin/*/corpus/lessons/round-8*.md 2>/dev/null | head -8`; skim titles only —
   you are a connector, not a reader of record): name any routed defect that touches kotoba's two
   surfaces.
4. Write {W1}/ConnectorOverlap.md with the boundary sentences + evidence commands, then
   {W1}/CONNECTOR_READY (content: the boundary sentence). Final answer: short JSON per the context.""",
    },
    {
        "role": "sentinel",
        "name": "SentinelScope",
        "prompt": GS + f"""## SentinelScope — write-scope and host-safety verification for the r90 wave

You run CONCURRENTLY with the other seats; verify only what exists at your read time, then do one final
sweep late (sleep 600 once, then sweep again) and report both passes.

1. Lane-tree write audit: `find /home/vgpnk/Projects/shokunin/kotoba-shokunin -newer
   /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-90-controls.md -type f -not -path '*/.git/*'
   | sort` — every path must be inside the ownership map in the wave context (the L1's files may also
   appear after integration; note them as expected-L1). A path outside the map = a FINDING with mtime.
2. Fleet-root audit: `git -C /home/vgpnk/Projects/shokunin status --porcelain | head -40` — name any
   untracked file whose content mentions kotoba or round-90 (misroot class); do not touch it.
3. Host safety: `cat /proc/sys/user/max_user_namespaces` must read 122865 (or the pre-wave value —
   record it twice, 60 s apart); `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master`
   must be unchanged by seats (only the L1 commits); no seat may have written /proc/sys (read-only check).
4. Scratch hygiene at the final sweep: `ls /fast/scratch/hyaku/kotoba-r90/` — seats that ended must have
   removed their dirs; a leftover dir is a FINDING naming the seat (their receipts live in the wave dir).
5. Write {W1}/SentinelScope/sentinel.md with both passes' evidence. Write scope: only
   {W1}/SentinelScope/. Final answer: short JSON per the context.""",
    },
    {
        "role": "scribe",
        "name": "ScribeCorpus",
        "prompt": GS + f"""## ScribeCorpus — draft the round-90 corpus material (SOURCES S260/S261, knowledge entries, Q82, lesson)

Poll every 120 s (up to 45 min) for {W1}/SOURCE_READY, {W1}/BATTERY_READY, {W1}/CENSUS_READY — draft
from what exists; if a handoff never appears, draft that section as `pending-<handoff>` and say so.

1. corpus/SOURCES.md — append EXACTLY two rows (append-only; no existing cell changes; contract v1:
   11 cells, no `|` inside any cell, tier scoped in `scope`, status `queued` or `mined` only after the
   entry citing it is written — use `queued` here; `used-by` names the knowledge files you write):
   S260 from ScoutMutSource's notes (source = title — canonical URL; anchor = the located line + access
   date; teaches = the grounded learner benefit; your own Gate-block quote data comes from the scout's
   recorded `sed -n` lines). S261 = own-work row: source `git show
   0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`
   (kind own-work, tier A scoped to the r89 mutant matrix record).
2. corpus/knowledge/mutation-battery-round90.md — provenance trio first (Q12): `source:` citing S260 +
   S261 with anchors, `verified-at:` (the BATTERY_READY sha + rev), `recheck:` the runnable command
   `python3 -B verifiers/check_mutation_battery.py --rev <rev> --self-test`; body: what the battery
   does (manifest classes, probe set, baseline-flip kill rule, Q47 two-sided), bounds (what it does not
   prove — no oracle for equivalent correctness beyond the generated rewrite class; d5 baseline is
   path-dependent per Q79),Limits section naming reviewer-judged parts.
3. corpus/knowledge/host-census-round90.md — provenance trio (source: the r82 capability + this round's
   receipts; verified-at: the CENSUS_READY measured line; recheck: the census command), body: the
   measured census line, the NAME-COLLISION ledger result, findings routed read-only, bounds.
4. corpus/QUALITY.md — append ONE criterion row Q82 (extends Q11/M15, never rewrites it): a per-round
   wave-evidence byte budget measured at landing (`du -sb` of the round's .ufo/waves/round-90/ stated
   in the report; a bundle over the stated budget names the oversized artifact and its claim);
   `grounded in` names corpus/lessons/round-90.md § Mistakes/Considerthese and the considerthese
   pointer (considerthese/2026-10-26.md proposal 5, 2026-10-26).
5. corpus/lessons/round-90.md — scaffold with: header (author: ScribeCorpus seat + L1 completes the
   settlement), `## Gate` (candidates: S260 admit/rejected routes from the scout's record, S261 admit;
   assimilation: none — L0 kotoba|round-88 open; considerthese: proposal 5 mined as Q82, 3 and 4
   carried), `## Mistakes` (the r89 floors half-bump row: class, evidence pointer, captured-by = the
   registry bump-in-step rule + the guard anchor that caught it, fix = the completed bump + the
   half-bump regression arm), and a `## Seat record` placeholder the L1 completes.
6. Write {W1}/SCRIBE_READY (content: the file list). Write scope: ONLY the five owned corpus paths +
   {W1}/ScribeCorpus/. Final answer: short JSON per the context.""",
    },
]

spec = {
    "wave": "r90-w1",
    "milestone": "r90-w1: C1 mutation-battery runner over the final r89 gate bytes; C2 host installed-skill census re-pinned to this host's live root; carry-in floors half-bump + index-row repairs; 5 attack seats",
    "reportDir": ".ufo/waves/round-90/w1",
    "context": CONTEXT,
    "items": items,
}

with open(".ufo/waves/round-90/r90-w1-spec.json", "w") as f:
    json.dump(spec, f, indent=1)
print("items:", len(items))
print("roles:", sorted({i["role"] for i in items}))
print("attack:", [i["name"] for i in items if i["role"] in ("reviewer", "critic", "mutation-tester", "sentinel")])
