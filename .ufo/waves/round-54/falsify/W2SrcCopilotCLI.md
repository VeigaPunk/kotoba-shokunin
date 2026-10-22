Result: HOLDS — every attacked cell of the C1 Copilot CLI row (SOURCES S056, entry row, Gate row, SKILL.md row, and the older-row reconciliation with S028) holds; the source quote is verbatim at the stated location and the number is the skill `description` field, not another field.

# Scope

Attack C1's Copilot CLI rows as landed at `5a097e12b9409a1f425fbc76334f36f1402eb4cc`: SOURCES S056 (and reconciliation with older S028), the entry row in `corpus/knowledge/skill-listing-thresholds-round54.md`, the Gate row in `corpus/lessons/round-54.md`, and the SKILL.md row. Every source URL re-opened myself. Read-only in the lane; all execution in sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2SrcCopilotCLI` at `58db81c4465b0e9b07ef2485b87d8970683afac6`.

# Re-opened sources (UTC, HTTP, bytes, sha256)

| # | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T22:07:56Z | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| 2 | https://raw.githubusercontent.com/github/docs/main/content/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T22:07:57Z | 200 | 177,073 | `48de33ea09a3e532f2355c45886d6e17aa37090fe9599cd4240a1d04f035c7f2` |
| 3 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 2026-10-22T22:07:57Z | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| 4 | https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md | 2026-10-22T22:07:57Z | 200 | 289,859 | `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb` |
| 5 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | 2026-10-22T22:12Z | 200 | 10,057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |

Commands (exit codes 0 everywhere):

```
$ cd /fast/scratch/hyaku/kotoba-r54/W2SrcCopilotCLI/fetch
$ curl -sS -o cmdref.md -w 'cmdref.md HTTP %{http_code} %{size_download}B\n' 'https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md'
# HTTP 200 461944B
$ curl -sS -o cmdref-src.md -w '...' 'https://raw.githubusercontent.com/github/docs/main/content/copilot/reference/copilot-cli-reference/cli-command-reference.md'
# HTTP 200 177073B
$ curl -sS -o pluginref.md -w '...' 'https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md'
# HTTP 200 47200B
$ curl -sS -o changelog.md -w '...' 'https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md'
# HTTP 200 289859B
$ sha256sum cmdref.md cmdref-src.md pluginref.md changelog.md
# c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9  cmdref.md
# 48de33ea09a3e532f2355c45886d6e17aa37090fe9599cd4240a1d04f035c7f2  cmdref-src.md
# d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0  pluginref.md
# c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb  changelog.md
```

All hashes match the recorded hashes (SOURCES S056 cell 5, seat report SrcCopilotCLI.md §3, Gate row S056). The `.md` route return 200 and identical bytes, so the fetched page is the one the quote cites.

# Findings

## 1. SOURCES S056 row — HOLDS

`corpus/SOURCES.md:69` (11 cells, tier A, kind docs, status mined, opened `2026-10-22`, used-by names the entry). URL is on pinned host `docs.github.com` (counter `HOSTS["Copilot CLI"]`, `verifiers/check_description_thresholds.py:94`). Anchor cell cites `cli-command-reference.md:1274`; fresh fetch line 1274 is:

```
| `description`              | string              | Yes      | What the skill does and when to use it. Max 1024 characters. |
```

The number is the skill frontmatter `description` field row in `### Skill frontmatter fields` (header at `cmdref.md:1269`), not a name, plugin, or MCP field. Same sentence at the docs source `cmdref-src.md:1285` (recorded; corroborates wording). Teaches cell ("A skill description is required in frontmatter and its documented maximum is 1024 characters") is exactly what the quote supports.

## 2. Entry row (Per-client record) — HOLDS

`corpus/knowledge/skill-listing-thresholds-round54.md:42`:

```
| Copilot CLI | S056 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | Authoring maximum: the frontmatter table caps a skill description at 1024 characters, and the page states no behaviour past the cap. |
```

Quote is 12 words, verbatim (spot-checked byte-for-byte against `cmdref.md:1274`, including capitalization and punctuation), carries the `1024` token as a whole token. Reading cell says "authoring maximum" — correct: the row describes the accepted frontmatter value; it does not claim a render cut. It says "the page states no behaviour past the cap" — verified: `grep -niE 'truncat|cut|limit|budget|drop|omit'` over `### Skill frontmatter fields` onward and over the whole `cmdref.md` finds no skill-description consequence (only `copilot skill list --json` shape at `:1330`, no truncation note). The reading states no more than the quote plus the seat sweep.

## 3. Gate row — HOLDS

`corpus/lessons/round-54.md:26`:

```
| S056 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T21:18:03Z | 461,944 B, sha256 c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | SrcCopilotCLI |
```

URL, UTC window, byte count, sha256 and quote all match the fresh fetch. The Gate row says exactly what the counter requires (counter `judge` reads `gate_quotes_by_id`).

## 4. SKILL.md row — HOLDS

`SKILL.md:188`:

```
| Copilot CLI | `description` max 1024 characters | Not documented; the page states the cap and no truncation, shortening or refusal | keep the description at 1024 characters or fewer, front-loaded on what the skill does and when to use it |
```

Threshold cell has number token `1024`; action non-empty; past-the-threshold cell is scoped to the page ("the page states …"), which matches the seat evidence: no truncation/shortening/refusal sentence exists on the command-reference page. It does not claim a client-wide absence (see residual risk below).

## 5. Reconciliation with older S028 — HOLDS (no contradiction)

`corpus/SOURCES.md:41` (S028, plugin reference page) teaches: "…the page's 1,024-character cap sits under legacy plugin-manifest fields (`:195`); the page states no cap for the SKILL.md `description`". Re-verified on the fresh `pluginref.md` fetch:

- `:195` is in `### Legacy manifest fields` → `#### Optional metadata fields` — the plugin-manifest `description` cap, not a skill field.
- `:349` is the Agent Plugins 1.0 manifest `description` cap (same family, still plugin metadata).
- `grep -niE 'skill' pluginref.md | grep -iE 'max|cap|1024|char|limit|length'` → 0 hits; exit 1. The plugin page never ties a cap to a skill `description`.

S028 and S056 are different pages (`cli-plugin-reference` vs `cli-command-reference`), so a 1024 cap on the command-reference `description` row is not "contradicted" by S028's statement about the plugin page. The Rejected row in the round-54 lesson (`round-54.md:42`) confirms the plugin caps were deliberately excluded exactly because they are not skill `description` caps.

## 6. No older row/entry contradicts the 1024 number

`grep -rn '1024\|1,024' corpus/knowledge/ | grep -i copilot` (excluding the round-54 entry) → no Copilot-CLI-specific older number. `frontmatter-rule-authorities-round48.md:44` and `render-mechanism-round7.md:24` carry the 1024 as the spec/validator cap, not as a Copilot CLI statement. Also `mcp-server-instructions-round52.md:32` and `skill-overlap-levers-round51.md:21` quote Copilot CLI on other topics (instructions flag, `disable-model-invocation`) — no conflict with a description cap.

## 7. Counter re-run at tip — confirms

In the sandbox clone at `58db81c`:

```
$ python3 -B verifiers/check_description_thresholds.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6
# Claude Code  BACKED
# Codex        BACKED
# VS Code      BACKED
# Copilot CLI  BACKED
# Gemini CLI   BACKED
# Cursor       BACKED
# opencode     BACKED
# description thresholds backed 7 of 7 clients
$ echo $? → 0
$ python3 -B verifiers/check_description_thresholds.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6 --fetch
# Copilot CLI  BACKED found=True
# description thresholds found on the live page 7 of 7
# exit 0
```

This is the frozen counter (`e3371548`), unchanged at tip; `--fetch` is the secondary live-present measurement, and it confirms the quote is on the live page.

# Residual risk / verification gaps

1. **Uncited changelog sentence (observation, not a break).** `changelog.md:1993` (version 1.0.32, `## 1.0.32 - 2026-04-17` at `:1972`): "Skills that exceed the token limit are still discoverable and invocable by name". This is a client-documented consequence involving a (unnumbered) token limit; the record's "Not documented" cells are scoped to the command-reference page, and the counter requires a number token, so the claim C1 is unaffected. The seat report itself flagged this line (`SrcCopilotCLI.md:97`). The record could add a sentence in the entry's Limits noting this changelog sentence and why it is not a per-`description` numeric cap, so a reader does not infer client-wide silence. Not a breaker: the findings cell "Two clients cut or budget the listing" is about documented numbers; this changelog line has no number and describes discoverability-by-name, not necessarily a description cut. [INFERENCE] that "discoverable and invocable by name" means the full listing entry is not shown; the sentence alone does not state that the description is dropped.
2. The served `.md` vs the docs source differ in line numbers (1274 vs 1285) — already recorded; only the served page is the pin, the source is corroboration.
3. No client binary was run (bounds: no model calls; only `--version`/`--help` are allowed), so "no behaviour past the cap" is a documentation-absence statement, not an empirical check. The seat's binary probe was inconclusive and is correctly not relied upon.

# Conclusion

All attacked cells HOLD; no corrected text is needed. The only actionable note is the optional Limits-sentence addition in the entry (residual risk 1). Overall verdict: HOLDS.
