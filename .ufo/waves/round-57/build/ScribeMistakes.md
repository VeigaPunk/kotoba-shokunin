Result: DONE — drafted M58–M61 for the round-57 lesson and ran the two requested read-only falsifiers.

## Proposed `## Mistakes` section

- **M58 `sandbox-hash-unlabelled`** · `.ufo/reports/round-56/kotoba.md:14` cites `40c2b5eb`, `41c2f484` and `7639deba` without a `sandbox` label; the non-author spot-check says they do not resolve in the lane and are scratch-clone commits (`corpus/lessons/round-56-verifier-spotcheck.md:30-31,219-221`) · captured-by: the round-56 non-author spot-check (R1) · fix: label sandbox hashes with `sandbox` and their clone path in each context/report, or cite the committed receipt lines (`plans/round-57.md:81-85`; `.ufo/waves/round-57/bounds.md:4`) · shown able to fail: this read-only scan skips tokens explicitly introduced by `sha256` (digest prefixes, not commit references), checks unresolved 7–40-hex commit candidates with `git rev-parse --verify -q <h>^{commit}`, and prints the three unlabelled references:

  ```sh
  python3 -B -c 'import pathlib,re,subprocess; p=pathlib.Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md"); repo="/home/vgpnk/Projects/shokunin/kotoba-shokunin"; out=sorted({h for line in p.read_text().splitlines() if not re.search(r"\bsandbox\b",line,re.I) for h in re.findall(r"(?<![0-9a-fA-F])[0-9a-fA-F]{7,40}(?![0-9a-fA-F])",line) if not re.search(r"\bsha256\s+`?"+re.escape(h)+r"(?![0-9a-fA-F])",line,re.I) and subprocess.run(["git","-C",repo,"rev-parse","--verify","-q",h+"^{commit}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode != 0}); print("\n".join(out))'
  ```

  ```text
  40c2b5eb
  41c2f484
  7639deba
  exit code: 0
  ```

- **M59 `shaped-quote-note-unverified`** · the round-56 lesson's quote-note paragraph describes S076's project line and S078's fenced example inaccurately (`corpus/lessons/round-56.md:22-25`); the re-open found S076's quote verbatim but a better unshaped quote across `:320-323`, and that S078's `text` is a fence info string, not quote prose (`corpus/lessons/round-56-verifier-spotcheck.md:107-121,222-228`) · captured-by: the round-56 non-author source spot-check (R2) · fix: correct the S076/S078 notes (prefer S076 `:320-323`), accurately mark what was removed/normalized, and source or drop the separate `SKILL.md:109` clause as routed in R2 (`round-56-verifier-spotcheck.md:222-228`; `plans/round-57.md:83-85`) · shown able to fail: the source re-open caught the note/source mismatch for both entries; the spot-check says neither choice changed G's substance (`round-56-verifier-spotcheck.md:107-121`).

- **M60 `case-folded-held-ground`** · the round-56 counter case-folded held-ground counts and treated `.claude/AGENTS.md` and `.codex/AGENTS.md` as the lowercase agent directories, understating G (3 rather than 5) (`corpus/lessons/round-56-verifier-spotcheck.md:63-67,233-236`) · captured-by: the round-56 non-author spot-check (R4) · fix: the round-57 C1 v2 rule checks held paths case-insensitively at segment boundaries while keeping distinct new-ground values case-folded (`plans/round-57.md:35-40,114-118`; `verifiers/check_plugin_manifests.py:960-979`) · shown able to fail: CtlC1HeldVariant re-scored its exact v1 held-variant world under v2 as `0 of 0; new ground 0`, exit 1 (`.ufo/waves/round-57/controls/CtlC1HeldVariant.md:65-72`). This closes that world, but its bare tokens and duplicate rows also trigger other v2 guards, so it is not an isolated demonstration of the case-fold check. The frozen counter has explicit case-variant, segment-boundary and memory-file-analogue self-test cases (`verifiers/check_plugin_manifests.py:1681-1690`); I did not execute that self-test.

- **M61 `pattern-kill-no-cap`** · round-56's `ExecFloorsTimeout` used `pkill -f` on a shared scratch path, killed three sibling runs and ran a contention test that drove load to 96 (`.ufo/reports/round-56/kotoba.md:36`; `corpus/lessons/round-56.md:61-64`); R7 notes that M56's PID-only fix and contention cap had not been shown able to fail (`corpus/lessons/round-56-verifier-spotcheck.md:241-246`) · captured-by: the round-56 non-author spot-check (R7) · fix: round-57 bounds require killing only PIDs started by the seat and cap requested contention tests at 4 processes/120 seconds (`.ufo/waves/round-57/bounds.md:6`; `plans/round-57.md:85-87`) · shown able to fail: the required presence check distinguishes the old context from the new bound (the grep tests the PID sentence; the cap is independently visible on bounds line 6):

  ```sh
  grep -c 'Kill only by the PIDs you started' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-56/build-spec.json
  ```

  ```text
  0
  exit code: 1
  ```

  ```sh
  grep -c 'Kill only by the PIDs you started' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/bounds.md
  ```

  ```text
  1
  exit code: 0
  ```

## Scope and limits

- This is a draft for L1 to integrate; `corpus/lessons/round-57.md` was absent when read, and the binding bounds allow this seat to write only its own report (`.ufo/waves/round-57/bounds.md:2-3`).
- Touched surface: this report only, `.ufo/waves/round-57/build/ScribeMistakes.md`.
- No lesson, product code, verifier, counter, control, or judge was edited. No build, test suite, or gate was run; the only executed checks above were the requested read-only commit-reference scan and `grep -c` comparisons. No tools were installed or updated.
- The M61 grep detects the presence of the PID sentence; it does not independently prove a checker will reject an omitted contention cap. No claim is made that the lesson integration or a general context validator has been run.
