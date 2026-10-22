Result: HOLDS — the frozen C1 counter reproduces the declared lines at all three revisions and the measured opencode substrate is unchanged since 2026-10-22T17:50:30Z (independently re-hashed: still sha256 538fcb1b…).

# Scope

Target: C1's measurement (frozen counter `verifiers/check_opencode_repin.py`). Seat `KotobaR53.W2RerunC1`, 2026-10-22, lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Read-only in the lane: no git writes, no lane file edits, no installs (tooling directive: nothing installed; only preinstalled python3, git, sha256sum, stat, file used).

# Precondition checks

- Lane HEAD: `git rev-parse HEAD` → `c775d6823bfca8f0de8c0874032a954438b38edc` (floors commit).
- Counter is the frozen copy: `git rev-parse 3bb0a7a3:verifiers/check_opencode_repin.py` = `213b346ae2b00dcebdece45913db200bde510629`; `git rev-parse HEAD:verifiers/check_opencode_repin.py` = same; `git hash-object verifiers/check_opencode_repin.py` (working tree) = same; `git diff --stat 3bb0a7a3 HEAD -- verifiers/check_opencode_repin.py` = empty. The counter I ran is byte-identical to the plan-commit freeze.
- Dirty working-tree entries (`PROVINCE.md`, `SKILL.md`, `corpus/QUALITY.md`, `corpus/README.md`, `corpus/SOURCES.md` modified; `.ufo/waves/round-53/`, `corpus/lessons/round-53.md` untracked) cannot affect the counter: it reads only committed objects (`git show BASE_REV:…`, `git archive <rev> -- verifiers corpus`) and executes the extracted tree from a `TemporaryDirectory`, never the working tree.

# Re-runs (counter frozen at 3bb0a7a3, SELFTEST_FLOOR=129, CHECKS_TOTAL=7, PINS_TOTAL=3)

Run from lane root, `python3 -B verifiers/check_opencode_repin.py --rev <rev>`, UTC 2026-10-22 ~20:37Z (sha probe below stamped 20:36:39Z; runs followed immediately).

1. `--rev 55973a20ac728f7b11ac8de518620ba128c13afa` (C2 commit), wall 6.46 s, EXIT=1:
   ```
   opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 133 assertions
   substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
   ```
   Declared (context freshness block): same line, exit 1. MATCH.
2. `--rev 6dd311644f987cef62a40f0c028ea2be2fc6ff67` (C1 commit), wall 15.61 s, EXIT=0:
   ```
   opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 155 assertions
   substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
   ```
   Declared: same line, exit 0. MATCH.
3. `--rev c775d6823bfca8f0de8c0874032a954438b38edc` (floors commit), wall 16.47 s, EXIT=0:
   Same two lines as run 2. Consistent with the floors commit registering `surfaces` at 155 (printed assertions 155 ≥ frozen floor 129; exit 0). MATCH.

# Substrate verification (my own hash, not the counter's)

- `which opencode` → `/home/vgpnk/.local/bin/opencode`; `opencode --version` → `1.19.4`, exit 0 (2026-10-22T20:36:39Z).
- `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` → `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, `stat` bytes=214522032, mtime `2026-10-22 14:50:30.116162200 -0300` = 17:50:30.116Z. Exactly the substrate line's path, sha and byte count. Still 538fcb1b… → no host drift since the plan's baseline moment; these are the same measurements.
- Why the PATH entry hashes differently: `/home/vgpnk/.local/bin/opencode` is a 1460-byte bash wrapper (omarchy npm launcher, `file`: "Bourne-Again shell script"). It resolves the package bin via `npx --yes --package opencode-ai -- which opencode` and `exec`s the resolved path; the npx cache `e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` is the real executable the gate measures. `sha256sum` of the wrapper itself is `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b` — that is the launcher, not the pinned artifact; recorded to preempt a false drift alarm.

# Judgment

HOLDS. Before (55973a2) and after (6dd3116, c775d68) match the declared lines exactly, exit codes 1/0/0 as declared, and the substrate named on the counter's second line is the binary I hashed myself, unchanged since 17:50:30Z.

# Residual risk and verification gaps

- The substrate line (path/sha/bytes) is authored by the measured revision's own `verify_surfaces.py`, so a revision could print a fixture path there; my independent hash confirms the printed path is the live host artifact, but the deeper guard (gate reads host binary vs fixture; independent `strings` dump) belongs to the erratum guard seats (CriticC1Sizing patch B), not this seat.
- The counter trusts the revision's gate for P, `opencode_extract` status and self-test parsing (patches A–D, F); not attacked here — out of this seat's target.
- The artifact filename `opencode.exe` under `node_modules/opencode-ai/bin/` on Linux is unusual but is the npm package's own naming and hashes to the plan-declared sha, so the plan measured the same bytes; no finding.
- Exact UTC wall-clock stamps for the three counter runs are inferred (~20:37Z) from the 20:36:39Z probe in the same sequence; outputs and exit codes above are verbatim.
