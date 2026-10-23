Result: DONE — read-only report-hash checker delivered at `.ufo/waves/round-57/build/check_report_hashes.sh` (sha256 `89bfbbc8…`); it flags exactly `40c2b5eb`, `41c2f484`, `7639deba` on the round-56 report (exit 1) and exits 0 on a synthetic report whose only non-commit hash is a labelled sandbox hash; usage errors exit 2.

## Deliverable

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/build/check_report_hashes.sh`
- 2944 bytes, mode `-rwxr-xr-x`, sha256 `89bfbbc8ce03ce0f8f309bc0f9b968ad7ec626bff7d650bc59ce389c92edf3ef` (2026-10-23T04:49Z).
- `bash -n` exit 0; `shellcheck -S warning` (ShellCheck 0.11.0) exit 0.
- Not under `verifiers/`, as required. It is a report-dir artifact; the L1 integrates/commits it.

## Contract

```
check_report_hashes.sh <lane-repo> <report.md>
```
- Candidate token: a hex run of 7–40 chars that is not part of a longer hex run. The boundary lookarounds mean a whole 64-char sha256 never matches, while a short prefix is a candidate.
- Skip: a token on any line containing `sandbox` (case-insensitive) — a labelled sandbox hash per the round-57 bounds; a token introduced by a digest marker (`sha256`, `sha-256`, `sha512`, `sha1`, `md5`, `blake2`, `b2sum`, `cksum`, `digest`, `hash`) followed only by up to three non-alphanumeric characters (spaces, backtick, colon). The marker test is per token, on the text before that token.
- Resolve: `git --no-optional-locks -C <lane-repo> rev-parse --verify --quiet <token>^{commit}`. An ambiguous prefix fails `--verify` and is therefore reported. Ambient `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` and friends are unset first.
- Output: one line per offending occurrence, `<report>:<line>: <token>` on stdout; nothing else on stdout.
- Exit: 0 no offender; 1 at least one (all printed); 2 usage error (argument count ≠ 2, repo not a directory or not a git repo, report not a readable file, mktemp mismatch, git/python3 missing, or the scanner exiting nonzero — a failed scan never passes silently).

## Evidence — round-56 report (fails as intended)

```
$ ./check_report_hashes.sh /home/vgpnk/Projects/shokunin/kotoba-shokunin /home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 40c2b5eb
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 41c2f484
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 7639deba
exit=1
```

Exactly the three expected unlabelled sandbox hashes (all on line 14, the control-call paragraph). No other token is printed: the 8-char commit prefixes `f897d18a` and `b0b7140b` resolve in the lane, and both sha256 prefixes are skipped.

What the digest filter is doing (calibration probe: a one-off copy with the DIGEST regex disabled, run on the same report):

```
...kotoba.md:14: 40c2b5eb
...kotoba.md:14: 41c2f484
...kotoba.md:14: 7639deba
...kotoba.md:14: 2f672bd1
...kotoba.md:15: 73497d2a
...kotoba.md:55: 2f672bd1
exit=1
```

So the un-filtered check would add three false hits: `2f672bd1` (line 14 and line 55) and `73497d2a`, all sha256 prefixes of the counter bytes, each written as ``sha256 `2f672bd1…` `` / ``(sha256 `73497d2a…`)``. The delivered checker skips them because the digest marker immediately precedes the token. Full digests need no filter: the 64-char sha256 bound already excludes them (probe: a report containing only a 64-char hex run exits 0, see below).

The three tokens do not resolve in the lane, while the report's commit tokens do (read-only checks, `git --no-optional-locks`):

```
40c2b5eb: unresolved   41c2f484: unresolved   7639deba: unresolved
f897d18ae9eca90d… (full): resolves   b0b7140b5a7cf8a5… (full): resolves   0f58a469: resolves
```

## Evidence — synthetic pass (sandbox hashes labelled)

Scratch file `/fast/scratch/hyaku/kotoba-r57/ExecR1HashCheck/synthetic-pass.md` cites lane tip `27af04a` (resolves), a full 64-char sha256, two digest-marked prefixes, `sandbox f259a70c (/fast/scratch/hyaku/kotoba-r57/ExecR1HashCheck)` and `Sandbox: f259a70c …` (capital S).

```
$ ./check_report_hashes.sh <lane-repo> synthetic-pass.md
exit=0
```

`f259a70c` is a real commit I made inside my sandbox clone (labelled per R1: sandbox f259a70c (/fast/scratch/hyaku/kotoba-r57/ExecR1HashCheck)); it does not resolve in the lane (`rev-parse` exit 1) and does resolve in the clone (exit 0). The pass therefore comes from the sandbox label, not from accidental resolvability.

Negative control — the same hash with the label removed must fail, so the pass is not vacuous:

```
$ ./check_report_hashes.sh <lane-repo> synthetic-fail.md
...synthetic-fail.md:5: f259a70c
...synthetic-fail.md:6: 0123456789abcdef0123456789abcdef01234567
exit=1
```

(The fabricated 40-hex is caught; the `sha256 2f672bd1…` line in the same file is not printed.)

Per-token marker check (one line holding both a digest and an unlabelled hash):

```
$ ./check_report_hashes.sh <lane-repo> synthetic-mixed.md
...synthetic-mixed.md:3: f259a70c
exit=1
```
on `sha256 2f672bd1… and commit f259a70c on one line.` — only the commit-shaped token is reported.

## Evidence — exit codes

```
benign report (no hashes):                     exit=0
report with only a 64-char hex run:            exit=0
no args:                                       exit=2
one arg:                                       exit=2
three args:                                    exit=2
missing report file:                           exit=2
repo path is a plain dir (/tmp):               exit=2
report path is a dir:                          exit=2
TMPDIR=/nonexistent-r1 (scan cannot start):    exit=2
```

Also verified: the checker is path-independent (run from `/tmp` with absolute paths, same round-56 output), and running it with the sandbox clone as `<lane-repo>` reproduces the same three findings, confirming resolution is against the repo argument, not the caller's cwd.

## Known limits (calibration)

- A bare digest prefix with no marker word (`the digest is 73497d2a`, or a naked `bf11a4efc1c7589a`) is reported as an unresolved hash. This is a deliberate false-positive: a hash token with no label and no digest marker is exactly what R1 asks to surface. The marker must be adjacent (spaces/backtick/colon only); `digest 73497d2a` is skipped, `digest is 73497d2a` is not.
- The sandbox skip is a line-level literal, as specified: any unlabelled non-commit hash sharing a line with the word "sandbox" is skipped (false negative by construction), and any line containing "Sandbox"/"SANDBOX" is treated the same.
- A hex-looking word or path fragment of 7–40 hex chars (e.g. inside a filename) would be reported; no such token occurs in the round-56 report.
- Not measured: whether a resolving token actually belongs to the lane's intended history (a truncated foreign hash could collide); only 7-char+ ambiguity is excluded by git.

## Hygiene

- Wrote only the delivered script and this report in the lane; no git/jj writes in the lane or fleet, no edits to counters, `verifiers/`, SKILL.md or any other lane file.
- The only commit I made is inside my clone: sandbox f259a70c (/fast/scratch/hyaku/kotoba-r57/ExecR1HashCheck), checked out at 01312a77e36317feb6e961aba77841ddab1225ca.
- Installs: none (ShellCheck 0.11.0 and python3 were already present; no pacman).
- All commands were wrapped in `timeout`; no processes were killed; no background jobs started.
