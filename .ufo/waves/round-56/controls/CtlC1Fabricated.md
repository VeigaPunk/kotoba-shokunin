Result: DONE — Both assigned C1 fabricated worlds were rejected by the unchanged frozen counter, with exact stopping branches observed.

## Scope and axes

Seat: `CtlC1Fabricated`. Reviewed only C1 fabricated quotations and invented pinned-host URLs. Axes: **depth**, **calibration**, and **consistency**; the risk is false source provenance being mistaken for learning. These observations do not admit or judge the round's eventual claim.

Sandbox: `/fast/scratch/hyaku/kotoba-r56/CtlC1Fabricated`, cloned from the lane and checked out at freeze `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257` before creating the worlds.

Frozen counter SHA-256, checked by both runners before execution:

```text
1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
```

Full commands, stdout, stderr, exits and predicate labels: `.ufo/waves/round-56/controls/CtlC1Fabricated.txt`.

## Counterexamples and outcomes

Both worlds deliberately skip source-grounded claim work: all seven quotations are invented. The table, entry, Gate, fresh source IDs S901–S907, tier A, `mined`, and opened date `2026-10-23` are otherwise accepted. The relevant paths are `.claude/agents/`, `.codex/agents/`, `.github/agents/` (two clients), `.gemini/agents/`, `.cursor/agents/`, and `.opencode/agents/`.

Example **invented control text, not a source quotation**: “Create an agent in `.github/agents/` with a description for deliberate task routing.”

World file evidence, at each recorded sandbox revision:
- `SKILL.md:308-320`: exact heading, table header, seven backticked paths, five-word actions.
- `corpus/knowledge/agent-definition-files-round56.md:5-13`: source IDs and invented quotations containing the matching path plus `agent` outside it.
- `corpus/SOURCES.md:85-91`: pinned-host URLs and accepted source metadata.
- `corpus/lessons/round-56.md:3-13`: Gate repeats every invented quotation.

### 1. Existing pages, invented quotations — NOT MET

Sandbox commit: `acf6dd74b3d8ac3c0eeae311863c12bc5139f885`.

```text
timeout 480 python3 -B verifiers/check_agent_definitions.py --rev acf6dd74b3d8ac3c0eeae311863c12bc5139f885 --fetch
agent-definition locations found on the live page 0 of 7; new ground 0
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
```

The auxiliary non-fetch run reported `agent-definition locations backed 7 of 7`, exit 1 by design. Thus the control was not rejected for malformed rows, held source IDs, re-cited base URLs, dates, tier, host, missing agent words, or missing Gate text. All seven ordinary page captures returned HTTP 200.

**Exact stop:** `verifiers/check_agent_definitions.py:711-712`:

```python
if not quote or norm(quote) not in page:
    return False
```

A read-only `sys.settrace` observer executing the unchanged frozen file recorded `found_on_page return False ... :712` for **each of the seven clients**. The empty-quote case is excluded by the accepted nonempty entry quotations. This is the missing fabricated-quote branch, before the boundary-path test at `:713`. Final predicate rejection is `:1054`.

Trace command: `timeout 240 python3 -B trace_branches.py --child --rev acf6dd74b3d8ac3c0eeae311863c12bc5139f885 --fetch`, exit 1. Full trace and stdout are in the receipt and `control-evidence/existing-urls-fabricated-quotes-trace.json` under the sandbox.

### 2. Invented URLs and invented quotations — NOT MET

Sandbox commit: `6e609320ef194bc5624e337b0c4a533011f113dd`.

This child commit changes only the seven added source rows, replacing each real page URL with its host's invented `/kotoba-round56-fabricated-agent-definitions-7392-not-a-page` path. All seven rows remain statically BACKED.

```text
timeout 480 python3 -B verifiers/check_agent_definitions.py --rev 6e609320ef194bc5624e337b0c4a533011f113dd --fetch
agent-definition locations found on the live page 0 of 7; new ground 0
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
```

**Exact stops by client:**
- **Claude Code and Cursor:** invented URLs return HTTP 200, but the trace observes `found_on_page` return False at `:712`, from the absent-quote condition at `:711`. Rejecting these is not merely a 404 check.
- **Codex, VS Code, Copilot CLI, Gemini CLI, opencode:** HTTPError 404 at `:698`, two attempts; re-raised at `:705`. Main catches it at `:1015-1017` and sets `found=False`.
- **World:** the F/G threshold expression at `:1054` returns exit 1.

Trace command: `timeout 240 python3 -B trace_branches.py --child --rev 6e609320ef194bc5624e337b0c4a533011f113dd --fetch`, exit 1. The auxiliary `--fetch --json` run, also exit 1, records exactly those five `fetch_error: HTTP Error 404: Not Found` fields. Full records: `control-evidence/invented-urls-fabricated-quotes-runs.json` and `control-evidence/invented-urls-fabricated-quotes-trace.json` under the sandbox.

## Ordinary HTTP access evidence

For **every** capture below, `timeout 5 date -u` printed:

```text
Fri Oct 23 02:26:36 AM UTC 2026
```

Each capture used ordinary `curl -L`, with `timeout 50`, `--max-time 40`, `--connect-timeout 10`, `--max-redirs 5`, and User-Agent `kotoba-shokunin-counter/56`; all curl processes exited 0. Because curl was not given `--fail`, its exit 0 for a 404 is **not** counter success. Complete per-URL commands, HTTP headers, response bodies, UTC date lines, statuses, sizes, hashes, and effective URLs are preserved in sandbox `control-evidence/fetch-log.json:1-534` and `existing-01` through `existing-07` / `invented-01` through `invented-07` `.body`, `.headers`, and `.json` files.

These are separately captured response bytes; the counter does not retain its own downloaded bytes. No external prose is quoted here, no markdown was stripped for a quotation, and no client-silence/Q30 claim is made.

### Existing page URLs

| Client | Requested URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| Claude Code | https://code.claude.com/docs/en/overview | 200 | 562513 | `96ac89838a214fa00d0b1ffa7a27ebf1550b4061e1f43d7e557d728506bba87f` |
| Codex | https://developers.openai.com/codex/ | 200 | 381019 | `a1826a7a5f3901069ec6d99243e3d18ac99841fb52b1dfa32c48052cf3dc893b` |
| VS Code | https://code.visualstudio.com/docs | 200 | 89890 | `444fe84a95f9b806f64c80763af5c8a155a65c8c14a2bf4e4c4a812d7fe4b7c0` |
| Copilot CLI | https://docs.github.com/en/copilot | 200 | 931788 | `86359275ca3e31a03ad3ad87a2cb6b94c072d1331f19878efde4b9316e150e4a` |
| Gemini CLI | https://geminicli.com/docs/ | 200 | 111011 | `8a4b728f42049b68b1725dc1477f9bbbf2cc44c35c657845a1a5dc3fc223eba9` |
| Cursor | https://cursor.com/docs | 200 | 603587 | `4cc822c8fb4a83321e0e89b94e94c28829705b8645dbeb45d30d00567e420512` |
| opencode | https://opencode.ai/docs/ | 200 | 99209 | `b4d607a9b9ea98d0a53a678e44348d2df5774ada452aa6178b85987190d26b13` |

Codex's effective URL was https://learn.chatgpt.com/docs; all other effective URLs in this table equal the requested URL. Both original and redirected Codex hosts are pinned.

### Invented URLs

All URLs below are **control inputs**, not asserted documentation pages.

| Client | Requested URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| Claude Code | https://code.claude.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 200 | 630032 | `16aa429018300e81be3794942301333ac3411f4c64d13654535eff7ad201a20e` |
| Codex | https://developers.openai.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |
| VS Code | https://code.visualstudio.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 404 | 19510 | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |
| Copilot CLI | https://docs.github.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| Gemini CLI | https://geminicli.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 404 | 31633 | `d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee` |
| Cursor | https://cursor.com/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 200 | 193034 | `7f61aeaa3065093c3f1b7a32f45934c7540427a25ff7e553e0c4ec29314e677b` |
| opencode | https://opencode.ai/kotoba-round56-fabricated-agent-definitions-7392-not-a-page | 404 | 5307 | `7327d53ab6b28552fbd32b0417dbe26388c145176c5de3c62870b8b94fb25d35` |

Claude Code's invented URL redirected to https://claude.com/product/claude-code; all other effective URLs in this table equal the requested URL. That redirect is recorded, not treated as documentation or proof of a passing bypass.

## Smallest safe correction and limits

**No counter patch is supported by these two controls.** Preserve the mandatory `--fetch` predicate and do not promote `BACKED 7 of 7` or HTTP 200 to claim success. Both observed worlds have F=0 and G=0. This is a narrow result for the tested fabricated quotations and URLs, not an exhaustive proof against all possible shortcuts.

No genuinely documented, correctly quoted path was substituted to make a world pass. No tools were installed or updated. No headless browser, bot-challenge workaround, paid client call, other judge/runtime, push, admission, integration, or shipping was used. All started bounded processes completed. Lane writes were limited to this seat's requested report and receipt; the frozen counters and other lane content were not edited.

Report: .ufo/waves/round-56/controls/CtlC1Fabricated.md
