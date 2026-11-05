#!/usr/bin/env python3
"""Generate r89-w1-spec.json — kotoba round 89, one v1 wave, 12 seats (band 8-16)."""
import json

GS = """You are a Godspeed-enabled subagent.

1. **Name the axes.**
2. **Iterate cheap, in parallel.**
3. **Keep moves that improve any axis and harm none.**
4. **Don't aim — let the frontier walk itself.**

## IMMEDIATELY STOP ASKING CLARIFYING QUESTIONS. Execute tool calls concurrently in large batches. Do not serialize what can run in parallel. Do not output philosophical reasoning or verbose plans. Act directly via tool calls.
"""

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
W1 = LANE + "/.ufo/waves/round-89/w1"
RCPT = LANE + "/.ufo/waves/round-89/receipts"
SCRATCH = "/fast/scratch/hyaku/kotoba-r89"

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
in your item. Message only agent://KotobaR89 (never agent://all).
Host kernel: never write /proc/sys or run sysctl -w (a 2026-11-05 incident set user.max_user_namespaces=0
and broke every sandbox). If you need a kernel or host setting changed, report it in your final answer.
Processes: Kill only by the PIDs you started; contention cap (4 processes, 120 s per probe).
Attribution: never write under the lane identity or any "KotobaR89 (lane L1)" heading — your files and
LOG/lesson headings carry YOUR seat name only. Only the L1 commits, after the wave.
Security: never write a raw environment dump, credential or token anywhere; never read a secret store.
Tooling (operator 2026-10-19): you may install or upgrade tools that help the task. Read
/home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate). Record each install as
tool, version, channel, reason in your final answer. PACMAN IS PAUSED host-wide: no pacman transaction of
any kind (no -S, -Sy, -Syu, -U, -R); use uv tool, npx, or an official binary in ~/.local/bin, or report the need.
Final answer: a short JSON with files_written, evidence (commands and the observed lines), findings, risks.

## Frozen state (round 89, Linux host, omp 18.15.0)
Base (lane tip at plan draft commit): a5b3b15c00b1de5db321e4226a0a7db17340e605 (round-88 verifier spot-check).
Plan draft (committed): {LANE}/plans/round-89.md at 43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3 —
read it fully first. Its predicate sentences, targets, controls and kill rules are FROZEN: nobody edits
them (the L1 alone may append the freeze header/receipts at the freeze commit). A counter defect you find
is a FINDING reported in your answer; do not rescue a counter by changing its predicate.
The round-88 instruments are FROZEN and stay byte-identical: verifiers/check_r86_routed_repairs_v2.py,
verifiers/check_omp_root_semantics_v2.py, verifiers/verify_corpus_integrity.py, verifiers/corpus-baseline.json.
Never edit them.
Before-state receipts (committed): {RCPT}/census-before.txt, before-c1-absence.txt, before-v2-selftest.txt.
Round-88 evidence (readable, committed): {LANE}/.ufo/waves/round-88/ (w1/ExecMonotoneD5.md F1,
w1/ReviewerC2/review.md C2-S2/S3, receipts/before-C2-tip.txt, c1-forged-matrix.txt) and
{LANE}/corpus/lessons/round-88-verifier-spotcheck.md (routed defects 1-6).

## File ownership (one writer per production file; no two seats write the same file)
ExecFreezeGate owns verifiers/check_freeze_gate.py, everything under verifiers/fixtures/freeze-gate/,
and verifiers/floors-registry.json (adds ONLY its own freeze_gate row; never rewrites other rows).
ExecD5Gate owns verifiers/check_r86_routed_repairs_v3.py and everything under verifiers/fixtures/d5v3/.
ExecCtlWorlds writes only under {W1}/ExecCtlWorlds/, {RCPT}/ (ctl-*.txt receipts) and its scratch.
ScoutSource, Connector, ReviewerFreezeGate, ReviewerD5Gate, CriticFalsify, MutTesterGates write only
under {W1}/<their-seat-name>/.
ScribeEntry owns corpus/knowledge/freeze-gate-round89.md and corpus/knowledge/instance-d5-round89.md.
ScribeSources owns corpus/SOURCES.md (rows S258, S259 only) and corpus/README.md (index rows + one
append-only Frontier note).
ScribeLesson owns corpus/lessons/round-89.md, corpus/QUALITY.md (criterion Q81 row only) and LOG.md
(its round-89 entry appended at the file end, headed with its seat name).
The L1 integrates plans/, SCORECARD.md, SKILL.md (registry rows) and the commits. Nobody else edits those.

## Handoff files (poll every 120 seconds with `sleep 120`, up to 45 minutes; if one never appears, report on what exists and say so)
{W1}/SOURCE_READY   — ScoutSource, after both source records are complete (content: the two S-ids).
{W1}/FG_READY       — ExecFreezeGate, after the gate's --self-test passes (content: the script sha256).
{W1}/D5_READY       — ExecD5Gate, after the v3 gate's --self-test passes (content: the script sha256).
{W1}/CTL_READY      — ExecCtlWorlds, after the five control polarities are recorded.
{W1}/ENTRY_READY    — ScribeEntry, after both knowledge entries are written.
{W1}/CONNECTOR_READY — Connector, after its sibling scan is complete.

## Instrument conventions
Python stdlib only; `python3 -B`; honour TMPDIR and accept a scratch/--work argument; exit ladder 0 pass,
1 content fail, 2 could-not-evaluate (3 = invalid spec where the plan declares it); `--self-test` prints
`0 failure(s) over N assertions`. Every self-test assertion names the arm it guards. No network inside a
counter; no writes outside named paths; rev-scoped reads go through `git show <rev>:<path>`, never a
second working tree inside the lane.
"""

items = []

items.append({
    "role": "scout",
    "name": "ScoutSource",
    "prompt": GS + f"""## ScoutSource — open the two SOURCES rows S258 and S259 (round-89 §2b)

1. **S258 (external).** Open a preregistration-methods primary source grounding the freeze-before-data
   principle (claim C1's sourced row). Try, in order, stopping at the first HTTP-200 success:
   (a) https://pmc.ncbi.nlm.nih.gov/articles/PMC5813543/ (Nosek, Ebersole, DeHaven, Mellor,
   "The preregistration revolution", PNAS 115(11), 2018, open access);
   (b) https://www.pnas.org/doi/10.1073/pnas.1708274114 ;
   (c) https://doi.org/10.1073/pnas.1708274114 .
   Fetch with curl (set a browser-like User-Agent if 403), save the bytes under
   {W1}/ScoutSource/s258.html (or .pdf/.txt per content type). Record: final URL, HTTP status,
   access date 2026-11-05, byte count, sha256 of the saved bytes, and TWO candidate located quotes,
   each <= 25 words, each with its location (section/heading or paragraph), one on preregistration
   distinguishing confirmatory from exploratory research, one on the timing of design/analysis
   registration relative to outcomes. If every route fails, record each failure (status/error text)
   honestly — S258 then does not exist and C1's sourced leg rests on S259 alone; do not fabricate.
2. **S259 (own-work).** Verify the round-88 spot-check bytes: `git -C {LANE} show
   a5b3b15c00b1de5db321e4226a0a7db17340e605:corpus/lessons/round-88-verifier-spotcheck.md | sha256sum`,
   and locate routed defects 3 and 4 (`grep -n 'freeze-gate\\|Freeze gate\\|instance-level'` on the same
   bytes). Produce one <= 25-word located quote for the freeze-gate requirement (defect 3) with its line
   number.
3. Write {W1}/ScoutSource/SOURCE_ROW.md carrying, for each row: id, title-canonical URL (S259: the repo
   path + commit as the own-work locator), kind (paper | own-work), tier proposal with scope sentence,
   anchor (section/line + revision), the quote(s) with locations, sha256, access date, and a one-line
   `teaches` proposal. Copy the fetch command transcript to {W1}/ScoutSource/receipts.txt.
4. Write {W1}/SOURCE_READY (content: the two ids, e.g. "S258 S259", or "S259" if S258 failed).
""",
})

items.append({
    "role": "executor",
    "name": "ExecFreezeGate",
    "prompt": GS + f"""## ExecFreezeGate — write the freeze gate (C1 instrument; frozen predicate in plans/round-89.md § C1)

Write {LANE}/verifiers/check_freeze_gate.py. Python stdlib only, `python3 -B` style.
1. Implement exactly the frozen predicate: `--self-test` prints `0 failure(s) over N assertions`
   (N >= 24) exit 0; `--plan <file>` parses `## Controls` blocks whose entries are
   `- control <name>: <command>` followed by `expect: exit <rc>[; stdout contains <literal>]`;
   runs every declared control with cwd={LANE}, TMPDIR set to a fresh dir under the process TMPDIR
   (never a hardcoded /tmp path), timeout 120 s per control, captures stdout; compares declared vs
   observed. Exit 0 = all held; 1 = refused naming the first violated control with declared-vs-observed
   text; 2 = could-not-evaluate (command missing/not executable/timeout); 3 = invalid spec (control
   with no command or no expect, or an empty controls block).
2. Build the two committed fixtures under {LANE}/verifiers/fixtures/freeze-gate/:
   sim-*.sh simulators grounded in committed round-88 receipts (fail-closed: each simulator greps the
   named receipt under {LANE}/.ufo/waves/round-88/ and prints the OBSERVED world verdict it records;
   a missing receipt exits 2). Ground at least: plans/round-88.md § C2 (the four declarations),
   .ufo/waves/round-88/w1/ExecMonotoneD5.md F1 (w_added_red observed PASS), .ufo/waves/round-88/w1/
   ReviewerC2/review.md (C2-S2/S3), .ufo/waves/round-88/receipts/before-C2-tip.txt.
   r88-controls.md declares what the r88 freeze expected (w_added_red: `expect: exit 0; stdout contains
   D5=FAIL` — the unsatisfiable declaration); r88-controls-fixed.md declares the observed verdicts for
   all four controls (w_added_red D5=PASS, w_silenced D5=FAIL-world-unreachable as recorded, w_healed
   PASS, w_tip PASS) so the same gate holds. The unsatisfiable arm MUST refuse (exit 1 naming
   w_added_red); the fixed arm MUST hold (exit 0).
3. `--self-test` arms (every one names its arm): full-hold fixture exit 0; the r88-controls.md world
   exit 1 naming w_added_red; the fixed world exit 0; expectation-sign flip exit 1; omitted-control
   plan exit 3; missing-command control exit 2; malformed declaration exit 3; empty block exit 3;
   stdout-pattern miss exit 1; timeout path exit 2 (a `sleep 200` control with a 120 s cap may be
   shortened via an internal constant the self-test overrides — no 200 s waits); TMPDIR honoured (the
   gate records its TMPDIR in verbose mode; a self-test arm asserts no /tmp literal in the source).
4. Add the row `freeze_gate` to {LANE}/verifiers/floors-registry.json (floor = N; add the key, never
   rewrite other rows; validate JSON parses afterwards).
5. Receipts under {W1}/ExecFreezeGate/: self-test output, the three predicate arms' runs with exit
   codes, sha256 of the script and of each fixture. Write {W1}/FG_READY (content: the script sha256).
""",
})

items.append({
    "role": "executor",
    "name": "ExecD5Gate",
    "prompt": GS + f"""## ExecD5Gate — write the instance-level D5 successor gate (C2 instrument; frozen predicate in plans/round-89.md § C2)

Write {LANE}/verifiers/check_r86_routed_repairs_v3.py. First read the frozen v2 gate
verifiers/check_r86_routed_repairs_v2.py and verifiers/verify_corpus_integrity.py (both stay
byte-identical). Python stdlib only.
1. Carry D1–D4 from v2 unchanged in meaning (reimplement; cite the v2 line in a comment per check).
2. Implement D5 exactly per the frozen predicate:
   `--write-base-receipt <path>` runs `python3 -B verifiers/verify_corpus_integrity.py --json` with
   cwd={LANE}, pins: the lane HEAD revision, sha256 of verifiers/verify_corpus_integrity.py and
   verifiers/corpus-baseline.json (computed on the working-tree bytes), and the full observation dict
   (all nine checks with live values); writes the JSON receipt.
   `--base-receipt <receipt> [--root <dir>] [--print-observation]` re-measures (default root = the
   lane; cwd = root) and compares: d5i the check-name list equals the receipt's AND the integrity
   script's `--self-test` exits 0 at the root; d5ii the DRIFT-name set is a subset of the receipt's;
   d5iii every name's observed value <= the receipt's value; snapshot the two pinned digests match the
   measured files, else `snapshot_tampered`. Prints `r86 routed defects closed N of 5` and
   `instance drift K`. Exit 0 iff N == 5 AND K == 0 AND digests match AND D1-D4 hold; exit 1 naming
   the first failing leg (d1..d4 | d5i | d5ii | d5iii | snapshot_tampered); exit 2 could-not-evaluate.
   `--print-observation` prints the measured observation dict (for the equivalence receipts).
3. Location discipline (Q79): all live measurements run with cwd = the measured root; the gate never
   writes anywhere except its optional receipt path; a root whose integrity self-test fails is
   could-not-evaluate for the comparison, never a silent verdict.
4. `--self-test` over hermetic fixtures under {LANE}/verifiers/fixtures/d5v3/ (micro observation
   dicts + synthetic receipt files written under the process TMPDIR, never /tmp literals): arms all
   hold exit 0; d5i fail (a check name renamed); d5ii fail (a new red name); d5iii fail (an added
   instance under an already-red name); healed red passes (value drops); re-recorded baseline
   (digest mismatch) fails as snapshot_tampered; silenced check (name removed) fails d5i; D1-D4
   import arms (one must-fail arm per carried check using synthetic inputs). Prints
   `0 failure(s) over N assertions`; every assertion names its arm.
5. Honours TMPDIR and accepts `--work <dir>` from birth; zero /tmp literals in the source.
6. Receipts under {W1}/ExecD5Gate/: self-test output, sha256 of the script. Do NOT write the lane's
   base receipt (the L1 writes it at the freeze commit). Write {W1}/D5_READY (content: the sha256).
""",
})

items.append({
    "role": "executor",
    "name": "ExecCtlWorlds",
    "prompt": GS + f"""## ExecCtlWorlds — execute the five declared controls + the v2-blindness receipt (before the freeze)

Wait for {W1}/D5_READY (poll every 120 s, up to 45 min). Work in
{SCRATCH}/ExecCtlWorlds/ (one dir; trap-clean it). The gate author must not be the control author:
build every world yourself from committed bytes.
1. Provisional base receipt at the plan-draft revision: in a pristine shared clone
   `D={SCRATCH}/ExecCtlWorlds/pristine && git clone -q --shared {LANE} "$D"`; verify
   `git -C "$D" rev-parse --show-toplevel` equals $D; check out 43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3
   detached (`git -C "$D" checkout -q 43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3` inside the clone only —
   allowed there, never in the lane); run
   `python3 -B verifiers/check_r86_routed_repairs_v3.py --write-base-receipt {SCRATCH}/ExecCtlWorlds/base-draft.json`
   with cwd=$D; record the receipt's digest + the observation dict.
2. Equivalence (Q79): on a second pristine clone at the same revision run
   `--base-receipt base-draft.json --print-observation`; diff the two observation dicts — must be
   identical (receipt ctl-equivalence.txt). If the checkout location flips any name (the known
   shape: bare fleet-root report paths, r88 ExecMonotoneD5 F2), record exactly which names and values
   differ — that is a FINDING; the gate's verdict for such a world is could-not-evaluate, and your
   receipt states it. Do not repair the gate.
3. Build the five worlds as deltas on the pristine clone (one clone per world, all at the draft
   revision; commits allowed inside scratch clones only, author `kotoba-worlds <kotoba@shokunin.local>`
   is NOT needed — use `git -c user.name=world-builder -c user.email=world@local commit`):
   w_added_instance: add one new corpus lesson line citing an unresolvable commit (a 41-hex garbage
   hash in backticks after the word commit).
   w_silenced: edit verifiers/verify_corpus_integrity.py in the world to skip one check (e.g. make
   CHECKS drop one entry).
   w_rerecorded: edit verifiers/corpus-baseline.json expectations to match the drifted live counts.
   w_healed: repair the one unresolvable commit citation (corpus/lessons/round-81.md:8) so it resolves
   or is annotated in a resolving form (the citation may be re-pointed at a resolvable object).
   w_tip: no delta (the pristine clone itself).
4. Run each world: `--base-receipt <base-draft.json> --root <world>`; record polarity:
   w_added_instance exit 1 naming d5iii; w_silenced exit 1 naming d5i and/or snapshot_tampered;
   w_rerecorded exit 1 naming snapshot_tampered; w_healed exit 0; w_tip exit 0. Copy each run's full
   output to {RCPT}/ctl-<world>.txt.
5. v2-blindness receipt: run the frozen v2 gate's `--self-test` and quote the w_added_red arm (reads
   PASS); additionally attempt a direct v2 run against w_added_instance (`python3 -B
   verifiers/check_r86_routed_repairs_v2.py --rev <world-head>` from the world clone) and record its
   honest output — if D1-D4 location effects make the direct run unreadable, record that; the
   self-test arm remains the blindness receipt. Copy to {RCPT}/ctl-v2-blindness.txt.
6. Copy the provisional base receipt to {RCPT}/d5v3-base-receipt-draft.json (the L1 writes the
   freeze-revision receipt later). Write {W1}/CTL_READY (content: the five observed polarities).
""",
})

items.append({
    "role": "scribe",
    "name": "ScribeEntry",
    "prompt": GS + f"""## ScribeEntry — draft the two round-89 knowledge entries

Wait for {W1}/SOURCE_READY, {W1}/FG_READY and {W1}/D5_READY (poll every 120 s, up to 45 min). Read
{LANE}/plans/round-89.md and the two instruments as built (verifiers/check_freeze_gate.py,
verifiers/check_r86_routed_repairs_v3.py) plus the seat records under {W1}/.
1. Write {LANE}/corpus/knowledge/freeze-gate-round89.md: opens with the provenance trio —
   `source:` citing the S258 row (URL + anchor) and the S259 row (repo path @ a5b3b15c...), using the
   exact ids/quotes from ScoutSource's SOURCE_ROW.md; `verified-at:` 2026-11-05 @ 43fc784...;
   `recheck:` the predicate command from plans/round-89.md § C1. Body: what the gate refuses and why
   (the r88 F1 class), the fixture design (declared-vs-observed simulators grounded in committed
   receipts), the exit ladder, bounds (what the gate does NOT check: it does not judge predicate
   soundness, only declared-vs-observed). No claim beyond what an instrument run shows.
2. Write {LANE}/corpus/knowledge/instance-d5-round89.md: provenance trio citing S259 (routed defect 4)
   with `verified-at:`/`recheck:` per the § C2 predicate. Body: name-level vs instance-level D5 (the
   v2 blindness with its receipt), the base-receipt design, the digest pins, the five controls, the
   Q79 location discipline, bounds.
3. Do NOT cite `.ufo/reports/round-89/kotoba.md` anywhere (the report does not exist yet).
4. Write {W1}/ScribeEntry/summary.md (short) and {W1}/ENTRY_READY (content: the two file paths).
""",
})

items.append({
    "role": "scribe",
    "name": "ScribeSources",
    "prompt": GS + f"""## ScribeSources — the registry rows S258/S259 and the corpus index rows

Wait for {W1}/SOURCE_READY and {W1}/ENTRY_READY (poll every 120 s, up to 45 min). Read ScoutSource's
SOURCE_ROW.md and the two knowledge entries.
1. Append exactly two rows to the Registry table of {LANE}/corpus/SOURCES.md, after S257, in the exact
   11-column shape of the existing rows (no `|` inside any cell): S258 (external paper; tier A scoped
   to the freeze-before-data claim discipline; anchor = the located section + access revision;
   teaches from the scout's grounded quote; status mined; opened 2026-11-05; recheck 180d; used-by
   corpus/knowledge/freeze-gate-round89.md) and S259 (kind own-work; source = the repo path
   corpus/lessons/round-88-verifier-spotcheck.md + commit a5b3b15c00b1de5db321e4226a0a7db17340e605;
   tier A scoped to the round-89 routed successor requirements; status mined; opened 2026-11-05;
   recheck 90d; used-by both new knowledge entries). If S258 failed to open, write only S259 and say
   so in your summary.
2. {LANE}/corpus/README.md: add index rows for the two new knowledge entries, corpus/lessons/round-89.md,
   and the previously unindexed corpus/lessons/round-88-verifier-spotcheck.md — copy the row shape of
   the existing round-88 rows (the FILE-column token must match the integrity instrument's pattern
   grammar; keep it a literal repo-relative path). Append one short round-89 note at the end of the
   Frontier section (append-only; what moved: the two instruments + the two rows; written before the
   claims are scored — no claim of admission).
3. Verify your own edit: `python3 -B verifiers/verify_corpus_integrity.py --json` with cwd={LANE} —
   `unindexed` must not grow vs the pre-edit value you recorded first (save that pre-edit output to
   {W1}/ScribeSources/receipts.txt). If your rows introduce unindexed/stale/missing findings, fix your
   own rows; never edit other files.
4. Write {W1}/ScribeSources/summary.md and {W1}/SOURCES_INDEX_READY (plain file, content: rows added).
""",
})

items.append({
    "role": "scribe",
    "name": "ScribeLesson",
    "prompt": GS + f"""## ScribeLesson — the round-89 lesson, criterion Q81, and the LOG freeze entry

Wait for {W1}/CTL_READY, {W1}/SOURCE_READY and {W1}/ENTRY_READY (poll every 120 s, up to 45 min). Read
{LANE}/plans/round-89.md fully, {LANE}/corpus/lessons/round-88-verifier-spotcheck.md, and the control
receipts under {RCPT}/.
1. Write {LANE}/corpus/lessons/round-89.md with sections in order:
   provenance header (`author: ScribeLesson (round-89 wave r89-w1, scribe seat)` — never a lane-identity
   heading; round 89; base a5b3b15c...; plan draft 43fc784...; tip: `TIP-REV` placeholder the L1 fills);
   `## Gate` — candidates considered: S258 (admit/reject per the scout's actual evidence; a failed
   fetch is an honest reject with the reason and the flip), S259 (admit), the two record corrections
   (admitted as mined mistakes), the considerthese review (proposals 2/3/5 of considerthese/2026-10-26.md
   reviewed, none taken: 2 is L0-blocked line 174, 3 and 5 do not fit the claim cap beside the two
   routed successors — each with its reason), the assimilation set (reject: 55 id collisions, L0 open);
   `## Mistakes` — exactly the two rows from plans/round-89.md § Record corrections, each
   class · evidence pointer · captured-by · fix, in the round-88 lesson's table shape;
   `## Sources` — the S258/S259 records (URL, access date, sha256, located quotes with line/section);
   `## Assimilation: none` — the 55-collision re-derivation and the open L0;
   `## Considerthese` — the review above. Follow Q76: every count names the artifact file it counts and
   carries its counting command.
2. Append criterion Q81 to the criterion table of {LANE}/corpus/QUALITY.md (append the row, never
   rewrite existing rows): "A filed report is never rewritten: a correction lands as an appended
   erratum naming the superseded text in a new commit; the filed bytes of a landed round report are
   immutable. | filed round reports and their fleet commits | the round-89 lesson § Mistakes row 1
   (fleet 5306df4 → d6c5ec57 rewrite, round-88 spotcheck routed defect 1) | —".
3. Append the round-89 freeze entry at the end of {LANE}/LOG.md (append-only; never edit existing
   bytes), headed `### Round 89 — freeze entry (ScribeLesson, wave r89-w1, pre-scoring)` — what is
   frozen (the two predicates, the five controls, the freeze protocol), the before-state receipts, and
   that candidate scores are not yet taken. No verdict language.
4. Write {W1}/ScribeLesson/summary.md (short).
""",
})

items.append({
    "role": "reviewer",
    "name": "ReviewerFreezeGate",
    "prompt": GS + f"""## ReviewerFreezeGate — independent review of the freeze gate (attack seat, C1)

Wait for {W1}/FG_READY (poll every 120 s, up to 45 min). Work in {SCRATCH}/ReviewerFreezeGate/ and
{W1}/ReviewerFreezeGate/. Attack C1 without trusting the author's receipts:
1. Re-run the three predicate arms yourself (self-test; --plan r88-controls.md must exit 1 naming
   w_added_red; --plan r88-controls-fixed.md must exit 0) and record outputs.
2. Forge attack plans (in your scratch, then commit the informative ones as fixture-world records under
   your wave dir): a plan declaring exit 0 on the refusing simulator (must refuse); a control whose
   command is `false` (must refuse naming it); a control whose expect declares the wrong stdout
   literal (must refuse); a plan with two controls where the second fails after the first passed (must
   name the SECOND); a control command that exits 2 unexpectedly (gate exit 2, not a silent pass);
   nondeterministic output (a command printing different text per run — the gate must be stable).
3. Verify the simulators are receipt-grounded: for each sim-*.sh, run it in a scratch copy of the lane
   with the cited receipt renamed away — it must exit nonzero (fail-closed), not print a verdict.
4. Read the gate source for escape hatches: any hardcoded /tmp, any path where a failing command is
   swallowed, any control skipped silently on parse quirks (indentation, CRLF, duplicate names —
   duplicate control names must be invalid spec, exit 3).
5. Write {W1}/ReviewerFreezeGate/review.md: verdict per attack (repelled | finding), with commands and
   observed lines. A finding is a defect report, never an edit to the gate.
""",
})

items.append({
    "role": "reviewer",
    "name": "ReviewerD5Gate",
    "prompt": GS + f"""## ReviewerD5Gate — independent review of the instance-level D5 gate (attack seat, C2)

Wait for {W1}/D5_READY and {W1}/CTL_READY (poll every 120 s, up to 45 min). Work in
{SCRATCH}/ReviewerD5Gate/ and {W1}/ReviewerD5Gate/. Attack C2 from the committed bytes:
1. Re-derive the five control polarities yourself from the ExecCtlWorlds receipts (each receipt's
   command, output and exit; the receipts live under {RCPT}/ctl-*.txt) and re-run at least
   w_added_instance and w_healed in your own clones.
2. Forge worlds beyond the declared controls (your own clones from the pristine revision): a renamed
   red check (d5i must fail); count shrink under one name plus one new red name (d5ii must fail);
   an added instance under a GREEN name (exit 1 via d5ii or d5iii — never 0); a receipt with a
   tampered digest (snapshot_tampered); a receipt whose observation dict is truncated (a missing name
   — must fail closed d5i, never treat missing as zero); two simultaneous deltas (healed one name,
   grew another — exit 1 naming the growth).
   ANY world where v3 exits 0 but the world is worse than the receipt is a FINDING.
3. Read the gate source for escape hatches: comparison direction flips (<= vs <), digest checks that
   only warn, names compared case-insensitively, values read from the wrong dict key, D1-D4 drift from
   the v2 semantics (diff the carried checks against v2's source and report any meaning change).
4. Write {W1}/ReviewerD5Gate/review.md: verdict per attack with commands and observed lines.
""",
})

items.append({
    "role": "critic",
    "name": "CriticFalsify",
    "prompt": GS + f"""## CriticFalsify — falsify the two frozen claims before anyone trusts them (attack seat)

Read {LANE}/plans/round-89.md, {LANE}/corpus/lessons/round-88-verifier-spotcheck.md (routed defects
1-6), {LANE}/corpus/QUALITY.md (Q25, Q26, Q37, Q47, Q63, Q76, Q79, Q80), and the round-87/88 lessons'
mistake rows. Work in {W1}/CriticFalsify/ (read-only over the lane otherwise).
1. Q26 headline audit, both claims: list every clause of each frozen predicate and name the arm that
   turns it on; a clause no arm turns on must be reported NOW (before data) as a narrowing demand.
   In particular check: does C1's "exit 1 naming w_added_red" clause have its arm; does C2's
   `instance drift K` print have an arm that pins its value at 0 vs >0.
2. Do-nothing controls: could a round that lands neither instrument reach either target? (C1: the
   absence receipt says no instrument exists — but could the OLD instruments satisfy the C1 predicate
   arms? Run the r88-controls.md fixture expectations mentally against check_r86_routed_repairs_v2.py's
   --self-test and say whether any pre-existing check already refuses that world.) (C2: v2 on the
   added-instance world — receipt it.)
3. Vacuity risk, C2: the landing adds no corpus bytes after the freeze, so "exit 0 at the landing tip"
   could be trivially met. Audit whether the five control polarities + the digest pins + D1-D4 make the
   gate non-vacuous, and name the cheapest world the gate must fail on for the claim to mean anything.
4. Kill rules: audit both kill rules and the freeze-protocol diff command
   (`git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus`) — name anything the
   diff path misses (e.g. fixtures outside those prefixes, floors-registry.json, SKILL.md registry
   rows changing semantics after a score).
5. Q80: name this wave's attack seats. Sourced-claim audit: C1 cites S258+S259 — verify from
   ScoutSource's record that the quotes exist and are <= 25 words with locations; a failed S258 fetch
   must be reported as an honest reject, never paraphrased into evidence.
6. Write {W1}/CriticFalsify/attacks.md: a verdict table per claim (attack stands | repelled) with
   commands/lines, and an explicit PRE-DATA narrowing list for the L1 (findings that must be fixed
   before the first candidate score).
""",
})

items.append({
    "role": "mutation-tester",
    "name": "MutTesterGates",
    "prompt": GS + f"""## MutTesterGates — mutate both new instruments; every declared mutant killed, equivalents survive (attack seat)

Wait for {W1}/FG_READY and {W1}/D5_READY (poll every 120 s, up to 45 min). Work ONLY in
{SCRATCH}/MutTesterGates/ (scratch copies of the lane; the lane originals are never touched).
Two-sided measure per Q47: every declared mutant killed AND every semantics-preserving equivalent
survives; equivalents are generated at measurement time, not a fixed published list.
1. Freeze-gate mutants (each killed = a committed fixture changes verdict under the mutant, observed
   exit differs from the frozen predicate): expectation-sign flip; control-skip (one control not run);
   exit-ladder swap (1<->2); parse mutation dropping `stdout contains` clauses; duplicate-name
   acceptance (must stay exit 3).
2. D5 gate mutants (each killed against the ExecCtlWorlds fixture worlds — rebuild the needed world in
   your scratch or reuse the receipts' recipes): d5iii removed (w_added_instance then passes = killed
   by polarity); digest check removed (w_rerecorded passes); subset test flipped to superset
   (w_added_instance or the new-name world passes); instance comparison < instead of <= (w_healed or
   w_tip false-red = killed by the PASS polarity); D1-D4 dropped (the honest tip then reads N<5 —
   killed by the w_tip polarity if it changes N's meaning; record what actually changes).
3. Equivalents (must survive — exit codes unchanged on the honest fixtures): reorder the controls
   dict; rename locals; reformat the expect-line parser (same accepted grammar); move helper functions.
4. Write the two-sided table to {W1}/MutTesterGates/mutants.tsv (mutant | file | killed-by-fixture |
   observed exit before/after) and equivalents.tsv. Copy run transcripts under your wave dir.
""",
})

items.append({
    "role": "connector",
    "name": "Connector",
    "prompt": GS + f"""## Connector — sibling-overlap scan for the freeze-gate / instance-drift / preregistration ground (read-only)

Read-only. For each sibling lane repo under /home/vgpnk/Projects/shokunin/<id>-shokunin (skip kotoba
itself), run read-only greps against the working tree (`grep -rn --include='*.md' -l` and targeted
`grep -n`) for: freeze gate / pre-freeze control execution / preregistration; instance-level drift or
(name, observed) tuple gates; routed-repairs successor gates; "controls executed before the freeze".
1. Classify each hit: owns the ground (a sibling's own instrument does this) | cites it | no ground.
   Quote each hit with path:line (short, <= 25 words per quote).
2. Specifically check chousa (research method — does preregistration-as-a-source belong to its
   province?) and tameshi (fixture and mutation method — does the mutation battery on the new gates
   overlap its method ground?). kotoba cites chousa's method and never re-derives it; if S258's
   preregistration principle is method ground, flag the boundary for the round report.
3. Write {W1}/Connector/overlap.md (table: lane | hit | classification | quote) and
   {W1}/CONNECTOR_READY (content: done + any contested finding).
""",
})

spec = {
    "wave": "r89-w1",
    "milestone": "r89-w1: C1 freeze gate refuses the r88 unsatisfiable control; C2 instance-level D5 with five pre-freeze control polarities; 4 attack seats",
    "reportDir": ".ufo/waves/round-89/w1",
    "context": CONTEXT,
    "items": items,
}

with open(f"{LANE}/.ufo/waves/round-89/r89-w1-spec.json", "w") as f:
    json.dump(spec, f, indent=1, ensure_ascii=False)
print("wrote spec:", len(items), "seats")
