Result: MIXED — The recorded C1 measurement reproduces exactly; a one-word schema-content mutant survives without changing any measured row or count.

## Scope and axes

Seat `KotobaR58.RerunC1Counter`. Attacks the reported C1 measurement and its dependence on technical content (depth). Supporting axes: reproducibility and exact restoration. This is a scoped detector finding, not a round-admission judgment or a finding that the original Gemini statement is false. No conclusion is offered on other seats' source reviews, routed repairs, the budget move, or whole-round no-harm.

All execution and Git writes occurred only in `/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter`. `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` were unset for execution; `TMPDIR=/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter/.probe/tmp` kept self-test temporary repositories inside the owned sandbox. Every process was bounded with `timeout` (900 seconds maximum). No subagents or client model runtimes were invoked. No tools were installed or updated.

## Finding 1 — The reported count and frozen bytes reproduce

The frozen and content-commit counter blobs have the required identical full SHA-256. Commands ran in the sandbox after cloning the lane and checking out `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`; the compound hash command exited 0:

```text
$ timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_command_files.py | timeout 900 sha256sum
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  -
$ timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git show 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe:verifiers/check_command_files.py | timeout 900 sha256sum
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  -
```

### Required content-revision rerun

```text
Fri Oct 23 08:26:54 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
stderr: (empty)
exit 0
```

### Required base-revision rerun

```text
Fri Oct 23 08:26:54 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit 1
```

### Required self-test rerun

```text
Fri Oct 23 08:26:54 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_command_files.py --self-test
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
stderr: (empty)
exit 0
```

### Line-by-line comparison against the L1 receipt

Compared the actual stdout strings against `.ufo/waves/round-58/C1-measure.txt`, read directly from the lane. Both counter-output blocks contain exactly 10 lines; all 10 match, including spacing and the Copilot `:456` rejection.

| C1-measure.txt line | Rerun stdout line | Comparison |
|---|---|---|
| 3 | 1 | byte-exact |
| 4 | 2 | byte-exact |
| 5 | 3 | byte-exact |
| 6 | 4 | byte-exact |
| 7 | 5 | byte-exact |
| 8 | 6 | byte-exact |
| 9 | 7 | byte-exact |
| 10 | 8 | byte-exact |
| 11 | 9 | byte-exact |
| 12 | 10 | byte-exact |

Other receipt lines:

- Line 1 is the prior measurement timestamp, `Fri 23 Oct 2026 08:20:43 AM UTC`. The new run timestamp above differs, as expected; its `date -u` formatting also differs with the process locale.
- Line 2 is the receipt's command/blob annotation. The rerun uses the same Python command, arguments, measured commit, and counter bytes, with the requested outer `timeout 900` bound. This wrapper line is not counter stdout.
- Line 13 is byte-exact `exit 0`, matching the observed rerun exit.
- Line 14 is the static predicate label, `label: C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) [TARGET=4, NEW_TARGET=3]`. With the unchanged thresholds, the observed F=6 and G=4 satisfy it. It is not counter stdout.

Thus the measured before/after is base F=0, K=0, G=0, exit 1 → content F=6, K=6, G=4, exit 0. The self-test independently reports 244 assertions and zero failures. No difference in the reported measurement was found.

## Finding 2 — One false requiredness statement is invisible to the count

**Mutant:** in `SKILL.md:117`, inside Gemini CLI's `What a file sets` cell, change only `required` to `optional` immediately before the backticked `prompt` field. The path, source id, action, knowledge entry, source registry and Gate quotes remain untouched. This is a plausible one-word schema-documentation defect, not junk, a counter edit, or a threshold change.

```diff
- TOML `.toml`; required `prompt`, optional `description`;
+ TOML `.toml`; optional `prompt`, optional `description`;
```

**Source contradiction:** ordinary direct HTTPS reopen of S093, `https://geminicli.com/docs/cli/custom-commands.md`, saved at `.probe/fetched/S093.md` in the sandbox. Access receipt:

```text
$ timeout 10 date -u
Fri 23 Oct 2026 08:27:54 AM UTC
$ timeout 90 curl --location --max-time 75 --max-filesize 5242880 --silent --show-error --output .probe/fetched/S093.md --dump-header .probe/fetched/S093.headers --write-out 'HTTP %{response_code}; bytes %{size_download}; URL %{url_effective}\n' https://geminicli.com/docs/cli/custom-commands.md
HTTP 200; bytes 12129; URL https://geminicli.com/docs/cli/custom-commands.md
$ timeout 10 sha256sum .probe/fetched/S093.md
8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872  .probe/fetched/S093.md
exit 0
```

Verbatim fetched bytes at lines 44–46 (18 whitespace-separated words; no Markdown bytes stripped):

```text
### Required fields

- `prompt` (String): The prompt that will be sent to the Gemini model when the
```

The frozen detector's own network fetches do not emit HTTP status, byte-count or response-digest receipts; those response bytes were not captured separately. The standalone S093 reopen above is separate evidence, not a claimed capture of the detector's HTTP responses.

**Expected detector:** the same frozen `python3 -B verifiers/check_command_files.py --rev <full-commit> --fetch` used for the reported measurement, on pristine, mutant, and exact restored content. Because it reads committed blobs (`verifiers/check_command_files.py:1908–1914`), the one-word change was committed only in the sandbox before its run.

If the count discriminated this schema-content defect, Gemini's row or its contribution to F/G would change. Under the frozen margins, dropping just Gemini would still allow F=5 and G=3 to exit 0; therefore exit 0 alone is not the survival evidence. The decisive observation is that Gemini remains BACKED/found=yes and F/G stay exactly 6/4.

Mutation commit: sandbox 012c59bfadb899367f8dc70a2d6f5962cfb173ac (/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter).

```text
[detached HEAD 012c59b] sandbox: one-word Gemini prompt-requiredness mutant
 1 file changed, 1 insertion(+), 1 deletion(-)
exit 0
```

### Mutated detector output

The revision in this block is sandbox 012c59bfadb899367f8dc70a2d6f5962cfb173ac (/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter), not a lane revision.

```text
Fri Oct 23 08:28:21 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_command_files.py --rev 012c59bfadb899367f8dc70a2d6f5962cfb173ac --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 012c59bfadb899367f8dc70a2d6f5962cfb173ac
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
stderr: (empty)
exit 0
```

**Verdict: SURVIVED.** Pristine exit 0, mutant exit 0 with all row details and counts unchanged, restored exit 0 with all details/counts unchanged. The two outputs are byte-identical to pristine after substituting only the measured revision line.

The static explanation is visible at `verifiers/check_command_files.py:763–784`: `judge()` inspects the command-token cell `sr[1]` and the action word count `sr[3]`, but not the semantic `What a file sets` cell `sr[2]`. The source/quote checks ground the command folder, not this mutated schema assertion. This is a coverage limitation for using the numeric count as evidence of correct technical detail. It does not falsify the reproduced F/G values or show a breach of the frozen row rules. No change to the frozen counter, contract or target is proposed.

## Restoration evidence

The mutation was reversed immediately after its detector run using the exact inverse one-word edit. The edit tool returned the original `SKILL.md` snapshot identity, and SHA-256 returned to the pristine value. Counter bytes were never edited.

| File | Pristine SHA-256 | Mutant SHA-256 | Restored SHA-256 |
|---|---|---|---|
| SKILL.md | 18e0fde1abdb2a7a56e1fdcce18cd04bae4f35d78668ae2485dc36b653f9ada6 | 82d304d994ee3a2cdad9d8968a41680364ebec09b0ba41fa04c28401e1e19a33 | 18e0fde1abdb2a7a56e1fdcce18cd04bae4f35d78668ae2485dc36b653f9ada6 |
| verifiers/check_command_files.py | aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c | aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c | aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c |

Actual hash command, run once per state, was `timeout 900 sha256sum SKILL.md verifiers/check_command_files.py` for pristine and `timeout 10 sha256sum SKILL.md verifiers/check_command_files.py` for mutant/restored; each exited 0. The mutant/restored outputs were:

```text
82d304d994ee3a2cdad9d8968a41680364ebec09b0ba41fa04c28401e1e19a33  SKILL.md
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
exit 0
18e0fde1abdb2a7a56e1fdcce18cd04bae4f35d78668ae2485dc36b653f9ada6  SKILL.md
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
exit 0
```

Restoration commit: sandbox dcabe2d8172e6295475d41268eff0841f7d04d72 (/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter). This commit changes only `SKILL.md` back; no source changes were made in the lane.

```text
[detached HEAD dcabe2d] sandbox: restore exact pristine Gemini requiredness bytes
 1 file changed, 1 insertion(+), 1 deletion(-)
exit 0
```

### Restored detector output

The revision in this block is sandbox dcabe2d8172e6295475d41268eff0841f7d04d72 (/fast/scratch/hyaku/kotoba-r58/KotobaR58.RerunC1Counter), not a lane revision.

```text
Fri Oct 23 08:28:35 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_command_files.py --rev dcabe2d8172e6295475d41268eff0841f7d04d72 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev dcabe2d8172e6295475d41268eff0841f7d04d72
custom command files found on the live page 6 of 6; new ground 4
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=yes held-at-base=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=yes held-at-base=yes
VS Code      BACKED token=.github/prompts norm=.github/prompts found=yes held-at-base=yes
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
Gemini CLI   BACKED token=~/.gemini/commands/ norm=.gemini/commands found=yes held-at-base=no
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=yes held-at-base=no
stderr: (empty)
exit 0
```

The original file bytes are restored. The sole lane write is this report. No patch is offered for integration: the original requiredness statement is the one supported by S093. The assigned single mutation probe is complete.
