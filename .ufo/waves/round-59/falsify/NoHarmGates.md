Result: MIXED — the after-column is exit-for-exit identical to the before-column (all 33 registered gates exit 0 on `--self-test` at `c63ccc68`, and the five real predicates the before-column measured keep their exits), but the landing is not finding-neutral: it adds one instance to an already-red gate's `commit_unresolvable` set (1 → 2) via `corpus/lessons/round-59.md:45`.

# Round-59 FALSIFY — no-harm after-column at the claim tip

Seat `KotobaR59.NoHarmGates` (leaf). Item: re-run every registered gate's `--self-test` at
`c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, write the receipt in the base receipt's format, diff the
exit columns; plus the real-predicate after half of the same column where the before half exists.

**What this attacks.** The no-harm claim implied by the before-column: that landing round 59 leaves
the lane's gate battery in exactly the state it was at base — no gate that was green turns red, and no
red gate gains a reason attributable to the round. Two halves are attacked separately because they
answer different questions: the *self-test* column (is any instrument self-broken after the landing?)
and the *finding* column (did the landing put new material in front of an instrument?).

## Sandbox and provenance

- clone `/fast/scratch/hyaku/kotoba-r59/NoHarmGates/world/kotoba-shokunin`, `git rev-parse HEAD` =
  `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`; checkout dir named `kotoba-shokunin`, 58 fleet-root
  top-level entries (all but the lane, `.git`, `.jj`) symlinked read-only into `world/` — same shape
  as `build/ExecNoHarmBase.md` § Method.
- registry read from `SKILL.md` **at the rev under test**, § Gate registry lines 458-490, 33 rows;
  gate list machine-extracted (`grep -oP '^\| `\Kverifiers/[A-Za-z0-9_.]+\.(py|sh)' SKILL.md` → 33),
  asked list and registry list verified equal (`diff` → identical).
- runner `run_selftests.sh` sha256 `6d071a66f8a0a8a962081ccba3fa71898cf3c8e4f5385b42d411781eed52ca0d`;
  `<gate> --self-test` from the checkout root, `timeout 600` each, gate pairs only (≤ 2 concurrent).
- `date -u`: 09:53:01Z first gate, 09:55:20Z last result, 139 s wall; 33 logs, 30715 bytes.
- receipt `.ufo/waves/round-59/receipts/noharm-tip-selftests.txt` (per-gate exit, seconds, final
  line, provenance, before/after exit table) — same row/column layout as
  `receipts/noharm-base-selftests.txt`.

## Half 1 — self-test column: HOLDS

`timeout 900 bash run_selftests.sh world/kotoba-shokunin logs-tip $(cat gates-tip.txt)` → runner
exit 0. `awk -F'\t' '{print $2}' logs-tip/*.res | sort | uniq -c` → `33 0`. No exit 124, no nonzero.

Compared with the before-column (`receipts/noharm-base-selftests.txt`, base `a975cbbf`):

| attack | result |
|---|---|
| a gate green at base turns red at tip | none — 33/33 exit 0 |
| an existing gate's output moved | none — final-line column is byte-identical for 32 of 33 rows (`diff base-final.tsv tip-final.tsv` → exactly one differing row) |
| the round's own new gate is self-broken | no — `check_hook_files.py --self-test` exit 0, `self-test: 0 failure(s) over 323 assertions`, and it prints `counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`, byte-identical to the sha256 the claim's counter command cites |
| registry drift (rows vs files) | `python3 -B verifiers/check_gate_registry.py --rev c63ccc68…` → exit 0, `gate registry rows conformant 33 of 33 lane verifiers; phantom 0` |

The one differing final line is the hook counter row itself: base `python3: can't open file … [Errno
2] No such file or directory` (the script does not exist at the base rev) → tip `self-test: 0
failure(s) over 323 assertions`. Timing moved (check_agentdef_boxes 13 s → 36 s,
verify_harness_independent 65 s → 82 s, column 89 s → 139 s); exits did not.

## Half 2 — real predicates where a before-column exists: exits HOLD, findings MOVE

The before-column for real predicates is `receipts/base-r59-a975cbbf.txt` (five commands). Re-run
verbatim at the tip, same sandbox, `timeout 300` each:

| command | base exit | tip exit | tip observation |
|---|---|---|---|
| `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | 0 | 11 PASS, 0 fail; `trigger.line_budget` **587 lines within budget 600** (base 596); citation tokens 137 → 141; command subjects 34 → 34 |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | 1 | 5 of 9 checks PASS (base 4 of 9); see the delta below |
| `python3 -B verifiers/check_gate_registry.py --rev c63ccc68…` | 0 (32 of 32) | 0 (33 of 33) | as quoted above |
| `python3 -B verifiers/check_assertion_floors.py` | 0 | 0 | the same 14 `PASS … observed=/floor=` lines, values unchanged |
| `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0 | `correction sweep: 0 stale block(s)` |

So the exit column of the real-predicate half is also unchanged. The finding population is not.

## The one delta (this is the falsification result)

`verify_corpus_integrity.py --json` at the tip, exit 1:

```
"commit_unresolvable": 2,
"commit_unresolvable_detail": [
  "corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff",
  "corpus/lessons/round-59.md:45: b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b"
]
```

The before-column has `commit_unresolvable: 1` (the round-54 instance only). The second instance is
created by this round's own lesson. The lesson text at that line (byte-exact from
`corpus/lessons/round-59.md:45` in the sandbox) is:

> sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`

- the hash does not resolve in the lane: `git --no-optional-locks cat-file -t b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` → `fatal: git cat-file: could not get object info`, **exit 128** (same for the older `451a02ff`, exit 128);
- the gate's rule is `commit `<token>`` where the token is 7-40 hex and `git cat-file -e <hex>^{commit}` fails (`verifiers/verify_corpus_integrity.py:25-28`); its only commit-side exclusion is the double-quoted meta-finding idiom (`…:57-61`);
- **shortening the hash is not a fix**: the pre-existing flagged token `451a02ff` is 8 hex and still flagged, so the 7-40-hex rule catches any prefix.

Two honest readings, stated so the L1 can rule:

1. **Content is correct, gate class is too coarse.** Writing `sandbox commit <40-hex>` is what the
   round-59 bounds themselves require of sandbox hashes, and a sandbox commit can never resolve in
   the lane. The durable correction is gate-side: classify a token preceded by `sandbox commit` (or
   whose line names a `/fast/scratch/…` path) into a context class beside `quoted meta-finding` —
   a gate change, so it needs its own before/after control in a later round, not a quiet edit here.
2. **Landing is a conformance defect.** Until that class exists, a red gate that gains a
   round-caused instance is exactly what PROTOCOL.md § Gate standard (“Closure consequence”) tells
   the integrator to record and route, status-neutral. Recommended immediate step: note the
   `commit_unresolvable 1 → 2` delta in the round notes with this receipt and the gate line, and do
   not rewrite the lesson's provenance to buy a greener counter (dropping the word `commit` or
   double-quoting the hash would move the token into `commit_quoted_detail`, i.e. hide a true
   citation from the check that exists to catch dead ones).

Other measured moves in the same gate, for the ledger: `tracked_files` 94 → 96 (expected 81),
`unindexed` 1 → 0 (cleared: the round-58 spot-check lesson is now indexed), `report_total` 64 → 64
(expected 51), `commit_total` 33 → 34 (expected 32), `stale_patterns` 0, `missing_paths` 0,
`report_dead` 0, `commit_nonhash` 0 — all unchanged at their before values.

## Why the self-test half is capability, not measurement

`git --no-optional-locks diff --name-status a975cbbf… c63ccc68… -- verifiers/` → `A
verifiers/check_hook_files.py` and nothing else: the other 32 instruments are byte-identical to the
base rev. Their self-tests build their fixtures in `$TMPDIR`, so the identical columns are the
structurally expected result, not independent evidence about the round's content. PROTOCOL.md § Gate
standard says the same in words: “Self-test green is capability, not a measurement.” That is why
half 2 exists in this report and why the one delta — a real predicate reading real landed content —
is the finding, while 33/33 green is the baseline rather than the result.

## Unrun / boundaries of this column

- The five `--fetch` gates (`check_agent_definitions`, `check_command_files`,
  `check_explicit_invocation`, `check_hook_files`, `check_plugin_manifests`) were **not** run in
  their `--rev … --fetch` form: this item asks for `--self-test`, and a live-network lane gate run is
  the L1's data step, not a falsify seat's. Their self-tests are green (above); their predicates over
  the round's content are untested here.
- 28 further gates have no before-column in `receipts/base-r59-a975cbbf.txt`, so no after value
  could be diffed for them; their self-tests are the only comparable measurement and they are green.
- The claim's own C1 counter (`check_hook_files.py --rev … --fetch`, 6 of 6) was not re-run here;
  the self-test proves the instrument's logic, not the hook-file evidence. Nothing here is evidence
  for or against the 6-of-6 receipt.

## Operability notes / risks

- No residue: `git status --porcelain` in the sandbox after both halves → 0 lines; all temp trees
  went to `$TMPDIR`. No lane file was edited; no git or jj write ran in the lane; nothing was written
  outside this report and the named receipt.
- Tool installs: none. No package manager ran, no network fetch, no paid model call.
- [INFERENCE] `verifiers/floors-registry.json` at the tip has no row for the hook counter
  (`instrument_total: 14`; `grep hook` → no match), and `check_assertion_floors.py` exits 0 — so a
  323-assertion gate now has no assertion floor. PROTOCOL.md § Gate standard's Registry clause does
  not require a floor row, so this is an observation for the L1, not a defect under the standard;
  the next round may want a floor so the hook counter's assertion count cannot silently shrink.
- The 600 s cap was never approached (longest gate 82 s); load moved seconds, never exits.

## Deliverables

- `.ufo/waves/round-59/receipts/noharm-tip-selftests.txt` — the after-column receipt.
- `.ufo/waves/round-59/falsify/NoHarmGates.md` — this report.

`ls -l` of both (printed 2026-10-23T10:01:42Z, immediately before this block was inserted — the
report's own size in the listing therefore predates this block by the block's length; the receipt was
final when listed):

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/falsify/NoHarmGates.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/receipts/noharm-tip-selftests.txt
-rw-r--r-- 1 vgpnk vgpnk 11820 Oct 23 07:01 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/falsify/NoHarmGates.md
-rw-r--r-- 1 vgpnk vgpnk 14926 Oct 23 07:01 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/receipts/noharm-tip-selftests.txt
```

(Local file times; the host clock reads UTC-3 against the `date -u` stamps above.)

## Scope note on the lane worktree at report time

Every measurement here is against the **committed** rev `c63ccc68` (clean clone). The lane worktree
meanwhile carries four uncommitted modifications from other seats — `git --no-optional-locks diff
--stat` → `SKILL.md | 10 +-`, `corpus/README.md | 2 +-`,
`corpus/knowledge/hook-files-round59.md | 32 +++++-----`, `corpus/lessons/round-59.md | 31 ++++++`.
Not mine, not judged here, and they do not enter any number above. The one finding does survive them
at report time: `grep -n b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b corpus/lessons/round-59.md` in the
worktree → hit at line 45, exit 0. The L1 re-runs this column against whatever rev it finally lands.
