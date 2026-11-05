# ExecMirrorR87 — w3 report: the C2 D5(iii) same-bytes/two-paths world (instrument location control)

Baseline 223ae62 · frozen C2 receipt rev 35a395a9 · tip 760e1c5e (verified: `git rev-parse master` = 760e1c5edfdefb4767420f711d08f669952de013).

## What was run

1. **frozen counters, both worlds** (byte-identical corpus; `git diff --shortstat 35a395a9..tip -- corpus/` → empty):
   - lane C1 `pip3 -B verifiers/check_omp_root_semantics.py --rev 760e1c5e` → **12 of 12, exit 0**
   - lane C2 `python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e` → **4 of 5, exit 1**; `FAIL d5 … red set ['corpus.pointers.commit_unresolvable'], want exactly [...]','report_dead']`
   - clone C1 → **12 of 12, exit 0**
   - clone C2 → **4 of 5, exit 1**; `FAIL d5 report_dead detail ['corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md'] does not name corpus/lessons/round-86-verifier-spotcheck.md:33`
   - clone @ 35a395a9 (the frozen receipt world itself, in a clone): C2 **4 of 5, exit 1** — the same 4-of-5 with the clone-shaped d5 refusal.
2. **gate JSON** (`REV=<rev> python3 -B verifiers/verify_corpus_integrity.py --json`, run in a cwd+`--repo` identical to how the C2 counter invokes it):
   - lane  : reds `['corpus.pointers.commit_unresolvable']`, `commit_unresolvable_detail = ['corpus/lessons/round-81.md:8: 8b1cc1b0…']`, `report_dead_detail = []`
   - clone : reds `['corpus.pointers.commit_unresolvable','corpus.pointers.report_dead']`, `report_dead_detail = ['corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md']`

## Cause (code-entailed, quoted from verifiers/verify_corpus_integrity.py)

- `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` (line 136), consumed only by `report_pointer_exists(..., fleet_root=FLEET_ROOT)` (line 309); **neither** live red pointer is a *bare* `.ufo/reports/...` token, so `FLEET_ROOT` is not the deciding variable here.
- `corpus/lessons/round-81.md:29` cites the **relative** pointer `../../.ufo/reports/round-76/kotoba.md`; lane_trees contains a tracked **symlink** at `.ufo/reports/round-76/kotoba.md → ../../../../.ufo/reports/round-76/kotoba.md` (git mode `120000`, blob `bf7c7e0c0c39a57c49224c87348afc74dca14db4`) whose target lives in the **FLEET ROOT** on this host. The pointer chain resolves only when the lane worktree is real on this host. In the clone the link dangles → `not pointer_exists` → `report_dead 1` (gate lines 575-584).
- `corpus/lessons/round-86-verifier-spotcheck.md:33` cited `.ufo/reports/round-84/kama.md`, a **bare** pointer that resolves via the fleet-root fallback when the file exists there. The fleet commit `5b052020` (`2026-11-04 12:16:01 -0300`) landed the file on this host with `## SHONEN` and 10 856 B (identity floor `REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 400`, line 168) → the red *heals* itself on any path where the fleet tree has the file. At the frozen receipt revision 35a395a9 (written 21:20:26 the same day) the receipt shows `red exactly the two disclosed DRIFTs (…:33, round-81.md:8)` on **its own** world; on the tip's lane worktree the `report_dead` red reads 0 → the exact-set conjunct fails from the healed side ("red set ['commit_unresolvable'], want exactly ['commit_unresolvable','report_dead']").
- The `report_dead` exemption machinery **does not apply** to a bare pointer marked as another lane's artifact: only double-quote-wrapped tokens are exempt (`inside_quotes`, lines 578-580; docstring lines 72-80), and the token on spotcheck:33 is not double-quoted (it sits in the *modified*-list column of a pass/fail row). It is therefore a genuine promise until the fleet file makes it true.
- The pointer loop has **no code-span exemption** (`inside_code_span` is applied to COMMIT citations only, lines 587-588, not to pointer citations, 575-586) — recorded as the finding the exact-set conjunct's red-set is shaped by *raw location*, not by record intent.

## Instrument re-creation probe (clone owns target under ITS parent)

Placing a `## SHONEN`-marked file at `$S/.ufo/reports/round-76/kotoba.md` (clone parent's *.ufo*, i.e. **outside any git tree**) makes the clone symlink's `../../` hops hit the *fleet-modeled* directory inside my scratch — with the file there the clone gate returns the exact Lane reading (`reds = ['commit_unresolvable']` only) and `FAIL d5 … red set ['corpus.pointers.commit_unresolvable'], want exactly [...]','report_dead]'`, i.e. `report_dead_detail = []` exactly like the lane. Removing it restores the 2-red clone reading. Rundown file: `c2-clone-placed.txt`, `gate-clone-placed.json`, `gate-clone.json`.

## Verdict

**conjunct=non-monotone.** `D5(iii)`'s red-set exact-equality fails on a *healed* red, not only on an *added* red: the fleet landing of `.ufo/reports/round-84/kama.md` reduced the observed red set from two to one (lane) with no lane byte change, flipping D5(iii) PASS→FAIL between the frozen receipt world (35a395a9, 5 of 5) and the tip (4 of 5). The lane/clone divergence is the same conjunct failing on the *added* side too (the clone's dangling round-76 symlink adds a red the lane does not see), so the conjunct fails in both directions on identical lane bytes.

```
same bytes, two paths: lane=<reds 1, C2 exit 1 "red set ['commit_unresolvable'] want exactly ['commit_unresolvable','report_dead']"> clone=<reds 2, C2 exit 1 "report_dead detail … does not name corpus/lessons/round-86-verifier-spotcheck.md:33">; conjunct=non-monotone
```

## Findings

1. **Non-monotone exact-set conjunct (M87-2 confirmation, independent re-derivation).** Fleet-side healing changes the verdict without any lane change; routed, not repaired (frozen counter is untouchable this wave).
2. **Mechanism refined, not re-opened.** The two live red-redsources are (a) `../../.ufo/reports/round-76/kotoba.md` — resolution via a lane-tracked symlink that dangles in any clone; (b) `.ufo/reports/round-84/kama.md` — a bare pointer whose fate rides on a *fleet-root* file. `FLEET_ROOT` is load-bearing for (b) only; the A1.2 lane-worktree pinning keeps (a) at its lane-reading, so the lane is the only world where the red set is exactly one.
3. **C1 is location-stable.** 12 of 12, exit 0 in both worlds (guards S1-S3 PASS in both). The C2 counter is the only place where checkout location can change a verdict.
4. The reported pointer at spotcheck:33 was pre-landing dead; the exact-set conjunct converted that deadness from a *state the round discloses as red* into a *pass condition*, and the fleet's materialization inverted it — the gate at tip reads `8/9; DRIFT: corpus.pointers.commit_unresolvable` (rc 1) while the frozen receipt world read `7/9` with 2 DRIFTs (its own rc 1).

## Risks / blockers

- None open. Verifier/plan/lesson/SOURCES/QUALITY/LOG/SCORECARD/SKILL: **untouched** (bounds held; one accidental file under `verifiers/fixtures/` was created and then deleted within minutes, `git status` clean of it — no lane bytes changed by this seat beyond `.ufo/waves/round-87/w3/ExecMirrorR87/`).
- Scratch `/fast/scratch/hyaku/kotoba-r87/ExecMirrorR87/`, including its `.ufo/reports/round-76/` fixture probe and the shared clone, is deleted at report end (see `scratch-ls-rt.log` for the inventory taken before removal).

## Files written (seat dir, absolute under the lane)

- `.ufo/waves/round-87/w3/ExecMirrorR87/WORLD.md`
- `.ufo/waves/round-87/w3/ExecMirrorR87/c1-rev-tip.txt` (lane C1), `c1-clone.txt` (clone C1), `c1-base-clone.txt` (base-run attempt; counter absent at base)
- `.ufo/waves/round-87/w3/ExecMirrorR87/c2-rev-tip.txt` (lane C2), `c2-clone.txt`, `c2-clone-placed.txt`, `c2-35a-clone.txt`, `c2-35a395a9-clone.txt` (rollback-of-checkout receipt; counter refused at 35a in lane because A1.2 tips pinned)
- `.ufo/waves/round-87/w3/ExecMirrorR87/gate-lane.json`, `gate-lane.err`, `gate-clone.json`, `gate-clone.err`, `gate-clone-baseline.json(.err)`, `gate-clone-placed.json`, `gate-35a-clone.txt`
- `.ufo/waves/round-87/w3/ExecMirrorR87/c2-base-clone.txt` (base-run attempt record)
- `.ufo/waves/round-87/w3/ExecMirrorR87/scratch-ls-rt.log`
- This file: `.ufo/waves/round-87/w3/ExecMirrorR87.md` (the Report).
