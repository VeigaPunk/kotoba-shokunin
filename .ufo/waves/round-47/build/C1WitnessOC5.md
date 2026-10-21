verdict: anchor-still-present, but the BASE anchor is non-discriminating — `OPENCODE_DISABLE_PROJECT_CONFIG` is live code (9 occurrences / 7 `strings` lines; 6 functional sites) and gates exactly the behaviour OC-5 names, while the second OR branch `OPENCODE_CONFIG_PROJECT_DISABLE` is absent (0 hits, no renamed sibling) and the comment's `V7({project:i.config?.project})` / config `project:false` wiring does not exist on 1.19.3; because one of the 9 occurrences is embedded help text, the bare-token rule would still PASS on a binary whose code gate was deleted, so OC-5 needs a shape anchor, not a literal.

Base: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`, exit 0).
Substrate: `/fast/scratch/kotoba-r47/shared/{bin/opencode-1.19.3, opencode-1.19.3.strings}`; `sha256sum -c SHA256SUMS` → `bin/opencode-1.19.3: OK`, `opencode-1.19.3.strings: OK` (4/4 OK, exit 0).
Dump citations below are **line indices of the `strings -n 4` dump**, not binary offsets. Binary was re-grepped to confirm each anchor exists byte-for-byte in the ELF (table in §5).

## 1. What OC-5 is at BASE

- Comment: `verifiers/verify_surfaces.py:383-385`
  > `# OC-5: resolution switch witness — the project source is disabled only via`
  > `# config \`project:false\` (env \`OPENCODE_CONFIG_PROJECT_DISABLE\` or`
  > `# \`OPENCODE_DISABLE_PROJECT_CONFIG\`), wired as \`V7({project:i.config?.project})\`.`
- Constants: `verifiers/verify_surfaces.py:386-387` — `OC_ENV_PROJECT_CONFIG = "OPENCODE_DISABLE_PROJECT_CONFIG"`, `OC_ENV_PROJECT_CONFIG_2 = "OPENCODE_CONFIG_PROJECT_DISABLE"`.
- Rule: `verifiers/verify_surfaces.py:435-438` — `switch = (OC_ENV_PROJECT_CONFIG in dump or OC_ENV_PROJECT_CONFIG_2 in dump)`; `rule("OC-5", [], switch, [...])`; owns no class id.
- Self-test fixture entry: `verifiers/verify_surfaces.py:969` — `("strings-opencode-drop-oc5.txt", "OC-5")`.
- Fixtures: `verifiers/fixtures/surfaces/strings-opencode-clean.txt:18` is the whole OC-5 anchor (`process.env.OPENCODE_DISABLE_PROJECT_CONFIG`); `verifiers/fixtures/surfaces/strings-opencode-drop-oc5.txt:1-3` removes it.

So OC-5 is a rule-identity witness: it contributes no class id, and a mismatch surfaces only as `FAIL surfaces.opencode_extract: rule(s) matched nothing: OC-5 …`.

## 2. Anchor status on 1.19.3: still present (token 1), second token gone

`grep -o -- 'OPENCODE_DISABLE_PROJECT_CONFIG' opencode-1.19.3.strings | wc -l` → **9** (exit 0).
Per-line occurrence counts (`grep -n -o … | awk`): `442392:1, 443993:2, 445482:1, 446350:1, 446380:1, 446403:1, 447235:2`.

| dump line | occurrences | role (verbatim excerpt, trimmed) | code? |
|---|---|---|---|
| 445482 | 1 | `qE.OPENCODE_DISABLE_PROJECT_CONFIG\|\|!h?[]:yield*H.up({targets:["AGENTS.md"],start:S,stop:$})` inside `InstructionContext.observe` — **the project instruction walk-up gate OC-5 exists to witness** | yes |
| 443993 | 2 | `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)return yield*e.globUp(T,d.directory,d.worktree)…;return yield*e.globUp(T,r.config,r.config)` (Instruction state switch) and `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)for(…findUp(O,d.directory,d.worktree)…)` (`Instruction.systemPaths`) | yes |
| 446380 | 1 | `if(!k.OPENCODE_DISABLE_PROJECT_CONFIG)for(let G of yield*_2.files("opencode",B.directory,B.worktree)…)` — project-local `opencode.json*` discovery skipped | yes |
| 446403 | 1 | `…!_.OPENCODE_DISABLE_PROJECT_CONFIG?yield*r.up({targets:[".opencode"],…}):[]` — project `.opencode` dirs skipped | yes |
| 442392 | 1 | `let I=_.OPENCODE_DISABLE_PROJECT_CONFIG?[]:yield*e("tui",W.directory)` | yes |
| 447235 | 2 | `get OPENCODE_DISABLE_PROJECT_CONFIG(){return j("OPENCODE_DISABLE_PROJECT_CONFIG")}` — env accessor (`j` admits `"true"`/`"1"`) | yes |
| 446350 | 1 | `- \`OPENCODE_DISABLE_PROJECT_CONFIG=1\`: skip the project's local \`opencode.json\`` under `## Escape hatches` — **embedded documentation, not code** | no |

**Behaviour verdict: present.** The switch OC-5 describes — env or config disables the *project* source, leaving the global/config source — is live at 445482 (`||!h?[]:` empties the walk-up) and at 443993 (project `directory/worktree` → `config/config` re-scope). The two `globUp` shapes from the round-14 doc (`corpus/knowledge/opencode-extraction-round14.md:46`) both still exist: `globUp(<v>,<v>.directory,<v>.worktree)` ×1, `globUp(<v>,<v>.config,<v>.config)` ×1.

**Second token: absent, not renamed.** `OPENCODE_CONFIG_PROJECT_DISABLE` → 0 in dump and 0 in binary. Sweep of plausible renames, all 0: `OPENCODE_DISABLE_PROJECT`, `OPENCODE_PROJECT_DISABLE`, `OPENCODE_PROJECT_CONFIG_DISABLE`, `OPENCODE_DISABLE_PROJECT_CONFIGURATION`, `OPENCODE_CONFIG_PROJECT`, `OPENCODE_DISABLE_LOCAL_CONFIG`, `OPENCODE_CONFIG_DISABLE_PROJECT`, `OPENCODE_DISABLE_PROJECT_INSTRUCTIONS`. Namespace-level check: the only `OPENCODE_[A-Z0-9_]*PROJECT[A-Z0-9_]*` token in the whole dump is `OPENCODE_DISABLE_PROJECT_CONFIG` (9). So on 1.19.3 the OR at `verify_surfaces.py:436` is a dead branch: OC-5 is a single-token rule that happens to be spelled as a disjunction.

## 3. Comment prose that no longer holds (re-derive, do not copy)

- `V7({project:i.config?.project})` — `config?.project` **0** hits; `config.project` 2 hits, both unrelated code trees bundled into the same ELF: the VS Code TS language server (`W.config.projects` project graph, dump 449276) and a Cloud Speech URL builder (`${this.config.project}`, dump 449560). Neither is this bundle's instruction path. `V7({` occurs once at 449516 and is an unrelated validator: `new V7({check:"size_equals",…})`. The claimed wiring literal is a **false friend** on 1.19.3.
- `config project:false` — the two config-schema copies (`opencode-1.19.3.strings:447094` Effect-schema; `:447178` second schema/mapper) declare `autoupdate`, `share`, `instructions`, `references`, `plugins`, … but no `project` field. The remaining `project:<value>` shapes are unrelated: `project:!1` is an acorn parser option (448316), `project:null` a GitLab model-discovery result, `project:process…` Vertex env resolution, and the rest `ProjectSummary`/OpenAI/Vertex fields. **[INFERENCE]** the config `project` field was removed and only the env remains; strings cannot prove a runtime schema absence, so this is a 0-hit sweep plus shape reasoning, not schema introspection.
- Stale prose is duplicated in `corpus/knowledge/instruction-surface-census-round13.md:184-185` (the inventory the verifier reads), so a comment-only fix leaves the census contradicting the rule.

## 4. The calibration defect: BASE OC-5 can pass on help text alone

Counterexample, executed (python3, exit 0):

- The docs line 446350 alone satisfies `OC_ENV_PROJECT_CONFIG in dump` → `switch = True`.
- Simulated dump with the only instruction gate rewritten (`qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:` → `false?[]:`; i.e. behaviour deleted, docs kept): BASE rule still matches (`"OPENCODE_DISABLE_PROJECT_CONFIG" in sim` → True; OC-5 would PASS), while the shape regexes below match 0.

Minimal discriminating anchors, tested against the real dump, the docs-only string, and the gate-removed simulation:

```
A1 = re.compile(r'OPENCODE_DISABLE_PROJECT_CONFIG\|\|[^;`]{0,80}\?\[\]:[^;`]{0,160}targets:\["AGENTS\.md"\]')
A2 = re.compile(r'globUp\([A-Za-z_$][\w$]*,[A-Za-z_$][\w$]*\.config,[A-Za-z_$][\w$]*\.config\)')
A3 = re.compile(r'if\(![A-Za-z_$][\w$]*\.OPENCODE_DISABLE_PROJECT_CONFIG\)')   # optional, 3 sites: 443993 ×2, 446380
```

| rule | real dump | docs-only | gate-removed sim |
|---|---|---|---|
| `A1` | 1 | 0 | 0 |
| `A2` | 1 | 0 | 1 (different site, untouched by sim) |
| `A3` | 3 | 0 | 3 |
| `A1 and A2` (recommended) | True | False | False |
| BASE token-or | True | **True** | **True** |

**Minimum set for 1.19.3:** `{A1}` is the minimum that discriminates (ties the env token to the `targets:["AGENTS.md"]` walk-up gate; immune to the docs occurrence). **Recommended set:** `{A1, A2}` — two anchors, both required, covering the two instruction entry points (`InstructionContext.observe` gate and `Instruction.systemPaths` project→config re-scope) and matching the repo's two-anchor witness convention. `A3` is a cheap third if the selector should also pin project *config-file* discovery, but it is not needed for minimality. None of these regexes use minified callee names (`qE`, `H`, `h`, `T`, `r`), only env literal, ternary punctuation and domain property names (`AGENTS.md`, `.config`, `.directory`, `.worktree`).

**Do not use `V7({` as an anchor** — it matches an unrelated schema validator on this dump and would be a permanent false positive.

## 5. Binary fidelity (so this is not a dump artefact)

| token | `grep -a -o` on `bin/opencode-1.19.3` | dump |
|---|---|---|
| `OPENCODE_DISABLE_PROJECT_CONFIG` | 9 | 9 |
| `OPENCODE_CONFIG_PROJECT_DISABLE` | 0 | 0 |
| `targets:["AGENTS.md"]` | 1 | 1 |
| `globUp(T,r.config,r.config)` | 1 | 1 |

Binary sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` (agrees with the OC-1 seat's `C1WitnessOC1.json` snapshot block).

## 6. Corroboration from the verifier at BASE (run in my scratch clone)

| command | exit | key output |
|---|---|---|
| `python3 -B - <<'EOF'` → `importlib` load of `verifiers/verify_surfaces.py`, then `extract_opencode_classes(<1.19.3 dump>)` | 0 | `OC-5` record: `{"matched": true, "missing": []}`; ids produced = `['opencode:config/AGENTS.md', 'opencode:config/instructions']` |
| `python3 -B verifiers/verify_surfaces.py --self-test` (scratch clone @ BASE) | 0 | `0 failure(s) over 87 assertions` |
| `verify_surfaces.py --opencode-strings …/strings-opencode-drop-oc5.txt …` (scratch clone) | 1 | `FAIL surfaces.opencode_extract: rule(s) matched nothing: OC-5 (owns no class id (shape witness); missing OPENCODE_DISABLE_PROJECT_CONFIG \| OPENCODE_CONFIG_PROJECT_DISABLE)` |
| `verify_surfaces.py --omp-strings …omp-18.12.5.strings --opencode-strings …opencode-1.19.3.strings --json` (snapshot dumps, fleet repo read-only) | 1 | `surfaces.opencode_extract` FAIL detail names `OC-1`, `OC-4`, `OC-6` — **OC-5 is not named**, i.e. it matched on the real 1.19.3 dump. (The omp failures in the same run are other seats' axis, not assessed here.) |

## 7. Integration notes for the L1 (not applied; production is read-only to me)

1. **Rule shape.** Replace the literal-OR at `verifiers/verify_surfaces.py:435-437` with the `{A1, A2}` pair; update the anchor display strings (currently `"OPENCODE_DISABLE_PROJECT_CONFIG | OPENCODE_CONFIG_PROJECT_DISABLE"`) so an unmatched report names the shapes, not tokens. Drop `OC_ENV_PROJECT_CONFIG_2` (`:387`) — on 1.19.3 it can only ever be dead weight. Note the sibling `C1WitnessOC1.json` repins OC-1 onto `InstructionContext.observe` + `targets:["AGENTS.md"]` — the **same** dump site as `A1`. Keep OC-5's discriminant in the *env gate* (`||!h?[]:`), otherwise OC-5 degenerates into a re-assertion of OC-1's literal and can no longer fail even if the switch is removed.
2. **Comment rewrite (`:383-385`).** Suggested text: env-only on 1.19.3; cite `InstructionContext.observe` gate (dump 445482), `Instruction.systemPaths` re-scope (443993), `Config.loadInstanceState` / `ConfigPaths.directories` skips (446380/446403); record `OPENCODE_CONFIG_PROJECT_DISABLE` and config `project:false` as **absent** (0 hits; no `OPENCODE_*PROJECT*` sibling) rather than deleted from the prose. Mirror the correction at `corpus/knowledge/instruction-surface-census-round13.md:184-185`.
3. **Fixtures.** Tightening the rule breaks the current synthetic fixtures, which key on the bare token: `strings-opencode-clean.txt:18` must become the gate shape(s) (`qE.OPENCODE_DISABLE_PROJECT_CONFIG||!h?[]:yield*H.up({targets:["AGENTS.md"],start:S,stop:$})` plus `globUp(T,r.config,r.config)`), and `strings-opencode-drop-oc5.txt` must remove both shapes. Add a **negative** fixture (clean dump minus the code gate, plus the 446350 docs line) asserted to exit 1 naming OC-5 — that is the assertion that would have caught the §4 defect. Keep the self-test tuple at `:969`.
4. **Fixture-comment inaccuracy already at BASE.** `strings-opencode-drop-oc5.txt:2` says “Both env-gate literals are gone”, but the clean fixture only ever contained one (`grep -c OPENCODE_CONFIG_PROJECT_DISABLE strings-opencode-clean.txt` → 0, exit 1). Cosmetic, but it is a record/matching error in the same rule.
5. **Lineage caution.** The 1.19.3 dump self-identifies as `var n="1.19.3"` (dump 447186) and has 0 hits for `2.0.26`; the round-18/21 OC shapes (`ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`, `SessionInstructions.load`) are absent while round-14 shapes (`InstructionContext.observe`, `Instruction.systemPaths`, `globUp`) are present. **[INFERENCE]** 1.19.3 is a different (numerically earlier) generation than the 2.0.26 bundle most OC prose was written from, so every OC comment is a candidate for re-derivation, not just OC-5's config half. OC-5's *behaviour* survives the generation change; only its prose does not.

## 8. Counterexamples / honest limits

- One of nine occurrences is help text; the BASE rule cannot tell it from code. Demonstrated by the gate-removed simulation (§4), not asserted.
- `V7({` is a real string on this dump but an unrelated validator — a literal re-pin of the old comment would be a false positive.
- `globUp(...)` remains, but minification could flatten it into a destructured local in a future build; `A2` is a witness that fails closed, which is the intended contract.
- `[INFERENCE]` on: config `project` field removal (strings sweep, no runtime schema dump); 1.19.3 predating 2.0.26 (only version strings + shape generations); runtime effect of the env gate (code shape only).

## 9. What I did NOT check

- No disassembly/bytecode, no byte-offset mapping; analysis is `strings -n 4` line-level, corroborated by whole-file binary greps for four anchors only. A shape split across a non-printable byte would be invisible (binary greps cover the specific anchors used here).
- Did not execute opencode 1.19.3 (and never the `~/.local/bin/opencode` npx wrapper); no runtime env-gate test, no `--version` on the wrapper, and I did not verify that the wrapper resolves to the snapshot binary.
- Did not run `check_substrate_pins.py`, `verify_corpus_*`, or any other lane-wide gate; the only verifier runs are the four listed in §6, all in my scratch clone with snapshot dumps.
- Did not assess OC-1/OC-2/OC-3/OC-4/OC-6 beyond the rule report printed in §6 (other seats own those).
- Did not examine the omp dump.
- No production edits and no patch artifact: `verify_surfaces.py` is concurrently owned by C1 siblings (`C1WitnessOC1.patch`, `C1WitnessOC4.patch` exist in this build dir), so changes here are L1-integrated recommendations only.
- No tools installed or upgraded.
