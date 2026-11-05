# SentinelScopeR92 — scope and safety of the round-92 w1 candidate

Seat: SentinelScopeR92 (sentinel, round-92 wave 1, lane kotoba-shokunin). Poll for the four builder
READY files completed: all four appeared (ExecCtlWorlds_READY `CTL-WORLDS-READY 81f7c8b91d592cece20d81e981a13a88c376b525`,
ExecKillPin_READY `KILLPIN-READY N=28`, ExecLadderR92_READY `LADDER-READY N'=34`, ScribeCorpusR92_READY
`CORPUS-READY`) — polled at 120 s, well inside the 60-minute cap.

## Candidate built

- Base: `e073723ae667b64e534f8621bddb83ad12ad0e71` (freeze commit). Clone:
  `/fast/scratch/hyaku/kotoba-r92/SentinelScopeR92/repo` (created with the mandated command;
  `git rev-parse --show-toplevel` printed exactly the clone path before commit).
- All four builder patches applied: `git apply --check` clean, then `git apply` of
  ExecCtlWorlds.patch, ExecKillPin.patch, ExecLadderR92.patch, ScribeCorpusR92.patch.
- Candidate revision: **`fb8c0573073797e8ce039f8b8e7cc46f6eb7e0ac`** (scratch clone only; identity
  `scratch <scratch@invalid>`; lane untouched). Gates can name this rev for candidate readings.
- Post-apply `git status --porcelain` matched the patch headers exactly (8 modified files +
  `corpus/lessons/round-92.md` + `verifiers/fixtures/round-92/` as new).

## Findings

**S1 — patch scope: PASS.** `git diff --name-status e073723..fb8c0573` = exactly 14 paths, all
inside plans/round-92.md § Touch list:
ExecCtlWorlds (new): `verifiers/fixtures/round-92/controls-run.sh`, `ctl-c1-honest.sh`,
`ctl-c1-manifest-only-v2.sh`, `ctl-c2-capline-only-v2.sh`, `ctl-c2-honest.sh`;
ExecKillPin: `verifiers/check_mutation_battery.py`;
ExecLadderR92: `verifiers/check_freeze_gate.py`, `verifiers/check_assertion_floors.py`,
`verifiers/check_tip_battery.py`, `verifiers/floors-registry.json`;
ScribeCorpusR92: `corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md`,
`corpus/lessons/round-92.md` (new).
Explicit zero-diff checks over the forbidden set returned empty: SKILL.md,
`corpus/lessons/round-*-verifier-spotcheck.md`, `verifiers/fixtures/round-91/`, frozen instruments
(`check_r86_routed_repairs_v3.py`, `verify_corpus_integrity.py`, `corpus-baseline.json`,
`check_gate_registry.py`, `verify_skill_checklist.py`), plans/*, SCORECARD.md, LOG.md, PROVINCE.md.
No patch touches SCORECARD/LOG/PROVINCE (L1-only at integration). No violation.

**S2 — write containment: PASS.** The (b) find (`round-92` tree, `-newer plans/round-92.md`)
contains only: L1 wave-control artifacts (`r92-w1-spec.json`, `r92-w1-dispatch.json`,
`r92-w1.ready*`, `report-draft.md`, `gen-w1.py`, `w1/swarm-registry.json`) and seat receipts under
`w1/<seat>/` plus top-level `w1/<Seat>.md` report copies and `<Seat>_READY` markers (the
validator-rendered Report-trailer convention). Nothing at the fleet root attributable to a kotoba
seat: fleet-root files newer than the plan = `MANIFEST.json` only, whose last commit is fleet-level
(`57faca14 protocol-shokunin Thu Nov 5 15:00:00 2026 — rounds ledger: revenger r95 closure`,
non-author); fleet porcelain shows only harness state `.scratch/run15-state.json`. Strict sibling
check: zero files matching any kotoba-R92 seat name (`*R92*`, ExecCtlWorlds, ExecKillPin,
ExecLadder, ScribeCorpus) newer than the plan outside kotoba-shokunin. `SentinelScope.md` files
seen in kaidoku-shokunin are that lane's own earlier-round seats (rounds 35–79 paths), not this
wave. No violation.

**S3 — secrets/host safety: PASS.** Wave-tree greps: `sysctl` and `pacman` appear only in bounds/
dispatch text (`gen-w1.py`, `r92-w1-spec.json`, `r92-w1-dispatch.json`) and in seat reports as
negative attestations ("no sysctl", "no pacman"); `op://` only in the bounds text; token-shaped
strings (ghp_/github_pat_/AKIA/xox/sk-/JWT/private-key/AWS_SECRET): zero hits; env-dump markers
(printenv/declare -x/env -0/set -x): zero hits. No sysctl write, no pacman invocation, no
credential material, no raw environment dumps in any seat receipt.

**S4 — scratch discipline: PASS.** No `/tmp/` literal in any patch bytes, in any added line of the
candidate diff, or in the candidate's `verifiers/fixtures/round-92/` files. The new C1 control
scripts root all writes at `${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r92/ExecCtlWorlds` via
`mktemp -d`, pass `TMPDIR="$W"` and `--work "$W/battery"` to instrument invocations, and commit
worlds only inside scratch clones; no absolute writes outside scratch, no network, no sudo, no
destructive ops (`sudo |chmod 777|rm -rf /|mkfs|dd if=` zero hits over all four patches); all five
committed scripts pass `bash -n`. `/fast/scratch/hyaku/kotoba-r92/` holds only seat-named dirs
(+ `l1-predata` for L1 pre-data); scratch of finished seats already removed at observation time.

**S5 — kill-cap bounds sentence: PRESENT.** Verbatim in my own brief: "Kill only by the PIDs you
started; contention cap (4 processes, 120 s per probe)." Verified in the wave dispatch source:
`r92-w1-dispatch.json` → `taskCall.context` carries `## Bounds (read first)`, the kill-cap
sentence, the PACMAN pause line and the sysctl prohibition, and `taskCall.tasks` lists all 12
seats (ExecCtlWorlds, ExecKillPin, ExecLadderR92, ScoutPyDocs, ScribeCorpusR92,
ConnectorOverlapR92, ReviewerCtl, MutTesterCtl, ReviewerFloors, MutTesterBattery, CriticClaimsR92,
SentinelScopeR92) — the shared context is wave-wide. Per-seat brief bodies beyond the shared
context are trusted to the validator as my item directs.

**S6 — SKILL.md freeze: PASS.** `git diff --stat e073723..fb8c0573 -- SKILL.md` is empty;
SKILL.md remains 600 lines / 92 672 bytes at the candidate (the Q78 ceiling, untouched).

**S7 — candidate integrity: PASS.** `git apply --check` passed for all four patches together;
apply produced exactly the header-declared file set; commit made only after re-asserting
`rev-parse --show-toplevel` equals the clone path. No lane, fleet, or sibling git/jj write
performed by this seat.

**S8 — red-before receipts at freeze: CONFIRMED.** `git ls-tree e073723 -- .ufo/waves/round-92/`
tracks all receipts the predicates cite: `redbefore-ctl-c1/c2`, `redbefore-ladder-127/dup/work`,
`redbefore-m6-dropped-row`, `redbefore-honest-fp-minimal`, the `base-*` family, `freeze-gate-r92.txt`,
`q73-sweep-raw.txt`, `census-before.txt`. (Supporting evidence for the C1/C2 predicate
preconditions; predicate readings themselves belong to the gates.)

## Risks / observations

- R1: mtime-based attribution has limits — fleet-root `MANIFEST.json`, fleet `.git`/`.ufo` dir
  mtimes moved during the window, but content evidence attributes them to the fleet harness
  (protocol-shokunin rounds ledger; `.scratch/run15-state.json`), not to any kotoba seat.
- R2: top-level `w1/<Seat>.md` copies sit outside `<Seat>/` subdirs; both locations are inside the
  wave receipt tree and match the Report-trailer convention, so I classify them as compliant, not
  as seat scope violations.
- R3: I did not run the C1/C2 predicates — correctness belongs to the gates/reviewers; my scope was
  candidate scope and safety, which is clean. Candidate for their readings:
  `fb8c0573073797e8ce039f8b8e7cc46f6eb7e0ac`.

## Trailers

Tooling installs this round: none. Pacman: untouched (host pause honored). Kernel/host settings:
untouched. Scratch `/fast/scratch/hyaku/kotoba-r92/SentinelScopeR92/` deleted before yield.
