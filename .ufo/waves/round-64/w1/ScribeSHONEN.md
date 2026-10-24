# ScribeSHONEN — SHONEN.md four-box verification and refreshed anchors (round 64, wave 1)

Role: scribe, leaf. Scope: verify each of the four `SHONEN.md` boxes' evidence
pointers resolve at the dispatch base `078eec4`, and deliver the four refreshed
anchor lines the L1 writes when the round-64 lands move a pointer. Read-only
outside this file; no git/jj writes; no production edits; no reruns of seat
work. No tool installs were made (no channel used).

Provenance of every number below: lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base at dispatch `078eec4` = `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`; measured
tip `c04fffbe` = plan freeze (the only commit above base). Command output pasted
as run; exit codes as printed.

```
$ git rev-parse HEAD
c04fffbeafcaf810897258d56f99cca736ed3a91
$ git log --oneline -3
c04fffbe round-64: freeze plan — C1 G7 span_missing pinning arms (219->223), C2 r63 routed defects counter (4 of 4); two v1 waves 32+32
078eec4 round-63 verifier spot-check (integrator, hyaku): non-author admit/reject
38defdc round-63: post-close MutW2SplitClauses E3 paperwork verification update
$ git diff --stat 078eec4 c04fffbe -- LOG.md SKILL.md PROVINCE.md corpus/ SHONEN.md
(empty — every surface below is byte-identical at base and tip)
$ sha256sum of SHONEN.md at 078eec4 / c04fffbe / working tree
35f048eef3a414b8b479deda7100aa960e3384761b8053b7e38354c85fb4b069  (all three)
```

`SHONEN.md` is 12 lines; each box is one bullet line plus one physical
`evidence:` line (lines 5–12). All four bullets are `[~]` and none is `[x]`.

## Box-by-box verification at 078eec4 / c04fffbe

### Box 1 — SKILL.md contains real decision tables, error patterns, checklists, cited sources

Pointer set, each checked:

```
$ git cat-file -e 078eec4:.ufo/round-46/scouts/B2.md ; echo exists
exists
$ git show 078eec4:.ufo/round-46/scouts/B2.md | grep -n "41 checklist"
44:`SKILL.md` SHA-256 `0404fdc0…`, 521 lines against the 600-line budget. Recount: 41 checklist items (15/9/9/8), seven anatomy-table data rows, five decision-table data rows, and 38 Sources entries. …
$ git show 078eec4:corpus/knowledge/anatomy-and-compression.md | sed -n '100,110p'
## Decision tables — when to use one
| Situation | Table? | Evidence |
|-----------|--------|----------|
| Intent → command/route mapping | Yes: `Intent | Command | Notes` | bailian-cli … |
| Request classification … | Yes: `Class | Pattern | Action` | bailian-protocol … |
| Flag → effect reference | Yes: `Flag | Effect` | sekhmet-l3 |
| Ordered pipeline | No — numbered steps or ASCII chain | bailian-finetune 7-step chain |
| One conditional | No — one sentence | — |
   (5 decision-shape data rows at :104-108, inside the cited :102-108 span — holds)
$ git show 078eec4:SKILL.md | sed -n '241p'
Decision-table shape (situation → table or plain steps) and the action-cell rule — every row needs an action cell (…): `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Decision tables (round 57), verbatim.
$ git show cbbee56e:SKILL.md | awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' | wc -l
18
$ git show 078eec4:SKILL.md | awk '…same…' | wc -l
18
$ awk '…same…' SKILL.md | wc -l          # working tree = c04fffbe
18
$ git show 07c33d73:SKILL.md | awk '…same…' | wc -l   → 33
$ git show c63ccc68:SKILL.md | awk '…same…' | wc -l   → 20
$ git show 078eec4:SKILL.md | wc -l                   → 598
```

Every cited figure resolves. The `SKILL.md:241` pointer is still line 241 at
`c04fffbe` (`SKILL.md` byte-identical, 598 lines), and `anatomy-and-compression.md:102-108`
still holds the five decision rows. **Verdict: box 1's current evidence line is
true at the measured tip — only the gate-registry count is expected to move this
round** (see Finding F4).

Live registry measurement (not currently cited by the box; recommended addition):

```
$ python3 -B verifiers/check_gate_registry.py --rev 078eec4 | tail -1
gate registry rows conformant 41 of 41 lane verifiers; phantom 0
$ echo $?
0
$ python3 -B verifiers/check_gate_registry.py --rev c04fffbe | tail -1
gate registry rows conformant 41 of 41 lane verifiers; phantom 0
$ git ls-tree 078eec4 verifiers/ | awk '$4 ~ /\.(py|sh)$/' | wc -l
41
$ git show 078eec4:SKILL.md | awk '/^## Gate registry/{p=1} p && /^\| `verifiers\//{c++} END{print c+0}'
41
```

### Box 2 — At least one end-to-end domain task executed and logged in LOG.md

```
$ git cat-file -e 078eec4:corpus/knowledge/cold-run-round11.md ; echo exists
exists
$ git show 078eec4:corpus/knowledge/cold-run-round11.md | head -6
# Cold run — `verifiers/verify_corpus_integrity.py` — round 11
**NON-AUTHOR cold run.** The runner (lane `ColdRunRecord`) did **not** author
`verifiers/verify_corpus_integrity.py` …
$ git show 078eec4:LOG.md | grep -n 'cold-run-round11'
287:  ids. Non-author cold run (`corpus/knowledge/cold-run-round11.md`): runner
294:  `corpus/knowledge/cold-run-round11.md`, `corpus/lessons/round-11.md`,
342:  … Both repairs are declared in `corpus/knowledge/cold-run-round11.md` §7, …
```

Pointer resolves and the task is logged at three `LOG.md` sites. **Verdict:
box 2 holds as `[~]`.** Caveat already correct in the fleet protocol: the runner
was lane-dispatched, so this is lane evidence, not non-author credit
(`../PROTOCOL.md` § Promotion gates, line 61–63: "a subagent the lane dispatched
is still the lane"). The current evidence line does not claim otherwise; the
refreshed line adds the LOG line numbers so the logging half of the gate is
checkable.

### Box 3 — Instructions executable by an agent without oral context

This is the box whose **anchor claim is falsified**, not merely moved.

```
$ git cat-file -e 078eec4:corpus/lessons/round-8-aggregator-box3-coldrun.md ; echo exists
exists
$ git show 078eec4:corpus/lessons/round-8-aggregator-box3-coldrun.md | sed -n '36,37p'
| B1 | :168-170 | "read … the newest `<skills>` block …" — newest-mtime session file carries 0 `<skills>` blocks … (the verifier brute-scans all) | not-found |
| B2 | :618-620 | `fault_injection_corpus.sh` sits in the runnable-verifier list with no mutating-gate warning … | ambiguous |
$ git show 078eec4:corpus/lessons/round-8-aggregator-box3-coldrun.md | sed -n '78p'
Grade impact: **none.** The verdict stays `[~]` on B1 + B2 — a counted gate does not repair the newest-block recipe gap (B1) or the unlabeled-mutator ambiguity (B2); with the gate now counted, the remaining `[~]` driver is B1 alone (B2's executability confusion survives the gate count). Verdict does not default to `[~]` on the refusal; the refusal is credited, the recipe gap stands.
$ git show 078eec4:corpus/lessons/round-8-aggregator-box3-coldrun.md | sed -n '100,103p'
## kotoba reconciliation (round 13, 2026-09-28)
Presentational only — no verdict, count, or quotation above was changed. Three
pointer sites were repaired because `python3 verifiers/verify_corpus_integrity.py`
flagged them on the landed tree (`report_dead=3`) …
$ ls corpus/knowledge/ | grep -i cold
cold-run-round11.md
```

**Finding F1 (calibration defect in `SHONEN.md` itself).** The box-3 evidence
line says the defects were "both fixed in round 13". The cited file contradicts
that at two points: the round-13 pass is "presentational only — no verdict,
count, or quotation above was changed" (three pointer sites repaired), and
`round-8-aggregator-box3-coldrun.md:78` states in terms that "the recipe gap
stands". Nothing later closes B1; `corpus/knowledge/` holds exactly one cold-run
record (`cold-run-round11.md`, round 11), so "no fresh non-author re-run since"
remains true. The refreshed line withdraws the "both fixed" wording — the box
stays `[~]`, which is what the file and the fleet protocol both support.

### Box 4 — No cross-domain bleed (PROVINCE.md still accurate)

```
$ git cat-file -e 078eec4:.ufo/round-46/scouts/w2-connector.md ; echo exists
exists
$ git show 078eec4:PROVINCE.md | grep -n '^## '
8:## Core
28:## Frontier
35:## Adjacent
$ git show 078eec4:PROVINCE.md | sed -n '35,37p'
## Adjacent
(blank)
Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census
$ git show 078eec4:PROVINCE.md | wc -l
67
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
$ echo $?
0
```

Heading `:35` and rewrite sentence `:37` hold at base; the worktree bytes equal
`078eec4` for `PROVINCE.md`, the census file and the guard (`git diff --stat`
empty), so the guard's output is the base-tip measurement. **Verdict: box 4
holds as `[~]`.** The line numbers are the round's most fragile pointer: round 63
appended one line to `§ Frontier` twice (`cbbee56`, `849a546`), each time pushing
`## Adjacent` down. Any round-64 append above line 35 moves both numbers.

**Finding F2 (live governance red, outside the four boxes but on the same
pointer-hygiene surface).** At `c04fffbe` (= base bytes) the lane's own checklist
gate is red:

```
$ python3 -B verifiers/verify_skill_checklist.py --json
… "detail": "LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; LOG.md:2580: '.ufo/watchdog.log' does not resolve from …; SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve from …; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused",
    "id": "governance.citation_resolves", "status": "FAIL"
  ], "exit_code": 1, "fail": 1, "na": 0, "pass": 10
$ ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md
-rw-r--r-- 1 vgpnk vgpnk 11849 Oct 23 15:24 /home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md
```

All three are fleet-repo paths written in the bare lane-relative form — the
M95/M96 citation class the round-8 lesson already documents ("the round-12
pointer is now the host-absolute shape"). The files exist on the host, so this
is a form defect, not a lost artifact. It does not falsify any of the four boxes
(the failing citations are in `LOG.md`/`SCORECARD.md`, not in SKILL.md
instructions or PROVINCE.md), but it is a base-tip red the L1 should either fix
in the round-64 LOG corrections block or route explicitly. [INFERENCE] the
round-47 `GOVERNANCE_ERRATA` horizon (line 2315) does not cover lines 2533/2580.

## The four lines the L1 should write (verbatim)

Replacement for `SHONEN.md` lines 5–12 (four bullets + four `evidence:` lines;
`[~]` throughout, no `[x]` — promotion is operator-owned per `../PROTOCOL.md` §
Promotion gates and the r63 spot-check's item 6). Placeholders in `<…>` are the
only tokens to resolve at the landed tip; every other number is measured.

```markdown
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  evidence: `.ufo/round-46/scouts/B2.md:44` (SKILL.md inventory at the round-46 tree: 7 anatomy rows, 5 decision rows, 41 checklist boxes 15/9/9/8, 38 Sources entries; lane-run). Recount: the 5 decision-shape rows are `corpus/knowledge/anatomy-and-compression.md:102-108`, pointer `SKILL.md:241` (both unchanged at `c04fffbe`; `SKILL.md` byte-identical to `078eec4`, 598 lines); § Sources holds `<SOURCES_ENTRIES>` top-level entries at `<TIP>` — `awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md | wc -l` printed 18 at `c04fffbe` (18 at `cbbee56e`, 20 at `c63ccc68`, 33 at `07c33d73`); gate registry `python3 -B verifiers/check_gate_registry.py --rev <TIP>` prints `gate registry rows conformant <REG_ROWS> of <REG_ROWS> lane verifiers; phantom 0`, exit 0 (41 of 41 at `c04fffbe`; `<REG_ROWS>` = `<42>` iff `verifiers/check_r64_routed_repairs.py` is registered in `SKILL.md` § Gate registry)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  evidence: `corpus/knowledge/cold-run-round11.md` (corpus-integrity verifier red-before → green-after, cold run by a lane-dispatched reviewer — lane evidence per `../PROTOCOL.md` § Promotion gates, no non-author credit claimed); logged at `LOG.md:287,294,342` at `078eec4` (cold-run record and the artifacts list)
- [~] Instructions executable by an agent without oral context
  evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md` (only cold run on record: `[~]` on break points B1 newest-block recipe under-determined — `:36` — and B2 unlabeled mutating harness — `:37`; the round-13 pass `:100` was "presentational only — no verdict, count, or quotation above was changed", and `:78` records that with the gate counted "the recipe gap stands"; the earlier "both fixed in round 13" wording is withdrawn here as falsified; no fresh non-author cold run since — `corpus/knowledge/` holds one cold-run record)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  evidence: `PROVINCE.md` § Adjacent (round 46 sibling-overlap scan `.ufo/round-46/scouts/w2-connector.md`; section rewritten round 49 from `corpus/knowledge/sibling-overlap-census-round49.md`; at `c04fffbe` `grep -n '^## Adjacent' PROVINCE.md` prints `35:` and the rewrite sentence is `:37` — a round-64 append above it moves both, so re-grep and set `<ADJ_LINE>`/`<ADJ_REWRITE_LINE>`; the guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` prints `rows 20 verified 20` / `province rows 20 matched 20`, exit 0)
```

Placeholder resolution rules (for the L1, at the landed tip):

| Token | Value now (`c04fffbe`) | Expected after the round-64 lands | Command |
|---|---|---|---|
| `<TIP>` | `c04fffbe` | the round-64 data tip | `git rev-parse --short=8 HEAD` |
| `<SOURCES_ENTRIES>` | 18 | 18 unless a bullet is added to SKILL.md § Sources — S120 lands in `corpus/SOURCES.md`, which is not the counted surface | the awk in the line |
| `<REG_ROWS>` | 41 | `<42>` if the new counter gets its § Gate registry row; 41 otherwise | `check_gate_registry.py --rev <TIP>` last line |
| `<ADJ_LINE>` / `<ADJ_REWRITE_LINE>` | 35 / 37 | shift by +N for each line appended to § Frontier | `grep -n '^## Adjacent' PROVINCE.md` and `grep -n 'Rewritten round 49' PROVINCE.md` |

## Findings (claim mapping)

- **F1 supports/refines box 3; falsifies the box-3 anchor's "both fixed in
  round 13" clause.** Evidence as pasted above (`:78`, `:100-103`). No box
  promotion: the box remains `[~]`.
- **F2 (new red at base) supports C2's defect class, not C1.** `verify_skill_checklist.py
  --json` exit 1, `pass 10 / fail 1`, `governance.citation_resolves` FAIL over
  `LOG.md:2533,2580` and `SCORECARD.md:158`. Not one of the four SHONEN boxes;
  routed for the L1's LOG corrections block.
- **F3 (drift risk) supports the round-63 lesson's pointer-drift class.** The
  `PROVINCE.md:35/:37` anchor moved 33→35 across round 63; another `§ Frontier`
  append moves it again. The refreshed line carries the re-grep command so the
  anchor is self-verifying.
- **F4 supports box 1's refresh.** Gate registry is `41 of 41` at both base and
  tip; it becomes `42 of 42` only when the r64 counter is both created and
  registered. The plan's C2 does not say the counter is registered; the L1 must
  decide it at integration, and the placeholder covers either outcome.
- **F5 (no move):** `SKILL.md` § Sources is 18 top-level entries at `cbbee56e`,
  `078eec4` and `c04fffbe`. Opening S120 adds a row to `corpus/SOURCES.md`
  (117 S-rows at base, max `S119` → 118 rows, max `S120`), not to the SKILL.md
  section the box counts. [INFERENCE] therefore `<SOURCES_ENTRIES>` stays 18
  unless the round also adds a SKILL.md § Sources bullet.
- **F6 (box 2 unchanged):** the cold-run record and its three LOG citations
  resolve; the fleet protocol bars calling it non-author credit, and the
  refreshed line states that explicitly rather than silently.

## Out of scope / untouched

- No production file, verifier, LOG, SCORECARD, SOURCES or SHONEN edit was made
  (write bound: this report only).
- No git/jj write, no commit, push, or index change; the inherited working-tree
  modification `.ufo/waves/round-63/w2/MutW2SplitClauses.md` was read but not
  touched (it is C2 check 1's material).
- No seat work was rerun to decorate the report; the only verifiers executed are
  the ones cited (`check_sibling_census.py`, `check_gate_registry.py`,
  `verify_skill_checklist.py`), plus git/awk/grep reads.
- Tool installs: none, no channel used.

## Artifact

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/w1/ScribeSHONEN.md`
