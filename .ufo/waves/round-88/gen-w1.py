#!/usr/bin/env python3
"""Generate the round-88 wave-1 spec (14 seats) for the v1 swarm validator.

Every seat prompt is self-contained; the shared context carries the bounds, the frozen state,
the file-ownership map and the handoff files. Output: r88-w1-spec.json beside this script.
"""
import json
from pathlib import Path

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = f"{LANE}/.ufo/waves/round-88/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r88"
TIP = "4df1e8005016c75390a5e06b209462df58c95918"
BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
ELF = "/home/vgpnk/.local/bin/omp"
ELF_SHA = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only), .ufo/state/, .ufo/watchdog.log, MANIFEST.json, scripts/, templates/,
or /home/vgpnk/Projects/shokuknow (read-only: read it, never write, fetch or run a campaign tool there).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR to it, pass it to any
--work argument, and delete it before you yield (`trap 'rm -rf -- "$S"' EXIT`). Copy receipts you need
under {WAVE}/<your-seat-name>/ first. /tmp only for files under 50 MB. Never write under /tmp by a
hardcoded path in any committed file.
Git: never run a git or jj write in the lane or the fleet (no add, commit, stash, checkout, reset, switch,
pull, push, branch, or any mutating jj command). Read-only git (log, show, diff, status, ls-files,
rev-parse, cat-file, archive, merge-base) is fine. A scratch repo is created only as
`D={SCRATCH}/<seat>/repo && git clone -q --shared {LANE} "$D"`; every later git call names `-C "$D"`, and
`git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Never touch the fleet root, another lane, the lane's jj state, the lane's git index, or any file not named
in your item. Message only agent://KotobaR88 (never agent://all).
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you may install or upgrade tools that help the task. Read
/home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate). Record each install as
tool, version, channel, reason in your final answer. PACMAN IS PAUSED host-wide: no pacman transaction of
any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official binary in ~/.local/bin, or report the need.
Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 88, Linux host, omp 18.15.0)
Tip {TIP}. Reference base for the C2 red-set test {BASE}. Plan and freeze: {LANE}/plans/round-88.md —
read it fully first. Its predicates, targets, controls and kill rule are FROZEN: nobody edits the predicate
sentences, the targets or the kill rule. A counter defect you find is a FINDING, reported in your answer; do
not rescue a counter by changing its predicate.
ELF: {ELF}, sha256 {ELF_SHA}; it is 277 MB and carries its TypeScript source as a bun bundle. Read it with
python mmap and re, read-only; never copy it into the lane; never execute it (except `omp --version`).
Round-87 evidence (readable, committed): {LANE}/.ufo/waves/round-87/ (w3/CriticSemanticsR87/ holds the four
forged-world records; w3/ScoutPatternsR87/derived-roots.txt the six unledgered joins; w3/ExecProbeBoundR87/ the
live walk-up probe; plans/round-87.md the r87 predicates).
The r87 counters are FROZEN and stay byte-identical: `verifiers/check_omp_root_semantics.py` (sha256
6e826f3b…8922), `verifiers/check_r86_routed_repairs.py`, `verifiers/omp-skill-roots-semantics.tsv`,
`verifiers/omp-skill-roots.tsv`, `verifiers/check_omp_catalogue_repro.py`, `verifiers/verify_corpus_integrity.py`.
Never edit them. The new files are named in your item.

## File ownership (one writer per production file; no two seats write the same file)
ExecLiveBound owns verifiers/check_omp_root_semantics_v2.py and the one floors-registry row for it (if
verifiers/floors-registry.json exists; add the row, do not rewrite others).
ExecMonotoneD5 owns verifiers/check_r86_routed_repairs_v2.py.
ExecForgeryWorlds writes only under {WAVE}/ExecForgeryWorlds/ and its scratch.
ScoutUpstream, ScoutElfMap, Connector, ReviewerC1, ReviewerC2, CriticFalsify, MutTesterV2, Sentinel write only
under {WAVE}/<their-seat-name>/.
ScribeEntry owns corpus/knowledge/omp-root-semantics-round88.md.
ScribeSources owns corpus/SOURCES.md (one new row S257) and corpus/README.md (index row + § Frontier note).
ScribeLesson owns corpus/lessons/round-88.md, corpus/QUALITY.md (criterion Q80 only) and LOG.md (append only).
The L1 integrates plans/, SCORECARD.md, SKILL.md and the commits. Nobody else edits those.

## Handoff files (poll every 120 seconds with `sleep 120`, up to 45 minutes; if one never appears, report on what exists and say so)
{WAVE}/ELF_MAP_READY  — written by ScoutElfMap after {WAVE}/ScoutElfMap/ELF_MAP.tsv is complete.
{WAVE}/SOURCE_READY   — written by ScoutUpstream after its source record is complete.
{WAVE}/C1_READY       — written by ExecLiveBound after the v2 counter's own --self-test passes (content: its sha256).
{WAVE}/C2_READY       — written by ExecMonotoneD5 after the v2 gate's own --self-test passes (content: its sha256).
{WAVE}/FORGERY_READY  — written by ExecForgeryWorlds after the v2 run over the forged worlds is recorded.
{WAVE}/CONNECTOR_READY — written by Connector after its sibling scan is complete.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR and accept a scratch argument; exit ladder 0 pass,
1 content fail, 2 could-not-evaluate; `--self-test` prints `0 failure(s) over N assertions`. Every
self-test assertion names the arm it guards. No network inside a counter. No execution of the ELF inside a
counter (read-only mmap)."""

ITEMS = [
    dict(role="scout", name="ScoutUpstream", prompt=f"""## ScoutUpstream — open the upstream omp source for the bound conjunct (new SOURCES row S257)

Target: the upstream file `packages/coding-agent/src/discovery/agents.ts` at tag v18.15.0 (it reads
`{{cwd}}/.agents/skills` and `~/.agents/skills`, the walk-up root; the ledger row 4 names it).
1. Fetch the raw file with `curl -fsSL` into {SCRATCH}/ScoutUpstream/ (never pipe a remote file into a shell).
   URL: https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts
   Record the HTTP status, byte size, sha256, and the access date (today's date in ISO form).
2. Locate the walk-up loop that bounds the project walk (the home-directory stop). Quote one line verbatim
   that shows the bound (<= 25 words, located by line number). Also record the ELF offset of the same
   code if it is present in the ELF bytes (python mmap, read-only), so the row is grounded on both.
3. Write {WAVE}/ScoutUpstream/SOURCE_ROW.md containing the fields for ONE new SOURCES.md row: id S257,
   source (title + URL), kind `code`, tier `A`, scope (the bound of the project walk for `{{cwd}}/.agents/skills`),
   anchor (`packages/coding-agent/src/discovery/agents.ts`, line N, tag v18.15.0, sha256 …), teaches (one line),
   status `mined`, opened (access date), recheck `on-release`, used-by `corpus/knowledge/omp-root-semantics-round88.md`.
   No `|` inside any cell. Put the located quote in your report, not in the row.
4. Write {WAVE}/ScoutUpstream/receipts.txt with the exact commands and their observed output.
5. Write {WAVE}/SOURCE_READY (content: the sha256 of the fetched file).
Acceptance: the file was fetched and hashed, the bound line is quoted and located, the row fields are complete.
If the fetch fails, report the HTTP status and the error text verbatim and do not invent a row.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="scout", name="ScoutElfMap", prompt=f"""## ScoutElfMap — the ELF evidence for the binding token sets (feeds C1 conjunct 2, 3, 5)

Read-only. Use python mmap and re on {ELF} (sha256 must equal {ELF_SHA}; if not, stop and report).
1. For each of the 12 rows of {LANE}/verifiers/omp-skill-roots-semantics.tsv (read it at {TIP} with
   `git -C {LANE} show {TIP}:verifiers/omp-skill-roots-semantics.tsv`), record: the row's module, the module
   header offset (`// packages/<module>`), the reader quote's first offset, the `binary_quote` offset (conjunct 5),
   and the NEAREST join-token line that builds the root (a line carrying `join(` or `.join(` or `resolve(`).
   Name the token that the join line uses for the root literal or its declared variable. Write the table to
   {WAVE}/ScoutElfMap/ELF_MAP.tsv with header
   `root_pattern<TAB>module<TAB>module_offset<TAB>reader_offset<TAB>binary_quote_offset<TAB>join_line_token<TAB>binding_token_candidate`.
2. The six unledgered joins (round-87 `w3/ScoutPatternsR87/derived-roots.txt` § C, rows with no ledger
   entry: `~/.claude/skills` @173840218, `~/.codex/skills` @173882129, `~/.config/opencode/skills`
   @172785499, `<agent-plugin>/skills` @173778070, `<claude-plugin>/skills` @173851107, `~/.omp/plugins/node_modules/*`
   @166892485). For each, re-read its offset in the ELF and state whether it is a reader code line (join token
   present) or not. Write them as a second block in ELF_MAP.tsv under the comment `# unledgered`.
3. Write {WAVE}/ScoutElfMap/receipts.txt with the mmap commands and their observed lines.
4. Write {WAVE}/ELF_MAP_READY (content: sha256 of ELF_MAP.tsv) as soon as the table is complete.
Acceptance: 12 ledger rows plus 6 unledgered rows; every non-empty offset re-finds its quote in the ELF
(show the re-find as a receipt line); no fabricated quote — write NONE where no line exists and say why.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="executor", name="ExecLiveBound", prompt=f"""## ExecLiveBound — write the v2 omp root counter (C1 instrument; frozen predicate in plans/round-88.md § C1)

Write {LANE}/verifiers/check_omp_root_semantics_v2.py. The r87 counter stays untouched.
Implement exactly the frozen predicate: `python3 -B verifiers/check_omp_root_semantics_v2.py --rev <rev>`
prints `omp root semantics grounded N of 12` and `forgeries rejected M of 4`, exit 0 iff N == 12 and M == 4
and guards S1–S5 PASS; exit 1 on content fail; exit 2 could-not-evaluate.

Conjuncts (read § C1 of the plan for the exact wording):
1 pattern — as r87 (equal to the round-86 ledger pattern at <rev>, no `..`, no wildcard in the first segment).
2 reader — the reader quote occurs in the ELF on a line that carries a join token AND the row's binding token
  set. Binding token sets: take them from {WAVE}/ScoutElfMap/ELF_MAP.tsv (column binding_token_candidate) once
  ScoutElfMap writes {WAVE}/ELF_MAP_READY; you may start the file with the r87 ledger's rows and add the sets
  later, but the sets must be FROZEN in the file's first committed-looking version before any forged or honest
  world is scored by you. Record the sets in a comment block at the top of the counter with a sha256 of that block.
  Empty sets are refused.
3 module — the `// packages/<module>` header occurs and precedes the reader quote's first occurrence.
4 bound (LIVE) — compute the expansion set for `{{cwd}}/` rows from the probe cwd /home/u/proj/sub with HOME=/home/u
  (strictly below HOME: /home/u/proj/sub and /home/u/proj). Join the row pattern to each element, normalize,
  refuse any candidate that escapes the set or contains `..`. A `~/` row must produce only HOME-rooted candidates.
  Compare with the set the row's module code walks (for agents.ts use the walk-up bound in the upstream file
  that ScoutUpstream fetches to {WAVE}/ScoutUpstream/ when SOURCE_READY exists; until then encode the bound from
  the ELF quote at ScoutElfMap's offset and record that it is pending the upstream check).
5 binary — the row's binary_quote occurs verbatim in the ELF.
Guards: S1 read the ledgers from <rev> bytes (git show); S2 ELF sha256 equals the pinned value else exit 2;
S3 pattern column equal to the round-86 ledger's at <rev>; S4 --self-test prints `0 failure(s) over N
assertions` with N >= a floor row you add to verifiers/floors-registry.json (if the file exists; add one row
for this counter); S5 the ELF is opened read-only (mmap); the counter never execs it.
Forged-world arms the self-test must include (build them as in-memory ledgers, not scratch commits, so the
self-test runs anywhere): one arm per conjunct failure, the doc-quote arm (reader quote repeating a string-table
line), the `..` candidate arm, the walking-into-HOME arm, and a positive control (honest rows pass).
The four forged worlds of round 87 are measured by ExecForgeryWorlds, not by you.
Run `--self-test` and `--rev {TIP}`; write the observed lines to {WAVE}/ExecLiveBound/receipts.txt.
When the self-test prints `0 failure(s)`, write {WAVE}/C1_READY (content: sha256 of the counter file).
Report: the counter sha256, the self-test count, the N at {TIP} (must be 12 if your conjuncts are right — if it is
not 12, say which conjunct refuses which row and why; do not weaken a conjunct to reach 12).""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="executor", name="ExecForgeryWorlds", prompt=f"""## ExecForgeryWorlds — build the four round-87 forged worlds and measure the r87 counter (before) and v2 (after)

Only in scratch and {WAVE}/ExecForgeryWorlds/.
1. Read {LANE}/.ufo/waves/round-87/w3/CriticSemanticsR87/forgery-worlds.txt, attribution.txt and
   forgery-ledger-diffs.txt. Each world is a ledger edit against the tip ledger. Recreate the four worlds as
   scratch repos: `D={SCRATCH}/ExecForgeryWorlds/<world>/repo && git clone -q --shared {LANE} "$D"`, check out
   {TIP}, apply the edit to verifiers/omp-skill-roots-semantics.tsv, commit with an identity of
   `forgery <forgery@scratch.local>` ONLY inside $D, verify `git -C "$D" rev-parse --show-toplevel` equals $D first.
   Names: w_cross_row7, w_subdir_row9, w_misattr_row12, w_renderline_row6.
2. BEFORE: for each world run the r87 counter (`{LANE}/verifiers/check_omp_root_semantics.py`, copied into $D
   or run from the lane path with the world as --rev in $D) and record `omp root semantics grounded N of 12`
   and the exit code. Expected from round 87: 12 of 12 exit 0 on every world (M = 0 of 4). If any world does not
   read 12 of 12, record it exactly and say so; the do-nothing control must be measured, not assumed.
3. AFTER: wait for {WAVE}/C1_READY (poll every 120 s, up to 45 minutes). Then run the v2 counter
   (`{LANE}/verifiers/check_omp_root_semantics_v2.py`, copied as a file, never edited) on each world and on the
   honest tip. Record N, the forged-world rejection count M, exit codes and the first failing conjunct per row.
4. Write {WAVE}/ExecForgeryWorlds/matrix.tsv (world, r87_N, r87_exit, v2_N, v2_exit, first_failing_conjunct)
   and {WAVE}/ExecForgeryWorlds/receipts.txt with the commands and observed lines. Then write
   {WAVE}/FORGERY_READY (content: sha256 of matrix.tsv).
5. Remove every scratch repo you created (rm -rf the scratch dir) before you yield.
Acceptance: four worlds measured under both counters, the matrix committed under your wave dir. A world that
v2 accepts is a finding to report verbatim (with its conjunct trace); do not alter the world or the counter.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="executor", name="ExecMonotoneD5", prompt=f"""## ExecMonotoneD5 — write the v2 routed-repairs gate (C2 instrument; frozen predicate in plans/round-88.md § C2)

Write {LANE}/verifiers/check_r86_routed_repairs_v2.py. The r87 gate `check_r86_routed_repairs.py` stays untouched.
Predicate: `python3 -B verifiers/check_r86_routed_repairs_v2.py --rev <rev>` prints
`r86 routed defects closed N of 5`, exit 0 iff N == 5, exit 1 otherwise, exit 2 could-not-evaluate.
Items D1–D4: reproduce the r87 gate's logic for D1 (tip-catalogue and tip-registry receipts exist with the
frozen lines and the instruments are byte-identical between 04647b0f and <rev>), D2 (the validator sentence
`planner/distiller/labrat/Main are frozen-topology seats and can never be swarm lanes.` occurs in
~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs and SWARM_ROLES lacks planner), D3 (round-87 lesson `## Gate` holds
a row whose decision cell is `reject` with a reason of >= 8 words), D4 (plans/round-87.md names the boundary
`after the first candidate score`). Read these from <rev> bytes with git show; never from the worktree.
D5 (v2, the item this round changes), holds iff BOTH:
- (i) identity: `python3 -B verifiers/verify_corpus_integrity.py --json` run in a scratch clone of <rev> and in a
  scratch clone of {BASE} list the same SET of check names (nine names at both);
- (ii) monotone: the set of names whose verdict is DRIFT at <rev> is a SUBSET of the set at {BASE}.
Compute both in scratch clones (`git clone -q --shared {LANE} "$D"`, `git -C "$D" checkout -q <rev>`, verify the
toplevel first). Never run the integrity script in the lane tree for the scored value.

Controls (each a scratch clone, committed before you score the candidate; receipts under your wave dir):
- w_tip: <rev> = {TIP} → D5 PASS.
- w_healed: base {BASE} with the one report_dead red fixed → D5 PASS (ii holds, (i) holds).
- w_added_red: <rev> plus an unresolvable commit citation in a new lesson line → D5 FAIL via (ii).
- w_silenced: <rev> with one integrity check removed from the script → D5 FAIL via (i).
- monotone-only arm: the same w_silenced world scored by (ii) alone → PASS (this is why (i) exists; record it).
The gate's own --self-test must print `0 failure(s) over N assertions` and include one arm per control.
Write the file, run --self-test, run --rev {TIP}, and write {WAVE}/C2_READY (content: sha256 of the gate file)
after the self-test passes. Record the observed lines in {WAVE}/ExecMonotoneD5/receipts.txt.
Report the N at {TIP}; if it is not 5 of 5, say which item refuses and why. Do not repair the corpus, do not
re-record corpus-baseline.json, do not edit the integrity script.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="scribe", name="ScribeEntry", prompt=f"""## ScribeEntry — draft the round-88 knowledge entry (waits for the instruments)

Wait for {WAVE}/C1_READY, {WAVE}/C2_READY, {WAVE}/FORGERY_READY and {WAVE}/SOURCE_READY (poll every 120 s, up to 45 min).
Then write {LANE}/corpus/knowledge/omp-root-semantics-round88.md. Its first three lines are the provenance trio:
`source:` (the S257 row id and URL, plus the omp v18.15.0 ELF sha256 {ELF_SHA}), `verified-at:` ({TIP} and today's
date), `recheck:` (the two commands: `python3 -B verifiers/check_omp_root_semantics_v2.py --rev <rev>` and
`python3 -B verifiers/check_r86_routed_repairs_v2.py --rev <rev>`).
Body (≤ 160 lines): what the v2 counter grounds and how (the five conjuncts, the binding token sets and why they
exist); the four forged worlds and the matrix from {WAVE}/ExecForgeryWorlds/matrix.tsv (before 0 of 4, after the
measured M); the upstream bound from S257 with its located quote; the honest bounds (12 of the 18 surface roots
ledgered; the six unledgered joins listed from {WAVE}/ScoutElfMap/ELF_MAP.tsv; the r87 instruments kept frozen).
Every number carries its command (CORPUS.md: a count carries its command) and every negative carries its sweep.
Write no claim without its evidence pointer. Do not write `[x]` anywhere.
Write your draft summary to {WAVE}/ScribeEntry/summary.md and your final answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="scribe", name="ScribeSources", prompt=f"""## ScribeSources — the registry row S257 and the index rows

Wait for {WAVE}/SOURCE_READY (poll every 120 s, up to 45 min). Then:
1. Append the row S257 to the Registry table of {LANE}/corpus/SOURCES.md using the fields in
   {WAVE}/ScoutUpstream/SOURCE_ROW.md. The row MUST have exactly 11 cells (NF 13 with the outer pipes) and no
   `|` inside a cell. Place it after S256. Do not change any other row except if a change is logged in the lesson.
   Verify with `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
   (exit 0 required; warnings allowed; the W04 duplicate-url warnings are pre-existing).
2. In {LANE}/corpus/README.md: add one index row for `corpus/knowledge/omp-root-semantics-round88.md` and one
   § Frontier note (append only) stating what round 88 moved (the bound conjunct live; the forged-world matrix) and what
   stays held (the six unledgered joins; the 18-root surface). Index rows are claims: write them only when the file exists.
3. Run `python3 -B verifiers/verify_corpus_integrity.py --json` in the lane and record the before and after index
   check lines (`corpus.index.tracked_files`, `corpus.index.unindexed`) in {WAVE}/ScribeSources/receipts.txt.
   Do not change the expected counts in verifiers/corpus-baseline.json.
Write {WAVE}/ScribeSources/summary.md (what changed, with line numbers) and answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="scribe", name="ScribeLesson", prompt=f"""## ScribeLesson — the round-88 lesson, Q80, the LOG entry and the R87-D7 correction

Write {LANE}/corpus/lessons/round-88.md with these sections, in order: a provenance header (author, round, base
{BASE}, tip {TIP}); `## Gate` (candidates considered; admitted; rejected with reasons; for S257 the URL, the access
date, the sha256 and the ≤25-word located quote from {WAVE}/ScoutUpstream/SOURCE_ROW.md; the status and used-by
changes old→new, if any; `Spot-check result: pending — non-author closure`); `## Mistakes` with one row:
class · evidence pointer · captured-by · fix. The mistake is R87-D7: LOG.md line 3315 says C2 "verified, `5 of 5`"
while the tip reads `4 of 5` (receipt {LANE}/.ufo/waves/round-88/receipts/before-C2-tip.txt). Captured-by: none.
Fix: an appended correction entry in LOG.md (never an in-place edit). State that the fix must be shown able to fail:
the sweep `grep -n '5 of 5' LOG.md | grep 'C2'` is red before and green after the annotation; the L1 runs it.
Also `## Considerthese`: proposal 4 of /home/vgpnk/Projects/shokunin/kotoba-shokunin/considerthese/2026-10-26.md
("don't close a round before its falsify wave runs") is mined into a QUALITY criterion (Q80) below; proposal 3 is
carried, not landed.
Then `## Sources` (S257 only) and `## Assimilation: none` with its reason (merge/kotoba exists but its id space
collides with S256 and no staged theme matches this round's ground).
Append Q80 to {LANE}/corpus/QUALITY.md: "a round whose wave has no attack seat (reviewer, critic, mutation-tester)
closes provisional, not admitted; the round lesson names the attack seats." Cite the lesson path and this file's
considerthese line. Do not rewrite any existing criterion.
Append a round-88 entry to {LANE}/LOG.md summarizing the two claims as frozen and the forged-world and gate
controls by their command names (the numbers come from the receipts; you do not invent them). Append the R87-D7
correction entry naming line 3315's text. Use `cat >> ` only for the append-only files.
Write {WAVE}/ScribeLesson/summary.md (the line numbers you wrote) and answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="connector", name="Connector", prompt=f"""## Connector — sibling-overlap scan for the omp root semantics surface (read-only)

Scan the other lanes' committed corpus, PROVINCE.md and SKILL.md for any claim about omp skill roots, the omp
catalogue, or the omp ELF (read-only, `git -C <lane> grep -n` against each lane's HEAD, or grep the working trees
read-only): lanes live at /home/vgpnk/Projects/shokunin/<id>-shokunin for the ids in
/home/vgpnk/Projects/shokunin/MANIFEST.json and PROVINCE.md. Known neighbours: kumitate (dispatch tooling),
tameshi (fixture method), kaidoku (reverse engineering), revenger (artifact reverse engineering), tabi, kagi.
Report, per lane that matches, the file:line and whether it states a claim about omp's skill roots (absorb = no;
report = yes). Also report whether any other lane's counter reads the same ELF surface and would collide with
v2's binding token sets. Write {WAVE}/Connector/overlap.md and {WAVE}/CONNECTOR_READY (content: match count).
Do not edit any sibling. Answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="reviewer", name="ReviewerC1", prompt=f"""## ReviewerC1 — independent review of the v2 root counter (attack seat)

Wait for {WAVE}/C1_READY and {WAVE}/FORGERY_READY (poll every 120 s, up to 45 min). Then attack C1 without relying
on the executor's receipts:
1. Re-implement the bound conjunct independently in your scratch (from the plan's words only) and compare its
   verdict per row with the counter's; record any disagreement with both lines.
2. Check each binding token set is FROZEN in time: `git -C {LANE} log` of the file is empty for the working copy
   (the file is not yet committed), so compare the set's sha256 in the counter header with the set's content and
   the set's source in ELF_MAP.tsv. Report whether any set could have been tuned after a score (you cannot prove
   it from git; say so and name what evidence would).
3. Re-run the counter at {TIP} and on the four forged worlds through the matrix. Confirm each rejection's first
   failing conjunct is real (read the ledger diff, then the ELF bytes at the cited offset). A rejection by a generic
   failure (a crash, a missing file) does not count: report it as a blanket refusal.
4. Confirm the positive control: the honest ledger reads 12 of 12.
Write {WAVE}/ReviewerC1/review.md with a verdict per claim sub-item: agree / disagree / unprovable, each with
its command and observed line. Answer as JSON with the verdict per conjunct.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="reviewer", name="ReviewerC2", prompt=f"""## ReviewerC2 — independent review of the v2 routed-repairs gate (attack seat)

Wait for {WAVE}/C2_READY (poll every 120 s, up to 45 min). Then attack C2:
1. Re-derive D5(i) and D5(ii) independently: run `verify_corpus_integrity.py --json` in fresh scratch clones at {TIP}
   and {BASE}; compare the name sets and the DRIFT subsets with plain set arithmetic. Record the two lists.
2. Build one NEW world the executor did not list (for example: a second check removed while another check is
   healed; or a red that is renamed, not added) and say whether v2 D5 passes or fails it, and whether that verdict
   is correct. A passing dishonest world is a finding.
3. Confirm the silenced-check control really removes a check (diff the scripts) and that the monotone-only arm passes
   it (proving (i) is necessary). If the monotone-only arm fails it, the claim's rationale is wrong; report that.
4. Re-run D1–D4 at {TIP} and confirm they agree with the r87 gate's output.
Write {WAVE}/ReviewerC2/review.md with a verdict per item and each command with its observed line.
Answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="critic", name="CriticFalsify", prompt=f"""## CriticFalsify — falsify both frozen predicates before anyone trusts them

Read {LANE}/plans/round-88.md, then the round-87 closure {LANE}/corpus/lessons/round-87-verifier-spotcheck.md § 2 and § 6
(the routed defects). Your job is to find the cheapest world that reaches each frozen target WITHOUT the claimed work.
Specifically:
- C1: a ledger edit that the v2 counter accepts (N == 12 and M == 4 both met) while the claimed property is false.
  Try a forged reader quote that carries a join token and the binding token of its row but names a different
  root; a forged module header placed after the quote; a candidate that escapes HOME through a symlink-free
  path string. Each accepted world is a counter defect: report its exact construction and command.
- C2: a world where D5 v2 passes but a new red exists, or where a check is removed and the names still match
  (for example by renaming a check). Each is a finding.
- Consider the blanket-refusal failure mode for both: a counter that fails everything also satisfies M == 4 and
  D5 FAIL; the positive controls must be what stops it. Confirm the positive controls exist and fail when broken.
Build each attack in your scratch, never in the lane. Report: survivors with construction, the honest bound each
survivor becomes, and which survivor should block admission. Write {WAVE}/CriticFalsify/attacks.md; answer as JSON.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="mutation-tester", name="MutTesterV2", prompt=f"""## MutTesterV2 — mutate the two v2 instruments; every mutant must be killed (attack seat)

Wait for {WAVE}/C1_READY and {WAVE}/C2_READY (poll every 120 s, up to 45 min). Work in scratch copies only.
C1 mutants of verifiers/check_omp_root_semantics_v2.py (each a copy, one change):
 m1 drop conjunct 4 (the live bound); m2 drop conjunct 5 (binary_quote); m3 empty the binding token sets (must be refused);
 m4 accept `..` candidates; m5 skip S5 (the mmap read) or exec the ELF; m6 return exit 0 when N < 12;
 m7 compare the forged-world count against 0 instead of 4.
C2 mutants of verifiers/check_r86_routed_repairs_v2.py: n1 drop (i); n2 drop (ii); n3 invert the subset to a superset;
 n4 exit 0 on D5 FAIL; n5 hardcode D5 PASS; n6 read the tip integrity script from the worktree instead of the rev.
For each mutant run its --self-test and the controls (C1: the four worlds plus the honest tip; C2: the four controls)
and record KILLED (a named arm or control fails) or SURVIVED. Report survivors with the arm that should have caught
them and whether the frozen predicate allows the survivor. Scratch dirs removed before you yield.
Write {WAVE}/MutTesterV2/mutants.tsv and {WAVE}/MutTesterV2/report.md; answer as JSON with the kill count.""",
         solutionSpace="one wave item, spec in task text"),
    dict(role="sentinel", name="Sentinel", prompt=f"""## Sentinel — safety and scratch-discipline review of the new instruments (read-only)

Wait for {WAVE}/C1_READY and {WAVE}/C2_READY (poll every 120 s, up to 45 min). Review the two new files
{LANE}/verifiers/check_omp_root_semantics_v2.py and {LANE}/verifiers/check_r86_routed_repairs_v2.py and the
floors-registry row (if added) for:
- any exec, spawn or shell call that runs the omp ELF (only read-only mmap is allowed);
- any write outside the TMPDIR/--work scratch argument (the only permitted write is the scratch dir);
- any hardcoded /tmp, /var/tmp or home-directory write path (scratch discipline §7.4 of the operator directive);
- any read of credentials, environment dumps, or network access inside a counter;
- any use of `git` write commands, or `git` against the lane worktree (only `show` and `cat-file` at a rev);
- path handling that accepts `..` in a rev or a path argument.
Each finding: file:line, the construct, the risk, and whether it blocks admission. Confirm the instruments honour an
explicit scratch argument (run one with TMPDIR set to a scratch dir and verify nothing lands in /tmp).
Write {WAVE}/Sentinel/review.md; answer as JSON with the finding count and the blocking count.""",
         solutionSpace="one wave item, spec in task text"),
]


GODSPEED_DIRECTIVE = Path("/home/vgpnk/.agents/skills/godspeed/directive.md").read_text(encoding="utf-8")


def main() -> None:
    for it in ITEMS:
        it.pop("solutionSpace", None)
        it["prompt"] = GODSPEED_DIRECTIVE + "\n" + it["prompt"]
    spec = {
        "wave": "r88-w1",
        "milestone": "r88-w1: C1 v2 root counter forged-world rejection 4 of 4; C2 v2 routed gate D5 identity+monotone; 4 attack seats",
        
        "reportDir": ".ufo/waves/round-88/w1",
        "context": CONTEXT,
        "items": ITEMS,
    }
    out = Path(__file__).resolve().parent / "r88-w1-spec.json"
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    roles = {}
    for it in ITEMS:
        roles[it["role"]] = roles.get(it["role"], 0) + 1
    print(f"wrote {out} items={len(ITEMS)} roles={roles}")


if __name__ == "__main__":
    main()


