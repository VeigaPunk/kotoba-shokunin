# ScribeS114 — Copilot CLI scope-key source

## Result and scope

Produced the S114 source evidence and draft `SOURCES.md` row, round-61 Gate line, snapshot destination, and A1 key-set member for Copilot CLI. The source directly documents `.github/instructions/**/*.instructions.md` and the `applyTo` frontmatter key. This is vendor documentation, not a CLI runtime test; it supports the key-set input, not the C1 counter predicate or a measured row verdict.

The canonical public page is the same URL as S048, but the new row's scope is the path-specific key and matching semantics that S048 did not teach. I re-opened the canonical non-enterprise page as the assignment permits, and the row begins exactly `re-opens S048 — canonical scope-key set`. I checked the linked official `Support for different types of custom instructions` page (`https://docs.github.com/en/copilot/reference/custom-instructions-support`): it lists the Copilot CLI path-specific file location, but does not name `applyTo`. A scoped official-docs search returned the CLI guide and a general code-review tutorial; I found no separate official Copilot CLI source for the key itself. I did not use the `enterprise-cloud@latest` rendering.

## Fetch provenance

Read the v2 counter's fetch implementation (`verifiers/check_scoped_rules.py:1169-1228`). The request used its URL, `-sSL`, 30-second cap, Chrome/130 User-Agent, Accept header, and write-out fields. The first capture used the same request headers and URL but added a final newline to the write-out for terminal readability; the counter-compatible capture below was made immediately afterward with the counter's exact write-out string. Both returned identical body size and SHA-256. The latter is the cited capture.

First capture command (scratch initialization and first response capture):
```sh
set -eu; mkdir -p /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114; date -u; curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page -w '\n%{http_code} %{url_effective}\n' 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md'; sha256sum /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page; wc -c /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```
Output:
```text
Fri 23 Oct 2026 07:09:39 PM UTC

200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
8730 /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```
Exit: 0 (the `set -eu` command completed successfully).

Counter-compatible capture command:
```sh
set -eu; date -u; curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' -o /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md'; printf '\n'; sha256sum /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page; wc -c /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```
Output:
```text
Fri 23 Oct 2026 07:11:44 PM UTC

200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
8730 /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```
Exit: 0 (the `set -eu` command completed successfully). Effective URL remained the requested canonical public URL; HTTP 200. SHA-256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; body 8,730 bytes.

The quote below is the unshaped first sentence of fetched page line 32, with its original backticks and punctuation. Its word-count command and output were:
```sh
date -u; printf '%s\n' 'Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.' | wc -w
```
```text
Fri 23 Oct 2026 07:11:14 PM UTC
18
```
Exit: 0.

## Drafts for the L1 integrator

Proposed `corpus/SOURCES.md` row (S114):
```text
| S114 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Copilot CLI's documented modular repository instruction pattern and the applyTo frontmatter key for matching-file instructions (vendor documentation, not a runtime test) | § Types of custom instructions (`add-custom-instructions.md:18`); § Creating path-specific custom instructions (`:52-60,66`); § How multiple instruction files interact (`:32`); re-opened 2026-10-23T19:11:44Z (HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`) | re-opens S048 — canonical scope-key set: Copilot CLI documents `.github/instructions/**/*.instructions.md` as modular repository instructions and `applyTo` as the frontmatter key for path-specific instructions that match files | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md |
```

Proposed `corpus/lessons/round-61.md` Gate line:
```text
- **S114 Copilot CLI (re-opens S048)** — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md — accessed 2026-10-23T19:11:44Z (HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; snapshot `.ufo/waves/round-61/snapshots/S114.page`) — `add-custom-instructions.md:32`: "Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with."
```

Proposed snapshot destination (not written by this seat): `.ufo/waves/round-61/snapshots/S114.page`; expected fetched bytes SHA-256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`, 8,730 bytes. The downloaded scratch copy is `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page`; scratch is untrusted and is not cited as committed evidence.

Proposed A1 key-set member:
```text
Copilot CLI -> `applyTo` (source S114:66: `applyTo: "app/models/**/*.rb"`).
```
The page's line 66 is a key-form site with a path-like glob value; line 32 states the path-match behavior. The cited quote is exactly 18 whitespace-separated words, within the 6–25 bound, and avoids the literal-pipe table quote that the r60 `ExecKeyForms.md` documented as truncating in the counter's table parser.

## Gates, touched surfaces, and limits

- **A1 evidence:** S114 directly supports Copilot CLI's `applyTo` key. The other client keys, the counter implementation, and A1's full per-client set remain for integration; this row alone does not establish them.
- **Not run:** `check_scoped_rules.py --self-test`, any frozen-world fixture, `--rev ... --fetch`, the C2 checker, C3 checks, and no-harm/integration gates. No C1/C2/C3 pass or result is claimed.
- **Touched:** only this report in the lane; one raw fetched page in the explicitly permitted scratch directory. No lane product file, fleet/sibling file, `.ufo/state`, git/jj index, or revision was written or mutated. No git/jj commands, installs, dispatches, or asks were made.
- **Known limit:** documentation page text establishes what GitHub documents, not what a particular installed Copilot CLI binary does at runtime. The page was byte-identical to the recorded S048/S106 fetch; this round's fresh successful HTTP fetch, date, URL, and hash are recorded above.

Installs: no installs.
Blockers: none.
Produced: Copilot CLI S114 primary-source evidence, its `applyTo` A1 key-set member, and proposed SOURCES/Gate text.
