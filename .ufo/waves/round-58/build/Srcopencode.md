Result: DONE — Drafted S095, the opencode entry, SKILL row, and Gate evidence; the pinned-source quote passes the frozen page predicate.

## Findings

- **Command-file behavior documented:** At the pinned OpenCode V2 docs source, `commands.mdx:21` gives global `~/.config/opencode/commands/` and project `.opencode/commands/` locations. Line 28 says only `.md` files are discovered and nested paths become command names separated by `/`; lines 37 and 68 say the Markdown body is the prompt template and optional frontmatter shares fields with JSON; line 99 documents `$ARGUMENTS` as the complete entered argument string. This is documentation evidence, not a runtime test.
- **Legacy wording:** The plural `.opencode/commands/` form is not marked legacy. `commands.mdx:34-35` says legacy singular `command/` directories are still discovered, but recommends `commands/` for new files. Separately, `commands.mdx:77` calls `subtask` a deprecated alias for `subagent`; that is a field, not the command-folder form.
- **Quote selected:** Exact, unshaped source line 21 (10 words): `Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.` It contains the `.opencode/commands/` token and `commands` outside the token. No source bytes were stripped from this quote.
- **Live-page result and pinned-source result differ:** A plain GET of the served page returned HTML (no `Accept` header). The counter's `found_on_page` returned `False` for that URL and quote; its page normalization leaves a space before the final period after stripping inline HTML tags. The same `fetch` and `found_on_page` functions returned `True` for the pinned raw Markdown source URL below, so S095 uses that pinned URL. This establishes only the requested page predicate, not a full C1 counter pass.

## Commands and observed evidence

Sandbox setup, exit 0, no output:
```sh
mkdir -p /fast/scratch/hyaku/kotoba-r58 && unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/Srcopencode && git -C /fast/scratch/hyaku/kotoba-r58/Srcopencode checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

Plain served-page fetch, exit 0:
```sh
timeout 30s sh -c 'date -u; curl -sSL -D /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-headers.txt -o /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-page.bin -w "HTTP_STATUS=%{http_code}\nSIZE_DOWNLOAD=%{size_download}\nFINAL_URL=%{url_effective}\n" https://opencode.ai/v2/docs/commands/; sha256sum /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-page.bin; wc -c /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-page.bin'
```
Observed output:
```text
Fri Oct 23 08:08:16 AM UTC 2026
HTTP_STATUS=200
SIZE_DOWNLOAD=32304
FINAL_URL=https://opencode.ai/v2/docs/commands/
32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0  /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-page.bin
32304 /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands-page.bin
```

Pinned raw source fetch, exit 0:
```sh
timeout 30s sh -c 'date -u; curl -sSL -D /fast/scratch/hyaku/kotoba-r58/Srcopencode/source-headers.txt -o /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx -w "HTTP_STATUS=%{http_code}\nSIZE_DOWNLOAD=%{size_download}\nFINAL_URL=%{url_effective}\n" https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx; sha256sum /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx; wc -c /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx'
```
Observed output:
```text
Fri Oct 23 08:08:26 AM UTC 2026
HTTP_STATUS=200
SIZE_DOWNLOAD=7242
FINAL_URL=https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx
dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11  /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx
7242 /fast/scratch/hyaku/kotoba-r58/Srcopencode/commands.mdx
```

Pinned URL counter test, run from the sandbox clone at the named freeze revision, exit 0; output `True`:
```sh
timeout 40s python3 -B -c 'from verifiers.check_command_files import fetch, found_on_page; url="https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx"; quote="Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`."; page=fetch(url); print(found_on_page(page, quote, ".opencode/commands/"))'
```

Plain served URL counter test with the same quote, exit 0; output `False`:
```sh
timeout 40s python3 -B -c 'from verifiers.check_command_files import fetch, found_on_page; url="https://opencode.ai/v2/docs/commands/"; quote="Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`."; page=fetch(url); print(found_on_page(page, quote, ".opencode/commands/"))'
```
The diagnostic `norm_page` result showed `...project commands in .opencode/commands/ . ~/.config...` and `contains False`; the pinned Markdown source does not have this HTML tag-induced space.

## Drafts (verbatim)

SOURCES row:
```md
| S095 | anomalyco/opencode — V2 commands documentation source, pinned at `4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3` — https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx | docs | A | OpenCode V2's documented Markdown command locations, file-to-command naming, prompt templates, frontmatter, and argument placeholders | § Markdown (`commands.mdx:21,28,34-37`); § Fields (`:68-77`); § Arguments (`:99-105`); fetched 2026-10-23T08:08:26Z, HTTP 200, 7,242 B, sha256 `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` (seat Srcopencode) | OpenCode V2 documents project `.opencode/commands/` and user `~/.config/opencode/commands/` Markdown files, slash names from nested paths, body templates, and optional YAML metadata | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md
```

Knowledge entry row:
```md
| opencode | .opencode/commands/ | S095 | "Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`." |
```

SKILL.md row:
```md
| opencode | `.opencode/commands/` (project; user: `~/.config/opencode/commands/`) | Markdown `.md` body is the prompt template; nested paths map to slash command names; optional YAML frontmatter sets metadata; `$ARGUMENTS` receives the complete entered string. Evidence: “Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.” (`commands.mdx:21`); “Only `.md` files are discovered. Nested paths become command names with `/` separators:” (`:28`); “Add YAML frontmatter when the command needs metadata. The trimmed Markdown body is always the prompt template.” (`:37`); “Use `$ARGUMENTS` for the complete argument string exactly as entered.” (`:99`). | Write and document reusable opencode prompt commands. |
```

Gate line:
```md
- opencode — https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx; fetched 2026-10-23T08:08:26Z; located quote: “Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.” (`commands.mdx:21`).
```

## Gates, surfaces, limits

- **Requested predicate:** `fetch(url)` plus `found_on_page(page, quote, token)` is `True` on the exact pinned raw URL and quote. The quote has 10 words, and the captured MDX line is verbatim. The served HTML check is `False`; use S095's pinned raw URL, not the live URL, for this quote.
- **Not claimed:** No full `python3 -B verifiers/check_command_files.py --rev ... --fetch` run; no complete C1 finding, corpus integration, or other gate result is claimed. No other clients, R3/defect items, or C2 work were tested here.
- **Touched surfaces:** Only this report was written in the lane. Fetch captures and the frozen-revision clone are under `/fast/scratch/hyaku/kotoba-r58/Srcopencode/`; no lane product files were edited. No tooling was installed or updated.
- **Integration note:** Frozen context says SKILL.md is at its 600-line budget. This is a draft only; pair any eventual SKILL addition with the assigned equal verbatim move (ExecBudgetMove).
- **Artifact:** `.ufo/waves/round-58/build/Srcopencode.md`.
