# ExecTipDefense — round 70 wave 1

**Verdict: AGREE, 12 of 12 receipt lines.** Each of the three r69 counters reproduces the verdict line, exit code and self-test tally recorded in `.ufo/waves/round-70/receipts/r69-tip-defense.txt`. I ran them independently in a `git clone --shared` sandbox with `--repo <sandbox>`.

## Setup

- Sandbox: `mktemp -d /tmp/k70w1-ExecTipDefense.XXXX` gave `/tmp/k70w1-ExecTipDefense.9NGY`. It was deleted before return.
- `git clone --shared -q /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/lane`, then `git rev-parse HEAD` gave `16b212a390c7ce68b6bce49b2c3766b154fbcbae`, which is the lane tip.
- Python 3.14.8. Run started at 2026-10-25T11:56:23Z.
- In the lane checkout, `git diff --quiet 9ce102b9e3f8896d5ed3f050ee896ca90d693a38 HEAD -- verifiers/check_skill_precedence.py verifiers/check_r68_routed_repairs.py verifiers/check_province_core.py` printed `diff-vs-tip-exit=0`. The counter bytes at the lane tip are therefore the same as at the r69 tip, which extends the receipt's own claim (r69 tip vs `a647fa7`) through to `16b212a`.
- Command form: `timeout 290 python3 -B verifiers/<counter>.py --repo $S/lane --rev 9ce102b9e3f8896d5ed3f050ee896ca90d693a38` and `... --repo $S/lane --self-test`.

## Agreement per line

| Counter | Receipt line | Sandbox observed | Agree |
|---|---|---|---|
| check_skill_precedence | `measured-rev: 9ce102b9…` | `measured-rev: 9ce102b9e3f8896d5ed3f050ee896ca90d693a38` | yes |
| check_skill_precedence | `skill precedence backed 5 of 5` | `skill precedence backed 5 of 5` | yes |
| check_skill_precedence | `exit=0` | `exit=0`, stderr empty | yes |
| check_skill_precedence | `self-test: 0 failure(s) over 22 assertions`, `selftest-exit=0` | same tally, `selftest-exit=0` | yes |
| check_r68_routed_repairs | `measured-rev: 9ce102b9…` | `measured-rev: 9ce102b9e3f8896d5ed3f050ee896ca90d693a38` | yes |
| check_r68_routed_repairs | `r68 routed defects closed 8 of 8` | `r68 routed defects closed 8 of 8` | yes |
| check_r68_routed_repairs | `exit=0` | `exit=0`, stderr empty | yes |
| check_r68_routed_repairs | `self-test: 0 failure(s) over 25 assertions`, `selftest-exit=0` | same tally, `selftest-exit=0` | yes |
| check_province_core | `measured-rev: 9ce102b9…` | `measured-rev: 9ce102b9e3f8896d5ed3f050ee896ca90d693a38` | yes |
| check_province_core | `province core rows 2 of 2` | `province core rows 2 of 2` | yes |
| check_province_core | `exit=0` | `exit=0`, stderr empty | yes |
| check_province_core | `self-test: 0 failure(s) over 10 assertions`, `selftest-exit=0` | same tally, `selftest-exit=0` | yes |

## Extra falsifiers (all passed)

1. **Rerun from the r69 tip's own checked-out bytes.** In the sandbox, `git checkout -q 9ce102b9e3f8896d5ed3f050ee896ca90d693a38` (HEAD confirmed `9ce102b9…`), then the same six commands were rerun. The results were identical: `skill precedence backed 5 of 5` exit=0 with 22 assertions, `r68 routed defects closed 8 of 8` exit=0 with 25 assertions, and `province core rows 2 of 2` exit=0 with 10 assertions. Every self-test reported 0 failures with `selftest-exit=0`.
2. **Non-vacuity control.** Each counter was run with `--rev 0000000000000000000000000000000000000000`. All three printed `environment error: unknown revision 0000000000000000000000000000000000000000` and exited 2. The counters really resolve `--rev` against the repository; they do not pass whatever revision they are given.
3. **Clean sandbox.** After the lane-tip runs, `git -C $S/lane status --porcelain` printed nothing, so the counters did not write into the worktree.

## Note on the receipt bytes

When the receipt is shown by a file viewer, lines 10 and 20 appear with prefixes like `    10|`. `grep -n '' … | cat -A` shows that line 10 is really `self-test: 0 failure(s) over 22 assertions$` and line 20 is empty. The prefixes come from the viewer and are not defects in the receipt.

## Risks and blockers

- None blocking.
- The receipt was run from the lane checkout with no `--repo` flag. This reproduction passes `--repo <sandbox>`, so it agrees on a different invocation path. The outputs are identical either way.
- Tools installed or updated: none.
- Files changed: only this report.
