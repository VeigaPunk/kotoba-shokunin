# Sibling description rewrites — producer-ready package (round 8)

Domain: prompt & skill craft (kotoba-shokunin). Subject: the `description:`
frontmatter field of the five sibling `*-shokunin/SKILL.md` files, all under
`/home/vgpnk/projects/shokunin/`.

**Deliverable:** five drop-in replacements, one per sibling, each with the
exact YAML block to paste plus the rendered evidence that justifies it.
**Read-only guarantee:** no sibling file was edited by this lane; every sibling
citation below is a read. Writing is confined to this artifact's own path.

## 1. Method and mechanism

`description` is read by the omp router only through the **cache-or-truncate**
render (mechanism + constants in `render-mechanism-round7.md`; supersedes the
round-5 "model-compressed render" framing):

1. Module-template check `sha256(prompt_template \0 name \0 ws-collapsed
   description)` against `~/.omp/agent/skill-descriptions.db` — an LLM one-liner
   (≤160 chars, ≤12 words) if a row exists, else
2. deterministic truncator `previewSkillDescription` (H7s): ws-collapse; if
   `len <= 100` keep; else `s = t.slice(0, 99)`; if the first
   `/^.*?[.!?](?=\s|$)/` sentence in `s` is **≥40 chars**, keep exactly that
   sentence with **no ellipsis**; else cut `s` at the last ASCII space and append
   U+2026 `…`.

The H7s implementation used for every render below (Python; the JS original is
string-slice-identical):

```python
import re
def ws(t): return re.sub(r'\s+', ' ', t).strip()
def h7s(d):
    t = ws(d); n = len(t)
    if n <= 100:
        return t, ('keep(len<=100)', n, len(t))
    s = t[:99]
    m = re.match(r'^.*?[.!?](?=\s|$)', s)
    if m and len(m.group(0)) >= 40:
        return m.group(0), ('first-sentence>=40', n, len(m.group(0)))
    i = s.rfind(' ')
    out = (s[:i] if i > 0 else s) + '\u2026'
    return out, ('last-space+ellipsis', n, len(out))
```

**Harness validation (both paths reproduced before trusting the tool).**

| Check | Expected (round-7 doc) | Measured by this harness |
|---|---|---|
| godspeed, sentence-1 branch | sentence 1 kept verbatim, no ellipsis | `Use on every prompt, including nested and delegated prompts, without waiting for a keyword.` (91) — keep, no ellipsis |
| kotoba's own 814-char description, ellipsis branch | `Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /…` | byte-identical string, measured **94** chars incl. `…` (the round-7 doc states 104 — the *string* matches; the count in that doc does not reproduce under char or byte accounting, so treat 94 as measured) |
| 17 live offered descriptions | keep 55–96 | 56–98, both branches observed; sentence-branch keeps = 87 / 81 / 91 (omarchy, xbrd-ask, godspeed) |

**Discovery-root caveat (unchanged, do not overclaim):** the six `*-shokunin`
SKILL.md files sit at repo roots, outside every omp discovery root
(`.agent/skills`, `.agents/skills`, `.claude/skills`, marketplace cache), so
none of them is offered in `<skills>`; no render of any kind is produced for
them today. These rewrites therefore serve (a) audit-hygiene conformance to the
trigger-fidelity checklist, (b) any future roster/tool that reads frontmatter,
(c) discovery if a file ever moves into a root. The cliff rules are applied
anyway because they are the domain standard.

**Drift pin.** Sibling line citations below were verified against these exact
bytes (`md5sum`, mtime 2026-09-28, siblings were being edited by their own
lanes during this round):

| File | md5 | lines | mtime |
|---|---|---|---|
| `kagi-shokunin/SKILL.md` | `20f3c9acd023d56cea0eeba07a729030` | 322 | 17:41:28 |
| `kake-shokunin/SKILL.md` | `a7d2faa1f90ee41758074d2534dabe02` | 245 | 17:42:11 |
| `kasegi-shokunin/SKILL.md` | `217d7732ade91cd7a6e01aa205d8312c` | 493 | 17:39:15 |
| `kengaku-shokunin/SKILL.md` | `6e59ecb2c96a8b15b57d9e480433703d` | 312 | 17:25:32 |
| `kumitate-shokunin/SKILL.md` | `a6de9b8887b99d42fffba120029922fa` | 521 | 17:30:37 |

If a hash has moved, re-grep the cited phrase before trusting the line number —
do not propagate a line ref whose source moved. `description:` line 3 was
checked to be unchanged (mint-template text) at citation time for all five.

## 2. Summary

| Sibling | current render (H7s) | proposed render (H7s) | S1 ws-collapsed | branch | desc src len | quoted triggers (surviving in render) |
|---|---|---|---|---|---|---|
| kagi | 96 chars, last-space+`…` | 92 chars, sentence, no ellipsis | 92 | first-sentence | 876 | 16 (6 incidental) |
| kake | 97 chars, last-space+`…` | 95 chars, sentence, no ellipsis | 95 | first-sentence | 988 | 15 (2 incidental) |
| kasegi | 98 chars, last-space+`…` | 93 chars, sentence, no ellipsis | 93 | first-sentence | 920 | 15 (2 incidental) |
| kengaku | **70 chars**, last-space+`…` (worst in fleet) | 96 chars, sentence, no ellipsis | 96 | first-sentence | 880 | 11 (3 incidental) |
| kumitate | 93 chars, last-space+`…` | 97 chars, sentence, no ellipsis | 97 | first-sentence | 852 | 12 (2 incidental) |

"Incidental" = the quoted string happens to appear inside sentence 1; the
`Triggers:` list itself still sits past the 99-char cliff. That is by design:
sentence 1 carries the capability + the match-critical WHEN nouns; sentences 2+
are the audit/cache layer (they survive verbatim only if an LLM cache row
lands, and that path paraphrases).

## 3. Proposals

### 3.0 Checklist items quoted verbatim (source: `kotoba-shokunin/SKILL.md`, "Trigger-fidelity checklist")

- **Item 2:** "`description` contains ≥1 literal trigger string in quotes or an explicit `Triggers:` list."
- **Item 3:** "`description` contains at least one anti-trigger or exclusion clause."
- **Item 4:** "Overlapping sibling skills are named **concretely** with an arbitration rule in the `description` (a generic "the owning domain skill" does not count; body/PROVINCE boundary text does not count — the router never reads it). Write `N/A — no overlapping sibling exists` when applicable: a bare absence is indistinguishable from an unconsidered one."

**YAML style chosen:** `description: >` folded block scalar, 2-space indent,
wrapped at 76 columns — the same style kotoba-shokunin's own frontmatter uses.
Fold style is **render-irrelevant**: H7s ws-collapses first, and each block
below was machine-parsed (`yaml.safe_load`) and confirmed to fold back to the
exact intended single-line string (876/988/920/880/852 chars). Hard rule for
the producer: keep every line of the block at exactly the 2-space indent — a
more-indented line becomes a literal line break in a folded scalar — and insert
no blank line inside the block.

---

### 3.1 kagi-shokunin — secrets & vault ops

**Current (verbatim, `kagi-shokunin/SKILL.md:3`):**

```
description: Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault lifecycle. Rank: shonen.
```

**Proposed (paste over line 3):**

```
description: >
  Secrets and vault ops: the-janitor requests, 1Password op refs, credential
  hygiene evidence. Triggers: "the-janitor", "janitor", "secrets", "vault",
  "1Password", "op", "op.env", "credential hygiene", "AUTH_REQUIRED",
  "tac-check", "cdp-bridge", "OP_SERVICE_ACCOUNT_TOKEN", "transcript-scan",
  "janitor request wedged", "headless handler", "where are the keys". Implicit
  intents: a handler that will not start, or a request that hangs; deciding
  whether a value is secret-shaped. Anti-triggers: printing, copying, or
  pasting a secret value, session token, cookie, or vault field into any
  artifact; generic password-manager advice with no handler, op, or receipt
  flow. Sibling boundary: kagi owns vault auth and the CDP bridge itself; kake
  owns the property fleet and the shared burner-chrome lease (CDP
  127.0.0.1:9222) - report lease conflicts to kake, never absorb. Rank:
  shonen.
```

- **Sentence 1** (renders verbatim, no ellipsis): `Secrets and vault ops: the-janitor requests, 1Password op refs, credential hygiene evidence.` — ws-collapsed length **92** (40 ≤ 92 ≤ 99 ✓); no internal `.`/`!`/`?` ✓. Internal dots were deliberately kept out of sentence 1: `1Password`, `the-janitor`, `op` carry no dot, while `op.env` / `op://` / `~/.config/...` had to move to sentence 2 because a dotted token inside sentence 1 would still be a *candidate* terminator only if whitespace followed — it does not, but keeping them out removes the class of risk entirely.
- **Triggers and sources** (sibling repo `kagi-shokunin/SKILL.md`, pinned hash above):

| Trigger string | Line(s) | Observed text |
|---|---|---|
| `"the-janitor"` | 8, 23–36 | L23 `\| Ask the handler anything \| `echo '…' \| the-janitor request`` |
| `"janitor"` | 8 | `the-janitor persistent handler (tmux `janitor`, OpenCode server` |
| `"secrets"`, `"vault"` | 6, 14–17 | L14 `**Hard rule:** never print, copy, or exfiltrate a secret value…`; L17 `Handle hygiene *evidence* and *flows*, not secret material.` |
| `"1Password"` | 10, 27 | L10 `1Password CLI `op` 2.35.0`; L27 `Check 1Password authorization` |
| `"op"` | 10, 28 | L28 `assuming handler auth; it uses caller's `op`` |
| `"op.env"` | 28, 191 | L28 `needs `~/.config/the-janitor/op.env` present`; L191 `\| `op://` refs in `op.env` \| vault item \|` |
| `"credential hygiene"` | 15–17, 202 | L202 header `## Credential-hygiene checklist` |
| `"AUTH_REQUIRED"` | 27 | `handler calls `janitor_auth` → `AUTH_OK`/`AUTH_REQUIRED`` |
| `"tac-check"` | 31, 206, 231 | L31 `\| Verify TAC receipt \| `the-janitor tac-check`` |
| `"cdp-bridge"` | 33, 206 | L33 `\| 1Password in musketeer Chrome \| `cdp-bridge ensure` then `status`` |
| `"OP_SERVICE_ACCOUNT_TOKEN"` | 24, 144 | L24 `\| Run handler headless \| export `OP_SERVICE_ACCOUNT_TOKEN`…`; L144 `Auth selectors (read by `_serve`, L194–210)` |
| `"transcript-scan"` | 36 | `\| Audit transcript for leaked secrets \| `corpus/transcript-scan.sh`` |
| `"janitor request wedged"` (implicit intent) | 34, 97 | L34 `\| Diagnose a wedged handler \|`; L97 ``a hung request wedges `stop``` |
| `"headless handler"` | 24 | `\| Run handler headless \|` |
| `"where are the keys"` (implicit intent) | 28–29 | L29 `\| Inventory env keys \| `the-janitor refs`` |
| `"is the vault unlocked"` (implicit intent, in anti-trigger list) | 250 | `Treating `status`/`tac-check` OK as "vault is unlocked" or "TAC is live"` |

- **Anti-triggers:** printing/copying/pasting a secret value, session token, cookie, or vault field into an artifact (L14–17 hard rule); generic password-manager advice with no handler/`op`/receipt flow. Also cites the in-body absorb refusal (L254 `Absorbing cross-domain surfaces (CDP lease, musketeer profile) into this repo — report to integrator.`).
- **Arbitration (rival named: kake):** L216 `- [ ] CDP port 9222 + musketeer profile are shared with the kake fleet: report lease conflicts, don't absorb them.` Rule in the description: kagi owns vault auth + the CDP bridge; kake owns the property fleet and the shared burner-chrome lease; lease conflicts go to kake.
- **H7s render — actual output:**

```
CURRENT  src=120  branch=last-space+ellipsis  out=96
Domain specialist — secrets & vault ops — the-janitor flows, credential hygiene evidence, vault…
PROPOSED src=876  branch=first-sentence>=40   sent=92  out=92
Secrets and vault ops: the-janitor requests, 1Password op refs, credential hygiene evidence.
```

Current loses `vault lifecycle. Rank: shonen.` and every capability word past offset 99; the proposed render is a complete, ellipsis-free hint. 6 of 16 quoted strings appear incidentally inside sentence 1 (`the-janitor`, `janitor`, `vault`, `1Password`, `op`, `credential hygiene`).

- **Checklist self-application:**

| Item (verbatim, §3.0) | Mark | Evidence |
|---|---|---|
| Item 2 | **PASS** | `Triggers:` list present; 16 quoted strings (`"the-janitor"` … `"where are the keys"`) |
| Item 3 | **PASS** | `Anti-triggers: printing, copying, or pasting a secret value, session token, cookie, or vault field into any artifact…` |
| Item 4 | **PASS** | rival named concretely (`kake`) + rule (`report lease conflicts to kake, never absorb`), sourced to L216/L254 |

---

### 3.2 kake-shokunin — web properties & publishing

**Current (verbatim, `kake-shokunin/SKILL.md:3`):**

```
description: Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen.
```

**Proposed (paste over line 3):**

```
description: >
  Web properties and publishing: webzites probes, ds4cc and Kimi mirrors,
  operator-gated publish. Triggers: "ds4cc.com", "kimi.page", "kimi.pro",
  "webzites", "fleet.config.json", "probe --all", "sync-check", "grokbot
  tick", "mirror", "republish", "Pages deploy", "speedrun", "the site is 404",
  "the mirror is stale", "publish this site". Implicit intents: a live URL
  disagreeing with source bytes; deciding whether a row needs a republish or a
  marker re-pin. Anti-triggers: never git push, never click Publish, never
  call PublishApp/PublishDeployment/UnpublishApp - publish stays
  operator-gated; not for runtime repos or non-git snapshot trees (ufofsdbeta,
  ufofsdbeta-kimi-review). Sibling boundary: kagi owns vault auth and the
  cdp-bridge handler surface; kake owns fleet publish probes and holds the
  shared burner-chrome lease (musketeer profile, CDP 127.0.0.1:9222) - kagi
  reports lease conflicts to kake rather than absorbing them, and the
  vault/auth surface stays kagi's. Rank: shonen.
```

- **Sentence 1:** `Web properties and publishing: webzites probes, ds4cc and Kimi mirrors, operator-gated publish.` — ws-collapsed length **95** ✓; no internal `.`/`!`/`?` ✓. Dotted hostnames (`ds4cc.com`, `kimi.page`, `kimi.pro`, `fleet.config.json`) are deliberately in sentence 2 only.
- **Triggers and sources** (`kake-shokunin/SKILL.md`, pinned hash):

| Trigger string | Line(s) | Observed text |
|---|---|---|
| `"ds4cc.com"` | 16, 19, 28 | L16 `\| ds4cc.com (primary) \| `https://ds4cc.com/`` |
| `"kimi.page"` | 19, 22, 24–25, 27 | L19 `\| ds4cc kimi mirror \| `https://ds4cc.kimi.page/`… STALE` |
| `"kimi.pro"` | 23 | `\| ufo-fsd.kimi.pro \| `https://ufo-fsd.kimi.pro/` \| none (Vite shell)` |
| `"webzites"` | 30, 46 | L30 `Registry of record: `~/Projects/webzites/fleet/fleet.config.json``; L46 `node ~/Projects/webzites/bin/webzites.mjs probe --all` |
| `"fleet.config.json"` | 30 | same line |
| `"probe --all"` | 46 | `1. **Probe, don't guess.** … probe --all` |
| `"sync-check"` | 66 | ``node scripts/kimi-surface.mjs sync-check [<id>]` (pure HTTP, no browser;` |
| `"grokbot tick"` | 61 | ```grokbot tick` daily. Check `state/probe-latest.json` age before`` |
| `"mirror"` | 19, 22 | L22 `canonical kimi charter mirror (stale: serves 09-18 beat, canonical 09-28)` |
| `"republish"` | 108 | `6. **Re-pin markers after republish.**` |
| `"Pages deploy"` | 16, 26 | L26 `Pages branch deploy on push — live 200, verified 09-28` |
| `"speedrun"` | 95 | `- **ds4cc.com/speedrun has its own gated lane.** Keeper:` |
| `"the site is 404"` (implicit) | 24–27 | L27 `\| lucario kimi slot \| `https://lucario.kimi.page/` — 404, **never published**` |
| `"the mirror is stale"` (implicit) | 19, 22 | L19 `STALE (~Aug-29 vintage)` |
| `"publish this site"` (implicit) | 8, 243 | L243 `Hard rule, repeated: publish stays operator-gated.` |

- **Anti-triggers:** the operator gate (L243 `Never `git push`, never click Publish, never call `PublishApp`/`PublishDeployment`/`UnpublishApp``; L74 `GHP rows: the publish verb is `git push origin main` — operator action.`); non-publishable source trees (L38 `Non-sources: `~/Projects/ufofsdbeta` is the UFO-FSD *runtime* repo (no Pages site…)`).
- **Arbitration (rival named: kagi):** L104–107 `5. **Lease before browser.** … The shared burner chrome (`the-musketeer` profile, CDP `127.0.0.1:9222`) serializes the whole kimi fleet` + kagi L216 (lease conflicts reported to kake). Rule in the description: kagi owns vault auth + the cdp-bridge surface; kake holds the shared burner-chrome lease and reports/arbitrates lease conflicts.
- **H7s render — actual output:**

```
CURRENT  src=119  branch=last-space+ellipsis  out=97
Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages…
PROPOSED src=988  branch=first-sentence>=40   sent=95  out=95
Web properties and publishing: webzites probes, ds4cc and Kimi mirrors, operator-gated publish.
```

Current keeps `Pages` then dies before `deploys. Rank: shonen.`; proposed keeps the four match-critical nouns (`webzites`, `ds4cc`, `Kimi`, `mirrors`) plus the `operator-gated publish` constraint. 2 of 15 quoted strings survive incidentally (`webzites`, `mirror`).
- **Note (drift observed this round):** kake is being edited by its own lane; L46 changed from a bare `webzites probe --all` to `node ~/Projects/webzites/bin/webzites.mjs probe --all` between reads (the round-5 audit's bare-bin defect, L46 in the 211-line version). The rewrite below is independent of that fix.

- **Checklist self-application:**

| Item (verbatim, §3.0) | Mark | Evidence |
|---|---|---|
| Item 2 | **PASS** | `Triggers:` list present; 15 quoted strings (`"ds4cc.com"` … `"publish this site"`) |
| Item 3 | **PASS** | `Anti-triggers: never git push, never click Publish, never call PublishApp/PublishDeployment/UnpublishApp - publish stays operator-gated…` |
| Item 4 | **PASS** | rival named concretely (`kagi`) + rule (lease ownership + conflict routing), sourced to L104–107 and kagi L216 |

---

### 3.3 kasegi-shokunin — bounty & security research

**Current (verbatim, `kasegi-shokunin/SKILL.md:3`):**

```
description: Domain specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim packages. Rank: shonen.
```

**Proposed (paste over line 3):**

```
description: >
  Bounty and security research: policy reads, hunt triage, claim packages and
  submission gates. Triggers: "bounty", "bug bounty", "claim package",
  "claim-ready", "honest-zero", "scope snapshot", "program rules", "policy
  read", "claim-check", "review verdict", "autopsy", "bounty-map", "VDP
  disclosure", "is this claimable", "continue or drop this mission". Implicit
  intents: deciding what a program's policy actually grants; turning a bounded
  negative into an honest-zero package. Anti-triggers: never submit -
  submission is operator-only (decree 2026-09-05) and the fleet stages, never
  sends; no manufactured findings; no generic security theory without program
  bytes. Sibling boundary: kasegi owns the bounty tree, its claim machinery,
  and ~/Projects/bounties/ledger/telemetry.jsonl; kengaku interprets that
  ledger for route claims but does not own it, and ufo-fsd/OMP dispatch
  tooling belongs to kumitate. Rank: shonen.
```

- **Sentence 1:** `Bounty and security research: policy reads, hunt triage, claim packages and submission gates.` — ws-collapsed length **93** ✓; no internal `.`/`!`/`?` ✓.
- **Triggers and sources** (`kasegi-shokunin/SKILL.md`, pinned hash):

| Trigger string | Line(s) | Observed text |
|---|---|---|
| `"bounty"` | 8 | `Grounded in `/home/vgpnk/Projects/bounties` (UFO fleet HQ): 275 claim packages` |
| `"bug bounty"` | 124 | ``map `github-bug-bounty` (the one`` |
| `"claim package"` | 8, 276 | L8 `275 claim packages`; L276 `## Evidence-package anatomy` |
| `"claim-ready"` | 11, 23, 73 | L11 `at `docs/claim-ready-index.md``; L73 `claimable:true` … `docs/claim-ready-index.md` (12 queued)` |
| `"honest-zero"` | 20, 77 | L77 `\| Bounded negative result … \| LEARNED honest-zero (438/486) \|` |
| `"scope snapshot"` | 16, 33 | L16 `policy read (AR14, passive only) → evidence/<program>/scope-snapshot.json`; L33 `Fill `evidence/<program>/scope-snapshot.json`` |
| `"program rules"` | 31 | `## Program-rule checklist (step 1 of any mission)` |
| `"policy read"` | 16 | same L16 |
| `"claim-check"` | 21, 85 | L85 ``claim-check.mjs` enforces all of it (authoritative list:`` |
| `"review verdict"` | 82 | ``Verdict rule from `fleets/review-mission.md`: **drop** = dead end, **continue**`` |
| `"autopsy"` | 78, 248 | L78 `docs/autopsies/<program>.md`; L248 `## Retirement lane — autopsies & the detail regex` |
| `"bounty-map"` | 8–10 | `1088 program records under `bounty-map/programs/`` |
| `"VDP disclosure"` | 235 | `## VDP disclosure packages (sibling format)` |
| `"is this claimable"` (implicit) | 66–78, 73 | triage table; `claimable:true` column |
| `"continue or drop this mission"` (implicit) | 82 | `**drop** = dead end, **continue** = name the one executable next step, **leave** = don't touch again` |

- **Anti-triggers:** automated submission (L24 `submission → OPERATOR ONLY, never automated (decree 2026-09-05)`); manufactured findings (L299 `## Disclosure anti-patterns`; the honest-zero class at L77 is a first-class deliverable); generic security theory without program bytes (the whole file is file-cited).
- **Arbitration (rivals named: kengaku, kumitate):**
  - kengaku `SKILL.md:139` reads `1. **Lane-routing ledger**: `~/Projects/bounties/ledger/telemetry.jsonl`` and `:305` cites the same file — kasegi owns the file (kasegi L151 `actions. `ledger/telemetry.jsonl` (7218 lines) is the dispatcher heartbeat`), kengaku interprets it read-only.
  - kumitate owns the ufo-fsd/OMP dispatch machinery; kasegi's L169 `## Mission control plane` runs its own in-repo `ops/fleet-dispatch.mjs` — a bounty mission envelope stays here, the OMP transport belongs to kumitate.
- **H7s render — actual output:**

```
CURRENT  src=121  branch=last-space+ellipsis  out=98
Domain specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim…
PROPOSED src=920  branch=first-sentence>=40   sent=93  out=93
Bounty and security research: policy reads, hunt triage, claim packages and submission gates.
```

Current dies mid-word after `claim`; proposed renders `policy reads`, `hunt triage`, `claim packages`, `submission gates`. 2 of 15 quoted strings survive incidentally (`claim package`, `policy read`).

- **Checklist self-application:**

| Item (verbatim, §3.0) | Mark | Evidence |
|---|---|---|
| Item 2 | **PASS** | `Triggers:` list present; 15 quoted strings (`"bounty"` … `"continue or drop this mission"`) |
| Item 3 | **PASS** | `Anti-triggers: never submit - submission is operator-only (decree 2026-09-05) and the fleet stages, never sends; no manufactured findings…` |
| Item 4 | **PASS** | rivals named concretely (`kengaku`, `kumitate`) + rules (ledger ownership; dispatch-machinery boundary), sourced to kasegi L151/L169, kengaku L139/L305 |

---

### 3.4 kengaku-shokunin — LLM/model research & evaluation

**Current (verbatim, `kengaku-shokunin/SKILL.md:3`):**

```
description: Domain specialist — LLM/model research & evaluation — scopes llm-wiki (~/Projects/webzites/repos/llm-wiki), route telemetry. Rank: shonen.
```

**Proposed (paste over line 3):**

```
description: >
  LLM and model research: benchmark selection, eval batteries, route
  telemetry, capability claims. Triggers: "benchmark", "eval", "llm-wiki",
  "battery", "route telemetry", "model capability", "contamination",
  "calibration", "SWE-Bench", "which benchmark", "is this model actually
  better". Implicit intents: choosing or designing a benchmark; making a
  capability or routing claim stand on evidence. Anti-triggers: Aliyun/Bailian
  model facts (pricing, context windows, API params, model selection) belong
  to bailian-docs-llm-wiki; runtime code changes are out of scope; reading a
  telemetry ledger confers no ownership of it. Sibling boundary: kengaku owns
  the llm-wiki corpus, bench-arena batteries, and eval-design claims;
  bailian-docs-llm-wiki owns Bailian model data, and kasegi owns
  ~/Projects/bounties/ledger/telemetry.jsonl - route-claim overlap is
  read-only here. Rank: shonen.
```

- **Sentence 1:** `LLM and model research: benchmark selection, eval batteries, route telemetry, capability claims.` — ws-collapsed length **96** ✓; no internal `.`/`!`/`?` ✓.
- **Triggers and sources** (`kengaku-shokunin/SKILL.md`, pinned hash):

| Trigger string | Line(s) | Observed text |
|---|---|---|
| `"benchmark"` | 17, 24 | L17 `## Decision table — benchmark selection`; L24 `SWE-Bench Pro (public)` |
| `"eval"` | 8, 150, 274 | L150 `2. **Eval battery**: `~/bench-arena/telemetry-qwenlocal-v2.csv` (33`; L274 `## Production checklist — running an eval` |
| `"llm-wiki"` | 8 | `Source of truth: `~/Projects/webzites/repos/llm-wiki`` |
| `"battery"` | 33, 150, 228 | L33 `\| Search-shape claims \| **Custom battery only**` |
| `"route telemetry"` | 108, 305 | L108 `## Route-telemetry interpretation`; L305 `live lane-routing corpus, 7,218 events` |
| `"model capability"` | 8, 24 | L8 `LLM/model research & evaluation.` + the benchmark tables measure capability |
| `"contamination"` | 24, 47, 49 | L24 `Verified increasingly contaminated per OpenAI 2026-02-23`; L49 `1. **Leaderboard worship / stale benchmark trust.** OpenAI retired` |
| `"calibration"` | 55, 62, 65 | L62 `4. **Skip ex-ante calibration.** Record framer predictions before runs;` |
| `"SWE-Bench"` | 24 | `\| Software engineering \| SWE-Bench Pro (public) \|` |
| `"which benchmark"` (implicit) | 17 | benchmark-selection decision table |
| `"is this model actually better"` (implicit) | 24, 33, 47 | the anti-patterns that punish under-evidenced capability claims |

- **Anti-triggers:** Aliyun/Bailian model facts → `bailian-docs-llm-wiki` (kengaku L303 cites that skill's `models/index.md` + `models.jsonl` as its own read-only source, which is exactly the overlap); runtime code changes; reading the bounty ledger does not transfer ownership (kasegi L151).
- **Arbitration (rivals named: bailian-docs-llm-wiki, kasegi):** L303 `~/.bailian/skills/bailian-docs-llm-wiki/models/index.md` + `models.jsonl` — 180 families / 413 models … for model selection` (Bailian model data lives there); L139/L305 `~/Projects/bounties/ledger/telemetry.jsonl` (kasegi owns the file, kengaku interprets). Rule in the description: Bailian model facts route to `bailian-docs-llm-wiki`; route-telemetry reads are read-only.
- **H7s render — actual output:**

```
CURRENT  src=138  branch=last-space+ellipsis  out=70
Domain specialist — LLM/model research & evaluation — scopes llm-wiki…
PROPOSED src=880  branch=first-sentence>=40   sent=96  out=96
LLM and model research: benchmark selection, eval batteries, route telemetry, capability claims.
```

The current render is the worst in the fleet — **70 chars**, because the first 99 collapsed chars contain no `[.!?]`+whitespace terminator (the dots in `~/Projects/webzites/repos/llm-wiki` are followed by letters), so the truncator backs off to the space after `llm-wiki`. It loses the entire capability clause. Proposed renders four capability/WHEN terms verbatim. 3 of 11 quoted strings survive incidentally (`benchmark`, `eval`, `route telemetry`).

- **Checklist self-application:**

| Item (verbatim, §3.0) | Mark | Evidence |
|---|---|---|
| Item 2 | **PASS** | `Triggers:` list present; 11 quoted strings (`"benchmark"` … `"is this model actually better"`) |
| Item 3 | **PASS** | `Anti-triggers: Aliyun/Bailian model facts (pricing, context windows, API params, model selection) belong to bailian-docs-llm-wiki; …` |
| Item 4 | **PASS** | rivals named concretely (`bailian-docs-llm-wiki`, `kasegi`) + rules (Bailian model-data routing; read-only ledger), sourced to kengaku L303/L139/L305 and kasegi L151 |

---

### 3.5 kumitate-shokunin — orchestration & tooling

**Current (verbatim, `kumitate-shokunin/SKILL.md:3`):**

```
description: Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts, crates/ufo-core-runtime. Rank: shonen.
```

**Proposed (paste over line 3):**

```
description: >
  Orchestration and tooling: OMP dispatch shapes, ufo-fsd scripts, native
  judged rounds, the queue. Triggers: "dispatch", "swarm wave", "sighting",
  "native round", "judge-handoff", "ParetoGate", "fleet-dispatcher", "wave
  size", "queue", "ufo CLI", "which dispatch shape", "route this lane".
  Implicit intents: choosing spawn wave vs sighting mission vs judged round;
  explaining why a lane was refused or parked. Anti-triggers: no judging
  outside the native judged round; Sekhmet/L3 stays shelved;
  application-domain bytes (bounty claims, site content, vault flows) stay
  with their owning skill. Sibling boundary: kumitate owns the ufo-fsd/OMP
  dispatch machinery and runtime; kasegi owns its in-repo bounty fleet
  dispatcher (~/Projects/bounties/ops/fleet-dispatch.mjs) - a bounty mission
  envelope is kasegi's, the OMP transport is kumitate's. Rank: shonen.
```

- **Sentence 1:** `Orchestration and tooling: OMP dispatch shapes, ufo-fsd scripts, native judged rounds, the queue.` — ws-collapsed length **97** ✓; no internal `.`/`!`/`?` ✓ (`ufo-fsd`, `OMP` carry no dots; `crates/ufo-core-runtime` does not, but the path form was dropped for the trigger nouns that actually appear in requests).
- **Triggers and sources** (`kumitate-shokunin/SKILL.md`, pinned hash):

| Trigger string | Line(s) | Observed text |
|---|---|---|
| `"dispatch"` | 12, 14, 18–20 | L14 `Three dispatch shapes exist. Pick by what the work needs, not by convenience.` |
| `"swarm wave"` | 18, 37 | L18 `\| **Swarm wave** (`ufo-swarm-wave.mjs`) \|`; L37 ``### `scripts/ufo-swarm-wave.mjs` — wave producer`` |
| `"sighting"` | 19, 64 | L19 `\| **Sighting mission** (`ufo-sighting`) \|`; L64 ``### `scripts/ufo-sighting.mjs` — mission lifecycle surface`` |
| `"native round"` | 20 | `\| **Native judged round** (`run-omp-native-trial.mjs` + `collect-omp-native-handoff.mjs`) \|` |
| `"judge-handoff"` | 20 | `typed handoff → `ufo judge-handoff` → Rust ParetoGate verdict` |
| `"ParetoGate"` | 20 | same line |
| `"fleet-dispatcher"` | 104 | ``### `scripts/fleet-dispatcher.mjs` — queue drain + iterate chain`` |
| `"wave size"` | 20 | `(`usage_wave_size_*` refusals)` |
| `"queue"` | 104 | `queue drain + iterate chain` |
| `"ufo CLI"` | 303 | ``### `ufo` CLI (`crates/ufo-cli`, backed by `crates/ufo-core-runtime`)`` |
| `"which dispatch shape"` (implicit) | 14, 32 | L32 `- Need many cheap parallel probes with no judgment? Swarm wave.` |
| `"route this lane"` (implicit) | 285, 297 | L285 `Canonical hand-rolled parser over the global OMP config (no YAML dep);`; L297 ``ufo route-plan --role <role>` prints the same resolution from the Rust`` |

- **Anti-triggers:** no judging outside the native judged round (L233 `The launcher NEVER calls `task`` + the L20 row "The only path whose output is judged"); Sekhmet/L3 shelved (L501 `14. **Sekhmet/L3 stays shelved.** No sparks dispatched; its 64-worker`); application-domain bytes (bounty claims, site content, vault flows) stay with the owning skill (L446 `## Anti-patterns — enforced or fired, never advisory-only`).
- **Arbitration (rival named: kasegi):** kumitate owns the ufo-fsd/OMP dispatch machinery and runtime (L9 `its source in the origin repo (`/home/vgpnk/Projects/origin-work/ufo-fsd-alpha``), while kasegi's L169 `## Mission control plane` describes a separate in-repo engine `ops/fleet-dispatch.mjs` under the bounties tree. Rule in the description: the bounty mission envelope is kasegi's; the OMP transport is kumitate's. (kotoba-shokunin is deliberately *not* named: it audits file craft, it does not own dispatch — and the checklist's own rule bar is "concretely" + arbitration, which the kasegi clause satisfies.)
- **H7s render — actual output:**

```
CURRENT  src=131  branch=last-space+ellipsis  out=93
Domain specialist — orchestration & tooling — scopes OMP task/hub dispatch, ufo-fsd scripts,…
PROPOSED src=852  branch=first-sentence>=40   sent=97  out=97
Orchestration and tooling: OMP dispatch shapes, ufo-fsd scripts, native judged rounds, the queue.
```

Current dies before `crates/ufo-core-runtime. Rank: shonen.`; proposed renders the four dispatch-shape nouns plus `the queue`. 2 of 12 quoted strings survive incidentally (`dispatch`, `queue`).

- **Checklist self-application:**

| Item (verbatim, §3.0) | Mark | Evidence |
|---|---|---|
| Item 2 | **PASS** | `Triggers:` list present; 12 quoted strings (`"dispatch"` … `"route this lane"`) |
| Item 3 | **PASS** | `Anti-triggers: no judging outside the native judged round; Sekhmet/L3 stays shelved; application-domain bytes … stay with their owning skill.` |
| Item 4 | **PASS** | rival named concretely (`kasegi`) + rule (mission envelope vs OMP transport), sourced to kumitate L9 and kasegi L169 |

---

## 4. Producer instructions

1. For each sibling, replace **line 3 only** (`description: …` + nothing else) with
   the §3 block. Keep the `---` fences, `name:`, and every body line untouched —
   these rewrites are frontmatter-scoped.
2. Keep the folded block uniformly at 2-space indent; no blank line inside; no
   line more indented than its siblings. Verify the fold-back after editing:
   `python3 -c "import yaml,sys;s=yaml.safe_load(open(sys.argv[1]).read().split('---')[1])['description'];print(len(s))" file` should print the §3 char count (876/988/920/880/852).
3. `Rank: shonen.` is retained at the end of every description (roster
   metadata, and the truncator never reaches it — end position costs nothing).
4. Do not add a `Triggers:`-only description and keep the audit blockers in the
   body (hard rules, refusal tables): the description now points at them, the
   body still enforces them.
5. Re-run the checklist items 2–4 by reading only the file after the edit —
   items 2–4 are body-independent by construction.

## 5. Falsification and limits

- **Reproduce a render:**
  `python3 -c "import re,sys;d=sys.stdin.read();t=re.sub(r'\s+',' ',d).strip();s=t[:99];m=re.match(r'^.*?[.!?](?=\s|\$)',s);print(m.group(0) if (m and len(m.group(0))>=40) else (s[:s.rfind(' ')]+'\u2026' if len(t)>100 else t))"`
  piped with the description string — should print the §3 render exactly.
- **Harness validation** is §1: godspeed's sentence-1 keep and kotoba's own
  ellipsis render both reproduce, so the tool is not merely plausible.
- **Unverifiable / not claimed:** (a) whether any of these renders would route
  better is unmeasured — none of the five is offered today, so no activation
  attribution is possible; (b) the LLM-cache branch is not exercised here (no
  cache row can exist for an unoffered skill: the key includes the name and the
  description, both current as of this file); (c) the round-7 doc's "104" char
  count for kotoba's own render did not reproduce (measured 94) — the rendered
  *string* is identical, so nothing downstream depends on the count.
- **Drift risk:** kake (245 lines) and kasegi (493 lines) were mutated by their
  own lanes mid-round; cite by hash (§1) or re-grep the phrase before trusting
  a line number.