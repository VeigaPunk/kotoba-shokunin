# Kb79S08 — independent Q45 census re-derivation

Fetched using `urllib.request` with UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36`, 2026-10-27. Counts below are case-insensitive matches of `allowed[-_ ]tools` in response UTF-8-decoded with replacement (raw) and after a simple HTML view transform (remove script/style blocks, tags, HTML-unescape, collapse whitespace). For markdown/plain-text responses that transform naturally leaves bytes' textual content. This is a census signal, not a full semantic support determination. Hashes SHA-256 of exact response bytes.

| Client | URL | HTTP | Bytes | SHA-256 | Raw count | Text-view count | States field? | Quote (5–25 words if yes) |
|---|---|---:|---:|---|---:|---:|---|---|
| Open specification | https://agentskills.io/specification.md | 200 | 7608 | 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16 | 4 | 4 | Yes | “Space-separated string of pre-approved tools the skill may use. (Experimental)” |
| Claude Code | https://code.claude.com/docs/en/skills.md | 200 | 117962 | 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9 | 23 | 23 | Yes | “an `allowed-tools` grant goes through the normal permission flow” |
| Factory | https://docs.factory.ai/cli/configuration/skills | 200 | 341235 | 81457fbf081aceaa5b90c50a8d7685450dc8801229f9a9202e40acde8fa201fa | 21 | 7 | Yes | “allowed-tools: - Read - Grep - Glob” |
| Microsoft Agent Framework | https://learn.microsoft.com/en-us/agent-framework/agents/skills | 200 | 157339 | 34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2 | 1 | 1 | Yes | “Space-delimited list of pre-approved tools the skill may use. Experimental” |
| pi | https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md | 200 | 4793 | 5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5 | 1 | 1 | Yes | “Experimental pre-approved tool list” |
| Mistral Vibe | https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md | 200 | 77634 | fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0 | 1 | 1 | Yes | “allowed-tools: - read - grep - ask_user_question” |
| Codex | https://developers.openai.com/codex/skills | 200 | 417416 | 63064111759477928aedb9743030f315165e5fb5aeb3c5d2429b2dcd803c5504 | 0 | 0 | No occurrence | — |
| VS Code | https://code.visualstudio.com/docs/copilot/customization/agent-skills | 200 | 157102 | 4b40d645823df78c69cd55519aa5492262c7738aa197e7ee01e1ebfdb91547af | 0 | 0 | No occurrence | — |
| opencode | https://opencode.ai/docs/skills/ | 200 | 71581 | 3dfbef2163f9d05d4606209ba9a22194d5ab4fd74f50d350fd01767870124f6a | 0 | 0 | No occurrence | — |
| Gemini CLI | https://geminicli.com/docs/cli/skills/ | 200 | 114148 | b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640 | 0 | 0 | No occurrence | — |
| GitHub Copilot | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills | 200 | 566781 | e99da06055ca858c486cec1e834bc7353fb3b93525036ad2e10a032ea8e6eaea | 0 | 0 | No occurrence | — |
| Cursor | https://cursor.com/docs/context/skills | 200 | 490061 | abb0613a5403df0137472a0828e507f1129d939107876b3cf1657a0c703a2f1d | 0 | 0 | No occurrence | — |
| Amp | https://ampcode.com/docs/customize/skills | 200 | 105370 | 8f323d77909486a7c7d599855b84f54bff8379d700c2a6a77cadc5c6291fad89 | 0 | 0 | No occurrence | — |
| Roo Code | https://docs.roocode.com/features/skills | 200 | 71129 | fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2 | 0 | 0 | No occurrence | — |
| Kilo Code | https://kilo.ai/docs/customize/skills | 200 | 138104 | 26d76430140148d252c0195609682ae8bbb9d3d70ea9cd16c1cf6ae64ce52c08 | 0 | 0 | No occurrence | — |
| Junie | https://junie.jetbrains.com/docs/agent-skills.html | 200 | 38509 | a44a510e30445815b2f911fbaa77ca42e8f0504b3c4694507f053eb9425e9d21 | 0 | 0 | No occurrence | — |
| Hermes Agent | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | 200 | 206631 | 397e06d14a2b13620642a480ccc33bceeb2ed398f7c7b1b60118c1230b417f5c | 0 | 0 | No occurrence | — |
| Goose (planned census URL) | https://block.github.io/goose/docs/guides/context-engineering/using-skills/ | 404 | 932 | — | 0 | 0 | No; 404 | — |
| Windsurf | https://docs.windsurf.com/windsurf/cascade/skills | 200 | 471336 | a7e33f3a12363a33fd96e26e6a26e1d1f412dfc1c2a18d2715eb64f22f7cb85b | 0 | 0 | No occurrence | — |
| Cline | https://docs.cline.bot/features/skills | 200 | 228466 | ef602792f4d2074678eadcd39f1d506d604dbed4bbee69df05865792e6c57fdc | 0 | 0 | No occurrence | — |
| Continue | https://docs.continue.dev/customize/deep-dives/agent-skills | 404 | — | — | — | — | Not checked (404) | — |
| Zed | https://zed.dev/docs/ai/skills | 200 | 55646 | b5b780873b6ab6ef239953307f9e29db7cde24111ebdd1d951fb743ea22b747d | 0 | 0 | No occurrence | — |
| Kiro (steering docs, candidate) | https://kiro.dev/docs/steering/ | 200 | 322674 | d2c413e042842588a22aba1d3da409e5542d3ac08a6b3d480fd953b4e177f32b | 0 | 0 | No occurrence | — |
| Warp | https://docs.warp.dev/agents/skills | 404 | — | — | — | — | Not checked (404) | — |
| Augment | https://docs.augmentcode.com/commands/skills | 404 | — | — | — | — | Not checked (404) | — |
| Qwen Code | https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/ | 200 | 607888 | cd2f5ff04e4ff7dea07e440d5b823704134ad4089a473daf81086be389cc7b79 | 2 | 1 | Yes | “Qwen Code reads the allowedTools frontmatter field.” |
| Crush | https://github.com/charmbracelet/crush/blob/main/docs/skills.md | 404 | — | — | — | — | Not checked (404) | — |
| OpenHands | https://docs.all-hands.dev/usage/skills | 404 | — | — | — | — | Not checked (404) | — |
| Goose (alternate candidate URL) | https://block.github.io/goose/docs/guides/using-extensions/skills/ | 404 | — | — | — | — | Not checked (404) | — |
| Cody | https://sourcegraph.com/docs/cody/capabilities/skills | 404 | — | — | — | — | Not checked (404) | — |
| JetBrains AI Assistant | https://www.jetbrains.com/help/ai-assistant/agent-skills.html | 200 | 29830 | d333793e8433368b71d153b9aba8a96e57ed84bf1f99a71e6e81eef431e1817 | 0 | 0 | No occurrence | — |
| Aider (conventions page candidate) | https://aider.chat/docs/usage/conventions.html | 200 | 32512 | 5612a7fdbae67ead3ad0823d05ef85708f3165d49ddd1ec4917e2de6fe3db068 | 0 | 0 | No occurrence | — |
| Devin | https://docs.devin.ai/agents/skills | 404 | — | — | — | — | Not checked (404) | — |

## Assessment

Observed: the six frozen pages all still return HTTP 200 and all have at least one matching field occurrence. Their table population is therefore supported by this fetch; no missing-field/moved-page counterexample among the six. The twelve census-silent sources likewise reproduce their zero raw/text-view matches, except the planned Goose URL is still 404. This independent fetch did not find another Goose skills URL that resolved.

Fresh extension: Qwen Code is a stronger omission candidate than the zero-hit clients. Its docs explicitly state `allowedTools` (camel case) is read from frontmatter; source quote: “Qwen Code reads the allowedTools frontmatter field. An allowed-tools field written for another agent is ignored.” This differs in spelling but directly documents the corresponding permission-list concept and merits a later-round candidate review. The assigned frozen-table population is six pages that literally state `allowed-tools`; Qwen does not invalidate that literal census, but suggests the broader product population is incomplete if spelling variants count. This is a sourced discovery, not a counter result.

Other successful additional candidates with zero occurrences: Windsurf, Cline, Zed, Kiro steering docs, JetBrains AI Assistant, Aider conventions page. Candidate URLs returning 404 (Continue, Warp, Augment, Crush, OpenHands, second Goose URL, Cody, Devin) are not evidence of absence. No full three-part negative sweep was performed, so all zero-match findings describe fetched bytes only.

Freshness limitation: I started an independent second Factory fetch with a 60-second delay; the first returned same 341235-byte hash above. The fetch process was cut off by the tool's 130-second deadline before the second result arrived. Therefore byte-to-byte change status after a minute is unresolved; no claim that any URL was stable across two fetches. L1 receipt does not provide hashes or comparable per-page second fetches, and same-size bytes alone cannot establish sameness.

VERDICT: Frozen six-page literal-field population confirmed on this fetch; Qwen Code's `allowedTools` documentation is a notable broader-population omission candidate; one-minute byte-change test unresolved.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79S08CensusRederive.md