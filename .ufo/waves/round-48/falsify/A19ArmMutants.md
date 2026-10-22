# A19 ArmMutants — C2 self-test arm mutation probe

Verdict: **SURVIVOR FOUND (coverage finding)** — the 115-assertion self-test
kills 5 of the 6 assigned configured-root mutants; one reading of "list
instead of set" survives (M4b). Secondary finding: the evidence assertion
cannot discriminate removal of the singular root ("skill" substring of
"skills").

Target: `verifiers/verify_harness_independent.py`, configured-root enumeration
(lines 596-615), C2 commit `d1ae45830235c38320b31032b57a8323cbf90b17`, run in
private clone `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A19ArmMutants/clone`
(`git clone -q` lane; checkout `d1ae458…`, clean). Lane never modified; no
installs performed (system python3 3.14.8).

## Baseline (pristine)
`python3 -B verifiers/verify_harness_independent.py --self-test` → exit 0,
`0 failure(s) over 115 assertions`. Before hash
`d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`.

## Protocol
Per mutant: replace marker lines in the scratch copy, run the same command,
record exit + FAIL labels + hash, restore exact original bytes; hash verified
equal to baseline after every run. Mutant source hashes below.

## Results
| # | Mutation (behavior-bearing point) | Kill verdict | Exit | Asserts failed |
|---|---|---|---|---|
| M1 | Drop singular root: `configured = {str(s.oc_config / d) for d in ("skills",)}` | KILLED | 1 | 6 |
| M2 | Drop plural root: `configured = {str(s.oc_config / d) for d in ("skill",)}` | KILLED | 1 | 5 |
| M3 | Recursive rglob: `for entry in sorted(path.rglob("*")):` | KILLED | 1 | 6 |
| M4a | List instead of set (name collection): `names = [...]` + `names.append` | KILLED | 1 | 6 |
| M4b | List instead of set (root union): `for directory in sorted(list(sources) + list(configured)):` | **SURVIVED** | 0 | 0 |
| M5 | Count any child dir: `if entry.is_dir():` (drop SKILL.md test) | KILLED | 1 | 7 |
| M6 | Drop union with log roots: `for directory in sorted(configured):` | KILLED | 1 | 1 |
| M1-full | Extra probe: drop singular root from `root_dirs` AND `configured` | KILLED | 1 | 6 |

Kill labels (M1/M3/M6 representative):
- M1: `round 48: the configured roots are enumerated: got 4 want 5`; `…a
  root named by the log and by the configuration is one root: got 4 want 5`;
  also `…a root the log names is still enumerated: got 5 want 6`.
- M2: same set minus `a root the log names is still enumerated` (union kept).
- M3: `…a nested skill is not a name (direct children only): got 2 want 0`;
  `…the configured roots are enumerated: got 7 want 5`.
- M4a: `…without the same-name pair the count drops by one: got 2 want 1`;
  `…the configured roots are enumerated: got 6 want 5`.
- M5: `…a directory without SKILL.md and a plain file are not names: got 6
  want 4`; `…the configured roots are enumerated: got 7 want 5`.
- M6: `…a root the log names is still enumerated: got 5 want 6` (sole failure).

Mutant hashes: M1 `76d65b32fa84628c81a9321fef3cb241cd45ef48acd9d4e6bb1b196898add371`,
M2 `26d20668709cccf1ae334410398292bd43f634f8ce35184a268780712eb517b3`,
M3 `ea518cd70dac066d1cab50287319af88db28af9b75a17c3968db564d2f5172fa`,
M4a `4f1d2b6ee7c399d90071623fb42a8dc3f8d7eea8342a435b0f9cb20929d48833`,
M4b `8d0ab89414e087cb9e6be59b38ea249f53d3222fb0a715d1c26038a531640796`,
M5 `4db454546dcb177c055c6c0072534d82b94ee4cd24228044115fe04fbc4ed8c2`,
M6 `85c68a34cee926115a3612d147b1f5be37ac6f7391d20bfe8d194c4df54b9b62`,
M1-full `735659ea3ca10d7a60563d0fd2b88a9eef55bae39c967abff4dbcda710337297`.

## Survivor analysis (M4b)
`sorted(list(sources) + list(configured))` — a directory named by the log
*and* by the configuration is iterated twice and its direct-child names are
added twice; because `names` remains a set, the observable count never moves.
The arm's set-semantics assertions (`…and by the configuration is one root`,
`…the same-name pair`), all pass. Expected detector for this mutant: a probe
that counts enumerated root visits (e.g. a counter keyed by directory), not
the name-count. The contract comment ("Names are a set … never adds twice")
states the dedup the arm measures; it does not measure the union's setness.

## Secondary finding (weak discriminator)
The evidence assertion `round 48: the row's evidence names the configured
roots` checks `("skill" in evidence, "skills" in evidence)`. Because `"skill"`
is a substring of `"skills"`, M1-full (singular root removed from the row text
entirely) still passes it — the assertion cannot detect a fully removed
singular root (kills come only from the numeric assertions).

## Restoration evidence
After every mutant run the file was restored and its sha256 re-verified;
final hash equals baseline `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`.
Clone checkout still `d1ae458…`, `git status` clean; lane untouched.
