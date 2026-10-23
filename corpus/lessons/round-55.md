# Round 55 — lessons (kotoba, hyaku campaign, attempt 1)

Base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`; plan and frozen counters `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`;
erratum 1 (C1 counter v2, before any C1 content) `b04a9005c494d14e4667b201b723857005effb0d`. Claims: C1 depth (explicit
invocation by client; the learning and sourced claim), C2 operability (could-not-evaluate paths of 13 gates). Seat
reports: `.ufo/waves/round-55/build/` and `.ufo/waves/round-55/falsify/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S065 | https://code.claude.com/docs/en/skills.md | 2026-10-22T23:12:23Z | 112,748 B, sha256 `909dd50a…` | "You can type `/skill-name` to invoke it directly, and Claude can load it automatically when relevant to your conversation." | `skills.md:547` | SrcClaudeCode |
| S066 | https://developers.openai.com/blog/eval-skills.md | 2026-10-22T23:13:16Z | 19,356 B, sha256 `6cf414bb…` | "Use the $setup-demo-app skill to create the project in this directory." | `eval-skills.md:148` (inside a `codex exec` prompt string) | SrcCodex |
| S067 | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T23:13:16Z | 23,082 B, sha256 `26973567…` | "You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`." | `agent-skills.md:287` | SrcVSCode |
| S068 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | 2026-10-22T23:12:41Z | 10,057 B, sha256 `989af498…` | "Use the /frontend-design skill to create a responsive navigation bar in React." | `add-skills.md:128` (body of a fenced example; direction at `:125`) | SrcCopilotCLI, ScoutCopilotMoved |
| S069 | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md | 2026-10-22T23:15:25Z | 5,855 B, sha256 `111e8bfa…` | "description and calls the `activate_skill` tool." | `skills-getting-started.md:127-129` | SrcGeminiCLI |
| S070 | https://cursor.com/docs/skills.md | 2026-10-22T23:12:21Z | 18,477 B, sha256 `a642fa96…` | "When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context." | `cursor-skills.md:175` | SrcCursor |
| S071 | https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx | 2026-10-22T23:12:55Z | 9,187 B, sha256 `931b5425…` | "To load a skill yourself, mention it in your prompt as @skill-id." | `skills.mdx:201` (the source wraps `@skill-id` in backticks; stripped here as the counter's page normalisation does) | Srcopencode |

Quote notes: S067's quote keeps the page's backticks; S071's quote drops the source's inline backticks around
`@skill-id` (the counter's page normalisation drops them too); S069's quote is a clause from a numbered step;
S068's quote is the body of a fenced example. S069 (Gemini CLI) is a model-side tool call and is not counted by the
v2 counter (erratum 1).

### Rejected (opened this round, not admitted)

| source | opened | reason | flip |
|---|---|---|---|
| `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md:1277` `/SKILL-NAME` (seat SrcCopilotCLI, ScoutCopilotMoved) | 2026-10-22T23:12:41Z | already rows S031, S038, S056 at base; the how-to page (S068) states the form in a prompt example, so the reference adds no new page | none needed |
| `https://learn.chatgpt.com/docs/build-skills.md:218` "explicit `$skill` invocation still works" (seat SrcCodex) | 2026-10-22T23:12:58Z | already rows S013, S021, S054 at base and the `$skill` form is held in `skill-overlap-levers-round51.md:26`; re-citing it would re-score held knowledge (critic world W3) | none |
| `https://geminicli.com/docs/cli/skills.md` (seat SrcGeminiCLI) | 2026-10-22T23:12:14Z | already S029 at base; `/skills` there lists, enables or disables skills and does not invoke one | a page with a user-typed invocation form |
| VS Code quote at `agent-skills.md:287` as a counted row | 2026-10-22T23:13:16Z | admitted as S067, but the v2 counter does not count it: the quote holds the token and not the word `skill` (erratum 1) | none; kept on the reading |
| Copilot concept route `concepts/agents/about-agent-skills.md` (round-54 reject 1, routed defect 4) | 2026-10-22T23:12:17Z (ScribeMinor) and 23:12:42Z (ScoutCopilotMoved) | still 404 (502 B); the no-`.md` route 301s to `concepts/customizations/agent-skills`, whose `.md` is 200, 2,622 B, sha256 `ed1e2944…` and states no description threshold (grep 0 hits); the reject stands | — |

### Rows touched (old → new)

None. S065–S071 are new rows; no existing row's cell changed (`check_sources_append_only.py --base f0e5de82` is in the falsify wave).

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M48 | `receipt-revision-mismatch` | Fleet report `.ufo/reports/round-54/kotoba.md:56-57` claims finding-delta `--head cae8f2ea` and `checklist 11/11 PASS`. The outside spot-check `corpus/lessons/round-54-verifier-spotcheck.md:207-213` says the committed receipt instead measures `b38c32a0` and that the checklist claim has no committed receipt; the receipt `.ufo/waves/round-54/build/ExecTipRuns.md:214-221` records base `422ffd10`, head `b38c32a0`, and `new 0, resolved 3`. It repeats round-53 routed defect 5's “commit the runs with the revision measured” class. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n cae8f2e c501cd53 -- .ufo/waves/round-54/` → exit 1, no output (no matches). `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n '11/11 PASS' c501cd53 -- .ufo/waves/round-54/` → exit 1, no output; this exact-string search alone does not prove absence, while the spot-check records no committed receipt. The committed-receipt check `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n 'rev=b38c32a078cbb91cda601d6566ae309b6e7ea8fb' c501cd53 -- .ufo/waves/round-54/build/ExecTipRuns.md` → exit 0; output includes line 214: `### rev=b38c32a078cbb91cda601d6566ae309b6e7ea8fb — \`python3 -B verifiers/check_gate_finding_delta.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --head b38c32a078cbb91cda601d6566ae309b6e7ea8fb\` — exit 0`. | Q03 (`corpus/QUALITY.md:14`): a report claim must identify the commit holding the bytes it describes. Q27 is about seat outputs/completeness sweeps, not measurement-revision attribution. | Practice, not counted: report each measurement against the exact revision in its committed receipt, and do not claim an unreceipted result. No executable regression was implemented or shown able to fail, so this is not counted as a demonstrated fix. |
| M49 | `hollow-control` (C1) | The C1 plan committed two §9 controls (do-nothing, fabricated quotes) and both failed the v1 predicate, but wave-1 critic `CriticC1Sizing` met it with real quotes holding no invocation form (world W1 `04869b82`: `found on the live page 7 of 7; new ground 7`, exit 0) and re-scored held `$skill` by a case flip (W3). Receipt: `.ufo/waves/round-55/controls/C1-shortcut-W1W3.txt`. | addendum §9 (cheapest shortcut) — the L1 built only the fabricated one | Counter v2 committed in erratum 1 (`b04a9005`) before any C1 content; shown able to fail: W1 → `0 of 0`, exit 1; W3 → `3 of 3; new ground 1`, exit 1 (same receipt). Q37. |
| M50 | `hollow-predicate-found-after-data` (C2) | Wave-1 critic `CriticC2Sizing` met the frozen C2 predicate (`25 of 25; 13 of 13`, exit 0) with a remap of findings 1→2 (sandbox `9c992b8d`), an entry check only (`65f5d237`) and a standard-library shadow `verifiers/argparse.py` with no gate change (`eb97c954`), after seats had scored their patches. The V control (0 or 1 on the real revision) cannot see a remap when V is 0. Report `.ufo/waves/round-55/build/CriticC2Sizing.md`. | addendum §9 (cheapest shortcut) — the committed shortcut (exit 2 unless `--self-test`) was not the cheapest | Not amended: data had been scored, so the C2 rule stays as frozen and the claim is reported as not verifiable as declared. Q37 names the missing controls for later counters. Not shown able to fail this round, so not counted as a fix. |
| M51 | `bounds-incident` | Seat `CriticC2Sizing` ran a real `git status` at the fleet root (cwd `/home/vgpnk/Projects/shokunin`, ~23:29:20Z) through a PATH shim that bash's hash table bypassed; `.git/index` mtime changed, no staged content changed (seat's own disclosure). | the wave context's "never any git in the fleet repo" bound — a rule, not a check | Recorded; future no-git probes run with `hash -r` and an absolute shim, inside the sandbox cwd. Not counted. |

## Routed defects from the round-54 spot-check

1. Receipts with revisions: base receipts `.ufo/waves/round-55/build/ExecBaseReceipts.md` (each block prints the revision); `verify_skill_checklist.py` at base in a sandbox 8 PASS / 3 FAIL (`../` citations that resolve only in the fleet root, and the sandbox directory name), and on the lane checkout 11/11 PASS, exit 0 — the receipt that "checklist 11/11" lacked. Tip receipts: falsify wave. M48, Q36.
2. QUALITY criteria for M45 and M47: Q34, Q35.
3. Over-wide C1 cells: Codex (unpinned parser cut removed), Gemini (threshold marked a size estimate; pointers `skillLoader.ts:211`, `snippets.ts:320` @ google-gemini/gemini-cli@451a02ff), Cursor (`references/` advice removed), landed `ed3e8996` (seat ScribeC1Cells). The round-54 counter still reads Gemini's `100` as a number; that is its own limit.
4. Reject-1 route move recorded above (Rejected, last row). Decision stands.
5. Registry counter: probe rows that declare `1=failed` or carry an exact `--self-test` handler are rejected, and flags match an exact `add_argument` or shell `case` arm (`4d700b17`, seat ExecRegistryHarden; all-probe control `0 of 26`, exit 1).
6. `fault_injection_corpus.sh`: harness repairs landed `4d700b17` (fault-g, fault-h, self-test T2/T3; self-test exit 0); the entry still exits 1 on real corpus findings (control dirty: the unresolvable `451a02ff` in the closure-authored `round-54-verifier-spotcheck.md:147`, which the lane never edits). The row stays a routed red gate.
7. Minor: S057's Gate quote drops the list marker `1.` and the `**` around `Metadata (name + description)` (line 24 bytes: `1.  **Metadata (name + description)**: Always in context (~100 words).`); S060's single grounding quote is "To specify a different name or a list of names, use the `context.fileName` property." (`gemini-md.md:97-98`). SKILL.md 599 → 598 after this round's table (anti-pattern prose moved verbatim to `skill-overlap-levers-round51.md`).
8. Carried: the 12 earlier SOURCES in-place edits are filed as one L0 line (fleet `d2b2c566`); environment failures beyond the two probe classes are listed in `.ufo/waves/round-55/build/ExecEnvSweep.md`; weak self-tests (callee rename, opencode repin) carried.
