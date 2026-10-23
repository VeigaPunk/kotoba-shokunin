# ScribeS113 — VS Code `applyTo` source

## Finding and scope

I checked whether the moved VS Code agent-customization page has a first-party, not-yet-registered canonical source suitable for S113. The published article's canonical route is `https://code.visualstudio.com/docs/agent-customization/custom-instructions` (no `.md`): its HTML carries that `og:url` and says articles are also available as Markdown by appending `.md`. The no-suffix route returns HTML; its highlighted YAML example wraps `applyTo` and its colon in separate `<span>` elements, so it does not give the frozen key-site check a plain `applyTo: <path-pattern>` line. The `.md` route was already opened as S105 at the round-61 base and S105 already records `applyTo`, so it is not a valid A3 re-open for this key.

I found the current article source at Microsoft's `microsoft/vscode-docs` repository, `docs/agent-customization/custom-instructions.md`. The GitHub contents API reported the file at that path, and the latest file-touch commit was `5f82fce32d763abe6d39d674691f1d2f1b7d5ef9` (2026-10-22T20:00:41Z). Its commit-pinned `raw.githubusercontent.com` URL is on the verifier's VS Code host allowlist and was not found in the base `corpus/SOURCES.md` URL search. It preserves the Markdown key form and is the proposed new S113 source URL; this is a first-party documentation source, not a VS Code runtime observation.

## Fetch and quote evidence

The frozen `verifiers/check_scoped_rules.py:1169-1176` fetch uses `curl -sSL --max-time 30`, the Chrome 130 User-Agent, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`, and `-w '\n%{http_code} %{url_effective}'`. I used those request options and added only `-o` to save the response body to permitted scratch. All fetch commands below continued through the `&&` chain, so the shell exit code was 0.

Published canonical page, no `.md` (exploratory URL check; not the proposed S113 snapshot):

```sh
date -u && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body -w '\n%{http_code} %{url_effective}' 'https://code.visualstudio.com/docs/agent-customization/custom-instructions' && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body && wc -l /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body
```

Pasted stdout:

```text
Fri 23 Oct 2026 07:10:18 PM UTC
200 https://code.visualstudio.com/docs/agent-customization/custom-instructions162303 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body
dfffae3cc91c051776bb656fcc8a8afd16d8de94062ddc4d9782760dfd8df2eb  /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body
  2589 162303 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-canonical.body
```

The curl write-out trailer has no final newline, so it runs directly into the next command's `wc -c` output. The page body is HTML. Read-only inspection of that saved body found `og:url` at line 24 and the article's Markdown-route note at line 90.

The proposed source URL was fetched twice, first at `main` and then pinned to the latest file-touch commit. Both returned the same byte count and SHA; the pinned URL below is the deliverable.

```sh
date -u && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md -w '\n%{http_code} %{url_effective}' 'https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md' && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && wc -l /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

Pasted stdout:

```text
Fri 23 Oct 2026 07:13:53 PM UTC
200 https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md25556 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9  /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
 380 25556 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

The pinned source fetch is HTTP 200, 25,556 bytes, 380 lines, SHA-256 `b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9`, at `2026-10-23T19:13:53Z`. This hash also matched the preceding `main` fetch. The shell exit code was 0.

Quote/key extraction from the pinned raw snapshot:

```sh
sed -n '45p' /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && printf '%s\n' 'Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.' | wc -w && sed -n '177p' /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

Pasted stdout (exit 0):

```text
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.
10
applyTo: '**/*.py'
```

The quoted substring is contiguous and unchanged from the raw source line: 10 words under `wc -w`, within the 6–25-word bound. The `applyTo` example is a key-form occurrence with a path glob on the same line. The quoted words are documentation data; no page text was treated as instructions.

## Drafts for L1

Exact 11-cell SOURCES row draft (no pipe characters in any cell):

```text
Target: corpus/SOURCES.md
| S113 | Visual Studio Code docs source — Use custom instructions in VS Code — https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md | docs | A | First-party VS Code custom-instructions documentation source for the targeted workspace instruction path and the frontmatter key for matching-file scope; not a runtime test | § Choose a format (`custom-instructions.md:40`); Local-harness instructions note (`:45`); `applyTo` field (`:169`) and YAML example (`:177`) | VS Code's own docs source lists `.github/instructions/**/*.instructions.md` as a targeted instructions path and shows `applyTo` as the matching-file glob key; this is documentation, not observed editor behavior | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, verifiers/check_scoped_rules.py |
```

Gate line draft:

```text
Target: corpus/lessons/round-61.md § Gate
- **S113 VS Code** — https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md — accessed 2026-10-23T19:13:53Z (HTTP 200, 25,556 B, sha256 `b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9`; snapshot `.ufo/waves/round-61/snapshots/S113.page`) — `custom-instructions.md:45`: "Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`."
```

A1 key-set fact for the v3 counter (candidate mapping line; cite the demonstrated key site):

```text
Target: verifiers/check_scoped_rules.py — A1 canonical scope-key set
"VS Code": {"applyTo"},  # S113 :177
```

Snapshot for L1 to land:

```text
Target: .ufo/waves/round-61/snapshots/S113.page
Bytes: 25556
SHA-256: b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9
```

The exact body currently resides at `/fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md` as a transfer locator only; scratch is untrusted and is not evidence. This seat did not write the lane snapshot.

## Gates, touched surfaces, and limits

- **Behavior established:** first-party documentation describes `.github/instructions/**/*.instructions.md` and demonstrates `applyTo` with a glob. No VS Code runtime behavior was exercised.
- **C1 counter gates:** `check_scoped_rules.py --self-test` and any base/tip `--fetch` measurement were not run by this seat. No C1 predicate result or integration pass is claimed. L1 still must land the source row, Gate line, and snapshot bytes before any measured revision can use them.
- **Read-only checks:** round-61 plan and v3 A1 spec; r60 S047/S105 rows and scoped-rule evidence; round-61 dispatch/spec; checker fetch implementation; official docs page, GitHub docs-source file, and its API metadata; base SOURCES URL search. No `git` or `jj` mutation, no dispatch, and no edits to sibling files.
- **Touched surfaces:** this report is the only lane file this seat writes. The two downloaded VS Code pages are scratch-only and are not lane/fleet changes.
- **Out of scope:** counter implementation, fixtures, self-test, base/tip measurement, integration, commit/push, runtime testing, and tool installation.
- **Artifact paths:** report `.ufo/waves/round-61/wave/ScribeS113.md`; proposed snapshot `.ufo/waves/round-61/snapshots/S113.page`; transfer-only fetched bytes `/fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md`.

Installs: no installs.
Blockers: none.
Produced/attacked: Produced the pinned first-party VS Code `applyTo` source draft, quote, Gate line, snapshot hash, and A1 key-set evidence; the C1 counter gate remains unrun by this seat.
