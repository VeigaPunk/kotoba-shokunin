# ReopenS094 — Cursor row re-opened (kotoba round 58, falsify)

Result: HOLDS — every S094 byte-count/sha, the `:54` quote (byte-exact, unshaped), and every fact in the SKILL.md `What a file sets`/`Action` cells and the entry bullet verified against refetched byte-identical pages; two calibration findings (unsourced scope word "(project)"; the live-page arm of the frozen counter now reads Cursor `found=no` because cursor.com 403s Python-urllib fetches, which does not flip the frozen predicate).

Measured revision (content under attack): `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. Lane read-only; all execution in sandbox clone `/fast/scratch/hyaku/kotoba-r58/ReopenS094/clone` (checkout of that rev; no sandbox commits made). No tools installed (curl/python3/git already present).

## Fetch records (all `date -u` lines as observed)

| URL | UTC access | Status | Bytes | sha256 |
|---|---|---|---|---|
| https://cursor.com/docs/reference/deeplinks.md | Fri 23 Oct 2026 08:29:02 AM UTC | HTTP 200 | 5,972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| https://cursor.com/docs/customize-cursor.md | Fri 23 Oct 2026 08:29:02 AM UTC | HTTP 200 | 5,200 | `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e` |
| https://cursor.com/changelog/1-6 | Fri 23 Oct 2026 08:29:17 AM UTC | HTTP 200 | 145,839 | `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152` |

All three match the S094 row's fetch records byte-for-byte (corpus/SOURCES.md:106 at 46b4a70). Both docs URLs serve `text/markdown; charset=utf-8` (probed 08:29:02Z), confirming the row's "(direct Markdown, no bytes stripped)". The changelog row note "HTML tags stripped for rendered quote; not the scored source URL" is accurate: the recorded sha/bytes are of the raw HTML; I stripped tags the same way and found the same sentence.

## Quote verbatim at the stated line

Entry `corpus/knowledge/command-files-round58.md:39`, lesson `corpus/lessons/round-58.md:14`, and the quote cell all carry, byte-exact (checked by substring count: 1 occurrence in each file, and 1 occurrence in the fetched bytes):

> "Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory."

It is the second sentence of `deeplinks.md:54` (first sentence: "Share commands that others can execute directly in their Cursor environment."). 13 words with backticks intact — no shaping, within E6's 6–25. **Q42 verdict: accurate.** The entry's quote-note paragraph (`command-files-round58.md:28-31`) claims every quote is copied from the fetched bytes and names shaping only for VS Code (table pipes → `&#124;`), Gemini CLI (list marker/bold kept), and opencode (pinned source); the Cursor quote needed no shaping and got none — confirmed byte-exact. The SOURCES-row scope cell also checks out: `§ Commands` heading at `deeplinks.md:52`, quote at `:54` (range `52-54` correct); name/content parameters at `:72-73` inside the cited `:67-74`; page `:54` says "creates a new command with the specified name and content", matching the row's "command-deeplink name/content model".

## Fact table — one line per fact

SKILL.md:118 (§ Custom command files by client, Cursor row) and entry `command-files-round58.md:55-56`:

| # | Fact (where claimed) | Verdict | Page evidence |
|---|---|---|---|
| 1 | Command files token `.cursor/commands` (SKILL.md:118; entry:39) | **holds** | deeplinks.md:54, byte-exact inside the quote |
| 2 | "(project)" scope word (SKILL.md:118) | **unsourced** (not contradicted) | "project" occurs 0 times in deeplinks.md; customize-cursor.md's 3 "project" hits are all rules links (line 27, `rules.md#project-rules`). The folder is a dot-path whose project-relative placement is convention, not page text. No user-level commands folder is documented anywhere in the current docs tree either (docs index llms.txt lists only Cursor *CLI* slash-commands pages), so the annotation contradicts nothing — it is the reviewer's application of the frozen row rule's "the only one documented" case |
| 3 | "Markdown workflow prompt" (SKILL.md:118) | **holds** | customize-cursor.md:31: "Commands are markdown files that define a focused workflow or action." + "Reusable prompts you invoke with `/` in Agent chat." |
| 4 | "no frontmatter or argument schema documented" (SKILL.md:118; entry:56) | **holds** | 0 occurrences of frontmatter/front-matter/argument/YAML in deeplinks.md and customize-cursor.md; changelog's 7 "argument" hits are all `arguments` in JS analytics stubs, not a command schema. Citations land: folder sentence at `S094 :54`, markdown sentence at `customize-cursor.md:31` |
| 5 | Action "Audit the body only; nothing else to check" (SKILL.md:118) | **holds as grounded judgment** (see finding F3) | within the scored pages nothing else is documented; the row's supplemental changelog does document filename/invocation but is excluded from scoring by the frozen E3 row rule (lesson § Rejected, round-58.md:33-34) and is disclosed in the SOURCES row itself |
| 6 | Entry bullet "Markdown files in the project folder (customize-cursor.md:31, supporting page in the S094 row)" (entry:55) | **holds except "project"** (same as #2) | attribution is honest: "Markdown files" from customize-cursor.md:31; the folder from the S094 row (deeplinks.md:54); the word "project" from neither |
| 7 | Entry bullet "no frontmatter or argument schema is documented on these pages" (entry:56) | **holds** | as #4, across all three row pages |
| 8 | SOURCES row scope text: "supporting docs describe Markdown prompt files and a `[command].md` form" (SOURCES.md:106) | **holds** | customize-cursor.md:31; changelog stripped-text line 2: "Commands are stored in .cursor/commands/[command].md." |
| 9 | Lesson reject: `[command].md` "printed only on a changelog page" (round-58.md:33-34) | **holds** | `[command]` occurs in neither docs page (substring check False on both); only on the changelog |
| 10 | Row metadata: kind docs, tier A, status mined, opened 2026-10-23, recheck 90d, used-by the entry (SOURCES.md:106) | **holds** | present in the row; row URL is not a changelog/release path (E3 clean) |

The other Cursor rows in SKILL.md (:90 agents, :104 plugin manifests, :196 compression, :210 invocation) cite other sources (`cursor-skills.md`, plugin round-57 basis), not S094; S094's used-by is the command-files entry only. No false S094 backing anywhere — those rows are outside this item's named scope.

## Findings by severity

**F1 (calibration, medium) — the frozen counter's Cursor arm is environment-sensitive right now; predicate still passes.** L1 receipt `.ufo/waves/round-58/C1-measure.txt` (run 2026-10-23T08:20:43Z): `Cursor BACKED … found=yes`, `6 of 6; new ground 4`, exit 0. My sandbox rerun of the same frozen command (`python3 -B verifiers/check_command_files.py --rev 46b4a70… --fetch`, counter sha `aae12d36…` matching the receipt) at 08:34Z and again 08:36:03Z: `Cursor … found=no`, `5 of 6; new ground 3`, **exit 0 both times**. Cause isolated: cursor.com returns **HTTP 403 Forbidden** to the counter's own request shape (Python urllib, UA `kotoba-shokunin-counter/58`) at 08:35:29Z and still at 08:38:06Z, while curl gets HTTP 200 with the byte-identical page — including curl carrying the *same* UA string at 08:36:02Z. The discriminator is the client fingerprint (TLS/header set), not the UA string, and serving changed between 08:20Z (found=yes) and 08:34Z. The counter's "fetch failure = not found" is by design (docstring, check_command_files.py fetch()), so the behavior is honest; but the printed measurement line is not stable across runs this hour. Any seat re-running C1 now will see 5 of 6 / new ground 3 — that is the 403, not a content regression: the scored page still carries the quote (my 200-fetch is byte-identical to the scored fetch). I did not attempt to evade the bot filter (bounds); the diagnosis stops at fingerprint-vs-UA.

**F2 (calibration, low) — predicate margins under Cursor degradation.** Degraded state sits exactly at G's floor: G=3 = NEW_TARGET=3; F=5 ≥ TARGET=4 (two further failures of slack). The Cursor arm alone can never flip exit 1; but if any one *other* new-ground arm (Claude Code, Gemini CLI, opencode — each `held-at-base=no`) degraded in the same run, G=2 < 3 and exit flips. The frozen targets were sized with F-slack and zero G-slack; the claim's content dependence is exactly "Cursor plus one more vendor fetch must succeed".

**F3 (text, low) — "(project)" is a scope word the pages never say.** Facts #2/#6 above. Neither cited page states a project/user folder distinction for commands; the current docs tree documents no user-level commands folder at all. Correction text the L1 may integrate: in SKILL.md:118 and entry:55, either drop "(project)"/"project folder" (the pages say only "your `.cursor/commands` directory", deeplinks.md:54) or keep it marked as the row-rule's lead-folder annotation. The frozen row rule itself is not attacked.

**F4 (observation, info) — Action cell vs the row's own supplemental page.** The Action cell "nothing else to check" is true of the scored pages, but the SOURCES row's supplemental changelog documents the `[command].md` filename and `/`-invocation (stripped line 2). The exclusion is the frozen E3 rule and the row discloses the page, so this is not a defect — a reader auditing a Cursor command file may still want the filename→invocation check the SOURCES row points at.

## Residual risk and verification gaps

- Whether cursor.com's urllib 403 is IP-rate-scoring or pure fingerprinting was not determined further (two probes only; no header-crafting evasion attempted per bounds). The 08:20Z found=yes vs 08:34Z found=no flip shows serving-side change or rate scoring; either way re-runs are not byte-stable on this arm today.
- The real-world existence of a user-level `~/.cursor/commands` folder is unverified: no current docs page documents one (llms.txt index checked), so "(project)" is uncontradicted, not confirmed. Marked [INFERENCE]-free: everything above is from fetched bytes or lane files.
- I did not re-run the other five clients' fetches beyond what the counter did; their arms printed found=yes in my sandbox runs at 08:34/08:36Z (Claude Code, Codex, VS Code, Gemini CLI, opencode), which is evidence, not proof, that only the Cursor arm is affected right now.
- Quotes above are byte-exact from the fetched files in `/fast/scratch/hyaku/kotoba-r58/ReopenS094/` (`deeplinks.md`, `customize-cursor.md`, `changelog-1-6.html`); line numbers are of the fetched bytes.
