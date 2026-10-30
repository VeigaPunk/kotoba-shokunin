# Kb82E07C2Worlds — C2 independent discriminator runner (round 82)

Seat role: C2 independent discriminator runner for the hermetic checklist
self-test repair. L1 owns planning/integration; this is evidence only, no
score claim. Judged axes: freshness, operability (this seat feeds operability).

## Base and setup

- Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch clone
  `/fast/scratch/hyaku/kotoba-r82/Kb82E07C2Worlds/clone`, shared clone,
  every git call `-C`-scoped, toplevel asserted before mutations).
- Production repo has since advanced to `006a834` (freeze commit); all
  measurements here cite the base revision. Fleet before receipt:
  `.ufo/waves/round-82/receipts/before-checklist-selftest.txt`
  (`1 failure(s) over 1863 assertions`, exit 1, dead SCORECARD.md:480/482/484).
- Clone state note: `git clone --shared` carries only tracked bytes; the
  governance live arm also resolves `../`-hop tokens against repo ancestors
  and one committed symlink (`.ufo/reports/round-76/kotoba.md`). I replicated
  the production before-state in my own sandbox by creating the missing
  base-era untracked paths under the clone and its parent (fixture-only,
  sandbox-only). After that, the clone self-test reproduces the fleet
  before receipt byte-for-byte in shape:
  `1 failure(s) over 1863 assertions`, exit 1, same three named dead
  subjects, same `2 recorded absence(s) excused, 4 recorded correction(s)
  excused` context (`Kb82E07C2Worlds-receipts/before-selftest-clone-replica.txt`).
- No tool installs/upgrades (none needed); pacman untouched; disk-guard
  checked (`/fast` 46% used) before heavy work. TMPDIR under seat scratch.

## Deliverable: the runner

`build/Kb82E07C2Worlds-runner.py` — standalone harness; imports the verifier
under test by path, builds isolated fixture worlds (temp repos with
LOG.md + SCORECARD.md + corpus/), and asserts the red/green contract of the
round-65 correction machinery. Worlds:

- W1 valid correction -> green (1 recorded correction excused)
- W2 missing correction -> red (stale token named)
- W3 stale target restored -> red ("stale, the old token now resolves")
- W4 unrelated dead citation -> red (unrelated subject named; the valid
  correction still excuses only its own subject — no masking)
- W5a–W5e guard-disabled variants -> red: digest drift, wording, past
  horizon, no live red subject, corrected token dead
- W6 live-drift independence: runs the verifier's own `--self-test` in a
  repo copy, appends one dead citation to that copy's live SCORECARD.md,
  re-runs, and requires byte-identical output + exit.

## Results

### Base verifier (blob sha256 `b7d7b0fc…39615`, clone copy)

- W1–W5: all 9 fixture worlds discriminate correctly
  (`worlds-base.json`: `worlds_discriminating: 9`).
- W6: **FAIL** — the base selftest is live-coupled. Mutating the sandbox
  SCORECARD.md changed the failure detail (`evaluated 1366 -> 1367`,
  `+35 more -> +36 more`; receipts `w6-live-drift-before.txt` /
  `w6-live-drift-after.txt`). This is the measured defect: a fixture-only
  selftest reads the evolving live governance files.
- Additional base finding: the live arm also resolves `../` tokens against
  repo ancestors and one committed symlink, so its result depends on host
  layout outside the repo — a hermetic replacement must not depend on
  either.

### Shortcut analysis (the count-floor question)

Question: can `0 failure(s) over N>=1863` be met by deleting the failing
assertion and padding with trivial assertions? **Yes, mechanically.**
Three scratchpad variants of the base verifier (sandbox-only, no commits):

- remap named arm to `True` (plan-forbidden): `0 failure(s) over 1863
  assertions`, exit 0 (`shortcut-remap.txt`).
- delete named arm: `0 failure(s) over 1862 assertions`, exit 0 — the
  N>=1863 floor alone rejects deletion (`shortcut-delete.txt`).
- delete + one trivial `rec("shortcut padding assertion", True, None)`:
  `0 failure(s) over 1863 assertions`, exit 0 (`shortcut-delete-pad.txt`).
- the remap variant is evidence-blind: re-run with a dead citation
  appended to live SCORECARD.md gives byte-identical output
  (`shortcut-remap-drift-before.txt` == `-after.txt`, sha256 `dc04b2e0…`).

Consequence: the numeric target is satisfiable without any semantic
content, so it cannot certify the repair by itself. Any overclaim resting
on `0/N>=1863` alone is invalid; the claim must anchor on the named arm
being replaced by isolated fixture evidence with the required
discriminators, and the assertion inventory must show semantic (not
padding) arms.

### Candidate patch test (E03, present at test time; checked once, no polling)

`build/Kb82E03Checklist.patch` — applied to a fresh copy of the prepared
clone (`clone-e03`). Postimage file sha256 `24fec2837ce5618ac0deeb62e0d8b1a3d7253f775aa50efda4038fdf166ffb56`, git blob `bc3674e4854e7c4b87435289884687dbde6745a3` —
both match E03's published `Kb82E03Checklist-blob.txt`. Scope: one file,
`verifiers/verify_skill_checklist.py`, +109/-16.

The patch replaces the two live-coupled arms with a hermetic
`round-82-mirror` fixture world inside the selftest's existing tempdir,
embedding the recorded LOG.md lines as byte literals behind a sha256
digest guard, and replays the pinned GOVERNANCE_ERRATA /
GOVERNANCE_CORRECTIONS rows there. Independent verification:

1. Patched selftest in my sandbox: `0 failure(s) over 1867 assertions`,
   exit 0 (`e03patched-selftest-green.txt`). N=1867 >= 1863; the +4 delta
   is four semantic arms, audited by name:
   added = `fixture recorded lines are the pinned rows` (digest guard),
   `fixture round-65 corrections land, errata-excused`,
   `fixture missing correction still fails`,
   `fixture restored stale target turns correction stale`,
   `fixture unrelated dead citation still fails`; removed =
   `live round-65 corrections land, errata-excused` (replaced, not
   deleted-to-success). No padding arms; no other arm touched.
2. My runner against the patched verifier: all 9 fixture worlds still
   discriminate; **W6 now passes** — live SCORECARD.md mutation leaves the
   patched selftest output byte-identical (`worlds-e03patched.json`,
   `verdict: PASS`).
3. Guard-disabled, reproduced independently (mine, not E03's receipt):
   corrupting one embedded literal in a sandbox copy turns the digest-guard
   arm and both dependent fixture arms red — `3 failure(s) over 1867
   assertions`, exit 1 (`guard-disabled-independent.txt`). The replacement
   guard is load-bearing.
4. Required discriminators, all present and green/red as specified:
   fixture valid correction green; missing correction red; restored stale
   target red; unrelated dead subject red; live-governance change does not
   change fixture results (W6); guard-disabled shows the fixture failing.
5. Public live gate not masked: under the patch,
   `--check governance.citation_resolves` on the repo still FAILs, naming
   the same three genuinely dead citations (`.ufo/wapes`,
   `corpus/lessons/round-80-verifier-spotcheck.md:30,37`,
   `.ufo/reports/round-81/kotoba.md`), exit 1 (`live-gate-patched.txt`).
   The patch touches only `--self-test`; live checking is unchanged.

## Risks / blockers

- E03's design was not read as a peer report (not present when work
  started); the patch artifact was treated as untrusted data and verified
  independently end-to-end. All patch claims re-derived, not assumed.
- My sandbox replication of the production before-state required
  recreating untracked base-era paths (clone `.ufo` files, ancestor
  `../` targets, one symlink replaced by a regular file). This is
  sandbox-only; it does not mutate fleet, siblings, or production. The
  fleet before receipt remains the authoritative before; my replica is a
  secondary, shape-identical confirmation.
- The patch embeds large recorded-line literals; future LOG.md appends are
  safe (append-only), but any re-pin of the errata/correction tables trips
  the digest guard until the literal set is extended — that is the
  intended fail-closed behavior, demonstrated in guard-disabled world.

VERDICT: C2 discriminators proven against base (defect reproduced: live
selftest reads evolving SCORECARD/LOG and host-external `../` paths); the
count floor is mechanically reachable by delete+padding, so numeric
targets alone certify nothing; candidate patch Kb82E03Checklist.patch
independently verified — hermetic, semantically anchored (N=1867, +4
named discriminator arms, no padding), all required red/green
discriminators hold, replacement guard is load-bearing, live gate still
flags genuinely dead citations. No axis score claimed; L1 decides
integration.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E07C2Worlds-runner.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E07C2Worlds-receipts/ (14 files, sha256s recorded above)
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E07C2Worlds.md
