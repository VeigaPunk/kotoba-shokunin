Result: DONE — Re-opened the Codex hooks page, confirmed S097’s teaches clause omits the documented one-invocation trust bypass, and drafted S111 plus its Gate entry for L1 integration.

## Findings

- `corpus/SOURCES.md:109` currently says: “non-managed hook definitions must be reviewed and trusted before they run” without the exception. The re-opened page says at `hooks.md:64-67` that Codex requires review and trust for non-managed hooks, then at `:76-78` documents the exception for one-off automation that vets hook sources outside Codex. The qualification in the draft below is limited to that stated exception; it does not claim hooks are safe or trusted generally.
- The page bytes contain no `by default` wording in the reviewed trust passage. The re-opened source states the normal review requirement and separately states the invocation-specific bypass; the draft avoids presenting “by default” as a direct quote.

## Provenance and gates

- URL: https://learn.chatgpt.com/docs/hooks.md
- Access time: `date -u` output `Fri 23 Oct 2026 12:08:18 PM UTC` (2026-10-23T12:08:18Z).
- Command (successful; all `&&`-chained steps completed): `mkdir -p /fast/scratch/hyaku/kotoba-r60/ScribeR4S097 && date -u && timeout 90s curl --location --silent --show-error --output /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md --write-out 'HTTP %{http_code}\n' https://learn.chatgpt.com/docs/hooks.md && wc -c /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md && sha256sum /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md && sed -n '19p;76,78p' /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md` — exit 0.
- Observed output: `HTTP 200`; `47133 /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md`; SHA-256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`, exactly equal to S097’s full recorded hash (`corpus/SOURCES.md:109`).
- Fetched-byte excerpt with line numbers, from `nl -ba /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md | sed -n '19p;62,80p'`:
  ```text
      19  - Non-managed hooks must be reviewed and trusted before they run.
      62  ## Review and trust hooks
      63
      64  Codex lists configured hooks before deciding which ones can run. Before a
      65  non-managed hook can run, Codex requires you to review and trust the exact hook
      66  definition. Codex records trust against the hook's current hash, so new or
      67  changed hooks are marked for review and skipped until trusted.
      68
      69  Use `/hooks` in the CLI to inspect hook sources, review new or changed hooks,
      70  trust hooks, or disable individual non-managed hooks. If hooks need review at
      71  startup, Codex prints a warning that tells you to open `/hooks`.
      72
      73  Managed hooks from system, MDM, cloud, or `requirements.toml` sources are marked
      74  as managed, trusted by policy, and can't be disabled from the user hook browser.
      75
      76  For one-off automation that already vets hook sources outside Codex, pass
      77  `--dangerously-bypass-hook-trust` to run enabled hooks without requiring
      78  persisted hook trust for that invocation.
      79
      80  ## Config shape
  ```
- Quote-length check: `sed -n '76,78p' /fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md | wc -w` — output `24` (under the 25-word limit). The Gate quote below preserves source line breaks and inline-code backticks.
- Quote bytes from `hooks.md:76-78`:
  > For one-off automation that already vets hook sources outside Codex, pass
  > `--dangerously-bypass-hook-trust` to run enabled hooks without requiring
  > persisted hook trust for that invocation.

## Draft for L1 integration

Proposed append-only `corpus/SOURCES.md` row S111, following the existing row schema:

```markdown
| S111 | OpenAI Learn — Hooks (S097 teaches correction) — https://learn.chatgpt.com/docs/hooks.md | docs | A | Codex hook trust review requirement and the documented one-invocation bypass for one-off automation (vendor documentation, not a runtime test) | § Review and trust hooks (`hooks.md:64-67,76-78`); re-opened 2026-10-23T12:08:18Z, HTTP 200, 47,133 B, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` (same SHA-256 as S097's recorded row) | supersedes S097 — Codex requires review and trust before non-managed hooks run; one-off automation that already vets hook sources outside Codex can pass `--dangerously-bypass-hook-trust` to run enabled hooks without persisted hook trust for that invocation | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Proposed `corpus/lessons/round-60.md` `## Gate` entry (quote is the fetched passage above, line breaks preserved):

```markdown
- **S111 Codex (S097 teaches correction)** — https://learn.chatgpt.com/docs/hooks.md — accessed 2026-10-23T12:08:18Z (HTTP 200, 47,133 B, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`; same SHA-256 as S097's recorded row; seat `ScribeR4S097`) — `hooks.md:76-78`:
  > For one-off automation that already vets hook sources outside Codex, pass
  > `--dangerously-bypass-hook-trust` to run enabled hooks without requiring
  > persisted hook trust for that invocation.
```

## Scope and artifacts

- Touched lane surface: this report only, `.ufo/waves/round-60/build/ScribeR4S097.md`. The fetched page is in this seat’s scratch directory at `/fast/scratch/hyaku/kotoba-r60/ScribeR4S097/hooks.md`.
- No lane source, lesson, snapshot, product code, or counter was edited or run. This seat did not create `.ufo/waves/round-60/snapshots/S111.page`; L1 must commit that snapshot with the row and lesson entry. `corpus/lessons/round-60.md` was not present when checked, so the Gate text above is a draft, not a claimed integration.
- Out of scope: C1 counter/semantic checks and all other source rows.
- Artifact: `.ufo/waves/round-60/build/ScribeR4S097.md`.
