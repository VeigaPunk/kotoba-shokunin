Result: MIXED — M46 and M47 hold and routed defects 1, 2, 3 (S050), 4, 6 and 7 hold; M45 breaks on two wrong captured-by facts and a stale fix cell whose own landing precondition was not met, and routed defect 5 breaks: `LOG.md` never gained `e5355a62`, and its pinned finding-delta run compares the wrong pair of revisions.

# W2CriticLesson — attack on `corpus/lessons/round-54.md` § Mistakes and § Routed defects at `5a097e12`

Seat: critic, leaf. Lane read-only. Every run was in my sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2CriticLesson`
(cloned from the lane, tip `58db81c4465b0e9b07ef2485b87d8970683afac6`, checked out per run and restored to the tip).
The only lane write is this file. No tools were installed or updated (python3, git, curl, strings only). No paid model
calls. Runs were at 2026-10-22T21:52Z–21:59Z.

## Verdict per row

| row | verdict | one line |
|---|---|---|
| M45 | **BREAKS** (fixable) | The evidence and the fix's ability to fail reproduce exactly. Two captured-by facts are wrong, and the fix cell still says "draft, seat sandbox" with a landing precondition that was not met |
| M46 | HOLDS | The times are confirmed by the L1 transcript. There is one adjacent unrecorded instance of the same class (the C1 base exit code was never observed), plus one wording nit |
| M47 | HOLDS | Every leg re-measured: exit 2 ×4 before, exit 0 ×4 after, normal output identical, honest registry 19 of 23 exit 1 |
| RD1 drift sentinel | HOLDS | Note: recorded in the round-54 lesson, not appended to `round-53.md` as routed, and the lesson does not say so |
| RD2 S046 | HOLDS | S060 supersedes S046's `teaches` cell; the pinned bytes re-fetched with 0 hits for "replac" |
| RD3 S050 | HOLDS for S050 | S061 plus a gate that goes red on `e792607e`. The 12 earlier changes are carried; see M45 |
| RD4 registry | HOLDS | 24 of 24 at `bf65974c`; both named verifiers have rows |
| RD5 tip runs | **BREAKS** | `LOG.md` has 0 hits for `e5355a62` at base, at `5a097e12` and at the tip. The "pinned" delta has its base later than its head |
| RD6 baseline note | HOLDS | Note-only diff; the regeneration reproduces `2d72d83f…` |
| RD7 carried | HOLDS | Nothing is claimed |

Cross-cutting: at `5a097e12`, every wave-1 report the lesson cites is absent (`git cat-file -e 5a097e12:.ufo/waves/round-54/build/{ScribeMistake,ExecTipRuns,ExecBaselineNote,CriticC2Sizing,ReviewCounters,ScribeS046Fix,ScribeS050Fix}.md` → absent ×7). All of them resolve from `58db81c4`, which commits them after the lesson. They resolve at the tip, so this changes no verdict; the ordering is recorded for the closure.

## M45 — `append-only-breach` — BREAKS (fixable defect, not a tradeoff)

**What holds (re-measured):**
- The landed gate is the seat's draft, byte for byte. `git show bf65974:verifiers/check_sources_append_only.py | sha256sum` gives `d4d1d62b…3805`, which equals the sandbox draft and the hash in the row. It is 189 lines (`diff` is empty).
- All of the row's arms reproduce:
  - `--base 55973a20 --rev e792607e` → `breach e792607e8 S050 anchor: …at commit `cfb894a5`… -> …at zed-industries/zed@…`, `1 change(s) in 1 of 1 commits`, exit 1.
  - `--base 55973a20 --rev e792607e^` → clean, exit 0.
  - `--base 34cfffbb --rev 55973a20` → `4 commits scanned, 0 protected-cell changes`, exit 0.
  - `--self-test` → `0 failure(s) over 14 assertions`, exit 0.
  - `--rev 7ad05d34` → exactly the 13 listed changes (`bfd5a583a` S022 teaches; `542f51567` ×6; `bf109cacc` ×5; `e792607e8` S050 anchor), `13 change(s) in 4 of 16 commits`, exit 1.
- Round 54 keeps rule 2. `--base 422ffd10 --rev 5a097e12` → `1 commits scanned, 0 protected-cell changes`, exit 0. The one in-place move is the S046 `used-by` cell, and § Rows touched logs it old→new.
- Every pointer resolves to the quoted text:
  - fleet `CORPUS.md:116` (rule 2, unchanged since `6a1dd8ce`, 2026-10-19);
  - `round-53.md:43-46`, `round-53-verifier-spotcheck.md:192`, `round-49.md:50`, `round-50.md:76-78`, `round-51.md:65`;
  - `round-52-verifier-spotcheck.md:30`.

**Counterexample 1 — "four read a revision's bytes with `git show`" is a miscount.** At `7ad05d34`, nine verifiers call `git show <rev>:<path>`:
- `check_alwayson_boxes.py:129`, `check_callee_rename.py:87`, `check_correction_sweep.py:128` and `check_description_thresholds.py:116`;
- `check_gate_registry.py:95`, `check_mcp_instructions.py:102`, `check_opencode_repin.py:88`, `check_overlap_levers.py:529` and `check_sibling_census.py:316`.

The count of four comes from `grep -ln 'git show'` (ScribeMistake.md:154), which matches only the literal text and misses the `git(repo, "show", …)` call form (`grep -lE '"show"' verifiers/*.py | wc -l` → 9). The conclusion still holds: no verifier runs `rev-list` or `git log` (0 files), and none compares a row with its parent. Only the number is wrong.

**Counterexample 2 — "cannot tell a rewritten row from an appended one" is false.** The round-52 test is `git diff … | grep '^-|'`; the `\|` in the table cell is the markdown escape for a pipe. A rewrite shows up as a removed line:

```
git diff <c>^ <c> -- corpus/SOURCES.md | grep -c '^-|'
bfd5a583a 1   542f51567 2   bf109cacc 4   e792607e 1      # every breach commit is flagged
55973a20  2   a78fec1ff 8                                 # permitted-cell moves only: also flagged
```

The test's real blind spots are different:
1. It flags permitted `status`/`used-by` moves the same way as protected-cell rewrites, so it cannot tell the two apart. Its red output is noise that a reader learns to discount.
2. It was run once, on round 52's range only (`c8579a4c..0c9180a6` → 0 removed lines), never as an instrument over rounds 49, 50 or 53.

This supports the new gate even better (it separates protected from permitted cells), but the cell states a false mechanism.

**Counterexample 3 — the fix cell is stale, and its own precondition went unmet without a record.** The cell reads "(draft, seat sandbox, 189 lines …) … Landing it needs a disposition of the 12 earlier changes (operator ratification, or one superseding row each) and … a SKILL.md Gate registry row". At `5a097e12`:
- the gate had already landed in `bf65974c` (commit subject: "M45 fix verifiers/check_sources_append_only.py");
- the registry row exists (`SKILL.md:467`);
- the 12 earlier changes have no superseding rows and no L0 question. `grep -n -i 'append-only\|ratif…' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` has no kotoba row on this; the nearest is the unrelated round-47 LOG item at `:85`. Line 56 of the lesson says only "carried, not corrected this round".

So the record says the gate is a sandbox draft, which it is not, and names a landing condition that the round then bypassed without recording a waiver. This is the over-wide/other-than-happened record class (M43/M46) inside M45 itself. One consequence follows: the landed gate in its unbounded form is red at the tip (`--rev 58db81c4` → `13 change(s) in 4 of 17 commits`, exit 1). The registry row's entry command, `--base <rev> --rev <rev>`, names no base, so a closure re-run has no pinned input. [INFERENCE] A reader cannot tell from the registry whether red-from-root is the expected state.

**Counterexample 4 — the pressure M45 describes is live again at the tip, and the lesson does not record it.** `verify_corpus_integrity.py` at `5a097e12` and at `58db81c4` reports `commit_unresolvable: corpus/knowledge/skill-listing-thresholds-round54.md:43: 451a02ff` (DRIFT `commit_unresolvable` observed=1 expected=0; `5/9 checks pass`, exit 1). It is the same mechanism that pushed round 53 into the S050 in-place edit: an upstream Gemini CLI hash written as "commit `451a02ff`" is read as a lane commit. `check_gate_finding_delta.py --base 422ffd10… --head 58db81c4…` → `new: corpus.pointers.commit_total, corpus.pointers.commit_unresolvable`, `new 2, resolved 1`, exit 1. The difference from round 53 is that this one sits in an entry, which may be edited, not in SOURCES. The safe repair is in the entry text, never in S046/S060.

Impacted axes: calibration (record wider/other than measured), consistency (registry row with an unpinned base).

**Smallest safe correction (text for the L1):**
- captured-by: "four read" → "nine read … (`git(repo, "show", …)` form; a literal `grep 'git show'` finds four)". Replace "which cannot tell a rewritten row from an appended one" with "which flags every in-place change as a removed line, permitted `status`/`used-by` moves included (`55973a20`: 2, `a78fec1ff`: 8), so it cannot separate a protected-cell rewrite from a permitted one; and it was run on round 52's range only".
- fix: "(draft, seat sandbox, …)" → "landed `bf65974c` (byte-identical to the seat draft, sha256 `d4d1d62b…`)". Replace "Landing it needs a disposition of the 12 …" with "Landed without a disposition of the 12 earlier changes: they are carried (§ Rows touched) and await operator ratification via L0 (question to file) or one superseding row each; until then the gate is red from the file's root and is run with a pinned `--base`." Pin the base in the registry row's entry command (e.g. `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`), or say why none is pinned.
- Record the `451a02ff` red at the tip in the lesson (no-harm), and repair the entry line `skill-listing-thresholds-round54.md:43` as the upstream form `google-gemini/gemini-cli@\`451a02ff\`` (the form round 53 used for Zed).

## M46 — `overclaim` (times) — HOLDS

- The class matches the lane's existing class for this defect: `overclaim` is M43's class (`round-53.md:14`, 3 uses across the lessons).
- The plan text says `21:30Z`/`21:31Z`/`21:32Z` (`e3371548:plans/round-54.md:6,27,42`). The erratum is `d051ec40` (`plans/round-54.md:71-79`).
- ScribeMistake § 2.2 marked the 21:08–21:11Z window as [INFERENCE]. I checked it against the L1 transcript (read-only, `~/.omp/agent/sessions/-Projects-shokunin/2026-10-22T17-34-59-437Z_…/KotobaR54.jsonl`): the C1 base run was at `2026-10-22T21:10:43.486Z` and the C2 base run at `21:11:36.798Z`, both before the plan commit's committer time of 21:12:08Z. The lesson's statement is now backed by more than the inference.
- captured-by: Q19 (`corpus/QUALITY.md:30`) asks that a value be "printed with its command and commit", with no time stamp, so "binds the values, not the stamps" is accurate.
- fix: it says honestly that the fix is "not shown able to fail mechanically … recorded, not counted". That is correct.

**Adjacent instance, same class, not recorded anywhere.** The plan says the C1 base run printed `backed 0 of 7`, "exit 1" (`plans/round-54.md:27`). The only C1 base run before the plan commit was `python3 -B verifiers/check_description_thresholds.py --rev 422ffd10 | tail -3; echo exit=$?`. It printed `exit=0`, which is `tail`'s exit code, not the counter's (transcript, 21:10:43.585Z). The counter's exit code was therefore never observed at plan time. [INFERENCE] It was taken from the docstring ("Exit 0 iff … at least TARGET"). The value is true: I re-measured `--rev 422ffd10` at 21:5xZ → `description thresholds backed 0 of 7 clients`, exit=1. Erratum 1 restates the C1 run without an exit code and the C2 run with "exit 1", which narrows the record without striking line 27. M46's practice fix (paste what the run printed) would have caught this too.

**Wording nit.** M46 says "Erratum `d051ec40` before any content". The enabling move `7ad05d34` landed before it (`git log`: `e337154` → `7ad05d3` → `d051ec4`), and the erratum itself says "before any C1 or C2 content". The lesson is slightly wider than its source.

Smallest correction: "before any C1 or C2 content (after the enabling move `7ad05d34`)". Add one erratum line: "C1 base exit 1 was not observed at plan time (the run piped through `tail`); re-measured exit 1 by W2CriticLesson."

## M47 — `unregistered-gate` — HOLDS

- Before (`7ad05d34`), `--self-test` exits 2 for all four gates, with argparse `required: --rev` (for `check_callee_rename`: `one of the arguments --rev --root`).
- After (`b55550b9`), all four exit 0. Last lines:
  - `box_proof_case_deletion`: `0 failure(s) over 10 assertions`;
  - `check_alwayson_boxes`: `self-test PASS: counted box exit 0; missing delegate exit 1`;
  - `check_callee_rename`: `0 failure(s) over 2 assertions`;
  - `check_opencode_repin`: `0 failure(s) over 2 assertions`.
- "Judging unchanged": the normal mode `--rev b38c32a0`, run from each script at `7ad05d34` and at `b55550b9`, gives byte-identical stdout and stderr for all four (`cmp` → identical ×4; exits 0; e.g. `killed 6 of 6`, `callee-rename robust 4 of 4 fixtures`). This is one input revision, not every input.
- The fix can fail, and I re-measured it rather than taking the critic's word. I fetched CriticC2Sizing's honest registry commit `46545fd53bea9545d4b8cb72b83c92f30915b564` (parent `7ad05d3`, "W0-honest") into my clone. `check_gate_registry.py --rev 46545fd5…` → `gate registry rows conformant 19 of 23 lane verifiers; phantom 0`, exit 1. Exactly the four rows fail with `gate with self-test none`. The self-test arm exists (`check_gate_registry.py:239`), and `--self-test` → `0 failure(s) over 22 assertions`. The counter is unchanged since the plan (`git diff --stat e337154 58db81c -- verifiers/check_gate_registry.py verifiers/check_description_thresholds.py` → empty).
- The disclosed bound is accurate: the flag check is a substring test (`ReviewCounters.md:40-42` F5; `CriticC2Sizing.md:53-54`), and erratum 2 (`plans/round-54.md:88-93`) carries the guard.
- Attribution: the four Reg* seats were told to "run its self-test mode (if any)" (`build-dispatch.json` task text), so they found the gap by running the scripts. CriticC2Sizing found it independently (`CriticC2Sizing.md:19,32`). This holds.
- Class nit, a tradeoff rather than a defect: the evidence is "gate without a self-test" (PROTOCOL.md § Gate standard, Self-test, line 398), while the class names its cause, the missing registry. It is defensible because the row says "the lane had no registry, so no one compared".

## Routed defects vs `round-53-verifier-spotcheck.md` § 8

**RD1 — HOLDS.**
- C1 works Per-render consumption.
- `git diff --stat 422ffd10 58db81c -- verifiers/verify_surfaces.py verifiers/verify_alwayson.py verifiers/verify_skill_checklist.py verifiers/checklist-baseline.json verifiers/surfaces-baseline.json` → empty.
- The two facts the closure asked for (the C1 repeat, and the tie-break reversal pointing to adjacency) are in `round-54.md:62-65`.
- Gap: § 8.1 says "Append to `lessons/round-53.md`", and `round-53.md` is unchanged from base to tip (no commit after `570876b`). Lane practice never appends to a previous round's lesson (the commits for rounds 50–53 are all in-round), so the substitution is reasonable. The lesson does not say it substituted, though. Correction: add "recorded here instead of appending to `round-53.md` (lessons are not edited after their round)".
- [INFERENCE] `b55550b9` adds self-tests to `check_alwayson_boxes.py` and `box_proof_case_deletion.py`, the checklist and always-on instruments. That is registry conformance, not a claim on that row, and the lesson's sentence is bounded to "no claim", so it holds.

**RD2 — HOLDS.**
- S060's `teaches` opens "supersedes S046's teaches cell —". The census regex `supersedes S[0-9]{3}` (`scripts/sources-census.sh:648`) accepts it. The contract's literal form is `supersedes S0NN —`, a cosmetic difference.
- I re-fetched `https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md` at 2026-10-22T21:57:06Z: HTTP 200, 3,807 B, sha256 `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf`, 116 lines. `grep -o -i replac` → 0. Line 97 holds "To specify a different name or a list of names, use the".
- S046 is unchanged except `used-by` (gate log line `5a097e12b S046 used-by`).
- Census `validate`, run against my clone at `422ffd10` and at `5a097e12` (temp root with a copy of `shokunin.conf`) → `kotoba ok`, exit 0 both times. The W04 duplicate-URL warnings change from S018/S019/S021 to S019/S021/S054/S055/S056.

**RD3 — HOLDS for S050.** S061's `teaches` opens "supersedes S050 —", S050 is not edited this round (the gate shows no S050 change in `422ffd10..58db81c4`), and the gate is red on `e792607e`. Its 17-word quote counts 17. The spot-check's "or ask the operator to ratify" applies only to S050, and the correction row satisfies it. The 12 older changes are outside § 8.3 but inside M45's fix cell; see M45 counterexample 3.

**RD4 — HOLDS.** `check_gate_registry.py --rev bf65974` → `conformant 24 of 24 …; phantom 0`, exit 0. It prints the same at `5a097e12` and `58db81c4`, and gives `0 of 23`, exit 1, at `7ad05d34`. `SKILL.md` at `5a097e12` has 24 `verifiers/` rows, and rows exist for both `verify_alwayson.py` and `check_gate_finding_delta.py` (count 2).

**RD5 — BREAKS (claimed done, partly not done).**
1. "`LOG.md` gains the missing `e5355a62`": `git show <r>:LOG.md | grep -c e5355a62` → `422ffd10` 0, `5a097e12` 0, `58db81c` 0. No round-54 commit touches `LOG.md` (`git log 422ffd10..58db81c -- LOG.md` is empty). This is stated as done and is not done.
2. The "finding delta with base pinned to `422ffd10` … at `b38c32a0`" has its base later than its head. `git merge-base --is-ancestor b38c32a0 422ffd10` is true, one commit apart. Its output, `resolved 3` (`ExecTipRuns.md:214-221`), only says that the spot-check commit introduced three drifts. It does not re-measure the questioned round-53 figure, "new 0, resolved 5 … against the moving ref `master`". The L1's own seat prompt asked for this pairing, so the seat ran what it was asked. The pinned re-measurement the closure needed is round 53's base to round 53's head, and I ran it:

   ```
   check_gate_finding_delta.py --base e78dff667237fba2e3cf9eccb802eff5bc9ea302 --head b38c32a078cbb91cda601d6566ae309b6e7ea8fb
   → base drift 5, head drift 0; new: none; resolved: tracked_files, unindexed, commit_total, report_dead, report_total
   → finding delta: new 0, resolved 5   exit 0
   ```

   So the round-53 figure is confirmed with pinned revisions, but by this seat, not by the lane's committed run.
3. These hold: corpus integrity 9/9 and the independent derivation exiting 0 at `b38c32a0`, the floors guard `surfaces observed=175 floor=175` at `b38c32a0` (`ExecTipRuns.md:141,174,184`), and the checklist runs, whose reds are environment-only (the clone basename and `..` citations).

Correction: land the `e5355a62` LOG line, or strike "gains" and mark it pending. Replace the inverted pair with the `e78dff66 → b38c32a0` run above (exit 0, `new 0, resolved 5`). Add the tip's own pinned delta, `422ffd10 → 58db81c4` → `new 2, resolved 1`, exit 1 (see M45 counterexample 4).

**RD6 — HOLDS.**
- `git show fed5686 -- verifiers/baseline.json` changes one line, `opencode_round53_note`. No other `+`/`-` line exists in `git diff 422ffd10 58db81c -- verifiers/baseline.json`, and the pin `538fcb1b…` occurs twice, unchanged.
- At 21:59:31Z, `sha256sum <binary>` → `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7` and `strings -n 4 <binary> | sha256sum` → `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98` (pipe exits 0 0). This matches `ExecBaselineNote.md:5-7`.
- The pointer `fed56863` resolves (`fed5686304613609…`).

**RD7 — HOLDS.** "Carried as listed by the closure" claims nothing. Nothing in round 54 touches the carried items' files (`verify_alwayson.py` and the checklist guard are unchanged; `check_gate_finding_delta.py` is unchanged).

## What I did not check

- The C1 client rows, the Gate table quotes other than S060, and the S061 fetch. Other falsify seats own these.
- Whether `b55550b9` leaves judging unchanged on inputs other than `--rev b38c32a0`.
- Whether any operator or L1 blessed the 12 earlier rewrites outside the lane and the fleet L0 queue.
