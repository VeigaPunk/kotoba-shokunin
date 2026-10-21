verdict: PARTIAL — OC-5's per-anchor kill probes all hold (each single-anchor removal/corruption exits 1 naming OC-5; equivalent rename fails closed as designed), but three structural mutants survive exit 0, so the rule witnesses token presence only, not the switch's polarity, branch binding, or locality.

Attacked: `verifiers/verify_surfaces.py` rule OC-5 at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f, mutation-probed against the real frozen opencode dump.

## Setup

- Scratch clone at 7ad7fad (detached, `git log -1` = `7ad7fad round-47: C1 re-derive+re-pin …`), clone path `/fast/scratch/kotoba-r47/w2/W2DropOC5-2/kotoba-shokunin`. Frozen substrate digest-verified: `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → exit 0, all four (`bin/omp-18.12.5`, `bin/opencode-1.19.3`, `omp-18.12.5.strings`, `opencode-1.19.3.strings`) OK.
- Baseline: `python3 verifiers/verify_surfaces.py --opencode-strings mut/pristine.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` → exit 0.
- Anchor map of the real dump (67,839,091 bytes, `strings -n 4`): the OC-5 switch lives on dump line 443993 (verifier comment names the same line, verify_surfaces.py:402-405):
  - `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp(T,d.directory,d.worktree).pipe(s.catch(()=>s.succeed([])));return yield*e.globUp(T,r.config,r.config).pipe(...)` — byte offsets 10893368–10893560.
  - `globUp(T,d.directory,d.worktree)` occurs exactly 1× and `globUp(T,r.config,r.config)` exactly 1× in the whole dump (the other 3 `globUp` hits are `FileSystem.globUp` export/definition at dump lines 447041/447206 and match neither regex).
  - `OPENCODE_DISABLE_PROJECT_CONFIG` occurs 9× on dump lines 442392 (TUI loader), 443993 ×2 (the switch + a `findUp` loader), 445482 (OC-6 region), 446350 (docs escape-hatch text), 446380, 446403, 447235 ×2.
- Rule under test: verifiers/verify_surfaces.py:406-408 (anchors), :485-492 (rule call, `owns=[]`), :440-445 (`rule()` sets `missing` = all anchors when unmatched), :748-754 (FAIL line formatting), :1041-1048 (self-test expects the shipped drop-oc5 fixture to exit 1 naming `OC-5`).

## Kill probes (each anchor removed/corrupted one at a time) — all hold

Runner (each mutant = byte replacement on a copy of the pristine dump, then the full verifier): `python3 verifiers/verify_surfaces.py --opencode-strings mut/<mutant>.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`.

| mutant | change | exit | opencode_extract |
|---|---|---|---|
| M1_env_removed_all | all 9 `OPENCODE_DISABLE_PROJECT_CONFIG` → removed | 1 | FAIL names OC-5 |
| M2_globup_project_corr | `globUp(T,d.directory,d.worktree)` → `globUp(T,d.directory,d.worktreX)` (unique occurrence) | 1 | FAIL names OC-5 |
| M3_globup_config_corr | `globUp(T,r.config,r.config)` → `globUp(T,r.config,r.cfg)` (unique occurrence) | 1 | FAIL names OC-5 |
| M4_rename_globUp_walkUp | renamed-but-equivalent: `globUp` → `walkUp` everywhere (pure identifier rename, 5 sites) | 1 | FAIL names OC-5 |

FAIL line for every killing mutant (identical text; exit 1):

```
FAIL surfaces.opencode_extract: rule(s) matched nothing: OC-5 (owns no class id (shape witness); missing OPENCODE_DISABLE_PROJECT_CONFIG + globUp(<v>.directory,<v>.worktree) + globUp(<v>.config,<v>.config))
```

So the acceptance "exit 1 with surfaces.opencode_extract naming the owned class(es) or the rule" is met: OC-5 owns no classes (verify_surfaces.py:485-492, `owns=[]`), and the FAIL names the rule itself via the unmatched-rule branch at :748-754. The only imprecision is cosmetic: `missing` lists all three anchors even when one was corrupted (`rule()` at :441 sets `missing = list(anchors)` wholesale), so the FAIL line does not say which anchor died.

Renamed-but-equivalent verdict: M4 goes red on a semantically equivalent rename, i.e. the rule is identifier-brittle and in that sense too narrow. This is the documented contract, not a defect: the rule's own comment says it "witnesses the path … so losing it is a drift FAIL rather than a silent re-scope" (verify_surfaces.py:485-486), and a renamed `globUp` in a future bundle means the pinned shape drifted — the gate fails closed, which is the safe direction for a version pin. Caveat: `globUp` is also opencode's exported `FileSystem.globUp` API name (dump line 447206), so a real upstream rename would be a genuine interface change, not purely cosmetic.

Calibration against the shipped fixture: `verifiers/fixtures/surfaces/strings-opencode-drop-oc5.txt` drops the whole OC-5 block (both globUp lines + env ref; diff vs `strings-opencode-clean.txt` confirms) and exits 1 naming OC-5 (re-run: exit 1, same FAIL text) — my per-anchor mutants are strictly finer than the shipped fixture and each is still killed. The fixture family never tests the structural mutants below.

## Surviving mutants (exit 0) — rule is too wide

All three pass the full suite: `PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`, exit 0.

- M5 — polarity flip (exit 0, SURVIVES). Repro: on dump line 443993 replace
  `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp(T,d.directory,d.worktree)` with
  `if(Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp(T,d.directory,d.worktree)`.
  This inverts the escape hatch (env set → walk project; unset → config-only). All three anchors still present, OC-5 green. The rule witnesses that the env var and the two call shapes exist, not what the `!` does. [INFERENCE: behavioral inversion argued from reading the minified line; the bundle was not executed.]
- M6 — branch-arm swap (exit 0, SURVIVES). Repro: swap the two argument lists across the arms —
  `globUp(T,d.directory,d.worktree).pipe(s.catch(()=>s.succeed([])));return yield*e.globUp(T,r.config,r.config)` →
  `globUp(T,r.config,r.config).pipe(s.catch(()=>s.succeed([])));return yield*e.globUp(T,d.directory,d.worktree)`.
  The two regexes (:407-408) are independent dump-global searches; they are not bound to their branch arms, so project names can be read from global config and vice versa while OC-5 stays green. [INFERENCE: same non-execution caveat.]
- M7 — switch-site env removal (exit 0, SURVIVES). Repro: replace
  `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp` with
  `if(!1)return yield*e.globUp` (line 443993 only).
  The env anchor is a dump-global substring check (`OC_ENV_PROJECT_CONFIG in dump`, :487) satisfied by any of the 9 occurrences — including the prose docs at dump line 446350 and the unrelated TUI loader at 442392 — so the switch can drop its env gating entirely and OC-5 stays green.

Net: OC-5 kills exactly the single-token-loss mutants it was built for; it does not detect structural drift within the switch. Given the comment's own framing ("shape witness", :485-486) this is a known, accepted limitation, but the round's C1 gate-strength claim should not be read beyond it: three one-line mutations of the real dump keep surfaces 7/7 exit 0.

## Commands (exit codes)

- `sha256sum -c SHA256SUMS` (frozen substrate) → 0
- baseline pristine run → 0
- M1/M2/M3/M4 runs → 1 each, FAIL names OC-5
- M5/M6/M7 runs → 0 each (surviving)
- shipped `strings-opencode-drop-oc5.txt` fixture run → 1, FAIL names OC-5

## Artifacts

- `.ufo/waves/round-47/falsify/W2DropOC5.results.json` — machine-readable per-mutant results.
- `.ufo/waves/round-47/falsify/W2DropOC5.mutdiffs.txt` — changed-byte contexts for the three surviving mutants.
- Mutant dumps (67 MB each) kept out of the lane dir, in scratch: `/fast/scratch/kotoba-r47/w2/W2DropOC5-2/mut/`.

## What I did NOT check

- Behavioral equivalence of M5/M6/M7 was argued from the minified source line, not executed against a real opencode binary.
- Whitespace-tolerance of `OC_GLOBUP_CONFIG_RE`'s `\s*,\s*` (:408) — no whitespace-variant mutant was built (the real dump contains none at the switch).
- Only OC-5 was probed; OC-1–OC-4/OC-6 and the omp-side rules are untouched by this probe.
- Mutants were derived from the frozen, digest-verified dump, not from a fresh `strings` run of the binary.
- No tools were installed or upgraded for this probe (system python3 only); no labrat probe was needed.
