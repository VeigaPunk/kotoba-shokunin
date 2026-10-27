# Kb79R02ClaudeRow — surface `claude`, registry id S227 (drafts; the L1 stitches)

Snapshot: `.ufo/waves/round-79/snapshots/S227-claude.md` (117 962 B, sha256 `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9`), pin `.ufo/waves/round-79/snapshots/S227.manifest`, fetch record `.ufo/waves/round-79/snapshots/S227.fetch.json`. Fetched twice (`curl -sSL -A 'Mozilla/5.0' --max-time 60`), 2026-10-27T21:41:02Z and 2026-10-27T21:41:04Z, both HTTP 200 / 117 962 B / identical sha256.

**Pre-data amendment (L1, via IRC):** the frozen grant-grounding token for claude is `without prompting you for approval`, and the entry quote must be a pipe-free prose quote. Both rows below use that. The earlier draft's table-row quote (L404, token `without asking permission`) is superseded and kept only in `.ufo/waves/round-79/build/Kb79R02ClaudeRow.facts.txt`; receipt for this version: `.ufo/waves/round-79/build/Kb79R02ClaudeRow.quote-amended.txt`.

## 1. Registry row for corpus/SOURCES.md (11 cells)

| S227 | Claude Code — Extend Claude with skills (skills.md) — https://code.claude.com/docs/en/skills.md | docs | B | what the allowed-tools frontmatter field grants in Claude Code and when managed settings withhold it; tier B because the page is one vendor's own product documentation, states no conformance to the open specification and states no revision of itself — tier A for what the field is stays with the open-spec row S226 | § Frontmatter reference, row `allowed-tools` (L404), and § Pre-approve tools for a skill (L617), with § When only managed permission rules apply (L643) as the caveat; the page states no revision for itself (no last-modified, no commit in the bytes) and names Claude Code v2.1.282 as the version floor for that caveat; quote "The `allowed-tools` field grants permission for the listed tools during the turn that invokes the skill" (16 words); fetched 2026-10-27T21:41:02Z, HTTP 200, 117962 B, sha256 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9 | in Claude Code the field is a per-turn pre-approval grant that clears on the next user message, does not restrict the tool pool, and is ignored for project and personal skills when managed settings set `allowManagedPermissionRulesOnly` | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

## 2. Entry-table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| Claude Code | S227 | `allowed-tools`, `space- or comma-separated string`, `YAML list`, `without prompting you for approval` | pre-approves | located quote "`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval." |

Row shape: 5 cells (`awk -F'|'` → NF=7); no `|` inside any cell, so a plain `[1:-1].split("|")` parses it, same as r73's `_cells`.

## 3. Q53 — proof the quotes are page bytes

Command and output, verbatim (receipts `.ufo/waves/round-79/build/Kb79R02ClaudeRow.quote-amended.txt` and `…facts.txt`):

```
$ sed -n '617p' S227-claude.md
The `allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval. The grant clears when you send your next message, even though the skill content [stays in context](#skill-content-lifecycle); invoking the skill again re-applies it for that turn. It does not restrict which tools are available: every tool remains callable, and your [permission settings](https://code.claude.com/docs/en/permissions.md) still govern tools that are not listed. To pre-approve tools for the whole session rather than a single turn, add allow rules to those permission settings instead.

$ grep -n -F '`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval.' S227-claude.md
617:The `allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval. The grant clears when you send your next message, even though the skill content [stays in context](#skill-content-lifecycle); invoking the skill again re-applies it for that turn. It does not restrict which tools are available: every tool remains callable, and your [permission settings](https://code.claude.com/docs/en/permissions.md) still govern tools that are not listed. To pre-approve tools for the whole session rather than a single turn, add allow rules to those permission settings instead.
grep rc=0

$ sed -n '643p' S227-claude.md
When your organization sets `allowManagedPermissionRulesOnly` in managed settings, Claude Code ignores `allowed-tools` in project and personal skills and in the [other sources the setting's entry lists](https://code.claude.com/docs/en/settings-reference.md#allowmanagedpermissionrulesonly). This requires Claude Code v2.1.282 or later.
```

Bytes dropped, joined or shaped:

- Entry quote (25 words): **one contiguous slice of line 617**, byte offset 68 988 of the snapshot, `raw_count == 1`, `whitespace-collapsed count == 1`, ground-token hits 1. It starts at the page's own `allowed-tools` token and stops after "approval." — the page's `The ` immediately before it and the rest of the paragraph after it are outside the quote. **Nothing inside was dropped, joined, re-ordered, de-marked-up or entity-decoded**; both words of the value form and the ground phrase are page bytes.
- Registry quote (16 words): a **strict prefix of the same line**, offset 68 984, `raw_count == 1`, collapsed count 1; it stops before ", so Claude can use them without prompting you for approval." Nothing inside is shaped. It is quoted short (16 of 25) so that a word-count checker that splits on punctuation as well as whitespace cannot push it over 25.
- The page is the `.md` export (`## Documentation Index` is line 1), plain UTF-8 markdown, 0 NUL bytes: there are no HTML tags to strip and no character references to decode anywhere on line 617. The only transformation applied to either quote is **none** (the spaces are already single).

Word-bounded occurrences of the four page tokens in the snapshot (ASCII boundaries, `(?<![A-Za-z0-9_-])tok(?![A-Za-z0-9_-])`): `allowed-tools` 21, `space- or comma-separated string` 2, `YAML list` 4, `without prompting you for approval` 1.

## 4. Q70 — the quote is not another page's text

Other page: https://agentskills.io/specification.md, read from the byte-identical snapshot `.ufo/waves/round-79/snapshots/S226-spec.md` (7 608 B, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` — the S226 seat's snapshot and this seat's independent 2026-10-27T21:41:54Z fetch are the same bytes).

```
$ grep -c -F '`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval.' S226-spec.md
0        # grep rc=1 (zero matches — the count is the datum)
$ grep -c -F '<same quote>' S227-claude.md
1        # rc=0
```

Whitespace-collapsed: `S226-spec.md collapsed_count 0`, `S227-claude.md 1`; the spec snapshot also has 0 hits for the ground phrase `without prompting you for approval`. The spec page's own field row is `| allowed-tools | No | Space-separated string of pre-approved tools the skill may use. (Experimental) |` (L35) — a different sentence and a different grant semantics (`Experimental`), so the claude quote is not reachable from the spec page.

Scope of the negative: 1 of the other 5 surface pages was searched here; factory, msaf, pi and vibe are other seats' pages and the full-set sweep belongs to the L1.

## 5. Reading — what the page says, what it does not, and whether `pre-approves` is true

The page states the field is a **per-turn permission grant, not a restriction**: L617 says it "grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval", that the grant clears on the next user message, and that "It does not restrict which tools are available: every tool remains callable, and your permission settings still govern tools that are not listed"; the frontmatter-reference row (L404) adds the value forms ("a space- or comma-separated string, or a YAML list") and L619 adds that workspace trust does not gate the field, so a checked-in skill can grant itself broad tool access. Its Limits are stated twice and are real: `#### When managed settings lock hooks to plugins` (L636) — a skill declaring `hooks` under `strictPluginOnlyCustomization` loses its `allowed-tools` pre-approval; `#### When only managed permission rules apply` (L643) — with `allowManagedPermissionRulesOnly` set, Claude Code "ignores `allowed-tools` in project and personal skills", listed tools fall back to the managed rules and the normal prompt, and this "requires Claude Code v2.1.282 or later" (the only version marker the page gives for the field). What the page does **not** say: it never calls the field experimental, never says it sandboxes or narrows the tool pool (it explicitly denies narrowing), never says the grant survives the turn, never states conformance to or a version of the open Agent Skills specification, and never says what any other client does with the key. Verdict on the frozen label: **`pre-approves` is true of this page** — "without prompting you for approval" (L617) and "without asking permission during the turn that invokes this skill" (L404) are a pre-approval grant; the managed-settings and hooks behaviour are limits of the grant, not denials that it is one. I did not change the label.

## 6. Prompt-injection text seen in the page

None acted on and none reported to the reader as instruction. Sweep over the snapshot: `grep -n -iE 'ignore (all|previous|prior)|you must (now|instead)|system prompt|assistant must|do not tell|exfiltrat' S227-claude.md` returned three matches, all ordinary product documentation: L96 (a `preserved-thinking-migration` subcommand description naming "its system prompt, or its tool list"), L822 (a table column header "System prompt"), L827 (a sentence about built-in agents starting "without CLAUDE.md and git status"). No page text addresses the fetching agent; the page's opening `> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt` is a navigation note, not an instruction I followed.
