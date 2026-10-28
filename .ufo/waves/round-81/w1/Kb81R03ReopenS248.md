# Kb81R03ReopenS248 — Re-open S248/S249 access records (round 81, w1)

Scope: re-fetch `https://code.claude.com/docs/en/agent-sdk/skills.md` (C2 surface S249; previously probed as queued S248) and `https://code.claude.com/docs/en/skills.md` (S227 CLI page); record http/bytes/sha256/utc; check the line-348 sentence occurrence count and the r80 S227 quote; flag byte instability; reconcile with seat Kb81E08C2Entry's canonical snapshot.

## Method (all commands run under /fast/scratch/hyaku/kotoba-r81/Kb81R03ReopenS248, TMPDIR set, scratch removed on yield)

Both URLs fetched twice each: `curl -sSL -A 'Mozilla/5.0' --max-time 90 -o <f> -w '...' <url>`.

- SDK page: two fetches at 2026-10-28T02:28:23Z and :24Z — both HTTP 200, 28395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`; `cmp sdk_1.md sdk_2.md` rc=0.
- CLI page: two fetches at 2026-10-28T02:28:23Z — both HTTP 200, 117962 B, sha256 `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9`; `cmp cli_1.md cli_2.md` rc=0; `cmp cli_1.md .ufo/waves/round-79/snapshots/S227-claude.md` rc=0 (live bytes identical to the committed r79 snapshot).

Fetch records: `.ufo/waves/round-81/build/Kb81R03Reopen-fetch.json`.

## Findings

### 1. SDK page (S249 surface) — line-348 sentence occurs exactly once

`sed -n '348p'` (the `§ Pre-approve tools for skills` note under `> [!NOTE]`):

> In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's [`allowed-tools`](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill) frontmatter or with the `allowedTools` option (`allowed_tools` in Python) in your query configuration. If your organization sets [`allowManagedPermissionRulesOnly`](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly) in managed settings, Claude Code ignores both. Skills [synced from claude.ai](https://code.claude.com/docs/en/skills.md#how-claude-code-handles-the-frontmatter-of-a-synced-skill) follow their own frontmatter rules.

- `grep -Fxc "<line 348>" sdk_1.md` → 1. The sentence fragment `In SDK sessions, you can pre-approve tools for a project or personal skill` → `grep -cF` 1. The S248 row's normalized located quote (`"In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option"`) → `grep -cF` **0** in raw bytes: link markup interrupts it (`[`allowed-tools`](url)`). For the C2 entry's located quote (must occur in the snapshot's text view): verbatim raw substrings that do match once are e.g. `with the `allowedTools` option (`allowed_tools` in Python) in your query configuration` (grep -cF = 1), `When you set `skills`, the SDK adds the Skill tool to `allowedTools` automatically` (line 46, grep -cF = 1), and `The list pre-approves the named tools rather than restricting the others.` (line 389, grep -cF = 1). The line-389 sentence is a plain-text 11-word verbatim candidate; the line-46 sentence is 14 words verbatim. The stripped-markdown rendering of the line-348 sentence also occurs once.
- Grant note at line 389 (S248's second located quote) is present verbatim (raw text, count 1).
- Page shape: llms.txt-style .md export; first heading `# Extend agents with skills` at line 5; `allowedTools` token appears 5×, `allowed-tools` 1×, `allowed_tools` 4×.

### 2. CLI page (S227) — r80 quote still present verbatim, no drift

- Located quote `"allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval."`: the raw line carries a leading `` `allowed-tools` `` field name in backticks (`The `allowed-tools` field grants permission ...`), so the normalized fragment `allowed-tools field grants permission ... approval.` → `grep -cF` 0, but the full paragraph at **line 617** is present verbatim including the quote text (`grep -nF 'grants permission'` → line 617). § anchor lines 617 (`§ Pre-approve tools for a skill`) and 643 (`§ When only managed permission rules apply` / `allowManagedPermissionRulesOnly` paragraph) match the S227 row exactly.
- `cmp` vs `.ufo/waves/round-79/snapshots/S227-claude.md` rc=0 — the page's raw .md bytes have NOT changed since the r79 pin.
- The r80 spotcheck row (corpus/lessons/round-80-verifier-spotcheck.md:49) claimed 'live page now reads differently ("grants permission" wording replaced by "without asking permission" table row)'. **Not confirmed in raw bytes**: `without asking permission` occurs at line 404 and `grants permission` at line 617 in BOTH the r79 committed snapshot and the live bytes (identical greps on both files). Both wordings coexisted in the pinned bytes; the spotcheck compared different sections, not a live-vs-snapshot diff. No M-class instability.

### 3. Byte stability summary — no M-class event

| Page | Live sha256 (2× fetch) | Pin/snapshot sha256 | Match |
|---|---|---|---|
| agent-sdk/skills.md (S249) | ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2 | same (S248 row; E08 S249.md; Kb80S05 r80 build copy) | yes |
| skills.md (S227) | 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9 | same (S227 row; r79 S227-claude.md; Kb80R03 r80 refetch) | yes |

### 4. E08 canonical snapshot reconciliation

`.ufo/waves/round-81/snapshots/S249.md` was published by Kb81E08C2Entry (fetch record `S249.fetch.json`, fetched_utc 2026-10-28T02:27:26Z) ~1 min before my fetch. `sha256sum` on it = ac62c2df…; `cmp` vs my bytes rc=0 — **sha256 does NOT differ from E08's, so no flag**; E08's file stands as the canonical snapshot (identical bytes, earlier publication; preferring my fetch would change nothing). I did not overwrite it.

## Tooling

None installed (curl/sha256sum/cmp/grep/sed already present). No pacman run (host-wide pause honored).

VERDICT: S249 SDK page byte-stable at sha256 ac62c2df (line-348 sentence occurs exactly once; verbatim quote candidates exist at lines 46/348/389); S227 CLI page byte-identical to the r79 pin (r80 quote present at line 617); the r80 'live drift' note is not confirmed — no M-class instability; E08's S249.md confirmed canonical (cmp rc=0, no flag).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81R03Reopen-fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R03ReopenS248.md
