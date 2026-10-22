# ReviewDriver: verifiers/box_proof_case_deletion.py at 956ee1676e4c18480bce8ac3993541462be76e11

Verdict: HOLDS-BOUNDED. At 956ee the driver prints `killed 6 of 6` (exit 0) on claimed revision 542f515 and on 956ee, and `killed 0 of 6` on base f3046464 (exit 1). It aborts with exit 2 when the intact proof fails, removes its temp directory on every path I ran, and writes nothing into the checkout. Two error paths crash with a traceback instead of exiting 2, and the kill test accepts any stderr that contains the name, so the count is only as strong as the instrument's own message. Applies to honest instruments at this commit.

## Answers to the assigned questions

1. Read-only on the lane: yes. The only git call is `git -C <root> archive --format=tar <rev>`, unpacked with `tarfile` into a `TemporaryDirectory` (lines 120-145, 233-238). Every write goes to the temp tree: the manifest rewrite targets the export (line 292) or a copied fixture dir (lines 287-289). Scratch clone `git status --porcelain --ignored` printed 0 after the default, in-place, 542f515, f3046464 and error-path runs. I did not run the driver against the lane checkout itself (bounds); the code path is the same at that commit.
2. Kill rule: implemented as stated (`classify`, lines 191-206). Exit must be exactly 1; stdout must hold an exact line `boxes proven 0` or `boxes proven 1`; stderr must contain the conjunct name. The name test is a substring test over the whole stderr, not a test on the line for the deleted case (F1).
3. Denominator pinned: yes. `CONJUNCTS` is a six-entry constant (lines 68-75) and the printed total and exit test use the literal 6 (lines 340, 344). The manifest only chooses which case gets deleted (`pool[0]`, lines 302-313).
4. Abort on a failed intact proof: yes. Lines 257-265 return 2. Adversarial advA (box proof always exits 1) gave exit 2 and no kill lines.
5. Temp cleanup: yes. `TemporaryDirectory` (line 233) cleans up on normal return, on the exit-2 abort, and on both traceback exits. Leftover count after each run was 0.
6. Adversarial revisions: see the table below.

## Findings, by severity

F1. Medium. Kill naming is a substring test over all of stderr. In advB (commit 8f01966) the intact corpus exits 0, and any reduced corpus exits 1 with stdout `boxes proven 1` and one stderr line naming all six conjuncts. The driver printed six `exit 1 killed` lines, `controls killed 2 of 2`, `na killed 1 of 1`, `killed 6 of 6`, and exited 0. The counter cannot tell a conjunct-specific failure from a generic one. The real instrument does attribute its failures (see the probe below), so this is a weakness of the test, not a present false kill. Fix: require the instrument's own problem line, `box-proof: <box>: no isolated must-fail case for conjunct <name>` (or `no N/A case for conjunct ...`), with the box id on the same line.

F2. Medium. An unknown revision crashes instead of exiting 2. `--rev 0000000000000000000000000000000000000000` ends in `tarfile.ReadError: empty file` with exit 1 and no `ERROR` line. Cause: `tarfile.open(..., mode="r|")` reads the first member (line 131) before the git return code is checked (line 141), and `main` catches only `DriverError` (line 239). Fix: check the git return code first, or run `git cat-file -e <rev>^{commit}`, and turn `tarfile.TarError` into `DriverError`.

F3. Medium-low. A malformed manifest crashes instead of exiting 2. advC (commit 6ef54f4, manifest `{"cases": [`) ends in `DriverError: cannot parse .../manifest.json (Expecting value: line 2 column 1 (char 12))`, exit 1. `read_manifest` (line 254) sits outside any `try`. Fix: catch `DriverError` around the whole body of `main` after the export and return 2.

F4. Low. Control naming differs from the docstring. Docstring lines 39-40 say "for a case that declares no conjunct: its id". Code line 325 uses `[case.get("id"), case.get("check")]`. In the clean probe, deleting `d04-control` printed only `box-proof: dispatch.04: no all-PASS control case`; the id `d04-control` never appears. So `controls killed 2 of 2` counts box-level messages. It does not change `killed K of 6` or the exit code. Fix: name the control id in the instrument message, or change the docstring.

F5. Low, not run. `run_box_proof` (lines 186-187) uses `timeout=600` and handles neither `subprocess.TimeoutExpired` nor `OSError`. Either would give a traceback and exit 1, as in F2 [INFERENCE from reading the code].

F6. Info. Coverage is one case per conjunct: `pool[0]` (line 313). A second must-fail case for the same conjunct is never deleted. The `survived (absent)` branch (lines 309-312) was not exercised at any revision I ran: at 956ee the control aborts first, and at f3046464 all six cases exist.

F7. Info. Extraction calls `tar.extract(member, dest)` with no filter. On Python 3.14.8 here the default is `data_filter` (checked in `tarfile.py`). Older Pythons may extract unfiltered [INFERENCE from PEP 706; not run]. The rev holds 6039 symlinks, all with absolute targets and none relative (counted with a script). `safe_member` skips all of them, so no extraction failed.

## Adversarial revisions

Scratch clones `advA`, `advB`, `advC` are commits on top of 956ee. The driver was run from the scratch clone with `--rev HEAD --repo <clone>`.

| clone (commit) | change | driver output | exit |
|---|---|---|---|
| advA (0a00caa) | box proof always exits 1 | `control: exit 1 boxes proven 1`; `ERROR the intact box proof at HEAD does not exit 0; case coverage is not measurable`; no kill lines | 2 |
| advB (8f01966) | exits 1 on any reduced corpus, names all six conjuncts | `killed 6 of 6`, `controls killed 2 of 2`, `na killed 1 of 1` | 0 |
| advC (6ef54f4) | manifest is `{"cases": [` | `DriverError ... cannot parse` traceback | 1 |

## Measured results

- `--rev 956ee1676e4c18480bce8ac3993541462be76e11` (default mode): exit 0. Control `exit 0 boxes proven 2`. All six `exit 1 killed`. `controls killed 2 of 2`, `na killed 1 of 1`, `killed 6 of 6`. Stderr empty. Leftover temp entries 0.
- Same rev with `--in-place`: exit 0, same counts, leftover 0.
- `--rev 542f515672306e1baefcb69ba79f1d4c18b6450e`: exit 0, `killed 6 of 6` (matches the claim).
- `--rev f30464660c675d1c1e2851a3bf0366a3aaffe5a8`: exit 1, all six `exit 0 survived`, `killed 0 of 6` (matches the claim).
- `--repo <directory with no .git>`: exit 2, `ERROR ... is not a git checkout`.
- Clean probe: each of the six must-fail deletions gave exit 1, stdout `boxes proven 1`, and one stderr line naming the conjunct. d04-placeholder: `no isolated must-fail case for conjunct report_path_literal`. d04-stem: `report_stem_is_lane_id`. d04-unknown-lane: `lane_identity_known`. d08-role-round: `filename_role_round_equal`. d08-report-dir-round: `filename_report_dir_round_equal`. d08-above-state: `round_le_latest_dispatched`. The N/A case gave `no N/A case for conjunct round_le_latest_dispatched`. Deleting d04-control or d08-control gave only the box-level `no all-PASS control case` line.

## Residual risk and verification gaps

- The lane checkout was not executed (bounds). The read-only result rests on code reading and the scratch clone.
- Not run: the 600 s timeout path (F5); Python versions other than 3.14.8 (F7); the `survived (absent)` branch (F6).
- A probe mistake: my first probe read its base manifest from a copy I had already edited (d04-control removed). Its box counts were wrong and I discarded them. Every number above comes from a clean copy or from the driver's own export.
- Tools: none installed or updated. Used Python 3.14.8 and git 2.56.0, both already present.
- Scratch: /fast/scratch/hyaku/kotoba-r50/falsify/ReviewDriver/ (clone `lane`; adversarial clones `advA`, `advB`, `advC`; probe copies `clean-fixtures`, `probe2-*`).
