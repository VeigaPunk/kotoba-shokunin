# ExecGateAll — round-69 wave-1 gate battery (kotoba)

**Scope.** Run the assigned seven-gate battery against the lane tip with the L1's round-69 draft in
a sandbox clone, print each command with its exit code and verdict line, and report every gate that
is not green. Leaf seat: no lane mutation, no commits, no jj, no dispatch.

**Headline.** At the final snapshot (2026-10-25T07:26:45-03:00, draft rev `c01b70d8`):
**3 of 7 green** — `check_gate_registry` 49/49, `verify_corpus_independent` exit 0,
`check_province_core` 2/2. **4 red** — `verify_corpus_integrity` 6/9, `verify_skill_checklist`
10/11, `check_r68_routed_repairs` 6/8, `check_skill_precedence` **0 of 5**. The two hard ones are a
C1 regression that landed mid-wave (S207 row/entry divergence) and a C2 D7 expectation that **no
correct landing can satisfy** (arithmetic proof below); the other two are the unre-recorded corpus
baseline (R68-8) and two LOG.md citations from round 67 that sit past the checklist's frozen
correction horizon.

## Measurement setup

| item | value |
|---|---|
| lane | `/home/vgpnk/Projects/shokunin/kotoba-shokunin` |
| lane tip (`git rev-parse HEAD`) | `a238989a96cb0d2b939679126b832d75b861ca6e` (r69 plan commit); unchanged throughout |
| plan's pinned base | `a5f7459f99bb27bf697e9438362e75ac5833eca8` (r68 spot-check) |
| final sandbox | `/tmp/r69s2/kotoba-shokunin`, parent mirrors the fleet root |
| final integration rev | `c01b70d89971b268282507a400799c3688b17b0c` (single sandbox commit over `a238989`) |
| base sandbox | `/tmp/r69base/kotoba-shokunin` = `git worktree add --detach a238989` |

**Why an integration commit.** The four `--rev` counters read committed bytes (`check_skill_precedence`
via `_materialize`/`git show <rev>:<path>`; the r68, province and registry counters read the tree at
`<rev>`). The draft is uncommitted, so at the bare tip every content claim is `0 of N` — verified, see
§ Base controls. Each snapshot is therefore the lane working tree rsynced into a `/tmp` clone and
committed **only there**; the lane's index, working tree and jj state were never written, and lane git
use was read-only (`rev-parse`, `log`, `show`, `ls-tree`, `blame`, `diff`, `status`).

**Sandbox fidelity matters.** The lane's checks are path-sensitive. A first sandbox named
`/tmp/r69-gate` with no fleet siblings produced two false results: `trigger.name_directory`
(`name 'kotoba-shokunin' != directory 'r69-gate'`) and 15 extra `governance.citation_resolves` tokens
(`../PROTOCOL.md`, `../kasegi-shokunin/corpus/instruments/*.py`, `../AXES.md`, "+11 more") because
`../` pointed at `/tmp`. Every number below comes from a sandbox named `kotoba-shokunin` whose parent
symlinks all sibling lane entries and the hidden entries `.devin .gitignore .omp .scratch .tower .ufo`,
so `../…` resolves exactly as in the fleet. `.git`, `.jj`, `__pycache__` and
`.ufo/waves/round-68/w1/controls/c2falsify-clone/` (269 MB, the path the lesson dispositions as
removed) are excluded from the rsync.

**The draft moved while I measured it** (round-69 wave 1 is live). I froze four snapshots; verdicts
changed materially between them, which is itself a finding: a gate result reported earlier in the wave
is not evidence for the later draft.

| snapshot | rev | what changed in the draft | battery shape |
|---|---|---|---|
| S1 07:19 | `b8c6e6a1` | first capture (pre-seat edits) | registry ✅, C1 5/5 ✅, C3 2/2 ✅; integrity 5/9, independent exit 1, checklist 9/11, C2 4/8 |
| S2 07:22 | `4db49342` | `SOURCES.md`, C1 entry, lesson, r67+r68+precedence counters | C1 **0/5**, C2 6/8 (D3, D6 fixed) |
| S3 07:25 | `9189aa12` | `corpus/README.md`, `client-trust-gates-round68.md`, lesson | independent ✅, integrity 6/9 (unindexed cleared) |
| S4 07:26 | `c01b70d8` | `SKILL.md` 603 → 597 lines | checklist 10/11 (line budget fixed) |

Byte anchors for S4 (`sha256` prefix, full tree committed at `c01b70d8`): `SKILL.md` `599fcd7f2a6579a5`,
`corpus/SOURCES.md` `31292a39f112b529`, `corpus/knowledge/skill-name-precedence-round69.md`
`9d907e3f21d76ed8`, `corpus/lessons/round-69.md` `77ddae8d3ee4f5d4`, `verifiers/corpus-baseline.json`
`d3f8acd44d65786b` (unchanged from base). After S4 the only further drift is one untracked seat report
(`ScoutStaleLane.md`), i.e. the content verdicts below are stable for S4.

## The assigned battery at S4 (`c01b70d8`)

Run from `/tmp/r69s2/kotoba-shokunin`.

### 1. `python3 -B verifiers/verify_corpus_integrity.py --json`

```
exit=1
6/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.commit_total
```

Expected 9/9 exit 0 → **RED.** JSON: `tracked_files 127` vs `124`, `report_total 87` vs `85`,
`commit_total 39` vs `38`; `unindexed 0` (cleared at S3 by the new coverage-map row), and
`stale_patterns`, `missing_paths`, `report_dead`, `commit_unresolvable`, `commit_nonhash` all 0/PASS.

### 2. `python3 -B verifiers/verify_corpus_independent.py --json`

```
exit=0
```

Expected exit 0 → **GREEN.** Nine results: six PASS, three INFO (`tracked_files 127`,
`report_total 87`, `commit_total 39` are `observe`-mode by design), no DRIFT.
(The S1/S2 value was exit 1 — `corpus.index.unindexed 1`, `corpus/lessons/round-69.md`.)

### 3. `python3 -B verifiers/verify_skill_checklist.py --json`

```
exit=1
{"exit_code": 1, "fail": 1, "na": 0, "pass": 10}
FAIL governance.citation_resolves | LOG.md:2676: '.ufo/waves/round-67/w1/controls/census-validate-append.txt'
       does not resolve; LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve
       (10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused,
        3 recorded correction(s) excused)
```

Expected exit 0 → **RED** (one check). `trigger.line_budget` now PASSes:
`597 lines within budget 600 (from box at line 319)` — it failed at 603 in S1-S3, and the S4 SKILL.md
edit fixed it. `trigger.name_directory`, `trigger.frontmatter_parses`, `trigger.no_xml_tag` and the
other eight are PASS.

### 4. `python3 -B verifiers/check_gate_registry.py --rev c01b70d8…`

```
exit=0
gate registry rows conformant 49 of 49 lane verifiers; phantom 0
```

**GREEN**, expected 49 of 49. The three round-69 counters have conformant rows (`SKILL.md:517-519`).

### 5. `python3 -B verifiers/check_r68_routed_repairs.py --rev c01b70d8…`

```
exit=1
measured-rev: c01b70d89971b268282507a400799c3688b17b0c
r68 routed defects closed 6 of 8
  - D7: the r68 wave diff from a5f7459 is +6379/-251, expected +4081/-251 — a truncated landing passes the path test
  - D8: baseline corpus.index.tracked_files expects 124, the gate measures 127
  - D8: baseline corpus.pointers.report_total expects 85, the gate measures 87
  - D8: baseline corpus.pointers.commit_total expects 38, the gate measures 39
```

Expected 8 of 8 → **RED at 6 of 8.** D1, D2, D3, D4, D5 and D6 are green at S4 (D3 and D6 went green
at S2; the clone-disposition half of D7 went green at S3). Only D7's diff-size conjunct and D8 remain.

### 6. `python3 -B verifiers/check_skill_precedence.py --rev c01b70d8…`

```
exit=1
measured-rev: c01b70d89971b268282507a400799c3688b17b0c
skill precedence backed 0 of 5
  - S207: the row's source cell is not in the entry's source line
```

Expected 5 of 5 → **RED at 0 of 5.** This is the live regression; at S1 the same counter printed
`skill precedence backed 5 of 5`, exit 0.

### 7. `python3 -B verifiers/check_province_core.py --rev c01b70d8…`

```
exit=0
measured-rev: c01b70d89971b268282507a400799c3688b17b0c
province core rows 2 of 2
```

**GREEN**, expected 2 of 2; the `## Frontier`/`## Adjacent` byte-identical no-harm conjunct also holds
(the counter returns 0 only when both areas and that conjunct pass).

## Base controls, re-derived (no seat's word taken)

| command | base `a238989` / `a5f7459` | S4 `c01b70d8` |
|---|---|---|
| `check_skill_precedence.py --rev` | `0 of 5`, exit 1 | `0 of 5`, exit 1 |
| `check_r68_routed_repairs.py --rev` | `0 of 8`, exit 1 | `6 of 8`, exit 1 |
| `check_province_core.py --rev` | `0 of 2`, exit 1 | `2 of 2`, exit 0 |
| `verify_corpus_integrity.py` | `6/9 checks pass`, exit 1 | `6/9 checks pass`, exit 1 |
| `verify_skill_checklist.py` (base worktree) | 1 real fail (`governance.citation_resolves`); `trigger.line_budget` PASS at 600/600 | 1 fail (same citation); `line_budget` PASS at 597/600 |

The base integrity measurement reproduces the committed
`.ufo/waves/round-69/controls/C2-base-integrity.txt` exactly (`125` tracked vs `124`, `unindexed 1` =
`corpus/lessons/round-68-verifier-spotcheck.md`, `report_total 87` vs `85`, `commit_total 38` = the
baseline), so neither the base control nor my sandbox is inflating anything. `git ls-tree -r -- corpus`
counts 125 at `a5f7459` and `a238989`, 127 at S4 (+ entry, + lesson).

## Red gate 1 — the corpus baseline was never re-recorded (R68-8)

`verifiers/corpus-baseline.json` is not among the draft's modified files and its sha is the base sha, so
its pinned expectations are still the r68 numbers while the gate measures the draft:

| key | baseline expect | S4 observed | source of the delta |
|---|---|---|---|
| `corpus.index.tracked_files` | 124 | 127 | +`skill-name-precedence-round69.md`, +`lessons/round-69.md`, and the base itself was already 125 (inherited one behind) |
| `corpus.pointers.report_total` | 85 | 87 | inherited (also 87 at the base — two report pointers were never recorded) |
| `corpus.pointers.commit_total` | 38 | 39 | 38 at the base + the content commit itself |

Only the third is commit-shape; the first two are content. Green path: re-record the four `expect`
values from the gate's own `--no-baseline --json` at the final content rev — **127 / 0 / 87 / 39**
(`unindexed` is 0 at S4, so the zero-check is satisfied as well). This also clears D8's three findings.
This is one consistent defect, not four: `verify_corpus_integrity` and C2 D8 read the same baseline.

## Red gate 2 — C2 D7's diff-size expectation is unsatisfiable by a correct landing

The counter pins `R68_INS, R68_DEL = 4081, 251` and checks
`git diff --numstat a5f7459 <rev> -- <24 paths>`. Measured at S4: **+6379/-251**. The deletions match
exactly; the insertions are +2298. The arithmetic explains both numbers:

- **4081** is exactly the diff of the **ten tracked modified** r68 paths (their current working-tree
  content): 286+93+198+238+375+901+385+626+412+567 = **4081**, deletions 243+8×1+0 = **251**.
- **6379** is that same 4081 plus the **thirteen previously-untracked** paths that D7 requires to be
  committed: 77+117+153+130+99+137+109 (seven seat reports) + 68 (`c2falsify2.py`) + 662+1+534+81
  (four drafts) + 130 (`seat-results.json`) = **2298**; 4081+2298 = **6379**.

The expectation was recorded from `git diff` **before** the untracked files were added to the index
(untracked files do not appear in `git diff <commit> -- path`), while the check runs at a revision
where all 24 paths are committed. So committing the wave correctly can only produce 6379/251, and the
conjunct fails by construction. The counter's own `--self-test` cannot catch this: `FakeRepo.numstat`
returns the pinned constant by default (`check_r68_routed_repairs.py:381-382`), so the mutation battery
is blind to the value.

Green paths: (i) set the expectation to the landable 6379/251, or (ii) make the check compare per-path
content (e.g. the blob set D7 already validates) instead of a single aggregate. Either is an instrument
change; **D7 has no content-only green path** — escalate with D8's baseline re-record both landing in
the same instrument/content edit.

## Red gate 3 — C1 regressed to 0 of 5 on an S207 row/entry divergence

The counter's per-id source test requires the SOURCES row's `source` cell (cell 1) to occur in the
entry's `source:` line for that id. At S4 the two bytes disagree on the page label:

```
entry  line 5 : source: S207 — opencode — Agent skills (served docs page) — https://opencode.ai/docs/skills/ …
SOURCES line 148: | S207 | opencode — Agent skills (served V1 docs page) — https://opencode.ai/docs/skills/ | docs | …
```

`served V1 docs page` is not in the entry line, so `S207: the row's source cell is not in the entry's
source line`, and the counter's global rule makes the count 0 (a partial entry is not partially
backed). Both files' S4 shas (`31292a39…`, `9d907e3f…`) are the live lane bytes; the divergence
appeared between S1 and S2 (S1 was 5 of 5, exit 0). Minimal fix: make the two strings identical —
add "V1" to the entry's S207 source line, or drop it from the SOURCES cell — then re-run; nothing else
in C1 is currently failing (S203-S206 pass their five conjuncts).

This is the counter doing its job: two seats edited the row and the entry independently and the pair no
longer matches. Any 5-of-5 claim made before this edit is stale.

## Red gate 4 — `governance.citation_resolves`: inherited, and outside the frozen correction horizon

Both dead tokens are in `LOG.md` and are untouched by the draft (`git diff a238989 -- LOG.md` empty):

```
LOG.md:2675  - **Erratum (append-only; routed defect R67-2).** … cites …
LOG.md:2676    `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the file that exists is
LOG.md:2677    `.ufo/waves/round-67/controls/census-validate-append.txt`. The r67 report is not edited.
LOG.md:2678  - **Routed defect R67-3 (disclosure).** `.ufo/waves/round-67/w1/controls/junk-world/` — a 254 MB …
```

`git blame` attributes lines 2674-2679 to `605b84b` ("round-68: C1 depth client trust gates … and C2
consistency routed r67 repairs"), an ancestor of `a5f7459`. Neither path exists at the base or at S4
(`git ls-tree -r a238989` carries only `.ufo/waves/round-67/controls/census-validate-append.txt`; there
is no `w1` directory and no `junk-world`). The r65 mechanism cannot excuse them:
`GOVERNANCE_CORRECTIONS_HORIZON = 2621`, with three byte-pinned rows at lines 2619-2621. A notice at
2676 and stale tokens at 2676/2678 are past the horizon by construction, and the "corrected token must
resolve" arm would have to name a replacement that resolves.

Consequence: the r68 closure's stated tip result
(`.ufo/waves/round-68/w1/CriticC2Predicate.md:11`, "Tip: `9/9 checks pass` exit 0 · independent `--json`
exit 0") **does not reproduce at its own tip** — `verify_skill_checklist` is red at `a238989` and at
every S1-S4 snapshot for these two tokens. This red cannot be closed by a content edit under the
current instrument: either the two cited paths must resolve (commit the receipt at the `w1` path and
something under `junk-world/`), or the correction table/horizon must be widened (a Q28 instrument
change). Escalate to L1 with the C2 D7 decision.

## What is green (do not disturb)

- `check_gate_registry` — 49 of 49, phantom 0, exit 0.
- `verify_corpus_independent` — exit 0, no DRIFT (S3/S4).
- `check_province_core` — 2 of 2, exit 0 (C3 complete).
- C2 D1, D2, D3, D4, D5, D6 and D7's path/disposition half.
- Checklist: 10 of 11 checks.

## Minimal path to a fully green battery

1. `corpus/knowledge/skill-name-precedence-round69.md` **or** `corpus/SOURCES.md`: reconcile the S207
   source string ("served V1 docs page" vs "served docs page") → C1 back to 5 of 5.
2. `verifiers/corpus-baseline.json`: record `127 / 0 / 87 / 39` from the gate's own `--no-baseline
   --json` at the final content rev → integrity 9/9 and C2 D8.
3. C2 D7: fix the `R68_INS` expectation (6379) or replace the aggregate with a per-path content check
   → C2 7 of 8. *Instrument change.*
4. Checklist `governance.citation_resolves`: make the two r67 LOG.md tokens resolve, or register a
   correction inside the horizon (needs a wider, byte-pinned row) → checklist 11 of 11.
   *Instrument or file-placement decision.*
5. Re-run the seven commands at the landing rev; do not reuse any pre-07:26 result — three of the
   seven verdicts changed between my snapshots without the claim text changing.

## Caveats

- `commit_total 39` is commit shape: my sandbox commit is the 39th, and the lane's own content commit
  will also be the 39th **if it is a single commit**. Splitting the landing moves the number; the
  baseline must be recorded from the gate's measurement at the final rev, never by arithmetic.
- The S1/S2 `0 recorded correction(s) excused` vs S4 `3 recorded correction(s) excused` difference is
  an artifact of the sandbox mirror (the base worktree, run with the same instrument, reports 3); the
  two failing tokens are identical in every run, so the red is real regardless.
- `check_skill_precedence.py --fetch` was **not** run — outside this seat's assigned battery (fetch
  arm owns it).
- No gate ran inside the lane; all execution was in `/tmp/r69s2` and `/tmp/r69base`. At most two gate
  processes ran concurrently (cap 4).
- No tool was installed or updated for this seat.

## Reproduction

```
rm -rf /tmp/r69s2 && mkdir -p /tmp/r69s2
# mirror every sibling lane entry + hidden entries (.devin .gitignore .omp .scratch .tower .ufo)
#   of /home/vgpnk/Projects/shokunin into /tmp/r69s2 as symlinks
git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/r69s2/kotoba-shokunin
rsync -a --exclude='.git/' --exclude='.jj/' --exclude='__pycache__/' \
      --exclude='.ufo/waves/round-68/w1/controls/c2falsify-clone/' \
      /home/vgpnk/Projects/shokunin/kotoba-shokunin/ /tmp/r69s2/kotoba-shokunin/
cd /tmp/r69s2/kotoba-shokunin && git add -A && git commit -m 'round-69 draft integration snapshot'
# then the seven commands above with --rev <that commit>
```

Raw outputs: `/tmp/r69-ev3` (S1 `b8c6e6a1`), `/tmp/r69-ev4` (S2 `4db49342`), `/tmp/r69-ev5`
(S3 `9189aa12`), `/tmp/r69-ev6` (S4 `c01b70d8`), each holding `integrity_json`, `integrity_human`,
`independent_json`, `independent_human`, `checklist_json`, `checklist_human`, `registry`, `r68`,
`precedence`, `province`; base evidence in `/tmp/r69-ev3/base_integrity*` and
`/tmp/r69-ev3/base_checklist_json.out` (`--repo /tmp/r69base/kotoba-shokunin`).
