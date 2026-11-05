# WORLD.md — ExecMirrorR87, w3 instrument location control

Baseline: 223ae62 · frozen C2 receipt revision: 35a395a9 · tip: 760e1c5e
Instrument: python3 -B verifiers/verify_corpus_integrity.py --json (rev via `REV=<token>` env var, 

## Command list (one lane, one clone, one fixture toggle, one counter probe)

```bash
# 1) worlds
D=$S/repo && git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$D"
git -C "$D" checkout -q -B master 760e1c5edfdefb4767420f711d08f669952de013
# 2) counter + gate in clone
cd "$D" && { python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e → 4 of 5, exit 1  \
              FAIL d5: red set = ['commit_unresolvable','report_dead'] }
cd "$D" && { REV=760e1c5e python3 -B verifiers/verify_corpus_integrity.py --json → 2 reds: commit_unresolvable + report_dead (detail: round-81.md:29 ../../ pointer) }
# 3) counter + gate in lane
cd lane && { python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e → 4 of 5, exit 1 \
              FAIL d5: red set = ['commit_unresolvable'] only }
cd lane && { REV=760e1c5e python3 -B verifiers/verify_corpus_integrity.py --json → 8/9, \
              reds = ['commit_unresolvable'], detail round-81.md:8 only }
# 4) clone re-creation: TARGET FILE UNDER THE CLONE's parent
mkdir -p $S/.ufo/reports/round-76/
head -c 400 <(echo '## SHONEN'; echo …content…) $S/.ufo/reports/round-76/kotoba.md
cd "$D" && { REV=760e1c5e python3 -B verifiers/verify_corpus_integrity.py --json → 1 red (lane reading exactly) }
cd "$D" && { python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e → FAIL d5: red set ['commit_unresolvable'] != want ['commit_unresolvable','report_dead'] }
# 5) toggle off
rm $S/.ufo/reports/round-76/kotoba.md && rmdir $S/.ufo/reports $S/.ufo
cd "$D" && REV=760e1c5e python3 -B verifiers/verify_corpus_integrity.py --json → 2 reds again (clone reading)
# 6) revision cross-check: 35a395a9 (the receipt world) and 223ae62 (base) in clone
git -C "$D" checkout 35a395a9 → identical 2 reds to tip; identical 4 of 5
git -C "$D" checkout 223ae62  → verifiers/verify_corpus_integrity.py + counters DO NOT exist on this rev
                               (frozen base: 0 of 5 / 0 of 12 by code-absence; base receipts in round-87/receipts/)
git -C "$D" checkout master
# 7) counter identity const, code gates
print(FLEET_ROOT) == "/home/vgpnk/Projects/shokunin"   # constant, not derived
# citation-loop excerpt, lines 570-586:
#     if not pointer_exists(base, token):
#         report_dead.append(...)
# inside CODE SPAN tokens are EXEMPT only in the COMMIT loop (line 587-588);
# the POINTER loop (lines 570-586) has NO code-span exemption — only dbl-quote.
```

## The two readings (tip, same corpus bytes — verified `git diff --shortstat 35a395a tip -- corpus/` → identical)

```text
lane  : reds=['corpus.pointers.commit_unresolvable']  C2 prints 4 of 5 (fails D5(iii))
clone : reds=['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead'] C2 prints 4 of 5 (fails D5(iii))
```

Idempotency: relacing the reported file under the CLONE parent filters the extraneous red → lane reading. Removing it re-fires the clone reading. (Deterministic back-and-forth; receipts `c2-clone-placed.txt` / `gate-clone-placed.json`.)

## Verdict

**NOT the round-lesson the item template offered** ("a bare `.ufo/reports/...` path resolves from a fleet root" — that mechanism does NOT apply to either of the citations here; `FLEET_ROOT` never enters the waves). The computed cause is the two RED SOURCES being checkout-sensitive:

- `corpus/lessons/round-81.md:29` cites `../../.ufo/reports/round-76/kotoba.md` — resolves in the lane worktree via the tracked SYMLINK `.ufo/reports/round-76/kotoba.md → ../../../../.ufo/reports/round-76/kotoba.md` (which dangles in any clone). Today it *resolves* in lane (into the fleet worktree) and *dangles* in clone.
- `corpus/lessons/round-86-verifier-spotcheck.md:33` cites `.ufo/reports/round-84/kama.md` (the `5b052020` fleet commit landed 11-04 22:47 «...»). *Resolves* in both worlds today because lane worktree ADOPTED the pointer count by the fleet-materialized file; the standalone C2 receipt world at 223ae62 (pre-landing) read only liveness via lane's **own** tree where the commit does not exist — this is the locality the round's C2-final 5-of-5 was captured in, and the tip's 4-of-5 is the changed parity.

`D5(iii)` is therefore **checkout-location-DEPENDENT on its red-SET-SHAPE conjunct**: the lane reds are 1, the clone reds are 2, and both pass D5(iii)'s *set-equality* gate only in the `2-red` world, never the `1-red` world (the lane). The lane reds are healthy, but the exact-set outcome is not location-independent.

**conjunct=non-monotone** (a location where the cited vuln resolves *heals* the red and fails D5).
`same bytes, two paths: lane=<760e1c5 lane tree, 4/5, D5-red-set=1> clone=<760e1c5 clone parent tree, 4/5, D5-red-set=2>; conjunct=non-monotone`
