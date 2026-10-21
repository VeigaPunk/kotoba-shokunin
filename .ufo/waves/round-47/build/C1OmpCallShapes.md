verdict: patch-ready for L1 — the omp 18.12.5 callee re-pin (`lq`/`Xl`/`Fo`) turns `literal_present` and `no_uncovered_class` green on the real dump (reproduced from a fresh BASE clone); `surfaces` still exits 1 solely on `opencode_extract` (OC-1/OC-4/OC-6, outside this lane).

# C1OmpCallShapes — round-47 build, omp registration callees

Base: `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Scratch lane `/fast/scratch/kotoba-r47/C1OmpCallShapes/lane` (detached at BASE, uncommitted, `git add -N` in scratch only). Production was read only. Writes: this report and `.ufo/waves/round-47/build/C1OmpCallShapes.{patch,before.json,after.json,matches.json}`.

## 1. Before → after per check (real dumps, `--json`)

| check | BASE `c61a973` | after patch |
|---|---|---|
| surfaces.literal_present | FAIL — `8 loader literal(s) not verifiable` (the 8 loader-group rows; no call shape) | PASS — `38 loader-kind entries verified against the dumps` |
| surfaces.no_uncovered_class | FAIL — `vacuity: 0 loader class(es) extracted … declares 8`; `extractor blind: 33 declared literal(s) …` | PASS — `all 8 extracted loader class(es) declared` |
| surfaces.opencode_extract | FAIL — OC-1, OC-4, OC-6 match nothing | FAIL — detail byte-identical (not touched) |
| surfaces.table_parity | PASS — 38 ids | PASS — identical |
| surfaces.literal_parity | PASS — 38 | PASS — identical |
| surfaces.kind_parity | PASS — 38 | PASS — identical |
| surfaces.excluded_reason | PASS — 9 | PASS — identical |
| `--json` exit | **1** (4 PASS / 3 FAIL) | **1** (6 PASS / 1 FAIL) |
| `--self-test` | **0**, `0 failure(s) over 87 assertions` | **0**, `0 failure(s) over 90 assertions` (+3 in `(b2c)`) |

The BASE column reproduces `.ufo/waves/round-47/before/SUMMARY.md` line 4. Per-check comparison of `before.json` and `after.json`: exactly two checks changed status, and every other detail string is identical.

## 2. Re-derived 18.12.5 registration shape

The shape is unchanged: `callee(<v>, <group>, "<file>.md")` followed by `,` or `)`, where the group is quoted or an identifier resolved through a unique `var X = "..."` binding. The callee set changed to `lq` (2 sites), `Xl` (5), `Fo` (4).

Scanning the whole 48,115,461-byte dump with the verifier's own shape and any identifier callee gives exactly **11** `.md` registration triples, covering the 8 distinct (group, file) pairs. With the allowlist extended, the extractor's output is those same 8 pairs.

Exact matched lines (`/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`, verifier line numbering):

| class (group, file) | dump line(s) | exact matched text | nearest provenance marker above |
|---|---|---|---|
| omp:agents-md/AGENTS.md | L895129 | `  return lq(u, f$, "AGENTS.md");`; binding `var f$ = "agents-md";` at L895126 (unique) | L895125 `discovery/agents-md.ts` |
| omp:claude-md/CLAUDE.md | L895140 | `  return lq(u, m$, "CLAUDE.md");`; binding `var m$ = "claude-md";` at L895137 (unique) | L895136 `discovery/claude-md.ts` |
| omp:gemini/GEMINI.md | L898856, L898867 | `  const T = Xl(u, "gemini", "GEMINI.md");` / `  const M = Fo(u, "gemini", "GEMINI.md");` | L898800 `discovery/gemini.ts` |
| omp:gemini/SYSTEM_TEMPLATE.md | L898992, L898994 | `  await R(Fo(u, "gemini", "SYSTEM_TEMPLATE.md"), "project", "template");` / `  await R(Xl(u, "gemini", "SYSTEM_TEMPLATE.md"), "user", "template");` | L898800 `discovery/gemini.ts` |
| omp:gemini/system.md | L898993, L898995 | `  await R(Fo(u, "gemini", "system.md"), "project", "text");` / `  await R(Xl(u, "gemini", "system.md"), "user", "text");` | L898800 `discovery/gemini.ts` |
| omp:opencode/AGENTS.md | L899090 | `  const T = Xl(u, "opencode", "AGENTS.md");` | L899021 `discovery/opencode.ts` |
| omp:github/copilot-instructions.md | L899328 | `  const T = Fo(u, "github", "copilot-instructions.md");` | L899320 `discovery/github.ts` |
| omp:windsurf/memories/global_rules.md | L900239 | `  const T = Xl(u, "windsurf", "memories/global_rules.md");` | L900187 `discovery/windsurf.ts` |

Callee evidence. This supports the registration reading but does not prove identity, because the verifier matches by shape.
- `lq`: `async function lq(e, t, n) {` at L862812. It walks up from `cwd`, joining the file name `n` (`c.join(k, n)`, L862831), and reads it (L862832). Nearest provenance marker is L862442 `discovery/helpers.ts`.
- `Xl` and `Fo`: 3-parameter definitions `function Xl(e, t, n) {` (L862506) and `function Fo(e, t, n) {` (L862510), in the same chunk as `lq`. At the gemini call site `Xl`'s result is used as a path (`const T = Xl(...)`, then `if (T) { const I = await Ue(T); …`, L898856–898858).
- Overloading: `Xl` has six declarations in the dump (L676246, L686325, L739666, L862506, L1147554, L1262170). `Fo` has thirteen (arities 0–3). `lq` has two (`function` at L862812, `var lq = 60*60*1000` at L1151345). The minified names are reused across scopes.

Artifact: `C1OmpCallShapes.matches.json` lists the 11 matches with line, callee, group, file, matched text and provenance, plus the pair-to-line map.

## 3. Patch — `C1OmpCallShapes.patch` (6,799 bytes, sha256 `1c4f3df7fd727a0cc0bee7f599bb345abc5fa03880e2d1a9c5bbc21551497160`)

`verifiers/verify_surfaces.py` (+22/−4), cited at BASE:
- `:21` docstring alternation: adds `|lq|Xl|Fo`.
- `:142–143` allowlist history comment: adds a `lq/Xl/Fo (2026-10-21, 18.12.5 …)` line.
- `:155–159` `OMP_CALL_RE`: adds `|lq|Xl|Fo` to the omp-only alternation. `CALL_RE` (`:150–154`, opencode) and the opencode `CALLEE_SHAPES` entry are unchanged.
- `:160–163` `CALLEE_SHAPES["omp"]`: same list (used only in failure text).
- Self-test `(b2c)`: inserted after BASE `:822`. It runs the new fixture with `--check literal_present --check no_uncovered_class` and asserts exit 0, `PASS literal_present`, and `PASS no_uncovered_class: all 8 extracted loader class(es) declared`.

New fixtures under `verifiers/fixtures/surfaces/`:
- `strings-omp-18.12.5.txt` (14 lines). Lines 1–13 are the real dump lines above (2 bindings and 11 call lines, exact text). Line 14 is a **synthetic** 2-char alias decoy, `const q = Xl; var decoy = q(u, "evil", "EVIL.md");`, which must not extract.
- `baseline-18.12.5.json`. The 8 loader-group rows copied from `verifiers/surfaces-baseline.json:6,13,20,27,34,41,48,55`.

I kept the historical callee names (`Id…Mo`) on purpose. They are the documented generation history, and the existing fixtures `strings-omp-clean.txt` and `strings-omp-newcallees.txt` depend on them. Pruning them is an L1 decision.

## 4. Commands and exit codes

All runs used `python3 -B` in the scratch lane unless noted.
1. `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` → **0**, 4/4 OK. The dumps match `33df0aef…` (omp) and `f4d8f34a…` (opencode); the binaries match `fdbc8136…` and `179ca421…`.
2. `git clone --no-hardlinks` and `checkout --detach c61a973…` → **0**. `rev-parse HEAD` = `c61a973b…`, status clean. Lane and production `verify_surfaces.py` both `9fa10d44…`.
3. BASE `verify_surfaces.py --omp-strings … --opencode-strings … --json` → **1** (4 PASS / 3 FAIL), saved as `before.json`.
4. BASE, same arguments as text → **1**.
5. BASE `--self-test` → **0**, `0 failure(s) over 87 assertions`.
6. BASE code × new fixture (`--check literal_present --check no_uncovered_class`) → **1**. Output: `FAIL surfaces.literal_present: 8 loader literal(s) not verifiable …`; `FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted …; extractor blind: 8 declared literal(s) …`.
7. AFTER `--json` (real dumps) → **1** (6 PASS / 1 FAIL), saved as `after.json`. The only FAIL is `opencode_extract`.
8. AFTER, same arguments as text → **1**.
9. AFTER `--self-test` → **0**, `0 failure(s) over 90 assertions`.
10. AFTER × new fixture → **0**. Output: `PASS surfaces.literal_present: 8 loader-kind entries …`; `PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared`.
11. Fresh extraction with `python3 -B -c` importing the patched module: real dump → 8 pairs, exit 0. New fixture → the same 8 pairs, with no `evil`, exit 0. `strings-omp-clean.txt` → 2 pairs (`claude-md/CLAUDE.md`, `gemini/GEMINI.md`), exit 0.
12. Fresh clone at BASE (`/fast/scratch/kotoba-r47/C1OmpCallShapes/verify`): `git apply --check` → **0**, `git apply` → **0**. `--json` → **1**, byte-identical to `after.json`. `--self-test` → **0**, 90 assertions.
13. `sha256sum` of artifacts: patch `1c4f3df7…`, `before.json` `b5ce8dbe…`, `after.json` `976ca644…`, `matches.json` `0e74795d…`.

Tools: none installed or upgraded (python3, git, sha256sum and strings were already present). Labrat: not spawned.

## 5. Counterexamples, rejected alternative, known gaps

**Bounded callee shape** (`[A-Za-z_$][A-Za-z0-9_$]{0,2}\(` in place of the allowlist). Measured, **not adopted**.
- On the 18.12.5 dump it gives the same 8 pairs as the allowlist.
- On the historical fixtures it gives the same sets as BASE.
- On the new fixture it adds `omp:evil/EVIL.md` from the 2-char alias decoy. That is undeclared, so the new `(b2c)` assertion would fail.
- So it does not stay discriminating on the evidence. The allowlist fails loud on rename; the bounded shape fails loud on over-match. The allowlist is the documented round-21 design, so changing it is an L1 decision.

**Unbounded any-callee.** It extracts `omp:evil/EVIL.md` from the existing decoy at `verifiers/fixtures/surfaces/strings-omp-clean.txt:10`, so that fixture would FAIL. Rejected.

**Known gaps, unchanged and documented:**
- A 2-char alias of an allowlisted callee (`q = Xl; q(...)`) is invisible. That is a silent miss, not a FAIL. The new decoy locks in the non-extraction; it is not a fix.
- Every future rename is a vacuity FAIL until someone re-pins this list. Callee names are not part of the pin I read: `verifiers/baseline.json:7` pins the binary sha/mtime, and I did not read `check_substrate_pins.py`.
- 18.12.5 also contains non-`.md` `cursor/rules` shapes with callees `Fo` and `Xl` (2 call shapes). The `.md` extractor skips them by design. `omp:cursor/rules` (loader-literal) is therefore witnessed only by the bare literal `"rules"`, which occurs 19 times in the dump. That is a weak witness; I did not change it, and it is a calibration question for L1.
- `f$` and `m$` each have one binding today. A rebinding in a future dump becomes `<unresolved-var:…>` and FAILs. That is fail-closed.

**Assertion floor ratchet (L1 decision; not edited).** `verifiers/check_assertion_floors.py:509` checks `assertions >= floor`, so 90 ≥ 87 still passes. The floor is held at 87 in two places that must agree: `verifiers/check_assertion_floors.py:140–141` and `verifiers/floors-registry.json:38`, with the drift check at `check_assertion_floors.py:350`. Locking in the three new assertions means bumping both to 90. I did not touch those files.

## 6. Not checked

- Older real omp binaries (18.11.1, 18.12.2) are not in the snapshot. Those generations are covered only by existing fixtures.
- Runtime firing of the loaders and whether their output reaches a prompt (documented limit).
- Full lexical scope analysis of `lq`/`Xl`/`Fo`. I relied on arity, provenance and the call-site body. Identity is [INFERENCE].
- I did not re-run `strings -n 4` on the binary; I used the checksum-verified frozen dump.
- opencode OC-1/OC-4/OC-6 (`opencode_extract` still FAIL) belong to the sibling OC lanes. Measured: `CALL_RE` extraction on 1.19.3 is `[]`, so this patch cannot change opencode's `no_uncovered_class`.
- `verifiers/baseline.json` `measured_against` and the omp substrate pin re-pin to 18.12.5, and the baseline `assembled` note: not touched.
- Census text (`corpus/knowledge/instruction-surface-census-round13.md:272`, "75 assertions") and historical receipts under `.ufo/reports/**` (which cite older `OMP_CALL_RE` line numbers) are append-only. Not updated.
- Not run: `check_assertion_floors.py`, `verify_harness_claims.py`, `verify_skill_checklist.py`, `verify_corpus_*.py`, and any lane-wide gate. Only the named verifier was run, and only in scratch.
