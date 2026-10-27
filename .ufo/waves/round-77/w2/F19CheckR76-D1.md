# F19CheckR76-D1 — round-77 w2 falsification: R76-D1 stray-path cleanup preservation

Seat: reviewer (leaf, godspeed), lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Attacked revision: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`), branch `master`, the only commit past r76 tip `2f67554`. Working tree clean for every path examined below (`git status --porcelain -- kotoba-shokukin/` -> empty).
Axes (godspeed): depth, consistency, calibration, freshness, operability. Every move below is a read-only check or a scratch-clone re-run; nothing lane-owned was written except this report.

## 1. Verdict summary

**FALSIFIED AT THE LANDED TIP.** R76-D1 ("delete the stray duplicate `kotoba-shokukin/…` path from the lane repo", `corpus/lessons/round-76-verifier-spotcheck.md` §5.1) is **not preserved at `6523ace` — it has not landed at all**. Both stray files are still tracked in the HEAD tree and still on disk; no commit in any ref deletes them; no committed gate detects them; and the w1 detection script is structurally blind to this exact defect class. C1/C2 remain red at the tip (no claim data is committed — the round's data landing has not happened), so nothing green exists to falsify either. This is a blocker, not a landed-state pass: any w2 claim that "R76-D1 stray path removed" is done at the current tip is false.

## 2. Frozen counters: pins and re-runs at the landed tip

Counter bytes at HEAD match the plan's pins exactly:

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show HEAD:verifiers/check_desc_craft.py | sha256sum
cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e   (pin: same)
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show HEAD:verifiers/check_r75_routed_repairs.py | sha256sum
989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63   (pin: same)
```

Scratch clone (shared, identity set before any hypothetical write; toplevel asserted):

```
$ git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r77/F19CheckR76-D1/clone
$ git -C <clone> config user.name scratch-r77 && user.email scratch@example.invalid
$ git -C <clone> rev-parse --show-toplevel
/fast/scratch/hyaku/kotoba-r77/F19CheckR76-D1/clone
$ git -C <clone> rev-parse HEAD
6523aced1ee0ebe07dca996213bdc645a6acbd1e
```

C1 at the tip (own exit captured, no pipelines):

```
$ cd <clone> && python3 -B verifiers/check_desc_craft.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e
measured-rev: 6523aced1ee0ebe07dca996213bdc645a6acbd1e
(a) snapshot chain: fail
(b) located quotes: fail
(c) act-on: fail
(d) self-audit: fail
(e) registry: fail
(f) provenance: fail
description craft backed 0 of 6
exit=1
```

C2 at the tip (own exit captured):

```
$ cd <clone> && python3 -B verifiers/check_r75_routed_repairs.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /fast/scratch/hyaku/kotoba-r77/F19CheckR76-D1/work
R1: open
R2: open
R3: open
R4: open
r75 routed repairs closed 0 of 4
exit=1
```

Self-tests at the tip (own exits):

```
$ python3 -B verifiers/check_desc_craft.py --self-test        -> self-test: 0 failure(s) over 53 assertions, exit=0
$ python3 -B verifiers/check_r75_routed_repairs.py --self-test --work <work>  -> self-test: 0 failure(s) over 27 assertions, exit=0
```

Read: consistent with the committed base receipts (`.ufo/waves/round-77/receipts/c1-base-…txt`, `c2-base-…txt`, both red at `2f675548`). **No claim data is committed at the landed tip; C1/C2 are unverifiable-as-green and must not be reported landed. Blocker, per the wave contract.**

## 3. R76-D1 state at the tip — the falsified item

Routed defect text (committed at `2f67554`, `corpus/lessons/round-76-verifier-spotcheck.md` §5.1): "Delete the stray duplicate `kotoba-shokunin/` typo path `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` from the lane repo (the correct copy exists)". The round-77 plan (landed at `6523ace`) lists under "Routed r76 defects handled": "**R76-D1** stray `kotoba-shokukin/` path removed" — present tense in a plan whose tip does not contain the removal.

Facts (all commands read-only, in the lane):

```
$ git ls-tree -r HEAD --name-only | grep -i shokukin
kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md
kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md
$ git log --oneline HEAD -- kotoba-shokukin/
6ce2724 round-76: recover fleet-root A18 seat report          (A)
ac9f295 round-75: preserve recovered misroot seat report      (A)
$ git log --all --oneline -- kotoba-shokukin/ | wc -l          -> 4 commits, ALL adds, no deletion in any ref
$ test -e kotoba-shokukin && echo exists                       -> exists  (working tree still carries both files)
$ git status --porcelain=v1 -- kotoba-shokukin/                -> empty  (tracked, unmodified)
```

Duplication and loss analysis (blob ids at HEAD):

| stray path | blob | rooted counterpart | verdict |
|---|---|---|---|
| `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` | `6b0a54c7` | `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` = same blob `6b0a54c7`; `git show` sha256 of both = `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb` | pure duplicate; safe to delete |
| `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` | `7bbf72a1`, sha256 `a419cc6f2513d0a5a6bf0887e3694445ffd04cbaa3872c47053c3f96f4c9fdd9` | `.ufo/waves/round-75/w1/R75Facet48.md` **ABSENT** (`git ls-tree HEAD -- .ufo/waves/round-75/w1/R75Facet48.md | wc -l` -> 0; sibling listing has Facet01–47, 49–64) | the stray is the ONLY copy of a real r75 w1 seat report; deleting it destroys data |

So at the tip: (i) the routed R76-D1 deletion is absent from the tree; (ii) the routed text's own premise "the correct copy exists" is false for a SECOND stray the route did not name (`R75Facet48`) — the copy exists only under the typo prefix; (iii) the plan's "handled: … removed" wording is not true of any committed revision. **Preservation check fails for the trivial reason: there is nothing preserved — the cleanup itself is unlanded.**

## 4. Mutation test of the relevant gate (operability)

The only R76-D1 follow-up instrument w1 produced is `.ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh` (fleet-root untracked-path sweep; read-only: one `git status` call at the fleet root — source read before running). The live tree IS the mutant (stray path committed): running the gate on the mutant must fail for the gate to be sound. Observed:

```
$ cd /home/vgpnk/Projects/shokunin && bash kotoba-shokunin/.ufo/waves/round-77/build/E11StrayAndMisroot.misroot_sweep.sh ; echo exit=$?
sweep: CLEAN — no untracked fleet-root path matching kotoba|round-77
exit=0
```

**Survivor.** The sweep scans only fleet-root `??` entries; the actual defect (stray files committed and clean INSIDE the lane) produces neither a fleet-root untracked path nor a lane `git status` line, so the gate reports CLEAN over a tree that still carries both strays. A lane-side `git status` check would also miss it (files are tracked and clean). No committed verifier references the stray path either:

```
$ git grep -c 'kotoba-shokukin' HEAD -- verifiers/    -> no matches (rc=1)
```

Net: **nothing committed, and nothing drafted, detects the R76-D1 state.** Reintroduction or non-removal is invisible to the round's own instrumentation.

## 5. Minimal repair (recommendation; no lane writes made)

1. Land the cleanup exactly as w1 E11StrayAndMisroot §4 prescribes (single commit, three named files — never a directory): `cp` the stray `R75Facet48.md` to `.ufo/waves/round-75/w1/R75Facet48.md`, `cmp` (expect 0), `rm` both stray files, then `jj-lane.sh commit --as kotoba` naming `.ufo/waves/round-75/w1/R75Facet48.md`, `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`, `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md`. Expected diff: `A` rooted Facet48, `D` both strays. [INFERENCE on the jj mechanics: rests on E11's helper reading; I did not re-read `jj-lane.sh` myself and did not execute any mutation.]
2. Strengthen detection so the class is guarded: add to the sweep (or a committed gate) a lane-side tracked-tree check, e.g. `git ls-tree --name-only HEAD | grep -Fx kotoba-shokukin` must be empty (or `git cat-file -e refs/heads/master:kotoba-shokukin` must fail), exit 1 on hit. Harm to other axes: none — no gate reads either stray path (§4 grep), the deliberate `kote-shokunin/` fixture dirs live under `verifiers/fixtures/dispatch-prompts/d0*/fleet/` and are untouched, and C1/C2/no-harm inputs are disjoint from `.ufo/waves/round-7[56]/w1` report paths. Frontmatter wording owed: `corpus/lessons/round-75.md:12` and `round-75-verifier-spotcheck.md:44` still describe a clean recovery that the tree contradicts (E11 §5 already routed this; restating as in-scope for the same fix).
3. Freshness: no external source is involved in R76-D1 (repo-internal defect); no S213 re-open is owed from this seat. Quote reopening and the battery belong to sibling seats; the landed tip contains no new quotes/rows/lessons to reopen (freeze commit touched only `plans/round-77.md` + receipts — `git show 2f67554 --stat` = the 87-line spotcheck lesson; `6523ace` = plan + base receipts).

## 6. Residual risk and verification gaps

- I did not execute the `rm` + `jj-lane.sh commit` recipe (lane/git/jj mutation is out of my scope); the end-to-end deletion transition is [INFERENCE] from the helper analysis, not an observed run.
- Broadened stray census at HEAD: the only lane-name-typo top-level entry is `kotoba-shokukin` (top-level listing checked: `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus kotoba-shokukin plans verifiers`). Sibling lanes were not scanned (out of lane scope).
- Fleet root currently holds an older-wave untracked spill `.ufo/waves/round-75/` (E11's `--extra` output, reproduced by me), invisible to the sweep's required `kotoba|round-77` filter — pre-existing, disclosed, not caused by round 77.
- Scratch dir `/fast/scratch/hyaku/kotoba-r77/F19CheckR76-D1` is removed before yield; no tools installed (none needed); no pacman; ≤4 concurrent processes; every quoted exit is the command's own (no pipelines across exit boundaries).

VERDICT: FALSIFIED at landed tip 6523ace — R76-D1 stray-path cleanup is not landed (both kotoba-shokukin/ files still tracked and on disk, one the only copy of R75Facet48, which must be restored before deletion); C1 0-of-6 exit 1 and C2 0-of-4 exit 1 at the tip with counters byte-matching their pins, so no claim data is landed (blocker); the w1 misroot sweep is mutation-blind to committed strays (prints CLEAN, exit 0); minimal repair = w1 E11's restore+delete single commit plus a committed lane-side stray-tree check, harming no axis.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F19CheckR76-D1.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F19CheckeckR76D1.md
