# Kb81L01Grammar — external-commit grammar recon (scout, leaf)

Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e` (working tree = base; receipts `.ufo/waves/round-81/receipts/`).
Scope: every line in `corpus/SOURCES.md` + `corpus/knowledge/` + `corpus/lessons/` matching a third-repository
commit citation; extended to all 154 tracked `corpus/*.md` because both corpus gates scan exactly that set
(`verify_corpus_integrity.py` `POINTERS reads every tracked *.md under corpus/`; `verify_corpus_independent.py`
`analyse_commits` over `tracked_corpus`). The extra scan surface found hits in `corpus/README.md` and
`corpus/QUALITY.md` (reported below; the assigned dirs are covered completely).

## Grammar actually gated (frozen base bytes, observed)

Both gates harvest only `commit \`<token>\`` (integrity `COMMIT_RE` line 151 `(?<![A-Za-z0-9_-])commit[ \t]+\`([^\`\n]+)\``;
independent line 126 `commit\s+\`([^\s]+)\``). A token is counted in `commit_total` iff 7–40 hex, NOT double-quoted on
its line (`commit_quoted`, 6 sites), NOT `<hex>…`-truncated (`commit_truncated`, 4 sites); then it must resolve
`git cat-file -e <hex>^{commit}` lane-first then fleet (`FLEET_ROOT=/home/vgpnk/Projects/shokunin`) or it is
`commit_unresolvable`. The r80 E05 marker grammar (`EXTERNAL_RE` line-marker → `commit_external`) is SUPERSEDED:
R2 exempts a hash iff absent from lane+fleet AND pinned in `verifiers/external-commits.json`.
`<rev>:<path>` report pointers are tokenized by the `.ufo/reports/round-\d+` pointer regex (the `rev:` prefix rides
inside the captured token on integrity; the independent regex excludes `:` from the head class), resolved as a path
relative to citing dir then fleet-root file — the R1 repair adds `<rev>:<path>` object resolution + content identity.

## Census totals (raw sweep, before the gates' exclusions)

`commit \`token\`` sites: **56** in 11 files' worth of lines — 50 hex-shaped (46 live + 4 double-quoted), 6 non-hex
(`<hex>` round-53.md:45, `round-N` round-6-aggregator-audit.md:45, four `…`-truncated). Reconciles exactly with the
base receipts: `commit_candidates 56 = commit_total 46 + quoted 6 + truncated 4`, `commit_unresolvable 2`,
`nonhash 0` (Kb81K02Patterns integrity-base.json / independent-base.json). Zero `commit \`owner/repo@hex\`` sites —
the r80 E05 token-level grammar arm fires on nothing live (matches E05's R4 residual).

## A. The red pool — `commit \`<hex>\`` absent from lane AND fleet (3 distinct hashes, 5 sites)

| file:line | token | lane `cat-file -e` | fleet `cat-file -e` | repo named on line | r81 manifest binds? | R2 verdict |
|---|---|---|---|---|---|---|
| corpus/SOURCES.md:171 | `7bb48f213ac677f943d5c791199ed3dddf302f00` | no | no | `badlogic/pi-mono` URL (wrong repo — S230, R80-D4) | YES → `mistralai/mistral-vibe` | **exempt** (`commit_external`) |
| corpus/SOURCES.md:172 | `7bb48f213ac677f943d5c791199ed3dddf302f00` | no | no | `mistralai/mistral-vibe` URL (correct — S231) | YES → `mistralai/mistral-vibe` | **exempt** (`commit_external`) |
| corpus/lessons/round-53.md:44 | `cfb894a5` | no | no | `zed-industries/zed@` (inside the quoted span) | no | **stays green** — `commit_quoted`, exits upstream of resolution; R2 must keep it quoted-context, never reaches external/unresolvable |
| corpus/lessons/round-54.md:13 | `cfb894a5` | no | no | `zed-industries/zed@` | no | same — quoted exclusion |
| corpus/lessons/round-54-verifier-spotcheck.md:147 | `451a02ff` | no | no | none (bare `` `` commit `451a02ff` `` `` inside double quotes; `google-gemini/gemini-cli@` on :148) | no | same — quoted exclusion |

R2 binding analysis: the r81 manifest draft `.ufo/waves/round-81/build/Kb81E03ExtManifest.json` binds exactly one
hash — `7bb48f213ac677f943d5c791199ed3dddf302f00` → `mistralai/mistral-vibe`, evidence `.ufo/waves/round-79/snapshots/S231.fetch.json`.
One manifest row covers both citation sites (:171 wrong-repo, :172 right-repo) because the bind is hash→repo, not
site→repo; the S250 `supersedes S230` row (repair 5) is what fixes the :171 provenance record. The two quoted
absent hashes (`cfb894a5`→zed-industries/zed, `451a02ff`→google-gemini/gemini-cli) NEVER need manifest rows under
the current grammar — they are context, not citations; a future grammar that drops the quoted arm would have to
bind `cfb894a5` and `451a02ff` to `zed-industries/zed` and `google-gemini/gemini-cli` respectively (W6 stays red
without them anyway since `commit_unresolvable` would count them).

## B. The live population — `commit \`<hex>\`` that resolves (44 sites; nothing to exempt)

- 40 sites, distinct 24 lane hashes: lane commits (`git cat-file -e` OK in lane, e.g. `3b029b8`, `63ceba7`,
  `36ab0d3`, `4c003a4b`, `a647fa7`, `072048f`, `1e03d19…`). R2 leaves them `commit_total`, untouched.
- 4 sites, 4 fleet-only hashes (resolve via the round-66 fleet hop, never in lane): `def4b9fffbf59e9e121b89ef73fbeb89426bd614`
  (round-62-verifier-spotcheck.md:13), `7b370d54bd0e74eef4aa90b2e8b2fc9736b3d39f` (round-65:11),
  `1154d57a9ebb17faa4c9f8f456a6e53c51c230ae` (round-66:11), `33ee79336683f4abf4ae1448b751b17f3b84f7d5` (round-75-sc:7).
  R2 leaves them resolved; the fleet hop must be preserved (removing it would put 4 more in the red pool needing binds).

## C. `owner/repo@<hex>` citations (prose, not `commit \``-gated) — 16 sites

Full-hex sites absent from lane+fleet and currently **unbound** — all outside `COMMIT_RE` scope so they are
invisible to the commit grammar (context for the repair authors: if R2's harvest were ever widened to
`owner/repo@`, each of these needs a manifest row or it turns `commit_unresolvable`; today they need nothing):

| file:line | token | repo | resolves lane/fleet | bound? |
|---|---|---|---|---|
| corpus/README.md:137 | `agentskills/agentskills@69ef37e` | agentskills/agentskills | no/no | no |
| corpus/SOURCES.md:82 | `google-gemini/gemini-cli@a713410a` | google-gemini/gemini-cli | no/no | no |
| corpus/SOURCES.md:165 | `agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379` | agentskills/agentskills | no/no | no |
| corpus/knowledge/skill-eval-artefacts-round70.md:5,6 | `agentskills/agentskills@69ef37e…6379` (×2) | agentskills/agentskills | no/no | no |
| corpus/lessons/round-53.md:27 | `microsoft/vscode-docs@fd64d648` | microsoft/vscode-docs | no/no | no |
| corpus/lessons/round-54-verifier-spotcheck.md:37,148 | `google-gemini/gemini-cli@451a02ff` (×2) | google-gemini/gemini-cli | no/no | no |
| corpus/lessons/round-55.md:54 | `google-gemini/gemini-cli@451a02ff` | google-gemini/gemini-cli | no/no | no |
| corpus/lessons/round-71.md:6 | `agentskills/agentskills@69ef37e…6379` | agentskills/agentskills | no/no | no |
| corpus/lessons/round-71.md:13 | `anthropics/skills@dbd4588f9e1033efb41dad4bef2f7947c8993d44` | anthropics/skills | no/no | no |
| corpus/lessons/round-74.md:37 | `agentskills/agentskills@69ef37e` | agentskills/agentskills | no/no | no |
| corpus/lessons/round-75-verifier-spotcheck.md:36 | `anthropics/skills@dbd4588` | anthropics/skills | no/no | no |

Truncated `owner/repo@<hex>…` (renderings): round-52-verifier-spotcheck.md:99 `anomalyco/opencode@cdf1c200…`,
:100 `github/copilot-cli@7ea98dfc…`, round-71-verifier-spotcheck.md:102 `agentskills/agentskills@69ef37e…`.
Schematic/scaffold `slug@` markers with no hex: `zed-industries/zed@` (SOURCES.md:63,74; round-53.md:44;
round-54.md:13,52), `sst/opencode@dev` (opencode-offer-trace-round8.md:160), `google-gemini/gemini-cli@\`451a02ff\``
(skill-listing-thresholds-round54.md:29 — note hex inside its own backtick), `owner/repo@` (QUALITY.md:92,
round-80-verifier-spotcheck.md:22 — the plan's own marker-name examples). The marker surface a line-marker rule
would read: 27 files/45 grep-lines carry `slug@` or a github.com URL (`grep -rlE '…@|https?://(raw\.githubusercontent|github)\.com/' corpus/ | wc -l` = 45 lines' files — sweep below); under W6/W9 controls none of that matters: manifest-or-red.

## D. Bare backticked hex tokens with a repo named on the same/adjacent line — 177 sites

All NOT `commit \``-prefixed → invisible to `COMMIT_RE` today (sha256 fingerprints, upstream head-pins, table cell
hexes). 148 are `…`-truncated or sha256-shaped (>40 hex: not in the `cat-file` candidate class anyway). The 29
full-hex non-`commit`` tokens that are absent lane+fleet and unbound sit mostly in `SOURCES.md` fetch cells
(e.g. `dbd4588`, `fd64d648`, `e3c4eb24`, `4e0bc522`, `8aeff47`, `69ef37e`, `12ed2af6c5f4`, `ad6e6687ab4c` —
upstream heads/pins for anthropics/skills, agentskills, opencode, vscode-docs, zed, gemini-cli, claude-code). They
are the **blast radius if R2's harvest widens one char beyond `commit \`** — then ~25 manifest rows would be needed
or every one stays red. Under the declared R2 (manifest + `commit \`` grammar unchanged) they stay green by
invisibility; under the superseded marker rule they were the W8/W9 spoof surface. Full 177-site list is in the
census artifact (generated; not committed — re-derivable via the sweep commands below).

## E. `<rev>:<path>` tokens — the R1 surface (14 sites)

Report-pointer shape (`.ufo/reports/round-\d+/…`): exactly ONE —
`corpus/lessons/round-77-verifier-spotcheck.md:15` `HEAD:.ufo/reports/round-77/kotoba.md`. Observed at base:
integrity `report_dead 1` (its `resolve_pointer` treats `HEAD:…` as a path); independent `report_dead 0` (its
regex excludes `:` so the token starts at `.ufo/reports/` and the fleet-root file exists).
Object resolution (R1 grammar): `git -C /home/vgpnk/Projects/shokunin cat-file -e HEAD:.ufo/reports/round-77/kotoba.md`
**exit 0** (fleet HEAD); lane `cat-file -e` fails (report lives only in the fleet repo — the `HEAD` is the fleet's).
Content identity (R1's added arm): `git show` of that object = 8547 bytes and contains `## SHONEN` (line cites
"SHONEN contains four `[~]` lines", verified `grep -c '^## SHONEN'` = 1) → under R1 this token classifies
resolved-report (green); a W8-class marker file substituted at that path stays `report_dead` on the ≥400B+`## SHONEN`
arms. Caution for the R1 implementer: `HEAD` resolves in whichever repo `cat-file` runs — the lane-first-then-fleet
order in E04's draft is correct, but `HEAD:.ufo/…` must NOT be peeled in the citing lane first when the lane lacks
the path (lane cat-file exits 128 → fall through to fleet, as E04 already does).

Sibling `<rev>:<path>` tokens pointing OUTSIDE `.ufo/reports/` (13 sites, never harvested by the pointer regex —
listed because they share the `rev:path` shape): 11 resolve lane (`b1be35f:.ufo/round-40/claims.json` round-46.md:24;
`588f5824:…DescDraft.md` r51-sc:137; `a745411c:…C1-worlds.txt` r61-sc:100; `3e7aed9b:…ScribeEntry62.md` r62-sc:33;
`8c4cefa:`/`2ba4547:`/`cbbee56:` r63-sc:49,53,83; `2cf0d99:` r68-sc:75; `9ce102b:` r69-sc:71; `d1e9c93:` r70-sc:61);
ONE dead rev:path — `corpus/QUALITY.md:75` `35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`
(rev exists in lane, path absent at that rev — an ungated Q60-rule breach; also quoted context in a Q-criterion row);
ONE template — `0de5aba5:.ufo/waves/round-59/snapshots/<S>.page` r59-sc:72 (angle-bracket placeholder);
ONE brace-glob — `ec2c1d3:.ufo/waves/round-74/snapshots/{best-practices,…}.md` r74-sc:55.

## F. What R2 must exempt vs what stays red (the classification the seat exists for)

- **Exempt (bound in manifest draft):** `7bb48f213ac677f943d5c791199ed3dddf302f00` at SOURCES.md:171 AND :172.
- **Stays green without manifest:** 44 lane/fleet-resolved `commit \`hex\`` sites; 4 quoted-absent; 4 truncated;
  2 quoted-nonhash; all `owner/repo@` and bare-hex prose (invisible to `COMMIT_RE`).
- **Stays red by design (W6/W9 classes):** any `commit \`hex\`` absent lane+fleet and absent from
  `external-commits.json` — marker or not. Live example of that shape at base: none beyond the bound hash (the
  only unbound absent `commit \`` tokens are the two quote-excluded ones, which never reach the arm).
- **Guard for the implementer:** quoted/truncated/context arms (`commit_quoted` 6, `commit_truncated` 4) must
  remain green and must run BEFORE the manifest lookup (kill rule: no existing classification dropped);
  `commit_nonhash` stays 0 — `commit \`owner/repo@hex\`` would land in `nonhash` unless the grammar keeps an
  external arm for it (0 live sites, preventive only).

## Sweeps (every negative claim)

- `commit \`tokens\``: `grep -rnoE 'commit[ \t]+\`[^\`]+\`' corpus/` → 56 sites (50 hex / 6 nonhex; python recount above).
- `owner/repo@hex`: `grep -rnoE '[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{7,40}' corpus/` → 16 sites.
- `slug@` markers incl. bare: `grep -rnoE '[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@' corpus/` → 28.
- `rev:.ufo/reports/` pointers: `grep -rnoE '[A-Za-z0-9._/-]+:\.ufo/' corpus/` → 14 (`reports/` subset: 1).
- Bare backticked hex w/ repo ctx: custom scan (all tracked `corpus/*.md`, context ±1 line, repo vocab = the 14
  URL/@-derived slugs: VeigaPunk/kama-shokunin, agentskills/agentskills(.git), anomalyco/opencode,
  anthropics/claude-code, anthropics/skills, badlogic/pi-mono, github/copilot-cli, google-gemini/gemini-cli,
  microsoft/vscode-docs, mistralai/mistral-vibe, moonshotai/kimi-cli, sst/opencode, vinhnx/vtcode,
  zed-industries/zed) → 177 sites.
- `commit \`…:.ufo/…\`` (rev:path inside commit grammar): `grep -rnoE 'commit[ \t]+\`[A-Za-z0-9._/-]+:\.ufo/[^\`]+\`' corpus/` → 0.
- corpus `.json` files (sibling-citation-routing-round16.json — unscanned by gates anyway): 0 hits for all three patterns.
- Resolution: `git -C <lane|fleet> cat-file -e <hex>^{commit}` per distinct hash; `<rev>:<path>` resolved with
  `git cat-file -e <rev>:<path>` verbatim in both repos.
- Manifest: `.ufo/waves/round-81/build/Kb81E03ExtManifest.json` — read; binds exactly `7bb48f213ac677f943d5c791199ed3dddf302f00`→`mistralai/mistral-vibe` (evidence `.ufo/waves/round-79/snapshots/S231.fetch.json`). No `verifiers/external-commits.json` exists at base (new file this wave).

VERDICT: 56 `commit \`token\`` sites across 154 tracked corpus md — one hash (`7bb48f21…`, 2 sites at SOURCES.md:171-172) needs and gets the manifest exemption; 3 absent hashes never need binding (quoted-context); 44 resolve lane/fleet; all `owner/repo@`/bare-hex prose is outside COMMIT_RE scope; one `HEAD:.ufo/reports` pointer resolves green under R1's strengthened arms (fleet object, ## SHONEN, 8547B).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81L01Grammar.md
