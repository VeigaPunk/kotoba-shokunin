# RevC1Counter — review of `verifiers/check_r69_routed_repairs.py` (round 70, wave 1)

## Verdict

**The counter is consistent with its plan and docstring, and its 9/10 reading at the tip reproduces. As a measure, though, it is mostly a presence floor.**

- A token-dump world (one LOG line, two SCORECARD lines, a fake receipt, two lesson lines, a stub gate, plus the two real inherited blobs) reads **10 of 10, exit 0**.
- Read independently of the counter, the measured tip's prose is **true**.
- K69-11 **is substantively closed** at the tip. The counter's `/tmp/.../clone` sandbox cannot see the repair.
- So 9/10 is an honest miss under the frozen rule, and it understates the substance. The 10/10 the counter could print elsewhere would overstate the evidence.

Calibration of the docstring's trust boundary (lines 38–42): it correctly discloses K69-1/2/3/6/7/9/10 as presence floors. It overstates two items:

- K69-8 "pins a receipt's lines". In fact it is a presence floor over a text file: the `--rev` in the command is not required, and the verdicts are unanchored.
- K69-11 "recomputes from a sandbox run". In fact it executes `--rev`'s **own** `verifiers/verify_skill_checklist.py`, so the measured revision defines its own PASS.

Scratch: `/tmp/k70w1-RevC1Counter.wqbK` (deleted before return). No lane file was edited except this report. No tools were installed.

## Required runs (from the lane root)

```
$ git log --oneline 53de0ac..16b212a -- verifiers/check_r69_routed_repairs.py    -> (empty; frozen bytes)
$ python3 -B verifiers/check_r69_routed_repairs.py --self-test
PASS honest world: closed 10 of 10 … (16 broken worlds rejected)
self-test: 0 failure(s) over 17 assertions          exit=0
$ python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae
measured-rev: 16b212a390c7ce68b6bce49b2c3766b154fbcbae
r69 routed defects closed 9 of 10
  K69-11: governance.citation_resolves FAIL          exit=1
$ python3 -B verifiers/check_r69_routed_repairs.py --rev 7d51253f99906b8551b6a0a108761eedac00de74
r69 routed defects closed 0 of 10   (13 finding lines, every item)  exit=1
```

These match `controls/C1-base.txt`, `receipts/C1-measure.txt` (9/10 at `8edeb49`) and the plan's frozen predicate (plans/round-70.md:30-32).

## Findings, by severity

### HIGH-1: a zero-substance world reads 10 of 10 (calibration)

Reproducer: `forge.sh` world A, built on the base `7d51253`. It appends:

- **LOG.md:** `## Round 69` followed by one line: `trigger: action: outcome: pointer: orchestrator fast-forward a02ba7e 54f4b6c 278b9dc 9ce102b 4844216b 9d9f181e probe 0a1199a0 110 receipts 123 landed 21 dispositioned`.
- **SCORECARD.md:** `**Round 69 axis annotations` followed by the three counter filenames and two SHAs.
- **Inherited reports:** the two real blobs, copied from the tip.
- **`round-70.md`:** both paths and `S201 (14 words) (13 words)`, with the direction reversed.
- **`round-69.md`:** `(18 assertions) 22 assertions`.
- **Receipt:** `measured-rev: 9ce102b…`, then `command: echo check_skill_precedence.py --rev a5f7459…`, `skill precedence backed 5 of 50`, `exit=0`, and likewise `8 of 80` and `2 of 20`.
- **Gate:** `verifiers/verify_skill_checklist.py` replaced by `print(json.dumps({"checks":[{"id":"governance.citation_resolves","status":"PASS"}]}))`.

```
$ python3 -B verifiers/check_r69_routed_repairs.py --repo /tmp/…/A --rev c9dcd10a…
r69 routed defects closed 10 of 10
exit=0
```

The only substance this world needs is the two inherited blobs (K69-5). The plan's committed skip control (`controls/C1-skip-control.txt`: bare headings, 0/10) is therefore far weaker than the cheapest real skip.

### HIGH-2: K69-11 executes the measured revision's own gate

`k11_governance` → `Repo.checklist` (lines 113–121) runs `clone/verifiers/verify_skill_checklist.py` from `--rev`. It parses whatever JSON that file prints and ignores the exit code. World A's 3-line stub flips K69-11 from FAIL (the base gate, in the same sandbox) to closed. This is not "recomputes from a sandbox run"; the item trusts code the lane commits in the same round.

### MEDIUM-1: K69-11 is environment-bound. The tip has closed it, but the counter cannot see it (confirms M116 and locates the mechanism)

In the counter's sandbox shape (`<tmp>/clone`), the gate fails on fleet-relative tokens such as `'../.ufo/reports/round-60/kotoba.md'` and `'../.ufo/watchdog.log'` (LOG.md:2619-2621, LOG.md:177, "+30 more"), plus `trigger.name_directory FAIL name 'kotoba-shokunin' != directory 'clone'`. This happens at both base and tip. Base lines are append-only, so an honest revision cannot remove those tokens. [INFERENCE] A revision could pass only through a gate edit (HIGH-2) or false absence notices.

Fleet-shaped sandbox: the clone is named `kotoba-shokunin` in `/tmp/…/shaped/`, with read-only symlinks to the fleet's top-level entries. No fleet mutation.

```
7d51253: pass 10 of 11; governance.citation_resolves FAIL LOG.md:2676 '.ufo/waves/round-67/w1/controls/census-validate-append.txt' … LOG.md:2678 '.ufo/waves/round-67/w1/controls/junk-world/' … 3 recorded correction(s) excused
16b212a: pass 11 of 11; governance.citation_resolves PASS 1253 governance citation token(s) resolve across 2 files; … 5 recorded correction(s) excused
```

At the base, the red is exactly the closure's routed pair (spotcheck.md:208-211). At the tip it is closed by the two appended correction notices (LOG.md tip lines under "Governance corrections (K69-11…)"). This independently confirms commit `16b212a`'s "gate 11/11 … in the clean lane checkout". Under the frozen no-narrowing rule the 9/10 miss stands; the report should cite this as out-of-claim evidence, not as C1.

### MEDIUM-2: "appended" / "after the base's last line" is enforced by line index, not by append

`_r69_log_entry` (lines 136–139) and `k10_erratum` (line 238) slice at `len(base.splitlines())`. They never check that the base is a prefix of `--rev`.

- **World B** (the tip with all 2696 base LOG lines blanked; `base-history lines kept: 0`) reads `9 of 10`, the same as the honest tip. The LOG history destruction is invisible.
- **World C** (the base, with lesson-69 line 24 edited **in place** to `(18 assertions) — corrected in place: 22 assertions.` and 200 blank lines padded on top; diff `201 insertions(+), 1 deletion(-)`) reads `closed 1 of 10`, with **no K69-10 finding**. So the form the closure forbids ("Append the correction") closes the item.

The tip itself is honest here. The base is an exact prefix of the tip for LOG.md (+28/−0), SCORECARD.md (+7/−0) and `round-69.md` (+5/−0), checked with `cmp` against `head -n <base lines>`.

### MEDIUM-3: K69-7 is a substring floor that accepts wrong numbers

`k7_numeric` (line 203) uses `"10 receipts" in entry`. World A's `110 receipts`, `123 landed` and `21 dispositioned` pass. Negations pass too (world E: `not 10 receipts, not 23 landed, not 1 dispositioned`).

### MEDIUM-4: the `## Round 69` slice accepts wrong rounds and negated prose

`startswith("## Round 69")` (line 137) matches `## Round 690`. World E (the base plus `## Round 690 — unrelated future round` with "the orchestrator did not fast-forward; no commits a02ba7e … exist; nobody named probe wrote 4844216b …; no trigger: no action: no outcome: no pointer:") reads `closed 4 of 10`. K69-2, K69-3, K69-6 and K69-7 are all closed by a wrong-round entry that denies every fact. K69-2 tests `fast-forward` and `orchestrator` as independent substrings. K69-3 accepts `probe` inside `probed`/`probes`, and never ties the identity to the commits.

### MEDIUM-5: the K69-1 block runs past its own section

The regex terminator (line 152) is `^\*\*Round 7\d|^## |\Z`. Hyphenated headings, which this file already uses (`**Round-64 wave-2 corrections`, SCORECARD.md:377), do not end the block. World F (`**Round 69 axis annotations (append-only).** nothing recorded.` followed by `**Round-70 wave-2 corrections.** unrelated: <3 filenames> <2 SHAs>`) reads `closed 1 of 10` with **no K69-1 finding**.

The item also never checks what the closure's fix demands (spotcheck.md:156-158: "carrying each claim's command and measured revision"). No command text, verdict, base value or delta is required.

### MEDIUM-6: the K69-8 receipt checks are looser than "per counter at the tip"

Lines 212–224:

- `measured-rev:` is checked once, file-wide.
- The `command:` line need only contain the filename (world A: `command: echo check_skill_precedence.py --rev a5f7459…`).
- The verdict regex is unanchored, so `5 of 50`, `8 of 80` and `2 of 20` pass.
- The receipt is never recomputed.

The tip receipt is nevertheless true. Re-running the three counters from the tip's bytes:

```
python3 -B verifiers/check_skill_precedence.py --rev 9ce102b9…    -> skill precedence backed 5 of 5     exit=0
python3 -B verifiers/check_r68_routed_repairs.py --rev 9ce102b9…  -> r68 routed defects closed 8 of 8   exit=0
python3 -B verifiers/check_province_core.py --rev 9ce102b9…       -> province core rows 2 of 2          exit=0
```

### LOW-1: K69-9 ignores direction

`k9_s201` (line 230) needs the three tokens on one line in any order. World A's reversed `(14 words) (13 words)` passes.

### LOW-2: no self-test arm covers any hole above

The self-test (lines 338–359) has no arms for: wrong numbers by substring, negation, `## Round 690`, non-append (blanked or padded base), K69-1 overflow, a non-`--rev` or unanchored receipt verdict, a reversed S201 direction, or a stub gate. The gate timeout of 600 s (line 117) exceeds the round's 300 s per-command cap; observed runtime was about 1.5 s.

## Substance vs presence, per item (with the tip's truth checked independently)

| Item | What the counter proves | Tip prose true? (command) |
|---|---|---|
| K69-1 | presence: 5 tokens after a heading | yes: r69 counters re-run give 0/5, 0/8, 0/2 exit 1 at `a5f7459` and 5/5, 8/8, 2/2 exit 0 at `9ce102b` |
| K69-2 | presence: 6 substrings | yes: the four commits are ancestors of `16b212a`; `9ce102b`'s parent is `278b9dc` |
| K69-3 | presence: 4 substrings | yes: `git -C <fleet> log -- .ufo/reports/round-69/kotoba.md` gives `probe … 9d9f181e`, `probe … 4844216b`, `kotoba-shokunin … 0a1199a0` |
| K69-5 | **substance** for the blobs (exact bytes); presence for the lesson paths | yes: tip blob = worktree `hash-object` for both paths (`59585ea1…`, `6f4c23ba…`). The closure's "pathspec-discipline check" half is not counted (lesson round-70.md:132 records a porcelain run) |
| K69-6 | presence: 4 label substrings plus an index-based heading | yes: the entry carries Trigger/Action/Outcome/Pointer |
| K69-7 | presence: substrings (wrong numbers pass) | yes: `ls-tree … recapture/` gives 10; `a02ba7e` round-68 paths give 23 |
| K69-8 | presence over a text receipt | yes: re-run above |
| K69-9 | presence: 3 tokens on one line | yes: `git diff a5f7459 9ce102b -- corpus/SOURCES.md` S201 goes `(13 words)` → `(14 words)` |
| K69-10 | presence plus an index-based tail | yes: an appended `## Errata` section, base preserved as an exact prefix |
| K69-11 | would be substance if the gate were trusted and the sandbox fleet-shaped; as built, it is rev-controlled and environment-bound | yes: 11/11 in the fleet-shaped sandbox (MEDIUM-1) |

## Residual risk and verification gaps

- I did not run the counter against unreferenced (jj-only) revisions. The `git clone --shared` in K69-11 may not carry them, which would make it exit 2. [INFERENCE] Unobserved.
- The forged worlds attribute each hole by construction. I did not mutate one item at a time on the tip for every finding; worlds C, E and F do isolate K69-10, K69-2/3/6/7 and K69-1.
- The fleet-shaped sandbox resolves `../` through symlinks to the live fleet tree, not to fleet bytes at a pinned revision.
- **A foreign lane mutation was observed while this review ran.** At return, `git status --short` shows ` M verifiers/verify_skill_checklist.py`, ` M corpus/knowledge/skill-eval-artefacts-round70.md` and ` M corpus/README.md` (mtimes 2026-10-25 09:00:19/09:00:44 -03). This seat did not write them; all of its worlds lived in `/tmp` clones.
  - `git diff verifiers/verify_skill_checklist.py` drops the K69-11 correction row `(2724, "13a858af…", "LOG.md", 2678, …)` and sets `GOVERNANCE_CORRECTIONS_HORIZON = 2723`.
  - Every measurement above reads committed bytes (`git show`, clones at `--rev`), so none is affected.
  - Reported to L1Kotoba70.
