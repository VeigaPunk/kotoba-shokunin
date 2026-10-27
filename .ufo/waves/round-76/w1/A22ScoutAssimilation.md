# A22 — kotoba assimilation-register hand-check (round 76)

Verdict: 1 adoptable; 6 refuse as quote-absent in the fetched source; 6 unverifiable. These are hand-check results, not changes to the register. The register's `payload-absent` class was treated as a candidate, not accepted as proof.

## Reachable payload-absent rows

| Row | Cited source / hand-check | Verdict |
|---|---|---|
| S151 | `https://agentskills.io/skill-creation/optimizing-descriptions.md` fetched HTTP 200 (13,403 bytes). The page gives description-writing advice and eval procedure, but none of the quoted fragments is there: notably “metadata-only routing loses 37–44 points at ~80K skills” and the `CANNOT-ANSWER.md` / Qwen commentary. The correct scale-routing evidence is distinct material (SkillRouter, cited in staged S210), not this page. | **Refuse (fabrication-class quote absent).** |
| S167 | `https://agentskills.io/client-implementation/adding-skills-support.md` fetched HTTP 200 (20,446 bytes). It does contain a three-tier progressive-disclosure table, but not the quoted lane-editorial wording (“The lane holds this page as S002… Re-check: refetch…”). | **Refuse (fabrication-class quote absent).** |
| S168 | `https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` fetched HTTP 200 (899,785 bytes). The served article documents its eval results; the registered quote `section:` was not located in the fetched article text. | **Refuse (fabrication-class quote absent).** |
| S172 | `https://junie.jetbrains.com/docs/agent-skills.html` fetched HTTP 200 (38,509 bytes). The text explicitly says: “If a project-level and a user-level skills share the same name, the project-level skill takes precedence and the user-level skill is ignored.” | **Adoptable** for that documented Junie precedence claim. |
| S176 | `https://agentskills.io/client-implementation/adding-skills-support.md` fetched HTTP 200 (20,446 bytes). The page contains its progressive-disclosure table, but not the registered phrase “The three-tier progressive disclosure table and the two”; this is editorial summary, not source text. | **Refuse (fabrication-class quote absent).** |
| S180 | `https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja` fetched HTTP 200 (113,450 bytes; archived capture dated 2026-09-08). The page discusses installing Gemini API skills, but the exact registered phrase `スキルのインストール` was not found in the fetched payload. | **Refuse (fabrication-class quote absent).** |
| S185 | `https://docs.roocode.com/features/skills` fetched and served as Roo Code's current canonical documentation (`https://roocodeinc.github.io/Roo-Code/features/skills/`). It has a “Choose a location” section and describes skill locations, but the registered exact quote/heading `Skill locations` was not present in this currently served page. No historical snapshot was available to establish whether the wording differed when S185 was authored. | **Refuse as quote not located in current fetched source; historical wording remains unresolved.** |

## Unreachable kotoba rows: unverifiable, not fabrication

The register lists S169 (round 5), S236, S237, S238, S239 and S243 (round 10) in the kotoba unreachable section. Their cited URLs are respectively Gemini coding agents; `skills.sh/docs`; `skills.sh/audits`; Claude Code security docs; `skills.sh/agent`; and `skills.sh/docs/api`. **All six are unverifiable under the register's stated unreachable status; none is a fabrication verdict.** No kotoba S240–S242 rows appear in the register's unreachable list.

## Staged description-craft material vs round-76 opening

The staged merge package is read-only and says it was not written into the lane. Its `MERGE-REPORT.md` lists description-writing/trigger-testing knowledge and its `SOURCES.append.md` includes S204–S216 plus S231/S232 and S248/S252/S285. There **is** coverage beyond the round-76 opening's single S213 source:

- Staged `knowledge/corpus/knowledge/description-writing-and-trigger-testing.md` combines Anthropic skill-creator and Qwen guidance with SkillRouter and SkillsBench. It adds cross-source comparison and separates **trigger fidelity**, **large-registry routing**, and **post-load utility**; the specific SkillRouter scale finding (31–44 percentage-point drop) is not a claim in the S213 optimizing-descriptions guide.
- Staged `knowledge/corpus/knowledge/skill-craft-rules-from-chinese-vendors.md` (TRAE, CodeBuddy, Kimi) adds vendor-specific prescriptions and a freedom-of-guidance ladder, one-skill-one-task boundaries, and additional body/structure constraints.
- Staged `knowledge/corpus/knowledge/spec-description-trigger-discipline.md` cites S231, the same optimizing-descriptions URL as the in-round opening; its description-writing rules and eval query advice substantially overlap S213. It adds comparison with S232 and other sources, including the distinction between negative trigger scope and negative body directives.

Therefore: **yes**, staged description-craft material covers additional ground, principally the separately evidenced routing/utility axes and non-Anglophone vendor craft rules. The part based solely on S231 is not novel relative to the S213 opening. The staged materials are not themselves proof that their claims are acceptable; the individual source rows still require normal provenance review.

## Evidence and limits

Fetched source pages were read from the cited URLs on 2026-10-27; statuses and byte counts above are from the source fetches. The static reader returned ECONNREFUSED for the Wayback URL, but `curl` fetched the archive successfully and its payload was inspected. The in-round draft `.ufo/waves/round-76/build/quotes-s213.md` identifies the opening as the optimizing-descriptions page and records 13 located fragments; its reported digest is `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`. I did not run lane counters or modify any source/merge-tree content.
 
Exact fetch command used for the six source downloads:
`curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' --max-time 60 -o "$id.html" -w '%{http_code}' "$url"`; HTTP results: S151 200, S167 200, S168 200, S172 200, S185 200, S180 200. Response sizes: 13,403; 20,446; 899,785; 38,509; 71,129; 113,450 bytes respectively. The enclosing fetch loop exited 0. S180 archive content yielded no grep match for its quoted fragment.
Exact grep query used on fetched payloads: `metadata-only routing loses|The lane holds this page as S002|section:|If a project-level and a user-level skills share|スキルのインストール|Skill locations`; no matches were returned for those downloaded files. The later Junie source read independently located the quoted precedence sentence in live page text; grep over raw HTML did not match its encoded markup.