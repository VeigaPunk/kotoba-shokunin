Result: MIXED — R4 newly kills two of four mutants, one survives, and the required historical live receipt was 3 of 4 rather than 4 of 4 because Cursor returned HTTP 403 to the counter.

## Scope and detector

Seat: `KotobaR58.MutR4Arm`. Axes examined: operability/detection, historical-output preservation, and exact restoration. This is a mutation-probe result, not a round-admission judgment.

- Attacked content revision: `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`.
- Before-repair comparison: `3de87aad29e960c95ed35840442f424c48c29729`.
- Only execution/mutation checkout: `/fast/scratch/hyaku/kotoba-r58/MutR4Arm`.
- `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` were removed from subprocess environments. `TMPDIR` was `/fast/scratch/hyaku/kotoba-r58/MutR4Arm/.probe-tmp`, keeping the self-test's temporary Git worlds inside this sandbox.
- Lane source files were not edited. Each mutant changed one line and was reversed before the next mutant. No correction or changed frozen predicate is proposed.

The same bounded detector was run on pristine, each independently mutated, and each restored version at both revisions:

```text
timeout 120 python3 -B verifiers/check_plugin_manifests.py --self-test
```

Cwd for every invocation: the scratch checkout above. All detector stderr streams were empty. Complete commands, UTC timestamps, stdout, stderr, exit codes, exact mutations, and before/after SHA-256 values are retained in `/fast/scratch/hyaku/kotoba-r58/MutR4Arm/.probe-receipts/probe.json` (abbreviated `probe.json` below).

Pristine outputs (both exit 0):

```text
# content revision; probe.json:58-65
counter sha256 7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6
self-test: 0 failure(s) over 239 assertions

# freeze revision; probe.json:148-155
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
```

Neither baseline failed; no mutant result is classified inconclusive.

## Mutants and observed verdicts

All source references in this section are to `verifiers/check_plugin_manifests.py`. Line pairs below are content/freeze. Exact before/after text is also recorded at `probe.json:14-54`.

| Mutant | Smallest change | Expected detector | Freeze result | Content result | Newly killed? |
|---|---|---|---|---|---|
| M1 | At 1944/1858, replace final `return predicate(args.fetch, found, ground)` with `return 0` | Broken-world `main()` must return 1 | SURVIVED: exit 0, 0/235 failures | KILLED: exit 1, 1/239 failures | Yes |
| M2 | At 1933/1847, change summary arguments from `k, found, ground` to `found, k, ground` | Broken world must print `1 of 2`, not `2 of 1` | SURVIVED: exit 0, 0/235 failures | KILLED: exit 1, 1/239 failures | Yes |
| M3 | At 1944/1858, replace final return with `return 0 if args.fetch and found >= TARGET else 1` | Main path must enforce the independent `NEW_TARGET`/G condition | SURVIVED: exit 0, 0/235 failures | SURVIVED: exit 0, 0/239 failures | No |
| M4 | At 675/675, replace `if not quote_in_gate(quote, gate_raw, gate_plain):` with `if False:` | A quote absent from the lesson Gate must not back the row | KILLED: exit 1, 1/235 failures | KILLED: exit 1, 3/239 failures | No; already killed |

### Exact detector failures

M1, content (`probe.json:68-75`):

```text
FAIL R4: the broken world exits 1: got 0, expected 1
self-test: 1 failure(s) over 239 assertions
```

M2, content (`probe.json:88-95`):

```text
FAIL R4: the broken world prints the one-of-two line: got False, expected True
self-test: 1 failure(s) over 239 assertions
```

M3, content (`probe.json:108-115`):

```text
self-test: 0 failure(s) over 239 assertions
```

M4, freeze (`probe.json:218-225`):

```text
FAIL a quote missing from the Gate is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
self-test: 1 failure(s) over 235 assertions
```

M4, content (`probe.json:128-135`):

```text
FAIL a quote missing from the Gate is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
FAIL R4: the broken world exits 1: got 0, expected 1
FAIL R4: the broken world prints the one-of-two line: got False, expected True
self-test: 3 failure(s) over 239 assertions
```

Freeze M1/M2/M3 each printed `self-test: 0 failure(s) over 235 assertions`, with no FAIL lines (`probe.json:158-165`, `178-185`, `198-205`). Each run's preceding `counter sha256` line is preserved in the receipt; exact mutant hashes are below.

### Surviving-mutant finding

M3 removes G enforcement only at the final `main()` decision; it leaves the `predicate()` helper and its unit assertions intact. The new R4 fixture sets `TARGET = NEW_TARGET = 2` at content line 1826 and exercises F/G = 2/2 and 1/1 (lines 1831-1852). Thus its broken world fails F as well as G. The unit assertion at line 1741 does exercise a ground-only failure in the helper, but does not check that `main()` delegates to it correctly.

Observed fact: this main-path defect passes all 239 assertions. [INFERENCE] A main world with F meeting TARGET but G below NEW_TARGET would distinguish this mutant from the frozen predicate. This is a coverage finding, not permission to change the contract.

## Before, mutated, and restored bytes

SHA-256 values for the complete verifier file:

| Revision/state | SHA-256 |
|---|---|
| Content pristine and every content restoration | `7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6` |
| Content M1 | `6499b28c3402b15c42b6233ca13c8cae5463d2259ffb2926e486d75aac24f385` |
| Content M2 | `19f31efba49cb0aa8761de193ea875cbcabc77ad2a8491db8711795a53cc3f1f` |
| Content M3 | `ab4dadf0f3add38d043e78d974553b9424fb1b65f1cd4cbc00404ee2cd00639f` |
| Content M4 | `dc7d041326832ec79233c425874bb84e9f9d7811b6c36b8c1bd508d6df9b23e6` |
| Freeze pristine and every freeze restoration | `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` |
| Freeze M1 | `da1f900b6ad247588146a8e2f51ac211fc829f359bbe4f4afe7f40387ac2df87` |
| Freeze M2 | `9ab78273f489638f707e8e90c71c6fddea390f02b52ab74a1e964b0fdb67881f` |
| Freeze M3 | `9a17bc14cba72e36c66782bcbd5cde2151d9479f582082b680181d2b6961182f` |
| Freeze M4 | `145648322980b178e463a35302bce09a3cf01dd6d37d39d7327b3bec31717f22` |

Every detector's before/after hash was identical: the detector did not mutate its own file. Every inverse edit recovered the applicable pristine hash, followed by the same bounded detector:

| Restored run | Exit | Observed summary | Evidence |
|---|---|---|---|
| Content after M1 | 0 | `self-test: 0 failure(s) over 239 assertions` | `probe.json:78-85` |
| Content after M2 | 0 | Same 239-assertion summary | `probe.json:98-105` |
| Content after M3 | 0 | Same 239-assertion summary | `probe.json:118-125` |
| Content after M4 | 0 | Same 239-assertion summary | `probe.json:138-145` |
| Freeze after M1 | 0 | `self-test: 0 failure(s) over 235 assertions` | `probe.json:168-175` |
| Freeze after M2 | 0 | Same 235-assertion summary | `probe.json:188-195` |
| Freeze after M3 | 0 | Same 235-assertion summary | `probe.json:208-215` |
| Freeze after M4 | 0 | Same 235-assertion summary | `probe.json:228-235` |
| Final checkout restored to content revision | 0 | Same 239-assertion summary | `probe.json:238-245` |

The final three historical runs also retained the pristine content hash (`probe.json:248-275`). No mutant remains applied.

## Historical no-harm receipt: expected count not reproduced

Command on restored content bytes:

```text
timeout 240 python3 -B verifiers/check_plugin_manifests.py --rev 118d3ac4c6ca9db51d4b05a7dc2ce82d35cc4711 --fetch
```

First run, `date -u` output `Fri Oct 23 08:33:09 AM UTC 2026`; exit **1**, stderr empty (`probe.json:248-255`):

```text
counter sha256 7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6
counter rev 118d3ac4c6ca9db51d4b05a7dc2ce82d35cc4711
plugin manifests found on the live page 3 of 4; new ground 3
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
```

One bounded retry at `Fri Oct 23 08:34:51 AM UTC 2026` produced the same 3-of-4/new-ground-3 summary and exit 1 (`probe.json:258-265`). The requested **4-of-4/new-ground-4 receipt has not passed** in this sandbox run; only the expected exit 1 was reproduced.

A bounded diagnostic added the existing `--json` flag to the same command at `Fri Oct 23 08:35:14 AM UTC 2026`; exit 1, stderr empty (`probe.json:268-275`). It reported `backed: 4`, `of: 4`, `found: 3`, `new_ground: 3`, and the following Cursor fields:

```json
{
  "client": "Cursor",
  "row": "S084",
  "url": "https://cursor.com/docs/plugins.md",
  "backed": true,
  "found": false,
  "fetch_error": "HTTP Error 403: Forbidden"
}
```

This is an observed transport failure, not evidence that R4 changed the runtime predicate. The read-only comparison of the two verifier revisions showed only the self-test global declaration and new R4 arm added. No access-control bypass was attempted.

### Independent ordinary source receipts

To investigate the missing live page, ordinary `curl` GETs were recorded separately. These are **independent later responses**, not assertions about the exact response bytes served to the counter's urllib requests. All four returned curl exit 0, HTTP 200, no redirect, and empty stderr. Each access's `date -u` output was:

```text
Fri Oct 23 08:34:11 AM UTC 2026
```

Command pattern, with the actual expanded argv retained at `probe.json:278-410`:

```text
timeout 80 curl --location --max-time 60 --max-filesize 5242880 --silent --show-error --user-agent kotoba-shokunin-counter/57 --dump-header <scratch>/.probe-receipts/<id>.headers --output <scratch>/.probe-receipts/<id>.body --write-out '%{http_code} %{size_download} %{url_effective}\n' <URL>
```

| ID | URL / effective URL | HTTP | Bytes | SHA-256 of fetched body |
|---|---|---|---|---|
| S079 | https://code.claude.com/docs/en/plugins-reference.md | 200 | 42124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` |
| S080 | https://developers.openai.com/plugins/build/plugins.md | 200 | 38036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` |
| S083 | https://geminicli.com/docs/extensions/reference.md | 200 | 12022 | `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` |
| S084 | https://cursor.com/docs/plugins.md | 200 | 20323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` |

The counted Cursor quote is still a byte-exact contiguous substring of the independent curl body at `/fast/scratch/hyaku/kotoba-r58/MutR4Arm/.probe-receipts/S084.body:28` (no markdown bytes stripped):

> plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and

Its successful curl transport does not turn the counter's 403 into a passing historical receipt.

## Tooling and closure

No tool was installed or updated. No subagent or other agent runtime was invoked. The only lane write is this report. Assigned mutation probe is complete; all four mutants were restored on both revisions and the sandbox ends on the attacked content revision with its original verifier hash.
