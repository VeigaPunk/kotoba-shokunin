verdict: HOLDS — all six assigned OMP extractor mutations were killed; each detector was clean before mutation and after exact restoration.

## Scope and axes

Lane-authored mutation review of `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, not round admission or non-author closure. Production sources were read-only. Six independent canonical-layout scratch clones live under `/fast/scratch/kotoba-r47/w2/W2OmpMutants-2/{M1..M6}/kotoba-shokunin`; sibling fleet paths are symlinks, not write targets.

- **Freshness:** deletion, severe truncation, and renamed OMP helper calls must make the frozen-dump detector red.
- **Operability:** exercise the actual verifier CLI with bounded invocations, rather than helper-only assertions.
- **Calibration:** reject coordinated kind laundering, and ensure the shipped self-test detects both an obsolete allowlist and an over-broad callee matcher.

All 18 detector invocations completed within a 90-second per-command bound. The six cases ran concurrently within each pristine / mutant / restored batch. No subagents, runtime sessions, package installs, or upgrades were used. Existing Python: `3.14.8` (`/usr/bin/python`).

## Kill matrix

`P/M/R` means pristine / mutated / restored exit code. A kill requires a clean baseline, the named behavioral failure, and a clean rerun after exact restoration.

| Mutant | Smallest assigned defect / input change | Expected detector | Actual mutant output | P/M/R | Verdict |
|---|---|---|---|---|---|
| M1 | Delete the two whole frozen-dump lines containing `"gemini", "GEMINI.md"` (84 bytes) | `surfaces.literal_present` names `omp:gemini/GEMINI.md` | `FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: omp:gemini/GEMINI.md`; no call shape; 6 other checks PASS | 0/1/0 | killed |
| M2 | Keep the first 481,154 of 48,115,461 dump bytes: floor(1%) | Freshness red, not vacuous green | `FAIL surfaces.literal_present: 28 loader literal(s) not verifiable`; `FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted ... baseline declares 8`; blindness also names 5 surviving declared literals; 5 other checks PASS | 0/1/0 | killed |
| M3 | Replace every textual `Xl(`/`Fo(`/`lq(` occurrence with `Zq(`: 29/54/5 occurrences, 88 total, zero leftovers | Rename must still make freshness red | `FAIL surfaces.literal_present: 8 loader literal(s) not verifiable`; `FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted ... baseline declares 8`; blindness also names 33 literal-bearing declared entries; 5 other checks PASS | 0/1/0 | killed |
| M4 | Change only `omp:gemini/GEMINI.md` from `loader-group` to `doc` in both baseline and census | `surfaces.no_uncovered_class` detects kind laundering | `FAIL surfaces.no_uncovered_class: 1 extracted loader class(es) re-kinded in the baseline — kind reassignment is not a bypass: omp:gemini/GEMINI.md->doc`; 6 other checks PASS, including `kind_parity` | 0/1/0 | killed |
| M5 | Remove `|lq|Xl|Fo` only from the behavior-bearing `OMP_CALL_RE` alternatives | `--self-test` rejects the obsolete allowlist | Three failed assertions, all `18.12.5-callees`; `3 failure(s) over 99 assertions` | 0/1/0 | killed |
| M6 | Replace `OMP_CALL_RE`'s explicit callee alternatives with `[A-Za-z_$][A-Za-z0-9_$]*` | `--self-test` rejects arbitrary callees / aliases | Clean fixture reports undeclared `omp:evil/EVIL.md`; `7 failure(s) over 99 assertions` | 0/1/0 | killed |

No surviving counterexample or inconclusive baseline occurred in this assigned set. This does not establish whole-binary census completeness.

## Exact source anchors and findings

All repository path:line references in this section are at **7ad7fad**.

1. **Lost loader calls are independently detected.** `verifiers/verify_surfaces.py:156-160` defines `OMP_CALL_RE`; `:316-333` selects it for OMP and resolves variable-bound groups. `:563-585` checks both literal presence and extracted `(group,file)` membership. M1 deleted the only two quoted gemini/GEMINI registration lines in the frozen dump:

   ```text
   omp-18.12.5.strings:898856  const T = Xl(u, "gemini", "GEMINI.md");
   omp-18.12.5.strings:898867  const M = Fo(u, "gemini", "GEMINI.md");
   ```

   The literal still exists elsewhere: the actual failure is **missing call shape**, not absent spelling. `no_uncovered_class` remains PASS for the other 7 classes, while `literal_present` makes the combined command fail. This is the required targeted rejection, not an unrelated failure.

2. **Truncation and unknown helper names cannot turn extraction blindness green.** `verifiers/verify_surfaces.py:622-637` supplies the zero-extraction and literal-bearing blindness arms. M2 and M3 both hit them. M3 preserves dump byte length and literals, yet the detector rejects all eight formerly extracted loader classes. Its textual replacement also affects unrelated occurrences and printable noise; the recorded counts are textual occurrences, not a claim of 88 loader registrations.

3. **Baseline+census agreement cannot launder the extracted loader into `doc`.** The attacked row is `verifiers/surfaces-baseline.json:27-31` (`context_kind` at `:30`) and `corpus/knowledge/instruction-surface-census-round13.md:76`. The independent check at `verifiers/verify_surfaces.py:643-652` rejects `omp:gemini/GEMINI.md->doc` even while both parity columns agree and `literal_present` verifies the remaining 41 loader-kind entries. This is a targeted kill of the coordinated mutation, not merely disagreement between the two edited files.

4. **The new-generation regression test kills removing the newly pinned callees.** Only `verifiers/verify_surfaces.py:157` changed in M5; the diagnostic `CALLEE_SHAPES` text was deliberately left untouched. `:879-894` requires exit 0, a passing literal check, and all 8 extracted pairs from `verifiers/fixtures/surfaces/strings-omp-18.12.5.txt:1-14`. Actual failed assertion labels:

   ```text
   self-test FAIL: 18.12.5-callees: exit 0: got 1
   self-test FAIL: 18.12.5-callees: PASS literal_present
   self-test FAIL: 18.12.5-callees: PASS no_uncovered_class, all 8 pairs
   3 failure(s) over 99 assertions
   ```

5. **The self-test also kills callee widening.** M6 changes the same single regex line. `verifiers/fixtures/surfaces/strings-omp-clean.txt:10` carries `const xSomeId = Id; var decoy = xSomeId(e, "evil", "EVIL.md");`; the new-generation fixture also carries a short alias decoy at `strings-omp-18.12.5.txt:14`. The existing positive expectations at `verifiers/verify_surfaces.py:857-877,879-894` reject over-extraction. Actual failure labels: `clean: exit 0`, `clean: PASS surfaces.no_uncovered_class`, `new-callees: exit 0`, `new-callees: PASS no_uncovered_class`, `18.12.5-callees: exit 0`, `18.12.5-callees: PASS no_uncovered_class, all 8 pairs`, and `oc-extra: exit 0`. The first reported finding is undeclared `omp:evil/EVIL.md`; summary is `7 failure(s) over 99 assertions`.

## Commands executed and reproduction

For each case, working directory was:

```text
/fast/scratch/kotoba-r47/w2/W2OmpMutants-2/<M1|M2|M3|M4|M5|M6>/kotoba-shokunin
```

Setup used `git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin <case>/kotoba-shokunin`, then `git -C <case>/kotoba-shokunin checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f`; all six clone and checkout pairs exited **0**. All Git mutations were confined to those clones.

M1–M3 ran the following exact detector shape at every stage, with `<case>` substituted by the corresponding actual path:

```sh
/usr/bin/python verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/w2/W2OmpMutants-2/<case>/kotoba-shokunin/probe-omp.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
```

M4 ran at every stage:

```sh
/usr/bin/python verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
```

M5 and M6 each ran at every stage:

```sh
/usr/bin/python verifiers/verify_surfaces.py --self-test
```

The pristine and restored full runs each printed **7 PASS / 0 FAIL**, including 42 verified loader-kind entries, all 8 extracted OMP loader classes declared, opencode 9/9 classes from 7/7 rules, and 42 inventory ids. The pristine/restored self-tests each printed `0 failure(s) over 99 assertions`, exit **0**. Their stderr includes expected `NO-SUCH.txt`, `NO-SUCH.md`, and `NO-SUCH.json` errors from negative fixtures; these also appear in the mutated self-tests and are not baseline failures.

To reproduce the input mutations in a new isolated canonical clone, take `S` as the **bytes** of the frozen `omp-18.12.5.strings`. The exact generated-input formulas were:

```python
# import re; S is the frozen dump bytes
M1 = b"".join(line for line in S.splitlines(keepends=True)
              if not re.search(rb'"gemini"\s*,\s*"GEMINI\.md"', line))
M2 = S[:len(S) // 100]
M3 = re.sub(rb'(?:Xl|Fo|lq)\(', b'Zq(', S)
```

Write the selected result only to that clone's `probe-omp.strings`; use the corresponding detector above. M4 replaces `loader-group` with `doc` **only** in the two anchored gemini rows. M5 removes `|lq|Xl|Fo` from `OMP_CALL_RE` line 157 only. M6 replaces that regex line's noncapturing callee alternation with the generic JS-identifier pattern above. Each state was applied separately, never stacked.

M4–M6 tracked mutations and restorations were committed with path-limited `git -c user.name=W2OmpMutants-2 -c user.email=W2OmpMutants-2@shokunin.local -c core.hooksPath=/dev/null -c commit.gpgsign=false commit --only -m 'falsify <case> <mutated|restored>' -- <affected-paths>`; all six commits exited **0**. Scratch mutation→restoration commits: M4 `89f869c`→`d567448`; M5 `25e73bf`→`862122a`; M6 `38bd6ad`→`8b5395d`. M1–M3 were generated external-input fixtures, not committed source changes.

## Hashes and exact restoration

SHA-256 identifiers below denote the **full** hashes, not abbreviations:

- `H_OMP` = `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301`
- `H_OC` = `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`
- `H_VERIFIER` = `e44bf34b1a52c0e5e4cd320b8f90a20c10c0a997bc225e9b36bf90ccf173be4e`
- `H_BASELINE` = `6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b`
- `H_CENSUS` = `ed292ce27e4e97400a5d3371f1dfee597c9a46c5763a1bbd7a993e841a9c4a7b`

| Mutant / changed bytes | Pristine SHA-256 | Mutated SHA-256 | Restored SHA-256 |
|---|---|---|---|
| M1 OMP dump | `H_OMP` | `e72ab081200e2a97919fcd9acf1baa2a67e431a52345dd635d989b944693c262` | `H_OMP` |
| M2 OMP dump | `H_OMP` | `e90d587e779a1fad2d026c83d05bd56bffa92787a5c3c9927fdaf36dc2ba324e` | `H_OMP` |
| M3 OMP dump | `H_OMP` | `7b9ebdd47eeae00ae9eaf28435c27b0cad99a67a18077fe6a5294bfa50202cd8` | `H_OMP` |
| M4 baseline | `H_BASELINE` | `3ae58e6bfe5be8c22d7b864deb6b9901adee91682149dd54e53e8547e47b72b8` | `H_BASELINE` |
| M4 census | `H_CENSUS` | `712982e31e6c0ddfb16f68c9aeccfc8a0f20595964b84032e5a47c86213b088c` | `H_CENSUS` |
| M5 verifier | `H_VERIFIER` | `fd44714368e04fabdde42852ae1e3728623cc60c3fc6b128eebacb531e82b387` | `H_VERIFIER` |
| M6 verifier | `H_VERIFIER` | `27320e0f9547b5b5f148c08606e890e02e4c71e07f5f7be89b241f8fd1e96bfd` | `H_VERIFIER` |

After restoring, direct byte comparisons confirmed every changed input/source exactly equals its pristine bytes; all per-stage watched hashes also match pristine→restored. The three scratch dumps are each back to 48,115,461 bytes. All three tracked targets (verifier, baseline, census) were compared to their original bytes in every case; all comparisons were true. The shared OMP/opencode dump hashes remained `H_OMP`/`H_OC` before and after; neither shared dump was mutated. Scratch dump permissions were returned to the frozen source's mode with `chmod --reference=...` (exit 0).

Full, untruncated stdout/stderr, exact argv/cwd, timeout bounds, timings, mutation counts, before/mutated/restored hashes, commit command outputs, and restoration booleans are retained in **`W2OmpMutants.results.json`** beside this report. No strings dump or binary was copied into production.

## Not checked

- Default binary resolution, installed-binary authentication, or live runtime loader behavior. This probe deliberately used the supplied frozen dumps; it does not re-establish the entire C1 substrate-pin claim.
- C2's XML/frontmatter checklist rule, C3's governance erratum / corpus gates / fault harness, registry source-row quotations, or the complete round-47 ledger and learning verdicts.
- Independent opencode-rule removal mutants, arbitrary future loader shapes, or freshness guarantees beyond the six assigned mutations.
- No integration, shipping, round judgment, SHONEN marks, builds, formatters, or unrelated checks.

Tooling note: one initial scratch fixture write hit EACCES because copying a frozen dump preserved its read-only mode. Only scratch copies were made writable and the write retried before any mutated detector ran. No partial-input detector result was counted. Two tool-I/O inconsistencies (missing read edit anchors on the large dump; `xd://eval/helpers` range handling) were reported through `xd://report_issue`; they did not affect any detector output.
