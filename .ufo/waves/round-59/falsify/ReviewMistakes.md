Result: HOLDS — all five 'shown able to fail' commands re-run byte-match their recorded outputs, every captured-by and fix is accurate against the landed artifacts, and M84 is a real, accurately-captured process mistake whose fix is implemented and whose fail-command reproduces (12 ≥ 1).

# Scope and method

Reviewed `corpus/lessons/round-59.md` `## Mistakes` (lines 36–55, M79–M84; line numbers below are at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`). Read-only lane access; all evidence dumps in `/fast/scratch/hyaku/kotoba-r59/ReviewMistakes/`. No tools installed or upgraded. No network fetches made by this seat (all cited bytes are lane-tracked or `.ufo`-external files; the one external scratch path cited by the lesson still exists and was read). Commands were re-run verbatim as printed in the lesson; `rc=` echoes were appended only to capture exit status.

# M79 `misrooted-seat-report-and-premature-sweep` (lesson :41) — HOLDS

- Re-run: `timeout 5 ls /home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` → exit 0, stdout exactly `/home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md`. Byte-matches the recorded claim.
- captured-by: `corpus/lessons/round-58-verifier-spotcheck.md:243-252` = routed defect R1; the block names the fleet-root write (10,299 B, mtime 05:34:09-03:00), the seat-paragraph omission, and the stale misroot sweep (snapshot 08:27:59Z). Accurate.
- fix: `.ufo/waves/round-59/bounds.md` bullet 2 pins the output directory into the lane and names the exact R1 misroot path as WRONG — landed. The copy+provenance leg (from the R1 spotcheck fix) is also done: `ReviewBudgetMove.md` + `ReviewBudgetMove.provenance.md` are tracked at tip `3f15f84`, committed by `a3e70a3` ("R1 misroot copy"); they are absent at `ed44e0c4` as expected.
- Caveat (fix implementation, not a claim error): the "rerun the sweep after the last seat settles" leg is not yet executed — `ScoutMisroot.md` mtime is still 05:28:13 -0300 (snapshot 08:27:59Z, before the report write), and no round-59 misroot sweep receipt exists in `.ufo/waves/round-59/falsify/` as of 2026-10-23T10:06Z. `build/ScribeLogDraft.md:13` schedules it ("run and commit the misroot sweep after the last seat settles"). Outstanding at wave close, not a false claim.

# M80 `final-tip-receipts-asserted-not-committed` (lesson :43) — HOLDS

- Re-run: `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only ed44e0c4807b92d99417eaff04a0fd2122f981b4 -- .ufo/waves/round-58 | grep -E 'verify_skill_checklist|checklist.*tip'` → exit 1, no output. Byte-matches.
- captured-by: `corpus/lessons/round-58-verifier-spotcheck.md:253-257` = R2 (asserted `verify_skill_checklist.py` exit 0 and "4 DRIFT" at `ed44e0c4` without receipts). Accurate.
- Evidence files cited by the lesson check out: `.ufo/waves/round-58/noharm-tip.txt:2` records `measured rev 46b4a706…`; `.ufo/waves/round-58/C1-remeasure-tip.txt:4` records `counter rev 6de8e2eb…` and `:24` shows `FAIL governance.citation_resolves` — "where the checklist fails" is accurate.
- fix: implemented. `.ufo/waves/round-59/receipts/tip-r58-ed44e0c4.txt` is committed at `c63ccc68` (ls-tree confirms) and records checklist exit 0 (11/11) plus exactly 4 DRIFT at `ed44e0c4` (`w0/ExecR2TipReceipts.md:1,22,37`); sibling receipts `base-r59-a975cbbf.txt`, `noharm-base-selftests.txt`, `noharm-tip-selftests.txt`, `data-r59-c63ccc68.txt` are all revision-named. `.ufo/waves/round-59/C1-measure.txt` (committed at `d64d945`, blob `bf7bc16b`) names the measured rev, counter sha256, the `--fetch` run, and the committed-bytes second run.

# M81 `counter-blind-fields-and-ua-sensitive-fetch` (lesson :45) — HOLDS

- The shown-able-to-fail is honestly marked "the earlier seat's recorded run, not a run by me" — I verified the record rather than re-running it. `.ufo/waves/round-58/falsify/MutC1Content.md:146-161` records mutant (f) verbatim: sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` (confirmed present: `git -C /fast/scratch/hyaku/kotoba-r58/MutC1Content cat-file -t` → `commit`), stdout `custom command files found on the live page 6 of 6; new ground 4` + `exit 0`, verdict "SURVIVED and invisible to this detector", `f_stdout_equals_pristine_except_rev: true`.
- `.ufo/waves/round-58/falsify/ReopenS094.md:46-48` (F1): cursor.com returns HTTP 403 to the counter's own Python-urllib request shape (UA `kotoba-shokunin-counter/58`) while curl gets 200 with byte-identical page; degraded run sits at `G=3 = NEW_TARGET=3` — "moving G to its floor" is accurate (it is exactly the floor, not through it).
- Frozen-source pointer `.ufo/waves/round-58/w0/check_command_files.py:762-783`: confirmed that region parses the SKILL command cell for the backticked token (`spans = BACKTICK_RE.findall(sr[1])`); the blindness to the sets cells is established by the mutant record. `corpus/lessons/round-58-verifier-spotcheck.md:258-262` = R3. Accurate.
- fix: implemented in the round-59 counter and wave. `verifiers/check_hook_files.py:112-120` docstring: "EVENTS CELL (round-58 routed defect R3, the field check)" — the counter now scores the field cell (the round-59 table's `Events` column, `SKILL.md:125` header `| Client | Hook config | Events | Action |`); `:126+` "SNAPSHOT (round-58 routed defect R3, the reader check)" binds committed snapshots; `build/ScribeLogDraft.md:13` records "counter reads Events field cells, binds each committed snapshot to the SOURCES sha256, and fetches with curl plus browser User-Agent". The "name the seat that checks them" leg is also satisfied: falsify seats `Cells<Client>.md` (e.g., `CellsVSCode.md`) review the remaining cells at `c63ccc68`. Committed `--fetch` snapshot run = `C1-measure.txt` + `snapshots/S096-S101.page` tracked at `c63ccc68` (ls-tree count 6). Counter sha256 verified: `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`.

# M82 `budget-delta-started-at-freeze-not-base` (lesson :47) — HOLDS

- Re-run: `timeout 20 bash -o pipefail -c 'for r in f56f6e191762c27c1aa2af11a204db9e2ca4edec 3de87aad29e960c95ed35840442f424c48c29729 ed44e0c4807b92d99417eaff04a0fd2122f981b4; do printf "%s SKILL.md lines: " "$r"; git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show "$r:SKILL.md" | wc -l; done'` → exit 0; output `…f56f6e19… 598`, `…3de87aad… 600`, `…ed44e0c4… 596`. Byte-matches: base 598, freeze 600, tip 596 — "600 → 596 counted from the freeze" is correct.
- captured-by: `corpus/lessons/round-58-verifier-spotcheck.md:265-266` = R5. Accurate.
- fix: implemented. `build/ScribeLogDraft.md:13`: "every budget line uses base SKILL.md count 596 at `a975cbbf`" — verified independently: `git show a975cbbf:SKILL.md | wc -l` → 596. `build/ExecBudgetMove.md:3` states the freeze rev and count (`67b68e0f`, 597 lines) for the round-59 delta.

# M83 `source-anchor-label-not-page-heading` (lesson :49) — HOLDS

- Re-run: `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -o -F '§ Where skills live' ed44e0c4807b92d99417eaff04a0fd2122f981b4 -- corpus/SOURCES.md` → exit 0, stdout `ed44e0c4807b92d99417eaff04a0fd2122f981b4:corpus/SOURCES.md:102:§ Where skills live`. Byte-matches.
- Page side: the `.ufo`-external snapshot `/fast/scratch/hyaku/kotoba-r58/SrcClaudeCode/claude-slash-commands.md` exists (114,542 B), sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` — identical to the S089/S102 fetch sha. Line 152 reads `## Choose where skills load` exactly; line 172 (S089's `:172` pointer) is a bullet about Command files, not a heading — the old anchor matched no heading at its cited line, so the defect was real.
- captured-by: `corpus/lessons/round-58-verifier-spotcheck.md:263-264` = R4. Accurate.
- fix: contract citation `CORPUS.md:112-118` (fleet-root file; lane has no `CORPUS.md`) confirmed: append-only, only `status`/`recheck`/`used-by` change in place, corrections are new `supersedes S0NN —` rows. `corpus/SOURCES.md` diff `ed44e0c4→c63ccc68`: zero `-` data lines, seven `+` rows S096–S102 only — S089 byte-identical as claimed; S102 row (`corpus/SOURCES.md:114`) opens `supersedes S089 —`, anchor `§ Choose where skills load (slash-commands.md:152)`. `build/ScribeR4Note.md` exists as cited.
- Note: `snapshots/` holds S096–S101 only; S102 has no committed `.page` (consistent with the claim-under-attack's snapshot enumeration and with the S102 row carrying no snapshot path). The anchor's page-side evidence is the external scratch file + sha-identity — re-fetchable but not committed. Residual risk, not a defect of the mistake record.

# M84 `census-token-substituted-without-rescore` (lesson :51–55, the mined mistake) — HOLDS as a real mistake

- Re-run: `grep -c 'audit.json' .ufo/waves/round-59/w0/CensusVSCode.md` → `12` (≥1), exit 0; the freeze plan's VS Code row `plans/round-59.md:69` (verified at both `4b2125c9` and `c63ccc68`, identical) leads with `.github/hooks/*.json`. Both halves of the fail-command hold.
- Mistake chain verified: `w0/CensusVSCode.md:1` "Result: DONE — VS Code: ELIGIBLE `.github/hooks/audit.json`", `:3` says the wildcard "also passes the path grammar, but Copilot CLI's hooks reference prints that same token, so a Copilot row that leads with it is E5 (both rows out)", with a dedicated "`### .github/hooks/*.json` — fails E5" section — "E5-rejected on the premise that Copilot CLI would lead with it" is accurate. Draft `a3e70a3` contains no VS Code census row; the row was introduced at the freeze (`4b2125c9` diff shows `+` lines 69–70) with the substituted token and the in-cell note — so the L1 substitution happened at freeze, before any seat re-score (SrcVSCode is a build-wave report). The build context repeated it as the census: `build/SentinelContexts.md:26` quotes `build-spec.json:12,31-36` listing the wildcard as the S098 census lead against `CensusVSCode.md:1-3,76-85`.
- captured-by: `SentinelContexts.md:1,26` (MIXED, names the discrepancy and impact) and `ScribeEntry.md:1,11-13,53` (MIXED, verbatim-conflicts census :1/:3 vs plan :69; "the conflicting census finding is recorded"). Accurate — both flagged it.
- fix verified component-wise:
  1. In-cell disclosure: `plans/round-59.md:69` — "(the seat's lead was the example file `.github/hooks/audit.json`; the folder pattern is the documented location)". Present at the freeze itself.
  2. Re-score by a seat: `build/SrcVSCode.md:1,5,62,79-86` — counter sha `f695d59e…`, `quote_why`/`event_on_page`/`events_cell_why`/`page_why`/`run_curl` on the committed snapshot AND a fresh live fetch via the counter's own curl fetcher: `snapshot_quote True`, `live_quote True`, all nine events True on both, `snapshot_page []`, `live_page []`. Its scope note ("full C1 counter not run; only S098's quote/events checks") matches the fix's exact wording "quote and event checks" — no overclaim.
  3. "Copilot row leads with its own path so E5 does not fire": counter E5 compares the first backticked span per client row (`check_hook_files.py:143,775,2076-2088`); `corpus/knowledge/hook-files-round59.md:31` Copilot row leads `~/.copilot/hooks/*.json` vs VS Code `.github/hooks/*.json` — no collision; the committed `--fetch` run exited 0 with 6 of 6 (`C1-measure.txt`).
  4. The rule for next rounds is stated in the M84 text itself.
- Judgment: the mistake is real — a process defect (substituted at freeze without pre-freeze rescore; build context propagated it as the census lead while the census report said the opposite), even though the end-state row proved counter-valid (exit 0, 6 of 6). The name matches the verified facts; the shown-able-to-fail reproduces the mismatch signature.

# Header paragraph (lesson :38–39) — accurate

"M79–M83 are the round-58 spot-check routes R1, R2, R3, R5 and R4" — order verified against `spotcheck.md:243,253,258,265,263`; `build/ScribeMistakes.md` exists as named; M84 is correctly identified as this round's own.

# Findings by severity

- **None breaking.** Every re-runnable command reproduces its recorded output byte-exact; every captured-by and fix citation resolves and is accurate.
- **Watch (implementation timing, not a claim defect):** M79's "rerun the sweep after the last seat settles" is unexecuted as of 10:06Z; `ScoutMisroot.md` still predates the report write. Prescribed in `ScribeLogDraft.md:13` — must land at wave close.
- **Residual risk:** S102 (the M83 fix row) has no committed `.page` snapshot; its anchor evidence rests on the external round-58 scratch file (sha-identical, still present) rather than committed bytes.

# Verification gaps

- M81's shown-able-to-fail is a recorded prior-seat run, not re-executed by me — the record file, verdict and named sandbox commit all verify, but I did not replay the mutant counter run.
- M79's `.provenance.md:3-10` and `ScoutMisroot.md:3-27` line-pin contents were spot-checked by existence and the sweep's dated snapshot, not line-by-line.
