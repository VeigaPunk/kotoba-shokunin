Result: MIXED — Six of sixteen isolated C1 v2 mutants were killed by --self-test; ten survived both requested detectors, with exact restoration after every probe.

# Scope and method

- Axis challenged: depth; evidence quality and restoration fidelity were guardrails, not additional round claims.
- Target revision: `f0e6b695b746775823b65a8c45de7d50ea33e84f`.
- Sandbox: `/fast/scratch/hyaku/kotoba-r55/MutC1v2` (a clone checked out at that revision, with inherited Git directory/worktree/index variables removed). Only its `verifiers/check_explicit_invocation.py` was mutated, one rule at a time. No lane source, predicate, counter, gate, index, or jj state was changed.
- Read `plans/round-55.md` first. The governing v2 rules are its Erratum 1, lines 94–115, and the target docstring, lines 75–97. This report does not judge or admit C1 and does not propose changing the frozen counter.
- For each mutant, ran the same two bounded commands on pristine, mutated, and restored source bytes, in that order. Every subprocess had an external timeout; there were no background jobs. No other runtime or paid client call was invoked. No tools were installed or updated.

Commands, each from the sandbox (run independently, so a self-test failure did not skip fetch):

```sh
timeout 180 python3 -B verifiers/check_explicit_invocation.py --self-test
timeout 180 python3 -B verifiers/check_explicit_invocation.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch
```

Before every pair: `timeout 5 date -u` and `timeout 10 sha256sum verifiers/check_explicit_invocation.py`.

Raw receipts: `/fast/scratch/hyaku/kotoba-r55/MutC1v2/.mutation-evidence/Mnn-{pristine,mutated,restored}.json:1`; each contains command, exit, full stdout/stderr, UTC date line, source SHA-256 and elapsed time. The matrix is `summary.json:1` in that directory. These scratch receipts supplement the actual output recorded below.

# Baseline and restored detector output

All 16 pristine runs and all 16 restored runs exited 0 on both commands and produced the following identical stdout; every stderr was empty:

```text
self-test: 0 failure(s) over 44 assertions
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
```

Initial `date -u` line:

```text
Fri Oct 23 12:10:12 AM UTC 2026
```

# Mutant results

All line numbers below refer to the pristine target at the pinned revision. A killed mutant means its pristine self-test passed and its mutated self-test failed; no baseline failure was counted as a kill. A survivor is a limit of this sampled detector, not proof that the intended contract changed.

Every mutated `--fetch` command exited **0**. Only M01 and M05 changed the final fetch line. M09 changed a client diagnostic but not that final line. The other thirteen left the entire fetch stdout unchanged.

| Mutant | Smallest rule change | Expected detector or uncovered case | Self-test exit / failures | Fetch F/K; G (exit 0) | Verdict |
|---|---|---|---|---|---|
| M01 | `TOKEN_RE, line 145`: Allow a bare underscore-containing tool identifier in addition to the user-typed grammar. | tool-name assertion at 493 | 1 / 1 of 44 | 6/6; 5 | KILLED |
| M02 | `TOKEN_RE, line 145`: Add # to the admitted sigils, leaving the token body grammar unchanged. | sigil rejection; existing #file: case at 540 also contains a forbidden colon | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M03 | `BUILTINS, line 147`: Remove compact from the excluded built-ins. | /compact assertion at 539 | 1 / 1 of 44 | 5/5; 4 | KILLED |
| M04 | `BUILTINS, line 147`: Remove help from the excluded built-ins. | /help exclusion; no isolated /help assertion | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M05 | `judge, lines 427–428`: Delete the skill-substring quote guard. | word-skill assertion at 546–552 | 1 / 1 of 44 | 6/6; 4 | KILLED |
| M06 | `norm_page, line 330`: Delete the style/script block removal. | style/script assertion at 563–565 | 1 / 1 of 44 | 5/5; 4 | KILLED |
| M07 | `norm_page, line 330`: Remove the regex i flag, retaining s: uppercase HTML blocks are no longer dropped. | case-insensitive block removal; fixture at 564 is lowercase only | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M08 | `url_key, line 342`: Change the suffix pattern from \.mdx?$ to \.md$, forgetting .mdx. | URL canonicalization; URL fixtures at 555–562 and 569–571 use .md only | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M09 | `base_url_keys, line 352`: Read c[3] instead of c[2], the kind column rather than the source column. | base source-cell assertion at 569–571 | 1 / 1 of 44 | 5/5; 4 | KILLED |
| M10 | `base_url_keys, line 352`: Process only the first URL in each source cell. | all base URLs; fixture at 570 contains just one URL | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M11 | `new_ground, line 443`: Use t = token instead of t = token.lower(). | case-flip assertion at 553–554 | 1 / 1 of 44 | 5/5; 4 | KILLED |
| M12 | `new_ground, line 444`: Search base_skill without lowercasing it; leave base knowledge folding intact. | case-insensitive base SKILL text; case-flip fixture at 553 uses base knowledge instead | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M13 | `main, line 623`: Count eligible client rows rather than distinct lowercased tokens. | distinct-token count; self_test never runs main counting | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M14 | `TARGET, line 117`: Lower TARGET from 4 to 3. | client-count boundary; no main exit-boundary assertion | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M15 | `NEW_TARGET, line 118`: Lower NEW_TARGET from 2 to 1. | new-ground boundary; no main exit-boundary assertion | 0 / 0 of 44 | 5/5; 4 | SURVIVED |
| M16 | `main, line 643`: Replace the two-threshold conjunction with disjunction. | both thresholds required; no main exit-boundary assertion | 0 / 0 of 44 | 5/5; 4 | SURVIVED |

Exact changed expressions (everything else, including all self-tests, remained pristine):

```python
M01: TOKEN_RE = re.compile(r"^(?:[/$@][A-Za-z<][A-Za-z0-9<>_-]*|[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]*)$")
M02: TOKEN_RE = re.compile(r"^[/$@#][A-Za-z<][A-Za-z0-9<>_-]*$")
M03: remove only "compact", from BUILTINS
M04: remove only "help", from BUILTINS
M05: delete the two-line if "skill" not in quote.lower(): / why.append(...) block
M06: delete only s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
M07: s = re.sub(r"(?s)<(style|script)\b.*?</\1\s*>", " ", s)
M08: path = re.sub(r"\.md$", "", u.path.rstrip("/"))
M09: for m in URL_RE.finditer(c[3]):
M10: for m in list(URL_RE.finditer(c[2]))[:1]:
M11: t = token
M12: if t in base_skill or any(t in k.lower() for k in base_know):
M13: ground = sum(1 for r in counted if r["new_ground"])
M14: TARGET = 3
M15: NEW_TARGET = 1
M16: return 0 if value >= TARGET or ground >= NEW_TARGET else 1
```

## Actual failing self-test stdout

Each block below had exit 1 and empty stderr; all other mutated self-tests had exit 0 and exactly `self-test: 0 failure(s) over 44 assertions`.

M01:

```text
FAIL v2: tool name is not a user-typed token: got ['activate_skill'], expected []
self-test: 1 failure(s) over 44 assertions
```

M03:

```text
FAIL v2: built-in /compact is not a form: got ['/compact'], expected []
self-test: 1 failure(s) over 44 assertions
```

M05:

```text
FAIL v2: quote without the word skill fails: got ['Claude Code', 'Codex'], expected ['Codex']
self-test: 1 failure(s) over 44 assertions
```

M06:

```text
FAIL v2: page style/script dropped: got True, expected False
self-test: 1 failure(s) over 44 assertions
```

M09:

```text
FAIL v2: base_url_keys reads source cells: got set(), expected {'cursor.com/docs/skills'}
self-test: 1 failure(s) over 44 assertions
```

M11:

```text
FAIL v2: case flip is not new ground: got True, expected False
self-test: 1 failure(s) over 44 assertions
```

## Actual fetch differences

The full baseline fetch output above is unchanged except for these exact replacement lines:

M01 (exit 0, empty stderr):

```text
Gemini CLI   BACKED token=activate_skill new=True found=True
user-typed invocation forms found on the live page 6 of 6; new ground 5
```

M05 (exit 0, empty stderr):

```text
VS Code      BACKED token=/webapp-testing new=False found=True
user-typed invocation forms found on the live page 6 of 6; new ground 4
```

M09 (exit 0, empty stderr):

```text
Claude Code  BACKED token=/skill-name new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
```

# Surviving mutants: measured limits

1. **TOKEN_RE sigil isolation (M02):** the `#file:` test at line 540 does not isolate the forbidden `#`; its colon still violates the body grammar after admitting `#`. [INFERENCE] A colon-free `#my-skill` would be accepted by this mutant. Both requested detectors survived unchanged.
2. **BUILTINS coverage (M04):** losing `help` survives, while losing the explicitly tested `compact` dies (M03). The fixtures at 538–539 test two excluded names, not the whole frozen set. [INFERENCE] This survivor would allow `/help` to be treated as a form.
3. **Case-insensitive page block removal (M07):** deleting all style/script removal dies (M06), but dropping only the case-insensitive flag survives. The fixture at 564 is all lowercase. [INFERENCE] Uppercase STYLE/SCRIPT payload text could then satisfy quote matching.
4. **URL suffix coverage (M08):** `.mdx` normalization can be lost without a failing assertion or changed live count. The canonicalization fixtures exercise `.md`, not `.mdx`. [INFERENCE] Equivalent `.mdx`/extensionless URLs could then be scored as different ground.
5. **Multiple source URLs (M10):** parsing only the first URL survives. The sole base_url_keys fixture has one URL. [INFERENCE] A second URL in a base source cell would no longer exclude re-used ground. Reading the wrong source column does fail self-test (M09), but even that defect leaves the final live count unchanged: Claude Code becomes new, yet shares `/skill-name` with the already-new Cursor row.
6. **Base SKILL case coverage (M12):** forgetting to fold base SKILL text survives. The case-flip assertion supplies its held token in base knowledge, not base SKILL. [INFERENCE] An uppercase held token present only in base SKILL could be incorrectly scored new. Losing token folding itself is caught (M11).
7. **Distinct-token aggregation (M13):** changing distinct lowercased tokens to client-row count survives. Although the real table repeats `/skill-name`, only Cursor qualifies as new ground at this revision; the repetition therefore does not exercise deduplication among two eligible rows. The self-test calls judge/new_ground directly and does not reach main aggregation at line 623.
8. **Exit boundaries (M14–M16):** lowering either target, or replacing AND by OR, survives. The self-test returns at main line 592 before evaluating its counting/exit path; the live sample is F=5, G=4 and satisfies both original floors. [INFERENCE] Boundary worlds F=3/G=2, F=4/G=1, or one satisfied floor would distinguish these defects. Those boundary worlds were not executed in this assignment.

These are limits of the specific self-test plus this revision’s live receipt. They are not permission to alter the frozen predicate, and they do not demonstrate that C1 is false on the pristine counter.

# Restoration and hashes

`H0` (every pristine and every restored target SHA-256):

```text
e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a
```

| Mutant | Before | Mutated SHA-256 | After | Pristine/restored stdout, stderr and exits |
|---|---|---|---|---|
| M01 | H0 | `5f622e20267e81af33c12b6480bd918078567c7dcc48b64cfe3c88740c8914f7` | H0 | identical |
| M02 | H0 | `86c40bb3fadb8e5de8e98136592b6ab17ea4e3c9bea95e0a36fe36e165faa8be` | H0 | identical |
| M03 | H0 | `b07cc2e5df410b562ac5078f7f517915c44e643f1f5c93fe3f82f879f2b6c816` | H0 | identical |
| M04 | H0 | `c13ceaa533332c97023c428a68772a7418140a59233d8a12bae13c6128c00626` | H0 | identical |
| M05 | H0 | `bd33af66dd1dec72703b740bc1a682595f15411bdd07334e5973fc344aefb59e` | H0 | identical |
| M06 | H0 | `5dbe23d4b8b3dc7fef054bf17a969352d4ea823b1ffc55a8a8fd4630c1d48afe` | H0 | identical |
| M07 | H0 | `6076b06d08648deac528109017c60d30c94c7e8204deefc7e11a5ddec267ada0` | H0 | identical |
| M08 | H0 | `d38939492c01b47d6750955c1913cc32ad0713c5e10972d7ac10ad6161ee3694` | H0 | identical |
| M09 | H0 | `ce4ebf292cf14fd857a578a913634696f173ddac10aa3e2f6475c252ae212a1f` | H0 | identical |
| M10 | H0 | `e01cce820c207e77b492f3d0defe94cfbe003fe1cb43041faea52e3199193008` | H0 | identical |
| M11 | H0 | `5a31dba139416137b0125b8c58e4061d59f5a4bc86dd556650a24e81801232fc` | H0 | identical |
| M12 | H0 | `91977f9ae9556ee2a7974c59da44941b9e59ed032e563857811663c88e89065c` | H0 | identical |
| M13 | H0 | `0f6e0e6c2d7bc3d4acb8082a10f7332ab192a3dfcb1a949c417ccdd921b09529` | H0 | identical |
| M14 | H0 | `46833ac7be090e9d768481dc2a27fbb344353f04c128c0eb29ed62a99d70df7b` | H0 | identical |
| M15 | H0 | `56a83fb0fcae2d112ea98c9c5382a723576d17edfa0a715f11e1b6e82888ee4e` | H0 | identical |
| M16 | H0 | `6daea4751e16f35da74998fc0dc40b7d4c0cb9504ec7895462eeb43759da3820` | H0 | identical |

All sixteen mutated hashes differ from H0. All sixteen restoration hashes equal H0 exactly. Every restored detector output and exit code equalled its own pristine control, not merely its final count. No mutant was left applied.

Final restoration `date -u` line:

```text
Fri Oct 23 12:13:58 AM UTC 2026
```

## Per-probe UTC date lines

| Mutant | Pristine `date -u` | Mutated `date -u` | Restored `date -u` |
|---|---|---|---|
| M01 | Fri Oct 23 12:10:12 AM UTC 2026 | Fri Oct 23 12:10:20 AM UTC 2026 | Fri Oct 23 12:10:27 AM UTC 2026 |
| M02 | Fri Oct 23 12:10:28 AM UTC 2026 | Fri Oct 23 12:10:33 AM UTC 2026 | Fri Oct 23 12:10:39 AM UTC 2026 |
| M03 | Fri Oct 23 12:10:41 AM UTC 2026 | Fri Oct 23 12:10:46 AM UTC 2026 | Fri Oct 23 12:10:52 AM UTC 2026 |
| M04 | Fri Oct 23 12:10:53 AM UTC 2026 | Fri Oct 23 12:10:59 AM UTC 2026 | Fri Oct 23 12:11:04 AM UTC 2026 |
| M05 | Fri Oct 23 12:11:05 AM UTC 2026 | Fri Oct 23 12:11:11 AM UTC 2026 | Fri Oct 23 12:11:16 AM UTC 2026 |
| M06 | Fri Oct 23 12:11:17 AM UTC 2026 | Fri Oct 23 12:11:25 AM UTC 2026 | Fri Oct 23 12:11:31 AM UTC 2026 |
| M07 | Fri Oct 23 12:11:32 AM UTC 2026 | Fri Oct 23 12:11:38 AM UTC 2026 | Fri Oct 23 12:11:44 AM UTC 2026 |
| M08 | Fri Oct 23 12:11:45 AM UTC 2026 | Fri Oct 23 12:11:50 AM UTC 2026 | Fri Oct 23 12:11:56 AM UTC 2026 |
| M09 | Fri Oct 23 12:11:58 AM UTC 2026 | Fri Oct 23 12:12:12 AM UTC 2026 | Fri Oct 23 12:12:18 AM UTC 2026 |
| M10 | Fri Oct 23 12:12:19 AM UTC 2026 | Fri Oct 23 12:12:25 AM UTC 2026 | Fri Oct 23 12:12:31 AM UTC 2026 |
| M11 | Fri Oct 23 12:12:32 AM UTC 2026 | Fri Oct 23 12:12:43 AM UTC 2026 | Fri Oct 23 12:12:48 AM UTC 2026 |
| M12 | Fri Oct 23 12:12:49 AM UTC 2026 | Fri Oct 23 12:12:55 AM UTC 2026 | Fri Oct 23 12:13:00 AM UTC 2026 |
| M13 | Fri Oct 23 12:13:01 AM UTC 2026 | Fri Oct 23 12:13:08 AM UTC 2026 | Fri Oct 23 12:13:14 AM UTC 2026 |
| M14 | Fri Oct 23 12:13:16 AM UTC 2026 | Fri Oct 23 12:13:21 AM UTC 2026 | Fri Oct 23 12:13:28 AM UTC 2026 |
| M15 | Fri Oct 23 12:13:29 AM UTC 2026 | Fri Oct 23 12:13:35 AM UTC 2026 | Fri Oct 23 12:13:41 AM UTC 2026 |
| M16 | Fri Oct 23 12:13:42 AM UTC 2026 | Fri Oct 23 12:13:48 AM UTC 2026 | Fri Oct 23 12:13:58 AM UTC 2026 |

# Ordinary source access receipts

These separate ordinary GETs record provenance for the seven URLs involved. They are not asserted to pin the bytes of every individual counter GET, which the unmodified counter does not retain. They were fetched without a browser, authentication, challenge bypass, or markdown stripping.

For each URL below, the executed command was:

```sh
timeout 90 curl --silent --show-error --location --max-time 75 --user-agent kotoba-shokunin-counter/55 --output /fast/scratch/hyaku/kotoba-r55/MutC1v2/.mutation-evidence/Snnn.response --write-out '%{http_code}\n%{size_download}\n%{url_effective}\n' <URL>
```

All seven curl commands exited 0 with empty stderr, HTTP 200, and the effective URL equal to the requested URL. `timeout 10 wc -c <response>` and `timeout 10 sha256sum <response>` also exited 0. Each fetch was preceded by this actual `timeout 5 date -u` output:

```text
Fri Oct 23 12:14:20 AM UTC 2026
```

| Row | Requested / effective URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| S065 | <https://code.claude.com/docs/en/skills.md> | 200 | 112748 | `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737` |
| S066 | <https://developers.openai.com/blog/eval-skills.md> | 200 | 19356 | `6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2` |
| S067 | <https://code.visualstudio.com/docs/agent-customization/agent-skills.md> | 200 | 23082 | `26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a` |
| S068 | <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md> | 200 | 10057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |
| S069 | <https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md> | 200 | 5855 | `111e8bfa1b99c2d2e2728864d092728334f73eb4fc9ce2998f6cf6ba3ca1c167` |
| S070 | <https://cursor.com/docs/skills.md> | 200 | 18477 | `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d` |
| S071 | <https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx> | 200 | 9187 | `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b` |

Raw bytes: `/fast/scratch/hyaku/kotoba-r55/MutC1v2/.mutation-evidence/Snnn.response`. Access metadata: `sources.json:1` in that directory. Short byte-exact excerpts from those fetched bytes (source markdown/backticks retained; no stripping):

- S065.response:547 — "You can type `/skill-name` to invoke it directly".
- S066.response:148 — "Use the $setup-demo-app skill to create the project in this directory."
- S067.response:287 — "You can add extra context after the slash command."
- S068.response:128 — "Use the /frontend-design skill to create a responsive navigation bar in React."
- S069.response:128 — "description and calls the `activate_skill` tool."
- S070.response:175 — "When `true`, the skill is only included when explicitly invoked via `/skill-name`."
- S071.response:201 — "To load a skill yourself, mention it in your prompt as `@skill-id`."

No client-behavior, freshness, negative-documentation, C2, or whole-round no-harm claim is made by this scoped probe.
