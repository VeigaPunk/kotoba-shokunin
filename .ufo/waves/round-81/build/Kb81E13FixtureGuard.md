# Kb81E13FixtureGuard — tooling hygiene sweep (round 81, wave w1)

Lane base: `b284223105f4d106f7e8f56ed4fd296c643cda0e` (verified `git -C <lane> rev-parse HEAD` →
`b284223105f4d106f7e8f56ed4fd296c643cda0e`, read-only).
Scope: `verifiers/` (62 `*.py` + 2 shell/JSON data files) and the round-81 build scripts as they
landed during the wave (`run-battery.sh`, `refresh-corpus-baseline.py`, `Kb81E14PinAudit-recompute.py`,
`Kb81S11GateQuotes-verify.py`, `Kb81S17ReceiptIndex-check.py`, the two doc patches, and the JSON data
files). Scratch (removed before yield): `/fast/scratch/hyaku/kotoba-r81/Kb81E13FixtureGuard/`.
Tooling: **nothing installed, upgraded or run through a package manager**; `pacman` untouched (host
pause respected); no network fetch by this seat.

## Class counts

```
T1  7   hardcoded /tmp root                 → 0 real  (7 fixture strings, listed below)
P   0   pacman invocation                   → 0
N  15   network-capable counters            → 0 in a measured path (all behind --fetch; the 7 battery files import no network module)
G 349   subprocess git/jj sites             → 0 mutating site outside a sandbox, EXPECT 3 defect (build harness, below)
R   1   repo-path write outside TMPDIR      → 3 sites (2 self-test, 1 build harness), triaged F1/F2/F3
```

Every mutating git call in `verifiers/` takes `-C <temp dir>` (or `cwd=<temp dir>`), and the temp dir is
`tempfile.mkdtemp()` / `TemporaryDirectory()` with a `rev-parse --show-toplevel` assertion that the
directory is its own toplevel. `jj` is invoked nowhere (`check_report_pointers.py:153` is a prose
command vocabulary).

## T1 — `/tmp` literals that do not honour TMPDIR: none

Command (AST; string constants inside docstrings excluded):

```
python3 - <<'PY'  # walks verifiers/*.py, prints Constant nodes containing "/tmp" outside docstrings
PY
```

```
verifiers/check_agentdef_boxes.py:1559        'delegated:/tmp/verify_agentdef.py'          fixture string (absolute-path scenario)
verifiers/check_spec_craft.py:1766            '/tmp'                                       fixture repo_arg, expects exit 2
verifiers/verify_corpus_independent.py:657    '# t\n\n## Coverage map\n…'                  fixture table body
verifiers/verify_corpus_independent.py:791    'corpus/README.md:12: /tmp/x2-nowhere.md…'   expected-output literal
verifiers/verify_corpus_integrity.py:1189     '/tmp/x/'                                    unit assertion token_path_class
verifiers/verify_corpus_integrity.py:1195     '## Coverage map\n…'                         fixture table body
verifiers/verify_corpus_integrity.py:1212     'corpus/README.md:6: /tmp/x2-nowhere/…'      expected-output literal
total=7
```

All seven are **fixture text** fed to a counter as data, never an actual scratch root. The only shell
worlds root is TMPDIR-first: `verifiers/fault_injection_corpus.sh:53` →
`WORLDS=${TMPDIR:-/tmp}/round12-faults.$$`. Every Python scratch root in the tree is
`tempfile.mkdtemp(...)`/`TemporaryDirectory()` (TMPDIR honouring) — including
`check_allowed_tools.py:792` `mkdtemp(prefix=prefix, dir=_WORK)` where `_WORK` is `None` unless
`--work` is passed.

## P — pacman / package managers: none

```
grep -rn --include='*' -E '\bpacman\b' verifiers/ .ufo/waves/round-81/build/
.ufo/waves/round-81/build/Kb81S12AssimDisp.md:27: - Tooling: nothing installed or upgraded (no pacman; the host pause was respected).
```

One prose sentence in a seat report; zero invocation, zero `sudo`, zero `-Sy/-Syu`.

## N — network calls in a measured path: none

Fifteen counters are network-*capable* (`urllib.request.urlopen` or a `curl` subprocess). Static
reachability (AST: network primitives → enclosing function → every call site and its enclosing `if`
tests) shows exactly one gate per file, `if args.fetch`, except the self-test paths, which substitute
the transport before calling it:

```
check_agent_definitions.py:1116      if args.fetch
check_client_trust_gates.py:382,386  if args.fetch and args.rev
check_command_files.py:1926          if args.fetch            (self_test stubs `fetch`)
check_description_thresholds.py:495  if args.fetch
check_explicit_invocation.py:612     if args.fetch
check_hook_files.py:2390             if args.fetch            (L1095 fetch→run_curl; self_test rebinds run_curl, L2246-2289)
check_mcp_instructions.py:415        if args.fetch
check_overlap_levers.py:651          if args.fetch            (fetch_probe's only call site, L641 block)
check_plugin_manifests.py:1909       if args.fetch            (self_test stubs `fetch`, L1824)
check_scoped_rules.py:2527           if args.fetch            (self_test rebinds run_curl, L2055-2082; score() rebinds globals L2274-2280)
check_scoped_rules_v31.py:2680       if args.fetch            (same pattern, L2132-2160 / L2427-2441)
check_scoped_rules_v32.py:3091       if args.fetch            (same pattern, L2380-2408 / L2640-2689)
check_skill_evals.py:345             if args.fetch
check_skill_evals_v2.py:700          if args.fetch and backed
check_skill_precedence.py:423,427    if args.fetch and n == TOTAL   (conditional expression)
```

The seven files the tip battery runs — `check_gate_registry.py`, `check_assertion_floors.py`,
`verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`,
`check_correction_sweep.py`, `check_tip_battery.py` — contain **no** network primitive at all:

```
grep -nE '\b(urllib|urlopen|http\.client|socket|curl|wget|requests)\b' <the seven>
grep-exit=1 (no match)
```

(`verify_skill_checklist.py:90` contains the word "curly", which a substring search reports; it is
prose in a docstring, not a primitive.)

`check_assertion_floors.py` re-runs the self-tests of the instruments, including
`check_overlap_levers.py` and `check_scoped_rules_v32.py`; both self-tests replace the transport
(`run_curl = lambda …`, `globals()["run_curl"] = …`) before any `fetch()` is reached, so the battery's
self-test path is network-free too — the static rebinds are cited by line above.

The one `curl` in the measured *documentation* channel is text only: `check_hook_files.py:170-172`
and `check_scoped_rules*.py:246-248` describe the frozen `curl -sSL --max-time 30 -A <browser UA> …`
recheck invocation in a docstring; the executable form is `run_curl()` → `curl_argv()`, reachable only
from `fetch()`, reachable only from the `--fetch` branches named above.

## G — mutating git/jj outside a sandbox: none in `verifiers/`

349 `subprocess` sites whose head is `git` (no `jj`). Mutating verbs (`init`, `add`, `commit`,
`checkout`, `reset`, `clean`, `clone`, `apply`) occur only in fixture/self-test worlds; representative
constructions, each with its own toplevel assertion:

```
check_allowed_tools.py:1536-1550   git = ["git","-c","commit.gpgsign=false","-C",str(root)]; init/add/commit; asserts rev-parse --show-toplevel == root
check_spec_craft.py:1287-1300      d = tempfile.mkdtemp(prefix="k74-c1-"); git = [... "-C", d]; toplevel asserted; add/commit
check_cn_vendor_surfaces.py:1012-1029   same pattern (k73-c1-)
check_author_rules.py:581-589      same pattern
check_desc_craft.py:1258-1272      mkdtemp(dir=WORK_DIR or None); toplevel asserted
check_overlap_levers.py:1197-1219  tempfile.TemporaryDirectory(); git init/add/commit with cwd=repo
verify_corpus_integrity.py:1035-1046    _one_commit_repo: git init/add/commit with -C str(path)
check_tip_battery.py:186-200, 411-425   git clone --shared <lane> <scratch>; fixture init/add/commit in the fixture lane; `_commit_all` asserts toplevel
```

Read-only plumbing (`rev-parse`, `cat-file`, `show`, `archive`, `diff`, `hash-object`, `for-each-ref`)
does take `-C <lane>`, which is the intended measurement target. No site writes to `LANE`/`REPO`.

**Exception (build harness, F3):** `.ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py` runs
`git apply` (L156), `git checkout -- .` and `git clean -qfd verifiers` (`resync()`, L82-84) against
whatever `--repo` names, guarded only by `rev-parse --show-toplevel == repo` (L100). At this base the
lane's own HEAD *is* `b2842231`, so pointing it at the lane would apply patches and clean
`verifiers/` inside the lane with no refusal. See F3.

## R — repo-path writes outside TMPDIR: three sites, triaged

| site | what | verdict |
|---|---|---|
| `check_mcp_instructions.py:274` | `TemporaryDirectory(prefix="mcp-self-test-", dir=LANE)` | **F1** — self-test scratch inside the measured repo |
| `compare_harness_independent.py:1499,1576` | `TemporaryDirectory(prefix=".scope-cwd-" / ".fixture-", dir=FIXTURE_DIR)` | **F2** — self-test scratch inside the repo fixture tree |
| `Kb81E14PinAudit-recompute.py` | `git apply` / `checkout` / `clean` into `--repo` | **F3** (above) |

All three clean up on the normal path. Measured empirically in the scratch clone
(`python3 -B verifiers/check_mcp_instructions.py --self-test` → `self-test: 0 failure(s) over 17
assertions`, exit 0; `compare_harness_independent.py --self-test` → `0 failure(s) over 330 assertions`,
exit 0) and `git -C clone status --porcelain --untracked-files=all` was empty after each run
(`leftovers-after-mcp=0`, `leftovers-after-compare=0`). The residual is kill-time debris: a SIGKILL
between creation and cleanup leaves `mcp-self-test-*` in the lane root and `.scope-cwd-*` /
`.fixture-*` under `verifiers/fixtures/compare-harness-independent/`, i.e. exactly the R80-D2 class
(probe output outside the wave dir) — `[INFERENCE: not exercised; both counters are kill-tested by
nothing in the tree]`.

## refresh-corpus-baseline.py — the two required claims, verified

The round-81 build copy is **byte-identical** to the reviewed round-80 artifact, so these measurements
are of the round-81 bytes:

```
sha256sum .ufo/waves/round-80/build/refresh-corpus-baseline.py .ufo/waves/round-81/build/refresh-corpus-baseline.py
8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a  round-80/…/refresh-corpus-baseline.py
8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a  round-81/…/refresh-corpus-baseline.py
```

### (a) writes exactly one path

Static: the only write whose target is a repo path is `baseline_path.write_text(...)` (L356). Every
other write is a temp-dir write under `tempfile.mkdtemp(prefix="refresh-corpus-baseline.",
dir=os.environ.get("TMPDIR") or None)` (L218): `gate_json` writes `<tmp>/<name>.json` and
`<tmp>/<name>.err` (L153-155); the `finally` block unlinks that temp dir (L403-413). No `open(...,
"w")`, no `shutil.copy`, no symlink creation anywhere in the file.

Empirical (scratch clone `…/Kb81E13FixtureGuard/clone` at `b2842231`, fixture commit `e008a65` adding a
coverage-map row so the zero-mode index class reads 0):

```
python3 -B refresh-r81.py --repo <clone> --carry corpus.pointers.report_dead \
        --carry corpus.pointers.commit_unresolvable
exit=0
gate disagreement (not recorded, expectation stays 0): corpus.pointers.report_dead integrity 1 vs independent 0
corpus.index.tracked_files         154 -> 155
corpus.pointers.report_total       109 -> 111
carried red: corpus.pointers.report_dead observed 1, expectation stays 0
carried red: corpus.pointers.commit_unresolvable observed 2, expectation stays 0
wrote /fast/scratch/hyaku/kotoba-r81/Kb81E13FixtureGuard/clone/verifiers/corpus-baseline.json (head e008a65 (detached measurement commit; …))
post-refresh: 7/9 checks pass, exit 1, drift: corpus.pointers.report_dead, corpus.pointers.commit_unresolvable
independent: exit 1; exit 1
--- changed paths (porcelain, untracked included)
 M verifiers/corpus-baseline.json
--- git diff --stat
 verifiers/corpus-baseline.json | 13 +++++++------
 1 file changed, 7 insertions(+), 6 deletions(-)
```

One path changed, no untracked residue, TMPDIR emptied (`ls -A $S/tmp | wc -l` → `0`).

### (b) refuses symlinks

```
lrwxrwxrwx … verifiers/corpus-baseline.json -> corpus-baseline.real.json
python3 -B refresh-r81.py --repo <clone> --dry-run
exit=2
refresh-corpus-baseline: refused: verifiers/corpus-baseline.json is a symlink; refusing to write through it
sha256 target before == after: cbae8df5e6df96b16083b8362a331accbe2c409625ac0dbbd1a3cf121c1b983c
```

The refusal fires **before** the write and before the `--dry-run` return (check at L258-260; write at
L356), and the symlink target's bytes were unchanged.

Control refusals (no write in either case, tree left clean):

```
python3 -B refresh-r81.py --repo <clone> --dry-run     # clean tree, no --carry
exit=2
refresh-corpus-baseline: refused: zero-mode corpus.index.unindexed observed 1, not 0; fix the drift …
git -C clone status --porcelain --untracked-files=all  → (empty)
verifiers/corpus-baseline.json sha256 unchanged: cbae8df5…b983c
```

Also verified in the same runs: a dirty tree is refused (`open_tree`, `git status --porcelain
--untracked-files=all`, L136-146), an index class can never be carried (L210-214), and the recorded
`head_label` marks a detached measurement commit as "resolvable in the measuring clone only, not in the
lane repository" (L317-322).

## external-commits.json — pure data

The committed file had **not landed** in the build dir when this sweep ran
(`find .ufo/waves/round-81 -name external-commits.json` → nothing). The derived draft it will be
written from is pure data:

```
python3 -c "import json; d=json.load(open('Kb81E03ExtManifest.json')); print(type(d).__name__, len(d)); print(sorted(d[0].keys()))"
list 1
['evidence', 'hash', 'pinned_at', 'repo']
non-string leaves: []
```

A JSON array of one object with four plain-string fields (`hash`, `repo`, `evidence`, `pinned_at`), no
nested executables, no shell strings. Requirement recorded for the landed file: it must parse with
`json.load`, resolve to `list`/`dict` of strings only, and be read by both corpus gates as data (never
`eval`/`exec`/`import`/`subprocess` of a value). The gate-side half of that check belongs to the seat
that lands the readers; this seat re-checks the file itself when it appears (see "Landed during the
wave").

## Findings

- **F1 (medium, `verifiers/check_mcp_instructions.py:274`)** — self-test scratch dir rooted at `LANE`
  instead of TMPDIR. Cleaned in the `with` block; a kill leaves `mcp-self-test-*` in the lane root and
  turns the tree dirty (which the refresher then refuses). The same file uses the default TMPDIR two
  screens later (L290), so the `dir=LANE` choice is not load-bearing.
- **F2 (low-medium, `verifiers/compare_harness_independent.py:1499,1576`)** — self-test scratch dirs
  rooted at `verifiers/fixtures/compare-harness-independent`. Same kill-debris class; the `.`-prefixed
  names keep a leftover out of the case scan (`case.json` filter, L1466), so the case reader is not
  misled.
- **F3 (medium, build harness `.ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py:82-84,100,156`)**
  — mutating git (`apply`, `checkout -- .`, `clean -qfd verifiers`) against an operator-supplied
  `--repo` with only a toplevel assertion. The refresher's stronger preconditions (clean tree,
  required-file set, toplevel identity) are the house pattern; this harness has none of them, and the
  lane at this base satisfies the one assertion it does make.
- **F4 (observation, same file, L257-259)** — the counter self-test is run with
  `TMPDIR=str(repo.parent/"tmp")`; if that directory does not exist, `tempfile` in the child fails
  rather than falling back. Not exercised here (the seat created it).
- **F5 (low, build harness `build/c1_controls.py:725-731`, git sites L222/L281)** — `--work` is taken
  as given and worlds are `git init`ed under it; the default is a TMPDIR `mkdtemp`, so the normal path
  is sandboxed, but an operator pointing `--work` at the lane would write world directories into it.
  Same class and remedy as F3 (refuse a work root that is the lane, the fleet root, or a repository
  toplevel).

No claim-critical defect: none of F1–F5 touches the C1 or C2 predicate, the six battery gates, or a
measured path.

## Clean sweeps (one line each)

- `clean — grep -rn -E '\bpacman\b' verifiers/ .ufo/waves/round-81/build/` (one prose sentence in a seat report, zero invocations).
- `clean — python3 AST /tmp sweep over verifiers/*.py` (7 fixture strings, zero scratch roots).
- `clean — grep -nE '\b(urllib|urlopen|http\.client|socket|curl|wget|requests)\b' <the seven battery files>` (exit 1).
- `clean — AST reachability over verifiers/*.py` (15 network-capable counters, every primitive behind `if args.fetch` or a rebinding self-test).
- `clean — AST subprocess sweep` (349 git sites, 0 `jj`; all mutating sites `-C <tempdir>` with a toplevel assertion).
- `clean — diff -u round-80/build/run-battery.sh round-81/build/run-battery.sh` (header + scratch-root lines only; 0 `/tmp`, 0 pacman, 0 network, one `git clone --shared` into its own `$S` world with a toplevel assertion, `rm -rf -- "$S"` on exit).
- `clean — grep -rn --include='*.py' -E 'shell=True|os\.system|os\.popen|subprocess\.call\(' verifiers/` (exit 1 — no shell string is ever handed to a shell; every child is an argv list).
- `clean — grep -rn --include='*.py' -E '"sudo"|"systemctl"' verifiers/` (four hits, all command-vocabulary data or docstrings: `check_infoless_fences.py:134`, `verify_skill_checklist.py:142,356`, `check_report_pointers.py:156`; zero invocations).
- `clean — grep '^+' on Kb81S08ReadmeRows.patch, Kb81S08ReadmeRows.stageA.patch, Kb81S10Province.patch, Kb81S05SourcesEdits.patch, Kb81S09SkillRule-SKILL.patch` (17 added lines total, all prose/table cells; zero hits for `/tmp`, `pacman`, `urllib`, `curl `, `wget `, `subprocess`, `eval(`, `exec(`, `sudo`).

## Documented recheck text (the permitted fetch form)

`build/allowed-tools-sdk-round81.md` (the C2 corpus entry) carries its `recheck:` line as a documented
shell recipe — `curl -fsSL -A Mozilla/5.0 --max-time 60 "$u" -o "$f" && sha256sum "$f" && tr -d '\140'
< "$f" | grep -c -F "<quote>"` — which is text a human re-runs, not code a counter executes. That is the
form the seat spec allows ("fetch code may exist only as documented recheck text"); the corresponding
executable path in counters is still `--fetch`-only (N section above). The same entry states it was
located in the committed snapshot's own bytes, which is what keeps the measurement off the network.

## Landed during the wave (final state of the sweep)

Build scripts swept at the end of the seat (all of `*.py` / `*.sh` present under
`.ufo/waves/round-81/build/`, 127 entries in the directory at that moment):

```
run-battery.sh                     clean — header + scratch-root lines only vs r80; git clone --shared into its own $S world with a toplevel assertion; rm -rf -- "$S"
refresh-corpus-baseline.py         byte-identical to r80 (sha256 8481be46…b470a); two claims verified empirically above
Kb81E14PinAudit-recompute.py       F3: mutating git (apply/checkout/clean) on an operator-supplied --repo, toplevel assertion only
Kb81E07C2Worlds.ref-counter.py     clean — 362 lines, imports argparse/hashlib/html/re/subprocess/sys only (no network module); git read-only (rev-parse, cat-file); 0 write_text/open(…"w")
Kb81S11GateQuotes-verify.py        clean — one write, to sys.argv[1] (the caller's receipt path)
Kb81S17ReceiptIndex-check.py       clean — no subprocess, no writes, no network
c1_controls.py                     F5: git init/add under --work (default a TMPDIR mkdtemp); an operator-supplied --work is not refused for the lane/fleet root
Kb81G01Revenge-probe-round76-token.py  clean — read-only probe; imports a verifier by absolute lane path, writes nothing, no network
```

**Still absent at the end of the sweep** (verified by `find .ufo/waves/round-81 -name
'check_sdk_allowed_tools*' -o -name 'external-commits*'` → no output, and
`ls verifiers/external-commits.json verifiers/check_sdk_allowed_tools.py` → both "No such file"):

- the C1 instrument patches over `verify_corpus_integrity.py` / `verify_corpus_independent.py` and the
  amended `check_tip_battery.py`;
- the C2 counter `verifiers/check_sdk_allowed_tools.py` (only the read-only draft
  `Kb81E07C2Worlds.ref-counter.py` exists, swept above);
- `verifiers/external-commits.json` (only the derived draft `Kb81E03ExtManifest.json`, strings-only).

Those three artifacts are therefore **unswept** for the four classes. The L1's integration step is to
re-run the same sweeps over their added lines and to check the manifest is strings-only data. One
cross-artifact note for the integrator: `Kb81S09SkillRule-SKILL.patch` adds the registry row that cites
`verifiers/check_sdk_allowed_tools.py` (plan R6 says the row and the counter ship in the same commit) —
if the counter does not land, that row names a gate that does not exist.

`c1_controls.py` is the fifth finding (F5, `--work` not refused for the lane or the fleet root); its
default work root is a TMPDIR `mkdtemp`, so the normal path is sandboxed.
