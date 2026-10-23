Result: PARTIAL — Copilot CLI evidence and integration text are ready, but this read-only seat cannot write the required snapshot into the lane.

## Findings

- Client: Copilot CLI, eligible as the v2 re-open of S048. The census report records the canonical URL and path token (`.ufo/waves/round-60/w0/CensusCopilotCLI.md:1,7-10,18`); the current SOURCES row S048 has that same URL (`corpus/SOURCES.md:61`). The frozen counter requires a `re-opens S### —` teaches prefix, a base row whose URL matches, and a key absent from that base row (`verifiers/check_scoped_rules.py:972-994`). The row below starts with the required prefix. S048’s visible current row does not contain `applyTo`; this seat did not independently extract the S048 row from the base Git object.
- Fetch: `date -u` printed `Fri 23 Oct 2026 12:08:47 PM UTC`. The counter-equivalent curl argv, with shell redirection to retain stdout, was `curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' > /fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.curl-output` (curl exit 0). This uses the exact `curl_argv` values (`verifiers/check_scoped_rules.py:321-324,1169-1176`); `run_curl` extracts the body at the last newline before the status trailer (`:1185-1197`). Observed HTTP 200, effective URL unchanged, 8,730 body bytes, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`.
- Body-extraction command (exit 0): `python3 -c 'from pathlib import Path; import hashlib; p=Path("/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.curl-output"); raw=p.read_bytes(); body, sep, tail=raw.rpartition(b"\n"); status, _, url=tail.decode("utf-8", errors="replace").partition(" "); assert sep and status.isdigit() and url; Path("/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page").write_bytes(body); print(f"curl_exit=0\nhttp_status={status}\neffective_url={url}\nbytes={len(body)}\nsha256={hashlib.sha256(body).hexdigest()}")'`. Output: `curl_exit=0`, `http_status=200`, `effective_url=https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md`, `bytes=8730`, `sha256=00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`.
- Exact fetched body saved at `/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page`; combined raw curl stdout/trailer is `/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.curl-output`. The requested lane snapshot `.ufo/waves/round-60/snapshots/S106.page` was not written, because the lane is read-only to this seat and only the report may be written. The scratch body is the exact byte sequence to install at that path during integration.
- The fetched line 18 is the table row naming the token and the surrounding words `Modular repository instructions`; `instructions` occurs outside the backticked token. The selected quote is a contiguous 10-word slice, from the opening token backtick through `locations`, with no source bytes omitted. The single table `|` in that slice is represented as `&#124;` only where embedded in the Markdown entry row / Gate line, so the row parser does not split a fourth column; the frozen quote normalizer HTML-unescapes it (`verifiers/check_scoped_rules.py:935-960`).

### Snapshot excerpts and counts

Commands below read the fetched scratch snapshot. Combined command exit code: 0.

```text
$ sed -n '18p' /fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page
| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |
$ printf '%s\n' '`.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations' | wc -w
10
```

The count command’s output is 10 (`wc -w`); the quote is 6–25 words and contains the exact token plus `instructions` outside that token. The chosen quote is the slice printed in the command, not the whole source row.

```text
$ sed -n '66,69p' /fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page
   applyTo: "app/models/**/*.rb"
   ---
   ```

$ sed -n '60p' /fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page
4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.
```

The Action cell’s distinct content-word set, after excluding backticks/citation and the counter STOPWORDS, is `create, path, specific, instruction, file, glob, syntax, specify, files, directories, instructions, apply`.

```text
$ printf '%s\n' create path specific instruction file glob syntax specify files directories instructions apply | wc -w
12
$ printf '%s\n' create file glob syntax specify files directories instructions apply | wc -w
9
```

The action threshold is `max(2, ceil(12/2)) = 6`; the cited line 60 shares the listed 9 words (`create`, `file`, `glob`, `syntax`, `specify`, `files`, `directories`, `instructions`, `apply`). The threshold and comparison rules are frozen at `verifiers/check_scoped_rules.py:881-912`.

## Integration text

Candidate SOURCES row (11 columns, matching the lane registry convention; `teaches` starts with the required re-open prefix):

```markdown
| S106 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Copilot CLI repository-scoped modular instruction files and their path selector (vendor documentation; not a runtime test) | § Types of custom instructions table (`add-custom-instructions.md:13-22`); § Creating path-specific custom instructions (`:52-60`); frontmatter example (`:64-68`); fetched 2026-10-23T12:08:47Z (HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`); exact bytes staged at `/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page`, intended lane snapshot `.ufo/waves/round-60/snapshots/S106.page` | re-opens S048 — Copilot CLI's repository modular instruction files use `.github/instructions/**/*.instructions.md`; `applyTo` selects matching file paths, and authors can add glob-based frontmatter | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md, SKILL.md |
```

Candidate knowledge entry row:

```markdown
| Copilot CLI | `.github/instructions/**/*.instructions.md` | S106 | `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations |
```

Candidate Gate line (the quote is the same 10-word line-18 slice; `&#124;` restores the source table separator under the counter normalizer):

```markdown
- S106 — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md; opened 2026-10-23T12:08:47Z; HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; quote at `add-custom-instructions.md:18`: `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations
```

Candidate SKILL table header and Copilot CLI row:

```markdown
### Scoped rule files by client

| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Copilot CLI | `.github/instructions/**/*.instructions.md` (modular repository instruction files, S106 :18) | `applyTo` (e.g. `app/models/**/*.rb`, S106 :66) | Create a path-specific instruction file with an `applyTo` glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60). |
```

## Manual frozen-counter checks (not a counter run)

- Token: `.github/instructions/**/*.instructions.md` satisfies `TOKEN_RE`; it has four segments, a dot-led first segment, no forbidden skill/agent/command/prompt/plugin/extension/hook segment, and no foreign client marker (`verifiers/check_scoped_rules.py:292-319,634-662`). The client is in the frozen client list and `docs.github.com` is a Copilot CLI host pin (`:260-288`).
- Entry quote: `entry_row_verdict` requires the backticked skill token to match the entry Rule files cell, 6–25 whitespace words, token presence, and a rule/instruction word outside the token (`verifiers/check_scoped_rules.py:997-1030`). The proposed entry uses the exact token; the quoted slice is present on fetched line 18 and `instructions` is outside it. The Gate line contains that same entity-encoded quote, and the frozen Gate check searches the normalized quote within `## Gate` (`:739-754`).
- Source/re-open: `entry_row_verdict` checks `docs`, tier A, `mined`, opened date 2026-10-23, URL, host, changelog path, and full row SHA (`verifiers/check_scoped_rules.py:1041-1083`). The candidate row supplies those values and the full hash. `reopen_why` accepts the required `re-opens S048 —` prefix only when the named base row has the same normalized URL and the key is absent from that base row (`:972-994`); S048 is the row identified by the supplied census and its current registry URL is identical (`corpus/SOURCES.md:61`, `.ufo/waves/round-60/w0/CensusCopilotCLI.md:7-10`).
- Snapshot/Semantics: the proposed Scope key’s first backticked item is `applyTo`; its own citation is `S106 :66`. Line 66 has `applyTo:` followed on the same line by the first value token `app/models/**/*.rb`, containing `*`, so it meets the key-form and path-pattern check (`verifiers/check_scoped_rules.py:759-771,814-869`). The Action cell cites its own source line 60; its `W` has 12 distinct content words, 9 are shared with the line, and the required threshold is 6 (`:881-912`). The snapshot SHA reported by this fetch is the full hash printed in the candidate SOURCES row; the counter will compare it to the committed snapshot bytes when L1 integrates them (`:1068-1096,2525-2528`).

## Gates, touched surfaces, and limits

- C1 counter was **not run**, as required while control receipts are being scored. All findings above are manual checks against the frozen counter source and the fetched bytes, not counter execution evidence. No build, tests, or other runtime checks were run. No tools were installed or updated.
- Lane surface written by this seat: this report only. The source row, knowledge row, Gate line, and SKILL row are proposed integration text, not edits to their product files. The exact snapshot bytes exist in the scratch artifact path above; the requested lane snapshot path remains unwritten under the read-only boundary, so this item is PARTIAL until L1 integrates it.
- Out of scope: no edits to `corpus/SOURCES.md`, `corpus/knowledge/scoped-rules-round60.md`, `corpus/lessons/round-60.md`, `SKILL.md`, or the counter; no enterprise-cloud `@latest` alias, no paid client CLI call, and no counter run.

## Artifact paths

- Report: `.ufo/waves/round-60/build/SrcCopilotCLI.md`
- Exact fetched body: `/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.page` (8,730 B, sha256 above)
- Curl stdout including status trailer: `/fast/scratch/hyaku/kotoba-r60/SrcCopilotCLI/S106.curl-output`
- Required but not written by this read-only seat: `.ufo/waves/round-60/snapshots/S106.page`
