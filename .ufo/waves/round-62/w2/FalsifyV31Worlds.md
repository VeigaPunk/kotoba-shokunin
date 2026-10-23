# FalsifyV31Worlds — v3.1 successor re-run + guard-scope audit (round-62 wave 2)

Seat: `L1kotoba62.FalsifyV31Worlds`. Lane tip under test: `e6da78bbe420722dd18a13182a7c4b64ce02f005`
(`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `e6da78b…`, 2026-10-23).

## Verdict

**PASS.** Both frozen commands re-run at the committed bytes reproduce
`.ufo/waves/round-62/C1-v31-successor.txt` byte-for-byte (diff exit 0 on each
recorded block). The frozen counter is byte-identical to the r61 pin. The
frozen→v31 diff is confined to the declared E2c/E2e/E2f guards plus self-test
arms; no unrelated arm or world path changed. Findings below are LOW severity.

## Evidence (every number carries its command)

1. Byte identity, worktree and committed blob:
   - `sha256sum verifiers/check_scoped_rules.py` →
     `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
     (matches plan pin and receipt line 4). `git show HEAD:verifiers/check_scoped_rules.py | sha256sum`
     → identical. Last change commit `git log -- verifiers/check_scoped_rules.py`
     → `6a7f722` (round-61 C1 freeze); the pin reaches back to the r61 freeze, not
     a silent re-freeze.
   - `sha256sum verifiers/check_scoped_rules_v31.py` →
     `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`
     (matches receipt line 3 and the self-test's own `counter sha256` line).
     `git show HEAD:verifiers/check_scoped_rules_v31.py | sha256sum` → identical;
     blob `b2ca693` landed in tip commit `e6da78b`.
   - Receipt file itself committed in `e6da78b`, worktree bytes identical:
     `sha256sum .ufo/waves/round-62/C1-v31-successor.txt` =
     `git show HEAD:… | sha256sum` = `b8399baa15f6242c…`.

2. Self-test re-run (lane tip, committed bytes):
   `python3 -B verifiers/check_scoped_rules_v31.py --self-test` → exit 0;
   stdout mechanically diffed against receipt lines 8–29 → `diff` exit 0.
   Reproduced: `worlds reject 7 of 7; eligible rows pass 4 of 4`;
   `survivors closed 5 of 6` with `e2f-compound-purpose-outside-citation`
   still accepted (the declared G9 bound, printed honestly);
   `must-fail` arms print `yes` for both the E2e guard mutation and the G7
   mutation; `self-test: 0 failure(s) over 201 assertions`.

3. Fetch arm re-run:
   `python3 -B verifiers/check_scoped_rules_v31.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch`
   → exit 0; output byte-identical to receipt lines 32–38 (diff exit 0):
   `scoped rule files backed on committed snapshots 4 of 4; found on the live
   page 4 of 4`, canonical scope keys line, three client rejects (Codex,
   Gemini CLI, opencode). The `--rev` is the pinned r60 data revision, not the
   lane tip — frozen-predicate semantics, consistent.

4. Guard-scope audit: `diff -u verifiers/check_scoped_rules.py
   verifiers/check_scoped_rules_v31.py` → 11 hunks, +174/−21. Every non-test
   hunk maps to a declared survivor class:
   - E2c (A4(iv)): `FETCHED_ISO_RE` (line 334); `alias_sha_why` now binds the
     `supersedes S###` target to the base row owning the sha and rejects a
     `fetched <ISO>` assertion in the teaches cell (lines 1236–1252). Sole
     consumer: the A4 arm at line 1439.
   - E2e (A1 key form): `KEY_SUFFIX_RE` narrowed `["'`]?[ \t]*[:=]` →
     `["'`]?[ \t]*:` (line 401); `KEY_NEGATION_RE` (402); `_yaml_comment_start`
     + `key_site_guard` (953–979) wired into `key_site` (988) and `path_site`
     (1107). `KEY_SUFFIX_RE`/`key_site_guard` have no other consumers (grep:
     only lines 990, 988, 1107, 1109 plus self-test mutation at 2589–2594);
     `key_site` also feeds `any_key_site` → the live-page check (1320), which
     is inside the A1 arm — in-scope.
   - E2f (G7): `BACKTICKED_IDENTIFIER_RE` (405); `g7_conjunct` (1046–1058)
     appended as `action_conjunct`'s return (1088). Sole consumer chain: A2
     arm at 1463.
   - Self-test: verdict updates (equals→False, commented/negated keys→False,
     matching-vs-wrong supersedes target, fetched-timestamp reject, G7 unit
     check) and the survivor catalogue arm (2537–2612) that imports
     `check_erratum_absorption.py`, re-derives `before` verdicts against the
     pinned frozen module, and runs the two must-fail guard mutations.
   The instrument pin is real: `check_erratum_absorption.py` lines 15–97 set
   `COUNTER_SHA256 = 5a5adc94…` and `load_counter` raises `CounterPinMismatch`
   on file bytes *and* on `counter.self_sha()` — v31's "before" column is
   measured against the actual frozen bytes, fail-closed.

## Findings (LOW; none falsify the claim)

- **F1 — `receipt_rev` predates the file it measures.** Receipt line 2 is
  `receipt_rev=f9ab0812…`; `git ls-tree f9ab0812 -- verifiers/check_scoped_rules_v31.py`
  is empty — v31 landed only in `e6da78b`. The measurement was made on the
  working tree pre-commit. No dishonesty (the printed `counter sha256
  a07c2269` equals the committed blob), but the rev field does not name a
  revision containing the measured bytes.
- **F2 — Negation guard is a line-scoped prefix heuristic, broader than the
  measured classes.** `key_site_guard` rejects a key if
  `do not use|don't use|never use|avoid` appears *anywhere before the key on
  the same line* (`KEY_NEGATION_RE.search(line[:position])`). An honest line
  such as `Avoid broad globs; paths: src/**/*.ts` loses its site — an
  over-rejection surface the frozen E2e instances do not exercise (they are
  `Do not use paths: …` and comment cases). Not contradicted by the receipt;
  a strictness/scope note on the E2e guard.
- **F3 — Undeclared runtime dependency in the self-test.** v31 `--self-test`
  now imports `verifiers/check_erratum_absorption.py` by sibling-path
  (`with_name`) and binds to its internals (`COUNTER_PATH`, `ERRATA`,
  `attack.ident/score`, `load_counter`). Absence/rename of the instrument
  makes `--self-test` raise `EnvError` → non-zero. The survivor arm is
  defined in terms of the frozen catalogue, so the coupling is principled,
  but it is a new failure mode not present in the frozen v3 self-test.
- **F4 — Stale header.** v31's module docstring still reads
  "check_scoped_rules.py -- frozen counter for the round-61 C1 claim (v3)";
  identification is by printed sha256, so cosmetic only.
- **Observation (not a defect):** `g7_conjunct` rescues a backticked
  identifier absent from the cited line if it occurs anywhere in the page
  text (`token not in raw_line and token not in raw_page`). A cell citing
  line L can borrow a token from an unrelated line — a partial conjunct,
  consistent with G9 being the declared remaining bound, but weaker than a
  line-local reading of "raw evidence".

## Residual risk / verification gaps

- The 201-assertion self-test was re-run, not re-derived; individual A-arm
  unit probes beyond the receipt's printed lines were not independently
  re-attacked here (sibling seats cover the matrix instances).
- `--rev 43fe0180…` fetch hit the live page once (4 of 4); live-page drift
  after receipt time could flip this arm at any re-run — it matched today.
- Lane working tree carries unrelated in-flight modifications
  (`w1/ScribeEntry62.md`, `w1/ScribeLessonQ57.md`, untracked w2 files);
  verifier bytes themselves are clean at HEAD.

## Tooling

No installs (system `python3`, `git`, `diff`, `sha256sum` sufficed; pacman
paused, nothing needed beyond stock tools).
