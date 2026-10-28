# Kb80E13FixtureGuard — tooling hygiene sweep (round 80, wave w1)

Seat: `Kb80E13FixtureGuard` (leaf executor, no dispatch).
Date: 2026-10-27. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/` (removed before yield).

Scope as dispatched: scan every file under `verifiers/` plus the new wave build files for
(hardcoded `/tmp` roots that ignore TMPDIR, pacman invocations, network calls at measurement
time, mutating git/jj outside a sandbox); verify the refresh script's writes (exactly one path,
refuses symlinks); publish the findings.

**This seat ships no patch and no repair.** It measures and reports. Every count below carries
its command; every verdict carries its own exit status.

---

## 0. Method

Scanner (tokenize-based, so comments and docstrings are excluded from the code-level classes):
`/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/scan.py`. It classifies a line only when a
**code** token (not a comment) matches. Classes: `T1` hardcoded `/tmp` root, `P` pacman,
`N` network call, `G` git/jj mutation.

```
python3 -B scan.py <verifiers dir> <round-80 build dir>
```

Run over `verifiers/` (60 files) and `.ufo/waves/round-80/build/`:
`T1` 7, `P` 0, `N` 65, `G` 184, total 256 findings — **all 256 triaged below**; only 3 are
defects (F1, F2, F3 below). The rest are benign and the classification is stated.

---

## 1. `P` — pacman invocations

**None. Zero findings, whole scope.**

```
python3 -B scan.py <verifiers> <round-80 build> | awk -F'\t' '$1=="P"'   → no output
grep -c pacman <verifiers/*.py>  → 0 in every file
```

The operator tooling directive (2026-10-19) freezes pacman host-wide. No verifier, no wave
build file, and no shell runner invokes it. **Clean.**

---

## 2. `T1` — hardcoded `/tmp` roots that ignore TMPDIR

**Zero real findings.** 7 raw hits, all benign:

| file:line | class | why benign |
|---|---|---|
| `verifiers/check_agentdef_boxes.py:1559` | fixture-string | `"delegated:/tmp/verify_agentdef.py"` is a **test fixture string** for the absolute-path arm, never opened. |
| `verifiers/check_spec_craft.py:1766` | fixture-string | `repo_arg="/tmp"` is a **self-test argument** asserting "not a git worktree" → exit 2. Never written. |
| `verifiers/verify_corpus_independent.py:791` | fixture-string | expected-output literal for a rooted-dead-token fixture. |
| `verifiers/verify_corpus_integrity.py:1189` | fixture-string | `token_path_class("/tmp/x/")` unit assertion. |
| `verifiers/verify_corpus_integrity.py:1197` | fixture-string | fixture table row. |
| `verifiers/verify_corpus_integrity.py:1212` | fixture-string | expected-output literal. |

The one **shell** runner with a `/tmp` default is
`verifiers/fault_injection_corpus.sh:53` — `WORLDS=${TMPDIR:-/tmp}/round12-faults.$$`:
**TMPDIR-first, `/tmp` only as fallback.** Correct shape.

**Verified TMPDIR is honoured end-to-end** (not just in the code):

```
$ export TMPDIR=/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/tmp
$ python3 -c "import tempfile,os; print(tempfile.gettempdir())"
/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/tmp
```

Every `tempfile.mkdtemp(...)` / `TemporaryDirectory(...)` in `verifiers/` uses the default
location (i.e. TMPDIR-aware) with one exception noted in F1.

---

## 3. `N` — network calls at measurement time

**The measurement path is network-free in every counter.** 65 raw hits across 15 verifiers; all
are behind an opt-in `--fetch` flag or are the counter's *own* fetch machinery that the default
path never enters.

Measured, per file (the `--fetch` argument count is the gate on the network branch):

| file | `--fetch` arg | network site |
|---|---|---|
| `check_agent_definitions.py` | 1 | `:766` `urlopen` — called only at `:1116` under `if args.fetch:` |
| `check_client_trust_gates.py` | 1 | `:272` `urlopen` — `fetch()` called only at `:381`/`:385` under `if args.fetch:` |
| `check_command_files.py` | 1 | `:916` `urlopen` — called only at `:1926` under `if args.fetch:` |
| `check_description_thresholds.py` | 1 | `:262` `urlopen` — called only at `:495` under `if args.fetch:` |
| `check_explicit_invocation.py` | 1 | `:359` `urlopen` — called only at `:612` under `if args.fetch:` |
| `check_hook_files.py` | 1 | `:1059`–`:1087` `curl` argv — called only at `:2390` under `if args.fetch:` |
| `check_mcp_instructions.py` | 1 | `:221` `urlopen` — called only at `:415` under `if args.fetch:` |
| `check_overlap_levers.py` | 1 | `:496` `urlopen` — `fetch_probe` only at `:651` under `if args.fetch:` |
| `check_plugin_manifests.py` | 1 | `:877` `urlopen` — called only at `:1909` under `if args.fetch:` |
| `check_scoped_rules.py` | 1 | `:1495`–`:1528` `curl` argv — called only at `:2527` under `if args.fetch:` |
| `check_scoped_rules_v31.py` | 1 | `:1552`–`:1585` — only under `if args.fetch:` (`:2680`) |
| `check_scoped_rules_v32.py` | 1 | `:1648`–`:1681` — only under `if args.fetch:` (`:3091`) |
| `check_skill_evals.py` | 1 | `:185` `urlopen` — `live_fetch` only at `:345` under `if args.fetch:` |
| `check_skill_evals_v2.py` | 1 | `:333` `urlopen` — `live_fetch` only at `:700` under `if args.fetch:` |
| `check_skill_precedence.py` | 1 | `:276` `urlopen` — only at `:423`/`:427` under `if args.fetch and n == TOTAL` |

**The six gates the tip battery actually runs are network-free by construction** — zero hits in
any of them:

```
for f in check_gate_registry.py check_assertion_floors.py verify_skill_checklist.py \
         verify_corpus_integrity.py verify_corpus_independent.py check_correction_sweep.py \
         check_tip_battery.py; do
  grep -c 'urlopen\|urllib\.request\|requests\.\|socket\.\|"curl"' "$f"
done
→ 0 0 0 0 0 0 0
```

The recheck **text** naming curl is documentation (allowed by the seat brief). The one live
`curl` in the wave build dir is
`.ufo/waves/round-80/build/Kb80N01Sentinel-recheck-c2-stability.py:87` — a **source-stability
recheck** tool whose whole purpose is re-opening the six pages live. It is not imported by, or
in the measured path of, any counter (`grep -rn 'Kb80N01Sentinel' verifiers/` → no output).
**Correct shape: a recheck fetches; a measurement does not.**

**Clean.**

---

## 4. `G` — mutating git/jj outside a sandbox

**Zero findings.** 184 raw hits, every one of them inside a sandbox. Verified by tracing each
write site to its repository argument:

- Every write uses an explicit `-C <path>` / `cwd=<path>` aimed at a `tempfile` scratch
  (`check_author_rules.py:587`, `check_cn_vendor_surfaces.py:1026`, `check_desc_craft.py:1269`,
  `check_spec_craft.py:1286`, `check_command_files.py:1107`, `check_hook_files.py:1282`,
  `check_plugin_manifests.py:1069`, `check_alwayson_boxes.py:145`, `check_opencode_repin.py:151`,
  `check_agentdef_boxes.py:1440`, `check_r63_routed_repairs.py:353`, `check_r64_routed_repairs.py:571`,
  `check_overlap_levers.py:1208`, `check_tip_battery.py:418`).
- The `root`/`repo` argument of every one of those is a `tempfile.mkdtemp`/`TemporaryDirectory`
  directory: `check_agentdef_boxes.py:1467` (`root = Path(td)`),
  `check_r63_routed_repairs.py:434` (`tmp = Path(tempfile.mkdtemp(prefix="r63-c2-"))`),
  `check_r64_routed_repairs.py:790` (`root = temp / "counter-world"`).
- **No `git` write is aimed at the lane.** The searches for a lane-derived write target return
  empty:
  ```
  grep -nE '\["git", "-C", str\((LANE|REPO|Path\(__file__\))\)' *.py | grep -E '"(add|commit|checkout|reset|...)"'  → (empty)
  grep -nE 'git\(LANE|git\(REPO|git\(Path\(__file__\)' *.py                                                  → (empty)
  ```
- `check_could_not_evaluate.py:248` and `check_r67/r68/r69*` **clone** the lane into a temp dir
  and `checkout` *in the clone* (`-C str(clone)`), never in the lane.
- **jj: not used anywhere.** `grep -rn '\bjj\b' verifiers/*.py` returns one hit,
  `check_report_pointers.py:153`, which is a **command-name vocabulary list** for a prose parser
  (`python python3 py git bash sh zsh dash fish jj jj-lane.sh awk …`), not an invocation.

**Clean.**

---

## 5. The refresh script's writes — verified, both claims

Script under test: `.ufo/waves/round-79/build/refresh-corpus-baseline.py` (r79 reviewed draft;
the r80 build dir does not yet carry a copy — see F4).

### 5.1 "Writes exactly one path" — **CONFIRMED**

Claim (script docstring line 47): *"Writes exactly one path: `<root>/verifiers/corpus-baseline.json`
(never through a symlink)."*

Measured in a scratch clone at base (`/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/clone2`,
toplevel asserted):

```
$ python3 -B .../refresh-corpus-baseline.py --repo "$S/clone2" \
      --carry corpus.pointers.report_dead --carry corpus.pointers.commit_unresolvable
exit=0
corpus.index.tracked_files         144 -> 152
corpus.pointers.report_total       99 -> 109
corpus.pointers.commit_total       43 -> 46
carried red: corpus.pointers.report_dead observed 1, expectation stays 0
carried red: corpus.pointers.commit_unresolvable observed 2, expectation stays 0
wrote .../clone2/verifiers/corpus-baseline.json (head 6941d37 ...)
post-refresh: 7/9 checks pass, exit 1, drift: corpus.pointers.report_dead, corpus.pointers.commit_unresolvable

$ git -C "$S/clone2" status --porcelain --untracked-files=all
 M verifiers/corpus-baseline.json

$ git -C "$S/clone2" diff --stat
 verifiers/corpus-baseline.json | 17 +++++++++--------
 1 file changed, 9 insertions(+), 8 deletions(-)
```

**Exactly one path changed: `verifiers/corpus-baseline.json`.** The gate JSON documents the
script reads are written under `$TMPDIR` (`tempfile.mkdtemp(prefix="refresh-corpus-baseline.",
dir=os.environ.get("TMPDIR") or None)`, line ~217) and unlinked in the `finally` block
(`os.unlink(os.path.join(tmpdir, name))` × 4, then `os.rmdir(tmpdir)`).

### 5.2 "Refuses symlinks" — **CONFIRMED**

Both the code path and the behaviour:

```
# code, line 258-260
baseline_path = root / BASELINE
if baseline_path.is_symlink():
    raise Refused(f"{BASELINE} is a symlink; refusing to write through it")
```

```
$ ln -s <outside target> clone2/verifiers/corpus-baseline.json
$ git add -A && git commit          # so the tree is clean and the symlink is committed
$ python3 -B .../refresh-corpus-baseline.py --repo "$S/clone2" --carry ...
refresh-corpus-baseline: refused: verifiers/corpus-baseline.json is a symlink; refusing to write through it
exit=2

$ sha256sum <the symlink target>   → 22d5f0bb…  (unchanged; the target was NOT written through)
$ ls -l clone2/verifiers/corpus-baseline.json
lrwxrwxrwx … clone2/verifiers/corpus-baseline.json -> …/symtarget/baseline.json   (still a symlink)
```

The refusal precedes the write, the target file's digest is unchanged, and the symlink is not
replaced. **Both claims verified.**

### 5.3 Additional fail-closed properties observed (not required, recorded)

- **Dirty tree refused** (exit 2, baseline untouched) — `git status --porcelain --untracked-files=all`
  must be empty.
- **Unindexed corpus file refused** (exit 2): at base the script refused with
  `zero-mode corpus.index.unindexed observed 1, not 0` — `corpus/lessons/round-79-verifier-spotcheck.md`
  is unindexed. The coverage-map row must land **before** the refresh, or the refresh writes nothing.
- **`--carry` refuses index classes**: `--carry corpus.index.unindexed` is rejected outright.
- **Symmetric refusal**: `report_dead` and `commit_unresolvable` were refused as zero-mode
  classes until named by `--carry`.

---

## 6. Findings (defects)

### F1 — `check_mcp_instructions.py` writes a scratch dir **inside the lane tree** (medium)

`verifiers/check_mcp_instructions.py:274`

```python
with tempfile.TemporaryDirectory(prefix="mcp-self-test-", dir=LANE) as td:
```

`LANE` is the **lane repository root** (`:64` `LANE = Path(__file__).resolve().parent.parent`).
Proven, not inferred:

```
$ python3 -c "import tempfile,pathlib; LANE=pathlib.Path('/home/.../kotoba-shokunin').resolve(); \
  t=tempfile.TemporaryDirectory(prefix='mcp-self-test-', dir=LANE); print(t.name, pathlib.Path(t.name).is_relative_to(LANE))"
/home/vgpnk/Projects/shokunin/kotoba-shokunin/mcp-self-test-fqrhmdp_ True
```

This is the only `dir=` in `verifiers/` that points at a **tracked tree** rather than TMPDIR.
The `TemporaryDirectory` context manager removes it on normal exit — measured: running
`python3 -B verifiers/check_mcp_instructions.py --self-test` in the scratch clone left **no**
residue and a **clean** `git status` — so this is a *transient* write into the lane root, not
accumulating litter. It is still a hygiene defect: a counter that creates a directory in the
lane it is measuring, at a path the lane's own `no-deletions` guard and `git status` see.

**Class:** hardcoded scratch root inside the measured tree (ignores TMPDIR).
**Suggested repair (not applied — verifiers/ is out of my write scope):** drop `dir=LANE`;
`TemporaryDirectory` without `dir=` honours TMPDIR. Note `check_correction_sweep.py:310` and
`:323` already use the TMPDIR-default form for the same purpose.

Same class, **lower severity**, benign in practice:

- `verifiers/compare_harness_independent.py:1499` and `:1576` use
  `tempfile.TemporaryDirectory(prefix=".scope-cwd-", dir=FIXTURE_DIR)` /
  `prefix=".fixture-", dir=FIXTURE_DIR`, where `FIXTURE_DIR = REPO / "verifiers" / "fixtures" /
  compare-harness-independent` (`:1433`) — inside the tracked tree. Measured: running
  `compare_harness_independent.py --self-test` (330 assertions, exit 0) left **no** residue and
  a clean `git status`. These prefixes are already named in `SKILL.md`'s registry row
  ("removable temp dirs under `verifiers/fixtures/compare-harness-independent` (nested self-test)"),
  so the lane has accepted this shape deliberately. **Recorded, not a defect.**

### F2 — the C2 counter's snapshot manifest **does not exist**: `.ufo/waves/round-79/snapshots/MANIFEST.sha256` (high, load-bearing)

The counter's conjunct (c) reads the snapshot pins from a **committed aggregate manifest**:

```
verifiers + .ufo/waves/round-79/build/check_allowed_tools.py:191-192
  SNAPDIR = ".ufo/waves/round-79/snapshots"
  MANIFEST = SNAPDIR + "/MANIFEST.sha256"
```

**That file is absent — from the working tree and from all of git history:**

```
$ find .ufo/waves/round-79 -name 'MANIFEST*'            → (nothing)
$ git log --all --oneline -- '.ufo/waves/round-79/snapshots/MANIFEST.sha256'   → (nothing)
$ git ls-files .ufo/waves/round-79/snapshots/ | wc -l   → 18   (6 × {snapshot, .fetch.json, .manifest})
$ ls .ufo/waves/round-79/snapshots/
S226-spec.md  S226.fetch.json  S226.manifest  …  S231-vibe.md  S231.fetch.json  S231.manifest
```

The counter therefore **cannot evaluate (c) at any revision**:

```
$ python3 -B …/check_allowed_tools.py --rev 398cbe1… --repo "$S/clone"
Repo -> EXC EnvError no manifest at .ufo/waves/round-79/snapshots/MANIFEST.sha256 at
       398cbe1…: the snapshots are unpinned, so (c) cannot be evaluated
```

and in the counter's own words (`:705`): *"the snapshots are unpinned, so (c) cannot be
evaluated"* → `EnvError` → **exit 2 (could-not-evaluate)**, not exit 1.

**What the r79 wave actually committed** is six **per-S** manifests, each pinning one snapshot:

```
$ for m in .ufo/waves/round-79/snapshots/*.manifest; do … sha256sum …; done
OK   S226.manifest -> S226-spec.md
OK   S227.manifest -> S227-claude.md
OK   S228.manifest -> S228-factory.md
OK   S229.manifest -> S229-msaf.html
OK   S230.manifest -> S230-pi.md
OK   S231.manifest -> S231-vibe.md
```

All six per-S pins are **correct** against the committed snapshot bytes, and the same six digests
agree with the six `S###.fetch.json` fetch records (`sha256` field) — e.g. S227
`31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9` in both.

**The fix is a mechanical concatenation and it works.** Measured in the scratch clone:

```
$ cat .ufo/waves/round-79/snapshots/*.manifest > .ufo/waves/round-79/snapshots/MANIFEST.sha256
$ python3 - <<'PY'   # import the counter, call Repo.manifest()
manifest() -> {'S226-spec.md': '9a67de89…', 'S227-claude.md': '31623035…', 'S228-factory.md': '81409d89…',
               'S229-msaf.html': '34016233…', 'S230-pi.md': '5b980552…', 'S231-vibe.md': 'fc48a5db…'}
S226 snapshot_name: S226-spec.md     S227 snapshot_name: S227-claude.md
S228 snapshot_name: S228-factory.md  S229 snapshot_name: S229-msaf.html
S230 snapshot_name: S230-pi.md       S231 snapshot_name: S231-vibe.md
```

The aggregate manifest satisfies the counter's parser exactly (its regex is
`([0-9a-f]{64})[ \t]+\*?(\S(?:.*\S)?)` — `sha256sum` output is `<64hex>  <name>`, which matches),
each `snapshot_name()` resolves unambiguously, and the "manifest pins a second digest" and
"manifest path escapes SNAPDIR" guards are satisfied because every name is a bare basename.

**Consequence for C2:** without this file the counter cannot reach `6 of 6` on any world — it
exits 2 before scoring. **This is the single highest-leverage missing byte-stream in the round.**

**Class:** missing fixture (the counter's pin table), not a code defect.
**Owner:** the snapshot/entry seat must land the aggregate manifest (or the counter seat must
read the six per-S `.manifest` files instead — a one-line change to `Repo.manifest()`).

### F3 — the plan's grammar class does **not** match the tokens the gates actually report red (high)

The plan (§Trigger, and the C1 repair-5 bullet) names the two `commit_unresolvable` tokens as
`google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`, in the `owner/repo@<hex>`
grammar. **Measured at base, both corpus gates report a different pair**, in a different grammar:

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json    (scratch clone at base)
commit_unresolvable_detail: ['corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00',
                             'corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00']

$ python3 -B verifiers/verify_corpus_independent.py --repo <clone> --json   (pristine clone at base)
commit_unresolvable_detail: ['corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00',
                             'corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00']
commit_quoted_detail:      [… 'corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff',
                                'corpus/lessons/round-53.md:44: cfb894a5', …]
```

- The two red tokens are the **same** commit `7bb48f21…` cited **twice**, at
  `corpus/SOURCES.md:171` and `:172` — the S230 and S231 rows (pi-mono and Mistral Vibe).
- `451a02ff` and `cfb894a5` are **already classified** — as *quoted meta-findings*, i.e.
  **excluded** from `commit_unresolvable` (`commit_quoted_excluded`), because they sit inside a
  code span in those lessons. They are **not** the red pair.
- `7bb48f21…` is in **neither** the lane nor the fleet:
  `git -C <lane> cat-file -t 7bb48f21…` → `fatal: git cat-file: could not get object info`;
  same for the fleet root. It is a genuine third-repository object (badlogic/pi-mono).

**Therefore the plan's literal grammar rule is a no-op on this corpus.** Measured with the
plan's rule applied literally to every `commit \`<token>\`` candidate:

```
commit-tokens the PLAN rule would call external: 0
commit-tokens the PLAN rule would NOT call external: 50
  → corpus/SOURCES.md:171 7bb48f21…   STILL RED under the plan's literal rule
  → corpus/SOURCES.md:172 7bb48f21…   STILL RED under the plan's literal rule
```

Reason: the S230/S231 rows cite the repo as `` `badlogic/pi-mono` commit `7bb48f21…` `` —
**backticked owner/repo followed by the word "commit"**, not the `owner/repo@<hex>` adjacency:

```
line 171: owner/repo@hex present in the ±120-char window: False
          owner/repo@hex present ANYWHERE in the line:     False
          window: …page revision `main` resolved to `badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00`; fetched 2026-10-27 …
```

A rule that keys on the **`owner/repo` + `commit` + `<hex>` adjacency** (or on the row's
third-party host) *does* classify them: `owner/repo@hex anywhere in line = False`, but
`third-party host URL in row = True` for both lines (`raw.githubusercontent.com/badlogic/pi-mono`,
`raw.githubusercontent.com/mistralai/mistral-vibe`).

**Class:** fixture/grammar mismatch between the plan's stated class and the corpus's actual
citation grammar — the repair would land as a no-op and leave the gate red.
**Owner:** the grammar-fix seat (Kb80E05GrammarFix) must confirm the rule against the *measured*
token pair, not the plan's named pair.

### F4 — the round-80 C2 counter currently in the build dir is **byte-identical to the r79 draft** (high)

```
$ diff round-79/build/check_allowed_tools.py round-80/build/check_allowed_tools.py
BYTE-IDENTICAL to the r79 draft
sha r79 : 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6
sha r80 : 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6
```

The round-80 plan's frozen predicate requires a **redesigned** counter. The file currently in
`.ufo/waves/round-80/build/` still carries the r79 semantics on every delta the plan names:

| plan §C2 requires | file at `.ufo/waves/round-80/build/check_allowed_tools.py` |
|---|---|
| headline `allowed-tools surfaces documented N of 6` | `:2270` `allowed-tools surfaces backed {n} of {TOTAL}` |
| `generator world: M of 6` | `:2271` `script-only world: {m} of {TOTAL}` |
| exit 0 iff **N == 6** | `:188` `TARGET = 5`; `:2283` `ok = n >= TARGET and …` |
| entry `corpus/knowledge/allowed-tools-surfaces-round80.md` | `:190` `ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"` |

Also: the counter's own self-test passes on this copy —
`python3 -B check_allowed_tools.py --self-test` → `exit=0`,
`self-test: 0 failure(s) over 231 assertions in 80 world(s)`.

**Class:** stale fixture — the round-80 counter build output is the r79 draft, unredesigned.
This is expected mid-wave (the counter seat is still running) and is recorded so the L1
freezes the *redesigned* bytes, not this copy. The freeze receipt's sha256 must be taken from
the final file.

### F5 — the plan's stated base figures for `commit_unresolvable` are the wrong pair (medium)

Already implied by F3, recorded separately because it is a **plan-text** defect rather than a
code defect. The plan (line 10) says:

> `verify_corpus_independent.py` → `unindexed=1` (…round-79-verifier-spotcheck.md),
> `commit_unresolvable=2` (`451a02ff` in the pinned `round-54-verifier-spotcheck.md:147`,
> `cfb894a5` in `round-54.md:13`), exit 1

The `unindexed=1` figure is **confirmed** (measured `unindexed_detail:
['corpus/lessons/round-79-verifier-spotcheck.md']`). The `commit_unresolvable` **count** of 2 is
confirmed, but the **identities** are wrong: those two tokens are in `commit_quoted_detail`
(excluded), and the actual red pair is `7bb48f21…` at `corpus/SOURCES.md:171`/`:172`.

Note the plan also says *"One lives in a `spotcheck-identity`-pinned file and cannot be edited"* —
true of `451a02ff` (in `round-54-verifier-spotcheck.md`, which the tip battery's
`spotcheck-identity` guard pins byte-identically) — but that file is **not** where the red is.
The red is in `corpus/SOURCES.md`, which is append-only and whose S230/S231 rows are
**freshly authored this round** (r79's own rows). So the red pair *is* editable-by-design — but
the corpus is append-only, so the grammar class (not an edit) is the right instrument. The
classification must still target the measured pair.

### F6 — the base `commit_unresolvable` count will not reach 0 by grammar alone if the rule over-matches (medium, risk)

If repair 5 extends the *scanner* to the `owner/repo@<hex>` grammar (rather than only
reclassifying tokens the scanner already finds), it would **create** 16 new unresolvable
citations — every `owner/repo@<hex>` occurrence in the corpus is a third-repo object absent from
both lane and fleet:

```
owner/repo@hex tokens in corpus: 16
  resolvable in lane/fleet: 0
  NOT resolvable        : 16
  NEW-RED if grammar extended: corpus/README.md:5 69ef37e
                             corpus/SOURCES.md:8 a713410a
                             corpus/SOURCES.md:8 69ef37e9424c0a7ea9dd2293b559e43ec8176379
                             corpus/knowledge/skill-eval-artefacts-round70.md:1 69ef37e9… (×2)
                             corpus/lessons/round-52-verifier-spotcheck.md:1 cdf1c200
                             corpus/lessons/round-52-verifier-spotcheck.md:1 7ea98dfc
                             corpus/lessons/round-53.md:3 fd64d648
                             corpus/lessons/round-54-verifier-spotcheck.md:7 451a02ff
                             corpus/lessons/round-54-verifier-spotcheck.md:1 451a02ff
                             corpus/lessons/round-55.md:3 451a02ff
                             corpus/lessons/round-71-verifier-spotcheck.md:1 69ef37e
                             corpus/lessons/round-71.md:1 69ef37e9…
                             corpus/lessons/round-71.md:1 dbd4588f9e1033efb41dad4bef2f7947c8993d44
                             corpus/lessons/round-74.md:1 69ef37e
                             corpus/lessons/round-75-verifier-spotcheck.md:1 dbd4588
```

**Mitigation:** classify only tokens the **existing** scanner already reaches (the
`commit \`<token>\`` grammar — 55 candidates, 46 hex), and mark a candidate external only when
its own row carries the third-party provenance. Under that shape the red pair
(`SOURCES.md:171/172`) is classified external and **no** new red is created.

**Class:** over-matching risk in the repair; the fix is to classify, not to extend the scanner.

### F7 — the integrity gate silently DROPS a new class unless it is registered in two lists (high, trap)

`verifiers/verify_corpus_integrity.py` does **not** return the per-file classifier's dict
wholesale. `corpus_observations()` builds its observed block from **two explicit key lists** and
aggregates with `for key in agg: agg[key] += found[key]` (`:645-660`, `:684-690`):

```python
agg = { "tracked_files": 0, …, "commit_unresolvable": 0, … }   # an EXPLICIT list
details: dict[str, list[str]] = { "report_dead_detail": [], …, "commit_quoted_detail": [] }
…
for key in agg:      agg[key] += found[key]
for key in details:  details[key].extend(found[key])
```

So a class added to `citation_findings()`'s return dict but **not** registered in `agg` (and its
`*_detail` list in `details`) is **silently discarded** — no error, no warning, and the gate
still prints a plausible number. I hit exactly this: my prototype drove
`commit_unresolvable` 2 → 0 while `commit_external` was **absent from `observed.corpus`
entirely** (`commit_external present in integrity observed: False`).

**Measured, after registering the class in both lists:**
```
commit_external = 2
commit_external_detail = ['corpus/SOURCES.md:171: 7bb48f21…', 'corpus/SOURCES.md:172: 7bb48f21…']
commit_unresolvable = 0
```

**The independent gate has no such trap** — `analyse_commits()` returns its dict wholesale, so
its `commit_external` appears in `observed.commits` with no extra registration.

**Class:** silent-observation-loss trap for any new class in the integrity gate. Any repair that
adds a class to only one of the two gates makes the two corpus gates **disagree on a class the
plan says both must count** — the independence the plan relies on.

**Class-check for the reviewer:** after any repair-5 patch, confirm
`observed.corpus.commit_external` is present in the integrity gate's JSON **and** equals the
independent gate's `observed.commits.commit_external`. If the integrity JSON has no such key,
the class was dropped, not absent.

### F8 — the C2 entry's citation was a live third-red hazard; **resolved at source** (medium, closed)

The C2 entry draft published at
`.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md` carried, at line 125:

```
- The mistral-vibe README was served from commit `7bb48f213ac677f943d5c791199ed3dddf302f00`, …
```

Under a line-scope external rule that line has **no** third-party marker at all — the repo is
named only as the bare word "mistral-vibe", with no `owner/repo` token, no `owner/repo@<hex>`
and no `raw.githubusercontent.com` URL **on that line** (measured: all three `False`). Landing
that entry would therefore have **added a third unresolvable** and kept both corpus gates red —
i.e. the entry and the grammar class would have fought each other.

Two independent routes, both verified:

- **The published rule (Y01's `SOURCES_COMMIT_RE`)**, which anchors the marker *before* the
  commit token on the line: for that line the prefix match is `False` → the token stays RED.
- **My line-scope rule**: also `False` → stays RED.

**Resolution: closed at source.** The entry draft was revised at 20:32 and the citation now
reads *"served from the repository head named in that page's fetch record"* — **no commit token
at all**. Verified: `grep -nE 'commit[ \t]+`'` over the current draft returns **no match**, and
with the revised entry committed into the Y01 world the integrity gate reads
`commit_unresolvable = 0`, `commit_external = 2`.

**Class:** cross-seat hazard (entry draft vs counter rule) — worth a coordination note, not a
code defect. **It is closed as of the 20:32 draft revision; I record it because the entry
draft is still a build artefact and may be re-published.**

### F9 — the S230 corpus row cites the WRONG repository's commit (medium, base defect, real)

`corpus/SOURCES.md:171` (the S230 row) reads:

```
… page revision `main` resolved to `badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00` …
```

**That commit is not pi-mono's.** The committed fetch records say otherwise:

```
S230.fetch.json (badlogic/pi-mono):  main at fetch time = bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923
S231.fetch.json (mistralai/mistral-vibe):  main resolved to commit 7bb48f213ac677f943d5c791199ed3dddf302f00
```

So `7bb48f21…` is the **mistral-vibe** head, cited in the **pi-mono** row. The S230 row names
the wrong repository's commit for its own page.

Consequence for the round: the two `commit_unresolvable` tokens are **the same token twice** —
one of them (the S230 row's) is attached to the wrong repo — so a grammar class that
classifies "absent from lane and fleet" as external is classifying the pi-mono row on the
strength of a mistral-vibe commit id. **The class still correctly clears the red** (the token is
absent from both repos either way), but the SOURCES.md row itself is defective.

**This is a corpus row in the append-only corpus**, outside every write scope in this round
(plan §Frontier: *"Files not authored by this lane … are never edited"*; the frontier step
forbids editing that anchor cell this round). **It belongs in the round-80 lesson as an
erratum line** — the lesson's `## Mistakes` or `## Gate` should name it. Seat
`Kb80E08C2Entry` raised it independently; I verified it from the committed fetch records.

**Class:** base defect in a corpus anchor cell, correctly classified by the external-commit
class, but the underlying citation is wrong and must be recorded as an erratum rather than
silently inherited.

### F10 — the C2 counter's Q70 quote rule **misfires on the msaf page**: no admissible quote exists (high, C2-blocking)

The r79 draft counter rejects a quote that "lies in the first-heading block" by finding the
page's first heading with a **`#`-prefix line scan** (`check_allowed_tools.py:893`):

```python
first_head = next((i for i, l in enumerate(lines) if l.startswith("#")), None)
…
if first_head is not None and idx <= first_head + 1:
    return False, "quote lies in the first-heading block (Q70)"
```

On an **HTML** page read as a text view, a line can start with `#` because it is a **Python
comment inside a code sample**, not a heading. Measured on the committed
`.ufo/waves/round-79/snapshots/S229-msaf.html`:

```
raw occurrences of 'allowed-tools'      : 1   (raw line 818, a <td><code> cell)
text-view occurrences                   : 1   (view line 78)
raw '#'-prefix lines                     : raw 910  '# Auto-approve load_skill and read_skill_resource…'
                                          raw 1058 '# Discover skills from the 'skills' directory'
raw <h1>                                : raw 676  'Agent Skills'
counter's first_head (view line 151)     : '# Auto-approve load_skill and read_skill_resource…'  <-- a PYTHON COMMENT
the REAL h1 'Agent Skills' (view line 22)
the only quote occurrence (view line 78)
Q70 test: 78 <= 151+1  ->  True  ->  REJECTED
```

The page's real `<h1>` is at view line 22; the heuristic picks view line 151, a Python comment
in a code sample, and then rejects the quote for being "before" it — when the quote is
**after** the real heading. **No admissible msaf quote exists under this rule**, so conjunct (c)
for S229 cannot be satisfied and the counter cannot reach `6 of 6` no matter how the entry is
written.

This is **structural, not a quote choice** — seat `Kb80E08C2Entry` states it independently and
correctly, and I verified it from the committed snapshot bytes. The counter seat owns the fix
(e.g. detect the first heading from the page's heading structure rather than a `#`-prefix scan,
or apply the Q70 first-heading rule to *markdown* pages only). **I am not repairing it** — the
counter is not my artefact — but it must be on the C2 critical-path list, because a perfect
entry plus a perfect manifest still yields 5 of 6.

**Class:** counter defect (a rule misfiring on an HTML text view), load-bearing for C2.

---

## 7. Adjacent facts measured for the wave (no scoring done)

These are observations, not claims. No after-value was measured; no world was scored.

- **E04 patch applies cleanly to base** and is load-bearing:
  ```
  $ git -C "$S/clone2" apply --check .ufo/waves/round-80/build/Kb80E04DeadPointer.patch
  E04 APPLIES CLEANLY to base
  $ git diff --numstat -- verifiers/verify_corpus_integrity.py
  17  0
  $ git rev-parse HEAD:verifiers/verify_corpus_integrity.py
  051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f      ← equals Kb80E04DeadPointer.blob
  ```
  With E04 applied (plus the coverage row), the integrity gate's `report_dead` goes **1 → 0**
  and `unindexed` **1 → 0**; `commit_unresolvable` stays **2** (the F3 pair) — i.e. repairs 3+4
  are load-bearing and repair 5 is still needed, exactly as the plan's W3 control predicts.

- **Instrument-size budget** — **CORRECTED after further measurement; my first reading was wrong.**
  At base the six battery instruments already carry `added=22 deleted=3` against the pinned
  base `072048fa8e8a52c707d25f7079772fa317244eb7` (measured `git diff --numstat`); E04 adds
  **+17**. That gives `22 + 17 = 39`, leaving `60 − 39 = 21` lines for the grammar class across
  **both** corpus gates — the plan's arithmetic.
  **The budget IS reachable, and the class that reaches it is published.** Seat
  Kb80Y01Simplify's world (`019f27ab199ad79f488fb388a0abe8f7fe1ca0ba`, includes E04) measures
  `added=59 deleted=10` over the pinned base — i.e. **repair 5 costs 20 lines of the 21
  budgeted** — and its tip battery reads `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0
  (`.ufo/waves/round-80/build/Kb80Y01-tipbattery-early-dot.txt`, `-narrow-dot.txt`).
  **I must retract my earlier reading.** My own prototype measured **69 added**, over the cap —
  but that was **an over-built prototype, not a floor**: I wrote the rule with a separate
  `EXTERNAL_HOST_RE` constant, a separate `external` list per gate, and two `*_detail` output
  keys, and I registered the class in the integrity gate's `agg` **and** `details` lists.
  Y01's implementation is materially leaner (one regex constant, the class folded into the
  existing branch, one output key) and lands at 59. **The correct finding is: the cap arithmetic
  holds with 1 line of slack, and the plan's kill rule does NOT fire.** My 69 was a measurement
  of my own implementation, and I generalised it into a claim about the budget that the
  published counter contradicts. The retraction is recorded here deliberately.
  The only budget caveat that survives: **1 line of slack**. Any further growth in the six
  instruments (including the new `verifiers/check_allowed_tools.py`, if it is ever added to the
  battery's instrument list) trips `instrument-size`.

- **Instrument pins at base** — every base blob is already a pinned blob, so the base is
  `instrument-pin PASS` (confirmed by the base receipt `guards 5 of 5`):
  ```
  check_gate_registry.py     95ffed38…  (pinned)
  check_assertion_floors.py  9cb860bd…  (pinned)
  verify_skill_checklist.py  6aab1684…  (pinned)
  verify_corpus_integrity.py e470eaaa…  (pinned)
  verify_corpus_independent.py edac0df7… (pinned)
  check_correction_sweep.py  c94b771f…  (pinned)
  ```
  E5's `INSTRUMENT_PINS` must gain the two **new** instrument blobs, since the guard requires the
  measured blob to be *one of* the pinned set.
  **Pin-ordering correction (L1 Addendum 1, commit `308bff9`, seat Kb80E06CounterErratum):** the
  integrity pin is the **E04∘E05 composed blob**, *not* the E04-only blob `051b8c5f…` — that value
  is the E04-only cross-check, cited as such wherever it appears. (My earlier note named
  `051b8c5f…` as the integrity pin; that was wrong, and the L1's clarification supersedes it.)
  The E5 amendment is exactly three things: `LINE_CAP = 40` → `60`; `INSTRUMENT_PINS` gains the
  composed E04∘E05 integrity blob and the E05 independent blob (two entries); and the counter's
  **self-test fixture constants** that hard-assert the old bound (the 41-line growth
  expectation, the 60-line loss expectation, the cap mentions) are re-anchored to derive from
  `LINE_CAP`, arm semantics unchanged. The plan's own note: as literally worded ("LINE_CAP and
  the pin table, nothing else"), E5 falsified the counter's own self-test.
  **My own measurement bears this out:** the counter's self-test hard-anchors
  `"FAIL guard instrument-size: instruments gain 41 lines > 40"`, so a `LINE_CAP` change without
  re-anchoring that string makes the self-test fail on its own fixture. Any E5 counter must
  re-derive those expectations from `LINE_CAP`, not only change the constant.
  **Measured:** a copy of the counter with **only** `LINE_CAP = 40` → `60` changed, run as
  `--self-test`, gives **`self-test: 4 failure(s) over 69 assertions`**:
  ```
  FAIL size world exits 1: exit 0
  FAIL size world names the instrument-size guard
  FAIL stub world exits 1: exit 0
  FAIL stub world fails the deletion side of the size cap
  ```
  The two hard-anchored strings are at `check_tip_battery.py:522`
  (`"…instruments gain 41 lines > 40"`) and `:559`
  (`"…instruments lose 60 lines > 40"`). Under `LINE_CAP = 60` the growth arm must become
  61 and the loss arm 61 for the arms to keep their semantics — i.e. the fixture constants must
  be re-derived from `LINE_CAP`, exactly as the L1's Addendum 1 §3 states. **This is the
  operative detail for whoever writes the E5 counter: a constant-only change is not enough,
  and the failure is invisible unless you actually run the counter's own `--self-test`.**

- **The refresh script's `--carry` semantics interact with the plan.** The plan's C1 repair 3
  says *"every zero class must read 0 after repairs 4+5"* with `--carry` none. Measured: at base
  the script **refuses** (exit 2) on `corpus.index.unindexed` — the coverage-map row must land
  first — and after E04 it still refuses on `corpus.pointers.commit_unresolvable` unless that
  class is carried. So the plan's "refresh with `--carry` none" is only reachable **after**
  repair 5 lands. Order matters: index rows → E04 → grammar → refresh.

- **Registry gate at base**: `python3 -B verifiers/check_gate_registry.py --rev 398cbe1…` →
  `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1. The two offenders
  are exactly the two the registry repair targets: `verifiers/check_desc_craft.py` and
  `verifiers/check_r75_routed_repairs.py` ("no registry rows naming it: 0 (need 1)"). A new
  `verifiers/check_allowed_tools.py` will be a **63rd** verifier and will need its own row.

### Status of my findings against the lane as it now stands (checked after the L1's commits)

The lane advanced while this seat worked (`c2f69d4` → `308bff9` → `a481913`). I re-read the
current bytes; here is which of my findings the L1 has already addressed:

| finding | status at `a481913` |
|---|---|
| **F3/F5** (plan names the wrong tokens) | **ADDRESSED.** `a481913` ("correct base unresolvable citation locators before claim data") amends `plans/round-80.md` §Trigger with an explicit correction naming `corpus/SOURCES.md:171-172` and the S230/S231 `badlogic/pi-mono` resolution, citing Kb80V03Instruments' primary-byte audit. The plan text now matches what both gates measure. |
| **E5 self-test anchoring** | **ADDRESSED.** `308bff9` (Addendum 1) states E5's third element — re-anchor the self-test fixture constants to derive from `LINE_CAP`. My measurement above confirms this is necessary, not optional. |
| **F2** (`MANIFEST.sha256` absent) | **STILL OPEN.** `git ls-files .ufo/waves/round-79/snapshots/` at `a481913` still lists only the six per-S `.manifest` files — no aggregate `MANIFEST.sha256`. The C2 counter still cannot evaluate conjunct (c). |
| **F9** (S230 row cites the wrong repo's commit) | **STILL OPEN in the corpus** (as expected: the frontier step forbids editing that anchor cell this round). `corpus/SOURCES.md:171` still reads "resolved to `badlogic/pi-mono` commit `7bb48f21…`". The L1's `a481913` corrects the **plan's description** of the token; it does not correct the **row**, which needs the lesson erratum line. |
| **F7** (integrity gate drops an unregistered class) | **STILL OPEN** — inherent to the integrity gate's design; it bites whoever writes the grammar class. |
| **F10** (msaf Q70 misfire) | **STILL OPEN** — the counter's rule, on the counter seat. |
| **F4** (round-80 counter build output is the r79 draft) | **STILL OPEN** as of this writing. |
| **F8** (entry's third-red citation) | **CLOSED at source** by the entry author's 20:32 revision; the current draft carries no commit-shaped citation. |

**F9's status is the one that needs a decision.** The plan's Trigger paragraph now *describes*
the token correctly, but the corpus **row** still attributes the mistral-vibe commit to
pi-mono. If that row is left as-is, the round's lesson inherits a known-wrong citation anchor
that no gate can catch (the token is absent from lane and fleet either way, so the external
class clears it). The erratum line in `corpus/lessons/round-80.md` is the right instrument, per
the frontier step.

---

## 8. What I did NOT do

- I did not write, edit or patch any file under `verifiers/`, `corpus/`, `SKILL.md`, `PROVINCE.md`
  or the lane tree. The L1 integrates; only the L1 commits.
- I did not measure or score any claim's after-value, and I did not build or run any control or
  shortcut world. Scoring is the L1's and the round-80 reviewer's.
- I did not run the tip battery to produce a **claim** value. I DID run it twice on my own
  scratch prototype worlds, as a **hygiene/guard measurement** of my own patch (never as a
  score of the round's claim): on the over-built prototype it read
  `instruments added 66 … FAIL guard instrument-size` / `guards 3 of 5; tip battery exit 0: 1 of 6`,
  and with the E5-amended counter (LINE_CAP 60 + the two measured pin blobs) it read
  `instruments added 69 … FAIL guard instrument-size: instruments gain 69 lines > 60` /
  `guards 4 of 5; tip battery exit 0: 1 of 6`. Both were **my** worlds, not the round's; the
  published C1 stack value belongs to the battery seat, and Y01's own world already measures
  `guards 5 of 5; tip battery exit 0: 6 of 6` (exit 0). I have published no after-value.
- I did not fetch any URL. No network call was made by me during this seat.

## 9. Tooling

No tool was installed, upgraded or removed by this seat. The sweep used only pre-existing
software: `python3` (3.x, stdlib `tokenize`/`hashlib`/`json`/`subprocess`), `git`, `grep`,
`sha256sum`, `find`, `diff`. `pacman` was not run (host-wide paused by directive).

## 10. Coordination

- Sent `Kb80E10Battery` a note that this seat ships no patches (so the C1 stack assembly is not
  waiting on me), plus the two measurements that bear directly on world assembly: the refresh
  script's refusal order (index row first) and the F3 token-identity mismatch.
- Sent `Kb80E07C2Counter` the F2 missing-manifest finding (with the verified concatenation fix)
  and F4 (the round-80 counter build output is still the r79 draft, byte-identical, sha
  `74e067cc…`).
- Sent `Kb80E05GrammarFix` the F3 token-identity finding, the F6 over-match risk, the size
  budget, and the pin requirement.
- Sent `Kb80V03Instruments` a measured reference implementation of the grammar class (both
  gates, self-test receipts, numstat) after they asked for it, plus the F7 agg/details trap.
- Sent `Kb80E10Battery` a second note after they flagged the C2-entry third-red hazard: I
  **confirmed** it by measurement (the hazard line matches no external marker under either
  rule) and confirmed it was **resolved at source** by the entry author's 20:32 revision.
- **F2, F3, F4 are addressed to the seats that own them** and are not a blocker for this seat's
  own deliverable. Flagging here for the L1: F2 (missing `MANIFEST.sha256`) and F4 (the
  round-80 counter build output is still the r79 draft) are both on the C2 critical path.

---

Report: `.ufo/waves/round-80/w1/Kb80E13FixtureGuard.md`
Build note: `.ufo/waves/round-80/build/Kb80E13FixtureGuard.md`

VERDICT: Hygiene is clean where it must be — zero pacman, zero /tmp roots that ignore TMPDIR, every network call behind an opt-in `--fetch` (the six battery gates have zero network hits), every git/jj mutation confined to a TMPDIR sandbox, and the refresh script's two claims verified empirically (exactly one path written, symlinks refused, exit 2, target digest unchanged); six defects recorded, four on the C2 critical path — the counter's snapshot manifest `.ufo/waves/round-79/snapshots/MANIFEST.sha256` exists neither in the tree nor in any commit (conjunct (c) cannot be evaluated, exit 2; the six per-S `.manifest` files are correct and a verified concatenation fixes it), the counter's Q70 '#'-prefix first-heading heuristic misfires on the msaf HTML page so NO admissible quote exists for S229 (a perfect entry plus a perfect manifest still yields 5 of 6), the integrity gate silently DROPS any new observed class not registered in both its `agg` and `details` key lists, and the round-80 counter build output is still byte-identical to the r79 draft — plus the base corpus defect that `corpus/SOURCES.md:171` attributes the mistral-vibe commit to the pi-mono row (the L1 has corrected the plan's description of the token but not the row, which needs the lesson erratum line); my first budget reading (69 added, over cap) is RETRACTED — the published class lands at 59 with E04 included (repair 5 = 20 of 21 budgeted lines) and its world reads `guards 5 of 5; tip battery exit 0: 6 of 6` — and the E5 counter must re-anchor its self-test fixture constants, since a constant-only `LINE_CAP` change yields `4 failure(s) over 69 assertions`.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E13FixtureGuard.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E13FixtureGuard.md
