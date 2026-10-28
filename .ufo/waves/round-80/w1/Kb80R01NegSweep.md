# Seat report — Kb80R01NegSweep (round 80 w1, leaf scout)

Item: negative sweep of the 12 census-negative clients named in
`plans/round-79.md` § C2 population census / `.ufo/waves/round-79/receipts/c2-census-l1.txt`
(Codex, VS Code, opencode, Gemini CLI, GitHub Copilot, Cursor, Amp, Roo, Kilo,
Junie, Hermes, Goose-404).

## What I did

1. Recovered the exact 12 URLs from `.ufo/waves/round-79/receipts/c2-census-l1.txt:23-38`
   (raw read; `kilo` = `https://kilo.ai/docs/customize/skills` — not kilocode.ai).
   Cross-checked against `plans/round-79.md` § C2 — same 12.
2. Fetched each page MYSELF twice (passes at 2026-10-27T23:13:14Z and
   2026-10-27T23:13:43–44Z): `curl -sSL -A 'Mozilla/5.0' --max-time 60 -D headers -o body`,
   recording per pass: UTC time, redirect chain (from `location:` headers), final
   URL, HTTP status, bytes, sha256 of the body. curl 8.23.0. ≤4 concurrent curls.
3. Grepped every body for `allowed[-_ ]tools` (r79 census pattern, case-insensitive),
   `allowed[-_]tools` (brief pattern), case-sensitive `allowed-tools`, and a broad
   `allowed.{0,2}tools` variant sweep (catches `allowedTools`, `allowed tools`).
4. Cross-pass comparison: sha256 equality both passes; `diff` where hashes differed.
5. Extracted page `<title>` per body as page-identity ground; characterized the
   nearest variant tokens found (`allowing-tools` on ghcopilot = nav link to a
   Copilot CLI how-to; `available-tools` on roo = docs section; Hermes
   `requires_tools`/`fallback_for_toolsets` config keys).

## Result

- 12/12 NEGATIVE: 0 hits on all four patterns, both passes, all 12 bodies.
- 11/12 byte-identical across passes; `amp` differs only in 3 rotating CSP
  `<script nonce=` attribute values (content identical).
- `goose`: HTTP 404, 932 B, byte-identical across passes (matches r79 census).
- Redirects since r79: codex → `learn.chatgpt.com/docs/build-skills` (301);
  vscode → `/docs/agent-customization/agent-skills` (301); ghcopilot →
  `/en/copilot/concepts/customizations/agent-skills` (301); cursor → `/docs/skills`
  (301); roo → `roocodeinc.github.io/Roo-Code/features/skills/` (301×2). Chains
  recorded per client in the build file.
- No page mentions the field → NO admit candidates →
  `Kb80R01NegSweep-admit.md` intentionally not created.

## Full evidence

Per-client fetch records (two passes each: status, bytes, sha256, UTC, chain,
grep counts, page title) are published in
`.ufo/waves/round-80/build/Kb80R01NegSweep.md`. That file is the ground for the
S232+ rejection rows; the L1 can lift URL + access date + identity quote per row
from it.

## Coordination

- Replied to Kb80E10Battery: this seat produces none of the six C1 stack items
  (E01–E06); my output is C2 evidence, not a patch.
- No other peer outputs consumed (none needed — the r79 receipt is the sole input).

## Tooling

No installs or upgrades: curl 8.23.0 and grep were already present. Nothing
installed via any channel.

## Scratch

Working dir `/fast/scratch/hyaku/kotoba-r80/Kb80R01NegSweep/` (pages, pages2,
urls.txt, fetch1.sh, fetch2.sh) — removed before yield; the only persisted
artifacts are the two reports below (scratch dir deletion verified by command in
this session; bodies were never copied into the lane).

VERDICT: 12/12 census-negative clients confirmed negative live this round (0 hits all patterns, 2 passes each; goose 404; 4 URLs redirected, chains recorded) — grounds S232+ rejection rows, no admits.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R01NegSweep.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80R01NegSweep.md
