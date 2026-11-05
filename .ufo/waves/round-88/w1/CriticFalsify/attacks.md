# CriticFalsify — round 88 attacks on the frozen predicates

Seat: CriticFalsify (critic, attack set). Scope: falsify C1 (root-semantics v2) and C2 (routed D5 v2).
Lane HEAD measured: `89579c7` (the freeze commit adds only `plans/round-88.md`; `git diff --stat 4df1e80 HEAD -- verifiers` is empty). Tip `4df1e80` also measured.
Frozen bytes checked: `verifiers/check_omp_root_semantics.py` sha256 prefix `6e826f3bf8d45853` (r87 counter, unchanged). `verifiers/check_r86_routed_repairs_v2.py` sha256 `10bd5508a7e5f8c1…` (the C2 v2 gate, as landed).
Scratch: `/fast/scratch/hyaku/kotoba-r88/CriticFalsify/` (deleted at yield). Probe scripts and integrity JSON copied to `receipts/`.
Nothing in the lane was written. No git write in the lane. No ELF execution.

## Summary

| id | predicate | survivor | evidence | admission |
|---|---|---|---|---|
| C2-S2 | D5 (i)+(ii) | in-place silencing of a red check passes D5 v2 | `silenced_inplace`: v2 `d5 PASS` | **blocks** |
| C2-S3 | D5 (i)+(ii) | re-recording `corpus-baseline.json` expects heals three reds, D5 v2 passes | `rerecord`: v2 `d5 PASS`; baseline file outside the kill rule | **blocks** |
| C2-S1 | D5 control `w_added_red` | the frozen control, as written, cannot FAIL under (ii); v2 self-test is red 1 of 16 on that arm | `addred_same`: `new_vs_base=[]`; v2 `--self-test` rc 1 | **blocks** (control must change before scoring) |
| C2-S4 | D5 (ii) | growth of instance count inside an already-DRIFT name is invisible | `addred_count` (3 unresolvable): v2 `d5 PASS` | bound (disclose) |
| C2-S5 | D5 `<rev>` | integrity reads the working tree and fleet root; verdict on `report_dead` depends on clone location | lane HEAD: `report_dead` green; scratch clone at same rev: `report_dead` DRIFT | bound (disclose) |
| C1-S1 | C1 conj. 1 (S3) | one commit rewrites both ledgers: a fake root grounds 12 of 12 | `s3_both`: r87 counter `12 of 12`, exit 0, `row 11 GROUND '/tmp/x/skills'` | **blocks** |
| C1-S2 | C1 conj. 3 | module mislabels accepted: header order only | `mod_row2`, `mod_row12`: r87 counter `12 of 12`, exit 0; conj.-3 accepts 47 of 84 (row, module) pairs | **blocks** (fix: nearest-preceding header, §C1-S2) |
| C1-S3 | C1 conj. 2 | the four r87 forged worlds are accepted under any legal binding set that contains `cwd` or `skills` | ELF lines of the forged worlds carry `cwd` and `skills` | **blocks** unless binding sets are keyed per pattern and reviewed |
| C1-S4 | C1 conj. 1+4 | absolute / `~user` patterns escape `$HOME` with no `..` | `/etc/skills`, `/tmp/x/skills`, `~root/skills`: `pattern_problem=None`, `bound=True` | **blocks** |
| C1-S5 | C1 M==4 / N==12 | a counter that lookup-matches known ledgers passes both targets with no grounding | construction (inference, not built against v2) | bound; fix by a fresh honest-variant control |
| C1-S6 | C1 conj. 4 | "module code visibly walks" has no mechanical extractor; the walk is not on the reader line | `function Wne` @173865174, reader @173865724 | bound (predicted inert, as r87) |

Controls checked: the removal control works (v2 identity FAIL on `removed_check`, 8 vs 9 names). The blanket-refusal failure mode is caught by N==12 on the honest ledger (r87 counter's honest run reads 12). A blanket-accept counter is caught by M==0 on the do-nothing run (the r87 counter reads `12 of 12` on all four forged worlds, so M==0, which is the frozen do-nothing value). Both positive controls exist; neither catches S5.

## C2 — routed D5 v2

Measurement: the v2 gate (`check_r86_routed_repairs_v2.py --rev <rev> --repo <world> --work <scratch>`) and the integrity gate run in scratch copies of the base or tip. Base reds (6): `index.tracked_files`, `index.unindexed`, `pointers.report_total`, `pointers.report_dead`, `pointers.commit_total`, `pointers.commit_unresolvable`. Names: 9.

Worlds (each a committed scratch commit):

| world | construction | integrity change | v2 D5 | expected by plan |
|---|---|---|---|---|
| `addred_same` | new lesson with unresolvable commit `1234567890abcdef…` | `commit_unresolvable` observed 1→2, stays DRIFT | **PASS** (new_vs_base=[]) | FAIL (ii) |
| `addred_count` | new lesson with two more unresolvable commits | `commit_unresolvable` observed 3, stays DRIFT | **PASS** | FAIL (ii) |
| `addred_new` | new lesson with `commit \`zz-not-hex\`` | `commit_nonhash` 0→1, DRIFT | **FAIL** `monotone FAIL: DRIFT at rev not at base: ['corpus.pointers.commit_nonhash']` | FAIL (ii) |
| `silenced_inplace` | `report_dead` verdict forced PASS, check kept | `report_dead` DRIFT→PASS | **PASS** | FAIL (i) (plan says identity catches silencing) |
| `removed_check` | `commit_nonhash` removed from `CHECKS` | names 8 | **FAIL** `identity FAIL: rev has 8 names, base has 9; missing ['corpus.pointers.commit_nonhash']` | FAIL (i) |
| `rerecord` | `corpus-baseline.json` equal expects set to observed 170/125/59 | three equal reds PASS | **PASS** (monotone holds; DRIFT set shrinks) | (not in plan; survivor) |
| lane tip `4df1e80` | none | none | **PASS**, `closed 5 of 5` | PASS |
| lane HEAD `89579c7` | none | none | **PASS**, `closed 5 of 5` | PASS |

**C2-S1 — control defect.** The frozen control `w_added_red` (an unresolvable commit citation) cannot FAIL a name-level monotone test, because `commit_unresolvable` is already DRIFT at base. The v2 gate's own self-test reports `1 failure(s) over 16 assertions` on exactly that arm (`FAIL arm w_added_red (frozen control)`), yet `C2_READY` was written with the text "bytes final". The handoff precondition ("after the v2 gate's own --self-test passes") is not met. Fix, before any candidate is scored: replace the control with a new-name shape (`commit_nonhash`, row `addred_new`), which v2 FAILs. If a candidate has already been scored against the old control, the kill rule applies and the control change is a finding, not a repair.

**C2-S2 — silencing passes (i) and (ii).** Identity (i) compares name sets only, so an in-place silenced check keeps its name. Monotone (ii) then reads a silenced red as a healed red. The integrity script's own self-test catches it: `silenced_inplace` self-test reads `FAIL evaluate/zero-drift: got 'PASS' want 'DRIFT'`, `self-test: 2 failure(s) over 178 assertions`. Fix: D5 must also require `verify_corpus_integrity.py --self-test` exit 0 at `<rev>` (the base self-test is `0 failure(s) over 178 assertions`; the tip self-test is the same).

**C2-S3 — re-recording heals by convention.** `verifiers/corpus-baseline.json` is outside the kill rule and outside the fixture list. Setting its three `equal` expects to the observed values (170, 125, 59) turns `tracked_files`, `report_total` and `commit_total` PASS; v2 reads `d5 PASS`. The r87 closure already re-recorded this file (its `note` field). Fix: D5 requires the blob of `verifiers/corpus-baseline.json` at `<rev>` to equal its blob at `223ae62`, or the file joins the kill-rule list.

**C2-S4 — count growth in a red name.** Known to v2 (its F1 disclosure). Bound it: monotone should compare `(name, observed)` and require observed not to grow inside a name that is DRIFT at base.

**C2-S5 — location dependence.** `verify_corpus_integrity.py` reads the working tree and the fleet root, not `<rev>`. At lane HEAD `89579c7`, `report_dead` is green (fleet `.ufo/reports/round-84/kama.md`, 10 856 B). The same revision in a scratch clone reads `report_dead` DRIFT (`observed=1 expected=0`). The lane run: `corpus.pointers.report_dead` absent from the non-PASS list. The v2 monotone test still holds because base and rev are measured in the same location, but the healed-red claim is location-specific. Bound it in the admission text; do not claim `<rev>`-pinned integrity.

Other lane-side facts: integrity at lane HEAD reads `tracked_files 173 vs 172`, `report_total 134 vs 127`, `commit_total 60 vs 59`, `commit_unresolvable 1`, `unindexed 1`. The three equal-check drifts are not the plan's numbers; the plan's tip reading of `report_total` and `commit_total` is not re-measured here.

## C1 — root semantics v2

The v2 counter (`check_omp_root_semantics_v2.py`) has not landed (`C1_READY` absent). Every C1 result below is on the frozen r87 counter (the do-nothing control) or on the r87 conjunct helpers imported read-only. Each is a construction that v2 must refuse; they are not v2 verdicts.

Honest baseline: r87 counter at tip `4df1e80` reads `omp root semantics grounded 12 of 12`, exit 0. The ELF sha256 is `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`. The honest ledger is `verifiers/omp-skill-roots-semantics.tsv` at `4df1e80`.

**C1-S1 — both ledgers rewritten in one commit (blocks).** Scratch commit `7c240ed462a9379caca804a51210d4a3ab909756`: `verifiers/omp-skill-roots.tsv` and `verifiers/omp-skill-roots-semantics.tsv` both change `~/.agents/skills` to `/tmp/x/skills`, reader unchanged.

```
$ python3 -B verifiers/check_omp_root_semantics.py --rev 7c240ed4… --repo <world>
row 11 GROUND '/tmp/x/skills' module='coding-agent/src/discovery/agents.ts' @173865523
guard S3 pattern-set PASS
omp root semantics grounded 12 of 12
exit=0
```

Cause: S3 compares the semantics ledger's patterns with the round-86 ledger *at the same `<rev>`*, which the same commit can rewrite. Conjunct 1 is therefore self-consistency. Fix: anchor S3 to a frozen commit that a rev cannot rewrite (the round-86 closing SHA), and key binding sets by the pattern string (an unknown pattern has an empty set, which is refused).

**C1-S2 — module provenance (blocks).** Two single-cell forgeries:

- `mod_row2` `9600b00c…`: row 2 (`{cwd}/.claude/skills`) module changed to `coding-agent/src/discovery/builtin.ts`. r87 counter: `row 2 GROUND '{cwd}/.claude/skills' module='coding-agent/src/discovery/builtin.ts' @173840364`, `12 of 12`, exit 0.
- `mod_row12` `3a6b694f…`: row 12 (`~/.omp/agent/managed-skills`) module changed to `coding-agent/src/discovery/helpers.ts`. r87 counter: `row 12 GROUND … module='coding-agent/src/discovery/helpers.ts' @173809938`, `12 of 12`, exit 0.

Measured by importing the r87 helpers read-only (`modmis.py`): conjunct 3 accepts 47 of 84 (row, module) pairs. Conjunct 3 checks only that some `// packages/<module>` header precedes the quote, so any earlier header passes. Repair that costs nothing on the honest ledger: the module must be the **nearest** preceding header. `nearest.py` shows all 12 honest rows agree with the nearest preceding header (rows 1–12, `AGREE`), and the two forgeries disagree (`claude.ts` precedes offset 173840364, not `builtin.ts`; `managed-skills.ts` precedes offset 173809938, not `helpers.ts`; derived from the same table).

**C1-S3 — binding tokens are substrings, and the four forged worlds carry generic tokens (blocks unless sets are pattern-specific).** `bind.py` on the forged lines:

```
w_cross_row7   (.github/skills <- codex line)   line='return Xr.join(u.cwd, ".codex");'   present candidates: ['cwd','join','n']
w_misattr_row12 (managed-skills <- plugins line) line='dir: Zo.join(R.path, "skills"),'    present candidates: ['skills','join']
w_renderline_row6 (.opencode/skills <- render)   line='c += `**Tags:** ${t.tags.join(", ")}' present candidates: ['join']
```

`cwd` is produced by the `{cwd}` placeholder in the row's own pattern, so it is a legal binding token under the frozen wording ("names at least one token that the row's root literal … produces"). `skills` is a segment of the managed-skills literal, so it is legal too. A binding set that contains either accepts a forged world. Whole-ELF census of join-carrying lines (`elfprobe.py`, regex window ±200 bytes, 5 677 lines in total): `cwd` on 100, `skills` on 15, `projectDir` on 13, `agent` on 50, `.codex` on 4, `.github` on 2, `managed-skills` on 1. Generic tokens bind many lines. Fix: the binding token must come from the root's own segment (`codex`, `github`, `managed-skills`), never the placeholder, and must appear on the line; a set is reviewed before scoring, not chosen after.

Note also rows 3/4, 10/11 and 6/7 share one reader quote each in the honest ledger (the same ELF line serves two roots). Binding by root literal then has nothing to bind to on those lines (the literal `.agent`, `.github` is not on the line); the frozen wording would have to use a generic token there. Disclose this as a grounding bound, not a pass.

**C1-S4 — `$HOME` escape by a path string (blocks).** Conjuncts 1 and 4 on the r87 helpers (`escape.py`):

```
'/etc/skills'           pattern_problem=None  bound=True  -> ACCEPTED
'/tmp/x/skills'         pattern_problem=None  bound=True  -> ACCEPTED
'~root/skills'          pattern_problem=None  bound=True  -> ACCEPTED
'~//etc/skills'         bound=False ("expands outside $HOME (/etc/skills)")  -> REFUSED
'{cwd}//etc/skills'     bound=False                                           -> REFUSED
'/home/u/../../etc/skills' pattern_problem: `..` segment                      -> REFUSED
```

Conjunct 4 binds only `{cwd}/` and `~/` rows. An absolute or `~user` pattern is never checked against `$HOME`, and no `..` is needed. The escape is symlink-free. Combined with C1-S1 (one commit rewrites both ledgers) it yields a fake root grounded at 12 of 12. Fix: every candidate root of every row must lie under `$HOME` or the session cwd ancestors (for `{cwd}/`), and absolute or `~user` patterns are refused.

**C1-S5 — lookup-table oracle (bound; construction, not built).** A counter that hashes the honest ledger, the synthetic honest fixture and the four r87 forged ledgers, and prints 12 on the honest hash and rejects the rest, satisfies N==12 on the tip, M==4, and S1–S3. Nothing in the frozen predicate requires scoring a world the counter has not seen. Fix: a fresh honest-variant control, for example an honest ledger in which one row's reader quote is a different join line in the same module, must score 12 with the same counter. This is an inference (no such counter exists yet) and is marked as such.

**C1-S6 — conjunct 4 has no mechanical "walk" (bound).** The predicate compares the computed expansion set with "the set the row's module code visibly walks". The walk for rows 3/4/10/11 is `function Wne` at 173865174 (`bind.py`'s pattern `function Wne`), 550 bytes before the reader quote at 173865724, not on the quote line itself. An extractor for that set is not specified; a hand-typed constant makes the comparison circular. This is the r87 inertness again. Bound: state the conjunct as unmeasured until the walk is extracted mechanically.

**Overfit bound.** M==4 counts four worlds that the critic built. A counter tuned to those four ledgers is not evidence about other forgeries; C1-S1, C1-S2 and C1-S4 are three further worlds the four do not cover.

## Which survivors block admission

1. **C2-S2 and C2-S3 block.** D5 v2 passes a world where the integrity gate was silenced in place, and a world where its expectations were re-recorded. Both are honest-state failures the plan says D5 must refuse.
2. **C2-S1 blocks.** The frozen control cannot fail under the monotone test as written; v2's own self-test is red on it while `C2_READY` says final. The control must change before the first candidate is scored, or it is a kill-rule event.
3. **C1-S1, C1-S2 and C1-S4 block.** The r87 counter (and any v2 that keeps its conjuncts 1, 3 and 4) reads `12 of 12`, exit 0, on forged ledgers. The fixes are cheap and measured above: anchor S3 to a frozen SHA, nearest-header module check, and a `$HOME` containment rule for every row.
4. **C1-S3 blocks unless binding sets are reviewed.** The binding predicate is the only conjunct that catches the r87 cross-row and render-line worlds; its frozen wording admits `cwd` and `skills`.
5. C2-S4, C2-S5, C1-S5 and C1-S6 are bounds to disclose in the admission text.

## Receipts (committed under `receipts/`)

- `elfprobe.py`, `bind.py`, `modmis.py`, `nearest.py`, `escape.py`: ELF and conjunct probes (read-only mmap, no exec).
- `c2worlds.py`, `c2recheck.py`: integrity world builder and reader.
- `integrity-base.json`, `integrity-tip.json`, `integrity-lane.json`, `rerec.json`: integrity `--json` output at base (scratch), at tip (scratch), at HEAD (lane, read-only run), and after the baseline re-record world.

## Not run

- The v2 C1 counter (absent). C1 results are constructions against the r87 counter and its helpers.
- The `w_healed` control (not built; a dead-pointer removal is trivially PASS on monotone).
- The r87 counter's C2 gate at tip was not re-run; the plan's `4 of 5` is taken from the plan.
