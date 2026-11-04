# ReviewerCounter (r86-w1): scoped findings

The full review is `ReviewerCounter/review.md`. Receipts are in `ReviewerCounter/receipts/` and probe sources in `ReviewerCounter/probes/`.

Instruments tested:

- **frozen**: `check_omp_catalogue_repro.py` at ecfad51, sha256 `2390eec2…`.
- **a1**: the same file at b9ee548, sha256 `39a014f2…`, re-attacked at KotobaR86's request.

## Findings, by severity

1. **CRITICAL (frozen). The counter falls to a forgery with no omp work at all.** F1 stores the renders as split literals, F2 as a zlib+base64 key. Both offer one old `ufo/SKILL.md` for every name and use the ledger row `*<TAB>application/json`. Both score **215 of 215, G1–G4 PASS, exit 0**. Why it works:
   - G1 only rejects a string constant that exactly equals a render.
   - G2 does not tie the offered path to the name or the render.
   - G4 accepts `*`.
2. **CRITICAL (frozen). The sandbox leaks the catalogue in two ways.**
   - E1, network: the pinned fixture is served by raw.githubusercontent.com at the pushed freeze commit (sha matches the pin). **215 of 215, exit 0.**
   - E2: `~/.omp/logs/http-400-requests` (141 files) is visible inside the sandbox. **215 of 215, exit 0.**
   - Not escapes: `/proc/<pid>/root` and `/proc/<pid>/mem` return EACCES, and the other `~/.omp` stores hold 0 hits.
3. **HIGH (governance).** The frozen counter changed after the freeze: working-tree edits (`d6c403…`, then `3b4bb2…`), then the commit b9ee548. The plan's kill rule lists "counter changed after this freeze" with no exception for addenda. The closure must rule on whether addendum-1 is admissible. In its favour: ExecModel's `CANDIDATE_READY` (22:32:52Z) is later than the commit (22:27:12Z).
4. **HIGH (a1). G4's dot-directory rule is a substring test, so located but irrelevant quotes pass.**
   - F6: the base module plus one `USER_ROOTS` line, with quotes `app.agents.hub` and `ts to ~/.omp/agent/a`. **215 of 215, exit 0.**
   - F4: a root-blind `os.walk` brute force with an encoded oracle, citing `rototype.localeCompare` for `.local` and `-reslint.config.tstailw` for `.config`. **214 of 215, exit 0.** 51 of its lines come from roots (OpenBot, devin, fnm) whose path components occur 0 times in the ELF.
   - a1 does close F1, F2, E1 and E2 (0 of 215 / exit 2).
5. **LOW. Exit-ladder divergence.** Some could-not-evaluate states end in an uncaught traceback and exit 1 instead of 2: a `KeyError` on the frozen counter; an `AttributeError` and a `UnicodeDecodeError` ledger on a1. All fail closed.
6. **LOW (plan fact).** The plan says "15 of 215 lines are cached". Under the counter's key the measured count is **35**. 186 cache rows carry a `:anthropic/claude-haiku-5-5` key suffix that the counter's key never matches; today no verdict depends on them.

## Identity table

`review.md` § 1 has the full table. The headline, the 205 threshold, the G1–G4 conjunction and the self-test count all match the plan. The divergences are G1's scope, G2's binding, the isolation claim, the exit-2 coverage, and G2's "lane" when `--repo` is a scratch clone.

## Fixture verdict: CONFIRMED

- The `<skills>` block in line 7 of `KakeR90.jsonl` has sha256 equal to the fixture's, and its 215 `(name, render)` pairs equal the fixture entries in order.
- The 228 cache rows equal the live DB.
- The DB's ctime (21:02:19Z) and mtime (Oct 31) are before the render, and the WAL is empty, so no row was added after 21:55:22Z.
- A later row *could* flip a verdict: for the 35 cache-rendered names if their row were replaced, or for any of the 180 preview names if a row keyed by its description were added. No such row exists.

## Candidate

ExecModel's candidate (`bd793b6c…` / `36021309…`) re-scores on a1 at **215 of 215, exit 0**. G4 cannot tell its quote `var Gh = ".omp";` for the plugin root apart from F6's irrelevant quotes, so the verdict rests on ReviewerRoots.
