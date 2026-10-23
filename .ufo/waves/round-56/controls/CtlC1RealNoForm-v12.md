Result: PARTIAL — Neither new v1.2 real-text control met C1; an incidental non-agent changelog quote counts one held location, not the full predicate.

## Counter and scored worlds

Read the counter docstring, ERRATUM 2, OWN_ROOTS, source-kind and tracker checks. Copied the L1's v1.2 working-copy bytes into my existing sandbox; no counter modification was made.

Sandbox: `/fast/scratch/hyaku/kotoba-r56/CtlC1RealNoForm`.
Counter sha256: `b5d58ec2f39063099742f642b217de559e1ffaa3888d813a19872c293f6f71ff`.
Resumed start `date -u`: `Fri 23 Oct 2026 02:41:13 AM UTC`.

| World | Sandbox commit | Exact headline | Exit | Predicate |
|---|---|---|---|---|
| V12NativeNonAgentChangelog | `2270e3091ffb08405aaa6309b3b20189bcac5cd5` | `agent-definition locations found on the live page 1 of 1; new ground 0` | 1 | NOT MET |
| V12NativeNegatedHooks | `d2cac63271e66ce027a53fd260f59ae4489252a9` | `agent-definition locations found on the live page 0 of 0; new ground 0` | 1 | NOT MET |

Commands, from the sandbox:

```text
timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 2270e3091ffb08405aaa6309b3b20189bcac5cd5 --fetch
timeout 180 python3 -B verifiers/check_agent_definitions.py --rev d2cac63271e66ce027a53fd260f59ae4489252a9 --fetch
```

Full stdout, stderr, exit, sha256sum and MET/NOT MET labels for both worlds are in `.ufo/waves/round-56/controls/CtlC1RealNoForm-v12.txt`. That receipt also records all eight new curl requests with exact URL, literal UTC date line, HTTP status, bytes and sha256. Raw bytes and `v12-fetch-manifest.json` remain in the sandbox. The old L1-reported rescores were not rerun.

## Strongest local incidental-text counterexample

[Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md), sandbox `source-v12-claude-changelog.txt:7750-7754`, version 2.1.43:

> Fixed spurious warnings for non-agent markdown files in `.claude/agents/` directory

This is byte-exact source text excluding its list marker; Markdown retained. It describes warning handling for **non-agent** files rather than asserting those files are agent definitions. The new docs row S906 supplies that quote, and the world explicitly says not to infer definition discovery from it (`SKILL.md:602-606`, entry row 7, lesson Gate).

Observed per-client output:

```text
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
```

Thus v1.2 still accepts an incidental native-root mention as support. This is not a full BREAK: F=1, G=0. The directory itself is a real native agent directory; this experiment does not prove its location false, and I did not fill the other rows with genuine definition documentation merely to manufacture F>=5.

## Negated native non-definition file

[Cursor hooks](https://cursor.com/docs/hooks.md), sandbox `source-v12-cursor-hooks.txt:102`:

> User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents.

Byte-exact sentence, Markdown retained. A native-root path and outside-path `agents` word are present, but it is a hooks file, not an agent-definition location. The world honestly assigns it that role. Observed output:

```text
Cursor       no     SKILL.md location token '~/.cursor/hooks.json' is not well-formed
```

F=0, K=0, G=0, exit 1. The exact agent-directory-segment requirement blocks this cheap non-definition/negation attempt.

## Genuine-work boundary and remaining uncertainty

The Copilot release-note hit (`source-v12-copilot-changelog.txt:3320`) explicitly says custom agent definitions are pulled from its native directories. That is genuine documented location work and was not used as a shortcut. The inspected native Gemini/Codex/Cursor definition references and VS Code migration guidance likewise describe real discovery/storage, so those lines were stopped rather than used to pad the predicate.

The v1.2 guard fixes the observed v1.1 foreign/issue controls according to L1's receipt. I found no new five-client/two-new-form shortcut in this re-attack. Two failed controls are not a proof of universal soundness, and no client is claimed silent or exhaustively checked.

## Impact and smallest safe correction

Residual issue: **depth/evidence calibration** at a single row—native-root quote presence still does not establish the quote's proposition is definition discovery. The exercised full predicate did not admit either world, so these results alone establish no new target-level regression. If semantic support is tightened further, require an affirmative definition/discovery proposition with the relevant scope, rather than treating any native-root mention as sufficient; a word ban on `non-agent` would only special-case this sentence. This is advisory evidence, not a canonical Rust judgment or a counter change.

No lane code, live client CLI, paid model call, browser, test suite or self-test was run. No tools installed. All started subprocesses completed with timeouts; none remains running. Lane writes are only this report and its named receipt.
