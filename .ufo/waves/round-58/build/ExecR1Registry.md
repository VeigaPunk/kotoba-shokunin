Result: DONE — both registry rows now carry an in-cell withdrawal annotation in the verdict-map cell
(no `SKILL.md` line added, 600 → 600), and `python3 -B verifiers/check_gate_registry.py --rev <rev>`
stays at exit 0 with `gate registry rows conformant 32 of 32 lane verifiers; phantom 0` — measured at
the frozen base, at the annotation commit, and again after applying the delivered patch to lane `HEAD`
`a39942c`.

Deliverable: `.ufo/waves/round-58/build/ExecR1Registry.patch` (4354 bytes, 22 lines,
sha256 `30c8a60245e5818866c7399a7f82783a6ca29b844290b9e6ce09b9a380c00fed`).
Report written 2026-10-23 08:11Z (`date -u` line pasted below).

## 1. The change (two lines, one cell each)

Base file: lane `SKILL.md` at `3de87aad29e960c95ed35840442f424c48c29729` (lane lines 461 and 469;
`git rev-parse HEAD:SKILL.md` in the apply clone prints blob `23cd061a7483f3786477258e93f873570959adf9`,
identical at lane `HEAD` `a39942c`, so one patch serves both).

`SKILL.md:461` — before/after differs only in the verdict-map cell:

- before: `… | 0=clean, 1=failed, 2=could-not-evaluate | \`--self-test\` | in-file | temp archives and per-case dirs under \`$TMPDIR\` (removed) | kotoba |`
- after: `… | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r57; not a claim gate until redesigned and re-controlled | \`--self-test\` | in-file | temp archives and per-case dirs under \`$TMPDIR\` (removed) | kotoba |`

`SKILL.md:469` — same shape:

- before: `… | 0=clean, 1=failed, 2=could-not-evaluate | \`--self-test\` | in-file | per-row temp git repos under \`$TMPDIR\` (removed) | kotoba |`
- after: `… | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r58 before data (plan erratum 1); not a claim gate until redesigned and re-controlled | \`--self-test\` | in-file | per-row temp git repos under \`$TMPDIR\` (removed) | kotoba |`

No other byte of `SKILL.md` changes: `git diff --stat` = `SKILL.md | 4 ++--`, `1 file changed, 2
insertions(+), 2 deletions(-)`; `wc -l` = 600 before and after, so item ExecBudgetMove is not
triggered. Row order, header, separator and every other row are untouched.

Why the verdict-map cell and not another: the frozen counter compares the name, kind and owner cells
for equality after stripping backticks (`verifiers/check_gate_registry.py:20-33`, `judge_row`), so
those three cells cannot carry prose. The verdict-map cell only has to *contain* at least one
`<code>=<class>` pair with no code twice (`check_gate_registry.py:26-33`); trailing prose is not
forbidden. The self-test cell would also parse, but it describes a flag, not a claim status; the
pinned-values and write-scope cells describe paths and writes. The verdict cell is therefore the
first cell that can carry the status without changing what the row asserts.

## 2. Why not the plan's `probe` relabel (measured, not argued)

`plans/round-58.md:13` routes R1 as "registry row re-labelled `probe` with the withdrawal reason".
That remedy is rejected by the frozen counter: a `probe` is rejected if its verdict map declares
`1=failed` **or** its source has an exact active `--self-test` handler
(`verifiers/check_gate_registry.py:34-36`). Both scripts have that exact handler
(`verifiers/check_infoless_fences.py:881`, `verifiers/check_sweep_mutants.py:384`), and both rows
declare `1=failed`.

Measured in the sandbox with the counter's own `judge()` over the annotated revision
(`check_gate_registry.py:20-36` rules, no script executed):

| world | conformant | phantom | non-conformant reasons |
|---|---|---|---|
| A. delivered annotation (sandbox `6921fae`) | 32 of 32 | `[]` | — |
| B. `probe` relabel, row otherwise unchanged (plan:13 route) | 30 of 32 | `[]` | both rows: `probe verdict map declares 1=failed`, `probe script has an exact --self-test handler` |
| C. `probe` with `1=failed` dropped and self-test cell set to `none` | 30 of 32 | `[]` | both rows: `probe script has an exact --self-test handler` |

So no row-only probe relabel can reach 32 of 32; making it conformant would require editing the
scripts' `--self-test` handlers (out of scope, and it would remove the gates' self-test) or the
frozen counter (forbidden). Deleting the rows would leave `registry rows naming it: 0` and score 31
of 32. The in-cell annotation is the smallest change that keeps the counter green. Note that
`plans/round-58.md:94` already blesses exactly this form for `check_sweep_mutants.py`: "stays
registered with an in-cell `claim withdrawn` annotation (the R1 rule applied to this round's own
counter)".

`S092`-style source fetches: none — this defect work opened no URL, so no access receipt applies.
No tool was installed or upgraded (nothing needed); no network use.

## 3. Evidence (commands, exits, output)

Sandbox statement for the hashes below: every cited commit is a **sandbox** commit, never a lane
commit.

```
$ date -u
Fri 23 Oct 2026 08:11:15 AM UTC

# A. base (sandbox checkout of the frozen commit)
$ cd /fast/scratch/hyaku/kotoba-r58/ExecR1Registry   # git rev-parse HEAD: 3de87aad… (detached)
$ timeout 300 python3 -B verifiers/check_gate_registry.py --rev 3de87aad29e960c95ed35840442f424c48c29729 > _run/registry-base.txt 2>&1
base_exit=0
$ tail -1 _run/registry-base.txt
gate registry rows conformant 32 of 32 lane verifiers; phantom 0

# B. annotation commit, sandbox 6921fae17e133bfd81cd953b33530fa29cdf9ca0 (/fast/scratch/hyaku/kotoba-r58/ExecR1Registry)
$ timeout 300 python3 -B verifiers/check_gate_registry.py --rev 6921fae17e133bfd81cd953b33530fa29cdf9ca0 > _run/registry-annotated.txt 2>&1
annotated_exit=0
$ tail -1 _run/registry-annotated.txt
gate registry rows conformant 32 of 32 lane verifiers; phantom 0
$ diff _run/registry-base.txt _run/registry-annotated.txt && echo IDENTICAL
IDENTICAL                      # every row's OK/no verdict and the trailer are byte-identical to the base run

$ timeout 300 python3 -B verifiers/check_gate_registry.py --self-test > _run/selftest.txt 2>&1
selftest_exit=0
$ cat _run/selftest.txt
self-test: 0 failure(s) over 28 assertions

# C. patch application to lane HEAD (fresh clone, sandbox)
$ git -C /fast/scratch/hyaku/kotoba-r58/ExecR1RegistryApply rev-parse HEAD   # checkout of a39942c
a39942c94027cd3875144284112422d1aa642260
$ git -C … rev-parse HEAD:SKILL.md
23cd061a7483f3786477258e93f873570959adf9
$ git -C … apply --check .ufo/waves/round-58/build/ExecR1Registry.patch
APPLY_CHECK_OK
$ git -C … apply … && wc -l SKILL.md && git -C … hash-object SKILL.md
APPLIED
600
5d257735b54f4821946b53b91f9bac4d674720cd
# post-apply commit: sandbox 19d23d87cbbcf198de82423499066c932d3b2090 (/fast/scratch/hyaku/kotoba-r58/ExecR1RegistryApply)
$ cd /fast/scratch/hyaku/kotoba-r58/ExecR1RegistryApply
$ timeout 300 python3 -B verifiers/check_gate_registry.py --rev 19d23d87cbbcf198de82423499066c932d3b2090 > _run/registry.txt 2>&1
counter_exit=0
$ tail -1 _run/registry.txt
gate registry rows conformant 32 of 32 lane verifiers; phantom 0
$ grep -c " OK $" _run/registry.txt
32
```

The post-apply file is byte-identical to the annotation-branch file:
`sha256sum SKILL.md` prints `77dd7daf6c10709b119055a819d88bff6b2295cae4cdb8528cefd7491952492e`
in both clones (base file sha256 `9b51cab880766ce30440eaabe0593f08a0d45d2d6d99588a39f26f93af6602cf`).

Patch digest: `sha256sum .ufo/waves/round-58/build/ExecR1Registry.patch` =
`30c8a60245e5818866c7399a7f82783a6ca29b844290b9e6ce09b9a380c00fed`; `wc -c -l` = 4354 bytes,
22 lines; the patch is `git diff --src-prefix=a/ --dst-prefix=b/` (plain `git diff` in the
jj-colocated clone emits `i/`/`w/` mnemonic prefixes, which I replaced for portable `git apply`).

## 4. Frozen-counter compliance, cell by cell

For each of the two rows, re-parsed at the annotation commit: kind cell strips to `gate`; entry
command still contains `verifiers/<file>`; `PAIR_RE.findall` on the verdict cell returns exactly
`[('0','clean'), ('1','failed'), ('2','could-not-evaluate')]` — the annotation adds no digit-pair,
so the "gate declares 0=clean and 1=failed" and "no code twice" rules still hold; the self-test cell
still names only `--self-test`, an exact `add_argument` handler in both files; pinned values `in-file`;
write scope non-empty; owner `kotoba`. No row is a phantom (name cells unchanged). Em dash is already
present 103 times in `SKILL.md`, so non-ASCII is not new to the file.

Other consumers of the table: `grep -rn "Gate registry" --include=*.py verifiers/` matches only
`check_gate_registry.py` (parser) and the docstring line
`verifiers/check_could_not_evaluate.py:6`; that gate never parses the table — it consumes a
hardcoded map and invokes `check_gate_registry.py` at the pinned revision
`422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` (`verifiers/check_could_not_evaluate.py:128`), which is
older than this change, so its expectation is unaffected. `verifiers/README.md:4` only names the
columns.

## 5. Divergence the L1 should record (not resolved by me)

`plans/round-58.md:13` states the probe relabel; the routed defect item and the frozen counter
(§2 measurements) forbid it, and `plans/round-58.md:94` already prescribes the in-cell annotation for
the r58 counter. I did not edit the frozen plan. Suggested round-note line: R1 delivered as in-cell
annotations because a `probe` row is rejected for both scripts (`1=failed` plus exact `--self-test`
handler, measured 30 of 32), per `plans/round-58.md:94`.

## 6. Risks and limits

- The kind column still reads `gate`, because the frozen counter admits only `gate` or `probe` there
  and a probe row is impossible without changing the scripts. A reader who skims only that column is
  still told "gate"; the withdrawal is visible in the verdict cell of the same row. Fixing the column
  itself is a redesign of the counter, not a defect patch.
- The annotation is prose inside a machine-parsed cell. The frozen parser tolerates it (§4), but a
  future counter that required the cell to hold nothing but pairs would flag it; that would be a new
  frozen measurement, and the same text could then move to the free-text write-scope cell
  [INFERENCE — not measured].
- Citation discipline: `6921fae…` and `19d23d8…` are sandbox commits in
  `/fast/scratch/hyaku/kotoba-r58/ExecR1Registry` and `/fast/scratch/hyaku/kotoba-r58/ExecR1RegistryApply`;
  they are not in the lane and must never be cited bare. The only lane hash cited here is lane `HEAD`
  `a39942c94027cd3875144284112422d1aa642260` (read-only).
- I did not run any other lane gate, and did not run either annotated script itself; the rewrite
  behaviour of `check_infoless_fences.py`/`check_sweep_mutants.py` is unchanged by this patch (no
  verifier file is touched).
- Lane working-tree state from me: only `.ufo/waves/round-58/build/ExecR1Registry.patch` and this
  report were written; `git status --porcelain` in the lane shows the pre-existing untracked
  `.ufo/waves/round-58/build/` and `.ufo/waves/round-58/build-taskcall-sent.json` plus nothing else
  of mine.

## 7. What the L1 should run after integrating

1. `git apply .ufo/waves/round-58/build/ExecR1Registry.patch` in the lane (or `jj` equivalent), then
   `git diff --stat` → expect `SKILL.md | 4 ++--`.
2. `wc -l SKILL.md` → 600 (budget unchanged).
3. `timeout 300 python3 -B verifiers/check_gate_registry.py --rev <lane commit>` → expect
   `gate registry rows conformant 32 of 32 lane verifiers; phantom 0`, exit 0.
4. `timeout 300 python3 -B verifiers/check_gate_registry.py --self-test` → expect
   `self-test: 0 failure(s) over 28 assertions`, exit 0.

## 8. Sources & frontier

SOURCES: unchanged — defect work (registry annotation); no source rows opened or touched, no URL
fetched, no `corpus/` write.
