Result: HOLDS — the two new registry rows match their scripts at f0e6b69 on every cell; both --self-tests exit 0 and a nonexistent --rev exits 2 from each counter; one wording imprecision (nit) on the C2 write-scope cell.

# Scope

SKILL.md § Gate registry lines 457 and 459 (tip f0e6b695b746775823b65a8c45de7d50ea33e84f):
- `verifiers/check_could_not_evaluate.py` row (the C2 counter)
- `verifiers/check_explicit_invocation.py` row (the C1 counter)

Cells checked against script behavior: Name, Kind, Entry command, Verdict map,
Self-test, Pinned values, Write scope, Owner. All work read-only in the lane;
runs executed in sandbox clone /fast/scratch/hyaku/kotoba-r55/ReviewRegistryRows55
at f0e6b695 (date -u at clone: Fri 23 Oct 2026 12:10:04 AM UTC).

# Cell-by-cell consistency

## check_could_not_evaluate.py (SKILL.md:457)

| Cell | Registry | Script evidence | Match |
|---|---|---|---|
| Entry command | `python3 -B verifiers/check_could_not_evaluate.py --rev <rev>` | docstring usage line 46 identical; argparse `--rev` required (verifiers/check_could_not_evaluate.py:211, 219-220); `--json` optional, not in the cell, consistent with sibling rows | yes |
| Verdict map | 0=clean, 1=failed, 2=could-not-evaluate | line 238: `return 0 if honoured == N_PROBES and held == N_GATES else 1`; EnvError/OSError → 2 (lines 221-225); docstring lines 40-43 | yes |
| Self-test | `--self-test` | argparse flag line 213, mutex with --rev/--json (216-218); observed exit 0 | yes |
| Pinned values | in-file | GATES table, REV_TOKEN, RAND_TOKEN, N_PROBES, N_GATES all literal (lines 66-84); docstring lines 13-16 | yes |
| Write scope | temporary clone (removed) | `tempfile.TemporaryDirectory(prefix="kotoba-r55-cne-")` at line 145; clone inside `td/lane` (146-152), auto-removed | yes, with nit below |
| Kind / Owner | gate / kotoba | counter for the lane's C2 claim | yes |

Nit (non-blocking): the same temporary directory also holds `nogit-bin/`, a
sibling of the clone containing a `python3` symlink to `sys.executable`
(lines 157-159) used as the whole PATH for class-G probes. "temporary clone
(removed)" understates the write scope slightly; both objects sit inside one
removed `TemporaryDirectory`, so the cell is materially correct. Registry-row
precision only; no behavioral defect.

## check_explicit_invocation.py (SKILL.md:459)

| Cell | Registry | Script evidence | Match |
|---|---|---|---|
| Entry command | `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch` | docstring usage lines 71-73; argparse mutually-exclusive `--rev`/`--root` plus `--fetch`, `--json` (lines 582-587). `--fetch` is correctly pinned in the cell because the frozen C1 predicate is the --fetch form (docstring lines 64-68); unlike the other fetch-capable rows (`check_description_thresholds.py`, `check_mcp_instructions.py`, `check_overlap_levers.py`) whose predicates are not the fetch form | yes |
| Verdict map | 0=clean, 1=failed, 2=could-not-evaluate | line 643: `0 if value >= TARGET and ground >= NEW_TARGET else 1`; EnvError/UnicodeDecodeError/OSError → 2 (lines 595-604); docstring lines 63-68 | yes |
| Self-test | `--self-test` | flag line 587, mutex with all other flags (lines 589-592); observed exit 0, 44 assertions | yes |
| Pinned values | in-file | BASE, CLIENTS, HOSTS, BUILTINS, TOKEN_RE, OPENED, TARGET, NEW_TARGET, MAX_WORDS all literal (lines 111-158); no external data file | yes |
| Write scope | none; `--fetch` reads the network | only network operation is `urllib.request.urlopen` GET in `fetch()` (lines 357-360); all git operations are reads (`rev-parse --verify`, `git show`, `git ls-tree` lines 165-199); no filesystem writes found | yes |
| Kind / Owner | gate / kotoba | counter for the lane's C1 claim | yes |

# Probe runs (sandbox clone at tip; exit codes observed)

- `python3 -B verifiers/check_could_not_evaluate.py --self-test` →
  `self-test: 0 failure(s) over 12 assertions`, exit 0.
- `python3 -B verifiers/check_could_not_evaluate.py --rev deadbeef…(40 hex)` →
  `could-not-evaluate: revision 'deadbeef…' is not a commit …`, exit 2.
- `env PATH=/tmp/nogit-r55 python3 -B verifiers/check_could_not_evaluate.py --rev f0e6b695…` →
  `could-not-evaluate: git not runnable: [Errno 2] No such file or directory: 'git'`, exit 2.
- `python3 -B verifiers/check_explicit_invocation.py --self-test` →
  `self-test: 0 failure(s) over 44 assertions`, exit 0.
- `python3 -B verifiers/check_explicit_invocation.py --rev deadbeef…` → exit 2
  (same EnvError), and with `--fetch` appended → exit 2; the rev is verified
  before any network access (read_file → verify_rev, lines 202-205, 596).
- `env PATH=/tmp/nogit-r55 python3 -B verifiers/check_explicit_invocation.py --rev f0e6b695…` →
  exit 2, same "git not runnable" EnvError. So both counters honour their own
  declared `2=could-not-evaluate` under the exact two classes the C2 counter
  probes (unknown rev, git absent) — consistent with their own registry rows.

# Cross-checks

- `verifiers/check_gate_registry.py --rev f0e6b695…` in the sandbox →
  `gate registry rows conformant 26 of 26 lane verifiers; phantom 0`, exit 0;
  both new rows listed OK.
- Freeze check: `git log` shows check_could_not_evaluate.py untouched since the
  plan commit a10240c; check_explicit_invocation.py changed once, at b04a900
  ("erratum 1 — C1 counter v2"), the authorized pre-data fix. No seat edited a
  counter after content.
- Row provenance: the two rows were added verbatim in ed3e899 (routed defect 3
  commit) and are byte-identical at tip.
- Conventional consistency: `<rev>` full-hash convention, argparse exit 2 on
  usage errors falling under "undeclared nonzero code reads as
  could-not-evaluate" (SKILL.md:447-448) — matches how sibling rows behave.

# Findings

1. (nit, lowest) C2 write-scope cell "temporary clone (removed)" omits the
   `nogit-bin` sibling directory the counter also creates inside the same
   removed TemporaryDirectory (check_could_not_evaluate.py:157-159). A tighter
   cell would read "temporary clone and no-git PATH dir (removed)". No
   behavioral consequence; the scope is still bounded and still removed.

No other discrepancy found: entry commands, verdict maps, self-test flags,
pinned-value claims, write scopes and owners are all consistent with the
scripts at the tip.

No installs needed (python3 + git already present). No lane files modified;
all runs inside the sandbox clone.
