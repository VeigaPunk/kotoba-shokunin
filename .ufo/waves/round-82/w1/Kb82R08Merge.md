# Kb82R08Merge — staged package collision and quarantine scout

Axes: freshness (fresh input derivation), operability (safe adoption identity).

## Observed findings — high confidence

Named base: `47dbe8781657de563ff867caca6244d28e3db504`. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 47dbe8781657de563ff867caca6244d28e3db504:corpus/SOURCES.md` exited **0**; no clone, checkout, index operation, commit, production verifier, campaign tool, or web fetch was run. Counts below derive from captured base bytes and separately read working-tree bytes, not prior summaries.

- Base registry: **176 rows / 176 unique IDs**. Current working registry: **176 / 176**; its sole differing data row is S248 (status/content transition is not adjudicated here).
- Staged `SOURCES.append.md`: **188 rows / 188 unique IDs**, contiguous **S203–S390**.
- Base and working registry each collide with **48 staged IDs: S203–S250 inclusive**. Complete explicit lists are published in `Kb82R08Merge-{registry-ids,staged-ids,collisions}.txt`.
- Staged noncolliding IDs: **140, S251–S390**. Registry-only IDs: **128**. Noncollision alone is not permission to adopt: S251 is reserved by this round's plan for its independently derived host receipt.
- `MERGE-REPORT.md:9` says the registry holds **128** rows; that is stale against the observed **176**. Its first staged ID S203 remains correct. Round-81's 46-collision receipt is also stale for this base: S249 and S250 add two collisions.

Extraction: `^ {0,3}\|\s*(S[0-9]{3,})\s*\|` in multiline mode, retaining full data rows and line numbers. Zero matching rows are indented in any of the three inputs, but the extractor accepts 0–3 spaces. These are literal Markdown-data findings, not semantic symbol-resolution claims. No LSP device is exposed in this session's device inventory.

## Quarantine — derived from complete register data rows

Canonical input: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`. Selected **only** data rows with lane `kotoba`, `roundN`, and an S-id, excluding the register's `kotoba | 7` summary. Continued lines are retained through the next table row, preserving the multiline quote payloads at lines 103–107, 108–109, 111–113 and 114–115. Result: **13 rows: 7 payload-absent and 6 fetch-failure/never-checked records**. Full raw rows, original line numbers, and current/staged bindings are published, not merely the old 13-ID summary.

Exact-URL matches below are source-cell token comparisons; shared URLs indicate document identity, **not** identical claims or confirmed absent quotations.

| Register ID | Register line | Recorded class | Register document | Staged same-URL IDs | Base same-URL IDs |
|---|---:|---|---|---|---|
| S151 | 103 | payload-absent | https://agentskills.io/skill-creation/optimizing-descriptions.md | S231 | S210, S213 |
| S167 | 108 | payload-absent | https://agentskills.io/client-implementation/adding-skills-support.md | S247, S256 | none |
| S168 | 110 | payload-absent | https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | S248 | none |
| S172 | 111 | payload-absent | https://junie.jetbrains.com/docs/agent-skills.html | S252 | S206, S241 |
| S176 | 114 | payload-absent | https://agentskills.io/client-implementation/adding-skills-support.md | S247, S256 | none |
| S180 | 116 | payload-absent | https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | S260 | none |
| S185 | 117 | payload-absent | https://docs.roocode.com/features/skills | S265 | S203, S239 |
| S236 | 327 | never checked / fetch failure recorded | https://skills.sh/docs | S316 | none |
| S237 | 328 | never checked / fetch failure recorded | https://skills.sh/audits | S317 | none |
| S238 | 329 | never checked / fetch failure recorded | https://code.claude.com/docs/en/security.md | S318 | none |
| S239 | 330 | never checked / fetch failure recorded | https://skills.sh/agent | S319 | none |
| S243 | 331 | never checked / fetch failure recorded | https://skills.sh/docs/api | S323 | none |
| S169 | 332 | never checked / fetch failure recorded | https://ai.google.dev/gemini-api/docs/coding-agents | S249, S260 | none |

### Unresolved ID/document mismatches

All 13 quarantine IDs are unsafe as direct package join keys: **eight IDs are absent** from both staged/current registry space (S151, S167, S168, S169, S172, S176, S180, S185); the other **five exist but name different documents**:

| ID | Quarantine document | Staged document at same ID | Base document at same ID |
|---|---|---|---|
| S236 | skills.sh/docs | agentskills.io/skill-creation/using-scripts.md | GitHub Copilot agent skills |
| S237 | skills.sh/audits | agentskills.io/skill-creation/quickstart.md | Cursor skills |
| S238 | Claude security.md | kimi-cli CHANGELOG.md | Amp skills |
| S239 | skills.sh/agent | IHBench arXiv:2607.25987 | Roo Code skills |
| S243 | skills.sh/docs/api | self-evolving skills arXiv:2608.02636 | Hermes skills |

The register's S185 document is currently held as S203/S239 and staged as S265; joining by the register's old numeric ID misses it. S167/S176 share a URL and have two staged candidates; S169 also has two candidates. URL remapping therefore still requires claim/anchor comparison, not arithmetic renumbering or choosing the first match. The exact-URL method deliberately does not treat `skills.sh/docs` as matching `skills.sh/docs/api`.

## Disposition and remaining unknowns

**Recommend no adoption while these mismatches remain unresolved.** Do not execute the package's append/copy checklist as-is. Keep the 7 payload-absent records refused as quotations and 6 never-checked records unverified pending independently reopened, claim-level evidence. This seat did not freshly test remote availability or quote truth; historical HTTP statuses are not today's evidence. The register records old campaign IDs while staging renumbers source rows, and current registry IDs have their own independent meanings. Adopting anything requires explicit `(document URL, claim/anchor, provenance)` mapping, current openings, and collision-free lane allocation with every citation updated by the integrator. No source or package writes were performed, and no adoption was attempted.

## Evidence pins and execution scope

| Input | SHA256 |
|---|---|
| Base registry blob | `d6b172065f86d08f713c5ec18cecc7970a225088a5f1b97c3c5b140bada8d656` |
| Working registry captured bytes | `c48d3340ad833b2df752d878157cf8cbe5d31b3acc3f0a06dbdd1b8fdf78a5af` |
| Staged append | `e2bdff3fe7b1a44bc764f180c6bda2ba73e9c625bbe9dd28eec3d9cef7090aaf` |
| Full canonical quarantine register | `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833` |

Captured UTC: `2026-10-30T14:39:31.218227+00:00`. Python eval extraction completed without exception; the only git command exited 0 and its exact argv is in the evidence JSON. Initial directory guesses at lane/fleet `merge` returned missing; source search resolved the actual read-only package under shokuknow. An initial shell directory listing used a final echo status, so it is **not** treated as command-owned evidence. No checks or C1/C2 after-values are claimed. No tools installed/updated, no heavy work, no scratch or background processes created; disk guard was unnecessary for bounded in-memory text analysis. Remaining unknown: current remote quote validity and authoritative historical per-claim renumber map.

VERDICT: NO ADOPTION — 48 staged/registry collisions; 13 quarantine records freshly derived; document/ID mismatches unresolved.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82R08Merge.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R08Merge-evidence.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R08Merge-registry-ids.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R08Merge-staged-ids.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R08Merge-collisions.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R08Merge-quarantine-full.txt
