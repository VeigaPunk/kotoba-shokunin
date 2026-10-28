# Kb80L03Symlink — symlink probe worlds (round-80 w1)

Seat: `Kb80L03Symlink` (scout, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Date: 2026-10-27.

Question probed: the four symlink worlds using the available cap-60 C1 probe counter — does the
`.ufo/reports/round-76/kotoba.md` repair behave as the plan claims under (1) an absent
fleet tree, (2) wrong link depth, (3) a regular-file stand-in, (4) a `../`-form LOG.md edit?

## Method

- Counter bytes: `build/Kb80L03Symlink.probe-counter-e5.py` — the lane's
  `verifiers/check_tip_battery.py` with exactly `LINE_CAP` 40→60. At probe time the canonical
  E5 counter was unavailable. Later, `build/Kb80E06CounterErratum.cap60-provisional.py`
  appeared; its `LINE_CAP` is 60, but its `INSTRUMENT_PINS` lines 133–148 still contain only
  the r72 pins (confirmed by reading the file), not E5's two reviewed additions. No E05 blob
  receipt or E06 final counter was available. No probe world edits any of the six battery
  instruments, so the pin guard is invariant under the missing additions; nevertheless,
  these are NOT measurements on the complete frozen E5 pin table. Probe-counter sha256
  `bfbbd0a3c9433485cb311df121a5c3dfaaade6ba5dc818de24e03055137d0629`; one-line diff vs lane
  counter. Each battery run:
  `python3 -B <probe counter> --rev <world> --repo $S/clone --fleet <fleet|fleetless>`,
  the command's OWN exit status captured (`cmd > f 2>&1; rc=$?`) — no pipelines (M80-1).
- Worlds: one commit each on top of the base in a scratch clone
  (`/fast/scratch/hyaku/kotoba-r80/Kb80L03Symlink`, toplevel asserted, removed after).
  Full construction log with commit ids, git blob ids and the sha256 chain:
  `build/Kb80L03Symlink-worlds.txt`.
- Second, independent path: direct `verify_skill_checklist.py` runs on each world cloned
  into a fleet-shaped parent (every fleet entry symlinked beside the clone, dotglob).
  The first pass of these used a `*` glob that missed dotfiles (fleet `.ufo`) and produced
  environment-redundant reds; it was discarded and redone — the same M127-class trap the
  counter's `build_sandbox` avoids with `iterdir()`.

## Verdicts

**World 1 — symlink present, fleet tree ABSENT → fails closed, as required.**
World `e05e7b1` (4-hop link, blob `bf7c7e0c…` = the reviewed patch bytes) measured with
`--fleet` = an EMPTY directory: the counter's `build_sandbox` links every fleet entry into
the sandbox parent, so with none the parent holds only the clone and the 4-hop link dangles.
Battery receipt `build/Kb80L03Symlink-w1-fleetabsent-tipbattery.txt`:
`guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1, `verify_skill_checklist.py exit 1`.
The gate names the token in the direct run + bad-subject dump
(`build/Kb80L03Symlink-w1-badsubjects.txt`): `LOG.md:2818 '.ufo/reports/round-76/kotoba.md'`
is among the unresolved. Dangling = red, never green-by-absence. VERDICT: PASS (fails closed).

**World 2 — symlink with THREE hops (wrong depth) → must not resolve. It does not.**
World `b3bb6114` (link `../../../.ufo/reports/round-76/kotoba.md`, blob `66a93c3b…`): three
hops from `.ufo/reports/round-76/` land on the lane root, so the link resolves to itself —
a self-loop (`ELOOP`). Battery receipt
`build/Kb80L03Symlink-w2-threehop-tipbattery.txt`: `guards 5 of 5; tip battery exit 0: 1 of 6`,
exit 1, checklist gate exit 1; direct run names exactly
`LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve`. VERDICT: PASS (no resolution).

**World 3 — REGULAR FILE copy, identical bytes → checklist greens (existence test).**
World `2098c00a` (file bytes copied from the fleet report): battery receipt
`build/Kb80L03Symlink-w3-regularfile-tipbattery.txt`: `guards 5 of 5; tip battery exit 0: 3 of 6`,
exit 1, `verify_skill_checklist.py exit 0` (and floors exit 0 — the self-test arm on the
LOG.md:2818 token resolves too). Direct run: PASS, exit 0. So the gate tests EXISTENCE, not
identity: any bytes at that path would green it.
Identity evidence audited: the committed copy's sha256
(`git show w3:...|sha256sum` = `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f`)
equals the fleet file's, and the round's receipts DO carry exactly this equality —
`build/Kb80E02-symlink-identity.txt` (fleet sha256, resolved-target sha256 equal, realpath,
git blob `bf7c7e0c…`, patch sha256 `0f320240…` byte-identical to the r79 reviewed draft),
`build/Kb80S15FreezeShas-receipts.txt` (fleet-file sha256 block), and the designed after-receipt
line `SHA_SYMLINK_TARGET_TIP` (sha256 of the FOLLOWED link's bytes, not of the path/string).
The reports say so in prose: `w1/Kb80E02Symlink.md` §2 and its "Existence ≠ identity" finding,
and `build/Kb80S02Log.md` ("one artefact, one byte-stream (sha256 a025051d…)"). VERDICT: PASS
(greens; limit documented in the round's evidence).

**World 4 — symlink added AND LOG.md:2818 edited to a `../` form → the edit is WITHIN 3 hops;
the landmine does NOT fire.** World `79d4ccbb` (4-hop link + line 2818 token
`../.ufo/reports/round-76/kotoba.md`, verified from the committed bytes): battery receipt
`build/Kb80L03Symlink-w4-logdotdot-tipbattery.txt`: `guards 5 of 5; tip battery exit 0: 3 of 6`,
exit 1, checklist gate exit 0; direct run PASS, exit 0. The governance predicate
(`verify_skill_checklist.py:citation_resolve`) bounds `..` hops at 3 — this token is 1 hop,
resolving against the repo's ancestor, which the counter's sandbox populates with the fleet
root's entries, so the fleet file is found. Which of the two alternatives fires is therefore:
**within 3 hops → resolves; no landmine.**
Calibration that the cap itself is live: bonus world `561b6713` with the token written as the
4-hop string in tracked prose → direct run FAIL, exit 1, naming
`LOG.md:2818: '../../../../.ufo/reports/round-76/kotoba.md' does not resolve`
(`build/Kb80L03Symlink-w5-fourhopprose-checklist.txt`). The plan's landmine note ("the
four-hop string must never be written backticked in tracked prose") is exactly this: 4 > 3.
The repair's own 4-hop string lives only as the symlink's target, which the gate never parses
as prose. VERDICT: PASS (question answered; cap verified live).

## Notes and findings

- No world reaches the 6-of-6 kill threshold (max 3 of 6, on the two existence-green worlds);
  no counter defect, no narrowing. Worlds 1–2 keep the battery at the base figure 1 of 6,
  proving the checklist red at base is repairable only by the actual artefact.
- Evidence honesty: the first w4/w5 build used a sed whose backtick-heavy pattern silently
  matched nothing; the committed LOG.md lines were base bytes. Caught by re-reading the
  committed line, rebuilt with a robust pattern, receipts re-taken and the confounded w4
  battery receipt overwritten (its first "3 of 6" was in fact the symlink-only world).
  Stated in `build/Kb80L03Symlink-worlds.txt`.
- E02's own tip-battery world used the r72 frozen counter (LINE_CAP 40). This seat's cap-60
  probe copy likewise retained the base pin table; the subsequently published
  `Kb80E06CounterErratum.cap60-provisional.py` also lacks the two E5 pin additions. Thus the
  observed control-world verdicts are invariant for the unchanged instruments, but the
  complete E5 counter remains unmeasured here because its reviewed composed blob ids were
  unavailable.
- No lane file outside `.ufo/waves/round-80/` was touched; no commits in the lane; scratch
  removed before yield.

VERDICT: Under the available cap-60 probe counter with base pins, all four world outcomes match the plan's expected behavior: fleet-absent and wrong-depth links fail closed; the identical-bytes regular file greens the existence test with sha256 identity evidence carried in round receipts/reports; the 1-hop `../` edit resolves within the cap (a 4-hop prose token fails). Because the final two E5 pin additions were unavailable, these are not measurements on the complete amended counter.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80L03Symlink.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-worlds.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink.probe-counter-e5.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w1-fleetabsent-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w1-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w1-badsubjects.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w2-threehop-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w2-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w3-regularfile-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w3-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w4-logdotdot-tipbattery.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w4-logdotdot-checklist.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L03Symlink-w5-fourhopprose-checklist.txt
