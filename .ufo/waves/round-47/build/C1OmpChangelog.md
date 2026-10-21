# C1OmpChangelog — omp 18.12.3–18.12.5 embedded changelog (C1 provenance)

verdict: omp 18.12.3–18.12.5 adds no instruction-surface class and no Breaking Change, but the 18.12.5 binary renamed the loader registration callees to `Xl/Fo/lq` — adding that one alternation to `OMP_CALL_RE` restores 8/8 omp loader classes (surfaces 4 PASS/3 FAIL → 6 PASS/1 FAIL with the same dumps; the residual FAIL is opencode, not omp).

All line numbers are BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` unless the path says otherwise. `dump` below = `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` (sha256 `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301`, per `shared/SHA256SUMS`).

## 1. Substrate identity (re-derived, not copied from the before summary)

| fact | value | evidence |
|---|---|---|
| version string | `omp/18.12.5` | `omp --version` exit 0 (single line) |
| snapshot binary | sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`, 256575456 bytes | `sha256sum /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5` exit 0; `stat` |
| mtime | `2026-10-21 03:30:38.135013187 -0300` = `1792564238135013187` ns | `stat -c '%y %Y'` |
| live default binary | byte-identical to the snapshot (same sha256, same ns mtime) | `sha256sum /home/vgpnk/.local/bin/omp` exit 0; `readlink -f` = itself |
| changelog heading in binary | exactly 1 occurrence of `## [18.12.5] - 2026-10-21` | `grep -a -c` on the ELF exit 0 |
| opencode side | `~/.opencode/bin/opencode` absent (`ls` exit 2); live engine = npx-cache ELF `.../node_modules/opencode-linux-x64/bin/opencode`, sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, mtime `2026-10-20 18:33:42.152682158 -0300` | `sha256sum`, `stat`, `ls` |
| `~/.local/bin/opencode` | a **bash wrapper** (`#!/bin/bash`, runs `mise`/`node`), not an ELF | `file` → "Bourne-Again shell script"; `head -c 200` |

Operability trap for the re-pin: both gates still point at the **deleted** `~/.opencode/bin/opencode` — `verifiers/check_substrate_pins.py:63` and `verifiers/verify_surfaces.py:130`. A "default resolution" green therefore needs a stable ELF path (a deliberate copy) or a changed constant; pinning `~/.local/bin/opencode` instead would pin the wrapper's bytes and make `strings` extraction vacuous. I did not choose that path.

## 2. Changelog inventory (dump:2422122–2422255)

`# Changelog` starts at dump:2422122; `## [Unreleased]` at 2422123.

| release | heading | sub-headings | bullet entries |
|---|---|---|---|
| 18.12.5 | dump:2422124 | Added 2422125, Fixed 2422128 | 6 |
| 18.12.4 | dump:2422136 | Added 2422137, Changed 2422146, Fixed 2422153 | 59 |
| 18.12.3 | dump:2422205 | Added 2422206, Changed 2422215, Fixed 2422217 | 44 |
| 18.12.2 (next, for the boundary) | dump:2422256 | — | — |

No `### Breaking Changes` section exists in any of the three (the nearest is 18.12.1's, dump:2422306). Counts are bullet starts (`^- `) per range, not line counts: the dump carries **12 wrapped continuation lines** inside these ranges — dump:2422127, 2422130, 2422135 (18.12.5); 2422150, 2422155, 2422173, 2422177, 2422186, 2422203 (18.12.4); 2422222, 2422232, 2422255 (18.12.3). A line-oriented parser of this changelog will mis-split entries: e.g. dump:2422130 is the tail of the 2422129 bullet (` " \`max\`) while \`task.enableEffort\` is off; the field is now ignored …"`).

## 3. Entries touching skills, AGENTS.md/context files, instruction loading, discovery roots

**Skills / discovery root (the one substantive entry):**

- dump:2422218 (18.12.3, Fixed) — full text:
  > - Fixed `omp skill list` omitting skills from a `skills.customDirectories` entry that starts with `~`; such an entry now resolves against your home directory, matching the skill loader ([#16347](https://github.com/can1357/oh-my-pi/pull/16347) by [@yuzu-octopus](https://github.com/yuzu-octopus))

  Code witness in the same binary: config schema id `skills.customDirectories` at dump:861736 (default `V`, registered into the skills settings map at dump:861757); the skill-list path maps each entry through the path helper then absolutizes — dump:1208659–1208666 (`if (s.customDirectories?.length) { … customDirectories: s.customDirectories.map((t) => { const c = lo(t); return a.isAbsolute(c) ? c : a.resolve(r, c); })`), inside the `omp skill list` handler at dump:1208686–1208705. The `~` expander is `function lo(u, p)` at dump:969138–969146 (`u === "~"` → homedir; `~/`, `~\` → prefix swap; `~name` → join). `[INFERENCE]` that the `lo` called at 1208663 is the 969138 definition: a strings dump cannot prove lexical scope; the call shape (path in → `isAbsolute`/`resolve`) and the entry's own wording ("matching the skill loader") are the basis.

  Surface-class impact: **none new** — the literal is `skills`, already declared by `omp:agents/skills` (governed) at `verifiers/surfaces-baseline.json:174` and `omp:discovery/skills-roots` (excluded) at `:221`. The 18.12.3 fix is behaviour inside an already-excluded discovery root. Calibration note: the exclusion reason at surfaces-baseline.json:226 enumerates skill roots but does not mention `skills.customDirectories`; after 18.12.3 that config key is a real, `~`-expanding root. That row's text is stale-ish, not wrong (the row is excluded either way).

**Skill-prompt API (adjacent, not a loader literal):**

- dump:2422224 (18.12.3, Fixed) — full text:
  > - Fixed legacy pi extensions that import `contentText` from pi-ai or `formatSkillsForPrompt` from pi-coding-agent, such as `pi-claude-bridge`, failing to load ([#16313](https://github.com/can1357/oh-my-pi/pull/16313) by [@Jerryx333](https://github.com/Jerryx333))

  Compatibility for an exported skill-prompt formatter; no class/literal change.

**Instruction loading (narrow, tool-instruction surface):**

- dump:2422229 (18.12.3, Fixed) — full text:
  > - Fixed a parked subagent waking up with the `todo` tool and its instructions when messaged, though subagents are spawned without them ([#16281](https://github.com/can1357/oh-my-pi/pull/16281) by [@will-bogusz](https://github.com/will-bogusz))

  The subagent instruction set, not context files.
- dump:2422223 (18.12.3, Fixed) — full text:
  > - Fixed `/tan` clones with Mnemopi auto-recall re-sending the parent's recalled memories as an extra system-prompt block, which duplicated them and missed the parent's prompt cache ([#16337](https://github.com/can1357/oh-my-pi/issues/16337))

  Prompt-block assembly (memory), not file loading.

**Prompt text (closest 18.12.4 analogue):**

- dump:2422148 (18.12.4, Changed) — full text:
  > - Built-in style rule reminders no longer tell the model a user-defined rule matched and it MUST comply; they ask it to check its code against the rule and its exceptions, so models rewrite code a built-in rule allows less often ([#16420](https://github.com/can1357/oh-my-pi/pull/16420) by [@will-bogusz](https://github.com/will-bogusz))

  Reminder wording; a `prompt-text`-kind change, not a loader change.

**18.12.5 itself:** none of the six entries touches any of these axes — they are `providers.cacheRetention` (2422126), subagent `effort` (2422129), `omp update --check` vs JFrog (2422131), `<path>:conflicts` 10 MiB cap hint (2422132), and two `ts-*` style-rule fixes (2422133, 2422134).

**Absence evidence, case-exact counts over dump:2422124–2422255** (`awk` + `grep -c`, exit 0): `AGENTS.md` 0, `context file` 0, `Context file` 0, `frontmatter` 0, `system prompt` 0 (the hyphenated `system-prompt` appears once, 2422223), `SYSTEM.md` 0, `RULES.md` 0, `.claude` 0, `.omp/` 1 (2422255, `~/.omp/agent/history.db` test-fixture titles — false positive). Over the whole dump `AGENTS.md` occurs 37 times, the first at dump:520816, all outside the changelog block; the discovery module provenance comments sit at dump:895125 (`// packages/coding-agent/src/discovery/agents-md.ts`), 895136 (`claude-md.ts`), 895147 (`custom-context-files.ts`).

## 4. The actionable re-pin: registration callees moved again

The extractor's allowlist is documented as "minification-volatile — the FIRST thing to re-pin on a binary bump" (`verifiers/verify_surfaces.py:140`), and the last pin records `I5/Gl/Mo (2026-10-18, 18.12.2)` at :143. In 18.12.5 the registration shape `(<v>, <group>, "<file>.md")` is produced by **`lq`, `Xl`, `Fo`** — 11 call sites, 8 distinct `(group, file)` pairs, exactly the 8 baseline loader-group rows:

| dump line | callee | group | file |
|---|---|---|---|
| 895129 | `lq` | `f$` (`var f$ = "agents-md"` @895126) | AGENTS.md |
| 895140 | `lq` | `m$` (`var m$ = "claude-md"` @895137) | CLAUDE.md |
| 898856 | `Xl` | gemini | GEMINI.md |
| 898867 | `Fo` | gemini | GEMINI.md |
| 898992 | `Fo` | gemini | SYSTEM_TEMPLATE.md |
| 898993 | `Fo` | gemini | system.md |
| 898994 | `Xl` | gemini | SYSTEM_TEMPLATE.md |
| 898995 | `Xl` | gemini | system.md |
| 899090 | `Xl` | opencode | AGENTS.md |
| 899328 | `Fo` | github | copilot-instructions.md |
| 900239 | `Xl` | windsurf | memories/global_rules.md |

Whole-dump raw occurrence counts (shape-blind): `Xl(` 29, `Fo(` 53, `lq(` 5; the old names survive only as substrings — `I5(` 8, `Gl(` 25, `Mo(` 30 — with **zero** shape matches. That is the C1 before-state: vacuity (0/8 extracted), not missing literals (the `literal_present` before FAIL is a consequence: it verifies `(group, file)` pairs via the same shape).

Tested in `/fast/scratch/kotoba-r47/C1OmpChangelog-9/lane` (detached at BASE): patch `C1OmpChangelog.patch` adds `Xl|Fo|lq` to `OMP_CALL_RE` and to the `CALLEE_SHAPES["omp"]` doc string (4 insertions, 3 deletions; `CALL_RE`/opencode untouched).

```
python3 -B verifiers/verify_surfaces.py --omp-strings …/omp-18.12.5.strings \
        --opencode-strings …/opencode-1.19.3.strings --json
BASE      (production verifier, same dumps): exit 1, 4 PASS / 3 FAIL
patched   (clone):                          exit 1, 6 PASS / 1 FAIL
  surfaces.literal_present      PASS  "38 loader-kind entries verified against the dumps"
  surfaces.no_uncovered_class   PASS  "all 8 extracted loader class(es) declared"
  surfaces.opencode_extract     FAIL  OC-1/OC-4/OC-6 (opencode only)
  table_parity/literal_parity/kind_parity/excluded_reason  PASS
python3 -B verifiers/verify_surfaces.py --self-test
BASE    exit 0, "0 failure(s) over 87 assertions"
patched exit 0, "0 failure(s) over 87 assertions"
```

Over-match control: the patched run reports exactly 8 extracted classes, and `no_uncovered_class` would FAIL on any extra id; none appeared. `Xl`/`Fo` are common short names, but the shape constraint keeps their contribution at 6 and 5 matches. `git apply --check --reverse` of the patch against the modified clone exits 0.

## 5. Re-pin note draft (baseline.json `measured_against`)

Values to pin (all independently re-derived above):

```
"omp_binary_sha256": "fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e"
"omp_binary_mtime":  "2026-10-21T03:30:38.135013187-03:00"
```

`check_substrate_pins.py:245-254` compares ns-exactly when the pin carries 9 fractional digits; `parse_iso_ns("2026-10-21T03:30:38.135013187-03:00")` → `(1792564238135013187, 0)` tolerance 0 (verified by importing the verifier function, exit 0). A 6-digit pin would widen the window to microseconds — do not truncate.

End-to-end check of these values (clone, temporary baseline at `/tmp/r47-c1-pins.json`, no production edit):

```
python3 -B verifiers/check_substrate_pins.py --repo . --baseline /tmp/r47-c1-pins.json \
  --omp-binary …/shared/bin/omp-18.12.5 --opencode-binary …/opencode-linux-x64/bin/opencode
PASS omp_binary_sha256: fdbc8136…
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421…
OK 3/3 pins hold          (exit 0)
```

So the values themselves are exact; the only remaining condition for a default-resolution green is the path constants at `check_substrate_pins.py:61-63` / `verify_surfaces.py:128-130`.

Note string in the round-44 style (`verifiers/baseline.json` `measured_against`):

> `omp_round47_note`: "Re-pinned for 18.12.5: /home/vgpnk/.local/bin/omp --version reports omp/18.12.5 (embedded changelog `## [18.12.5] - 2026-10-21`, dump:2422124), sha256 fdbc8136…, mtime 2026-10-21T03:30:38.135013187-03:00; live binary is byte-identical to the frozen snapshot. 18.12.3–18.12.5 (dump:2422124-2422255) carry no Breaking Changes and no changelog entry naming AGENTS.md, context files, frontmatter, SYSTEM.md/RULES.md or instruction roots; the only skill-loader-adjacent entry is 18.12.3's `~` expansion of `skills.customDirectories` (dump:2422218, code at dump:1208659-1208666 / 969138-969146), inside an already-excluded discovery root. Registration callees moved I5/Gl/Mo → Xl/Fo/lq: 11 shape sites (dump:895129-900239) resolve to the same 8 loader-group classes."

The opencode half of the pin is a separate decision: the only ELF is the npx-cache path (`179ca421…`, mtime `2026-10-20T18:33:42.152682158-03:00`), and both gates' default path is missing. Whichever path is chosen must be a file that stays put, or the pin will drift on the next `npx` refresh.

## 6. SOURCES row draft (own-work, tier A) — for C1's "provenance" claim

Not written (production read-only to me). Proposed registry row, matching the 11-column `corpus/SOURCES.md:12` header:

```
| S012 | kotoba own work — /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 (sha256 fdbc8136…) + its strings dump; `omp --version` exit 0, "omp/18.12.5"; run 2026-10-21 | own-work | A | What omp 18.12.3–18.12.5 changed in skills / AGENTS.md / context-file / instruction loading | § embedded changelog dump:2422124-2422255; heading byte present once in the ELF (`grep -a -c`) | Three releases ship 6/59/44 entries and no Breaking Changes; no entry names AGENTS.md, context files, frontmatter or SYSTEM.md/RULES.md; the only skill-loader-adjacent entry is 18.12.3's `~` expansion for `skills.customDirectories`; the 18.12.5 loader registration callees are Xl/Fo/lq (11 sites → the same 8 loader-group classes) | mined | 2026-10-21 | on-release | verifiers/surfaces-baseline.json; verifiers/baseline.json |
```

Row-addition impact checked: no verifier parses `SOURCES.md` (`grep -rln SOURCES` over `*.py|*.sh|*.json` finds only `verifiers/corpus-baseline.json`, and that hit is a round-46 note string mentioning the path, not a pin); `corpus/SOURCES.md` is already a tracked, indexed corpus file (`corpus-baseline.json` note: tracked_files 58 includes it). So a row edit changes only the registry's own row count 11 → 12.

## 7. Counterexamples and limits

- "No instruction-surface change in 18.12.3–18.12.5" is a statement about **loader literals/classes**. Two entries do change prompt text: dump:2422148 (style-rule reminder wording) and dump:2422223 (extra system-prompt block from Mnemopi recall). A stricter reading that counts prompt text as "instruction loading" would say the window changed instruction text twice. I chose the census's class vocabulary (`prompt-text` is a distinct kind).
- The changelog is a release note, not a contract. The 18.12.3 entry asserts `omp skill list` now matches "the skill loader"; my code witness (dump:1208659) shows the expansion in the list path. I did not find an independent witness for the loader's own `customDirectories` expansion in the bundled settings path (dump:964387 is the default `customDirectories: Y = []`), so "list and loader agree" rests on the release note's wording plus the shared helper. `[INFERENCE]`.
- A dump-based regex cannot prove lexical binding for `lo`/`f$`/`m$`; the group bindings `f$`/`m$` are proven by their `var … = "…"` lines in the same module, `lo` only by inference (see §3).
- The `literal_present` check is broader than the changelog question: it verifies 38 loader-kind entries across both harnesses; the before FAIL text is a *missing shape*, not a missing literal — worth keeping straight when writing the after-state.

## 8. What I did NOT check

- Did not run either gate at **default resolution** (no `--omp-binary`/`--opencode-binary` overrides). `check_substrate_pins.py` default opencode path is missing, so its default run can only be exit 2 until the integrator picks a path; I did not alter constants.
- Did not touch the opencode 1.19.3 extraction: OC-1/OC-4/OC-6 still FAIL; that is another seat's slice.
- Did not open the upstream GitHub release pages — the embedded changelog text is the artefact read; I cannot say whether it matches the published notes byte-for-byte.
- Did not run `verify_harness_claims.py`, the checklist, or any corpus gate (out of scope; C2/C3 seats own them).
- Did not apply the patch to the lane repo (production read-only) or test `git apply` against a clean BASE tree — only `--check --reverse` against the patched clone.
- Did not inspect `Xl`/`Fo`/`lq` for collisions in the opencode dump (they are added to the omp-only regex; `CALL_RE` is unchanged).
- No tools installed or upgraded this seat; no pacman transactions.

## 9. Commands (exit codes)

| command | exit | key output |
|---|---|---|
| `omp --version` | 0 | `omp/18.12.5` |
| `grep -n '## \[18\.12' dump` | 0 | 2422124 / 2422136 / 2422205 / 2422256 / 2422305 / 2422316 |
| `sha256sum bin/omp-18.12.5` + `stat` | 0 | `fdbc8136…`, mtime `2026-10-21 03:30:38.135013187 -0300` |
| `sha256sum /home/vgpnk/.local/bin/omp` | 0 | same sha; live == snapshot |
| `grep -a -c '## \[18.12.5\] - 2026-10-21' bin/omp-18.12.5` | 0 | `1` |
| `grep -a -o 'Fixed \`omp skill list\`…starts with \`~\`' bin/omp-18.12.5` | 0 | one hit (entry present in the ELF) |
| `sha256sum …/opencode-linux-x64/bin/opencode` | 0 | `179ca421…` |
| `ls /home/vgpnk/.opencode/bin/opencode` | 2 | No such file |
| `file /home/vgpnk/.local/bin/opencode` | 0 | bash wrapper |
| `python3 -B verifiers/verify_surfaces.py --omp-strings … --opencode-strings … --json` (BASE) | 1 | 4 PASS / 3 FAIL |
| same, patched clone | 1 | 6 PASS / 1 FAIL (opencode only) |
| `python3 -B verifiers/verify_surfaces.py --self-test` (BASE and patched) | 0 | `0 failure(s) over 87 assertions` |
| `git clone … && git checkout --detach c61a973b…` | 0 | clone at BASE |
| `git -C lane apply --check --reverse C1OmpChangelog.patch` | 0 | patch applies |
| `python3 -c "from check_substrate_pins import parse_iso_ns; …"` | 0 | `(1792564238135013187, 0)` |
| `python3 -B verifiers/check_substrate_pins.py --baseline /tmp/r47-c1-pins.json --omp-binary <snapshot> --opencode-binary <npx ELF>` | 0 | `OK 3/3 pins hold` (delta 0 ns) |

Artifact: `.ufo/waves/round-47/build/C1OmpChangelog.patch` (the tested allowlist extension).
