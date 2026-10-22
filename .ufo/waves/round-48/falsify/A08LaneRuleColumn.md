# A08 LaneRuleColumn — FALSIFY wave: lane-checker column of frontmatter-rule-authorities-round48.md

Seat: `KotobaR48.A08LaneRuleColumn` (leaf mutation tester, no delegation). 2026-10-22 (UTC).
Target: the "lane checker (S020), observed" column of `corpus/knowledge/frontmatter-rule-authorities-round48.md`
(C1 build item). All code work in the private clone
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A08LaneRuleColumn/clone/` at
`887b6af54d3f4446f1fe51dc16f26b2e83bc82e1` (round C1 freshness HEAD). Lane checkout edited only for this report.

## Method
Detector = the lane checker CLI (`verifiers/verify_skill_checklist.py`, S020). Name/description cells run
`--check trigger.frontmatter_parses --check trigger.name_directory --check trigger.literal_trigger_string
--check trigger.anti_trigger_clause --check trigger.no_xml_tag` (exit 0 = all PASS); budget cell runs
`--check trigger.line_budget`; empty-description reverse probe runs only `--check trigger.frontmatter_parses`.
For each claimed "no rule" cell: pristine run (expected PASS), then mutate the verifier to ADD the smallest
plausible form of that rule and re-run (expected verdict flip to FAIL). A flip proves the cell describes code
behavior, not an assumption. Positive cells (empty fails; 600-line budget; name_directory literal compare) are
probed in reverse: REMOVE/relax the enforcing point and show the flip the other way. Exact bytes restored after
every mutant (sha256 back to pristine before the next probe). Pristine verifier sha256:
`4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a` (identical to C2 build receipt at
`75f671b`; S020 pin holds at HEAD). Final `git status --short` empty at `887b6af`. No tool installs; no web
sources reopened (claims are about lane code behavior, verified by execution).

## Per-cell verdicts
**1. name length — "no rule: a 65-character name passes".** Fixture: `name:` = 65x"a", dir named identically
(so `name_directory` passes). Pristine: exit 0, all PASS. Mutant: add `len(name.strip()) > 64 -> FAIL` to
`check_frontmatter`. Mutated: exit 1, `frontmatter_parses` FAIL. Verdict flips -> cell true of the code.
KILLED.

**2. name charset — "no rule: `Probe-Upper`, `技能-测试` pass".** Fixtures `Probe-Upper/`, `技能-测试/` (dir == name).
Pristine: both exit 0, all PASS. Mutant: add `re.fullmatch(r"[a-z0-9-]+", name)` failure. Mutated: both exit 1,
`frontmatter_parses` FAIL. Flips -> KILLED.

**3. name equals directory — "literal compare: dir `probe－full` vs `probe-full` FAIL".** Fixture: dir `probe－full`
(U+FF0D), `name: probe-full`. Pristine: exit 1, `name_directory` FAIL `name 'probe-full' != directory 'probe－full'`
— literal compare confirmed. Reverse mutant: NFKC-normalize both sides before comparing. Mutated: exit 0,
`name_directory` PASS. Flip proves the literal compare is what the code executes. KILLED.

**4. consecutive hyphens — "no rule: `probe--consec` passes".** Fixture `probe--consec/` (dir == name). Pristine:
exit 0, all PASS. Mutant: add `"--" in name -> FAIL`. Mutated: exit 1, `frontmatter_parses` FAIL. Flip -> KILLED.

**5. description length — "empty fails `trigger.frontmatter_parses`; no maximum: 1025 characters pass".**
Empty fixture: `description:` empty. Pristine: exit 1, `frontmatter_parses` FAIL ("empty description:") — positive
claim reproduced. Reverse mutant: neutralize empty-description check (only name stays required) -> exit 0 PASS;
flip proves empty-fails is code-driven. No-max fixture: description 1025 chars. Pristine: exit 0, all PASS.
Mutant: add `len(description.strip()) > 1024 -> FAIL` -> exit 1 FAIL; flip proves "no maximum" describes the code.
KILLED.

**6. description angle brackets — rule cell, not a "no rule" cell; measured by the C2 build seat, not challenged here.**

**7. third person — "no rule".** Fixture: description "I handle tasks; Says \"hi\" and never auto-runs" (quoted
span + exclusion marker so other checks pass). Pristine: exit 0, all PASS. Mutant: first-person pronoun heuristic
(`\b(?:I|we|my|our|me)\b` -> FAIL). Mutated: exit 1, `frontmatter_parses` FAIL. Flip -> no third-person rule in
code. KILLED.

**8. reserved words — "no rule: `claude-tools` passes".** Fixture `claude-tools/` (dir == name). Pristine: exit 0,
all PASS. Mutant: "claude"/"anthropic" in lowercased name -> FAIL. Mutated: exit 1 FAIL. Flip -> KILLED.

**9. unknown top-level fields — "no rule: `version: 1` passes".** Fixture adds `version: 1` to good frontmatter.
Pristine: exit 0, all PASS. Mutant: any key outside {name, description} -> FAIL. Mutated: exit 1 FAIL. Flip ->
KILLED.

**10. body length — "`trigger.line_budget` 600 ... 605 lines FAIL, 505 PASS".** Fixtures `probe-505/` (505 lines),
`probe-605/` (605 lines), no checklist box, so `--max-lines` default (600) applies. Pristine: 505 -> exit 0 PASS
("505 lines within budget 600 (from --max-lines)"); 605 -> exit 1 FAIL ("605 lines exceed budget 600"). Both claims
reproduced. Reverse mutant: `DEFAULT_MAX_LINES` 600 -> 700. Mutated: 605 -> exit 0 PASS ("within budget 700"). Flip
proves the 600 boundary is the code's own default constant. KILLED.

## Verdict
CONFIRMED — none of the ten probed lane-column cells was falsified. Every "no rule" cell was reproduced by a
passing fixture on pristine code, and each verdict flipped once the rule was added as a mutant, proving the cells
describe the code's actual behavior. Positive cells (empty fails, 605 FAIL/505 PASS, literal name_directory compare)
were reproduced, and their reverse mutants flipped, proving those behaviors are also code-driven. No surviving mutant.

## Evidence
- Pristine verifier sha256 `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a` before every mutant
  and after final restore (identical; final state verified).
- Mutant hashes (each restored after): name-length `3710746680c4eddeca9a2bac739bc2c6df87bcbf8e87aaa0ee3f5b8f67a1b9a7`;
  charset `7349c8c1a6bfa42ca5db45407e366196888f81fb10d43e7533cf71437cf9db1e`; hyphens
  `bbaa5c6e23bd9bc5f59c241befb5aad4a155505ed0f869ab0644278a95d692cd`; reserved
  `b85c738009e82b2b4cd02dcc1e11e8c134961847b72e66084353e80e40c85c51`; unknown-field
  `8d860e62bb9382318562fd276003413ff12ea16872d83b011bfd5dc3100f4e9a`; description-max
  `be41d0130a139d23c842a65c8fb6b90ce425bcf4c5384cf15b5d2377eadb2ecb`; third-person
  `f23a252c39d1b190e9e47fb00171175e923aa72319b15e874f339b0b1c505482`; empty-desc reverse
  `2f7b3e1555d527de07c14c07302cfb50d878c1e5b371f8d9420cd5613176d48a`; line-budget reverse
  `9352e72fdba44933c9e2b9b3cb931f8dacb937b4feded85add682b58cec26bb6`; NFKC-name_directory
  `7754743054cb2b4b6dccf7d05c0b0f80fe02168658e4127ce0bdc9bcb5fb2ab8`.
- Fixture sha256: 65-char `2d534dedece7368f39acb60e31d0ae668648a1e80c84fd56a877feb866d28234`; Probe-Upper
  `2fd3e35929bf153fc67eb3304370657f3c5930ce8d603f83e5bfc8acf9b684e1`; 技能-测试
  `e2388af1b181fe77788f54207114256d7ffe37e5afc679aa7f937e29fd4b7ade`; probe--consec
  `30ae7afffdaee871abe9fbfc7438107dab5d9a8da366524e0e64147d515a26e5`; claude-tools
  `9fe8244f15dca499d9f4c56196efc4fc717a6c71534c6fd32e119dac5038c650`; unknown
  `67da2a4e7c457157029bf0dbf369017afb2e9bad8622b8fefd4a9b90027b9ac0`; descmax
  `35dc3448a88eacaef8db0f31ed2f6cc8812973ee27931fe24a5c300a91805762`; descempty
  `83838abd68e17cd473509c00e245dcab3e8f14feb41c04900e3c9e81e601ab37`; thirdperson
  `452093282f7eb9d7357d014074c35c8650525f4e1d694cf9f2da7af6e6a31850`; 505
  `8fade9d47b1a14599d9d376d5736695485f6772eca97e398fc1ffef2464a4396`; 605
  `ceb05beca2ce4a8f9d5654e9c36ad286678a0e11d643952eb47f82e4086394b8`; probe－full
  `e84e460fe0e3b1dfd6f4fa5aaedce76bec961a41c497fff342f6bae820a072d5`.
- Clone HEAD `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1`; `git status --short` empty after final restore.
