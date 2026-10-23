Result: DONE — Copilot CLI: ELIGIBLE https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md token `.github/instructions/**/*.instructions.md` key `applyTo` line 66

Re-census seat RecensusCopilotCLI. One client. No lane files edited. No tools installed (pacman paused; `gh` was already logged in and was used only to list `github/docs` paths). Counter helpers imported read-only from `verifiers/check_scoped_rules.py`. Fetched bytes under `/fast/scratch/hyaku/kotoba-r60/RecensusCopilotCLI/`.

The census page `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` is base key `//docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions` (S048). `free-pro-team@latest` of that article redirects onto that base key. The enterprise-cloud rendering does not redirect, and its url_key is not in the base list.

## Eligible page

URL requested and final URL (no redirect; response headers are a single `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, `content-length: 8826`, `date: Fri, 23 Oct 2026 10:59:38 GMT`): `https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`

```
$ date -u
Fri 23 Oct 2026 10:59:38 AM UTC
$ curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' -o body-entcloud 'https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md'
200 https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
$ wc -c body-entcloud
8826 body-entcloud
$ sha256sum body-entcloud
70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e  body-entcloud
```

User-Agent is the counter's `CURL_UA` (`check_scoped_rules.py:300-301`). Bytes saved at `/fast/scratch/hyaku/kotoba-r60/RecensusCopilotCLI/body-entcloud`. Header dump: `hdr-entcloud.txt`.

```
$ python3 -B -c "import sys; sys.path.insert(0,'verifiers'); import check_scoped_rules as c; print(c.url_key('https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md'))"
//docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
$ grep -cxF '//docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions' .ufo/waves/round-60/w0b-base-url-keys.txt
0
```

`grep` exit 1 (count 0, no match). `grep -c enterprise` on that file is also 0. Same key for the final URL. `host_ok` True on `HOSTS["Copilot CLI"]` (`docs.github.com`). `url_is_change_note` False. `url_is_tracker` False.

Line that ties the page to Copilot CLI: line 1, `# Adding custom instructions for GitHub Copilot CLI`. Line 32 is the path-specific sentence: `Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.`

## Token

`.github/instructions/**/*.instructions.md` as printed on line 18. `token_well_formed` is True. `foreign_marker('Copilot CLI', token)` is None.

```
$ sed -n '18p' body-entcloud
| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |
```

## Quote

Whole line 18, backticks kept, nothing removed. 16 words after the counter's count (`quote.replace('`','').split()`).

```
$ sed -n '18p' body-entcloud | wc -w
16
```

`wc -w` is 16. The counter strips backticks and still gets 16.

`token_span` on the backtick-stripped line is `(2, 43)`, text `.github/instructions/**/*.instructions.md`. `rule_word_outside` is True (`instructions` in `repository instructions,` sits outside that span). `quote_why(page, line 18)` is `[]`. `live_why(page, line 18, 'applyTo')` is `[]`.

## Scope key

K = `applyTo`. L = 66. `key_site(lines, 66, 'applyTo')` is True. `key_site` at 60 and 11 is False (the word is backticked, not `applyTo:` / `applyTo=`). Later sites, also True: line 74 `applyTo: "**/*.ts,**/*.tsx"` (first token `**/*.ts`, cut at the comma) and line 94 `applyTo: "**"`.

~~~~
$ sed -n '66,69p' body-entcloud
   applyTo: "app/models/**/*.rb"
   ---
   ```

~~~~

Call (exit 0), `lines` = `body-entcloud` splitlines:

```
c.key_site(lines, 66, 'applyTo') → True
c.value_after(...) → ' "app/models/**/*.rb"'
c.first_value_token(...) → 'app/models/**/*.rb'
```

Line 66 has `applyTo` at an identifier boundary, then `:`. The value is the rest of the line (not a block). The first token contains `*` and is only `[A-Za-z0-9_./*{},!-]`.

## Action line

Line 60 is the author step (put an `applyTo` glob in the frontmatter so the instructions apply only to the named files).

```
$ sed -n '60p' body-entcloud
4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.
```

Call (exit 0):

```
cell = 'Create a frontmatter block with the applyTo keyword and use glob syntax so the instructions apply only to matching files (S901 :60)'
c.content_words(cell) → apply, applyto, block, create, files, frontmatter, glob, instructions, keyword, matching, syntax
c.action_conjunct(lines, cell, 60) → []
c.action_conjunct(lines, cell, 59) → shares 0 of its 11 content word(s) with line 59 (need >= 6)
```

`|W|` = 11, need `max(2, ceil(11/2))` = 6. Shared with line 60 = 9 (`applyto` is in the cell but not on the line, because line 60's `applyTo` is inside backticks and `content_words` drops backticked spans). `matching` is also only in the cell.

## Other pages checked

Each row: `date -u` as noted, `CURL_UA`, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`. `grep -cxF` of `c.url_key(final URL)` against `w0b-base-url-keys.txt` is the count column (exit 1 when the count is 0). `any_key_site(text, 'applyTo')` is the counter call.

| page (final URL) | when (UTC) | status | bytes | sha256 | base | why not the row |
|---|---|---|---|---|---|---|
| `.../add-custom-instructions.md` (the S048 page) | via `free-pro-team@latest` redirect, 10:59:39 | 200, final is the unversioned URL | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | 1 | final url_key is the base key. Same sha256 as the W0 census fetch |
| `.../reference/custom-instructions-support.md` | 10:55:39 | 200, no redirect | 14612 | `90150f5a25f493640b9a52da6ac0a363ece8ece13429bd2c6c4e5ebb0c44e814` | 0 | token on line 253 under `## Copilot CLI` (line 249). `any_key_site(applyTo)` False |
| `.../use-copilot-cli/overview.md` | 10:58:25 | 200, no redirect | 20619 | `3d7922046390c5277e88a09c1f392f79e01f452bdf579193378472d466a9f7aa` | 0 | CLI page. Token on line 160. `any_key_site(applyTo)` False |
| `.../concepts/prompting-and-context/custom-instructions.md` | 10:57:19 | 200, no redirect | 14669 | `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933` | 0 | Token on line 90 is under "Copilot Chat on GitHub.com", not the CLI sentences (lines 30 and 84). `any_key_site(applyTo)` False |
| `.../add-repository-instructions.md` | 10:55:41 | 200, no redirect | 22858 | `c29d67f0a342f2ae8de6bda04b8c7e7ce9a1341d61eaffdeee9a4fc8c9ced635` | 0 | `key_site` line 160 `applyTo: "app/models/**/*.rb"` True. No `CLI` on the page. Exact token absent |
| `.../tutorials/cloud-agent/get-the-best-results.md` | 10:58:24 | 200, no redirect | 14201 | `b530f411eeac316ff04e27585d4f42bd19f0cae1a91f9305016b8887dc216cd6` | 0 | Token lines 83 and 133. `key_site` line 140 `applyTo: "**/tests/*.spec.ts"` True. No `CLI` |
| `.../add-repository-instructions-in-your-ide.md` | 10:58:24 | 200, no redirect | 46556 | `9d76ff1414cca75440157d253ccdfd83848daacd77f27ec9bec6cc482adfb59b` | 0 | `applyTo:` key sites. No `CLI`. Exact token absent |
| `.../cli-command-reference.md` | 10:58:53 | 200, no redirect | 462608 | `52dfb285981b394fc6b7b636ad84403b5cce878a3c34df51d094e2cb4ebe94bc` | 1 | Base key. Token lines 948 and 955. `any_key_site(applyTo)` False. The example key is `paths:` line 959 (`key_site` True), with `applyTo` only in parentheses |
| `.../your-first-custom-instructions.md` | 10:55:41 | 200, no redirect | 5015 | `3b3b66325a13ae1a8d1ff7eb70d6ad0dfef1accf10feb5bedf66857b1892737f` | 0 | `applyTo` is a prose field name (line 23). `any_key_site` False. Line 23 names Copilot Chat in VS Code, Visual Studio, and cloud agent, not CLI |
| `.../customize-copilot/overview.md` | 10:57:20 | 200, no redirect | 4304 | `38f2e097044641c32451491df4bbe4b7e232969fe50558aa3bb4fda2ac79189b` | 0 | CLI page. Links to the base how-to. No token, `any_key_site(applyTo)` False |
| `.../cli-config-dir-reference.md` | 10:57:19 | 200, no redirect | 166811 | `ed83183ad8a276246b263236cc88ba60568ec2188a6524865da132de2835938f` | 0 | Personal `~/.copilot/instructions/` applied to every session. No token, `any_key_site(applyTo)` False |
| `https://raw.githubusercontent.com/github/copilot-cli/main/README.md` | 10:55:41 | 200, no redirect | 7740 | `33657f2e7383f2167b47d5f8c549a6071905a5c93d5d67d17e5c5399f126f07b` | 0 | CLI README. No token, no `applyTo`. Repo root is LICENSE, README, changelog, install.sh, `.github` only |
| `https://docs.github.com/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot.md` | 10:55:39 | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` | 0 | dead URL |
| `.../enterprise-server@latest/.../add-custom-instructions.md` | 10:59:38 | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` | — | dead URL |

`github/docs` code search (`gh api search/code`, 10:58:07Z, total_count 20) finds `applyTo` in Copilot CLI content only in the base how-to and the base command reference, plus the reusable `data/reusables/copilot/custom-instructions-path.md` which those two and the non-CLI repository/IDE how-tos include. That search is the index's count, not a proof the index is complete.

No experimental / preview / deprecated mark was scored on the enterprise page; those words were not required once the key site, quote, and CLI title were on the fetched bytes.
