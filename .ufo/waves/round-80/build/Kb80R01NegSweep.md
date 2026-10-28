# Kb80R01NegSweep — negative sweep: the 12 census-negative clients, re-opened live (round 80 w1)

Seat: Kb80R01NegSweep (leaf scout). Date: 2026-10-27. Wave: round 80 w1.
Purpose: ground the S232+ rejection rows of `corpus/SOURCES.md` and the round-80
lesson `## Gate` with my-own-eyes fetch records for the 12 clients the r79 census
recorded as NOT documenting the `allowed-tools` frontmatter field
(`plans/round-79.md` § C2 population census; receipt
`.ufo/waves/round-79/receipts/c2-census-l1.txt`).

URL list recovered from `.ufo/waves/round-79/receipts/c2-census-l1.txt:23-38`
(raw lines; note the census's `kilo` URL is `https://kilo.ai/docs/customize/skills`).

## Method

Per page, fetched twice (two independent passes, ≤4 concurrent curls each):

```
curl -sSL -A 'Mozilla/5.0' --max-time 60 -D headers.txt -o body.html \
  -w 'final_url/http_status/bytes/time' <url>
sha256sum body.html
grep -oi  'allowed[-_ ]tools' body.html | wc -l   # r79 census pattern (case-insens.)
grep -oiE 'allowed[-_]tools'  body.html | wc -l   # seat-brief pattern
grep -c   'allowed-tools'     body.html           # case-sensitive literal
grep -oiE 'allowed.{0,2}tools' body.html | wc -l  # broad variant sweep (catches allowedTools / "allowed tools")
```

- curl 8.23.0 (x86_64-pc-linux-gnu), OpenSSL 3.6.5. UA `Mozilla/5.0`.
- Fetch UTC recorded per pass; the two passes ran 2026-10-27T23:13:14Z and
  2026-10-27T23:13:43–44Z.
- Verdict criterion (identical to the r79 census receipt label): 0 occurrences of
  `allowed[-_ ]tools` (case-insensitive) on the raw fetched bytes = negative.
  A page with ≥1 hit would be an admit candidate (would have triggered
  `Kb80R01NegSweep-admit.md`). No page triggered it — no admit file exists.

## Summary

12 of 12 NEGATIVE. Every page: 0 hits on all four patterns, both passes.
11 of 12 byte-identical across passes; `amp` differs only in rotating CSP
`<script nonce=` attributes (content identical). `goose` is HTTP 404 (as the r79
census recorded). Four census URLs now redirect (codex, vscode, ghcopilot,
cursor — one hop each) and `roo` redirects twice; chains below.

| id | final status | bytes | hits (r79 pat) pass1/pass2 | stability |
|---|---|---|---|---|
| codex | 200 | 417416 | 0 / 0 | SAME |
| vscode | 200 | 157102 | 0 / 0 | SAME |
| opencode | 200 | 71581 | 0 / 0 | SAME |
| gemini | 200 | 114148 | 0 / 0 | SAME |
| ghcopilot | 200 | 566781 | 0 / 0 | SAME |
| cursor | 200 | 490061 | 0 / 0 | SAME |
| amp | 200 | 105308 | 0 / 0 | DIFF (CSP nonce only) |
| roo | 200 | 71129 | 0 / 0 | SAME |
| kilo | 200 | 138104 | 0 / 0 | SAME |
| junie | 200 | 38509 | 0 / 0 | SAME |
| goose | 404 | 932 | 0 / 0 | SAME |
| hermes | 200 | 206631 | 0 / 0 | SAME |

## Per-client fetch records

### 1. codex — NEGATIVE
- census URL: `https://developers.openai.com/codex/skills`
- chain: 301 `location: https://learn.chatgpt.com/docs/build-skills` → 200
- final URL: `https://learn.chatgpt.com/docs/build-skills`
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 417416 B, sha256 `e657e0e3fd937024fa6d686b28b6d54f9dfc637279a71eb564e93532d27f3860`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: r79pat 0, brief 0, case-sensitive 0, broad 0
- page identity: title "Codex | OpenAI Developers" (the Codex skills build doc).
- note: byte count 417416 equals the r79 census line for codex — the r79 fetch
  already followed this same redirect.

### 2. vscode — NEGATIVE
- census URL: `https://code.visualstudio.com/docs/copilot/customization/agent-skills`
- chain: 301 `location: /docs/agent-customization/agent-skills` → 200
- final URL: `https://code.visualstudio.com/docs/agent-customization/agent-skills`
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 157102 B, sha256 `4b40d645823df78c69cd55519aa5492262c7738aa197e7ee01e1ebfdb91547af`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Use Agent Skills in VS Code".

### 3. opencode — NEGATIVE
- census URL: `https://opencode.ai/docs/skills/` (no redirect)
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 71581 B, sha256 `3dfbef2163f9d05d4606209ba9a22194d5ab4fd74f50d350fd01767870124f6a`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Agent Skills | OpenCode".

### 4. gemini — NEGATIVE
- census URL: `https://geminicli.com/docs/cli/skills/` (no redirect)
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 114148 B, sha256 `b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Agent Skills | Gemini CLI".

### 5. ghcopilot — NEGATIVE
- census URL: `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills`
- chain: 301 `location: /en/copilot/concepts/customizations/agent-skills` → 200
- final URL: `https://docs.github.com/en/copilot/concepts/customizations/agent-skills`
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 566781 B, sha256 `e99da06055ca858c486cec1e834bc7353fb3b93525036ad2e10a032ea8e6eaea`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Agent skills - GitHub Docs".

### 6. cursor — NEGATIVE
- census URL: `https://cursor.com/docs/context/skills`
- chain: 301 `location: /docs/skills` → 200
- final URL: `https://cursor.com/docs/skills`
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 490061 B, sha256 `abb0613a5403df0137472a0828e507f1129d939107876b3cf1657a0c703a2f1d`
- pass 2: 2026-10-27T23:13:43Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Agent Skills | Cursor Docs".

### 7. amp — NEGATIVE
- census URL: `https://ampcode.com/docs/customize/skills` (no redirect)
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 105308 B, sha256 `d8a8eeb0b2fa7f9089113d34d1a408bc2e918946432f998803e3f05d3deddc07`
- pass 2: 2026-10-27T23:13:44Z, HTTP 200, 105308 B, sha256 `2bfc32145ec34fda3cf41796a691beb22863106e7509154a1ee146f7e1c0ca70`
- stability: DIFF — `diff` of the two bodies shows only the rotating CSP
  `<script nonce="…">` attribute values (3 occurrences); text content identical.
- hits: 0 / 0 / 0 / 0
- page identity: title "Skills | Amp Docs".

### 8. roo — NEGATIVE
- census URL: `https://docs.roocode.com/features/skills`
- chain: 301 `location: https://roocodeinc.github.io/Roo-Code/features/skills`, then
  301 `location: https://roocodeinc.github.io/Roo-Code/features/skills/` → 200
- final URL: `https://roocodeinc.github.io/Roo-Code/features/skills/`
- pass 1: 2026-10-27T23:13:14Z, HTTP 200, 71129 B, sha256 `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2`
- pass 2: 2026-10-27T23:13:44Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Skills | Roo Code Documentation".

### 9. kilo — NEGATIVE
- census URL: `https://kilo.ai/docs/customize/skills` (no redirect)
- pass 1: 2026-10-27T23:13:15Z, HTTP 200, 138104 B, sha256 `2ed06ad1c20c546d315c120849e35b6861ece1ec1526da9186ce2f04a5ba7353`
- pass 2: 2026-10-27T23:13:44Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Skills".

### 10. junie — NEGATIVE
- census URL: `https://junie.jetbrains.com/docs/agent-skills.html` (no redirect)
- pass 1: 2026-10-27T23:13:15Z, HTTP 200, 38509 B, sha256 `a44a510e30445815b2f911fbaa77ca42e8f0504b3c4694507f053eb9425e9d21`
- pass 2: 2026-10-27T23:13:44Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Agent skills | Junie Documentation".

### 11. goose — NEGATIVE (HTTP 404)
- census URL: `https://block.github.io/goose/docs/guides/context-engineering/using-skills/`
- chain: none — direct 404, final URL = census URL.
- pass 1: 2026-10-27T23:13:15Z, HTTP 404, 932 B, sha256 `c5b27efd5464711cad2593489c9d56b6dd3b098428ea52d46fac4e35c4aeba34`
- pass 2: 2026-10-27T23:13:44Z, HTTP 404, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0 (404 body; title "Page not found").

### 12. hermes — NEGATIVE
- census URL: `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills` (no redirect)
- pass 1: 2026-10-27T23:13:15Z, HTTP 200, 206631 B, sha256 `6817301c1b1a345c31c0c0f57e512b3f9d20d8fda2744f8757f30b9efae19a85`
- pass 2: 2026-10-27T23:13:44Z, HTTP 200, byte-identical (SAME)
- hits: 0 / 0 / 0 / 0
- page identity: title "Skills System | Hermes Agent".

## Near-neighbor advisory (NOT admits)

Variant tokens that a hostile reading might raise, all checked and excluded:

- `ghcopilot`: "allowing-tools" (2×) is a docs-nav link to
  `/en/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools` ("Allowing
  tools", a Copilot CLI how-to about approving tool use) — a different page and
  concept, not the frontmatter field.
- `roo`: "available-tools" (2×) is a docs-section path
  (`/Roo-Code/advanced-usage/available-tools/…`) about which tools exist — not
  the frontmatter field.
- `hermes`: `requires_tools`, `fallback_for_toolsets`, `requires_toolsets`
  config keys — Hermes's own toolset grammar, no `allowed-tools` key.
- broad sweep `grep -oiE 'allowed.{0,2}tools'`: 0 hits on all 12 bodies
  (covers `allowedTools`, `allowed tools`, `allowed-tools`, `allowed_tools`).

## Findings for the L1 (rejection rows S232+)

- 12/12 negative confirmed live this round, each with URL, two fetch records
  (status/bytes/sha256/UTC) and 0-hit greps — sufficient ground for 12 rejection
  rows. `goose` carries its 404 record as the r79 census did.
- Four census URLs moved server-side since r79 (codex, vscode, ghcopilot,
  cursor → one-hop 301s; roo → two-hop 301s). The rejection rows should cite the
  census URL and may note the current final URL from this file.
- No admit candidates. `Kb80R01NegSweep-admit.md` intentionally absent.
