ROW | tabi | master | e3cf4e0d30bb835532ff44b118c5ad52e09eb76d | SKILL.md | none | no | no | PROVINCE.md:3-4 | "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline."

# Census — tabi-shokunin (C1 adjacency, round 49)

Seat: KotobaR49.CensusTabi. Surface read-only: `/home/vgpnk/Projects/shokunin/tabi-shokunin`
+ `git show/ls-tree/rev-parse/log` only. No web sources fetched (none needed). No tool installs.

## Findings

1. **Pinned lane.** `rev-parse master` exit 0 → `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d`
   (`round-22: repair landing-stage oracle defects found by first positive run…`,
   2026-10-21 13:38:27 -0300). Checkout is **detached** (`symbolic-ref -q HEAD` exit 1,
   `branch --contains` shows `* (no branch)`); `master` and `hyaku/s3-tabi22-fresh-review`
   both point at the same commit, so the pinned bytes are master's bytes.
2. **Skill file.** Exactly one `SKILL.md`, at repo root (2441 lines, blob
   `7058140faa418d1de367e5aba177c8a0f5441760`, sha256
   `e39ff315e34a74e40427b16b19f59b95ba8aa46001295894135a46e4ce3c7c55`). No `skills/*/SKILL.md`.
3. **Frontmatter.** `name: tabi-shokunin`; `description: Domain specialist — browser &
   web-interaction craft. Rank: shonen (probation).` (SKILL.md:2-3). The description names
   **no sibling lane at all** — not kotoba, and no arbitration rule. Counts:
   `grep -c kotoba` on SKILL.md → **2**, on PROVINCE.md → **0** (exit 1), on AGENTS.md →
   **0** (exit 1). Both SKILL.md hits are the same watchdog-roster string
   (`LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`, SKILL.md:1313
   and :1450), carried under "Fleet-level, reported not absorbed" as evidence that *tabi* is
   absent from the roster. kotoba appears as a shell token in a roster, never as a province.
4. **PROVINCE.md** (21 lines, blob `c2222b16b3b18ce2c2058fb3a50d690c6e5735ae`, sha256
   `16c27b12a60dbbcc43903d40334c314f6587bd8703d1e890e076398eac1a946a`). Sections present:
   **Domain** (:3-4), **Owns (surfaces)** (:6-13), **Refuses** (:15-19), closing rule
   "`Out of province → report, never absorb.`" (:21). There is **no `Core` and no `Adjacent`
   section** in this file, so the sibling-arbitration form kotoba uses does not exist here.
   Refusal routes name three siblings — revenger/kaidoku (:15), kake (:16), kagi (:16-17) —
   **kotoba is not routed to, not named, and not mentioned**. So: description names kotoba =
   **no**; any arbitration clause (frontmatter or province) naming kotoba = **no**.
5. **Classification: `none`.** tabi owns browser/web-interaction craft — the kimi-webbridge
   plugin as substrate documentation, browser inventory, CDP session discipline, interaction
   records, dynamic-page evidence patterns (PROVINCE.md:6-13). It makes no claim on SKILL.md
   trigger/frontmatter craft, anatomy/compression, decision tables, the four fidelity
   checklists, agent-definition/always-on/dispatch-prompt craft, or instruments over those
   surfaces. Governing docs contain **zero** occurrences of `prompt`, `AGENTS.md`,
   `frontmatter`. Verified in the other direction too: tabi's own sibling-adjacency map
   `corpus/adjacency.tsv` dispositions 9 rows (kaidoku, revenger, kake, kagi, kumitate, kama;
   11 lines incl. header+comment) and contains **0** kotoba rows
   (`git show … | grep -c kotoba` → 0, exit 1).
6. **Nearest touchpoint (still not a claim).** The only `frontmatter` prose in the knowledge
   corpus is descriptive anatomy of the third-party plugin's loader: `corpus/knowledge/
   webbridge-plugin-anatomy.md:50-55` reads the substrate's `SKILL.md:2-4` `name`/`description`
   as *registration input*. That is substrate measurement, not authoring rules over kotoba's
   surface; tabi's own SKILL.md carries the token `SKILL.md` 36× (`git show … | grep -c
   'SKILL\.md'` → 36, exit 0), most resolving to the substrate plugin path as a pinned
   artifact (:64, :84, :211, :417, :580, :597-623, :677, :702-709, :751-754); the rest are
   self-pin rows for its own file (:830, :1197, :1328, :1339). It is not contested and,
   being a disjoint split (tabi measures one plugin's loader; kotoba owns frontmatter craft),
   not a shared boundary either — hence `none`, not `adjacent`.
7. **Census-relevant gap (other seats' scope, flagged only).** kotoba `PROVINCE.md` at HEAD
   `a5adc146a2995dcc5a95a6d8db6e5674f75191ac` has no `tabi` row (`grep -n tabi
   kotoba-shokunin/PROVINCE.md` exit 1) and its §Adjacent names 10 lanes (chousa, kumitate,
   kengaku, tameshi, kasegi, kotodama, mado, revenger, mori, kama) of the 20 siblings. This row
   supplies the tabi evidence the connector needs; I did not edit PROVINCE.md.
8. **Tabish tool worth knowing (not an instrument over kotoba's surface).**
   `scripts/check-adjacency.mjs` is tabi's own gate over *its* `corpus/adjacency.tsv`
   (surface/sibling_ref/sibling_quote 4..25 words/disposition; reads siblings read-only at
   pinned commits). It validates tabi's own adjacency claims; it asserts nothing about kotoba's
   province and owns no kotoba surface.

## Evidence (commands, exit codes)

Pin and tree — all in `/home/vgpnk/Projects/shokunin/tabi-shokunin`:
- `git rev-parse master` → `e3cf4e0d…76d`, exit 0.
- `git symbolic-ref -q HEAD` → empty, exit 1 (detached). `git rev-parse HEAD` → same 40-hex.
- `git for-each-ref --format='%(refname:short) %(objectname:short)' refs/heads` → `hyaku/s3-tabi22-fresh-review e3cf4e0`, `master e3cf4e0`.
- `git log -1 --format='%H %ci %s' e3cf4e0` → `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d 2026-10-21 13:38:27 -0300 round-22: repair landing-stage oracle defects found by first positive run; retain W2 cap-refusal chain`.
- `git ls-tree --name-only e3cf4e0` → `.gitignore .ufo AGENTS.md LOG.md MINT.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md corpus plans reports scripts`.
- `git ls-tree -r --name-only e3cf4e0 | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` → `SKILL.md`, exit 0 (count 1).
- `git show e3cf4e0:SKILL.md | wc -l` → 2441. `git show e3cf4e0:PROVINCE.md | wc -l` → 21.
- `git rev-parse e3cf4e0:SKILL.md e3cf4e0:PROVINCE.md` → `7058140f…1760`, `c2222b16…35ae`; `git show … | sha256sum` → `e39ff315…c55`, `16c27b12…46a`.

Mention counts at the pin:
- `git show e3cf4e0:SKILL.md | grep -c kotoba` → **2** (exit 0), lines 1313 and 1450.
- `git show e3cf4e0:PROVINCE.md | grep -c kotoba` → **0** (exit 1).
- `git show e3cf4e0:AGENTS.md | grep -c kotoba` → **0** (exit 1). AGENTS.md is 6 lines: LOG
  append rule, read-only substrates, secrets shape-only, lane identity on commits.
- `git show e3cf4e0:corpus/adjacency.tsv | grep -c kotoba` → **0** (exit 1).

`none` sweep (the required command, over the seven governing docs
`SKILL.md PROVINCE.md AGENTS.md README.md MINT.md SHONEN.md SCORECARD.md`):
`git -C … grep -EI 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' e3cf4e0 -- $FILES | wc -l`
→ **61** matches. Per pattern: `SKILL.md` 49 · `prompt` **0** · `AGENTS.md` **0** ·
`frontmatter` **0** · `trigger` 4 (all WebMCP call-lifecycle code spans, SKILL.md:2278-2325) ·
`description` 6 (frontmatter line 3; SQL `exception.description` :1955; `toolparamdescription`
:2112; DV-05 :2159; :2264) · `kotoba` 2 (the roster lines). Tree-wide the same regex gives
**11092** matches, all outside the governing docs: `.ufo` wave specs/receipts carry
`prompt` 1589, `corpus` 198 (dispatch/evidence receipts, incl. the substrate-anatomy note),
`scripts` 3 (`check-user-round-contract.mjs:541-546`, swarm item `prompt` field), `LOG.md` 2.
Zero of those state a rule over skill/prompt authoring for another lane.

Scope quote location (verbatim substring, fold after "real"):
`git show e3cf4e0:PROVINCE.md | tr '\n' ' ' | grep -c 'browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline.'`
→ 1, exit 0. Source line 3 is bolded `**Domain:**`; quote is PROVINCE.md:3-4.

Nearest-touchpoint quote (verbatim substring):
`git show e3cf4e0:corpus/knowledge/webbridge-plugin-anatomy.md | tr '\n' ' ' | grep -c "the loader scans that directory, finds \`kimi-webbridge/SKILL.md\`, and the skill's frontmatter \`name\`/\`description\` (SKILL.md:2-4) become the registration."`
→ 1, exit 0 (note :50-55).

Cross-check on kotoba's side (read-only): `grep -n tabi kotoba-shokunin/PROVINCE.md` → exit 1
(no tabi row at HEAD a5adc14). `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → 21
repos incl. kotoba, i.e. 20 siblings.

## Confidence

- Pin, skill path, frontmatter text, mention counts, PROVINCE sections: **observed** (commands above).
- Classification `none`: **high** — zero authoring-craft terms in the governing docs, description
  names no sibling, PROVINCE routes only to revenger/kaidoku, kake, kagi, and tabi's own
  adjacency map has no kotoba row.
- Remaining unknowns: none material. tabi's `corpus/adjacency.tsv` prose ruling text was not
  read line-by-line (only its sibling column and kotoba count), so a latent *mentions* kotoba
  in a quote column cannot exist (grep count 0), but a ruling that names kotoba indirectly
  is impossible by the same count.
