# ExecSkillGatesR74 — C1 landing-shape gate pre-test (round 74, wave 1)

**Verdict.** The `SKILL.md` landing shape for C1 is gate-clean end to end — `tip battery exit 0: 6 of 6`, `guards 5 of 5`
— **but only when three pieces land in one commit**: (i) the `SKILL.md` block (body-craft subsection + frame sentence +
`## Gate registry` rows), (ii) the two counter scripts, and (iii) a re-record of `verifiers/corpus-baseline.json`
(`corpus.index.tracked_files` 139 → 140). With (i)+(ii) and no (iii) the landing is red at
`corpus.index.tracked_files: observed=140 expected=139` (8/9) and the battery drops to `4 of 6`/`5 of 6`. Measured, not inferred:
the full landing shape (plan commit `329e7d9` + overlay + baseline) scores `6 of 6` at rev `5528765` of a throwaway sandbox.

Nothing in the lane was written except this report and `.ufo/waves/round-74/w1/build/ExecSkillGatesR74/`
(`landing-shape.patch`, `gate-run.txt`, `landing-commits.txt`, `landing-rev.txt`, patch sha256). No tool installed;
no network used (no fetched bytes, so no URL/quote rows here). Sandboxes deleted before return.

## Sandbox and revs

```
P=$(mktemp -d /tmp/k74fleet-ExecSkillGatesR74.XXXX)          # P=/tmp/k74fleet-ExecSkillGatesR74.qDRi
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do b=$(basename "$e");
  [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
```

Stage 1 `98b3e59` (overlay on the assigned base), stage 2 `e5650b2` (+ placeholder entry + index row),
`landing` clone of the real lane tip `329e7d9` → `a1e6962` → `a8c5a6e` → `5528765` (baseline re-record).
Every git write happened inside those throwaway repos, with identity `-c user.name=seat-ExecSkillGatesR74
-c user.email=seat@local.invalid -c commit.gpgsign=false`; `git rev-parse --show-toplevel` was checked first.

The assigned base `1e03d19` and the lane tip `329e7d9` differ exactly by the plan commit (`corpus/README.md` closure
index row + `verifiers/corpus-baseline.json`); `SKILL.md` is byte-identical between them, so a SKILL.md pre-test on
either rev is the same test. Attribution was measured on both (F1/F2 below).

## Findings

### F1 — the landing shape is green: `6 of 6`, guards 5 of 5

```
$ cd $P/landing && python3 -B verifiers/check_tip_battery.py --rev 55287654883ed0ac1e3b6fdd2f421937f2673217
measured rev 55287654883ed0ac1e3b6fdd2f421937f2673217 in a fleet-shaped sandbox; base 072048fa…
guarded paths 586, deleted 0; floors 15 rows; instruments added 0 / deleted 0 lines (cap 40); spotcheck base files 27
guard no-deletions PASS / floors PASS / instrument-size PASS / instrument-pin PASS / spotcheck-identity PASS
gate check_gate_registry.py exit 0 wall 0.5s
gate check_assertion_floors.py exit 0 wall 83.3s
gate verify_skill_checklist.py exit 0 wall 2.0s
gate verify_corpus_integrity.py exit 0 wall 1.2s
gate verify_corpus_independent.py exit 0 wall 0.7s
gate check_correction_sweep.py exit 0 wall 0.1s
fleet root /tmp/k74fleet-ExecSkillGatesR74.qDRi; guards 5 of 5; tip battery exit 0: 6 of 6      # exit 0, wall 90.0 s
```

The two new verifier scripts do **not** trip `instrument-size` (that guard measures the six battery instruments only:
`instruments added 0 / deleted 0 lines (cap 40)`) and do not trip `instrument-pin`.

### F2 — must-fix: re-record `corpus-baseline.json` in the landing commit

Overlay + placeholder entry + index row, no baseline change (rev `a8c5a6e`):

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=140 unindexed=0 stale=0 missing=0  (158 FILE-column patterns over 139 md files)
DRIFT   corpus.index.tracked_files: observed=140 expected=139
8/9 checks pass; DRIFT: corpus.index.tracked_files            # exit 1
$ python3 -B verifiers/verify_corpus_independent.py            # exit 0 (unchanged)
```

`verifiers/corpus-baseline.json:15` (`"expect": 139`) → `140`, same commit → `9/9 checks pass`, exit 0. Exact values to
record from `verify_corpus_integrity.py --no-baseline --json` at the landing shape: `tracked_files 140`,
`index_patterns 158`, `report_total 97`, `commit_total 41`, and every zero-class still 0 (`unindexed`, `stale_patterns`,
`missing_paths`, `report_dead`, `commit_unresolvable`, `commit_nonhash`). The plan defers the "baseline re-record" to
the round's closing commit; that is one commit too late — the wave-1 landing tip reads red until it moves.

### F3 — must-fix: the entry file and the `SKILL.md` rows must be in one commit

Stage 1 (SKILL.md rows landed, entry absent):

```
$ python3 -B verifiers/verify_skill_checklist.py
FAIL trigger.citation_resolves: evaluated 199 — line 205: 'corpus/knowledge/spec-skill-creation-craft-round74.md'
     does not resolve from /tmp/k74fleet-ExecSkillGatesR74.qDRi/kotoba-shokunin      # exit 1
```

`trigger.citation_resolves` subjects every backticked word starting `corpus/`… — so the frozen entry path is a hard
dependency. With the entry present: exit 0, wall 1.97 s. The index row is a second dependency for
`verify_corpus_integrity` (entry without a `corpus/README.md` row raises `unindexed` by 1); a row added as
`| Spec skill-creation body craft (round 74) | \`knowledge/spec-skill-creation-craft-round74.md\` | … |` after the
round-73 closure row keeps `unindexed=0`.

### F4 — line and byte arithmetic (the assignment's core number)

```
base 1e03d19 / 329e7d9 : 570 lines, 74174 B
landing shape          : 590 lines, 77132 B      (+20 lines, +2958 B)   budget 600 → 10 lines spare
```

Per-hunk (`git diff -U0 1e03d19 5528765 -- SKILL.md`): frame rewrite `@@ -24 +24,3 @@` (**+2**), decision row
`@@ -76,0 +79 @@` (**+1**), body-craft block `@@ -199,0 +203,15 @@` (**+15**), registry rows
`@@ -492,0 +511,2 @@` (**+2**); `--numstat` = `21 1`.

The instruction's "14 lines (one-line lead + header + 6 rows + closing line)" is 15 physical lines once markdown's
required blank lines are counted: heading, blank, lead, blank, `| Guide | Rule | Action |`, `| --- | --- | --- |`,
6 rows, blank, closing, blank. A 3-column table needs the blank before a following paragraph, so 14 is reachable only by
folding the closing sentence into the lead (then the block is 14). Either way the plan's 590 estimate holds; the
landing is at 590 because the frame rewrite costs +2, not +1. Lines over 300 characters: 74 → **78** (the lead, the
decision row and the two registry rows) — a recorded sweep number, not a gate.

### F5 — no gate reads this lane's `SKILL.md` by line number

```
$ grep -rn 'SKILL\.md:[0-9]' verifiers/*.py verifiers/*.json
verifiers/check_agent_definitions.py:1076:   sum_grep_counts("b0b7140b:LOG.md:3\nb0b7140b:SKILL.md:2\n"), 5)   # self-test fixture
verifiers/check_sibling_census.py:280:       """`SKILL.md:42` -> ("SKILL.md", 42)…"""                          # parser for census `path:line` cells
verifiers/verify_corpus_integrity.py:75:     * deliberately recorded dead paths (SKILL.md:588's `~/wikillm`…)   # docstring
$ grep -c 'SKILL\.md:[0-9]' verifiers/checklist-baseline.json verifiers/corpus-baseline.json
0 0
```

All three hits are non-live (a fixture string, a census-cell parser over *sibling* files, a docstring). Box line
numbers do **not** matter: the checklist baseline keys boxes on `(section, text_sha256)`
(`"normalization": "first line minus '- [ ]' marker + continuations stripped…"`), and `box_total` is 45. Empirically:
`PASS checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)` both at base
and after the +18-line shift (frame +2, decision row +1, block +15). **So the insertion at line 190 breaks no gate by line arithmetic.**

What *does* move is box **section** attribution: "A box's *section* is the text of the nearest preceding ``#``-led
heading" (`verifiers/verify_skill_checklist.py:15`). Inserting the same block anywhere inside
`## Trigger-fidelity checklist` would re-section its 19 boxes and FAIL `checklist.box_map_complete`; inserting it at the
end of `## Compression rules` (anchor: its last content line 198, `… line-budget box).`, next heading at 200) is safe
because that section holds no boxes. Keep the heading text byte-identical (`### Body craft — the specification's
skill-creation guides`, U+2014 em dash) — the C1 predicate (e) names it.

### F6 — the consumers a line shift does bend: 97 corpus prose citations

```
$ grep -rho 'SKILL\.md:[0-9]\+' corpus/*.md corpus/knowledge/*.md corpus/lessons/*.md | awk -F: '{print $2}' \
  | awk '$1>199{n++} $1>24{n2++} END{print NR, n, n2}'
97 38 70
```

38 citations point at lines >199 (each now 15 lines off) and 70 at lines >24 (2 lines off). No gate validates them
(`verify_corpus_integrity` resolves `commit` citations and `.ufo/reports/` pointers, not `SKILL.md:` line anchors) —
this is the file's own "cited line numbers are points-in-time" class. Route it as a reviewer item, not a gate red.

### F7 — what `check_gate_registry.py` demands (and a new verifier is auto-required)

Universe: "every blob directly under `verifiers/` at the revision whose name ends in `.py` or `.sh`" — 58 at base,
60 with the two counters, so **a new `verifiers/check_*.py` must carry a row**; without one:

```
$ python3 -B verifiers/check_gate_registry.py --rev <rev with an unregistered stub>
verifiers/check_unregistered_stub.py         no registry rows naming it: 0 (need 1)
gate registry rows conformant 60 of 61 lane verifiers; phantom 0        # exit 1
```

A row is conformant iff exactly one row under `## Gate registry` has the file in its name cell and: header cells
(lower-cased, backticks stripped) are `name | kind | entry command | verdict map | self-test | pinned values | write
scope | owner`; `kind` ∈ {`gate`, `probe`}; the entry-command cell contains the path; the verdict map declares
`<code>=<class>` pairs (class ∈ clean/failed/could-not-evaluate, no code twice), a `gate` declaring `0=clean` **and**
`1=failed` (a `probe` may not declare `1=failed`); the self-test cell is `none` or backticked flags, each an **exact
active** handler (Python `add_argument` with that exact string, or a shell `case` arm) — a `gate` may not say `none`;
the pinned-values cell is `none`, `in-file`, or existing repo-relative paths (a `gate` may not say `none`); write scope
non-empty; owner `kotoba`. Negatives, all fired:

```
B  self-test `--selftest` (no exact handler) → "no self-test flag --selftest lacks an exact handler"       exit 1
C  kind `probe` + `1=failed` + `--self-test`  → "no probe verdict map declares 1=failed; probe script has an
                                                  exact --self-test handler"                                 exit 1
```

My two rows (`gate`, `0=clean, 1=failed, 2=could-not-evaluate`, self-test `` `--self-test` ``, pinned `in-file`,
write scope `none (read-only)`, owner `kotoba`) read `60 of 60; phantom 0` — appended after
`verifiers/check_report_pointers.py`, which matches the table's round-ordered, not alphabetical, convention.

### F8 — a new verifier does **not** need a `floors-registry.json` row (and why it should get one anyway)

`check_assertion_floors.py` has no directory scan (`grep -n 'ls-tree|glob|iterdir|rglob|walk(' → no hits`); its universe
is the closed in-file `INSTRUMENTS`/`EXPECTED_INSTRUMENTS` tables cross-checked against the registry's
`instrument_total 15`. Empirically the two stubs (each printing `self-test: 0 failure(s) over 1 assertions`) left the
gate at `rc=0`, 15/15 PASS. The cost: their self-tests are **unfloored**, so a later silent shrink is invisible — the
exact defect class the guard exists for. If they are registered, the registry's own rule binds:
"BUMP-IN-STEP RULE: when a row's floor moves, edit this file, both in-file tables and the guard docstring in the same
change" (`verifiers/floors-registry.json`, `$comment`). Recommend registering both at their landed assertion counts.

### F9 — pre-existing reds and attribution (assigned base vs lane tip)

At the assigned base `1e03d19`, `verify_corpus_integrity` is red **before any overlay**:
`tracked=139 unindexed=1` → `unindexed: corpus/lessons/round-73-verifier-spotcheck.md` (the r73 closure file; the plan
commit's `corpus/README.md:144` row is what fixes it, with the baseline re-recorded). `verify_corpus_independent` is red
there for the same rev, and green at the plan commit. So the stage-1/stage-2 tip-battery `4 of 6` (wall 87.7 s) is the
base's state, not the overlay's: guards 5 of 5 PASS and every red is one of those two corpus gates.

### F10 — wall times (recorded, conservative planning number in parentheses)

`verify_skill_checklist` 1.94 s (red run) / 1.97 s (green); `check_gate_registry` 0.57 s; `check_province_core` 0.06 s
(`province core rows 2 of 2`); `verify_corpus_integrity` 0.25 s; `check_correction_sweep` 0.06 s
(`correction sweep: 0 stale block(s)`); `check_assertion_floors` **76.3 s** here (215.5 s recorded by the L1 at base);
`check_tip_battery` 87.7 s (overlay at 1e03d19) and 90.0 s (landing). Every run stayed under the 300 s cap; the floors
gate was run alone.

## Must-fix list for the real landing (ordered)

1. `verifiers/check_spec_craft.py` and `verifiers/check_sibling_reread.py`: real counters, each with an exact
   `--self-test` `add_argument` handler, printing the frozen predicate lines
   (`spec craft pages backed N of 3`, `sibling rows re-pinned and re-read N of 20`).
2. `corpus/knowledge/spec-skill-creation-craft-round74.md`: the sourced entry (real `source:`/`verified-at:`/`recheck:`
   trio and the six real rule rows) **in the same commit** as the `SKILL.md` rows (F3).
3. `corpus/README.md`: one index row for the entry, after the round-73 closure row.
4. `SKILL.md`: the body-craft block at the end of `## Compression rules` (anchor: line 198, before the blank at 199),
   the frame rewrite, the `.agents/skills/` decision row, and the two `## Gate registry` rows — heading text and em
   dash exactly as the counter's predicate names them.
5. `verifiers/corpus-baseline.json`: `corpus.index.tracked_files` 139 → 140 in the same commit (F2). Without it the
   landing tip is red and the battery reads below `6 of 6`.
6. Re-run `check_tip_battery.py --rev <landing rev>` and expect `guards 5 of 5; tip battery exit 0: 6 of 6`; if
   `corpus.index.tracked_files` drifts again, the entry/index/baseline trio is out of step.
7. Reviewer item (no gate): the 97 `SKILL.md:NNN` corpus citations, 38 of them now 15 lines off (F6).

## Bounds and what this does not show

- This is a **shape** pre-test. The placeholder rows contain no located tokens, so nothing here says the C1 counter can
  reach `3 of 3`, nor that the three pages carry two quotable rule tokens each (that is the wave-1 Q45 census).
- `check_author_rules.py`, `check_cn_vendor_surfaces.py` and the other claim counters were not in the assigned set and
  were not run; they read boxes and entries, neither of which this overlay changes structurally.
- The decision row's citation `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` resolves (it is a real file)
  and adds one `trigger.citation_resolves` subject; if the landed row is reworded to cite something else, re-run the
  checklist (the class is "any backticked `corpus/`/`verifiers/`/`.opencode/`/`.ufo/`/`../` token must exist").
- The C2 counter never reads `SKILL.md`; its row shape demands live in `check_sibling_census.py` and are the C2 seat's
  pre-test, not this one's.
- Q65's 600-line bound is prose only — `grep -rn '\b600\b' verifiers/*.py` finds timeout constants, no line-count gate.
  The bound is enforced by review, so 590 is inside it by 10 lines.

## Cleanup

`rm -rf /tmp/k74fleet-ExecSkillGatesR74.qDRi` (fleet sandbox, both lane clones, the apply-check clone). No lane file was
modified; no jj state, fleet repo, `shokuknow` or sibling lane was touched; no credential-shaped material was read.

## Correction appended (F6 scope, after the scribe's sweep) — appended, not rewritten

F6's 97/38 figure was measured over `corpus/*.md corpus/knowledge/*.md corpus/lessons/*.md` (direct children only).
The recursive count is larger, and the difference is one non-prose file:

```
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | wc -l                                      # 111
$ grep -rho 'SKILL\.md:[0-9]\+' corpus/*.md corpus/knowledge/*.md corpus/lessons/*.md | wc -l   # 97
$ grep -rlE 'SKILL\.md:[0-9]+' corpus/knowledge corpus/lessons | grep -vE '^corpus/(knowledge|lessons)/[^/]+\.md$'
corpus/knowledge/sibling-citation-routing-round16.json                               # 14 hits, the whole gap
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | awk -F: '{n=$2; tot++; if(n>198)a++; if(n>23)b++; if(n>570)c++} END{...}'
total 111 | >198: 45 | >23: 83 | >570 (past EOF at base): 13 | max 720
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | awk -F: '$2==24' | wc -l                   # 3
```

The L1 should take the recursive figure, not either seat's: 111 total = 97 prose citations in 32 `.md` files + 14 rows in
one JSON routing table. Affected set by route — 3 citations name line 24 (the frame sentence) and go stale on both
routes because its text changes; 45 name lines >198 and shift **+14** on the 14-line route (end of line 198, no trailing
blank) or **+15** on the 15-line route measured here. 13 citations already point past EOF at base (max `SKILL.md:720`
against 570 lines) — they are points-in-time records, which is the same class as the rest, and no gate reads any of them.
Re-run the sweep at the landing rev rather than inheriting either number: the corpus is the surface, not the glob I chose.

## Patch chain — three digests, all measured here (appended)

Two hashes appear for this pre-test and they measure different objects; a third closes the chain. All three below are
my own measurements, and the first two are byte-identical at both the assigned base and the lane tip, which is the
proof that the SKILL.md pre-test is the same test at either rev:

```
$ git show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:SKILL.md | sha256sum
c105b874a8166542747ffa67b60810301c9bf94d32cf584252e96a4f9533f5ab  -      # 74174 B, 570 lines
$ git show 329e7d91d7d750031c35d264f0e34af1d0ce8385:SKILL.md | sha256sum
c105b874a8166542747ffa67b60810301c9bf94d32cf584252e96a4f9533f5ab  -      # same blob — SKILL.md unchanged by the plan commit
$ sha256sum build/ExecSkillGatesR74/landing-shape.patch
a3a2863552c103e4ee925c52e19a0d31ccda2a8c2cb7f5f834b3aa0dabc8cb64  landing-shape.patch   # 165 lines / 12634 B; equals the .sha256 pin file
$ git apply landing-shape.patch && sha256sum SKILL.md
dee61faf9849d71e32400692f65fef5fb942d6305df894f20b3933cc5ad2b595  SKILL.md             # 590 lines / 77132 B
```

Chain for the L1 to verify: `c105b874…f5ab` (base, 570/74174) + `a3a28635…cb64` (patch) → `dee61faf…b595`
(landed file, 590/77132). The patch pin is the patch's digest, not the file's; neither supersedes the other.
