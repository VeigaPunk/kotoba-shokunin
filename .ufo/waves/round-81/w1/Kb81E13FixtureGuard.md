# Kb81E13FixtureGuard — tooling hygiene sweep (round 81, w1)

Seat: `Kb81E13FixtureGuard` (executor). Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Full sweep with commands, line numbers and receipts: `build/Kb81E13FixtureGuard.md`.

## What was asked and what was measured

Four classes over `verifiers/` (62 `*.py`, plus the shell and JSON data files) and the round-81 build
scripts: (1) hardcoded `/tmp` roots ignoring TMPDIR, (2) pacman invocations, (3) network calls in the
**measured** path of a counter, (4) mutating git/jj outside sandbox paths. Plus two named claims:
`refresh-corpus-baseline.py` writes exactly one path and refuses symlinks; `external-commits.json` is
pure data.

## Results

| class | count | verdict |
|---|---|---|
| `/tmp` literal roots | 7 | all fixture strings (`check_agentdef_boxes.py:1559`, `check_spec_craft.py:1766`, `verify_corpus_independent.py:657,791`, `verify_corpus_integrity.py:1189,1195,1212`); **0 real scratch roots**; the shell world builder is TMPDIR-first (`fault_injection_corpus.sh:53`) |
| pacman | 0 | one prose sentence in `build/Kb81S12AssimDisp.md:27`; no invocation anywhere |
| network in a measured path | 0 | 15 network-capable counters, every primitive behind `if args.fetch` or a transport rebinding in `--self-test`; the seven battery files import **no** network module (`grep -nE '\b(urllib\|urlopen\|http\.client\|socket\|curl\|wget\|requests)\b'` → exit 1) |
| mutating git/jj | 349 sites, 0 `jj` | all mutating sites `-C <tempdir>` / `cwd=<tempdir>` with `rev-parse --show-toplevel` assertions; **two build-harness exceptions** (F3, F5) |
| shell escapes | 0 | `grep -E 'shell=True\|os\.system\|os\.popen\|subprocess\.call\('` → exit 1; every child is an argv list |

## Two named claims — verified empirically

- `refresh-corpus-baseline.py` (the round-81 build copy is **byte-identical** to the round-80 artifact,
  sha256 `8481be46…b470a`, so the measurements are of the round-81 bytes): one repo-path write
  (`baseline_path.write_text`, L356), everything else in a TMPDIR `mkdtemp` removed in `finally`. A
  scratch-clone run with `--carry` wrote **exactly** `M verifiers/corpus-baseline.json` (porcelain with
  untracked files; `git diff --stat` 1 file, +7/−6), exit 0; a committed symlink at that path was
  refused (`exit=2`, "is a symlink; refusing to write through it") with the target's sha unchanged
  (`cbae8df5…b983c`); the clean-tree no-carry control refused on `corpus.index.unindexed observed 1`
  with the tree and the baseline bytes untouched.
- `verifiers/external-commits.json` had **not landed** anywhere in the wave or the lane at sweep end.
  The draft it is written from (`build/Kb81E03ExtManifest.json`) parses as a list of one object whose
  four fields are all strings — pure data. The strings-only rule is recorded for the landed file.

## Build scripts swept (round-81 wave)

```
run-battery.sh                     clean — vs r80 only header + scratch-root lines; git clone --shared into its own $S world with a toplevel assertion; rm -rf -- "$S"
refresh-corpus-baseline.py         byte-identical to r80; both claims verified empirically (above)
Kb81E14PinAudit-recompute.py       F3 — mutating git on an operator-supplied --repo, toplevel assertion only
Kb81E07C2Worlds.ref-counter.py     clean — no network module, git read-only (rev-parse, cat-file), zero writes
Kb81S11GateQuotes-verify.py        clean — one write to sys.argv[1]
Kb81S17ReceiptIndex-check.py       clean — no subprocess, no writes, no network
c1_controls.py                     F5 — git init/add under --work; default work root is a TMPDIR mkdtemp
Kb81G01Revenge-probe-round76-token.py  clean — read-only probe, writes nothing
```

## Findings (none claim-critical)

- **F1** `verifiers/check_mcp_instructions.py:274` — `TemporaryDirectory(..., dir=LANE)`: self-test
  scratch inside the measured repo. Cleaned on exit (verified: 17 assertions, exit 0, porcelain empty);
  a kill leaves `mcp-self-test-*` in the lane root — the R80-D2 class. The same file uses TMPDIR at
  L290, so `dir=LANE` is not load-bearing.
- **F2** `verifiers/compare_harness_independent.py:1499,1576` — self-test scratch under
  `verifiers/fixtures/compare-harness-independent` (`.scope-cwd-*`, `.fixture-*`). Verified clean exit
  (330 assertions, no residue); same kill-debris class; the `.`-prefix keeps leftovers out of the case
  scan (`case.json` filter, L1466).
- **F3** `build/Kb81E14PinAudit-recompute.py:82-84,100,156` — `git apply` / `checkout -- .` /
  `clean -qfd verifiers` against an operator-supplied `--repo` guarded only by a toplevel assertion. The
  lane's HEAD **is** the base commit, so pointing it at the lane satisfies that assertion and mutates
  `verifiers/`. The refresher's preconditions (clean tree, required files, toplevel identity) are the
  house pattern this harness lacks.
- **F4** same file, L257-259 — the child self-test gets `TMPDIR=<repo parent>/tmp`; a missing directory
  fails the child rather than falling back. Observation, not exercised.
- **F5** `build/c1_controls.py:725-731` (git sites L222/L281) — `--work` is taken as given and worlds
  are `git init`ed under it; the default is a TMPDIR `mkdtemp`, so the normal path is sandboxed, but a
  `--work` pointed at the lane would write world directories into it. Same class and remedy as F3.

## Unswept gap (explicit, not a pass)

At sweep end the wave contained **no** C1 instrument patch, **no** `verifiers/check_sdk_allowed_tools.py`
(only the read-only draft `Kb81E07C2Worlds.ref-counter.py`) and **no** `verifiers/external-commits.json`
(only the strings-only draft `Kb81E03ExtManifest.json`). Cross-artifact note for the integrator:
`Kb81S09SkillRule-SKILL.patch` adds the registry row citing `verifiers/check_sdk_allowed_tools.py`, and
plan R6 says the row and the counter ship in the same commit — if the counter does not land, that row
names a gate that does not exist.

## Tooling / scratch

No install, upgrade or package-manager call; pacman untouched (host pause respected); no network fetch
by this seat. Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E13FixtureGuard/` created for the refresher
and the two self-test runs and removed before yield; receipts copied into `build/` first.

VERDICT: Hygiene clean where it must be — 0 pacman, 0 real `/tmp` roots that ignore TMPDIR, 0 network calls in any measured path (the seven battery files have no network module at all, and every network-capable counter's primitive sits behind `if args.fetch` or a rebinding self-test), 0 shell-string escapes, 0 mutating git/jj sites outside a sandbox in `verifiers/`; the refresher's two claims verified empirically on the round-81 bytes (exactly one path written, symlink refused with exit 2, target sha unchanged) and the manifest draft is strings-only data — with five recorded findings (F1/F2 in-repo self-test scratch, F3/F5 unguarded operator-supplied build roots, F4 observation) none on a claim's path, and an explicit unswept gap for the C1 instrument patches, the C2 counter and `external-commits.json`, which had not landed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E13FixtureGuard.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E13FixtureGuard.md
