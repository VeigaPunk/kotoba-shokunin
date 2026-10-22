# SurfacesRepin — C1 freshness re-pin (omp 18.12.6), round 51 build

**Result: HOLD** — C1 counter `python3 -B verifiers/verify_surfaces.py --json` now prints `pass 7 / fail 0 / exit_code 0` against the installed omp 18.12.6; `--self-test` 115 assertions, 0 failures, exit 0; `check_assertion_floors.py` exit 0 (surfaces observed=115, floor=99 unchanged). The re-pin is allowlist `+Kl|Ho|bq` (exactly three names) plus a stated module-scope binding rule; baseline and inventory bytes are untouched.

## Findings

1. **Callee rename (18.12.6).** `strings -n 4 /home/vgpnk/.local/bin/omp` carries exactly 11 registration call shapes under callees `Kl` (5), `Ho` (4), `bq` (2), mapping one-to-one to the 8 declared omp loader-group pairs. The round-50 allowlist (`…|lq|Xl|Fo`) matches 0 shapes -> vacuity FAIL. Extended by exactly `Kl|Ho|bq` (append-only, per the file's own convention).
2. **`S$` conflict.** The live dump binds `var S$ = "title"` (strings line 843423, session/session-entries.ts) and `var S$ = "claude-md"` (line 895604, discovery/claude-md.ts, three lines before `bq(u, S$, "CLAUDE.md")` at 895607). The dump-wide first-seen table drops conflicting names by design, so allowlist-only leaves `omp:claude-md/CLAUDE.md` unverifiable (m0 live probe: exit 1, `omp:<unresolved-var:S$>/CLAUDE.md`).
3. **Stated resolution rule (does not guess).** Module-scope rule: the dump-wide table settles an identifier wherever it has an entry; a name it cannot settle (bound to two values in two different modules = two different variables) is resolved from the binding table of the call's OWN module scope, built by the SAME first-seen/drop-on-conflict policy. So: the `S$` case resolves to `claude-md` (its own module binds it once); a genuine ambiguity inside one module (two different values) stays `<unresolved-var:NAME>`; a name the call's module does not bind falls back to the dump-wide table (old conservative behaviour). Module boundaries are the source-path comments (`// packages/…/x.ts`); a dump without them is one scope -> the old conservative behaviour is restored (fail-closed).
4. **Self-test arms (16 new assertions, 99 -> 115).** `18.12.6-callees` (exit 0, both checks PASS, all 8 pairs), `18.12.6-round50-allowlist` (exit 1, FAIL literal_present + vacuity), `fx-renamed-var` (same conflict on `T$` resolves; kills any per-identifier hardcode), `ambiguous-rebind` extraction-level + CLI-level (exit 1, unresolved marker named), `cross-module conflict not settled` + `own-module binding settles` (Q18 controls).
5. **Mutation discrimination (verified in-clone).** keep-first -> 10 assertion failures (names `omp:title/CLAUDE.md`); keep-last -> 9 failures (names `omp:later/CLAUDE.md`, thanks to the fixture's later `var S$ = "later"`); m0 allowlist-only -> 7 failures (names `omp:<unresolved-var:S$>/CLAUDE.md`); hardcoded `S$` -> 5 failures (renamed-var + ambiguity arms). Base mutation targets (`constant_table` body, `CALL_RE`/`OMP_CALL_RE` literals) are kept byte-identical so the MutSurfacesBase harness's exact-old-text mutants still apply.
6. **`--json` provenance (Q26).** `emit_json` now carries `substrate` per harness: binary path + sha256/mtime/bytes when the binary was read (live: omp sha `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`), or `{"source": "dump", "path": …}` when `--<harness>-strings` was supplied.

## Files changed (patch: `/fast/scratch/hyaku/kotoba-r51/build/SurfacesRepin/patch.diff`, vs `43ca0bfb`)

- `verifiers/verify_surfaces.py` (+281/-13), `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt` (new, 36 lines). No other file touched; `surfaces-baseline.json`, census, floors registry, `baseline.json` unchanged.

## Q09 re-derivation record — lines changed (L1: fold into the record)

- Docstring loader-shape examples + allowlist text: `verify_surfaces.py:16-23` (added `bq(u, v$, "AGENTS.md")`/`Kl(u, "gemini", "GEMINI.md")`/`Ho(u, "github", "copilot-instructions.md")`; regex text now `(Id|Cl|jDe|jDf|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq)`).
- Docstring resolution rule: lines 32-50 (`IDENTIFIER RESOLUTION — MODULE SCOPE`).
- Docstring `--json` substrate note: lines 132-139.
- Comment/history + constants: lines 167-218 (`OMP_CALLEE_NAMES_ROUND50`, `call_re`, `CALL_RE`/`OMP_CALL_RE`, `CALLEE_SHAPES`, `MODULE_MARKER_RE`).
- Extraction model: `constant_table` docstring 354-360 (body untouched); new `module_scopes` 374, `scope_of` 387, `scope_table` 399; `extract_classes` 412 (merged scope+dump-wide table; the base `elif ident in consts:`/`else: group = "<unresolved-var:%s>" % ident` lines kept verbatim).
- Self-test arms: 1004-1112; substrate helpers `binary_digest` 1365 / `substrate_identity` 1378 / `emit_json` 1398; `main` wiring 1475-1477.
- Verified: omp `--version` = `omp/18.12.6`; sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`; mtime `2026-10-21 20:37:24.615549837 -0300`; size 256702432.

## Evidence (all in the private clone `/fast/scratch/hyaku/kotoba-r51/build/SurfacesRepin/lane` at `43ca0bfb`)

```
$ git rev-parse HEAD                       # 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10  exit 0
$ omp --version                            # omp/18.12.6  exit 0
$ sha256sum ~/.local/bin/omp               # 85d9daf3…07ccfa4  exit 0
$ stat -c '%y %s' ~/.local/bin/omp         # 2026-10-21 20:37:24.615549837 -0300 256702432  exit 0
$ python3 -B verifiers/verify_surfaces.py --json   # pass 7 fail 0 exit_code 0; omp substrate sha 85d9daf3…  exit 0
$ python3 -B verifiers/verify_surfaces.py --self-test  # 0 failure(s) over 115 assertions  exit 0
$ python3 -B verifiers/check_assertion_floors.py     # PASS surfaces observed=115 floor=99; exit 0
$ git diff 43ca0bfb --stat                  # 2 files, +304/-13  exit 0
```

Mutant verification (in-clone monkeypatch of `constant_table`/`scope_table`; baseline exit 0/0 failures): keep_first exit 1 / 10 failures; keep_last exit 1 / 9 failures (names `omp:later/CLAUDE.md`); hardcode exit 1 / 5 failures; m0 (scope_table -> {}) exit 1 / 7 failures (names `omp:<unresolved-var:S$>/CLAUDE.md`).

## Risks / notes

- Module scope is read off the source-path comments; a bundle that drops them degenerates to one scope -> conservative unresolved -> loud FAIL (documented limit, no silent pass).
- Keep-last and keep-first are discriminated by VALUE (`title` / `later` vs `claude-md`), not by separate arms; the ambiguity arms additionally pin "unresolved" for in-module rebinds.
- Tooling: nothing installed or upgraded. No web sources opened. No peer messages sent. Lane bounds respected: writes only to the two owned implementation files (in the clone) and this report.
