# kotoba — round 23 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 23, loop 1 (loop-round 3), dispatched and admitted.
Dispatch HEAD: `5a33c3e`. Work commit: `dc4c0c0` (this report lands in the follow-up publish commit, round-11 precedent).
Lane identity for the commits: `kotoba-shokunin <kotoba@shokunin.local>`.
Claim: **P — capability acquisition (freshness): land the substrate-pin guard** — `.ufo/round-23/claims.json`.
Provider adaptation: keys 3/4/5 of the opencode-go lane returned `402 Insufficient account funds` (2-lane probes each); the swarm dispatched on **opencode-go-6** (`opencode-go-6/deepseek-v4.1-flash`, 64 items). Recorded per the provider-exhaustion clause.
Swarm: **64 items; 64 completed** — lane A4's fragment landed late (after the swarm summary reported 63 and after a mid-run fragment check; `git add` captured it in the work commit, and this line corrects the pre-publish draft that recorded it as lost — the correction itself is the round-21 "64/64" class, caught before publish this time).
Status: **completed craft round, admitted** — the claim verifies as filed; no axis harmed.

## Work performed

- **P — the guard landed:** `verifiers/check_substrate_pins.py` (sha256 `fafe88d881eb…`, 474 lines) — the merged design from three independent implementation drafts (scouts D1-D3, all green) refined by twelve verification lanes (V1-V12); fixtures `verifiers/fixtures/pins/{mini,mini2,tripwire}.bin` (mini.bin `d3b4640e…`, byte-identical to the round-22 P4 design).
- **P — verification battery, integrator-run at landing (all as filed):**
  - live `python3 verifiers/check_substrate_pins.py` → **exit 0**, `OK 3/3 pins hold`, omp mtime `delta 0 ns` (ns-exact integer compare);
  - `--self-test` → `0 failure(s) over 46 assertions`;
  - six red probes on /tmp baseline copies: sha drift → **1** naming the pin (text + `--json`); mtime-only drift → **1** naming `omp_binary_mtime`; missing binary → **2**; corrupt baseline JSON → **3** no traceback; missing/null `measured_against` → **1** `VACUOUS` (the M6-D2 class); one pin deleted → **1** `PIN_ABSENT` (the P7-C9 class);
  - determinism: two live runs byte-identical; hash-never-exec (scout V3's strace: one execve total — the interpreter); read-only.
  - red-before replay: a baseline copy re-pinned to the round-18 omp sha `ff59fc1b…` → exit 1 `DRIFT omp_binary_sha256` — the state the 2026-10-16 rebuild produced while the harness gate stayed green.
- **P — debt state before:** `grep -c measured_against verifiers/*.py verifiers/*.sh` → 0 across all six instruments (scout D6 cmd 4); block deletable with every gate green (scout M6, round 22).
- **Provider-exhaustion handling:** keys 3, 4, 5 insta-failed the full dispatch + probes with 402; key 6 probed alive and carried the swarm. Next opencode-go round tries key 7, then re-probes 1-5 (recorded in claims.json `fallback`).
- **Adjacency (held, not claimed):** scouts A1-A3/A5-A7 re-measured: acknowledgment still 0 across siblings (A4's fragment lost — its slice is the one gap; A3/A7's kasegi coverage partially substitutes); the L0 round-22 line remains uncommitted in the fleet repo (integrator-owned, scout A1); kasegi's `anchorcheck.py` still always exits 0 (A7).
- **Deliberately not done:** no exec of the guarded binaries (the guard hashes); no re-pin (all pins hold — nothing to re-record); no push (divergence debt persists, ahead 6+); SHONEN untouched.

## Landed changes

- `verifiers/check_substrate_pins.py` + `verifiers/fixtures/pins/` (3 files) — the capability. [LOG § Round 23]
- `corpus/knowledge/substrate-pin-guard-round23.md` + `corpus/README.md` coverage row — the record + index.
- `SCORECARD.md` — **capabilities table gains its first row** (substrate-pin guard, first-working round 23); freshness row annotated; move-log row; planned refreshed.
- `SKILL.md` +2 lines (§ Sources instrument bullet, 518/600).
- `verifiers/corpus-baseline.json` — re-recorded 52→53 tracked (+2 report pointers observed at landing).
- `LOG.md` — § Round 23 appended.
- Intentionally unchanged: the other five instruments, protocol files, sibling repos, SHONEN.md.

## Before → after measurements

| Claim | Measurement | Before | After (round 23) | Command/evidence |
|---|---|---|---|---|
| P | pins enforced | 0 readers; corrupt sha → all gates green | live guard exit 0; sha drift → 1 | `python3 verifiers/check_substrate_pins.py` + /tmp probes |
| P | silent-shrink class | delete pin → `OK 2/2` exit 0 | `PIN_ABSENT` → exit 1 | probe (f) |
| P | TypeError class | non-string pin → traceback | exit 3, named error | probe (d)/V4 |
| P | block deletion (M6-D2) | exit 0 everywhere | `VACUOUS` → exit 1 | probe (e) |
| P | mtime compare | 874 ns float trap | integer-ns, delta 0 | live output |
| P | capabilities table | `— none yet —` | first row: substrate-pin guard | SCORECARD §Capabilities |

Axis verdicts: **freshness — improved** (score held 8.0: the substrate-drift detection gap is closed by a demonstrated, falsifiable capability; the 2026-10-16 class of silent movement can now never pass silently again); **adjacency — unchanged** (re-measured, still 0 ack; no claim made); coverage / operability / calibration / depth / consistency — **unchanged** (the guard adds an instrument without touching any other gate's scope; SKILL.md grew 2 lines to 518, box map intact). No trade.
Drift handling: A4's fragment landed late (64/64 — corrected pre-publish, see the header); the D6-vs-claim exit-code tension resolved **for the claim as filed** — the landed script exits 1 on missing/null block (claim-conformant), and the D6-drafted record texts were re-worded to the landed run's actual output (their own conditional-text rule); keys 3-5 exhaustion recorded with the key-6 adaptation.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged; the guard is an instrument, not box-1 content.
- [~] At least one end-to-end domain task executed and logged — unchanged; rounds 21-23 logged, lane-authored.
- [~] Instructions executable by an agent without oral context — strengthened, not claimed: the guard's six-probe matrix is an executable recipe in `corpus/knowledge/substrate-pin-guard-round23.md`, self-contained and host-portable.
- [~] No cross-domain bleed — unchanged; siblings read-only throughout; no fleet-path writes this round.
