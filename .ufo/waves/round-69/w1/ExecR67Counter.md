# ExecR67Counter — D3 repair verification (C2/R68-3)

Round 69, wave 1. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Seat scope: verify — never modify — `verifiers/check_r67_routed_repairs.py` (D3/R68-3).

## Pins and scope

| item | value |
|---|---|
| lane HEAD | `a238989a96cb0d2b939679126b832d75b861ca6e` (one commit past the plan base `a5f7459`: "round-69: frozen plan, three counters …") |
| artifact | `verifiers/check_r67_routed_repairs.py`, sha256 `443af4b1f57ea979ebbdd2182bce4ad595ed06f9eb82f8e72d6344f84412be39`, mtime `2026-10-25 07:15:22 -0300`, `git status` = ` M` (uncommitted L1 repair; HEAD blob sha256 `a3b91848…`) |
| r68 base | `e94ae32a5cd8dc3ee8e2d247816784bec2750cc0` (lacks `corpus/lessons/round-68.md`; corpus index = 122 files) |
| r68 tip | `2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f` (all three records present; corpus index = 124 files) |
| sandbox | `git clone --shared` of the lane → `/tmp/k69-r67-final-*/repo`, working-tree verifier copied in; all executions there, never in the lane |

**Live-edit hazard, observed.** The verifier changed during verification: sha256 `ea462492…` at 07:15:08 → `443af4b1…` at 07:15:22. Everything below is the delivered snapshot `443af4b1…` (re-hashed after every run, stable). The superseded `ea46` snapshot is itself reasoned about in §4.

## 1. Source checks

### (1) "no `git checkout` invocation" — literal check FAILS; operative (no lane write) check PASSES

```
$ grep -n "checkout" verifiers/check_r67_routed_repairs.py
97:        proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout",
101:        proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", rev],

$ grep -n "git checkout" verifiers/check_r67_routed_repairs.py
(no match)          # the subcommand is separated from `git` by `-C <clone>`
```

- Line 101 **is** a checkout invocation. Under the assignment's literal wording ("contain no `git checkout` invocation (grep the source)") the delivered file **does not pass**.
- Under the plan's operative wording ("stops running `git checkout <rev> -- corpus verifiers` **in the lane**; it wrote the lane's index and working tree") it **does pass**: `clone` is `Path(tmp)/"clone"` inside `tempfile.TemporaryDirectory(prefix="k68-baseline-")`, created by `git clone --shared` from the passed repo. The pre-repair HEAD version (`a3b91848`) ran `git -C <repo> checkout <rev> -- corpus verifiers` against the measured repo; that invocation is gone.
- Empirical no-write proof (tip run against the sandbox repo, state hashed before/after): `.git/index`, `.git/HEAD`, `git ls-files -s` and `git status --porcelain` all **identical**; no worktree file touched (`find . -newer marker -not -path './.git/*'` → empty). The only durable write target is the throwaway clone.

### (2) "a missing records file is a content verdict" — PASS

Code path (delivered snapshot): `_materialize` writes empty bytes for a path absent at `--rev` (no `EnvError`); `check` sets `missing_records`, appends a finding and short-circuits `return 0, findings`. No branch raises `EnvError` for a missing record.

Observed contrast on the same revision:

| build | r68 base `e94ae32a` | exit |
|---|---|---|
| pre-repair HEAD `a3b91848` | `environment error: cannot read corpus/lessons/round-68.md at e94ae32a…` | **2** |
| delivered `443af4b1` | `r67 routed defects closed 0 of 4` + one D1 content finding | **1** |

**Residual defect (classification is now over-broad).** A 40-hex revision that does not exist is also swallowed as content:

```
$ python3 -B verifiers/check_r67_routed_repairs.py --rev 1111111111111111111111111111111111111111
r67 routed defects closed 0 of 4
  - D1: cannot read the round-68 records at this revision — a missing records file is a content verdict, not an environment error (LOG.md)
  - … (SCORECARD.md)
  - … (corpus/lessons/round-68.md)
EXIT=1
```

The file's own docstring says "Exit codes: 0 all four closed · 1 not all closed · **2 usage/environment error**", and `--rev` with no value still exits 2 (`environment error: --rev <full-sha> is required`). `_git_show`'s `None` conflates "revision absent" with "path absent"; a `git cat-file -e <rev>^{commit}` guard before `_materialize` would restore exit 2 for an unknown revision without touching the content-verdict path.

## 2. Observed runs (delivered snapshot `443af4b1…`)

```
$ python3 -B verifiers/check_r67_routed_repairs.py --rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0
r67 routed defects closed 0 of 4
  - D1: cannot read the round-68 records at this revision — a missing records file is a content verdict, not an environment error (corpus/lessons/round-68.md)
EXIT=1                                  # 0.043 s — no gate run (short-circuit)

$ python3 -B verifiers/check_r67_routed_repairs.py --rev 2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f
r67 routed defects closed 4 of 4
EXIT=0                                  # 0.587 s

$ python3 -B verifiers/check_r67_routed_repairs.py --self-test
PASS honest world: closed 4 of 4
PASS broken world rejected: D1 correction absent
PASS broken world rejected: D2 receipt path absent
PASS broken world rejected: D3 disclosure absent
PASS broken world rejected: D4 index row absent
PASS broken world rejected: D4 stale baseline
self-test: 0 failure(s) over 6 assertions
EXIT=0
```

Both frozen expectations reproduce exactly: base `0 of 4` exit 1 (not 2), tip `4 of 4` exit 0.

**D4 is substantive, not a presence floor.** Instrumented `_baseline_values` at the tip:

```
measured at tip: {"commit_total": 38, "report_total": 85, "tracked_files": 124, "unindexed": 0}
baseline expect: {"corpus.index.tracked_files": 124, "corpus.index.unindexed": 0,
                  "corpus.pointers.commit_total": 38, "corpus.pointers.report_total": 85}
match: True
```

The nested clone+checkout+gate actually measured the tip (values are tip-specific; base would differ).

## 3. Receipt consistency

- `.ufo/waves/round-69/recapture/r67-repairs-base.txt` is **byte-identical** to my observed base output (`diff` printed nothing → `IDENTICAL`), carrying `command:`, `measured-rev: e94ae32a…`, `exit=1`.
- `.ufo/waves/round-69/recapture/` is **untracked** (`git ls-files` count = 0), while the plan's D3 requires "with the base receipt committed". Gap for closure (R68-7 class); not a seat mutation.
- `C2-routed-measure.txt` (tip, `4 of 4`) has mtime `07:11:47`, **before** the verified artifact's `07:15:22` — it evidences an earlier build, not the delivered bytes. My independent re-run reproduces its claim; the receipt itself should be regenerated against `443af4b1…` when it is committed.

## 4. Non-vacuity / scoring notes (attack findings, non-blocking)

1. **The base `0 of 4` is short-circuit-shaped.** At `e94ae32a` the record set is missing `corpus/lessons/round-68.md`, so `check` returns before scoring D2/D3/D4. D2's presence floor is already satisfied at the base it must score 0 on: `LOG.md:2641` at `e94ae32a` names `.ufo/waves/round-67/controls/census-validate-append.txt` (OBSERVED / `junk-world` / the index row are all absent at base: grep counts 0). Proven empirically with the intermediate snapshot `ea4624…` (no short-circuit): base scored **1 of 4**, D2 closed, D1/D3/D4 finding. So the frozen base value holds only through the missing-record short-circuit; it is not four independent base failures.
2. **D4 is coupled to D1–D3.** `else: if not findings: closed += 1` grants D4 only when no earlier finding exists, so a partially repaired world can never score D4 even with a matching baseline. Endpoints unaffected; intermediate N is not a per-defect count.
3. **Superseded snapshot `ea4624…` fails the predicate:** base `1 of 4`; tip `environment error: the corpus gate could not be run at the measured revision`, exit **2** (its mirror `.git` pointed at the sandbox index at HEAD, so the gate's `git ls-files` listed a corpus file absent at the tip rev), and it dropped `report_total` from `_baseline_values` while `check` indexes `observed["report_total"]` (latent `KeyError`). Both defects are gone in `443af4b1…`; recorded here because the receipts were minted around that window.
4. All missing-record findings are labelled `D1:`, including `LOG.md`/`SCORECARD.md` (cosmetic).
5. `--self-test` has **no missing-records world** — its 6 assertions cover the honest world plus one broken world each for D1, D2, D3 and two for D4. The repaired content-verdict behaviour (item 2) is protected only by the base-revision run, not by the self-test.

## 5. Bounds

All executions in `/tmp` `git clone --shared` sandboxes (`/tmp/k69-r67-final-*`, `/tmp/k69-r67-headver-*`); no lane git write, no checkout in the lane, no lane file created or modified by this seat; no installs. Lane `git status` before/after: unchanged (pre-existing sibling/round-68 paths only).

## Verdict

- Frozen predicate: **reproduced** — base `r67 routed defects closed 0 of 4`, exit 1; tip `4 of 4`, exit 0; `--self-test` exit 0 (6/6).
- D3 item (2) missing-record classification: **met**, with an over-broad edge (unknown revision → exit 1 instead of 2).
- D3 item (1): **met on the plan's operative terms** (no checkout or write in the measured repo; checkout confined to a throwaway clone) and **not met on the assignment's literal terms** (`grep -n checkout` finds `["git", …, "checkout", "-q", rev]` at line 101). The lane-write defect R68-3 describes is fixed; the literal "no checkout invocation" phrasing is not satisfiable by this build unless the temp-clone checkout is replaced (e.g. `git archive <rev> | tar -x -C <tmp>`); if the literal criterion is the standard, this is the seat's blocker, otherwise no change is required.
