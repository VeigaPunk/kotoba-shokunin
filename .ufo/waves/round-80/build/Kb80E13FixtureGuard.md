# Kb80E13FixtureGuard — build note (round 80, wave w1)

Machine-readable companion to `.ufo/waves/round-80/w1/Kb80E13FixtureGuard.md`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Scratch (removed): `/fast/scratch/hyaku/kotoba-r80/Kb80E13FixtureGuard/`.

## Hygiene sweep — class counts

Scope: `verifiers/` (60 files) + `.ufo/waves/round-80/build/` (*.py, *.sh).
Scanner: `scan.py` (tokenize-based; comments/docstrings excluded from code-level classes).

```
T1  7   hardcoded /tmp root        → 0 real (7 fixture-string hits, all listed in the report)
P   0   pacman invocation          → 0
N  65   network call                → 0 in the measured path (all behind --fetch)
G 184   git/jj mutation             → 0 outside a sandbox (all in TMPDIR dirs)
total 256 findings, all triaged; 3 defects reported (F1, F2, F3/F5/F6)
```

### The 7 `T1` hits — all benign

```
verifiers/check_agentdef_boxes.py:1559        fixture string "delegated:/tmp/verify_agentdef.py"
verifiers/check_spec_craft.py:1766            fixture arg repo_arg="/tmp" (self-test, expects exit 2)
verifiers/verify_corpus_independent.py:791    fixture expected-output literal
verifiers/verify_corpus_integrity.py:1189     fixture unit assertion token_path_class("/tmp/x/")
verifiers/verify_corpus_integrity.py:1197     fixture table row
verifiers/verify_corpus_integrity.py:1212     fixture expected-output literal
```

Shell runner: `verifiers/fault_injection_corpus.sh:53` → `WORLDS=${TMPDIR:-/tmp}/round12-faults.$$` (TMPDIR-first).

### The 15 network-capable verifiers — every one gated on `--fetch`

```
check_agent_definitions.py:766      check_client_trust_gates.py:272    check_command_files.py:916
check_description_thresholds.py:262  check_explicit_invocation.py:359   check_hook_files.py:1059-1087
check_mcp_instructions.py:221        check_overlap_levers.py:496        check_plugin_manifests.py:877
check_scoped_rules.py:1495-1528      check_scoped_rules_v31.py:1552-1585
check_scoped_rules_v32.py:1648-1681  check_skill_evals.py:185          check_skill_evals_v2.py:333
check_skill_precedence.py:276
```
Each has exactly one `add_argument("--fetch", action="store_true")` and its `urlopen`/`curl`
call site is under `if args.fetch:`.

### The six battery gates + the battery itself — zero network hits

```
check_gate_registry.py 0   check_assertion_floors.py 0   verify_skill_checklist.py 0
verify_corpus_integrity.py 0  verify_corpus_independent.py 0  check_correction_sweep.py 0
check_tip_battery.py 0
```

### Git writes — repository argument traced for every site

All writes take `-C <tempdir>` / `cwd=<tempdir>`; the `root`/`repo` argument is a
`tempfile.mkdtemp`/`TemporaryDirectory` path in every case. No write targets LANE/REPO.
`jj` is invoked nowhere (`check_report_pointers.py:153` is a prose vocabulary list).

## Refresh-script verification (r79 draft, `.ufo/waves/round-79/build/refresh-corpus-baseline.py`)

### Claim A — "Writes exactly one path"

```
$ python3 -B …/refresh-corpus-baseline.py --repo "$S/clone2" \
      --carry corpus.pointers.report_dead --carry corpus.pointers.commit_unresolvable
exit=0
corpus.index.tracked_files         144 -> 152
corpus.pointers.report_total       99 -> 109
corpus.pointers.commit_total       43 -> 46
wrote …/clone2/verifiers/corpus-baseline.json (head 6941d37 …)
post-refresh: 7/9 checks pass, exit 1, drift: corpus.pointers.report_dead, corpus.pointers.commit_unresolvable

$ git -C "$S/clone2" status --porcelain --untracked-files=all
 M verifiers/corpus-baseline.json
$ git -C "$S/clone2" diff --stat
 verifiers/corpus-baseline.json | 17 +++++++++--------
 1 file changed, 9 insertions(+), 8 deletions(-)
```
**Exactly one path. CONFIRMED.** Gate JSON docs go to `$TMPDIR` and are unlinked in `finally`.

### Claim B — "never through a symlink"

```
$ ln -s <outside> clone2/verifiers/corpus-baseline.json && git add -A && git commit
$ python3 -B …/refresh-corpus-baseline.py --repo "$S/clone2" --carry …
refresh-corpus-baseline: refused: verifiers/corpus-baseline.json is a symlink; refusing to write through it
exit=2
$ sha256sum <symlink target>  → 22d5f0bb6458abd63592f57e2230ea989860350f8b4b0723332ef743453374d7  (unchanged)
$ ls -l clone2/verifiers/corpus-baseline.json → still a symlink
```
**Refuses. CONFIRMED** (code: `refresh-corpus-baseline.py:258-260`).

### Fail-closed behaviours also observed

| condition | script output | exit |
|---|---|---|
| dirty tree | `refused: dirty tree: the gate reads worktree bytes while the baseline is recorded at HEAD` | 2 |
| unindexed corpus file | `refused: zero-mode corpus.index.unindexed observed 1, not 0` | 2 |
| `--carry corpus.index.unindexed` | `refused: --carry …: an index class is never carried` | 2 |
| symlinked baseline | `refused: verifiers/corpus-baseline.json is a symlink` | 2 |

## F2 — missing C2 fixture: `.ufo/waves/round-79/snapshots/MANIFEST.sha256`

```
$ find .ufo/waves/round-79 -name 'MANIFEST*'                          → (nothing)
$ git log --all --oneline -- '.ufo/waves/round-79/snapshots/MANIFEST.sha256' → (nothing)
$ git ls-files .ufo/waves/round-79/snapshots/ | wc -l                 → 18  (6 × snapshot/.fetch.json/.manifest)
```

Counter side (`.ufo/waves/round-79/build/check_allowed_tools.py:191-192`):
`SNAPDIR = ".ufo/waves/round-79/snapshots"` · `MANIFEST = SNAPDIR + "/MANIFEST.sha256"`.

```
Repo.manifest() → EXC EnvError no manifest at .ufo/waves/round-79/snapshots/MANIFEST.sha256 at 398cbe1…:
                 the snapshots are unpinned, so (c) cannot be evaluated      → exit 2
```

Per-S manifests ARE committed and CORRECT (6/6 match the snapshot bytes and the fetch records):

```
OK   S226.manifest -> S226-spec.md        9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16
OK   S227.manifest -> S227-claude.md      31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9
OK   S228.manifest -> S228-factory.md     81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9
OK   S229.manifest -> S229-msaf.html      34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2
OK   S230.manifest -> S230-pi.md          5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5
OK   S231.manifest -> S231-vibe.md        fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0
```

Constructive fix VERIFIED in the scratch clone — `cat *.manifest > MANIFEST.sha256` then:

```
manifest() -> {'S226-spec.md': '9a67de89…', 'S227-claude.md': '31623035…', 'S228-factory.md': '81409d89…',
               'S229-msaf.html': '34016233…', 'S230-pi.md': '5b980552…', 'S231-vibe.md': 'fc48a5db…'}
S226..S231 snapshot_name() each resolve unambiguously to their own snapshot.
```

## F3 — plan's grammar class is a no-op on the measured red pair

Both corpus gates, pristine clone at base:

```
verify_corpus_integrity.py   --no-baseline --json
  commit_unresolvable_detail: corpus/SOURCES.md:171: 7bb48f213ac677f943d5c791199ed3dddf302f00
                               corpus/SOURCES.md:172: 7bb48f213ac677f943d5c791199ed3dddf302f00
verify_corpus_independent.py --repo <clone> --json
  commit_unresolvable_detail: same pair
  commit_quoted_detail:      … round-54-verifier-spotcheck.md:147: 451a02ff,
                                 round-53.md:44: cfb894a5, round-54.md:13: cfb894a5 …   (EXCLUDED)
```

`7bb48f21…` in neither lane nor fleet: `git -C <lane> cat-file -t 7bb48f21…` → `fatal: git cat-file: could not get object info`; fleet root same.

Applying the plan's rule literally (hex token in `owner/repo@<hex>` grammar):

```
commit-tokens the PLAN rule would call external: 0
commit-tokens the PLAN rule would NOT call external: 50
  → corpus/SOURCES.md:171 7bb48f21…  STILL RED
  → corpus/SOURCES.md:172 7bb48f21…  STILL RED
```
The S230/S231 rows read `` `badlogic/pi-mono` commit `7bb48f21…` `` — backticked owner/repo then
the word "commit", NOT `owner/repo@<hex>` adjacency:
`owner/repo@hex present anywhere in the line = False`.
A third-party-host rule catches both (`raw.githubusercontent.com/badlogic/pi-mono`,
`raw.githubusercontent.com/mistralai/mistral-vibe`).

## F6 — over-match risk if the scanner is EXTENDED to `owner/repo@<hex>`

```
owner/repo@hex tokens in corpus: 16   resolvable in lane/fleet: 0   NOT resolvable: 16
```
Extending the scanner would create 16 new unresolvable citations (README.md:5, SOURCES.md:8 ×2,
skill-eval-artefacts-round70.md:1 ×2, round-52 ×2, round-53.md:3, round-54 ×2, round-55.md:3,
round-71 ×2, round-71-verifier-spotcheck.md:1, round-74.md:1, round-75-verifier-spotcheck.md:1).
**Classify, do not extend.**

## F4 — round-80 counter build output is still the r79 draft

```
$ diff round-79/build/check_allowed_tools.py round-80/build/check_allowed_tools.py
BYTE-IDENTICAL to the r79 draft
sha (both) 74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6
```
Still carries r79 semantics: `:2270` "backed" (plan wants "documented"), `:2271` "script-only
world" (plan wants "generator world"), `:188` `TARGET = 5` (plan wants N==6), `:190`
`ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"` (plan wants round80).
Self-test on the copy: `exit=0`, `self-test: 0 failure(s) over 231 assertions in 80 world(s)`.

## Adjacent measurements (no scoring done)

- **E04 applies and is load-bearing**: `git apply --check` OK at base; `17  0` numstat; resulting
  blob `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` == `Kb80E04DeadPointer.blob`.
  With E04 + coverage row: integrity `report_dead` 1->0, `unindexed` 1->0, `commit_unresolvable`
  stays 2.
- **Instrument-size budget — CORRECTED (my first reading was wrong).** Base spend at 398cbe1 is
  `added=22 deleted=3` (all in check_assertion_floors.py); E04 adds +17; that leaves
  `60 - 39 = 21` lines for the grammar class across BOTH corpus gates.
  **The budget is REACHABLE.** Seat Kb80Y01Simplify's world `019f27ab199ad79f488fb388a0abe8f7fe1ca0ba`
  (includes E04) measures `added=59 deleted=10` over the pinned base `072048fa` — i.e. repair 5
  costs **20 of the 21 budgeted lines** — and its tip battery reads
  `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0
  (`Kb80Y01-tipbattery-early-dot.txt`, `Kb80Y01-tipbattery-narrow-dot.txt`).
  **My own prototype measured 69 added (over cap) — RETRACTED.** That was an over-built
  prototype (separate regex constant, separate list per gate, two *_detail output keys, plus
  registering the class in the integrity gate's agg AND details lists), not a floor. The
  published class is materially leaner. The plan's kill rule does NOT fire; **1 line of slack
  remains**.
- **My reference artefact (published, labelled, NOT a lane patch)**:
  `.ufo/waves/round-80/build/Kb80E13FixtureGuard-REFERENCE-grammar-class.md` and
  `…-REFERENCE-grammar-class.diff`. Verified: the diff applies CLEANLY to a fresh base clone and
  yields `commit_unresolvable = 0`, `commit_external = 2`.
- **Instrument pins at base** (all six already pinned => base `instrument-pin PASS`):
  `95ffed38… / 9cb860bd… / 6aab1684… / e470eaaa… / edac0df7… / c94b771f…`
- **Registry at base**: `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1;
  offenders `verifiers/check_desc_craft.py`, `verifiers/check_r75_routed_repairs.py`
  ("no registry rows naming it: 0 (need 1)"). A new `verifiers/check_allowed_tools.py` is the
  63rd verifier and needs its own SKILL.md registry row.
- **Refresh ordering**: index row -> E04 -> grammar -> refresh (the refresh refuses before the
  grammar repair lands).

## F7 — the integrity gate SILENTLY DROPS a new observed class

`verifiers/verify_corpus_integrity.py` builds its observed block from TWO explicit key lists
(`agg` at ~:645, `details` at ~:659) and aggregates with `for key in agg: agg[key] += found[key]`.
A class added to `citation_findings()`'s return dict but not registered in `agg` (and its
`*_detail` list in `details`) is **discarded with no error**. Measured on my prototype:
`commit_unresolvable` 2 -> 0 while `commit_external` was **absent from `observed.corpus`**
(`commit_external present in integrity observed: False`). After registering in both lists:
`commit_external = 2`, `commit_external_detail = [SOURCES.md:171, SOURCES.md:172]`.
The **independent** gate returns its dict wholesale and needs no such registration.
REVIEWER CHECK: after any repair-5 patch, confirm `observed.corpus.commit_external` is PRESENT
in the integrity JSON and EQUALS the independent gate's `observed.commits.commit_external`.

## F9 — the S230 corpus row cites the wrong repository's commit

`corpus/SOURCES.md:171` (S230 row): "resolved to `badlogic/pi-mono` commit `7bb48f21…`".
But the committed fetch records say:
  S230.fetch.json (badlogic/pi-mono):        main at fetch time = bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923
  S231.fetch.json (mistralai/mistral-vibe):  main resolved to commit 7bb48f213ac677f943d5c791199ed3dddf302f00
`7bb48f21…` is the MISTRAL-VIBE head, cited in the PI-MONO row. The two unresolvable tokens
are therefore the SAME token twice, one attached to the wrong repo. The external class still
clears the red (absent from both repos either way), but the corpus row is defective and belongs
in the round-80 lesson as an erratum line (the frontier step forbids editing that anchor cell
this round).

## F10 — the C2 counter's Q70 quote rule misfires on the msaf page (C2-blocking)

`check_allowed_tools.py:893` finds the first heading with a `#`-prefix line scan. On an HTML
page read as a text view, a `#`-prefix line can be a PYTHON COMMENT inside a code sample.
Measured on the committed S229-msaf.html:
  raw 'allowed-tools' occurrences      : 1 (raw line 818, a <td><code> cell)
  text-view occurrences                : 1 (view line 78)
  raw '#'-prefix lines                  : raw 910 '# Auto-approve load_skill and read_skill_resource…'
                                          raw 1058 "# Discover skills from the 'skills' directory"
  raw <h1>                              : raw 676 'Agent Skills'
  counter's first_head (view line 151)  : '# Auto-approve load_skill…'   <-- a PYTHON COMMENT
  the REAL h1 'Agent Skills' (view line 22)
  Q70 test: 78 <= 151+1 -> True -> REJECTED
The real <h1> is at view line 22; the heuristic picks 151 and rejects the quote for being
"before" it, when the quote is AFTER the real heading. **No admissible msaf quote exists under
this rule** => conjunct (c) for S229 cannot be satisfied => the counter cannot reach 6 of 6
however the entry is written. Structural, not a quote choice; the counter seat owns the fix.
Raised independently by Kb80E08C2Entry; verified here from the committed snapshot bytes.

## Tooling

Nothing installed, upgraded or removed. Only pre-existing `python3` (stdlib), `git`, `grep`,
`sha256sum`, `find`, `diff`. `pacman` not run (host-wide paused by directive). No URL fetched
by this seat.

VERDICT: Hygiene clean (0 pacman, 0 /tmp roots ignoring TMPDIR, all network behind an opt-in --fetch with the six battery gates network-free, all git/jj mutations sandboxed); refresh script's two claims verified empirically (one path, symlink refused, exit 2); six defects recorded, four C2-critical (the snapshot MANIFEST.sha256 absent from the tree and from all history; the msaf Q70 '#'-prefix heading misfire that leaves NO admissible S229 quote so 6 of 6 is unreachable whatever the entry says; the plan's owner/repo@<hex> class a measured no-op against the pair the gates actually report red; the integrity gate's silent drop of an unregistered new observed class), one base corpus defect (SOURCES.md:171 attributes the mistral-vibe commit to the pi-mono row — the L1 corrected the plan's description, the row still needs the lesson erratum line), one closed (the entry's third-red citation, resolved at source); my first budget reading (69 added, over cap) RETRACTED — the published class lands at 59 with E04 included (repair 5 = 20 of 21 budgeted) and reads guards 5 of 5 / tip battery exit 0: 6 of 6; and the E5 counter must re-anchor its self-test fixture constants (a constant-only LINE_CAP change gives 4 failures over 69 assertions).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E13FixtureGuard.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E13FixtureGuard.md
