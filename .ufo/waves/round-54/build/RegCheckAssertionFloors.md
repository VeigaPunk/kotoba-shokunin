Result: DONE — prepared the C2 registry row from the assigned snapshot and recorded isolated help/self-test evidence.

| `verifiers/check_assertion_floors.py` | gate | `python3 -B verifiers/check_assertion_floors.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file; `verifiers/floors-registry.json` | fixture tempdirs under $TMPDIR; child self-tests | kotoba |

Evidence for each cell

- **Name:** `verifiers/check_assertion_floors.py:1-2,1206-1207` identifies the verifier and script entry point.
- **Kind:** `verifiers/check_assertion_floors.py:44-48,523-545` documents a read-only guard and gives clean/failure verdicts; it returns 1 for failed instrument summaries and 2 when the registry/anchor cannot be trusted, a declared path escapes, or a child self-test times out. It is a gate, not a probe.
- **Entry command:** In the sandbox clone at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, `python3 -B verifiers/check_assertion_floors.py --help` exited 0; the last output line was `                        temporary fixtures only`. `--repo` defaults to the repository containing the script (`:127`); the default run evaluates the instruments (`:453-461,523-545`).
- **Verdict map:** 0 = all instrument summaries meet their floors with zero failures (`:525-545`); 1 = a summary is missing/below floor/nonzero, or the self-test assertions fail (`:534-545,605-610,1200-1203`); 2 = registry/anchor/row/override drift or invalid paths (`:469-521`), child timeout (`:530-544`), or argparse usage error (`:461,499-504`). These are the only explicit return codes; argparse help exits 0 and its usage errors exit 2.
- **Self-test:** The literal flag is declared at `:459-460`. `TMPDIR="$PWD/.tmp/assertion-floor-self-test" python3 -B verifiers/check_assertion_floors.py --self-test` exited 0; last output line: `0 failure(s) over 150 assertions`. Runtime was 1.08 seconds. This mode writes temporary fixture trees (`:594-655,662`); I placed TMPDIR inside the sandbox clone, so no writes were directed outside it.
- **Pinned values:** The in-file expected floor table is `EXPECTED_INSTRUMENTS` (`:129-146`) and `INSTRUMENTS` carries the matching paths/floors (`:149-180`). `REGISTRY_REL` points to `verifiers/floors-registry.json` (`:149-151`), which `registry_anchor_drift()` cross-checks against both tables (`:312-388`). The JSON row has `floor: 150` and `path: verifiers/check_assertion_floors.py` (`verifiers/floors-registry.json:21-24`), matching the in-file `floors_guard` floor/path (`:141,170-171`).
- **Write scope:** The self-test creates fixture files/directories in `TemporaryDirectory` (`:594-655,662`) and cleans the temporary directory on exit. The default mode invokes child `--self-test` commands (`:525-529`). The `--script NAME=PATH` override can execute a supplied script, including a permitted unique-byte stub outside `--repo` (`:399-430`; fixture F25 at `:1111-1123`); callers should account for that override's behavior.
- **Owner:** The frozen registry-counter contract fixes the owner as `kotoba` (`verifiers/check_gate_registry.py:59-65,180-181`).

Mismatch check

- No conflicting floor/path was found. `floors-registry.json` agrees with the two in-file tables as shown above.
- At this snapshot SKILL.md has only the pointer to `§ Gate registry` (`SKILL.md:532-533`); no registry header or row for this verifier exists yet. `verifiers/README.md:3-6` says those registry rows live in SKILL.md and does not give a contrary verifier-specific claim. Search for `Gate registry|check_assertion_floors|floors-registry` in the three named files found only the SKILL pointer, README registry-home note, and matching JSON anchor.
