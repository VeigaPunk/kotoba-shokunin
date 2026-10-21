verdict: HOLDS — GOVERNANCE_ERRATA rejects four in-place laundering arms; --self-test kills all three guard-deletion mutants at 7ad7fad.

# W2ErrataLaunder — bounded mutation probe

Author: `KotobaR47-2.W2ErrataLaunder-2`. Revision: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.

**Axes:** freshness (execute the pinned landed bytes), operability (the bounded governance CLI rejects each laundering shape), calibration (the committed self-test detects removal of each erratum guard). This is lane-authored evidence about the assigned C3 seam, not round admission, non-author closure, or a verdict on all C1/C2/C3 work.

## Findings and source locations at 7ad7fad

- `verifiers/verify_skill_checklist.py:373–383` defines a reviewed in-source exception, horizon **2315**, for `LOG.md:2111`, token `.ufo/round-45/drafts/v10/post-r44-hunt.py`, exact line digest, and absence wording. The observed line digest without its newline was `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135`, matching the row.
- `verifiers/verify_skill_checklist.py:1474–1491` normally drops de-rooted, same-line quoted, and schematic tokens. The four planted historical edits still failed: `errata_problems` independently inspects its registered line, and `check_governance_citations` incorporates its problems even if extraction omitted the token (`:1519–1542`, `:1570–1594`). Quote/schematic exclusion counts changed as intended, so those probes exercised the laundering forms rather than merely renaming a live subject.
- `verifiers/verify_skill_checklist.py:1528–1530` enforces horizon/file length; `:1532–1533` enforces the line digest; `:1538–1539` rejects an erratum whose target now resolves. The self-test's relevant obligations are at `:2192–2226`, specifically horizon/line drift at `:2210–2220` and restored-path staleness at `:2221–2226`. Removing each corresponding guard produced exactly one named assertion failure, not a syntax error, traceback, or baseline failure.

## Isolation and commands actually run

Base clone: `/fast/scratch/kotoba-r47/w2/W2ErrataLaunder-2/kotoba-shokunin`. The contract's sibling-link/`git clone -q --no-hardlinks` setup and detached checkout of the full revision both completed in the setup command, exit **0**. Seven detached worktrees, each named `kotoba-shokunin` inside its own canonical fleet-layout parent, were then created from this isolated clone. The sibling-link command and each `git -C <base-scratch> worktree add --detach <arm-parent>/kotoba-shokunin 7ad7fadfc09354b74fb66605dfb0c1182c115a2f` command exited **0**. Exact expanded arguments/stdout/stderr are preserved in the JSON evidence.

For every row below, cwd was `/fast/scratch/kotoba-r47/w2/W2ErrataLaunder-2/<arm>/kotoba-shokunin`; detectors ran concurrently only against disjoint worktrees. `PYTHONDONTWRITEBYTECODE=1` was set, and every subprocess had a 120-second bound.

**G — governance detector:**

```sh
PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_skill_checklist.py --check governance.citation_resolves --json
```

**S — self-test detector:**

```sh
PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_skill_checklist.py --self-test
```

Each detector was run on **pristine → mutated → exact-restored bytes** in every worktree: 21 matrix executions. Two preliminary controls in the base clone also ran G and S, both exit **0**. Pristine/restored G reported **PASS, evaluated 848**, 9 quoted and 3 schematic exclusions, **1 recorded absence excused**. Pristine/restored S reported `0 failure(s) over 1845 assertions`. All captured stderr streams were empty; no timeouts occurred. Python reported version **3.14.8**. No tools were installed or updated.

## Kill matrix

| Arm | Original location | Detector | Pristine rc | Mutant rc | Restored rc | Mutant output / distinguishing signal | Verdict |
|---|---|---|---:|---:|---:|---|---|
| `de_root` | `LOG.md:2111` | G | 0 | 1 | 0 | line text drifted | **KILLED** |
| `quote_wrap` | `LOG.md:2111` | G | 0 | 1 | 0 | line text drifted; quoted exclusions 9→10 | **KILLED** |
| `ellipsis` | `LOG.md:2111` | G | 0 | 1 | 0 | line text drifted; schematic exclusions 3→4 | **KILLED** |
| `line_shift` | `LOG.md:2108 (subject 2111→2112)` | G | 0 | 1 | 0 | line text drifted; unresolved subject named at LOG.md:2112 | **KILLED** |
| `drop_sha` | `verifiers/verify_skill_checklist.py:1532–1534` | S | 0 | 1 | 0 | self-test FAIL: governance: erratum line drift fails closed | **KILLED** |
| `drop_still_dead` | `verifiers/verify_skill_checklist.py:1538–1539` | S | 0 | 1 | 0 | self-test FAIL: governance: erratum for a restored path is stale | **KILLED** |
| `drop_horizon` | `verifiers/verify_skill_checklist.py:1528` | S | 0 | 1 | 0 | self-test FAIL: governance: erratum past horizon fails closed | **KILLED** |

**Result: 7 killed, 0 survived, 0 inconclusive** (four laundering mutations and three gate-code mutations). Every baseline and restored detector passed. No red baseline was counted as a kill.

### Rejected counterexamples / exact mutations

1. **de_root:** at `LOG.md:2111`, change only `.ufo/round-45/drafts/v10/post-r44-hunt.py` → `round-45/drafts/v10/post-r44-hunt.py` inside the replay command.
2. **quote_wrap:** at `LOG.md:2111`, wrap the whole inline-backtick replay command in ASCII double quotes: from `` `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` `` to `` "`python3 .ufo/round-45/drafts/v10/post-r44-hunt.py`" ``.
3. **ellipsis:** at `LOG.md:2111`, change the `drafts` segment to Unicode `…`, retaining `.ufo/round-45/…/v10/post-r44-hunt.py`.
4. **line_shift:** insert one blank line before original `LOG.md:2108`. The registered historical line moves from 2111 to 2112. The detector reports both the erratum's line drift and the now-unexcused unresolved token at `LOG.md:2112` (evaluated **849**).
5. **drop_sha:** delete original `verifiers/verify_skill_checklist.py:1532–1533` and turn the following `elif quote not in text:` into `if quote not in text:`. No fixture or expected assertion is changed.
6. **drop_still_dead:** delete only original `verifiers/verify_skill_checklist.py:1538–1539`, allowing a restored target to be excused.
7. **drop_horizon:** at original `verifiers/verify_skill_checklist.py:1528`, replace `min(horizon, len(log_lines))` with `len(log_lines)`. This deliberately preserves array bounds; the failure is specifically loss of the policy horizon.

The first three G mutants each report `erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py': line text drifted`, **FAIL**, evaluated **848**, zero recorded absences excused. They do not silently turn the erratum into an excluded token.

### drop_sha

```text
self-test FAIL: governance: erratum line drift fails closed: got ('PASS', 1, '1 governance citation token(s) resolve across 2 files; 0 quoted meta-finding(s), 1 schematic token(s) excluded, 1 recorded absence(s) excused')
1 failure(s) over 1845 assertions
```

### drop_still_dead

```text
self-test FAIL: governance: erratum for a restored path is stale: got ('PASS', 1, '1 governance citation token(s) resolve across 2 files; 0 quoted meta-finding(s), 1 schematic token(s) excluded, 1 recorded absence(s) excused')
1 failure(s) over 1845 assertions
```

### drop_horizon

```text
self-test FAIL: governance: erratum past horizon fails closed: got ('PASS', 1, '1 governance citation token(s) resolve across 2 files; 0 quoted meta-finding(s), 1 schematic token(s) excluded, 1 recorded absence(s) excused')
1 failure(s) over 1845 assertions
```

These S outputs expose each defective checker returning `PASS` for its bad fixture; the self-test correctly rejects that behavior. They are killed mutants, not surviving production counterexamples.

## Restoration evidence

Every mutated target was restored using the inverse surgical edit **before this report**. Direct byte comparisons against the saved pristine bytes were true for all seven targets. Both `LOG.md` and the verifier hash matched their pristine values in every worktree after restoration. The identical detector was then rerun and returned exit 0 for each row.

Full original **and restored** SHA-256 values:

- `LOG.md`: `ef1a753c39cbfb06f1d421c9dafb29ac2481ae5f9d1367a2ef7a83c0a4e1f04e`
- `verifiers/verify_skill_checklist.py`: `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a`

| Arm | Mutated target SHA-256 | Restored state |
|---|---|---|
| `de_root` | `f1ec54a4dfce8b314e0fed63e4fe1b12415478ddfdd07ccc693b65deff5894d9` | exact original bytes; original hash below |
| `quote_wrap` | `8ad9091bd01c773f8f1e011375708dd99ac915ebe0867f36795286f2ef7a85b7` | exact original bytes; original hash below |
| `ellipsis` | `9d4fa36288c2bb290999bf0d12b0c511175939144b0d5e066df80cf886f91a26` | exact original bytes; original hash below |
| `line_shift` | `06694b6098aca49cde722c7f1e6e6b7a51968cdef2033acb41e03e80ff208aa3` | exact original bytes; original hash below |
| `drop_sha` | `55b15667ecc91e1b2ca1ea6d7166f9a8967b9a2cf7de77d281ba8c9213247c9a` | exact original bytes; original hash below |
| `drop_still_dead` | `d73534840a8a7ff6fdcac1d617c3cca709d0dfddde98b8e709b98aabc792015b` | exact original bytes; original hash below |
| `drop_horizon` | `a8fbb4021d5d1ee0a955189243e3fb312d361ac3f65cc82d7a373115ad331ff4` | exact original bytes; original hash below |

No production source, `LOG.md`, historical receipt, sibling source, fleet state, Git index/ref, or jj state was changed by this probe. Mutations were uncommitted scratch worktree edits; these two detectors read working bytes, so no corpus/fault-harness committed-state assertion is being made.

## Evidence and replay

`W2ErrataLaunder.results.json` preserves complete argv/cwd, actual stdout/stderr, exit codes, timings, patches, mutation hashes, and byte-restoration comparisons for every stage. Size: 42448 bytes; SHA-256 `d2d21d2712f5dccddc11739dd4da9f43aaf1b524273084cd08060e5ffe577ff6`. Every artifact is below the 1 MiB limit.

| Replay patch | Bytes | SHA-256 |
|---|---:|---|
| `W2ErrataLaunder.de_root.patch` | 2958 | `5316cb700d99cffe7f5945f67f793884fd69042a8b64da9de7a92ffb5dc9d47a` |
| `W2ErrataLaunder.quote_wrap.patch` | 2965 | `4808008f5899cdc0c552f0a13f8cbf1f95d436eb09ff68648401fe93ae92f5bf` |
| `W2ErrataLaunder.ellipsis.patch` | 2960 | `480cb357b94ddd3a436727f342a24deb3a380450ed57bd3752a44a2dffd25222` |
| `W2ErrataLaunder.line_shift.patch` | 1195 | `67f4014dc1b45f5b8c1591c54f96fb25a0b6a28bf2d596857f93cd1b6645578c` |
| `W2ErrataLaunder.drop_sha.patch` | 481 | `7652d7d74aab677935e1beaac58e2f38ff814733a3051a015911b9f312c335c3` |
| `W2ErrataLaunder.drop_still_dead.patch` | 395 | `8ebfc62a19b3b9133f22d51d605625b3dbd07fe7364ed9ee65ad769d96f26019` |
| `W2ErrataLaunder.drop_horizon.patch` | 418 | `28e804ad7a096cb46b0a98fc346facc956bd1ee56156fe2267ce0b777764be01` |

Replay instructions (not an additional executed battery): in the restored `<arm>` scratch worktree at the pinned revision, run the matching G/S command above (expect 0); apply only that arm's patch with `git -C "$S" apply "$E/W2ErrataLaunder.<arm>.patch"`; rerun the identical command (expect 1 and the named output above); reverse the same patch with `git -C "$S" apply --reverse "$E/W2ErrataLaunder.<arm>.patch"`; rerun (expect 0). Here `$S` is that scratch worktree, never the production checkout; `$E` is `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify`. Applied mutations in this probe used the hashline edit tool, not these replay commands.

## Not checked

- No broader C1 substrate re-derivation/pin battery, XML-trigger C2 review, source-registry reopening, corpus gate, fault-injection harness, or floor guard was run.
- No general append-only invariant, arbitrary unregistered line, alternate errata row, real historical runner restoration, or horizon modification beyond the specified guard-deletion mutant was tested. Restored-path behavior here is exercised by the committed self-test's `corpus/gone.md` fixture, not by creating the real `.ufo/round-45/...` path.
- The recorded after-battery value 804 was not investigated or reasserted; the actual delivered-revision bounded G count in this probe was 848.
- No production omp/opencode session, opencode wrapper, new runtime, host-private surface, or subagent was invoked. No blanket completeness, authentication, or whole-round closure claim follows from seven successful kills.
