Result: DONE — fetched and pinned VS Code’s current targeted-instructions page and supplied the exact S105 source, entry, Gate, and SKILL text; the C1 counter was not run.

## Fetch and provenance

URL opened: `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md`. The request used the frozen counter’s `curl_argv` settings (`verifiers/check_scoped_rules.py:1169-1176`): `-sSL`, 30-second cap, exact Chrome/130 User-Agent and Accept header. The response was saved verbatim as `.ufo/waves/round-60/snapshots/S105.page`.

Command: `timeout 60s sh -c 'date -u; curl -sSL --max-time 30 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -H "Accept: text/markdown, text/plain;q=0.9, */*;q=0.8" -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page -w "\n%{http_code} %{url_effective}\n" https://code.visualstudio.com/docs/agent-customization/custom-instructions.md; rc=$?; printf "curl exit: %s\n" "$rc"; wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page; exit "$rc"'` — exit 0. Observed stdout:

```text
Fri Oct 23 12:08:55 PM UTC 2026

200 https://code.visualstudio.com/docs/agent-customization/custom-instructions.md
curl exit: 0
23715 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page
```

The page title is `Use custom instructions in VS Code` (`S105.page:3`). W0 recorded that the `.md` form of the old route returned 404, while the unsuffixed old route redirected to the moved docs page (`.ufo/waves/round-60/w0/CensusVSCode.md:7-15`). This matters for the teaches wording: the current source is a different, non-base URL; the 404 observation specifically applies to the old `.md` form, not the unsuffixed URL that W0 observed redirecting.

## Quote selection and exact snapshot lines

Chosen unshaped quote, a contiguous sentence span from snapshot line 32; no bytes inside the quote were stripped or rewritten:

`Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.`

Command: `sed -n '32p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page` — exit 0; output:

```text
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.
```

Word-count command: `printf '%s\n' 'Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.' | wc -w` — exit 0; output `10`.

Token context: `sed -n '27p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page` — exit 0; output:

```text
| Copilot | [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) or [`AGENTS.md`](#use-an-agentsmd-file) | [`.github/instructions/**/*.instructions.md`](#use-instructionsmd-files) |
```

Scope-key proof: `sed -n '164,167p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page` — exit 0; output:

```text
applyTo: '**/*.py'
---
# Python testing

```

Action proof: `sed -n '329p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S105.page` — exit 0; output:

```text
* For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.
```

## Exact candidate text for integration

SOURCES row S105:

```text
| S105 | Visual Studio Code — Use custom instructions in VS Code — https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | docs | A | VS Code targeted instruction-file location and frontmatter path key for matching-file scope | § Types of instruction files, Choose a format (`custom-instructions.md:17,25-32`); `applyTo` field (`:150-158`) and example (`:160-164`); task- or language-specific instructions (`:329`); fetched 2026-10-23T12:08:55Z (HTTP 200, 23,715 B, sha256 `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f`); exact bytes `.ufo/waves/round-60/snapshots/S105.page` | VS Code documents targeted files at `.github/instructions/**/*.instructions.md`, matched by `applyTo`; this is the moved successor of base row S047's `docs/copilot/customization/custom-instructions` route (the `.md` form is 404; the unsuffixed URL redirected to the successor) | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

Entry row:

```text
| VS Code | `.github/instructions/**/*.instructions.md` | S105 | Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. |
```

Gate line:

```text
- **S105 VS Code** — https://code.visualstudio.com/docs/agent-customization/custom-instructions.md — accessed 2026-10-23T12:08:55Z (HTTP 200, 23,715 B, sha256 `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f`; snapshot `.ufo/waves/round-60/snapshots/S105.page`) — `custom-instructions.md:32`: "Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`."
```

SKILL row:

```text
| VS Code | `.github/instructions/**/*.instructions.md` (Local-harness targeted instructions, S105 :32) | `applyTo` (`**/*.py`, S105 :164) | Use multiple instruction files per topic and apply them selectively (S105 :329) |
```

## Manual check against the frozen counter (not run)

- **Fetch/source gates:** The frozen client host list admits `code.visualstudio.com` for VS Code (`verifiers/check_scoped_rules.py:262-270`). The fetched URL is the moved `.md` page, not S047’s old URL; the previous census records the old route behavior above. The source-row gates require `docs`, tier `A`, `mined`, an opened date in `OPENED`, a full SHA-256, a same-hash snapshot and an own-host URL (`:1034-1081`). The candidate row supplies those values and its full digest equals the observed snapshot digest. Redirect/live-page checks require HTTP 200, pinned final host and no disallowed base URL (`:1200-1225`); observed final URL is the requested moved page on the pinned host.
- **Quote:** The quote contains the exact token case-sensitively, bounded by spaces, and `instructions` outside the token; `rule_word_outside` requires a whole rule/instruction word outside the token span (`:679-723`). The quote-length check is 6–25 words and the Gate must record it (`:1018-1031`); the count command/output above is the quote’s `wc -w` evidence. The Gate candidate records the same literal quote. Quote normalization and snapshot quote matching are at `:935-961`.
- **Scope key (A1):** The first backticked key in the candidate Scope key cell is `applyTo`; its own citation is `S105 :164`. On that cited snapshot line it appears in key form followed by `:` and the value `'**/*.py'`. After stripping the quote, the first value token is `**/*.py`, which contains `*` and fits the counter's pattern-token alphabet (`first_value_token` / `pattern_value`: `:814-830`; strict `key_site`: `:853-869`). The pasted `sed -n '164,167p'` output proves the value and the following context.
- **Action (A1):** For `Use multiple instruction files per topic and apply them selectively (S105 :329)`, the distinct content-word set after removing the citation and pinned stopwords is `{multiple, instruction, files, topic, apply, selectively}`. The cited line's shared set is `{multiple, files, topic, apply, selectively}`. The counter defines content words and requires at least three distinct words plus `max(2, ceil(|W|/2))` shared words on the own-source cited line (`:881-912`); these listed sets meet that gate. The pasted `sed -n '329p'` output is the cited line.
- **Row glue:** The entry candidate repeats the SKILL token exactly; its source is one `S###` id, the quote is between 6 and 25 `split()` words after backtick removal, and the quote must be in Gate (`:1011-1032`). The semantic cells each cite their own S105 source line and are checked against this snapshot (`:1083-1096`).

No C1 counter, `--fetch`, build, or test was run. No tool was installed or updated. Only the assigned snapshot and this report were written in the lane; SOURCES, the knowledge entry, lesson, and SKILL integration remain for the L1. Report path: `.ufo/waves/round-60/build/SrcVSCode.md`.