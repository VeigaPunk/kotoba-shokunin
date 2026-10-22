# C2CodexOpencodeDocs — per-client SKILL.md frontmatter authority (Codex, opencode)

Seat `KotobaR48.C2CodexOpencodeDocs`, 2026-10-22. C2 source slice: the two clients' skill docs
plus the shipped implementations they describe. Read-only on the lane; the only write is this
report. No tool installed or upgraded (no pacman transaction attempted).

## Findings (observed)

1. **Codex docs say almost nothing about frontmatter validity.** The page's whole normative
   sentence is md:48 (name and description must be included). Absence sweep over the live
   markdown (232 lines): `regex` 0, `1-64` 0, `64` 0, `lowercase` 0, `hyphen` 0, `1024` 0,
   `XML`/`xml` 0, `angle` 0, `third person` 0, `500 lines` 0, `must match` 0,
   `directory name` 0 hits. The description rules the page does state are router-side only
   (md:37-44): 2% context budget / 8,000 characters, descriptions shortened first,
   `skills.max_context_tokens` up to 10,000 tokens.
2. **Codex implementation imposes rules its docs omit, and in different form** (tag
   `rust-v0.163.0` = installed `codex-cli 0.163.0`): `parser.rs:4` `MAX_NAME_LEN = 64` used at
   `:82`; `name` is **optional** — absent/empty falls back to the parent directory name
   (`parser.rs:71-79`, `host.rs:396 default_skill_name`); `description` must be non-empty
   (`:83-85`, `MissingField("description")`); **no name charset rule anywhere** (grep
   `regex|is_ascii_lowercase|a-z0-9` over `parser.rs`, `model.rs`, `required.rs`,
   `loader/{mod,namespace,host,metadata,discovery}.rs` → 0 hits); no description length check
   at parse time.
3. **Codex truncation is numeric and named**: `render.rs:23-24`
   `MAX_CATALOG_SKILL_DESCRIPTION_CHARS = 1_024` + `TRUNCATED_SKILL_DESCRIPTION_SUFFIX = "..."`
   applied by `truncate_catalog_skill_description` (`:1091-1109`); `render.rs:19-22`
   `8_000`-char default budget, `10_000`-token configured max, `SKILL_METADATA_CONTEXT_WINDOW_PERCENT = 2`.
   So Codex cuts descriptions at exactly 1,024 chars — the same number opencode's docs impose
   as a validity cap, but as a display truncation, not a load gate.
4. **Codex invalid frontmatter**: parse failure → `SkillError` recorded and the skill skipped
   for non-`System` scopes (`host.rs:333-336`); `System`-scope failures are dropped with no
   record (`:336`). Two leniencies: a line-oriented YAML repair retry for prose values with
   colons (`parser.rs:53-54`), and optional metadata failing open (`loader/metadata.rs:83`).
5. **opencode docs impose the open-spec rules verbatim**: name 1–64, lowercase alphanumeric
   with single hyphen separators, no leading/trailing `-`, no `--`, must match the directory
   name, regex `^[a-z0-9]+(-[a-z0-9]+)*$` (md:54-66); description 1-1024 (md:72); "Each
   `SKILL.md` must start with YAML frontmatter" (md:31).
6. **opencode 1.19.3 (npm `latest`, = installed) enforces none of them.** The loader's only
   frontmatter check is `typeof name === "string"` (`index.ts:53-58`); a file failing it is
   skipped with **no log and no event** (`:123`). A parse failure gets a `Session.Event.Error`
   plus `logError "failed to load skill"` and a skip (`:112-116`). Duplicate names log a
   warning and the last one wins (`:125-140`). No name regex, no 1-64, no 1-1024 anywhere in
   the v1.19.3 tree (regex 0 hits; `1024` 0 hits in skill code; `Info` schema is unconstrained
   `Schema.String`, `:37-42`). `InvalidError`/`NameMismatchError` are declared (`:61-70`) but
   **never constructed in `src`** — the only constructions are
   `test/skill/skill.test.ts:326,333`, a class-shape test.
7. **opencode docs are ahead of the shipped client.** Two live-page deltas vs the docs source
   shipped inside v1.19.3 (`packages/web/src/content/docs/skills.mdx`, sha256 `7ff4df3a…`):
   live says "Use these Agent Skills fields:" where v1.19.3 said "Only these fields are
   recognized:" plus "Unknown frontmatter fields are ignored."; live adds metadata keys
   `opencode/slash` and `opencode/autoinvoke` (md:44-48) that have 0 occurrences in the
   v1.19.3 TS tree and 0 in the installed 1.19.3 binary.
8. **S013 freshness**: the markdown body is byte-identical to the round-47 access
   (sha256 `ed6e324f…`, 232 lines) while the served HTML hash changed
   (`78abf995…` → `d738d309…`) and `Last-Modified` moved `2026-10-21T15:05:00Z` →
   `2026-10-22T04:05:41Z`: deploy/HTML churn, not content change. The round-47 report's byte
   count for that markdown (3,970 B) contradicts the live 11,035 B at the same sha256.
9. **"What happens on invalid frontmatter" is documented only by opencode**, and only as a
   symptom list (md:225-228), never as a rule. Codex's page is silent on malformed frontmatter
   entirely; its docs also do not say name is optional or that the directory name is the
   fallback.

## Quotes (≤25 words, located)

| quote | source, location |
|---|---|
| "The `SKILL.md` file must include `name` and `description`." | Codex docs, md:48 |
| "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" | Codex docs, md:37-39 |
| "If many skills are installed, Codex shortens skill descriptions first." | Codex docs, md:40-41 |
| "If two skills share the same `name`, Codex doesn't merge them; both can appear in skill selectors." | Codex docs, md:138 |
| "Some third-party skills use prose like `description: Build for AWS: ECS`" | codex-rs/skills/src/parser.rs:53 |
| "Fail open: optional metadata should not block loading SKILL.md." | codex-rs/ext/skills/src/loader/metadata.rs:83 |
| `MAX_CATALOG_SKILL_DESCRIPTION_CHARS: usize = 1_024` / `TRUNCATED_SKILL_DESCRIPTION_SUFFIX: &str = "..."` | codex-rs/ext/skills/src/render.rs:23-24 |
| "Each `SKILL.md` must start with YAML frontmatter." | opencode docs, md:31 |
| "Be 1–64 characters" / "Match the directory name that contains `SKILL.md`" | opencode docs, md:56, md:60 |
| "`description` must be 1-1024 characters." | opencode docs, md:72 |
| "If a skill does not show up:" … "Check that frontmatter includes `name` and `description`" | opencode docs, md:225, md:228 |
| `if (!isSkillFrontmatter(md.data)) return` | packages/opencode/src/skill/index.ts:123 |

## Evidence

| item | value |
|---|---|
| Codex page URL | `https://developers.openai.com/codex/skills` → `308` → `https://learn.chatgpt.com/docs/build-skills` (`location` header; second hop `200`) |
| Codex page accessed (UTC) | `2026-10-22T08:11:03Z` (response `date`); markdown re-fetch byte-identical (`cmp` exit 0) |
| Codex page stamps | HTML `Last-Modified: Thu, 22 Oct 2026 04:05:41 GMT`, `ETag: "05515a538c5ed12b2b141913bbefb301"`; markdown 232 lines / 11,035 B, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`; HTML 417,112 B sha256 `d738d30986a5f6ccd52e6b8d4fae5c5a6cb1060a76719b2050197fad35fc009c`; no body-level revision date found |
| opencode page URL | `https://opencode.ai/docs/skills` (+ `.md`) `200`; accessed `2026-10-22T08:11:04Z` (`date`), HTML again `08:14:39Z` |
| opencode page stamps | markdown 5,365 B sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`; **no `Last-Modified` and no `ETag`** on either representation; no version/date string in the body |
| Codex implementation identity | installed `codex --version` → `codex-cli 0.163.0` (exit 0); cited tag `rust-v0.163.0`, GitHub `releases/latest` `published_at 2026-10-15T21:30:38Z` |
| opencode implementation identity | installed `opencode --version` → `1.19.3` (exit 0); npm `opencode-ai` `latest` = `1.19.3`, `time['1.19.3'] = 2026-10-16T12:32:00.280Z`; tag `v1.19.3` = `e3c4eb242585dcd77be1a867391b7c25fd47ce52` (`git ls-remote --tags`, no 2.x on npm) |
| source files read (raw, tag-pinned) | `codex-rs/skills/src/{parser,model,loading}.rs`, `codex-rs/ext/skills/src/{render,catalog}.rs`, `.../loader/{host,metadata,discovery,namespace,mod}.rs`, `.../required.rs`; opencode `packages/opencode/src/skill/index.ts` + full v1.19.3 tarball (`codeload` 74,724,841 B, 136 MB extracted) |
| decisive greps (exit codes) | `grep -rn 'NameMismatchError' oc-src --include=*.ts` → 4 hits (declaration + 3 test lines), exit 0; `grep -rn -E '\^\[a-z0-9\]\+\(-' … --include=*.ts` → 0 hits, exit 1; `grep -rn '1024' … | grep -i skill` → 0 hits, exit 1; `grep -rn 'autoinvoke' packages --include=*.ts` → 0 hits, exit 1; installed binary `grep -c -a -F 'opencode/slash'` → `0` |
| absence sweep (Codex md) | every token in finding 1 → `grep -c` = 0, exit 1 |
| no tool installs | none; `pacman` untouched (transactions paused host-wide) |

## Remaining unknowns

- Which opencode version the live docs page targets: the page is unversioned and the server
  sends no `Last-Modified`/`ETag`, so "docs ahead of 1.19.3" is proven only for the delta
  against the in-repo v1.19.3 `skills.mdx` (sha256 `7ff4df3a…`), not dated.
- Whether a non-`packages/**/*.ts` path (server, plugin host, or a future V2 skill module)
  enforces the name regex in 1.19.3. Both skill modules present in the tree are lenient; the
  `NameMismatchError` constructor has no `src` caller.
- `MAX_SKILL_NAME_BYTES = 256` (`render.rs:28`) appears once in that file and is unused in the
  other files read; no full-crate sweep was run, so its enforcement status is unknown.
- No live client run: every implementation statement above is source or binary evidence, not
  observed routing. Codex was not launched; opencode was not launched.
