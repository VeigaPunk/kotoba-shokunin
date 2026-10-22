# FrSourceDefects — what exactly is defective in SOURCES S001 / S003 / S010 / S013

Seat `KotobaR48.FrSourceDefects`, leaf, read-only. Lane tip read: `75f671b109d8eddd0d64c1429bd6379fe577175a`
(`git rev-parse HEAD`). Row line numbers at that tip: S001 `corpus/SOURCES.md:14`, S003 `:16`, S010 `:23`,
S013 `:26` (15 rows total). Defect routing read: `corpus/lessons/round-47-verifier-spotcheck.md:52` ("S001/S003/S010
defects, S013's versioned client semantics and unreviewed source claims remain routed rather than silently
corrected"), `:71` ("Supersede invalid source anchors/teaches in new registry rows, preserve old cells/history");
fleet `.ufo/waves/hyaku/parent-closures/kotoba47/{evidence.json,closure-entry.json}`; the advisory
`/fast/scratch/hyaku-resume-s3/kotoba47-full-review.md` §4 (S003 D2 confirmed against the live open spec). Every
source below was re-opened by me this session; contract = fleet `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` rules 1–2.

## S001 — defective cell: `anchor`

- **Defect.** `anchor` reads "§ Skill metadata table, § Progressive disclosure; live page opened 2026-10-19". No such
  heading exists: `grep -c -i 'skill metadata' specification.md` → `0` (exit 1). The live sections are
  `## SKILL.md format` (md:22) → `### Frontmatter` (md:26) → `#### description field` (md:97), and
  `## Progressive disclosure` (md:229). The embedded "opened 2026-10-19" is also stale after the round-47 re-open,
  and the page carries no version/release identifier, so `anchor`'s "plus revision" requirement needs a byte token.
- **Corrected anchor** (for a superseding row): `§ SKILL.md format › Frontmatter field table (md:31) and the
  \`description\` field bullets (md:99-101); § Progressive disclosure ("under 500 lines", md:237); revision =
  specification.md sha256 9a67de89… (7,608 B), fetched 2026-10-22T08:13:32Z`.
- **Re-opened quote (15 words), § Progressive disclosure, md:237:** "Keep your main `SKILL.md` under 500 lines.
  Move detailed reference material to separate files."
- Secondary (optional, same row): `teaches` says "matching its directory" where md:63 says the parent directory, and
  the page states no character/tag rule for `description` — md:31 "Max 1024 characters. Non-empty. Describes what the
  skill does and when to use it." The round-47 lesson records only the anchor defect, so anchor is the routed cell.

## S003 — defective cell: `teaches` (closing clause)

- **Defect.** `teaches` ends "…body under 500 lines; an Anthropic-only rule the open spec lacks". The open spec **does**
  carry the 500-line rule; only the XML-tag ban and the third-person rule are Anthropic-only. The clause's position
  after "body under 500 lines" reads as denying the spec a rule it has (the row's own wave-1 seat logged this as D2,
  `.ufo/waves/round-47/build/SrcS003.md`; the advisory review re-confirmed it against the live spec).
- **Corrected teaches** (superseding row): "The `description` cannot contain XML tags and must be third person —
  Anthropic-only rules the open spec's `description` bullets carry neither — and states what the skill does and when;
  the body under 500 lines, which the open spec states too."
- **Re-opened quotes:** "Cannot contain XML tags" (`best-practices.md:162`, `description` bullet; `:155` is the `name`
  bullet) and "Keep the `SKILL.md` body under 500 lines for optimal performance." (`best-practices.md:257`), against
  the spec's "Keep your main `SKILL.md` under 500 lines." (`specification.md:237`).
- **Freshness note for the writing seat:** the Anthropic `.md` drifted since round 47 — 42,028 B sha256 `727f3fa1…`
  (2026-10-21) → 42,169 B sha256 `f0a5d61b…` (2026-10-22T08:13:33Z), 1,191 lines; every cited rule line is unchanged
  (155/161/162/206/257/1133/1134/1140/1150). The new Gate entry must carry today's hash, not round-47's.

## S010 — defective cells: `anchor` (measured values) and `teaches` (second clause)

- **Defect.** `anchor` records "--self-test exit 0 and --json exit 1 (9 PASS / 1 FAIL governance.citation_resolves at
  LOG.md:2111) … Final line \"0 failure(s) over 1597 assertions\"". At the lane tip those numbers are stale: the
  self-test final line is "0 failure(s) over 1845 assertions" and `--json` is **exit 0, 11 PASS / 0 FAIL** (the
  LOG.md:2111 red is excused by the C3 erratum). `teaches` says "the frontmatter check is a lenient structural parse
  with no XML-tag rule" — false since round-47 C2 landed `trigger.no_xml_tag`
  (`verifiers/verify_skill_checklist.py:97, :310, :1294`). `recheck` is `on-commit` and the instrument's commit
  changed in that very landing, so the row is stale by its own cadence.
- **Corrected anchor** (superseding row): "verifiers/verify_skill_checklist.py — `--self-test` exit 0, final line
  \"0 failure(s) over 1845 assertions\"; `--json` exit 0, 11 PASS / 0 FAIL, \"41 boxes mapped (8 executed, 0
  delegated, 33 unexecuted)\"; run 2026-10-22 at lane tip 75f671b".
- **Corrected teaches:** "All 41 prose boxes are accounted for as executed, delegated, or unexecuted under a
  sha256-pinned normalization; the frontmatter check is a lenient structural parse whose `trigger.no_xml_tag` rule is
  lexical over the parsed `name`/`description` — it misses the YAML-alias, escaped-scalar and non-ASCII-tag cases the
  vendor packager refuses."
- **Re-opened quote (own-work row, command output):** `0 failure(s) over 1845 assertions` (self-test final line, exit 0).

## S013 — defective cells: `anchor`, `teaches` (and the `scope` label)

- **Defect (a), anchor grounds 1 of 3 facts.** The anchor names "§ How ChatGPT and Codex use skills" (md:91), but the
  budget and description-shortening sentences sit in the page intro at md:37-40, 53 lines earlier; only the
  implicit-invocation clause lives in the named section (md:98-99).
- **Defect (b), the revision token is a CDN stamp, not content identity.** The row pins "page Last-Modified
  2026-10-21T15:05:00Z"; today the HTML already reports ETag `W/"05515a538c5ed12b2b141913bbefb301"` and Last-Modified
  `2026-10-22T04:05:41Z` while the markdown bytes are unchanged (sha256 `ed6e324f…`, 11,035 B, 232 lines). The
  round-47 seat's own record said the sha256 is the durable identity.
- **Defect (c), versioned client semantics stated as flat facts.** The source attributes per clause: "In Codex, the
  initial list also includes each skill's file path. By default, this list uses at most 2% of the model's context
  window, or 8,000 characters when the context window is unknown." and "Implicit invocation: ChatGPT or Codex can
  choose a skill when your task matches the skill `description`." The row says "Codex … gates implicit invocation on
  the description" (under-scopes a rule stated for both clients), drops "By default" and the override
  ("Use `skills.max_context_tokens` to set a different budget, up to 10,000 tokens.", md:43-44), collapses the
  two-branch rule (8,000 characters is the unknown-window fallback), and mixes characters with tokens.
- **Corrected anchor** (superseding row): `page intro md:37-40 (budget + shortening + "may omit some skills"); md:43-44
  override; § How ChatGPT and Codex use skills md:91, implicit-invocation bullet md:98-99, \`allow_implicit_invocation\`
  md:218 (default true); revision = build-skills.md sha256 ed6e324f… (11,035 B, 232 lines), fetched 2026-10-22T08:13:33Z`.
- **Corrected teaches:** "supersedes S013 — As documented for the ChatGPT/Codex clients (vendor documentation, not a
  measurement of omp or opencode): by default Codex's initial skill list uses at most 2% of the model's context window,
  or 8,000 characters when the window is unknown, may omit skills for large sets, and shortens descriptions first; the
  budget is overridable via `skills.max_context_tokens` (up to 10,000 tokens); implicit invocation is stated for
  ChatGPT or Codex and is gated on the `description`."
- **Re-opened quotes:** "By default, this list uses at most 2% of the model's context window, or 8,000 characters when
  the context window is unknown." (22 words, md:37-39) and "Implicit invocation: ChatGPT or Codex can choose a skill
  when your task matches the skill `description`." (16 words, md:98-99).

## Consequence and non-defects

- Contract rule 2 forbids in-place `teaches`/`anchor` edits: each correction is a **new row whose `teaches` opens
  `supersedes S0NN —`**, old cells preserved. The wrong S013 quote location is repeated in
  `corpus/lessons/round-47.md:36`; lessons are append-only, so the round-48 `## Gate` line must carry the corrected
  location and today's hash.
- Cells that are **not** defective and must be preserved: S001 `teaches` (holds; see secondary note), S003's
  description/third-person/what-and-when clauses, S010's "41 prose boxes accounted for" claim (still 41 today), S013's
  three taught facts as claims about the documented clients.

## Evidence (commands, exit codes, hashes; all run 2026-10-22 UTC)

Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/FrSourceDefects/` (private clone of the lane at 75f671b named
`kotoba-shokunin`; the lane tree itself was never written).

| command | exit | key output |
|---|---|---|
| `curl -sSL --compressed -o spec001.md https://agentskills.io/specification.md` (08:13:32Z) | 0 | 7,608 B, sha256 `9a67de89…` (= round-47 fetch) |
| `curl … -o s003.md …/best-practices.md` (08:13:33Z) | 0 | 42,169 B, sha256 `f0a5d61b…` (round-47: `727f3fa1…`) |
| `curl … -o s013.md https://learn.chatgpt.com/docs/build-skills.md` (08:13:33Z) | 0 | 11,035 B, 232 lines, sha256 `ed6e324f…` (= round-47 fetch) |
| `curl -sSL … https://learn.chatgpt.com/docs/build-skills` (08:14:54Z) | 0 | 417,112 B, sha256 `d738d309…`, ETag `W/"05515a53…"`, Last-Modified 2026-10-22T04:05:41Z |
| `grep -c -i 'skill metadata' spec001.md` | 1 | `0` (anchor label absent) |
| `grep -nE '^#{1,4} ' spec001.md` | 0 | `## SKILL.md format` 22, `### Frontmatter` 26, `#### description field` 97, `## Progressive disclosure` 229 |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` (lane root, read-only, `-B`) | 0 | `0 failure(s) over 1845 assertions` |
| `python3 -B verifiers/verify_skill_checklist.py --json` (lane root) | 0 | `exit_code 0, pass 11, fail 0`; `checklist.box_map_complete` "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)"; `governance.citation_resolves` 872 tokens |
| `git -C <lane> status --porcelain` after the runs | 0 | unchanged pre-existing entries only (attempt-1 `M verifiers/verify_harness_independent.py`, `?? .ufo/waves/round-48/`, `?? plans/round-48.md`) |

Note: the same `--json` run inside a clone whose directory was not named `kotoba-shokunin` fails `trigger.name_directory`
and two `../.ufo/...` citation checks — layout artefacts, not lane state; the numbers above come from the lane root.

## Limits

- No fleet `sources-census.sh` run (census mechanics are the integrator's; the shape constraints are the contract's).
- S003's `.md` drift cause is not locatable: round-47 retained metadata only, and the `.md` endpoint has no archive.
- `.md` line numbers are representation-specific and move; section names are the durable locators.
- No tool installed or upgraded (nothing needed; `curl`, `sha256sum`, `python3` were present).
