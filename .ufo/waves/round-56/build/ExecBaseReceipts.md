Result: DONE — seven revision-stamped no-harm receipts at `b0b7140b` are saved; the dispatched battery is green except `verify_corpus_integrity` (pre-existing red) and the checklist in a plain clone (layout artifact), and one routed observation: the gate registry is red from the round's own freeze commit on.

## Deliverable

`.ufo/waves/round-56/build/base-receipts.txt` — 259 lines, sha256
`1e8ebad1b70730272781eafd1805271fe87b07fdd67685a84094dc3aca7f3b36`. Every block carries
`git rev-parse HEAD: b0b7140b5a7cf8a50f13989ee6285fc8ee245c41`, the `date -u` line, the command,
verbatim output and the exit code (Q36). Outputs were checked line-for-line against the run logs
(`/fast/scratch/hyaku/kotoba-r56/ExecBaseReceipts/logs/*.log`, hashes below); 0 missing lines in
all ten.

## Layout (why two clones, both at `b0b7140b`)

- `clone`: `/fast/scratch/hyaku/kotoba-r56/ExecBaseReceipts/clone` — plain clone (bounds template).
- `mirror`: `.../mirror/kotoba-shokunin` — same revision, directory named `kotoba-shokunin`, parent
  holding a symlink to every fleet-root entry except the lane (the round-49 `NoHarmGates` layout).
- Both: `git status --porcelain --ignored=matching` empty, no file newer than checkout, `TMPDIR`
  empty after all runs. The lane working copy was read once, read-only (`rev-parse HEAD` =
  `3d8efd7c…` at 02:50:38Z — it moved during the wave, which is why the receipts are taken in
  clones pinned to the base). No lane file was written except `base-receipts.txt` and this report.

## Dispatched battery at `b0b7140b` (all in the plain clone unless noted)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `python3 -B verifiers/verify_skill_checklist.py` | 1 | 8 PASS, 3 FAIL — all three layout artifacts (below); the mirror clone at the same revision: **11 PASS, 0 FAIL, exit 0** |
| 2 | `check_gate_registry.py --rev b0b7140b` | 0 | `rows conformant 26 of 26 lane verifiers; phantom 0` |
| 3 | `check_sources_append_only.py --base b0b7140b --rev b0b7140b` | 0 | `0 commits scanned, 0 protected-cell changes` — vacuous, range is empty |
| 4 | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md` (registry form) | 0 | `rows 20 verified 20`; full form (`--province PROVINCE.md --skill SKILL.md`) also exit 0 with `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, `length 1019 of 1024` |
| 5 | `verify_corpus_integrity.py` | 1 | `4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable` |
| 6 | `check_assertion_floors.py` (+ `uptime`) | 0 | 13 PASS rows, no FAIL; `elapsed=60s`; load 10.87/12.14/9.05 before, 13.07/12.43/9.33 after |
| 7 | `check_gate_finding_delta.py --base b0b7140b --head b0b7140b` | 0 | `base drift 5, head drift 5`, `new: none`, `resolved: none` |

## Findings

1. **Layout artifacts, not revision facts (calibration).** In a plain clone the checklist exits 1 on
   `trigger.name_directory` (`name 'kotoba-shokunin' != directory 'clone'`) and both citation checks
   (`../`-tokens such as `../.ufo/reports/round-7/kotoba.md` resolve against repo *ancestors* —
   `verify_skill_checklist.py` `citation_resolve`, ~:1484-1505 — and scratch has no fleet-root
   parent). The mirror clone at the same revision passes 11/11. This reproduces round-49
   `NoHarmGates` finding 2; any later comparison must use the mirror layout or read those three rows
   as artifacts.
2. **Two of the seven receipts are green only because their range is empty.** (a)
   `check_sources_append_only --base b0b7140b --rev b0b7140b` scans 0 commits; the registry form
   without `--base` at the same revision is **exit 1** — `13 change(s) in 4 of 18 commits`
   (pre-existing, same 13 as round-55's receipt at `f0e5de82`, which read "4 of 17"). So the
   dispatched no-harm baseline must not be read as "sources history clean at base"; the append-only
   rule is red across full history and only the *new* commits are being judged. (b)
   `check_gate_finding_delta --base b0b7140b --head b0b7140b` compares the revision with itself:
   `new 0, resolved 0` is vacuous by construction; its useful output is the base DRIFT-id set
   (5 ids), which the post-wave run must compare against.
3. **`verify_corpus_integrity` is red at base (exit 1, 5 DRIFT ids)** — pre-existing, not caused by
   this wave: the baseline (`verifiers/corpus-baseline.json`) still expects the round-54-era numbers
   (tracked 81 vs 85, report_total 51 vs 56, …). The same gate was red at round-55's base with the
   same five ids. Any post-wave comparison should be by DRIFT-id set, not exit code.
4. **Floors gate green under load (routed defect 4 context).** 13 PASS, exit 0, 60 s wall at load
   average 10.9 → 13.1 (uptime pasted before and after in the receipt). The nested-timeout exit 2
   reported for this guard did not reproduce at base under this load; the receipt records load and
   elapsed so a later red can be read against them.
5. **ROUTED (not fixed, not my file): the registry gate goes red inside the round's own commits.**
   `check_gate_registry.py` at `0f58a469` and at `e02f5f5d` prints
   `verifiers/check_agent_definitions.py  no registry rows naming it: 0 (need 1)` and the same for
   `verifiers/check_agentdef_boxes.py`, `conformant 26 of 28`, **exit 1** — versus `26 of 26`, exit 0
   at `b0b7140b`. The two counters were committed without `SKILL.md` § Gate registry rows, and no
   round-56 seat owns adding them (grep of `build-spec.json` for `registry` finds only the
   line-budget seat, whose prompt forbids touching the Gate registry, plus my own receipt item).
   Restoring the base value
   needs two registry rows; I did not add them (out of my scope: I write this report and the
   receipt only).
6. **Census command note.** The registry row names `<census.md>`; the lane's only census file is
   `corpus/knowledge/sibling-overlap-census-round49.md`. The bare form runs only the row check
   (`rows 20 verified 20`); `--province`/`--skill` are the cross-checks that make it a full guard.
   Its default `--fleet` is `/home/vgpnk/Projects/shokunin` (`check_sibling_census.py:142`), so it
   read sibling lanes read-only at their row-pinned commits from the real fleet root.

## Evidence (commands, exit codes)

- Clone provenance: `git clone -q …/kotoba-shokunin .../ExecBaseReceipts/clone && git checkout -q
  b0b7140b…` → `rev-parse HEAD` `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41`, exit 0; mirror clone the
  same, exit 0; re-read at 02:50:38Z, both unchanged.
- Transcription check (Python over receipt text vs logs): 0 missing lines for
  registry(27), sources(1), census-bare(1), census-full(4), corpus-integrity(24), finding-delta(4),
  checklist-clone(11), checklist-mirror(11), sources-full(39), floors(15).
- Supplemental registry runs: `--rev 0f58a469` and `--rev e02f5f5d` → exit 1, `26 of 28`
  (logs `registry-freeze.log`, `registry-erratum.log`).
- Log hashes (sha256): registry `748a5115…`, sources `ef1a8a15…`, census-bare `eaefd923…`,
  census-full `323d7e11…`, corpus-integrity `17ff729b…`, finding-delta `028e290f…`,
  checklist-clone `d6b982e5…`, checklist-mirror `da9361db…`, floors `a55de408…`,
  sources-full `e1da2887…`, registry-freeze `fdce6ee5…`, registry-erratum `6ebba3db…`.

## Scope, risks, gaps

- Not run: the `--self-test` arms of the seven gates (not in the dispatched list; the floors gate
  internally runs the nested self-tests it owns). Not run at `0f58a469`/`e02f5f5d`: the other six
  gates — so finding 5 is scoped to the registry gate alone.
- `verify_skill_checklist.py` in the mirror depends on fleet-root entries existing at run time (the
  `../`-token rule); it reads them, never writes.
- No subagent or labrat was spawned (allowance unused); no tool was installed or updated; no lane
  git/jj command was run; no paid model call was made.
- Scratch (all writes): `/fast/scratch/hyaku/kotoba-r56/ExecBaseReceipts/{clone,mirror,logs,tmp}`.
