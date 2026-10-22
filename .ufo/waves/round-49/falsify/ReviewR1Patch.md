# ReviewR1Patch: round-49 falsify, R1 repair

HOLDS-BOUNDED. Applies to the R1 identity arm (name over directory for configured and log-named roots, well-formed names), the 7 new self-test arms, and the floors bump. FAILS as stated for three sub-claims: the no-name fallback as opencode fidelity (F1), the agents-root unreadable-file claim (F2), and the frontmatter reader's YAML edge cases (F3).

Judged: lane master c48793db (head) against a5adc146 (base). Scope: verifiers/verify_harness_independent.py, verifiers/floors-registry.json, verifiers/check_assertion_floors.py. No lane mutation; scratch under /fast/scratch/hyaku/kotoba-r49/falsify/ReviewR1Patch/.

## Findings, by severity

**F1 HIGH. The no-name fallback is not what opencode does, and the comments and a test arm say it is.**
- The comments at verify_harness_independent.py:291-310 and :633-638 credit S016 for "the directory name is the fallback ONLY when the frontmatter carries no name". S016 (corpus/SOURCES.md:29) supports only the identity sentence. It says nothing about a fallback.
- Opencode v1.19.3 skips a nameless skill. `isSkillFrontmatter` requires `typeof data.name === "string"` (packages/opencode/src/skill/index.ts:53-59, check at :56). `add()` returns at :123 (`if (!isSkillFrontmatter(md.data)) return`) with no event and no log. Verdict: DIVERGENCE. The fallback counts a skill that opencode never loads.
- Name `""`: `typeof "" === "string"`, so opencode loads it under key "" (:134). R1 uses the directory name instead.
- Pre-existing at base (agents root `.get("name") or dir`; configured and log roots `entry.name`). R1 keeps it and extends the single-operator claim to every root.
- The arm `build_frontmatter_fallback_fixture` (self-test expects 3) pins the divergent count. Opencode would load 2 (alpha, beta).

**F2 MEDIUM. False claim about the agents root.** The derive comment (:670-673) says the agents root "has always fallen back to" the directory name when SKILL.md cannot be read. `offered()` (:206-209) runs `except OSError: continue`, so the agents root drops unreadable files and does not fall back. Only the configured and log-named loop (:668-675) uses the directory name. The read_frontmatter docstring (:279-282) and skill_identity docstring (:302-303) repeat the false claim. Opencode also skips unreadable files: the read failure lands in the catch in `add()` and then `if (!md) return` (:121).

**F3 MEDIUM. Reader edge cases.** parse_frontmatter (:233-275) is unchanged from base, but R1 now makes it decide identity on every root. Battery run on the head module (R1 identity) against a YAML oracle (PyYAML 6.0.3) and against gray-matter and opencode source for the BOM, unclosed, and type rules:

| frontmatter input | R1 identity | YAML / opencode | result |
|---|---|---|---|
| `name: x` (LF or CRLF, plain) | x | x | match |
| `name: "x"` | x | x | match |
| BOM before `---`, `name: x` | dir name | x (gray-matter strips BOM, lib/to-file.js:39, lib/utils.js:48) | DIVERGES |
| CRLF `name: >` then `  x` | `>` | x | DIVERGES (header `>\r` not recognised) |
| LF `name: \|` then `  x` as last key | `x\n` | x | DIVERGES (clip newline added; the frontmatter excludes the final break) |
| `name: >` with empty body | `\n` | "" (opencode keys "") | DIVERGES; breaks the docstring's "empty means dir" rule |
| `name: x # c` | `x # c` | x | DIVERGES; S008 (SOURCES.md:21): plain scalars never contain " #" |
| `name: "x" # c` | `x" # c` | x | DIVERGES |
| `"name": x` (quoted key) | dir name | x | DIVERGES |
| `---` with no closing `---` | dir name | x (gray-matter index.js:94-95, `closeIndex = len`) | DIVERGES |
| `name:` then indented `  x` | "" then dir name | x | DIVERGES |
| `name: 123` | `123` | number; opencode skips (isSkillFrontmatter) | DIVERGES (counts a skill opencode skips) |
| `name:` (null) | "" then dir name | null; opencode skips | DIVERGES |

Consequence [INFERENCE from the set union in derive; not run]: base keyed configured roots by directory name, which is right by coincidence when the directory matches the opencode identity. Example: skills/x/SKILL.md with `name: x # note`, plus agents-root `x`. Base counts 1 (correct). R1 counts 2.

**F4 MEDIUM. Test gap.** None of the F3 inputs appear in the 7 new arms (alias, control, fallback, log-named). The fallback arm (F1) would fail a fix that matches opencode, so the test currently encodes the wrong rule.

**F5 LOW, latent. Cross-channel operator mismatch.** verify_harness_claims.py:472-476 (`oc_observations`) counts DIRECTORY names (`e.name`) over ~/.agents/skills, ~/.config/opencode/skills and ~/.claude/skills. R1 keys configured and log-named roots by frontmatter name, so the two channels that compare_harness_independent joins use different operators. Neither the live verifier nor the compare driver changed. Measured effect today: none (see the host check below).

**F6 LOW. Records.** The R1 comments cite "round-48 falsify seat A21's probe: 4 -> 5" (verify_harness_independent.py:309, :642, :1613-1614). The cited record, .ufo/waves/round-48/falsify/A21NoHarmBattery.md, reports `oc.roots.names_plus_builtin = 10` in all three runs and has no "4 -> 5" line (grep below). The provenance of that number is unverified.

## Checked and holding

- S016 identity claim is accurate. Opencode keys skills by frontmatter name (`state.skills[md.data.name] = {`, skill/index.ts:134). The row's anchor :24 (OPENCODE_SKILL_PATTERN) matches line 24. The config-dir scan at :206-207 matches the row's :205-207. Tag v1.19.3 was fetched. The upstream commit hash in the row was not checked.
- Name over directory for configured and log-named roots, on well-formed names: correct direction. The new arms produce 3 (alias), 4 (control), 3 (fallback), 3 (log-named), as asserted.
- Floors bump is in step in all four places: registry (instrument_total 10; ten entries; harness_independent 123; dispatch_prompts 32); EXPECTED_INSTRUMENTS (check_assertion_floors.py:123-134); INSTRUMENTS (:141-162; the dispatch regex matches the self-test's final line); docstring (lines 7-9 and 19-23). The guard runs green at head (see commands).
- parse_frontmatter body is unchanged; the first diff hunk starts after it (:275). Self-test count 116 to 123 is exactly 7 new expects, matching the docstring "116->123".

## Commands and exit codes

1. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --stat a5adc146... c48793db... -- <3 files>`: exit 0. 3 files, 229 insertions, 16 deletions.
2. `git diff a5adc146... c48793db... -- verifiers/verify_harness_independent.py`: exit 0 (full diff read; copy in scratch).
3. `git clone -q <lane> <scratch>/head`, then `git -C <scratch>/head checkout -q c48793db...`: exit 0; rev-parse = c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. Base clone at a5adc146a2995dcc5a95a6d8db6e5674f75191ac (rev-parse matched).
4. head: `python3 -B verifiers/verify_harness_independent.py --self-test`: exit 0; final line `0 failure(s) over 123 assertions`.
5. base: same command: exit 0; final line `0 failure(s) over 116 assertions`.
6. head: `python3 -B verifiers/check_assertion_floors.py`: exit 0. All ten PASS, observed = floor: harness 10, corpus_integrity 150, corpus_independent 91, surfaces 99, checklist 1845, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 150, dispatch_prompts 32.
7. head and base: `python3 -B verifiers/verify_harness_independent.py --json` (host, read only): exit 0 each, stderr 0 bytes. `oc.roots.names_plus_builtin` value 10 in both; the only changed row is its evidence text.
8. `ls -la /home/vgpnk/.agents/skills /home/vgpnk/.claude/skills`: exit 0 (read only). Glob found no SKILL.md under ~/.config/opencode/skill or skills.
9. Reader battery: Python cell importing the head module; output is the F3 table. The cell completed.
10. Record check: grep `4 -> 5|4→5` in .ufo/waves/round-48/falsify/A21NoHarmBattery.md: no match.
11. Source downloads (curl, access 2026-10-22T11:35:44Z to 11:35:46Z):
   - opencode v1.19.3 packages/opencode/src/skill/index.ts: 11843 B, sha256 91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6
   - packages/core/src/config/markdown.ts: 1220 B, sha256 add3093be2a87835fef66882853cf2b12f3bdc2d96883eefbcfec7463a8a0215
   - packages/opencode/src/config/markdown.ts: 1173 B, sha256 bcb87009e9ffc760e0e2f0878543f582b5ca7ecc67bebb2087de2467ae28cbfe
   - packages/core/package.json: 4287 B, sha256 e18c4f710f040157274f674102a3c7d507aefe82553fb2b9feb3e0f24ff6ea43 (pins gray-matter 4.0.3)
   - packages/opencode/src/config/paths.ts: 1312 B, sha256 cd86a34461b27caf1042f8cba140fbbed47790c4f30cd9691f87298e8d4d4444
   - gray-matter master index.js: 6140 B, sha256 0e35aa201de0273eb77d255362199d85f479ea361df539eb3aa483e900478da4
   - gray-matter master lib/utils.js: 1257 B, sha256 ffe0d4ac7aa2379d1be2ca02824f41ce2fa36703648bd58c0fb4bc5b1c4e788f
   - gray-matter master lib/to-file.js: 1145 B, sha256 c1d5e2e8830bf8188403203c51aea7608667655979e49589aab9635f38210b3a
   - gray-matter tag 4.0.3 index.js: HTTP 404 (curl exit 22). Not opened. Master used instead.
   - Located lines (≤25 words each): skill/index.ts:56 `typeof data.name === "string" &&`; :123 `if (!isSkillFrontmatter(md.data)) return`; :134 `state.skills[md.data.name] = {`; to-file.js:39 `file.content = utils.toString(file.content);`; utils.js:48 `return stripBom(input);`; index.js:94-95 `if (closeIndex === -1) {` / `closeIndex = len;`.

## Residual risk and gaps

- gray-matter was read from master, not 4.0.3 (the tag path is 404). [INFERENCE] 4.0.3 has the same paths.
- No js-yaml run. PyYAML 6.0.3 was the proxy for YAML semantics. The BOM, unclosed, and type rules rest on gray-matter and opencode source, not on execution. The opencode binary was not executed (bound: fetched code).
- compare_harness_independent.py and verify_harness_claims.py were not run. F5 rests on reading the code.
- Symlinked agents-root entries (omarchy, shokunin, swarm, tower, ufo) were not name-checked. The measured host value is equal at base and head, so this does not change the verdict.
- Corpus baseline re-record, R4 and Q25 are outside this diff and were not reviewed.
- Suggested fix direction, not applied: match opencode (skip nameless, empty, non-string, and unreadable skills), or document the fallback as a deliberate divergence from S016 and stop citing S016 for it. Add reader arms for BOM, CRLF block headers, trailing comments, and clip-at-end.

## Tooling

No tools installed or upgraded. Used host Python 3.14.8 and PyYAML 6.0.3 (already present). Scratch: /fast/scratch/hyaku/kotoba-r49/falsify/ReviewR1Patch/ (head and base clones, src/ downloads, selftest-head.txt, selftest-base.txt, floors-head.txt, ind-host-head.json, ind-host-base.json).
