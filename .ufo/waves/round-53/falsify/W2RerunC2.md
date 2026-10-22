# W2RerunC2 — falsify: C2 measurement + erratum §3 disposition guard

Result: MIXED — the C2 reruns and the erratum §3 guard both hold at the judged revisions, but the frozen counter itself has no absolute/`..` delegate rejection and I reproduce the out-of-revision delegate printing `2 of 8` live (severity MEDIUM; compensated only by the procedural guard).

Seat bounds honored: lane untouched (read-only git only); all writes in the sandbox clone `/fast/scratch/hyaku/kotoba-r53/w2/W2RerunC2` (cloned from the lane, checked out at `c775d6823bfca8f0de8c0874032a954438b38edc`, then one exploit commit inside the clone); no installs, no paid model calls, no URL fetches this seat; no `task` spawns.

## F1 — Rerun fidelity: HOLDS

All three reruns reproduce the quoted fresh measurements; first line byte-identical in each case.

```
$ python3 -B verifiers/check_alwayson_boxes.py --rev aeed0890efb7cb62ef1364ce7d7ba5566ef3fed6
always-on boxes executed and discriminating 0 of 8
  alwayson.04: not counted (disposition unexecuted)
  alwayson.07: not counted (disposition unexecuted)
exit=1
```
Cross-check at that rev: `git show aeed0890:verifiers/checklist-baseline.json` → section has exactly 8 always-on boxes; `alwayson.04` and `alwayson.07` both `unexecuted:surface = AGENTS.md/CLAUDE.md class; …` — matches the two "not counted (disposition unexecuted)" lines.

```
$ python3 -B verifiers/check_alwayson_boxes.py --rev 55973a20ac728f7b11ac8de518620ba128c13afa
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
```

```
$ python3 -B verifiers/check_alwayson_boxes.py --rev c775d6823bfca8f0de8c0874032a954438b38edc
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
```

The floors commit `c775d682` does not disturb C2, and the repairs commit `aeed0890` correctly still reads 0 of 8.

## F2 — Erratum §3 disposition guard at `55973a20`: HOLDS

`git show 55973a20:verifiers/checklist-baseline.json`, always-on section (8 boxes, `alwayson.01`–`alwayson.08`, of 41 total boxes):

- `alwayson.04` → `delegated:verifiers/verify_alwayson.py`
- `alwayson.07` → `delegated:verifiers/verify_alwayson.py`

Guard, both prongs:

1. Relative: both strings are repo-relative — no leading `/`, no `..` component.
2. Listed: `git ls-tree -r 55973a20ac728f7b11ac8de518620ba128c13afa --name-only` → 11,039 paths; `grep -Fx 'verifiers/verify_alwayson.py'` → 1 exact match (`verifiers/verify_alwayson.py`), exit 0.

Stability and symlink check:

- `git diff 55973a20 c775d682 -- verifiers/checklist-baseline.json` → empty; the dispositions at the judged tip are the same two relative in-tree paths.
- `git ls-tree 55973a20 verifiers/verify_alwayson.py` and same at `c775d682` → `100755 blob a761c9d062eb87824bcec3ebed65d6a790707c39` both — a regular blob, not a `120000` symlink, so `Path.is_file()` in the counter cannot be made to follow a tracked link out of the tree at these revs.

So the guard the erratum prescribes for the C2 verdict passes at the revision the claim is measured on.

## F3 — Counter has no absolute/`..` rejection: BREAKS (severity MEDIUM, pre-acknowledged by erratum §3)

Defect: `verifiers/check_alwayson_boxes.py:144` joins without validation:

```python
script = tree / d.split(":", 1)[1]
```

`pathlib` discards `tree` entirely when the disposition's path is absolute, and a `../`-prefixed path escapes the extracted tree; `check_alwayson_boxes.py:141` only checks the `delegated:` prefix. This is exactly the CriticC2Sizing finding the erratum records.

Live reproduction (sandbox clone only; the delegate is an extracted copy of the revision's own instrument placed untracked outside the tree):

```
$ python3 mutate_map.py            # both dispositions -> delegated:/fast/scratch/hyaku/kotoba-r53/w2/W2RerunC2/outside/verify_alwayson.py
mutated 2 dispositions -> delegated:/fast/scratch/.../W2RerunC2/outside/verify_alwayson.py
$ git commit ...                   # sandbox rev ad119e2171dd146f903bf6057399c0326b94e79f
$ python3 -B <lane>/verifiers/check_alwayson_boxes.py --rev ad119e2171dd146f903bf6057399c0326b94e79f --repo <clone>
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
```

An out-of-revision delegate prints the exact C2 target line, exit 0. The prescribed guard catches that revision: the absolute path is not relative and `git ls-tree -r ad119e2 --name-only | grep -Fx '/fast/.../outside/verify_alwayson.py'` → no match, exit 1.

Impact, bounded:

- At the judged revs the guard passes (F2), so the landed C2 claim stands; this defect does not overturn it.
- Because the counter is frozen at `3bb0a7a3`, no in-counter fix is possible without breaking the frozen-counter rule; the fix lives in the verdict procedure — the guard (relative + listed by `git ls-tree -r <rev>`) must run at every future C2 measurement, not once.
- The guard as specified is sufficient against this whole class: absolute → fails the relativity prong; `..` → relative but never listed by `ls-tree`; in-tree untracked → not listed. It is not enforced by any code, only by procedure.

## F4 — Frozen counter: HOLDS

`git diff 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 c775d6823bfca8f0de8c0874032a954438b38edc -- verifiers/check_alwayson_boxes.py` → empty, exit 0. The counter measured at tip is the counter frozen at the plan commit.

## F5 — Rev-pinning and separability: HOLDS

By source (`check_alwayson_boxes.py:127-135`), the counter reads the map with `git show <rev>:verifiers/checklist-baseline.json` and the instrument with `git archive --format=tar <rev> -- verifiers` — object DB only, never the lane working tree, so the reruns are rev-pinned regardless of checkout state; it reads no file outside `verifiers/`, so C1 work cannot move it. Exit contract `return 0 if n == len(CASES) else 1` (`:166`) — exit 0 iff both pinned boxes count, matching both dispositions observed. Note (as erratum §3 says): `N of T` where `T = len(section)` comes from the revision's map (8 here, verified), and exit 0 is independent of `T`, so "of 8" is carried by the printed text only.

## Residual risk and verification gaps

- I did not mutation-test the instrument `verifiers/verify_alwayson.py` itself; my rerun proves only that the 12 pinned cases discriminate as the counter pins them (6 PASS + 6 FAIL, all matched). Semantic adequacy of those cases is sibling seats' scope (MutCountC2 / ReviewAlwaysOn).
- The `..`-escape variant of F3 was not executed live; the BREAK verdict for it is code reading of the same join at `:144` (`pathlib` semantics) — [INFERENCE] for that variant specifically; the absolute variant is executed and proven.
- The guard is procedural. Nothing in the repo forces it to run; a future revision can print `2 of 8` exit 0 through an out-of-revision delegate and pass the counter alone (proven at `ad119e2`). Closure must re-run F2's two prongs at whatever tip it judges.
- No sources were opened by this seat; the SOURCES basis for alwayson.04/.07 was not re-verified here.
