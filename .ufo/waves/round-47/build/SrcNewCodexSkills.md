verdict: ADMIT S012 — OpenAI "Build skills" (canonical https://learn.chatgpt.com/docs/build-skills, 308 from the assigned developers.openai.com/codex/skills URL) is an opened, tier-A, docs-kind primary source that states the 2%-of-context / 8,000-character initial-list budget, description-first shortening, and description-gated implicit invocation; status queued, zero census findings.

# SrcNewCodexSkills — candidate SOURCES.md row (round 47, frontier SOURCES step)

Seat `MoriR22R.SrcNewCodexSkills-9`. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`
(`git rev-parse HEAD`, exit 0). Production files were read only; the only writes are this
report and `SrcNewCodexSkills.json` beside it. No code edit, no patch — the deliverable is a
registry row plus its gate record.

## 1. What the source is (observed, not inferred)

- The assigned URL is **not a page**: `https://developers.openai.com/codex/skills` answers
  `308` with `location: https://learn.chatgpt.com/docs/build-skills`, under both `Accept: */*`
  and `Accept: text/html`; the `.md` suffix and the trailing-slash variant redirect the same
  way. The Codex doc tree appears relocated — two sibling probes land on the new host:
  `https://developers.openai.com/codex` → `…/docs`, and `…/codex/evals` → `…/docs/evals`
  (the URL of the adjacent lead at `corpus/SOURCES.md:74`). [INFERENCE] from two probes, not
  an exhaustive redirect census.
- The canonical page is self-declared in the HTML
  (`<link rel="canonical" href="https://learn.chatgpt.com/docs/build-skills">`) and is served
  by Vercel with `last-modified: Wed, 21 Oct 2026 15:05:00 GMT`, `etag:
  W/"ffc66e554470ca914642d4df868b6dc7"`, HTTP `200`.
- The page advertises a markdown representation; `…/build-skills.md` returns 232 lines /
  3,970 bytes, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`,
  and is byte-identical when re-fetched (same hash at 15:55Z) and when fetched through the
  `developers.openai.com` host (same hash). HTML decoded bytes 417,112, sha256
  `78abf99589567f6d56bbd6eebcaf251f5de38eab23c4d26d68e40d598d919e81`.
- The load-bearing content is in two anchored sections:
  `<a id="how-codex-uses-skills"></a>` / `## How ChatGPT and Codex use skills` (md:89/91) and
  `<a id="where-to-save-skills"></a>` / `## Where Codex loads local skills` (md:134/136),
  plus `## Optional metadata` (md:193) and `allow_implicit_invocation` (md:218).
- Revision caveat: the page carries **no body-level revision date** and no JSON-LD
  `datePublished`/`dateModified` (0 hits). `Last-Modified` is a CDN deploy timestamp that
  happens to equal the access day, so the sha256 is the durable identity and the anchor cell
  records both.

## 2. Draft row (validated, ready to append after S011)

```
| S012 | OpenAI — Build skills (ChatGPT and Codex) — https://learn.chatgpt.com/docs/build-skills (308 redirect from https://developers.openai.com/codex/skills) | docs | A | Codex client skill routing: initial-list budget, description shortening, implicit invocation | § How ChatGPT and Codex use skills (anchor #how-codex-uses-skills) ¶2–4, § Optional metadata policy.allow_implicit_invocation, § Where Codex loads local skills; page Last-Modified 2026-10-21T15:05:00Z, ETag W/"ffc66e554470ca914642d4df868b6dc7", accessed 2026-10-21 | Codex caps its initial skill list at 2% of context (8,000 characters when unknown), shortens descriptions first, and gates implicit invocation on the description | queued | 2026-10-21 | 90d | — |
```

Census proof (real validator, temp copy of `corpus/SOURCES.md` with this row inserted after
S011, `SKILL.md` copied beside it so `used-by` resolves):

```
bash scripts/sources-census.sh validate --file /tmp/sources-test/corpus/SOURCES.md --today 2026-10-21
  -> "file\tok\t/tmp/sources-test/corpus/SOURCES.md"   exit 0
bash scripts/sources-census.sh census --file /tmp/sources-test/corpus/SOURCES.md --today 2026-10-21
  -> rows 12 · tier.A 11 · tier.C 1 · status.queued 7 · status.mined 4 · status.rejected 1   exit 0
```

Base had 11 rows / tier.A 10 / queued 6, so the row adds exactly one A-tier queued entry and
introduces no E01–E12 or W-code finding. **ID caveat:** `S012` is "next unused" at BASE only;
if a sibling seat also lands a row this round, the integrator must re-key one of them (contract:
ids are never reused, rule 2). The row body is id-independent.

## 3. Gate record (SOURCES contract v1 rule 1)

| field | value |
|---|---|
| id | S012 |
| URL | `https://developers.openai.com/codex/skills` → `308` → `https://learn.chatgpt.com/docs/build-skills` (final `200`) |
| accessed (UTC) | `2026-10-21T15:54:43Z` (response `date` header), window closed `2026-10-21T15:56:05Z` (`date -u`) |
| sha256 | HTML `78abf99589567f6d56bbd6eebcaf251f5de38eab23c4d26d68e40d598d919e81` (417,112 B decoded); markdown `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` (3,970 B) |
| quote (20 words) | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" |
| location | § How ChatGPT and Codex use skills, md lines 37–39 (visible-render check: `grep -c "at most 2% of the model"` on the HTML → 1) |
| second quote (20 words) | "Front-load the key use case and trigger words so a host can still match the skill if descriptions are shortened." — same section, md lines 102–103 |
| kind / tier | `docs` / `A`, scoped to **Codex client skill routing**; not A for the open standard, which the page itself defers to (`https://agentskills.io`, md:7) |
| `teaches` | Codex caps its initial skill list at 2% of context (8,000 characters when unknown), shortens descriptions first, and gates implicit invocation on the description |
| status / recheck | `queued` / `90d` (vendor doc, no version number to key `on-release` to) |

## 4. Relevance to the round-47 claims

- **C2 operability (`plans/round-47.md:28`, `corpus/QUALITY.md:19` Q08).** The lane's
  description XML-tag rule is sourced on S003, an Anthropic doc (`corpus/SOURCES.md:16`).
  The other major client's skill documentation is **silent**: `XML`, `xml tag`, `angle`,
  `angle bracket`, `third person`, `1024`, `1,024`, `500 lines` → **0 hits in both the
  markdown and the HTML**. This is a counterexample to any "all clients forbid XML tags in
  `description`" framing and supports keeping C2's check attributed and scoped to S003
  (Anthropic) rather than presented as a cross-client contract. Silence is not permission —
  the row does **not** claim Codex accepts tags.
- **Router budget in another client.** Codex's initial list carries name + description +
  **file path**, capped at 2% of the context window or **8,000 characters** when unknown,
  with descriptions shortened first and whole skills dropped (with a warning) for huge sets;
  the knob is `skills.max_context_tokens`, max 10,000 **tokens** (md:37–44). Two calibration
  hazards for the lane: (a) the default is stated in **characters** while the override is in
  **tokens** — a re-derivation that reads "8000" as tokens is wrong; (b) Codex's shortening is
  a *host-side* per-description truncation, structurally the same class as omp's 99-char cliff
  the lane already models, so `knowledge/harness-router-models-round9.md` can gain a third
  client row without a new model.
- **Router control surface.** `policy.allow_implicit_invocation` (default `true`, md:218) is a
  per-skill gate that neither omp nor opencode exposes; it is the Codex analogue of the
  "offer gate" the lane measures, and is a second axis (policy) beside budget (size).
- **Loader roots.** Documented: `$CWD/.agents/skills` walk-up to repo root,
  `$HOME/.agents/skills`, `/etc/codex/skills`, plus bundled SYSTEM skills (md:140–147), with
  symlinked skill folders followed (md:149). Distinct from omp's discovery roots; note that
  `~/.codex/skills` is **not** in that table, although the lane's surfaces baseline already
  lists it as an omp-observed root (`verifiers/surfaces-baseline.json:226`).

## 5. Counterexamples / things the source does not say

1. **The assigned URL is a redirect, not a document.** A row that cites
   `developers.openai.com/codex/skills` as its anchor would point at a 308; the row cites the
   redirect and the canonical, and the sha256 is of the canonical bytes.
2. **No description-length or content constraint** is stated by Codex: no 1,024-char bound,
   no XML-tag ban, no third-person rule, no 500-line body bound. Those remain S001/S003
   facts, not a universal client contract.
3. **Docs vs the client's own bundled prompt.** Codex 0.163.0's binary embeds skill-creator
   text: "create discoverable skills in `$CODEX_HOME/skills`, or `~/.codex/skills` when
   `CODEX_HOME` is unset" and "Installs into `$CODEX_HOME/skills/<skill-name>` (defaults to
   `~/.codex/skills`)" — a location the page's loader table omits. So the documented loader
   list is **not exhaustive**, and the lane should not treat it as an absence proof for
   `~/.codex/skills`. [INFERENCE] the path is still loaded; the observed fact is only that the
   client's own prompt calls it "discoverable".
4. **Duplicate names are not merged** — "If two skills share the same `name`, Codex doesn't
   merge them; both can appear in skill selectors" (md:138). That is the opposite of the
   dedupe-by-name behavior the lane recorded for opencode; a same-name uniqueness rule cannot
   be justified by client dedupe on Codex.
5. **Budget not witnessed in the binary.** `strings -n 4` on the 0.163.0 ELF (284 MB,
   3,213,285 lines, sha256 `399ff69c…`) contains `max_context_tokens` (18), 
   `allow_implicit_invocation` (8), `.agents/skills` (3), `.codex/skills` (2, both from the
   bundled skill-creator text above), but no `2%`/`8000`-character constant. The budget claim
   rests on the documentation alone; it is **not** independently witnessed.
6. **The same host serves two corroborating pages** (not drafted as rows, contract rule 4):
   `customization/overview.md` (sha256 `e4f466bb…`, § Skills table global `~/.agents/skills`
   / repo `.agents/skills`; "It starts with metadata (`name`, `description`) for discovery";
   "Clear skill descriptions improve triggering reliability.") and `skills-and-plugins.md`
   (sha256 `39aa2756…`), which only restates the name+description point.

## 6. Commands run (all in `/tmp` or read-only; exit codes as reported)

| command | exit | key output |
|---|---|---|
| `git -C …/kotoba-shokunin rev-parse HEAD` | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `curl -sS -D h -o codex-skills.html -L --compressed https://developers.openai.com/codex/skills` | 0 | `http=200`, final URL `https://learn.chatgpt.com/docs/build-skills`, 308 hop recorded in `h` |
| `sha256sum codex-skills.html` | 0 | `78abf995…9e81`, 417,112 B decoded |
| `curl … https://learn.chatgpt.com/docs/build-skills.md` | 0 | `http=200`, 3,970 B, `ed6e324f…9d5` |
| re-fetch of the `.md` (15:55Z) + fetch via `developers.openai.com/codex/skills.md` | 0 | identical sha256 `ed6e324f…9d5` both times |
| `grep -c "at most 2% of the model" codex-skills.html` | 0 | `1` |
| absence sweep, md + html (`XML`, `xml tag`, `angle`, `angle bracket`, `third person`, `1024`, `1,024`, `500 lines`) | 0/1 | every count `0` (grep exit 1 = no match) |
| `bash scripts/sources-census.sh validate --file /tmp/sources-test/corpus/SOURCES.md --today 2026-10-21` | 0 | `file ok` |
| `bash scripts/sources-census.sh census --file …` | 0 | rows 12, tier.A 11, queued 7 |
| `strings -n 4 bin/codex \| grep -c …` | 0 | counts in §5.5 |

No tool was installed or upgraded; no pacman transaction was attempted. No omp/opencode/codex
session was launched and no credential file was read.

## 7. What I did NOT check

- No live Codex run: the client-behavior claims are documentation plus binary strings, not
  observed routing. Whether `~/.codex/skills` is loaded by 0.163.0 is unverified (the docs omit
  it; only the bundled prompt names it).
- No non-author re-open: per contract, the spot-check sample belongs to the orchestrator/next
  lane. My quotes are single-author.
- No check of the ChatGPT-side (non-Codex) skill behavior, plugin distribution, or
  `agents/openai.yaml` semantics beyond what is quoted.
- The base census numbers in §2 come from the temp-copy run, not from a lane-root run; I did
  not run any lane-wide gate at the lane root (contract).
- `recheck: 90d` is a judgement, not a measurement; the page exposes no version to key a
  release cadence to.
